# exam-idea

Skill OPENCLAW: xây dựng bộ đề bài tập + ma trận + bảng đặc tả cho các môn
Khoa học tự nhiên, Toán, Vật lí, Hoá học, Sinh học lớp 6–12.

Đọc `SKILL.md` để biết quy trình đầy đủ.

## Cài đặt

```bash
pip install -r requirements.txt
```

**VPS Ubuntu** (cách được khuyến nghị — tạo venv, sinh locale UTF-8, chạy thử):

```bash
bash scripts/setup_ubuntu.sh          # thêm --pdf nếu muốn xuất PDF bằng LibreOffice
source .venv/bin/activate
```

Ubuntu không có lệnh `python`, chỉ có `python3`. Dùng venv để các lệnh dưới đây
chạy nguyên văn. Các lỗi môi trường thường gặp (locale, PEP 668, font, phân biệt
hoa–thường): xem `references/chay-tren-ubuntu-vps.md`.

## Dùng nhanh

```bash
# 1. Tạo thư mục bộ đề mới (nhanh nhất là sao chép bộ đề mẫu)
cp -r output/KHTN6_MoDau_DaDangChat output/BO_DE_MOI

# 2. Sửa 3 file JSON trong thư mục đó
#    de_bai_tap.json · bang_ma_tran.json · bang_dac_ta_ma_tran.json

# 3. Kiểm tra + xuất 3 file Word
python scripts/build_all.py output/BO_DE_MOI
```

Kết quả:

| File | Nội dung |
|------|----------|
| `1_Cac_dang_bai_tap.docx` | Mục tiêu cần đạt · Hệ thống dạng bài tập · Đề minh hoạ · Đáp án |
| `2_Bang_ma_tran.docx` | Ma trận, A4 ngang, đúng form mẫu |
| `3_Bang_dac_ta.docx` | Bảng đặc tả, A4 ngang, đúng form mẫu |

## Đóng gói lại thành .zip

```bash
python scripts/package.py              # -> ../exam-idea.zip
python scripts/package.py --no-demo    # chỉ khung skill, bỏ output/
python scripts/package.py -o /tmp/x.zip
```

Zip chứa đúng một thư mục gốc `exam-idea/` theo quy ước OpenClaw; tự loại
`__pycache__`, `.venv`, `.claude` và các file làm việc ở thư mục gốc; giữ
quyền thực thi 0755 cho `setup_ubuntu.sh`.

## Vì sao đi qua JSON?

Bảng ma trận và bảng đặc tả có cấu trúc gộp ô phức tạp (4 dòng tiêu đề, gộp
dọc theo chủ đề, 3 dòng chân bảng). Sửa trực tiếp trên Word rất dễ vỡ form.

Với skill này: **JSON là nguồn sự thật duy nhất**, script dựng lại docx từ đầu
mỗi lần chạy nên form không bao giờ hỏng. Đổi số mức độ từ 3 sang 4, thêm chủ
đề, thêm đơn vị kiến thức — bảng tự giãn đúng.

## Ba lớp kiểm tra trước khi xuất file

1. `check_schema.py` — cú pháp JSON (đúng khoá, đúng kiểu)
2. `validate.py` — đồng bộ nội dung:
   - chủ đề / đơn vị kiến thức khớp giữa ma trận và đặc tả
   - số lệnh hỏi từng ô khớp tuyệt đối
   - tổng điểm và tỉ lệ mức độ đạt yêu cầu
   - số câu trong đề khớp ma trận (loại 2 = 4 ý, loại 4 = 2 ý)
3. Mắt thường — mở docx đối chiếu với `assets/mau_bang_*.docx`

Form mẫu có hai biến thể: bản gốc 3 mức độ (Biết / Hiểu / Vận dụng) theo form
của Bộ, và bản `*_4mucdo.docx` thêm mức *Liên hệ thực tế* — dùng bản 4 mức khi
đối chiếu các bộ đề trong `output/`. Sinh lại bằng:

```bash
python assets/tao_form_mau.py --muc-do 4      # bỏ cờ để lấy bản 3 mức
```

## Bộ đề mẫu có sẵn

`output/KHTN6_MoDau_DaDangChat/` — KHTN 6, chủ đề *Mở đầu về Khoa học tự nhiên*
và *Đa dạng chất – Các thể của chất*:

- 12 câu loại 1 + 4 câu loại 2 + 2 câu loại 3 + 3 câu loại 4
- Quy đổi: 12 + 16 + 2 + 6 = **36 lệnh hỏi**
- Tỉ lệ Nhận biết : Thông hiểu : Vận dụng : Liên hệ thực tế = **50 : 30 : 10 : 10**
- Tổng **10,0 điểm**, validate 0 lỗi

## Quy tắc đếm lệnh hỏi

| Loại câu hỏi | Lệnh hỏi / câu |
|--------------|----------------|
| 1 – Trắc nghiệm nhiều lựa chọn | 1 |
| 2 – Đúng/Sai | 4 (ý a, b, c, d) |
| 3 – Trả lời ngắn | 1 |
| 4 – Tự luận | **2** (ý a, b) |

Ma trận và bảng đặc tả **luôn đếm theo lệnh hỏi**, không đếm theo câu. Các ý
trong cùng một câu có thể ở các mức độ khác nhau — đây là công cụ chính để
đạt tỉ lệ mức độ khớp tuyệt đối.
