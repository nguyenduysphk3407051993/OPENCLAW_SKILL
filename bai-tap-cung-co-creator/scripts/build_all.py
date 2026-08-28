# -*- coding: utf-8 -*-
"""Chạy trọn bộ: kiểm tra cú pháp -> kiểm tra nội dung -> xuất 2 file docx.

Dùng:  python build_all.py <thư mục chứa he_thong_bai_tap.json> [--skip-validate]

Đầu vào:  he_thong_bai_tap.json
Đầu ra :  He_thong_bai_tap_HS.docx   (chỉ đề bài)
          He_thong_bai_tap_GV.docx   (có phương pháp giải + lời giải + đáp án)
"""

from __future__ import annotations

import os
import sys

import bai_tap_to_docx
import check_schema
import validate
from docx_common import load_json

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    folder = os.path.abspath(args[0]) if args else os.getcwd()
    skip = "--skip-validate" in sys.argv

    errors = 0
    if not skip:
        print("=" * 62)
        print("KIEM TRA CU PHAP JSON")
        print("=" * 62)
        errors += check_schema.run(folder)
        print()
        print("=" * 62)
        print("KIEM TRA NOI DUNG")
        print("=" * 62)
        errors += validate.run(folder)
        print()

    src = os.path.join(folder, "he_thong_bai_tap.json")
    if not os.path.exists(src):
        print(f"[LOI] khong co he_thong_bai_tap.json trong {folder}")
        return 1
    if errors:
        print(f"*** Con {errors} loi - hay sua JSON roi chay lai. "
              f"Khong xuat docx. ***")
        return 1

    print("=" * 62)
    print("XUAT FILE DOCX")
    print("=" * 62)
    data = load_json(src)
    for suffix, kem in (("HS", False), ("GV", True)):
        out = os.path.join(folder, f"He_thong_bai_tap_{suffix}.docx")
        info = bai_tap_to_docx.build(data, out, kem_loi_giai=kem)
        print(f"[OK] He_thong_bai_tap_{suffix}.docx  {info}")
    return 0


if __name__ == "__main__":
    import warnings

    warnings.filterwarnings("ignore", category=DeprecationWarning)
    sys.exit(main())
