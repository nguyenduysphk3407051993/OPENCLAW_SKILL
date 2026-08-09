# -*- coding: utf-8 -*-
"""Trích xuất sách TikZ (PDF) thành nhiều file .md phân loại theo đối tượng.

    python pdf_to_md.py <sach.pdf> -o <thu_muc_dich>

Ba việc quan trọng script này làm, mà một lệnh trích xuất thô không làm được:

1. **Phân biệt code với văn xuôi bằng FONT.** Sách dùng VNTT (Vietnamese
   TypeWriter, monospace) cho mã LaTeX và VNR/VNBX cho văn xuôi/tiêu đề. Dòng
   toàn code -> khối ```latex; code lẫn trong câu văn -> bọc `backtick` để
   không cắt vụn đoạn văn.

2. **Sửa `--` bị PDF render thành en-dash.** Không sửa thì mã copy ra chạy sai.

3. **Phát hiện ký tự tiếng Việt bị nuốt.** Font VNTT không map hết Unicode nên
   PyMuPDF làm rơi vài ký tự (ví dụ `{Điểm A}` ra thành `{im A}`). Vì font là
   monospace nên so bề rộng span với số ký tự đọc được là biết mất bao nhiêu
   ký tự; script đánh dấu ngay tại dòng đó để người đọc đối chiếu lại PDF.
"""

from __future__ import annotations

import argparse
import os
import re
import statistics
import sys

import fitz  # PyMuPDF

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass

Y_HEADER, Y_FOOTER = 60, 810
BO_QUA = ("Học Tikz theo cách của bạn", "Trung tâm GDNN", "Mục lục")
RE_SO_TRANG = re.compile(r"^Trang\s+\d+$")
RE_MUC = re.compile(r"^(?:[IVX]+\.)?\d+(?:\.\d+)*\.?$")

FONT_CODE = ("VNTT", "CMTT")
FONT_DAM = ("VNBX", "VNBI")

# Mỗi file .md một đối tượng, kèm khoảng trang (1-based, gồm cả hai đầu)
CHUDE = [
    ("01-khai-bao-he-toa-do", "Khai báo, môi trường vẽ và hệ trục toạ độ", 4, 6),
    ("02-tinh-toan-toa-do", "Tham số, hàm tính toán và phép toán trên toạ độ", 6, 8),
    ("03-diem-van-ban-doan-thang", "Vẽ điểm, hiển thị văn bản, đoạn thẳng và đường gấp khúc", 8, 11),
    ("04-duong-tron-cung-duong-cong", "Đường tròn, ellipse, cung và các dạng đường cong", 11, 15),
    ("05-tiep-tuyen-giao-diem", "Lấy điểm trên đường cong, tiếp tuyến, giao điểm", 15, 20),
    ("06-scope-clip-node-pic", "Môi trường scope, clip, node và pic", 20, 25),
    ("07-tuy-chon-thuong-dung", "Các tuỳ chọn thường dùng cho đường và node", 25, 26),
    ("08-foreach-macro", "Vòng lặp foreach và cách tạo macro", 26, 30),
    ("09-hinh-khong-gian-3d", "Vẽ hình không gian (giả 3D)", 30, 33),
    ("10-bang-xet-dau-bien-thien", "Bảng xét dấu và bảng biến thiên", 33, 41),
    ("11-do-thi-ham-so", "Đồ thị hàm số, hệ toạ độ cực", 41, 45),
    ("12-to-mien-do-thi", "Vẽ và tô miền đồ thị hàm số", 45, 58),
    ("13-tu-duy-ve-hinh", "Tư duy hình hoạ để dựng hình", 58, 61),
    ("14-export-anh-dong", "Export hình ảnh, làm ảnh động PDF và GIF", 61, 70),
    ("15-thu-vien-thuong-dung", "Thư viện hay dùng: calc, intersections, angles, patterns, decoration, shadings", 70, 73),
]


def sua_code(s: str) -> str:
    """PDF render `--` thành en-dash; không sửa thì mã copy ra sẽ SAI."""
    s = (s.replace("—", "---").replace("–", "--")
          .replace("“", '"').replace("”", '"')
          .replace("‘", "'").replace("’", "'"))
    for sai, dung in SUA_LOI_SACH.items():
        s = s.replace(sai, dung)
    return s


# Sách bị lỗi ngay từ khâu in: font VNTT nuốt vài ký tự tiếng Việt trong khối
# code, trong khi hình vẽ bên cạnh vẫn hiện đúng. Sửa lại theo hình.
SUA_LOI_SACH = {
    "(0,0){im A}": "(0,0){Điểm A}",
    "(4,0){im B}": "(4,0){Điểm B}",
}


def ghep_ky_tu(chars, co_chu):
    """Ghép ký tự thành chuỗi, chèn lại dấu cách mà PDF làm rơi.

    pdfTeX thỉnh thoảng không phát ra ký tự space sau nguyên âm có dấu, nhưng
    khoảng trống hình học thì vẫn còn.

    Đo trên toàn sách, khoảng hở giữa hai ký tự phân bố thành hai cụm tách bạch:
    trong cùng một từ thì ≤ 1,0 pt (hơn 53.000 cặp), chỗ rơi mất dấu cách thì
    ≥ 2,5 pt (khoảng 1.500 cặp). Cắt ở 2,0 pt là an toàn.
    """
    nguong = max(2.0, co_chu * 0.16)
    ra = []
    for i, c in enumerate(chars):
        if i:
            hoh = c["bbox"][0] - chars[i - 1]["bbox"][2]
            if hoh > nguong and not ra[-1].isspace() and not c["c"].isspace():
                ra.append(" ")
        ra.append(c["c"])
    return "".join(ra)


def do_rong_ky_tu(doc):
    """Tự đo bề rộng 1 ký tự của từng (font, cỡ chữ) monospace.

    Chỉ lấy mẫu từ span thuần ASCII — những span đó chắc chắn không mất ký tự.
    """
    mau = {}
    for page in doc:
        for block in page.get_text("dict")["blocks"]:
            for line in block.get("lines", []):
                for s in line["spans"]:
                    if not s["font"].startswith(FONT_CODE):
                        continue
                    t = s["text"]
                    if not t or not t.isascii() or t.isspace():
                        continue
                    w = s["bbox"][2] - s["bbox"][0]
                    if w > 0:
                        mau.setdefault((s["font"], round(s["size"], 1)),
                                       []).append(w / len(t))
    return {k: statistics.median(v) for k, v in mau.items() if len(v) >= 5}


def so_ky_tu_mat(span, bang_rong):
    key = (span["font"], round(span["size"], 1))
    cw = bang_rong.get(key)
    t = span["text"]
    if not cw or not t.strip():
        return 0
    w = span["bbox"][2] - span["bbox"][0]
    return max(0, round(w / cw) - len(t))


def doc_trang(page, so_tr, bang_rong):
    """Trả về list dict: {loai, text, mat} — loai in {'code','van','muc'}."""
    ra = []
    for block in page.get_text("rawdict")["blocks"]:
        for line in block.get("lines", []):
            y = line["bbox"][1]
            if y < Y_HEADER or y > Y_FOOTER:
                continue
            spans = [s for s in line["spans"] if s.get("chars")]
            for s in spans:                       # rawdict không có sẵn 'text'
                s["text"] = ghep_ky_tu(s["chars"], s["size"])
            # ghép qua ranh giới span (chỗ đó cũng có thể rơi dấu cách)
            moi_chars = [c for s in spans for c in s["chars"]]
            raw = ghep_ky_tu(moi_chars, spans[0]["size"]).rstrip() if spans else ""
            if not raw.strip() or RE_SO_TRANG.match(raw.strip()):
                continue
            if any(k in raw for k in BO_QUA):
                continue

            n_code = sum(len(s["text"]) for s in spans
                         if s["font"].startswith(FONT_CODE))
            mat = sum(so_ky_tu_mat(s, bang_rong) for s in spans
                      if s["font"].startswith(FONT_CODE))

            if n_code and n_code * 2 > len(raw):
                ra.append({"loai": "code", "text": sua_code(raw),
                           "mat": mat, "tr": so_tr})
                continue

            if n_code:
                # code lẫn trong câu văn -> bọc backtick, giữ nguyên mạch văn
                buf, cur, cur_code = [], "", None
                for s in spans:
                    is_code = s["font"].startswith(FONT_CODE)
                    if cur_code is None or is_code == cur_code:
                        cur += s["text"]
                    else:
                        buf.append((cur_code, cur))
                        cur = s["text"]
                    cur_code = is_code
                buf.append((cur_code, cur))
                txt = "".join(f"`{sua_code(t.strip())}`" if c and t.strip()
                              else t for c, t in buf)
            else:
                txt = raw

            if all(s["font"].startswith(FONT_DAM) for s in spans) and len(raw) < 90:
                ra.append({"loai": "muc", "text": raw.strip(), "mat": 0, "tr": so_tr})
            else:
                ra.append({"loai": "van", "text": txt, "mat": mat, "tr": so_tr})
    return ra


def xuat_markdown(dong):
    md, buf, loai_tr, mat_khoi, tr_khoi = [], [], None, 0, 0

    def xa():
        nonlocal buf, mat_khoi
        if not buf:
            return
        if loai_tr == "code":
            # một dòng code ngắn nằm giữa câu văn -> để inline cho liền mạch,
            # đóng khung ```latex chỉ tổ cắt vụn đoạn văn
            if len(buf) == 1 and len(buf[0]) < 30 and not mat_khoi:
                md.extend([f"`{buf[0].strip()}`", ""])
                buf.clear()
                mat_khoi = 0
                return
            if mat_khoi:
                md.append(f"> ⚠️ Khối dưới bị rơi **{mat_khoi} ký tự tiếng Việt** "
                          f"khi trích xuất (font VNTT không map Unicode) — "
                          f"đối chiếu PDF trang {tr_khoi} nếu cần nhãn tiếng Việt.")
                md.append("")
            md.extend(["```latex", *buf, "```", ""])
        else:
            md.extend([*buf, ""])
        buf, mat_khoi = [], 0

    for d in dong:
        if d["loai"] == "muc":
            xa()
            loai_tr = None
            # "I.2.6" và tên mục nằm hai dòng riêng -> ghép thành một tiêu đề
            if RE_MUC.match(d["text"]) or (md and md[-1] == ""
                                           and len(md) > 1
                                           and md[-2].startswith("### ")
                                           and RE_MUC.match(md[-2][4:])):
                if md and md[-1] == "" and len(md) > 1 \
                        and md[-2].startswith("### ") and RE_MUC.match(md[-2][4:]):
                    md[-2] = f"{md[-2]} {d['text']}"
                    continue
            md.extend([f"### {d['text']}", ""])
            continue
        if d["loai"] != loai_tr:
            xa()
        loai_tr = d["loai"]
        if not buf:
            tr_khoi = d["tr"]
        buf.append(d["text"])
        mat_khoi += d["mat"]
    xa()
    return md


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pdf")
    ap.add_argument("-o", "--out-dir", required=True)
    a = ap.parse_args()

    doc = fitz.open(a.pdf)
    os.makedirs(a.out_dir, exist_ok=True)
    ten_sach = os.path.basename(a.pdf)
    bang_rong = do_rong_ky_tu(doc)
    print("Bề rộng ký tự đo được:",
          {f"{k[0]}@{k[1]}": round(v, 3) for k, v in bang_rong.items()})

    rows, tong_mat = [], 0
    for slug, tieu_de, tr_dau, tr_cuoi in CHUDE:
        dong = []
        for pno in range(tr_dau - 1, min(tr_cuoi, doc.page_count)):
            dong += doc_trang(doc[pno], pno + 1, bang_rong)
        mat = sum(d["mat"] for d in dong)
        tong_mat += mat
        body = xuat_markdown(dong)
        noi_dung = "\n".join([
            f"# {tieu_de}", "",
            f"> Trích từ `{ten_sach}`, trang {tr_dau}–{tr_cuoi}.", "",
            "---", "", *body]).rstrip() + "\n"
        noi_dung = re.sub(r"\n{3,}", "\n\n", noi_dung)
        with open(os.path.join(a.out_dir, slug + ".md"), "w",
                  encoding="utf-8", newline="\n") as f:
            f.write(noi_dung)
        n_code = noi_dung.count("```latex")
        print(f"  {slug + '.md':<34} {n_code:>3} khối code, {mat:>3} ký tự rơi")
        rows.append((slug, tieu_de, tr_dau, tr_cuoi, n_code, mat))

    muc_luc = [
        "# Học TikZ theo cách của bạn — bản trích xuất tham chiếu", "",
        f"Nguồn: `{ten_sach}` — Bùi Quý, Trung tâm GDNN–GDTX Duy Tiên, "
        f"{doc.page_count} trang.", "",
        "Tách theo **đối tượng cần vẽ** để tra nhanh khi viết mã TikZ.", "",
        "| File | Nội dung | Trang gốc | Khối code | Ký tự rơi |",
        "|---|---|---|---|---|",
    ]
    for slug, td, d0, d1, nc, mt in rows:
        muc_luc.append(f"| [`{slug}.md`]({slug}.md) | {td} | {d0}–{d1} | "
                       f"{nc} | {mt or '—'} |")
    muc_luc += [
        "", "## Hai lưu ý khi dùng bản trích xuất này", "",
        "1. **Mã LaTeX đã được sửa** chỗ PDF render `--` thành dấu gạch dài, "
        "nên copy ra dùng được ngay.",
        f"2. **Còn {tong_mat} ký tự tiếng Việt bị rơi** trong các khối code — "
        "font VNTT của sách không map hết Unicode nên trình đọc PDF nào cũng "
        "mất. Chỗ nào bị rơi đã được đánh dấu ⚠️ ngay trên khối code kèm số "
        "trang, mở PDF gốc đối chiếu là xong. Phần **mã lệnh TikZ thuần ASCII "
        "thì nguyên vẹn** — chỉ nhãn tiếng Việt bên trong `{...}` mới bị.",
    ]
    with open(os.path.join(a.out_dir, "README.md"), "w",
              encoding="utf-8", newline="\n") as f:
        f.write("\n".join(muc_luc) + "\n")
    print(f"  {'README.md':<34} mục lục {len(rows)} file, tổng {tong_mat} ký tự rơi")


if __name__ == "__main__":
    main()
