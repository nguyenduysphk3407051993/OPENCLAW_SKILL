# Cập nhật skill `canva-ppt-lesson-designer` — dựa trên plugin CANVA

Skill này tạo bài giảng KHTN **bằng plugin Canva (Canva MCP)**: khi bạn nhập một CHỦ ĐỀ, skill suy ra
**từ khóa** để chọn icon/ảnh, áp **Brand Kit EduTechND** (gam vàng đất nền tối + font 9Slide, accent theo
môn), tạo **template thật trong Canva**, rồi **export** ra file.

> **TUYỆT ĐỐI KHÔNG dựng .pptx bằng python-pptx hay bất kỳ code nào.** File chỉ tạo bằng `export-design` từ Canva.

> **Lưu ý cài đặt:** Tôi không ghi trực tiếp vào skill đã cài (cache chỉ-đọc). Hãy cài gói này qua
> **Settings → Capabilities** (chép vào thư mục skill `canva-ppt-lesson-designer`).

## Cấu trúc gói (đặt trùng cấu trúc skill)
```
canva-ppt-lesson-designer-update/
├─ SKILL.md                              # bản cập nhật: Canva-first, không code pptx
├─ assets/
│  ├─ brand-standard.json               # giá trị Brand Kit Canva: gam màu + accent theo môn + font 9Slide
│  └─ visual-keyword-library.json       # chủ đề KHTN → từ khóa EN + mô tả VI để chọn icon/ảnh trên Canva
└─ references/
   ├─ canva-workflow.md                 # TRÌNH TỰ tool Canva MCP (mấu chốt 80%)
   ├─ keyword-expansion-framework.md    # chủ đề → từ khóa → hình ảnh (cho Canva)
   └─ slide-design-framework.md         # gam màu/font chuẩn, 6 mẫu bố cục, QA (hướng Canva)
```

## Điều kiện dùng (một lần)
1. Kết nối connector **Canva** trong Cowork.
2. Tạo **Brand Kit EduTechND** trong Canva (tài khoản đang có brand kit id `kAHLq3RErqs`):
   - Brand Colors: `#4B2E2B`, `#8C5A3C`, `#FFF8F0`, và accent theo môn (`#D98E48` Lý, `#6FA89C` Hóa,
     `#8FAE5D` Sinh, `#C08552` chung).
   - Brand fonts: **upload font 9Slide** (cần Canva Pro). Tiêu đề bộ "Tieu de", nội dung bộ "Noi dung".
3. (Khuyến nghị) Tạo **Brand Template** EduTechND nền tối để tạo nhanh và đồng nhất.

> Canva MCP **không đổi font-family qua API** → font 9Slide phải nằm sẵn trong Brand Kit/Template thì mới áp đúng.

## Luồng tạo bài giảng (Canva MCP)
```
list-brand-kits
→ request-outline-review (brand_kit_id, pages[])     # bạn duyệt outline trong widget
→ [tuỳ chọn] upload-asset-from-url (ảnh bạn đề xuất)
→ generate-design-structured (brand_kit_id, outlines, asset_ids)   # hoặc create-design-from-brand-template
→ start/perform/commit-editing-transaction (tinh chỉnh màu/chữ/bố cục, chèn icon)
→ get-export-formats → export-design (pptx/pdf) → nhận URL tải về
```
Chi tiết: `references/canva-workflow.md`.

## Cách dùng
Nhập, ví dụ: *"Thiết kế bài giảng Quang hợp, Sinh học lớp 7, 45 phút, dùng Brand Kit EduTechND"* —
skill sẽ: dựng outline → bạn duyệt → tạo design trong Canva (accent xanh lá olive, font 9Slide) →
chèn icon/ảnh phù hợp (lá, mặt trời, sơ đồ quang hợp…) → export.

## Đã bỏ so với bản trước
- Bỏ generator python-pptx (`build_lesson_template.py`) và thư viện icon vector (`icons.py`) cùng file
  .pptx sinh bằng code — theo đúng yêu cầu **không tạo pptx bằng ngôn ngữ lập trình**. Mọi thứ chuyển sang Canva.
