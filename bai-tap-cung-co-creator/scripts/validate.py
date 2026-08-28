# -*- coding: utf-8 -*-
"""Kiểm tra NỘI DUNG he_thong_bai_tap.json.

Bắt đúng những lỗi mà JSON Schema không bắt được:
  1. Mã dạng trùng nhau
  2. Bỏ nhóm A-I mà không khai lí do trong `nhom_bo_qua`
  3. Nhóm vừa có dạng vừa khai bỏ (mâu thuẫn)
  4. `muc_tieu_lien_quan` trỏ tới mục tiêu không tồn tại
  5. Mục tiêu không được dạng nào phủ (cảnh báo)
  6. Bài tập thiếu lời giải / đáp án (chuỗi rỗng, "TODO", "...")
  7. Tầng khai trong cau_hinh.tang nhưng không có bài nào
  8. Dạng chỉ có 1 tầng duy nhất trong khi cau_hinh.tang có >= 3 tầng (cảnh báo)
  9. Bài trắc nghiệm thiếu phương án
 10. `lo_trinh` trỏ tới mã dạng không tồn tại
 11. Mức độ của bài lệch quá xa so với tầng (VDC ở tầng 1, NB ở tầng 4)

Dùng:  python validate.py <thư mục chứa json>
Exit code 1 nếu có LOI (cảnh báo không làm fail).
"""

from __future__ import annotations

import os
import sys

from docx_common import MUC_DO, NHOM, load_json

TAT_CA_NHOM = list(NHOM.keys())
RONG = {"", "todo", "...", "tbd", "chua co", "chưa có", "n/a"}

# tầng -> các mức độ chấp nhận được
TANG_MUC_DO = {
    1: {"NB", "TH"},
    2: {"NB", "TH", "VD"},
    3: {"TH", "VD", "VDC"},
    4: {"VD", "VDC"},
}


def _rong(s):
    return str(s or "").strip().lower() in RONG


def run(folder):
    path = os.path.join(folder, "he_thong_bai_tap.json")
    if not os.path.exists(path):
        print(f"[LOI] khong tim thay he_thong_bai_tap.json trong {folder}")
        return 1

    d = load_json(path)
    cfg = d.get("cau_hinh", {})
    muc_tieu = d.get("muc_tieu", [])
    dangs = d.get("dang_bai_tap", [])
    bo_qua = {x["nhom"]: x["ly_do"] for x in d.get("nhom_bo_qua", [])}

    loi, canh_bao = [], []

    # 1. mã dạng trùng
    ma_dang = [x["ma"] for x in dangs]
    trung = {m for m in ma_dang if ma_dang.count(m) > 1}
    for m in sorted(trung):
        loi.append(f"ma dang '{m}' bi trung {ma_dang.count(m)} lan")

    # 2 + 3. phủ nhóm
    co_dang = {x["nhom"] for x in dangs}
    for n in TAT_CA_NHOM:
        if n not in co_dang and n not in bo_qua:
            loi.append(f"nhom {n} ({NHOM[n]}) khong co dang nao "
                       f"va khong khai li do trong 'nhom_bo_qua'")
        if n in co_dang and n in bo_qua:
            loi.append(f"nhom {n} vua co dang vua khai bo qua - mau thuan")

    # 4 + 5. mục tiêu
    ma_mt = {x["ma"] for x in muc_tieu}
    da_dung_mt = set()
    for x in dangs:
        for mt in x.get("muc_tieu_lien_quan", []):
            if mt not in ma_mt:
                loi.append(f"dang {x['ma']}: muc tieu '{mt}' khong ton tai")
            else:
                da_dung_mt.add(mt)
    for mt in sorted(ma_mt - da_dung_mt):
        canh_bao.append(f"muc tieu {mt} khong duoc dang bai tap nao phu")

    # 6 + 9 + 11. từng bài tập
    tang_co_bai = set()
    for x in dangs:
        bts = x.get("bai_tap", [])
        tang_trong_dang = set()
        for i, bt in enumerate(bts, 1):
            nhan = f"dang {x['ma']} bai {bt.get('ma') or i}"
            if _rong(bt.get("de")):
                loi.append(f"{nhan}: de trong")
            if _rong(bt.get("loi_giai")):
                loi.append(f"{nhan}: thieu loi giai")
            if _rong(bt.get("dap_an")):
                loi.append(f"{nhan}: thieu dap an")
            t = bt.get("tang")
            if t:
                tang_co_bai.add(int(t))
                tang_trong_dang.add(int(t))
            md = bt.get("muc_do")
            if md and t and md not in TANG_MUC_DO.get(int(t), set()):
                canh_bao.append(
                    f"{nhan}: muc do {md} ({MUC_DO.get(md, md)}) "
                    f"khong hop voi tang {t}")
            if bt.get("hinh_thuc") == "trac_nghiem":
                pa = bt.get("phuong_an") or []
                if len(pa) < 4:
                    loi.append(f"{nhan}: bai trac nghiem can du 4 phuong an "
                               f"(dang co {len(pa)})")

        # 8. dạng chỉ một tầng
        khai_tang = cfg.get("tang") or [1, 2, 3, 4]
        if len(khai_tang) >= 3 and len(tang_trong_dang) == 1:
            canh_bao.append(f"dang {x['ma']} chi co bai o 1 tang - "
                            f"chua phan tang cho moi doi tuong")

    # 7. tầng khai nhưng không có bài
    for t in cfg.get("tang", []):
        if int(t) not in tang_co_bai:
            loi.append(f"tang {t} duoc khai trong cau_hinh nhung khong co bai nao")

    # 10. lộ trình
    tap_ma = set(ma_dang)
    for lt in d.get("lo_trinh", []):
        for m in lt.get("dang", []):
            if m not in tap_ma:
                loi.append(f"lo_trinh buoi {lt.get('buoi')}: "
                           f"ma dang '{m}' khong ton tai")

    # ------------------------------------------------------------ báo cáo
    tong_bai = sum(len(x.get("bai_tap", [])) for x in dangs)
    print(f"Chu de : {cfg.get('mon')} {cfg.get('lop')} - {cfg.get('chu_de')}")
    print(f"Muc tieu: {len(muc_tieu)} | Dang: {len(dangs)} | Bai tap: {tong_bai}")
    print("Phu nhom: " + " ".join(
        f"{n}{'+' if n in co_dang else ('-' if n in bo_qua else '!')}"
        for n in TAT_CA_NHOM) + "   (+ co dang, - bo co li do, ! THIEU)")
    dem_tang = {t: 0 for t in (1, 2, 3, 4)}
    for x in dangs:
        for bt in x.get("bai_tap", []):
            if bt.get("tang"):
                dem_tang[int(bt["tang"])] = dem_tang.get(int(bt["tang"]), 0) + 1
    print("Theo tang: " + " | ".join(f"tang {t}: {c} bai"
                                     for t, c in sorted(dem_tang.items())))
    print()

    for c in canh_bao:
        print(f"[CANH BAO] {c}")
    for e in loi:
        print(f"[LOI] {e}")
    if not loi:
        print("[OK]  he_thong_bai_tap.json dong bo, khong co loi")
    return len(loi)


if __name__ == "__main__":
    folder = sys.argv[1] if len(sys.argv) > 1 else "."
    sys.exit(1 if run(folder) else 0)
