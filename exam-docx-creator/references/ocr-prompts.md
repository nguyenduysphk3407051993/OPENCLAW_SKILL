# OCR Prompts — Tham chiếu

Các prompt dưới đây được sử dụng trong `ocr_to_docx.py` để gọi Gemini Vision API.
Giữ nguyên từ `ocr_service.py` trong dự án chính.

## PROMPT_WORD_PAGE (mode: page)

Dùng khi OCR **cả trang** tài liệu:

```
Ban la chuyen gia OCR tai lieu de chuyen sang Microsoft Word.
Hay trich xuat toan bo noi dung trang nay thanh Markdown sach,
toi uu de doi sang .docx.

QUY TAC:
1. Bao toan thu tu doc va cau truc tai lieu.
2. Tieu de dung #, ##, ### khi ro rang.
3. Doan van viet bang Markdown thuong.
4. Danh sach dung - hoac 1.
5. Bang ro rang thi dung bang Markdown.
6. Cong thuc inline dung $...$, cong thuc rieng dong bat buoc dung \[...\].
7. Tieng Viet giu nguyen dau, khong dich.
8. Khong dua chu tieng Viet vao trong $...$ hoac \[...\].
9. Neu bat buoc phai co chu trong cong thuc, dung ASCII khong dau trong \text{...}.
10. Khong them code fence, khong them loi mo dau/ket luan, khong giai thich.
11. Neu la cau trac nghiem co phuong an A., B., C., D. thi dat moi phuong an tren mot dong rieng.
12. Neu co cac y nho a., b., c., d. hoac a), b), c), d) thi dat moi y tren mot dong rieng.
```

## PROMPT_WORD_SINGLE (mode: single)

Dùng khi OCR **1 công thức** hoặc **1 ảnh nhỏ**:

```
Ban la chuyen gia OCR tai lieu de chuyen sang Microsoft Word.
Hay trich xuat noi dung trong anh thanh Markdown sach,
toi uu de doi sang .docx.

QUY TAC:
1. Van ban thuong giu dang doan van Markdown.
2. Cong thuc inline dung $...$, cong thuc rieng dong bat buoc dung \[...\].
3. Neu anh chi co 1 cong thuc, chi tra ve \[...\].
4. Tieu de dung #, ## khi thuc su co tieu de.
5-12. (Tương tự PROMPT_WORD_PAGE)
```

## Lưu ý khi tùy chỉnh prompt

- Prompt viết **không dấu** để tương thích tốt nhất với Gemini
- Luôn nhấn mạnh: phương án A-D mỗi dòng riêng, ý nhỏ a-d mỗi dòng riêng
- Luôn nhấn mạnh: KHÔNG đưa tiếng Việt vào trong math mode
- Luôn nhấn mạnh: dùng `\[...\]` thay `$$...$$`
