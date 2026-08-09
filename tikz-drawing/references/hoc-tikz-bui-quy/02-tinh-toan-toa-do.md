# Tham số, hàm tính toán và phép toán trên toạ độ

> Trích từ `HocTikztheocachcuaBan_BuiQuy.pdf`, trang 6–8.

---

### I.2.2 Các lệnh cơ bản của Tikz

Với Tikz có các lệnh vẽ cơ bản sau:
1. Lệnh vẽ đường:

`\draw[tùy chọn] Nội dung vẽ;`

2. Lệnh đưa đầu bút vẽ đến vị trí nào đó:

```latex
\path (Tọa độ điểm) Nội dung làm việc ;
```

3. Lệnh tô màu:

`\fill[tùy chọn] miền tô màu;`

Tất nhiên trong Tikz còn một số lệnh khác, nhưng khi vẽ các hình thông thường ta
chỉ cần sử dụng ba lệnh trên là đủ.

### I.2.3 Khai báo điểm, tham số

Khi vẽ hình ta có những điểm cần sử dụng nhiều lần, các thông số cần sử dụng nhiều
làm và các số liệu tính toán. Yêu cầu này buộc ta cần khai báo tên các điểm và giá trị
của các tham số (hiểu đơn giản là một cách viết tắt cho những đoạn lệnh dài hơn).
• Khai báo điểm có tọa độ cho trước:

```latex
\coordinate[tùy chọn] (Tên điểm) at (Tọa độ);
\coordinate[label=above:A] (A) at (1,2); sẽ khai báo cho ta điểm A(1; 2)
```

và khi vẽ điểm A Tikz sẽ tự động thêm nhãn của điểm là A ở phía trên của điểm.
`\coordinate (A) at (30:2);` sẽ khai báo cho ta điểm A(30 : 2) và không thêm
nhãn của điểm.
• Gán giá trị cho tham số:
`\def\a{3}` : Gán cho tham sốa giá trị3 (hiểu là cho a = 3). Khi dùng đến giá
trị này trong Tizk chỉ cần gọi
`\a` .
`\pgfmathsetmacro\a{2*sqrt(2)}` : Gán cho tham sốa giá trị2
√
2. Chú ý khi
gán giá trị cho tham số, dùng

`\def`

khi gán một giá trị là một số cụ thể (không
tính toán thông qua các phép tính) còn nếu buộc phải tính toán qua các phép tính
thì dùng

`\pgfmathsetmacro .`

### I.2.4 Các hàm tính toán số liệu cơ bản

Một số hàm tính toán trong Tikz
• sin (α): Trả về giá trị sin α.
• cos (α): Trả về giá trị cos α.
• tan (α): Trả về giá trị tan α.
• asin (b): Trả về giá trị arcsin b.
• pow (α,a): Trả về giá trị aα.
• ln (a): Trả về giá trị ln a.
• exp (α): Trả về giá trị eα.
• loga (b) : Trả về giá trị loga b.
• sqrt (a): Trả về giá trị √a.
• abs(a): Trả về giá trị tuyệt đối của a.
• int (a): Trả về phần nguyên của số a.
Ngoài ra, các phép tính toán thông thường: cộng, trừ, nhân, chia, lũy thừa dùng các
ký hiệu tương ứng

`+,-,*,/,^ .`

### I.2.5 Các phép toán đối với tọa độ

• Cộng tọa độ: Nếu ta có điểm A(xA, yA) và điểm B(xB, yB). Khi đó ta có tọa độ
điểm C(xA + xB, yA + yB) bằng cách khai báo:

```latex
\coordinate (C) at ($(A)+(B)$);
```

• Điểm chia tỉ lệ đoạn thẳng (Phép vị tự): Ta có hai điểm A và B. Lấy điểm
C sao cho AC
AB = k ta khai báo:

```latex
\coordinate (C) at ($(A)!k!(B)$);
```

Như vậy, hoàn toàn ta có thể lấy trung điểm đoạn thẳng AB bằng cách

```latex
\coordinate (M) at ($(A)!.5!(B)$);
```

• Phép quay: Muốn lấy điểm B là ảnh của điểm A qua phép quay tâm I, góc quay
ϕ ta có thể dùng:

```latex
\coordinate (A) at ($(I)!1!góc quay:(B)$)
```

Chẳng hạn lấy điểm A là ảnh của B qua phép quay tâm I, góc quay 30◦ ta dùng:

```latex
\coordinate (A) at ($(I)!1!30:(B)$);
```

Hơn thế nữa, ta có thể kết hợp phép quay và phép vị tự bằng lệnh:
`\coordinate (A) at ($(I)!k!30:(B)$)` . Khi đó ta được điểm A là ảnh của B
qua việc thự hiện liên tiếp phép quay tâm I, góc quay 30◦ và phép vị tự tâm I tỉ
số k.
• Lấy chân đường vuông góc: Lấy điểm chân đường vuông góc kẻ từ A đến cạnh
BC

```latex
\coordinate (H) at ($(B)!(A)!(C)$);
```

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
