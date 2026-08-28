# Cấu trúc `he_thong_bai_tap.json`

File JSON là **nguồn duy nhất**: sửa JSON rồi chạy lại `build_all.py` là ra file
Word mới, không bao giờ mất định dạng. Schema kiểm tra cú pháp:
`schemas/he_thong_bai_tap.schema.json`. Bản mẫu đầy đủ đã chạy được:
`output/VATLI9_DinhLuatOhm/he_thong_bai_tap.json`.

Schema đặt `additionalProperties: false` — **thêm khoá lạ sẽ báo lỗi**. Chỉ dùng
đúng các khoá dưới đây.

## Khung tổng thể

```json
{
  "cau_hinh":     { ... },
  "muc_tieu":     [ ... ],
  "nhom_bo_qua":  [ ... ],
  "dang_bai_tap": [ ... ],
  "lo_trinh":     [ ... ]
}
```

Bắt buộc: `cau_hinh`, `muc_tieu`, `dang_bai_tap`. Hai khoá còn lại tuỳ chọn
(nhưng `nhom_bo_qua` trở thành bắt buộc nếu có nhóm A–I không dùng).

## `cau_hinh`

| Khoá | Kiểu | Bắt buộc | Ghi chú |
|------|------|----------|---------|
| `mon` | string | ✔ | "Vật lí", "Hoá học", "Khoa học tự nhiên", "Toán"… |
| `lop` | int 1–12 | ✔ | |
| `chu_de` | string | ✔ | Tên chủ đề, dùng làm tiêu đề file Word |
| `bo_sach` | string | | "Kết nối tri thức", "Chân trời sáng tạo", "Cánh Diều" |
| `muc_dich` | enum | | `phu_dao` · `on_tap` (mặc định) · `on_thi` · `boi_duong` |
| `tang` | array int 1–4 | | Các tầng độ khó sẽ có bài. Mặc định `[1,2,3,4]` |
| `ghi_chu` | string | | |

## `muc_tieu[]`

| Khoá | Kiểu | Bắt buộc | Ghi chú |
|------|------|----------|---------|
| `ma` | `MT<số>` | ✔ | `MT1`, `MT2`… |
| `noi_dung` | string | ✔ | Bắt đầu bằng động từ đúng mức độ |
| `muc_do` | `NB`/`TH`/`VD`/`VDC` | ✔ | |

## `nhom_bo_qua[]`

Khai báo nhóm A–I **không dùng** cho chủ đề này, kèm lí do. Nếu bỏ nhóm mà không
khai ở đây, `validate.py` sẽ báo lỗi.

```json
{ "nhom": "C", "ly_do": "Chủ đề Phân loại thế giới sống ở lớp 6 không có nội dung định lượng." }
```

## `dang_bai_tap[]`

| Khoá | Kiểu | Bắt buộc | Ghi chú |
|------|------|----------|---------|
| `ma` | `<A-I><số>` | ✔ | `A1`, `C2`, `G1`… — duy nhất trong file |
| `nhom` | A–I | ✔ | Phải khớp chữ cái đầu của `ma` (nên giữ nhất quán) |
| `ten` | string | ✔ | Đặt tên **bám sát chủ đề**, không copy tên nhóm |
| `muc_tieu_lien_quan` | array `MT<số>` | | Phải trỏ tới mục tiêu có thật |
| `dau_hieu_nhan_biet` | string | | Đề có dấu hiệu gì thì biết là dạng này |
| `phuong_phap` | array string | ✔ | Các bước giải, mỗi phần tử một bước |
| `loi_thuong_gap` | array string | | 2–3 lỗi học sinh hay mắc |
| `luu_y` | string | | |
| `bai_tap` | array | ✔ | ≥1 phần tử |

## `dang_bai_tap[].bai_tap[]`

| Khoá | Kiểu | Bắt buộc | Ghi chú |
|------|------|----------|---------|
| `ma` | string | | `C1.3` — tiện đối chiếu |
| `tang` | int 1–4 | ✔ | ⭐ · ⭐⭐ · ⭐⭐⭐ · ⭐⭐⭐⭐ |
| `muc_do` | `NB`/`TH`/`VD`/`VDC` | | `validate.py` cảnh báo nếu lệch tầng |
| `hinh_thuc` | enum | | `tu_luan` · `trac_nghiem` · `dung_sai` · `tra_loi_ngan` · `dien_khuyet` · `noi_cot` · `thuc_hanh` |
| `de` | string | ✔ | |
| `phuong_an` | array string | | **Bắt buộc 4 phần tử** khi `hinh_thuc = trac_nghiem` |
| `loi_giai` | string | ✔ | Trình bày theo bước; không được để "TODO", "..." |
| `dap_an` | string | ✔ | Kết quả cuối; với trắc nghiệm ghi "A"/"B"/"C"/"D" |

## `lo_trinh[]`

| Khoá | Kiểu | Bắt buộc | Ghi chú |
|------|------|----------|---------|
| `buoi` | int ≥1 | ✔ | |
| `ten` | string | | Tên buổi luyện |
| `dang` | array mã dạng | ✔ | Phải trỏ tới dạng có thật |
| `so_bai` | int | | Số bài gợi ý làm trong buổi |
| `moc_danh_gia` | string | | Điều kiện để sang buổi sau |

## Những gì `validate.py` bắt (mà schema không bắt)

1. Mã dạng trùng nhau
2. Nhóm A–I bị bỏ mà không khai lí do; hoặc vừa có dạng vừa khai bỏ
3. `muc_tieu_lien_quan` trỏ tới mục tiêu không tồn tại
4. Mục tiêu không được dạng nào phủ *(cảnh báo)*
5. `loi_giai` / `dap_an` / `de` rỗng hoặc còn "TODO", "..."
6. Tầng khai trong `cau_hinh.tang` nhưng không có bài nào
7. Dạng chỉ có bài ở đúng 1 tầng khi khai ≥3 tầng *(cảnh báo)*
8. Bài `trac_nghiem` thiếu phương án
9. `lo_trinh` trỏ tới mã dạng không tồn tại
10. Mức độ lệch tầng, ví dụ `VDC` ở tầng 1 *(cảnh báo)*

Cảnh báo không làm fail; **lỗi thì fail và không xuất docx**.
