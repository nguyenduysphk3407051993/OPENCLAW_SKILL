---
name: tikz-drawing
description: "Skill viết mã TikZ/PGF LaTeX để vẽ hình. Dùng BẤT CỨ KHI NÀO cần một hình vẽ trong tài liệu LaTeX — bài tập, đề thi, bài giảng, giáo án, slide, chuyên đề, sách, báo cáo — không giới hạn ở bài tập STEM. Vẽ được: hình học phẳng và không gian (tam giác, tứ giác, đường tròn, hình hộp, hình chóp), đồ thị hàm số, bảng biến thiên, bảng xét dấu, biểu đồ, sơ đồ khối, lưu đồ, sơ đồ tư duy, hình vật lí (vector lực, mạch điện, quang học, sóng), công thức cấu tạo hoá học (chemfig), sơ đồ phản ứng, hình minh hoạ tự do. Hỗ trợ TikZ, PGFplots, tkz-tab, chemfig, circuitikz, tikz-3dplot."
allowed-tools: Read, Write, Glob, Grep, Bash
argument-hint: "[loại hình] [mô tả]"
---

# TikZ Drawing Skill

Skill chuyên viết mã TikZ/PGF LaTeX để **vẽ hình trong tài liệu LaTeX**.

Dùng bất cứ khi nào cần một hình vẽ, không cần phải là bài tập STEM: bài giảng,
giáo án, slide, chuyên đề, đề thi, sách, báo cáo, hay chỉ một hình minh hoạ lẻ.
Toán – Vật lí – Hoá học – Sinh học là những chỗ hay dùng nhất, nhưng sơ đồ khối,
lưu đồ, biểu đồ, sơ đồ tư duy hay hình trang trí đều nằm trong phạm vi skill này.

> Skill này trước đây tên `tikz-stem-drawing`. Đã đổi thành `tikz-drawing` vì
> cái tên cũ khiến người dùng tưởng chỉ vẽ được hình cho bài tập STEM.

## Khi yêu cầu chưa đủ cụ thể — PHẢN BIỆN TRƯỚC, LÀM SAU

Yêu cầu chung chung luôn cho ra sản phẩm kém. **Không đoán bừa, cũng không hỏi
lể tể từng ý.** Hãy nêu rõ đang thiếu gì, rồi đưa **một prompt mẫu đã điền sẵn
giá trị mặc định hợp lý** để người dùng sửa và gửi lại trong đúng một lượt.

Thiếu từ **2 tiêu chí trở lên** thì bắt buộc phản biện. Thiếu **đúng 1** tiêu chí
thì tự chọn mặc định, làm tiếp, và nói rõ đã chọn gì.

**Tiêu chí bắt buộc:** loại hình · mô tả chi tiết hình · nhãn/kí hiệu cần ghi · kích thước · môn học

**Mẫu phản biện:**

> Yêu cầu hiện thiếu: **mô tả chi tiết**, **nhãn cần ghi**. Nếu làm luôn thì tôi phải đoán, dễ lệch
> ý bạn. Bạn copy prompt dưới đây, sửa chỗ in đậm rồi gửi lại:
>
> ```
> Vẽ TikZ hình **tam giác vuông nội tiếp đường tròn**.
> Chi tiết: tam giác **ABC vuông tại A**, **BC là đường kính**, tâm **O**
> Nhãn cần ghi: **A, B, C, O**, kí hiệu **góc vuông tại A**, **bán kính R**
> Kích thước: **rộng khoảng 6 cm** · Dùng cho: **bài tập Toán lớp 9**
> ```

---

## Quy trình làm việc

### Bước 1: Phân tích đề bài

**Xác định các yếu tố:**

| Yếu tố | Câu hỏi cần trả lời |
|--------|---------------------|
| Bối cảnh | Hình dùng cho tài liệu gì: bài tập, bài giảng, slide, báo cáo? |
| Lĩnh vực | Toán / Vật lí / Hoá học / Sinh học / sơ đồ tổng quát? |
| Loại hình | Hình phẳng / không gian / đồ thị / bảng biến thiên / sơ đồ? |
| Đối tượng | Điểm, đường, hình, vector, phân tử nào? |
| Nhãn | Tên điểm, độ dài, góc, công thức? |
| Đặc biệt | Nét đứt, màu sắc, đánh dấu góc vuông? |

### Bước 2: Chọn thư viện và template

| Loại hình | Thư viện | File tham khảo |
|-----------|----------|----------------|
| Hình học phẳng | `tikz`, `calc` | `references/geometry.md` |
| Hình học không gian | `tikz-3dplot` | `references/geometry.md` |
| Đồ thị hàm số | `pgfplots` | `references/plots.md` |
| Vector lực, cơ học | `tikz`, `arrows.meta` | `references/physics.md` |
| Mạch điện | `circuitikz` | `references/physics.md` |
| Quang học | `tikz`, `decorations` | `references/physics.md` |
| CTCT hóa học | `chemfig` | `references/chemistry.md` |
| Sơ đồ phản ứng | `chemfig` | `references/chemistry.md` |

### Bước 3: Viết code theo cấu trúc chuẩn

```latex
% === PREAMBLE ===
\documentclass[tikz,border=5pt]{standalone}
% Hoặc trong document lớn:
% \documentclass{article}
% \usepackage{tikz}

% === THƯ VIỆN TIKZ ===
\usetikzlibrary{
    calc,           % Tính toán tọa độ
    arrows.meta,    % Mũi tên đẹp
    angles,         % Đánh dấu góc
    quotes,         % Nhãn góc
    positioning,    % Vị trí tương đối
    patterns,       % Mẫu tô (gạch chéo...)
    decorations.markings  % Đánh dấu trên đường
}

% === DOCUMENT ===
\begin{document}
\begin{tikzpicture}[
    % === ĐỊNH NGHĨA STYLE ===
    point/.style={circle, fill, inner sep=1.5pt},
    line/.style={thick},
    dashed line/.style={dashed, thick},
    vector/.style={-{Stealth[length=3mm]}, thick},
]
    % === CODE VẼ HÌNH ===
    
\end{tikzpicture}
\end{document}
```

### Bước 4: Áp dụng kỹ thuật phù hợp

Xem `references/techniques.md` để biết:
- Tính toán tọa độ với `calc`
- Đánh dấu góc vuông, góc bất kỳ
- Vẽ đường nét đứt (cạnh khuất)
- Tô màu vùng
- Đặt nhãn đúng vị trí

### Bước 5: Kiểm tra và tinh chỉnh

**Checklist:**
- [ ] Code biên dịch không lỗi
- [ ] Tất cả nhãn hiển thị đúng vị trí (không chồng chéo)
- [ ] Các cạnh khuất dùng nét đứt
- [ ] Góc vuông được đánh dấu
- [ ] Kích thước hình cân đối
- [ ] Style nhất quán (độ dày nét, font...)

## Quy tắc quan trọng

### 1. Đặt tên coordinate rõ ràng
```latex
% ✅ TỐT
\path(0, 0) coordinate (A) 
     (2, 0) coordinate (B);

% ❌ TRÁNH
 \path(0, 0) coordinate (p1);
 \coordinate (A) at (0, 0);
```

### 2. Dùng calc cho mọi tính toán
```latex
% Trung điểm M của AB
\path($(A)!0.5!(B)$) coordinate (M);

% Điểm chia theo tỉ lệ 2:1
\path ($(A)!0.67!(B)$) coordinate (M);
% Hình chiếu vuông góc của C lên AB
\path ($(A)!(C)!(B)$) coordinate (H);

% Điểm cách A một khoảng 2cm theo hướng B
\path ($(A)!2cm!(B)$) coordinate (P);
```

### 3. Comment code đầy đủ
```latex
% Vẽ tam giác ABC
\draw[thick] (A) -- (B) -- (C) -- cycle;

% Đường cao từ C xuống AB
\path ($(A)!(C)!(B)$) coordinate (H);
\draw[dashed] (C) -- (H);
```

### 4. Định nghĩa style để tái sử dụng
```latex
\begin{tikzpicture}[
    % Style cho điểm
    point/.style={circle, fill, inner sep=1.5pt},
    % Style cho đường chính
    main line/.style={thick, blue},
    % Style cho đường phụ
    aux line/.style={thin, gray, dashed},
]
```

### 5. Đơn vị và tỉ lệ phù hợp
```latex
% Hình nhỏ: scale mặc định
\begin{tikzpicture}

% Hình lớn hơn
\begin{tikzpicture}[scale=1.5]

% Hình rất nhỏ
\begin{tikzpicture}[scale=0.5]
```

## Ví dụ nhanh

### Yêu cầu
> Vẽ tam giác ABC vuông tại A, đường cao AH

### Code
```latex
\begin{tikzpicture}[
    point/.style={circle, fill, inner sep=1.5pt}
]
    % Định nghĩa đỉnh
	\path (0,0) coordinate (A);
	\path (4,0) coordinate (B);
	\path (0,3) coordinate (C);
 
    % Chân đường cao
    \path ($(B)!(A)!(C)$) coordinate (H) ;
    
    % Vẽ tam giác
    \draw[thick] (A) -- (B) -- (C) -- cycle;
    
    % Đường cao AH
    \draw[blue, thick] (A) -- (H);
    
    % Góc vuông tại A
    \draw (A) rectangle ++(0.3,0.3);
    
    % Góc vuông tại H
    \draw (H) ++(-0.2,0.15) -- ++(-0.15,-0.2) -- ++(0.2,-0.15);
    
    % Nhãn
    \path (A) node[below left] {$A$};
	\path (B) node[below right] {$B$};
	\path (C) node[above] {$C$};
	\path (H) node[above right] {$H$};
    
    % Đánh dấu điểm
    \foreach \p in {A,B,C,H} \fill (\p) circle (1.5pt);
\end{tikzpicture}
```

## Tài liệu tham khảo

| File | Nội dung | Khi nào đọc |
|------|----------|-------------|
| `references/geometry.md` | Mẫu hình học Toán | Vẽ tam giác, tứ giác, đường tròn, hình không gian |
| `references/physics.md` | Mẫu sơ đồ Vật lý | Vẽ vector lực, mạch điện, quang học, sóng |
| `references/chemistry.md` | Mẫu CTCT Hóa học | Vẽ công thức cấu tạo, sơ đồ phản ứng |
| `references/plots.md` | Mẫu đồ thị | Vẽ đồ thị hàm số, biểu đồ |
| `references/techniques.md` | Kỹ thuật TikZ | Tham khảo cú pháp, trick hay |

### Giáo trình "Học TikZ theo cách của bạn" (Bùi Quý)

`references/hoc-tikz-bui-quy/` là bản trích xuất sách gốc
`HocTikztheocachcuaBan_BuiQuy.pdf`, **tách theo đối tượng cần vẽ** để tra nhanh.
Mở `references/hoc-tikz-bui-quy/README.md` để xem mục lục đầy đủ.

| Cần vẽ gì | Đọc file |
|-----------|----------|
| Khai báo, hệ trục toạ độ | `01-khai-bao-he-toa-do.md` |
| Tham số, hàm tính toán, phép toán toạ độ | `02-tinh-toan-toa-do.md` |
| Điểm, văn bản, đoạn thẳng, đường gấp khúc | `03-diem-van-ban-doan-thang.md` |
| Đường tròn, ellipse, cung, đường cong | `04-duong-tron-cung-duong-cong.md` |
| Tiếp tuyến, giao điểm | `05-tiep-tuyen-giao-diem.md` |
| scope, clip, node, pic | `06-scope-clip-node-pic.md` |
| Tuỳ chọn nét vẽ và node | `07-tuy-chon-thuong-dung.md` |
| foreach, macro | `08-foreach-macro.md` |
| Hình không gian giả 3D | `09-hinh-khong-gian-3d.md` |
| Bảng xét dấu, bảng biến thiên | `10-bang-xet-dau-bien-thien.md` |
| Đồ thị hàm số, toạ độ cực | `11-do-thi-ham-so.md` |
| Tô miền đồ thị | `12-to-mien-do-thi.md` |
| Trình tự tư duy khi dựng hình | `13-tu-duy-ve-hinh.md` |
| Export ảnh, ảnh động PDF/GIF | `14-export-anh-dong.md` |
| calc, intersections, angles, patterns, decoration, shadings | `15-thu-vien-thuong-dung.md` |

Sinh lại bản trích xuất khi cần: `python scripts/pdf_to_md.py <sách.pdf> -o <thư mục>`.

---

## Scripts

| Script | Chức năng | Cú pháp |
|--------|-----------|---------|
| `validate_tikz.py` | Soi lỗi cú pháp trước khi biên dịch: lệch ngoặc, thiếu `;`, sai `--`, gõ nhầm lệnh | `python scripts/validate_tikz.py hinh.tex` |
| `compile_tikz.py` | Biên dịch ra PDF/PNG, tự bọc preamble nếu chỉ đưa đoạn mã | `python scripts/compile_tikz.py hinh.tex -o hinh.pdf`<br>`python scripts/compile_tikz.py -c "\draw (0,0) circle (1);" -o tron.pdf` |
| `extract_tikz.py` | Bóc các hình TikZ ra khỏi một tài liệu LaTeX lớn | `python scripts/extract_tikz.py tailieu.tex --list` |
| `pdf_to_md.py` | Trích xuất sách PDF thành tài liệu tham chiếu `.md` | `python scripts/pdf_to_md.py sach.pdf -o thumuc` |

Quy trình khuyến nghị: **viết mã → `validate_tikz.py` (0 lỗi) → `compile_tikz.py`**.

Xuất PNG cần ImageMagick. Trên Windows **phải** có lệnh `magick` — đừng gọi
`convert`, vì đó là tên của `C:\Windows\System32\convert.exe`, tiện ích chuyển
FAT sang NTFS, hoàn toàn không liên quan. Script đã tự tránh chỗ này.


## Lưu file output

**QUAN TRỌNG:** Khi đã có code TikZ, **BẮT BUỘC** lưu file `.tex` vào thư mục:

```
./output/
```

**Quy tắc đặt tên file:**
- Format: `LOAI_TEN_HINH.tex` — chữ HOA, không dấu, nối bằng `_`
- Ví dụ:
  - `GEOMETRY_TRIANGLE_CIRCUMCIRCLE.tex`
  - `PHYSICS_FORCE_VECTORS.tex`
  - `CHEMISTRY_BENZENE_STRUCTURE.tex`

> **Không dùng dấu ngoặc vuông trong tên file** (kiểu `[GEOMETRY]_...tex`).
> `pdflatex` đọc được, nhưng `[...]` là ký tự đại diện của PowerShell và của
> hầu hết công cụ glob — `Copy-Item`, `Remove-Item`, `Glob` sẽ lặng lẽ không
> khớp file nào. Vài file cũ trong `output/` còn dùng kiểu này, đổi tên dần.

**Sau khi lưu file, TỰ ĐỘNG biên dịch.** Cách gọn và chạy được trên cả Windows
lẫn Linux (không phụ thuộc `cd`, không dùng `&&` vốn lỗi trên PowerShell 5.1):

```bash
python "<SKILL_DIR>/scripts/validate_tikz.py" "<SKILL_DIR>/output/TEN_FILE.tex"
python "<SKILL_DIR>/scripts/compile_tikz.py"  "<SKILL_DIR>/output/TEN_FILE.tex" -o "<SKILL_DIR>/output/TEN_FILE.pdf"
```

Nếu muốn gọi thẳng `pdflatex` thì dùng `-output-directory` thay cho `cd`:

```bash
pdflatex -interaction=nonstopmode -output-directory "<SKILL_DIR>/output" "<SKILL_DIR>/output/TEN_FILE.tex"
```

Trong đó `<SKILL_DIR>` là đường dẫn tuyệt đối đến thư mục chứa file SKILL.md này.

**LƯU Ý:** Luôn validate rồi mới biên dịch. Hình có nhãn tiếng Việt thì preamble
bắt buộc có `\usepackage[utf8]{vietnam}` — chỉ dùng `inputenc` là rơi dấu, mất chữ.


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
