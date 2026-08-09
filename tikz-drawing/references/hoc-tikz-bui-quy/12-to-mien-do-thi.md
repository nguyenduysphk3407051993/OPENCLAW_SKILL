# Vẽ và tô miền đồ thị hàm số

> Trích từ `HocTikztheocachcuaBan_BuiQuy.pdf`, trang 45–58.

---

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

```latex
\begin{tikzpicture}[>=stealth]
\def\f(#1){sqrt(#1+1)}
\draw[->] (-3,0)--(0,0)node[below
right]{$O$}--(4,0)
node[above]{$x$};
\draw[->]
(0,-4)--(0,4)node[left]{$y$};
\draw[samples=500,blue, line
width=1]
plot[domain=-1:4](\x,{\f(\x)})
plot[domain=-1:4](\x,{-\f(\x)});
\draw (3,-1)
node[above]{$f(x)=-\sqrt{x+1}$};
\draw[dashed] (3,0)--(3,2)--(0,2);
\draw (3,3)node{\bf samples};
\end{tikzpicture}
```

O
x
y
f(x) = −
√
x + 1

### samples

Một điều khác nữa tôi lưu ý các bạn, thông thường các bạn hay để domain ở ngay
tham số sau lệnh`\draw` . Điều này gây khó khăn khi ta vẽ hai đồ thị liên tiếp để tô miền
(mà tôi sẽ nói ở phần sau). Thông thường ta nên để domain ở sau

`plot[domain=]`

thì sẽ chủ động hơn trong việc quyết định khoảng vẽ đồ thị giống như hai ví dụ trên.
Qua kinh nghiệm vẽ đồ thị hàm số. Việc lựa chọn domain cũng cần sự tinh tế nhất
định. Chẳng hạn với hàm số y =
√
2 − x. Bạn thông thường vẽ đồ thị hàm số với domain
=-2:2 tức là điểm xuất phát là bên trái, điểm kết thúc là bên phải. Nhưng bạn hãy thử
xem hình dưới đây để thấy sự lựa chọn domain cần sự tinh tế như thế nào:

```latex
\begin{tikzpicture}[>=stealth]
\draw[->] (-3,0)--(0,0)node[below
right]{$O$}--(3,0)
node[above]{$x$};
\draw[samples=500,blue, line
width=1]
plot[domain=-2:2](\x,{sqrt(2-\x)});
\draw (2,0)node[below]{$2$};
\end{tikzpicture}
```

O
x
2
Nếu zoom lên, bạn sẽ thấy tại điểm x = 2 đồ thị bị cách trục hoành một khoảng nhỏ
mặc dù trên phương diện lý thuyết thì hàm số vẫn xác định tại x = 2. Lý do chính là
cách vẽ của Tikz chia thành các khoảng nhỏ để vẽ các đoạn thẳng thông qua tham số
samples nên ở một lân cận nào đó của điểm x = 2 sẽ kết thúc việc vẽ dẫn đến bị đứt
đoạn.
Để giải quyết vấn đề này bạn chỉ cần đổi chiều domain. Tại sao lại vậy? Vì khi đổi
chiều domain thì Tikz sẽ vẽ từ điểm bắt đầu là x = 2 nên đồ thị sẽ liền nét từ đó,
phần cách đoạn là phần cuối cùng tại một lân cận của x = −2 nên bạn sẽ hầu như thấy
không thay đổi tại x = −2 (vì không vẽ tiếp đồ thị nữa). Bạn hãy so sánh code dưới đây
và code phía trên cùng hai hình vẽ để có kinh nghiệm cho bản thân:

```latex
\begin{tikzpicture}[>=stealth]
\draw[->] (-3,0)--(0,0)node[below
right]{$O$}--(3,0)node[above]{$x$};
\draw[samples=500,blue, line
width=1]
plot[domain=2:-2](\x,{sqrt(2-\x)});
\draw (2,0)node[below]{$2$};
\end{tikzpicture}
```

O
x
2

### III.2 Tô miền đồ thị hàm số

Thông thường trong các bài toán, ta có một số dạng tô miền đồ thị như sau:
• Tô miền đồ thị hàm số y = f(x), x = a, x = b và trục hoành.
• Tô miền đồ thị hàm số giao bởi hai đồ thị hàm số y = f(x) và y = g(x)
Với cả hai dạng trên, ta quy về việc có sẵn các hoành độ để tô miền hay không. Với
mục đích code càng ngắn gọn, đơn giản và đặc biệt là độ chính xác càng cao thì càng
tốt. Mỗi trường hợp ta có cách giải quyết cụ thể khác nhau.

### III.2.1 Khi đã biết hoành độ các điểm cận của miền cần tô

Khi đã biết hoành độ các điểm cận của miền cần tô, ta dùng lệnh ngắn gọn như sau:
Chẳng hạn cần tô miền giới hạn bởi đồ thị hàm số y = f(x), y = g(x), x = a và x = b,
khi đó ta sử dụng lệnh:

```latex
\draw[smooth] plot[domain=a:b](\x,{f(x)})--plot[domain=b:a](\x,{g(x)})--cycle;
```

Ở đây ta để ý đầu bút vẽ. Hiểu đơn giản sẽ là bút vẽ đồ thị hàm số f(x) từ x = a
đến điểm x = b và sau đó vẽ tiếp đồ thị hàm số g(x) từ điểm x = b đến x = a. Và như
vậy bút vẽ sẽ đi một miền kín để tô màu ưng ý.
Ví dụ cụ thể, chẳng hạn tô miền đồ thị hàm số y = x3
3 , x = 1 , x = 2 và trục hoành:

```latex
\begin{tikzpicture}[>=stealth]
\def\f(#1){((#1)^2)/3}
\draw[->] (-3,0)--(0,0) node[below
right]{$O$}--(5,0)
node[above]{$x$};
\draw[->] (0,-4)--(0,4)
node[left]{$y$};
\fill[blue,smooth] (1,0) --
plot[domain=1:2] (\x,{\f(\x)})
-- (2,0) -- cycle;
\draw[smooth,red, line width=1]
plot[domain=-1:2.5]
(\x,{\f(\x)});
\draw (1,0) node[below left]{$1$}
(2,0) node[below left]{$2$};
\end{tikzpicture}
```

O
x
y
1
2
Như vậy việc còn lại bạn chỉ cần vẽ hai đường thẳng x = 1 và x = 2 nữa là việc tô
miền đã hoàn thành.
Một ví dụ khác là tô miền phần giao hai đồ thị mà ta có thể dễ dàng tìm thấy các
hoành độ giao điểm bằng cách giải phương trình f(x) = g(x). Chẳng hạn tô miền phần
giới hạn bởi hai đồ thị hàm số y = x + 2 và y = x2
Ta dễ dàng tìm được hoành độ giao điểm của hai đồ thị này là nghiệm phương trình
x2 = x + 2 ⇒ x = −1 hoặc x = 2. Khi đó ta thực hiện vẽ đồ thị y = x2 từ x = −1 đến
x = 2 rồi tiếp tục vẽ y = x + 2 từ x = 2 đến x = −1:

```latex
\begin{tikzpicture}[>=stealth]
\draw[->] (-3,0)--(0,0) node[below
right]{$O$} -- (3,0)
node[above]{$x$};
\draw[->] (0,-4)--(0,4)
node[left]{$y$};
\fill[blue,smooth]
plot[domain=-1:2] (\x,{(\x)^2})
-- plot[domain=2:-1] (\x,{\x+2})
-- cycle;
\draw[smooth,red, line width=1]
plot[domain=-1.5:2.5]
(\x,{(\x)^2});
\draw[smooth,red, line width=1]
plot[domain=-1.5:2.5] (\x,{\x
+2});
\draw[dashed] (-1,0)--(-1,1)
(2,0)--(2,4);
\draw (-1,0) node[below left]{$-1$}
(2,0) node[below left]{$2$};
\end{tikzpicture}
```

O
x
y
−1
2
Chú ý rằng các bài toán có thể tìm hoành độ giao điểm nhưng hoành độ đó là số vô
tỉ hoặc các số thập phân vô hạn. Ta không nên lấy các giá trị xấp xỉ của nó mà hãy gán
cho giá trị đó vào một biến. Khi đó ta hoàn toàn có thể dùng biến đó đưa vào domain
để chính xác đồ thị.
Chẳng hạn như hoành độ giao điểm của hai đồ thị f(x) = x2 và g(x) = −x+1. Khi giải
phương trình f(x) = g(x) ta có hai nghiệm lần lượt là x1 = −1 −
√
5
2
và x2 = −1 +
√
5
2
.
Nếu bạn bấm máy tính để lấy xấp xỉ các con số để đưa vào domain dẫn đến đồ thị
không hoàn toàn chính xác và đồng thời việc nhớ các con số dài ngoằng để nhập vào
cũng làm code của bạn bớt đi tính thẩm mĩ. Giải pháp là bạn sẽ gán hai biến a = x1 và
b = x2 sau đó đưa a, b vào domain

```latex
\begin{tikzpicture}[>=stealth]
\pgfmathsetmacro{\a}{(-1-sqrt(5))/2}
\pgfmathsetmacro{\b}{(-1+sqrt(5))/2}
\draw[->] (-3,0)--(0,0) node[below
right]{$O$} -- (3,0)
node[above]{$x$};
\draw[->] (0,-4)--(0,4)
node[left]{$y$};
\fill[blue,smooth]
plot[domain=\a:\b](\x,{(\x)^2})
-- plot[domain=\b:\a]
(\x,{-\x+1}) -- cycle;
\draw[smooth,red, line width=1]
plot[domain=\a-0.5:\b+0.5]
(\x,{(\x)^2});
\draw[smooth,red, line width=1]
plot[domain=\a-0.5:\b+0.5]
(\x,{-\x +1});
\draw[dashed] (\a,0) -- (\a,-\a+1)
(\b,0) -- (\b,-\b+1);
\draw (\a,0) node[below]
{$\dfrac{-1-\sqrt{5}}{2}$}
(\b,0) node[below]
{$\dfrac{-1+\sqrt{5}}{2}$};
\end{tikzpicture}
```

O
x
y
−1 −
√
5
2
−1 +
√
5
2
Nếu cả hai hàm số đều có công thức phức tạp mà không phải là bậc nhất như
trên, bạn hãy gán thêm hai biến fa và fb là các tung độ giao điểm tương ứng với lệnh
pgfmathsetmacro như khi gán biến a và b rồi đưa các tung dộ tương ứng vào điểm
cần vẽ.

### III.2.2 Tô miền đồ thị không biết hoành độ giao điểm

Một vấn đề đặt ra là nhiều khi ta có hàm số f(x), hàm số g(x) nhưng việc giải phương
trình f(x) = g(x) gặp khó khăn. Khi đó đến cả công thức nghiệm ta cũng chẳng có thì
làm thế nào? Bạn hãy dùng môi trường scope với lệnh clip
Một ví dụ đơn giản là tô miền phần giới hạn của đồ thị hàm số f(x) = x3 và đường
tròn có tâm là gốc tọa độ, bán kính bằng 1 được đánh dấu X như hình vẽ sau:

```latex
\begin{tikzpicture}[x=2cm,y=2cm]
\draw[->] (-1.5,0)--(1.5,0)
node[below]{$x$};
\draw[->] (0,-1.5) --(0,1.5)
node[left]{$y$};
\draw plot[domain=-1.1:1.1,smooth]
(\x,{(\x)^3})
node[below right]{$y=x^3$};
\draw (0,0) circle(1);
\path
(0,0) node[above left]{$O$}
(1,0) node[below right]{$1$}
(-1,0) node[below left]{$-1$}
(0,1) node[above left]{$1$}
(0,-1) node[below left]{$-1$};
\draw (0.75,0.15) node{X}
(-0.75,-0.15)node{X};
\end{tikzpicture}
```

x
y
y = x3
O
1
−1
1
−1
X
X
Bình thường bạn sẽ nghĩ đến việc dùng phương trình đường tròn x2 + y2 = 1 để suy
ra hàm số y =
p
1 − x2. Tuy nhiên việc giải phương trình x3 =
p
1 − x2 đã quá sức bạn.
Hoặc có thể bạn giải được nhưng mất rất nhiều thời gian.
Bạn hãy phân tích phần được tô miền sẽ nằm trong đường tròn và nằm ở phần giới
hạn bởi đồ thị f(x) = x3 với trục hoành và đường thẳng x = 1, x = −1. Khi đó bạn hãy
tô toàn bộ phần giới hạn bởi đồ thị hàm số f(x) = x3 với các đường x = 1, x = −1 và
trục hoành. Sau đó cắt đi chỉ lấy phần nằm bên trong đường tròn:

```latex
\begin{tikzpicture}[x=2cm,y=2cm]
\draw[->] (-1.5,0)--(1.5,0)
node[below]{$x$};
\draw[->] (0,-1.5) --(0,1.5)
node[left]{$y$};
\fill[blue,smooth] (-1,0) --
plot[domain=-1:1] (\x,{(\x)^3})
-- (1,0) -- cycle;
\draw plot[domain=-1.1:1.1,smooth]
(\x,{(\x)^3}) node[below right]
{$y=x^3$};
\draw (0,0) circle(1);
\path
(0,0) node[above left]{$O$}
(1,0) node[below right]{$1$}
(-1,0) node[below left]{$-1$}
(0,1) node[above left]{$1$}
(0,-1) node[below left]{$-1$};
\end{tikzpicture}
```

x
y
y = x3
O
1
−1
1
−1

```latex
\begin{tikzpicture}[x=2cm,y=2cm]
\draw[->] (-1.5,0)--(1.5,0)
node[below]{$x$};
\draw[->] (0,-1.5) --(0,1.5)
node[left]{$y$};
\begin{scope}
\clip (0,0) circle (1);
\fill[blue,smooth] (-1,0) --
plot[domain=-1:1] (\x,{(\x)^3})
-- (1,0) -- cycle;
\end{scope}
\draw plot[domain=-1.1:1.1,smooth]
(\x,{(\x)^3}) node[below right]
{$y=x^3$};
\draw (0,0) circle(1);
\path
(0,0) node[above left]{$O$}
(1,0) node[below right]{$1$}
(-1,0) node[below left]{$-1$}
(0,1) node[above left]{$1$}
(0,-1) node[below left]{$-1$};
\end{tikzpicture}
```

x
y
y = x3
O
1
−1
1
−1
Và bây giờ bạn đã thấy thành quả. Bạn chỉ việc xem hai code trên bạn đã hiểu việc
dùng scope và clip hiệu quả như thế nào.
Bạn hãy thử thực hành với các hình vẽ khác xem sao.

### III.2.3 Sử dụng even odd rule

Một cách khác để tô một miền kín là sử dụng tham số even odd rule. Hiểu đơn
giản even là chẵn, odd là lẻ. Và tham số even odd rule chính là lựa chọn miền tô
không giao nhau của các miền kín.
Ví dụ ta có ba miền kín coi như ba tập hợp A, B và C. Khi biểu diễn ba tập hợp
này sẽ có các miền giao nhau và không giao nhau. Miền nào thuộc số chẵn trong số ba
tập hợp A, B, C thì sẽ không tô và chỉ tô miền lẻ.
Các bạn hãy xem hình dưới đây để hiểu thế nào là miền chẵn (even) và lẻ (odd):

```latex
\begin{tikzpicture}[scale=0.75]
\fill[blue!50, even odd rule] (0,0)
circle (3) (3,0) circle (3)
(3,3) circle (3);
\draw (0,0) circle (3);
\draw (3,0) circle (3);
\draw (3,3) circle (3);
\draw (1,-1)node{2} (4,-2)node{1}
(4,1)node{2} (4,4)node{1}
(1.5,1.75)node{3}
(0.5,2.5)node{2} (-1,0)node{1};
\end{tikzpicture}
```

2
1
2
1
3
2
1
Nhìn hình vẽ trên, các miền là giao của số lẻ miền sẽ được tô, các miền là giao của
số chẵn miền không được tô. Tác động này là do sử dụng lệnh:

```latex
\fill[blue!50,even odd rule](0,0) circle (3)
(3,0) circle (3) (3,3) circle (3);
```

Mặc định của tikz (khi không sử dụng even odd rule) là tô kín mọi miền kể cả số
chẵn và số lẻ. Khi đó ta sử dụng khéo léo even odd rule sẽ tô được miền ta ưng ý.
Như vậy, khi tô các miền lẻ thì ta sử dụng even odd rule. Vậy muốn tô miền chẵn thì
làm thế nào? Ta hãy đánh lừa Tikz bằng cách thêm một miền bao bên ngoài tất cả các
miền trên, khi đó các miền đang lẻ sẽ thành chẵn và ngược lại. Hoặc là bạn có thể sử
dụng một cách khác, tức là bạn tô sẵn nền, sau đó to các miền lẻ bằng white. Vậy là
các miền chẵn sẽ được tô. Chú ý rằng muốn dùng thủ thuật đánh tráo này, bạn sẽ phải
clip hình bởi nếu không sẽ có những miền lẻ mới và miền chẵn mới như hình dưới đây
tôi đã thêm một miền mới bằng lệnh:

```latex
\fill[blue!50, even odd rule] (0,0) circle (3) (3,0) circle (3)
(3,3) circle (3) (2,2) circle (7);
\begin{tikzpicture}
\fill[blue!50, even odd rule] (0,0) circle (3) (3,0) circle (3) (3,3) circle
(3) (2,2) circle (7);
\draw (0,0) circle (3);
\draw (3,0) circle (3);
\draw (3,3) circle (3);
\draw (1,-1)node{2} (4,-2)node{1} (4,1)node{2} (4,4)node{1} (1.5,1.75)node{3}
(0.5,2.5)node{2} (-1,0)node{1};
\end{tikzpicture}
```

2
1
2
1
3
2
1

### III.3 Các kiểu tô miền

Bạn thích tô màu các miền thì thực hiện các lệnh fill như trên đây tôi trình bày, chỉ
việc đổi tên màu là bạn đã đạt được ý nguyện. Nếu bạn không muốn tô miền bằng màu
sắc bạn cũng có các kiểu tô miền khác mà Tikz đã thiết kế sẵn gọi là pattern.
Để sử dụng pattern, trong file biên dịch bạn cần gọi thư viện này ra bằng

`\usetikzlibrary{patterns}`

trước

`\begin{document} .`

Tại lệnh fill bạn sử dụng như sau:

`\fill[pattern=name pattern] .`

Một số lựa chọn kiểu tô:
• horizontal lines
• vertical lines
• north east lines
• north west lines
• grid
• crosshatch
• dots
• crosshatch dots
• fivepointed stars
• sixpointed stars
• bricks
• checkerboard
• checkerboard light gray
• horizontal lines light gray
• horizontal lines gray
• horizontal lines dark gray
• horizontal lines light blue
• horizontal lines dark blue
• crosshatch dots gray
• crosshatch dots light steel blue
Chẳng hạn, ở ví dụ trên tôi sẽ dùng kiểu gạch sọc:

```latex
\begin{tikzpicture}[x=2cm,y=2cm]
\draw[->] (-1.5,0) -- (1.5,0) node[below]{$x$};
\draw[->] (0,-1.5) -- (0,1.5) node[left]{$y$};
\begin{scope}
\clip (0,0) circle (1);
\fill[pattern=north east lines,smooth] (-1,0) -- plot[domain=-1:1]
(\x,{(\x)^3}) -- (1,0) -- cycle;
\end{scope}
\draw plot[domain=-1.1:1.1,smooth] (\x,{(\x)^3}) node[below right]{$y=x^3$};
\draw (0,0) circle(1);
\path
(0,0) node[above left]{$O$}
(1,0) node[below right]{$1$}
(-1,0) node[below left]{$-1$}
(0,1) node[above left]{$1$}
(0,-1) node[below left]{$-1$};
\end{tikzpicture}
```

x
y
y = x3
O
1
−1
1
−1
Vậy là bạn đã hoàn thành được việc vẽ tô miền cho các hàm số trong các bài tích
phân rồi đó. Chúc bạn có thể đơn giản hơn một phần việc không hề dễ dàng này trong
tương lai!

### IV

### Tư duy hình họa để vẽ hình

Để có một hình vẽ khoa học đảm bảo độ chính xác, hơn nữa lại đẹp và code vẽ tối
ưu. Khuyến cáo bạn nên tìm hiểu về phương pháp tư duy và trình tự phân tích, tổng
hợp các yếu tố cơ bản của một hình vẽ. Từ đó bạn sẽ có thể vẽ bất cứ thứ gì bạn muốn.

### IV.1 Trình tự cơ bản

Bạn hãy tham khảo sơ đồ sau:
Phân tích
hình ảnh
Các thông số
đầu vào
Mối liên quan
giữa các đối tượng
Yêu cầu
hiển thị
Độ chính xác
của thông số
Mối liên quan
của thông số
Hình ảnh
hiển thị
Màu sắc
hiển thị
Cách
khai báo
Công thức
tính toán
Chọn lệnh
vẽ
Tùy chọn
cho lệnh vẽ
Tọa độ
đặt đối tượng
Tạo macro hoặc
dùng lập trình
nếu thấy cần thiết
Soạn thảo code
Kiểm tra độ chính xác
của hình vẽ
Chỉnh sửa code
cho hợp lý
Kết quả
cuối cùng
Các bước khuyến cáo trên đây mặc dù nhìn có vẻ rất rối và nhiều thao tác. Tuy
nhiên, khi bạn rèn luyện thường xuyên, quá trình phân tích hình vẽ sẽ rất nhanh, có thể
chỉ xảy ra trong một khoảng thời gian rất ngắn khi nó đã trở thành thói quen của bạn.
Việc phân tích hình vẽ là điều tối quan trọng, bởi từ đó bạn sẽ có thể tìm ra phương
pháp vẽ tối ưu nhất cho hình vẽ của bạn.
