# Học TikZ theo cách của bạn — bản trích xuất tham chiếu

Nguồn: `HocTikztheocachcuaBan_BuiQuy.pdf` — Bùi Quý, Trung tâm GDNN–GDTX Duy Tiên, 73 trang.

Tách theo **đối tượng cần vẽ** để tra nhanh khi viết mã TikZ.

| File | Nội dung | Trang gốc | Khối code | Ký tự rơi |
|---|---|---|---|---|
| [`01-khai-bao-he-toa-do.md`](01-khai-bao-he-toa-do.md) | Khai báo, môi trường vẽ và hệ trục toạ độ | 4–6 | 9 | — |
| [`02-tinh-toan-toa-do.md`](02-tinh-toan-toa-do.md) | Tham số, hàm tính toán và phép toán trên toạ độ | 6–8 | 11 | — |
| [`03-diem-van-ban-doan-thang.md`](03-diem-van-ban-doan-thang.md) | Vẽ điểm, hiển thị văn bản, đoạn thẳng và đường gấp khúc | 8–11 | 10 | — |
| [`04-duong-tron-cung-duong-cong.md`](04-duong-tron-cung-duong-cong.md) | Đường tròn, ellipse, cung và các dạng đường cong | 11–15 | 17 | — |
| [`05-tiep-tuyen-giao-diem.md`](05-tiep-tuyen-giao-diem.md) | Lấy điểm trên đường cong, tiếp tuyến, giao điểm | 15–20 | 14 | — |
| [`06-scope-clip-node-pic.md`](06-scope-clip-node-pic.md) | Môi trường scope, clip, node và pic | 20–25 | 15 | — |
| [`07-tuy-chon-thuong-dung.md`](07-tuy-chon-thuong-dung.md) | Các tuỳ chọn thường dùng cho đường và node | 25–26 | 1 | — |
| [`08-foreach-macro.md`](08-foreach-macro.md) | Vòng lặp foreach và cách tạo macro | 26–30 | 7 | — |
| [`09-hinh-khong-gian-3d.md`](09-hinh-khong-gian-3d.md) | Vẽ hình không gian (giả 3D) | 30–33 | 5 | — |
| [`10-bang-xet-dau-bien-thien.md`](10-bang-xet-dau-bien-thien.md) | Bảng xét dấu và bảng biến thiên | 33–41 | 20 | — |
| [`11-do-thi-ham-so.md`](11-do-thi-ham-so.md) | Đồ thị hàm số, hệ toạ độ cực | 41–45 | 11 | — |
| [`12-to-mien-do-thi.md`](12-to-mien-do-thi.md) | Vẽ và tô miền đồ thị hàm số | 45–58 | 16 | — |
| [`13-tu-duy-ve-hinh.md`](13-tu-duy-ve-hinh.md) | Tư duy hình hoạ để dựng hình | 58–61 | 0 | — |
| [`14-export-anh-dong.md`](14-export-anh-dong.md) | Export hình ảnh, làm ảnh động PDF và GIF | 61–70 | 9 | — |
| [`15-thu-vien-thuong-dung.md`](15-thu-vien-thuong-dung.md) | Thư viện hay dùng: calc, intersections, angles, patterns, decoration, shadings | 70–73 | 6 | — |

## Hai lưu ý khi dùng bản trích xuất này

1. **Mã LaTeX đã được sửa** chỗ PDF render `--` thành dấu gạch dài, nên copy ra dùng được ngay.
2. **Còn 0 ký tự tiếng Việt bị rơi** trong các khối code — font VNTT của sách không map hết Unicode nên trình đọc PDF nào cũng mất. Chỗ nào bị rơi đã được đánh dấu ⚠️ ngay trên khối code kèm số trang, mở PDF gốc đối chiếu là xong. Phần **mã lệnh TikZ thuần ASCII thì nguyên vẹn** — chỉ nhãn tiếng Việt bên trong `{...}` mới bị.
