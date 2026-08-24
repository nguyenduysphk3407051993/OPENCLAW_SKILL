# -*- coding: utf-8 -*-
"""Trich text nam trong Word TEXT BOX (w:txbxContent) cua file .docx.

python-docx chi duyet paragraph o body nen bo sot toan bo noi dung text box.
Hop "KIEN THUC CAN NHO" cua bo de cuong nay nam trong text box, vi vay phai
doc thang word/document.xml moi lay duoc.
"""
import sys
import re
import zipfile

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")


def boxes_of(path):
    xml = zipfile.ZipFile(path).read("word/document.xml").decode("utf-8")
    return re.findall(r"<w:txbxContent>(.*?)</w:txbxContent>", xml, re.S)


def lines_of(box):
    out = []
    for p in re.findall(r"<w:p[ >].*?</w:p>", box, re.S):
        t = "".join(re.findall(r"<w:t[^>]*>(.*?)</w:t>", p, re.S))
        if t.strip():
            out.append(t.strip())
    return out


def main(src, dst):
    seen = set()
    chunks = []
    for i, box in enumerate(boxes_of(src), 1):
        lines = lines_of(box)
        if not lines:
            continue
        key = "\n".join(lines)
        if key in seen:
            continue
        seen.add(key)
        chunks.append(f"===== BOX {i} =====\n" + key)
    with open(dst, "w", encoding="utf-8") as f:
        f.write("\n\n".join(chunks))
    print(f"OK: {src} -> {dst} ({len(chunks)} box khac nhau)")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
