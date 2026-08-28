# Bắt cầu sang các skill khác trong repo

Skill này **chỉ sinh nội dung** (dạng bài tập + bài tập phân tầng + lời giải) và
kết xuất Word. Mọi định dạng khác đều bàn giao sang skill chuyên trách — không
tự làm lại.

## Bảng chuyển giao

| Người dùng muốn | Skill nhận | Bàn giao cái gì |
|-----------------|-----------|-----------------|
| Đề kiểm tra + **ma trận** + **bảng đặc tả** đúng Công văn 7991 | `exam-idea` | Danh sách mục tiêu + bản đồ dạng bài tập (mục 1 dưới đây) |
| File **.tex / PDF** đẹp, có lời giải tách riêng | `exam-latex-creator` | Từng bài tập ở form câu hỏi loại 1–4 (mục 2) |
| File **.docx đề thi** đúng form tab/indent | `exam-docx-creator` | Như trên |
| **Đề cương** ôn tập cả học kì (KHTN, LaTeX) | `de-cuong-khtn-creator` | Hệ thống dạng theo từng bài |
| **Kế hoạch bài dạy / giáo án** dùng hệ bài tập này | `stem-lesson-creator`, `ke-hoach-day-hoc` | Lộ trình + bài tập theo tầng |

## 1. Chuyển sang `exam-idea`

`exam-idea` cần **mục tiêu** và **hệ thống dạng bài tập** ở Bước 1–2 của nó.
Hai thứ này skill hiện tại đã có sẵn.

Ánh xạ khoá JSON:

| Của skill này | Sang `de_bai_tap.json` của `exam-idea` |
|---------------|----------------------------------------|
| `muc_tieu[].ma / noi_dung / muc_do` | `muc_tieu[]` (giữ nguyên, đổi `VDC` → `VD` hoặc `LH` tuỳ thang 3/4 mức) |
| `dang_bai_tap[].ma / ten` | `dang_bai_tap[].ma / ten` |
| `dang_bai_tap[].dau_hieu_nhan_biet` | `dang_bai_tap[].mo_ta` |
| `bai_tap[]` tầng 1–2 | ví dụ cho loại 1 (trắc nghiệm) |
| `bai_tap[]` tầng 3–4 nhóm F, G, I | ví dụ cho loại 4 (tự luận) |

**Khác biệt về thang mức độ:** skill này dùng `NB · TH · VD · VDC`; `exam-idea`
dùng `NB · TH · VD · LH` (LH = liên hệ thực tế). Khi chuyển:
- Bài nhóm **G** (ứng dụng thực tiễn) → `LH`
- Bài nhóm **I** (tổng hợp, nâng cao) → `VD` hoặc `LH` tuỳ nội dung

Nói rõ với người dùng rằng ma trận/đặc tả ràng buộc theo **thang điểm 10,0** nên
số câu có thể phải cắt bớt so với hệ thống bài tập đầy đủ.

## 2. Chuyển sang `exam-latex-creator` / `exam-docx-creator`

Hai skill đó dùng **4 loại câu hỏi thi cử**. Ánh xạ `hinh_thuc`:

| `hinh_thuc` của skill này | Loại câu hỏi | Môi trường LaTeX |
|---------------------------|--------------|------------------|
| `trac_nghiem` | Loại 1 — trắc nghiệm 4 phương án | `ex` |
| `dung_sai` | Loại 2 — đúng/sai 4 ý | `ex` |
| `tra_loi_ngan` | Loại 3 — trả lời ngắn (đáp án là số) | `ex` |
| `tu_luan` | Loại 4 — tự luận | `bt` |
| `dien_khuyet`, `noi_cot`, `thuc_hanh` | **không có tương ứng** | phải viết lại thành loại 1 hoặc 4 |

Ba hình thức cuối là đặc thù luyện tập (tầng ⭐). Khi chuyển sang đề thi phải
**viết lại**, không ép khuôn.

Trước khi bàn giao, đọc `exam-latex-creator/references/<loại>.md` để đúng format,
và tra `exam-latex-creator/references/MAPID_<MÔN><LỚP>.tex` để gán ID6.

## 3. Nguyên tắc chung khi chuyển giao

- **Không tự viết file .tex hoặc chạy pdflatex** trong skill này.
- Nói rõ với người dùng: "Nội dung đã sẵn sàng; để ra PDF cần dùng skill
  `exam-latex-creator`" — rồi gọi skill đó, đưa kèm đường dẫn file JSON.
- Giữ nguyên tên dạng và tên chủ đề khi chuyển để hai skill gọi tên thống nhất.
