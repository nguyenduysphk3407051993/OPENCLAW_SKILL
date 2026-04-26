# -*- coding: utf-8 -*-
import io
"""
latex_tools.py  —  Bộ công cụ tích hợp cho exam_latex_creator skill
=====================================================================
Gộp toàn bộ chức năng từ các file:
  • fix_latex_errors.py      → sửa lỗi LaTeX phổ biến
  • extract_images.py        → trích ảnh từ .docx
  • assemble_exam.py         → ghép các part thành file đề thi
  • generate_two_exams.py    → tạo 2 mã đề từ 1 file nguồn
  • generate_khtn9_cuoihkii.py → tạo MADE102 bằng cách xáo trộn MADE101

Cách dùng (CLI):
  python latex_tools.py fix       input.tex [output.tex]
  python latex_tools.py images    source.docx output_dir
  python latex_tools.py assemble  config.json
  python latex_tools.py shuffle   source_made101.tex [--seed 42] [--made2 102]
  python latex_tools.py compile   file.tex [--dir output_dir] [--times 2]
"""

import os
import re
import sys
import json
import random
import subprocess

SKILL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_DIR = os.path.join(SKILL_DIR, "output")

# ===========================================================================
# MODULE 1 — fix_latex_errors
# ===========================================================================

latex_error_dict = {
    # Dấu ngoặc kép "..." → \lq\lq ... \rq\rq
    r'"([^"]*)"': r'\\lq\\lq \1 \\rq\\rq',
    # $$...$$ → \[ ... \]  (CHỈ áp dụng khi $$ đứng đầu dòng hoặc sau khoảng trắng, tránh xrightarrow)
    # r'\$\$([\S\s]*?)\$\$': r'\\[ \1 \\]',  # TẮT — gây lỗi với \xrightarrow[$$...]
    # \xrightarrow[a][b]
    r'\\xrightarrow\[([^\]]*)\]\[([^\]]*)\]': r'\\xrightarrow[$\1$][$\2$]',
    # \xrightarrow[a]{b}
    r'\\xrightarrow\[([^\]]*)\]\{([^}]*)\}': r'\\xrightarrow[$\1$][$\2$]',
    # \xrightarrow[a] (không có tham số 2)
    r'\\xrightarrow\[([^\]]*)\](?![\[\{])': r'\\xrightarrow[$\1$]',
    # \xrightarrow{a}
    r'\\xrightarrow\{([^}]*)\}': r'\\xrightarrow[$\1$]',
    # ... → \dots
    r'\.\.\.': r'\\dots',
    # số x số → số \times số
    r'(\d+)\s*x\s*(\d+)': r'\1 \\times \2',
    # \frac → \dfrac
    r'\\frac': r'\\dfrac',
    # Chỉ số dưới tiếng Việt
    r'_đ(?!\w)':   r'_{\\text{đ}}',
    r'_\{đ\}':     r'_{\\text{đ}}',
    r'_tđ(?!\w)':  r'_{\\text{tđ}}',
    r'_\{tđ\}':    r'_{\\text{tđ}}',
    # Xoá thẻ trích dẫn AI
    r'\[cite_start\]': '',
    r'\[cite_end\]':   '',
    r'\[cite[:\s]*[\d,\s]+\]': '',
    # \xrightarrow[$$...$$ ] → \xrightarrow[$...$]  (bỏ $$ thừa bên trong [...])
    r'\\xrightarrow\[\$\$([^\]]*)\$\$\]': r'\\xrightarrow[$\1$]',
    # [$$] rỗng → xóa hoàn toàn
    r'\[\$\$\]': '',
    r'\[\$\s*\\\$\]\]': '',
    # ^o → ^\circ (ký hiệu độ)
    r'\^o(?=[^a-zA-Z])': r'^\\circ',
    # Xoá "Sai." hoặc "Đúng." thừa sau \itemch
    r'(\\itemch)\s*(?:Sai\.|Đúng\.)\s*': r'\1 ',
}

_CHOICE_OPTION = re.compile(
    r'(\{(?:\\True\s+)?)((?:[^{}]|\{[^{}]*\})+?)(\s*\})'
)

def _strip_trailing_dot(m):
    content = m.group(2).rstrip()
    if content.endswith('.'):
        content = content[:-1]
    return m.group(1) + content + m.group(3)

def remove_trailing_dot_in_choices(text):
    def process_block(m):
        block = m.group(0)
        block = _CHOICE_OPTION.sub(_strip_trailing_dot, block)
        return block
    text = re.sub(r'\\choiceTF\s*(\{(?:[^{}]|\{[^{}]*\})*\}){4}', process_block, text)
    text = re.sub(r'\\choice\s*(\{(?:[^{}]|\{[^{}]*\})*\}){4}', process_block, text)
    return text

def fix_latex_common_errors(input_text):
    if not input_text:
        return ""
    processed = input_text
    for pattern, replacement in latex_error_dict.items():
        processed = re.sub(pattern, replacement, processed)
    processed = re.sub(r'  +', ' ', processed)
    processed = remove_trailing_dot_in_choices(processed)
    processed = wrap_chem_text_in_equations(processed)
    return processed

# ---------------------------------------------------------------------------
# Bọc ký tự hóa học bằng \text{} trong phương trình có mũi tên phản ứng
# ---------------------------------------------------------------------------

# Mũi tên phản ứng hóa học
_ARROW_RE = re.compile(
    r'\\(?:xrightarrow|rightarrow|longrightarrow|xrightleftharpoons|rightleftharpoons)'
)

# Ký tự hóa học: 1-2 chữ cái bắt đầu bằng HOA, không đứng sau \
# Không bắt nếu đã trong \text{...} hoặc \mathrm{...}
_CHEM_ATOM_RE = re.compile(
    r'(?<!\\)(?<!{)(?<!\w)([A-Z][a-z]?)(?=[\^_{}\s\+\-\)\]\,\.\d\\]|$)'
)

# Nhãn LaTeX cần loại trừ (không bọc \text)
_LATEX_CMD_BEFORE = re.compile(r'\\[a-zA-Z]+$')

def _wrap_chem_inner(inner):
    """Bọc chuỗi ký tự hóa học liên tiếp bằng \\text{} bên trong một phương trình.
    VD: C_6H_{12}O_6 → \\text{C}_6\\text{H}_{12}\\text{O}_6
        Ag_2O       → \\text{Ag}_2\\text{O}
        NH_3        → \\text{NH}_3  (nhóm liền nhau → 1 \\text{})
    """
    result = []
    i = 0
    n = len(inner)
    while i < n:
        # Bỏ qua lệnh LaTeX bắt đầu bằng \
        if inner[i] == '\\':
            j = i + 1
            while j < n and inner[j].isalpha():
                j += 1
            result.append(inner[i:j])
            i = j
            continue

        # Bắt chuỗi chữ cái hóa học liên tiếp (VD: NH, OH, CO, Ag, Ca...)
        # Điều kiện: bắt đầu bằng HOA, không đứng sau chữ cái khác
        if inner[i].isupper() and (i == 0 or not inner[i-1].isalpha()):
            j = i
            # Đọc toàn bộ chuỗi chữ cái liên tiếp (hoa + thường xen kẽ)
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
    """
    Tìm các khối \\[ ... \\] chứa mũi tên phản ứng hóa học,
    tự động bọc các ký tự hóa học bằng \\text{}.

    Dấu hiệu nhận diện: có \\xrightarrow, \\rightarrow, v.v.
    """
    def process_block(m):
        inner = m.group(1)
        # Chỉ xử lý nếu có mũi tên phản ứng
        if not _ARROW_RE.search(inner):
            return m.group(0)
        # Bỏ qua nếu đã có \text{ (đã xử lý tay)
        if r'\text{' in inner:
            return m.group(0)
        new_inner = _wrap_chem_inner(inner)
        return r'\[' + new_inner + r'\]'

    return re.sub(r'\\\[([\s\S]*?)\\\]', process_block, text)



def cmd_fix(args):
    if len(args) < 1:
        print("Usage: python latex_tools.py fix input.tex [output.tex]")
        sys.exit(1)
    input_path  = args[0]
    output_path = args[1] if len(args) >= 2 else input_path
    with open(input_path, "r", encoding="utf-8") as f:
        original = f.read()
    fixed = fix_latex_common_errors(original)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(fixed)
    changed = sum(1 for a, b in zip(original, fixed) if a != b)
    print("Done. Output: %s  (approx %d chars changed)" % (output_path, changed))


# ===========================================================================
# MODULE 2 — extract_images (từ .docx)
# ===========================================================================

def extract_images_from_docx(doc_path, output_dir):
    try:
        import docx
    except ImportError:
        print("ERROR: python-docx chưa được cài. Chạy: pip install python-docx")
        sys.exit(1)
    doc = docx.Document(doc_path)
    os.makedirs(output_dir, exist_ok=True)
    counter = 1
    for rel in getattr(doc.part, 'rels', {}).values():
        if "image" in rel.target_ref:
            img_part = rel.target_part
            img_ext  = img_part.content_type.split('/')[-1]
            if img_ext == 'jpeg':
                img_ext = 'jpg'
            img_filename = f"image_{counter}.{img_ext}"
            img_path = os.path.join(output_dir, img_filename)
            with open(img_path, "wb") as f:
                f.write(img_part.blob)
            print(f"Extracted {img_filename}")
            counter += 1
    print(f"Total: {counter - 1} images → {output_dir}")

def cmd_images(args):
    if len(args) < 2:
        print("Usage: python latex_tools.py images source.docx output_dir")
        sys.exit(1)
    extract_images_from_docx(args[0], args[1])


# ===========================================================================
# MODULE 3 — assemble_exam (ghép part files thành đề thi hoàn chỉnh)
# ===========================================================================

def assemble_exam_from_config(config_path):
    """
    Config JSON mẫu:
    {
      "monhoc": "Khoa học tự nhiên 6",
      "ngaykt": "04/02/2026",
      "nh": "2025 - 2026",
      "thoigian": "45",
      "made": "847",
      "ten_de": "Đề cương giữa kì 2",
      "output_name": "DeCuong_GiuaKi2_VL6_847.tex",
      "tieudegiua": true,
      "parts": {
        "EX": "path/to/part_ex.tex",
        "TF": "path/to/part_tf.tex",
        "SA": "path/to/part_sa.tex",
        "BT": "path/to/part_bt.tex"
      }
    }
    """
    with open(config_path, "r", encoding="utf-8") as f:
        cfg = json.load(f)

    def read(path):
        if not path or not os.path.isfile(path):
            return ""
        with open(path, "r", encoding="utf-8") as f:
            return f.read()

    monhoc   = cfg.get("monhoc", "")
    ngaykt   = cfg.get("ngaykt", "")
    nh       = cfg.get("nh", "")
    thoigian = cfg.get("thoigian", "45")
    made     = cfg.get("made", "101")
    ten_de   = cfg.get("ten_de", "Kiểm tra")
    out_name = cfg.get("output_name", f"exam_MADE{made}.tex")
    sophong  = cfg.get("sophong", "")
    truong   = cfg.get("truong", "")
    tieudegiua = cfg.get("tieudegiua", False)

    parts = cfg.get("parts", {})
    ex_content = read(parts.get("EX", ""))
    tf_content = read(parts.get("TF", ""))
    sa_content = read(parts.get("SA", ""))
    bt_content = read(parts.get("BT", ""))

    tieude_cmd = (
        f"\\Tieudegiua{{{ten_de} - Mã đề \\made}}"
        if tieudegiua
        else f"\\section[{ten_de} - Mã đề \\made]{{{ten_de}}}"
    )

    def section(title, open_cmds, counter_reset, content, close_cmds, bangdapan=""):
        if not content.strip():
            return ""
        lines = [f"\n%%%=============={title}==============%%%"]
        lines.append(f"\\subsection{{{title}}}")
        lines += open_cmds
        if counter_reset:
            lines.append("\\setcounter{ex}{0}")
        lines.append(content)
        lines += close_cmds
        if bangdapan:
            lines.append(f"%{bangdapan}")
        return "\n".join(lines) + "\n"

    header_lines = ["\\documentclass[FileMain.tex]{subfiles}"]
    if sophong:
        header_lines.append(f"\\gdef\\sophong{{{sophong}}}")
    if truong:
        header_lines.append(f"\\gdef\\truong{{{truong}}}")
    header_lines += [
        f"\\gdef\\monhoc{{{monhoc}}}",
        f"\\gdef\\ngaykt{{{ngaykt}}}",
        f"\\gdef\\nh{{{nh}}}",
        f"\\gdef\\thoigian{{{thoigian}}}",
        f"\\gdef\\made{{{made}}}",
        "\\setcounter{section}{0}",
        "%\\tatloigiai",
        "%\\hienthiloigiai",
        "%\\dongkeloigiai",
        "\\begin{document}",
        tieude_cmd,
    ]
    header = "\n".join(header_lines) + "\n"

    body = ""
    body += section(
        "Bài tập trắc nghiệm nhiều lựa chọn",
        [f"\\Opensolutionfile{{ansex}}[Ans/LGEX-{out_name[:-4]}]",
         f"\\Opensolutionfile{{ans}}[Ans/Ans-{out_name[:-4]}]"],
        False, ex_content,
        ["\\Closesolutionfile{ans}", "\\Closesolutionfile{ansex}"],
        f"\\bangdapan{{Ans-{out_name[:-4]}}}"
    )
    body += section(
        "Trắc nghiệm đúng sai",
        [f"\\Opensolutionfile{{ansex}}[Ans/LGTF-{out_name[:-4]}]",
         f"\\Opensolutionfile{{ansbook}}[Ansbook/AnsTF-{out_name[:-4]}]",
         f"\\Opensolutionfile{{ans}}[Ans/Tempt-{out_name[:-4]}]"],
        True, tf_content,
        ["\\Closesolutionfile{ans}", "\\Closesolutionfile{ansbook}", "\\Closesolutionfile{ansex}"],
        f"\\bangdapanTF{{AnsTF-{out_name[:-4]}}}"
    )
    body += section(
        "Bài tập trả lời ngắn",
        [f"\\Opensolutionfile{{ansex}}[Ans/LGSA-{out_name[:-4]}]",
         f"\\Opensolutionfile{{ansexh}}[Ans/AnsSA-{out_name[:-4]}]"],
        True, sa_content,
        ["\\Closesolutionfile{ansexh}", "\\Closesolutionfile{ansex}"]
    )
    body += section(
        "Bài tập tự luận",
        [f"\\Opensolutionfile{{ansbth}}[Ans/LGBT-{out_name[:-4]}]",
         f"\\Opensolutionfile{{ansbt}}[Ans/AnsBT-{out_name[:-4]}]"],
        False, bt_content,
        ["\\Closesolutionfile{ansbt}", "\\Closesolutionfile{ansbth}"]
    )

    footer = (
        "\n\\begin{center}\n"
        " \\rule[4pt]{2cm}{1pt}\\,\\large\\bfseries Hết\\,\\rule[4pt]{2cm}{1pt}\n"
        "\\end{center}\n"
        "\\label{x}\n"
        "\\end{document}\n"
    )

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    out_path = os.path.join(OUTPUT_DIR, out_name)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(header + body + footer)
    print(f"Assembled: {out_path}")
    return out_path

def cmd_assemble(args):
    if len(args) < 1:
        print("Usage: python latex_tools.py assemble config.json")
        sys.exit(1)
    assemble_exam_from_config(args[0])


# ===========================================================================
# MODULE 4 — shuffle (tạo mã đề mới bằng cách xáo trộn)
# ===========================================================================

def extract_blocks(prefix, src):
    pattern = (
        r'(%%%[=]+\s*' + prefix + r'_\d+\s*[=]+%%%'
        r'[\s\S]*?'
        r'\\end\{(?:ex|bt)\})'
    )
    return [m.group(1).strip() for m in re.finditer(pattern, src)]

def renumber_blocks(blocks, prefix):
    result = []
    for i, block in enumerate(blocks, 1):
        block = re.sub(
            r'%%%[=]+\s*' + prefix + r'_\d+\s*[=]+%%%',
            f'%%%============={prefix}_{i}=============%%%',
            block
        )
        result.append(block)
    return result

def get_gdef(name, src, default=""):
    m = re.search(r'\\gdef\\' + name + r'\{([^}]*)\}', src)
    return m.group(1) if m else default

def build_exam_content(src_text, ex_blocks, tf_blocks, sa_blocks, bt_blocks, made):
    """Tạo nội dung đề thi đầy đủ theo cấu trúc chuẩn."""
    sophong  = get_gdef("sophong",  src_text, "")
    truong   = get_gdef("truong",   src_text, "")
    truongh  = get_gdef("truongh",  src_text, "")
    monhoc   = get_gdef("monhoc",   src_text, "")
    nh       = get_gdef("nh",       src_text, "2025 - 2026")
    thoigian = get_gdef("thoigian", src_text, "45")

    # Lấy tên section từ file gốc
    m_sec = re.search(r'\\section\[([^\]]*?)(?:\s*-\s*Mã đề[^\]]*)\]', src_text)
    ten_de = m_sec.group(1).strip() if m_sec else "Kiểm tra"

    # Tiêu đề (section hoặc Tieudegiua)
    if re.search(r'\\Tieudegiua', src_text):
        tieude = f"\\Tieudegiua{{{ten_de} - Mã đề \\made}}"
    else:
        tieude = f"\\section[{ten_de} - Mã đề \\made]{{{ten_de}}}"

    file_stem = f"exam_MADE{made}"

    lines = ["\\documentclass[FileMain.tex]{subfiles}"]
    if sophong:  lines.append(f"\\gdef\\sophong{{{sophong}}}")
    if truong:   lines.append(f"\\gdef\\truong{{{truong}}}")
    if truongh:  lines.append(f"\\gdef\\truongh{{{truongh}}}")
    lines += [
        f"\\gdef\\monhoc{{{monhoc}}}",
        "\\gdef\\ngaykt{}",
        f"\\gdef\\nh{{{nh}}}",
        f"\\gdef\\thoigian{{{thoigian}}}",
        f"\\gdef\\made{{{made}}}",
        "\\setcounter{section}{0}",
        "%\\tatloigiai",
        "%\\hienthiloigiai",
        "%\\dongkeloigiai",
        "\\begin{document}",
        tieude,
    ]

    def add_section(title, opens, counter_reset, blocks, closes):
        if not blocks:
            return []
        sec = [f"\n%%%=============={title}==============%%%",
               f"\\subsection{{{title}}}"]
        sec += opens
        if counter_reset:
            sec.append("\\setcounter{ex}{0}")
        sec.append("\n\n".join(blocks))
        sec += closes
        return sec

    lines += add_section(
        "Bài tập trắc nghiệm nhiều lựa chọn",
        [f"\\Opensolutionfile{{ansex}}[Ans/LGEX-{file_stem}]",
         f"\\Opensolutionfile{{ans}}[Ans/Ans-{file_stem}]"],
        False,
        renumber_blocks(ex_blocks, "EX"),
        ["\\Closesolutionfile{ans}", "\\Closesolutionfile{ansex}"]
    )
    lines += add_section(
        "Trắc nghiệm đúng sai",
        [f"\\Opensolutionfile{{ansex}}[Ans/LGTF-{file_stem}]",
         f"\\Opensolutionfile{{ansbook}}[Ansbook/AnsTF-{file_stem}]",
         f"\\Opensolutionfile{{ans}}[Ans/Tempt-{file_stem}]"],
        True,
        renumber_blocks(tf_blocks, "TF"),
        ["\\Closesolutionfile{ans}", "\\Closesolutionfile{ansbook}", "\\Closesolutionfile{ansex}"]
    )
    lines += add_section(
        "Bài tập trả lời ngắn",
        [f"\\Opensolutionfile{{ansex}}[Ans/LGSA-{file_stem}]",
         f"\\Opensolutionfile{{ansexh}}[Ans/AnsSA-{file_stem}]"],
        True,
        renumber_blocks(sa_blocks, "SA"),
        ["\\Closesolutionfile{ansexh}", "\\Closesolutionfile{ansex}"]
    )
    lines += add_section(
        "Bài tập tự luận",
        [f"\\Opensolutionfile{{ansbth}}[Ans/LGBT-{file_stem}]",
         f"\\Opensolutionfile{{ansbt}}[Ans/AnsBT-{file_stem}]"],
        False,
        renumber_blocks(bt_blocks, "BT"),
        ["\\Closesolutionfile{ansbt}", "\\Closesolutionfile{ansbth}"]
    )

    lines += [
        "\n\\begin{center}",
        " \\rule[4pt]{2cm}{1pt}\\,\\large\\bfseries Hết\\,\\rule[4pt]{2cm}{1pt}",
        "\\end{center}",
        "\\label{x}",
        "\\end{document}",
    ]
    return "\n".join(lines) + "\n"

def cmd_shuffle(args):
    """
    Tạo mã đề mới bằng cách xáo trộn câu hỏi từ file nguồn.
    Usage: python latex_tools.py shuffle source.tex [--seed 42] [--made2 102] [--out-name NAME]
    """
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("source")
    parser.add_argument("--seed",     type=int, default=42)
    parser.add_argument("--made2",    type=int, default=None,
                        help="Mã đề mới (mặc định: tăng 1 so với file gốc)")
    parser.add_argument("--out-name", default=None,
                        help="Tên file output (không cần đuôi .tex)")
    parsed = parser.parse_args(args)

    with open(parsed.source, "r", encoding="utf-8") as f:
        src = f.read()

    all_ex = extract_blocks("EX", src)
    all_tf = extract_blocks("TF", src)
    all_sa = extract_blocks("SA", src)
    all_bt = extract_blocks("BT", src)
    print(f"Trích được: {len(all_ex)} EX, {len(all_tf)} TF, {len(all_sa)} SA, {len(all_bt)} BT")

    # Xác định mã đề mới
    if parsed.made2 is None:
        m = re.search(r'\\gdef\\made\{(\d+)\}', src)
        made2 = int(m.group(1)) + 1 if m else 102
    else:
        made2 = parsed.made2

    random.seed(parsed.seed)
    ex2 = all_ex[:]
    tf2 = all_tf[:]
    sa2 = all_sa[:]
    bt2 = all_bt[:]
    random.shuffle(ex2)
    random.shuffle(tf2)
    random.shuffle(sa2)
    random.shuffle(bt2)

    content = build_exam_content(src, ex2, tf2, sa2, bt2, made2)

    out_name = parsed.out_name or f"exam_MADE{made2}"
    out_stem = os.path.splitext(os.path.basename(parsed.source))[0]
    # Thay số mã đề cũ bằng mã đề mới trong tên file
    out_file = re.sub(r'MADE\d+', f'MADE{made2}', out_stem) + ".tex"
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    out_path = os.path.join(OUTPUT_DIR, out_file)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Đã tạo: {out_path}")


# ===========================================================================
# MODULE 5 — compile (biên dịch pdflatex)
# ===========================================================================

def compile_latex(tex_file, work_dir=None, times=2):
    if work_dir is None:
        work_dir = os.path.dirname(os.path.abspath(tex_file))
    basename = os.path.basename(tex_file)
    errors = []
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
        # Lọc lỗi thực sự (dòng bắt đầu bằng !)
        errs = [l for l in result.stdout.splitlines() if l.startswith("!")]
        errors.extend(errs)
        if result.returncode != 0 and i == 1:
            print("STDERR:", result.stderr[-500:])
    if errors:
        print("\n[!] Loi LaTeX:")
        for e in set(errors):
            print(" ", e)
    else:
        pdf = os.path.join(work_dir, basename.replace(".tex", ".pdf"))
        print(f"\n[OK] Bien dich thanh cong -> {pdf}")
    return len(errors) == 0

def cmd_compile(args):
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("tex_file")
    parser.add_argument("--dir",   default=None, help="Thư mục làm việc")
    parser.add_argument("--times", type=int, default=2, help="Số lần chạy pdflatex")
    parsed = parser.parse_args(args)
    compile_latex(parsed.tex_file, parsed.dir, parsed.times)


# ===========================================================================
# ENTRY POINT
# ===========================================================================

COMMANDS = {
    "fix":      cmd_fix,
    "images":   cmd_images,
    "assemble": cmd_assemble,
    "shuffle":  cmd_shuffle,
    "compile":  cmd_compile,
}

def main():
    # Đảm bảo stdout hỗ trợ UTF-8 trên Windows
    if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    if len(sys.argv) < 2 or sys.argv[1] not in COMMANDS:
        print(__doc__)
        print("Cac lenh co san:", ", ".join(COMMANDS.keys()))
        sys.exit(0)
    cmd  = sys.argv[1]
    rest = sys.argv[2:]
    COMMANDS[cmd](rest)

if __name__ == "__main__":
    main()
