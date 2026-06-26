# Ví dụ Input/Output - TikZ STEM Drawing

Tài liệu này chứa các ví dụ cụ thể về cách chuyển đổi yêu cầu bài tập thành code TikZ.

---

## TOÁN HỌC

### Ví dụ 1: Tam giác với đường cao

**Yêu cầu:**
> Vẽ tam giác ABC, kẻ đường cao AH

**Phân tích:**
- Đối tượng: Tam giác ABC, đường cao AH
- H là chân đường cao từ A xuống BC
- Cần đánh dấu góc vuông tại H

**Output:**
```latex
\begin{tikzpicture}
    % Đỉnh tam giác
    \coordinate (A) at (1.5,3);
    \coordinate (B) at (0,0);
    \coordinate (C) at (4,0);
    
    % Chân đường cao H (hình chiếu A lên BC)
    \coordinate (H) at ($(B)!(A)!(C)$);
    
    % Vẽ tam giác
    \draw[thick] (A) -- (B) -- (C) -- cycle;
    
    % Đường cao AH
    \draw[blue, thick] (A) -- (H);
    
    % Góc vuông tại H
    \draw[blue] (H) ++(0,0.25) -- ++(-0.25,0) -- ++(0,-0.25);
    
    % Nhãn
    \node[above] at (A) {$A$};
    \node[below left] at (B) {$B$};
    \node[below right] at (C) {$C$};
    \node[below] at (H) {$H$};
    
    % Đánh dấu điểm
    \foreach \p in {A,B,C,H} \fill (\p) circle (1.5pt);
\end{tikzpicture}
```

---

### Ví dụ 2: Tam giác vuông với đường cao

**Yêu cầu:**
> Cho tam giác ABC vuông tại A, đường cao AH. Đánh dấu các góc vuông.

**Phân tích:**
- Tam giác vuông tại A → A nằm ở góc vuông
- H là chân đường cao từ A lên BC (cạnh huyền)
- Cần 2 góc vuông: tại A và tại H

**Output:**
```latex
\begin{tikzpicture}
    % Tam giác vuông tại A
    \coordinate (A) at (0,0);
    \coordinate (B) at (4,0);
    \coordinate (C) at (0,3);
    
    % Chân đường cao (A chiếu lên BC)
    \coordinate (H) at ($(B)!(A)!(C)$);
    
    % Vẽ tam giác
    \draw[thick] (A) -- (B) -- (C) -- cycle;
    
    % Đường cao AH
    \draw[red, thick] (A) -- (H);
    
    % Góc vuông tại A
    \draw (A) rectangle ++(0.3,0.3);
    
    % Góc vuông tại H (xoay theo hướng BC)
    \draw[red] (H) ++(-0.18,0.22) -- ++(-0.22,-0.18) -- ++(0.18,-0.22);
    
    % Nhãn
    \node[below left] at (A) {$A$};
    \node[below right] at (B) {$B$};
    \node[above left] at (C) {$C$};
    \node[above right] at (H) {$H$};
\end{tikzpicture}
```

---

### Ví dụ 3: Đường tròn ngoại tiếp tam giác

**Yêu cầu:**
> Vẽ tam giác ABC nội tiếp đường tròn (O), vẽ bán kính OA

**Phân tích:**
- Cần vẽ đường tròn trước, tam giác sau
- Tâm O, bán kính R
- Ba đỉnh nằm trên đường tròn

**Output:**
```latex
\begin{tikzpicture}
    % Tâm và bán kính
    \coordinate (O) at (0,0);
    \def\R{2.5}
    
    % Đường tròn
    \draw[blue, thick] (O) circle (\R);
    
    % Ba đỉnh trên đường tròn (dùng góc)
    \coordinate (A) at (90:\R);   % 90 độ
    \coordinate (B) at (210:\R);  % 210 độ
    \coordinate (C) at (330:\R);  % 330 độ
    
    % Tam giác
    \draw[thick] (A) -- (B) -- (C) -- cycle;
    
    % Bán kính OA
    \draw[red, dashed] (O) -- (A);
    
    % Nhãn
    \fill (O) circle (2pt);
    \node[below] at (O) {$O$};
    \node[above] at (A) {$A$};
    \node[below left] at (B) {$B$};
    \node[below right] at (C) {$C$};
    \node[left, red] at ($(O)!0.5!(A)$) {$R$};
\end{tikzpicture}
```

---

### Ví dụ 4: Hình hộp chữ nhật

**Yêu cầu:**
> Vẽ hình hộp chữ nhật ABCD.A'B'C'D', đường chéo AC'

**Phân tích:**
- Hình 3D, cần thiết lập hệ tọa độ
- Cạnh khuất vẽ nét đứt
- Đường chéo AC' xuyên qua hình hộp

**Output:**
```latex
\begin{tikzpicture}[
    x={(1cm,0cm)},
    y={(0.4cm,0.3cm)},
    z={(0cm,1cm)}
]
    \def\a{3.5}  % chiều dài
    \def\b{2.5}  % chiều rộng  
    \def\c{2}    % chiều cao
    
    % Mặt đáy ABCD
    \draw[thick] (0,0,0) -- (\a,0,0) -- (\a,\b,0) -- (0,\b,0) -- cycle;
    
    % Mặt trên A'B'C'D'
    \draw[thick] (0,0,\c) -- (\a,0,\c) -- (\a,\b,\c) -- (0,\b,\c) -- cycle;
    
    % Cạnh bên nhìn thấy
    \draw[thick] (0,0,0) -- (0,0,\c);
    \draw[thick] (\a,0,0) -- (\a,0,\c);
    \draw[thick] (\a,\b,0) -- (\a,\b,\c);
    
    % Cạnh khuất
    \draw[dashed] (0,\b,0) -- (0,\b,\c);
    
    % Đường chéo AC'
    \draw[red, thick] (0,0,0) -- (\a,\b,\c);
    
    % Nhãn
    \node[below left] at (0,0,0) {$A$};
    \node[below right] at (\a,0,0) {$B$};
    \node[right] at (\a,\b,0) {$C$};
    \node[left] at (0,\b,0) {$D$};
    \node[above left] at (0,0,\c) {$A'$};
    \node[above right] at (\a,0,\c) {$B'$};
    \node[right] at (\a,\b,\c) {$C'$};
    \node[left] at (0,\b,\c) {$D'$};
\end{tikzpicture}
```

---

## VẬT LÝ

### Ví dụ 5: Vật trên mặt phẳng nghiêng

**Yêu cầu:**
> Vẽ vật trên mặt phẳng nghiêng góc alpha, phân tích trọng lực P thành Px và Py

**Phân tích:**
- Mặt phẳng nghiêng góc α
- Vật hình chữ nhật trên mặt nghiêng
- P thẳng đứng xuống
- Px song song mặt nghiêng
- Py vuông góc mặt nghiêng

**Output:**
```latex
\begin{tikzpicture}[>=Stealth]
    \def\angle{30}
    
    % Mặt phẳng nghiêng
    \draw[thick] (0,0) -- (6,0) -- (6,{6*tan(\angle)}) -- cycle;
    \fill[pattern=north east lines] (0,0) -- (6,0) -- (6,{6*tan(\angle)}) -- cycle;
    
    % Vật (xoay theo mặt nghiêng)
    \begin{scope}[rotate=\angle]
        \draw[fill=blue!20, thick] (2.8,0.1) rectangle (4,1.1);
        \coordinate (G) at (3.4,0.6);
    \end{scope}
    
    % Trọng lực P (thẳng đứng)
    \draw[->, thick, red, line width=1.2pt] (G) -- ++(0,-2) node[right] {$\vec{P}$};
    
    % Phân tích: Py vuông góc mặt nghiêng
    \draw[->, thick, blue, line width=1pt] (G) -- ++({-1.5*sin(\angle)},{-1.5*cos(\angle)}) 
        node[left] {$\vec{P_y}$};
    
    % Phân tích: Px song song mặt nghiêng (hướng xuống dốc)
    \draw[->, thick, green!60!black, line width=1pt] (G) -- ++({1.2*cos(\angle)},{-1.2*sin(\angle)}) 
        node[below right] {$\vec{P_x}$};
    
    % Góc nghiêng
    \draw (1.2,0) arc (0:\angle:1.2);
    \node at (1.5,0.35) {$\alpha$};
\end{tikzpicture}
```

---

### Ví dụ 6: Mạch điện nối tiếp

**Yêu cầu:**
> Vẽ mạch điện gồm nguồn E, hai điện trở R1 và R2 mắc nối tiếp, có ampe kế

**Output:**
```latex
\usepackage{circuitikz}

\begin{circuitikz}[european]
\draw
    (0,0) to[battery1, l=$E$, invert] (0,3)
    to[short] (3,3)
    to[R, l=$R_1$] (3,1.5)
    to[R, l=$R_2$] (3,0)
    to[ammeter, l=$A$] (0,0);
\end{circuitikz}
```

---

### Ví dụ 7: Phản xạ ánh sáng

**Yêu cầu:**
> Vẽ tia sáng phản xạ trên gương phẳng, đánh dấu góc tới i và góc phản xạ r

**Output:**
```latex
\begin{tikzpicture}[>=Stealth]
    % Gương phẳng
    \draw[thick] (0,0) -- (5,0);
    \fill[pattern=north east lines] (0,-0.3) rectangle (5,0);
    
    % Điểm tới I
    \coordinate (I) at (2.5,0);
    
    % Pháp tuyến
    \draw[dashed, thick] (I) -- ++(0,3) node[above] {$N$};
    
    % Tia tới
    \draw[->, red, thick, line width=1.2pt] (0.5,2.5) -- (I);
    
    % Tia phản xạ
    \draw[->, blue, thick, line width=1.2pt] (I) -- (4.5,2.5);
    
    % Góc tới i
    \draw (2.5,0.8) arc (90:120:0.8);
    \node at (2.1,1.1) {$i$};
    
    % Góc phản xạ r
    \draw (2.5,0.8) arc (90:60:0.8);
    \node at (2.9,1.1) {$r$};
    
    \fill (I) circle (2pt);
    \node[below] at (I) {$I$};
\end{tikzpicture}
```

---

## HÓA HỌC

### Ví dụ 8: Công thức cấu tạo Etanol

**Yêu cầu:**
> Viết CTCT thu gọn và đầy đủ của Etanol (C2H5OH)

**Output:**
```latex
\usepackage{chemfig}

% CTCT thu gọn
\chemfig{H_3C-CH_2-OH}

% CTCT đầy đủ (hiển thị tất cả H)
\chemfig{H-C(-[2]H)(-[6]H)-C(-[2]H)(-[6]H)-O-H}
```

---

### Ví dụ 9: Sơ đồ phản ứng chuỗi

**Yêu cầu:**
> Viết sơ đồ: CH4 → CH3Cl → CH3OH → HCHO

**Output:**
```latex
\schemestart
\chemfig{CH_4}
\arrow{->[\chemfig{Cl_2}][as]}
\chemfig{CH_3Cl}
\arrow{->[\chemfig{NaOH}][$t^\circ$]}
\chemfig{CH_3OH}
\arrow{->[\chemfig{CuO}][$t^\circ$]}
\chemfig{HCHO}
\schemestop
```

---

### Ví dụ 10: Vòng Benzen có nhóm thế

**Yêu cầu:**
> Vẽ CTCT của Phenol (C6H5OH) và Anilin (C6H5NH2)

**Output:**
```latex
% Phenol
\chemfig{*6(=-=(-OH)-=-)}

% Anilin
\chemfig{*6(=-=(-NH_2)-=-)}

% Para-Cresol (4-methylphenol)
\chemfig{*6(=-=(-OH)-=-(-CH_3))}
```

---

## ĐỒ THỊ

### Ví dụ 11: Đồ thị hàm bậc hai

**Yêu cầu:**
> Vẽ đồ thị y = x² - 4x + 3, đánh dấu đỉnh và giao điểm với trục Ox

**Phân tích:**
- Đỉnh: x = 2, y = -1 → I(2, -1)
- Giao Ox: y = 0 → x = 1 hoặc x = 3

**Output:**
```latex
\begin{tikzpicture}
\begin{axis}[
    axis lines=middle,
    xlabel={$x$}, ylabel={$y$},
    xmin=-1, xmax=5,
    ymin=-2, ymax=5,
    grid=both,
    samples=50,
]
    % Parabol
    \addplot[blue, thick, domain=-0.5:4.5] {x^2 - 4*x + 3};
    
    % Đỉnh I(2, -1)
    \addplot[mark=*, red, mark size=3pt] coordinates {(2,-1)};
    \node[below, red] at (axis cs:2,-1) {$I(2;-1)$};
    
    % Giao Ox: (1,0) và (3,0)
    \addplot[mark=*, green!60!black, mark size=2pt] coordinates {(1,0) (3,0)};
    \node[above left] at (axis cs:1,0) {$(1;0)$};
    \node[above right] at (axis cs:3,0) {$(3;0)$};
    
    % Trục đối xứng
    \draw[dashed, red] (axis cs:2,-2) -- (axis cs:2,5);
\end{axis}
\end{tikzpicture}
```

---

## ANTI-PATTERNS (Những gì KHÔNG nên làm)

### ❌ Sai: Không định nghĩa coordinate

```latex
% SAI - Khó sửa đổi
\draw (0,0) -- (4,0) -- (2,3) -- cycle;
\node at (0,0) {$A$};
```

### ✅ Đúng: Định nghĩa coordinate trước

```latex
% ĐÚNG - Dễ sửa đổi
\coordinate (A) at (0,0);
\coordinate (B) at (4,0);
\coordinate (C) at (2,3);
\draw (A) -- (B) -- (C) -- cycle;
\node[below left] at (A) {$A$};
```

---

### ❌ Sai: Không đánh dấu góc vuông

```latex
% SAI - Thiếu góc vuông
\draw (A) -- (B) -- (C) -- cycle;
\draw (A) -- (H);  % Đường cao nhưng không có góc vuông
```

### ✅ Đúng: Luôn đánh dấu góc vuông

```latex
% ĐÚNG
\draw (A) -- (B) -- (C) -- cycle;
\draw (A) -- (H);
\draw (H) ++(0,0.25) -- ++(-0.25,0) -- ++(0,-0.25);  % Góc vuông
```

---

### ❌ Sai: Cạnh khuất vẽ nét liền

```latex
% SAI - Hình 3D mà không có nét đứt
\draw[thick] (0,0,0) -- (0,\b,0);  % Cạnh khuất cũng nét liền
```

### ✅ Đúng: Cạnh khuất vẽ nét đứt

```latex
% ĐÚNG
\draw[dashed] (0,\b,0) -- (0,\b,\c);  % Cạnh khuất nét đứt
```
