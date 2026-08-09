# -*- coding: utf-8 -*-
"""Kiểm tra skill có chạy được trên Linux (VPS Ubuntu) hay không.

Linux phân biệt HOA/thường trong tên file, còn Windows thì không. Vì vậy một
file .tex chạy tốt trên Windows có thể vỡ trên VPS chỉ vì `\\input{Khaibao/dethi}`
trong khi file thật tên `Khaibao/DETHI.tex`. Script này soi trước các lỗi đó.

Dùng:
    python scripts/check_linux.py              # kiểm tra latex-output/
    python scripts/check_linux.py <thư mục>
"""

from __future__ import annotations

import os
import re
import shutil
import subprocess
import sys

for _s in (sys.stdout, sys.stderr):
    if (getattr(_s, "encoding", "") or "").lower().replace("-", "") not in \
            ("utf8", "utf_8") and hasattr(_s, "reconfigure"):
        try:
            _s.reconfigure(encoding="utf-8", errors="replace")
        except (ValueError, OSError):
            pass

SKILL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INPUT_RE = re.compile(r"\\(?:input|include|subfile|subfileinclude)\s*\{([^}]+)\}")
PKG_RE = re.compile(r"\\usepackage(?:\[[^\]]*\])?\s*\{([^}]+)\}")

# Gói LaTeX skill cần, kèm tên gói apt chứa nó trên Ubuntu
GOI_CAN = {
    "vietnam": "texlive-lang-other",
    "subfiles": "texlive-latex-extra",
    "tkz-tab": "texlive-pictures",
    "tikz": "texlive-pictures",
    "pgfplots": "texlive-pictures",
    "chemfig": "texlive-science",
    "circuitikz": "texlive-pictures",
    "bbding": "texlive-fonts-extra",
    "fontawesome5": "texlive-fonts-extra",
}


def _norm(p):
    return os.path.normpath(p).replace("\\", "/").lstrip("./")


def quet_file_thuc(goc):
    thuc = set()
    for root, _dirs, names in os.walk(goc):
        for n in names:
            thuc.add(_norm(os.path.relpath(os.path.join(root, n), goc)))
    return thuc


def kiem_tra_input(goc):
    """Đối chiếu mọi \\input/\\include với file thật, phân biệt HOA/thường."""
    thuc = quet_file_thuc(goc)
    thuc_low = {p.lower(): p for p in thuc}

    tex_files = [p for p in thuc if p.lower().endswith(".tex")]
    lech, thieu, n_ref = [], [], 0
    for rel in sorted(tex_files):
        try:
            with open(os.path.join(goc, rel), "r", encoding="utf-8",
                      errors="ignore") as f:
                noi_dung = f.read()
        except OSError:
            continue
        for m in INPUT_RE.finditer(noi_dung):
            tham_chieu = m.group(1).strip()
            if not tham_chieu or "#" in tham_chieu:
                continue
            # bỏ qua dòng đã bị chú thích bằng % (không tính \% escape)
            dau_dong = noi_dung.rfind("\n", 0, m.start()) + 1
            truoc = noi_dung[dau_dong:m.start()]
            if re.search(r"(?<!\\)%", truoc):
                continue
            n_ref += 1
            ung_vien = [_norm(tham_chieu), _norm(tham_chieu + ".tex")]
            if any(c in thuc for c in ung_vien):
                continue                       # khớp chính xác - Linux OK
            khop_low = next((thuc_low[c.lower()] for c in ung_vien
                             if c.lower() in thuc_low), None)
            if khop_low:
                lech.append((rel, tham_chieu, khop_low))
            else:
                thieu.append((rel, tham_chieu))
    return n_ref, lech, thieu


def kiem_tra_goi(goc):
    goi = set()
    for root, _dirs, names in os.walk(goc):
        for n in names:
            if not n.lower().endswith(".tex"):
                continue
            try:
                with open(os.path.join(root, n), "r", encoding="utf-8",
                          errors="ignore") as f:
                    for m in PKG_RE.finditer(f.read()):
                        for g in m.group(1).split(","):
                            goi.add(g.strip())
            except OSError:
                pass
    return goi


def main():
    goc = sys.argv[1] if len(sys.argv) > 1 else os.path.join(SKILL_DIR, "latex-output")
    goc = os.path.abspath(goc)
    print(f"Thu muc kiem tra: {goc}")
    print("=" * 64)
    loi = 0

    # 1. Tên file phân biệt HOA/thường
    n_ref, lech, thieu = kiem_tra_input(goc)
    print(f"[1] Tham chieu \\input/\\include: {n_ref}")
    if lech:
        loi += len(lech)
        print(f"    [LOI] {len(lech)} tham chieu SAI HOA/THUONG - "
              f"chay duoc tren Windows nhung VO tren Linux:")
        for src, ref, that in lech[:20]:
            print(f"      {src}: \\input{{{ref}}}  ->  file that: {that}")
    if thieu:
        print(f"    [CANH BAO] {len(thieu)} tham chieu khong tim thay file "
              f"(co the la goi he thong):")
        for src, ref in thieu[:10]:
            print(f"      {src}: \\input{{{ref}}}")
    if not lech and not thieu:
        print("    [OK] moi tham chieu khop chinh xac ten file")

    # 2. Tên file/thư mục có dấu hoặc khoảng trắng
    xau = [p for p in quet_file_thuc(goc)
           if any(ord(c) > 127 for c in p) or " " in p]
    print(f"[2] Ten file co dau/khoang trang: {len(xau)}")
    if xau:
        print("    [CANH BAO] nen doi ten thanh khong dau, khong khoang trang:")
        for p in xau[:10]:
            print(f"      {p}")

    # 3. Công cụ biên dịch
    print("[3] Cong cu:")
    for ten, goi_apt in (("pdflatex", "texlive-latex-base"),
                         ("latexmk", "latexmk")):
        d = shutil.which(ten)
        if d:
            print(f"    [OK] {ten}: {d}")
        else:
            loi += (ten == "pdflatex")
            print(f"    [{'LOI' if ten == 'pdflatex' else 'CB '}] khong co {ten}"
                  f"  ->  sudo apt install {goi_apt}")

    # 4. Gói LaTeX
    goi = kiem_tra_goi(goc)
    can = sorted(g for g in goi if g in GOI_CAN)
    print(f"[4] Goi LaTeX dac biet dang dung: {', '.join(can) or '(khong)'}")
    if can:
        apt = sorted({GOI_CAN[g] for g in can})
        print(f"    Tren Ubuntu can: sudo apt install {' '.join(apt)}")
    print("    Cach chac chan nhat: sudo apt install texlive-full  (~5 GB)")

    # 5. Kiểm tra gói thật sự dùng được (nếu có kpsewhich)
    if shutil.which("kpsewhich"):
        thieu_goi = []
        for g in can:
            try:
                r = subprocess.run(["kpsewhich", g + ".sty"],
                                   capture_output=True, text=True)
                if not r.stdout.strip():
                    thieu_goi.append(g)
            except OSError:
                break
        if thieu_goi:
            loi += len(thieu_goi)
            print(f"    [LOI] chua cai cac goi: {', '.join(thieu_goi)}")
        else:
            print("    [OK] cac goi tren deu da co trong he thong TeX")

    print("=" * 64)
    print(f"Tong so loi chan Linux: {loi}")
    return 1 if loi else 0


if __name__ == "__main__":
    sys.exit(main())
