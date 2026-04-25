# 10 Thành phần đề xuất cho user xác nhận

File này dùng ở **bước 2 của workflow**. Khi đề xuất thành phần cho user, bám sát checklist này để không sót, và dùng giá trị mặc định theo loại ảnh.

## Cấu trúc bảng đề xuất

Luôn dùng bảng markdown 4 cột: `# | Thành phần | Đề xuất | Lựa chọn khác`. Cột "Đề xuất" là giá trị Claude tự chọn dựa trên phân tích bước 1; cột "Lựa chọn khác" liệt kê 2-3 phương án phổ biến để user dễ đổi.

## Chi tiết 10 thành phần

### #1 — Loại ảnh (Image Type)

Ảnh hưởng **lớn nhất** đến phong cách và bố cục. Xem `image_types.md` để chọn.

| Loại | Khi nào chọn |
|---|---|
| Infographic | Truyền đạt khái niệm có nhiều thành phần, kèm số liệu/text |
| Mindmap | Phân nhánh ý tưởng từ trung tâm (tổng quan chương, ôn tập) |
| Diagram | Sơ đồ kỹ thuật/khoa học (mạch điện, cấu tạo tế bào) |
| Illustration | Minh hoạ sinh động cho nhân vật, cảnh, vật thể |
| Photo | Ảnh chân thực (cảnh quan, vật phẩm, nhân vật lịch sử) |
| Comic | Truyện tranh ngắn dạy bài học |
| Poster | Cổ động, kêu gọi hành động (an toàn giao thông, BVMT) |
| Banner | Ảnh ngang dài (cover Facebook, header website) |
| Icon | Biểu tượng đơn lẻ, trong suốt nền |
| Scientific | Sơ đồ khoa học chính xác (chu trình, cấu tạo phân tử) |
| Worksheet | Hình minh hoạ cho phiếu bài tập (đếm số, tô màu) |
| Slide Hero | Ảnh trang bìa slide bài giảng |

### #2 — Chủ đề chính (Subject)

Mô tả **NỘI DUNG cụ thể** của ảnh, không phải tên bài. Ví dụ:
- ❌ "Bài 5: Quang hợp" 
- ✅ "Cây xanh hấp thụ CO₂ và H₂O, dưới ánh sáng mặt trời tạo ra O₂ và Glucose"

Với chủ đề khoa học: nêu **các yếu tố BẮT BUỘC phải có** trong ảnh (input/output, quá trình, công thức).

### #3 — Phong cách (Style)

Xem `style_library.md` để biết 15 phong cách đã test tốt. Mặc định theo loại ảnh:

| Loại ảnh | Style mặc định | Style alternative |
|---|---|---|
| Infographic | Educational vector flat illustration | Isometric 3D • Hand-drawn doodle |
| Mindmap | Hand-drawn doodle on whiteboard | Digital flat • Sketchnote |
| Diagram | Technical line drawing | Blueprint • Schematic |
| Illustration | Storybook watercolor | Anime • Cartoon vector |
| Photo | Photorealistic, natural lighting | Studio shot • Documentary |
| Comic | Manga-inspired panels | Western comic • 4-koma |
| Poster | Vintage propaganda style | Modern minimal • Retro |
| Scientific | Textbook scientific illustration | Photographic macro • CGI render |
| Slide Hero | Editorial magazine cover | Abstract gradient • Cinematic |

### #4 — Bố cục (Composition)

Bố cục quyết định **mắt user nhìn vào đâu trước**. Đề xuất theo loại:

- **Infographic**: Center-out (chủ thể giữa, nhánh ra) hoặc Top-to-bottom flow.
- **Mindmap**: Radial từ trung tâm.
- **Diagram**: Left-to-right flow (input → process → output) hoặc Cycle.
- **Illustration**: Rule of thirds, chủ thể lệch trái/phải.
- **Comic**: Grid 4-6 ô.
- **Poster**: Hero subject ở 1/3 trên, text ở 1/3 dưới.

Nếu user không rõ, đề xuất bố cục chuẩn nhất cho loại đó và mô tả ngắn (vd "Trung tâm là cây, mũi tên ra/vào hai bên").

### #5 — Bảng màu (Color Palette)

Đề xuất **3-5 màu hex cụ thể**, không nói chung chung "xanh xanh đỏ đỏ". 

**Bảng màu giáo dục Việt Nam được khuyến nghị**:
- Tươi sáng tiểu học: `#4CAF50` `#FFC107` `#2196F3` `#FF5722` `#FFFFFF`
- Trang trọng THPT: `#1976D2` `#388E3C` `#F57C00` `#424242` `#FAFAFA`
- Pastel mềm mại: `#FFB6C1` `#B0E0E6` `#FFDEAD` `#98FB98` `#FFFFE0`
- Khoa học chính xác: `#0D47A1` `#1B5E20` `#B71C1C` `#212121` `#FFFFFF`
- Năng động (poster): `#E91E63` `#FFEB3B` `#000000` `#FFFFFF`

User có thể nói tên (vd "pastel") → expand thành hex tương ứng trong prompt.

### #6 — Tâm trạng (Mood)

Tâm trạng tổng thể, ảnh hưởng ánh sáng, độ bão hoà, biểu cảm:

| Mood | Phù hợp với |
|---|---|
| Tươi sáng, gần gũi | Tiểu học, mầm non |
| Năng động, vui nhộn | THCS, hoạt động ngoại khoá |
| Trang trọng, học thuật | THPT, nghiên cứu |
| Bí ẩn, kích thích tò mò | Hoá học, vũ trụ, lịch sử cổ đại |
| Cảnh báo, nghiêm túc | An toàn, môi trường |
| Truyền cảm hứng | Ngày lễ, khai giảng, cổ động |

### #7 — Tỷ lệ khung (Aspect Ratio / Size)

**CHỈ 3 SIZE HỢP LỆ** với gpt-image-2 (theo doc OpenAI):

| Size | Tỷ lệ | Dùng cho |
|---|---|---|
| `1024x1024` | 1:1 vuông | Post Facebook/Instagram, icon, cover bài tập |
| `1536x1024` | 3:2 ngang | Banner, slide ngang, cover Facebook |
| `1024x1536` | 2:3 dọc | Poster, infographic dài, story Instagram |

Nếu user nói "ngang dài" → `1536x1024`; "dọc" → `1024x1536`; "vuông" hoặc không nói → `1024x1024`.

(Có size cao hơn tới 2560×1440 nhưng experimental, **không dùng** trừ khi user yêu cầu rõ và chấp nhận rủi ro.)

### #8 — Văn bản trong ảnh (Text/Labels)

gpt-image-2 render text **tốt với tiếng Việt có dấu**. Quy tắc:

- **≤ 6 cụm từ ngắn** trong một ảnh (mỗi cụm ≤ 4 từ). Quá nhiều text → chữ bị méo.
- Tiêu đề ảnh: viết HOA, font sans-serif đậm.
- Nhãn các thành phần: thường, tiếng Việt có dấu OK.
- Công thức hoá học: dùng subscript thực (`H₂O`, `CO₂`, `C₆H₁₂O₆`) — gpt-image-2 render đúng.

Nếu user không cần text → ghi rõ "no text in image" trong prompt (mục Constraints).

### #9 — Chất lượng (Quality)

3 mức của gpt-image-2:

| Quality | Token output | Giá ước tính (1024² square) | Dùng khi |
|---|---|---|---|
| `low` | ~272 | ~$0.011 | Thumbnail, draft, preview hàng loạt |
| `medium` | ~1056 | ~$0.042 | Slide phụ, ảnh thử nghiệm |
| `high` | ~4160 | ~$0.167 | Ảnh cuối cùng, in ấn, slide chính |

Mặc định `high` cho ảnh giao cuối; `medium` nếu user yêu cầu thử nhiều biến thể.

### #10 — Mức chi tiết (Detail Level)

Số yếu tố visual trong ảnh:

| Mức | Số yếu tố chính | Phù hợp |
|---|---|---|
| Tối giản | 3-5 | Icon, slide hero, poster cô đọng |
| Trung bình | 6-10 | Infographic chuẩn, diagram thường |
| Nhiều chi tiết | 10-20 | Mindmap chương lớn, cảnh phức tạp |

**Trên 20 yếu tố** → khuyên user chia thành nhiều ảnh, vì gpt-image-2 sẽ bắt đầu bỏ sót hoặc render méo.

## Mặc định nhanh theo loại ảnh

Để Claude không phải nghĩ lại từ đầu mỗi lần, đây là mặc định "an toàn" cho 8 loại phổ biến nhất:

```yaml
infographic:
  style: Educational vector flat illustration
  composition: Center-out với title trên đỉnh
  palette: ["#4CAF50", "#FFC107", "#2196F3", "#FFFFFF", "#212121"]
  mood: Tươi sáng, gần gũi
  size: 1024x1536
  text: Title + 4-6 nhãn ngắn
  quality: high
  detail: Trung bình (6-10 yếu tố)

mindmap:
  style: Hand-drawn doodle on whiteboard
  composition: Radial từ trung tâm
  palette: ["#1976D2", "#E91E63", "#388E3C", "#F57C00", "#FFFFFF"]
  mood: Năng động, sáng tạo
  size: 1536x1024
  text: 1 cụm trung tâm + 4-8 nhánh ngắn
  quality: high
  detail: Trung bình

diagram:
  style: Technical line drawing
  composition: Left-to-right flow
  palette: ["#0D47A1", "#212121", "#FFFFFF", "#9E9E9E"]
  mood: Trang trọng, chính xác
  size: 1536x1024
  text: Nhãn các thành phần, không tô màu
  quality: high
  detail: Trung bình

illustration:
  style: Storybook watercolor
  composition: Rule of thirds
  palette: ["#FFB6C1", "#B0E0E6", "#FFDEAD", "#98FB98", "#FFFFFF"]
  mood: Tươi sáng, mơ mộng
  size: 1024x1024
  text: Không text (trừ khi user yêu cầu)
  quality: high
  detail: Trung bình

poster:
  style: Modern minimal poster design
  composition: Hero 1/3 trên, text 1/3 dưới
  palette: ["#E91E63", "#FFEB3B", "#000000", "#FFFFFF"]
  mood: Truyền cảm hứng, mạnh mẽ
  size: 1024x1536
  text: Title lớn + slogan + 2-3 cụm phụ
  quality: high
  detail: Tối giản

scientific:
  style: Textbook scientific illustration
  composition: Tuỳ chủ đề (cycle, cross-section, layered)
  palette: ["#0D47A1", "#1B5E20", "#B71C1C", "#212121", "#FFFFFF"]
  mood: Trang trọng, chính xác
  size: 1024x1536
  text: Nhãn khoa học có dấu, công thức đúng
  quality: high
  detail: Trung bình đến nhiều

slide_hero:
  style: Editorial magazine cover
  composition: Hero subject lớn 70% khung
  palette: Tuỳ chủ đề, ưu tiên 2-3 màu chủ đạo
  mood: Trang trọng + lôi cuốn
  size: 1536x1024
  text: Tiêu đề slide + (tuỳ chọn) phụ đề
  quality: high
  detail: Tối giản đến trung bình

comic:
  style: Manga-inspired panels with clean line art
  composition: Grid 4 ô (2x2) hoặc 6 ô (2x3)
  palette: ["#000000", "#FFFFFF", "#FFC107", "#E91E63"]
  mood: Vui nhộn, đối thoại
  size: 1024x1536
  text: Speech bubbles tiếng Việt
  quality: high
  detail: Trung bình
```
