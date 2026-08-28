# -*- coding: utf-8 -*-
"""he_thong_bai_tap.json  ->  file Word .docx

Sinh 2 bản:
  * bản HS  (kem_loi_giai=False): chỉ đề bài, có chừa chỗ làm bài
  * bản GV  (kem_loi_giai=True) : đầy đủ phương pháp giải, lời giải, đáp án

Dùng trực tiếp:
    python bai_tap_to_docx.py <thu_muc> [--hs | --gv]
"""

from __future__ import annotations

import os
import sys

from docx_common import (MUC_DO, NHOM, apply_widths, heading, load_json, new_doc,
                         page_break, para, repeat_header, rich_para, sao,
                         save_doc, set_borders, set_fixed_layout, shade, title,
                         write)

CHU_CAI = ["A", "B", "C", "D", "E", "F"]


def _tieu_de(doc, d):
    cfg = d["cau_hinh"]
    title(doc, "HỆ THỐNG BÀI TẬP CỦNG CỐ KIẾN THỨC", size=15, space_after=2)
    title(doc, str(cfg["chu_de"]).upper(), size=14, space_after=2)
    para(doc, f"Môn {cfg['mon']} — Lớp {cfg['lop']}"
         + (f" — {cfg['bo_sach']}" if cfg.get("bo_sach") else ""),
         align="center", italic=True, size=12, space_after=10)


def _bang_muc_tieu(doc, d):
    heading(doc, "I. MỤC TIÊU CẦN ĐẠT")
    t = doc.add_table(rows=1, cols=3)
    set_borders(t)
    set_fixed_layout(t)
    hdr = t.rows[0]
    repeat_header(hdr)
    for i, (txt, w) in enumerate((("Mã", 1.4), ("Mục tiêu", 12.8), ("Mức độ", 2.8))):
        write(hdr.cells[i], txt, bold=True, size=11)
        shade(hdr.cells[i], "DCE6F1")
    for mt in d["muc_tieu"]:
        r = t.add_row()
        write(r.cells[0], mt["ma"], size=11)
        write(r.cells[1], mt["noi_dung"], align="left", size=11, valign="top")
        write(r.cells[2], MUC_DO.get(mt["muc_do"], mt["muc_do"]), size=11)
    apply_widths(t, [1.4, 12.8, 2.8])
    para(doc, "", space_after=6)


def _bang_ban_do(doc, d):
    heading(doc, "II. BẢN ĐỒ CÁC DẠNG BÀI TẬP")
    bo_qua = {x["nhom"]: x["ly_do"] for x in d.get("nhom_bo_qua", [])}
    t = doc.add_table(rows=1, cols=4)
    set_borders(t)
    set_fixed_layout(t)
    hdr = t.rows[0]
    repeat_header(hdr)
    for i, txt in enumerate(("Nhóm", "Mã", "Tên dạng", "Số bài / tầng")):
        write(hdr.cells[i], txt, bold=True, size=11)
        shade(hdr.cells[i], "DCE6F1")
    for nhom, ten_nhom in NHOM.items():
        ds = [x for x in d["dang_bai_tap"] if x["nhom"] == nhom]
        if not ds:
            r = t.add_row()
            write(r.cells[0], f"{nhom}. {ten_nhom}", align="left", size=10,
                  valign="top")
            c = r.cells[1].merge(r.cells[3])
            write(c, "Không sử dụng — " + bo_qua.get(nhom, "(chưa nêu lí do)"),
                  align="left", italic=True, size=10, valign="top")
            continue
        for k, x in enumerate(ds):
            r = t.add_row()
            write(r.cells[0], f"{nhom}. {ten_nhom}" if k == 0 else "",
                  align="left", size=10, valign="top")
            write(r.cells[1], x["ma"], size=10, valign="top")
            write(r.cells[2], x["ten"], align="left", size=10, valign="top")
            tang = sorted({int(b["tang"]) for b in x["bai_tap"]})
            write(r.cells[3],
                  f"{len(x['bai_tap'])} bài / tầng " + ",".join(map(str, tang)),
                  size=10, valign="top")
    apply_widths(t, [4.6, 1.4, 8.0, 3.0])
    para(doc, "", space_after=6)


def _bai(doc, bt, so, kem_loi_giai):
    rich_para(doc, [
        (f"Bài {so}. ", {"bold": True}),
        (f"[{sao(bt['tang'])}"
         + (f" · {MUC_DO.get(bt.get('muc_do'), '')}" if bt.get("muc_do") else "")
         + "] ", {"italic": True, "size": 10}),
        (bt["de"], {}),
    ], align="justify", space_before=4, indent=0.5)
    for i, pa in enumerate(bt.get("phuong_an", [])):
        para(doc, f"{CHU_CAI[i]}. {pa}", indent=1.2, size=12, space_after=1)
    if kem_loi_giai:
        para(doc, "Lời giải: " + bt["loi_giai"], italic=True, indent=1.0,
             align="justify", size=11, space_before=2)
        rich_para(doc, [("Đáp án: ", {"bold": True, "size": 11}),
                        (bt["dap_an"], {"bold": True, "size": 11})],
                  indent=1.0, space_after=4)
    else:
        para(doc, "", space_after=10)


def _dang(doc, x, kem_loi_giai):
    heading(doc, f"Dạng {x['ma']} — {x['ten']}", size=12.5, space_before=12)
    para(doc, f"Nhóm {x['nhom']}: {NHOM[x['nhom']]}"
         + ("   |   Mục tiêu: " + ", ".join(x["muc_tieu_lien_quan"])
            if x.get("muc_tieu_lien_quan") else ""),
         italic=True, size=10, space_after=4)

    if kem_loi_giai:
        if x.get("dau_hieu_nhan_biet"):
            rich_para(doc, [("Dấu hiệu nhận biết: ", {"bold": True, "size": 11}),
                            (x["dau_hieu_nhan_biet"], {"size": 11})],
                      align="justify")
        para(doc, "Phương pháp giải:", bold=True, size=11, space_before=2)
        for i, b in enumerate(x["phuong_phap"], 1):
            para(doc, f"{i}. {b}", indent=0.8, size=11, space_after=1)
        if x.get("loi_thuong_gap"):
            para(doc, "Lỗi thường gặp:", bold=True, size=11, space_before=3)
            for b in x["loi_thuong_gap"]:
                para(doc, f"– {b}", indent=0.8, size=11, space_after=1)
        if x.get("luu_y"):
            para(doc, "Lưu ý: " + x["luu_y"], italic=True, size=11,
                 space_before=3, align="justify")
        para(doc, "Bài tập:", bold=True, size=11, space_before=5)
    else:
        para(doc, "Phương pháp giải:", bold=True, size=11, space_before=2)
        for i, b in enumerate(x["phuong_phap"], 1):
            para(doc, f"{i}. {b}", indent=0.8, size=11, space_after=1)
        para(doc, "Bài tập:", bold=True, size=11, space_before=5)

    for i, bt in enumerate(sorted(x["bai_tap"], key=lambda b: int(b["tang"])), 1):
        _bai(doc, bt, i, kem_loi_giai)


def _lo_trinh(doc, d):
    lt = d.get("lo_trinh")
    if not lt:
        return
    heading(doc, "IV. LỘ TRÌNH LUYỆN TẬP GỢI Ý", space_before=14)
    t = doc.add_table(rows=1, cols=5)
    set_borders(t)
    set_fixed_layout(t)
    hdr = t.rows[0]
    repeat_header(hdr)
    for i, txt in enumerate(("Buổi", "Nội dung", "Dạng", "Số bài", "Mốc đánh giá")):
        write(hdr.cells[i], txt, bold=True, size=11)
        shade(hdr.cells[i], "DCE6F1")
    for b in lt:
        r = t.add_row()
        write(r.cells[0], b["buoi"], size=10)
        write(r.cells[1], b.get("ten", ""), align="left", size=10, valign="top")
        write(r.cells[2], ", ".join(b["dang"]), size=10, valign="top")
        write(r.cells[3], b.get("so_bai", ""), size=10)
        write(r.cells[4], b.get("moc_danh_gia", ""), align="left", size=10,
              valign="top")
    apply_widths(t, [1.3, 5.0, 2.6, 1.4, 6.7])


def build(data, out_path, kem_loi_giai=True):
    doc = new_doc(landscape=False, base_size=12)
    _tieu_de(doc, data)
    para(doc, "BẢN DÀNH CHO GIÁO VIÊN — có phương pháp giải, lời giải và đáp án"
         if kem_loi_giai else
         "BẢN DÀNH CHO HỌC SINH — tự làm rồi đối chiếu với bản đáp án",
         align="center", bold=True, size=11, space_after=10)
    _bang_muc_tieu(doc, data)
    _bang_ban_do(doc, data)
    page_break(doc)
    heading(doc, "III. HỆ THỐNG DẠNG BÀI TẬP CHI TIẾT", space_before=0)
    for x in sorted(data["dang_bai_tap"], key=lambda y: (y["nhom"], y["ma"])):
        _dang(doc, x, kem_loi_giai)
    _lo_trinh(doc, data)
    save_doc(doc, out_path)
    tong = sum(len(x["bai_tap"]) for x in data["dang_bai_tap"])
    return f"({len(data['dang_bai_tap'])} dang, {tong} bai)"


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    folder = os.path.abspath(args[0]) if args else os.getcwd()
    data = load_json(os.path.join(folder, "he_thong_bai_tap.json"))
    gv = "--hs" not in sys.argv
    suffix = "GV" if gv else "HS"
    out = os.path.join(folder, f"He_thong_bai_tap_{suffix}.docx")
    print(build(data, out, kem_loi_giai=gv), "->", out)


if __name__ == "__main__":
    main()
