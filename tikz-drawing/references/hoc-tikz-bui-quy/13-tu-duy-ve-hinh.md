# Tư duy hình hoạ để dựng hình

> Trích từ `HocTikztheocachcuaBan_BuiQuy.pdf`, trang 58–61.

---

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

### IV.2 Lựa chọn hệ tọa độ hợp lý

Việc vẽ hình bằng Tikz là làm việc với các tọa độ (điểm đặt các đối tượng hình ảnh)
và các câu lệnh (lệnh vẽ hình). Như vậy việc lựa chọn hợp lý khi vẽ hình là rất cần thiết.
Với mỗi hình vẽ, bạn cần hình dung vị trí đặt của hình. Vì vậy bạn lựa chọn gốc tọa
độ là điểm nào để thuận tiện điều khiển các tọa độ tiếp theo cũng nên cân nhắc. Mặt
khác, bạn sẽ sử dụng tọa độ Đề-các hay tọa độ cực cũng nên quan tâm. Chẳng hạn bạn
muốn vẽ một tam giác với đường tròn nội (ngoại tiếp) bạn sẽ vẽ như thế nào? Vẽ đường
tròn trước hay tam giác trước? gốc tọa độ nên đặt ở đâu? . . . Với tôi thì tôi sẽ vẽ đường
tròn trước, và tâm đường tròn nằm đúng gốc tọa độ. Ngay lập tức dùng hệ tọa độ cực
thì có ngay ba điểm nằm trên đường tròn là ba đỉnh tam giác nội tiếp đường tròn. Nếu
bạn vẽ đường tròn trước, việc bạn phải đi tìm tâm, bán kính đường tròn ngoại tiếp tam
giác sẽ vất vả hơn. Tất nhiên trong một bài toán tổng hợp nhiều hơn nữa, có thể bạn
vẫn phải lựa chọn vẽ tam giác trước, bởi ba đỉnh tam giác được sinh ra từ việc vẽ các
đường trước đó. Khi ấy bạn sẽ cần đến việc tạo và sử dụng macro.

### IV.3 Sử dụng Macro

Trong nhiều hình vẽ, việc sử dụng các thư viện của Tizk có thể đảm bảo vẽ cho bạn
hầu hết các hình. Nhưng vấn đề lại là những thư viện đó bạn ít khi dùng đến nên việc
nhớ các câu lệnh, các tùy chọn của thư viện không hề đơn giản. Chính vì vậy việc sử
dụng macro hợp lý mặc dù có vẻ rườm rà nhưng lại tiết kiệm nơ ron thần kinh của bạn
một cách đáng kể.
Hoặc hơn nữa, nhiều khi hình vẽ có những đối tượng tương tự nhau, chỉ sai khác
một vài thông số cơ bản. Vậy bạn hãy tạo macro để tùy biến vừa đơn giản lại nhanh
gọn.
Chẳng hạn như trong sơ đồ ở phần trên. Khi vẽ tôi đã hình dung có nhiều khung
chữ cùng loại, điểm khác biệt là màu nền, nội dung chữ, độ lớn khung và điểm đặt nó.
Mặc dù Tikz cũng có thư viện tùy chọn node nhưng không phong phú bằng. Vậy tôi
sẽ nghĩ đến việc tạo macro cho việc này, thông số đầu vào sẽ là tọa độ hiển thị, độ lớn
khung, màu nền và nội dung chữ trong khung . . . . Và tôi đã làm như thế.

### IV.4 Sử dụng vòng lặp foreach

Nếu trong hình vẽ của bạn có nhiều tình huống lặp đi lặp lại, bạn cũng có thể sử
dụng vòng lặp foreach để Tikz thực hiện cho bạn. Sử dụng hợp lý sẽ tiết kiệm thời
gian soạn code vẽ và các chi tiết đảm bảo thống nhất trong một hình vẽ.
Chẳng hạn như bạn muốn vẽ một biểu đồ hình cột, rõ ràng Tikz có tùy chọn ybar
để vẽ biểu đồ cột nhưng không thể linh hoạt như bạn tự vẽ:
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
SK1-1
SK1-2
SK1-3
SK1-4
SK2
H-max
WX
VS
ZJ
Với biểu đồ trên, bạn chỉ cần tư duy một chút là bạn hoàn toàn có thể vẽ hàng loạt
biểu đồ tương tự mà chỉ cần thay đổi một vài thông số.

### IV.5 Kỹ năng tìm kiếm

Không phải lúc nào bạn cũng nhớ được tất cả, có những vấn đề bạn nhớ mang
máng, có những vấn đề bạn chưa từng được nghe đến. Kỹ năng tìm kiếm sẽ giúp bạn
rút ngắn thời gian vẽ hình. Những địa chỉ tìm kiếm tốt nhất khi vẽ hình cho bạn là còn
pgfmanul.pdf và trang web https://tex.stackexchange.com.
Bạn cũng nên chú ý cách tìm kiếm, cần đưa ra những từ khóa mấu chốt cho quá
trình tìm kiếm thu gọn hơn để tiết kiệm thời gian.

### V

### Export hình ảnh

Khi bạn vẽ hình để soạn tài liệu, tài liệu của bạn có nhiều hình vẽ code Tikz sẽ làm
chậm quá trình biên dịch. Vì vậy bạn có thể biên dịch mỗi hình thành một file pdf riêng
để

`\includegraphics`

hình ảnh vào nhằm cải thiện thời gian biên dịch.
Mặt khác, khi bạn cần hình ảnh để upload lên web hoặc insert vào các trình soạn
thảo tài liệu khác (chẳng hạn như MS Word) thì bạn làm như thế nào?

### V.1 Cài đặt ImageMagick và Ghostscript

Bạn cần download ImageMagick và Ghostscript từ Internet về máy tính và cài đặt
một cách bình thường. Bạn có thể vào link sau:
ImageMagick: https://imagemagick.org
Ghostscript https://www.ghostscript.com
Tất nhiên bạn cũng có thể vào Google và seach với các từ khóa ImageMagick và
Ghostscript và bạn sẽ tìm thấy ngay những trang này. Vào đây bạn hãy chọn phiên
bản cho phù hợp với hệ điều hành máy của bạn (32 bit hoặc 64 bit) và cài đặt theo thứ
tự như sau:
• Bước 1: Cài đặt ImageMagick (lưu ý khi cài đặt chọn đầy đủ các tính năng).
