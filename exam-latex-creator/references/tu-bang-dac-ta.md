# Ra đề từ bảng đặc tả có sẵn (.docx / .json)

Khi người dùng đưa **bảng đặc tả**, không được tự nghĩ ra cấu trúc đề. Phải
bung bảng đặc tả thành kế hoạch ra đề rồi bám đúng kế hoạch đó.

Script: `scripts/spec_to_exam.py`

---

## Quy trình 4 bước

```bash
# 1) Bảng đặc tả -> kế hoạch (plan.json)
python scripts/spec_to_exam.py read <spec.docx|spec.json> -o plan.json --lop 6 --mon K

# 2) Kế hoạch -> file .tex theo ĐÚNG assets/template-de-thi.tex
python scripts/spec_to_exam.py skeleton plan.json \
    -o latex-output/<TEN_FILE>_MADE101.tex \
    --ten-de "Kiểm tra định kì giữa học kì I" --monhoc "Khoa học tự nhiên 6" \
    --ngaykt 20/10/2026 --thoigian 45 --made 101

# 3) Điền nội dung vào các chỗ % TODO, tra MAPID thay dấu '?' trong ID6

# 4) Đối chiếu lại với bảng đặc tả
python scripts/spec_to_exam.py verify plan.json latex-output/<TEN_FILE>_MADE101.tex
```

Nếu đã có sẵn nội dung câu hỏi dạng `de_bai_tap.json` (đầu ra của skill
`exam-idea`), bỏ qua bước 2–3 và dùng thẳng:

```bash
python scripts/spec_to_exam.py fill plan.json de_bai_tap.json \
    --id6-map id6_map.json -o latex-output/<TEN_FILE>_MADE101.tex \
    --ten-de "..." --monhoc "..." --ngaykt ... --thoigian 45 --made 101
```

Sau đó nối vào chuỗi công cụ sẵn có của skill:

```bash
python scripts/export_pdf.py fix     latex-output/<TEN_FILE>_MADE101.tex
python scripts/export_pdf.py compile <TEN_FILE>_MADE101.tex --dir latex-output --times 2 --clean
python scripts/mix_exam.py  shuffle  latex-output/<TEN_FILE>_MADE101.tex --seed 42 --made2 102
```

---

## Quy tắc quy đổi LỆNH HỎI → CÂU

Bảng đặc tả đếm theo **lệnh hỏi**, đề đếm theo **câu**:

| Loại | Nhóm trong bảng đặc tả | Lệnh hỏi / câu |
|------|------------------------|----------------|
| 1 – EX | Nhiều lựa chọn | 1 |
| 2 – TF | "Đúng – Sai" | **4** (ý a, b, c, d) |
| 3 – SA | Trả lời ngắn | 1 |
| 4 – BT | Tự luận | 1, hoặc **2** nếu bảng đếm theo ý a), b) |

Cờ điều chỉnh: `--y-dung-sai 4` và `--y-tu-luan 2`.
Khi nguồn là `.json` có khai `so_y_moi_cau`, script tự lấy theo file — chỉ
truyền cờ khi muốn ghi đè.

**Kiểm tra bắt buộc:** tổng lệnh hỏi mỗi nhóm phải chia hết cho số ý mỗi câu.
Nếu không, script in `[CANH BAO] ... lenh hoi le` → bảng đặc tả có vấn đề, phải
hỏi lại người dùng chứ không tự làm tròn.

## Quy đổi mức độ → ký tự ID6

| Mức độ trong bảng | Mã | Ký tự ID6 |
|-------------------|----|-----------|
| Nhận biết / Biết | NB | `N` |
| Thông hiểu / Hiểu | TH | `H` |
| Vận dụng | VD | `V` |
| Vận dụng cao | VDC | `C` |
| Liên hệ thực tế / thực tiễn | LH | `T` |

Script sinh ID6 dạng `6K?N?-?`. Dấu `?` là **Chương** và **Bài–Dạng** — bắt
buộc tra `references/MAPID_<MÔN><LỚP>.tex` để thay. `verify` sẽ báo lỗi nếu còn
sót dấu `?`.

---

## Bảng đặc tả .docx cần có gì

Script tự dò, không cần đúng tuyệt đối vị trí, nhưng phải có:

- Một ô tiêu đề chứa đúng chữ **"Yêu cầu cần đạt"**
- Cột đầu là **TT**, gộp dọc hết vùng tiêu đề (dùng để đếm số dòng tiêu đề)
- Dòng tiêu đề áp chót ghi tên **nhóm câu hỏi**, dòng cuối ghi tên **mức độ**
- Các dòng chân bảng bắt đầu bằng "Tổng số...", "Tỷ lệ..." (script dừng ở đây)

Dòng nhãn kiểu `Nhận biết:` không có số → script tự bỏ qua, không tính là YCCĐ.

Form chuẩn: `exam-idea/assets/mau_bang_dac_ta_ma_tran.docx`.

---

## Giới hạn tuyệt đối khi sinh .tex

1. **Chỉ dùng đúng cấu trúc `assets/template-de-thi.tex`.** Script nạp nguyên
   file template, chỉ thay các chỗ `<...>` và chèn câu vào 4 điểm đánh dấu.
2. **KHÔNG thêm bất kỳ gói (`\usepackage`) hay lệnh LaTeX mới nào.** Chỉ dùng
   các lệnh đã có trong template và trong `ex-trac-nghiem.md`, `tf-dung-sai.md`,
   `sa-tra-loi-ngan.md`, `bt-tu-luan.md`.
3. **Giữ nguyên dòng hướng dẫn thí sinh** sau mỗi `\subsection`
   (`\textit{\large Thí sinh trả lời từ câu ... }`) — chỉ thay con số tổng câu.
4. Phần nào **không có câu hỏi thì xoá cả khối** `\subsection` đó (kể cả cặp
   `\Opensolutionfile`/`\Closesolutionfile`), đúng quy định của skill.
5. File `.tex` phải nằm **cùng thư mục với `FileMain.tex`** (`latex-output/`) vì
   dùng `\documentclass[FileMain.tex]{subfiles}`.

### Ký tự Unicode phải chuyển sang LaTeX

`pdflatex` + `\usepackage[utf8]{vietnam}` chỉ nhận chữ Việt, không nhận ký hiệu
toán Unicode. Script tự chuyển:

| Unicode | LaTeX |
|---------|-------|
| `°C` | `$^\circ$C` |
| `×` | `$\times$` |
| `−` (U+2212) | `$-$` |
| `→` | `$\rightarrow$` |
| `³` `²` | `$^3$` `$^2$` |
| `–` `—` | `--` `---` |
| `…` `...` | `\dots` |
| `“ ” "` | `\lq\lq` `\rq\rq` |
| `% & # _` | `\% \& \# \_` |

Gặp ký tự lạ ngoài danh sách, script in `[CANH BAO] ky tu Unicode chua co quy
tac chuyen doi` — phải xử lý trước khi biên dịch, không bỏ qua.

---

## Đầu ra của `verify`

```
So cau theo loai:
  [OK ] EX: dac ta 12 - de 12
  [OK ] TF: dac ta 4 - de 4
  [OK ] SA: dac ta 2 - de 2
  [OK ] BT: dac ta 3 - de 3
  [OK ] 21 cau deu da co ID6
Tong so loi: 0
```

Chỉ bàn giao khi `Tong so loi: 0`.

---

## Ví dụ đã chạy thật

`demo/` chứa kế hoạch và bảng ánh xạ ID6 của bộ đề mẫu:

- Nguồn: `exam-idea/output/KHTN6_MoDau_DaDangChat/3_Bang_dac_ta.docx`
- Kết quả: `latex-output/KTDK_KHTN6_MoDau_DaDangChat_MADE101.tex` + `.pdf`
- 12 EX + 4 TF + 2 SA + 3 BT = 21 câu / 36 lệnh hỏi, `verify` 0 lỗi,
  biên dịch ra PDF 5 trang bằng `export_pdf.py compile`
