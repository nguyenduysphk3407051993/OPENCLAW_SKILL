# Vẽ điểm, hiển thị văn bản, đoạn thẳng và đường gấp khúc

> Trích từ `HocTikztheocachcuaBan_BuiQuy.pdf`, trang 8–11.

---

• Giao điểm của hai đường thẳng: Giao điểm của hai đường thẳng đi qua AB
và CD

```latex
\coordinate (M) at (intersection of A--B and C--D);
```

### I.2.6 Hiển thị văn bản trong Tikz

Hiển thị tên điểm khi chưa khai báo label:

```latex
\node[tùy chọn] (Tên điểm) at (Tọa độ điểm){Nội dung hiển thị};
```

Với lệnh trên, Tên điểm là tên khai báo của node (dùng để sau này ta vẽ thêm các
đối tượng khác liên quan đến node). Nội dung hiển thị nội dung văn bản ta cần hiển
thị trong hình vẽ.
Ví dụ:

```latex
\begin{tikzpicture}
\node[circle,fill=yellow,draw] (A)
at (0,0){Điểm A};
\node[rectangle,fill=blue!30,draw]
(B) at (4,0){Điểm B};
\draw[->] (A)--(B);
\end{tikzpicture}
```

Điểm A
Điểm B
Chú ý rằng coordinate và node có thể dùng bất cứ chỗ nào (trong các lệnh`\draw` ,

`\fill`

hoặc

`\path ).`

### I.2.7 Vẽ Điểm

Ta xác định một điểm trên hình vẽ bằng tọa độ. Trên hệ Oxy ta xác định điểm bằng
tọa độ (x; y). Còn trên hệ tọa độ cực ta xác định điểm bằng (α : r).
Ví dụ ta muốn vẽ điểm A(3; −1) ta dùng lệnh sau:`\draw (3,-1) circle (1pt);`
Chú ý rằng tọa độ của điểm trong Tikz ngăn cách hoành độ và tung độ bởi dấu
"phẩy" (,) chứ không phải dấu "chấm phẩy" (;) như ta thường viết trong văn bản. Kết
thúc lệnh vẽ luôn bằng dấu "chấm phẩy" (;).
Ta cũng có thể vẽ điểm bằng lệnh`\draw (60:2) circle (1pt);` . Khi đó ta sẽ vẽ
được điểm B sao cho OB = 2 và góc giữa OB và Ox là 60o.
Hãy xem ví dụ dưới đây:

```latex
\begin{tikzpicture}[>=stealth]
\draw[step=1,gray,very thin]
(-3,-3) grid (3,3);
\draw[->](-3,0)--(3,0);
\draw[->](0,-3)--(0,3);
\draw[dashed] (0,1)--(2,1)--(2,0);
\draw (2,1) circle (0.04);
\draw (3,0) node[above]{$x$} (0,3)
node[left]{$y$} (0,0) node[below
left]{$O$};
\draw (-60:2) circle (0.04);
\draw (-60:2) -- (0,0);
\draw (2,1) node[above right]{$A$}
(-60:2) node[below right]{$B$};
\draw[->](-60:4mm) arc (-60:0:4mm);
\draw (-30:5mm)node[below
right]{$-60^{o}$};
\end{tikzpicture}
```

x
y
O
A
B
−60o
Chú ý rằng lệnh vẽ điểm là

```latex
\draw (point) circle (radius);
```

trong đó point
là tọa độ điểm và radius là bán kính điểm (thường dùng là 1pt hoặc 2pt).

### I.2.8 Đoạn thẳng, đường gấp khúc

Chúng ta biết rằng để vẽ đoạn thẳng từ A đến B ta dùng lệnh

`\draw (A)--(B); .`

Tuy nhiên, nếu vẽ một đường gấp khúc từ A đến B rồi đến C tiếp tục đến D thì ta có
thể dùng lệnh ròi rạc từng đoạn. Như vậy sẽ gây khó khăn vì phải gõ nhiều ký tự. Ta
có một số cách sau đây để vẽ một đường gấp khúc:
• Dùng liên tiếp –: Ta có thể dùng

`\draw (A)--(B)--(C)--(D);`

Cách dùng này thường được dùng khi ta đã khai báo (hoặc biết tọa độ) tất cả 4
điểm A, B, C, D. Ví dụ:

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
\draw (A)--(B)--(C)--(D);
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
• Dùng –++: Chẳng hạn ta mới có điểm A và B và biết rằng điểm C có tọa độ
dạng C(xB + xo; yB + yo), khi đó ta sẽ dùng lệnh cộng tọa độ:

`\draw (A)--(B)--++(xo,yo);`

Cái hay của Tikz là việc cộng tọa độ này sẽ được cộng dồn. Sau khi vẽ đến C theo
như lệnh trên ta hoàn toàn có thể tiếp tục vẽ thêm đoạn thẳng cộng tiếp tọa độ
từ điểm C đến điểm D
Cũng như trên, ta thấy điểm C(3, 4) = (2 + 1; 1 + 3), như vậy C(xB + 1; yB + 3) và
tương tự D(xC + 1; yC − 3). Ta sẽ dùng lệnh vẽ:

```latex
\draw (A)--(B)--++(1,3)--++(1,-3);
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
