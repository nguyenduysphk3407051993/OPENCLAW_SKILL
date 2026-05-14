---
name: mapid-classifier
description: Phân loại và tạo Map ID cho bài tập Hóa học THCS/THPT. Sử dụng khi cần phân tích file PDF bài tập để tạo cấu trúc phân cấp Map ID theo định dạng 6 tham số (Lớp-Môn-Chương-Mức độ-Bài-Dạng). Trigger khi người dùng upload PDF bài tập hoặc yêu cầu tạo Map ID, phân loại câu hỏi, hoặc xây dựng cấu trúc phân cấp cho ngân hàng đề thi.
---

# Map ID Classifier

Skill phân loại bài tập Hóa học và tạo cấu trúc Map ID cho ngân hàng đề thi.

## Quy ước mã hóa

### Cấu trúc Map ID
```
%[<Lớp><Môn><Chương><Mức độ><Bài>-<Dạng>]
```
**Ví dụ:** `%[0H1G3-5]` = Lớp 10, Hóa học, Chương 1, Mức độ Giỏi, Bài 3, Dạng 5

### Bảng mã

| Tham số | Giá trị |
|---------|---------|
| **Lớp** | `6`=Lớp 6, `7`=Lớp 7, `8`=Lớp 8, `9`=Lớp 9, `0`=Lớp 10, `1`=Lớp 11, `2`=Lớp 12 |
| **Môn** | `H`=Hóa học, `K`=Khoa học tự nhiên |
| **Chương** | Số thứ tự: 1-9, vượt quá 9 dùng chữ cái: A=10, B=11, C=12... |
| **Mức độ** | `N`=Nhận biết, `T`=Thông hiểu, `V`=Vận dụng, `G`=Vận dụng cao |
| **Bài** | Số thứ tự bài trong chương: 1-9, vượt quá 9 dùng chữ cái: A=10, B=11... |
| **Dạng** | Số thứ tự dạng trong bài: 1-9, vượt quá 9 dùng chữ cái: A=10, B=11... |

### Định dạng phân cấp

| Cấp | Số dấu `-` | Nội dung |
|-----|------------|----------|
| 1 | 1 | Lớp |
| 2 | 4 | Môn |
| 3 | 7 | Chương/Chuyên đề |
| 4 | 10 | Bài/Chủ đề |
| 5 | 13 | Dạng |

## Quy trình thực hiện

### Bước 1: Đọc PDF và xác định thông tin cơ bản

1. Trích xuất nội dung văn bản từ PDF
2. Xác định:
   - **Lớp**: Từ tiêu đề hoặc nội dung kiến thức
   - **Môn**: Hóa học (H) hoặc KHTN (K)
   - **Chương**: Từ mục lục hoặc tiêu đề chính

### Bước 2: Phân tích cấu trúc nội dung

1. Xác định các **bài/chủ đề** chính trong tài liệu
2. Với mỗi bài, xác định các **dạng bài tập** khác nhau:
   - Dạng lý thuyết
   - Dạng tính toán
   - Dạng giải thích
   - Dạng thực hành/thí nghiệm
   - Dạng vận dụng thực tiễn

### Nguyên tắc dạng bài thực tiễn (Xu hướng Bộ GD&ĐT)

> **QUY TẮC VÀNG:** Bài tập phải SÁT với thực tiễn nhưng KHÔNG được BỊA ĐẶT thực tiễn.

**Tiêu chí đạt chuẩn thực tiễn:**
| ✅ Được phép | ❌ Không được phép |
|-------------|-------------------|
| Hiện tượng tự nhiên có thật, quan sát được | Bịa số liệu không có căn cứ khoa học |
| Tình huống sinh hoạt học sinh thực sự gặp | Tạo tình huống giả tạo, gượng ép |
| Dữ liệu thực tế (giá cả, nhiệt độ, khoảng cách thật) | Số liệu tròn đẹp phi thực tế |
| Ứng dụng công nghệ, sản xuất có thật | Gán ghép kiến thức vào ngữ cảnh không liên quan |
| Vấn đề môi trường, sức khỏe đang xảy ra | Phóng đại hoặc sai lệch thông tin thực tế |

**Các dạng thực tiễn được khuyến khích:**
1. **Giải thích hiện tượng tự nhiên** — hiện tượng học sinh quan sát được hàng ngày
2. **Ứng dụng trong sinh hoạt** — tình huống thật trong gia đình, trường học
3. **Xử lý tình huống thực tế** — tình huống an toàn, sức khỏe, môi trường
4. **Phân tích dữ liệu thực** — bảng biểu, nhãn sản phẩm, bản tin thời tiết
5. **Liên hệ sản xuất, công nghệ** — quy trình sản xuất, thiết bị có thật
6. **Đánh giá, đề xuất giải pháp** — vấn đề cộng đồng, địa phương thực tế

### Bước 3: Tạo cấu trúc phân cấp

Viết output theo format:
```
-[<mã_lớp>] <tên_lớp>

----[<mã_môn>] <tên_môn>

-------[<số_chương>] <tên_chương>

----------[<số_bài>] <tên_bài>

-------------[<số_dạng>] <tên_dạng>
```

**Quy tắc:**
- Luôn có **1 dòng trống** giữa các cấp khác nhau
- Mã trong `[x]` đứng **ngay sau** các dấu `-`
- Tên đầy đủ theo sau mã

### Bước 4: Lưu file output

1. Tạo file với tên: `MapID_<TênChương/TênTàiLiệu>.tex`
2. Lưu vào thư mục: `./output/`
3. Trình bày file cho người dùng download

## Ví dụ output hoàn chỉnh

```markdown
# Map ID - Cấu tạo nguyên tử

-[0] Lớp 10

----[H] Hóa học

-------[1] Cấu tạo nguyên tử

----------[1] Thành phần nguyên tử

-------------[1] Tìm hiểu các loại hạt cấu tạo nên nguyên tử

-------------[2] Kích thước và khối lượng của nguyên tử

----------[2] Nguyên tố hoá học

-------------[1] Hạt nhân nguyên tử

-------------[2] Nguyên tố hoá học

-------------[3] Đồng vị

-------------[4] Nguyên tử khối và nguyên tử khối trung bình
```

## Xử lý trường hợp đặc biệt

| Trường hợp | Cách xử lý |
|------------|------------|
| PDF không rõ lớp/chương | Hỏi người dùng xác nhận trước khi phân loại |
| Bài tập trắc nghiệm lẫn lộn | Gom nhóm theo chủ đề kiến thức, sau đó phân dạng |
| Nhiều chương trong 1 PDF | Liệt kê đầy đủ tất cả, mỗi chương là 1 khối riêng |
| Chỉ có 1 chủ đề nhỏ | Chi tiết hóa đến cấp dạng bài cụ thể |

## Tham khảo cấu trúc mẫu

Xem file `references/hoa-hoc-10.md` để tham khảo cấu trúc chương trình Hóa học lớp 10 đầy đủ.