# Canva Workflow — cách skill dùng plugin Canva để tạo template

Đây là cơ chế CHÍNH (≈80%) của skill: mọi slide/template được tạo và chỉnh **trong Canva qua Canva MCP**,
áp font + icon + gam màu + hình ảnh do người dùng đề xuất. **TUYỆT ĐỐI KHÔNG sinh file .pptx bằng
python-pptx hay bất kỳ ngôn ngữ lập trình nào.** File chỉ được tạo ra bằng cách **export** từ Canva.

## 0. Điều kiện cần (một lần)
- Kết nối connector **Canva** trong Cowork.
- Có **Brand Kit EduTechND** trong Canva chứa:
  - Palette gam vàng đất (xem `assets/brand-standard.json`): `#4B2E2B`, `#8C5A3C`, `#FFF8F0`, và 4 accent theo môn.
  - **Brand fonts = font 9Slide** (upload trong Brand Kit; cần Canva Pro để dùng custom font).
- (Khuyến nghị) Một **Brand Template** EduTechND nền tối để tạo nhanh và đồng nhất.

> Lưu ý kỹ thuật quan trọng: Canva MCP **không đổi được font-family qua API** (`perform-editing-operations`
> chỉ format được size/màu/đậm/nghiêng…). Vì vậy **font 9Slide phải nằm sẵn trong Brand Kit / Brand Template**
> để khi generate là áp đúng. Đừng hứa đổi font bằng API.

## 1. Lấy Brand Kit
- Gọi `list-brand-kits` → lấy `brand_kit_id` của EduTechND (tài khoản hiện có 1 brand kit: `kAHLq3RErqs`).
- Nếu chưa có brand kit đúng chuẩn → hướng dẫn người dùng tạo (dùng tool `help` với câu hỏi cụ thể về
  "create brand kit", "upload brand fonts", "add brand colors").

## 2. Chọn đường tạo template (ưu tiên từ trên xuống)
A. **Có Brand Template EduTechND** (id bắt đầu `BTM`):
   - `search-brand-templates` (query rỗng hoặc theo tên; `dataset="non_empty"` nếu định autofill) → lấy id.
   - `create-design-from-brand-template` (brand_template_id, page_numbers) để tạo design giữ nguyên thiết kế;
     hoặc `autofill-design` nếu template có dataset field để điền tiêu đề/nội dung tự động.
B. **Không có template phù hợp** → tạo presentation theo outline:
   1. Soạn outline từ chủ đề (mỗi slide 1 title + description bullet bằng `-`).
   2. `request-outline-review` (topic, pages[], brand_kit_id, brand_kit_name, audience="educational",
      style, length="short|balanced") → **người dùng duyệt outline trong widget**.
   3. Sau khi duyệt: `generate-design-structured` (topic, audience, style, length, design_type="presentation",
      presentation_outlines[], **brand_kit_id**, asset_ids[]) → tạo design áp brand kit (palette + font 9Slide).

> Quy tắc cứng: `generate-design-structured` CHỈ gọi sau khi outline được duyệt qua `request-outline-review`.
> Mọi yêu cầu sửa outline (thêm/bớt/đổi thứ tự slide) → cập nhật pages rồi gọi lại `request-outline-review`.

## 3. Thêm icon / hình ảnh người dùng đề xuất
- **Ảnh/icon có URL** (hoặc người dùng cung cấp): `upload-asset-from-url` (url, name) → nhận `asset_id`.
  - Chèn khi tạo: truyền `asset_ids` vào `generate-design-structured`.
  - Chèn sau: `start-editing-transaction` → `perform-editing-operations` (`insert_fill`/`update_fill` với
    asset_id, page_id, vị trí) → `commit-editing-transaction`.
- **Icon trong kho Canva (Elements):** dùng từ khóa EN từ `assets/visual-keyword-library.json` +
  `references/keyword-expansion-framework.md`. API không search Elements trực tiếp → hai cách:
  1. Để `generate-design-structured` tự chọn element theo style/outline (đa số trường hợp); hoặc
  2. Hướng dẫn người dùng kéo icon Elements theo đúng bộ từ khóa (giữ một style icon), rồi ta tinh chỉnh.
- Giữ **một style icon** cho cả deck; ưu tiên icon sáng màu/line hợp nền tối.

## 4. Áp & tinh chỉnh màu / chữ / bố cục
- Màu & font: do **Brand Kit/Template** lo. Tinh chỉnh nhỏ qua `perform-editing-operations`:
  `format_text` (color #hex theo gam, font_size, font_weight bold, text_align), `replace_text`,
  `find_and_replace_text`, `update_fill`, `position_element`, `resize_element`, `delete_element`.
- Quy tắc khi chỉnh màu: chỉ dùng 4 vai trò gam vàng đất; accent theo môn < 10% (1 điểm/slide).
- Luôn bọc trong `start-editing-transaction` … `commit-editing-transaction` (nếu bỏ thì `cancel`).
  ⚠️ Chưa commit là CHƯA lưu — không báo "đã xong" trước khi commit thành công.
- Trên trang `is_responsive`, chỉ được dùng: `update_title, replace_text, update_fill,
  delete_element, find_and_replace_text` — thao tác khác phải báo không hỗ trợ.

## 5. Xem lại & xuất file
- `get-design` / `get-design-pages` / `get-design-thumbnail` để kiểm tra trực quan.
- `get-export-formats` → kiểm định dạng hỗ trợ.
- `export-design` (format: `pptx` để có file PowerPoint, hoặc `pdf`/`png`) → trả **URL tải về**; LUÔN hiển thị
  URL cho người dùng. (Đây là cách duy nhất tạo .pptx — export từ Canva, KHÔNG dựng bằng code.)

## 6. Trình tự tool gọn (đường B — không có template)
```
list-brand-kits
→ request-outline-review (brand_kit_id, pages[])         # người dùng duyệt
→ [tuỳ chọn] upload-asset-from-url (ảnh người dùng đề xuất)
→ generate-design-structured (brand_kit_id, outlines, asset_ids)
→ [tinh chỉnh] start-editing-transaction → perform-editing-operations → commit-editing-transaction
→ get-export-formats → export-design (pptx/pdf) → đưa URL tải về
```

## 7. Tuyệt đối tránh
- KHÔNG dùng python-pptx / code để dựng .pptx (chỉ export từ Canva).
- KHÔNG gọi `generate-design-structured` trước khi outline được duyệt.
- KHÔNG hứa đổi font-family qua API (font phải có sẵn trong Brand Kit/Template).
- KHÔNG báo đã lưu khi chưa `commit-editing-transaction`.
- KHÔNG dùng nền sáng mặc định; KHÔNG thay font 9Slide bằng Calibri/Cambria; KHÔNG để accent > 10%.
