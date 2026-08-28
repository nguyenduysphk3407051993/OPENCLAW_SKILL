# Quy trình 6 bước đề xuất hệ thống bài tập

Bắt buộc theo đúng thứ tự. Không được nhảy thẳng vào viết bài tập.

---

## Bước 1 — Khoanh vùng kiến thức & viết mục tiêu

**Đầu ra:** danh sách 4–8 mục tiêu, mỗi mục tiêu gắn 1 mức độ NB/TH/VD/VDC.

1. Liệt kê các **đơn vị kiến thức** của chủ đề (bám SGK bộ sách đang dùng và
   yêu cầu cần đạt của CT GDPT 2018).
2. Với mỗi đơn vị kiến thức, viết mục tiêu theo mẫu ở `muc-do-va-dong-tu.md` §4.
3. Đánh mã `MT1`, `MT2`, …

**Chốt chặn:** nếu không nêu được ít nhất 1 mục tiêu ở mức VD hoặc VDC thì chủ đề
đang bị hiểu quá hẹp — mở rộng sang ứng dụng thực tiễn.

---

## Bước 2 — Quét đủ 9 nhóm dạng A → I

**Đầu ra:** bảng bản đồ dạng bài tập.

Đọc `he-thong-dang-bai-tap.md`, đi lần lượt từ A đến I. Với mỗi nhóm:

- Đề xuất **1–3 dạng** cụ thể, đặt tên **bám sát chủ đề** (không copy tên nhóm).
  - ✗ "Dạng C — Tính toán theo công thức"
  - ✓ "C1 — Tính điện trở tương đương của đoạn mạch nối tiếp"
- Gán mã `A1`, `A2`, `B1`, … `I1`.
- Nối mỗi dạng với các mục tiêu ở Bước 1 (`muc_tieu_lien_quan`).

**Nhóm không dùng được thì phải viết một dòng lí do**, ví dụ:
> *Nhóm C (Tính toán): chủ đề "Phân loại thế giới sống" không có nội dung định
> lượng ở lớp 6 → bỏ, thay bằng đếm/thống kê ở nhóm D.*

Đọc thêm `references/mon/<môn>.md` để lấy biến thể đặc thù môn và kho quan niệm
sai (phục vụ nhóm H).

**Chốt chặn:** dưới 7 nhóm được dùng mà không kèm lí do → quay lại Bước 2.

---

## Bước 3 — Viết hồ sơ cho từng dạng

Mỗi dạng phải có đủ **4 mục**, đây là phần giá trị nhất với người học:

| Mục | Nội dung |
|-----|----------|
| **Dấu hiệu nhận biết** | Đề bài có từ khoá/dữ kiện nào thì biết là dạng này |
| **Phương pháp giải** | Các bước đánh số 1., 2., 3. — dùng lại được cho mọi bài cùng dạng |
| **Lỗi thường gặp** | 2–3 lỗi học sinh hay mắc ở đúng dạng này |
| **Lưu ý** *(tuỳ chọn)* | Mẹo nhớ, trường hợp đặc biệt, đơn vị cần cẩn thận |

Phương pháp giải viết ở dạng **mệnh lệnh ngắn**, ví dụ:
> 1. Tóm tắt: ghi các đại lượng đã biết kèm đơn vị.
> 2. Quy đổi về đơn vị chuẩn (mA → A, kΩ → Ω).
> 3. Chọn hệ thức liên hệ; biến đổi để đại lượng cần tìm đứng một mình.
> 4. Thay số, tính, ghi kèm đơn vị.
> 5. Kiểm tra tính hợp lí của kết quả.

---

## Bước 4 — Sinh bài tập phân tầng

Đọc `phan-tang-doi-tuong.md`. Với mỗi dạng:

1. Viết **bài gốc ở tầng ⭐⭐** (tầng chuẩn) trước.
2. Từ bài gốc, dùng bảng kĩ thuật §3 để **hạ xuống ⭐** và **nâng lên ⭐⭐⭐, ⭐⭐⭐⭐**.
3. Mỗi bài bắt buộc có `loi_giai` (các bước) và `dap_an` (kết quả cuối).
4. Số bài mỗi tầng theo tỉ lệ ở `phan-tang-doi-tuong.md` §2 tuỳ `muc_dich`.

**Chốt chặn:** bài ở hai tầng liền nhau chỉ khác nhau con số → chưa phân tầng
thật, làm lại bằng kĩ thuật khác.

---

## Bước 5 — Lộ trình luyện tập

**Đầu ra:** bảng gợi ý thứ tự luyện, để giáo viên/học sinh biết học theo trình tự nào.

- Nhóm dạng theo **buổi/phiên** (mỗi buổi 1–3 dạng liên quan).
- Nguyên tắc thứ tự: **A → B → C/D → E/F → G/H → I**. Không cho học sinh làm G
  (thực tiễn) khi chưa vững A, C.
- Mỗi buổi ghi: dạng nào · số bài · tầng nào · mốc tự đánh giá ("làm đúng 4/5 bài
  tầng ⭐⭐ mới sang buổi sau").

---

## Bước 6 — Kết xuất & kiểm tra

1. Xác định dạng đầu ra theo bảng **CHỌN DẠNG ĐẦU RA** trong `SKILL.md`.
2. Nếu ghi file: viết `he_thong_bai_tap.json` vào `output/<MÔN><LỚP>_<CHU_DE>/`.
3. Chạy `python scripts/build_all.py "<OUT>"` — bắt buộc PASS cả 2 bước kiểm tra
   trước khi bàn giao.
4. Đối chiếu **Checklist trước khi hoàn thành** trong `SKILL.md`.
5. Báo cáo: liệt kê số dạng theo nhóm, số bài theo tầng, các nhóm đã bỏ + lí do,
   đường dẫn file đã tạo.
