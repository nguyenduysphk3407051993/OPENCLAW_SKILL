# -*- coding: utf-8 -*-
"""Đóng gói skill thành file .zip theo quy ước OpenClaw.

File zip chứa đúng một thư mục gốc trùng tên skill:

    exam-idea.zip
    └── exam-idea/
        ├── SKILL.md
        ├── references/ ...

Dùng:
    python scripts/package.py                 # xuất ra ../exam-idea.zip
    python scripts/package.py -o /tmp/x.zip   # chỉ định nơi lưu
    python scripts/package.py --no-demo       # bỏ thư mục output/ (chỉ khung skill)

Bỏ qua: .git, .venv, __pycache__, .claude, exam-latex-creator, file .zip,
file tạm và các file làm việc ở thư mục gốc (ảnh/docx nguồn, prompt).
"""

from __future__ import annotations

import argparse
import os
import stat
import sys
import zipfile

# Console Windows mặc định là cp1252/cp437 -> in tiếng Việt sẽ ném
# UnicodeEncodeError. Ép UTF-8 để chạy giống nhau trên Windows lẫn Linux.
for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass

SKILL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILL_NAME = os.path.basename(SKILL_DIR)

# Thư mục bỏ qua ở mọi cấp
SKIP_DIRS = {
    ".git", ".venv", "venv", "__pycache__", ".claude", ".idea", ".vscode",
    "node_modules", "exam-latex-creator",
}
# Đuôi file bỏ qua
SKIP_EXT = {".zip", ".pyc", ".pyo", ".log", ".tmp", ".bak"}
# File ở THƯ MỤC GỐC bỏ qua (file làm việc, không thuộc skill)
SKIP_ROOT_FILES = {
    "make_docx.py",
    "prompt_exam_idea_skill.txt",
    "bang_ma_tran.png", "bang_ma_tran.docx",
    "bang_dac_ta_ma_tran.png", "bang_dac_ta_ma_tran.docx",
}
# Cấp quyền thực thi trong zip (quan trọng khi giải nén trên Linux)
EXECUTABLE = {".sh"}


def _skip(rel_path: str, name: str, at_root: bool) -> bool:
    if name.startswith("~$") or name.startswith("._"):
        return True
    if os.path.splitext(name)[1].lower() in SKIP_EXT:
        return True
    if at_root and name in SKIP_ROOT_FILES:
        return True
    return False


def collect(include_demo=True):
    files = []
    for root, dirs, names in os.walk(SKILL_DIR):
        dirs[:] = sorted(d for d in dirs if d not in SKIP_DIRS)
        rel_dir = os.path.relpath(root, SKILL_DIR).replace("\\", "/")
        if rel_dir == ".":
            rel_dir = ""
        if not include_demo and rel_dir.startswith("output"):
            continue
        for name in sorted(names):
            if _skip(rel_dir, name, at_root=(rel_dir == "")):
                continue
            abs_path = os.path.join(root, name)
            rel = f"{rel_dir}/{name}" if rel_dir else name
            files.append((abs_path, rel))
    return files


def build_zip(out_path, include_demo=True):
    files = collect(include_demo)
    out_path = os.path.abspath(out_path)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)

    with zipfile.ZipFile(out_path, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for abs_path, rel in files:
            arc = f"{SKILL_NAME}/{rel}"
            info = zipfile.ZipInfo.from_file(abs_path, arc)
            info.compress_type = zipfile.ZIP_DEFLATED
            mode = 0o755 if os.path.splitext(rel)[1].lower() in EXECUTABLE else 0o644
            info.external_attr = (stat.S_IFREG | mode) << 16
            with open(abs_path, "rb") as f:
                z.writestr(info, f.read())
    return out_path, files


def main():
    ap = argparse.ArgumentParser(description="Đóng gói skill thành .zip")
    ap.add_argument("-o", "--output",
                    default=os.path.join(os.path.dirname(SKILL_DIR),
                                         f"{SKILL_NAME}.zip"),
                    help="Đường dẫn file zip (mặc định: ../<tên skill>.zip)")
    ap.add_argument("--no-demo", action="store_true",
                    help="Không đóng gói thư mục output/ (bộ đề mẫu)")
    args = ap.parse_args()

    out, files = build_zip(args.output, include_demo=not args.no_demo)
    size = os.path.getsize(out)
    print(f"[OK] {out}")
    print(f"     {len(files)} file, {size / 1024:.1f} KB")
    print(f"     thu muc goc trong zip: {SKILL_NAME}/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
