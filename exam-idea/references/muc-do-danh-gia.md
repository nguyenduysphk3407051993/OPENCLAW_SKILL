# Mức độ đánh giá và cách phân bổ điểm

## 1. Bốn mức độ dùng trong skill

| Mã | Tên đầy đủ | Tên ngắn (dùng trong bảng) | Bản chất |
|----|------------|----------------------------|----------|
| `NB` | Nhận biết | Biết | Tái hiện, nhắc lại kiến thức đã học đúng như SGK |
| `TH` | Thông hiểu | Hiểu | Diễn đạt lại bằng cách khác, phân biệt, so sánh, giải thích trong tình huống quen |
| `VD` | Vận dụng | Vận dụng | Dùng kiến thức giải quyết tình huống mới nhưng vẫn trong phạm vi học thuật |
| `LH` | Liên hệ thực tế | Liên hệ | Giải thích hiện tượng đời sống, đề xuất giải pháp, đánh giá tác động thực tiễn |

> Form mẫu gốc theo Công văn 7991 chỉ có **3 mức** (Biết – Hiểu – Vận dụng),
> trong đó "Vận dụng" đã bao hàm liên hệ thực tiễn. Skill này cho phép cấu
> hình **3 hoặc 4 mức** qua khoá `cau_hinh.muc_do`; script tự giãn số cột.
> Chỉ tách `LH` thành mức riêng khi người dùng yêu cầu tỉ lệ 4 con số.

## 2. Động từ đặc trưng — chọn đúng động từ là chọn đúng mức độ

| Mức độ | Động từ nên dùng | Động từ KHÔNG được dùng |
|--------|------------------|-------------------------|
| NB | nêu, kể tên, liệt kê, nhận ra, chỉ ra, phát biểu, trình bày (theo SGK) | giải thích, phân tích, đề xuất |
| TH | phân biệt, so sánh, giải thích, xác định, sắp xếp, phân loại, mô tả bằng lời của mình | nêu, kể tên (quá thấp); đề xuất (quá cao) |
| VD | vận dụng, tính, dự đoán, tiến hành, thiết kế, lựa chọn, giải quyết bài toán | nêu, trình bày |
| LH | liên hệ, đề xuất, đánh giá, phản biện, giải quyết tình huống thực tiễn, đưa ra khuyến nghị | nêu, phân biệt |

**Bẫy thường gặp:** viết "Nêu 3 quy tắc an toàn" rồi xếp vào Thông hiểu — sai,
đó là Nhận biết. Muốn lên Thông hiểu phải hỏi "**Giải thích vì sao** phải…".

## 3. Bảng tỉ lệ thông dụng

| Kiểu đề | NB | TH | VD | LH | Ghi chú |
|---------|----|----|----|----|---------|
| Kiểm tra thường xuyên (15 phút) | 50% | 30% | 10% | 10% | củng cố kiến thức nền |
| Kiểm tra giữa kì | 40% | 30% | 20% | 10% | phổ biến nhất |
| Kiểm tra cuối kì | 40% | 30% | 20% | 10% | |
| Đề chọn HSG / nâng cao | 20% | 30% | 30% | 20% | |

Tỉ lệ tính trên **điểm**, không phải trên số câu.

## 4. Kỹ thuật đạt tỉ lệ khớp tuyệt đối

Bài toán: cho trước số câu từng loại và tỉ lệ mức độ, tìm cách phân bổ.

### 4.1 Chọn thang điểm trước

Ví dụ đề 12 – 4 – 2 – 3 (loại 1 – 2 – 3 – 4), tổng 10,0:

| Loại | Số câu | Điểm/lệnh hỏi | Số lệnh hỏi | Tổng điểm |
|------|--------|---------------|-------------|-----------|
| 1 | 12 | 0,25 | 12 | 3,0 |
| 2 | 4 | 0,25 (mỗi ý) | 16 | 4,0 |
| 3 | 2 | 0,5 | 2 | 1,0 |
| 4 | 3 (mỗi câu 2 ý a, b) | khai tường minh | 6 | 2,0 |
| | | | **36** | **10,0** |

### 4.2 Rải mức độ để đạt đúng tỉ lệ

Với tỉ lệ 50 : 30 : 10 : 10 → cần 5,0 / 3,0 / 1,0 / 1,0 điểm.

| Mức độ | Loại 1 | Loại 2 (ý) | Loại 3 | Loại 4 (ý) | Tổng điểm |
|--------|--------|------------|--------|------------|-----------|
| NB | 8 câu = 2,0 | 10 ý = 2,5 | 1 câu = 0,5 | – | **5,0** |
| TH | 4 câu = 1,0 | 4 ý = 1,0 | 1 câu = 0,5 | 2 ý = 0,5 | **3,0** |
| VD | – | 2 ý = 0,5 | – | 2 ý = 0,5 | **1,0** |
| LH | – | – | – | 2 ý = 1,0 | **1,0** |
| **Tổng** | 12 câu / 3,0 | 16 ý / 4,0 | 2 câu / 1,0 | 6 ý / 2,0 | **10,0** |

Đây chính là ma trận của bộ đề mẫu `output/KHTN6_MoDau_DaDangChat/`.

### 4.3 Mẹo tinh chỉnh

- Câu loại 1 là "tiền lẻ": mỗi câu chỉ 0,25 điểm → dùng để bù trừ khi lệch.
- Câu loại 2 rất mạnh: 4 ý của **cùng một câu** có thể thuộc **các mức độ khác
  nhau**. Đây là công cụ chính để đẩy tỉ lệ NB lên cao mà không cần thêm câu.
- Câu loại 4 gánh phần VD và LH. Mỗi câu tự luận có **2 ý a), b) = 2 lệnh hỏi**,
  hai ý có thể ở hai mức độ khác nhau → thêm một nấc tinh chỉnh nữa.
- Nếu tỉ lệ vẫn lệch, ưu tiên đổi phân bố ý của câu loại 2 trước khi đổi số câu.

## 5. Phân bố mức độ trong một câu loại 2

Khuyến nghị mỗi câu loại 2 sắp 4 ý theo độ khó tăng dần, ví dụ:

- a) NB — kiểm tra định nghĩa
- b) NB — kiểm tra một quan niệm sai phổ biến
- c) TH — so sánh / suy luận một bước
- d) VD hoặc LH — tình huống thực tế, bác bỏ cách giải thích sai

Số ý đúng phải **khác nhau giữa các câu** trong cùng đề (ví dụ 2Đ, 3Đ, 2Đ, 2Đ
là chấp nhận được; cả 4 câu đều 2Đ–2S là dấu hiệu đề kém).
