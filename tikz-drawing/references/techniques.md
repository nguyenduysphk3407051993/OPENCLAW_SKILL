# Kỹ thuật TikZ - Tham khảo nhanh

## THƯ VIỆN TIKZ THƯỜNG DÙNG

```latex
\usetikzlibrary{
    calc,                  % Tính toán tọa độ
    arrows.meta,           % Mũi tên đẹp
    angles,                % Đánh dấu góc
    quotes,                % Nhãn cho góc
    positioning,           % Vị trí tương đối (above, below, left, right of)
    patterns,              % Mẫu tô (north east lines, dots, ...)
    shapes.geometric,      % Hình học (ellipse, regular polygon, ...)
    decorations.pathmorphing,  % Sóng, lò xo
    decorations.markings,  % Đánh dấu trên đường
    intersections,         % Tìm giao điểm
    through,               % Đường tròn qua các điểm
    backgrounds,           % Vẽ nền
}
```

---

## TÍNH TOÁN TỌA ĐỘ VỚI `calc`

### Trung điểm

```latex
% Trung điểm của AB
\coordinate (M) at ($(A)!0.5!(B)$);
```

### Điểm chia theo tỉ lệ

```latex
% Điểm P chia AB theo tỉ lệ 1:2 (từ A)
\coordinate (P) at ($(A)!0.33!(B)$);

% Điểm Q chia AB theo tỉ lệ 2:1 (từ A)
\coordinate (Q) at ($(A)!0.67!(B)$);
```

### Hình chiếu vuông góc

```latex
% Hình chiếu của C lên đường thẳng AB
\coordinate (H) at ($(A)!(C)!(B)$);
```

### Điểm cách một khoảng cố định

```latex
% Điểm P cách A một đoạn 2cm theo hướng B
\coordinate (P) at ($(A)!2cm!(B)$);
```

### Điểm xoay

```latex
% Xoay B quanh A một góc 60 độ
\coordinate (C) at ($(A)!1!60:(B)$);
```

### Phép tịnh tiến

```latex
% Dịch chuyển A theo vector (2,3)
\coordinate (A') at ($(A)+(2,3)$);
```

### Phép đối xứng

```latex
% Đối xứng C qua đường thẳng AB
\coordinate (C') at ($(A)!(C)!(B)$);
\coordinate (C_sym) at ($(C)!2!(C')$);
```

---

## ĐÁNH DẤU GÓC

### Góc vuông (hình vuông nhỏ)

```latex
% Cách 1: Dùng rectangle
\draw (H) rectangle ++(0.3,0.3);

% Cách 2: Góc vuông xoay theo hướng
\draw (H) ++(0,0.25) -- ++(-0.25,0) -- ++(0,-0.25);
```

### Góc bất kỳ với nhãn

```latex
\usetikzlibrary{angles, quotes}

% Góc BAC với nhãn alpha
\draw pic[draw=blue, angle radius=8mm, "$\alpha$", angle eccentricity=1.3] 
    {angle=B--A--C};
```

### Góc với màu tô

```latex
\draw pic[draw=red, fill=red!20, angle radius=6mm, "$\beta$"] 
    {angle=C--B--A};
```

### Nhiều góc

```latex
% Cung tròn đơn
\draw (A) ++(0:0.5) arc (0:60:0.5);

% Cung tròn đôi (góc bằng nhau)
\draw (A) ++(0:0.4) arc (0:60:0.4);
\draw (A) ++(0:0.5) arc (0:60:0.5);
```

---

## KIỂU ĐƯỜNG

### Nét đứt và nét chấm

```latex
\draw[dashed] (A) -- (B);        % Nét đứt
\draw[dotted] (A) -- (B);        % Nét chấm
\draw[dash dot] (A) -- (B);      % Nét gạch chấm
\draw[dash dot dot] (A) -- (B);  % Nét gạch chấm chấm
```

### Độ dày

```latex
\draw[ultra thin] (A) -- (B);    % Rất mỏng
\draw[very thin] (A) -- (B);     % Mỏng
\draw[thin] (A) -- (B);          % Bình thường
\draw[thick] (A) -- (B);         % Dày
\draw[very thick] (A) -- (B);    % Rất dày
\draw[ultra thick] (A) -- (B);   % Cực dày
\draw[line width=2pt] (A) -- (B);% Tùy chỉnh
```

### Màu sắc

```latex
\draw[red] (A) -- (B);
\draw[blue!60] (A) -- (B);       % 60% blue
\draw[green!50!black] (A) -- (B);% Pha màu
```

---

## MŨI TÊN

### Kiểu mũi tên

```latex
\usetikzlibrary{arrows.meta}

\draw[->] (A) -- (B);            % Mũi tên đơn giản
\draw[<->] (A) -- (B);           % Hai chiều
\draw[-{Stealth}] (A) -- (B);    % Stealth (đẹp)
\draw[-{Latex}] (A) -- (B);      % Latex arrow
\draw[-{Triangle}] (A) -- (B);   % Tam giác
\draw[-{Circle}] (A) -- (B);     % Tròn
```

### Tùy chỉnh mũi tên

```latex
\draw[-{Stealth[length=3mm, width=2mm]}] (A) -- (B);
\draw[-{Stealth[scale=1.5]}] (A) -- (B);
```

---

## TÔ MÀU VÀ PATTERN

### Tô màu đơn

```latex
\fill[blue!30] (A) -- (B) -- (C) -- cycle;
```

### Tô màu với viền

```latex
\draw[thick, fill=red!20] (A) -- (B) -- (C) -- cycle;
```

### Pattern (mẫu tô)

```latex
\usetikzlibrary{patterns}

\fill[pattern=north east lines] (0,0) rectangle (2,1);
\fill[pattern=north west lines] (0,0) rectangle (2,1);
\fill[pattern=horizontal lines] (0,0) rectangle (2,1);
\fill[pattern=vertical lines] (0,0) rectangle (2,1);
\fill[pattern=grid] (0,0) rectangle (2,1);
\fill[pattern=dots] (0,0) rectangle (2,1);
\fill[pattern=crosshatch] (0,0) rectangle (2,1);
```

### Độ trong suốt

```latex
\fill[blue, opacity=0.3] (A) -- (B) -- (C) -- cycle;
```

---

## NHÃN VÀ VĂN BẢN

### Vị trí nhãn

```latex
\node[above] at (A) {$A$};
\node[below] at (A) {$A$};
\node[left] at (A) {$A$};
\node[right] at (A) {$A$};
\node[above left] at (A) {$A$};
\node[above right] at (A) {$A$};
\node[below left] at (A) {$A$};
\node[below right] at (A) {$A$};
```

### Nhãn trên đường

```latex
\draw (A) -- (B) node[midway, above] {$5$};
\draw (A) -- (B) node[midway, below] {$AB = 5$};
\draw (A) -- (B) node[pos=0.3, above] {text};  % Vị trí 30% từ A
```

### Font và kích thước

```latex
\node[font=\small] at (A) {text};
\node[font=\large] at (A) {text};
\node[font=\bfseries] at (A) {bold};
\node[font=\itshape] at (A) {italic};
```

---

## VÒNG LẶP

### Vẽ nhiều điểm

```latex
\foreach \p in {A, B, C, D} {
    \fill (\p) circle (2pt);
}
```

### Vẽ nhiều đường

```latex
\foreach \i in {1,2,3,4,5} {
    \draw (0,\i*0.5) -- (3,\i*0.5);
}
```

### Đánh số điểm

```latex
\foreach \i in {0,1,2,3,4} {
    \coordinate (P\i) at (\i,0);
    \fill (P\i) circle (2pt);
    \node[below] at (P\i) {$P_\i$};
}
```

---

## HÌNH CƠ BẢN

### Đường thẳng

```latex
\draw (A) -- (B);
```

### Đường gấp khúc

```latex
\draw (A) -- (B) -- (C) -- (D);
```

### Đa giác khép kín

```latex
\draw (A) -- (B) -- (C) -- cycle;
```

### Đường tròn

```latex
\draw (O) circle (2);              % Tâm O, bán kính 2
\draw (O) circle [radius=2cm];     % Tương đương
```

### Elip

```latex
\draw (O) ellipse (2 and 1);       % Bán trục 2 và 1
```

### Cung tròn

```latex
\draw (O) arc (0:90:2);            % Từ 0° đến 90°, bán kính 2
\draw (O) ++(30:2) arc (30:120:2); % Cung từ 30° đến 120°
```

### Hình chữ nhật

```latex
\draw (0,0) rectangle (3,2);
\draw[rounded corners=5pt] (0,0) rectangle (3,2);  % Bo góc
```

---

## SCOPE VÀ TRANSFORM

### Xoay

```latex
\begin{scope}[rotate=45]
    \draw (0,0) rectangle (2,1);
\end{scope}
```

### Dịch chuyển

```latex
\begin{scope}[shift={(3,2)}]
    \draw (0,0) circle (1);
\end{scope}
```

### Scale

```latex
\begin{scope}[scale=0.5]
    \draw (0,0) -- (4,0) -- (2,3) -- cycle;
\end{scope}
```

### Kết hợp nhiều transform

```latex
\begin{scope}[shift={(2,1)}, rotate=30, scale=0.8]
    % Code vẽ
\end{scope}
```

---

## GỢI Ý THỰC HÀNH

### 1. Luôn định nghĩa coordinate trước

```latex
% Tốt
\coordinate (A) at (0,0);
\coordinate (B) at (4,0);
\draw (A) -- (B);

% Không nên
\draw (0,0) -- (4,0);  % Khó sửa đổi sau
```

### 2. Dùng style để tái sử dụng

```latex
\begin{tikzpicture}[
    point/.style={circle, fill, inner sep=1.5pt},
    main/.style={thick, blue},
    aux/.style={thin, dashed, gray},
]
    \draw[main] (A) -- (B);
    \draw[aux] (C) -- (D);
    \node[point] at (A) {};
\end{tikzpicture}
```

### 3. Comment rõ ràng

```latex
% === PHẦN 1: VẼ TAM GIÁC ===
\draw[thick] (A) -- (B) -- (C) -- cycle;

% === PHẦN 2: ĐƯỜNG CAO ===
\coordinate (H) at ($(A)!(C)!(B)$);
\draw[dashed] (C) -- (H);
```

### 4. Kiểm tra biên dịch thường xuyên

Sau mỗi phần code nhỏ, compile để phát hiện lỗi sớm.
