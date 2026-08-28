# bai-tap-cung-co-creator

Skill xây dựng **hệ thống dạng bài tập củng cố kiến thức** cho Toán, Vật lí,
Hoá học, Sinh học, KHTN lớp 6–12.

Đưa vào một chủ đề → nhận về bản đồ đầy đủ các dạng bài tập, mỗi dạng kèm phương
pháp giải và bài tập ở 4 tầng độ khó cho mọi đối tượng học sinh.

## Điểm khác biệt

- **Quét đủ 9 nhóm dạng**, không bỏ sót: củng cố lý thuyết · nhận diện – phân
  loại – so sánh · tính toán · đọc và xử lí dữ liệu · thí nghiệm – thực hành ·
  giải thích hiện tượng · ứng dụng thực tiễn · phát hiện lỗi sai · tổng hợp
  nâng cao. Nhóm nào không dùng phải nêu lí do.
- **Phân tầng thật.** Bài ⭐ và bài ⭐⭐⭐⭐ của cùng một dạng là cùng bài gốc được
  hạ/nâng độ khó bằng 12 kĩ thuật có chủ đích, không phải bốn bài rời rạc.
- **Mỗi dạng có phương pháp giải theo bước** — thứ học sinh mang đi dùng lại.
- **Mọi bài đều có lời giải và đáp án**, được script kiểm tra tự động.

## Cách dùng

Chỉ cần nói với Claude, ví dụ:

```
Xây dựng hệ thống bài tập củng cố môn Vật lí lớp 9,
chủ đề Định luật Ohm và đoạn mạch nối tiếp, song song.
Mục đích: ôn tập. Đối tượng: mọi trình độ, đủ 4 tầng.
Số bài: 2–4 bài mỗi dạng. Đầu ra: xuất 2 file Word.
```

Thiếu thông tin, skill sẽ đưa lại một prompt mẫu đã điền sẵn để bạn sửa.

## Đầu ra

| Yêu cầu | Kết quả |
|---------|---------|
| Hỏi "có những dạng bài tập nào" | Bảng bản đồ dạng bài tập ngay trong chat |
| Xin ví dụ vài dạng | Hồ sơ dạng + bài phân tầng có lời giải, trong chat |
| Xin file Word | `He_thong_bai_tap_HS.docx` (bản học sinh) và `He_thong_bai_tap_GV.docx` (bản giáo viên, có lời giải) |

File Word sinh từ `he_thong_bai_tap.json` — sửa JSON rồi chạy lại là ra bản mới,
không mất định dạng.

## Cài đặt

```bash
pip install -r requirements.txt        # python-docx + jsonschema
```

Trên Ubuntu/VPS dùng `python3` thay cho `python`, hoặc tạo venv:

```bash
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
```

## Chạy tay

```bash
python scripts/build_all.py "output/VATLI9_DinhLuatOhm"
```

Lệnh này kiểm tra cú pháp JSON → kiểm tra nội dung (đủ nhóm, đủ tầng, đủ lời
giải) → xuất 2 file Word. Có lỗi thì dừng, không xuất file.

## Bộ mẫu

`output/VATLI9_DinhLuatOhm/` — Vật lí 9, Định luật Ohm: 8 mục tiêu, 11 dạng phủ
đủ 9 nhóm, 33 bài trải đều 4 tầng. Dùng làm khuôn khi làm chủ đề mới.

## Skill liên quan

| Cần gì | Dùng skill |
|--------|-----------|
| Ma trận + bảng đặc tả đề kiểm tra | `exam-idea` |
| File .tex / PDF | `exam-latex-creator` |
| File .docx đề thi đúng form | `exam-docx-creator` |
| Đề cương học kì môn KHTN | `de-cuong-khtn-creator` |
