# -*- coding: utf-8 -*-
import os
import re
import sys
import json
import random
import subprocess
import hashlib
from difflib import SequenceMatcher

# Fix console encoding on Windows to prevent UnicodeEncodeError
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
    def __init__(self, env_type, content, id6=None):
        self.env_type = env_type  # 'ex' or 'bt'
        self.content = content    # raw inner content of the environment
        self.id6 = id6            # e.g., "0H1VD3-3"
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
#                            PARSER & LOADER CÂU HỎI
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

def parse_questions_from_text(text):
    # Pattern to find all \begin{ex}...\end{ex} or \begin{bt}...\end{bt}
    pattern = re.compile(r'\\begin\{(ex|bt)\}(.*?)\\end\{\1\}', re.DOTALL)
    questions = []
    for match in pattern.finditer(text):
        env_type = match.group(1)
        raw_content = match.group(2)
        
        # Extract the ID6 if present in a comment
        id6 = None
        id_match = re.search(r'%\[\s*([^\]\s]+)\s*\]', raw_content)
        if id_match:
            id6 = id_match.group(1)
            # Remove the ID6 comment from raw_content
            content = raw_content[:id_match.start()] + raw_content[id_match.end():]
        else:
            content = raw_content
            
        content = content.strip()
        q = Question(env_type, content, id6)
        questions.append(q)
    return questions

def load_questions_from_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        return parse_questions_from_text(content)
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
#                            METADATA PARSER
# ==============================================================================

def parse_metadata_from_tex(tex_content):
    metadata = {}
    for field in ['monhoc', 'ngaykt', 'nh', 'thoigian', 'made']:
        match = re.search(r'\\gdef\\' + field + r'\{([^\}]*)\}', tex_content)
        if match:
            metadata[field] = match.group(1)
    
    # Find section title
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
    
    # Check if ends with _MADE\d+ or MADE\d+
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
    
    # 1. EX Subsection
    if ex_questions:
        lines.append("%%%==============Phần trắc nghiệm nhiều lựa chọn==============%%%")
        lines.append(f"\\subsection{{Bài tập trắc nghiệm nhiều lựa chọn}}\\textit{{\\large Thí sinh trả lời từ câu 1 đến câu {len(ex_questions)}. Mỗi câu thí sinh chỉ chọn một phương án}}")
        lines.append(f"\\Opensolutionfile{{ansex}}[Ans/LGEX-{ten_file}_MADE{made}]")
        lines.append(f"\\Opensolutionfile{{ans}}[Ans/Ans-{ten_file}_MADE{made}]")
        lines.append(ex_content)
        lines.append("\\Closesolutionfile{ans}")
        lines.append("\\Closesolutionfile{ansex}")
        lines.append(f"%\\bangdapan{{Ans-{ten_file}_MADE{made}}}")
        
    # 2. TF Subsection
    if tf_questions:
        lines.append("%%%==============Phần trắc nghiệm đúng sai==============%%%")
        lines.append(f"\\subsection{{Trắc nghiệm đúng sai}}\\textit{{\\large Thí sinh trả lời từ câu 1 đến câu {len(tf_questions)}. Trong mỗi ý a), b), c), d) ở mỗi câu thí sinh chọn đúng hoặc sai}}")
        lines.append(f"\\Opensolutionfile{{ansex}}[Ans/LGTF-{ten_file}_MADE{made}]")
        lines.append(f"\\Opensolutionfile{{ansbook}}[Ansbook/AnsTF-{ten_file}_MADE{made}]")
        lines.append("\\setcounter{ex}{0}")
        lines.append(tf_content)
        lines.append("\\Closesolutionfile{ansbook}")
        lines.append("\\Closesolutionfile{ansex}")
        lines.append(f"%\\bangdapanTF{{AnsTF-{ten_file}_MADE{made}}}")
        
    # 3. SA Subsection
    if sa_questions:
        lines.append("%%%==============Phần bài tập trả lời ngắn==============%%%")
        lines.append(f"\\subsection{{Bài tập trả lời ngắn}}\\textit{{\\large Thí sinh trả lời từ câu 1 đến câu {len(sa_questions)}}}")
        lines.append(f"\\Opensolutionfile{{ansex}}[Ans/LGSA-{ten_file}_MADE{made}]")
        lines.append(f"\\Opensolutionfile{{ansexh}}[Ans/AnsSA-{ten_file}_MADE{made}]")
        lines.append("\\setcounter{ex}{0}")
        lines.append(sa_content)
        lines.append("\\Closesolutionfile{ansexh}")
        lines.append("\\Closesolutionfile{ansex}")
        
    # 4. BT Subsection
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

def shuffle_loigiai_content(lg_content, shuffle_map):
    # Match \begin{itemchoice}[...] ... \end{itemchoice}
    match = re.search(r'\\begin\{itemchoice\}\[([^\]]*)\](.*?)\\end\{itemchoice\}', lg_content, re.DOTALL)
    if match:
        labels_str = match.group(1)
        items_content = match.group(2)
        
        labels = [lbl.strip() for lbl in labels_str.split(',')]
        parts = re.split(r'\\itemch\b', items_content)
        
        if len(parts) >= 5 and len(labels) == 4:
            explanations = [part.strip() for part in parts[1:5]]
            inv_map = {new: old for old, new in shuffle_map.items()}
            
            new_explanations = [explanations[inv_map[i]] for i in range(4)]
            new_labels = []
            for i in range(4):
                old_idx = inv_map[i]
                old_lbl = labels[old_idx]
                new_lbl = old_lbl[0] + str(i + 1)
                new_labels.append(new_lbl)
                
            new_items_content = parts[0] + "\n" + "\n".join(f"\t\t\\itemch {exp}" for exp in new_explanations) + "\n\t"
            new_labels_str = ",".join(new_labels)
            
            new_itemchoice = f"\\begin{{itemchoice}}[{new_labels_str}]{new_items_content}\\end{{itemchoice}}"
            lg_content = lg_content[:match.start()] + new_itemchoice + lg_content[match.end():]

    old_labels = ['A', 'B', 'C', 'D']
    old_labels_lower = ['a', 'b', 'c', 'd']
    
    temp_map = {}
    for old_idx, new_idx in shuffle_map.items():
        if old_idx != new_idx:
            temp_map[old_labels[old_idx]] = f"__TEMP_LBL_{old_labels[new_idx]}__"
            temp_map[old_labels_lower[old_idx]] = f"__TEMP_LBL_{old_labels_lower[new_idx]}__"
            
    for old, temp in temp_map.items():
        lg_content = re.sub(r'\b' + old + r'\b', temp, lg_content)
        lg_content = re.sub(r'\b' + old + r'\)', temp + ')', lg_content)
        
    for old_idx, new_idx in shuffle_map.items():
        lg_content = lg_content.replace(f"__TEMP_LBL_{old_labels[new_idx]}__", old_labels[new_idx])
        lg_content = lg_content.replace(f"__TEMP_LBL_{old_labels_lower[new_idx]}__", old_labels_lower[new_idx])
        
    return lg_content

def shuffle_question_options(block_content, seed):
    if '\\choiceTF' in block_content:
        cmd = '\\choiceTF'
    elif '\\choice' in block_content:
        cmd = '\\choice'
    else:
        return block_content

    idx = block_content.find(cmd)
    if idx == -1:
        return block_content

    start = idx + len(cmd)
    opt1, s1, e1 = find_next_brace_content(block_content, start)
    if opt1 is None: return block_content
    opt2, s2, e2 = find_next_brace_content(block_content, e1)
    if opt2 is None: return block_content
    opt3, s3, e3 = find_next_brace_content(block_content, e2)
    if opt3 is None: return block_content
    opt4, s4, e4 = find_next_brace_content(block_content, e3)
    if opt4 is None: return block_content

    options = [opt1, opt2, opt3, opt4]
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
            shuffled_lg = shuffle_loigiai_content(lg_content, shuffle_map)
            block_content = (
                block_content[:s1] +
                new_choice_part +
                block_content[e4:lg_s] +
                "{" + shuffled_lg + "}" +
                block_content[lg_e:]
            )
            return block_content

    block_content = block_content[:s1] + new_choice_part + block_content[e4:]
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
#                            LATEX FIX ENGINE
# ==============================================================================

_ARROW_RE = re.compile(
    r'\\(?:xrightarrow|rightarrow|longrightarrow|xrightleftharpoons|rightleftharpoons)'
)

def _wrap_chem_inner(inner):
    result = []
    i = 0
    n = len(inner)
    while i < n:
        if inner[i] == '\\':
            j = i + 1
            while j < n and inner[j].isalpha():
                j += 1
            result.append(inner[i:j])
            i = j
            continue

        if inner[i].isupper() and (i == 0 or not inner[i-1].isalpha()):
            j = i
            while j < n and inner[j].isalpha():
                j += 1
            atom_group = inner[i:j]
            result.append(r'\text{' + atom_group + r'}')
            i = j
            continue

        result.append(inner[i])
        i += 1
    return ''.join(result)

def wrap_chem_text_in_equations(text):
    def process_block(m):
        inner = m.group(1)
        if not _ARROW_RE.search(inner):
            return m.group(0)
        if r'\text{' in inner:
            return m.group(0)
        new_inner = _wrap_chem_inner(inner)
        return r'\[' + new_inner + r'\]'

    return re.sub(r'\\\[([\s\S]*?)\\\]', process_block, text)

def remove_trailing_dot_in_choices(text):
    if not text:
        return text
    pattern = re.compile(r'\\choice(?:TF)?(?![a-zA-Z])')
    result = text
    offset = 0
    for match in pattern.finditer(text):
        search_start = match.end() + offset
        current_pos = search_start
        for i in range(4):
            content, start_brace, end_pos = find_next_brace_content(result, current_pos)
            if content is None:
                break
            new_content = re.sub(r'(?<![0-9])\.(?:\s*)$', '', content)
            if new_content != content:
                old_part = '{' + content + '}'
                new_part = '{' + new_content + '}'
                result = result[:start_brace] + new_part + result[end_pos:]
                offset += len(new_part) - len(old_part)
                end_pos = start_brace + len(new_part)
            current_pos = end_pos
    return result

def fix_latex_common_errors(input_text):
    if not input_text:
        return ""
    processed = input_text
    
    # 1. Double quotes "..." to \lq\lq ... \rq\rq
    processed = re.sub(r'"([^"]*)"', r'\\lq\\lq \1 \\rq\\rq', processed)
    
    # 2. \xrightarrow formatting
    processed = re.sub(r'\\xrightarrow\[([^\]]*)\]\[([^\]]*)\]', r'\\xrightarrow[$\1$][$\2$]', processed)
    processed = re.sub(r'\\xrightarrow\[([^\]]*)\]\{([^}]*)\}', r'\\xrightarrow[$\1$][$\2$]', processed)
    processed = re.sub(r'\\xrightarrow\[([^\]]*)\](?![\[\{])', r'\\xrightarrow[$\1$]', processed)
    processed = re.sub(r'\\xrightarrow\{([^}]*)\}', r'\\xrightarrow[$\1$]', processed)
    
    # 3. ... to \dots
    processed = re.sub(r'\.\.\.', r'\\dots', processed)
    
    # 4. A x B to A \times B
    processed = re.sub(r'(\d+)\s*x\s*(\d+)', r'\1 \\times \2', processed)
    
    # 5. \frac to \dfrac
    processed = re.sub(r'(?<!\\d)\\frac\b', r'\\dfrac', processed)
    
    # 6. Vietnamese subscripts
    processed = re.sub(r'_đ(?!\w)', r'_{\\text{đ}}', processed)
    processed = re.sub(r'_\{đ\}', r'_{\\text{đ}}', processed)
    processed = re.sub(r'_tđ(?!\w)', r'_{\\text{tđ}}', processed)
    processed = re.sub(r'_{tđ\}', r'_{\\text{tđ}}', processed)
    
    # 7. Remove AI citation markers
    processed = re.sub(r'\[cite_start\]', '', processed)
    processed = re.sub(r'\[cite_end\]', '', processed)
    processed = re.sub(r'\[cite[:\s]*[\d,\s]+\]', '', processed)
    
    # 8. Remove duplicate spaces
    processed = re.sub(r'  +', ' ', processed)
    
    # 9. Remove trailing dots in choices
    processed = remove_trailing_dot_in_choices(processed)
    
    # 10. Wrap chemical formulas in math equations
    processed = wrap_chem_text_in_equations(processed)
    
    return processed

# ==============================================================================
#                            DOCX IMAGE EXTRACTOR
# ==============================================================================

def extract_images_from_docx(doc_path, output_dir):
    try:
        import docx
    except ImportError:
        print("ERROR: python-docx chưa được cài. Chạy: pip install python-docx")
        sys.exit(1)

    doc = docx.Document(doc_path)
    os.makedirs(output_dir, exist_ok=True)

    A_NS = 'http://schemas.openxmlformats.org/drawingml/2006/main'
    R_NS = 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'

    rels = doc.part.rels
    image_counter = 1
    manifest = []

    def save_image_from_rel(r_embed):
        nonlocal image_counter
        if r_embed not in rels:
            return None
        rel = rels[r_embed]
        if "image" not in rel.target_ref:
            return None
        img_part = rel.target_part
        img_ext = img_part.content_type.split('/')[-1]
        if img_ext == 'jpeg':
            img_ext = 'jpg'
        img_filename = f"image_{image_counter}.{img_ext}"
        img_path = os.path.join(output_dir, img_filename)
        with open(img_path, "wb") as f:
            f.write(img_part.blob)
        print(f"Extracted {img_filename}")
        image_counter += 1
        return img_filename

    paragraphs = doc.paragraphs
    n = len(paragraphs)

    for idx, para in enumerate(paragraphs):
        blips = para._p.findall(f'.//{{{A_NS}}}blip')
        if not blips:
            continue

        para_images = []
        for blip in blips:
            r_embed = blip.get(f'{{{R_NS}}}embed')
            fname = save_image_from_rel(r_embed)
            if fname:
                para_images.append(fname)

        if not para_images:
            continue

        ctx_before = []
        for j in range(max(0, idx - 3), idx):
            t = paragraphs[j].text.strip()
            if t:
                ctx_before.append(t)

        ctx_after = []
        for j in range(idx + 1, min(n, idx + 4)):
            t = paragraphs[j].text.strip()
            if t:
                ctx_after.append(t)

        for fname in para_images:
            abs_path = os.path.abspath(os.path.join(output_dir, fname)).replace("\\", "/")
            entry = {
                "filename": fname,
                "absolute_path": abs_path,
                "para_index": idx,
                "para_text": para.text.strip(),
                "context_before": ctx_before,
                "context_after": ctx_after,
            }
            manifest.append(entry)
            print(f"  -> {fname} (para {idx}): {abs_path}")

    manifest_path = os.path.join(output_dir, "image_manifest.json")
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)

    print(f"\nTotal: {image_counter - 1} images -> {output_dir}")
    print(f"Manifest saved: {manifest_path}")
    return manifest

def find_image_for_question(question_text, manifest_path, threshold=0.3):
    if not os.path.isfile(manifest_path):
        return []

    with open(manifest_path, "r", encoding="utf-8") as f:
        manifest = json.load(f)

    if not manifest:
        return []

    def normalize(s):
        return re.sub(r'\s+', ' ', s.lower().strip())

    q_norm = normalize(question_text)
    best_matches = []

    for entry in manifest:
        all_context = " ".join(
            entry.get("context_before", []) +
            [entry.get("para_text", "")] +
            entry.get("context_after", [])
        )
        ctx_norm = normalize(all_context)
        score = SequenceMatcher(None, q_norm, ctx_norm).ratio()

        q_words = set(q_norm.split())
        c_words = set(ctx_norm.split())
        overlap = len(q_words & c_words) / max(len(q_words), 1)
        combined = score * 0.5 + overlap * 0.5

        if combined >= threshold:
            img_dir = os.path.dirname(manifest_path)
            img_path = os.path.join(img_dir, entry["filename"]).replace("\\", "/")
            best_matches.append((combined, img_path, entry["filename"]))

    best_matches.sort(key=lambda x: -x[0])
    return [(path, fname, score) for score, path, fname in best_matches]

# ==============================================================================
#                            IMAGE PATH NORMALIZER
# ==============================================================================

def normalize_image_paths_in_tex(tex_content, base_dir=None, tex_file_path=None):
    search_dirs = []
    if base_dir and os.path.isdir(base_dir):
        search_dirs.append(os.path.abspath(base_dir))
    if tex_file_path:
        tex_dir = os.path.dirname(os.path.abspath(tex_file_path))
        if tex_dir not in search_dirs:
            search_dirs.append(tex_dir)

    pattern = re.compile(r'(\\includegraphics(?:\[[^\]]*\])?)\{([^}]+)\}')
    changed = 0
    warnings = []

    def replace_path(m):
        nonlocal changed
        cmd_part = m.group(1)
        img_path = m.group(2).strip()

        img_path_normalized = img_path.replace("\\", "/")

        if os.path.isabs(img_path_normalized):
            abs_str = img_path_normalized.replace("\\", "/")
            if abs_str != img_path:
                changed += 1
            return f"{cmd_part}{{{abs_str}}}"

        resolved = None
        for d in search_dirs:
            candidate = os.path.normpath(os.path.join(d, img_path_normalized))
            if os.path.isfile(candidate):
                resolved = candidate
                break

        if resolved:
            abs_str = os.path.abspath(resolved).replace("\\", "/")
            changed += 1
            return f"{cmd_part}{{{abs_str}}}"
        else:
            warnings.append(f"  [WARN] Không tìm thấy ảnh: '{img_path}'")
            return m.group(0)

    result = pattern.sub(replace_path, tex_content)
    if warnings:
        for w in warnings:
            print(w)
    print(f"[imgpaths] Đã chuẩn hóa {changed} đường dẫn \\includegraphics.")
    return result

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

def cmd_fix(args):
    import argparse
    parser = argparse.ArgumentParser(description="Sửa lỗi LaTeX phổ biến.")
    parser.add_argument("input_file", help="Đường dẫn file LaTeX đầu vào")
    parser.add_argument("output_file", nargs="?", default=None, help="Đường dẫn file đầu ra")
    parsed = parser.parse_args(args)
    
    out_path = parsed.output_file if parsed.output_file else parsed.input_file
    
    with open(parsed.input_file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    fixed = fix_latex_common_errors(content)
    
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(fixed)
        
    print(f"Done. Sửa lỗi LaTeX thành công. Lưu tại: {out_path}")

def cmd_images(args):
    import argparse
    parser = argparse.ArgumentParser(description="Trích xuất ảnh từ file .docx và ánh xạ ngữ cảnh.")
    parser.add_argument("source", help="File .docx nguồn")
    parser.add_argument("output_dir", help="Thư mục lưu ảnh")
    parser.add_argument("--find", default=None, help="Tìm ảnh phù hợp cho câu hỏi")
    parsed = parser.parse_args(args)

    if parsed.find:
        manifest_path = os.path.join(parsed.output_dir, "image_manifest.json")
        results = find_image_for_question(parsed.find, manifest_path)
        if results:
            print("Ảnh phù hợp nhất:")
            for path, fname, score in results[:3]:
                print(f"  [{score:.2f}] {fname} -> {path}")
        else:
            print("Không tìm thấy ảnh phù hợp.")
    else:
        extract_images_from_docx(parsed.source, parsed.output_dir)

def cmd_imgpaths(args):
    import argparse
    parser = argparse.ArgumentParser(description="Chuẩn hóa đường dẫn \\includegraphics thành tuyệt đối.")
    parser.add_argument("tex_file", help="File LaTeX cần xử lý")
    parser.add_argument("--base-dir", default=None, help="Thư mục gốc chứa ảnh để resolve relative path")
    parser.add_argument("--inplace", action="store_true", help="Ghi đè trực tiếp lên file gốc")
    parser.add_argument("--out", default=None, help="Đường dẫn file output khác")
    parsed = parser.parse_args(args)

    with open(parsed.tex_file, "r", encoding="utf-8") as f:
        content = f.read()

    new_content = normalize_image_paths_in_tex(
        content,
        base_dir=parsed.base_dir,
        tex_file_path=parsed.tex_file
    )

    if parsed.inplace:
        with open(parsed.tex_file, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"[imgpaths] Đã ghi đè thành công: {parsed.tex_file}")
    elif parsed.out:
        with open(parsed.out, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"[imgpaths] Đã lưu tại: {parsed.out}")
    else:
        print(new_content)

def cmd_shuffle(args):
    import argparse
    parser = argparse.ArgumentParser(description="Trộn câu hỏi và phương án để sinh mã đề thi mới.")
    parser.add_argument("source", help="File LaTeX đề thi gốc")
    parser.add_argument("--seed", type=int, default=42, help="Seed xáo trộn")
    parser.add_argument("--made2", type=str, default=None, help="Mã đề mới (3 chữ số)")
    parser.add_argument("--out-name", type=str, default=None, help="Đường dẫn file output tùy chọn")
    parsed = parser.parse_args(args)
    
    if not os.path.exists(parsed.source):
        print(f"Lỗi: File nguồn không tồn tại: {parsed.source}")
        sys.exit(1)
        
    with open(parsed.source, 'r', encoding='utf-8') as f:
        src_content = f.read()
        
    src_content = normalize_image_paths_in_tex(src_content, tex_file_path=parsed.source)
    questions = parse_questions_from_text(src_content)
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
    assembled_content = build_exam_string(shuffled_qs, ten_file, made2, metadata)
    
    os.makedirs(os.path.dirname(os.path.abspath(out_path)), exist_ok=True)
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(assembled_content)
        
    print(f"Trộn đề thành công -> Đã lưu tại: {out_path}")

def cmd_assemble(args):
    import argparse
    parser = argparse.ArgumentParser(description="Ghép các câu hỏi LaTeX vào mẫu đề thi chuẩn.")
    parser.add_argument("--input", nargs="+", help="Các file hoặc thư mục chứa câu hỏi")
    parser.add_argument("--output", help="Đường dẫn file LaTeX đề thi đầu ra")
    parser.add_argument("--monhoc", default=None, help="Tên môn học")
    parser.add_argument("--ngaykt", default=None, help="Ngày thi")
    parser.add_argument("--nh", default="2025 - 2026", help="Năm học")
    parser.add_argument("--thoigian", default="45", help="Thời gian làm bài (phút)")
    parser.add_argument("--made", default=None, help="Mã đề thi")
    parser.add_argument("--ten-de", default="Kiểm tra", help="Tên kì thi")
    parser.add_argument("--config", help="Đọc cấu hình tùy chọn từ file JSON")
    parsed = parser.parse_args(args)
    
    cfg = {}
    if parsed.config:
        if os.path.exists(parsed.config):
            with open(parsed.config, 'r', encoding='utf-8') as f:
                cfg = json.load(f)
        else:
            print(f"Lỗi: Không tìm thấy file config: {parsed.config}")
            sys.exit(1)
            
    inputs = parsed.input if parsed.input else cfg.get("input", [])
    if not inputs and "parts" in cfg:
        inputs = [p for p in cfg["parts"].values() if p]
        
    if isinstance(inputs, str):
        inputs = [inputs]
        
    output = parsed.output if parsed.output else cfg.get("output", "assembled_exam.tex")
    monhoc = parsed.monhoc if parsed.monhoc else cfg.get("monhoc", "<Tên môn học>")
    ngaykt = parsed.ngaykt if parsed.ngaykt else cfg.get("ngaykt", "<Ngày thi>")
    nh = parsed.nh if parsed.nh else cfg.get("nh", "2025 - 2026")
    thoigian = parsed.thoigian if parsed.thoigian else cfg.get("thoigian", "45")
    made = parsed.made if parsed.made else cfg.get("made", None)
    ten_de = parsed.ten_de if parsed.ten_de else cfg.get("ten_de", "Kiểm tra")
    
    if not inputs:
        print("Lỗi: Không chỉ định file câu hỏi đầu vào (dùng --input hoặc config).")
        sys.exit(1)
        
    questions = load_questions_from_paths(inputs)
    if not questions:
        print("Lỗi: Không phân tích được câu hỏi nào từ các nguồn đầu vào.")
        sys.exit(1)
        
    ten_file, computed_made = get_tenfile_and_made(output, made)
    
    metadata = {
        'monhoc': monhoc,
        'ngaykt': ngaykt,
        'nh': nh,
        'thoigian': thoigian,
        'ten_de': ten_de
    }
    
    assembled_content = build_exam_string(questions, ten_file, computed_made, metadata)
    
    os.makedirs(os.path.dirname(os.path.abspath(output)), exist_ok=True)
    with open(output, 'w', encoding='utf-8') as f:
        f.write(assembled_content)
        
    print(f"Ghép đề thành công -> Đã lưu tại: {output}")

def cmd_compile(args):
    import argparse
    parser = argparse.ArgumentParser(description="Biên dịch file LaTeX thành PDF.")
    parser.add_argument("tex_file", help="File LaTeX cần biên dịch")
    parser.add_argument("--dir", default=None, help="Thư mục làm việc")
    parser.add_argument("--times", type=int, default=2, help="Số lần chạy pdflatex")
    parsed = parser.parse_args(args)
    
    work_dir = parsed.dir if parsed.dir else os.path.dirname(os.path.abspath(parsed.tex_file))
    compile_latex(parsed.tex_file, work_dir, parsed.times)

def compile_latex(tex_file, work_dir, times=2):
    basename = os.path.basename(tex_file)
    errors = []
    print(f"Đang biên dịch: {basename} trong thư mục: {work_dir}")
    for i in range(1, times + 1):
        print(f"\n-- pdflatex pass {i}/{times} --")
        result = subprocess.run(
            ["pdflatex", "-interaction=nonstopmode", basename],
            cwd=work_dir,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace"
        )
        errs = [l for l in result.stdout.splitlines() if l.startswith("!")]
        errors.extend(errs)
        if result.returncode != 0 and i == 1:
            print("STDERR:", result.stderr[-500:])
            
    if errors:
        print("\n[!] Có lỗi xảy ra trong quá trình biên dịch:")
        for e in set(errors):
            print(" ", e)
    else:
        pdf = os.path.join(work_dir, basename.replace(".tex", ".pdf"))
        print(f"\n[OK] Biên dịch hoàn tất -> {pdf}")
    return len(errors) == 0

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

def cmd_deduplicate(args):
    import argparse
    parser = argparse.ArgumentParser(description="Lọc câu hỏi trùng lặp.")
    parser.add_argument("input_path", help="Đường dẫn file/thư mục nguồn")
    parser.add_argument("output_file", help="Đường dẫn file lưu kết quả")
    parser.add_argument("--threshold", type=float, default=0.85, help="Ngưỡng tương đồng (0.0 đến 1.0)")
    parsed = parser.parse_args(args)
    
    questions = load_questions_from_paths([parsed.input_path])
    if not questions:
        print("Không tìm thấy câu hỏi nào.")
        return
        
    initial_count = len(questions)
    print(f"Nạp {initial_count} câu hỏi. Đang tiến hành lọc trùng...")
    
    unique_qs, removed = remove_duplicates(questions, parsed.threshold)
    final_count = len(unique_qs)
    
    print(f"Đã loại bỏ {removed} câu hỏi trùng. Còn lại: {final_count} câu.")
    
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
            
    print(f"Lưu kết quả thành công tại: {parsed.output_file}")

# ==============================================================================
#                            ENTRY POINT
# ==============================================================================

COMMANDS = {
    "fix": cmd_fix,
    "images": cmd_images,
    "imgpaths": cmd_imgpaths,
    "shuffle": cmd_shuffle,
    "assemble": cmd_assemble,
    "compile": cmd_compile,
    "parse": cmd_parse,
    "dedup": cmd_deduplicate,
}

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python latex_tools.py <command> [args]")
        print("Available commands:", ", ".join(COMMANDS.keys()))
        sys.exit(1)
        
    cmd = sys.argv[1]
    if cmd in COMMANDS:
        COMMANDS[cmd](sys.argv[2:])
    else:
        print(f"Lỗi: Không tìm thấy lệnh: {cmd}")
        print("Lệnh khả dụng:", ", ".join(COMMANDS.keys()))
        sys.exit(1)
