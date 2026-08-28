# -*- coding: utf-8 -*-
"""Kiểm tra CÚ PHÁP he_thong_bai_tap.json theo JSON Schema trong <SKILL_DIR>/schemas.

Bước kiểm tra *hình thức* (đúng khoá, đúng kiểu dữ liệu). Bước kiểm tra
*nội dung* (đủ nhóm, đủ tầng, đủ lời giải) nằm ở `validate.py`.

Dùng:  python check_schema.py <thư mục chứa json>

Bỏ qua êm nếu chưa cài `jsonschema` (pip install jsonschema).
"""

from __future__ import annotations

import json
import os
import sys

for _s in (sys.stdout, sys.stderr):
    if (getattr(_s, "encoding", "") or "").lower().replace("-", "") not in \
            ("utf8", "utf_8") and hasattr(_s, "reconfigure"):
        try:
            _s.reconfigure(encoding="utf-8", errors="replace")
        except (ValueError, OSError):
            pass

SKILL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCHEMA_DIR = os.path.join(SKILL_DIR, "schemas")

PAIRS = [
    ("he_thong_bai_tap.schema.json", "he_thong_bai_tap.json"),
]


def _load(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def run(folder):
    try:
        from jsonschema import Draft7Validator
    except ImportError:
        print("[BO QUA] chua cai jsonschema (pip install jsonschema)")
        return 0

    errors = 0
    for schema_file, data_file in PAIRS:
        path = os.path.join(folder, data_file)
        if not os.path.exists(path):
            print(f"[LOI] khong tim thay {data_file} trong {folder}")
            errors += 1
            continue
        schema = _load(os.path.join(SCHEMA_DIR, schema_file))
        validator = Draft7Validator(schema)
        errs = sorted(validator.iter_errors(_load(path)),
                      key=lambda e: list(map(str, e.path)))
        if errs:
            errors += len(errs)
            print(f"[LOI] {data_file}: {len(errs)} loi cu phap")
            for e in errs[:15]:
                loc = " / ".join(str(x) for x in e.path) or "(goc)"
                print(f"      {loc}: {e.message}")
        else:
            print(f"[OK]  {data_file} dung cu phap schema")
    return errors


if __name__ == "__main__":
    import warnings

    warnings.filterwarnings("ignore", category=DeprecationWarning)
    folder = sys.argv[1] if len(sys.argv) > 1 else "."
    sys.exit(1 if run(folder) else 0)
