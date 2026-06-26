---
name: exam-docx-creator
description: "Skill chuyển đổi PDF/ảnh sang Word (.docx) và tạo câu hỏi loại 1-4 bằng AI xuất ra file Word định dạng đẹp mắt. Sử dụng khi người dùng cần: chuyển file PDF sang Word, chuyển ảnh sang Word, OCR tài liệu sang docx, tạo câu hỏi trắc nghiệm/đúng sai/trả lời ngắn/tự luận xuất file Word, soạn đề thi Word, hoặc bất kỳ yêu cầu nào liên quan đến tạo file .docx chứa câu hỏi giáo dục Việt Nam với định dạng tab/indent chuẩn."
allowed-tools: Read, Write, Edit, Glob, Grep, WebFetch
argument-hint: "[chuyển pdf/ảnh sang word | tạo câu hỏi loại 1/2/3/4 ra word]"
---

# Skill: Exam DOCX Creator

## Mô tả

Skill chuyên xử lý 2 nhiệm vụ chính, xuất ra file .docx có định dạng đẹp mắt theo chuẩn giáo dục Việt Nam:

1. **Chuyển PDF/ảnh → Word**: AI đọc trực tiếp file PDF/ảnh → chuyển thành markdown → xuất .docx có tab/indent/font chuẩn (không cần dùng API Key).
2. **Tạo câu hỏi AI → Word**: AI soạn câu hỏi loại 1-4 → xuất .docx với layout phương án A-D theo cột, tiền tố câu hỏi in đậm + màu xanh.
**Yêu cầu bắt buộc**: Tất cả file docx đầu ra phải được lưu vào thư mục `output-docx` của dự án.

## Khi nào dùng

- Chuyển file PDF sang Word (.docx)
- Chuyển ảnh (png/jpg/bmp/tiff) sang Word
- OCR tài liệu giáo dục sang docx
- Tạo câu hỏi trắc nghiệm (loại 1), đúng/sai (loại 2), trả lời ngắn (loại 3), tự luận (loại 4) → xuất Word
- Soạn đề thi/kiểm tra hoàn chỉnh → file Word
- Bất kỳ yêu cầu "tạo câu hỏi ra word/docx"

## Cấu trúc thư mục

```
exam-docx-creator/
├── SKILL.md                    ← File này
├── references/
│   ├── ai-generation-prompts.md  ← Prompt hướng dẫn AI sinh câu hỏi theo 6 tiêu chí
│   ├── format-cau-hoi.md       ← Format 4 loại câu hỏi (markdown cho docx)
│   └── ocr-prompts.md          ← OCR prompts cho Gemini
├── scripts/
│   ├── build_exam_docx.py      ← Core: markdown → formatted docx
│   └── ocr_to_docx.py          ← OCR: pdf/ảnh → markdown → docx (Ít dùng, AI tự đọc PDF/ảnh)
├── output-docx/                ← Thư mục bắt buộc chứa các file .docx xuất ra
└── assets/                     ← Template (mở rộng sau)
```

## Quy ước đường dẫn

| Biến | Ý nghĩa |
|------|---------|
| `<SKILL_DIR>` | Đường dẫn tuyệt đối đến thư mục gốc skill |
| `<BUILD>` | `python "<SKILL_DIR>/scripts/build_exam_docx.py"` |
| `<OCR>` | `python "<SKILL_DIR>/scripts/ocr_to_docx.py"` |

**Lưu ý:** Khi chạy trong bash sandbox, dùng đường dẫn VM mount thay cho đường dẫn Windows.

---

## Instruction

### Bước 0: Cài đặt dependencies (chạy 1 lần)

```bash
pip install python-docx pypandoc Pillow PyMuPDF httpx --break-system-packages
```

### Bước 1: Xác định nhiệm vụ

| Yêu cầu người dùng | Nhiệm vụ | Pipeline |
|---------------------|-----------|----------|
| "Chuyển PDF/ảnh sang Word" | Read → DOCX | AI đọc file PDF/ảnh → xử lý markdown → `build_exam_docx.py` (Lưu file vào `output-docx/`) |
| "Tạo câu hỏi loại 1/2/3/4 ra Word" | AI Generate → DOCX | AI tạo markdown → `build_exam_docx.py` (Lưu file vào `output-docx/`) |
| "Tạo đề thi hoàn chỉnh ra Word" | AI Generate → DOCX | AI tạo markdown đề thi → `build_exam_docx.py` (Lưu file vào `output-docx/`) |

---

## Nhiệm vụ 1: Chuyển PDF/ảnh → Word

**LƯU Ý QUAN TRỌNG:** Tác vụ này do AI tự xử lý hoàn toàn offline (không dùng API Key). AI đọc trực tiếp file PDF hoặc ảnh bằng công cụ xem file (`view_file`).

1. AI tự đọc file PDF hoặc ảnh bằng công cụ tích hợp sẵn (ví dụ: `view_file` tool).
2. AI viết nội dung trích xuất được ra file markdown theo format chuẩn (xem bên dưới).
3. Gọi script `build_exam_docx.py` để format và xuất ra file word. **BẮT BUỘC lưu vào thư mục `output-docx/`**.

```bash
mkdir -p "<SKILL_DIR>/output-docx"
<BUILD> --input "<markdown_file.md>" --output "<SKILL_DIR>/output-docx/<tên_file>.docx"
```

Hoặc pipe trực tiếp:

```bash
mkdir -p "<SKILL_DIR>/output-docx"
echo '<nội_dung_markdown>' | <BUILD> --stdin --output "<SKILL_DIR>/output-docx/<tên_file>.docx"
```

---

## Nhiệm vụ 2: Tạo câu hỏi AI → Word

### Bước 2a: Đọc format và yêu cầu sinh câu hỏi (BẮT BUỘC)

Đọc 2 file sau để nắm rõ quy tắc:
1. `<SKILL_DIR>/references/format-cau-hoi.md`: Nắm format markdown chuẩn cho từng loại câu hỏi.
2. `<SKILL_DIR>/references/ai-generation-prompts.md`: Nắm cấu trúc sinh câu hỏi và yêu cầu 6 tiêu chí đầu vào.

### Bước 2b: Thu thập thông tin từ người dùng

Theo yêu cầu trong `ai-generation-prompts.md`, trước khi tạo câu hỏi (loại 1, 2, 3, hoặc 4), AI **phải yêu cầu người dùng cung cấp các thông tin quan trọng sau** (nếu họ chưa cung cấp đủ):
- Môn học
- Lớp
- Chương
- Bài / Chủ đề
- Dạng câu hỏi
- Mức độ (Nhận biết, Thông hiểu, Vận dụng, Vận dụng cao)

### Bước 2c: AI tạo nội dung markdown

AI đóng vai trò giáo viên chuyên môn, soạn câu hỏi bám sát 6 thông tin đã nhận và tuân thủ NGHIÊM NGẶT format trong `format-cau-hoi.md`.

### Bước 2d: Lưu markdown và chạy script

```bash
# Đảm bảo thư mục output tồn tại
mkdir -p "<SKILL_DIR>/output-docx"

# Lưu markdown vào file
cat > "<temp_file.md>" << 'MARKDOWN_EOF'
<nội_dung_markdown_câu_hỏi>
MARKDOWN_EOF

# Chuyển sang docx
<BUILD> --input "<temp_file.md>" --output "<SKILL_DIR>/output-docx/<tên_file>.docx"
```

---

## Format Markdown chuẩn cho câu hỏi (tóm tắt)

### Loại 1 — Trắc nghiệm

```markdown
Câu 1. Nội dung câu hỏi trắc nghiệm?
A. Phương án A
B. Phương án B
C. Phương án C
D. Phương án D

Lời giải.

- [Ý chính 1 giải thích]
  + [Ý phụ 1a của ý chính 1]
  + [Ý phụ 1b của ý chính 1]
- [Ý chính 2 giải thích]

Đáp án.

Chọn C
```

### Loại 2 — Đúng/sai

```markdown
Câu 1. Nội dung câu hỏi kèm 4 phát biểu:
a) Phát biểu thứ nhất
b) Phát biểu thứ hai
c) Phát biểu thứ ba
d) Phát biểu thứ tư

Lời giải.

- a) Đúng: [Giải thích cho ý a]
  + [Chi tiết bổ sung cho ý a]
- b) Sai: [Giải thích cho ý b]
- c) Đúng: [Giải thích cho ý c]
- d) Sai: [Giải thích cho ý d]
```

### Loại 3 — Trả lời ngắn

```markdown
Câu 1. Nội dung câu hỏi yêu cầu trả lời bằng con số.

Lời giải.

- [Bước 1: công thức/cách giải]
  + [Chi tiết tính toán phụ]
- [Bước 2: thay số/tính toán]

Đáp án.

40
```

### Loại 4 — Tự luận

```markdown
Bài 1. Nội dung bài tập tự luận.

Lời giải.

- 1. [Bước chính 1 của bài toán]
  + [Ý phụ 1a]
- 2. [Bước chính 2 của bài toán]
- 3. [Kết luận]
```

### Công thức toán

- Inline: `$x^2 + 1$`
- Display (riêng dòng): `\[x^2 + y^2 = r^2\]`
- **KHÔNG** dùng `$$...$$`

---

## Chi tiết định dạng DOCX đầu ra

Script `build_exam_docx.py` tự động áp dụng các định dạng sau (khớp với logic `converter_service.py` trong dự án):

### Trang
| Thuộc tính | Giá trị |
|-----------|---------|
| Khổ giấy | Letter (21.59 × 27.94 cm) |
| Lề trái | 2.0 cm |
| Lề phải | 1.25 cm |
| Lề trên | 1.5 cm |
| Lề dưới | 1.0 cm |

### Font
| Thuộc tính | Giá trị |
|-----------|---------|
| Font chữ | Times New Roman |
| Cỡ chữ body | 12pt |
| Font áp dụng | Toàn bộ (ascii, hAnsi, eastAsia, cs) |

### Tiền tố câu hỏi ("Câu N", "Bài N", "Ví dụ N")
- **In đậm** + **Màu xanh** (RGB: #0070C0)
- Nằm cùng dòng với nội dung câu hỏi

### Phương án A-D (tab layout tự động)

| Điều kiện | Layout | Tab positions |
|-----------|--------|---------------|
| Tất cả ≤ 20 ký tự, tổng ≤ 80 | 4 cột 1 dòng | 0.5, 4.5, 9.0, 13.0 cm |
| Tất cả ≤ 40 ký tự | 2 cột 2 dòng | 0.5, 9.0 cm |
| Còn lại | 1 phương án/dòng | indent 0.5 cm |

- Marker (A., B., C., D.) **in đậm**
- Nội dung phương án **không đậm**
- Left indent: 0.5 cm
- Spacing: before 3pt, after 3pt, line spacing 1

### Ý nhỏ a-d
- Indent 0.5 cm
- Marker **không đậm**

### Bảng biểu (Tables)
- Tự động căn giữa toàn bộ bảng trên trang.
- Đổi kiểu viền sang `'Table Grid'` mảnh nhẹ thanh lịch.
- Hàng tiêu đề (Header row): Tự động tô màu nền xám nhạt (`#F2F2F2`), chữ in đậm, cỡ chữ 11pt, căn giữa.
- Các hàng nội dung: Cỡ chữ 11pt, đệm ô (`cell padding`) giãn rộng thoáng mát dễ đọc.

### Hình ảnh (Images)
- Tất cả các đoạn chứa ảnh trong đề thi đều được tự động căn giữa.
- Giới hạn chiều rộng tối đa của ảnh là `12 cm` để tránh tràn lề giấy (tự động co dãn theo đúng tỷ lệ gốc).
- Hỗ trợ pipeline trích xuất ảnh gốc từ file PDF nguồn khi chạy OCR và tự động liên kết thẻ ảnh vào văn bản.

---

## Scripts — Chi tiết sử dụng

### build_exam_docx.py

**Chức năng:** Nhận file markdown (hoặc stdin) → xuất .docx có định dạng đẹp mắt

```bash
# Từ file markdown
<BUILD> --input "questions.md" --output "de_thi.docx"

# Từ stdin
echo "Câu 1. ..." | <BUILD> --stdin --output "de_thi.docx"

# Giữ công thức TeX dạng text (cho MathType Toggle TeX)
<BUILD> --input "questions.md" --output "de_thi.docx" --toggle-tex

# Chuyển công thức sang OMML (Word Equation)
<BUILD> --input "questions.md" --output "de_thi.docx" --equation
```

| Flag | Mặc định | Mô tả |
|------|----------|-------|
| `--input` | | File markdown đầu vào |
| `--stdin` | false | Đọc markdown từ stdin |
| `--output` | `output.docx` | File docx đầu ra |
| `--toggle-tex` | **true** | Giữ công thức dạng TeX text (MathType Toggle TeX) |
| `--equation` | false | Chuyển công thức sang OMML (Word Equation thực sự) |

### ocr_to_docx.py

**Chức năng:** Trích xuất text và hình ảnh từ file PDF chạy offline (không dùng API key) → xuất .docx

```bash
# Trích xuất PDF và chuyển đổi sang docx
<OCR> --input "document.pdf" --output "result.docx"
```

| Flag | Mặc định | Mô tả |
|------|----------|-------|
| `--input` | | File PDF đầu vào |
| `--output` | `output.docx` | File docx đầu ra |
| `--toggle-tex` | true | Giữ công thức TeX text |
| `--equation` | false | Chuyển sang OMML |

---

## Workflow mẫu

### WF1: Chuyển ảnh/PDF đề thi sang Word

1. AI tự đọc nội dung file ảnh/PDF.
2. AI định dạng lại nội dung dưới dạng markdown chuẩn.
3. AI lưu file markdown và chạy:
```bash
mkdir -p "<SKILL_DIR>/output-docx"
<BUILD> --input "/tmp/de_thi.md" --output "<SKILL_DIR>/output-docx/de_thi.docx"
```

### WF2: Tạo 5 câu trắc nghiệm Hóa 9 ra Word

1. Đọc `<SKILL_DIR>/references/format-cau-hoi.md`
2. AI soạn 5 câu markdown
3. Lưu file markdown + chạy:
```bash
mkdir -p "<SKILL_DIR>/output-docx"
<BUILD> --input "/tmp/hoa9_questions.md" --output "<SKILL_DIR>/output-docx/hoa9_trac_nghiem.docx"
```

---

## Checklist trước khi hoàn thành

- [ ] Cài dependencies: `python-docx pypandoc Pillow PyMuPDF httpx`
- [ ] Đọc format tham chiếu nếu tạo câu hỏi AI
- [ ] Markdown đúng format (Câu N cùng dòng, A-D mỗi dòng, $...$ cho math)
- [ ] Chạy script → kiểm tra file .docx output tồn tại
- [ ] Gửi file .docx cho người dùng
