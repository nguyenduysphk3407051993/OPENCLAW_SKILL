---
name: tikz-stem-drawing
description: "Skill viết mã TikZ/PGF LaTeX vẽ hình minh họa cho bài tập STEM. Sử dụng khi cần vẽ: hình học phẳng/không gian (tam giác, tứ giác, đường tròn, hình hộp, hình chóp), đồ thị hàm số, biểu đồ, sơ đồ vật lý (vector lực, mạch điện, quang học, sóng), công thức cấu tạo hóa học (chemfig), sơ đồ phản ứng. Hỗ trợ TikZ, PGFplots, chemfig, circuitikz."
allowed-tools: Read, Write, Glob, Grep
argument-hint: "[loại hình] [mô tả]"
---

# TikZ STEM Drawing Skill

Skill chuyên dụng viết mã TikZ/PGF LaTeX để vẽ hình minh họa cho bài tập Toán, Vật lý, Hóa học.

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
| Môn học | Toán / Vật lý / Hóa học? |
| Loại hình | Hình phẳng / không gian / đồ thị / sơ đồ? |
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


## Lưu file output

**QUAN TRỌNG:** Khi đã có code TikZ, **BẮT BUỘC** lưu file `.tex` vào thư mục:

```
./output/
```

**Quy tắc đặt tên file:**
- Format: `[LOẠI]_TÊN_HÌNH.tex`
- Ví dụ:
  - `[GEOMETRY]_TRIANGLE_CIRCUMCIRCLE.tex`
  - `[PHYSICS]_FORCE_VECTORS.tex`
  - `[CHEMISTRY]_BENZENE_STRUCTURE.tex`

**Sau khi lưu file, TỰ ĐỘNG biên dịch bằng lệnh:**
```bash
cd "<SKILL_DIR>/output" && pdflatex "TÊN_FILE.tex"
```
Trong đó `<SKILL_DIR>` là đường dẫn tuyệt đối đến thư mục chứa file SKILL.md này.

**LƯU Ý:** Luôn chạy lệnh biên dịch ngay sau khi lưu file để tạo PDF.


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
