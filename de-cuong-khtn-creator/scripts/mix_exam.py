# -*- coding: utf-8 -*-
"""
mix_exam.py — Ghép đề, trộn đề, phân tích và lọc trùng câu hỏi LaTeX.

Commands:
  assemble  — Ghép câu hỏi từ nhiều nguồn vào template đề thi
  shuffle   — Trộn đề tạo mã đề mới (xáo trộn câu hỏi + phương án)
  parse     — Phân tích và thống kê câu hỏi
  dedup     — Lọc câu hỏi trùng lặp

Usage:
  python mix_exam.py <command> [args]
"""
import os
import re
import sys
import json
import random
import hashlib
import shutil
from difflib import SequenceMatcher

# Console Windows mặc định là cp1252/cp437 -> in tiếng Việt sẽ ném
# UnicodeEncodeError. Ép UTF-8 để chạy giống nhau trên Windows lẫn Linux.
for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass

# Fix console encoding on Windows
if sys.platform.startswith('win'):
    import io
    try:
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')
    except AttributeError:
        pass

# ==============================================================================
#                            CẤU TRÚC DỮ LIỆU CÂU HỎI
# ==============================================================================

class Question:
    def __init__(self, env_type, content, id6=None, source_path=None):
        self.env_type = env_type  # 'ex' or 'bt'
        self.content = content
        self.id6 = id6
        self.source_path = source_path
        self.question_type = self._determine_type()

    def _determine_type(self):
        if self.env_type == 'bt':
            return 'BT'
        if '\\choiceTF' in self.content:
            return 'TF'
        if '\\shortans' in self.content:
            return 'SA'
        if '\\choice' in self.content:
            return 'EX'
        return 'BT'

# ==============================================================================
#                            PARSER & LOADER
# ==============================================================================

def find_next_brace_content(text, start_pos=0):
    try:
        open_brace_index = text.find('{', start_pos)
        if open_brace_index == -1:
            return None, -1, -1
        balance = 1
        i = open_brace_index + 1
        while i < len(text):
            char = text[i]
            if char == '\\':
                if i + 1 < len(text):
                    i += 2
                    continue
                else:
                    return None, -1, -1
            if char == '%':
                newline_index = text.find('\n', i)
                if newline_index == -1:
                    return None, -1, -1
                i = newline_index + 1
                continue
            if char == '{':
                balance += 1
            elif char == '}':
                balance -= 1
            if balance == 0:
                content = text[open_brace_index + 1 : i]
                return content, open_brace_index, i + 1
            i += 1
        return None, -1, -1
    except Exception:
        return None, -1, -1


def parse_questions_from_text(text, source_path=None):
    pattern = re.compile(r'\\begin\{(ex|bt)\}(.*?)\\end\{\1\}', re.DOTALL)
    questions = []
    for match in pattern.finditer(text):
        env_type = match.group(1)
        raw_content = match.group(2)
        id6 = None
        id_match = re.search(r'%\[\s*([^\]\s]+)\s*\]', raw_content)
        if id_match:
            id6 = id_match.group(1)
            content = raw_content[:id_match.start()] + raw_content[id_match.end():]
        else:
            content = raw_content
        content = content.strip()
        q = Question(env_type, content, id6, source_path)
        questions.append(q)
    return questions


def load_questions_from_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        return parse_questions_from_text(content, os.path.abspath(filepath))
    except Exception as e:
        print(f"[ERROR] Lỗi khi đọc file {filepath}: {e}")
        return []


def load_questions_from_paths(paths):
    questions = []
    for path in paths:
        if not os.path.exists(path):
            print(f"[WARN] Đường dẫn không tồn tại: {path}")
            continue
        if os.path.isdir(path):
            for root, dirs, files in os.walk(path):
                for file in files:
                    if file.endswith('.tex'):
                        filepath = os.path.join(root, file)
                        questions.extend(load_questions_from_file(filepath))
        else:
            questions.extend(load_questions_from_file(path))
    return questions


# ==============================================================================
#                            QUESTION ASSET HANDLING
# ==============================================================================

IMAGE_EXTENSIONS = [".pdf", ".png", ".jpg", ".jpeg", ".webp", ".eps", ".tex"]


def _safe_path_part(value):
    value = os.path.splitext(os.path.basename(value or "inline"))[0]
    value = re.sub(r"[^A-Za-z0-9_.-]+", "_", value).strip("_.-")
    return value or "inline"


def _is_dynamic_latex_path(path_value):
    if not path_value:
        return True
    stripped = path_value.strip()
    if stripped.startswith(("http://", "https://")):
        return True
    return "\\" in stripped or "#" in stripped


def _candidate_paths(raw_path, source_dir):
    raw_path = raw_path.strip().strip('"').replace("/", os.sep)
    if not raw_path:
        return []

    bases = []
    if os.path.isabs(raw_path):
        bases.append(raw_path)
    else:
        if source_dir:
            bases.append(os.path.join(source_dir, raw_path))
        bases.append(os.path.abspath(raw_path))

    candidates = []
    for base in bases:
        candidates.append(base)
        root, ext = os.path.splitext(base)
        if not ext:
            candidates.extend(root + suffix for suffix in IMAGE_EXTENSIONS)
    return candidates


def _resolve_asset_path(raw_path, source_dir):
    if _is_dynamic_latex_path(raw_path):
        return None
    for candidate in _candidate_paths(raw_path, source_dir):
        if os.path.isfile(candidate):
            return os.path.abspath(candidate)
    return None


def _copy_asset_to_output(src_path, output_dir, bucket, copy_sidecars=False):
    src_path = os.path.abspath(src_path)
    try:
        rel_existing = os.path.relpath(src_path, output_dir)
        if not rel_existing.startswith("..") and not os.path.isabs(rel_existing):
            return rel_existing.replace("\\", "/")
    except ValueError:
        pass

    dest_dir = os.path.join(output_dir, "Images", "_assets", bucket)
    os.makedirs(dest_dir, exist_ok=True)

    dest_path = os.path.join(dest_dir, os.path.basename(src_path))
    shutil.copy2(src_path, dest_path)

    if copy_sidecars:
        src_dir = os.path.dirname(src_path)
        src_stem = os.path.splitext(os.path.basename(src_path))[0]
        for name in os.listdir(src_dir):
            name_stem, _ = os.path.splitext(name)
            sidecar = os.path.join(src_dir, name)
            if name_stem == src_stem and os.path.isfile(sidecar):
                shutil.copy2(sidecar, os.path.join(dest_dir, name))

    return os.path.relpath(dest_path, output_dir).replace("\\", "/")


def rewrite_question_asset_paths(question, output_file, question_index):
    output_dir = os.path.dirname(os.path.abspath(output_file))
    source_dir = os.path.dirname(question.source_path) if question.source_path else output_dir
    bucket = f"{_safe_path_part(question.source_path)}_q{question_index:03d}"
    content = question.content

    def replace_includegraphics(match):
        cmd_part = match.group(1)
        raw_path = match.group(2).strip()
        resolved = _resolve_asset_path(raw_path, source_dir)
        if not resolved:
            print(f"[WARN] Không tìm thấy ảnh cho câu {question_index}: {raw_path}")
            return match.group(0)
        new_path = _copy_asset_to_output(resolved, output_dir, bucket)
        return f"{cmd_part}{{{new_path}}}"

    content = re.sub(
        r"(\\includegraphics(?:\[[^\]]*\])?)\{([^}]+)\}",
        replace_includegraphics,
        content,
    )

    def replace_input(match):
        raw_path = match.group(1).strip()
        if raw_path.startswith(("Ans/", "Ansbook/", "Khaibao/")):
            return match.group(0)
        resolved = _resolve_asset_path(raw_path, source_dir)
        if not resolved:
            return match.group(0)
        new_path = _copy_asset_to_output(resolved, output_dir, bucket, copy_sidecars=True)
        return f"\\input{{{new_path}}}"

    content = re.sub(r"\\input\{([^}]+)\}", replace_input, content)
    question.content = content


def rewrite_assets_for_questions(questions, output_file):
    for idx, question in enumerate(questions, 1):
        rewrite_question_asset_paths(question, output_file, idx)

# ==============================================================================
#                            METADATA PARSER
# ==============================================================================

def parse_metadata_from_tex(tex_content):
    metadata = {}
    for field in ['monhoc', 'ngaykt', 'nh', 'thoigian', 'made']:
        match = re.search(r'\\gdef\\' + field + r'\{([^\}]*)\}', tex_content)
        if match:
            metadata[field] = match.group(1)
    match_sec = re.search(r'\\section\[([^\]]*?)(?:\s*-\s*Mã đề[^\]]*)\]', tex_content)
    if match_sec:
        metadata['ten_de'] = match_sec.group(1).strip()
    else:
        match_sec2 = re.search(r'\\section(?:\[[^\]]*\])?\{([^\}]+)\}', tex_content)
        if match_sec2:
            metadata['ten_de'] = match_sec2.group(1).strip()
    return metadata


def get_tenfile_and_made(output_path, default_made=None):
    filename = os.path.basename(output_path)
    if filename.endswith(".tex"):
        filename = filename[:-4]
    match = re.search(r'_MADE(\d+)$', filename, re.IGNORECASE)
    if match:
        made = match.group(1)
        ten_file = filename[:match.start()]
    else:
        match2 = re.search(r'MADE(\d+)$', filename, re.IGNORECASE)
        if match2:
            made = match2.group(1)
            ten_file = filename[:match2.start()]
        else:
            made = default_made if default_made else f"{random.randint(100, 999)}"
            ten_file = filename
    return ten_file, made

# ==============================================================================
#                            TEMPLATING / ASSEMBLY
# ==============================================================================

def format_question_list(questions, prefix):
    formatted = []
    for idx, q in enumerate(questions, 1):
        header = f"%%%%%============{prefix}_{idx}================%%%%%%"
        env = q.env_type
        if q.id6:
            begin_line = f"\\begin{{{env}}}%[{q.id6}]"
        else:
            begin_line = f"\\begin{{{env}}}"
        formatted.append(f"{header}\n{begin_line}\n{q.content}\n\\end{{{env}}}")
    return "\n\n".join(formatted)


def build_exam_string(questions, ten_file, made, metadata):
    ex_questions = [q for q in questions if q.question_type == 'EX']
    tf_questions = [q for q in questions if q.question_type == 'TF']
    sa_questions = [q for q in questions if q.question_type == 'SA']
    bt_questions = [q for q in questions if q.question_type == 'BT']

    ex_content = format_question_list(ex_questions, "EX")
    tf_content = format_question_list(tf_questions, "TF")
    sa_content = format_question_list(sa_questions, "SA")
    bt_content = format_question_list(bt_questions, "BT")

    lines = []
    lines.append("\\documentclass[FileMain.tex]{subfiles}")
    lines.append(f"\\gdef\\monhoc{{{metadata.get('monhoc', '<Tên môn học>')}}}")
    lines.append(f"\\gdef\\ngaykt{{{metadata.get('ngaykt', '<Ngày thi>')}}}")
    lines.append(f"\\gdef\\nh{{{metadata.get('nh', '2025 - 2026')}}}")
    lines.append(f"\\gdef\\thoigian{{{metadata.get('thoigian', '45')}}}")
    lines.append(f"\\gdef\\made{{{made}}}")
    lines.append("\\begin{document}")

    ten_ki_thi = metadata.get('ten_de', '<Tên kì thi>')
    lines.append(f"\\section[{ten_ki_thi} - Mã đề \\made]{{{ten_ki_thi}}}")
    lines.append("")

    if ex_questions:
        lines.append("%%%==============Phần trắc nghiệm nhiều lựa chọn==============%%%")
        lines.append(f"\\subsection{{Bài tập trắc nghiệm nhiều lựa chọn}}\\textit{{\\large Thí sinh trả lời từ câu 1 đến câu {len(ex_questions)}. Mỗi câu thí sinh chỉ chọn một phương án}}")
        lines.append(f"\\Opensolutionfile{{ansex}}[Ans/LGEX-{ten_file}_MADE{made}]")
        lines.append(f"\\Opensolutionfile{{ans}}[Ans/Ans-{ten_file}_MADE{made}]")
        lines.append(ex_content)
        lines.append("\\Closesolutionfile{ans}")
        lines.append("\\Closesolutionfile{ansex}")
        lines.append(f"%\\bangdapan{{Ans-{ten_file}_MADE{made}}}")

    if tf_questions:
        lines.append("%%%==============Phần trắc nghiệm đúng sai==============%%%")
        lines.append(f"\\subsection{{Trắc nghiệm đúng sai}}\\textit{{\\large Thí sinh trả lời từ câu 1 đến câu {len(tf_questions)}. Trong mỗi ý a), b), c), d) ở mỗi câu thí sinh chọn đúng hoặc sai}}")
        lines.append(f"\\Opensolutionfile{{ansex}}[Ans/LGTF-{ten_file}_MADE{made}]")
        lines.append(f"\\Opensolutionfile{{ansbook}}[Ansbook/AnsTF-{ten_file}_MADE{made}]")
        lines.append(f"\\Opensolutionfile{{ans}}[Ans/Tempt-{ten_file}_MADE{made}]")
        lines.append("\\setcounter{ex}{0}")
        lines.append(tf_content)
        lines.append("\\Closesolutionfile{ans}")
        lines.append("\\Closesolutionfile{ansbook}")
        lines.append("\\Closesolutionfile{ansex}")
        lines.append(f"%\\bangdapanTF{{AnsTF-{ten_file}_MADE{made}}}")

    if sa_questions:
        lines.append("%%%==============Phần bài tập trả lời ngắn==============%%%")
        lines.append(f"\\subsection{{Bài tập trả lời ngắn}}\\textit{{\\large Thí sinh trả lời từ câu 1 đến câu {len(sa_questions)}}}")
        lines.append(f"\\Opensolutionfile{{ansex}}[Ans/LGSA-{ten_file}_MADE{made}]")
        lines.append(f"\\Opensolutionfile{{ansexh}}[Ans/AnsSA-{ten_file}_MADE{made}]")
        lines.append("\\setcounter{ex}{0}")
        lines.append(sa_content)
        lines.append("\\Closesolutionfile{ansexh}")
        lines.append("\\Closesolutionfile{ansex}")
        lines.append(f"%\\bangdapanSA{{AnsSA-{ten_file}_MADE{made}}}")

    if bt_questions:
        lines.append("%%%==============Phần bài tập tự luận==============%%%")
        lines.append(f"\\subsection{{Bài tập tự luận}}\\textit{{\\large Thí sinh trả lời từ bài 1 đến bài {len(bt_questions)}}}")
        lines.append(f"\\Opensolutionfile{{ansbth}}[Ans/LGBT-{ten_file}_MADE{made}]")
        lines.append(f"\\Opensolutionfile{{ansbt}}[Ans/AnsBT-{ten_file}_MADE{made}]")
        lines.append(bt_content)
        lines.append("\\Closesolutionfile{ansbt}")
        lines.append("\\Closesolutionfile{ansbth}")

    lines.append("")
    lines.append("\\begin{center}")
    lines.append(" \\rule[4pt]{2cm}{1pt}\\,\\large\\bfseries Hết\\,\\rule[4pt]{2cm}{1pt}")
    lines.append("\\end{center}")
    lines.append("\\label{x}")
    lines.append("\\end{document}")

    return "\n".join(lines) + "\n"

# ==============================================================================
#                            SHUFFLER LOGIC
# ==============================================================================

def option_is_true(option_text):
    return bool(re.match(r'\s*\\True\b', option_text))


def get_choice_options(block_content, cmd):
    idx = block_content.find(cmd)
    if idx == -1:
        return None

    current_pos = idx + len(cmd)
    options = []
    positions = []
    for _ in range(4):
        option, start_brace, end_pos = find_next_brace_content(block_content, current_pos)
        if option is None:
            return None
        options.append(option)
        positions.append((start_brace, end_pos))
        current_pos = end_pos

    return idx, options, positions


def parse_itemchoice(lg_content):
    match = re.search(
        r'\\begin\{itemchoice\}\[([^\]]*)\](.*?)\\end\{itemchoice\}',
        lg_content,
        re.DOTALL,
    )
    if not match:
        return None

    items_content = match.group(2)
    item_matches = list(re.finditer(r'\\itemch\b', items_content))
    if len(item_matches) != 4:
        return None

    prefix = items_content[:item_matches[0].start()]
    explanations = []
    for idx, item_match in enumerate(item_matches):
        start = item_match.end()
        end = item_matches[idx + 1].start() if idx + 1 < len(item_matches) else len(items_content)
        explanations.append(items_content[start:end].strip())

    return {
        "match": match,
        "labels": [label.strip() for label in match.group(1).split(",")],
        "prefix": prefix,
        "explanations": explanations,
    }


def relabel_tf_explanation(text, old_idx, new_idx):
    old_letter = "abcd"[old_idx]
    new_letter = "abcd"[new_idx]
    if old_letter == new_letter:
        return text

    text = re.sub(rf'\b(ý|phương án)\s+{old_letter}\b', rf'\1 {new_letter}', text, flags=re.IGNORECASE)
    text = re.sub(
        rf'(^|[\s(\[]){old_letter}\)',
        rf'\1{new_letter})',
        text,
    )
    return text


def rebuild_tf_loigiai(lg_content, options, new_order):
    parsed = parse_itemchoice(lg_content)
    if not parsed:
        return None

    new_labels = []
    new_items = []
    for new_idx, old_idx in enumerate(new_order):
        new_labels.append(("T" if option_is_true(options[old_idx]) else "F") + str(new_idx + 1))
        explanation = parsed["explanations"][old_idx]
        new_items.append(relabel_tf_explanation(explanation, old_idx, new_idx))

    new_items_content = (
        parsed["prefix"]
        + "\n"
        + "\n".join(f"\t\t\\itemch {item}" for item in new_items)
        + "\n\t"
    )
    new_itemchoice = (
        f"\\begin{{itemchoice}}[{','.join(new_labels)}]"
        f"{new_items_content}\\end{{itemchoice}}"
    )
    match = parsed["match"]
    return lg_content[:match.start()] + new_itemchoice + lg_content[match.end():]


def shuffle_loigiai_content(lg_content, shuffle_map):
    parsed = parse_itemchoice(lg_content)
    if not parsed:
        return lg_content

    inv_map = {new: old for old, new in shuffle_map.items()}
    new_order = [inv_map[i] for i in range(4)]
    new_labels = []
    new_items = []
    for new_idx, old_idx in enumerate(new_order):
        new_items.append(parsed["explanations"][old_idx])
        old_label = parsed["labels"][old_idx] if old_idx < len(parsed["labels"]) else ""
        old_label_match = re.match(r'\s*([TF])', old_label, re.IGNORECASE)
        truth = old_label_match.group(1).upper() if old_label_match else "F"
        new_labels.append(truth + str(new_idx + 1))

    new_items_content = (
        parsed["prefix"]
        + "\n"
        + "\n".join(f"\t\t\\itemch {item}" for item in new_items)
        + "\n\t"
    )
    new_itemchoice = (
        f"\\begin{{itemchoice}}[{','.join(new_labels)}]"
        f"{new_items_content}\\end{{itemchoice}}"
    )
    match = parsed["match"]
    return lg_content[:match.start()] + new_itemchoice + lg_content[match.end():]


def shuffle_question_options(block_content, seed):
    if '\\choiceTF' in block_content:
        cmd = '\\choiceTF'
    elif '\\choice' in block_content:
        cmd = '\\choice'
    else:
        return block_content

    parsed_choice = get_choice_options(block_content, cmd)
    if not parsed_choice:
        return block_content

    idx, options, positions = parsed_choice
    first_start = positions[0][0]
    last_end = positions[-1][1]
    indices = [0, 1, 2, 3]

    rng = random.Random(seed)
    rng.shuffle(indices)

    shuffle_map = {old: new for new, old in enumerate(indices)}
    new_options = [options[i] for i in indices]
    new_choice_part = cmd + "\n" + "\n".join(f"\t{{{opt}}}" for opt in new_options)

    lg_idx = block_content.find('\\loigiai')
    if lg_idx != -1:
        lg_content, lg_s, lg_e = find_next_brace_content(block_content, lg_idx)
        if lg_content:
            if cmd == '\\choiceTF':
                shuffled_lg = rebuild_tf_loigiai(lg_content, options, indices)
                if shuffled_lg is None:
                    print("[WARN] Bỏ qua trộn phương án TF vì không tìm đủ 4 \\itemch trong \\loigiai.")
                    return block_content
            else:
                shuffled_lg = shuffle_loigiai_content(lg_content, shuffle_map)
            block_content = (
                block_content[:idx] +
                new_choice_part +
                block_content[last_end:lg_s] +
                "{" + shuffled_lg + "}" +
                block_content[lg_e:]
            )
            return block_content

    block_content = block_content[:idx] + new_choice_part + block_content[last_end:]
    return block_content


def shuffle_questions(questions, seed):
    ex_qs = [q for q in questions if q.question_type == 'EX']
    tf_qs = [q for q in questions if q.question_type == 'TF']
    sa_qs = [q for q in questions if q.question_type == 'SA']
    bt_qs = [q for q in questions if q.question_type == 'BT']

    rng = random.Random(seed)
    rng.shuffle(ex_qs)
    rng.shuffle(tf_qs)
    rng.shuffle(sa_qs)
    rng.shuffle(bt_qs)

    for i, q in enumerate(ex_qs):
        q.content = shuffle_question_options(q.content, seed + i)
    for i, q in enumerate(tf_qs):
        q.content = shuffle_question_options(q.content, seed + 1000 + i)

    return ex_qs + tf_qs + sa_qs + bt_qs

# ==============================================================================
#                            DEDUPLICATION
# ==============================================================================

def normalize_text_for_comparison(text):
    text = re.sub(r'%.*?\n', '\n', text)
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'%\[.*?\]', '', text)
    return text.strip().lower()


def calculate_similarity(text1, text2):
    norm1 = normalize_text_for_comparison(text1)
    norm2 = normalize_text_for_comparison(text2)
    return SequenceMatcher(None, norm1, norm2).ratio()


def get_text_hash(text):
    normalized = normalize_text_for_comparison(text)
    return hashlib.md5(normalized.encode('utf-8')).hexdigest()


def remove_duplicates(questions, threshold=0.85):
    unique_questions = []
    removed_count = 0
    seen_hashes = set()

    for q in questions:
        h = get_text_hash(q.content)
        if h in seen_hashes:
            removed_count += 1
            continue
        is_duplicate = False
        for uq in unique_questions:
            if q.question_type == uq.question_type:
                similarity = calculate_similarity(q.content, uq.content)
                if similarity >= threshold:
                    is_duplicate = True
                    removed_count += 1
                    break
        if not is_duplicate:
            unique_questions.append(q)
            seen_hashes.add(h)

    return unique_questions, removed_count

# ==============================================================================
#                            COMMAND HANDLERS
# ==============================================================================

def cmd_parse(args):
    import argparse
    parser = argparse.ArgumentParser(description="Phân tích câu hỏi LaTeX và hiển thị thống kê.")
    parser.add_argument("path", help="Đường dẫn file hoặc thư mục")
    parsed = parser.parse_args(args)

    questions = load_questions_from_paths([parsed.path])
    if not questions:
        print(f"Không tìm thấy câu hỏi nào tại: {parsed.path}")
        return

    stats = {
        'total': len(questions),
        'EX': sum(1 for q in questions if q.question_type == 'EX'),
        'TF': sum(1 for q in questions if q.question_type == 'TF'),
        'SA': sum(1 for q in questions if q.question_type == 'SA'),
        'BT': sum(1 for q in questions if q.question_type == 'BT'),
    }

    print("=== THỐNG KÊ NGÂN HÀNG CÂU HỎI ===")
    print(f"Tổng số câu: {stats['total']}")
    print(f"Trắc nghiệm nhiều lựa chọn (EX): {stats['EX']}")
    print(f"Trắc nghiệm đúng sai (TF): {stats['TF']}")
    print(f"Trả lời ngắn (SA): {stats['SA']}")
    print(f"Tự luận (BT): {stats['BT']}")


def cmd_dedup(args):
    import argparse
    parser = argparse.ArgumentParser(description="Lọc câu hỏi trùng lặp.")
    parser.add_argument("input_path", help="Đường dẫn file/thư mục nguồn")
    parser.add_argument("output_file", help="Đường dẫn file lưu kết quả")
    parser.add_argument("--threshold", type=float, default=0.85, help="Ngưỡng tương đồng (0.0-1.0)")
    parsed = parser.parse_args(args)

    questions = load_questions_from_paths([parsed.input_path])
    if not questions:
        print("Không tìm thấy câu hỏi nào.")
        return

    initial_count = len(questions)
    print(f"Nạp {initial_count} câu hỏi. Đang lọc trùng...")

    unique_qs, removed = remove_duplicates(questions, parsed.threshold)

    print(f"Đã loại bỏ {removed} câu trùng. Còn lại: {len(unique_qs)} câu.")

    os.makedirs(os.path.dirname(os.path.abspath(parsed.output_file)), exist_ok=True)
    with open(parsed.output_file, 'w', encoding='utf-8') as f:
        for idx, q in enumerate(unique_qs, 1):
            f.write(f"%%%============={q.question_type}_{idx}=============%%%\n")
            if q.id6:
                f.write(f"\\begin{{{q.env_type}}}%[{q.id6}]\n")
            else:
                f.write(f"\\begin{{{q.env_type}}}\n")
            f.write(q.content)
            f.write(f"\n\\end{{{q.env_type}}}\n\n")

    print(f"Lưu kết quả: {parsed.output_file}")


def cmd_shuffle(args):
    import argparse
    parser = argparse.ArgumentParser(description="Trộn câu hỏi và phương án để sinh mã đề mới.")
    parser.add_argument("source", help="File LaTeX đề thi gốc")
    parser.add_argument("--seed", type=int, default=42, help="Seed xáo trộn")
    parser.add_argument("--made2", type=str, default=None, help="Mã đề mới (3 chữ số)")
    parser.add_argument("--out-name", type=str, default=None, help="Đường dẫn file output")
    parsed = parser.parse_args(args)

    if not os.path.exists(parsed.source):
        print(f"Lỗi: File nguồn không tồn tại: {parsed.source}")
        sys.exit(1)

    with open(parsed.source, 'r', encoding='utf-8') as f:
        src_content = f.read()

    questions = parse_questions_from_text(src_content, os.path.abspath(parsed.source))
    metadata = parse_metadata_from_tex(src_content)

    made2 = parsed.made2
    if made2 is None:
        old_made = metadata.get('made', '101')
        try:
            made2 = f"{int(old_made) + 1:03d}"
        except Exception:
            made2 = f"{random.randint(100, 999)}"

    shuffled_qs = shuffle_questions(questions, parsed.seed)

    if parsed.out_name:
        out_path = parsed.out_name
        if not out_path.endswith('.tex'):
            out_path += '.tex'
    else:
        source_dir = os.path.dirname(os.path.abspath(parsed.source))
        source_base = os.path.basename(parsed.source)
        if source_base.endswith('.tex'):
            source_base = source_base[:-4]
        match = re.search(r'(_?)MADE(\d+)', source_base, re.IGNORECASE)
        if match:
            new_base = source_base[:match.start()] + match.group(1) + "MADE" + made2
        else:
            new_base = source_base + "_MADE" + made2
        out_path = os.path.join(source_dir, new_base + ".tex")

    ten_file, _ = get_tenfile_and_made(out_path, made2)
    rewrite_assets_for_questions(shuffled_qs, out_path)
    assembled_content = build_exam_string(shuffled_qs, ten_file, made2, metadata)

    os.makedirs(os.path.dirname(os.path.abspath(out_path)), exist_ok=True)
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(assembled_content)

    print(f"Trộn đề thành công -> {out_path}")


def cmd_assemble(args):
    import argparse
    parser = argparse.ArgumentParser(description="Ghép câu hỏi LaTeX vào mẫu đề thi.")
    parser.add_argument("--input", nargs="+", help="Các file/thư mục chứa câu hỏi")
    parser.add_argument("--output", help="Đường dẫn file đề thi đầu ra")
    parser.add_argument("--monhoc", default=None, help="Tên môn học")
    parser.add_argument("--ngaykt", default=None, help="Ngày thi")
    parser.add_argument("--nh", default=None, help="Năm học")
    parser.add_argument("--thoigian", default=None, help="Thời gian (phút)")
    parser.add_argument("--made", default=None, help="Mã đề thi")
    parser.add_argument("--ten-de", default=None, help="Tên kì thi")
    parser.add_argument("--config", help="File JSON cấu hình")
    parsed = parser.parse_args(args)

    cfg = {}
    if parsed.config:
        if os.path.exists(parsed.config):
            with open(parsed.config, 'r', encoding='utf-8-sig') as f:
                cfg = json.load(f)
        else:
            print(f"Lỗi: Không tìm thấy config: {parsed.config}")
            sys.exit(1)

    inputs = parsed.input if parsed.input else cfg.get("input", [])
    if not inputs and "parts" in cfg:
        inputs = [p for p in cfg["parts"].values() if p]
    if isinstance(inputs, str):
        inputs = [inputs]

    default_output = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "latex-output", "assembled_exam.tex"))
    output = parsed.output if parsed.output else cfg.get("output", default_output)
    monhoc = parsed.monhoc if parsed.monhoc else cfg.get("monhoc", "<Tên môn học>")
    ngaykt = parsed.ngaykt if parsed.ngaykt else cfg.get("ngaykt", "<Ngày thi>")
    nh = parsed.nh if parsed.nh else cfg.get("nh", "2025 - 2026")
    thoigian = parsed.thoigian if parsed.thoigian else cfg.get("thoigian", "45")
    made = parsed.made if parsed.made else cfg.get("made", None)
    ten_de = parsed.ten_de if parsed.ten_de else cfg.get("ten_de", "Kiểm tra")

    if not inputs:
        print("Lỗi: Không chỉ định file đầu vào (dùng --input hoặc --config).")
        sys.exit(1)

    questions = load_questions_from_paths(inputs)
    if not questions:
        print("Lỗi: Không phân tích được câu hỏi nào.")
        sys.exit(1)

    ten_file, computed_made = get_tenfile_and_made(output, made)
    metadata = {
        'monhoc': monhoc, 'ngaykt': ngaykt, 'nh': nh,
        'thoigian': thoigian, 'ten_de': ten_de
    }

    rewrite_assets_for_questions(questions, output)
    assembled_content = build_exam_string(questions, ten_file, computed_made, metadata)

    os.makedirs(os.path.dirname(os.path.abspath(output)), exist_ok=True)
    with open(output, 'w', encoding='utf-8') as f:
        f.write(assembled_content)

    print(f"Ghép đề thành công -> {output}")

# ==============================================================================
#                            ENTRY POINT
# ==============================================================================

COMMANDS = {
    "assemble": cmd_assemble,
    "shuffle": cmd_shuffle,
    "parse": cmd_parse,
    "dedup": cmd_dedup,
}

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python mix_exam.py <command> [args]")
        print("Commands:", ", ".join(COMMANDS.keys()))
        sys.exit(1)

    cmd = sys.argv[1]
    if cmd in COMMANDS:
        COMMANDS[cmd](sys.argv[2:])
    else:
        print(f"Lỗi: Lệnh không hợp lệ: {cmd}")
        print("Commands:", ", ".join(COMMANDS.keys()))
        sys.exit(1)
