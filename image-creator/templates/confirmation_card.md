# Mẫu thẻ xác nhận thành phần (Bước 2)

File này là **template Claude copy/paste rồi điền vào** khi trình bày cho user.

## Template chính (dùng cho phần lớn yêu cầu)

```markdown
🎨 **Tôi đề xuất các thành phần sau cho ảnh "{TÊN_FILE}"**

| # | Thành phần | Đề xuất | Lựa chọn khác |
|---|---|---|---|
| 1 | Loại ảnh | **{LOAI_ANH}** | {ALT_1} • {ALT_2} |
| 2 | Chủ đề chính | {MO_TA_NOI_DUNG_KHOA_HOC_CHI_TIET} | – |
| 3 | Phong cách | **{STYLE}** | {STYLE_ALT_1} • {STYLE_ALT_2} |
| 4 | Bố cục | {COMPOSITION} | {COMP_ALT_1} • {COMP_ALT_2} |
| 5 | Bảng màu | {COLOR_HEX_LIST} | {PALETTE_ALT_1} • {PALETTE_ALT_2} |
| 6 | Tâm trạng | {MOOD} | {MOOD_ALT_1} • {MOOD_ALT_2} |
| 7 | Tỷ lệ khung | **{SIZE}** ({TY_LE}) | {SIZE_ALT_1} • {SIZE_ALT_2} |
| 8 | Văn bản trong ảnh | {TEXT_LIST} | Không text • Chỉ tiếng Anh |
| 9 | Chất lượng | **{QUALITY}** (~${COST}) | medium • low |
| 10 | Mức chi tiết | {DETAIL_LEVEL} | Tối giản • Nhiều chi tiết |

👉 **Xác nhận luôn** (gõ "OK") hoặc **chỉnh mục nào** (vd: "đổi #3 sang watercolor, #5 pastel, bỏ text").
```

## Ví dụ điền sẵn — INFOGRAPHIC quang hợp

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

👉 **Xác nhận luôn** (gõ "OK") hoặc **chỉnh mục nào** (vd: "đổi #3 sang watercolor, #5 pastel").
```

## Ví dụ điền sẵn — POSTER an toàn giao thông

```markdown
🎨 **Tôi đề xuất các thành phần sau cho ảnh "an_toan_giao_thong"**

| # | Thành phần | Đề xuất | Lựa chọn khác |
|---|---|---|---|
| 1 | Loại ảnh | **POSTER** | Banner • Illustration |
| 2 | Chủ đề chính | Học sinh đội mũ bảo hiểm khi đi xe đạp/xe máy, kêu gọi tuân thủ luật | – |
| 3 | Phong cách | **Modern minimal poster design** | Vintage propaganda • Storybook watercolor |
| 4 | Bố cục | Hero subject (học sinh đội mũ) ở 2/3 trên, slogan ở 1/3 dưới | Centered • Asymmetric |
| 5 | Bảng màu | `#E91E63` `#FFEB3B` `#000000` `#FFFFFF` | Cờ đỏ vàng • Pastel |
| 6 | Tâm trạng | Truyền cảm hứng, mạnh mẽ | Cảnh báo • Vui nhộn |
| 7 | Tỷ lệ khung | **1024×1536** (dọc 2:3) | 1024×1024 vuông • 1536×1024 ngang |
| 8 | Văn bản trong ảnh | Title "AN TOÀN LÀ TRÊN HẾT" + slogan "Đội mũ bảo hiểm — yêu thương chính mình" | Chỉ slogan • Không text |
| 9 | Chất lượng | **high** (~$0.19) | medium • low |
| 10 | Mức chi tiết | Tối giản (3-5 yếu tố) | Trung bình • Nhiều chi tiết |

👉 **Xác nhận luôn** (gõ "OK") hoặc **chỉnh mục nào**.
```

## Quy tắc khi điền template

1. **Bold** giá trị ở các mục #1, #3, #7, #9 — đó là 4 mục quan trọng nhất ảnh hưởng đến kết quả.
2. Mục #2 (chủ đề chính): viết **đầy đủ nội dung khoa học**, không chỉ chủ đề bài. Đây là cách Claude "ép" mình hiểu rõ trước khi sinh ảnh.
3. Mục #5 (palette): luôn dùng hex code, không nói tên màu.
4. Mục #8 (text): liệt kê chính xác các cụm từ sẽ xuất hiện, kèm dấu nháy kép.
5. Hai mục #2 và #8 thường không có "lựa chọn khác" → đặt dấu `–`.

## Sau khi user phản hồi

### Trường hợp 1: User OK

Trả lời ngắn gọn:
```
✅ Đã chốt. Đang tổng hợp prompt và sinh ảnh, đợi ~30-60 giây nhé.
```

Sau đó sang bước 4 (tổng hợp prompt) → 5 (sinh ảnh).

### Trường hợp 2: User chỉnh mục cụ thể

Cập nhật giá trị, **trình lại bảng** với các thay đổi đánh dấu rõ:

```
🔄 **Đã cập nhật theo yêu cầu**:

| # | Thành phần | Đề xuất (mới) | Đã đổi từ |
|---|---|---|---|
| 3 | Phong cách | **Storybook watercolor** | ~~Educational vector flat~~ |
| 5 | Bảng màu | `#FFB6C1` `#B0E0E6` `#FFDEAD` `#98FB98` | ~~Tươi sáng~~ → Pastel |

(Các mục khác giữ nguyên.)

👉 OK để sinh, hay chỉnh thêm?
```

### Trường hợp 3: User mơ hồ ("ờ tuỳ bạn", "sao cũng được")

Chốt theo đề xuất, không hỏi lại:
```
OK, mình chốt theo đề xuất ban đầu. Đang sinh ảnh...
```

### Trường hợp 4: User yêu cầu thay đổi lớn (đổi cả chủ đề)

Quay lại bước 1, phân tích lại, trình bảng mới hoàn toàn.
