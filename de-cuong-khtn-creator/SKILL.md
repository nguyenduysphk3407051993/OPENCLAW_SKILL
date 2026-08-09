---
name: de-cuong-khtn-creator
description: "Skill tạo Đề cương học kì (hoặc cả năm học) cho các môn Khoa học tự nhiên (Lớp 6, 7, 8, 9) chuẩn LaTeX. Hỗ trợ tự động cấu trúc theo từng Chương (với Mục tiêu), Bài (Lý thuyết trọng tâm trong môi trường kienthuccannho với các subsubsection, và Bài tập với 4 phần: Tự luận, Trắc nghiệm nhiều lựa chọn, Trắc nghiệm đúng sai, Trả lời ngắn), tự động đặt tên file đáp án (C01_B01_TenBai), chèn hình ảnh chú thích và biên dịch PDF bằng pdflatex."
allowed-tools: Read, Write, Edit, Glob, Grep, WebFetch
argument-hint: "[môn/lớp] [học kì/năm học] [chương/bài]"
---

# Skill: Vietnamese KHTN Semester Syllabus & Outline Generator (Đề cương học kì Khoa học tự nhiên)

## Khi yêu cầu chưa đủ cụ thể — PHẢN BIỆN TRƯỚC, LÀM SAU

Yêu cầu chung chung luôn cho ra sản phẩm kém. **Không đoán bừa, cũng không hỏi
lể tể từng ý.** Hãy nêu rõ đang thiếu gì, rồi đưa **một prompt mẫu đã điền sẵn
giá trị mặc định hợp lý** để người dùng sửa và gửi lại trong đúng một lượt.

Thiếu từ **2 tiêu chí trở lên** thì bắt buộc phản biện. Thiếu **đúng 1** tiêu chí
thì tự chọn mặc định, làm tiếp, và nói rõ đã chọn gì.

**Tiêu chí bắt buộc:** môn · lớp · học kì hoặc cả năm · phạm vi chương/bài · có kèm bài tập hay không

**Mẫu phản biện:**

> Yêu cầu hiện thiếu: **phạm vi chương/bài**, **mức độ chi tiết**. Nếu làm luôn thì tôi phải đoán, dễ lệch
> ý bạn. Bạn copy prompt dưới đây, sửa chỗ in đậm rồi gửi lại:
>
> ```
> Tạo đề cương môn **KHTN** lớp **7**, **học kì I**.
> Phạm vi: **chương 1 đến chương 5** (bài **1–18**).
> Mỗi bài cần: **lý thuyết trọng tâm + 3 câu trắc nghiệm + 1 bài tự luận**
> Định dạng: **LaTeX**, xuất PDF **có**
> ```

---

## Mô tả

Skill chuyên tạo **Đề cương học kì** (Học kì I, Học kì II hoặc cả năm học) cho môn **Khoa học tự nhiên** (Lớp 6, Lớp 7, Lớp 8, Lớp 9) theo định dạng LaTeX chuẩn. Skill đảm bảo chính xác về cấu trúc chương/bài, mục tiêu bài học, lý thuyết trọng tâm và bộ câu hỏi trắc nghiệm/tự luận phân loại 4 cấp độ.

## Khi nào dùng

- Tạo đề cương học kì I, học kì II hoặc ôn tập cả năm môn KHTN (6, 7, 8, 9).
- Soạn tài liệu học tập theo chương, bài gồm đầy đủ **Lý thuyết trọng tâm** và **Bài tập phân loại (4 phần)**.
- Trích xuất nội dung từ SGK / Đề ôn tập sang dạng mã LaTeX chuẩn.
- Tự động quản lý lưu file đáp án theo cú pháp `C<số chương>_B<số bài>_<Tên bài không dấu>`.
- Biên dịch ra PDF chất lượng cao thông qua `pdflatex` và bộ script hỗ trợ.

---

## Cấu trúc thư mục Skill

```
de-cuong-khtn-creator/
├── SKILL.md                          ← File hướng dẫn này
├── references/                       ← Tài liệu tham chiếu format câu hỏi + MAPID
│   ├── ex-trac-nghiem.md             ← Format loại 1: trắc nghiệm nhiều lựa chọn (EX)
│   ├── tf-dung-sai.md                ← Format loại 2: đúng/sai (TF)
│   ├── sa-tra-loi-ngan.md            ← Format loại 3: trả lời ngắn (SA)
│   ├── bt-tu-luan.md                 ← Format loại 4: tự luận (BT)
│   ├── mapid6-coding.md              ← Quy tắc mã hóa ID6
│   ├── MAPID_KHTN6.tex               ← Bản đồ nội dung KHTN lớp 6
│   ├── MAPID_KHTN7.tex               ← Bản đồ nội dung KHTN lớp 7
│   ├── MAPID_KHTN8.tex               ← Bản đồ nội dung KHTN lớp 8
│   └── MAPID_KHTN9.tex               ← Bản đồ nội dung KHTN lớp 9
├── scripts/
│   ├── mix_exam.py                   ← Ghép đề, trộn đề, parse, lọc trùng
│   └── export_pdf.py                 ← Sửa lỗi LaTeX, biên dịch PDF, xử lý ảnh
├── assets/
│   └── template-de-cuong.tex         ← Template cấu trúc Đề cương học kì KHTN chuẩn
└── latex-output/                     ← Thư mục xuất file .tex/.pdf
    ├── FileMain.tex                  ← File chính (document class, subfiles, packages)
    ├── Khaibao/                      ← Khai báo môi trường (Muctieu, kienthuccannho, ...)
    ├── Ans/                          ← Đáp án tự sinh (LGEX, Ans, LGTF, AnsBT, AnsSA...)
    ├── Ansbook/                      ← Bảng đáp án TF (AnsTF)
    └── Images/                       ← Thư mục chứa hình ảnh minh họa
```

## Quy ước đường dẫn & Lệnh execution

| Biến | Ý nghĩa |
|------|---------|
| `<SKILL_DIR>` | Đường dẫn tuyệt đối đến thư mục gốc skill |
| `<OUTPUT_DIR>` | `<SKILL_DIR>/latex-output` |
| `<EXPORT>` | `python "<SKILL_DIR>/scripts/export_pdf.py"` |
| `<MIX>` | `python "<SKILL_DIR>/scripts/mix_exam.py"` |

---

## Hướng dẫn Chi tiết Cấu trúc Đề cương Học kì KHTN

Mỗi file Đề cương học kì KHTN phải tuân thủ nghiêm ngặt cấu trúc LaTeX dưới đây:

### 1. Cấu trúc Khung File LaTeX

```latex
\documentclass[FileMain.tex]{subfiles}
\begin{document}

% Các Chương và Bài được chèn ở đây...

\end{document}
```

### 2. Cấu trúc từng Chương (`\chapter`)

Mỗi chương bắt đầu bằng lệnh `\chapter{<Tên chương>}` và môi trường `Muctieu`:

```latex
\chapter{<Tên chương>}
\begin{Muctieu}
    \item <Nội dung các ý mục tiêu cần đạt thứ nhất trong chương>
    \item <Nội dung các ý mục tiêu cần đạt thứ hai trong chương>
    ...
\end{Muctieu}
```

### 3. Cấu trúc từng Bài (`\section`)

Mỗi chương gồm nhiều bài (`\section{Tên bài}`). Trong mỗi bài gồm 2 phần chính:

#### **Phần A. Lý thuyết trọng tâm** (`\subsection{Lý thuyết trọng tâm ...}`)
Được bọc trong môi trường `kienthuccannho`. Bên trong dùng các mục `\subsubsection{...}` cấp 1:

```latex
\subsection{Lý thuyết trọng tâm bài <X> chương <Y>}
\begin{kienthuccannho}
    \subsubsection{Nội dung mục con cấp 1 thứ nhất}
    <Nội dung kết hợp văn bản, công thức math $, bảng tabular/longtable, tikz...>

    \subsubsection{Nội dung mục con cấp 1 thứ hai}
    <Nội dung kết hợp văn bản, công thức math $, bảng tabular/longtable, tikz...>

    \subsubsection{Nội dung mục con cấp 1 thứ n}
    <Nội dung kết hợp văn bản, công thức math $, bảng tabular/longtable, tikz...>
\end{kienthuccannho}
```

#### **Phần B. Bài tập** (`\subsection{Bài tập ...}`)
Gồm 4 phần tương ứng 4 loại câu hỏi trắc nghiệm / tự luận với cấu trúc nghiêm ngặt:

1. **Phần 1: Bài tập tự luận** (Câu hỏi loại 4 — 10 đến 15 câu):
```latex
%%%==============Phần bài tập tự luận==============%%%
\phan{Bài tập tự luận}
\textit{\large Thí sinh trả lời từ bài 1 đến bài <tổng bài loại 4>}
\Opensolutionfile{ansbth}[Ans/LGBT-<tên file lưu đáp án>]
\Opensolutionfile{ansbt}[Ans/AnsBT-<tên file lưu đáp án>]
  % <Chèn các câu hỏi loại 4 (BT) vào đây>
\Closesolutionfile{ansbt}
\Closesolutionfile{ansbth}
```

2. **Phần 2: Bài tập trắc nghiệm nhiều lựa chọn** (Câu hỏi loại 1 — 20 đến 25 câu):
```latex
%%%==============Phần trắc nghiệm nhiều lựa chọn==============%%%
\phan{Bài tập trắc nghiệm nhiều lựa chọn}
\textit{\large Thí sinh trả lời từ câu 1 đến <tổng câu loại 1>. Mỗi câu thí sinh chỉ chọn một phương án}
\Opensolutionfile{ansex}[Ans/LGEX-<tên file lưu đáp án>]
\Opensolutionfile{ans}[Ans/Ans-<tên file lưu đáp án>]
  % <Chèn các câu hỏi loại 1 (EX) vào đây>
\Closesolutionfile{ans}
\Closesolutionfile{ansex}
%\bangdapan{Ans-<tên file lưu đáp án>}
```

3. **Phần 3: Bài tập trắc nghiệm đúng sai** (Câu hỏi loại 2 — 10 đến 15 câu):
```latex
%%%==============Phần trắc nghiệm đúng sai==============%%%
\phan{Bài tập trắc nghiệm đúng sai}
\textit{\large Thí sinh trả lời từ câu 1 đến câu <tổng câu loại 2>. Trong mỗi ý a), b), c), d) ở mỗi câu thí sinh chọn đúng hoặc sai}
\Opensolutionfile{ansex}[Ans/LGTF-<tên file lưu đáp án>]
\Opensolutionfile{ansbook}[Ansbook/AnsTF-<tên file lưu đáp án>]
\Opensolutionfile{ans}[Ans/Tempt-<tên file lưu đáp án>]
\setcounter{ex}{0}
  % <Chèn các câu hỏi loại 2 (TF) vào đây>
\Closesolutionfile{ans}
\Closesolutionfile{ansbook}
\Closesolutionfile{ansex}
%\bangdapanTF{AnsTF-<tên file lưu đáp án>}
```

4. **Phần 4: Bài tập trả lời ngắn** (Câu hỏi loại 3 — 10 câu):
```latex
%%==============Phần bài tập trả lời ngắn==============%%%
\phan{Bài tập trả lời ngắn}
\textit{\large Thí sinh trả lời từ câu 1 đến câu <tổng câu loại 3>}
\Opensolutionfile{ansex}[Ans/LGSA-<tên file lưu đáp án>]
\Opensolutionfile{ansexh}[Ans/AnsSA-<tên file lưu đáp án>]
\setcounter{ex}{0}
  % <Chèn các câu hỏi loại 3 (SA) vào đây>
\Closesolutionfile{ansexh}
\Closesolutionfile{ansex}
%\bangdapanSA{AnsSA-<tên file lưu đáp án>}
```

---

## Cú pháp đặt tên `<tên file lưu đáp án>`

Tên file lưu đáp án bắt buộc tuân theo quy tắc:
`C<số chương có chữ số 0 đầu tiên>_B<số bài có chữ số 0 đầu tiên>_<Tên bài viết không dấu>`

**Ví dụ:**
- Chương 1, Bài 2 "Sự nở vì nhiệt": `C01_B02_SuNoViNhiet`
- Chương 3, Bài 10 "Tế bào - Đơn vị cơ sở của sự sống": `C03_B10_TeBaoDonViCoSoCuaSuSong`

---

## Cấu trúc Câu hỏi (Loại 1, 2, 3, 4) & Chèn Hình ảnh

Cấu trúc câu hỏi tuân thủ chính xác chuẩn của skill `exam-latex-creator`:

### 1. Chèn Hình ảnh có chú thích
```latex
\begin{center}
    \includegraphics[width=0.95\linewidth]{Images/<đường_dẫn_tới_file_ảnh>}
\end{center}
```

### 2. Loại 1 — Trắc nghiệm nhiều lựa chọn (`ex`)
```latex
\begin{ex}%[<ID6>]
Nội dung câu hỏi trắc nghiệm...
\choice
{Phương án A}
{\True Phương án B đúng}
{Phương án C}
{Phương án D}
\loigiai{
Lời giải chi tiết...
}
\end{ex}
```

### 3. Loại 2 — Trắc nghiệm Đúng / Sai (`ex`)
```latex
\begin{ex}%[<ID6>]
Nội dung câu hỏi phát biểu đúng sai...
\choiceTF
{\True Phát biểu a đúng}
{Phát biểu b sai}
{\True Phát biểu c đúng}
{Phát biểu d sai}
\loigiai{
\begin{itemchoice}[T1,F2,T3,F4]
  \itemch Lời giải ý a.
  \itemch Lời giải ý b.
  \itemch Lời giải ý c.
  \itemch Lời giải ý d.
\end{itemchoice}
}
\end{ex}
```

### 4. Loại 3 — Trả lời ngắn (`ex`)
```latex
\begin{ex}%[<ID6>]
Nội dung câu hỏi yêu cầu tính toán ra đáp số...
\shortans{$12{,}5$}
\loigiai{
Lời giải chi tiết...
}
\end{ex}
```

### 5. Loại 4 — Tự luận (`bt`)
```latex
\begin{bt}%[<ID6>]
Nội dung câu hỏi tự luận...
\loigiai{
Lời giải trình bày từng bước chi tiết...
}
\end{bt}
```

---

## Tra cứu MAPID & Mã hóa ID6

Trước khi soạn câu hỏi, đọc file mapid tương ứng trong `references/` (`MAPID_KHTN6.tex`, `MAPID_KHTN7.tex`, `MAPID_KHTN8.tex`, `MAPID_KHTN9.tex`) để gắn mã ID6:
`[<Lớp><Môn><Chương><Mức độ><Bài>-<Dạng>]`

- Lớp: `6`, `7`, `8`, `9`
- Môn: `K` (KHTN), `H` (Hóa), `L` (Vật lý), `S` (Sinh học)
- Mức độ: `N` (Nhận biết), `H` (Thông hiểu), `V` (Vận dụng), `C` (Vận dụng cao)

---

## Workflow Soạn Đề cương và Biên dịch PDF

1. **Chuẩn bị thông tin:** Xác định môn/lớp (KHTN 6, 7, 8, 9), học kì (HK1, HK2) và các Chương/Bài cần soạn đề cương.
2. **Soạn file `.tex` đề cương:** Đọc template tại `assets/template-de-cuong.tex`, điền Mục tiêu chương, Lý thuyết trọng tâm từng bài (trong `kienthuccannho`), và các bài tập 4 loại.
3. **Lưu file:** Lưu file `.tex` vừa tạo vào thư mục `<SKILL_DIR>/latex-output/DE_CUONG_KHTN<LỚP>_<HK>.tex`.
4. **Kiểm tra & Sửa lỗi LaTeX:**
   ```bash
   <EXPORT> fix "<OUTPUT_DIR>/DE_CUONG_KHTN<LỚP>_<HK>.tex"
   ```
5. **Biên dịch PDF:**
   ```bash
   <EXPORT> compile "DE_CUONG_KHTN<LỚP>_<HK>.tex" --dir "<OUTPUT_DIR>" --times 2 --clean
   ```

---

## Checklist trước khi hoàn tất

- [ ] Đề cương đầy đủ phần Header `\documentclass[FileMain.tex]{subfiles}` và `\begin{document}`.
- [ ] Mỗi Chương có `\chapter{...}` và môi trường `\begin{Muctieu} ... \end{Muctieu}`.
- [ ] Mỗi Bài có `\section{...}`.
- [ ] Phần Lý thuyết trọng tâm nằm trong `\begin{kienthuccannho} ... \end{kienthuccannho}` với các `\subsubsection{...}`.
- [ ] Phần Bài tập gồm đủ 4 phần (Tự luận, Trắc nghiệm nhiều lựa chọn, Trắc nghiệm đúng sai, Trả lời ngắn).
- [ ] Tên file đáp án mở/đóng đúng cú pháp: `C<xx>_B<yy>_<TenBaiKhongDau>`.
- [ ] Mã ID6 gắn đúng chuẩn MAPID KHTN 6-9.
- [ ] Các công thức math, hóa học, bảng biểu đúng chuẩn LaTeX ($...$, `\dfrac`, `{,}`).
- [ ] Đã chạy `<EXPORT> fix` và `<EXPORT> compile` tạo file PDF thành công.


---

## Tương thích đa nền tảng (Windows · Linux · môi trường skill)

Các script Python của skill này đã xử lý sẵn những chỗ hay vỡ khi đổi máy:

| Vấn đề | Đã xử lý thế nào |
|--------|-------------------|
| Console Windows là cp1252/cp437 → in tiếng Việt ném `UnicodeEncodeError` | Mỗi script tự `reconfigure` stdout/stderr sang UTF-8 ngay sau phần import |
| Đọc/ghi file | Luôn khai báo `encoding="utf-8"`; đọc thêm `utf-8-sig` để nuốt BOM của Notepad |
| Ghép đường dẫn | Dùng `os.path.join` / `pathlib`, không nối chuỗi `\` hay `/` |

Khi tự gõ lệnh, tuân thủ thêm 4 điểm sau:

1. **Bọc mọi đường dẫn trong dấu nháy kép** — thư mục tiếng Việt hay có dấu cách.
2. **Linux phân biệt HOA/thường.** `output/` khác `Output/`, `Khaibao/HeaderFooter`
   khác `Khaibao/Headerfooter`. Đặt tên file đầu ra **không dấu, không khoảng trắng**.
3. **Ubuntu không có lệnh `python`**, chỉ có `python3`. Dùng venv
   (`python3 -m venv .venv && source .venv/bin/activate`) để các lệnh trong tài
   liệu này chạy nguyên văn, hoặc thay `python` bằng `python3`.
4. **Không hard-code đường dẫn tuyệt đối** kiểu `D:\...` hay `/home/...` vào file
   cấu hình; luôn tính tương đối từ `<SKILL_DIR>`.

Khi chạy trong bash sandbox, dùng đường dẫn VM mount thay cho đường dẫn Windows.
