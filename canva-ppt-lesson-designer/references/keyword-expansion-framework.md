# Keyword Expansion Framework (chủ đề → từ khóa → hình ảnh trên Canva)

Mục tiêu: từ một CHỦ ĐỀ bài giảng KHTN, sinh bộ **từ khóa chính xác** để chọn **icon/ảnh trên Canva**
(Elements, hoặc ảnh người dùng đề xuất), rồi đặt vào design đúng gam màu + font chuẩn (xem
`slide-design-framework.md`, `canva-workflow.md`, `assets/brand-standard.json`).

Từ khóa tìm ảnh viết bằng **tiếng Anh**; mô tả/giải thích bằng tiếng Việt.

## 1. Quy trình 5 bước
1. **Chuẩn hoá chủ đề.** Bỏ dấu, viết thường; tách thành các *đơn vị kiến thức* — mỗi đơn vị 1 slide.
2. **Xác định môn** (Vật lý/Hóa/Sinh/KHTN) → chọn **accent màu** theo môn (`brand-standard.json → subject_accents`).
3. **Dò thư viện** `assets/visual-keyword-library.json`: mỗi slide lấy mô tả VI + từ khóa EN khớp nội dung.
4. **Mở rộng từ khóa** (mục 3 dưới): chủ thể chính / icon bổ trợ / background / video.
5. **Áp vào Canva:** dùng từ khóa để (a) chọn icon Canva Elements giữ một style, hoặc (b) chuẩn bị ảnh người
   dùng đề xuất để `upload-asset-from-url`. Ghi đủ trong kế hoạch .md: mô tả VI, ≥5 từ khóa EN, nguồn, phương án thay thế.

## 2. Bộ từ khóa lõi theo môn KHTN

### Vật lý (accent hổ phách)
- Lực/chuyển động: `force arrow icon`, `motion vector flat icon`, `push pull diagram`, `velocity arrow`
- Điện/năng lượng: `lightning bolt icon`, `electric circuit flat icon`, `energy power line icon`
- Từ/nam châm: `horseshoe magnet icon`, `magnetic field lines`, `magnet poles diagram`
- Nhiệt: `thermometer icon`, `heat transfer flat icon`, `temperature scale`
- Ánh sáng/quang: `light ray icon`, `lens refraction diagram`, `sunlight beam flat icon`
- Âm/sóng: `sound wave icon`, `frequency wave line icon`, `vibration diagram`
- Máy/cơ: `gear icon`, `simple machine lever`, `pulley diagram flat icon`

### Hóa học (accent xanh đồng ấm)
- Nguyên tử/phân tử: `atom structure icon`, `molecule model flat`, `chemical bond icon`
- Phản ứng/thí nghiệm: `beaker icon`, `erlenmeyer flask line icon`, `test tube reaction`, `lab safety`
- Dung dịch/chất: `water drop icon`, `solution liquid flat icon`, `pH scale acid base`
- Bảng tuần hoàn: `periodic table icon`, `chemical element tile`, `mendeleev table flat`

### Sinh học (accent xanh lá olive)
- Tế bào: `cell biology icon`, `plant cell diagram`, `nucleus organelle flat icon`
- Thực vật/quang hợp: `leaf icon`, `photosynthesis diagram`, `green plant flat icon`, `chloroplast`
- Sinh trưởng: `plant growth stages`, `seedling sprout icon`, `germination diagram`
- Di truyền: `dna double helix icon`, `gene chromosome flat icon`, `heredity diagram`
- Sinh thái: `ecosystem cycle icon`, `food chain flat icon`, `water cycle diagram`
- Cơ thể người: `human body system icon`, `organ anatomy flat icon`, `circulatory system`

### KHTN chung / sư phạm
- Mục tiêu: `target goal icon`; Kiến thức: `open book icon`; Tìm hiểu: `magnifier search icon`
- Quy trình: `process steps icon`, `flow arrows`; So sánh: `balance scale icon`, `versus compare`

## 3. Bốn trục mở rộng từ khóa

| Trục | Câu hỏi | Ví dụ thêm |
|---|---|---|
| Chủ thể chính | Vẽ cái gì? | `atom`, `leaf`, `force arrow`, `beaker` |
| Style icon | Đồng bộ? | `flat icon`, `line icon`, `outline`, `duotone`, `minimal` |
| Hành động/ngữ cảnh | Đang làm gì? | `experiment`, `growing`, `colliding`, `reacting` |
| Nền | Hợp nền tối? | `dark background`, `brown earth tone`, `transparent png` |

**Quy tắc style:** chọn MỘT style icon (flat/line/duotone) cho cả deck; vì nền tối, ưu tiên icon sáng màu
hoặc đổi được sang kem/accent; tránh icon nền trắng đặc.

## 4. Chất lượng từ khóa
- Không dùng từ chung chung (`beautiful image`, `nice icon`). Mỗi cụm 2–6 từ, có ngữ cảnh.
- Mỗi slide ≥5 cụm EN + 1 alt VI ngắn. Luôn có phương án thay thế.

## 5. Áp dụng trong Canva (không dùng code)
- **Icon Canva Elements:** dùng bộ từ khóa trên để chọn/kéo icon (giữ một style); hoặc để
  `generate-design-structured` tự chọn element theo outline/style rồi tinh chỉnh bằng `perform-editing-operations`.
- **Ảnh người dùng đề xuất:** có URL → `upload-asset-from-url` → chèn qua `asset_ids` hoặc `update_fill/insert_fill`.
- Toàn bộ đặt màu/chữ theo Brand Kit EduTechND. **Không sinh .pptx bằng code** — chỉ `export-design` từ Canva.
