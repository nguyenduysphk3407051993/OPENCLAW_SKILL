#!/usr/bin/env bash
# Cài đặt môi trường chạy skill exam-idea trên VPS Ubuntu (20.04 / 22.04 / 24.04).
#
#   bash scripts/setup_ubuntu.sh            # chỉ cài phần bắt buộc
#   bash scripts/setup_ubuntu.sh --pdf      # cài thêm LibreOffice + font để xuất PDF
#
# Script dùng venv nên không đụng tới Python hệ thống (tránh lỗi
# "externally-managed-environment" của Ubuntu 24.04).

set -euo pipefail

SKILL_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VENV="$SKILL_DIR/.venv"
WITH_PDF=0
[[ "${1:-}" == "--pdf" ]] && WITH_PDF=1

echo "==> Skill dir: $SKILL_DIR"

# ---------------------------------------------------------------- gói hệ thống
echo "==> Cài gói hệ thống"
sudo apt-get update -qq
sudo apt-get install -y python3 python3-pip python3-venv locales

# Locale UTF-8: bắt buộc để in tiếng Việt ra terminal không lỗi
if ! locale -a 2>/dev/null | grep -qi 'C.utf8\|en_US.utf8'; then
  echo "==> Sinh locale UTF-8"
  sudo locale-gen en_US.UTF-8 || true
  sudo update-locale LANG=en_US.UTF-8 || true
fi

if [[ $WITH_PDF -eq 1 ]]; then
  echo "==> Cài LibreOffice + font (để chuyển docx -> pdf)"
  sudo apt-get install -y libreoffice-writer fonts-liberation
  # Font Times New Roman thật (tuỳ chọn, cần kho contrib và chấp nhận EULA).
  # Không có cũng được: LibreOffice thay bằng Liberation Serif, cùng metric
  # nên bố cục trang gần như không đổi.
  # sudo apt-get install -y ttf-mscorefonts-installer
fi

# ------------------------------------------------------------------- venv
echo "==> Tạo virtualenv: $VENV"
python3 -m venv "$VENV"
"$VENV/bin/pip" install --upgrade pip -q
"$VENV/bin/pip" install -q -r "$SKILL_DIR/requirements.txt"

# ---------------------------------------------------------------- kiểm thử
echo "==> Chạy thử bộ đề mẫu"
"$VENV/bin/python" "$SKILL_DIR/scripts/build_all.py" \
  "$SKILL_DIR/output/KHTN6_MoDau_DaDangChat"

cat <<EOF

===============================================================
Cài đặt xong. Từ giờ dùng:

    $VENV/bin/python $SKILL_DIR/scripts/build_all.py <thư mục bộ đề>

Hoặc kích hoạt venv một lần rồi gõ ngắn:

    source $VENV/bin/activate
    python scripts/build_all.py output/<BO_DE>
EOF

if [[ $WITH_PDF -eq 1 ]]; then
  cat <<'EOF'

Xuất PDF (không cần Microsoft Word):

    soffice --headless -env:UserInstallation=file:///tmp/lo_exam_idea \
            --convert-to pdf --outdir output/<BO_DE> output/<BO_DE>/*.docx
EOF
fi
