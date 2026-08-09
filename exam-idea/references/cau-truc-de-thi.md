# Cấu trúc đề và thang điểm

## 1. Bốn loại câu hỏi

| Loại | Tên | Ký hiệu nhóm trong JSON | Đơn vị đếm |
|------|-----|--------------------------|------------|
| 1 | Trắc nghiệm nhiều lựa chọn (A, B, C, D — chọn 1) | `TN` | câu = 1 lệnh hỏi |
| 2 | Trắc nghiệm đúng/sai (4 ý a, b, c, d) | `DS` | câu = **4 lệnh hỏi** |
| 3 | Trắc nghiệm trả lời ngắn (đáp án là số) | `TLN` | câu = 1 lệnh hỏi |
| 4 | Tự luận (2 ý a, b) | `TL` | câu = **2 lệnh hỏi** |

Nhóm cha: loại 1, 2, 3 thuộc **TNKQ**; loại 4 thuộc **Tự luận**. Đây là cấu
trúc gộp ô của hai dòng tiêu đề trong form mẫu.

## 2. Các cấu trúc đề thông dụng

### 2.1 Đề 45 phút — 12 / 4 / 2 / 3 (dùng trong bộ đề mẫu)

| Loại | Số câu | Điểm/lệnh hỏi | Lệnh hỏi | Điểm |
|------|--------|---------------|----------|------|
| 1 | 12 | 0,25 | 12 | 3,0 |
| 2 | 4 | 0,25 | 16 | 4,0 |
| 3 | 2 | 0,5 | 2 | 1,0 |
| 4 | 3 (×2 ý) | tường minh | 6 | 2,0 |
| **Tổng** | **21 câu** | | **36** | **10,0** |

### 2.2 Đề 45 phút — 16 / 2 / 2 / 2 (nặng trắc nghiệm)

| Loại | Số câu | Điểm/lệnh hỏi | Lệnh hỏi | Điểm |
|------|--------|---------------|----------|------|
| 1 | 16 | 0,25 | 16 | 4,0 |
| 2 | 2 | 0,25 | 8 | 2,0 |
| 3 | 2 | 0,5 | 2 | 1,0 |
| 4 | 2 (×2 ý) | tường minh | 4 | 3,0 |
| **Tổng** | | | **30** | **10,0** |

### 2.3 Đề 90 phút — 18 / 4 / 6 / 4 (theo cấu trúc THPT 2025)

| Loại | Số câu | Điểm/lệnh hỏi | Lệnh hỏi | Điểm |
|------|--------|---------------|----------|------|
| 1 | 18 | 0,25 | 18 | 4,5 |
| 2 | 4 | 0,25 | 16 | 4,0 |
| 3 | 6 | 0,25 | 6 | 1,5 |
| 4 | — | — | — | — |
| **Tổng** | | | **40** | **10,0** |

### 2.4 Đề tự luận thuần (kiểm tra thường xuyên)

Chỉ dùng nhóm `TL`, mỗi câu khai `diem` tường minh, tổng 10,0.

## 3. Thang điểm câu loại 2 — hai cách tính

### Cách A — tính theo ý (skill này dùng mặc định)

Mỗi ý đúng được `diem_moi_lenh` điểm (thường 0,25). Câu 4 ý = 1,0 điểm.
Ưu điểm: ma trận và đặc tả đếm thẳng theo lệnh hỏi, cộng điểm tuyến tính,
dễ khớp tỉ lệ mức độ.

### Cách B — tính lũy tiến (như đề THPT quốc gia)

| Số ý đúng | 1 | 2 | 3 | 4 |
|-----------|---|---|---|---|
| Điểm | 0,1 | 0,25 | 0,5 | 1,0 |

Nếu người dùng yêu cầu cách B: vẫn khai `diem_moi_lenh: 0.25` trong ma trận để
tính tỉ lệ mức độ (điểm tối đa của câu vẫn là 1,0), và ghi rõ cách chấm lũy
tiến vào `ghi_chu` của ma trận và `huong_dan` của phần II trong đề.

## 3b. Câu tự luận bắt buộc 2 ý

Mỗi câu loại 4 phải chia thành đúng **2 ý a) và b)**:

- Mỗi ý là **1 lệnh hỏi độc lập**, có `muc_do` và `diem` riêng
- Hai ý có thể ở hai mức độ khác nhau — dùng để tinh chỉnh tỉ lệ
- Tổng điểm 2 ý = điểm của câu

Khai báo trong `bang_ma_tran.json`:

```json
"TL": { "LH": 2 }            // 2 lệnh hỏi ở mức Liên hệ thực tế
"diem": { "TL": { "LH": 1.0 } }   // tổng điểm 2 ý = 1,0
```

Nếu hai ý khác mức độ, tách thành hai khoá:

```json
"so_lenh_hoi": { "TL": { "TH": 1, "LH": 1 } },
"diem":        { "TL": { "TH": 0.5, "LH": 0.5 } }
```

## 4. Bố cục đề minh hoạ

```
PHẦN I.   TRẮC NGHIỆM NHIỀU LỰA CHỌN   (n1 câu – x1 điểm)
PHẦN II.  TRẮC NGHIỆM ĐÚNG – SAI       (n2 câu – x2 điểm)
PHẦN III. TRẮC NGHIỆM TRẢ LỜI NGẮN     (n3 câu – x3 điểm)
PHẦN IV.  TỰ LUẬN                      (n4 câu – x4 điểm)
```

Đánh số câu **liên tục** qua các phần (1 → 12 → 13 → 16 → 17 → 18 → 19 → 21).

Mỗi phần có dòng hướng dẫn nêu rõ phạm vi câu và cách tính điểm — script
`de_to_docx.py` đọc từ khoá `huong_dan`.

## 5. Thời lượng khuyến nghị

| Loại câu | Thời gian trung bình |
|----------|----------------------|
| 1 | 1 – 1,5 phút/câu |
| 2 | 3 – 4 phút/câu (4 ý) |
| 3 | 2 – 3 phút/câu |
| 4 | 4 – 8 phút/câu (2 ý) tuỳ điểm |

Kiểm tra: tổng thời gian ước tính không vượt quá thời lượng đề. Đề mẫu
12 / 4 / 2 / 3 ≈ 15 + 14 + 5 + 15 = 49 phút → phù hợp đề 45–50 phút.
