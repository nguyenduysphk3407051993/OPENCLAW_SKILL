---
name: latex-question-generator
description: Kỹ năng tự tạo và chuyển đổi câu hỏi/bài tập trắc nghiệm, tự luận (lớp 6-10) sang định dạng code LaTeX chuẩn theo yêu cầu giáo dục Việt Nam. Hỗ trợ 4 loại câu hỏi.
---

# Kỹ năng Tạo & Chuyển Đổi Câu Hỏi LaTeX (LaTeX Question Generator)

Kỹ năng này hướng dẫn trợ lý AI (OpenClaw/Antigravity) khởi tạo tự động các bài tập từ cơ sở dữ liệu hoặc trích xuất từ văn bản/PDF do người dùng tải lên, sau đó định dạng lại thành mã LaTeX chuẩn mực. Quá trình xử lý bao gồm 4 loại câu hỏi (Trắc nghiệm nhiều lựa chọn, Trắc nghiệm đúng/sai, Trả lời ngắn, Tự luận) chuyên dùng cho học sinh lớp 6 đến lớp 10.

## Khi yêu cầu chưa đủ cụ thể — PHẢN BIỆN TRƯỚC, LÀM SAU

Yêu cầu chung chung luôn cho ra sản phẩm kém. **Không đoán bừa, cũng không hỏi
lể tể từng ý.** Hãy nêu rõ đang thiếu gì, rồi đưa **một prompt mẫu đã điền sẵn
giá trị mặc định hợp lý** để người dùng sửa và gửi lại trong đúng một lượt.

Thiếu từ **2 tiêu chí trở lên** thì bắt buộc phản biện. Thiếu **đúng 1** tiêu chí
thì tự chọn mặc định, làm tiếp, và nói rõ đã chọn gì.

**Tiêu chí bắt buộc:** môn · lớp · chủ đề · loại câu hỏi · số lượng · mức độ

**Mẫu phản biện:**

> Yêu cầu hiện thiếu: **số lượng**, **mức độ**. Nếu làm luôn thì tôi phải đoán, dễ lệch
> ý bạn. Bạn copy prompt dưới đây, sửa chỗ in đậm rồi gửi lại:
>
> ```
> Tạo câu hỏi LaTeX môn **Hoá học** lớp **9**, chủ đề **Acid – Base – Muối**.
> Loại **1 (trắc nghiệm)**: **8** câu · Loại **4 (tự luận)**: **2** câu
> Mức độ: Nhận biết **3** câu, Thông hiểu **4** câu, Vận dụng **3** câu
> Có lời giải chi tiết: **có**
> ```

---

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
