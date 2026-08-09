# Khai báo, môi trường vẽ và hệ trục toạ độ

> Trích từ `HocTikztheocachcuaBan_BuiQuy.pdf`, trang 4–6.

---

### I

### Cơ bản về vẽ hình bằng Tikz

### I.1 Khai báo và môi trường vẽ

Khai báo gói lệnh:

```latex
\usepackage{tikz}
\usetikzlibrary{calc,angles}
```

Môi trường vẽ:

```latex
\begin{tikzpicture}
.......
\draw ....
......
\end{tikzpicture}
```

Như vậy. Một file vẽ hình bằng Tikz có thể đầy đủ để bạn biên dịch:

```latex
\documentclass{standalone}
\usepackage{tikz}
\usetikzlibrary{calc,angles}
\begin{document}
\begin{tikzpicture}
...........
\draw ....
...........
\end{tikzpicture}
\end{document}
```

### I.2 Các đối tượng hình học

### I.2.1 Hệ trục tọa độ

Các đối tượng hình học luôn gắn với hệ tọa độ. Chúng ta có thể sử dụng một trong
hai hệ tọa độ để xác định các đối tượng cần vẽ: Hệ tọa độ vuông góc Oxy hoặc tọa độ
cực.

```latex
\begin{tikzpicture}[>=stealth]
\draw[->](-3,0)--(3,0);
\draw[->](0,-3)--(0,3);
\draw[dashed] (0,1)--(2,1)--(2,0);
\draw (2,1) circle (0.04);
\draw (3,0) node[above]{$x$} (0,3)
node[left]{$y$} (0,0) node[below
left]{$O$};
\end{tikzpicture}
```

x
y
O

```latex
\begin{tikzpicture}[>=stealth]
\def\r{sqrt(5)}
\draw[->](-3,0)--(3,0);
\draw[->](0,-3)--(0,3);
\draw[dashed] (0,1)--(2,1)--(2,0);
\draw (0,0) circle (\r);
\draw (0,0)--(2,1);
\draw (2,1) circle (0.04);
\draw (3,0) node[above]{$x$} (0,3)
node[left]{$y$} (0,0) node[below
left]{$O$};
\end{tikzpicture}
```

x
y
O
Để dễ dàng cho bạn khi bắt đầu tập vẽ, ta nên tạo lưới tọa độ vùng vẽ để khi xem
kết quả ta dễ dàng hình dung ra cách thức và rút kinh nghiệm cho việc sử dụng lệnh
bằng cú pháp:

```latex
\draw[step=1,gray,thin] (lower left corner) grid (upper right corner);
```

trong đó lower left corner là tọa độ điểm góc trái phía dưới và upper right corner
là tọa độ điểm góc phải bên trên của vùng vẽ lưới
Chẳng hạn tạo một lưới tọa độ với vùng vẽ từ (−2; −1) đến (3; 2) ta dùng lệnh như
sau:

```latex
\begin{tikzpicture}
\draw[step=1,gray,very thin]
(-2,-1) grid (3,2);
\end{tikzpicture}
```

### I.2.2 Các lệnh cơ bản của Tikz

Với Tikz có các lệnh vẽ cơ bản sau:
1. Lệnh vẽ đường:

`\draw[tùy chọn] Nội dung vẽ;`

2. Lệnh đưa đầu bút vẽ đến vị trí nào đó:

```latex
\path (Tọa độ điểm) Nội dung làm việc ;
```

3. Lệnh tô màu:

`\fill[tùy chọn] miền tô màu;`

Tất nhiên trong Tikz còn một số lệnh khác, nhưng khi vẽ các hình thông thường ta
chỉ cần sử dụng ba lệnh trên là đủ.

### I.2.3 Khai báo điểm, tham số

Khi vẽ hình ta có những điểm cần sử dụng nhiều lần, các thông số cần sử dụng nhiều
làm và các số liệu tính toán. Yêu cầu này buộc ta cần khai báo tên các điểm và giá trị
của các tham số (hiểu đơn giản là một cách viết tắt cho những đoạn lệnh dài hơn).
• Khai báo điểm có tọa độ cho trước:

```latex
\coordinate[tùy chọn] (Tên điểm) at (Tọa độ);
\coordinate[label=above:A] (A) at (1,2); sẽ khai báo cho ta điểm A(1; 2)
```

và khi vẽ điểm A Tikz sẽ tự động thêm nhãn của điểm là A ở phía trên của điểm.
`\coordinate (A) at (30:2);` sẽ khai báo cho ta điểm A(30 : 2) và không thêm
nhãn của điểm.
• Gán giá trị cho tham số:
`\def\a{3}` : Gán cho tham sốa giá trị3 (hiểu là cho a = 3). Khi dùng đến giá
trị này trong Tizk chỉ cần gọi
`\a` .
`\pgfmathsetmacro\a{2*sqrt(2)}` : Gán cho tham sốa giá trị2
√
2. Chú ý khi
gán giá trị cho tham số, dùng

`\def`

khi gán một giá trị là một số cụ thể (không
tính toán thông qua các phép tính) còn nếu buộc phải tính toán qua các phép tính
thì dùng

`\pgfmathsetmacro .`

### I.2.4 Các hàm tính toán số liệu cơ bản

Một số hàm tính toán trong Tikz
• sin (α): Trả về giá trị sin α.
• cos (α): Trả về giá trị cos α.
• tan (α): Trả về giá trị tan α.
