# Chạy skill trên VPS Ubuntu (OpenClaw)

Skill này thuần Python, không phụ thuộc Microsoft Word hay Windows. Nhưng có
vài chỗ hay vỡ trên VPS mới dựng — dưới đây là toàn bộ.

## Cài nhanh

```bash
bash scripts/setup_ubuntu.sh          # bắt buộc
bash scripts/setup_ubuntu.sh --pdf    # thêm LibreOffice + font để xuất PDF
```

Script tạo `.venv` trong thư mục skill, cài `python-docx` + `jsonschema`, sinh
locale UTF-8 rồi chạy thử bộ đề mẫu.

Cài tay:

```bash
sudo apt update && sudo apt install -y python3 python3-pip python3-venv locales
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python scripts/build_all.py output/KHTN6_MoDau_DaDangChat
```

---

## 6 lỗi hay gặp và cách tránh

### 1. `python: command not found`

Ubuntu chỉ có `python3`, không có alias `python`.

```bash
python3 scripts/build_all.py output/<BO_DE>
```

Trong `.venv` thì `python` tồn tại — nên **luôn dùng venv** để lệnh trong
SKILL.md chạy nguyên văn.

### 2. `error: externally-managed-environment` (Ubuntu 23.10+, 24.04)

`pip install` thẳng vào Python hệ thống bị chặn (PEP 668).

Cách đúng: dùng venv (như trên). Đừng dùng `--break-system-packages`.

### 3. `UnicodeEncodeError` khi in log tiếng Việt

VPS mới thường ở locale `POSIX`/`C`, `print("Nhận biết")` sẽ ném lỗi.

Skill **đã tự phòng**: `docx_common.force_utf8_stdout()` và đoạn tương ứng
trong `check_schema.py` ép `stdout`/`stderr` sang UTF-8 ngay khi import.

Nhưng nên đặt luôn ở tầng hệ thống cho các tiến trình khác của OpenClaw:

```bash
# thêm vào ~/.bashrc hoặc file service của OpenClaw
export LANG=C.UTF-8
export LC_ALL=C.UTF-8
export PYTHONIOENCODING=utf-8
```

Với systemd:

```ini
[Service]
Environment=LANG=C.UTF-8
Environment=PYTHONIOENCODING=utf-8
```

### 4. `FileNotFoundError` khi lưu docx

Xảy ra khi thư mục đích chưa tồn tại. Skill **đã tự phòng**: `save_doc()` gọi
`os.makedirs(..., exist_ok=True)` trước khi ghi.

### 5. Phân biệt HOA/thường trong tên file

Linux phân biệt hoa–thường, Windows thì không. `Bang_Ma_Tran.json` khác
`bang_ma_tran.json`. Ba file JSON **phải đặt đúng tên**:

```
de_bai_tap.json
bang_ma_tran.json
bang_dac_ta_ma_tran.json
```

Tên thư mục bộ đề nên **không dấu, không khoảng trắng**:
`output/KHTN6_MoDau_DaDangChat` ✔ — `output/KHTN 6 mở đầu` ✘.

### 6. Font Times New Roman không có trên Ubuntu

**Không ảnh hưởng việc sinh file .docx** — `python-docx` chỉ ghi tên font vào
XML, không cần font cài trên máy. Mở file trên Windows/Word vẫn đúng font.

Chỉ ảnh hưởng khi **chuyển docx → PDF ngay trên VPS**. Không có font,
LibreOffice thay bằng Liberation Serif — vốn cùng metric với Times New Roman
nên bố cục trang gần như không đổi, chỉ khác nét chữ rất nhẹ.

Muốn giống 100%:

```bash
sudo add-apt-repository -y contrib multiverse
sudo apt install -y ttf-mscorefonts-installer   # cần chấp nhận EULA
sudo fc-cache -f
```

---

## Xuất PDF trên VPS (không có Word)

```bash
soffice --headless -env:UserInstallation=file:///tmp/lo_exam_idea \
        --convert-to pdf --outdir output/<BO_DE> output/<BO_DE>/*.docx
```

Hai lưu ý:

- `-env:UserInstallation=...` bắt buộc khi chạy dưới user không có `$HOME`
  ghi được (systemd service, docker). Thiếu nó LibreOffice treo im lặng ở
  lần chạy đầu.
- Chỉ chạy **một tiến trình soffice tại một thời điểm** cho mỗi profile dir.
  Nếu OpenClaw gọi song song, cấp mỗi lần một `UserInstallation` khác nhau.

---

## Kiểm tra sức khoẻ môi trường

```bash
python3 -c "import docx, sys; print('python-docx OK', sys.version)"
python3 -c "import jsonschema; print('jsonschema OK')"
python3 scripts/build_all.py output/KHTN6_MoDau_DaDangChat
```

Kết quả đúng phải kết thúc bằng `Tong so loi: 0` và 3 dòng `[OK] ....docx`.

---

## Những gì skill KHÔNG cần

- Không cần Microsoft Word, không cần `pywin32`/`win32com`
- Không cần LibreOffice (chỉ cần nếu muốn PDF)
- Không cần mạng khi chạy (chỉ cần lúc `pip install`)
- Không cần quyền root khi chạy (chỉ cần lúc cài gói hệ thống)

> Lưu ý minh bạch: toàn bộ script đã được kiểm chứng chạy đúng trên Windows +
> Python 3.13. Phần Ubuntu ở trên dựa trên rà soát mã nguồn (không có
> `win32com`, không có đường dẫn cứng, mọi `open()` đều `encoding="utf-8"`,
> `python-docx` là thuần Python) chứ **chưa chạy thực tế trên VPS**. Hãy chạy
> `scripts/setup_ubuntu.sh` một lần để xác nhận trước khi dùng cho công việc thật.
