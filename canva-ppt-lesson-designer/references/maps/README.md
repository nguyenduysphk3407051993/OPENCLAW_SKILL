# references/maps — Bản đồ bài học (lesson maps)

Thư mục này chứa các **bản đồ bài học** theo môn/lớp, giúp nội dung mỗi slide **bám sát từng đơn vị
bài học** của chương trình GDPT 2018 (thay vì để skill tự bịa). Đây là tương đương "MAPID" của skill
exam-latex-creator, nhưng định hướng **slide** thay vì câu hỏi.

Định dạng chuẩn của một file map: xem `../lesson-map-format.md`.

## Index các map

| File | Môn / Lớp | Trạng thái | Phạm vi |
|---|---|---|---|
| `MAP_KHTN6.md` | KHTN lớp 6 | ✅ Đầy đủ | 11 chương, toàn bộ bài |
| `MAP_KHTN7.md` | KHTN lớp 7 | 🟡 Khung | Header + cấu trúc, cần seed nội dung |
| `MAP_KHTN8.md` | KHTN lớp 8 | 🟡 Khung | Header + cấu trúc, cần seed nội dung |
| `MAP_KHTN9.md` | KHTN lớp 9 | 🟡 Khung | Header + cấu trúc, cần seed nội dung |

## Cách dùng (trong quy trình skill)

1. Xác định **môn + lớp** từ yêu cầu người dùng → mở `MAP_<MÔN><LỚP>.md`.
2. Tìm **Chương → Bài** chứa chủ đề người dùng yêu cầu.
3. Lấy danh sách `Đơn vị KT` của bài làm **outline nội dung slide** (mỗi đơn vị → 1 slide/khối).
4. Dùng `Trọng tâm` để chọn slide cần nhấn mạnh; `Liên hệ` để mở đầu/hoạt động.
5. Dùng `Visual` (key) tra `assets/visual-keyword-library.json` để lấy bộ từ khóa ảnh/icon/shape.
6. Dùng `Accent` để chọn màu nhấn theo môn con (tra `assets/brand-standard.json`).

## Thêm map mới

Làm theo mục 4 trong `../lesson-map-format.md`, rồi thêm một dòng vào bảng Index ở trên.
