---
name: tikz-stem-drawing
description: "Skill viết mã TikZ/PGF LaTeX vẽ hình minh họa cho bài tập STEM. Sử dụng khi cần vẽ: hình học phẳng/không gian (tam giác, tứ giác, đường tròn, hình hộp, hình chóp), đồ thị hàm số, biểu đồ, sơ đồ vật lý (vector lực, mạch điện, quang học, sóng), công thức cấu tạo hóa học (chemfig), sơ đồ phản ứng. Hỗ trợ TikZ, PGFplots, chemfig, circuitikz."
allowed-tools: Read, Write, Glob, Grep
argument-hint: "[loại hình] [mô tả]"
---

# TikZ STEM Drawing Skill

Skill chuyên dụng viết mã TikZ/PGF LaTeX để vẽ hình minh họa cho bài tập Toán, Vật lý, Hóa học.

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
 \path(0, 0) coordinate (p1)
```

### 2. Dùng calc cho mọi tính toán
```latex
% Trung điểm M của AB
\path($(A)!0.5!(B)$) coordinate (M);

% Điểm chia theo tỉ lệ 2:1
\path ($(A)!0.67!(B)$) coordinate (M);
% Hình chiếu vuông góc của C lên AB
\coordinate (H) at ($(A)!(C)!(B)$);

% Điểm cách A một khoảng 2cm theo hướng B
\coordinate (P) at ($(A)!2cm!(B)$);
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
    \coordinate (A) at (0,0);
    \coordinate (B) at (4,0);
    \coordinate (C) at (0,3);
    
    % Chân đường cao
    \coordinate (H) at ($(B)!(A)!(C)$);
    
    % Vẽ tam giác
    \draw[thick] (A) -- (B) -- (C) -- cycle;
    
    % Đường cao AH
    \draw[blue, thick] (A) -- (H);
    
    % Góc vuông tại A
    \draw (A) rectangle ++(0.3,0.3);
    
    % Góc vuông tại H
    \draw (H) ++(-0.2,0.15) -- ++(-0.15,-0.2) -- ++(0.2,-0.15);
    
    % Nhãn
    \node[below left] at (A) {$A$};
    \node[below right] at (B) {$B$};
    \node[above] at (C) {$C$};
    \node[above right] at (H) {$H$};
    
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