# Bảng xét dấu và bảng biến thiên

> Trích từ `HocTikztheocachcuaBan_BuiQuy.pdf`, trang 33–41.

---

### II

### Bảng xét dấu - Bảng biến thiên - Đồ

### thị hàm số

### II.1 Bảng xét dấu

Ta hãy hình dung bảng xét dấu gồm 2 dòng, một dòng có giá trị của biến x, một
dòng có giá trị là dấu của f(x) (hoặc f′(x)) trong bài khảo sát và vẽ đồ thị hàm số. Ta
có thể dùng foreach để vẽ bảng này một cách rất đơn giản. Chẳng hạn một bảng như
sau:

```latex
\begin{tikzpicture}[scale=.75]
\draw[thin,opacity=.5] (-1,-2) grid
(9,1);
\foreach \i/\x in
{0/x,2/-\infty,4/-1,6/2,8/+\infty}
\path (\i,.5) node{$\x$};
\foreach \i/\x in
{0/f(x),3/-,4/0,5/+,6/0,7/-}
\path (\i,-.5) node{$\x$};
\draw (-.5,0)--(8.5,0)
(.75,1)--(.75,-1);
\end{tikzpicture}
```

x
−∞
−1
2
+∞
f(x)
−
0
+
0
−
Tất nhiên trong code trên bạn đã hình dung trong đầu các vị trí các điểm cần đặt
giá trị. Công việc này bạn hoàn toàn có thể làm đúng như việc bạn vẽ bằng bút trên
giấy vậy. Một cách khác là bạn có thể sử dụng gói tkz-tab để vẽ mà tôi sẽ trình bày ở
phần sau đây.

### II.2 Bảng biến thiên

Cấu trúc của bảng biến thiên gồm ba dòng. Dòng giá trị x, dòng giá trị đạo hàm
f′(x) và dòng f(x). Như vậy ta cần đến gói Tkz-tab để làm việc này.
Khai báo gói bằng lệnh sau:

`\usepackage{tkz-tab}`

Sau khi khai báo gói rồi, ta bắt đầu vẽ bảng biến thiên nhé:

```latex
\begin{tikzpicture}
\tkzTabInit[nocadre,lgt=1.5,espcl=2,deltacl=.5]
{$x$/0.7, $f'(x)$/0.7, $f(x)$/2}
{$-\infty$,$-1$,$1$,$2$,$+\infty$}
\end{tikzpicture}
```

x
f′(x)
f(x)
−∞
−1
1
2
+∞
Như vậy ta đã có khung của một bảng biến thiên. Nếu bạn có ý định thay đổi thì cứ
thử thay đổi từng thông số một để kiểm tra sự thay đổi của hình vẽ. Như vậy bạn sẽ
hiểu thêm được ý nghĩa của các thông số.

```latex
\tkzTabInit[tùy chọn]{Đối số dòng}{Đối số cột}
```

• Tùy chọn

`[Tùy chọn]`

gồm các thông số đầu vào như sau:
Tùy chọn
Mặc định
Ý nghĩa
espcl
2 cm
Độ rộng cột
lgt
2 cm
Độ rộng cột thứ nhất
deltacl
0.5 cm
Độ rộng cột một và cột cuối cùng có đường kẻ cuối
lw
0.4 pt
Nét kẻ bảng
nocadre
false
Không có đường kẻ quanh ngoài bảng
color
false
Mầu bảng có hay không
colorC
white
Mầu cột thứ nhất
colorL
white
Mầu hàng thứ nhất
colorT
white
Mầu bên trong bảng
colorV
white
Mầu của các biến trong bảng
•
`{Đối số dòng}` : Quy định bảng của mình có bao nhiêu dòng. Trong ví dụ trên
bạn thấy ta nhập vào là

```latex
{$x$ / 0.7, $f'(x)$ / 0.7, $f(x)$ /2} . Điều đó
```

có nghĩa bảng có 3 dòng gồm dòng x với độ cao là 0.7, dòng f′(x) với độ cao là 0.7
và dòng f(x) với độ cao là 2. Bạn có thể thay đổi các độ cao và giá trị này để có
một bảng như ý.
•
`{Đối số cột}` : Quy định bảng có bao nhiêu cột. Trong ví dụ trên ta có:
`{$-\infty$,$-1$,$1$,$2$,$+\infty$}` . Như vậy bảng của ta gồm các thông
số (ở dòng x) lần lượt từ trái qua phải là −∞, −1, 2 và +∞.
`\tkzTabLine{Giá trị dòng}` : Để nhập thông số vào các dòng trong bảng biến
thiên, ta có thể sử dụng lệnh này, trong đó Giá trị dòng gồm các số liệu cần nhập vào.
Các số liệu nhập vào ngăn cách nhau bởi dấu

`,`

như trong ví dụ trên:
`\tkzTabLine{,-,z,+,d,-,z,+,}` . Các số liệu này có một số quy tắc sau:
Nhập vào
Hiển thị
z
cột đứng xuyên qua số 0
t
Đường đứng đứt đoạn
d
Kẻ hai đường đứng
h
Tô đường kẻ ô
+
ô mang dấu +
- ô
mang dấu -
Bạn xem bảng dưới đây:

```latex
\begin{tikzpicture}
\tkzTabInit[nocadre,lgt=1.5,espcl=2,deltacl=.5]
{$x$/0.7, $f'(x)$/0.7, $f(x)$/2}
{$-\infty$,$-1$,$1$,$2$,$+\infty$}
\tkzTabLine{,-,z,+,d,-,z,+,}
\end{tikzpicture}
```

x
f′(x)
f(x)
−∞
−1
1
2
+∞
−
0
+
−
0
+
`\tkzTabVar[Tùy chọn]{Các đối số}` : Dòng lệnh vẽ mũi tên thể hiện chiều biến
thiên. Mỗi đối số có dạng

`s/e`

trong đó s quy định chiều mũi tên, e là giá trị số hoặc
biểu thức (của hàm số).
Nhập s

`+/e`

Hiển thị giá trị e ở phía trên.

`-/e`

Hiển thị giá trị e ở phía dưới
Và khi đó, với hai thông số liên tiếp nhau dạng

`s/e`

ngăn cách nhau bởi dấu

`,`

thì tkz-tab tự hiểu rằng chiều mũi tên (chiều biến thiên) đi như thế nào. Chẳng hạn
như dưới đây:

```latex
\tkzTabVar{+/$+\infty$ ,-/ $-4$ ,+/$-3$, -/$-4$,+/$+\infty$}
```

Bạn sẽ có mã hoàn chỉnh của bảng biến thiên như sau:

```latex
\begin{tikzpicture}
\tkzTabInit[nocadre,lgt=1.5,espcl=2,deltacl=.5]
{$x$/0.7, $f'(x)$/0.7, $f(x)$/2}
{$-\infty$,$-1$,$1$,$2$,$+\infty$}
\tkzTabLine{,-,z,+,d,-,z,+,}
\tkzTabVar{+/$+\infty$ ,-/ $-4$ ,+/$-3$, -/$-4$,+/$+\infty$}
\end{tikzpicture}
```

x
f′(x)
f(x)
−∞
−1
1
2
+∞
−
0
+
−
0
+
+∞
+∞
−4
−4
−3
−3
−4
−4
+∞
+∞
Hoặc nếu dòng f(x), tại x = 1 cũng không xác định thì bạn có thể thay bằng dòng
lệnh:

```latex
\tkzTabVar{+/$+\infty$ ,-/ $-4$ ,+D+/$+\infty$, -/$-4$,+/$+\infty$}
```

Bạn sẽ có ngay kết quả:

```latex
\begin{tikzpicture}
\tkzTabInit[nocadre,lgt=1.5,espcl=2,deltacl=.5]
{$x$/0.7, $f'(x)$/0.7, $f(x)$/2}
{$-\infty$,$-1$,$1$,$2$,$+\infty$}
\tkzTabLine{,-,z,+,d,-,z,+,}
\tkzTabVar{+/$+\infty$ ,-/ $-4$ ,+D+/$+\infty$ , -/$-4$,+/$+\infty$}
\end{tikzpicture}
```

x
f′(x)
f(x)
−∞
−1
1
2
+∞
−
0
+
−
0
+
+∞
+∞
−4
−4
+∞
+∞
−4
−4
+∞
+∞
Hoặc sử dụng lệnh:

```latex
\tkzTabVar{+/$+\infty$ ,-/ $-4$ ,+D-/$+\infty$/$-\infty$, +/$-4$,-/$-\infty$}
```

Ta sẽ được:

```latex
\begin{tikzpicture}
\tkzTabInit[nocadre,lgt=1.5,espcl=2,deltacl=.5]
{$x$/0.7, $f'(x)$/0.7, $f(x)$/2}
{$-\infty$,$-1$,$1$,$2$,$+\infty$}
\tkzTabLine{,-,z,+,d,-,z,+,}
\tkzTabVar{+/$+\infty$ ,-/ $-4$ ,+D-/$+\infty$/$-\infty$ , +/$-4$,-/$-\infty$}
\end{tikzpicture}
```

x
f′(x)
f(x)
−∞
−1
1
2
+∞
−
0
+
−
0
+
+∞
+∞
−4
−4
+∞
−∞
−4
−4
−∞
−∞
Hơn thế nữa, nếu bạn muốn một khoảng nào đó f′(x) hoặc f(x) không xác định bằng
cách gạch chéo khoảng thuộc dòng đó, bạn có thể thay +D bằng +H hoặc −H,...

```latex
\begin{tikzpicture}
\tkzTabInit[nocadre,lgt=1.5,espcl=2,deltacl=.5]
{$x$/0.7, $f'(x)$/0.7, $f(x)$/2}
{$-\infty$,$-1$,$1$,$2$,$+\infty$}
\tkzTabLine{,-,z,h,d,-,z,+,}
\tkzTabVar{+/$+\infty$ ,-H/ $-4$ ,D-/$-\infty$ , +/$-4$,-/$-\infty$}
\end{tikzpicture}
```

x
f′(x)
f(x)
−∞
−1
1
2
+∞
−
0
−
0
+
+∞
+∞
−4
−∞
−4
−4
−∞
−∞

### II.3 Kết hợp Tikz và tkz-tab vẽ bảng biến thiên tùy chỉnh

Khi vẽ bảng biến thiên của các hàm số thực tế. Trong nhiều trường hợp quý vị cần
tùy chỉnh bảng biến thiên theo ý mình. Tất nhiên trong bảng biến thiên đó thì hai dòng
x và f′(x) hầu như không có gì cần tùy chỉnh. Chỉ cần tùy chỉnh dòng f(x) mà thôi.
Để tùy chỉnh dòng f(x), trước hết ta tìm hiểu về cách định nghĩa các điểm trong
bảng biến thiên. Gói tikz-tab đã định nghĩa các điểm cơ bản của bảng theo vị trí như
hình sau:

```latex
\begin{tikzpicture}
\tkzTabInit[nocadre,lgt=1.5,espcl=3,deltacl=0.5]
{$x$/1, $f'(x)$/1, $f(x)$/2.5}
{$-\infty$,$-1$,$1$,$2$,$+\infty$}
\tkzTabLine{,-,z,-,d,+,z,-,}
\foreach \i in {1,...,5}{
\foreach \j in {1,...,3}{
\draw (N\i\j) node[circle,fill=white,inner sep=0.1]{$N_{\i\j}$};
}
}
\end{tikzpicture}
```

x
f′(x)
f(x)
−∞
−1
1
2
+∞
−
0
−
+
0
−
N11
N12
N13
N21
N22
N23
N31
N32
N33
N41
N42
N43
N51
N52
N53
Như vậy Quý vị hoàn toàn có thể vẽ tùy ý dòng f(x) theo ý mình dựa vào các điểm
đã được định nghĩa Nij. Số điểm này phụ thuộc bảng của quý vị dài hay ngắn (có nhiều
giá trị x hay không). Chẳng hạn như ở bảng trên, khi ta vẽ chiều biến thiên từ −∞ đến
1 là nghịch biến. Nếu bình thường vẽ bằng lệnh

`\tkzTabVar`

thì sẽ vẽ thẳng một mũi
tên từ điểm N12 đến điểm N33. Tại hạ lại muốn vẽ kiểu mũi tên từ +∞ đến f(−1) = −2
rồi tiếp tục lại vẽ mũi tên thứ hai từ f(−1) đến f(1) = −4. Như vậy ta sẽ vẽ bằng tikz
thuần dựa vào các điểm có sẵn:

```latex
\begin{tikzpicture}
\tkzTabInit[nocadre,lgt=2,espcl=3,deltacl=0.5]
{$x$/1, $f'(x)$/1, $f(x)$/2.5}
{$-\infty$,$-1$,$1$,$2$,$+\infty$}
\tkzTabLine{,-,z,-,d,+,z,-,}
\draw (N12)node[below](A){$+\infty$} ($(N22)!0.5!(N23)$) node (B){$-2$} (N33)
node[above left](C){$-4$};
\draw[-stealth] (A)--(B);
\draw[-stealth] (B)--(C);
\end{tikzpicture}
```

x
f′(x)
f(x)
−∞
−1
1
2
+∞
−
0
−
+
0
−
+∞
−2
−4
Tiếp theo, quý vị muốn vẽ đường thẳng đứng biểu diễn hàm số không xác định tại
x = 1. Ta hãy vẽ đoạn thẳng từ N32 đến N33 với tham số double như sau:

```latex
\draw[double] ([yshift=-1mm]N32)--(N33);
```

Quý vị nên chú ý [yshift=-1mm] ở điểm N32 chính là đển đường thẳng đứng cách vạch
kẻ ngang 1mm. Nếu quý vị không muốn tách rời ra thì cứ việc bỏ nó đi là xong.
Phía bên phải của bảng biến thiên, Quý vị vẫn vẽ bình thường hai mũi tên biểu
diễn đồng biến từ x = 1 đến x = 2 và nghịch biến từ x = 2 đến +∞. Tuy nhiên giá trị
f(2) = −3 lại nhỏ hơn −2 nên quý vị muốn nó thấp hơn cả f(−1) = −2. Vậy thì quý vị
hãy xác định điểm đặt f(2) = −3 bằng công thức

`$(N42)!0.75!(N43)$`

như sau:

```latex
\draw (N33) node[above right](D){$-\infty$} ($(N42)!0.55!(N43)$)
node(E){$-3$} (N53) node[above](F){$-\infty$};
```

Chú ý rằng con số 0.55 ở trên quý vị có thể tùy ý chọn sao cho phù hợp. Hơn thế
nữa là thông số của

`$\f(x)$/2.5`

ở

`\tkzTabInit`

quý vị cũng nên chọn thay 2.5
bằng các thông số khác để nhìn bảng hài hòa hơn (độ cao của dòng f(x)).
Cuối cùng thì quý vị vẽ nốt hai mũi tên còn lại để hoàn thành bảng biến thiên:

```latex
\draw[-stealth] (D)--(E);
\draw[-stealth] (E)--(F);
```

Kết quả cuối cùng, quý vị hoàn thành bảng biến thiên theo tùy chỉnh của mình:

```latex
\begin{tikzpicture}
\tkzTabInit[nocadre,lgt=2,espcl=3,deltacl=0.5]
{$x$/1, $f'(x)$/1, $f(x)$/2.5}
{$-\infty$,$-1$,$1$,$2$,$+\infty$}
\tkzTabLine{,-,z,-,d,+,z,-,}
\draw (N12)node[below](A){$+\infty$} ($(N22)!0.5!(N23)$) node (B){$-2$} (N33)
node[above left](C){$-4$};
\draw[-stealth] (A)--(B);
\draw[-stealth] (B)--(C);
\draw[double] ([yshift=-1mm]N32)--(N33);
\draw (N33) node[above right](D){$-\infty$} ($(N42)!0.55!(N43)$)
node(E){$-3$} (N53) node[above](F){$-\infty$};
\draw[-stealth] (D)--(E);
\draw[-stealth] (E)--(F);
\end{tikzpicture}
```

x
f′(x)
f(x)
−∞
−1
1
2
+∞
−
0
−
+
0
−
+∞
−2
−4 −∞
−3
−∞

### II.4 Vẽ bảng biến thiên bằng tikz thuần

Việc vẽ bảng xét dấu và bảng biến thiên bằng tkz-tab quả thực cũng không quá khó
nếu bạn nhớ đầy đủ các lệnh và quy tắc của nó. Tất nhiên nhiều khi bạn không thể nhớ
được các lệnh, tùy chọn và quy cách của tkz-tab thì bạn cũng hoàn toàn vẽ được bảng
biến thiên bằng tikz thuần một cách đơn giản. Bạn hãy hình dung ra tọa độ của các
điểm đặt các thông số trong bảng biến thiên và sử dụng khéo léo

`\foreach`

là bạn
cũng có ngay một bảng biến thiên như ý (đặc biệt với những bảng biến thiên có sự khác
biệt thông thường). Chẳng hạn như bảng biến thiên sau:

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
