# Môi trường scope, clip, node và pic

> Trích từ `HocTikztheocachcuaBan_BuiQuy.pdf`, trang 20–25.

---

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

```latex
\begin{scope}
...
\draw ...
...
\end{scope}
```

Trong môi trường scope Mọi lệnh vẽ, lệnh khai báo chỉ có tác dụng trong môi
trường này, khi thoát ra khỏi scope thì các điểm đã khai báo , các giá trị đã gán,
tên đường đã gán . . . trong scope không còn tác dụng. Vì vậy cần sử dụng linh
hoạt môi trường này.
• Lệnh clip
Đi đôi với scope là lệnh
`\clip Dạng đường kín;` . clip dùng để cắt các phần
thừa khi vẽ hình để hình vẽ đúng theo ý vẽ. Chẳng hạn cần vẽ nửa một cung tròn
của đường tròn màu xanh nằm trong đường màu đỏ như sau:

```latex
\begin{tikzpicture}
\draw[red] (0,0) circle (1.5);
\draw[blue] (2,0) circle (2);
\end{tikzpicture}
```

Ta có thể clip như sau:

```latex
\begin{tikzpicture}
\draw[red] (0,0) circle (1.5);
\clip (0,0) circle (1.5);
\draw[blue] (2,0) circle (2);
\end{tikzpicture}
```

Để ý rằng lệnh clip sẽ có tác dụng từ vị trí đặt nó cho đến`\end{tikzpicture}`
nên ta cần kết hợp scope. Chẳng hạn trong hình vẽ trên ta lại muốn vẽ tiếp đoạn
thẳng năm bên ngoài đường tròn màu đỏ nhưng nếu để bình thường clip ta sẽ
không thấy hiển thị.

```latex
\begin{tikzpicture}
\draw[red] (0,0) circle (1.5);
\clip (0,0) circle (1.5);
\draw[blue] (2,0) circle (2);
\draw (1,0)--(4,0);
\end{tikzpicture}
```

Vậy thì ta phải đưa việc vẽ cung tròn đó vào trong môi trường scope để có thể
tiếp tục vẽ thêm

```latex
\begin{tikzpicture}
\draw[red] (0,0) circle (1.5);
\begin{scope}
\clip (0,0) circle (1.5);
\draw[blue] (2,0) circle (2);
\end{scope}
\draw (1,0)--(4,0);
\end{tikzpicture}
```

Kỹ thuật này rất hữu dụng trong việc vẽ các ký hiệu góc trong bài toán Hình học.
Chẳng hạn muốn thể hiện [
ABC trong tam giác ABC ta có thể làm như sau:

```latex
\begin{tikzpicture}
\draw (0,0) coordinate (B)
--(4,0) coordinate (C) --
(1,3) coordinate (A) --cycle;
\begin{scope}
\clip (B)--(A)--(C);
\draw[fill=yellow] (A) circle
(.25);
\end{scope}
\end{tikzpicture}
```

• node
Như tôi đã trình bày, lệnh

```latex
\node ... at ... {Đối tượng hiển thị};
```

hoặc
dùng kép kiểu như

```latex
\draw ... node{đối tượng hiển thị};
```

được dùng khá nhiều khi vẽ hình. Ở
đây ta tìm hiểu thêm về node để sử dụng cho thật sự linh hoạt.
Đối tượng hiển thị trong các lệnh trên (gọi tắt là node) được Tikz khá thoải
mái. Nó có thể là bất cứ lệnh nào trong LATEX chứ không riêng gì bfseries Tikz.
Chẳng hạn bạn muốn vẽ một hình bài toán thực tế có hình cây dừa, mà việc vẽ
cây dừa tốn quá nhiều thời gian, bạn có thể include hình png cây dừa đó vào trong
hình vẽ Tikz.

```latex
\begin{tikzpicture}
\draw (-3,0) -- (3,0);
\path (0,0) node[above]
{\includegraphics[scale=.3]
{caydua}};
\end{tikzpicture}
```

Hay nhất là trong node có thể đưa vào bất cứ thứ gì mà LATEX chấp nhận được,
kể cả môi trường tikzpictue

```latex
\begin{tikzpicture}
\draw (-3,0) -- (3,0);
\path (0,3) node{
\begin{tikzpicture}
\draw[fill=orange ] (0,0) circle
(1);
\end{tikzpicture}
};
\end{tikzpicture}
```

• pic
Tương tự như node, pic cũng là một trong những dạng có sẵn của Tikz. Sử dụng
cú pháp:

`\draw (tọa độ) pic{tên pic};`

Khi đó ta sẽ có hình ảnh của pic vào đúng tọa độ đã chỉ ra. Vấn đề là các pic này
ở đâu? tên pic là gì? Ta không cần quan tâm quá nhiều đến các pic có sẵn của
Tikz vì chủ tâm của người tạo ra Tikz là để người dùng tự tạo pic khi cần thiết.
Chẳng hạn bạn muốn vẽ một mạch điện, mỗi điện trở là một hình chữ nhật. Trong
khi mạch điện của ta có nhiều điện trở, mỗi lần vẽ điện trở lại phải vẽ một hình
chữ nhật thì thật vất vả. Ta sẽ tạo pic bằng cú pháp:

```latex
\tikzset{dientro/.pic={\draw(-.4,-.1)rectangle (.4,.1);}}
```

Sau đó ta sử dụng pic này thoải mái như sau:

```latex
\begin{tikzpicture}
\tikzset{dientro/.pic={
\draw(-.4,-.1) rectangle
(.4,.1);}}
\draw
(0,0) pic[local bounding box=R1]
{dientro}
(3,0) pic[local bounding box=R2]
{dientro}
(1.5,3) pic[local bounding
box=R3] {dientro}
;
\draw (1.75,0) --(R2) --(4,0)
--(4,3) --(R3) --(-1,3)
--(-1,0) --(R1) --(1.25,0);
\end{tikzpicture}
```

Nhân đây, để vẽ mạch điện tôi cũng đề cập đến một cách vẽ hai cạnh liên tiếp của
một hình chữ nhật xác định bởi hai đỉnh đối nhau (thường dùng khi gióng tọa độ
trong đồ thị hàm số và vẽ mạch điện) như sau:

```latex
\draw (A)-|(B); \draw (A)|-(B);
```

Chẳng hạn để rút ngắn lệnh vẽ mạch điện trên, tôi sẽ dùng:

```latex
\begin{tikzpicture}
\tikzset{dientro/.pic={
\draw(-.4,-.1) rectangle
(.4,.1);}}
\draw
(0,0) pic[local bounding box=R1]
{dientro}
(3,0) pic[local bounding box=R2]
{dientro}
(1.5,3) pic[local bounding
box=R3] {dientro}
;
\draw (1.75,0) --(R2) --(4,0)
|-(R3) -|(-1,0) --(R1)
--(1.25,0);
\end{tikzpicture}
```

### I.3 Các tùy chọn thường dùng

### I.3.1 Tùy chọn chung

Tùy chọn của Tikz là các tham số đầu vào nằm trong cặp [ ...] ở ngay sau mỗi môi
trường, lệnh vẽ. Với tất cả các lệnh vẽ, môi trường ta có một số tùy chọn chung như
sau:
• color=: Lựa chọn màu cho đối tượng. Với tùy chọn này thường thì ta không cần
nhập color= tên màu mà ta chỉ cần nhập tên màu là Tikz cũng tự hiểu được.
Tên màu có thể là yellow, blue, red, orange, pink, . . . Hơn nữa, việc xác định
màu có thêm tùy chọn red!50 ta hiểu là độ đỏ 50%, blue!20 là độ xanh 20% . . .
Ngoài ra có có một số tùy chọn left color=, right color=, bottom color=, top
color=, ball color= . . .
• rotate=: Quay đối tượng quanh gốc tọa độ một góc nào đó, đơn vị góc ở đây là
“độ” chứ không dùng radian.
• shift=: Tịnh tiến đối tượng theo một véc tơ nào đó.
Cụ thể hơn ta có xshift= và yshift= là cách tịnh tiến đối tượng theo chiều ngang
hoặc chiều dọc. Chú ý khi dùng xshift hoặc yshift thì các thông số đưa vào phải
có đơn vị độ dài (pt, mm, cm, . . . )
• scale=: Tỉ lệ hiển thị đối tượng.
Tương tự như trên ta cũng có xscale= lấy đối xứng đối tượng qua trục tung và
yscale lấy đối xứng đối tượng qua trục hoành.
• font=: Chọn cỡ chữ hiển thị trong hình vẽ (tùy chọn này thường dùng cho các
môi trường tikzpicture và scope để cỡ chữ thống nhất trong cùng một hình vẽ)
• line join, line cap: Tùy chọn này thường dùng cho môi trường tikzpicture. line
join=round để các đoạn gấp khúc mềm mại hơn, line cap=round để các đầu
mút đoạn thẳng được bo tròn.
• line width=: Độ dày nét vẽ, với tùy chọn này nếu đơn vị là điểm ảnh (pt) thì
thông số đầu vào không cần đơn vị. Nếu ta muốn dùng đơn vị độ dài khác thì cần
nhập thông số đi kèm đơn vị (mm, cm, . . . )
• smooth: Tạo độ trơn cho nét vẽ, thường dùng với vẽ đồ thị và đi kèm lệnh`\draw`
hoặc

`\fill`

• samples=: Ta hiểu rằng vẽ đường cong trong Tikz hoặc bất cứ phần mềm nào
bản chất vẫn là chia nhỏ đường cong thành các đoạn thẳng để vẽ liên tiếp các
đoạn thẳng này. samples quy định điều đó. samples càng lớn thì số điểm chia
càng nhiều, khi đó đường cong càng đẹp hơn. Tuy nhiên đi kèm với nó là việc tính
