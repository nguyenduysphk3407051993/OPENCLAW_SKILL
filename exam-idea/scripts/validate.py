# -*- coding: utf-8 -*-
"""Kiểm tra tính đồng bộ giữa ma trận – bảng đặc tả – đề minh hoạ.

Dùng:  python validate.py <thư mục chứa 3 file json>

Các phép kiểm tra:
  1. Danh sách chủ đề / đơn vị kiến thức trùng khớp giữa ma trận và đặc tả
  2. Số lệnh hỏi từng ô (đơn vị x nhóm x mức độ) trùng khớp
  3. Tổng điểm = tổng điểm cấu hình (mặc định 10,0)
  4. Tỷ lệ theo mức độ khớp `ty_le_muc_tieu` (nếu khai báo)
  5. Số câu thực tế trong đề minh hoạ khớp ma trận (loại 2 quy đổi theo số ý)
  6. Mọi câu trong đề đều trỏ tới chủ đề/đơn vị kiến thức có thật
"""

from __future__ import annotations

import os
import sys

from docx_common import get_muc_do, get_nhom, load_json

# Console Windows mặc định là cp1252/cp437 -> in tiếng Việt sẽ ném
# UnicodeEncodeError. Ép UTF-8 để chạy giống nhau trên Windows lẫn Linux.
for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass

OK, ERR, WARN = "[OK]  ", "[LOI] ", "[CB]  "


class Report:
    def __init__(self):
        self.lines = []
        self.errors = 0

    def ok(self, msg):
        self.lines.append(OK + msg)

    def err(self, msg):
        self.lines.append(ERR + msg)
        self.errors += 1

    def warn(self, msg):
        self.lines.append(WARN + msg)

    def show(self):
        print("\n".join(self.lines))
        print("-" * 62)
        print(f"Tong so loi: {self.errors}")
        return self.errors


def cells_ma_tran(mt):
    out = {}
    for cd in mt["chu_de"]:
        for nd in cd["noi_dung"]:
            for g, mm in (nd.get("so_lenh_hoi") or {}).items():
                for m, n in mm.items():
                    if n:
                        out[(cd["ten"], nd["ten"], g, m)] = int(n)
    return out


def cells_dac_ta(dt):
    out = {}
    for cd in dt["chu_de"]:
        for nd in cd["noi_dung"]:
            for y in nd.get("yeu_cau_can_dat", []):
                for g, n in (y.get("so_lenh_hoi") or {}).items():
                    if n:
                        k = (cd["ten"], nd["ten"], g, y["muc_do"])
                        out[k] = out.get(k, 0) + int(n)
    return out


def diem_ma_tran(mt):
    """Trả về (diem_theo_muc_do, diem_theo_nhom, tong)."""
    nhom, _ = get_nhom(mt)
    muc_do = get_muc_do(mt)
    dm = {m["ma"]: 0.0 for m in muc_do}
    dg = {g["ma"]: 0.0 for g in nhom}
    for cd in mt["chu_de"]:
        for nd in cd["noi_dung"]:
            for g in nhom:
                for m in muc_do:
                    ex = (nd.get("diem") or {}).get(g["ma"], {}).get(m["ma"])
                    if ex is not None:
                        d = float(ex)
                    else:
                        n = (nd.get("so_lenh_hoi") or {}).get(g["ma"], {}) \
                            .get(m["ma"], 0) or 0
                        d = n * float(g.get("diem_moi_lenh") or 0)
                    dm[m["ma"]] += d
                    dg[g["ma"]] += d
    return dm, dg, sum(dm.values())


def run(folder):
    r = Report()
    p_mt = os.path.join(folder, "bang_ma_tran.json")
    p_dt = os.path.join(folder, "bang_dac_ta_ma_tran.json")
    p_de = os.path.join(folder, "de_bai_tap.json")
    mt, dt = load_json(p_mt), load_json(p_dt)
    de = load_json(p_de) if os.path.exists(p_de) else None

    nhom, _ = get_nhom(mt)
    muc_do = get_muc_do(mt)
    tong_diem = float(mt["cau_hinh"].get("tong_diem", 10))

    # 1. cấu hình
    if [g["ma"] for g in nhom] != [g["ma"] for g in get_nhom(dt)[0]]:
        r.err("Cau hinh nhom cau hoi cua ma tran va dac ta khac nhau")
    else:
        r.ok("Cau hinh nhom cau hoi dong bo")
    if [m["ma"] for m in muc_do] != [m["ma"] for m in get_muc_do(dt)]:
        r.err("Cau hinh muc do cua ma tran va dac ta khac nhau")
    else:
        r.ok(f"Cau hinh muc do dong bo ({len(muc_do)} muc do)")

    # 2. chủ đề / đơn vị kiến thức
    key_mt = [(cd["ten"], nd["ten"]) for cd in mt["chu_de"]
              for nd in cd["noi_dung"]]
    key_dt = [(cd["ten"], nd["ten"]) for cd in dt["chu_de"]
              for nd in cd["noi_dung"]]
    if key_mt != key_dt:
        r.err("Danh sach chu de/don vi kien thuc KHONG khop:")
        for k in key_mt:
            if k not in key_dt:
                r.err(f"    chi co trong ma tran : {k}")
        for k in key_dt:
            if k not in key_mt:
                r.err(f"    chi co trong dac ta  : {k}")
    else:
        r.ok(f"Chu de/don vi kien thuc dong bo ({len(key_mt)} don vi)")

    # 3. từng ô
    a, b = cells_ma_tran(mt), cells_dac_ta(dt)
    diff = [k for k in set(a) | set(b) if a.get(k, 0) != b.get(k, 0)]
    if diff:
        r.err(f"Co {len(diff)} o so lenh hoi lech giua ma tran va dac ta:")
        for k in sorted(diff)[:20]:
            r.err(f"    {k}: ma tran={a.get(k, 0)} / dac ta={b.get(k, 0)}")
    else:
        r.ok(f"So lenh hoi tung o khop hoan toan ({len(a)} o co so lieu)")

    # 4. điểm & tỷ lệ
    dm, dg, tong = diem_ma_tran(mt)
    if abs(tong - tong_diem) > 1e-6:
        r.err(f"Tong diem = {tong} (yeu cau {tong_diem})")
    else:
        r.ok(f"Tong diem = {tong:g}")
    muc_tieu = mt["cau_hinh"].get("ty_le_muc_tieu")
    for m in muc_do:
        pct = dm[m["ma"]] / tong_diem * 100
        if muc_tieu and m["ma"] in muc_tieu:
            want = float(muc_tieu[m["ma"]])
            if abs(pct - want) > 1e-6:
                r.err(f"Ty le {m['ten']} = {pct:g}% (yeu cau {want:g}%)")
            else:
                r.ok(f"Ty le {m['ten']:<16} = {pct:g}%  ({dm[m['ma']]:g} diem)")
        else:
            r.warn(f"Ty le {m['ten']:<16} = {pct:g}%  ({dm[m['ma']]:g} diem)")
    for g in nhom:
        r.warn(f"Nhom  {g['ten']:<16} = {dg[g['ma']]:g} diem")

    # 5. đối chiếu đề minh hoạ
    if de and de.get("de_minh_hoa"):
        want = {}
        for g in nhom:
            want[g["ma"]] = sum(v for (c, n, gg, m), v in a.items() if gg == g["ma"])
        got = {g["ma"]: 0 for g in nhom}
        so_cau_loai = {}
        ma_theo_loai = {g.get("loai"): g["ma"] for g in nhom}
        for phan in de["de_minh_hoa"]["phan"]:
            for c in phan.get("cau", []):
                loai = c.get("loai", phan.get("loai"))
                so_cau_loai[loai] = so_cau_loai.get(loai, 0) + 1
                ma = ma_theo_loai.get(loai)
                if ma is None:
                    continue
                # số lệnh hỏi = số ý nếu câu chia ý (loại 2: 4 ý, loại 4: a/b),
                # ngược lại mỗi câu là 1 lệnh hỏi
                got[ma] += len(c["y"]) if c.get("y") else 1
        for g in nhom:
            n_cau = so_cau_loai.get(g.get("loai"), 0)
            y_moi_cau = g.get("so_y_moi_cau")
            if y_moi_cau and n_cau and got[g["ma"]] != n_cau * y_moi_cau:
                r.err(f"De: nhom {g['ten']} co {n_cau} cau nhung {got[g['ma']]} "
                      f"lenh hoi (can {y_moi_cau} y moi cau)")
            if got[g["ma"]] != want[g["ma"]]:
                r.err(f"De: nhom {g['ten']} co {got[g['ma']]} lenh hoi, "
                      f"ma tran yeu cau {want[g['ma']]}")
            else:
                r.ok(f"De: nhom {g['ten']:<16} {n_cau} cau / "
                     f"{got[g['ma']]} lenh hoi - khop ma tran")
        # 6. tham chiếu chủ đề
        hop_le = {(cd["ten"], nd["ten"]) for cd in mt["chu_de"]
                  for nd in cd["noi_dung"]}
        bad = 0
        for phan in de["de_minh_hoa"]["phan"]:
            for c in phan.get("cau", []):
                if c.get("chu_de") and c.get("don_vi"):
                    if (c["chu_de"], c["don_vi"]) not in hop_le:
                        r.err(f"De: cau {c.get('stt')} tro toi don vi khong "
                              f"co trong ma tran: {c['chu_de']} / {c['don_vi']}")
                        bad += 1
        if not bad:
            r.ok("De: moi cau deu tro toi chu de/don vi kien thuc hop le")
    elif de is None:
        r.warn("Khong tim thay de_bai_tap.json - bo qua buoc doi chieu de")

    return r.show()


if __name__ == "__main__":
    folder = sys.argv[1] if len(sys.argv) > 1 else "."
    sys.exit(1 if run(folder) else 0)
