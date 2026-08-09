# Vẽ hình không gian (giả 3D)

> Trích từ `HocTikztheocachcuaBan_BuiQuy.pdf`, trang 30–33.

---

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

```latex
\begin{tikzpicture}
\def\a{2}
\def\b{1}
\def\h{3}
\draw[dashed] (180:\a) arc
(180:0:{\a} and {\b});
\draw (-\a,\h)--(-\a,0) arc
(180:360:{\a} and {\b})--(\a,\h)
(90:\h) ellipse ({\a} and {\b});
\end{tikzpicture}
```

Bạn muốn một hình hộp chữ nhật?

```latex
\begin{tikzpicture}
\def\a{3}
\def\b{1}
\def\g{30}
\def\h{2}
\path
(0:0) coordinate (A)
--++(\g:\b) coordinate (B)
--++(0:\a) coordinate (C)
--++(\g-180:\b) coordinate (D)
\foreach
\x in {A,B,C,D}{
($(\x)+(90:\h)$) coordinate (\x
')}
;
\draw[dashed] (B')--(B)--(A)
(B)--(C);
\draw
(A)--(D)--(D')--(A')--cycle
(A')--(B')--(C')--(D')
(D)--(C)--(C')
;
\end{tikzpicture}
```

Bạn muốn một hình cầu:

```latex
\begin{tikzpicture}
\def\r{2}
\draw[dashed]
(180:\r) arc (180:0:{\r} and
{.3*\r})
(90:\r) arc (90:-90:{.3*\r} and
{\r})
;
\draw
(0:0) circle (\r)
(180:\r) arc (180:360:{\r} and
{.3*\r})
(90:\r) arc (90:270:{.3*\r} and
{\r})
;
\end{tikzpicture}
```

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
