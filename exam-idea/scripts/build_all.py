# -*- coding: utf-8 -*-
"""Chạy trọn bộ: validate -> xuất 3 file docx.

Dùng:  python build_all.py <thư mục chứa json> [--skip-validate]

Đầu vào (trong thư mục):
    de_bai_tap.json
    bang_ma_tran.json
    bang_dac_ta_ma_tran.json

Đầu ra:
    1_Cac_dang_bai_tap.docx
    2_Bang_ma_tran.docx
    3_Bang_dac_ta.docx
"""

from __future__ import annotations

import os
import sys

import check_schema
import dac_ta_to_docx
import de_to_docx
import ma_tran_to_docx
import validate
from docx_common import load_json


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
        print("KIEM TRA DONG BO")
        print("=" * 62)
        errors += validate.run(folder)
        print()

    print("=" * 62)
    print("XUAT FILE DOCX")
    print("=" * 62)
    jobs = [
        ("de_bai_tap.json", "1_Cac_dang_bai_tap.docx", de_to_docx.build),
        ("bang_ma_tran.json", "2_Bang_ma_tran.docx", ma_tran_to_docx.build),
        ("bang_dac_ta_ma_tran.json", "3_Bang_dac_ta.docx", dac_ta_to_docx.build),
    ]
    for src, dst, fn in jobs:
        p = os.path.join(folder, src)
        if not os.path.exists(p):
            print(f"[BO QUA] khong co {src}")
            continue
        out = os.path.join(folder, dst)
        info = fn(load_json(p), out)
        print(f"[OK] {dst}  {info}")

    if errors:
        print(f"\n*** Con {errors} loi dong bo - hay sua JSON roi chay lai ***")
    return 1 if errors else 0


if __name__ == "__main__":
    import warnings

    warnings.filterwarnings("ignore", category=DeprecationWarning)
    sys.exit(main())
