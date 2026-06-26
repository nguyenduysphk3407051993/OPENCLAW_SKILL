---
name: stem-lesson-creator
description: >-
  Soạn KẾ HOẠCH BÀI DẠY STEM (giáo án STEM) chi tiết, hoàn chỉnh và xuất ra
  file Word (.docx) theo đúng chuẩn định hướng giáo dục STEM của Việt Nam.
  Skill tự soạn đầy đủ: mục tiêu (kiến thức/năng lực/phẩm chất), thiết bị & học
  liệu, phân công vai trò kỹ sư cho học sinh, tiến trình từng tiết (lời thoại
  GV + thao tác HS + thí nghiệm đối chứng), phụ lục công thức, hệ thống phiếu
  học tập (Notebook) và rubric đánh giá. Phục vụ TOÀN BỘ môn KHTN (Hóa học, Vật
  lý, Sinh học) làm chủ trì, tích hợp Toán/Công nghệ. Số tiết linh hoạt. Sử
  dụng khi người dùng nói "soạn giáo án STEM", "kế hoạch bài dạy STEM", "làm
  giáo án STEM về một chủ đề", "thiết kế bài học STEM", hoặc nêu một chủ đề STEM
  (làm xà phòng, lên men, pin chanh, lọc nước...) và muốn xuất ra Word.
---

# STEM Lesson Creator — Soạn giáo án STEM chuẩn xuất Word

## 1. Skill này làm gì

Tạo một **Kế hoạch bài dạy STEM** hoàn chỉnh, chi tiết đến mức giáo viên cầm lên
dạy ngay được, rồi xuất thành `.docx` định dạng đẹp (Times New Roman 12pt,
heading đậm, bảng số liệu, phiếu học tập, rubric).

Triết lý cốt lõi của giáo án STEM chuẩn (PHẢI bám sát):

- **Bài toán thực tế dẫn dắt**: mở đầu bằng vấn đề đời sống / bối cảnh địa
  phương, không dạy lý thuyết suông.
- **Học sinh đóng vai kỹ sư/chuyên gia**: nhóm có vai trò rõ ràng (kỹ sư trưởng,
  kỹ sư hóa chất, kỹ sư năng lượng, chuyên viên dữ liệu...).
- **Thí nghiệm đối chứng**: thay đổi biến số để rút ra kết luận khoa học.
- **Tích hợp liên môn thật sự**: KHTN chủ trì + Toán (hiệu suất, đồ thị) +
  Công nghệ/Vật lý.
- **Định lượng & xử lý số liệu**: có công thức, bảng số liệu, biểu đồ, tính
  hiệu suất — HS dùng con số để biện luận.
- **Sản phẩm + phản biện cuối**: kết thúc bằng báo cáo/thuyết trình/"Shark Tank".
- **Vật liệu rẻ, dễ kiếm**: ưu tiên dụng cụ gia dụng, ghi rõ giá tiền & nơi mua.

## 2. Quy trình thực hiện (BẮT BUỘC theo thứ tự)

### Bước 1 — Làm rõ yêu cầu (nếu thiếu)
Xác định: chủ đề/sản phẩm STEM; môn chủ trì (Hóa/Lý/Sinh) + lớp/khối; số tiết
(mặc định gợi ý theo độ phức tạp — xem mục 3); bối cảnh địa phương (nếu có) để
gắn tình huống thực tế. Nếu người dùng đã nêu rõ chủ đề, chủ động chọn mặc định
hợp lý và soạn ngay, nêu rõ giả định đã dùng.

### Bước 2 — Nghiên cứu nội dung chuyên môn
Đọc `reference/structure.md` (khung 6 phần) và `reference/style_guide.md`
(văn phong, ngân hàng vai trò & hoạt động). Tự xây dựng: bản chất khoa học
(phản ứng/hiện tượng + công thức); ít nhất MỘT thí nghiệm đối chứng có biến số
rõ; bài toán định lượng phù hợp khối lớp. Cần số liệu thực tế (nhiệt trị, nồng
độ, giá vật liệu...) thì dùng WebSearch kiểm chứng.

### Bước 3 — Viết file nội dung JSON
Tạo `content.json` theo schema tại `reference/schema.md`. Điền ĐẦY ĐỦ, chi tiết:
lời thoại GV nguyên văn, thao tác HS cụ thể, số liệu mẫu có thật, phiếu học tập
có chỗ trống điền. Tham khảo `examples/example_content.json`.

### Bước 4 — Render ra Word
```bash
python3 scripts/build_docx.py content.json "Ten_file_dau_ra.docx"
```
Script tự định dạng TNR 12pt, heading đậm, bảng có nền tiêu đề, phiếu học tập,
rubric. Lưu `.docx` vào thư mục của người dùng.

### Bước 5 — Kiểm tra (verification)
Mở lại docx (đọc bằng python-docx) xác nhận đủ 6 phần, đủ số tiết, bảng render
đúng. Rà soát: mỗi tiết có mục tiêu + 2-3 hoạt động có mốc thời gian; ≥1 thí
nghiệm đối chứng; có công thức & phiếu học tập; tổng thời lượng mỗi tiết ≈ 45'.

## 3. Gợi ý số tiết theo độ phức tạp

| Quy mô chủ đề | Số tiết |
|---|---|
| Một thí nghiệm/sản phẩm đơn giản | 1–2 |
| Có thí nghiệm đối chứng + xử lý số liệu | 3 |
| Quy trình nhiều giai đoạn + tính toán + phản biện | 5 (chuẩn đầy đủ) |
| Dự án lớn liên môn sâu | 6–7 |

Khung 5 tiết kinh điển: (1) Thiết lập bài toán + chuẩn bị nền → (2) Thực hành
biến số chính → (3) Xử lý/định lượng vật lý → (4) Toán học STEM xử lý số liệu →
(5) Phản biện/thuyết trình sản phẩm.

## 4. Tài liệu trong skill
- `reference/structure.md` — khung 6 phần bắt buộc.
- `reference/style_guide.md` — văn phong, ngân hàng vai trò, mẫu hoạt động.
- `reference/schema.md` — đặc tả JSON đầy đủ.
- `scripts/build_docx.py` — bộ render JSON → Word.
- `examples/example_content.json` — giáo án mẫu hoàn chỉnh.

## 5. Lưu ý chất lượng
KHÔNG viết chung chung ("học sinh làm thí nghiệm"). PHẢI cụ thể: dùng gì, bao
nhiêu gram/ml, thao tác ra sao, hiện tượng quan sát là gì. Lời thoại GV viết như
kịch bản thật, có câu hỏi kích não. Mọi số liệu mẫu hợp lý khoa học. Dùng tiếng
Việt, thuật ngữ chuẩn chương trình GDPT 2018.
