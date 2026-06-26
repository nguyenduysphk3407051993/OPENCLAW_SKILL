# Scene Template — Mẫu chi tiết cho 1 cảnh

Dùng file này khi cần mẫu cụ thể hoặc khi không truy cập được skill `prompt-video-creator` / `prompt-image-creator`.

## 1. Bộ thành phần PROMPT VIDEO (tiếng Anh) — tối thiểu 15 mục

1. **Shot Type** — wide / medium / close-up / extreme close-up / over-the-shoulder / establishing / aerial
2. **Camera Movement** — dolly in/out, pan, tilt, tracking, crane, handheld, steadicam, zoom, orbit, drone
3. **Camera Angle** — eye-level, low angle, high angle, bird's eye, worm's eye, Dutch angle, POV
4. **Subject** — chính là mô tả NHÂN VẬT ĐỒNG NHẤT (copy y nguyên Character Sheet)
5. **Action** — verb + cách thức ("walking slowly", "explaining cheerfully")
6. **Setting/Environment** — bối cảnh chi tiết
7. **Time of Day** — golden hour, blue hour, midday, twilight, midnight
8. **Lighting** — cinematic, natural, three-point, rim light, neon, soft diffused
9. **Color Grading** — teal & orange, warm, cool, desaturated, vibrant, monochrome
10. **Mood/Atmosphere** — tense, dreamy, romantic, energetic, epic, intimate
11. **Visual Style** — cinematic film, documentary, 3D animated, anime, claymation, vintage 8mm
12. **Motion/Speed** — real-time, slow-motion, time-lapse, hyperlapse
13. **Lens & Depth of Field** — 24mm wide, 35mm, 50mm, 85mm telephoto, shallow DOF, bokeh
14. **Aspect Ratio & Quality** — 16:9 / 9:16 / 1:1 / 21:9; 4K/8K, 24fps/60fps
15. **Audio/Sound Design** — ambient, music genre, SFX, và **lời thoại nhân vật giữ TIẾNG VIỆT**: `Character speaks in Vietnamese: "..."`

### Công thức nhanh (cinematic 16:9)
```
[Shot Type] of [consistent character description] [action] in [setting], [time of day],
[lighting], [camera movement], [camera angle], [lens] with [DOF],
[color grading] palette, [mood] atmosphere, [visual style], [motion/speed],
audio: [ambient/music]; Character speaks in Vietnamese: "[lời thoại]",
16:9, 4K, 24fps cinematic.
```

### Công thức nhanh (TikTok/Reels dọc 9:16)
```
Vertical 9:16 [shot type] of [consistent character], [action], hook in first second,
[trendy aesthetic], [vibrant lighting], dynamic [camera movement],
[color palette], [mood], 60fps; Character speaks in Vietnamese: "[lời thoại]",
optimized for mobile vertical viewing.
```

## 2. Bộ thành phần PROMPT ẢNH (tiếng Anh)

1. **Subject** — nhân vật/đối tượng (copy Character Sheet nếu có người)
2. **Style** — photorealistic, 3D render, watercolor, flat illustration, anime, cinematic still
3. **Composition** — rule of thirds, centered, close-up, wide establishing
4. **Lighting** — soft natural, studio, golden hour, rim light, dramatic
5. **Color Palette** — warm/cool/pastel/vibrant + tông chủ đạo
6. **Mood** — cheerful, calm, mysterious, epic
7. **Background/Environment** — bối cảnh phía sau
8. **Camera/Lens** — 50mm portrait, 35mm, macro, wide-angle
9. **Detail & Texture** — highly detailed, intricate, clean
10. **Quality tags** — 8K, ultra-detailed, sharp focus, professional
11. **Aspect Ratio** — 16:9 / 9:16 / 1:1 (khớp video)

### Công thức nhanh
```
[Style] image of [consistent character/subject] [pose/expression] in [background],
[composition], [lighting], [color palette], [mood], shot on [camera/lens],
highly detailed, 8K, sharp focus, [aspect ratio].
```

## 3. Mẹo giữ NHÂN VẬT ĐỒNG NHẤT
- Viết một "Character Sheet" cố định: `Character "Mai": a 9-year-old Vietnamese girl, round face, big brown eyes, shoulder-length black hair with red hairband, wearing a yellow t-shirt and blue overalls, cheerful expression.`
- Dán y nguyên đoạn đó vào **Subject** của prompt video VÀ prompt ảnh ở MỌI cảnh.
- Chỉ thay đổi action, bối cảnh, góc máy giữa các cảnh — KHÔNG đổi ngoại hình/trang phục.
- Nếu công cụ hỗ trợ ảnh tham chiếu (reference image), dùng ảnh từ thành phần ④ của cảnh 1 làm gốc cho các cảnh sau.

## 4. VÍ DỤ CẢNH MẪU HOÀN CHỈNH

Chủ đề: *Video mở đầu bài học "Vòng đời của con bướm"* (bài giảng, 16:9).

🎭 **HỒ SƠ NHÂN VẬT:** Character "Cô Lan" — a 28-year-old Vietnamese female teacher, gentle oval face, warm smile, long straight black hair tied in a low ponytail, wearing a pastel green áo dài, friendly and energetic. Consistent across all scenes.

```
═══════════════════════════════════════
🎬 CẢNH 1: Lời chào mở đầu
⏱️ Thời lượng gợi ý: 8 giây
═══════════════════════════════════════

① 🎙️ LỜI THOẠI THUYẾT MINH (Tiếng Việt):
"Chào các em! Hôm nay cô trò mình sẽ cùng khám phá một hành trình kỳ diệu — vòng đời của con bướm. Các em đã sẵn sàng chưa nào?"

② 🧬 PROMPT TẠO NHÂN VẬT ĐỒNG NHẤT:
Character "Cô Lan": a 28-year-old Vietnamese female teacher, gentle oval face, warm smile, long straight black hair in a low ponytail, wearing a pastel green áo dài, friendly energetic demeanor, consistent appearance across all scenes.

③ 🎥 PROMPT SINH VIDEO (English):
Medium shot of Cô Lan (a 28-year-old Vietnamese female teacher, gentle oval face, long black hair in low ponytail, pastel green áo dài) standing in a bright sunny classroom decorated with butterfly posters, gently waving and smiling at the camera, morning golden light through windows, soft three-point lighting, slow dolly-in, eye-level angle, 50mm lens shallow depth of field, warm vibrant color grading, cheerful inviting mood, clean educational cinematic style, real-time motion, ambient classroom sound and soft cheerful music; Character speaks in Vietnamese: "Chào các em! Hôm nay cô trò mình sẽ cùng khám phá một hành trình kỳ diệu — vòng đời của con bướm." 16:9, 4K, 24fps.

④ 🖼️ PROMPT SINH ẢNH (English):
Cinematic still of Cô Lan (28-year-old Vietnamese teacher, gentle oval face, long black hair low ponytail, pastel green áo dài, warm smile) waving in a bright classroom with colorful butterfly posters on the wall, rule-of-thirds composition, soft golden window light, warm pastel color palette, cheerful welcoming mood, shot on 50mm portrait lens, highly detailed, 8K, sharp focus, 16:9.
```

Khi viết thật, lặp lại đúng khối 4 thành phần này cho mỗi cảnh, giữ nhân vật y hệt.
