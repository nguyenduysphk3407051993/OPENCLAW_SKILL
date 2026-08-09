# Export hình ảnh, làm ảnh động PDF và GIF

> Trích từ `HocTikztheocachcuaBan_BuiQuy.pdf`, trang 61–70.

---

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
• Bước 2: Khi cài xong ImageMagick, bạn vào thư mục cài đặt ImageMagick và tìm
đến file convert.exe và đổi tên file này thành imgconvert.exe
• Bước 3: Cài đặt Ghostscript.
• Bước 4: Cấu hình Configuration. Bạn thay thế dòng pdflatex trong Configuration
từ pdflatex -synctex=1 -interaction=nonstopmode %.tex
thành: pdflatex -synctex=1 -shell-escape -interaction=nonstopmode %.tex
• Bước 5: Thêm tùy chọn vào khai báo lớp văn bản:

```latex
\documentclass[tikz,border=1mm,convert={outfile=\jobname.png}]{standalone}
```

Trong đó bạn có thể thay định dạng file ảnh mà bạn muốn như jpg, svg . . .
• Bước 6: Nhấn biên dịch và hưởng thành quả.
Bạn cũng cần chú ý rằng cách thiết lập này hoàn toàn hiệu quả với các trình soạn
thảo như TexMaker và Texstudio. Riêng với Vietex thì tôi chưa tìm ra cách cấu
hình cho phù hợp mặc dù cũng đã từng thử qua. Tất nhiên bạn có thể cài song song vài
trình soạn thảo trên máy tính vì những trình soạn thảo này không hề làm tăng dung
lượng đáng kể cho máy tính của bạn (khoảng vài chục Mb với mỗi trình soạn thảo thì
quá đơn giản).

### V.2 Làm ảnh động trực tiếp trên PDF

Bạn muốn tạo những ảnh động trên file PDF trực tiếp bằng Tikz? Bạn hãy dùng
gói animate. Trước hết bạn gọi gói lệnh làm ảnh động bằng việc sử dụng
`\usepackage{animate}` . Sau đó là bạn tạo code vẽ.
Cấu trúc của code bao gồm:

```latex
\begin{animateinline}[controls,autoplay,loop]{s hình/giây}
\multiframe{\n}{i=0+1}{
\begin{tikzpicture}
..........................
...Lnh v hình...
..........................
\end{tikzpicture}
}
\end{animateinline}
```

Một vài tùy chọn của môi trường animate:
• controls: Hiển thị bảng điều khiển (play,pause, stop . . . )
• outoplay: Hình tự động chạy khi mở file PDF.
• loop: Chạy lặp đi lặp lại không dừng.
• palindrome: Chạy xuôi, ngược.
• số hình/giây: là một con số cụ thể quy định sự nhanh/chậm của chuyển động
hình ảnh.
• multiframe: Biến chạy i chạy từ 0 đến n theo quy luật i = i + 1
Trong phần lệnh vẽ hình, nếu code hình của bạn không có sự tham gia của biến i
thì hình vẽ của bạn sẽ luôn đứng yên (tác động của sự thay đổi biến i làm cho thay đổi
hình ảnh).
Ngoài ra bạn cần chú ý rằng, khi tạo ảnh động do việc thay đổi hình ảnh nên khung
hình sẽ có sự thay đổi. Khi đó bạn muốn ảnh chạy mà khung hình đứng yên bạn cần
khéo léo clip khung hình ngay trước tất cả các lệnh vẽ. Tôi sẽ làm một ví dụ đơn giản
như sau:

```latex
\begin{animateinline}[controls,autoplay,loop,palindrome]{5}
\multiframe{90}{i=0+1}{
\begin{tikzpicture}
\clip (-10:3) arc (0:190:3)--cycle;
\draw[-stealth,thick] (180:2.5)--(0:2.5);
\draw[-stealth,thick] (0:0)--(90:2.5);
\draw[blue,thick] (0:2) arc (0:2*\i : 2);
\end{tikzpicture}
}
\end{animateinline}
```

và ta sẽ được một ảnh động vẽ nửa đường tròn bán kính 2 đơn vị:
Bạn muốn xem được hình động trực tiếp trên PDF thì bạn cần phải cài đặt Adobe
AcrobatReader nhé. Các trình xem PDF khác không hỗ trợ bạn điều này.

### V.3 Làm ảnh động gif để upload lên web

Ngoài việc bạn làm ảnh động chạy trực tiếp trên file PDF, bạn có thể nhờ vào
ImageMagick để tạo ảnh động định dạng gif mà bạn thường thấy trên web.
Về bản chất ảnh gif chỉ là tập hợp các tấm ảnh xuất hiện liên tục. Do đó bạn cần
tạo nhiều ảnh liên tục rồi nhờ ImageMagick tạo ảnh gif cho bạn mà thôi. Như vậy
trước hết bạn cần tạo một file PDF có nhiều trang, mỗi trang là một hình ảnh, từ đó
bạn dùng lệnh convert của ImageMagick.
Để tạo một file PDF có nhiều trang liên tục, chẳng hạn như hình bạn vừa vẽ, bạn
sẽ có code như sau:

```latex
\documentclass[tikz,border=5mm]{standalone}
\begin{document}
\foreach \i in {0,...,90}{
\begin{tikzpicture}
\clip (-10:3) arc (0:190:3)--cycle;
\draw[-stealth,thick] (180:2.5)--(0:2.5);
\draw[-stealth,thick] (0:0)--(90:2.5);
\draw[blue,thick] (0:2) arc (0:2*\i : 2);
\end{tikzpicture}
}
\end{document}
```

Khi bạn biên dịch file này, bạn sẽ có một file PDF gồm 90 trang, mỗi trang là một
hình ứng với một giá trị của biến i. Bây giờ bạn hãy đặt nó ở đâu đó trong máy tính và
mở cmd của windown lên (Nhấn nút start rồi chọn run, gõ cmd). Bạn sẽ có cửa sổ cmd
như sau:
Bạn sử dụng dòng lệnh sau:

```latex
imgconvert convert -density 300 -delay 10 -alpha remove Duong dan den file
pdf Duong dan den file gif
```

Trong dòng lệnh trên, ta thấy một vài thông số cần hiểu:
• imgconvert convert: Lệnh chuyển đổi.
• -density 300: Chất lượng hình ảnh, thông thường để con số 300 là hợp lý. Con
số này càng lớn thì thời gian convert càng lâu đồng nghĩa với chất lượng hình ảnh
càng tốt.
• -delay 10: Thời gian chuyển hình ảnh (độ trễ). Như ở đây cứ 10/100 giây sẽ
chuyển một hình. Con số càng tăng thì hình càng chạy chậm và ngược lại.
• -alpha remove: Lệnh tạo gif và xóa bỏ những thiết đặt tạm sau khi chuyển đổi.
Khuyến cáo không thay đổi chỗ này.
• Đường dẫn đến file pdf: Chẳng hạn tôi đặt file Hinh01.pdf của tôi trong thư
mục Hinhgif của ổ D thì tôi sẽ đặt đường dẫn này là:

`D:\HinhGif\Hinh01.pdf`

• Đường dẫn đến file hình gif: Tương tự, tôi muốn convert file Hinh01.pdf
thành Hinh01.gif và đặt vào cùng thư mục file PDF thì tôi sẽ đặt đường dẫn này
là:

`D:\HinhGif\Hinh01.gif`

Vậy là tôi có thể đặt một dòng lệnh như sau:

```latex
imgconvert convert -density 300 -delay 10 -alpha remove D:\HinhGif\Hinh01.pdf
D:\HinhGif\Hinh01.gif
```

Xong xuôi việc đặt lệnh. Việc còn lại là copy dòng lệnh này vào cmd và nhấn Enter.
Chờ đợi cho đến khi cmd làm việc xong thì ta sẽ có một file ảnh gif để sử dụng.
Lời khuyên cho bạn là việc nhớ dòng lệnh trên khá khó nên bạn cứ copy rồi dán
dòng lệnh trên vào một file txt rồi lưu lại chỗ thuận tiện, khi muốn tạo hình gif thì mở
ra thay đổi thông số cho phù hợp yêu cầu rồi copy, paste cho khỏi dính lỗi sai lệnh.

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
