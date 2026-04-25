---
name: image-creator
description: "Skill tạo ảnh chất lượng cao bằng OpenAI gpt-image-2 cho mọi loại ảnh giáo dục và truyền thông. Sử dụng khi user yêu cầu tạo/vẽ/sinh ảnh, infographic, mindmap, sơ đồ, poster, banner, ảnh minh họa bài giảng, comic, illustration, scientific diagram, hoặc bất kỳ nội dung hình ảnh nào — kể cả khi user chỉ nói 'làm cho tôi cái ảnh', 'vẽ giúp', 'minh hoạ', 'tạo hình'. Skill có quy trình 7 bước có kiểm soát: phân tích yêu cầu → đề xuất 10 thành phần → user xác nhận → tổng hợp prompt chuẩn tiếng Anh → sinh ảnh bằng tool image-gen của OpenClaw → kiểm tra kích thước → upload Google Drive theo quy ước OPENCLAW/IMAGES/<TYPE>_<n>_<HH-mm-ss_dd-MM-yyyy> nếu file > 4MB. Bắt buộc dùng skill này thay vì sinh ảnh ad-hoc, vì bước xác nhận thành phần đảm bảo ảnh đầu ra đúng ý user và đạt chất lượng giáo dục."
allowed-tools: Read, Write, Edit, Bash, Glob
argument-hint: "[loại ảnh] [chủ đề] [tên file gợi ý]"
---

# Image Creator — Quy trình 7 bước với gpt-image-2

## Mục đích

Skill này biến yêu cầu mơ hồ của user (ví dụ "tạo cho tôi ảnh infographic về quang hợp") thành ảnh chất lượng cao thông qua một quy trình có kiểm soát. Khác với việc sinh ảnh ad-hoc, skill này **bắt buộc bước xác nhận thành phần với user** trước khi sinh ảnh — vì:

- Ảnh sai ý mất nhiều token và thời gian để regen.
- User Việt Nam thường mô tả ngắn gọn, thiếu chi tiết về phong cách/bố cục/màu sắc → cần "khai thác" thêm.
- Với giáo dục, sai một chi tiết khoa học là vấn đề lớn (ví dụ infographic quang hợp mà thiếu CO₂ vào, O₂ ra).

## Phân chia trách nhiệm

Skill này **không tự gọi OpenAI API**. Trong môi trường OpenClaw, việc gọi `gpt-image-2` đã được lo bởi cơ chế provider có sẵn (`openclaw.json` định tuyến tới OpenAI). Nhiệm vụ của skill là:

| Phần | Skill xử lý? |
|---|---|
| Phân tích yêu cầu user | ✅ Có |
| Đề xuất 10 thành phần & confirm | ✅ Có |
| Tổng hợp prompt chuẩn tiếng Anh | ✅ Có |
| **Gọi gpt-image-2 sinh ảnh** | ❌ Không — Claude (host) tự dùng tool image-gen có sẵn |
| Lưu file local | ❌ Không — Claude (host) tự lưu khi sinh |
| Kiểm tra kích thước & upload Drive | ✅ Có (`scripts/check_and_upload.py`) |
| Trả kết quả cho user | ✅ Có |

## Khi nào dùng

**Dùng khi user nói** (tiếng Việt hoặc tiếng Anh):
- "Tạo ảnh", "vẽ", "sinh hình", "minh hoạ"
- "Infographic về…", "mindmap về…", "sơ đồ về…", "poster…"
- "Làm cho tôi cái ảnh", "render hộ", "generate image"
- "Ảnh bìa bài giảng", "ảnh đại diện slide", "banner cho khoá học"
- Bất kỳ yêu cầu nào output cuối cùng là **một file ảnh raster** (.png, .jpg, .webp).

## Khi nào KHÔNG dùng

- User chỉ hỏi/mô tả/phân tích ảnh đã có → trả lời trực tiếp.
- User muốn vẽ sơ đồ TikZ/LaTeX → dùng skill `tikz-stem-drawing`.
- User muốn tạo cả slide PowerPoint, không phải chỉ ảnh đơn → dùng skill `pptx-designer` (skill đó có thể gọi skill này như sub-step để sinh hero image).
- User cần ảnh chứa logo/IP có bản quyền (Disney, Marvel…) → từ chối lịch sự.

## Quy trình 7 bước (BẮT BUỘC theo thứ tự)

### Bước 1 — Phân tích yêu cầu

Đọc kỹ yêu cầu của user và trả lời nội bộ 4 câu hỏi:

1. **Loại ảnh là gì?** (infographic, mindmap, illustration, photo, comic, poster, diagram, banner, icon, scientific diagram, worksheet illustration, slide hero) — nếu không rõ → mặc định `illustration`, nhưng phải hỏi lại ở bước 2.
2. **Chủ đề & nội dung khoa học** — nếu là chủ đề chuyên môn (vd "phản ứng oxi hoá khử", "chu trình nước"), phải hiểu **nội dung khoa học chính xác** trước khi viết prompt. Sai khoa học = ảnh vô dụng cho giáo dục.
3. **Đối tượng/Mục đích sử dụng** (học sinh lớp 6, sinh viên, slide bài giảng, ảnh bìa Facebook…) — quyết định mức độ phức tạp và phong cách.
4. **Tên file gợi ý** — nếu user chưa cho, đặt tên ngắn gọn không dấu, vd `quang_hop_lop6`, `dinh_luat_om`.

Nếu chủ đề khoa học và bạn không chắc về nội dung, **đọc tham khảo `references/image_types.md`** và có thể tra cứu thêm.

### Bước 2 — Đề xuất 10 thành phần để user xác nhận

Đây là **trái tim của skill**. Trình bày cho user một bảng/danh sách 10 thành phần với **giá trị đề xuất kèm 2-3 phương án thay thế**, để user dễ chọn. Định dạng phải gọn, dễ đọc trên mobile (vì user OpenClaw thường dùng mobile).

**Đọc file `references/component_checklist.md`** để xem 10 thành phần chi tiết và các giá trị mặc định theo từng loại ảnh, và **đọc file `templates/confirmation_card.md`** để có sẵn mẫu bảng xác nhận.

Mẫu trình bày tóm tắt (giữ nguyên cấu trúc này):

```
🎨 **Tôi đề xuất các thành phần sau cho ảnh "{tên_file}"**

| # | Thành phần | Đề xuất | Lựa chọn khác |
|---|---|---|---|
| 1 | Loại ảnh | Infographic | Mindmap • Diagram |
| 2 | Chủ đề chính | Quá trình quang hợp ở thực vật | – |
| 3 | Phong cách | Educational vector flat illustration | Watercolor • 3D isometric |
| 4 | Bố cục | Trung tâm là cây, mũi tên ra/vào hai bên | Top-down • Cycle |
| 5 | Bảng màu | `#4CAF50` `#FFC107` `#2196F3` `#FFFFFF` | Pastel • Monochrome |
| 6 | Tâm trạng | Tươi sáng, gần gũi, học sinh tiểu học | Trang trọng • Năng động |
| 7 | Tỷ lệ khung | 1024×1536 (dọc, hợp slide) | 1024×1024 • 1536×1024 |
| 8 | Văn bản trong ảnh | "QUANG HỢP" + nhãn CO₂/O₂/H₂O/Glucose | Không text • Chỉ tiếng Anh |
| 9 | Chất lượng | high | medium • low |
| 10 | Mức chi tiết | Trung bình (8-10 yếu tố) | Tối giản • Nhiều chi tiết |

👉 **Xác nhận luôn (gõ "OK") hoặc nói rõ mục nào muốn đổi** (vd: "đổi #3 sang watercolor, #5 pastel").
```

**Quy tắc khi đề xuất:**
- Mục #2 (chủ đề chính) phải **mô tả chính xác nội dung khoa học**, không nói chung chung.
- Mục #8 (text): với gpt-image-2 render text rất tốt **kể cả tiếng Việt có dấu**, nhưng giới hạn ≤ 6 cụm từ ngắn để tránh chữ bị méo.
- Mục #7 (tỷ lệ): chỉ đề xuất 3 size hợp lệ của gpt-image-2: `1024x1024`, `1536x1024`, `1024x1536`.
- Mục #9 (chất lượng): mặc định `high` cho ảnh cuối cùng; gợi ý `medium` nếu user muốn thử nghiệm nhanh.

### Bước 3 — Đợi user phản hồi & cập nhật

User có 3 khả năng phản hồi:

| Phản hồi | Hành động |
|---|---|
| "OK" / "duyệt" / "đồng ý" / 👍 | Sang bước 4 ngay với toàn bộ giá trị đề xuất |
| Chỉnh từng mục, vd "đổi #5 sang pastel, bỏ text" | Cập nhật rồi **trình lại bảng đã chỉnh** và hỏi xác nhận thêm 1 lần |
| User chỉnh nhiều/yêu cầu thêm chủ đề mới | Quay lại bước 1 |

**Tuyệt đối không** sang bước 4 khi user chưa xác nhận rõ ràng. Nếu user mơ hồ ("ờ tuỳ bạn") → chốt theo đề xuất và thông báo "Tôi chốt theo đề xuất, sẽ sinh ảnh ngay".

### Bước 4 — Tổng hợp prompt chuẩn cho gpt-image-2

**Đọc file `references/prompt_template.md`** để lấy khung prompt 5 lớp.

Cấu trúc prompt theo thứ tự (RẤT QUAN TRỌNG, gpt-image-2 đọc top-down):

```
[1. SCENE/BACKGROUND]      — Bối cảnh tổng thể, nền
[2. SUBJECT]               — Chủ thể chính, vị trí trung tâm
[3. STYLE]                 — Phong cách nghệ thuật, render
[4. COMPOSITION & DETAILS] — Bố cục, các yếu tố phụ, mũi tên, nhãn
[5. CONSTRAINTS]           — Tỷ lệ ngầm, "không có gì", chất lượng
```

Prompt **viết bằng tiếng Anh** (gpt-image-2 hiểu tốt nhất), **trừ phần text-trong-ảnh** giữ nguyên tiếng Việt có dấu.

**Trước khi sang bước 5, hiển thị prompt cuối cùng cho user và hỏi**: "Đây là prompt cuối. Sinh luôn hay cần chỉnh?" — bước này tốn ít token nhưng cứu được nhiều lần regen.

Sau khi user duyệt, lưu prompt vào file tạm để bước 5 dùng:

```bash
cat > /tmp/img_prompt.txt << 'EOF'
<prompt 80-180 từ tiếng Anh>
EOF
```

### Bước 5 — Sinh ảnh bằng tool image-gen của OpenClaw

**Skill không tự gọi OpenAI API.** Thay vào đó, ở bước này Claude (host OpenClaw) sẽ dùng cơ chế image generation có sẵn của môi trường (đã được cấu hình trong `openclaw.json` để route đến `gpt-image-2`) để sinh ảnh.

Khi sinh ảnh, truyền các tham số đã chốt ở bước 2:

| Tham số | Lấy từ mục |
|---|---|
| Prompt | Bước 4, file `/tmp/img_prompt.txt` |
| Size | Mục #7 (1024×1024 / 1536×1024 / 1024×1536) |
| Quality | Mục #9 (low / medium / high) |
| Output format | png (mặc định), webp/jpg nếu user yêu cầu |

**Yêu cầu lưu file ra**: `/tmp/<n>.<ext>` (ví dụ `/tmp/quang_hop_lop6.png`).

**Đọc file `references/style_library.md`** nếu cần tham khảo các style đã được test tốt với gpt-image-2.

**Xử lý lỗi thường gặp** (host trả lỗi):
- `model_not_found: gpt-image-2` → tổ chức chưa được verify cho gpt-image-2. Báo user, gợi ý bật fallback `gpt-image-1.5` trong `openclaw.json` provider config.
- `content_policy_violation` → nội dung bị chặn. Báo user, đề xuất viết lại prompt nhẹ nhàng hơn (vd thay "blood" → "red liquid").
- Timeout > 60s → thử lại với `quality=medium`.

### Bước 6 — Kiểm tra kích thước & Upload Google Drive (nếu > 4MB)

Sau khi có file `/tmp/<n>.<ext>`, chạy:

```bash
python /mnt/skills/user/image-creator/scripts/check_and_upload.py \
  --file /tmp/quang_hop_lop6.png \
  --type INFOGRAPHIC \
  --name quang_hop_lop6
```

Script tự động:
- **Nếu file ≤ 4MB** → giữ local, không upload, in path để user thấy.
- **Nếu file > 4MB** → gọi `upload_drive.py`, upload lên `OPENCLAW/IMAGES/` với tên đúng quy ước:

```
OPENCLAW/IMAGES/<TYPE>_<n>_<HH-mm-ss_dd-MM-yyyy>.<ext>
```

Ví dụ: `OPENCLAW/IMAGES/INFOGRAPHIC_quang_hop_lop6_14-32-05_25-04-2026.png`

**TYPE hợp lệ** (UPPERCASE): `INFOGRAPHIC`, `MINDMAP`, `ILLUSTRATION`, `DIAGRAM`, `PHOTO`, `COMIC`, `POSTER`, `BANNER`, `ICON`, `SCIENTIFIC`, `WORKSHEET`, `SLIDE_HERO`.

Script trả về JSON gồm `local.path`, `uploaded`, và (nếu có) `drive.web_view_link` — đó là link cần gửi cho user.

**Đọc file `references/upload_workflow.md`** để biết chi tiết về cấu trúc folder, service account, và xử lý lỗi.

**Override flags** (nếu cần):
- `--always-upload`: ép upload kể cả file nhỏ.
- `--never-upload`: ép giữ local kể cả file lớn.
- `--threshold-mb 2`: đổi ngưỡng (mặc định 4 MB).
- `--keep-diacritics`: giữ dấu tiếng Việt trong tên file Drive (mặc định bỏ dấu cho an toàn).

### Bước 7 — Trả kết quả cho user

Định dạng trả lời cuối:

```markdown
✅ **Đã sinh ảnh: {tên_file}.png**

📐 1024×1536 px • 3.2 MB
🎨 Educational vector flat illustration

📍 Local: `/tmp/quang_hop_lop6.png`
🔗 [Drive] {webViewLink}    ← chỉ hiện nếu > 4MB

Cần chỉnh sửa thêm? Tôi có thể:
- Đổi style/màu/bố cục → quay lại bước 2
- Tạo phiên bản khác (ngang, vuông) → đổi tỷ lệ ở mục #7
- Sinh thêm icon/biểu tượng kèm theo cùng chủ đề
```

## Tham khảo nhanh các loại ảnh

Để biết loại ảnh nào nên dùng phong cách nào, tỷ lệ nào, có nên có text không... → **đọc `references/image_types.md`**. Đây là cheat sheet 12 loại ảnh thông dụng trong giáo dục Việt Nam.

## Kiến thức quan trọng về gpt-image-2

(Để Claude đề xuất đúng tham số ở bước 2, không phải để gọi API.)

- Model ra mắt 21/4/2026, kế nhiệm gpt-image-1.5.
- **Render text đa ngôn ngữ** rất tốt, kể cả tiếng Việt có dấu (đột phá so với DALL-E 3).
- **Reasoning trước khi vẽ** — model "suy nghĩ" về cấu trúc ảnh, ít sai bố cục hơn.
- **Sizes hợp lệ**: `1024x1024` (1:1), `1536x1024` (3:2 ngang), `1024x1536` (2:3 dọc). Có thể tới 2K nhưng "experimental".
- **Quality**: `low` (~$0.02), `medium` (~$0.07), `high` (~$0.19) per image (giá tham khảo).

## Files trong skill

- `SKILL.md` — file này (workflow tổng).
- `references/image_types.md` — 12 loại ảnh giáo dục, đặc điểm, mặc định.
- `references/component_checklist.md` — chi tiết 10 thành phần và mặc định theo loại.
- `references/prompt_template.md` — khung prompt 5 lớp, ví dụ.
- `references/style_library.md` — 15 phong cách đã test với gpt-image-2.
- `references/upload_workflow.md` — Google Drive API setup, naming, quyền.
- `scripts/check_and_upload.py` — kiểm tra size + gọi upload nếu > 4MB.
- `scripts/upload_drive.py` — upload Google Drive, tự tạo folder, đặt tên theo quy ước.
- `templates/confirmation_card.md` — mẫu bảng xác nhận trình cho user.
- `examples/infographic_quang_hop.md` — ví dụ end-to-end thực tế.

## Lưu ý cho Claude khi dùng skill này

1. **Luôn theo đủ 7 bước**, không skip bước 2-3 (xác nhận thành phần) ngay cả khi user mô tả khá chi tiết — vì user Việt Nam thường ngầm hiểu nhiều điều mà model không biết.
2. **Trình bày bảng đề xuất bằng tiếng Việt**, nhưng prompt cuối là tiếng Anh (text-in-image giữ tiếng Việt).
3. **Nội dung khoa học phải đúng** — nếu user yêu cầu "infographic phản ứng oxi hoá khử" mà bạn không chắc về cơ chế, hãy hỏi lại hoặc tra cứu trước khi viết prompt. Ảnh giáo dục sai khoa học còn tệ hơn không có.
4. **Tôn trọng quy ước file trên Drive** — đúng pattern `OPENCLAW/IMAGES/<TYPE>_<n>_<TIMESTAMP>` để tích hợp với hệ thống thư mục lớn của user (n8n, các workflow khác có thể quét folder này).
5. **Báo chi phí ước tính** trước khi sinh nếu user gen nhiều ảnh: vd "5 ảnh × $0.19 = ~$0.95".
6. **Bước 5 không tự gọi API** — yêu cầu host (cơ chế image-gen của OpenClaw) sinh ảnh và lưu file ra `/tmp/`. Sau đó mới chạy `check_and_upload.py`.
