# Style Library — 15 phong cách đã test với gpt-image-2

File này dùng ở **bước 2 (đề xuất)** và **bước 4 (viết prompt)**. Mỗi phong cách có:
- **Cụm từ chuẩn** để chèn vào prompt (lớp 3 - STYLE)
- **Phù hợp với loại ảnh nào**
- **Ghi chú** (điểm mạnh/yếu khi test với gpt-image-2)

## 1. Educational vector flat illustration

```
Style: educational vector flat illustration, friendly geometric shapes, thick clean outlines, bright cheerful colors, no gradients, no shadows.
```

- Phù hợp: INFOGRAPHIC, ILLUSTRATION (tiểu học/THCS), DIAGRAM
- Mạnh: text rõ, dễ in trắng đen, học sinh dễ nhìn
- Yếu: kém biểu cảm cho cảnh phức tạp

## 2. Storybook watercolor

```
Style: storybook watercolor painting, soft brush strokes, slightly textured paper feel, dreamy warm tones, gentle color bleeds.
```

- Phù hợp: ILLUSTRATION (truyện kể, văn học, mầm non), POSTER (mềm mại)
- Mạnh: cảm xúc, ấm áp, không quá "AI"
- Yếu: chi tiết kỹ thuật bị mờ

## 3. Hand-drawn doodle on whiteboard

```
Style: hand-drawn doodle on white whiteboard, marker strokes in black with occasional colored highlights, sketchy and informal, like a teacher drew it during class.
```

- Phù hợp: MINDMAP, DIAGRAM (giảng giải nhanh), worksheet
- Mạnh: cảm giác gần gũi, "thầy cô vẽ"
- Yếu: text đôi khi bị nguệch ngoạc khó đọc → ép `crisp lettering`

## 4. 3D isometric illustration

```
Style: 3D isometric illustration, soft ambient shadows, matte plastic finish, modern infographic look, perfectly aligned to 30-degree axes.
```

- Phù hợp: INFOGRAPHIC (high-end), DIAGRAM (kiến trúc, không gian)
- Mạnh: trông "cao cấp", phù hợp slide doanh nghiệp/đại học
- Yếu: tốn token hơn, render chậm hơn

## 5. Technical line drawing / blueprint

```
Style: technical line drawing, monochrome, thin precise strokes like an engineering blueprint, white background with thin grid.
```

- Phù hợp: DIAGRAM (kỹ thuật, vật lý), SCIENTIFIC (cấu trúc)
- Mạnh: chính xác, "chuyên nghiệp"
- Yếu: đơn điệu nếu không có vài chi tiết

## 6. Storybook crayon for kids

```
Style: crayon-on-paper drawing as if made by a child, slightly imperfect lines, bright primary colors, white craft-paper background.
```

- Phù hợp: WORKSHEET (mầm non), ILLUSTRATION
- Mạnh: trẻ em yêu thích
- Yếu: text bị méo, hạn chế dùng nhãn

## 7. Manga-inspired clean line art

```
Style: manga-inspired panels with clean black line art, screentone shading in gray dots, minimal color, expressive character emotions.
```

- Phù hợp: COMIC, ILLUSTRATION (giáo dục đạo đức)
- Mạnh: học sinh THCS/THPT thích, "trendy"
- Yếu: nhân vật consistency giữa các ô không đảm bảo 100%

## 8. Western comic bold colors

```
Style: Western comic book art with bold black outlines, flat saturated colors, halftone shading dots, dynamic action poses.
```

- Phù hợp: COMIC (truyện anh hùng, khoa học vui)
- Mạnh: năng động, mạnh mẽ
- Yếu: quá "Mỹ", có thể không phù hợp văn hoá

## 9. Modern minimal poster

```
Style: modern minimal poster design with bold typography, large negative space, limited 2-3 color palette, sharp geometric shapes.
```

- Phù hợp: POSTER, BANNER
- Mạnh: thẩm mỹ cao, "design"
- Yếu: ít chi tiết → không phù hợp infographic

## 10. Vintage propaganda

```
Style: vintage Vietnamese propaganda poster style, bold red and yellow tones, strong silhouettes, hand-painted feel, slightly aged paper texture.
```

- Phù hợp: POSTER (lễ quốc khánh, giải phóng), môn Lịch sử
- Mạnh: rất "Việt Nam", phù hợp dịp lễ
- Yếu: hạn chế chủ đề

## 11. Photorealistic natural lighting

```
Style: photorealistic, natural lighting, shallow depth of field, professional DSLR look, true colors and textures.
```

- Phù hợp: PHOTO (cảnh, vật phẩm)
- Mạnh: chân thực
- Yếu: với người vẫn còn artifact (mắt, tay)

## 12. Textbook scientific illustration

```
Style: textbook scientific illustration, anatomically and structurally accurate, clean labeled cross-sections, muted natural colors with clear contrast for educational clarity.
```

- Phù hợp: SCIENTIFIC, DIAGRAM (sinh học, hoá học, địa lý)
- Mạnh: chính xác cho giáo dục
- Yếu: kém "wow", phù hợp giáo viên hơn học sinh

## 13. Pixel art retro

```
Style: 16-bit pixel art with limited 16-color palette, sharp pixels, retro game feel, no anti-aliasing.
```

- Phù hợp: ILLUSTRATION (game-based learning), ICON
- Mạnh: học sinh thích, "trendy"
- Yếu: chi tiết hạn chế

## 14. Editorial magazine cover

```
Style: editorial magazine cover layout, photo-illustration hybrid, sophisticated typography placement, premium feel.
```

- Phù hợp: SLIDE_HERO, BANNER (đại học, hội thảo)
- Mạnh: "cao cấp", phù hợp slide chính
- Yếu: chỉ phù hợp đối tượng người lớn

## 15. Flat icon vector

```
Style: flat icon vector, single subject isolated on transparent background, 2-color minimal, geometric simplification, suitable for UI/slide icons.
```

- Phù hợp: ICON
- Mạnh: dùng được trong nhiều slide khác nhau
- Yếu: không thể làm chủ thể chính

## Bảng chéo: Loại ảnh × Style mặc định

| Loại | Mặc định | Alternative 1 | Alternative 2 |
|---|---|---|---|
| INFOGRAPHIC | #1 Educational vector flat | #4 3D isometric | #3 Hand-drawn doodle |
| MINDMAP | #3 Hand-drawn doodle | #1 Educational vector flat | – |
| DIAGRAM | #5 Technical line | #12 Textbook scientific | #1 Educational vector flat |
| ILLUSTRATION | #2 Storybook watercolor | #7 Manga line art | #6 Crayon for kids |
| PHOTO | #11 Photorealistic | – | – |
| COMIC | #7 Manga | #8 Western comic | – |
| POSTER | #9 Modern minimal | #10 Vintage propaganda | #2 Watercolor |
| BANNER | #14 Editorial magazine | #9 Modern minimal | – |
| ICON | #15 Flat icon vector | – | – |
| SCIENTIFIC | #12 Textbook scientific | #5 Technical line | #11 Photorealistic |
| WORKSHEET | #1 Educational vector flat | #6 Crayon for kids | #5 Technical line |
| SLIDE_HERO | #14 Editorial magazine | #4 3D isometric | #11 Photorealistic |

## Cách kết hợp 2 style (advanced)

Đôi khi user muốn fusion. Cấu trúc:

```
Style: [style chính], with elements of [style phụ] in the [phần nào].
```

Ví dụ:
- `Style: educational vector flat illustration, with elements of storybook watercolor in the background sky.`
- `Style: technical line drawing, with subtle elements of pixel art in the icons.`

**Cảnh báo**: Fusion 2 style ngược nhau (vd photorealistic + flat) → kết quả không đoán được. Test trước khi giao cho user.
