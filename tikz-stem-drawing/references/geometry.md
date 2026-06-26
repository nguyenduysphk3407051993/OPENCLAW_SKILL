# Mẫu TikZ - Hình học Toán

## Preamble chuẩn cho hình học

```latex
\documentclass[border=3pt,tikz,12pt]{standalone}
\usepackage[utf8]{vietnam}
\usetikzlibrary{calc,angles,intersections,positioning,shapes.geometric,arrows,decorations.markings,arrows.meta,patterns.meta,patterns,quotes}
\usetikzlibrary{hobby}
\usepackage{tikz-3dplot,pgfplots}
\pgfplotsset{compat=1.15}
\usepgfplotslibrary{polar}
\usepackage{tkz-tab}
\usepackage{amsmath}
\begin{document}
    \begin{tikzpicture}[
        point/.style={circle, fill, inner sep=1.5pt},
        line/.style={thick},
    ]
    % Code ở đây
    \end{tikzpicture}
\end{document}
```

---

## HÌNH HỌC PHẲNG

### 1. Tam giác cơ bản với nhãn

```latex
\begin{tikzpicture}
    % Đỉnh tam giác
    \coordinate (A) at (0,0);
    \coordinate (B) at (4,0);
    \coordinate (C) at (1.5,3);
    
    % Vẽ tam giác
    \draw[thick] (A) -- (B) -- (C) -- cycle;
    
    % Nhãn đỉnh
    \node[below left] at (A) {$A$};
    \node[below right] at (B) {$B$};
    \node[above] at (C) {$C$};
    
    % Đánh dấu điểm
    \foreach \p in {A,B,C} \fill (\p) circle (1.5pt);
\end{tikzpicture}
```

### 2. Tam giác với đường cao, trung tuyến, phân giác

```latex
\begin{tikzpicture}
    \coordinate (A) at (0,0);
    \coordinate (B) at (5,0);
    \coordinate (C) at (2,3.5);
    
    % Tam giác
    \draw[thick] (A) -- (B) -- (C) -- cycle;
    
    % === ĐƯỜNG CAO từ C ===
    \coordinate (H) at ($(A)!(C)!(B)$);  % Hình chiếu C lên AB
    \draw[red, thick] (C) -- (H);
    % Góc vuông tại H
    \draw[red] (H) ++(0,0.25) -- ++(-0.25,0) -- ++(0,-0.25);
    \node[below, red] at (H) {$H$};
    
    % === TRUNG TUYẾN từ A ===
    \coordinate (M) at ($(B)!0.5!(C)$);  % Trung điểm BC
    \draw[blue, thick] (A) -- (M);
    \node[right, blue] at (M) {$M$};
    
    % Nhãn đỉnh
    \node[below left] at (A) {$A$};
    \node[below right] at (B) {$B$};
    \node[above] at (C) {$C$};
\end{tikzpicture}
```

### 3. Tam giác vuông

```latex
\begin{tikzpicture}
    % Tam giác vuông tại A
    \coordinate (A) at (0,0);
    \coordinate (B) at (4,0);
    \coordinate (C) at (0,3);
    
    \draw[thick] (A) -- (B) -- (C) -- cycle;
    
    % Góc vuông tại A (hình vuông nhỏ)
    \draw (A) rectangle ++(0.3,0.3);
    
    % Nhãn
    \node[below left] at (A) {$A$};
    \node[below right] at (B) {$B$};
    \node[above left] at (C) {$C$};
\end{tikzpicture}
```

### 4. Tam giác với góc được đánh dấu

```latex
\usetikzlibrary{angles, quotes}

\begin{tikzpicture}
    \coordinate (A) at (0,0);
    \coordinate (B) at (4,0);
    \coordinate (C) at (1.5,3);
    
    \draw[thick] (A) -- (B) -- (C) -- cycle;
    
    % Góc tại A
    \draw pic[draw=blue, angle radius=8mm, "$\alpha$", angle eccentricity=1.3] 
        {angle=B--A--C};
    
    % Góc tại B
    \draw pic[draw=red, angle radius=6mm, "$\beta$", angle eccentricity=1.4] 
        {angle=C--B--A};
    
    % Góc tại C
    \draw pic[draw=green!60!black, angle radius=5mm, "$\gamma$", angle eccentricity=1.5] 
        {angle=A--C--B};
    
    \node[below left] at (A) {$A$};
    \node[below right] at (B) {$B$};
    \node[above] at (C) {$C$};
\end{tikzpicture}
```

### 5. Đường tròn ngoại tiếp tam giác

```latex
\begin{tikzpicture}
    % Tam giác
    \coordinate (A) at (0,0);
    \coordinate (B) at (4,0);
    \coordinate (C) at (1,2.5);
    
    % Tâm đường tròn ngoại tiếp (giao trung trực)
    % Tính bằng công thức
    \coordinate (O) at (2, 0.95);
    
    % Bán kính (khoảng cách từ O đến A)
    \pgfmathsetmacro{\R}{sqrt((2-0)^2 + (0.95-0)^2)}
    
    % Vẽ đường tròn
    \draw[blue, thick] (O) circle (\R);
    
    % Vẽ tam giác
    \draw[thick] (A) -- (B) -- (C) -- cycle;
    
    % Tâm O
    \fill[red] (O) circle (2pt);
    \node[below right] at (O) {$O$};
    
    % Bán kính
    \draw[dashed, red] (O) -- (A);
    
    \node[below left] at (A) {$A$};
    \node[below right] at (B) {$B$};
    \node[above] at (C) {$C$};
\end{tikzpicture}
```

### 6. Đường tròn và tiếp tuyến

```latex
\begin{tikzpicture}
    % Đường tròn tâm O bán kính 2
    \coordinate (O) at (0,0);
    \def\R{2}
    \draw[thick, blue] (O) circle (\R);
    
    % Điểm tiếp xúc T tại góc 60 độ
    \coordinate (T) at (60:\R);
    
    % Tiếp tuyến tại T (vuông góc với OT)
    % Tiếp tuyến dài 3cm mỗi bên
    \draw[red, thick] ($(T)!-1.5cm!90:(O)$) -- ($(T)!1.5cm!90:(O)$);
    
    % Bán kính OT
    \draw[thick] (O) -- (T);
    
    % Góc vuông tại T
    \draw (T) ++(150:0.25) -- ++(240:0.25) -- ++(330:0.25);
    
    % Nhãn
    \fill (O) circle (2pt);
    \fill (T) circle (2pt);
    \node[below] at (O) {$O$};
    \node[above right] at (T) {$T$};
\end{tikzpicture}
```

### 7. Hai đường tròn cắt nhau

```latex
\begin{tikzpicture}
    % Đường tròn 1
    \coordinate (O1) at (0,0);
    \draw[blue, thick] (O1) circle (2);
    
    % Đường tròn 2
    \coordinate (O2) at (2.5,0);
    \draw[red, thick] (O2) circle (1.8);
    
    % Giao điểm (tính gần đúng)
    \coordinate (A) at (1.2, 1.6);
    \coordinate (B) at (1.2, -1.6);
    
    % Dây cung chung
    \draw[green!60!black, thick] (A) -- (B);
    
    % Đường nối tâm
    \draw[dashed] (O1) -- (O2);
    
    % Nhãn
    \fill (O1) circle (2pt);
    \fill (O2) circle (2pt);
    \fill (A) circle (2pt);
    \fill (B) circle (2pt);
    \node[below left] at (O1) {$O_1$};
    \node[below right] at (O2) {$O_2$};
    \node[above right] at (A) {$A$};
    \node[below right] at (B) {$B$};
\end{tikzpicture}
```

### 8. Hình vuông và đường chéo

```latex
\begin{tikzpicture}
    \coordinate (A) at (0,0);
    \coordinate (B) at (3,0);
    \coordinate (C) at (3,3);
    \coordinate (D) at (0,3);
    
    % Hình vuông
    \draw[thick] (A) -- (B) -- (C) -- (D) -- cycle;
    
    % Đường chéo
    \draw[dashed, blue] (A) -- (C);
    \draw[dashed, blue] (B) -- (D);
    
    % Tâm (giao đường chéo)
    \coordinate (O) at ($(A)!0.5!(C)$);
    \fill[red] (O) circle (2pt);
    
    % Góc vuông tại các đỉnh
    \draw (A) rectangle ++(0.25,0.25);
    \draw (B) ++(-0.25,0) rectangle ++(0.25,0.25);
    \draw (C) ++(-0.25,-0.25) rectangle ++(0.25,0.25);
    \draw (D) ++(0,-0.25) rectangle ++(0.25,0.25);
    
    % Nhãn
    \node[below left] at (A) {$A$};
    \node[below right] at (B) {$B$};
    \node[above right] at (C) {$C$};
    \node[above left] at (D) {$D$};
    \node[above right] at (O) {$O$};
\end{tikzpicture}
```

### 9. Hình thang cân

```latex
\begin{tikzpicture}
    % Đáy lớn AB, đáy nhỏ CD
    \coordinate (A) at (0,0);
    \coordinate (B) at (5,0);
    \coordinate (C) at (3.5,2.5);
    \coordinate (D) at (1.5,2.5);
    
    % Vẽ hình thang
    \draw[thick] (A) -- (B) -- (C) -- (D) -- cycle;
    
    % Đường cao
    \coordinate (H) at (1.5,0);
    \draw[dashed, blue] (D) -- (H);
    \draw[blue] (H) rectangle ++(0.25,0.25);
    
    % Nhãn
    \node[below left] at (A) {$A$};
    \node[below right] at (B) {$B$};
    \node[above right] at (C) {$C$};
    \node[above left] at (D) {$D$};
    \node[below] at (H) {$H$};
\end{tikzpicture}
```

---

## HÌNH HỌC KHÔNG GIAN

### 10. Hình hộp chữ nhật

```latex
\begin{tikzpicture}[
    x={(1cm,0cm)},
    y={(0.4cm,0.3cm)},
    z={(0cm,1cm)}
]
    % Kích thước
    \def\a{4}  % chiều dài
    \def\b{3}  % chiều rộng
    \def\c{2.5}  % chiều cao
    
    % === MẶT ĐÁY ===
    \draw[thick] (0,0,0) -- (\a,0,0) -- (\a,\b,0) -- (0,\b,0) -- cycle;
    
    % === MẶT TRÊN ===
    \draw[thick] (0,0,\c) -- (\a,0,\c) -- (\a,\b,\c) -- (0,\b,\c) -- cycle;
    
    % === CẠNH BÊN (nét liền - nhìn thấy) ===
    \draw[thick] (0,0,0) -- (0,0,\c);
    \draw[thick] (\a,0,0) -- (\a,0,\c);
    \draw[thick] (\a,\b,0) -- (\a,\b,\c);
    
    % === CẠNH KHUẤT (nét đứt) ===
    \draw[dashed] (0,\b,0) -- (0,\b,\c);
    
    % === ĐƯỜNG CHÉO (nếu cần) ===
    % \draw[red, dashed] (0,0,0) -- (\a,\b,\c);
    
    % Nhãn đỉnh
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

### 11. Hình lập phương

```latex
\begin{tikzpicture}[
    x={(1cm,0cm)},
    y={(0.4cm,0.35cm)},
    z={(0cm,1cm)}
]
    \def\a{3}
    
    % Mặt đáy
    \draw[thick] (0,0,0) -- (\a,0,0) -- (\a,\a,0) -- (0,\a,0) -- cycle;
    
    % Mặt trên
    \draw[thick] (0,0,\a) -- (\a,0,\a) -- (\a,\a,\a) -- (0,\a,\a) -- cycle;
    
    % Cạnh bên nhìn thấy
    \draw[thick] (0,0,0) -- (0,0,\a);
    \draw[thick] (\a,0,0) -- (\a,0,\a);
    \draw[thick] (\a,\a,0) -- (\a,\a,\a);
    
    % Cạnh khuất
    \draw[dashed] (0,\a,0) -- (0,\a,\a);
    
    % Nhãn
    \node[below left] at (0,0,0) {$A$};
    \node[below right] at (\a,0,0) {$B$};
    \node[right] at (\a,\a,0) {$C$};
    \node[left] at (0,\a,0) {$D$};
    \node[above left] at (0,0,\a) {$A'$};
    \node[above right] at (\a,0,\a) {$B'$};
    \node[right] at (\a,\a,\a) {$C'$};
    \node[left] at (0,\a,\a) {$D'$};
\end{tikzpicture}
```

### 12. Hình chóp tam giác đều (S.ABC)

```latex
\begin{tikzpicture}[
    x={(1cm,0cm)},
    y={(0.5cm,0.4cm)},
    z={(0cm,1cm)}
]
    % Đáy tam giác đều
    \coordinate (A) at (0,0,0);
    \coordinate (B) at (4,0,0);
    \coordinate (C) at (2,3.46,0);  % 2*sqrt(3) ≈ 3.46
    
    % Tâm đáy (trọng tâm)
    \coordinate (G) at (2,1.15,0);
    
    % Đỉnh chóp
    \coordinate (S) at (2,1.15,4);
    
    % Vẽ đáy
    \draw[thick] (A) -- (B);
    \draw[thick] (B) -- (C);
    \draw[dashed] (C) -- (A);  % Cạnh khuất
    
    % Vẽ cạnh bên
    \draw[thick] (S) -- (A);
    \draw[thick] (S) -- (B);
    \draw[thick] (S) -- (C);
    
    % Đường cao
    \draw[dashed, blue] (S) -- (G);
    \fill[blue] (G) circle (2pt);
    
    % Nhãn
    \node[below left] at (A) {$A$};
    \node[below right] at (B) {$B$};
    \node[right] at (C) {$C$};
    \node[above] at (S) {$S$};
    \node[below] at (G) {$G$};
\end{tikzpicture}
```

### 13. Hình chóp tứ giác đều (S.ABCD)

```latex
\begin{tikzpicture}[
    x={(1cm,0cm)},
    y={(0.45cm,0.35cm)},
    z={(0cm,1cm)}
]
    % Đáy hình vuông
    \coordinate (A) at (0,0,0);
    \coordinate (B) at (3,0,0);
    \coordinate (C) at (3,3,0);
    \coordinate (D) at (0,3,0);
    
    % Tâm đáy
    \coordinate (O) at (1.5,1.5,0);
    
    % Đỉnh chóp
    \coordinate (S) at (1.5,1.5,4);
    
    % Vẽ đáy
    \draw[thick] (A) -- (B) -- (C);
    \draw[dashed] (C) -- (D) -- (A);  % Cạnh khuất
    
    % Vẽ cạnh bên
    \draw[thick] (S) -- (A);
    \draw[thick] (S) -- (B);
    \draw[thick] (S) -- (C);
    \draw[dashed] (S) -- (D);  % Cạnh khuất
    
    % Đường cao
    \draw[dashed, red] (S) -- (O);
    
    % Nhãn
    \node[below left] at (A) {$A$};
    \node[below right] at (B) {$B$};
    \node[right] at (C) {$C$};
    \node[left] at (D) {$D$};
    \node[above] at (S) {$S$};
    \node[below right] at (O) {$O$};
\end{tikzpicture}
```

### 14. Hình lăng trụ tam giác

```latex
\begin{tikzpicture}[
    x={(1cm,0cm)},
    y={(0.5cm,0.4cm)},
    z={(0cm,1cm)}
]
    % Đáy dưới
    \coordinate (A) at (0,0,0);
    \coordinate (B) at (4,0,0);
    \coordinate (C) at (1.5,3,0);
    
    % Đáy trên
    \coordinate (A') at (0,0,3);
    \coordinate (B') at (4,0,3);
    \coordinate (C') at (1.5,3,3);
    
    % Vẽ đáy dưới
    \draw[thick] (A) -- (B);
    \draw[dashed] (B) -- (C) -- (A);
    
    % Vẽ đáy trên
    \draw[thick] (A') -- (B') -- (C') -- cycle;
    
    % Cạnh bên
    \draw[thick] (A) -- (A');
    \draw[thick] (B) -- (B');
    \draw[dashed] (C) -- (C');
    
    % Nhãn
    \node[below left] at (A) {$A$};
    \node[below right] at (B) {$B$};
    \node[right] at (C) {$C$};
    \node[above left] at (A') {$A'$};
    \node[above right] at (B') {$B'$};
    \node[above] at (C') {$C'$};
\end{tikzpicture}
```

### 15. Hình trụ

```latex
\begin{tikzpicture}
    \def\R{1.5}
    \def\H{4}
    
    % Đáy dưới (elip)
    \draw[thick] (0,0) ellipse ({\R} and {0.5*\R});
    
    % Đáy trên (elip)
    \draw[thick] (0,\H) ellipse ({\R} and {0.5*\R});
    
    % Đường sinh
    \draw[thick] (-\R,0) -- (-\R,\H);
    \draw[thick] (\R,0) -- (\R,\H);
    
    % Trục
    \draw[dashed] (0,0) -- (0,\H);
    
    % Nhãn
    \fill (0,0) circle (2pt);
    \fill (0,\H) circle (2pt);
    \node[below] at (0,0) {$O$};
    \node[above] at (0,\H) {$O'$};
    
    % Bán kính
    \draw[blue, thick] (0,0) -- (\R,0) node[midway, below] {$R$};
    
    % Chiều cao
    \node[right] at ({\R+0.3}, {\H/2}) {$h$};
\end{tikzpicture}
```

### 16. Hình nón

```latex
\begin{tikzpicture}
    \def\R{2}
    \def\H{4}
    
    % Đáy (elip)
    \draw[thick] (0,0) ellipse ({\R} and {0.6*\R});
    
    % Đường sinh (cạnh bên)
    \coordinate (S) at (0,\H);
    \draw[thick] (-\R,0) -- (S) -- (\R,0);
    
    % Đường cao
    \draw[dashed] (S) -- (0,0);
    
    % Nhãn
    \fill (0,0) circle (2pt);
    \fill (S) circle (2pt);
    \node[below] at (0,0) {$O$};
    \node[above] at (S) {$S$};
    
    % Bán kính
    \draw[blue] (0,0) -- (\R,0) node[midway, below] {$R$};
\end{tikzpicture}
```

### 17. Hình cầu

```latex
\begin{tikzpicture}
    \def\R{2}
    
    % Đường tròn lớn
    \draw[thick] (0,0) circle (\R);
    
    % Elip ngang (đường xích đạo)
    \draw[dashed] (0,0) ellipse ({\R} and {0.35*\R});
    
    % Elip dọc
    \draw[dashed] (0,0) ellipse ({0.35*\R} and {\R});
    
    % Tâm
    \fill (0,0) circle (2pt);
    \node[below left] at (0,0) {$O$};
    
    % Bán kính
    \draw[blue, thick] (0,0) -- (45:\R) node[midway, above left] {$R$};
\end{tikzpicture}
```

---

## HỆ TỌA ĐỘ VÀ VECTOR

### 18. Hệ tọa độ Oxy với điểm

```latex
\begin{tikzpicture}[>=Stealth]
    % Trục tọa độ
    \draw[->] (-0.5,0) -- (5,0) node[right] {$x$};
    \draw[->] (0,-0.5) -- (0,4) node[above] {$y$};
    
    % Gốc tọa độ
    \node[below left] at (0,0) {$O$};
    
    % Chia vạch
    \foreach \x in {1,2,3,4} {
        \draw (\x,0.1) -- (\x,-0.1) node[below] {\x};
    }
    \foreach \y in {1,2,3} {
        \draw (0.1,\y) -- (-0.1,\y) node[left] {\y};
    }
    
    % Điểm A(2,3)
    \coordinate (A) at (2,3);
    \fill[red] (A) circle (2pt);
    \node[above right] at (A) {$A(2;3)$};
    
    % Đường gióng
    \draw[dashed, gray] (A) -- (2,0);
    \draw[dashed, gray] (A) -- (0,3);
\end{tikzpicture}
```

### 19. Vector và phép cộng vector

```latex
\begin{tikzpicture}[>=Stealth]
    \coordinate (O) at (0,0);
    \coordinate (A) at (3,1);
    \coordinate (B) at (1,2.5);
    \coordinate (C) at ($(A)+(B)$);  % Tổng vector
    
    % Vector a
    \draw[->, thick, blue] (O) -- (A) node[midway, below] {$\vec{a}$};
    
    % Vector b
    \draw[->, thick, red] (O) -- (B) node[midway, left] {$\vec{b}$};
    
    % Vector tổng
    \draw[->, thick, green!60!black, line width=1.2pt] (O) -- (C) 
        node[midway, above right] {$\vec{a}+\vec{b}$};
    
    % Quy tắc hình bình hành
    \draw[dashed, gray] (A) -- (C);
    \draw[dashed, gray] (B) -- (C);
\end{tikzpicture}
```

### 20. Hệ tọa độ Oxyz (3D)

```latex
\begin{tikzpicture}[>=Stealth,
    x={(0.8cm,-0.4cm)},
    y={(0.8cm,0.4cm)},
    z={(0cm,1cm)}
]
    % Trục tọa độ
    \draw[->] (0,0,0) -- (4,0,0) node[right] {$x$};
    \draw[->] (0,0,0) -- (0,4,0) node[above right] {$y$};
    \draw[->] (0,0,0) -- (0,0,4) node[above] {$z$};
    
    % Gốc
    \node[below] at (0,0,0) {$O$};
    
    % Điểm M(2,3,2)
    \coordinate (M) at (2,3,2);
    \fill[red] (M) circle (2pt);
    \node[above right] at (M) {$M(2;3;2)$};
    
    % Hình chiếu
    \coordinate (M') at (2,3,0);
    \draw[dashed, gray] (M) -- (M');
    \draw[dashed, gray] (M') -- (2,0,0);
    \draw[dashed, gray] (M') -- (0,3,0);
\end{tikzpicture}
```
