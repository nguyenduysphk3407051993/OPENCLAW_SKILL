# Chạy skill trên VPS Ubuntu (OpenClaw)

## Cài nhanh

```bash
bash scripts/setup_ubuntu.sh          # TeX vừa đủ (~1,5 GB)
bash scripts/setup_ubuntu.sh --full   # texlive-full (~5 GB, chắc chắn nhất)
source .venv/bin/activate
python scripts/check_linux.py         # phải báo 0 lỗi
```

---

## Lỗi số 1: phân biệt HOA/thường trong `\input`

Đây là lỗi **hay gặp nhất và khó đoán nhất** khi mang bộ `.tex` từ Windows sang
Linux. Windows coi `Khaibao/HeaderFooter/` và `Khaibao/Headerfooter/` là một;
Linux thì không — biên dịch sẽ chết với `File not found`.

Chạy trước khi biên dịch:

```bash
python scripts/check_linux.py
```

Script đối chiếu **mọi** `\input` / `\include` / `\subfile` với tên file thật,
bỏ qua dòng đã chú thích bằng `%`, và chỉ ra chính xác chỗ lệch:

```
[LOI] 1 tham chieu SAI HOA/THUONG - chay duoc tren Windows nhung VO tren Linux:
  FileMain.tex: \input{Khaibao/HeaderFooter/Dethi_ver1.tex}  ->  file that: Khaibao/Headerfooter/Dethi_ver1.tex
```

> Lỗi này **đã có thật** trong `latex-output/FileMain.tex` và đã được sửa
> (`HeaderFooter` → `Headerfooter`). Nếu sau này thêm file khai báo mới, luôn
> chạy lại `check_linux.py`.

## Lỗi số 2: thiếu gói `vietnam` (vntex)

`FileMain.tex` dùng `\usepackage[utf8]{vietnam}`. Gói này **không** nằm trong
`texlive-latex-base`:

```bash
sudo apt install texlive-lang-other
kpsewhich vietnam.sty      # phải in ra đường dẫn
```

Thiếu nó thì mọi file đều chết ngay dòng preamble.

## Lỗi số 3: tên file có dấu hoặc khoảng trắng

`check_linux.py` mục `[2]` liệt kê các file kiểu `Images/Một số AO.zip`,
`Images/Icon 3d_18.png`. Ảnh có dấu/khoảng trắng khi `\includegraphics` trên
Linux dễ hỏng. Đổi thành không dấu, không khoảng trắng, rồi sửa đường dẫn trong
`.tex` (hoặc dùng `<EXPORT> imgpaths`).

## Lỗi số 4: `python` không tồn tại

Ubuntu chỉ có `python3`. Dùng venv để lệnh trong SKILL.md chạy nguyên văn:

```bash
source .venv/bin/activate
```

Ubuntu 23.10+ còn chặn `pip install` vào Python hệ thống (PEP 668
`externally-managed-environment`) — venv giải quyết luôn.

## Lỗi số 5: log tiếng Việt lỗi font trong terminal

VPS mới thường ở locale `POSIX`/`C`. Các script đã tự ép `stdout` sang UTF-8,
nhưng nên đặt luôn ở tầng hệ thống:

```bash
export LANG=C.UTF-8
export PYTHONIOENCODING=utf-8
```

---

## Gói TeX cần cho từng tính năng

| Dùng gì | Gói LaTeX | Gói apt |
|---------|-----------|---------|
| Tiếng Việt (bắt buộc) | `vietnam` | `texlive-lang-other` |
| Template đề thi | `subfiles` | `texlive-latex-extra` |
| Hình vẽ, đồ thị | `tikz`, `pgfplots`, `tkz-tab` | `texlive-pictures` |
| Công thức hoá học | `chemfig` | `texlive-science` |
| Ký hiệu, icon | `bbding`, `fontawesome5` | `texlive-fonts-extra` |
| Biên dịch nhiều lượt | `latexmk` | `latexmk` |

`check_linux.py` mục `[4]` tự quét `\usepackage` trong `latex-output/` và in ra
đúng câu lệnh `apt install` cần chạy, đồng thời dùng `kpsewhich` xác nhận gói đã
có thật trong hệ thống TeX.

## Python cần gì

Chỉ **`python-docx`**, và chỉ cho 2 việc:

- `spec_to_exam.py read <bảng đặc tả .docx>`
- `export_pdf.py images <file .docx>`

Toàn bộ phần còn lại (`mix_exam.py`, `export_pdf.py fix/compile/clean`,
`spec_to_exam.py skeleton/fill/verify`) chỉ dùng thư viện chuẩn.

## Kiểm tra sức khoẻ

```bash
python scripts/check_linux.py
python scripts/mix_exam.py  parse latex-output/
python scripts/export_pdf.py compile <FILE>.tex --dir latex-output --times 2 --clean
```

---

> Minh bạch: toàn bộ bộ script đã được kiểm chứng chạy thật trên Windows +
> Python 3.13 + TeX Live 2024 (sinh `.tex` và biên dịch ra PDF thành công).
> Phần Ubuntu ở trên dựa trên rà soát mã nguồn (không có `win32com`, không có
> đường dẫn cứng, mọi `open()` đều `encoding="utf-8"`) và trên kết quả thật của
> `check_linux.py` — nhưng **chưa chạy thực tế trên VPS**. Hãy chạy
> `setup_ubuntu.sh` rồi `check_linux.py` một lần để xác nhận.
