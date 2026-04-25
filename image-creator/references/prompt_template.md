# Khung Prompt 5 Lớp cho gpt-image-2

File này dùng ở **bước 4** để tổng hợp prompt cuối cùng từ các thành phần đã chốt với user.

## Nguyên lý vàng

gpt-image-2 đọc prompt **theo thứ tự**, các phần đầu được **ưu tiên cao hơn** khi model có ít "ngân sách chi tiết". Vì vậy, cấu trúc 5 lớp dưới đây không chỉ là format đẹp — nó **thực sự thay đổi chất lượng đầu ra**.

```
┌─ Lớp 1: SCENE/BACKGROUND ───── (5-15 từ)
├─ Lớp 2: SUBJECT ─────────────── (15-30 từ) — quan trọng nhất
├─ Lớp 3: STYLE ──────────────── (10-25 từ)
├─ Lớp 4: COMPOSITION & DETAILS ─ (30-80 từ) — phần dài nhất
└─ Lớp 5: CONSTRAINTS ─────────── (10-25 từ) — gồm "no..." và quality
```

**Tổng độ dài lý tưởng**: 80-180 từ. Ngắn hơn → model tự suy diễn nhiều, kết quả khó đoán. Dài hơn → model bắt đầu bỏ sót chi tiết cuối.

## Lớp 1 — SCENE / BACKGROUND

Mô tả nền, không gian tổng thể. **1-2 câu ngắn**.

Mẫu:
- `On a clean white background with subtle grid pattern.`
- `In a bright forest at sunrise, soft golden light filtering through leaves.`
- `Dark navy blue gradient background with sparse white dots like stars.`
- `Empty pastel pink seamless backdrop.`

**Quy tắc**:
- Infographic/Diagram → nền sáng, đơn giản (white, light gray, subtle pattern).
- Illustration/Photo → bối cảnh phù hợp chủ đề.
- Icon → "transparent background" (chỉ riêng trường hợp này).
- Poster → có thể full-bleed màu mạnh.

## Lớp 2 — SUBJECT (chủ thể chính)

Đây là **trái tim** của ảnh. Mô tả chi tiết chủ thể trung tâm: cái gì, ở đâu trong khung, kích thước tương đối, tư thế, biểu cảm.

Mẫu:
- `Centered in the frame is a stylized green plant with a tall trunk and three large oval leaves, standing upright in brown soil.`
- `A friendly cartoon Vietnamese girl, around 10 years old, short black hair, wearing a white school uniform and red scarf, smiling and pointing forward, occupying the left half of the frame.`
- `Three concentric circles in the center: innermost is a small atom nucleus with red protons and gray neutrons, middle and outer circles show electron orbits with small blue electrons.`

**Quy tắc**:
- Luôn nói rõ vị trí (`centered`, `in the upper-left`, `occupying the right half`).
- Nói rõ kích thước tương đối (`large`, `small`, `taking 60% of the frame`).
- Nếu là người → mô tả nhân khẩu học để model render đúng (tránh bias).

## Lớp 3 — STYLE

Phong cách nghệ thuật. **Càng cụ thể càng tốt**, không nói chung "cute" hay "beautiful".

Mẫu tốt:
- `Style: educational vector flat illustration, friendly geometric shapes, thick clean black outlines, suitable for elementary school textbook.`
- `Style: storybook watercolor painting, soft brush strokes, slightly textured paper feel, dreamy and warm.`
- `Style: technical line drawing, monochrome, thin precise strokes like an engineering blueprint.`
- `Style: 3D isometric illustration, soft shadows, matte finish, modern infographic look.`

**15 phong cách đã test tốt** — xem `style_library.md`.

**Câu thần chú** (đặt cuối Style): `suitable for [đối tượng/mục đích]` — model điều chỉnh độ phức tạp theo đối tượng. Ví dụ:
- `suitable for Vietnamese 6th-grade biology textbook`
- `suitable for university lecture slide`
- `suitable for kindergarten worksheet`

## Lớp 4 — COMPOSITION & DETAILS (phần dài nhất)

Liệt kê các yếu tố phụ, mũi tên, nhãn, các chi tiết bổ sung. **Đây là nơi bạn ghi text-trong-ảnh**.

Mẫu (cho infographic quang hợp):
```
Composition: a glowing yellow sun in the upper-left corner shooting straight light rays toward the leaves. Roots reach into brown soil at the bottom.
Arrows entering the leaves labeled "CO₂" (gray sans-serif) and "H₂O" from the roots (blue droplet icon next to it).
Arrows exiting the leaves labeled "O₂" (light blue) and "Glucose C₆H₁₂O₆" (orange).
The Vietnamese title "QUANG HỢP" appears at the top center in bold dark green sans-serif.
A small footer at the bottom reads "KHTN 6 - Bài 5".
All labels in Vietnamese with proper diacritics, crisp lettering.
Color palette: leaf green #4CAF50, sun yellow #FFC107, water blue #2196F3, soil brown #795548, white background.
```

**Quy tắc cho text-trong-ảnh** (khi dùng tiếng Việt):
1. Đặt text trong dấu ngoặc kép `"..."`.
2. Sau mỗi cụm, mô tả font/màu (`bold dark green sans-serif`, `thin gray italic`).
3. Cuối phần text, thêm câu: `All labels in Vietnamese with proper diacritics, crisp lettering.`
4. **Không** trộn nhiều ngôn ngữ kỳ lạ trong cùng cụm.

**Quy tắc cho màu**:
- Liệt kê palette ở cuối lớp 4: `Color palette: <màu1> #HEX, <màu2> #HEX, ...`.
- Nếu màu có ý nghĩa khoa học (vd CO₂ = xám), nói rõ: `CO₂ in gray (signifying the colorless gas convention)`.

## Lớp 5 — CONSTRAINTS

Điều **không** được có, và yêu cầu chất lượng/tỷ lệ.

Mẫu:
- `Mood: cheerful, approachable, child-friendly. Aspect ratio 2:3 portrait, high resolution. No shadows, no photorealism, no extra text outside the labeled arrows, no watermark.`
- `Aspect ratio 1:1 square. No background, isolated icon on transparent. No shadows, no extra elements.`
- `Aspect ratio 3:2 landscape. Leave the right 1/3 of the frame empty for title text overlay. No people, no animals.`

**Các "no" thường dùng**:
- `no shadows` — cho flat illustration
- `no photorealism` — cho illustration/infographic
- `no extra text outside the labeled elements` — tránh model thêm text bừa
- `no watermark, no signature, no logos` — tránh artifact
- `no people` — nếu user không muốn có người
- `no copyrighted characters or brands` — luôn thêm để an toàn

## Ví dụ end-to-end đầy đủ

### Input từ user (sau khi đã xác nhận thành phần)

```yaml
loại: INFOGRAPHIC
chủ đề: Quá trình quang hợp (cây xanh hấp thụ CO₂ + H₂O, dùng ánh sáng → O₂ + Glucose)
phong cách: Educational vector flat illustration
bố cục: Trung tâm là cây, mũi tên ra/vào hai bên
palette: ["#4CAF50", "#FFC107", "#2196F3", "#795548", "#FFFFFF"]
mood: Tươi sáng, gần gũi, học sinh tiểu học
size: 1024x1536
text: Title "QUANG HỢP" + nhãn CO₂/H₂O/O₂/Glucose
quality: high
detail: Trung bình
```

### Prompt được sinh ra

```
A bright educational infographic on a clean white background with a subtle light-green grid pattern.

Centered in the frame is a stylized green plant with a tall trunk and three large oval leaves standing upright in brown soil, occupying about 60% of the frame height. A glowing yellow sun is in the upper-left corner shooting straight light rays toward the leaves.

Style: educational vector flat illustration, friendly geometric shapes, thick clean dark-green outlines, suitable for Vietnamese 6th-grade biology textbook.

Composition: arrows enter the leaves from the left labeled "CO₂" (gray bold sans-serif) and from the roots labeled "H₂O" (blue droplet icon). Arrows exit the leaves to the right labeled "O₂" (light blue) and "Glucose C₆H₁₂O₆" (orange). The Vietnamese title "QUANG HỢP" appears at the top center in bold dark-green sans-serif. A small footer at the bottom reads "KHTN 6". All labels in Vietnamese with proper diacritics, crisp lettering.
Color palette: leaf green #4CAF50, sun yellow #FFC107, water blue #2196F3, soil brown #795548, white background.

Mood: cheerful, approachable, child-friendly. Aspect ratio 2:3 portrait, high resolution. No shadows, no photorealism, no extra text outside the labeled elements, no watermark, no copyrighted characters.
```

### Tham số API

```python
client.images.generate(
    model="gpt-image-2",
    prompt=prompt,         # 174 từ
    size="1024x1536",      # dọc 2:3
    quality="high",        # ảnh cuối
    n=1,
    output_format="png",
)
```

## Anti-patterns (tránh)

❌ **Quá ngắn**: `"Infographic về quang hợp"` → model tự bịa, kết quả ngẫu nhiên.

❌ **Trộn lung tung không có thứ tự**: `"Vẽ cây quang hợp với CO₂ và O₂ và mặt trời và đẹp đẹp tươi sáng nhé"` → kết quả lủng củng.

❌ **Mâu thuẫn nội tại**: `"flat 2D illustration with realistic shadows and photorealistic lighting"` → model lúng túng, chất lượng tệ.

❌ **Quá nhiều text**: `"with labels: A, B, C, D, E, F, G, H, I, J, K, L"` → text bị méo.

❌ **Yêu cầu ảnh người thật, có tên**: `"chân dung Bác Hồ đang viết"` — gpt-image-2 sẽ render mặt sai. Thay bằng "an elderly Vietnamese man in traditional brown robe, writing at a wooden desk".

## Checklist trước khi gọi API

- [ ] Có đủ 5 lớp (Scene → Subject → Style → Composition → Constraints)?
- [ ] Tổng độ dài 80-180 từ?
- [ ] Tất cả màu là hex code?
- [ ] Text trong ảnh có dấu tiếng Việt (nếu cần)?
- [ ] Có câu `suitable for [đối tượng]` ở Style?
- [ ] Có ít nhất 2 câu "no..." ở Constraints?
- [ ] Aspect ratio match với size sẽ truyền API?
