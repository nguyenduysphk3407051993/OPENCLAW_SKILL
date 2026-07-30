# Mẫu template yêu cầu (hiển thị cho người dùng duyệt)

> Khi người dùng gọi skill mà yêu cầu **chưa đầy đủ thông tin**, hãy nhận diện ý định rồi
> hiển thị **đúng 1 mẫu** bên dưới (đặt trong code block để dễ copy), mời người dùng điền/duyệt,
> rồi mới tạo. Nếu yêu cầu đã đủ thông tin thì bỏ qua bước hiển thị và làm luôn.

## Nhận diện ý định → chọn mẫu

| Tín hiệu trong yêu cầu | Mẫu hiển thị |
|------------------------|--------------|
| "tạo câu hỏi", "soạn câu", "vài câu", "bài tập lẻ" | Mẫu 1 |
| "tạo đề", "đề thi", "đề kiểm tra", "đề ôn tập", có cấu trúc nhiều phần | Mẫu 2 |
| "trích xuất", "chuyển sang LaTeX", có đính kèm file pdf/docx/ảnh | Mẫu 3 |
| "ghép đề", "trộn đề", "gộp file .tex", "tạo mã đề mới" | Mẫu 4 |
| Không rõ ý định | Hiển thị cả 4 mẫu (tóm tắt) và hỏi người dùng chọn |

---

## Mẫu 1 — Tạo câu hỏi lẻ

```
/exam-latex-creator
Loại câu hỏi: [1 (trắc nghiệm) | 2 (đúng/sai) | 3 (trả lời ngắn) | 4 (tự luận)]
Số lượng: [số câu]
Môn: [KHTN | Hóa | Lý | Sinh | Toán | Văn]
Lớp: [6 | 7 | 8 | 9 | 10 | 11 | 12]
Chương: [tên hoặc số chương]
Bài: [tên hoặc số bài, bỏ trống nếu muốn cả chương]
Mức độ: [Nhận biết | Thông hiểu | Vận dụng | Vận dụng cao | Hỗn hợp]
Yêu cầu thêm: [có lời giải | không lời giải | có hình ảnh | ...]
```

**Ví dụ điền:**

```
/exam-latex-creator
Loại câu hỏi: 1 (trắc nghiệm)
Số lượng: 10
Môn: KHTN
Lớp: 8
Chương: 2 - Phản ứng hóa học
Bài: Bài 5 - Định luật bảo toàn khối lượng
Mức độ: Hỗn hợp
Yêu cầu thêm: có lời giải chi tiết
```

---

## Mẫu 2 — Tạo đề thi hoàn chỉnh

```
/exam-latex-creator TẠO ĐỀ THI
Môn: [...]
Lớp: [...]
Tên đề: [Kiểm tra giữa kỳ 1 | Kiểm tra cuối kỳ 2 | Ôn tập chương 3 | ...]
Năm học: [2025 - 2026]
Ngày kiểm tra: [dd/mm/yyyy]
Thời gian: [45 | 60 | 90 | 120] phút
Mã đề: [101]
Phạm vi: [Chương 1-3 | Bài 1-5 chương 2 | Cả học kỳ 1 | ...]

Cấu trúc đề:
- Phần 1 (Trắc nghiệm): [số] câu
- Phần 2 (Đúng/sai): [số] câu
- Phần 3 (Trả lời ngắn): [số] câu
- Phần 4 (Tự luận): [số] câu

Phân bố mức độ: [Nhận biết 40% | Thông hiểu 30% | Vận dụng 20% | VD cao 10%]
Yêu cầu thêm: [có lời giải | trộn thêm mã đề 102, 103 | xuất PDF | ...]
```

**Ví dụ điền:**

```
/exam-latex-creator TẠO ĐỀ THI
Môn: KHTN
Lớp: 9
Tên đề: Kiểm tra giữa kỳ 1
Năm học: 2025 - 2026
Ngày kiểm tra: 15/10/2025
Thời gian: 90 phút
Mã đề: 101
Phạm vi: Chương 1-4

Cấu trúc đề:
- Phần 1 (Trắc nghiệm): 16 câu
- Phần 2 (Đúng/sai): 4 câu
- Phần 3 (Trả lời ngắn): 4 câu
- Phần 4 (Tự luận): 2 câu

Phân bố mức độ: Nhận biết 40% | Thông hiểu 30% | Vận dụng 20% | VD cao 10%
Yêu cầu thêm: có lời giải, trộn thêm mã đề 102 và 103, xuất PDF
```

---

## Mẫu 3 — Trích xuất & chuyển đổi

```
/exam-latex-creator TRÍCH XUẤT
File đính kèm: [đính kèm file pdf/docx/ảnh]
Loại câu hỏi cần chuyển: [1 | 2 | 3 | 4 | tự nhận diện]
Môn: [...]
Lớp: [...]
Yêu cầu: [chuyển sang LaTeX | gán ID6 | thêm lời giải | sửa lỗi nội dung | ...]
```

---

## Mẫu 4 — Ghép & trộn đề từ file có sẵn

```
/exam-latex-creator GHÉP ĐỀ
File nguồn: [file1.tex, file2.tex, ...]
Môn: [...]
Lớp: [...]
Tên đề: [...]
Ngày kiểm tra: [dd/mm/yyyy]
Thời gian: [phút]
Mã đề gốc: [101]
Trộn thêm mã đề: [102, 103] (seed tự động)
Xuất PDF: [có | không]
```
