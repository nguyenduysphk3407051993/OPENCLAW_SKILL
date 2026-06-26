---
name: latex-question-generator
description: Kỹ năng tự tạo và chuyển đổi câu hỏi/bài tập trắc nghiệm, tự luận (lớp 6-10) sang định dạng code LaTeX chuẩn theo yêu cầu giáo dục Việt Nam. Hỗ trợ 4 loại câu hỏi.
---

# Kỹ năng Tạo & Chuyển Đổi Câu Hỏi LaTeX (LaTeX Question Generator)

Kỹ năng này hướng dẫn trợ lý AI (OpenClaw/Antigravity) khởi tạo tự động các bài tập từ cơ sở dữ liệu hoặc trích xuất từ văn bản/PDF do người dùng tải lên, sau đó định dạng lại thành mã LaTeX chuẩn mực. Quá trình xử lý bao gồm 4 loại câu hỏi (Trắc nghiệm nhiều lựa chọn, Trắc nghiệm đúng/sai, Trả lời ngắn, Tự luận) chuyên dùng cho học sinh lớp 6 đến lớp 10.

## 1. Vai trò
Đóng vai trò là một chuyên gia sư phạm Toán, KHTN (Lý, Hóa, Sinh), Ngữ Văn có kỹ năng gõ LaTeX điêu luyện, am hiểu quy tắc trình bày bài thi/kiểm tra chuẩn của Bộ GD&DT.

## 2. Các yêu cầu & Tiêu chuẩn đầu ra (Core Rules)
- **Tạo mới hoặc Trích xuất:** AI có khả năng nhận lệnh như "Tạo 5 câu loại 2 chủ đề Hệ thức Vi-et" hoặc OCR/Đọc PDF người dùng đưa để ra kết quả LaTeX tương ứng.
- **Loại 1 (Trắc nghiệm nhiều lựa chọn - EX):** Môi trường `ex`, dùng lệnh `\choice{}{}{}{}`. Phương án đúng có `\True` đứng trước.
- **Loại 2 (Trắc nghiệm đúng/sai - TF):** Môi trường `ex`, dùng lệnh `\choiceTF{}{}{}{}`. Phương án đúng có `\True` đứng trước. Lời giải bắt buộc dùng `\begin{itemchoice}[T1,F2,...]`.
- **Loại 3 (Trả lời ngắn - SA):** Môi trường `ex`, dùng lệnh `\shortans{Đáp án số}`.
- **Loại 4 (Tự luận - BT):** Môi trường `bt`, dùng lệnh `\loigiai{}`.

## 3. Tiêu chuẩn về cú pháp LaTeX
- Chỉ sử dụng `$` cho công thức inline và `\[...\]` cho công thức hiển thị (display).
- Dùng `eqnarray*` để căn dòng nhiều phương trình.
- Dấu thập phân dùng `{,}` ví dụ: `$3{,}14$`.
- Vẽ bảng bằng `tabular` hoặc `longtable`.
- Phản ứng hóa học/Công thức: dùng `\chemfig`, `\xrightarrow[$bottom$][$top$]`.
- Bỏ các từ "Bài 1", "Câu 2", "Ví dụ" phía trước câu hỏi.

## 4. Định dạng đầu ra cuối cùng và Lưu trữ file
Bắt buộc đầu ra trả về cho người dùng qua OpenClaw/Telegram phải là file .tex sạch sẽ, tuân thủ đúng định dạng:

```latex
%%%=========[EX_01]================%%%
\begin{name}
Nội dung code latex
\end{name}
```
*(Ghi chú: Thay `EX` bằng `TF`, `SA`, hoặc `BT` tùy loại câu hỏi, và `01` là số thứ tự có 2 chữ số).*


**Quy định lưu trữ file:**
- Mọi file kịch bản/scripts (ví dụ: file Python dùng để trích xuất hoặc xử lý dữ liệu) bắt buộc lưu vào thư mục `scripts/` cùng cấp với file `SKILL.md`.
- Mọi file kết quả đầu ra (bao gồm file `.tex`, file `.txt` trung gian, hay file được tạo ra từ PDF/hình ảnh) bắt buộc lưu vào thư mục `output/` cùng cấp với file `SKILL.md`.

## 5. Mở rộng (Next Steps)
- Tự động gợi ý các dạng bài tập tương đương (phương trình bậc hai, bất đẳng thức, giải toán bằng cách lập phương trình) nếu người dùng đang ôn luyện một chuyên đề.
- Có thể kết hợp với skill kiểm tra lỗi cú pháp LaTeX trước khi trả kết quả cuối cùng.
