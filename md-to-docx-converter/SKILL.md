---
name: md-to-docx-converter
description: Kỹ năng chuyển đổi văn bản Markdown (đặc biệt là đề thi trắc nghiệm, tài liệu học tập) sang định dạng Word (.docx) tiêu chuẩn. Hỗ trợ xử lý bảng biểu, công thức toán học, và dàn trang dàn ý trắc nghiệm tự động.
---

# Kỹ năng Chuyển Đổi Markdown sang Word (MD to DOCX Converter)

Kỹ năng này hướng dẫn trợ lý AI (OpenClaw/Antigravity) xử lý và chuyển đổi nội dung từ định dạng Markdown sang file Microsoft Word (.docx), được tối ưu hóa đặc biệt cho các tài liệu giáo dục, đề thi trắc nghiệm và bài tập.

## 1. Vai trò
Đóng vai trò là một chuyên gia xử lý văn bản, hiểu và chuẩn hóa cú pháp Markdown, sau đó tạo ra các file Word có định dạng đẹp, tuân thủ các quy tắc sư phạm (như chia cột trắc nghiệm, định dạng font chữ, công thức toán học đồng bộ).

## 2. Các yêu cầu & Logic xử lý (Core Rules)

Khi được yêu cầu chuyển đổi Markdown sang DOCX, hoặc viết script thực hiện việc chuyển đổi, phải tuân theo đúng tuần tự các bước và logic dưới đây:

### Bước 1: Tiền Xử Lý Markdown (Pre-processing)
Cần xử lý content dạng Markdown để chuẩn bị tốt định dạng và tránh việc các công cụ chuyển đổi làm hỏng cấu trúc.
- **Bảo vệ nội dung Bảng (Table Masking):** 
  - Quét và nhận diện các bảng Markdown trong văn bản. 
  - Chuẩn hóa các bảng: Đảm bảo số lượng cột ở thẻ tiêu đề (header) và thân bảng (body) là bằng nhau (điền thêm khoảng trắng nếu thiếu).
  - Thay thế tạm thời các bảng bằng một placeholder dạng `{{__TABLE_BLOCK_X__}}` để bảo vệ bảng không bị các biểu thức chính quy xử lý văn bản làm vỡ.
- **Xử lý khoảng trắng và ngắt dòng:**
  - Xóa các chuỗi `**` bị dư thừa ở cuối dòng.
  - Bảo toàn ngắt dòng tự nhiên bằng cách thêm 2 dấu cách (`  `) vào cuối mỗi dòng trước ký tự ngắt dòng `\n`.
- **Định dạng tự động tiêu đề và đáp án:**
  - Tách đoạn và In đậm các từ khóa bắt đầu câu hỏi như: `Bài x.`, `Câu x.`, `Ví dụ x.` (Bọc bởi `**...**`).
  - Tách đoạn và In đậm các từ khóa bắt đầu lời giải/đáp án: `Lời giải:`, `Đáp án:`.
- **Dàn trang câu trắc nghiệm (Reformat Quiz Options):**
  - Nhận diện các dòng chứa lựa chọn bắt đầu bằng `A.`, `B.`, `C.`, `D.` hoặc `a)`, `b)`, `c)`, `d)`.
  - Giữ lại đúng format chữ thường/hoa, in đậm ký tự lựa chọn. (Ví dụ: `**A.**` hoặc `**a)**`).
  - Dựa vào độ dài của cụm đáp án lớn nhất để quyết định cách trình bày:
    - **1 dòng (chữ rất ngắn, dưới 22 ký tự):** Ghép 4 đáp án A, B, C, D trên cùng 1 dòng, cách nhau bởi một chuỗi ký hiệu thay thế tab `::::`.
    - **2 dòng (chữ vừa, dưới 45 ký tự):** Ghép A, B trên dòng 1; C, D trên dòng 2, cách nhau bởi `::::`.
    - **4 dòng (chữ dài, >= 45 ký tự):** Mỗi đáp án nằm trên 1 dòng riêng.
- **Khôi phục bảng (Unmask Tables):** 
  - Thay thế lại các placeholder `{{__TABLE_BLOCK_X__}}` thành cụm nội dung bảng Markdown đầy đủ, và loại bỏ các dòng trắng thừa (giới hạn tối đa 2 dòng ngắt liên tiếp).

### Bước 2: Chuyển đổi sang Word (Conversion)
- Sử dụng mô-đun `pypandoc` (gọi đến `pandoc`) để chuyển text Markdown đã tiền xử lý ở trên cấu trúc DOCX.
- Thiết lập định dạng (format) là: `markdown+grid_tables+pipe_tables+backtick_code_blocks`.
- Hỗ trợ truyền vào một Template (`--reference-doc=template.docx`) nếu có yêu cầu định dạng lề sẵn theo form riêng.

### Bước 2.5: Tích hợp hình ảnh bằng AI (AI Image Integration)
- Nếu văn bản, bài tập, hoặc câu hỏi có yêu cầu hình vẽ minh họa (vd: sơ đồ, bộ dụng cụ, đồ thị), trợ lý AI cần **TỰ ĐỘNG**:
  1. Sử dụng skill `ai-image-prompt-creator` để viết ra Prompt tạo ảnh.
  2. Dùng công cụ `generate_image` để tạo ảnh lưu vào hệ thống dưới dạng PNG.
  3. Chèn cú pháp chuẩn Markdown `![Tên ảnh](Đường_dẫn_tuyệt_đối)` vào bề mặt dữ liệu file MD. Hệ thống Pandoc sẽ tự động bắt lấy và gắp chúng vô Word Document ở Bước 3.

### Bước 3: Hậu xử lý File Word (Post-processing)
Sau khi tạo file DOCX, cần can thiệp qua thư viện `python-docx` để tinh chỉnh chi tiết:
- **Đồng bộ Font chữ tổng thể:**
  - Mục tiêu cho toàn bộ văn bản (bao gồm bảng): Font `Times New Roman`, Kích thước `12pt`.
  - Chỉnh sửa thuộc tính EastAsia (`w:eastAsia`) cũng dùng `Times New Roman`.
- **Xử lý Font Công thức Toán (Math Equations):**
  - Quét các phần tử toán học `m:r`, thêm nhánh `w:rFonts` chỉ định `Times New Roman` cho `ascii`, `hAnsi`, `cs`, và `eastAsia` để công thức tương đồng với văn bản.
- **Tô màu Text Đặc biệt (Quan trọng):**
  - Chú ý đặc biệt: Phải thiết lập và hiển thị màu sắc Xanh dương đậm (`RGB(0, 0, 255)`) đối với các Chữ `Câu`, `Bài` cộng số thứ tự (ví dụ: `Câu 1.`, `Bài 2.`) và các ký tự phương án trắc nghiệm in đậm.
- **Vị trí Tab & Lề các Phương án (Tuyệt đối):**
  - Mặc định, file Word được chốt thiết lập các lề giấy cốt lõi: Top = 1cm, Bottom = 1cm, Left = 2cm, Right = 1cm. Do đó không gian văn bản chiều ngang (Text width) trên khổ A4 luôn vừa khít **18 cm**.
  - Toàn bộ các dòng chứa phương án (A, B, C, D) phải được thiết lập lề trái (left indent) cứng là **0 cm**. Không sử dụng thụt lề treo (first line indent).
  - Khớp với việc gắn biến `::::` ngay đằng trước tất cả phương án, số cột biểu thị qua số điểm Left Tab Stop:
    - 4 cột (4 phương án 1 dòng): Đặt Left Tab lần lượt tại **0.5 cm**, **4.5 cm**, **9.0 cm**, **13.5 cm**.
    - 3 cột (3 phương án 1 dòng): Đặt Left Tab lần lượt tại **0.5 cm**, **6.0 cm**, **12.0 cm**.
    - 2 cột (2 phương án 1 dòng): Đặt Left Tab lần lượt tại **0.5 cm**, **9.0 cm**.
    - 1 cột (1 phương án dải đều): Đặt Left Tab tại duy nhất **0.5 cm**.
- **Dọn dẹp:**
  - Loại bỏ các ký tự rác từ Markdown vô tình sót lại như cặn `**` hay chuỗi list hoa thị đầu dòng lặp lại `* `.

## 3. Quy định lưu trữ
- Code mẫu hoặc script bằng Python (.py) sử dụng cho logic chuyển đổi này phải lưu trong thư mục `scripts/` cùng cấp với file `SKILL.md`.
- File đầu ra (file Word `.docx`) sẽ được lưu mặc định trong thư mục `output/` nếu không có cấu hình đường dẫn khác từ phía người dùng.
