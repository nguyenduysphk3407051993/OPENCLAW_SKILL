# Vòng lặp foreach và cách tạo macro

> Trích từ `HocTikztheocachcuaBan_BuiQuy.pdf`, trang 26–30.

---

toán của Tikz sẽ tăng lên làm chậm quá trình biên dịch. Khuyên dùng với thông
số samples=100 là vừa phải (1 đơn vị được chia thành 100 điểm nhỏ).
• ->: Dùng vẽ các đoạn thẳng (đoạn cong) có định hướng (mũi tên ở cuối đoạn).
Các kiểu mũi tên thường dùng là stealth, latex, . . . .
• opacity=: Tùy chọn này chỉ định độ hòa trộn giữa các lớp đối tượng (layer) trong
một hình vẽ. Giống như các phần mềm làm việc với hình ảnh khác, Tikz vẽ hình
theo các lớp, lớp sau đè lớp trước, opacity sẽ hòa trộn các đối tượng vào với nhau.
Thường dùng với

`\fill`

• double: Tùy chọn vẽ nét đôi trong lệnh vẽ`\draw` . Ta hoàn toàn có thể tùy chỉnh
khoảng cách giữa các nét đôi bằng tùy chọn double distance
• rounded corrners=: Tùy chọn làm mềm độ gấp khúc của lệnh

`\draw`

và

`\fill`

Ta hoàn toàn có thể dùng cùng lúc các tùy chọn này, Tikz sẽ thực hiện lần lượt từng
tùy chọn cho đến hết khi vẽ hình. Chú ý với các tùy chọn về các phép quay, tịnh tiến,
vị tự (rotate, shift, scale) khi dùng trong lệnh

`\draw`

hoặc

`\fill`

sẽ không thực
hiện nếu các điểm đã được định nghĩa từ trước.

### I.3.2 Với node, pic

Với pic và node ngoài những tùy chọn chung còn có một số tùy chọn riêng.
pic[local bounding box=A] ... là tùy chọn để khai báo vị trí đặt pic là A, dùng
để vẽ các đường nối các điểm một cách hợp lý.
sloped: Dùng với node khi ta node theo một đường nào đó (có thể cong hoặc thẳng).
Khi đó văn bản trong node sẽ nghiêng theo độ nghiêng của đường.
midway: Dùng với node như trên, vị trí đặt của node sẽ ở giữa đường đó. Thường
dùng khi đặt các khoảng cách giữa hai điểm.
Ngoài ra, còn rất nhiều tùy chọn khác trong các lệnh của Tikz mà tôi chưa liệt kê
ở đây, bởi nó ít được dùng. Bạn hoàn toàn có thể tra cứu pgfmabual.pdf có đầy trên
internet.

### I.3.3 Vòng lặp foreach

Vòng lặp foreach thực chất là lệnh của LATEX. Nhưng nó rất hữu dụng khi vẽ hình
bằng Tikz. Ta có thể hiểu vòng lặp này như sau:

```latex
\foreach tên biến in {tập hợp biến} {lệnh thực thi;}
```

Việc sử dụng foreach tiết kiệm cho ta việc gõ quá nhiều dòng lệnh giống nhau, chỉ
thay đổi một vài thông số. Chẳng hạn bạn muốn vẽ 20 đoạn thẳng song song và cùng
có độ dài bằng 2 từ các điểm trên trục tung, có tung độ tăng dần .1 đơn vị. Nếu bạn
vẽ lần lượt thì phải gõ đúng 20 dòng lệnh`\draw (...)--++(0:2);` Nhưng với foreach
bạn chỉ cần một dòng lệnh, Tikz (thực chất là LATEX) sẽ thay bạn làm việc đó:

```latex
\begin{tikzpicture}
\foreach \i in {1,...,20}\draw
(0,.1*\i)--++(0:2);
\end{tikzpicture}
```

Ở đây, ta thấy hoành độ luôn là 0, tung độ sẽ tăng dần, với i = 1 thì tung độ là
.1, với i=2 thì tung độ là .2, . . . Bạn thấy cú pháp chỗ lệnh thực thi ở trên được đặt
trong ngoặc nhọn còn trong ví dụ thì không? Nếu như chỉ cần làm một việc duy nhất
(một lệnh duy nhất) thì không cần cặp ngoặc nhọn đó, nhưng nếu từ hai lệnh trở lên
bạn cần phải có ngoặc nhọn, nếu không foreach chỉ thực thi cho bạn một lệnh đầu tiên
liền sát nó mà thôi.
foreach còn hơn thế, ta có thể dùng vòng lặp này lồng nhau để vẽ (hiển thị một
bảng). Chẳng hạn:

```latex
\begin{tikzpicture}
\foreach \i in {1,...,7}{
\foreach \j in {1,...,5}
\path (\i,\j) node{$a_{\i \j}$};
}
\end{tikzpicture}
```

a11
a12
a13
a14
a15
a21
a22
a23
a24
a25
a31
a32
a33
a34
a35
a41
a42
a43
a44
a45
a51
a52
a53
a54
a55
a61
a62
a63
a64
a65
a71
a72
a73
a74
a75
Quả là tiện lợi, nếu không dùng foreach bạn sẽ phải dùng 35 node với 35 tọa độ
và 35 văn bản. Tất nhiên, khi dùng foreach bạn cần chú ý đến những công thức mang
tính tổng quát. Chẳng hạn, cũng bảng trên nhưng tôi muốn hiển thị aij = ß +  thì tôi
sẽ làm:

```latex
\begin{tikzpicture}
\foreach \i in {1,...,7}{
\foreach \j in {1,...,5}
\pgfmathsetmacro{\ht}{int(\i+\j)}
\path (\i,\j) node{\ht};
}
\end{tikzpicture}
```

2
3
4
5
6
3
4
5
6
7
4
5
6
7
8
5
6
7
8
9
6
7
8
9
10
7
8
9
10
11
8
9
10
11
12
Tiếp tục nghiên cứu về foreach. Trong cái tập hợp biến ta có thể có nhiều cách
đưa vào. Chẳng hạn với giá trị biến là các con số có quy luật (chẳng hạn các số cách
đều nhau như ở ví dụ trên) thì ta nhập vào dạng

`.1,.3,...,5`

sẽ được danh sách là
.1, .3, .5, .7 . . . 5 sao cho các biến cách nhau .2. Còn nếu là các số nguyên thì chỉ cần
nhập vào số đầu tiên và số cuối cùng như trong ví dụ. Nếu các giá trị biến không có
quy luật hoặc định dạng không phải các con số thì sao? Ta buộc phải liệt kê các giá trị
biến trong đó.
Vậy còn tên biến? Bạn có thể đặt tên biến một cách thoải mái, hơn nữa ta có thể
dùng nhiều biến cùng lúc như ví dụ dưới đây:

```latex
\begin{tikzpicture}
\foreach \x/\col in {1/red, 2/blue,
3/orange, 4/pink, 5/yellow,
6/gray} \fill[\col] (\x,0)
rectangle +(.5,2);
\end{tikzpicture}
```

### I.3.4 Tạo macro

Macro là gì? Nó là một lệnh do người dùng tạo ra, bản chất là để thực hiện một
tập hợp các lệnh của LATEX theo kiểu “gõ tắt” trên word bằng Unikey mà thôi. Cú pháp
tạo lệnh:

`\def \name{Các lệnh thực thi}`

Như vậy, bạn có thể đặt name thoải mái, miễn sao đừng trùng với các lệnh có sẵn
của LATEX và Tikz để khỏi gây lỗi.
Phần lệnh thực thi bạn có thể đưa vào bất cứ lệnh vẽ nào của Tikz. Và khi nào
sử dụng đến tập hợp các lệnh đó bạn chỉ việc

`\name`

là xong.
Tất nhiên nếu chỉ có thế thì tạo macro cũng không tiện lợi mấy. Macro còn có thể
đưa thông số đầu vào và thông số đầu ra. Chẳng hạn với macro tạo lệnh vẽ ký hiệu góc
vuông và ký hiệu góc thường mà tôi đã từng tạo:

```latex
\begin{tikzpicture}
\def\khvuong(#1,#2,#3){
\path
($(#2)!2mm!(#1)$) coordinate (#2#1)
($(#2)!2mm!(#3)$) coordinate (#2#3)
;
\draw[blue] (#2#1)
--($(#2#1)+(#2#3)-(#2)$)--(#2#3);
}
\def\khgoc(#1,#2,#3){
\begin{scope}
\clip (#1)--(#2)--(#3);
\draw[red] (#2) circle (2mm);
\end{scope}
}
\draw (0,0) coordinate(B)
--(5,0) coordinate (C)
--(1,4) coordinate (A)
--cycle;
\khvuong(B,A,C)
\khgoc(A,B,C)
\end{tikzpicture}
```

Hơn nữa, macro còn lo cho ta cả thông số đầu ra. Chẳng hạn ta muốn tìm tâm nội
tiếp của một tam giác, ta cũng có thể xây dựng một macro như sau:

```latex
\begin{tikzpicture}
\def\tamnoitiep(#1,#2,#3)(#4){
\path
($($(#2)!2mm!(#1)$)!0.5!($(#2)!2mm!(#3)$)$)
coordinate (#2a)
($($(#1)!2mm!(#2)$)!0.5!($(#1)!2mm!(#3)$)$)
coordinate (#1a)
(intersection of #2-- #2a and
#1--#1a) coordinate (#4);
}
\draw (0,0) coordinate(B)
--(5,0) coordinate (C)
--(1,4) coordinate (A)
--cycle;
\tamnoitiep (A,B,C)(I)
\path ($(A)!(I)!(B)$) coordinate
(M);
\draw (I) let \p1=($(I)-(M)$) in
circle ({veclen(\x1,\y1)});
\end{tikzpicture}
```

Như vậy, bạn có thể tự tạo ra các macro để vẽ theo ý bạn và mạch tư duy hình học
của bạn để vẽ mà không mất quá nhiều thời gian. Về bản chất, gói lệnh tkz-euclide
được xây dựng với các ý tưởng như thế này (người ta gọi đó là các gói thứ cấp của
Tikz). Với bộ môn Vật lý hoặc Hóa học cũng có những gói thứ cấp của Tikz như vậy.

### I.3.5 Vẽ hình không gian (giả 3d)

Khi vẽ hình không gian (bản chất là vẽ 2d hình chiếu song song của một hình không
gian trên mặt phẳng), ta thường có một tham số đầu vào là góc nghiêng (góc nhìn
hình). Bạn cần nhắc lại về các quy tắc biểu diễn của một hình không gian trên mặt
phẳng. Bạn hãy nhớ đến các quy tắc về tính song song, tỉ lệ các đoạn thẳng song song
được giữ nguyên. Thêm nữa, bạn cần nhớ đến quy tắc nét liền, nét đứt.
Chẳng hạn bạn muốn biểu diễn một hình tròn, bạn sẽ vẽ một Ellipse. Vậy thì bạn
hoàn toàn có thể biểu diễn một hình trụ đơn giản như sau:
