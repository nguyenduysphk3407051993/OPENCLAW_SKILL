#!/usr/bin/env bash
# Dựng môi trường chạy skill exam-latex-creator trên VPS Ubuntu.
#
#   bash scripts/setup_ubuntu.sh          # cài bộ TeX vừa đủ (~1.5 GB)
#   bash scripts/setup_ubuntu.sh --full   # cài texlive-full (~5 GB, chắc chắn nhất)
#
# Sau khi cài, chạy scripts/check_linux.py để xác nhận.

set -euo pipefail

SKILL_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VENV="$SKILL_DIR/.venv"
FULL=0
[[ "${1:-}" == "--full" ]] && FULL=1

echo "==> Skill dir: $SKILL_DIR"

echo "==> Cai Python + locale"
sudo apt-get update -qq
sudo apt-get install -y python3 python3-pip python3-venv locales
if ! locale -a 2>/dev/null | grep -qi 'C.utf8\|en_US.utf8'; then
  sudo locale-gen en_US.UTF-8 || true
  sudo update-locale LANG=en_US.UTF-8 || true
fi

echo "==> Cai TeX Live"
if [[ $FULL -eq 1 ]]; then
  sudo apt-get install -y texlive-full latexmk
else
  # Vừa đủ cho FileMain.tex của skill:
  #   vietnam (vntex)  -> texlive-lang-other      [BẮT BUỘC, tiếng Việt]
  #   subfiles         -> texlive-latex-extra
  #   tikz/pgfplots    -> texlive-pictures
  #   chemfig          -> texlive-science
  #   bbding, fontawesome -> texlive-fonts-extra
  sudo apt-get install -y \
    texlive-latex-base texlive-latex-recommended texlive-latex-extra \
    texlive-lang-other texlive-pictures texlive-science \
    texlive-fonts-recommended texlive-fonts-extra latexmk
fi

echo "==> Tao virtualenv Python: $VENV"
python3 -m venv "$VENV"
"$VENV/bin/pip" install --upgrade pip -q
# python-docx chỉ cần cho: spec_to_exam.py read <bảng đặc tả .docx>
#                          export_pdf.py images <file .docx>
"$VENV/bin/pip" install -q python-docx

echo "==> Kiem tra tuong thich Linux"
"$VENV/bin/python" "$SKILL_DIR/scripts/check_linux.py" || true

cat <<EOF

===============================================================
Xong. Dung skill:

    source $VENV/bin/activate
    python scripts/spec_to_exam.py read <bang_dac_ta> -o plan.json
    python scripts/spec_to_exam.py skeleton plan.json -o latex-output/DE_MADE101.tex
    python scripts/export_pdf.py fix     latex-output/DE_MADE101.tex
    python scripts/export_pdf.py compile DE_MADE101.tex --dir latex-output --times 2 --clean

Neu check_linux.py bao loi HOA/thuong, PHAI sua truoc khi bien dich.
EOF
