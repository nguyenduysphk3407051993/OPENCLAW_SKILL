# -*- coding: utf-8 -*-
"""Dump nội dung .docx ra text theo đúng thứ tự đoạn văn / bảng.
Hình ảnh không trích xuất, chỉ đánh dấu [[HINH_ANH]] tại vị trí xuất hiện.
"""
import sys
import os

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

from docx import Document
from docx.table import Table
from docx.text.paragraph import Paragraph

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


def iter_block_items(parent):
    from docx.document import Document as _Doc
    from docx.oxml.table import CT_Tbl
    from docx.oxml.text.paragraph import CT_P

    if isinstance(parent, _Doc):
        parent_elm = parent.element.body
    else:
        parent_elm = parent._tc
    for child in parent_elm.iterchildren():
        if isinstance(child, CT_P):
            yield Paragraph(child, parent)
        elif isinstance(child, CT_Tbl):
            yield Table(child, parent)


def para_text(p):
    xml = p._p.xml
    txt = p.text
    n_img = xml.count("<pic:pic") + xml.count("<w:object") + xml.count("v:imagedata")
    marks = ""
    if "<pic:pic" in xml or "v:imagedata" in xml or "<w:object" in xml:
        marks = " [[HINH_ANH]]"
    # ký hiệu toán OMML
    if "m:oMath" in xml:
        marks += " [[OMML_MATH]]"
    return (txt or "").strip() + marks


def cell_text(cell):
    parts = []
    for blk in iter_block_items(cell):
        if isinstance(blk, Paragraph):
            t = para_text(blk)
            if t:
                parts.append(t)
        else:
            parts.append("<<BANG LONG NHAU>>")
    return " / ".join(parts)


def dump(path, out):
    doc = Document(path)
    lines = []
    ti = 0
    for blk in iter_block_items(doc):
        if isinstance(blk, Paragraph):
            t = para_text(blk)
            style = blk.style.name if blk.style is not None else ""
            if t:
                lines.append(f"[P|{style}] {t}")
        else:
            ti += 1
            rows = len(blk.rows)
            cols = len(blk.columns)
            lines.append(f"\n===== BANG {ti} ({rows} hang x {cols} cot) =====")
            for r in blk.rows:
                cells = [cell_text(c) for c in r.cells]
                lines.append(" | ".join(cells))
            lines.append(f"===== HET BANG {ti} =====\n")
    with open(out, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"OK: {path} -> {out} ({len(lines)} dong, {ti} bang)")


if __name__ == "__main__":
    src = sys.argv[1]
    dst = sys.argv[2]
    dump(src, dst)
