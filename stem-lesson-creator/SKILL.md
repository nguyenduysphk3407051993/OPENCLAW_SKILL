---
name: stem-lesson-creator
description: "Soạn KẾ HOẠCH BÀI DẠY STEM (giáo án STEM) chi tiết, hoàn chỉnh và xuất ra file Word (.docx) theo đúng chuẩn định hướng giáo dục STEM của Việt Nam. Skill tự soạn đầy đủ: mục tiêu (kiến thức/năng lực/phẩm chất), thiết bị & học liệu, phân công vai trò kỹ sư cho học sinh, tiến trình từng tiết (lời thoại GV + thao tác HS + thí nghiệm đối chứng), phụ lục công thức, hệ thống phiếu học tập (Notebook) và rubric đánh giá. Phục vụ TOÀN BỘ môn KHTN (Hóa học, Vật lý, Sinh học) làm chủ trì, tích hợp Toán/Công nghệ. Số tiết linh hoạt. Sử dụng khi người dùng nói \"soạn giáo án STEM\", \"kế hoạch bài dạy STEM\", \"làm giáo án STEM về một chủ đề\", \"thiết kế bài học STEM\", hoặc nêu một chủ đề STEM (làm xà phòng, lên men, pin chanh, lọc nước...) và muốn xuất ra Word."
allowed-tools: Read, Write, Bash
argument-hint: "[môn] [lớp] [chủ đề STEM] [số tiết] [sản phẩm đầu ra]"
---

# STEM Lesson Creator — Soạn giáo án STEM chuẩn xuất Word

## Khi yêu cầu chưa đủ cụ thể — PHẢN BIỆN TRƯỚC, LÀM SAU

Yêu cầu chung chung luôn cho ra sản phẩm kém. **Không đoán bừa, cũng không hỏi
lể tể từng ý.** Hãy nêu rõ đang thiếu gì, rồi đưa **một prompt mẫu đã điền sẵn
giá trị mặc định hợp lý** để người dùng sửa và gửi lại trong đúng một lượt.

Thiếu từ **2 tiêu chí trở lên** thì bắt buộc phản biện. Thiếu **đúng 1** tiêu chí
thì tự chọn mặc định, làm tiếp, và nói rõ đã chọn gì.

**Tiêu chí bắt buộc:** môn · lớp · chủ đề STEM · số tiết · sản phẩm đầu ra của học sinh · vật liệu sẵn có

**Mẫu phản biện:**

> Yêu cầu hiện thiếu: **sản phẩm đầu ra**, **vật liệu**. Nếu làm luôn thì tôi phải đoán, dễ lệch
> ý bạn. Bạn copy prompt dưới đây, sửa chỗ in đậm rồi gửi lại:
>
> ```
> Thiết kế bài học STEM môn **KHTN** lớp **8**, chủ đề **Chế tạo mạch điện đơn giản**.
> Số tiết: **3** · Sản phẩm học sinh làm ra: **đèn học dùng pin có công tắc**
> Vật liệu sẵn có: **pin AA, dây điện, bóng LED, bìa carton, băng dính**
> Cần có: **tiêu chí đánh giá sản phẩm**
> ```

---

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


---

## Tương thích đa nền tảng (Windows · Linux · môi trường skill)

Các script Python của skill này đã xử lý sẵn những chỗ hay vỡ khi đổi máy:

| Vấn đề | Đã xử lý thế nào |
|--------|-------------------|
| Console Windows là cp1252/cp437 → in tiếng Việt ném `UnicodeEncodeError` | Mỗi script tự `reconfigure` stdout/stderr sang UTF-8 ngay sau phần import |
| Đọc/ghi file | Luôn khai báo `encoding="utf-8"`; đọc thêm `utf-8-sig` để nuốt BOM của Notepad |
| Ghép đường dẫn | Dùng `os.path.join` / `pathlib`, không nối chuỗi `\` hay `/` |

Khi tự gõ lệnh, tuân thủ thêm 4 điểm sau:

1. **Bọc mọi đường dẫn trong dấu nháy kép** — thư mục tiếng Việt hay có dấu cách.
2. **Linux phân biệt HOA/thường.** `output/` khác `Output/`, `Khaibao/HeaderFooter`
   khác `Khaibao/Headerfooter`. Đặt tên file đầu ra **không dấu, không khoảng trắng**.
3. **Ubuntu không có lệnh `python`**, chỉ có `python3`. Dùng venv
   (`python3 -m venv .venv && source .venv/bin/activate`) để các lệnh trong tài
   liệu này chạy nguyên văn, hoặc thay `python` bằng `python3`.
4. **Không hard-code đường dẫn tuyệt đối** kiểu `D:\...` hay `/home/...` vào file
   cấu hình; luôn tính tương đối từ `<SKILL_DIR>`.

Khi chạy trong bash sandbox, dùng đường dẫn VM mount thay cho đường dẫn Windows.
