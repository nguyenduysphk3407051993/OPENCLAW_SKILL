# Lấy điểm trên đường cong, tiếp tuyến, giao điểm

> Trích từ `HocTikztheocachcuaBan_BuiQuy.pdf`, trang 15–20.

---

```latex
\begin{tikzpicture}
\draw[gray!50,thin,opacity=.5]
(-1,-1) grid (5,5);
\path (0,0) coordinate (A) (3,3)
coordinate (B) (4,1)
coordinate (C);
\draw [blue](A) parabola bend (B)
(C);
\foreach \x/\g in
{A/-150,B/60,C/-90}\fill[black]
(\x) circle (1pt)
($(\x)+(\g:3mm)$)node{$\x$};
\end{tikzpicture}
```

A
B
C
• plot coordinates: Vẽ đường cong qua nhiều điểm (một đường gấp khúc qua các
điểm một cách mềm mại). Ta có thể sử dụng cú pháp:

```latex
\draw[smooth] plot coordinate{ Tọa độ các điểm};
```

Ví dụ như đường cong sau đây:

```latex
\begin{tikzpicture}
\draw[gray!50,thin,opacity=.5]
(-1,-1) grid (5,5);
\draw[blue,smooth] plot
coordinates{(0,0) (1,0) (2,1)
(2,2) (3,1) (4,3)};
\end{tikzpicture}
```

• controls: Vẽ đường cong qua điểm A và B với các “lực đẩy”. Ta có cú pháp:

```latex
\draw (A).. controls (C) and (D) .. (B);
```

Trong cú pháp trên, A là điểm bắt đầu, B là điểm kết thúc của đường cong. Điểm
C và D chỉ tham gia với tư cách là “lực đẩy” để kéo cho đường nối từ A đến B có
độ cong mà không hiển thị trên hình vẽ.

### I.2.11 Lấy một điểm trên đường cong, tiếp tuyến của đường cong

Với một đường cong bất kỳ, ta có thể khai báo để lấy một điểm trên đường cong
theo tỉ lệ với cú pháp:

```latex
\draw Dạng đường cong coordinate[pos=tỉ lệ](A);
```

Chẳng hạn lấy một điểm A trên một đường controls như sau:

```latex
\draw (0,0)..controls +(0:1) and +(60:2)..(1,2) coordinate[pos=.5](A);
```

Khi đó ta lấy được điểm A là điểm chính giữa của đường cong này.
Ví dụ:

```latex
\begin{tikzpicture}
\draw[gray!50,thin,opacity=.5]
(-1,-1) grid (5,5);
\draw[red] (0,0)..controls +(0:1)
and +(60:2)..(1,2)
coordinate[pos=.5](B);
\draw (0,0) to[out=90,in=180]
coordinate[pos=.5](C) (3,4) ;
\foreach \x in {A,B,C}\fill[black]
(\x) circle (1pt)
($(\x)+(90:3mm)$)node{$\x$};
\end{tikzpicture}
```

A
B
C
Tất nhiên lấy một điểm trên các đường có sẵn phương trình (hoặc định dạng quen
thuộc như đường tròn hoặc ellipse) thì ta dùng cách khác sẽ tiện lợi hơn rất nhiều bằng
việc dùng

`\path ... coordinate ...`

hoặc

`\draw ... coordinate ...`

Chẳng hạn lấy điểm A trên đường tròn và điểm B trên ellipse như sau:

```latex
\begin{tikzpicture}
\draw[gray!50,thin,opacity=.5]
(-1,-1) grid (6,5);
\path
(0,0) arc (180:60:2) coordinate (A)
(0,0) arc (180:150:{3} and {1})
coordinate (B)
(0,0) arc (180:30:{3} and {1})
coordinate (C)
;
\draw
(0,0) arc (180:0:2)
(0,0) arc (180:0:{3} and {1})
;
\foreach \x in {A,B,C}\fill[black]
(\x) circle (1pt)
($(\x)+(90:3mm)$)node{$\x$};
\end{tikzpicture}
```

A
B
C
Việc vẽ các đường tiếp tuyến của đường tròn và Ellipse ta có thể căn cứ vào mối
quan hệ hình học (và phương pháp tọa độ trong mặt phẳng) để hoạch định cách vẽ cho
hợp lý. Tất nhiên Tikz cũng cung cấp thư viện decoration.markings để vẽ các đường
cát tuyến và tiếp tuyến của đường cong tại một điểm bất kỳ. Nhưng việc sử dụng thư
viện này chỉ nên dùng khi quá cần thiết (với dạng đường cong không quen thuộc mà
hầu hết ta rất hiếm khi dùng trong các hình vẽ các bài toán, và việc sử dụng thư viện
này khá phức tạp và khó nhớ) nên tôi không đề cập ở đây.
Trở lại với đường tròn và Ellipse, để vẽ tiếp tuyến của đường tròn tâm O bán kính
r tại điểm M nào đó, ta luôn thấy tiếp tuyến vuông góc với bán kính OM. Như vậy chỉ
cần quay tâm O quanh M một góc 90◦ hoặc −90◦ được điểm T thì ngay lập tức ta có
MT là tiếp tuyến của đường tròn rồi.
Tương tự như vậy, với một Ellipse có bán trục lớn a, bán trục nhỏ b ta có ngay phương
trình Ellipse dạng x2
a2 + y2
b2 = 1 và khi đó tiếp tuyến tại M(x◦, y◦) có dạng x.x◦
a2 + y.y◦
b2
= 1.
Vậy nếu có hoành độ (hoặc tung độ tiếp điểm) thì ta có được phương trình tiếp tuyến
của Ellipse, và như vậy việc vẽ tiếp tuyến chẳng qua chỉ là vẽ đồ thị một hàm số mà
thôi.
Ví dụ như hình vẽ một hình nón có đáy biểu diễn bởi một Ellipse có bán trục x là
a = 3, bán trục nhỏ là b = 1 và chiều cao h4. Muốn vẽ chính xác được không đơn giản
bởi nếu bình thường bạn sẽ vẽ

```latex
\begin{tikzpicture}[line
join=round, line cap=round]
\def\a{3}
\def\b{1}
\def\h{4}
\draw[dashed] (180:\a) arc
(180:0:{\a} and {\b});
\draw
(90:\h)--(180:\a)arc(180:360:{\a}
and {\b})--cycle;
\end{tikzpicture}
```

Nhìn hình vẽ trên ta thấy không được đẹp vì hai đường sinh hai bên cắt đường nét
đứt. Hình sẽ không “thật” lắm. Muốn hình được “thật” hơn, bạn phải tính toán sao cho
các đường sinh tiếp xúc với Ellipse. Ta sẽ đặt ra bài toán vẽ tiếp tuyến của Ellipse đi
qua đỉnh của hình nón.
Bạn vẽ phác hình ra để phân tích và tìm cách vẽ:
B
A
S
O
M
Trong hình vẽ trên, ta thấy điểm A(a; 0), B(−a; 0), S(0; h), O(0; 0) và điểm M(x◦; y◦).
Vấn đề là xác định được tọa độ điểm M. Chú ý rằng trong hình học tọa độ phẳng nếu
điểm, phương trình Ellipse là x2
a2 + y2
b2 = 1 và phương trình tiếp tuyến của Ellipse tại
M(x◦; y◦) là x.x◦
a2
+ y.y◦
b2
= 1. Vì tiếp tuyến đi qua điểm S(0; h) nên ta thay tọa độ điểm
S vào phương trình tiếp tuyến sẽ suy ra được y◦ = b2
h . Từ đó ta có thể tính được x◦.
Mặt khác, trong hệ tọa độ cực, tọa độ điểm M(ϕ : r) với ϕ = \
AOM thì hoành độ và
tung độ điểm M được tính theo công thức:



x◦ = a cos ϕ
y◦ = b sin ϕ
. Từ đây ta có thể tính góc
ϕ = arcsin y◦
b = arcsin b
h để lấy góc vẽ các cung Ellipse cần thiết. Như vậy ta có thể hoàn
thiện code vẽ một cách linh hoạt và đơn giản:

```latex
\begin{tikzpicture}[line
join=round,line
cap=round,font=\scriptsize]
\def\a{3}
\def\b{1}
\def\h{4}
\pgfmathsetmacro\g{asin(\b/\h)}
\pgfmathsetmacro\xo{\a *cos(\g)}
\pgfmathsetmacro\yo{\b *sin(\g)}
\draw[dashed]
(\xo,\yo) arc (\g:180-\g:{\a} and
{\b})
(180:\a)node[left]{$B$} --(0:\a)
node[right]{$A$} (90:\h)
node[above]{$S$} --(0:0)
node[below left]{$O$}
--(\xo,\yo)node[above right]{$M$}
;
\draw (90:\h)--(-\xo,\yo) arc
(180-\g:360+\g:{\a} and
{\b})--cycle;
\end{tikzpicture}
```

B
A
S
O
M
Với code vẽ trên, bạn có thể thay đổi tùy ý bán trục x, bán trục y và chiều cao h
của hình nón thì Tikz luôn tính được cho ta các điểm M một cách linh hoạt và tự động.
Hình nón sẽ đẹp như “thật”. Ngược lại, nếu hình nón cho điểm tiếp xúc M (biết góc ϕ)
thì ta thay đổi phần khai báo h bằng ϕ và lại tính h bằng công thức h =
b
sin ϕ là xong.

### I.2.12 Giao điểm của các đường

Trong vẽ hình khoa học, đặc biệt là các bài toán Hình học, việc sử dụng giao điểm của
các đường là thường gặp. Với giao của hai đường thẳng (đoạn thẳng) tôi đã trình bày ở
phần các phép toán tọa độ. Với hai đường bất kỳ ta cần sử dụng thư viện intersections.
Để sử dụng thư viện này, ta phải gọi thư viện (ngay sau khi khai báo gói Tikz và
trước
`\begin{document}` ) bằng cú pháp:

```latex
\usetikzlibrary{intersections}
```

Mỗi đường sẽ được đặt một cái tên cho đường bằng

```latex
\path[name path=tên đường] Dạng đường ;
hoặc \draw[name path=tên đường] Dạng đường ; . Chú ý rằng nếu sử dụng \path
```

thì Tizk chỉ đặt tên đường mà không vẽ ra, còn nếu sử dụng

`\draw`

thì đường được
vẽ ra trên hình vẽ.
Khi đó nếu có hai đường đã được đặt tên là c1 và c2 bằng cú pháp:

```latex
\path[name intersections={of=c1 and c2}] (intersection-1) coordinate (A);
```

Với những cặp đường chỉ có một giao điểm thì như vậy, nếu cặp đường có nhiều giao
điểm hơn thì ta sử dụng intersection-1, intersection-2, . . . cho đến hết sẽ khai báo được
tất cả các điểm.
Bạn có thể tham khảo code lấy giao điểm 2 đường tròn như dưới đây:

```latex
\begin{tikzpicture}
\draw[name path=ab] (-1.5,0)
coordinate (A) --(5.75,0)
coordinate (B);
\draw[name path=circ1] (0,0) circle
(2);
\draw[name path=circ2] (2.5,0)
circle (3);
\path[name intersections={of=circ1
and circ2}]
(intersection-1) coordinate (M)
(intersection-2) coordinate (N)
;
\path[name intersections={of=circ1
and ab}]
(intersection-1) coordinate (P)
(intersection-2) coordinate (Q)
;
\path[name intersections={of=circ2
and ab}]
(intersection-1) coordinate (I)
(intersection-2) coordinate (J)
;
\fill[blue] (M)node[right]{$M$}
circle (1pt);
\fill[red] (N)node[right]{$N$}
circle (1pt);
\foreach \x in
{A,B,P,Q,I,J}\fill[black] (\x)
circle (1pt)+(90:2mm)node{$\x$};
\end{tikzpicture}
```

M
N
A
B
P
Q
I
J
Bạn để ý thấy điểm Q không hiển thị đúng chỗ. Thật vậy. Vì đường tròn circ1 chỉ
cắt đoạn AB tại một điểm nên điểm Q Tikz sẽ lấy ngẫu nhiên. Điều này rất quan trọng
khi bạn cần tìm giao điểm của các đường bằng thư viện intersections bạn cần biết số
giao điểm “thực” của hai đường đó. (giao điểm nhìn thấy).

### I.2.13 Môi trường scope, clip, node và pic

• Môi trường scope:
Tikz cung cấp môi trường scope với cú pháp
