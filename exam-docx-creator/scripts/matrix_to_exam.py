# -*- coding: utf-8 -*-
"""Cầu nối exam-idea → exam-docx-creator.

Nhận `bang_ma_tran.json` do skill exam-idea sinh ra, bung thành kế hoạch ra đề,
dựng khung markdown đúng format của `build_exam_docx.py`, và đối chiếu ngược file
markdown đã điền với ma trận.

    python matrix_to_exam.py plan     bang_ma_tran.json -o plan.json
    python matrix_to_exam.py skeleton plan.json -o de.md
    python matrix_to_exam.py verify   bang_ma_tran.json de.md

Đơn vị đếm của ma trận là LỆNH HỎI, không phải câu: loại 1 và loại 3 mỗi câu 1
lệnh hỏi, loại 2 mỗi câu 4 ý, loại 4 mỗi câu 2 ý (đọc từ `so_y_moi_cau`).
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys

# Console Windows mặc định không phải UTF-8 -> in tiếng Việt sẽ vỡ.
# Ép UTF-8 cho stdout/stderr, chạy giống nhau trên Windows lẫn Linux.
for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):  # stream bị wrap hoặc đã đóng
        pass

ROMAN = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII"]
NHAN_Y = "abcdefgh"

RE_CAU = re.compile(r"^\s*(Câu|Bài)\s+(\d+)\s*[.):]", re.IGNORECASE)
RE_PHAN = re.compile(r"^\s*#{1,3}\s*Phần\b", re.IGNORECASE)
RE_Y = re.compile(r"^\s*([a-h])\s*[.)]\s*\S")
RE_PA = re.compile(r"^\s*([A-D])\s*[.)]\s*\S")
RE_LOI_GIAI = re.compile(r"^\s*(Lời giải|Hướng dẫn giải|Đáp án)\s*[.:]", re.IGNORECASE)


def load_json(path):
    # utf-8-sig: nuốt luôn BOM nếu file được soạn/lưu lại bằng Notepad trên Windows
    with open(path, "r", encoding="utf-8-sig") as f:
        return json.load(f)


def ghi_file(path, noi_dung):
    """Ghi UTF-8, xuống dòng LF trên mọi hệ điều hành."""
    thu_muc = os.path.dirname(os.path.abspath(path))
    os.makedirs(thu_muc, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(noi_dung)


def fmt_diem(x):
    """0.25 -> '0,25' ; 1.0 -> '1,0'."""
    s = f"{float(x):.2f}".rstrip("0").rstrip(".")
    if "." not in s:
        s += ",0"
        return s.replace(".", ",")
    return s.replace(".", ",")


def get_muc_do(cfg):
    out = []
    for m in cfg["cau_hinh"]["muc_do"]:
        if isinstance(m, str):
            out.append({"ma": m, "ten": m, "ten_ngan": m})
        else:
            out.append({"ma": m.get("ma", m["ten"]), "ten": m["ten"],
                        "ten_ngan": m.get("ten_ngan", m["ten"])})
    return out


# ------------------------------------------------------------------ plan
def build_plan(mt, nguon=None):
    """Bung ma trận thành danh sách câu hỏi, gom lệnh hỏi thành câu."""
    muc_do = get_muc_do(mt)
    ten_muc_do = {m["ma"]: m["ten"] for m in muc_do}
    nhom = mt["cau_hinh"]["nhom_cau_hoi"]
    canh_bao = []
    phan = []

    for g in nhom:
        ma_g = g["ma"]
        so_y = int(g.get("so_y_moi_cau") or 1)
        # 1. gom mọi lệnh hỏi của nhóm này theo thứ tự chủ đề → đơn vị → mức độ
        lenh = []
        for cd in mt["chu_de"]:
            for nd in cd["noi_dung"]:
                o = (nd.get("so_lenh_hoi") or {}).get(ma_g) or {}
                d_o = (nd.get("diem") or {}).get(ma_g) or {}
                for m in muc_do:
                    n = int(o.get(m["ma"]) or 0)
                    if not n:
                        continue
                    # `diem` khai báo trong ma trận là điểm của CẢ Ô -> chia đều
                    if m["ma"] in d_o:
                        d_lenh = float(d_o[m["ma"]]) / n
                    else:
                        d_lenh = float(g.get("diem_moi_lenh") or 0)
                    for _ in range(n):
                        lenh.append({"chu_de": cd["ten"], "don_vi": nd["ten"],
                                     "muc_do": m["ma"],
                                     "muc_do_ten": ten_muc_do[m["ma"]],
                                     "diem": d_lenh})

        if len(lenh) % so_y:
            canh_bao.append(
                f"Nhóm {g['ten']}: {len(lenh)} lệnh hỏi không chia hết cho "
                f"{so_y} ý/câu — ma trận cần sửa lại")

        # 2. cắt thành câu
        cau = []
        for i in range(0, len(lenh), so_y):
            khoi = lenh[i:i + so_y]
            for k, y in enumerate(khoi):
                y["nhan"] = NHAN_Y[k] if so_y > 1 else None
            don_vi = {y["don_vi"] for y in khoi}
            if len(don_vi) > 1:
                canh_bao.append(
                    f"Nhóm {g['ten']} câu {len(cau) + 1}: các ý rơi vào "
                    f"{len(don_vi)} đơn vị kiến thức khác nhau "
                    f"({' | '.join(sorted(don_vi))})")
            cau.append({"stt": len(cau) + 1,
                        "y": khoi,
                        "diem": round(sum(y["diem"] for y in khoi), 4)})

        so_cau_khai_bao = g.get("so_cau")
        if so_cau_khai_bao is not None and len(cau) != int(so_cau_khai_bao):
            canh_bao.append(
                f"Nhóm {g['ten']}: ma trận cho ra {len(cau)} câu nhưng "
                f"cau_hinh khai báo so_cau = {so_cau_khai_bao}")

        phan.append({"ma": ma_g, "ten": g["ten"], "loai": g.get("loai"),
                     "nhom_cha": g.get("nhom_cha"), "so_y_moi_cau": so_y,
                     "so_cau": len(cau), "so_lenh_hoi": len(lenh),
                     "diem": round(sum(c["diem"] for c in cau), 4),
                     "cau": cau})

    return {"nguon": nguon,
            "thong_tin": mt.get("thong_tin", {}),
            "muc_do": muc_do,
            "tong_diem": float(mt["cau_hinh"].get("tong_diem", 10)),
            "ty_le_muc_tieu": mt["cau_hinh"].get("ty_le_muc_tieu"),
            "phan": phan,
            "canh_bao": canh_bao}


# -------------------------------------------------------------- skeleton
HUONG_DAN = {
    1: "Mỗi câu hỏi thí sinh chỉ chọn một phương án.",
    2: "Trong mỗi ý a), b), c), d) ở mỗi câu, thí sinh chọn đúng hoặc sai.",
    3: "Thí sinh trả lời từ câu 1 đến câu {n}.",
    4: "Thí sinh trình bày lời giải vào giấy làm bài.",
}


def khung_cau(p, c):
    """Markdown khung cho một câu, kèm chú thích HTML (pandoc tự bỏ)."""
    loai = p["loai"]
    nhan_cau = "Bài" if loai == 4 else "Câu"
    out = []
    y0 = c["y"][0]
    out.append(f"<!-- Chủ đề: {y0['chu_de']} -->")
    out.append(f"<!-- Đơn vị kiến thức: {y0['don_vi']} -->")
    if p["so_y_moi_cau"] == 1:
        out.append(f"<!-- Mức độ: {y0['muc_do_ten']} "
                   f"| Điểm: {fmt_diem(c['diem'])} -->")
    else:
        out.append(f"<!-- Điểm cả câu: {fmt_diem(c['diem'])} -->")

    out.append(f"{nhan_cau} {c['stt']}. TODO — nội dung câu hỏi")
    out.append("")

    if loai == 1:
        for pa in "ABCD":
            out.append(f"{pa}. TODO")
        out.append("")
        out.append("Lời giải.")
        out.append("")
        out.append("- TODO — giải thích")
        out.append("")
        out.append("Đáp án.")
        out.append("")
        out.append("Chọn A")
    elif loai == 3:
        out.append("Lời giải.")
        out.append("")
        out.append("- TODO — các bước tính")
        out.append("")
        out.append("Đáp án.")
        out.append("")
        out.append("TODO")
    else:
        for y in c["y"]:
            out.append(f"{y['nhan']}) TODO — {y['muc_do_ten']}")
        out.append("")
        out.append("Lời giải.")
        out.append("")
        for y in c["y"]:
            if loai == 2:
                out.append(f"{y['nhan']}) Đúng. TODO")
            else:
                out.append(f"- {y['nhan']}) TODO "
                           f"({y['muc_do_ten']}, {fmt_diem(y['diem'])} điểm)")
    out.append("")
    return out


def build_skeleton(plan, tieu_de=None):
    tt = plan.get("thong_tin", {})
    md = []
    md.append(f"# {tieu_de or 'ĐỀ KIỂM TRA ĐỊNH KÌ'}")
    md.append("")
    dong = []
    if tt.get("mon"):
        dong.append(f"**Môn:** {tt['mon']}")
    if tt.get("lop"):
        dong.append(f"**Lớp:** {tt['lop']}")
    if tt.get("thoi_gian"):
        dong.append(f"**Thời gian:** {tt['thoi_gian']}")
    meta = []
    if dong:
        meta.append(" - ".join(dong))
    if tt.get("hinh_thuc"):
        meta.append(f"**Hình thức:** {tt['hinh_thuc']}")
    if tt.get("chu_de_chung"):
        meta.append(f"**Chủ đề:** {tt['chu_de_chung']}")
    # hai dấu cách cuối dòng = ngắt dòng cứng, tránh pandoc gộp thành một đoạn
    md.extend(x + "  " for x in meta)
    md.append("")

    for i, p in enumerate(plan["phan"]):
        if not p["cau"]:
            continue
        md.append(f"## Phần {ROMAN[i]}. {p['ten']}")
        md.append("")
        hd = HUONG_DAN.get(p["loai"])
        if hd:
            md.append(f"*{hd.format(n=p['so_cau'])} "
                      f"({p['so_cau']} câu / {p['so_lenh_hoi']} lệnh hỏi / "
                      f"{fmt_diem(p['diem'])} điểm)*")
            md.append("")
        for c in p["cau"]:
            md.extend(khung_cau(p, c))
    return "\n".join(md).rstrip() + "\n"


# ---------------------------------------------------------------- verify
def doc_de_markdown(path):
    """Đọc markdown đề -> danh sách phần, mỗi phần là list câu.

    Mỗi câu: {'nhan','stt','so_y','so_pa'} — chỉ đếm ý/phương án nằm trong phần
    đề bài, tức là trước dòng 'Lời giải.' của chính câu đó.
    """
    with open(path, "r", encoding="utf-8-sig") as f:
        lines = f.read().splitlines()

    phan, cau_ht, trong_loi_giai = [], None, False

    def dong_cau():
        if cau_ht is not None:
            if not phan:
                phan.append([])
            phan[-1].append(cau_ht)

    for raw in lines:
        line = re.sub(r"<!--.*?-->", "", raw)
        if RE_PHAN.match(line):
            dong_cau()
            cau_ht, trong_loi_giai = None, False
            phan.append([])
            continue
        m = RE_CAU.match(line)
        if m:
            dong_cau()
            cau_ht = {"nhan": m.group(1), "stt": int(m.group(2)),
                      "so_y": 0, "so_pa": 0}
            trong_loi_giai = False
            continue
        if cau_ht is None:
            continue
        if RE_LOI_GIAI.match(line):
            trong_loi_giai = True
            continue
        if trong_loi_giai:
            continue
        if RE_PA.match(line):
            cau_ht["so_pa"] += 1
        elif RE_Y.match(line):
            cau_ht["so_y"] += 1

    dong_cau()
    return [p for p in phan if p]


def verify(mt, md_path):
    plan = build_plan(mt)
    mong = [p for p in plan["phan"] if p["cau"]]
    thuc = doc_de_markdown(md_path)
    loi, ok = [], []

    for w in plan["canh_bao"]:
        loi.append(f"Ma trận: {w}")

    if len(thuc) != len(mong):
        loi.append(f"Đề có {len(thuc)} phần, ma trận yêu cầu {len(mong)} phần "
                   f"({', '.join(p['ten'] for p in mong)})")

    tong_lenh_mong = tong_lenh_thuc = 0
    for i, p in enumerate(mong):
        ten = p["ten"]
        tong_lenh_mong += p["so_lenh_hoi"]
        if i >= len(thuc):
            loi.append(f"Thiếu hẳn phần {i + 1} — {ten}")
            continue
        cau = thuc[i]
        if len(cau) != p["so_cau"]:
            loi.append(f"Phần {ROMAN[i]} ({ten}): đề có {len(cau)} câu, "
                       f"ma trận yêu cầu {p['so_cau']} câu")

        so_y = p["so_y_moi_cau"]
        lenh = 0
        for c in cau:
            n_y = c["so_y"] if c["so_y"] else 1
            lenh += n_y
            if so_y > 1 and c["so_y"] != so_y:
                loi.append(f"Phần {ROMAN[i]} ({ten}) câu {c['stt']}: có "
                           f"{c['so_y']} ý, cần đúng {so_y} ý")
            if p["loai"] == 1 and c["so_pa"] != 4:
                loi.append(f"Phần {ROMAN[i]} ({ten}) câu {c['stt']}: có "
                           f"{c['so_pa']} phương án, cần đúng 4 (A–D)")
        tong_lenh_thuc += lenh
        if lenh != p["so_lenh_hoi"]:
            loi.append(f"Phần {ROMAN[i]} ({ten}): đề có {lenh} lệnh hỏi, "
                       f"ma trận yêu cầu {p['so_lenh_hoi']}")
        else:
            ok.append(f"Phần {ROMAN[i]} {ten:<18} {len(cau)} câu / "
                      f"{lenh} lệnh hỏi / {fmt_diem(p['diem'])} điểm — khớp")

    if tong_lenh_thuc == tong_lenh_mong:
        ok.append(f"Tổng cộng {tong_lenh_thuc} lệnh hỏi — khớp ma trận")
    tong_diem = sum(p["diem"] for p in mong)
    if abs(tong_diem - plan["tong_diem"]) > 1e-6:
        loi.append(f"Ma trận: tổng điểm {fmt_diem(tong_diem)} khác "
                   f"{fmt_diem(plan['tong_diem'])}")
    else:
        ok.append(f"Tổng điểm {fmt_diem(tong_diem)}")

    for line in ok:
        print("[OK]  " + line)
    for line in loi:
        print("[LOI] " + line)
    print("-" * 62)
    print(f"Tong so loi: {len(loi)}")
    return len(loi)


# ------------------------------------------------------------------ CLI
def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    p1 = sub.add_parser("plan", help="bảng ma trận -> kế hoạch ra đề (json)")
    p1.add_argument("ma_tran")
    p1.add_argument("-o", "--output", default="plan.json")

    p2 = sub.add_parser("skeleton", help="kế hoạch (hoặc ma trận) -> khung .md")
    p2.add_argument("nguon", help="plan.json hoặc bang_ma_tran.json")
    p2.add_argument("-o", "--output", default="de_khung.md")
    p2.add_argument("--tieu-de", default=None)

    p3 = sub.add_parser("verify", help="đối chiếu file .md với ma trận")
    p3.add_argument("ma_tran")
    p3.add_argument("markdown")

    a = ap.parse_args()

    if a.cmd == "plan":
        plan = build_plan(load_json(a.ma_tran), os.path.abspath(a.ma_tran))
        ghi_file(a.output, json.dumps(plan, ensure_ascii=False, indent=2) + "\n")
        for p in plan["phan"]:
            print(f"  {p['ten']:<18} {p['so_cau']} câu / "
                  f"{p['so_lenh_hoi']} lệnh hỏi / {fmt_diem(p['diem'])} điểm")
        for w in plan["canh_bao"]:
            print("[CB]  " + w)
        print("->", a.output)
        return 0

    if a.cmd == "skeleton":
        raw = load_json(a.nguon)
        plan = raw if "phan" in raw else build_plan(raw, os.path.abspath(a.nguon))
        md = build_skeleton(plan, a.tieu_de)
        ghi_file(a.output, md)
        n = sum(p["so_cau"] for p in plan["phan"])
        print(f"-> {a.output}  ({n} câu, còn TODO cần điền)")
        for w in plan.get("canh_bao", []):
            print("[CB]  " + w)
        return 0

    return verify(load_json(a.ma_tran), a.markdown)


if __name__ == "__main__":
    sys.exit(main())
