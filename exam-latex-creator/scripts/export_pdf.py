# -*- coding: utf-8 -*-
"""
export_pdf.py — Sửa lỗi LaTeX, biên dịch PDF, xử lý ảnh.

Commands:
  fix       — Sửa lỗi LaTeX phổ biến (dấu chấm, xrightarrow, frac, ...)
  compile   — Biên dịch file .tex thành PDF
  images    — Trích xuất ảnh từ file .docx
  imgpaths  — Chuẩn hóa đường dẫn ảnh trong file .tex

Usage:
  python export_pdf.py <command> [args]
"""
import os
import re
import sys
import json
import subprocess
from difflib import SequenceMatcher

# Fix console encoding on Windows
if sys.platform.startswith('win'):
    import io
    try:
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')
    except AttributeError:
        pass

# ==============================================================================
#                            LATEX FIX ENGINE
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

    # 7. Remove AI citation markers
    processed = re.sub(r'\[cite_start\]', '', processed)
    processed = re.sub(r'\[cite_end\]', '', processed)
    processed = re.sub(r'\[cite[:\s]*[\d,\s]+\]', '', processed)

    # 8. Remove duplicate spaces
    processed = re.sub(r'  +', ' ', processed)

    # 9. Remove trailing dots in choices
    processed = remove_trailing_dot_in_choices(processed)

    # 10. Wrap chemical formulas
    processed = wrap_chem_text_in_equations(processed)

    return processed

# ==============================================================================
#                            COMPILER
# ==============================================================================

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
        print("\n[!] Lỗi biên dịch:")
        for e in set(errors):
            print(" ", e)
    else:
        pdf = os.path.join(work_dir, basename.replace(".tex", ".pdf"))
        print(f"\n[OK] Biên dịch hoàn tất -> {pdf}")
    return len(errors) == 0

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

    manifest_path = os.path.join(output_dir, "image_manifest.json")
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)

    print(f"\nTotal: {image_counter - 1} images -> {output_dir}")
    print(f"Manifest: {manifest_path}")
    return manifest

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
    for w in warnings:
        print(w)
    print(f"[imgpaths] Đã chuẩn hóa {changed} đường dẫn.")
    return result

# ==============================================================================
#                            JUNK FILE CLEANER
# ==============================================================================

JUNK_EXTENSIONS = {
    '.aux', '.log', '.out', '.toc', '.dvi', '.thm',
    '.ilg', '.ind', '.nav', '.snm', '.upa', '.answers'
}


def clean_junk_files(directory, recursive=True):
    """Xóa file rác LaTeX (tương đương XoaFileRac.bat)."""
    removed = 0
    if recursive:
        for root, dirs, files in os.walk(directory):
            for f in files:
                ext = os.path.splitext(f)[1].lower()
                if ext in JUNK_EXTENSIONS:
                    filepath = os.path.join(root, f)
                    try:
                        os.remove(filepath)
                        removed += 1
                    except OSError:
                        pass
    else:
        for f in os.listdir(directory):
            ext = os.path.splitext(f)[1].lower()
            if ext in JUNK_EXTENSIONS:
                filepath = os.path.join(directory, f)
                if os.path.isfile(filepath):
                    try:
                        os.remove(filepath)
                        removed += 1
                    except OSError:
                        pass
    print(f"[clean] Đã xóa {removed} file rác trong: {directory}")
    return removed


# ==============================================================================
#                            COMMAND HANDLERS
# ==============================================================================

def cmd_fix(args):
    import argparse
    parser = argparse.ArgumentParser(description="Sửa lỗi LaTeX phổ biến.")
    parser.add_argument("input_file", help="File LaTeX đầu vào")
    parser.add_argument("output_file", nargs="?", default=None, help="File đầu ra (mặc định ghi đè)")
    parsed = parser.parse_args(args)

    out_path = parsed.output_file if parsed.output_file else parsed.input_file

    with open(parsed.input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    fixed = fix_latex_common_errors(content)

    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(fixed)

    print(f"[fix] Sửa lỗi thành công -> {out_path}")


def cmd_compile(args):
    import argparse
    parser = argparse.ArgumentParser(description="Biên dịch LaTeX thành PDF.")
    parser.add_argument("tex_file", help="File .tex cần biên dịch")
    parser.add_argument("--dir", default=None, help="Thư mục làm việc")
    parser.add_argument("--times", type=int, default=2, help="Số lần chạy pdflatex")
    parser.add_argument("--clean", action="store_true", help="Xóa file rác sau khi biên dịch")
    parsed = parser.parse_args(args)

    work_dir = parsed.dir if parsed.dir else os.path.dirname(os.path.abspath(parsed.tex_file))
    success = compile_latex(parsed.tex_file, work_dir, parsed.times)
    if success and parsed.clean:
        clean_junk_files(work_dir)


def cmd_images(args):
    import argparse
    parser = argparse.ArgumentParser(description="Trích xuất ảnh từ .docx.")
    parser.add_argument("source", help="File .docx nguồn")
    parser.add_argument("output_dir", help="Thư mục lưu ảnh")
    parsed = parser.parse_args(args)

    extract_images_from_docx(parsed.source, parsed.output_dir)


def cmd_imgpaths(args):
    import argparse
    parser = argparse.ArgumentParser(description="Chuẩn hóa đường dẫn ảnh trong .tex.")
    parser.add_argument("tex_file", help="File LaTeX cần xử lý")
    parser.add_argument("--base-dir", default=None, help="Thư mục gốc chứa ảnh")
    parser.add_argument("--inplace", action="store_true", help="Ghi đè file gốc")
    parser.add_argument("--out", default=None, help="File output khác")
    parsed = parser.parse_args(args)

    with open(parsed.tex_file, "r", encoding="utf-8") as f:
        content = f.read()

    new_content = normalize_image_paths_in_tex(
        content, base_dir=parsed.base_dir, tex_file_path=parsed.tex_file
    )

    if parsed.inplace:
        with open(parsed.tex_file, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"[imgpaths] Ghi đè: {parsed.tex_file}")
    elif parsed.out:
        with open(parsed.out, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"[imgpaths] Lưu tại: {parsed.out}")
    else:
        print(new_content)


def cmd_clean(args):
    import argparse
    parser = argparse.ArgumentParser(description="Xóa file rác LaTeX (.aux, .log, .out, ...)")
    parser.add_argument("directory", nargs="?", default=".", help="Thư mục cần dọn (mặc định: thư mục hiện tại)")
    parser.add_argument("--no-recursive", action="store_true", help="Chỉ xóa ở thư mục gốc, không đệ quy")
    parsed = parser.parse_args(args)

    clean_junk_files(parsed.directory, recursive=not parsed.no_recursive)


# ==============================================================================
#                            ENTRY POINT
# ==============================================================================

COMMANDS = {
    "fix": cmd_fix,
    "compile": cmd_compile,
    "clean": cmd_clean,
    "images": cmd_images,
    "imgpaths": cmd_imgpaths,
}

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python export_pdf.py <command> [args]")
        print("Commands:", ", ".join(COMMANDS.keys()))
        sys.exit(1)

    cmd = sys.argv[1]
    if cmd in COMMANDS:
        COMMANDS[cmd](sys.argv[2:])
    else:
        print(f"Lỗi: Lệnh không hợp lệ: {cmd}")
        print("Commands:", ", ".join(COMMANDS.keys()))
        sys.exit(1)
