# Các tuỳ chọn thường dùng cho đường và node

> Trích từ `HocTikztheocachcuaBan_BuiQuy.pdf`, trang 25–26.

---

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
