# -*- coding: utf-8 -*-
"""Kiểm tra cú pháp 3 file JSON theo JSON Schema trong <SKILL_DIR>/schemas.

Đây là bước kiểm tra *hình thức* (đúng khoá, đúng kiểu dữ liệu). Bước kiểm tra
*nội dung* (đồng bộ ma trận – đặc tả – đề) nằm ở `validate.py`.

Dùng:  python check_schema.py <thư mục chứa json>

Bỏ qua êm nếu chưa cài `jsonschema` (pip install jsonschema).
"""

from __future__ import annotations

import json
import os
import sys

# In được tiếng Việt trên VPS Linux dùng locale C/POSIX
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
    ("bang_ma_tran.schema.json", "bang_ma_tran.json"),
    ("bang_dac_ta.schema.json", "bang_dac_ta_ma_tran.json"),
    ("de_bai_tap.schema.json", "de_bai_tap.json"),
]


def _load(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def _make_validator_factory(store):
    """Trả về hàm tạo validator, tương thích cả jsonschema cũ và mới.

    jsonschema >= 4.18 đánh dấu RefResolver là deprecated (sẽ bỏ ở bản 5) và
    thay bằng thư viện `referencing`. Ưu tiên API mới, tự lùi về API cũ.
    """
    from jsonschema import Draft202012Validator

    try:
        from referencing import Registry, Resource

        registry = Registry().with_resources(
            [(uri, Resource.from_contents(s, default_specification=None))
             for uri, s in store.items() if uri.startswith("exam-idea/")])
        return lambda schema: Draft202012Validator(schema, registry=registry)
    except Exception:
        from jsonschema import RefResolver

        return lambda schema: Draft202012Validator(
            schema, resolver=RefResolver(base_uri="", referrer=schema, store=store))


def run(folder):
    try:
        import jsonschema  # noqa: F401
    except ImportError:
        print("[BO QUA] chua cai jsonschema (pip install jsonschema)")
        return 0

    store = {}
    for fn in os.listdir(SCHEMA_DIR):
        if fn.endswith(".json"):
            s = _load(os.path.join(SCHEMA_DIR, fn))
            store[fn] = s
            if s.get("$id"):
                store[s["$id"]] = s
    make_validator = _make_validator_factory(store)

    errors = 0
    for schema_file, data_file in PAIRS:
        path = os.path.join(folder, data_file)
        if not os.path.exists(path):
            print(f"[BO QUA] khong co {data_file}")
            continue
        validator = make_validator(store[schema_file])
        errs = sorted(validator.iter_errors(_load(path)), key=lambda e: list(e.path))
        if errs:
            errors += len(errs)
            print(f"[LOI] {data_file}: {len(errs)} loi cu phap")
            for e in errs[:10]:
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
