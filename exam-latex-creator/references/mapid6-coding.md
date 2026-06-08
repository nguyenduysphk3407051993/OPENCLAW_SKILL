# Quy tắc mã hóa ID6

## Cấu trúc: `[<Lớp><Môn><Chương><Mức độ><Bài>-<Dạng>]`

Mỗi câu hỏi **bắt buộc** có ID6 đặt sau `\begin{ex}` hoặc `\begin{bt}`:
```latex
\begin{ex}%[6K2N1-1]
```

## Bảng mã hóa

### Lớp (1 ký tự)

| Giá trị | Lớp |
|---------|------|
| 6 | Lớp 6 |
| 7 | Lớp 7 |
| 8 | Lớp 8 |
| 9 | Lớp 9 |
| 0 | Lớp 10 |
| 1 | Lớp 11 |
| 2 | Lớp 12 |

### Môn (1 ký tự)

| Ký hiệu | Môn |
|----------|------|
| K | KHTN (Khoa học tự nhiên) |
| H | Hóa học |
| L | Vật lý |
| S | Sinh học |
| T | Toán |
| V | Ngữ Văn |

### Chương (1 ký tự)

Giá trị: `1-9`, `A-Z` (dùng chữ cái khi chương > 9)

### Mức độ (1 ký tự)

| Ký hiệu | Mức độ |
|----------|--------|
| N | Nhận biết |
| H | Thông hiểu |
| V | Vận dụng |
| C | Vận dụng cao |
| Y | Yếu |
| B | Trung bình |
| K | Khá |
| G | Giỏi |
| T | Thực tế |

### Bài (1 ký tự)

Giá trị: `1-9`, `A-Z`

### Dạng (1 ký tự)

Giá trị: `1-9`

## Ví dụ

| ID6 | Giải mã |
|-----|---------|
| `[6K2N1-1]` | Lớp 6, KHTN, Chương 2, Nhận biết, Bài 1, Dạng 1 |
| `[9K8H9-2]` | Lớp 9, KHTN, Chương 8, Thông hiểu, Bài 9, Dạng 2 |
| `[0H1V3-3]` | Lớp 10, Hóa, Chương 1, Vận dụng, Bài 3, Dạng 3 |
| `[7K5G2-1]` | Lớp 7, KHTN, Chương 5, Giỏi, Bài 2, Dạng 1 |
| `[2H3C1-2]` | Lớp 12, Hóa, Chương 3, Vận dụng cao, Bài 1, Dạng 2 |
