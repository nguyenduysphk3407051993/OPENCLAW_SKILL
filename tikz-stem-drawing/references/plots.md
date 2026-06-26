# Mẫu TikZ - Đồ thị và Biểu đồ

## Preamble chuẩn cho đồ thị

```latex
\documentclass[tikz,border=5pt]{standalone}
\usepackage{pgfplots}
\pgfplotsset{compat=1.18}
\usepgfplotslibrary{fillbetween}
\usepackage[utf8]{vietnam}
\usetikzlibrary{calc,angles,intersections,positioning,shapes.geometric,arrows,decorations.markings,arrows.meta,patterns.meta,patterns,quotes}
\usetikzlibrary{hobby}
\usepackage{tikz-3dplot,pgfplots}
\pgfplotsset{compat=1.15}
\usepgfplotslibrary{polar}
\usepackage{tkz-tab}
\usepackage{amsmath}
\begin{document}
\begin{tikzpicture}
\begin{axis}[
    axis lines=middle,
    xlabel={$x$},
    ylabel={$y$},
]
% Code plot ở đây
\end{axis}
\end{tikzpicture}
\end{document}
```

---

## ĐỒ THỊ HÀM SỐ

### 1. Hàm số bậc nhất y = ax + b

```latex
\begin{tikzpicture}
\begin{axis}[
    axis lines=middle,
    xlabel={$x$}, ylabel={$y$},
    xmin=-4, xmax=5,
    ymin=-3, ymax=6,
    xtick={-3,-2,-1,1,2,3,4},
    ytick={-2,-1,1,2,3,4,5},
    grid=both,
    grid style={line width=0.2pt, gray!30},
]
    % y = 2x - 1
    \addplot[blue, thick, domain=-2:4, samples=2] {2*x - 1};
    \addlegendentry{$y = 2x - 1$}
    
    % Giao điểm với trục Ox
    \addplot[mark=*, only marks, red] coordinates {(0.5,0)};
    \node[below right] at (axis cs:0.5,0) {$(0.5;0)$};
    
    % Giao điểm với trục Oy
    \addplot[mark=*, only marks, red] coordinates {(0,-1)};
    \node[below left] at (axis cs:0,-1) {$(0;-1)$};
\end{axis}
\end{tikzpicture}
```

### 2. Hàm số bậc hai y = ax² + bx + c (Parabol)

```latex
\begin{tikzpicture}
\begin{axis}[
    axis lines=middle,
    xlabel={$x$}, ylabel={$y$},
    xmin=-4, xmax=4,
    ymin=-2, ymax=10,
    samples=100,
    grid=both,
    grid style={gray!30},
]
    % y = x^2
    \addplot[red, thick, domain=-3:3] {x^2};
    \addlegendentry{$y = x^2$}
    
    % Đỉnh parabol
    \addplot[mark=*, only marks, blue, mark size=3pt] coordinates {(0,0)};
    \node[below right] at (axis cs:0,0) {$O(0;0)$};
    
    % Trục đối xứng
    \draw[dashed, blue] (axis cs:0,-1) -- (axis cs:0,10);
\end{axis}
\end{tikzpicture}
```

### 3. Parabol y = -x² + 4x - 3

```latex
\begin{tikzpicture}
\begin{axis}[
    axis lines=middle,
    xlabel={$x$}, ylabel={$y$},
    xmin=-1, xmax=5,
    ymin=-4, ymax=3,
    samples=100,
    grid=both,
]
    \addplot[blue, thick, domain=-0.5:4.5] {-x^2 + 4*x - 3};
    \addlegendentry{$y = -x^2 + 4x - 3$}
    
    % Đỉnh (2, 1)
    \addplot[mark=*, red, mark size=3pt] coordinates {(2,1)};
    \node[above] at (axis cs:2,1) {$I(2;1)$};
    
    % Giao Ox: x=1, x=3
    \addplot[mark=*, green!60!black, mark size=2pt] coordinates {(1,0) (3,0)};
\end{axis}
\end{tikzpicture}
```

### 4. Nhiều hàm số trên cùng đồ thị

```latex
\begin{tikzpicture}
\begin{axis}[
    axis lines=middle,
    xlabel={$x$}, ylabel={$y$},
    xmin=-4, xmax=4,
    ymin=-5, ymax=10,
    legend pos=north west,
    grid=both,
]
    \addplot[blue, thick, domain=-3:3] {x^2};
    \addlegendentry{$y = x^2$}
    
    \addplot[red, thick, domain=-4:4] {2*x + 1};
    \addlegendentry{$y = 2x + 1$}
    
    \addplot[green!60!black, thick, domain=-2.5:2.5] {-x^2 + 4};
    \addlegendentry{$y = -x^2 + 4$}
\end{axis}
\end{tikzpicture}
```

### 5. Hàm số bậc ba

```latex
\begin{tikzpicture}
\begin{axis}[
    axis lines=middle,
    xlabel={$x$}, ylabel={$y$},
    xmin=-3, xmax=3,
    ymin=-10, ymax=10,
    samples=100,
]
    % y = x^3 - 3x
    \addplot[blue, thick, domain=-2.5:2.5] {x^3 - 3*x};
    \addlegendentry{$y = x^3 - 3x$}
    
    % Cực đại (-1, 2)
    \addplot[mark=*, red] coordinates {(-1,2)};
    \node[above left] at (axis cs:-1,2) {CĐ$(-1;2)$};
    
    % Cực tiểu (1, -2)
    \addplot[mark=*, red] coordinates {(1,-2)};
    \node[below right] at (axis cs:1,-2) {CT$(1;-2)$};
\end{axis}
\end{tikzpicture}
```

### 6. Hàm số phân thức y = (ax+b)/(cx+d)

```latex
\begin{tikzpicture}
\begin{axis}[
    axis lines=middle,
    xlabel={$x$}, ylabel={$y$},
    xmin=-6, xmax=6,
    ymin=-6, ymax=6,
    samples=200,
    restrict y to domain=-10:10,
]
    % y = (2x+1)/(x-1)
    \addplot[blue, thick, domain=-6:0.9] {(2*x+1)/(x-1)};
    \addplot[blue, thick, domain=1.1:6] {(2*x+1)/(x-1)};
    
    % Tiệm cận đứng x = 1
    \draw[dashed, red] (axis cs:1,-6) -- (axis cs:1,6);
    \node[above, red] at (axis cs:1,5) {$x=1$};
    
    % Tiệm cận ngang y = 2
    \draw[dashed, green!60!black] (axis cs:-6,2) -- (axis cs:6,2);
    \node[right, green!60!black] at (axis cs:5,2) {$y=2$};
\end{axis}
\end{tikzpicture}
```

### 7. Hàm số lượng giác

```latex
\begin{tikzpicture}
\begin{axis}[
    axis lines=middle,
    xlabel={$x$}, ylabel={$y$},
    xmin=-2*pi-0.5, xmax=2*pi+0.5,
    ymin=-1.5, ymax=1.5,
    xtick={-6.28, -4.71, -3.14, -1.57, 0, 1.57, 3.14, 4.71, 6.28},
    xticklabels={$-2\pi$, $-\frac{3\pi}{2}$, $-\pi$, $-\frac{\pi}{2}$, $0$, 
                 $\frac{\pi}{2}$, $\pi$, $\frac{3\pi}{2}$, $2\pi$},
    samples=200,
    grid=both,
]
    \addplot[blue, thick, domain=-2*pi:2*pi] {sin(deg(x))};
    \addlegendentry{$y = \sin x$}
    
    \addplot[red, thick, dashed, domain=-2*pi:2*pi] {cos(deg(x))};
    \addlegendentry{$y = \cos x$}
\end{axis}
\end{tikzpicture}
```

### 8. Hàm số mũ và logarit

```latex
\begin{tikzpicture}
\begin{axis}[
    axis lines=middle,
    xlabel={$x$}, ylabel={$y$},
    xmin=-3, xmax=4,
    ymin=-2, ymax=8,
    samples=100,
    legend pos=north west,
]
    % y = e^x
    \addplot[blue, thick, domain=-3:2.1] {exp(x)};
    \addlegendentry{$y = e^x$}
    
    % y = ln(x)
    \addplot[red, thick, domain=0.05:4] {ln(x)};
    \addlegendentry{$y = \ln x$}
    
    % y = x (đường phân giác)
    \addplot[dashed, gray, domain=-2:4] {x};
\end{axis}
\end{tikzpicture}
```

---

## BIỂU ĐỒ

### 9. Biểu đồ cột đơn

```latex
\begin{tikzpicture}
\begin{axis}[
    ybar,
    xlabel={Tháng},
    ylabel={Doanh thu (triệu đồng)},
    symbolic x coords={T1, T2, T3, T4, T5, T6},
    xtick=data,
    ymin=0, ymax=150,
    bar width=18pt,
    nodes near coords,
    nodes near coords align={vertical},
    enlarge x limits=0.15,
]
    \addplot[fill=blue!60, draw=blue!80] coordinates {
        (T1, 80) (T2, 95) (T3, 110) (T4, 85) (T5, 120) (T6, 105)
    };
\end{axis}
\end{tikzpicture}
```

### 10. Biểu đồ cột so sánh (grouped)

```latex
\begin{tikzpicture}
\begin{axis}[
    ybar,
    xlabel={Lớp},
    ylabel={Số học sinh},
    symbolic x coords={9A, 9B, 9C, 9D},
    xtick=data,
    ymin=0, ymax=50,
    bar width=12pt,
    legend style={at={(0.5,1.05)}, anchor=south, legend columns=2},
    enlarge x limits=0.2,
]
    \addplot[fill=blue!60] coordinates {(9A, 35) (9B, 38) (9C, 40) (9D, 36)};
    \addlegendentry{Nam}
    
    \addplot[fill=red!60] coordinates {(9A, 25) (9B, 22) (9C, 20) (9D, 24)};
    \addlegendentry{Nữ}
\end{axis}
\end{tikzpicture}
```

### 11. Biểu đồ cột xếp chồng (stacked)

```latex
\begin{tikzpicture}
\begin{axis}[
    ybar stacked,
    xlabel={Quý},
    ylabel={Sản lượng (tấn)},
    symbolic x coords={Q1, Q2, Q3, Q4},
    xtick=data,
    ymin=0,
    legend style={at={(1.02,0.5)}, anchor=west},
    bar width=20pt,
]
    \addplot[fill=blue!60] coordinates {(Q1, 50) (Q2, 60) (Q3, 70) (Q4, 55)};
    \addlegendentry{Sản phẩm A}
    
    \addplot[fill=red!60] coordinates {(Q1, 40) (Q2, 45) (Q3, 50) (Q4, 48)};
    \addlegendentry{Sản phẩm B}
    
    \addplot[fill=green!60] coordinates {(Q1, 30) (Q2, 35) (Q3, 40) (Q4, 38)};
    \addlegendentry{Sản phẩm C}
\end{axis}
\end{tikzpicture}
```

### 12. Biểu đồ đường (line chart)

```latex
\begin{tikzpicture}
\begin{axis}[
    xlabel={Năm},
    ylabel={Sản lượng (nghìn tấn)},
    xmin=2018, xmax=2024,
    ymin=0, ymax=600,
    xtick={2019, 2020, 2021, 2022, 2023},
    legend pos=north west,
    grid=both,
]
    \addplot[blue, thick, mark=*] coordinates {
        (2019, 250) (2020, 320) (2021, 380) (2022, 420) (2023, 500)
    };
    \addlegendentry{Lúa}
    
    \addplot[red, thick, mark=square*] coordinates {
        (2019, 180) (2020, 220) (2021, 280) (2022, 350) (2023, 400)
    };
    \addlegendentry{Ngô}
    
    \addplot[green!60!black, thick, mark=triangle*] coordinates {
        (2019, 100) (2020, 130) (2021, 160) (2022, 200) (2023, 250)
    };
    \addlegendentry{Khoai}
\end{axis}
\end{tikzpicture}
```

### 13. Biểu đồ tròn (Pie chart)

```latex
\usepackage{pgf-pie}

\begin{tikzpicture}
\pie[
    text=legend,
    radius=2.5,
    color={blue!60, red!60, green!60, orange!60, purple!60}
]{
    35/Giỏi,
    40/Khá,
    15/Trung bình,
    7/Yếu,
    3/Kém
}
\end{tikzpicture}
```

### 14. Biểu đồ tròn với nhãn bên trong

```latex
\begin{tikzpicture}
\pie[
    text=inside,
    radius=3,
    color={blue!60, red!60, green!60, orange!60}
]{
    45/45\% Toán,
    25/25\% Lý,
    20/20\% Hóa,
    10/10\% Sinh
}
\end{tikzpicture}
```

### 15. Biểu đồ điểm (Scatter plot)

```latex
\begin{tikzpicture}
\begin{axis}[
    xlabel={Chiều cao (cm)},
    ylabel={Cân nặng (kg)},
    xmin=150, xmax=185,
    ymin=45, ymax=85,
    grid=both,
]
    \addplot[only marks, mark=*, blue, mark size=2pt] coordinates {
        (155, 50) (158, 52) (160, 55) (163, 57) (165, 58)
        (168, 62) (170, 65) (172, 68) (175, 70) (178, 75) (180, 78)
    };
    
    % Đường xu hướng (regression line)
    \addplot[red, thick, domain=150:185, dashed] {0.9*x - 88};
    \addlegendentry{Dữ liệu}
    \addlegendentry{Xu hướng}
\end{axis}
\end{tikzpicture}
```

---

## ĐỒ THỊ BẰNG TIKZ THUẦN

### 16. Hệ tọa độ vẽ tay

```latex
\begin{tikzpicture}[>=Stealth, scale=0.8]
    % Trục tọa độ
    \draw[->] (-4,0) -- (4,0) node[right] {$x$};
    \draw[->] (0,-1) -- (0,5) node[above] {$y$};
    \node[below left] at (0,0) {$O$};
    
    % Chia vạch trục x
    \foreach \x in {-3,-2,-1,1,2,3} {
        \draw (\x,0.1) -- (\x,-0.1) node[below, font=\small] {$\x$};
    }
    
    % Chia vạch trục y
    \foreach \y in {1,2,3,4} {
        \draw (0.1,\y) -- (-0.1,\y) node[left, font=\small] {$\y$};
    }
    
    % Lưới
    \draw[gray!30, very thin] (-3.5,-0.5) grid (3.5,4.5);
    
    % Vẽ parabol y = x^2
    \draw[blue, thick, domain=-2:2, samples=50] plot (\x, {\x*\x});
    \node[blue, right] at (1.8,3.5) {$y = x^2$};
\end{tikzpicture}
```

### 17. Tô màu vùng giữa hai đồ thị

```latex
\begin{tikzpicture}
\begin{axis}[
    axis lines=middle,
    xmin=-1, xmax=3,
    ymin=-1, ymax=5,
]
    % Định nghĩa hai đường
    \addplot[name path=A, blue, thick, domain=0:2] {x^2};
    \addplot[name path=B, red, thick, domain=0:2] {2*x};
    
    % Tô màu vùng giữa
    \addplot[fill=green!30] fill between[of=A and B, soft clip={domain=0:2}];
    
    \addlegendentry{$y = x^2$}
    \addlegendentry{$y = 2x$}
\end{axis}
\end{tikzpicture}
```

### 18. Histogram (biểu đồ tần số)

```latex
\begin{tikzpicture}
\begin{axis}[
    ybar interval,
    xlabel={Điểm số},
    ylabel={Số học sinh},
    xmin=0, xmax=11,
    ymin=0, ymax=15,
    xtick={0,1,2,3,4,5,6,7,8,9,10},
    minor y tick num=1,
]
    \addplot[fill=blue!50, draw=blue!80] coordinates {
        (0, 1) (1, 2) (2, 3) (3, 5) (4, 8) (5, 12) 
        (6, 10) (7, 8) (8, 5) (9, 3) (10, 2) (11, 0)
    };
\end{axis}
\end{tikzpicture}
```

---

## MẸO VÀ TÙY CHỈNH

### Thay đổi màu sắc

```latex
% Màu cơ bản
blue, red, green, orange, purple, cyan, magenta, yellow, black, gray

% Màu pha
blue!60 (60% blue + 40% white)
red!60!black (60% red + 40% black)
green!50!blue (50% green + 50% blue)
```

### Kiểu marker

```latex
mark=*        % Tròn đặc
mark=o        % Tròn rỗng
mark=square*  % Vuông đặc
mark=square   % Vuông rỗng
mark=triangle*% Tam giác đặc
mark=diamond* % Kim cương đặc
mark=x        % Chữ x
mark=+        % Dấu cộng
```

### Legend position

```latex
legend pos=north west
legend pos=north east
legend pos=south west
legend pos=south east
legend pos=outer north east
legend style={at={(0.5,-0.15)}, anchor=north}  % Dưới đồ thị
```
