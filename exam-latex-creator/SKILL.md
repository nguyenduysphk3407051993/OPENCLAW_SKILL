---
name: exam-latex-creator
description: "Skill tạo câu hỏi/bài tập LaTeX cho giáo dục Việt Nam (THCS & THPT). Sử dụng khi cần soạn câu hỏi loại 1 (trắc nghiệm), loại 2 (đúng/sai), loại 3 (trả lời ngắn), loại 4 (tự luận) cho các môn KHTN, Toán, Văn theo chuẩn LaTeX. Cũng dùng khi cần RA ĐỀ TỪ BẢNG ĐẶC TẢ có sẵn (.docx hoặc .json) để sinh đề đúng số câu/mức độ/chủ đề, trộn đề, ghép đề, lọc trùng, biên dịch PDF, hoặc trích xuất nội dung từ file pdf/ảnh/docx sang form LaTeX."
allowed-tools: Read, Write, Edit, Glob, Grep, WebFetch
argument-hint: "[loại câu hỏi] [số lượng] [chủ đề/chương/bài]"
---

# Skill: Vietnamese Education LaTeX Generator

## Khi yêu cầu chưa đủ cụ thể — PHẢN BIỆN TRƯỚC, LÀM SAU

Yêu cầu chung chung luôn cho ra sản phẩm kém. **Không đoán bừa, cũng không hỏi
lể tể từng ý.** Hãy nêu rõ đang thiếu gì, rồi đưa **một prompt mẫu đã điền sẵn
giá trị mặc định hợp lý** để người dùng sửa và gửi lại trong đúng một lượt.

Thiếu từ **2 tiêu chí trở lên** thì bắt buộc phản biện. Thiếu **đúng 1** tiêu chí
thì tự chọn mặc định, làm tiếp, và nói rõ đã chọn gì.

**Tiêu chí bắt buộc:** môn · lớp · chương/bài · loại câu hỏi · số lượng mỗi loại · mức độ

**Mẫu phản biện:**

> Yêu cầu hiện thiếu: **số lượng câu**, **mức độ**. Nếu làm luôn thì tôi phải đoán, dễ lệch
> ý bạn. Bạn copy prompt dưới đây, sửa chỗ in đậm rồi gửi lại:
>
> ```
> Soạn câu hỏi LaTeX môn **Toán** lớp **9**,
> chương **3 – Hàm số bậc nhất**, bài **Đồ thị hàm số y = ax + b**.
> Số lượng: **6** câu loại 1, **2** câu loại 2, **2** câu loại 3, **1** câu loại 4
> Mức độ: Nhận biết **30%**, Thông hiểu **40%**, Vận dụng **30%**
> Yêu cầu thêm: **có lời giải chi tiết, gán ID6 theo MAPID, biên dịch PDF**
> ```

---

## Mô tả

Skill chuyên tạo câu hỏi theo chủ đề/chương/bài/dạng (Toán, Lý, Hóa, Sinh, KHTN, Ngữ Văn) theo định dạng LaTeX chuẩn, tuân thủ nghiêm ngặt cấu trúc chương trình giáo dục Việt Nam (THCS & THPT). Hỗ trợ tạo đề thi hoàn chỉnh, trộn mã đề, lọc trùng, biên dịch PDF.

## Khi nào dùng

- Soạn câu hỏi loại 1 (trắc nghiệm), 2 (đúng/sai), 3 (trả lời ngắn), 4 (tự luận) dưới dạng mã LaTeX
- **Người dùng đưa BẢNG ĐẶC TẢ (.docx/.json) và yêu cầu ra đề đúng theo bảng đó** (`spec_to_exam.py`)
- Trích xuất nội dung từ file pdf/ảnh/docx chuyển sang form LaTeX
- Tạo đề thi hoàn chỉnh với nhiều loại câu hỏi
- Ghép câu hỏi từ nhiều nguồn thành đề thi (`assemble`)
- Trộn mã đề mới từ đề gốc (`shuffle`)
- Lọc câu hỏi trùng lặp (`dedup`)
- Sửa lỗi LaTeX phổ biến và biên dịch PDF (`fix`, `compile`)

## Cấu trúc thư mục

```
exam-latex-creator/
├── SKILL.md                          ← File này
├── references/                       ← Tài liệu tham chiếu format + MAPID
│   ├── ex-trac-nghiem.md             ← Format loại 1: trắc nghiệm (EX)
│   ├── tf-dung-sai.md                ← Format loại 2: đúng/sai (TF)
│   ├── sa-tra-loi-ngan.md            ← Format loại 3: trả lời ngắn (SA)
│   ├── bt-tu-luan.md                 ← Format loại 4: tự luận (BT)
│   ├── tu-bang-dac-ta.md             ← Ra đề từ bảng đặc tả .docx/.json
│   ├── chay-tren-ubuntu-vps.md       ← Triển khai trên VPS Ubuntu
│   ├── mapid6-coding.md              ← Quy tắc mã hóa ID6
│   ├── MAPID_KHTN6.tex               ← Bản đồ nội dung KHTN lớp 6 (11 chương, 33 bài, 184 dạng)
│   ├── MAPID_KHTN7.tex               ← Bản đồ nội dung KHTN lớp 7 (11 chương, 29 bài, 134 dạng)
│   ├── MAPID_KHTN8.tex               ← Bản đồ nội dung KHTN lớp 8 (8 chương, 39 bài, 137 dạng)
│   └── MAPID_KHTN9.tex               ← Bản đồ nội dung KHTN lớp 9 (12 chương, 42 bài, 208 dạng)
├── scripts/
│   ├── spec_to_exam.py               ← Bảng đặc tả → kế hoạch → khung .tex → đối chiếu
│   ├── mix_exam.py                   ← Ghép đề, trộn đề, parse, lọc trùng
│   ├── export_pdf.py                 ← Sửa lỗi LaTeX, biên dịch PDF, xử lý ảnh
│   ├── check_linux.py                ← Soi lỗi HOA/thường + gói TeX trước khi lên VPS
│   └── setup_ubuntu.sh               ← Dựng môi trường TeX + Python trên Ubuntu
├── assets/
│   └── template-de-thi.tex           ← Template đề thi chuẩn (subfiles)
└── latex-output/                     ← Thư mục xuất file .tex/.pdf
    ├── FileMain.tex                  ← File chủ (document class, packages, macro)
    ├── Khaibao/                      ← Thư mục chứa các file khai báo LaTeX con
    ├── Ans/                          ← Đáp án tự sinh (LG*, Ans-*, AnsBT-*, AnsSA-*)
    ├── Ansbook/                      ← Bảng đáp án TF
    └── Images/                       ← Hình ảnh đề thi
```

## Quy ước đường dẫn

| Biến | Ý nghĩa |
|------|---------|
| `<SKILL_DIR>` | Đường dẫn tuyệt đối đến thư mục gốc skill (tự detect OS) |
| `<OUTPUT_DIR>` | `<SKILL_DIR>/latex-output` |
| `<MIX>` | `python "<SKILL_DIR>/scripts/mix_exam.py"` |
| `<EXPORT>` | `python "<SKILL_DIR>/scripts/export_pdf.py"` |
| `<SPEC>` | `python "<SKILL_DIR>/scripts/spec_to_exam.py"` |

**Lưu ý:** Khi chạy trong bash sandbox, dùng đường dẫn VM mount thay cho đường dẫn Windows.

**Trên VPS Ubuntu:** chạy `bash scripts/setup_ubuntu.sh` một lần, rồi
`python scripts/check_linux.py` — phải báo **0 lỗi** trước khi biên dịch. Linux
phân biệt HOA/thường nên `\input{Khaibao/HeaderFooter/...}` sẽ vỡ nếu thư mục
thật tên `Khaibao/Headerfooter/`. Chi tiết: `references/chay-tren-ubuntu-vps.md`.

---

## Instruction

***Role:*** Bạn là chuyên gia tạo câu hỏi theo dạng thuộc các chủ đề môn học lớp 6-12, gồm 4 loại câu hỏi LaTeX.

### Bước 0: Đọc format tham chiếu (BẮT BUỘC trước khi tạo câu hỏi)

Đọc file tương ứng trong `<SKILL_DIR>/references/` để lấy format chuẩn:

| Loại | File | Môi trường |
|------|------|------------|
| Loại 1 — Trắc nghiệm | `ex-trac-nghiem.md` | `\begin{ex}...\end{ex}` với `\choice` |
| Loại 2 — Đúng/sai | `tf-dung-sai.md` | `\begin{ex}...\end{ex}` với `\choiceTF` |
| Loại 3 — Trả lời ngắn | `sa-tra-loi-ngan.md` | `\begin{ex}...\end{ex}` với `\shortans` |
| Loại 4 — Tự luận | `bt-tu-luan.md` | `\begin{bt}...\end{bt}` |
| ID6 | `mapid6-coding.md` | Quy tắc gán mã ID6 |

### Bước 1: Tra cứu MAPID — Bản đồ nội dung chương trình (BẮT BUỘC)

Thư mục `<SKILL_DIR>/references/` chứa các file `MAPID_<MÔN><LỚP>.tex` — bản đồ chi tiết toàn bộ chương/bài/dạng.

**Quy tắc:**
1. **Trước khi tạo câu hỏi**, XÁC ĐỊNH LỚP từ yêu cầu người dùng → ĐỌC file MAPID đúng lớp:
   - Lớp 6 → `MAPID_KHTN6.tex` (11 chương, 33 bài, 184 dạng)
   - Lớp 7 → `MAPID_KHTN7.tex` (11 chương, 29 bài, 134 dạng)
   - Lớp 8 → `MAPID_KHTN8.tex` (8 chương, 39 bài, 137 dạng)
   - Lớp 9 → `MAPID_KHTN9.tex` (12 chương, 42 bài, 208 dạng)
   - (Thêm file mới khi có: `MAPID_HOA10.tex`, `MAPID_TOAN9.tex`, ...)

2. Từ file MAPID, xác định chính xác:
   - Chương nào chứa chủ đề người dùng yêu cầu
   - Bài cụ thể trong chương
   - Các dạng bài đã có sẵn → dùng để gán ID6 chính xác

3. **Khi tạo câu hỏi hay/mới**, nếu dạng bài chưa có trong MAPID → **TỰ ĐỘNG cập nhật** bằng cách thêm dòng mới vào đúng vị trí trong file MAPID

4. Cấu trúc MAPID (mỗi level thêm 3 dấu `-`):
   ```
   -[6] Lớp 6
   ----[K] Khoa học tự nhiên
   -------[1] Chương: Các thể của chất
   ----------[1] Bài: Sự đa dạng và các thể cơ bản của chất
   -------------[1] Dạng: Nhận biết vật thể tự nhiên, nhân tạo...
   -------------[2] Dạng: Đặc điểm các thể cơ bản...
   ```

5. Mapping sang ID6: dòng `-------[1]` → Chương=1, `----------[2]` → Bài=2, `-------------[3]` → Dạng=3

**Lưu ý:** File MAPID_KHTN7/8/9 có phần header cấu hình mức độ ở đầu file (trước dòng `-[<Lớp>]`). Header này mô tả các ký hiệu mức độ dùng chung (Y, B, K, G, T, N, H, V, C).

**Ví dụ tra cứu:** Người dùng yêu cầu "tạo câu hỏi về lực ma sát lớp 6"
→ Đọc MAPID_KHTN6.tex → Tìm chương 9, bài 3 (Lực ma sát) → Các dạng 1-6
→ Gán ID6: `[6K9N3-1]`, `[6K9H3-2]`, ...

### Bước 2: Tạo câu hỏi

**Nhiệm vụ 1:** Tạo câu hỏi loại 1/2/3/4 theo chủ đề, chương, bài, số lượng
**Nhiệm vụ 2:** Trích xuất nội dung từ file pdf/ảnh/docx → chuyển sang form LaTeX
**Nhiệm vụ 3:** Tạo đề thi hoàn chỉnh theo cấu trúc (phần 1: EX, phần 2: TF, phần 3: SA, phần 4: BT)
**Nhiệm vụ 4:** Ra đề từ **bảng đặc tả có sẵn** (.docx/.json) — xem `references/tu-bang-dac-ta.md`

### Yêu cầu nghiêm ngặt theo loại câu hỏi

1. **Loại 1 (EX):**
   - `\choice` đủ **4 tham số** `\choice{}{}{}{}` — không được bỏ trống
   - Chỉ có **1 phương án đúng** duy nhất, đặt `\True` ngay trước nội dung
   - Các phương án **không có dấu chấm** ở cuối

2. **Loại 2 (TF):**
   - `\choiceTF` đủ **4 tham số** `\choiceTF{}{}{}{}` — không được bỏ trống
   - `\True` trước phương án đúng, số phương án đúng **ngẫu nhiên** (0-4) và **khác nhau giữa các câu**
   - Nội dung các phương án phải chứa **nội dung kiến thức** — không chấp nhận chỉ ghi "đúng"/"sai"
   - Lời giải bắt buộc format:
     ```latex
     \begin{itemchoice}[T1,F2,F3,T4]
       \itemch Lời giải phương án a
       \itemch Lời giải phương án b
       \itemch Lời giải phương án c
       \itemch Lời giải phương án d
     \end{itemchoice}
     ```
   - Bắt buộc 4 tùy chọn `[T1,F2,...]`: đúng = `T` + số, sai = `F` + số

3. **Loại 3 (SA):**
   - `\shortans{$<số>$}` chỉ chứa **con số**, không đơn vị
   - Số thập phân: `\shortans{$2{,}3$}`

4. **Loại 4 (BT):**
   - Dùng môi trường `\begin{bt}...\end{bt}` (không phải `ex`)
   - Lời giải chi tiết, trình bày đầy đủ các bước

### Yêu cầu nội dung LaTeX

1. Inline math: `$...$` — Display math: `\[...\]` (KHÔNG dùng `$$...$$`)
2. Số thập phân: dùng `{,}` thay `.` → `$3{,}14$` thay vì `$3.14$`
3. Công thức nhiều dòng: dùng `eqnarray*`:
   ```latex
   \begin{eqnarray*}
     f(x) & = & (x+1)^2 \\
          & = & x^2 + 2x + 1
   \end{eqnarray*}
   ```
4. Bảng: `tabular` (ngắn) hoặc `longtable` (dài nhiều trang)
5. Chỉ số trên/dưới: `$Al_2{(SO_4)}_3$` (KHÔNG dùng Unicode superscript ²³)
6. Chỉ dùng `\chemfig` khi vẽ **công thức cấu tạo** — công thức phân tử dùng `$...$`
7. Mũi tên phản ứng: `\xrightarrow[$đk$]` hoặc `\xrightarrow[$đk1$][$đk2$]` (KHÔNG dùng `\xrightarrow{...}`)
8. Danh sách trong loại 3, 4: dùng `enumerate`
9. **Bỏ** các cụm "Bài", "Ví dụ", "Câu" + số thứ tự trong nội dung câu hỏi
10. Dùng `\dfrac` thay cho `\frac`

### Định dạng đầu ra

#### Nhiệm vụ 1 & 2: Code block latex

```latex
%%%=========[EX|TF|SA|BT]_[số thứ tự]================%%%
\begin{ex}%[<ID6>]
Nội dung câu hỏi
\end{ex}
```

Trong đó:
- `name` là `ex` (loại 1/2/3) hoặc `bt` (loại 4)
- `<ID6>` theo quy tắc trong `mapid6-coding.md`
- Mỗi câu có dòng marker: `%%%=====<Loại>_<số>=====%%%`

#### Nhiệm vụ 3: File `.tex` hoàn chỉnh

Đọc template tại `<SKILL_DIR>/assets/template-de-thi.tex` rồi chèn câu hỏi vào.

**Lưu ý quan trọng khi dùng template:**
- `\documentclass[FileMain.tex]{subfiles}` → file output phải nằm cùng thư mục với `FileMain.tex` (tức `<OUTPUT_DIR>/`)
- Xóa **toàn bộ** phần `\subsection` nào không có câu hỏi
- Thay `<tên file>` trong `Opensolutionfile`/`Closesolutionfile` bằng tên file thực (không có `.tex`)
- Thay các `\gdef` phù hợp: `\monhoc`, `\ngaykt`, `\nh`, `\thoigian`, `\made`
- Có thể bỏ `\gdef\sophong`, `\gdef\truong`, `\gdef\truongh` nếu không cần header trường
- Dùng `\setcounter{section}{0}` cho đề 1, `{1}` cho đề 2, ...

### Bổ sung sau khi tạo câu hỏi

- Đề xuất thêm dạng toán và bài tập tương tự về chủ đề liên quan
- Gợi ý ý tưởng mở rộng bài toán
- Văn phong sư phạm, đảm bảo đúng kiến thức, khoa học

---

## Scripts

### spec_to_exam.py — Ra đề từ bảng đặc tả

| Lệnh | Mô tả | Cú pháp |
|------|-------|---------|
| `read` | Bảng đặc tả (.docx/.json) → kế hoạch ra đề | `<SPEC> read "<spec>" -o plan.json --lop 6 --mon K` |
| `skeleton` | Kế hoạch → file .tex theo `template-de-thi.tex` (còn `% TODO`) | `<SPEC> skeleton plan.json -o "<OUTPUT_DIR>/<TEN>.tex" --ten-de "..." --made 101` |
| `fill` | Kế hoạch + `de_bai_tap.json` → .tex đầy đủ nội dung | `<SPEC> fill plan.json de_bai_tap.json --id6-map id6.json -o "<OUTPUT_DIR>/<TEN>.tex"` |
| `verify` | Đối chiếu .tex với bảng đặc tả | `<SPEC> verify plan.json "<OUTPUT_DIR>/<TEN>.tex"` |

Cờ của `read`: `--y-dung-sai 4`, `--y-tu-luan 2` (số lệnh hỏi mỗi câu).
Cờ metadata của `skeleton`/`fill`: `--monhoc --ten-de --ngaykt --nh --thoigian
--made --so-de --ten-file`.

**Ràng buộc khi sinh .tex** (chi tiết: `references/tu-bang-dac-ta.md`):
- Chỉ dùng đúng cấu trúc `assets/template-de-thi.tex`
- KHÔNG thêm gói hay lệnh LaTeX mới
- Giữ nguyên dòng hướng dẫn thí sinh sau mỗi `\subsection`
- Xoá hẳn phần không có câu hỏi

### mix_exam.py — Ghép, trộn đề, phân tích, lọc trùng

| Lệnh | Mô tả | Cú pháp |
|-------|--------|---------|
| `parse` | Thống kê câu hỏi (đếm EX/TF/SA/BT, liệt kê ID6) | `<MIX> parse "<file_hoặc_thư_mục>"` |
| `dedup` | Lọc câu trùng (so sánh nội dung, loại bỏ trùng) | `<MIX> dedup "<input>" "<output>" --threshold 0.85` |
| `assemble` | Ghép câu hỏi từ nhiều nguồn vào template đề thi | Xem bên dưới |
| `shuffle` | Trộn mã đề mới (xáo trộn thứ tự câu + phương án) | `<MIX> shuffle "<file_gốc>" --seed <số> --made2 <mã_đề>` |

**assemble — chi tiết:**
```bash
<MIX> assemble \
  --input "<f1.tex>" "<f2.tex>" \
  --output "<OUTPUT_DIR>/<TEN_FILE>.tex" \
  --monhoc "Khoa học tự nhiên 6" \
  --ngaykt "08/06/2026" \
  --thoigian 45 \
  --made 101 \
  --ten-de "Kiểm tra giữa kỳ 1" \
  --nh "2025 - 2026"
```

Hoặc dùng file config JSON:
```bash
<MIX> assemble --config "<config.json>"
```
Config JSON:
```json
{
  "input": ["file1.tex", "file2.tex"],
  "output": "output.tex",
  "monhoc": "Khoa học tự nhiên 6",
  "ngaykt": "08/06/2026",
  "thoigian": "45",
  "made": "101",
  "ten_de": "Kiểm tra giữa kỳ 1",
  "nh": "2025 - 2026"
}
```

**shuffle — chi tiết:**
```bash
<MIX> shuffle "<OUTPUT_DIR>/<FILE_GỐC>.tex" --seed 42 --made2 102
# Tùy chọn: --out-name "<đường_dẫn_output>"
```

### export_pdf.py — Sửa lỗi LaTeX, biên dịch PDF, xử lý ảnh

| Lệnh | Mô tả | Cú pháp |
|-------|--------|---------|
| `fix` | Sửa 10 lỗi LaTeX phổ biến | `<EXPORT> fix "<file.tex>" [output_file]` |
| `compile` | Biên dịch file .tex thành PDF | `<EXPORT> compile "<file.tex>" --dir "<thư_mục>" --times 2 --clean` |
| `clean` | Xóa file rác LaTeX (.aux, .log, .out, ...) | `<EXPORT> clean "<thư_mục>" [--no-recursive]` |
| `images` | Trích xuất ảnh từ file .docx | `<EXPORT> images "<file.docx>" "<thư_mục_ảnh>"` |
| `imgpaths` | Chuẩn hóa đường dẫn ảnh trong .tex | `<EXPORT> imgpaths "<file.tex>" --inplace` |

**fix — 10 lỗi được sửa tự động:**
1. Ngoặc kép `"..."` → `\lq\lq ... \rq\rq`
2. `\xrightarrow` format sai → format chuẩn `\xrightarrow[$...$]`
3. `...` → `\dots`
4. `5 x 3` → `5 \times 3`
5. `\frac` → `\dfrac`
6. Subscript tiếng Việt: `_đ` → `_{\text{đ}}`
7. Xóa marker AI citation `[cite_start]`, `[cite_end]`
8. Xóa khoảng trắng thừa
9. Xóa dấu chấm cuối phương án trong `\choice`/`\choiceTF`
10. Bọc công thức hóa học trong math mode

---

## Workflow tạo đề thi hoàn chỉnh

### Cách 1: Tạo thủ công (viết trực tiếp)

1. **Đọc format** → `<SKILL_DIR>/references/<loại>.md`
2. **Tra MAPID** → `<SKILL_DIR>/references/MAPID_<MÔN><LỚP>.tex`
3. **Tạo câu hỏi** với ID6 đúng chuẩn
4. **Chèn vào template** → đọc `<SKILL_DIR>/assets/template-de-thi.tex`
5. **Lưu file** → `<OUTPUT_DIR>/<TEN_FILE>.tex`
6. **Fix + compile + clean:**
   ```bash
   <EXPORT> fix "<OUTPUT_DIR>/<TEN_FILE>.tex"
   <EXPORT> compile "<TEN_FILE>.tex" --dir "<OUTPUT_DIR>" --times 2 --clean
   ```

### Cách 4: Ra đề từ bảng đặc tả có sẵn — DÙNG KHI NGƯỜI DÙNG ĐƯA BẢNG ĐẶC TẢ

1. **Đọc** `references/tu-bang-dac-ta.md`
2. **Bung bảng đặc tả thành kế hoạch:**
   ```bash
   <SPEC> read "bang_dac_ta.docx" -o plan.json --lop 6 --mon K --y-tu-luan 2
   ```
3. **Sinh file .tex** theo đúng template — mỗi câu đã kèm chú thích Chủ đề /
   Đơn vị kiến thức / YCCĐ / Mức độ để bám sát khi viết:
   ```bash
   <SPEC> skeleton plan.json -o "<OUTPUT_DIR>/<TEN_FILE>_MADE101.tex" \
     --ten-de "Kiểm tra định kì giữa học kì I" --monhoc "Khoa học tự nhiên 6" \
     --ngaykt 20/10/2026 --thoigian 45 --made 101
   ```
4. **Điền nội dung** vào các chỗ `% TODO`; **tra MAPID** thay dấu `?` trong ID6
5. **Đối chiếu** — chỉ đi tiếp khi 0 lỗi:
   ```bash
   <SPEC> verify plan.json "<OUTPUT_DIR>/<TEN_FILE>_MADE101.tex"
   ```
6. **Fix + compile** như Cách 1; muốn nhiều mã đề thì `shuffle` như Cách 3

### Cách 2: Ghép từ nhiều nguồn (assemble)

1. Chuẩn bị các file câu hỏi riêng lẻ
2. Ghép đề:
   ```bash
   <MIX> assemble --input "cau_hoi_1.tex" "cau_hoi_2.tex" \
     --output "<OUTPUT_DIR>/DE_THI_MADE101.tex" \
     --monhoc "KHTN 9" --thoigian 90 --made 101 --ten-de "Kiểm tra cuối kỳ"
   ```
3. Fix + compile

### Cách 3: Trộn nhiều mã đề

1. Tạo đề gốc (cách 1 hoặc 2)
2. Trộn:
   ```bash
   <MIX> shuffle "<OUTPUT_DIR>/DE_GỐC.tex" --seed 42 --made2 102
   <MIX> shuffle "<OUTPUT_DIR>/DE_GỐC.tex" --seed 99 --made2 103
   ```

### Xử lý hình ảnh

Nếu đề có hình từ file .docx:
```bash
<EXPORT> images "<file.docx>" "<OUTPUT_DIR>/Images/<thư_mục_con>"
<EXPORT> imgpaths "<OUTPUT_DIR>/<TEN_FILE>.tex" --inplace
```

Chèn hình trong LaTeX:
```latex
\begin{center}
  \includegraphics[width=0.4\linewidth]{Images/<thư_mục_con>/<tên_ảnh>}
\end{center}
```

---

## ID6 — Mã định danh câu hỏi

**Cấu trúc:** `[<Lớp><Môn><Chương><Mức độ><Bài>-<Dạng>]`

Xem chi tiết tại `<SKILL_DIR>/references/mapid6-coding.md`.

**Tóm tắt nhanh:**

| Thành phần | Giá trị |
|------------|---------|
| Lớp | `6`=Lớp 6, `7`=Lớp 7, `8`=Lớp 8, `9`=Lớp 9, `0`=Lớp 10, `1`=Lớp 11, `2`=Lớp 12 |
| Môn | `K`=KHTN, `H`=Hóa, `L`=Lý, `S`=Sinh, `T`=Toán, `V`=Văn |
| Chương | `1-9`, `A-Z` |
| Mức độ | `N`=Nhận biết, `H`=Thông hiểu, `V`=Vận dụng, `C`=VD cao, `Y`=Yếu, `B`=TB, `K`=Khá, `G`=Giỏi, `T`=Thực tế |
| Bài | `1-9`, `A-Z` |
| Dạng | `1-9` |

**Ví dụ:** `[6K2N1-1]` = Lớp 6, KHTN, Chương 2, Nhận biết, Bài 1, Dạng 1

---

## Checklist trước khi hoàn thành

- [ ] Nếu có bảng đặc tả: đã chạy `<SPEC> read` + `<SPEC> verify` và báo 0 lỗi
- [ ] Không thêm bất kỳ gói hay lệnh LaTeX nào ngoài những gì template đã có
- [ ] Giữ nguyên dòng hướng dẫn thí sinh sau mỗi `\subsection`
- [ ] Đọc format reference đúng loại câu hỏi
- [ ] Tra MAPID đúng lớp/môn → gán ID6 chính xác cho mỗi câu
- [ ] Format đúng theo loại (choice 4 tham số, True đúng vị trí, itemchoice đúng label)
- [ ] Nội dung LaTeX đúng quy chuẩn ($...$, {,}, \dfrac, \xrightarrow, ...)
- [ ] Chèn template đầy đủ (nếu tạo đề): header, Opensolutionfile, Closesolutionfile, footer
- [ ] Xóa phần subsection không có câu hỏi
- [ ] Lưu vào `<OUTPUT_DIR>/`
- [ ] Chạy `<EXPORT> fix` để sửa lỗi
- [ ] Chạy `<EXPORT> compile` để biên dịch PDF
- [ ] Cập nhật MAPID nếu có dạng bài mới


---

## Cập nhật bắt buộc: template cứng và build đúng latex-output của skill

Khi tạo đề thi hoàn chỉnh bằng `exam-latex-creator`, bắt buộc tuân thủ các luật sau.

### 1. Dùng đúng template đề thi

File `.tex` phải sinh theo đúng template:

```text
<SKILL_DIR>/assets/template-de-thi.tex
```

Dòng đầu của file đề bắt buộc là:

```latex
\documentclass[FileMain.tex]{subfiles}
```

Không tự thêm bất cứ phần nào sau đây vào file đề:

```latex
\usepackage
```

Không tự thêm macro, preamble, `geometry`, `fancyhdr`, `tcolorbox`, `tikz`, màu, header/layout tự chế, hoặc lệnh trình bày ngoài template.

Chỉ được thay placeholder trong template và chèn câu hỏi vào đúng 4 vùng:

- trắc nghiệm nhiều lựa chọn `EX`;
- đúng/sai `TF`;
- trả lời ngắn `SA`;
- tự luận `BT`.

Nếu cần package/macro ngoài template để build, báo blocker; không tự sửa file đề bằng cách thêm package/macro.

### 2. Dùng đúng thư mục latex-output của chính skill

Source/build chính luôn nằm trong thư mục:

```text
<SKILL_DIR>/latex-output/
```

Với OpenClaw hiện tại:

```text
/home/node/.openclaw/skills/exam-latex-creator/latex-output/
```

Không build đề của skill này trong:

```text
/home/node/.openclaw/workspace/latex-edutechnd/latex-output/
```

### 3. Biên dịch bằng pdflatex 2 lần

Biên dịch trong đúng thư mục `latex-output` của skill:

```bash
cd <SKILL_DIR>/latex-output
pdflatex -interaction=nonstopmode -halt-on-error <ten-file>.tex
pdflatex -interaction=nonstopmode -halt-on-error <ten-file>.tex
```

Chạy 2 lần để cập nhật tham chiếu, nhãn, mục lục và số trang. Chỉ bàn giao khi lần 2 thành công.

### 4. Bàn giao file

Sau khi build thành công mới copy bản bàn giao sang workspace agent:

```text
/home/node/.openclaw/workspace/latex-edutechnd/01_Documents/<ten-file>.tex
/home/node/.openclaw/workspace/latex-edutechnd/01_Documents/<ten-file>.pdf
/home/node/.openclaw/workspace/latex-edutechnd/01_Documents/<ten-file>-report.txt
```

Không ghi sản phẩm ra gốc workspace.

### 5. Report hậu kiểm bắt buộc

Report phải ghi rõ:

- `Skill live`: đường dẫn `SKILL.md` đã dùng;
- `Template live`: đường dẫn `assets/template-de-thi.tex` đã dùng;
- `Build directory`: đúng `<SKILL_DIR>/latex-output/`;
- `Compiler pass 1` và `Compiler pass 2`;
- dòng đầu `.tex` là `\documentclass[FileMain.tex]{subfiles}`;
- số lần `\usepackage` trong file đề là `0`;
- số lượng `EX`, `TF`, `SA`, `BT`;
- kiểm `choiceTF` khớp `itemchoice`;
- PDF tồn tại và >0 byte;
- đường dẫn bản bàn giao trong `01_Documents/`.


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
