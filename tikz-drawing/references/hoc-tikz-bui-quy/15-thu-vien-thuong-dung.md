# Thư viện hay dùng: calc, intersections, angles, patterns, decoration, shadings

> Trích từ `HocTikztheocachcuaBan_BuiQuy.pdf`, trang 70–73.

---

### VI

### Các thư viện thường dùng

Trong việc vẽ hình Tikz, bạn có thể cần một số thư viện sẵn có của Tikz để việc vẽ
đơn giản và hiệu quả hơn, chúng ta có thể tìm hiểu một số thư viện thường dùng nhất.
Cú pháp để gọi thư viên của Tikz như sau:

```latex
\usetikzlibrary{calc,angles,intersections,patterns,decorations.text,shadings}
```

Trong cú pháp gọi thư viện trên, calc, angles, intersections . . . là tên các thư
viện ta cần gọi ra. Khi cần gọi nhiều thư viện bạn chú ý chỉ cần dùng một lệnh

`\usetikzlibrary{ }`

và liệt kê tên các thư viện trong cặp ngoặc nhọn (cách nhau
bởi dấu “phẩy”) chứ không cần thiết dùng quá nhiều lệnh gọi nhé.

### VI.1 calc

Thư viện cung cấp cho ta các phép tính đối với toạ độ của Tikz. Thư viện này được
sử dụng hàng đầu khi vẽ hình. Đặc biệt là các bài hình học phẳng. Khi chúng ta sử
dụng đến các mối liên quan giữa các điểm. Chẳng hạn muốn khai báo trung điểm của
đoạn thẳng AB ta sử dụng lệnh

```latex
\path ($(A)!.5!(B)$) coordinate (A);
```

Khi đó nếu bạn không gọi thư viện calc thì Tikz sẽ báo lỗi. Như vậy, khi bạn muốn
dùng các phép tính tọa độ thì việc gọi thư viện calc là bắt buộc.

### VI.2 intersections

Thư viện để tính toán và tìm tọa độ giao điểm giữa các đường bằng cách đặt tên đường
với tùy chọn name path và lệnh lấy giao điểm bằng tùy chọn name intersections.
Chú ý rằng riêng việc lấy giao điểm của hai đường thẳng ta hoàn toàn không cần gọi
thư viện intersections. Tuy nhiên việc sử dụng thư viện intersections cũng có những
hạn chế chỉ lấy được những giao điểm “thực” giữa các đường mà thôi (nói cách khác là
nó chỉ lấy được giao điểm của các đoạn). Còn khai báo

```latex
(intersection of A--B and C--D) coordinate M
```

sẽ lấy được giao điểm của hai đường thẳng cho dù đoạn AB và CD có cắt nhau thực
hay không. Lệnh này lấy chính xác giao điểm của hai đường đi qua hai đoạn thẳng đó.
Do vậy bạn cũng nên cân nhắc khi nào dùng khai báo trực tiếp, khi nào gọi thư viện và
đặt tên đường. Khuyến cáo là khi cần giao điểm của hai đường thẳng thì nên dùng trực
tiếp, còn các đối tượng khác (đường thẳng và đường cong, đường cong và đường cong)
thì nên gọi thư viện.

### VI.3 angles

Thư viện cho ta các kí hiệu góc trong hình học phẳng. Chẳng hạn bạn xem ví dụ
sau:

```latex
\begin{tikzpicture}
\draw (0,0) coordinate (A)
--(4,0) coordinate (B)
--(1,3) coordinate (C)
--cycle
;
\draw
pic[draw,double]{angle = C--B--A}
;
\end{tikzpicture}
```

Với pic, bạn có nhiều tùy chọn trong cặp ngoặc vuông, có thể là tùy chọn mũi tên
`->` , tùy chọn màu
`red,blue ...` , tùy chọn kiểu đường, độ đậm nhạt của đường,
tùy chọn tô hoặc không (fill), . . . Một chú ý khác là bạn cần nhớ đến thứ tự các điểm
sẽ cho ta góc trong hoặc góc ngoài của tam giác trong ví dụ trên nhé.
Riêng ký hiệu vuông góc thì trước đây Tikz cũng đã có nhưng sau đó phát sinh một
số lỗi. Phiên bản hiện nay không có ký hiệu này, bạn hoàn toàn có thể tạo macro riêng
cho mình bàng vài lệnh đơn giản hoặc bạn vẽ trực tiếp.
Tất nhiên là các ký hiệu này cũng chỉ có một vài mẫu cố định, còn nếu bạn muốn
tùy biến cách ký hiệu theo ý bạn thì tôi gợi ý cho bạn tạo macro để biểu diễn ký hiệu
góc cho thoải mái.

### VI.4 patterns

Thư viện dùng để tô nền một miền phẳng nào đó giới hạn bởi các đường. Phần này
tôi đã giới thiệu khá kỹ trong phần tô miền đồ thị hàm số.

### VI.5 Decoration

Một thư viện cũng khá thường dùng khi vẽ các hình minh họa, đặc biệt là các hình
vẽ bài toán thực tế. Chúng ta thường dùng nhất là decorations.pathmorphing và
decorations.text. Bạn có thể ít dùng decorations.pathmorphing hơn nên phần này
tôi dành cho các bạn tra cứu pgfmanual.pdf
Với decorations.text, bạn sẽ thường dùng hơn khi bạn muốn hiển thị chữ chạy theo
một đường path nào đấy. Chẳng hạn bạn muốn dòng chữ chạy theo một đường tròn:

```latex
\begin{tikzpicture}
\draw[decoration={text along path,
text={M{}t d{ò}ng ch{} ch{}y
theo n{}a {}ng
tr{ò}n}},decorate] (0,0)
arc
(180:0:3) ;
\end{tikzpicture}
```

M
ộ
t
d
ò
n
g
c
h
ữ
c
h
ạ
y
t
h
e
o
n
ử
a
đườ
n
g
t
r
ò
n
Bạn cần chú ý rằng, trong tùy chọn text along path thì dòng chữ cần hiển thị là
chữ tiếng Anh hoặc tiếng Việt không dấu bạn có thể gõ bình thường, nhưng nếu như
bạn muốn hiển thị tiếng Việt, tốt nhất bạn đặt cả cụm từ tiếng Việt trong cặp dấu
ngoặc nhọn thì Tikz mới biên dịch cho bạn. Nếu bạn không để ý đến chú ý này thì việc
biên dịch của bạn sẽ gặp lỗi.
Bạn muốn thêm các tùy chọn khác cho dòng chữ của bạn đẹp hơn. Vui lòng tra cứu
thêm pgfmanual.pdf

### VI.6 Shadings

Thư viện giúp bạn tô màu, pha trộn màu hoàn hảo hơn. Với thư viện này bạn hoàn
toàn có thể tùy biến tô màu khá đẹp và đảm bảo tính phức tạp của miền được tô màu.
Chúng ta có một số tùy chọn:
• top color: Màu trên đỉnh.
• bottom color: Màu dưới chân.
• middle color: Màu ở giữa.
• left color: Màu bên trái.
• right color: Màu bên phải.
• ball color: Tô màu dạng cầu.
• lower left: Góc trái bên dưới.
• upper left: Góc trái bên trên.
• upper right: Góc phải bên trên.
• lower right: Góc phải bên dưới.
• color wheel: Dạng đĩa màu.
• inner color: Tô từ trong ra.
• outer color: Tô từ ngoài vào.
Với các tùy chọn trên, bạn cần nhập tên màu với mỗi tùy chọn để kiểm chứng và
học hỏi. Tất nhiên bạn có thể phối trộn cùng lúc vài ba tùy chọn để việc tô màu của
bạn hoàn hảo hơn.

```latex
\begin{tikzpicture}
\fill[ball color=red] (0,0) circle
(1);
\shade[top color=blue,bottom
color=orange,middle color=white]
(2,-1) rectangle (6,1);
\end{tikzpicture}
\begin{tikzpicture}
\fill[lower left=red,upper
right=pink] (0,0) circle (1);
\shade[shading=color wheel] (2,-1)
rectangle (6,1);
\end{tikzpicture}
\begin{tikzpicture}
\fill[outer color=blue] (0,0)
circle (1);
\shade[inner color=yellow] (2,-1)
rectangle (6,1);
\end{tikzpicture}
```

Chắc rằng với vài ba ví dụ trên, bạn sẽ rút ra việc sử dụng các tùy chọn để tô màu
hình vẽ của mình cho hợp lý.
Tất nhiên rằng Tikz còn có nhiều thư viện khác, nếu bạn cần bạn hãy tra cứu để
biết thêm. Một vài thư viện tôi liệt kê trên đây chỉ là những thư viện thường dùng nhất
khi vẽ hình mà thôi.
