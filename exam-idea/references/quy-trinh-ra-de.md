# Quy trình ra đề — 4 bước bắt buộc

Mỗi khi người dùng đưa ra một chủ đề, thực hiện đúng thứ tự sau. Không được
nhảy bước, không được viết câu hỏi trước khi chốt ma trận.

---

## Bước 0 — Chốt tham số đề (trước khi làm bất cứ việc gì)

Nếu người dùng chưa nói rõ, tự chọn giá trị mặc định và **ghi rõ trong phần
mở đầu tài liệu** để họ biết mà sửa:

| Tham số | Mặc định | Ghi chú |
|---------|----------|---------|
| Môn – lớp | theo yêu cầu | quyết định khung nội dung phải tra |
| Chủ đề / chương | theo yêu cầu | tách thành các **đơn vị kiến thức** (2–6 đơn vị) |
| Thời gian | 45 phút | 45 / 60 / 90 phút |
| Cấu trúc đề | xem `cau-truc-de-thi.md` | số câu từng loại |
| Tỉ lệ mức độ | 40 : 30 : 20 : 10 | NB : TH : VD : LH |
| Tổng điểm | 10,0 | |

**Quy tắc tách đơn vị kiến thức:** mỗi đơn vị tương ứng 1 bài học hoặc 1 cụm
nội dung liền mạch trong SGK; đặt tên có đánh số `1.1.`, `1.2.`, `2.1.`… để
ma trận và đặc tả tham chiếu chính xác.

---

## Bước 1 — Mục tiêu cần đạt

Liệt kê mục tiêu theo **từng chủ đề**, mỗi mục tiêu gắn đúng 1 mức độ.

Nguồn: yêu cầu cần đạt của CT GDPT 2018 môn tương ứng. Diễn đạt lại cho ngắn
gọn nhưng **giữ nguyên động từ mức độ**.

Kiểm tra: mỗi mức độ (NB, TH, VD, LH) đều phải có ít nhất 1 mục tiêu, nếu
không thì đề sẽ không đủ dải mức độ.

Ghi vào `de_bai_tap.json` → `muc_tieu`.

---

## Bước 2 — Hệ thống dạng bài tập

Với **từng loại câu hỏi** (1, 2, 3, 4), đề xuất các *dạng* bám sát từng đơn vị
kiến thức. Xem thư viện mẫu tại `dang-bai-tap.md`.

Mỗi dạng khai báo: `ma` (1.1, 2.3, …), `ten`, `muc_do`, `mo_ta`, và `vi_du`
nếu dạng đó dễ hiểu sai.

**Số lượng khuyến nghị:** 4–6 dạng cho loại 1; 3–5 dạng cho loại 2; 3–4 dạng
cho loại 3; 3–4 dạng cho loại 4. Phủ đủ mọi đơn vị kiến thức và mọi mức độ.

Ghi vào `de_bai_tap.json` → `dang_bai_tap`.

---

## Bước 3 — Ma trận

### 3.1 Quy đổi lệnh hỏi

| Loại | Số lệnh hỏi / câu |
|------|-------------------|
| 1 – Nhiều lựa chọn | 1 |
| 2 – Đúng/Sai | **4** (mỗi ý a, b, c, d là 1 lệnh hỏi) |
| 3 – Trả lời ngắn | 1 |
| 4 – Tự luận | **2** (mỗi ý a, b là 1 lệnh hỏi) |

Vì mỗi câu tự luận bắt buộc có 2 ý, hai ý này **có thể ở hai mức độ khác nhau**
(ví dụ a) Thông hiểu, b) Liên hệ thực tế) — đây là chỗ tinh chỉnh tỉ lệ rất
hiệu quả.

Ma trận & bảng đặc tả **luôn đếm theo lệnh hỏi**, không đếm theo câu.

### 3.2 Chốt thang điểm

Chọn `diem_moi_lenh` cho từng nhóm sao cho tổng bằng đúng tổng điểm.
Nhóm Tự luận thường để `diem_moi_lenh: null` và khai `diem` tường minh cho
từng ô, vì mỗi câu tự luận có trọng số khác nhau.

### 3.3 Phân bổ

Lập bảng nháp trước khi ghi JSON:

```
đơn vị × loại × mức độ  →  số lệnh hỏi  →  điểm
```

Sau đó cộng theo 3 chiều và **kiểm tra bằng số học**:

1. Tổng điểm = tổng điểm cấu hình (thường 10,0)
2. Điểm mỗi mức độ / tổng điểm = tỉ lệ yêu cầu (khớp tuyệt đối)
3. Tổng lệnh hỏi mỗi loại = số câu × hệ số quy đổi

Ghi vào `bang_ma_tran.json`.

---

## Bước 4 — Bảng đặc tả

Với mỗi ô có số liệu trong ma trận, viết ra **yêu cầu cần đạt** cụ thể sinh ra
các lệnh hỏi đó.

Ràng buộc cứng:

- Chuỗi `chu_de[].ten` và `noi_dung[].ten` **giống hệt** bên ma trận
- Với mỗi (đơn vị, loại, mức độ): `Σ so_lenh_hoi` của các YCCĐ = ô ma trận
- Mỗi YCCĐ chỉ thuộc **một** mức độ

Ghi vào `bang_dac_ta_ma_tran.json`.

---

## Bước 5 — Đề minh hoạ + kết xuất

Viết câu hỏi đầy đủ (đề, phương án, đáp án, lời giải, hướng dẫn chấm) vào
`de_bai_tap.json` → `de_minh_hoa`, đánh số câu liên tục theo thứ tự
loại 1 → loại 2 → loại 3 → loại 4.

Chạy:

```bash
python scripts/build_all.py output/<TÊN_BỘ_ĐỀ>
```

Chỉ bàn giao khi báo cáo hiện `Tong so loi: 0`.

---

## Danh sách tự kiểm cuối cùng

- [ ] Mỗi mức độ đều có mục tiêu và có câu hỏi tương ứng
- [ ] Số câu từng loại đúng yêu cầu người dùng
- [ ] Tỉ lệ mức độ khớp tuyệt đối, tổng điểm đúng 10,0
- [ ] Ma trận ↔ đặc tả đồng bộ từng ô (validate 0 lỗi)
- [ ] Mỗi câu trong đề trỏ đúng chủ đề / đơn vị / mức độ trong ma trận
- [ ] Câu loại 1 chỉ có 1 đáp án đúng; phương án nhiễu hợp lí
- [ ] Câu loại 2: số ý đúng khác nhau giữa các câu (tránh 4 câu cùng 2 Đ 2 S)
- [ ] Câu loại 3: đáp án là một con số duy nhất
- [ ] Câu loại 4: **đủ 2 ý a), b)**, mỗi ý có mức độ và điểm riêng, có hướng dẫn chấm
- [ ] Mọi dữ kiện khoa học đều chính xác, không bịa
