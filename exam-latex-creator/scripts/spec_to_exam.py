# -*- coding: utf-8 -*-
"""Bảng đặc tả (.docx / .json)  ->  kế hoạch ra đề  ->  khung .tex

Cho phép nạp một bảng đặc tả có sẵn rồi sinh đề LaTeX ĐÚNG cấu trúc bảng đó:
đúng số câu từng loại, đúng mức độ, đúng chủ đề/đơn vị kiến thức của từng câu.

Lệnh:
    read     <spec.docx|spec.json> [-o plan.json] [--lop 6] [--mon K]
    skeleton <plan.json> [-o de.tex]
    verify   <plan.json> <de.tex>

Ví dụ:
    python spec_to_exam.py read bang_dac_ta.docx -o plan.json --lop 6 --mon K
    python spec_to_exam.py skeleton plan.json -o ../latex-output/DE_MADE101.tex
    python spec_to_exam.py verify plan.json ../latex-output/DE_MADE101.tex
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import unicodedata

for _s in (sys.stdout, sys.stderr):
    if (getattr(_s, "encoding", "") or "").lower().replace("-", "") not in \
            ("utf8", "utf_8") and hasattr(_s, "reconfigure"):
        try:
            _s.reconfigure(encoding="utf-8", errors="replace")
        except (ValueError, OSError):
            pass


# ============================================================ bảng quy đổi
# Tên nhóm câu hỏi trong bảng đặc tả -> loại câu hỏi của skill
NHOM_MAP = [
    (("nhieu lua chon", "trac nghiem nhieu", "mot lua chon", "4 lua chon"),
     {"kieu": "EX", "loai": 1, "moi_truong": "ex", "so_y_moi_cau": 1}),
    (("dung - sai", "dung sai", "dung-sai"),
     {"kieu": "TF", "loai": 2, "moi_truong": "ex", "so_y_moi_cau": 4}),
    (("tra loi ngan", "traloingan"),
     {"kieu": "SA", "loai": 3, "moi_truong": "ex", "so_y_moi_cau": 1}),
    (("tu luan",),
     {"kieu": "BT", "loai": 4, "moi_truong": "bt", "so_y_moi_cau": 1}),
]

# Tên mức độ -> mã + ký tự mức độ trong ID6 (xem references/mapid6-coding.md)
MUCDO_MAP = [
    (("van dung cao", "vdc"), {"ma": "VDC", "ten": "Vận dụng cao", "id6": "C"}),
    (("lien he", "thuc te", "thuc tien"), {"ma": "LH", "ten": "Liên hệ thực tế", "id6": "T"}),
    (("van dung", "vd"), {"ma": "VD", "ten": "Vận dụng", "id6": "V"}),
    (("thong hieu", "hieu"), {"ma": "TH", "ten": "Thông hiểu", "id6": "H"}),
    (("nhan biet", "biet"), {"ma": "NB", "ten": "Nhận biết", "id6": "N"}),
]


def _kd(s):
    """Bỏ dấu, hạ chữ thường, gom khoảng trắng — để so khớp tên cột."""
    s = unicodedata.normalize("NFD", str(s or ""))
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    s = s.replace("đ", "d").replace("Đ", "D")
    s = re.sub(r"[–—]", "-", s)
    s = re.sub(r"[^\w\s\-]", " ", s)
    return re.sub(r"\s+", " ", s).strip().lower()


def match_nhom(ten):
    k = _kd(ten)
    for keys, val in NHOM_MAP:
        if any(x in k for x in keys):
            return dict(val, ten=str(ten).strip())
    return None


def match_muc_do(ten):
    k = _kd(ten)
    for keys, val in MUCDO_MAP:
        if any(x in k for x in keys):
            return dict(val, ten_bang=str(ten).strip())
    return None


# ============================================================ đọc từ .docx
def _find_spec_table(doc):
    """Chọn bảng đặc tả: bảng có ô tiêu đề chứa 'Yêu cầu cần đạt'."""
    best = None
    for t in doc.tables:
        ncol = len(t.columns)
        if ncol < 6 or len(t.rows) < 5:
            continue
        head = " ".join(_kd(t.cell(0, c).text) for c in range(min(ncol, 8)))
        if "yeu cau can dat" in head:
            return t
        if best is None or ncol > len(best.columns):
            best = t
    return best


def _header_rows(t):
    """Số dòng tiêu đề: các dòng đầu mà cột 0 vẫn là ô 'TT' (gộp dọc)."""
    first = _kd(t.cell(0, 0).text)
    n = 0
    for r in range(min(6, len(t.rows))):
        if _kd(t.cell(r, 0).text) == first:
            n += 1
        else:
            break
    return max(n, 1)


def read_docx(path):
    try:
        from docx import Document
    except ImportError:
        raise SystemExit("[LOI] Can cai python-docx:  pip install python-docx")

    doc = Document(path)
    t = _find_spec_table(doc)
    if t is None:
        raise SystemExit("[LOI] Khong tim thay bang dac ta trong file docx")

    ncol = len(t.columns)
    hr = _header_rows(t)

    # cột "Yêu cầu cần đạt"
    c_yccd = None
    for c in range(ncol):
        if "yeu cau can dat" in _kd(t.cell(0, c).text):
            c_yccd = c
            break
    if c_yccd is None:
        raise SystemExit("[LOI] Khong tim thay cot 'Yeu cau can dat'")

    c_chude = 1 if ncol > 2 else 0
    c_donvi = c_yccd - 1

    # ánh xạ từng cột số liệu -> (nhóm, mức độ)
    cols = {}
    warn = []
    for c in range(c_yccd + 1, ncol):
        ten_nhom = t.cell(max(hr - 2, 0), c).text
        ten_md = t.cell(hr - 1, c).text
        nhom, md = match_nhom(ten_nhom), match_muc_do(ten_md)
        if nhom and md:
            cols[c] = (nhom, md)
        else:
            warn.append(f"cot {c}: nhom={ten_nhom!r} muc_do={ten_md!r} - bo qua")

    if not cols:
        raise SystemExit("[LOI] Khong doc duoc cot nhom/muc do nao")

    rows = []
    for r in range(hr, len(t.rows)):
        c0 = t.cell(r, 0).text.strip()
        if _kd(c0).startswith(("tong so", "ty le", "tong diem")):
            break
        yccd = t.cell(r, c_yccd).text.strip()
        so = {}
        for c, (nhom, md) in cols.items():
            v = t.cell(r, c).text.strip()
            m = re.search(r"\d+", v)
            if m:
                so[c] = int(m.group())
        if not so:
            continue                       # dòng nhãn "Nhận biết:" — bỏ qua
        rows.append({
            "chu_de": t.cell(r, c_chude).text.strip(),
            "don_vi": t.cell(r, c_donvi).text.strip(),
            "yccd": re.sub(r"\s+", " ", yccd),
            "so": so,
        })
    return rows, cols, warn


# ============================================================ đọc từ .json
def read_json(path):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    cfg = data.get("cau_hinh", {})
    md_by_ma, nhom_by_ma = {}, {}
    for m in cfg.get("muc_do", []):
        ma = m["ma"] if isinstance(m, dict) else m
        ten = m.get("ten", ma) if isinstance(m, dict) else m
        md_by_ma[ma] = match_muc_do(ten) or {"ma": ma, "ten": ten, "id6": "N",
                                             "ten_bang": ten}
    for g in cfg.get("nhom_cau_hoi", []):
        n = match_nhom(g.get("ten", "")) or {}
        n.setdefault("kieu", "EX")
        n.setdefault("loai", g.get("loai", 1))
        n.setdefault("moi_truong", "bt" if g.get("loai") == 4 else "ex")
        n["ten"] = g.get("ten", g["ma"])
        if g.get("so_y_moi_cau"):
            n["so_y_moi_cau"] = int(g["so_y_moi_cau"])
        n.setdefault("so_y_moi_cau", 4 if n["kieu"] == "TF" else 1)
        nhom_by_ma[g["ma"]] = n

    cols, rows, warn = {}, [], []
    key = 0
    col_of = {}
    for g_ma, nhom in nhom_by_ma.items():
        for m_ma, md in md_by_ma.items():
            col_of[(g_ma, m_ma)] = key
            cols[key] = (nhom, md)
            key += 1

    for cd in data.get("chu_de", []):
        for nd in cd.get("noi_dung", []):
            if "yeu_cau_can_dat" in nd:            # bảng đặc tả
                for y in nd["yeu_cau_can_dat"]:
                    so = {}
                    for g_ma, n in (y.get("so_lenh_hoi") or {}).items():
                        k = col_of.get((g_ma, y.get("muc_do")))
                        if k is not None and n:
                            so[k] = int(n)
                    if so:
                        rows.append({"chu_de": cd["ten"], "don_vi": nd["ten"],
                                     "yccd": y.get("noi_dung", ""), "so": so})
            else:                                   # ma trận (không có YCCĐ)
                warn.append(f"'{nd.get('ten')}' lay tu MA TRAN - khong co "
                            f"yeu cau can dat, khung .tex se de trong")
                for g_ma, mm in (nd.get("so_lenh_hoi") or {}).items():
                    for m_ma, n in mm.items():
                        k = col_of.get((g_ma, m_ma))
                        if k is not None and n:
                            rows.append({"chu_de": cd["ten"], "don_vi": nd["ten"],
                                         "yccd": "", "so": {k: int(n)}})
    return rows, cols, warn, data.get("thong_tin", {})


# ============================================================ dựng kế hoạch
def build_plan(rows, cols, lop="6", mon="K", thong_tin=None, nguon=""):
    """Bung từng ô số liệu thành danh sách LỆNH HỎI, rồi gom thành CÂU."""
    lenh = []
    for row in rows:
        for c, n in sorted(row["so"].items()):
            nhom, md = cols[c]
            for _ in range(n):
                lenh.append({"kieu": nhom["kieu"], "loai": nhom["loai"],
                             "nhom": nhom["ten"], "moi_truong": nhom["moi_truong"],
                             "so_y_moi_cau": nhom.get("so_y_moi_cau", 1),
                             "muc_do": md["ma"], "muc_do_ten": md["ten"],
                             "id6_muc_do": md["id6"],
                             "chu_de": row["chu_de"], "don_vi": row["don_vi"],
                             "yccd": row["yccd"]})

    thu_tu = {"EX": 0, "TF": 1, "SA": 2, "BT": 3}
    lenh.sort(key=lambda x: thu_tu.get(x["kieu"], 9))

    cau, canh_bao = [], []
    i = 0
    while i < len(lenh):
        cur = lenh[i]
        k = cur["so_y_moi_cau"]
        nhom_y = lenh[i:i + k]
        if len(nhom_y) < k:
            canh_bao.append(
                f"{cur['kieu']}: con {len(nhom_y)} lenh hoi le, khong du {k} y "
                f"cho mot cau - kiem tra lai bang dac ta")
            k = len(nhom_y)
        don_vi = {y["don_vi"] for y in nhom_y}
        if len(don_vi) > 1:
            canh_bao.append(
                f"{cur['kieu']} cau {len(cau) + 1}: 4 y trai tren nhieu don vi "
                f"kien thuc ({' | '.join(sorted(don_vi))}) - nen gom lai")
        c = {
            "stt": len(cau) + 1,
            "kieu": cur["kieu"], "loai": cur["loai"], "nhom": cur["nhom"],
            "moi_truong": cur["moi_truong"],
            "chu_de": cur["chu_de"], "don_vi": cur["don_vi"],
            "muc_do": cur["muc_do"], "muc_do_ten": cur["muc_do_ten"],
            "id6_goi_y": f"{lop}{mon}?{cur['id6_muc_do']}?-?",
        }
        if k > 1:
            c["y"] = [{"muc_do": y["muc_do"], "muc_do_ten": y["muc_do_ten"],
                       "yccd": y["yccd"], "don_vi": y["don_vi"]} for y in nhom_y]
            c["muc_do"] = sorted({y["muc_do"] for y in nhom_y})
            c["muc_do_ten"] = " / ".join(sorted({y["muc_do_ten"] for y in nhom_y}))
        else:
            c["yccd"] = cur["yccd"]
        cau.append(c)
        i += k

    tong = {}
    for c in cau:
        tong[c["kieu"]] = tong.get(c["kieu"], 0) + 1
    return {
        "nguon": nguon,
        "thong_tin": thong_tin or {},
        "lop": lop, "mon": mon,
        "tong_ket": {"so_cau_theo_loai": tong, "tong_so_cau": len(cau),
                     "tong_lenh_hoi": len(lenh)},
        "canh_bao": canh_bao,
        "cau": cau,
    }


# ============================================================ sinh khung tex
SKILL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(SKILL_DIR, "assets", "template-de-thi.tex")

# Thứ tự 4 phần trong template-de-thi.tex
LOAI_KIEU = {1: "EX", 2: "TF", 3: "SA", 4: "BT"}


def _than_cau(c):
    if c.get("_than"):                      # đã đổ nội dung thật
        return c["_than"] + "\n"
    if c["kieu"] == "EX":
        return ("% TODO: noi dung cau hoi\n"
                "\\choice\n{}\n{}\n{\\True }\n{}\n"
                "\\loigiai{\n% TODO: loi giai\n}\n")
    if c["kieu"] == "TF":
        y = c.get("y", [])
        dong = "".join(
            f"% y {chr(97 + i)}) [{v['muc_do_ten']}] {v['yccd']}\n"
            for i, v in enumerate(y))
        return (dong + "% TODO: phan dan chung\n"
                "\\choiceTF\n{}\n{}\n{}\n{}\n"
                "\\loigiai{\n\\begin{itemchoice}[T1,F2,T3,F4]\n"
                "  \\itemch % TODO a)\n  \\itemch % TODO b)\n"
                "  \\itemch % TODO c)\n  \\itemch % TODO d)\n"
                "\\end{itemchoice}\n}\n")
    if c["kieu"] == "SA":
        return ("% TODO: noi dung cau hoi (dap an la mot con so)\n"
                "\\shortans{$$}\n\\loigiai{\n% TODO: loi giai\n}\n")
    return "% TODO: noi dung cau tu luan\n\\loigiai{\n% TODO: huong dan cham\n}\n"


def _khoi_cau(plan, kieu):
    """Sinh khối câu hỏi của một loại, kèm chú thích truy vết bảng đặc tả."""
    out, n = [], 0
    for c in plan["cau"]:
        if c["kieu"] != kieu:
            continue
        n += 1
        env = c["moi_truong"]
        out += [
            f"%%%========={kieu}_{n}================%%%",
            f"% Chu de : {c['chu_de']}",
            f"% Don vi : {c['don_vi']}",
            f"% Muc do : {c['muc_do_ten']}",
        ]
        if c.get("yccd"):
            out.append(f"% YCCD   : {c['yccd']}")
        out += [
            f"\\begin{{{env}}}%[{c['id6_goi_y']}]",
            _than_cau(c).rstrip(),
            f"\\end{{{env}}}",
            "",
        ]
    return "\n".join(out)


# ---------------------------------------------------------------- đổ nội dung
# CHỈ dùng lệnh đã có sẵn trong template và trong references/*.md.
# TUYỆT ĐỐI không thêm gói hay lệnh LaTeX mới vào file .tex.
_TEX_SUB = [
    ("\\", "/"), ("%", "\\%"), ("&", "\\&"), ("#", "\\#"), ("_", "\\_"),
    ("°C", "$^\\circ$C"), ("°", "$^\\circ$"),
    ("³", "$^3$"), ("²", "$^2$"), ("×", "$\\times$"),
    ("−", "$-$"), ("→", "$\\rightarrow$"), ("≥", "$\\ge$"), ("≤", "$\\le$"),
    ("…", "\\dots"), ("...", "\\dots"),
    ("—", "---"), ("–", "--"),
    ("“", "\\lq\\lq "), ("”", "\\rq\\rq "), ("\"", "\\rq\\rq "),
]


_VIET = set("àáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợ"
            "ùúủũụưừứửữựỳýỷỹỵđ")
_VIET |= {c.upper() for c in _VIET}
KY_TU_LA = set()


def tex(s):
    """Chuyển văn bản thuần sang LaTeX an toàn, không dùng gói ngoài."""
    s = str(s or "").strip()
    for a, b in _TEX_SUB:
        s = s.replace(a, b)
    # Lưới an toàn: ghi nhận ký tự Unicode chưa có quy tắc chuyển đổi, vì
    # pdflatex + vietnam(utf8) sẽ báo lỗi khi gặp chúng.
    for ch in s:
        if ord(ch) > 127 and ch not in _VIET:
            KY_TU_LA.add(ch)
    return re.sub(r"[ \t]+", " ", s)


def _mucdo_set(c):
    if isinstance(c.get("muc_do"), list):
        return set(c["muc_do"])
    if c.get("y") and all(y.get("muc_do") for y in c["y"]):
        return {y["muc_do"] for y in c["y"]}
    return {c.get("muc_do")}


def _than_EX(c):
    dong = [tex(c["de"]), "\\choice"]
    dung = (c.get("dap_an") or "A").strip().upper()
    for i, o in enumerate(c.get("lua_chon", [])):
        t = tex(o).rstrip(".")
        dong.append("{\\True %s}" % t if "ABCD"[i] == dung else "{%s}" % t)
    dong += ["\\loigiai{", tex(c.get("loi_giai", "")), "}"]
    return "\n".join(dong)


# Môi trường itemchoice tự sinh chữ "Đúng."/"Sai." từ nhãn [T1,F2,T3,F4],
# nên phải bỏ các từ này nếu lời giải lặp lại ở đầu mỗi \itemch.
_DAU_DS_RE = re.compile(r"^\s*(?:Đúng|Sai)\s*[.,]\s*")


def bo_dau_dung_sai(s):
    """'Đúng, đây là...' -> 'Đây là...' ; 'Sai. Toả nhiệt...' -> 'Toả nhiệt...'"""
    m = _DAU_DS_RE.match(str(s or ""))
    if not m:
        return s
    t = str(s)[m.end():]
    return t[:1].upper() + t[1:] if t else t


def _than_TF(c):
    ys = c.get("y", [])
    dong = [tex(c["de"]), "\\choiceTF"]
    for y in ys:
        t = tex(y["nd"]).rstrip(".")
        dong.append("{\\True %s}" % t if y.get("dap_an") else "{%s}" % t)
    nhan = ",".join(("T" if y.get("dap_an") else "F") + str(i + 1)
                    for i, y in enumerate(ys))
    dong += ["\\loigiai{", "\\begin{itemchoice}[%s]" % nhan]
    for y in ys:
        dong.append("\\itemch %s" % tex(bo_dau_dung_sai(y.get("giai_thich", ""))))
    dong += ["\\end{itemchoice}", "}"]
    return "\n".join(dong)


def _than_SA(c):
    da = str(c.get("dap_an", "")).strip().replace(".", "{,}").replace(",", "{,}")
    return "\n".join([tex(c["de"]), "\\shortans{$%s$}" % da,
                      "\\loigiai{", tex(c.get("loi_giai", "")), "}"])


def _than_BT(c):
    dong = [tex(c["de"]) + "\\\\"]
    ys = c.get("y", [])
    for i, y in enumerate(ys):
        dong.append(tex(y["nd"]) + ("\\\\" if i < len(ys) - 1 else ""))
    dong.append("\\loigiai{")
    hd = c.get("huong_dan_cham") or []
    for i, b in enumerate(hd):
        dong.append(tex(b["nd"]) + ("\\\\" if i < len(hd) - 1 else ""))
    if not hd and c.get("loi_giai"):
        dong.append(tex(c["loi_giai"]))
    dong.append("}")
    return "\n".join(dong)


_THAN = {"EX": _than_EX, "TF": _than_TF, "SA": _than_SA, "BT": _than_BT}


def fill_plan(plan, de, id6_map=None):
    """Gắn nội dung câu hỏi từ de_bai_tap.json vào từng ô của kế hoạch."""
    kho = []
    for phan in de.get("de_minh_hoa", {}).get("phan", []):
        for c in phan.get("cau", []):
            c.setdefault("loai", phan.get("loai"))
            kho.append(c)

    chua_dung = list(kho)
    thieu, dem = [], {}
    for slot in plan["cau"]:
        loai, dv = slot["loai"], slot["don_vi"]
        mds = _mucdo_set(slot)
        chon = None
        for uu_tien in (
                lambda c: c["loai"] == loai and c.get("don_vi") == dv
                and _mucdo_set(c) == mds,
                lambda c: c["loai"] == loai and c.get("don_vi") == dv,
                lambda c: c["loai"] == loai):
            for c in chua_dung:
                if uu_tien(c):
                    chon = c
                    break
            if chon:
                break
        if chon is None:
            thieu.append(slot)
            continue
        chua_dung.remove(chon)
        dem[slot["kieu"]] = dem.get(slot["kieu"], 0) + 1
        slot["_than"] = _THAN[slot["kieu"]](chon)
        slot["_nguon_stt"] = chon.get("stt")
        if id6_map:
            key = f"{slot['kieu']}_{dem[slot['kieu']]}"
            if key in id6_map:
                slot["id6_goi_y"] = id6_map[key]
    return thieu, chua_dung


_SEC_RE = re.compile(r"^%+=+\s*Phần[^\n]*$", re.M)
_CHEN_RE = re.compile(r"^[ \t]*%[ \t]*<Chèn các câu hỏi loại\s*(\d)[^>]*>[ \t]*$", re.M)


def build_skeleton(plan, meta=None, template=TEMPLATE):
    """Sinh file .tex hoàn chỉnh theo assets/template-de-thi.tex.

    - Điền các `\\gdef` từ `meta`
    - Chèn câu hỏi vào đúng 4 vị trí đánh dấu
    - XÓA hẳn phần (subsection) nào không có câu hỏi, đúng quy định của skill
    - Thay `<tên file>` / `<mã đề>` trong Opensolutionfile
    """
    meta = meta or {}
    with open(template, "r", encoding="utf-8") as f:
        tpl = f.read()

    dem = {}
    for c in plan["cau"]:
        dem[c["kieu"]] = dem.get(c["kieu"], 0) + 1

    # ---- tách template: đầu | 4 phần | đuôi
    starts = [m.start() for m in _SEC_RE.finditer(tpl)]
    end = tpl.find("\\begin{center}")
    if not starts or end == -1:
        raise SystemExit(f"[LOI] Template khong dung dinh dang: {template}")
    bounds = starts + [end]
    head = tpl[:starts[0]]
    tail = tpl[end:]
    blocks = [tpl[bounds[i]:bounds[i + 1]] for i in range(len(starts))]

    # ---- xử lý từng phần
    giu = []
    for blk in blocks:
        m = _CHEN_RE.search(blk)
        if not m:
            giu.append(blk)
            continue
        loai = int(m.group(1))
        kieu = LOAI_KIEU.get(loai)
        so = dem.get(kieu, 0)
        if so == 0:
            continue                       # bỏ hẳn phần không có câu hỏi
        blk = _CHEN_RE.sub(lambda _m: _khoi_cau(plan, kieu).rstrip(), blk, count=1)
        blk = blk.replace(f"<tổng câu loại {loai}>", str(so))
        blk = blk.replace(f"<tổng bài loại {loai}>", str(so))
        giu.append(blk)

    doc = head + "".join(giu) + tail

    # ---- điền metadata
    ti = plan.get("thong_tin") or {}
    mon_mac_dinh = ti.get("mon", "")
    if ti.get("lop"):
        mon_mac_dinh = f"{mon_mac_dinh} {ti['lop']}".strip()
    made = str(meta.get("made") or "101")
    ten_file = meta.get("ten_file") or "DE"
    thay = {
        "<Môn học>": meta.get("monhoc") or mon_mac_dinh or "<Môn học>",
        "<ngày thi>": meta.get("ngaykt") or "<ngày thi>",
        "<thời gian>": str(meta.get("thoigian")
                           or re.sub(r"\D", "", str(ti.get("thoi_gian", ""))) or "45"),
        "<mã đề ngẫu nhiên>": made,
        "<số thứ tự đề -1>": str(int(meta.get("so_de", 1)) - 1),
        "<tên kì thi>": meta.get("ten_de") or "Kiểm tra định kì",
        "<môn thi>": meta.get("monhoc") or mon_mac_dinh or "",
        "<tên file>": ten_file,
        "<mã đề>": made,
    }
    for k, v in thay.items():
        doc = doc.replace(k, v)
    if meta.get("nh"):
        doc = re.sub(r"\\gdef\\nh\{[^}]*\}", r"\\gdef\\nh{%s}" % meta["nh"], doc)

    ghi_chu = (
        "% ====================================================================\n"
        f"% Khung de sinh tu bang dac ta: {plan.get('nguon') or '?'}\n"
        "% Moi cau da co san Chu de / Don vi kien thuc / Yeu cau can dat / Muc do.\n"
        "% Viec can lam: (1) dien noi dung cau hoi va loi giai vao cac cho TODO,\n"
        "%               (2) tra MAPID de thay dau '?' trong ID6.\n"
        "% ====================================================================\n"
    )
    return ghi_chu + doc


# ============================================================ đối chiếu đề
def _parse_tex(text):
    got = []
    for m in re.finditer(r"\\begin\{(ex|bt)\}(.*?)\\end\{\1\}", text, re.DOTALL):
        env, body = m.group(1), m.group(2)
        if env == "bt":
            kieu = "BT"
        elif "\\choiceTF" in body:
            kieu = "TF"
        elif "\\shortans" in body:
            kieu = "SA"
        elif "\\choice" in body:
            kieu = "EX"
        else:
            kieu = "BT"
        idm = re.search(r"%\[\s*([^\]\s]+)\s*\]", body)
        got.append({"kieu": kieu, "id6": idm.group(1) if idm else None})
    return got


def verify(plan, tex_path):
    with open(tex_path, "r", encoding="utf-8") as f:
        got = _parse_tex(f.read())

    loi = 0
    want = plan["tong_ket"]["so_cau_theo_loai"]
    have = {}
    for g in got:
        have[g["kieu"]] = have.get(g["kieu"], 0) + 1

    print("So cau theo loai:")
    for k in ("EX", "TF", "SA", "BT"):
        w, h = want.get(k, 0), have.get(k, 0)
        if w or h:
            ok = "OK " if w == h else "LOI"
            loi += (w != h)
            print(f"  [{ok}] {k}: dac ta {w} - de {h}")

    thieu = [g for g in got if not g["id6"] or "?" in g["id6"]]
    if thieu:
        loi += 1
        print(f"  [LOI] {len(thieu)} cau chua gan ID6 day du (con dau '?')")
    else:
        print(f"  [OK ] {len(got)} cau deu da co ID6")

    # đối chiếu ký tự mức độ trong ID6 với kế hoạch
    want_md = {}
    for c in plan["cau"]:
        for ma in (c["muc_do"] if isinstance(c["muc_do"], list) else [c["muc_do"]]):
            want_md[ma] = want_md.get(ma, 0) + 1
    print("Muc do theo ke hoach:",
          ", ".join(f"{k}={v}" for k, v in sorted(want_md.items())))

    print("-" * 58)
    print(f"Tong so loi: {loi}")
    return loi


# ============================================================ CLI
def _print_summary(plan, warn):
    ti = plan.get("thong_tin") or {}
    if ti:
        print("Thong tin:", " | ".join(f"{k}={v}" for k, v in ti.items()))
    tk = plan["tong_ket"]
    print(f"Tong: {tk['tong_so_cau']} cau / {tk['tong_lenh_hoi']} lenh hoi")
    for k, v in tk["so_cau_theo_loai"].items():
        print(f"   {k}: {v} cau")
    md = {}
    for c in plan["cau"]:
        for ma in (c["muc_do"] if isinstance(c["muc_do"], list) else [c["muc_do"]]):
            md[ma] = md.get(ma, 0) + 1
    print("Lenh hoi theo muc do:", ", ".join(f"{k}={v}" for k, v in sorted(md.items())))
    for w in warn + plan.get("canh_bao", []):
        print("[CANH BAO]", w)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("read", help="Doc bang dac ta -> plan.json")
    p.add_argument("spec")
    p.add_argument("-o", "--output", default=None)
    p.add_argument("--lop", default="6")
    p.add_argument("--mon", default="K")
    p.add_argument("--y-dung-sai", dest="y_ds", type=int, default=None,
                   help="So y moi cau Dung-Sai (mac dinh 4)")
    p.add_argument("--y-tu-luan", dest="y_tl", type=int, default=None,
                   help="So lenh hoi moi cau tu luan: 1 neu bang dac ta dem theo "
                        "cau, 2 neu dem theo y a)/b). Mac dinh: lay tu file JSON "
                        "neu co, nguoc lai la 1")

    p = sub.add_parser("skeleton",
                       help="plan.json -> file .tex hoan chinh theo template")
    p.add_argument("plan")
    p.add_argument("-o", "--output", default=None,
                   help="Nen dat trong latex-output/ (cung cho FileMain.tex)")
    p.add_argument("--monhoc", default=None)
    p.add_argument("--ten-de", dest="ten_de", default=None)
    p.add_argument("--ngaykt", default=None)
    p.add_argument("--nh", default=None)
    p.add_argument("--thoigian", default=None)
    p.add_argument("--made", default="101")
    p.add_argument("--so-de", dest="so_de", default=1, type=int)
    p.add_argument("--ten-file", dest="ten_file", default=None,
                   help="Ten dung trong Opensolutionfile (mac dinh: theo ten file output)")
    p.add_argument("--template", default=TEMPLATE)

    p = sub.add_parser("fill",
                       help="plan.json + de_bai_tap.json -> .tex day du noi dung")
    p.add_argument("plan")
    p.add_argument("de", help="File de_bai_tap.json (dinh dang skill exam-idea)")
    p.add_argument("-o", "--output", default=None)
    p.add_argument("--id6-map", dest="id6_map", default=None,
                   help="File JSON anh xa {\"EX_1\": \"6KCN1-1\", ...}")
    p.add_argument("--monhoc", default=None)
    p.add_argument("--ten-de", dest="ten_de", default=None)
    p.add_argument("--ngaykt", default=None)
    p.add_argument("--nh", default=None)
    p.add_argument("--thoigian", default=None)
    p.add_argument("--made", default="101")
    p.add_argument("--so-de", dest="so_de", default=1, type=int)
    p.add_argument("--ten-file", dest="ten_file", default=None)
    p.add_argument("--template", default=TEMPLATE)

    p = sub.add_parser("verify", help="Doi chieu de .tex voi plan.json")
    p.add_argument("plan")
    p.add_argument("tex")

    a = ap.parse_args()

    if a.cmd == "read":
        ext = os.path.splitext(a.spec)[1].lower()
        ti = {}
        if ext == ".docx":
            rows, cols, warn = read_docx(a.spec)
        elif ext == ".json":
            rows, cols, warn, ti = read_json(a.spec)
        else:
            raise SystemExit("[LOI] Chi ho tro .docx hoac .json")
        # số ý mỗi câu: chỉ ghi đè khi người dùng truyền cờ tường minh,
        # nếu không thì giữ giá trị đọc được từ file nguồn
        for nhom, _md in cols.values():
            if nhom["kieu"] == "TF" and a.y_ds:
                nhom["so_y_moi_cau"] = a.y_ds
            elif nhom["kieu"] == "BT" and a.y_tl:
                nhom["so_y_moi_cau"] = a.y_tl
        plan = build_plan(rows, cols, a.lop, a.mon, ti,
                          nguon=os.path.basename(a.spec))
        out = a.output or os.path.splitext(a.spec)[0] + "_plan.json"
        with open(out, "w", encoding="utf-8") as f:
            json.dump(plan, f, ensure_ascii=False, indent=2)
        _print_summary(plan, warn)
        print(f"[OK] Ghi ke hoach: {out}")
        return 0

    if a.cmd in ("skeleton", "fill"):
        with open(a.plan, "r", encoding="utf-8") as f:
            plan = json.load(f)
        if a.cmd == "fill":
            with open(a.de, "r", encoding="utf-8") as f:
                de = json.load(f)
            id6 = None
            if a.id6_map:
                with open(a.id6_map, "r", encoding="utf-8") as f:
                    id6 = json.load(f)
            thieu, du = fill_plan(plan, de, id6)
            print(f"Da do noi dung: {len(plan['cau']) - len(thieu)}"
                  f"/{len(plan['cau'])} cau")
            for t in thieu:
                print(f"[CANH BAO] thieu noi dung cho {t['kieu']} - "
                      f"{t['don_vi'][:50]} ({t['muc_do_ten']})")
            for c in du:
                print(f"[CANH BAO] cau {c.get('stt')} trong de_bai_tap.json "
                      f"khong khop o nao trong bang dac ta")
            if KY_TU_LA:
                print("[CANH BAO] ky tu Unicode chua co quy tac chuyen doi, "
                      "pdflatex se bao loi: "
                      + " ".join(f"U+{ord(c):04X}({c})" for c in sorted(KY_TU_LA)))
        out = a.output or os.path.splitext(a.plan)[0] + ".tex"
        out = os.path.abspath(out)
        ten_file = a.ten_file or re.sub(
            r"_MADE\d+$", "", os.path.splitext(os.path.basename(out))[0])
        meta = {"monhoc": a.monhoc, "ten_de": a.ten_de, "ngaykt": a.ngaykt,
                "nh": a.nh, "thoigian": a.thoigian, "made": a.made,
                "so_de": a.so_de, "ten_file": ten_file}
        os.makedirs(os.path.dirname(out), exist_ok=True)
        with open(out, "w", encoding="utf-8") as f:
            f.write(build_skeleton(plan, meta, a.template))
        print(f"[OK] Ghi de: {out}  ({plan['tong_ket']['tong_so_cau']} cau)")
        if os.path.basename(os.path.dirname(out)) != "latex-output":
            print("[CANH BAO] File .tex dung \\documentclass[FileMain.tex]{subfiles}"
                  " nen phai nam cung thu muc voi FileMain.tex (latex-output/)")
        print("Buoc tiep theo:")
        print("   1. Dien noi dung vao cac cho % TODO, tra MAPID de thay '?' trong ID6")
        print(f"   2. python scripts/spec_to_exam.py verify {a.plan} {out}")
        print(f"   3. python scripts/export_pdf.py fix \"{out}\"")
        print(f"   4. python scripts/export_pdf.py compile \"{os.path.basename(out)}\""
              f" --dir \"{os.path.dirname(out)}\" --times 2 --clean")
        return 0

    with open(a.plan, "r", encoding="utf-8") as f:
        plan = json.load(f)
    return 1 if verify(plan, a.tex) else 0


if __name__ == "__main__":
    sys.exit(main())
