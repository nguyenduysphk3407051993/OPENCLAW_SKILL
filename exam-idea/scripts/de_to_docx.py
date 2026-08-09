# -*- coding: utf-8 -*-
"""de_bai_tap.json  ->  <tên>.docx  (file "1. Các dạng bài tập")

Bố cục:
  PHẦN A. Mục tiêu cần đạt        (Bước 1)
  PHẦN B. Hệ thống các dạng bài tập theo 4 loại câu hỏi   (Bước 2)
  PHẦN C. Đề minh hoạ             (đúng cấu trúc & ma trận)
  PHẦN D. Đáp án – Hướng dẫn chấm

Dùng:  python de_to_docx.py <de_bai_tap.json> [output.docx]
"""

from __future__ import annotations

import sys

from docx_common import load_json, new_doc, para, rich_para, save_doc, title

ABCD = ["A", "B", "C", "D"]
ABCD_Y = ["a", "b", "c", "d"]
TEN_LOAI = {
    1: "Loại 1 – Trắc nghiệm nhiều lựa chọn (4 phương án, chọn 1)",
    2: "Loại 2 – Trắc nghiệm đúng/sai (4 ý a, b, c, d)",
    3: "Loại 3 – Trắc nghiệm trả lời ngắn (đáp án là số)",
    4: "Loại 4 – Tự luận",
}


def _muc_do_ten(cfg, ma):
    for m in cfg.get("cau_hinh", {}).get("muc_do", []):
        if isinstance(m, dict) and m.get("ma") == ma:
            return m["ten"]
    return ma


def _heading(doc, text, size=12, space_before=8):
    para(doc, text, bold=True, size=size, space_before=space_before,
         space_after=3)


# ------------------------------------------------------------------ câu hỏi
def _render_cau(doc, c, cfg, show_dapan=False):
    stt = c.get("stt", "")
    nhan = f"Câu {stt}. " if stt != "" else ""
    meta = []
    if c.get("muc_do"):
        meta.append(_muc_do_ten(cfg, c["muc_do"]))
    if c.get("dang"):
        meta.append(f"dạng {c['dang']}")
    if c.get("diem") is not None:
        meta.append(f"{str(c['diem']).replace('.', ',')} điểm")
    chunks = [(nhan, {"bold": True})]
    chunks.append((c["de"], {}))
    if meta:
        chunks.append(("  [" + "; ".join(meta) + "]", {"italic": True, "size": 9}))
    rich_para(doc, chunks, align="justify", space_before=4)

    loai = c.get("loai")
    if loai == 1:
        opts = c.get("lua_chon", [])
        flat = "   ".join(f"{ABCD[i]}. {o}" for i, o in enumerate(opts))
        if len(flat) <= 95:
            para(doc, flat, indent=0.6)
        else:
            for i, o in enumerate(opts):
                para(doc, f"{ABCD[i]}. {o}", indent=0.6)
    elif loai == 2:
        for i, y in enumerate(c.get("y", [])):
            para(doc, f"{ABCD_Y[i]}) {y['nd']}", indent=0.6)
    elif loai == 4:
        for y in c.get("y", []):
            d = y.get("diem")
            suffix = f"  ({str(d).replace('.', ',')} điểm)" if d else ""
            para(doc, f"{y['nd']}{suffix}", indent=0.6, align="justify")

    if show_dapan:
        _render_dapan(doc, c)


def _render_dapan(doc, c):
    loai = c.get("loai")
    stt = c.get("stt", "")
    if loai == 1:
        rich_para(doc, [(f"Câu {stt}. ", {"bold": True}),
                        (f"Đáp án {c.get('dap_an', '')}. ", {"bold": True}),
                        (c.get("loi_giai", ""), {})], align="justify",
                  space_before=3)
    elif loai == 2:
        kq = ", ".join(f"{ABCD_Y[i]}) {'Đ' if y.get('dap_an') else 'S'}"
                       for i, y in enumerate(c.get("y", [])))
        rich_para(doc, [(f"Câu {stt}. ", {"bold": True}), (kq, {"bold": True})],
                  space_before=3)
        for i, y in enumerate(c.get("y", [])):
            if y.get("giai_thich"):
                para(doc, f"{ABCD_Y[i]}) {y['giai_thich']}", indent=0.6,
                     align="justify")
    elif loai == 3:
        rich_para(doc, [(f"Câu {stt}. ", {"bold": True}),
                        (f"Đáp án: {c.get('dap_an', '')}", {"bold": True}),
                        ("  " + c.get("loi_giai", ""), {})], align="justify",
                  space_before=3)
    elif loai == 4:
        para(doc, f"Câu {stt}.", bold=True, space_before=3)
        for b in c.get("huong_dan_cham", []):
            d = b.get("diem")
            suffix = f"  ({str(d).replace('.', ',')} điểm)" if d else ""
            para(doc, f"{b['nd']}{suffix}", indent=0.6, align="justify")
        if c.get("loi_giai"):
            para(doc, c["loi_giai"], indent=0.6, align="justify")


# ------------------------------------------------------------------ dựng
def build(cfg, out_path):
    doc = new_doc(landscape=False, margin=2.0, base_size=11)
    title(doc, cfg.get("tieu_de", "CÁC DẠNG BÀI TẬP"), size=14)
    ti = cfg.get("thong_tin") or {}
    if ti:
        para(doc, " – ".join(x for x in [
            f"Môn: {ti['mon']}" if ti.get("mon") else None,
            f"Lớp: {ti['lop']}" if ti.get("lop") else None,
            ti.get("chu_de_chung"),
        ] if x), italic=True, align="center", space_after=8)

    # ---- PHẦN A: mục tiêu
    _heading(doc, "PHẦN A. MỤC TIÊU CẦN ĐẠT", size=13, space_before=4)
    for blk in cfg.get("muc_tieu", []):
        para(doc, blk["chu_de"], bold=True, space_before=6)
        for y in blk.get("yeu_cau", []):
            if isinstance(y, str):
                para(doc, f"– {y}", indent=0.5, align="justify")
            else:
                rich_para(doc, [(f"– [{_muc_do_ten(cfg, y['muc_do'])}] ",
                                 {"italic": True, "size": 10}),
                                (y["noi_dung"], {})],
                          indent=0.5, align="justify")

    # ---- PHẦN B: các dạng bài tập
    _heading(doc, "PHẦN B. HỆ THỐNG CÁC DẠNG BÀI TẬP", size=13)
    for blk in cfg.get("dang_bai_tap", []):
        para(doc, TEN_LOAI.get(blk["loai"], blk.get("ten", "")), bold=True,
             space_before=8)
        if blk.get("mo_ta"):
            para(doc, blk["mo_ta"], italic=True, size=10, align="justify")
        for d in blk.get("dang", []):
            rich_para(doc, [(f"Dạng {d['ma']}. ", {"bold": True}),
                            (d["ten"], {"bold": True}),
                            (f"  [{_muc_do_ten(cfg, d['muc_do'])}]"
                             if d.get("muc_do") else "",
                             {"italic": True, "size": 9})],
                      space_before=4, align="justify")
            if d.get("mo_ta"):
                para(doc, d["mo_ta"], indent=0.5, align="justify", size=10.5)
            if d.get("vi_du"):
                rich_para(doc, [("Ví dụ: ", {"italic": True, "bold": True,
                                             "size": 10.5}),
                                (d["vi_du"], {"italic": True, "size": 10.5})],
                          indent=0.5, align="justify")

    # ---- PHẦN C: đề minh hoạ
    dmh = cfg.get("de_minh_hoa")
    if dmh:
        doc.add_page_break()
        _heading(doc, "PHẦN C. ĐỀ MINH HOẠ", size=13, space_before=0)
        if dmh.get("cau_truc"):
            para(doc, dmh["cau_truc"], italic=True, align="justify",
                 space_after=4)
        for phan in dmh.get("phan", []):
            para(doc, phan["ten"], bold=True, space_before=8)
            if phan.get("huong_dan"):
                para(doc, phan["huong_dan"], italic=True, size=10,
                     align="justify")
            for c in phan.get("cau", []):
                c.setdefault("loai", phan.get("loai"))
                _render_cau(doc, c, cfg)

        # ---- PHẦN D: đáp án
        doc.add_page_break()
        _heading(doc, "PHẦN D. ĐÁP ÁN – HƯỚNG DẪN CHẤM", size=13,
                 space_before=0)
        for phan in dmh.get("phan", []):
            para(doc, phan["ten"], bold=True, space_before=8)
            for c in phan.get("cau", []):
                _render_dapan(doc, c)

    save_doc(doc, out_path)
    n = sum(len(p.get("cau", [])) for p in (dmh or {}).get("phan", []))
    return {"so_cau": n}


def main():
    src = sys.argv[1] if len(sys.argv) > 1 else "de_bai_tap.json"
    out = sys.argv[2] if len(sys.argv) > 2 else src.replace(".json", ".docx")
    info = build(load_json(src), out)
    print(f"[OK] {out}  ({info['so_cau']} cau trong de minh hoa)")


if __name__ == "__main__":
    main()
