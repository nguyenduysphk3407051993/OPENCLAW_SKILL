# Đồ thị hàm số, hệ toạ độ cực

> Trích từ `HocTikztheocachcuaBan_BuiQuy.pdf`, trang 41–45.

---

```latex
\begin{tikzpicture}
\foreach \x/\texn in {0/x,
2/-\infty,4/1,6/+\infty} \path
(\x,3.5)node{$\texn$};
\foreach \x/\texn in
{0/f'(x),3/-,4/0,5/+} \path
(\x,2.5)node{$\texn$};
\foreach \x/\y/\texn in {0/1/f(x),
2/1.5/+\infty,4/.5/-1,6/1.5/+\infty}
\path (\x,\y) node(\x){$\texn$};
\draw[-stealth] (2)--(4);
\draw[-stealth](4)--(6);
\draw
(-.5,3)--(6.5,3) (1,4)--(1,0)
(-.5,2)--(6.5,2)
(-.5,4) rectangle (6.5,0)
;
\end{tikzpicture}
```

x
−∞
1
+∞
f′(x)
−
0
+
f(x)
+∞
−1
+∞
Vấn đề là bạn xác định tọa độ các điểm sao cho khéo léo để bảng đẹp hơn mà thôi.

### II.5 Đồ thị hàm số

Để vẽ đồ thị một hàm số trong Tikz. Ta đã có lệnh`\draw[...] plot ();`
Cụ thể lệnh như sau:

```latex
\draw[smooth,samples...] plot[domain=xmin:xmax] (\x ,{f(x)});
```

trong đó xmin và xmax là các hoành độ xuất phát và kết thúc khi vẽ đồ thị
Ta cần chú ý một số tham số sau trong lệnh vẽ đồ thị:
• domain= a:b Tham số này quy định cho ta vùng vẽ đồ thị. Với giá trị cụ thể của a
và b thì Tikz vẽ cho ta phần đồ thị của hàm số với a ≤ x ≤ b. Việc xác định a, b cho
phù hợp hình vẽ là điều rất cần thiết để hình vẽ không quá lớn hoặc tràn ra ngoài
vùng cần vẽ.
• smooth Nếu ta không có tham số này, đồ thị của ta nhìn như các đường gấp khúc
nối lại, vẽ rất xấu và nhìn không ra hệ thống cống rãnh gì. Nhất là với các đồ thị là
đường cong.
•

`variable=\x`

hoặc

`variable=\y`

Định dạng cho ta vẽ đồ thị theo biến x hay
biến y. Với các đồ thị thông thường thì ta thường bỏ qua tham số này hoặc sử dụng

`variable=\x`

là chính.
• Ngoài ra, một số tham số màu (color), độ đậm nét của đường (line width) hoặc độ
hòa trộn (opacity) ... cũng có thể tùy biến để được một đồ thị ưng ý.
Hơn nữa, quý vị cũng cần chú ý đến cách viết công thức hàm số để Tikz có thể hiểu
được. Ví dụ như khi cần vẽ đồ thị hàm số y = 2
3x3 − 3x + 1 thì ta không viết như khi
viết văn bản là

`\dfrac{2}{3}x^{3}-3x+1`

mà phải viết

`(2/3)*(\x)^(3)-3*x+1 .`

Như vậy các dấu phép tính viết bình thường, nhưng phân số khi tính toán ta phải dùng
phép chia (dấu
`/` ), phép nhân phải dùng dấu nhân (dấu
`*` ) và phép lũy thừa thì
vẫn dùng dấu

`^`

nhưng chú ý rằng các đối tượng này nằm trong cặp ngoặc đơn () chứ
không phải cặp

`{ } .`

Ta hãy bắt đầu vẽ một vài đồ thị hàm số quen thuộc. Một đoạn lệnh đơn giản như
dưới đây đã vẽ được đồ thị hàm số y = x4 − 2x2 + 1:

```latex
\begin{tikzpicture}[>=stealth]
\draw[->] (-2,0) --(0,0) node[below
right]{$O$} -- (3,0)
node[below]{$x$};
\draw[->](0,-1)--(0,3)
node[right]{$y$};
\draw[smooth,blue,line width=1]
plot[domain=-1.65:1.65]
(\x,{(\x)^(4)-2*(\x)^(2)+1});
\draw (0,-1.5) node
{$y=x^{4}-2x^{2}+1$};
\end{tikzpicture}
```

O
x
y
y = x4 − 2x2 + 1
Quý vị cũng có thể thử vẽ đồ thị hàm bậc ba y = x3 − 3x2 + 3 với màu đỏ:

```latex
\begin{tikzpicture}[>=stealth]
\draw[->] (-2,0) --(0,0) node[below
right]{$O$} -- (3.5,0)
node[below]{$x$};
\draw[->](0,-1.25)--(0,4)
node[right]{$y$};
\draw[smooth,red,line width=0.75]
plot[domain=-1:3]
(\x,{(\x)^(3)-3*(\x)^(2)+3});
\draw[dashed] (0,-1)
node[left]{$-1$} -- (2,-1) --
(2,0) node[above]{$2$};
\draw (0,3) node[above right]{$3$};
\draw (0.75,-1.5) node
{$y=x^{3}-3x^{2}+3$};
\end{tikzpicture}
```

O
x
y
−1
2
3
y = x3 − 3x2 + 3
Tương tự như vậy bạn hoàn toàn có thể vẽ đồ thị hàm số bất kỳ nào.

### II.6 Đồ thị hàm số trong hệ tọa độ cực

Cấu trúc lệnh vẽ đồ thị hàm số trong hệ tọa độ cực hoàn toàn đơn giản như sau:

```latex
\draw[smooth] plot[domain=0:6.3] (canvas polar cs:angle=\x r,radius= {
r=f(x)});
```

Trong đó ta chú ý đến tham số domain=0: 6.3 chính là góc φ trong hệ tọa độ cực
với đơn vị là rad. Biến

`\x`

chính là góc θ và hàm số r = f(x) chính là công thức tính
r theo góc θ. Chẳng hạn ta muốn vẽ đồ thị hàm số r = cos(3θ) với 0 ≤ θ ≤ π thì ta dùng
lệnh:

```latex
\draw[smooth] plot[domain=0:6.3] (canvas polar cs:angle=\x r,radius=
{cos(3*\x r)});
```

Khi đó ta sẽ được:

```latex
\begin{tikzpicture}[>=stealth,scale=5]
\draw[domain=0:pi/3,samples=200,smooth]
plot (canvas polar cs:angle=\x
r,radius= {10*cos(3*\x r)});
\end{tikzpicture}
```

Ngoài ra, ta cũng có thể vẽ đồ thị hàm số với hệ tọa độ đề các và phương trình tham
số



x = u(t)
y = v(t)
bởi lệnh vẽ đồ thị như sau:

```latex
\draw [smooth,variable=\t] plot[domain=mint:maxt] ({u(t)},{v(t)});
```

Trong đó mint và maxt là giá trị nhỏ nhất, giá trị lớn nhất của tham số t cho vùng
cần vẽ. Biểu thức u(t) và v(t) chính là hai biểu thức hoành độ và tung độ theo t.
Chẳng hạn ta vẽ đồ thị hàm số



x = cos3 t
y = sin3 t
trên vùng 0 ≤ t ≤ 120π như sau:

```latex
\begin{tikzpicture}[>=stealth]
\draw[->](-2,0)--(2,0);
\draw[->](0,-2)--(0,2);
\draw [blue,smooth,variable=\t]
plot[domain=0:120*pi ]
({(cos(\t))^3},{(sin(\t))^3});
\end{tikzpicture}
```

### III

### Tô miền đồ thị hàm số với Tikz

Qua quá trình trao đổi cùng các bạn vẽ hình trong và ngoài nhóm TikZ - Asymp-
tote tôi thấy khá nhiều vướng mắc khi các bạn vẽ phần tô miền của đồ thị hàm số
trong các bài toán tính diện tích hình phẳng và thể tích khối tròn xoay. Chính vì vậy
tôi viết tạm bài viết ngắn này mong các bạn dễ dàng tháo gỡ khó khăn khi vẽ hình.

### III.1 Vẽ đồ thị hàm số

Thông thường khi vẽ đồ thị hàm số, các bạn vẫn dùng lệnh:

```latex
\draw [samples=100,smooth] plot[domain=0:120*pi] (\x,{\f(\x)});
```

Trong lệnh trên đây thì smooth quyết định độ trơn (nhẵn) của đồ thị hàm số, còn
samples quyết định số điểm chia để vẽ. Do đó việc sử dụng tham số nào cũng nên lưu
ý. Thông thường những hàm đa thức thường gặp ta chỉ cần dùng smooth là đủ, một
số hàm đặc biệt có độ gấp khúc cao thì ta cần sử dụng samples và tăng giá trị này để
tạo độ cong hợp lý khi zoom hình. Ví dụ sau đây cho các bạn thấy sự khác biệt ở hai
hình để giúp bạn lựa chọn cho phù hợp, bởi giá trị samples càng cao thì tốc độ biên
dịch sẽ tăng thêm đáng kể:

```latex
\begin{tikzpicture}[>=stealth]
\def\f(#1){sqrt(#1+1)}
\draw[->] (-3,0)--(0,0)node[below
right]{$O$}--(4,0)
node[above]{$x$};
\draw[->]
(0,-4)--(0,4)node[left]{$y$};
\draw[smooth,blue, line width=1]
plot[domain=-1:4](\x,{\f(\x)})
plot[domain=-1:4](\x,{-\f(\x)});
\draw (3,-1)
node[above]{$f(x)=-\sqrt{x+1}$};
\draw[dashed] (3,0)--(3,2)--(0,2);
\draw (3,3) node{\bf smooth};
\end{tikzpicture}
```

O
x
y
f(x) = −
√
x + 1

### smooth
