# Slide Design Framework — chuẩn EduTechND Earth (Dark) trên Canva

Khung chọn bố cục, gam màu, font, cách phân vai hình ảnh/văn bản/hoạt động cho bài giảng KHTN.
Mọi thiết kế tạo **trong Canva** (xem `canva-workflow.md`). **Không dựng .pptx bằng code** — chỉ export từ Canva.

## 1. Gam màu chuẩn (nền tối – chữ sáng, gam vàng đất) — đặt trong Brand Kit

| Vai trò | Hex | Ghi chú |
|---|---|---|
| Nền chủ đạo | `#4B2E2B` | nền mọi slide (60–70%) |
| Khối nền phụ / chú thích | `#8C5A3C` | panel, meta, kẻ mờ |
| Chữ & nét sáng | `#FFF8F0` | tiêu đề, nội dung |
| Accent theo môn (< 10%) | Vật lý `#D98E48` · Hóa `#6FA89C` · Sinh `#8FAE5D` · Chung `#C08552` | 1 điểm dẫn mắt/slide |

Nền + panel + chữ cố định; chỉ accent đổi theo môn. Khai báo đủ các màu này trong **Brand Colors** của Canva.

## 2. Font chuẩn (9Slide) — đặt trong Brand fonts của Brand Kit

Tiêu đề = bộ **"Tieu de"** (serif/display); nội dung = bộ **"Noi dung"** (sans). Giữ tương phản serif↔sans.
- Tiêu đề: `#9Slide01 Tieu de ngan` (≤25 ký tự) · `#9Slide02 Tieu de dai` · `#9Slide02 Tieu de rat dai 01/02`
- Nội dung: `#9Slide01 Noi dung ngan` · `#9Slide02 Noi dung dai` · `#9Slide02 Noi dung rat dai`
- Tối thiểu 24pt khi trình chiếu.
- ⚠️ Canva MCP không đổi font-family qua API → font 9Slide phải **upload sẵn** vào Brand Kit/Template (Canva Pro).

## 3. Sáu mẫu bố cục (mô tả để dựng/đặt trong Canva)

Một deck 6–14 slide nên dùng 5–6 mẫu, không lặp một mẫu:
1. **Cover** — tiêu đề lớn căn trái 1/3 dưới + 1 chi tiết accent (node/đường) + 1 icon chủ đề nửa phải.
2. **Đơn vị kiến thức** — tiêu đề đánh số + 1 ý (text trái ~45%) + icon/ảnh phải ~55% + số mục mờ (panel) ở góc.
3. **Quy trình/sơ đồ** — 3–4 node accent đánh số nối bằng kẻ mảnh, nhãn ngắn dưới mỗi node.
4. **So sánh 2 cột** — 2 panel `#8C5A3C` cân; 1 panel có chi tiết accent làm điểm mấu chốt.
5. **Số liệu nổi bật** — 1 con số accent khổng lồ + caption kem + bối cảnh nâu trung.
6. **Trích dẫn/Kết luận** — dấu ngoặc kép accent + 1 câu chốt kem cỡ lớn + nguồn nâu trung.

Khi tạo bằng `generate-design-structured`, mô tả các mẫu này trong `style`/outline; sau đó tinh chỉnh từng
trang bằng `perform-editing-operations` (format_text, position/resize, update_fill) để đúng bố cục.

## 4. Phân vai hình ảnh – văn bản – hoạt động
- **Hình ảnh:** mỗi slide ≥1 icon/ảnh khớp nội dung (từ khóa ở `visual-keyword-library.json`). Ưu tiên icon
  Canva Elements **một style đồng nhất**, sáng màu hợp nền tối; ảnh người dùng đề xuất → `upload-asset-from-url`.
- **Văn bản:** ngắn gọn ≤6–7 dòng/slide, một ý; phân cấp bằng cỡ + độ đậm trước, rồi mới màu.
- **Hoạt động:** gợi ý 1 tương tác/slide khi hợp (câu hỏi nhanh, dự đoán, so sánh, thí nghiệm mini).

## 5. Khoảng trắng & nhịp
- Khoảng cách đều; lề rộng; nội dung tràn → tách slide, không thu nhỏ chữ quá mức.
- Một motif lặp lại; mỗi slide MỘT đơn vị kiến thức; accent 1 điểm/slide.

## 6. Tạo trong Canva (tóm tắt — chi tiết ở canva-workflow.md)
```
list-brand-kits → request-outline-review (duyệt) → [upload-asset-from-url]
→ generate-design-structured (brand_kit_id, outlines, asset_ids)
→ start/perform/commit-editing-transaction (tinh chỉnh) → get-export-formats → export-design (pptx/pdf)
```

## 7. Checklist QA (xem thumbnail/preview trong Canva)
- [ ] Nền `#4B2E2B`, chữ kem `#FFF8F0` (nền tối – chữ sáng).
- [ ] Font 9Slide; tiêu đề serif, nội dung sans (không Calibri/Cambria).
- [ ] Accent đúng môn và < 10% diện tích.
- [ ] Mỗi slide một đơn vị kiến thức; không tràn chữ; khoảng trắng thoáng.
- [ ] Mỗi slide có icon/ảnh khớp nội dung; icon đồng nhất một style.
- [ ] Dấu tiếng Việt hiển thị đúng.
- [ ] File chỉ tạo bằng export-design (KHÔNG bằng code).
