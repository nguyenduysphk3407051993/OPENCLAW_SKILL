# Mẫu TikZ - Sơ đồ Vật lý

## Preamble chuẩn cho Vật lý

```latex
\documentclass[tikz,border=5pt]{standalone}
\usepackage{circuitikz}  % Cho mạch điện
\usetikzlibrary{
    calc, 
    arrows.meta, 
    patterns, 
    decorations.pathmorphing,  % Sóng, lò xo
    decorations.markings
}
\usepackage[utf8]{vietnam}
\usetikzlibrary{calc,angles,intersections,positioning,shapes.geometric,arrows,decorations.markings,arrows.meta,patterns.meta,patterns,quotes}
\usetikzlibrary{hobby}
\usepackage{tikz-3dplot,pgfplots}
\pgfplotsset{compat=1.15}
\usepgfplotslibrary{polar}
\usepackage{tkz-tab}
\usepackage{amsmath}
\begin{document}
\begin{tikzpicture}[>=Stealth]
% Code ở đây
\end{tikzpicture}
\end{document}
```

---

## CƠ HỌC - VECTOR LỰC

### 1. Vật trên mặt phẳng ngang - Các lực tác dụng

```latex
\begin{tikzpicture}[>=Stealth]
    % Mặt phẳng
    \draw[thick] (-1,0) -- (5,0);
    \fill[pattern=north east lines] (-1,-0.3) rectangle (5,0);
    
    % Vật (hình chữ nhật)
    \draw[fill=gray!30, thick] (1.5,0) rectangle (3.5,1.5);
    \node at (2.5,0.75) {$m$};
    
    % Tâm vật
    \coordinate (G) at (2.5,0.75);
    
    % Trọng lực P
    \draw[->, thick, blue, line width=1.2pt] (G) -- ++(0,-1.8) 
        node[right] {$\vec{P}$};
    
    % Phản lực N
    \draw[->, thick, red, line width=1.2pt] (2.5,0) -- ++(0,1.8) 
        node[right] {$\vec{N}$};
    
    % Lực kéo F
    \draw[->, thick, green!60!black, line width=1.2pt] (3.5,0.75) -- ++(2,0) 
        node[above] {$\vec{F}$};
    
    % Lực ma sát f
    \draw[->, thick, orange, line width=1.2pt] (1.5,0.2) -- ++(-1.2,0) 
        node[above] {$\vec{f}$};
\end{tikzpicture}
```

### 2. Vật trên mặt phẳng nghiêng

```latex
\begin{tikzpicture}[>=Stealth]
    % Góc nghiêng
    \def\angle{30}
    
    % Mặt phẳng nghiêng
    \draw[thick] (0,0) -- (6,0) -- (6,{6*tan(\angle)}) -- cycle;
    \fill[pattern=north east lines] (0,0) -- (6,0) -- (6,{6*tan(\angle)}) -- cycle;
    
    % Vật (hình vuông xoay theo mặt nghiêng)
    \begin{scope}[rotate=\angle]
        \draw[fill=blue!20, thick] (3,0.1) rectangle (4.2,1.3);
        \coordinate (G) at (3.6,0.7);
    \end{scope}
    
    % Trọng lực P (thẳng đứng xuống)
    \draw[->, thick, red, line width=1.2pt] (G) -- ++(0,-2) 
        node[right] {$\vec{P}$};
    
    % Phân tích P thành Px và Py
    % Py vuông góc mặt nghiêng
    \draw[->, thick, blue] (G) -- ++({-2*sin(\angle)},{-2*cos(\angle)}) 
        node[left] {$\vec{P_y}$};
    % Px song song mặt nghiêng
    \draw[->, thick, green!60!black] (G) -- ++({-1.5*cos(\angle)},{1.5*sin(\angle)}) 
        node[above] {$\vec{P_x}$};
    
    % Góc alpha
    \draw (1,0) arc (0:\angle:1);
    \node at (1.3,0.3) {$\alpha$};
    
    % Chiều cao h
    \draw[<->, thick] (6.3,0) -- (6.3,{6*tan(\angle)}) node[midway, right] {$h$};
\end{tikzpicture}
```

### 3. Chuyển động ném xiên

```latex
\begin{tikzpicture}[>=Stealth]
    % Trục tọa độ
    \draw[->] (-0.5,0) -- (7,0) node[right] {$x$};
    \draw[->] (0,-0.5) -- (0,4) node[above] {$y$};
    \node[below left] at (0,0) {$O$};
    
    % Quỹ đạo parabol
    \draw[blue, thick, domain=0:6, samples=50] 
        plot (\x, {-0.18*(\x-3)^2 + 3});
    
    % Vận tốc ban đầu
    \draw[->, red, thick, line width=1.2pt] (0,0) -- (1.5,1.8) 
        node[above right] {$\vec{v_0}$};
    
    % Góc ném
    \draw (0.8,0) arc (0:50:0.8);
    \node at (1.1,0.4) {$\alpha$};
    
    % Điểm cao nhất
    \fill[blue] (3,3) circle (3pt);
    \node[above] at (3,3) {$H_{max}$};
    \draw[dashed] (3,3) -- (3,0);
    
    % Tầm xa
    \draw[<->, thick] (0,-0.6) -- (6,-0.6) node[midway, below] {$L$};
    
    % Chiều cao cực đại
    \draw[<->, thick] (-0.4,0) -- (-0.4,3) node[midway, left] {$H$};
\end{tikzpicture>
```

### 4. Chuyển động tròn đều

```latex
\begin{tikzpicture}[>=Stealth]
    % Quỹ đạo tròn
    \draw[thick, blue] (0,0) circle (2.5);
    
    % Tâm O
    \fill (0,0) circle (2pt);
    \node[below left] at (0,0) {$O$};
    
    % Vật tại vị trí M
    \coordinate (M) at (60:2.5);
    \fill[red] (M) circle (4pt);
    \node[above right] at (M) {$M$};
    
    % Bán kính OM
    \draw[thick] (0,0) -- (M);
    \node[midway, below right] at (0,0) -- (M) {$R$};
    
    % Vận tốc v (tiếp tuyến)
    \draw[->, thick, green!60!black, line width=1.2pt] (M) -- ++(150:1.8) 
        node[above] {$\vec{v}$};
    
    % Gia tốc hướng tâm
    \draw[->, thick, red, line width=1.2pt] (M) -- ++(-120:1.5) 
        node[below left] {$\vec{a_{ht}}$};
    
    % Mũi tên chỉ chiều quay
    \draw[->, thick] (30:3) arc (30:80:3);
    \node at (55:3.3) {$\omega$};
\end{tikzpicture}
```

### 5. Con lắc đơn

```latex
\begin{tikzpicture}
    % Điểm treo
    \fill (0,4) circle (2pt);
    \draw[thick] (-1,4) -- (1,4);
    \fill[pattern=north east lines] (-1,4) rectangle (1,4.2);
    
    % Vị trí cân bằng (nét đứt)
    \draw[dashed, gray] (0,4) -- (0,0.5);
    
    % Dây treo ở vị trí lệch
    \draw[thick] (0,4) -- (2,1);
    
    % Vật nặng
    \shade[ball color=blue!60] (2,1) circle (0.4);
    
    % Góc lệch
    \draw (0,3) arc (270:300:1);
    \node at (0.4,2.7) {$\theta$};
    
    % Chiều dài dây
    \node[left] at (-0.2,2) {$\ell$};
    
    % Trọng lực
    \draw[->, thick, red] (2,1) -- (2,-0.5) node[right] {$\vec{P}$};
    
    % Lực căng dây
    \draw[->, thick, blue] (2,1) -- (0.8,3.4) node[above left] {$\vec{T}$};
\end{tikzpicture}
```

### 6. Lò xo và lực đàn hồi

```latex
\begin{tikzpicture}[
    spring/.style={decorate, decoration={coil, segment length=4pt, amplitude=4pt}}
]
    % Tường
    \fill[pattern=north east lines] (-0.3,-1) rectangle (0,2);
    \draw[thick] (0,-1) -- (0,2);
    
    % Lò xo tự nhiên
    \draw[spring, thick] (0,1.5) -- (3,1.5);
    \node[above] at (1.5,1.7) {$\ell_0$};
    
    % Lò xo bị nén
    \draw[spring, thick, blue] (0,0) -- (2,0);
    \draw[fill=blue!30, thick] (2,-0.3) rectangle (2.8,0.3);
    \draw[->, thick, red] (2.8,0) -- (4,0) node[above] {$\vec{F}$};
    \node[above] at (1,0.2) {Nén};
    
    % Lò xo bị dãn
    \draw[spring, thick, green!60!black] (0,-1.5) -- (4,-1.5);
    \draw[fill=green!30, thick] (4,-1.8) rectangle (4.8,-1.2);
    \draw[->, thick, red] (4.8,-1.5) -- (3.5,-1.5) node[above] {$\vec{F}$};
    \node[above] at (2,-1.3) {Dãn};
\end{tikzpicture}
```

---

## QUANG HỌC

### 7. Phản xạ ánh sáng trên gương phẳng

```latex
\begin{tikzpicture}[>=Stealth]
    % Gương
    \draw[thick] (0,0) -- (5,0);
    \fill[pattern=north east lines] (0,-0.3) rectangle (5,0);
    
    % Điểm tới I
    \coordinate (I) at (2.5,0);
    
    % Pháp tuyến
    \draw[dashed, thick] (I) -- ++(0,3) node[above] {$N$};
    
    % Tia tới SI
    \draw[->, red, thick, line width=1.2pt] (0.5,2.5) -- (I);
    \node[above left, red] at (0.8,2.2) {Tia tới};
    
    % Tia phản xạ IR
    \draw[->, blue, thick, line width=1.2pt] (I) -- (4.5,2.5);
    \node[above right, blue] at (4.2,2.2) {Tia phản xạ};
    
    % Góc tới i
    \draw (2.5,0.8) arc (90:120:0.8);
    \node at (2.1,1.1) {$i$};
    
    % Góc phản xạ r
    \draw (2.5,0.8) arc (90:60:0.8);
    \node at (2.9,1.1) {$r$};
    
    % Điểm I
    \fill (I) circle (2pt);
    \node[below] at (I) {$I$};
\end{tikzpicture}
```

### 8. Khúc xạ ánh sáng

```latex
\begin{tikzpicture}[>=Stealth]
    % Mặt phân cách
    \draw[thick] (-3,0) -- (3,0);
    
    % Môi trường 1 (trên)
    \fill[blue!10] (-3,0) rectangle (3,3);
    \node at (-2,2.5) {$n_1$};
    
    % Môi trường 2 (dưới)
    \fill[blue!30] (-3,0) rectangle (3,-3);
    \node at (-2,-2.5) {$n_2 > n_1$};
    
    % Pháp tuyến
    \draw[dashed] (0,3) -- (0,-3);
    
    % Tia tới
    \draw[->, red, thick, line width=1.2pt] (-2,2.5) -- (0,0);
    
    % Tia khúc xạ (lệch về phía pháp tuyến vì n2 > n1)
    \draw[->, blue, thick, line width=1.2pt] (0,0) -- (1,-2.5);
    
    % Góc tới
    \draw (0,0.8) arc (90:130:0.8);
    \node at (-0.5,1) {$i$};
    
    % Góc khúc xạ
    \draw (0,-0.6) arc (-90:-70:0.6);
    \node at (0.3,-0.8) {$r$};
    
    % Điểm tới
    \fill (0,0) circle (2pt);
\end{tikzpicture}
```

### 9. Thấu kính hội tụ - Tạo ảnh

```latex
\begin{tikzpicture}[>=Stealth]
    % Trục chính
    \draw[->] (-5,0) -- (5,0);
    
    % Thấu kính hội tụ
    \draw[thick, blue, fill=blue!10] 
        (0,-2) -- (0.15,-1.8) -- (0.15,1.8) -- (0,2) 
        -- (-0.15,1.8) -- (-0.15,-1.8) -- cycle;
    
    % Tiêu điểm
    \fill (-2,0) circle (2pt) node[below] {$F$};
    \fill (2,0) circle (2pt) node[below] {$F'$};
    
    % Quang tâm
    \fill (0,0) circle (2pt) node[below right] {$O$};
    
    % Vật AB (mũi tên đứng)
    \draw[->, thick, red, line width=1.5pt] (-3.5,0) -- (-3.5,1.5);
    \node[above, red] at (-3.5,1.5) {$B$};
    \node[below, red] at (-3.5,0) {$A$};
    
    % Tia qua quang tâm
    \draw[green!60!black] (-3.5,1.5) -- (0,0) -- (2.5,-1.07);
    
    % Tia song song trục chính -> qua tiêu điểm
    \draw[green!60!black] (-3.5,1.5) -- (0,1.5) -- (2.5,-1.07);
    
    % Ảnh A'B'
    \draw[->, thick, blue, line width=1.5pt] (2.5,0) -- (2.5,-1.07);
    \node[below, blue] at (2.5,-1.07) {$B'$};
    \node[above, blue] at (2.5,0) {$A'$};
\end{tikzpicture}
```

### 10. Lăng kính - Tán sắc ánh sáng

```latex
\begin{tikzpicture}[>=Stealth]
    % Lăng kính
    \draw[thick, fill=blue!10] (0,0) -- (3,0) -- (1.5,2.6) -- cycle;
    
    % Tia sáng trắng vào
    \draw[->, thick, line width=1.5pt] (-2,0.8) -- (0.5,0.8);
    \node[above] at (-1,0.8) {Ánh sáng trắng};
    
    % Tia phân tách (tán sắc)
    \draw[->, red, thick] (2.2,1.3) -- (4.5,2);
    \draw[->, orange, thick] (2.2,1.3) -- (4.5,1.7);
    \draw[->, yellow, thick] (2.2,1.3) -- (4.5,1.4);
    \draw[->, green, thick] (2.2,1.3) -- (4.5,1.1);
    \draw[->, blue, thick] (2.2,1.3) -- (4.5,0.8);
    \draw[->, violet, thick] (2.2,1.3) -- (4.5,0.5);
    
    % Nhãn màu
    \node[right, red] at (4.5,2) {Đỏ};
    \node[right, violet] at (4.5,0.5) {Tím};
\end{tikzpicture}
```

---

## MẠCH ĐIỆN (CircuiTikZ)

### 11. Mạch điện nối tiếp

```latex
\usepackage{circuitikz}

\begin{circuitikz}[european]
\draw
    (0,0) to[battery1, l=$E$, invert] (0,3)
    to[short] (3,3)
    to[R, l=$R_1$] (3,1.5)
    to[R, l=$R_2$] (3,0)
    to[short] (0,0);
    
% Ampe kế
\draw (3,3) to[short] (5,3)
    to[ammeter, l=$A$] (5,0)
    to[short] (3,0);
\end{circuitikz}
```

### 12. Mạch điện song song

```latex
\begin{circuitikz}[european]
\draw
    % Nguồn
    (0,0) to[battery1, l=$E$, invert] (0,3)
    to[short] (1.5,3)
    
    % Nhánh 1
    (1.5,3) to[short] (1.5,3.5)
    to[R, l=$R_1$] (4.5,3.5)
    to[short] (4.5,3)
    
    % Nhánh 2
    (1.5,3) to[short] (1.5,2.5)
    to[R, l=$R_2$] (4.5,2.5)
    to[short] (4.5,3)
    
    % Phần còn lại
    (4.5,3) to[ammeter, l=$A$] (4.5,0)
    to[short] (0,0);
\end{circuitikz}
```

### 13. Mạch điện hỗn hợp

```latex
\begin{circuitikz}[european]
\draw
    (0,0) to[battery1, l=$E{,}r$] (0,4)
    to[short] (2,4)
    to[R, l=$R_1$] (2,2)
    to[short] (2,2) -- (1,2)
    to[R, l=$R_2$] (1,0)
    to[short] (0,0)
    
    (2,2) -- (3,2)
    to[R, l=$R_3$] (3,0)
    to[short] (1,0);
    
% Vôn kế
\draw (4,4) to[voltmeter, l=$V$] (4,0);
\draw (2,4) -- (4,4);
\draw (3,0) -- (4,0);
\end{circuitikz}
```

---

## SÓNG VÀ DAO ĐỘNG

### 14. Sóng hình sin

```latex
\begin{tikzpicture}[>=Stealth]
    % Trục
    \draw[->] (-0.5,0) -- (10,0) node[right] {$x$};
    \draw[->] (0,-2) -- (0,2.5) node[above] {$y$};
    
    % Sóng sin
    \draw[blue, thick, domain=0:9.5, samples=200] 
        plot (\x, {1.5*sin(deg(1.2*\x))});
    
    % Biên độ A
    \draw[<->, red, thick] (0.5,0) -- (0.5,1.5);
    \node[right, red] at (0.5,0.75) {$A$};
    
    % Bước sóng lambda
    \draw[<->, green!60!black, thick] (0,-1.8) -- ({2*pi/1.2},-1.8);
    \node[below, green!60!black] at ({pi/1.2},-1.8) {$\lambda$};
    
    % Đường biên độ
    \draw[dashed, gray] (-0.3,1.5) -- (10,1.5);
    \draw[dashed, gray] (-0.3,-1.5) -- (10,-1.5);
\end{tikzpicture}
```

### 15. Giao thoa sóng

```latex
\begin{tikzpicture}
    % Hai nguồn S1 và S2
    \fill[red] (-2,0) circle (4pt) node[below] {$S_1$};
    \fill[red] (2,0) circle (4pt) node[below] {$S_2$};
    
    % Sóng từ S1
    \foreach \r in {0.5, 1, 1.5, 2, 2.5, 3, 3.5} {
        \draw[blue, thin] (-2,0) circle (\r);
    }
    
    % Sóng từ S2
    \foreach \r in {0.5, 1, 1.5, 2, 2.5, 3, 3.5} {
        \draw[green!60!black, thin] (2,0) circle (\r);
    }
    
    % Điểm cực đại (giao thoa tăng cường)
    \fill[red] (0,1.7) circle (3pt);
    \fill[red] (0,-1.7) circle (3pt);
    \fill[red] (0,0) circle (3pt);
\end{tikzpicture}
```

---

## ĐIỆN TỪ

### 16. Từ trường của dây dẫn thẳng

```latex
\begin{tikzpicture}
    % Dây dẫn (vuông góc với mặt phẳng - dòng điện đi vào)
    \draw[thick, fill=gray!50] (0,0) circle (0.2);
    % Dấu X (dòng đi vào)
    \draw[thick] (-0.12,-0.12) -- (0.12,0.12);
    \draw[thick] (-0.12,0.12) -- (0.12,-0.12);
    \node[above] at (0,0.4) {$I$ (vào)};
    
    % Đường sức từ (vòng tròn đồng tâm)
    \foreach \r in {0.8, 1.3, 1.8} {
        \draw[blue, ->, >=Stealth] (\r,0) arc (0:330:\r);
    }
    
    % Vector B tại một điểm
    \draw[->, red, thick, line width=1.2pt] (1.3,0) -- (1.3,0.8) 
        node[right] {$\vec{B}$};
\end{tikzpicture}
```

### 17. Lực từ tác dụng lên dây dẫn

```latex
\begin{tikzpicture}[>=Stealth]
    % Từ trường B (mũi tên song song)
    \foreach \y in {0.5, 1, 1.5, 2, 2.5} {
        \draw[->, blue, thick] (-1,\y) -- (0.5,\y);
    }
    \node[blue] at (-0.25,3) {$\vec{B}$};
    
    % Dây dẫn
    \draw[very thick] (2,0) -- (2,3);
    \draw[->, thick] (2,1.5) -- (2,2.5) node[right] {$I$};
    
    % Lực từ F
    \draw[->, red, very thick, line width=1.5pt] (2,1.5) -- (4,1.5) 
        node[above] {$\vec{F}$};
    
    % Quy tắc bàn tay trái
    \node at (3,-0.5) {Quy tắc bàn tay trái};
\end{tikzpicture}
```

### 18. Cảm ứng điện từ - Định luật Lenz

```latex
\begin{tikzpicture}[>=Stealth]
    % Cuộn dây (biểu diễn đơn giản)
    \draw[thick] (0,0) ellipse (1.5 and 0.5);
    \draw[thick] (-1.5,0) -- (-1.5,-2);
    \draw[thick] (1.5,0) -- (1.5,-2);
    \draw[thick] (0,-2) ellipse (1.5 and 0.5);
    
    % Nam châm di chuyển vào
    \draw[fill=red!60] (-0.5,2) rectangle (0.5,3);
    \node at (0,2.5) {N};
    \draw[fill=blue!60] (-0.5,3) rectangle (0.5,4);
    \node at (0,3.5) {S};
    
    % Mũi tên di chuyển
    \draw[->, thick, green!60!black, line width=1.5pt] (0,4.2) -- (0,3.2);
    \node[right] at (0.6,3.7) {$v$};
    
    % Từ thông tăng
    \draw[->, blue, thick] (0,1.5) -- (0,0.5) node[right] {$\Phi \uparrow$};
    
    % Dòng điện cảm ứng
    \draw[->, red, thick] (1.8,-1) arc (0:-180:0.3);
    \node[right, red] at (2,-1) {$I_{cu}$};
\end{tikzpicture}
```
