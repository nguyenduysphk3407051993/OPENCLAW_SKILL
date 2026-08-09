# Đường tròn, ellipse, cung và các dạng đường cong

> Trích từ `HocTikztheocachcuaBan_BuiQuy.pdf`, trang 11–15.

---

```latex
\begin{tikzpicture}
\draw[gray!50,thin,opacity=.5]
(-1,-1) grid (5,5);
\path
(0:0) coordinate (A)
(2,1) coordinate (B)
(3,4) coordinate (C)
(4,1) coordinate (D)
;
\draw (A)--(B)--++(1,3)--++(1,-3);
\foreach \x/\g in
{A/180,B/120,C/90,D/0}
\fill[black](\x) circle (1pt)
($(\x)+(\g:3mm)$) node{\x};
\end{tikzpicture}
```

A
B
C
D
• Dùng [turn]: Khi ta vẽ đoạn thẳng từ điểm A đến điểm B rồi, ta muốn vẽ tiếp
đến điểm C xác định bằng cách quay một góc ϕ và độ dài BC = d nào đó ta dùng
[turn] theo cú pháp:

```latex
\draw (A)--(B)--([turn]góc:độ dài);
```

Chẳng hạn trong ví dụ vẽ tam giác đều cạnh 2 ta có thể dùng [turn] như sau:

```latex
\begin{tikzpicture}
\draw[gray!50,thin,opacity=.5]
(-1,-1) grid (5,5);
\draw (0,0)coordinate (A)
--(2,0) coordinate(B)
--([turn]120:2) coordinate(C)
--cycle;
\foreach \x/\g in {A/180,B/0,C/90}
\fill[black](\x) circle (1pt)
($(\x)+(\g:3mm)$) node{\x};
\end{tikzpicture}
```

A
B
C
Như vậy, ta hoàn toàn có thể rút ngắn các lệnh vẽ bằng việc kết hợp nhiều cách vẽ
đoạn thẳng để có một đường gấp khúc tùy ý.

### I.2.9 Đường tròn, Ellipse. Cung tròn, cung Ellipse

Ta biết lệnh vẽ đường tròn là

```latex
\draw (Tâm) circle (bán kính); . Tuy nhiên, để
```

vẽ đường tròn khi biết tâm A và đi qua điểm B thì làm thế nào? Thực tế trong pgf
có lệnh lấy khoảng cách giữa hai điểm, tất nhiên khoảng cách này tính bằng đơn vị pt
(điểm ảnh) nên khó trong việc tính toán. Vấn đề tạo lệnh lấy khoảng cách giữa hai điểm
bằng thông số phù hợp với đơn vị của Tikz ta sẽ đề cập sau. Nhưng để vẽ đường tròn
biết tâm và đi qua một điểm ta có thể dùng lệnh:

```latex
\draw (I) let \p1=($(I)-(A)$) in circle ({veclen(\x1,\y1)});
```

Khi đó ta có đường tròn tâm I và đi qua điểm A.
Như vậy ta cũng có lệnh tương tự để vẽ Ellipse có bán trục lớn a, bán trục nhỏ b và
tâm I(xI; yI) như sau:

```latex
\draw (I) ellipse ({a} and {b});
```

Ngoài ra, ta có thể vẽ các cung tròn, cung Ellipse nếu biết điểm xuất phát cung,
điểm kết thúc cung (tính bằng góc) và các bán kính tương ứng của nó.

`\draw (A) arc (g1:g2:r);`

sẽ vẽ Từ điểm A một cung tròn có góc xuất phát là
g1, góc kết thúc là g2 và bán kính r. Ví dụ dưới đây vẽ từ gốc tọa độ một cung tròn
xuất phát từ góc 180 độ đến góc kết thúc 90 độ với bán kính bằng 2.

```latex
\begin{tikzpicture}
\draw[gray!50,thin,opacity=.5]
(-1,-1) grid (5,5);
\draw (0,0) arc (180:90:2);
\end{tikzpicture}
```

Tương tự, nếu dùng lệnh

```latex
\draw (A) arc (180:0:{2} and {1});
```

sẽ được cung
Ellipse từ điểm A với góc xuất phát là 180 độ, góc kết thúc 0 độ bán trụ lớn là 2 và bán
trục nhỏ là 1.

```latex
\begin{tikzpicture}
\draw[gray!50,thin,opacity=.5]
(-1,-1) grid (5,5);
\draw (0,0) arc (180:90:2);
\draw (0,0) arc (180:0:{2} and {1});
\end{tikzpicture}
```

### I.2.10 Các dạng đường cong khác

• to[tùy chọn]: Vẽ một đường cong từ điểm A đến điểm B với tùy chọn nào đó. Ta
có các loại tùy chọn bend left, bend right hoặc out, in.

```latex
\draw (A) to[bend left=30] (B);
```

cho ta một đường cong từ A đến B sao
cho góc đi ra của đường cong từ điểm A là 30◦ và góc đi vào của đường cong tại
điểm B là 180◦ − 30◦ = 150◦. Đường cong này sẽ cân xứng cả hai phía đối với A và
B. Chú ý rằng bend right cũng giống như vậy nhưng đường cong sẽ đảo ngược
lại. Ta hãy xem ví dụ sau:

```latex
\begin{tikzpicture}
\draw[gray!50,thin,opacity=.5]
(-1,-1) grid (5,5);
\path (0,0) coordinate (A) (4,3)
coordinate (B);
\draw[blue] (A)to[bend left=150]
(B);
\draw[red] (A)to[bend right=30]
(B);
\foreach \x/\g in
{A/-150,B/60}\fill[black]
(\x) circle (1pt)
($(\x)+(\g:3mm)$)node{$\x$};
\end{tikzpicture}
```

A
B
Ta cũng có thể dùng tùy chọn out, in để xác định các góc ra tại điểm A và góc
vào tại điểm B của đường cong. Cách dùng này cho ta thấy các góc ra, vào không
cân xứng:

```latex
\begin{tikzpicture}
\draw[gray!50,thin,opacity=.5]
(-1,-1) grid (5,5);
\path (0,0) coordinate (A) (4,3)
coordinate (B);
\draw[blue] (A)to[out=90,in=30]
(B);
\draw[red] (A)to[out=0,in=90] (B);
\foreach \x/\g in
{A/-150,B/60}\fill[black]
(\x) circle (1pt)
($(\x)+(\g:3mm)$)node{$\x$};
\end{tikzpicture}
```

A
B
Như vậy, tùy thuộc vào tính chất của đường cong để ta có thể lựa chọn tùy chọn
phù hợp cho hình vẽ của mình.
• Parabola[tùy chọn]: vẽ một đoạn Parabol từ điểm A đến điểm B. Tùy chọn
bend at end hoặc không chọn gì. Hoặc ta cũng có thể dùng parabola bend với
ba điểm A, B, C. Khi đó ta được đoạn Parabol xuất phát từ A, đỉnh B và kết thúc
ở C
Ta xem ví dụ sau để hiểu rõ tùy chọn bend at end:

```latex
\begin{tikzpicture}
\draw[gray!50,thin,opacity=.5]
(-1,-1) grid (5,5);
\path (0,0) coordinate (A) (2,3)
coordinate (B);
\draw [blue](A) parabola (B);
\draw[red] (A) parabola[bend at
end] (B);
\foreach \x/\g in
{A/-150,B/60}\fill[black]
(\x) circle (1pt)
($(\x)+(\g:3mm)$)node{$\x$};
\end{tikzpicture}
```

A
B
Và ví dụ dưới đây để hiểu về parabola bend

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
