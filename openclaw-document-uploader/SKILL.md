---
name: openclaw-document-uploader
description: "Tự động phân loại và lưu trữ các tài liệu được upload định hướng vào thư mục gốc OPENCLAW. Tự động parse tên file để tạo và phân loại vào các thư mục con."
allowed-tools: Read, Write, Bash
argument-hint: "[đường dẫn file tải lên] [thư mục gốc OPENCLAW]"
---

# Kỹ năng Phân loại & Lưu trữ Tài liệu OpenClaw (Document Uploader)

Kỹ năng này cung cấp một bộ khung (framework) để trợ lý AI (Antigravity/OpenClaw Gateway) tự động tiếp nhận tài liệu do người dùng upload, phân tích tên file, và lưu vào đúng cấu trúc thư mục bên trong thư mục gốc `OPENCLAW`.

## Nhiệm vụ chính
- Nhận diện các sự kiện người dùng upload tệp (document, ảnh, PDF, mã nguồn, v.v.).
- Phân tích cú pháp tên file để quyết định phân loại (môn học, dự án, loại dữ liệu, định dạng).
- Tự động tạo cây thư mục con tại thư mục gốc `OPENCLAW` nếu chưa tồn tại.
- Di chuyển/Lưu file an toàn vào đúng điểm đến và báo cáo kết quả cho người dùng.

## Quy trình xử lý (Workflow)

1. **Khởi tạo thư mục gốc:**
   - Luôn kiểm tra và đảm bảo thư mục gốc `OPENCLAW` (hoặc đường dẫn tuyệt đối mà hệ thống thiết lập) tồn tại.
   - Nếu chưa có, tạo mới thư mục này.

2. **Quy tắc phân tích tên file:**
   Suy luận logic từ tên file để tạo cấu trúc cây. Ví dụ quy tắc phổ biến:
   - Nếu tên file chứa các từ khóa giáo dục (ví dụ: `Toan_12_DeThi.pdf`), hãy tự động phân tách thành `OPENCLAW/Toan/Lop_12/DeThi/Toan_12_DeThi.pdf`.
   - Nếu tên file dạng `[Dự án]_[Hạng mục]_[Ngày tháng]` (ví dụ: `DAPhuongNam_BaoCao_2023.docx`), phân tách thành `OPENCLAW/DAPhuongNam/BaoCao/DAPhuongNam_BaoCao_2023.docx`.
   - Nếu không có quy tắc rõ ràng nào trong tên file: Phân chia theo định dạng đuôi file (Extension). Ví dụ: `OPENCLAW/PDF/`, `OPENCLAW/Images/`, `OPENCLAW/Docs/`...
   - Có thể chuẩn hóa tên file (Xóa dấu tiếng Việt, thay khoảng trắng thành `_` hoặc `-`) nếu cần để tránh lỗi hệ thống.

3. **Tiến hành lưu trữ (Tạo thư mục & Di chuyển file):**
   - Chạy lệnh tạo thư mục con đa cấp (tương đương `mkdir -p <đường_dẫn_đích>`).
   - Copy hoặc Move file được tải lên vào `<đường_dẫn_đích>`.
   - Dọn dẹp file tạm (temp files) sau khi di chuyển thành công (nếu có).

4. **Phản hồi người dùng (Telegram/OpenClaw):**
   - Trả lời bằng định dạng Markdown gọn gàng.
   - Ghi rõ đường dẫn thực tế mà file đã được lưu để người dùng biết.
   - Mẫu phản hồi:
     ```markdown
     ✅ **Đã upload và phân loại thành công!**
     - 📄 **Tên file:** `Toan_12_DeThi.pdf`
     - 📂 **Vị trí lưu:** `OPENCLAW/Toan/Lop_12/DeThi/Toan_12_DeThi.pdf`
     ```

## Quy tắc an toàn bắt buộc (Strict Rules)
1. **Sandboxing:** Mọi file tải lên chỉ được phép lưu trong phạm vi thư mục `OPENCLAW/`. Tuyệt đối không được ghi đè hay di chuyển ra các thư mục cấu hình hệ thống khác.
2. **Không ghi đè tự động:** Nếu file đã tồn tại ở đích đến, hãy thêm hậu tố (ví dụ: `_v2`, `_copy`) hoặc thời gian (timestamp) vào tên file để tránh mất dữ liệu của người dùng.
3. **Báo cáo lỗi minh bạch:** Nếu vì lý do nào đó (file hỏng, tên file quá dài do OS giới hạn, không đủ quyền hệ thống) mà không thể di chuyển, phải phản hồi rõ ràng bằng tiếng Việt cho người dùng qua Telegram.
