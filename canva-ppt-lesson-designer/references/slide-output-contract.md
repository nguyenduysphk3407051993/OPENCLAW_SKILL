# Slide Output Contract — hợp đồng đầu ra bắt buộc

Tài liệu này chốt **đúng những gì mỗi đầu ra của skill phải có**. Mọi kế hoạch thiết kế bài giảng
(file `.md` hoặc khi dựng trong Canva) đều phải tuân theo hợp đồng này. Nó gắn 3 yêu cầu cốt lõi:

1. **Thiết lập chung cho cả deck** (màu, font, bộ màu thương hiệu, quy tắc thiết kế chuyên nghiệp).
2. **Mỗi slide có bộ từ khóa hình ảnh / icon / shape.**
3. **Nội dung text bám sát từng đơn vị bài học, súc tích, dễ hiểu** (lấy từ `references/maps/`).

---

## PHẦN A — Thiết lập chung (1 lần, đặt ở đầu đầu ra)

Trước danh sách slide, LUÔN xuất một khối **"Thiết lập chung của deck"** gồm:

### A1. Hệ màu thương hiệu (đọc `assets/brand-standard.json`)
- **Nền chủ đạo** (60–70% diện tích): `#4B2E2B`
- **Panel / khối nền phụ**: `#8C5A3C`
- **Chữ & nét sáng**: `#FFF8F0`
- **Accent theo môn** (< 10% diện tích, 1 điểm/slide):
  Vật lý `#D98E48` · Hóa `#6FA89C` · Sinh `#8FAE5D` · Chung/STEM `#C08552`
- Quy tắc vai trò màu: Dominant 60–70% · Supporting 1–2 tone · Accent 1 màu, dùng ít.
  **Không bao giờ chia đều màu.** Không thêm màu ngoài bộ trên.

### A2. Font (đọc `assets/brand-standard.json` → `fonts`, `font_rules`)
- Tiêu đề = bộ **"Tieu de"** (vai trò serif/display): `#9Slide01 Tieu de ngan` (≤25 ký tự),
  `#9Slide02 Tieu de dai`, `#9Slide02 Tieu de rat dai 01/02`.
- Nội dung = bộ **"Noi dung"** (vai trò sans): `#9Slide01 Noi dung ngan`,
  `#9Slide02 Noi dung dai`, `#9Slide02 Noi dung rat dai`.
- **Chọn font theo độ dài chuỗi** (xem `font_rules`). Tối thiểu 24pt khi trình chiếu.
- Heading LUÔN bold, body LUÔN regular; chỉ bold cụm cần nhấn trong body.
- Giữ tương phản serif ↔ sans giữa tiêu đề và nội dung (không dùng chung một bộ).

### A3. Quy tắc thiết kế chuyên nghiệp (nghệ thuật layout + sắp chữ)
- **Phân cấp typography**: tỉ lệ size giữa các tầng ≥ 1.3×. Dùng độ đậm/cỡ trước, rồi mới tới màu.
- **Nghệ thuật xếp layout**: mỗi slide dùng 1 trong 6 mẫu bố cục (Cover, Đơn vị kiến thức,
  Quy trình/sơ đồ, So sánh 2 cột, Số liệu nổi bật, Trích dẫn/Kết luận — xem
  `slide-design-framework.md`). Một deck 6–14 slide nên dùng 5–6 mẫu, **không lặp một mẫu**.
- **Sắp chữ**: căn trái cho body & bullet; chỉ tiêu đề / số lớn / kết luận mới căn giữa.
- **Khoảng trắng & nhịp**: chọn đơn vị gap 0.3" hoặc 0.5", dùng nhất quán; lề tối thiểu 0.5"/cạnh.
- **Một motif lặp lại** cho cả deck; mỗi slide MỘT đơn vị kiến thức; accent 1 điểm/slide.
- **Tránh anti-patterns** (đường accent dưới tiêu đề, thanh màu trên/dưới, bevel/shadow, tràn chữ…)
  — xem `references/anti-patterns.md`.

### A4. Khai báo bản đồ bài học đã dùng
Ghi rõ đã tra map nào (vd `references/maps/MAP_KHTN6.md`), Chương/Bài nào → để truy vết nội dung.

---

## PHẦN B — Hợp đồng mỗi slide (lặp lại cho từng slide)

Mỗi slide BẮT BUỘC đủ các mục sau (giữ đúng nhãn để nhất quán & máy đọc được):

```markdown
#### Slide X: [Tiêu đề slide]

**Mục đích slide**
- Dẫn nhập / giải thích / luyện tập / tổng kết / chuyển ý.

**Nội dung chính**  ← BÁM ĐƠN VỊ BÀI HỌC
- 3–6 ý cốt lõi LẤY TỪ `Đơn vị KT` của bài trong map, viết lại súc tích, dễ hiểu.
- Tối đa ~6–7 dòng; một ý chính nổi bật; tránh đoạn văn dài.
- Mỗi ý ≤ ~14 từ; ưu tiên cụm danh từ/động từ rõ ràng, đúng kiến thức lớp.

**Bố cục đề xuất**
- Tên 1 trong 6 mẫu bố cục + mô tả vị trí khối (text trái/phải %, panel, số mục mờ…).

**Bộ từ khóa hình ảnh / icon / shape**  ← BẮT BUỘC ĐỦ 3 NHÓM
- `Hình ảnh (ảnh/illustration)`: mô tả tiếng Việt + ≥ 3 từ khóa EN.
- `Icon`: icon_id gợi ý + ≥ 3 từ khóa EN (giữ MỘT style icon cho cả deck: flat hoặc line).
- `Shape`: hình khối nền/trang trí gợi ý (vd circle + orbit, teardrop, gear, sine wave…).
- Nguồn: Canva Elements (ưu tiên) → ảnh người dùng đề xuất (`upload-asset-from-url`) → Canva Photos.
- Tra `assets/visual-keyword-library.json` theo `Visual` key của bài; không khớp → `fallback`.
- Vị trí + kích thước tương đối trên slide; Alt text ngắn tiếng Việt; phương án thay thế.

**Gợi ý video**
- Nếu không cần: ghi `Không cần video`. Nếu cần: loại, mục đích, thời lượng, từ khóa EN, nguồn,
  cách dùng trong lớp, lưu ý bản quyền/kỹ thuật.

**Màu sắc & font**
- Nền `#4B2E2B`, chữ `#FFF8F0`; accent đúng môn (< 10%). Nêu font tiêu đề & body theo `font_rules`.

**Hoạt động tương tác**
- 1 tương tác khi hợp (câu hỏi nhanh, dự đoán, so sánh, thí nghiệm mini…), hoặc `Không bắt buộc`.

**Ghi chú giảng viên**
- Điểm nhấn khi nói, lỗi học sinh hay gặp, mẹo chuyển sang slide sau.
```

---

## PHẦN C — Checklist nghiệm thu đầu ra

- [ ] Có khối "Thiết lập chung" (A1 màu + A2 font + A3 quy tắc + A4 map đã dùng) ở đầu.
- [ ] Mỗi slide đủ 8 mục của hợp đồng PHẦN B.
- [ ] **Nội dung chính của mỗi slide truy được về `Đơn vị KT`** của bài trong `references/maps/`.
- [ ] Mỗi slide có đủ **3 nhóm từ khóa: hình ảnh + icon + shape**.
- [ ] Màu chỉ trong bộ thương hiệu; accent đúng môn & < 10%; font đúng bộ 9Slide.
- [ ] Mỗi slide một đơn vị kiến thức; không tràn chữ; căn trái body; khoảng trắng thoáng.
- [ ] Không vi phạm `anti-patterns.md`.
- [ ] (Nếu xuất file) lưu `.md` theo mẫu tên trong SKILL.md; (nếu dựng) chỉ export từ Canva.
