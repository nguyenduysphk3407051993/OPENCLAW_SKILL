# -*- coding: utf-8 -*-
"""Trich xuat anh tu .docx theo dung THU TU XUAT HIEN trong tai lieu.

Ten file xuat: <prefix>_img<NNN>.<ext>  (NNN = so thu tu xuat hien, bat dau 001)
Kem file manifest .txt ghi: so thu tu -> doan van / o bang chua anh do.
"""
import sys
import os
import re
import zipfile
import shutil

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

from docx import Document
from docx.table import Table
from docx.text.paragraph import Paragraph

R_NS = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}"


def iter_block_items(parent):
    from docx.document import Document as _Doc
    from docx.oxml.table import CT_Tbl
    from docx.oxml.text.paragraph import CT_P

    parent_elm = parent.element.body if isinstance(parent, _Doc) else parent._tc
    for child in parent_elm.iterchildren():
        if isinstance(child, CT_P):
            yield Paragraph(child, parent)
        elif isinstance(child, CT_Tbl):
            yield Table(child, parent)


def rids_in_paragraph(p):
    """Lay danh sach r:embed / r:id cua anh trong doan, theo thu tu xuat hien."""
    xml = p._p.xml
    return re.findall(r'r:(?:embed|id)="(rId\d+)"', xml)


def walk(doc, part, out_dir, prefix, counter, manifest, context):
    for blk in iter_block_items(doc if part is None else part):
        if isinstance(blk, Paragraph):
            txt = (blk.text or "").strip()
            for rid in rids_in_paragraph(blk):
                counter[0] += 1
                save_image(part or doc, rid, out_dir, prefix, counter[0],
                           manifest, context, txt)
        else:
            for ri, row in enumerate(blk.rows, 1):
                for ci, cell in enumerate(row.cells, 1):
                    for cp in cell.paragraphs:
                        txt = (cp.text or "").strip()
                        for rid in rids_in_paragraph(cp):
                            counter[0] += 1
                            save_image(cp.part, rid, out_dir, prefix, counter[0],
                                       manifest, f"{context}BANG hang {ri} cot {ci}", txt)


def save_image(part_holder, rid, out_dir, prefix, idx, manifest, context, txt):
    try:
        rel = part_holder.part.rels[rid] if hasattr(part_holder, "part") else part_holder.rels[rid]
    except Exception:
        try:
            rel = part_holder.rels[rid]
        except Exception:
            manifest.append(f"{idx:03d} | KHONG LAY DUOC ({rid}) | {context} | {txt[:80]}")
            return
    if "image" not in rel.reltype:
        return
    blob = rel.target_part.blob
    ext = os.path.splitext(rel.target_part.partname)[1] or ".png"
    name = f"{prefix}_img{idx:03d}{ext}"
    with open(os.path.join(out_dir, name), "wb") as f:
        f.write(blob)
    manifest.append(f"{idx:03d} | {name} | {context} | {txt[:80]}")


def main(src, out_root, prefix):
    out_dir = os.path.join(out_root, prefix)
    os.makedirs(out_dir, exist_ok=True)
    doc = Document(src)
    counter = [0]
    manifest = []
    walk(doc, None, out_dir, prefix, counter, manifest, "")
    mf = os.path.join(out_dir, f"{prefix}_MANIFEST.txt")
    with open(mf, "w", encoding="utf-8") as f:
        f.write("STT | TEN FILE | VI TRI | VAN BAN CUNG DOAN\n")
        f.write("\n".join(manifest))
    print(f"OK: {src} -> {out_dir} ({counter[0]} anh)")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])
