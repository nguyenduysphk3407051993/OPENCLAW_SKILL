# Ví dụ End-to-End: Infographic "Quang Hợp" cho KHTN lớp 6

File này minh hoạ **đầy đủ 7 bước** cho 1 yêu cầu thực tế. Dùng làm tham chiếu khi bí ý tưởng.

---

## Yêu cầu user (đầu vào)

> "tạo cho tôi 1 cái infographic về quang hợp cho học sinh lớp 6"

---

## Bước 1 — Phân tích yêu cầu (nội bộ Claude)

```
- Loại ảnh: INFOGRAPHIC (user nói rõ)
- Chủ đề: Quang hợp ở thực vật
  + Đầu vào: CO₂ (qua lá), H₂O (qua rễ), năng lượng ánh sáng
  + Đầu ra: O₂ (thải qua lá), Glucose C₆H₁₂O₆ (lưu trữ trong cây)
  + Diễn ra ở: lục lạp, có chất diệp lục
- Đối tượng: Học sinh lớp 6 (KHTN, Bộ GDPT 2018)
  → đơn giản, tươi sáng, có tiếng Việt rõ
- Tên file gợi ý: quang_hop_lop6
```

## Bước 2 — Trình bảng đề xuất cho user

```markdown
🎨 **Tôi đề xuất các thành phần sau cho ảnh "quang_hop_lop6"**

| # | Thành phần | Đề xuất | Lựa chọn khác |
|---|---|---|---|
| 1 | Loại ảnh | **INFOGRAPHIC** | Mindmap • Diagram |
| 2 | Chủ đề chính | Cây xanh hấp thụ CO₂ + H₂O, dùng năng lượng ánh sáng → tạo O₂ + Glucose | – |
| 3 | Phong cách | **Educational vector flat illustration** | 3D isometric • Hand-drawn doodle |
| 4 | Bố cục | Cây ở trung tâm, mặt trời góc trên-trái, mũi tên CO₂/H₂O đi vào, O₂/Glucose đi ra | Top-down flow • Cycle circular |
| 5 | Bảng màu | `#4CAF50` `#FFC107` `#2196F3` `#795548` `#FFFFFF` | Pastel • Monochrome xanh |
| 6 | Tâm trạng | Tươi sáng, gần gũi, học sinh tiểu học | Trang trọng • Năng động |
| 7 | Tỷ lệ khung | **1024×1536** (dọc 2:3, hợp slide) | 1024×1024 vuông • 1536×1024 ngang |
| 8 | Văn bản trong ảnh | Title "QUANG HỢP" + nhãn `CO₂` `H₂O` `O₂` `Glucose C₆H₁₂O₆` | Không text • Chỉ tiếng Anh |
| 9 | Chất lượng | **high** (~$0.19) | medium (~$0.07) • low (~$0.02) |
| 10 | Mức chi tiết | Trung bình (8-10 yếu tố) | Tối giản • Nhiều chi tiết |

👉 **Xác nhận luôn** (gõ "OK") hoặc **chỉnh mục nào**.
```

## Bước 3 — User phản hồi

> "OK"

→ Chốt theo đề xuất, sang bước 4.

## Bước 4 — Tổng hợp prompt (lưu vào /tmp/img_prompt.txt)

```
A bright educational infographic on a clean white background with a subtle light-green grid pattern.

Centered in the frame is a stylized green plant with a tall trunk and three large oval leaves standing upright in brown soil, occupying about 60% of the frame height. A glowing yellow sun is in the upper-left corner shooting straight light rays toward the leaves.

Style: educational vector flat illustration, friendly geometric shapes, thick clean dark-green outlines, suitable for Vietnamese 6th-grade biology textbook.

Composition: arrows enter the leaves from the left labeled "CO₂" (gray bold sans-serif) and from the roots labeled "H₂O" (blue droplet icon next to it). Arrows exit the leaves to the right labeled "O₂" (light blue) and "Glucose C₆H₁₂O₆" (orange). The Vietnamese title "QUANG HỢP" appears at the top center in bold dark-green sans-serif. A small footer at the bottom reads "KHTN 6 - Bài 5". All labels in Vietnamese with proper diacritics, crisp lettering. Color palette: leaf green #4CAF50, sun yellow #FFC107, water blue #2196F3, soil brown #795548, white background.

Mood: cheerful, approachable, child-friendly. Aspect ratio 2:3 portrait, high resolution. No shadows, no photorealism, no extra text outside the labeled elements, no watermark, no copyrighted characters.
```

(Hiển thị prompt cho user, hỏi: "Đây là prompt cuối. Sinh luôn hay cần chỉnh?")

## Bước 5 — Sinh ảnh bằng tool image-gen của OpenClaw

Claude (host) gọi tool image generation có sẵn với các tham số:

```yaml
prompt: <nội dung file /tmp/img_prompt.txt>
size: 1024x1536
quality: high
output_format: png
output_path: /tmp/quang_hop_lop6.png
```

(Tham số được route đến `gpt-image-2` thông qua `openclaw.json` provider config.)

Sau khi sinh xong, file `/tmp/quang_hop_lop6.png` đã có sẵn ở filesystem của container.

## Bước 6 — Kiểm tra size & Upload Drive nếu cần

```bash
python /mnt/skills/user/image-creator/scripts/check_and_upload.py \
  --file /tmp/quang_hop_lop6.png \
  --type INFOGRAPHIC \
  --name quang_hop_lop6
```

Output (stderr):
```
→ File: /tmp/quang_hop_lop6.png (4.8 MB)
→ Upload: True (size 4.8MB > threshold 4.0MB)
→ Uploading quang_hop_lop6.png → OPENCLAW/IMAGES/INFOGRAPHIC_quang_hop_lop6_14-32-05_25-04-2026.png
  → Đã tạo folder mới 'OPENCLAW' (id=1AbCd...)
  → Đã tạo folder mới 'IMAGES' (id=1EfGh...)
✅ Uploaded: OPENCLAW/IMAGES/INFOGRAPHIC_quang_hop_lop6_14-32-05_25-04-2026.png
🔗 https://drive.google.com/file/d/1XyZ.../view?usp=sharing
```

JSON stdout:
```json
{
  "ok": true,
  "local": {
    "path": "/tmp/quang_hop_lop6.png",
    "size_mb": 4.8,
    "size_bytes": 5033164
  },
  "uploaded": true,
  "upload_reason": "size 4.8MB > threshold 4.0MB",
  "drive": {
    "ok": true,
    "drive_path": "OPENCLAW/IMAGES/INFOGRAPHIC_quang_hop_lop6_14-32-05_25-04-2026.png",
    "web_view_link": "https://drive.google.com/file/d/1XyZ.../view?usp=sharing",
    ...
  },
  "type": "INFOGRAPHIC",
  "name": "quang_hop_lop6"
}
```

## Bước 7 — Trả kết quả cho user

```markdown
✅ **Đã sinh ảnh: quang_hop_lop6.png**

📐 1024×1536 px • 4.8 MB
🎨 Educational vector flat illustration • gpt-image-2 quality=high
📁 Drive: `OPENCLAW/IMAGES/INFOGRAPHIC_quang_hop_lop6_14-32-05_25-04-2026.png`
🔗 [Xem ảnh](https://drive.google.com/file/d/1XyZ.../view?usp=sharing)

Cần chỉnh sửa thêm? Tôi có thể:
- Đổi style/màu/bố cục → quay lại bước 2
- Tạo thêm phiên bản (ngang, vuông) → đổi tỷ lệ ở mục #7
- Sinh thêm icon/biểu tượng kèm theo cùng chủ đề
```

---

## Bài học rút ra

1. **Bước 2 (xác nhận thành phần) là bắt buộc** — kể cả khi user mô tả khá rõ. User Việt Nam thường ngầm hiểu nhiều thứ (vd "lớp 6" → đơn giản, có tiếng Việt) mà nếu không trình bày tường minh thì model không biết.

2. **Mục #2 (chủ đề chính) phải mô tả nội dung khoa học chính xác**. Nếu chỉ ghi "quang hợp" mà không có CO₂/H₂O/O₂/Glucose → ảnh sinh ra có thể thiếu yếu tố quan trọng.

3. **Prompt cuối luôn tiếng Anh, text-trong-ảnh giữ tiếng Việt có dấu**. gpt-image-2 hiểu tiếng Anh tốt nhất, nhưng render text Việt rất tốt nhờ multilingual.

4. **File 4.8MB → upload đúng**, có Drive link gửi cho user. Nếu nhỏ hơn (vd 2MB) thì gửi luôn local trong chat.

5. **Naming chuẩn `INFOGRAPHIC_quang_hop_lop6_14-32-05_25-04-2026.png`** giúp:
   - Tìm theo loại (`INFOGRAPHIC_*`) → mọi infographic chung 1 chỗ.
   - Sort theo thời gian → bản gần nhất ở cuối.
   - Dễ tích hợp với n8n workflow (regex match được).
