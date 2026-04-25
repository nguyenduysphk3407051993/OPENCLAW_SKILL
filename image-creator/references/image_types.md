# 12 Loại ảnh giáo dục Việt Nam — Cheat Sheet

File này dùng ở **bước 1 và bước 2** để chọn loại ảnh phù hợp. Mỗi loại có **mã TYPE** dùng cho naming convention upload Drive.

## Bảng tra cứu nhanh

| TYPE | Tên Việt | Tỷ lệ ưu tiên | Có text? | Style mặc định |
|---|---|---|---|---|
| INFOGRAPHIC | Infographic giáo dục | Dọc 2:3 | Có (title + nhãn) | Vector flat |
| MINDMAP | Sơ đồ tư duy | Ngang 3:2 | Có (nhánh) | Hand-drawn |
| DIAGRAM | Sơ đồ kỹ thuật | Ngang 3:2 | Có (nhãn) | Technical line |
| ILLUSTRATION | Tranh minh hoạ | Vuông 1:1 | Tuỳ chọn | Watercolor / Cartoon |
| PHOTO | Ảnh chụp | Tuỳ | Không | Photorealistic |
| COMIC | Truyện tranh | Dọc 2:3 | Speech bubble | Manga / Western |
| POSTER | Poster cổ động | Dọc 2:3 | Có (slogan) | Modern minimal |
| BANNER | Banner ngang | Ngang 3:2 | Có (title) | Editorial |
| ICON | Biểu tượng | Vuông 1:1 | Không | Flat icon |
| SCIENTIFIC | Sơ đồ khoa học | Dọc 2:3 | Nhãn khoa học | Textbook scientific |
| WORKSHEET | Hình phiếu BT | Tuỳ | Không (hoặc nhãn rỗng) | Outline đen trắng |
| SLIDE_HERO | Ảnh bìa slide | Ngang 3:2 | Title slide | Magazine cover |

## Chi tiết từng loại

### 1. INFOGRAPHIC

**Khi nào dùng**: Truyền đạt một khái niệm có nhiều thành phần và mối liên hệ. Ví dụ: chu trình nước, quá trình quang hợp, cấu trúc ADN.

**Cấu trúc thường có**:
- Tiêu đề lớn ở trên
- Chủ thể trung tâm (cây, phân tử, cơ thể)
- 4-6 nhánh phụ với nhãn ngắn
- Mũi tên/đường nối thể hiện quan hệ
- Footer (logo trường, môn, lớp) — tuỳ chọn

**Cảnh báo**: gpt-image-2 vẽ infographic rất tốt nhưng nếu **>10 thành phần** sẽ bắt đầu render text sai chính tả. Nên chia thành nhiều ảnh hoặc dùng style đơn giản hơn.

**Ví dụ chủ đề tốt cho infographic**:
- "Quá trình quang hợp" (KHTN 6)
- "Vòng tuần hoàn nước" (Địa lý 6)
- "Cấu trúc nguyên tử" (Hoá học 8)
- "5 nhóm thực phẩm dinh dưỡng" (Sinh 8)

### 2. MINDMAP

**Khi nào dùng**: Tổng quan một chương, ôn tập, hệ thống hoá kiến thức từ một chủ đề trung tâm.

**Cấu trúc**:
- 1 ô trung tâm chứa chủ đề chính (vòng tròn hoặc hình elip)
- 4-6 nhánh chính (như cành cây)
- Mỗi nhánh chính có 2-4 nhánh phụ
- Phong cách hand-drawn cảm giác sáng tạo, gần gũi học sinh

**Cảnh báo**: Mindmap **không phải** danh sách dạng cây — phải có cảm giác phân nhánh hữu cơ, đường cong mềm. Nếu user muốn dạng "cây thư mục" thì nên chọn DIAGRAM.

### 3. DIAGRAM

**Khi nào dùng**: Sơ đồ chính xác về kỹ thuật, vật lý, hoá học. Ví dụ: mạch điện, lực kế, dụng cụ thí nghiệm, sơ đồ khối thuật toán.

**Đặc trưng**:
- Đường nét mảnh, đen hoặc xanh đậm
- Ít hoặc không tô màu
- Nhãn các thành phần rõ ràng
- Tỷ lệ cân đối, không méo
- Có thể có chú thích bên dưới

**Cảnh báo**: gpt-image-2 đôi khi **không vẽ chính xác mạch điện hoặc cấu tạo phức tạp**. Với diagram đòi hỏi độ chính xác kỹ thuật cao (vd cấu tạo động cơ, sơ đồ thí nghiệm cụ thể), cân nhắc dùng skill `tikz-stem-drawing` thay thế.

### 4. ILLUSTRATION

**Khi nào dùng**: Minh hoạ sinh động cho nội dung văn học, lịch sử, kỹ năng sống, truyện kể.

**Phong cách phổ biến**:
- Storybook watercolor — cho tiểu học, mầm non
- Cartoon vector — cho THCS, vui nhộn
- Anime / manga — học sinh thích
- Realistic painting — văn học, sử

**Lưu ý**: Tránh các nhân vật quá giống nhân vật bản quyền (Doraemon, Mickey…) → thay bằng "cute mascot character", "friendly cartoon child".

### 5. PHOTO

**Khi nào dùng**: Cần cảm giác chân thực — ảnh phong cảnh, ảnh dụng cụ, mô phỏng cảnh thí nghiệm, chân dung nhân vật lịch sử (đã mất, không có ảnh thật).

**Cảnh báo**:
- gpt-image-2 vẫn còn các artifact nhẹ ở mặt người (mắt, tay) khi yêu cầu chân dung.
- **KHÔNG dùng** PHOTO để tạo ảnh người thật còn sống/cụ thể (vi phạm chính sách).
- Với cảnh thí nghiệm cụ thể → ảnh sinh ra có thể "trông đúng nhưng sai chi tiết khoa học" — luôn để giáo viên review.

### 6. COMIC

**Khi nào dùng**: Dạy bài học qua kể chuyện ngắn, đối thoại nhân vật. Phù hợp giáo dục đạo đức, an toàn, kỹ năng sống.

**Cấu trúc**:
- Grid 4 ô (2×2) hoặc 6 ô (2×3)
- Speech bubble bằng tiếng Việt
- Nhân vật nhất quán giữa các ô (gpt-image-2 với "consistency" làm tốt)
- Câu chuyện có mở-thân-kết

**Cảnh báo**: gpt-image-2 đôi khi giữ **nhân vật chưa nhất quán 100%** giữa các ô. Nếu cần consistency cao, mô tả nhân vật rất chi tiết (tóc đen ngắn, áo xanh có in chữ "An", giày trắng) trong prompt.

### 7. POSTER

**Khi nào dùng**: Cổ động, kêu gọi hành động — bảo vệ môi trường, an toàn giao thông, phòng dịch, ngày lễ.

**Cấu trúc**:
- 1 hero subject lớn ở trên
- Slogan 5-10 từ in lớn
- 1-2 cụm phụ nhỏ (ngày, nơi)
- Màu sắc tương phản mạnh

### 8. BANNER

**Khi nào dùng**: Cover Facebook (1640×856 → ~3:2), header website, slide khai mạc, ảnh thumbnail YouTube.

**Tỷ lệ**: Luôn 1536×1024 (3:2 ngang).

### 9. ICON

**Khi nào dùng**: Biểu tượng đơn lẻ trong slide hoặc UI. Ví dụ icon môn học, icon kỹ năng.

**Đặc trưng**:
- Phong cách flat, đơn sắc hoặc 2 màu
- Nền **trong suốt** (yêu cầu rõ trong prompt: "transparent background")
- Hình đơn giản, không chi tiết phức tạp

**Lưu ý**: gpt-image-2 hỗ trợ output PNG có alpha channel (transparent) — phải set `output_format="png"` và prompt có "transparent background, no background, isolated icon".

### 10. SCIENTIFIC

**Khi nào dùng**: Sơ đồ khoa học chính xác — chu trình sinh hoá, cấu tạo phân tử, giải phẫu, địa chất.

**Khác DIAGRAM ở chỗ**: SCIENTIFIC có thể **tô màu, có texture nhẹ**, mô tả tự nhiên hơn (vd cấu tạo tế bào với nhân, ribosome, ti thể tô màu).

**Đặc trưng**:
- Nhãn khoa học chính xác (tiếng Việt + tên la-tinh nếu cần)
- Mũi tên chỉ rõ
- Có thể có cross-section (mặt cắt)
- Phong cách "textbook" — sách giáo khoa khoa học

### 11. WORKSHEET

**Khi nào dùng**: Hình minh hoạ cho phiếu bài tập, đặc biệt tiểu học (đếm số, tô màu, nối hình).

**Đặc trưng**:
- Outline đen trên nền trắng (để in)
- Hình đơn giản, học sinh dễ tô
- Không/ít text
- Có thể có khoảng trống cho học sinh điền

**Cảnh báo**: Với tô màu (coloring page), phải prompt rõ "black outline only on white background, no fill, no shading, suitable for children's coloring".

### 12. SLIDE_HERO

**Khi nào dùng**: Ảnh trang bìa slide PowerPoint/Google Slides, phía trên hoặc nền cho tiêu đề.

**Đặc trưng**:
- Tỷ lệ 16:9 ngang (gần với 3:2 = `1536x1024`)
- Subject lớn chiếm 60-70% khung
- Có phần "không gian âm" (negative space) cho text overlay
- Phong cách editorial, magazine cover

**Lưu ý**: Khi dùng làm nền slide, **prompt rõ "leave the right 1/3 empty for title text overlay"** để có chỗ đặt chữ.

## Quy tắc chọn TYPE khi user không nói rõ

Áp dụng theo thứ tự ưu tiên:

1. Có từ khoá rõ → chọn ngay (vd "infographic" → INFOGRAPHIC, "mindmap" → MINDMAP).
2. User nói "minh hoạ", "vẽ giúp" với chủ đề khoa học/quy trình → INFOGRAPHIC.
3. User nói "sơ đồ" → DIAGRAM (kỹ thuật) hoặc MINDMAP (kiến thức).
4. User nói "tranh", "minh hoạ" với chủ đề văn học/lịch sử → ILLUSTRATION.
5. User nói "ảnh bìa", "thumbnail" → SLIDE_HERO hoặc BANNER.
6. User nói "cổ động", "tuyên truyền" → POSTER.
7. Mặc định cuối cùng (không rõ): ILLUSTRATION.

Luôn xác nhận lại với user ở bảng đề xuất bước 2.
