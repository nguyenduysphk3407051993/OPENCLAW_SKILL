---
name: exam-idea
description: "Skill xây dựng bộ đề bài tập cho các môn Khoa học tự nhiên, Toán, Vật lí, Hoá học, Sinh học lớp 6–12. Sử dụng khi cần: đề xuất mục tiêu cần đạt cho một chủ đề, xây dựng hệ thống dạng bài tập theo 4 loại câu hỏi (trắc nghiệm nhiều lựa chọn, đúng/sai, trả lời ngắn, tự luận) ở đủ 4 mức độ (nhận biết, thông hiểu, vận dụng, liên hệ thực tiễn), lập bảng ma trận và bảng đặc tả đề kiểm tra. Đầu ra là 3 file Word docx (dạng bài tập, ma trận, đặc tả) sinh từ file JSON trung gian."
allowed-tools: Read, Write, Edit, Glob, Grep, Bash, WebFetch
argument-hint: "[môn] [lớp] [chủ đề] [cấu trúc đề: n1 câu loại 1, n2 câu loại 2, n3 câu loại 3, n4 câu loại 4] [tỉ lệ mức độ]"
---

# Skill: Exam Idea — Xây dựng bộ đề bài tập, ma trận và bảng đặc tả

## Khi yêu cầu chưa đủ cụ thể — PHẢN BIỆN TRƯỚC, LÀM SAU

Yêu cầu chung chung luôn cho ra sản phẩm kém. **Không đoán bừa, cũng không hỏi
lể tể từng ý.** Hãy nêu rõ đang thiếu gì, rồi đưa **một prompt mẫu đã điền sẵn
giá trị mặc định hợp lý** để người dùng sửa và gửi lại trong đúng một lượt.

Thiếu từ **2 tiêu chí trở lên** thì bắt buộc phản biện. Thiếu **đúng 1** tiêu chí
thì tự chọn mặc định, làm tiếp, và nói rõ đã chọn gì.

**Tiêu chí bắt buộc:** môn · lớp · chủ đề · cấu trúc đề (số câu từng loại) · tỉ lệ mức độ · tổng điểm

**Mẫu phản biện:**

> Yêu cầu hiện thiếu: **cấu trúc đề**, **tỉ lệ mức độ**. Nếu làm luôn thì tôi phải đoán, dễ lệch
> ý bạn. Bạn copy prompt dưới đây, sửa chỗ in đậm rồi gửi lại:
>
> ```
> Xây bộ đề môn **KHTN** lớp **6**,
> chủ đề **Mở đầu về KHTN – Đa dạng chất**.
> Cấu trúc: **12** câu loại 1, **4** câu loại 2, **2** câu loại 3, **3** câu loại 4
> Tỉ lệ mức độ: Nhận biết **50%**, Thông hiểu **30%**, Vận dụng **10%**,
>               Liên hệ thực tế **10%**
> Tổng điểm **10,0** · Thời gian **45 phút**
> ```

---

## Mô tả

Skill tạo trọn gói tài liệu ra đề cho một chủ đề môn học: **mục tiêu cần đạt →
hệ thống dạng bài tập → ma trận → bảng đặc tả → đề minh hoạ + đáp án**.

Điểm cốt lõi: **ma trận và bảng đặc tả được lưu dưới dạng JSON** rồi kết xuất
sang `.docx` bằng script, giữ nguyên form mẫu (gộp ô, đường viền, font
Times New Roman) — sửa JSON rồi chạy lại là ra file Word mới, không bao giờ
mất định dạng.

## Khi nào dùng

- Người dùng đưa ra một chủ đề/chương/bài và yêu cầu "ra bài tập", "xây dựng
  hệ thống bài tập", "soạn đề kiểm tra"
- Cần lập ma trận / bảng đặc tả đề kiểm tra định kì theo Công văn 7991 và
  CT GDPT 2018
- Cần kiểm tra tính đồng bộ giữa đề – ma trận – đặc tả
- Cần chuyển file JSON ma trận/đặc tả sang Word đúng form

## Cấu trúc thư mục

```
exam-idea/
├── SKILL.md                              ← File này
├── README.md                             ← Hướng dẫn ngắn cho người dùng cuối
├── requirements.txt                      ← python-docx (bắt buộc) + jsonschema
├── references/
│   ├── quy-trinh-ra-de.md                ← Quy trình 4 bước bắt buộc
│   ├── muc-do-danh-gia.md                ← 4 mức độ + động từ + cách phân bổ điểm
│   ├── dang-bai-tap.md                   ← Thư viện dạng bài tập cho 4 loại câu hỏi
│   ├── cau-truc-de-thi.md                ← Cấu trúc & thang điểm các dạng đề thông dụng
│   ├── json-schema.md                    ← Giải thích chi tiết 3 file JSON
│   ├── chay-tren-ubuntu-vps.md           ← Triển khai OpenClaw trên VPS Ubuntu
│   └── khung-noi-dung/
│       └── KHTN6.md                      ← Khung chủ đề/đơn vị kiến thức KHTN lớp 6
├── schemas/
│   ├── bang_ma_tran.schema.json          ← JSON Schema kiểm tra cú pháp
│   ├── bang_dac_ta.schema.json
│   └── de_bai_tap.schema.json
├── scripts/
│   ├── docx_common.py                    ← Lõi dựng docx (font, viền, gộp ô)
│   ├── ma_tran_to_docx.py                ← bang_ma_tran.json      → docx
│   ├── dac_ta_to_docx.py                 ← bang_dac_ta_ma_tran.json → docx
│   ├── de_to_docx.py                     ← de_bai_tap.json        → docx
│   ├── check_schema.py                   ← Kiểm tra cú pháp JSON theo schemas/
│   ├── validate.py                       ← Kiểm tra đồng bộ nội dung 3 file JSON
│   ├── build_all.py                      ← Chạy 2 bước kiểm tra + xuất cả 3 docx
│   ├── setup_ubuntu.sh                   ← Dựng môi trường trên VPS Ubuntu
│   └── package.py                        ← Đóng gói skill thành .zip
├── assets/
│   ├── mau_bang_ma_tran.docx             ← Form mẫu gốc 3 mức (tham chiếu mắt thường)
│   ├── mau_bang_ma_tran.png              ← Ảnh form gốc để đối chiếu
│   ├── mau_bang_dac_ta_ma_tran.docx
│   ├── mau_bang_dac_ta_ma_tran.png
│   ├── mau_bang_ma_tran_4mucdo.docx      ← Form 4 mức (khớp bộ đề trong output/)
│   ├── mau_bang_dac_ta_ma_tran_4mucdo.docx
│   └── tao_form_mau.py                   ← Script tái tạo form mẫu rỗng (3 hoặc 4 mức)
└── output/
    └── <TÊN_BỘ_ĐỀ>/                      ← Mỗi bộ đề một thư mục con
        ├── de_bai_tap.json
        ├── bang_ma_tran.json
        ├── bang_dac_ta_ma_tran.json
        ├── 1_Cac_dang_bai_tap.docx
        ├── 2_Bang_ma_tran.docx
        └── 3_Bang_dac_ta.docx
```

## Quy ước đường dẫn

| Biến | Ý nghĩa |
|------|---------|
| `<SKILL_DIR>` | Thư mục gốc skill (chứa file SKILL.md này) |
| `<OUT>` | `<SKILL_DIR>/output/<TÊN_BỘ_ĐỀ>` |
| `<BUILD>` | `python "<SKILL_DIR>/scripts/build_all.py" "<OUT>"` |

Yêu cầu môi trường: Python 3.9+ và `python-docx`; tuỳ chọn `jsonschema` để bật
bước kiểm tra cú pháp. Cài: `pip install -r requirements.txt`.

**Trên VPS Ubuntu:** chạy `bash scripts/setup_ubuntu.sh` một lần (tạo `.venv`,
sinh locale UTF-8), sau đó dùng `.venv/bin/python` thay cho `python`. Ubuntu
không có lệnh `python` — nếu không dùng venv phải gõ `python3`. Chi tiết và các
lỗi thường gặp: `references/chay-tren-ubuntu-vps.md`.

---

## Instruction

***Role:*** Bạn là chuyên gia khảo thí và phát triển chương trình môn Khoa học
tự nhiên / Toán / Vật lí / Hoá học / Sinh học cấp THCS – THPT, nắm vững
CT GDPT 2018 và cấu trúc đề kiểm tra định kì hiện hành.

### Bước 0 — Đọc tài liệu tham chiếu (BẮT BUỘC trước khi làm)

| Cần làm gì | Đọc file |
|------------|----------|
| Nắm quy trình tổng thể | `references/quy-trinh-ra-de.md` |
| Viết mục tiêu, phân mức độ | `references/muc-do-danh-gia.md` |
| Chọn/đặt tên dạng bài tập | `references/dang-bai-tap.md` |
| Chốt cấu trúc & thang điểm | `references/cau-truc-de-thi.md` |
| Viết JSON đúng khoá | `references/json-schema.md` |
| Tra chủ đề/đơn vị kiến thức | `references/khung-noi-dung/<MÔN><LỚP>.md` |
| Chạy trên VPS Ubuntu / gặp lỗi môi trường | `references/chay-tren-ubuntu-vps.md` |

Nếu skill `exam-latex-creator` có mặt cùng dự án, ĐỌC THÊM
`exam-latex-creator/references/MAPID_<MÔN><LỚP>.tex` để lấy đúng tên chương/bài/dạng
đã dùng trong ngân hàng câu hỏi, bảo đảm hai skill gọi tên thống nhất.

### Bước 1 — Đưa ra mục tiêu cần đạt cho chủ đề

- Bám sát **yêu cầu cần đạt** trong CT GDPT 2018 của môn/lớp tương ứng.
- Mỗi mục tiêu gắn đúng 1 mức độ: `NB` / `TH` / `VD` / `LH`.
- Dùng động từ đúng mức độ (xem `references/muc-do-danh-gia.md`): *nêu, trình
  bày, nhận biết* (NB); *phân biệt, so sánh, giải thích, xác định* (TH);
  *vận dụng, tính, dự đoán, tiến hành* (VD); *liên hệ, đề xuất, đánh giá,
  giải quyết tình huống thực tiễn* (LH).
- Ghi vào `de_bai_tap.json` → khoá `muc_tieu`.

### Bước 2 — Xây dựng hệ thống dạng bài tập

Với **mỗi loại câu hỏi**, đề xuất các **dạng** bám sát từng đơn vị kiến thức:

| Loại | Tên | Đặc tả bắt buộc |
|------|-----|-----------------|
| 1 | Trắc nghiệm nhiều lựa chọn | 4 phương án A, B, C, D; đúng **1** phương án; phương án nhiễu hợp lí, cùng trường ngữ nghĩa, độ dài tương đương |
| 2 | Trắc nghiệm đúng/sai | 1 ngữ cảnh chung + **4 ý** a), b), c), d); mỗi ý độc lập Đúng/Sai; số ý đúng **khác nhau giữa các câu**; các ý nên tăng dần mức độ |
| 3 | Trắc nghiệm trả lời ngắn | Đáp án là **một con số** duy nhất; dữ kiện đủ và rõ; nêu rõ đơn vị nếu có |
| 4 | Tự luận | Bắt buộc chia **2 ý a), b)** — mỗi ý là 1 lệnh hỏi có mức độ và thang điểm riêng; yêu cầu giải thích/đề xuất chứ không chỉ tái hiện |

Ghi vào `de_bai_tap.json` → khoá `dang_bai_tap`.

**Nguyên tắc nội dung (nghiêm ngặt):**
- Chỉ dùng dữ kiện khoa học **chính xác, có thật**; không bịa số liệu, hiện
  tượng, tên riêng. Nếu không chắc → tra cứu, không đoán.
- Ngữ cảnh ưu tiên **Việt Nam và đời sống học sinh** (trời nồm, chợ, bếp gas,
  ruộng lúa…) để phần liên hệ thực tiễn có ý nghĩa.
- Ngôn ngữ đúng thuật ngữ sách giáo khoa hiện hành của lớp đó; không dùng
  kiến thức vượt cấp.
- Mỗi câu hỏi phải quy chiếu được về đúng 1 đơn vị kiến thức và 1 mức độ.

### Bước 3 — Xây dựng ma trận

1. Chốt **cấu trúc đề** (số câu từng loại) và **tỉ lệ mức độ** theo yêu cầu
   người dùng.
2. Quy đổi ra **lệnh hỏi**: câu loại 1 và loại 3 = 1 lệnh hỏi; câu loại 2 =
   **4 lệnh hỏi** (4 ý a, b, c, d); câu loại 4 = **2 lệnh hỏi** (2 ý a, b).
   Ma trận và đặc tả luôn đếm theo lệnh hỏi.
3. Chọn thang điểm sao cho **tổng đúng 10,0** và **tỉ lệ mức độ khớp tuyệt đối**
   yêu cầu (xem bảng gợi ý trong `references/cau-truc-de-thi.md`).
4. Phân bổ số lệnh hỏi vào từng ô (đơn vị kiến thức × loại câu hỏi × mức độ).
5. Ghi ra `bang_ma_tran.json`.

**Bắt buộc tự kiểm tra bằng số học trước khi ghi file:** tổng điểm từng mức độ
chia cho tổng điểm phải bằng đúng tỉ lệ yêu cầu; tổng số lệnh hỏi từng loại
phải bằng đúng cấu trúc đề.

### Bước 4 — Xây dựng bảng đặc tả

- Dùng **cùng danh sách chủ đề và đơn vị kiến thức** (chuỗi giống hệt từng ký
  tự) như ma trận — đây là điều kiện để `validate.py` báo đồng bộ.
- Mỗi dòng "Yêu cầu cần đạt" là một mục tiêu cụ thể ở một mức độ, kèm số lệnh
  hỏi phân về từng loại câu hỏi.
- Tổng số lệnh hỏi của các YCCĐ trong một ô phải **bằng đúng** con số của ô
  tương ứng trong ma trận.
- Ghi ra `bang_dac_ta_ma_tran.json`.

### Bước 5 — Sinh đề minh hoạ và kết xuất

1. Viết đầy đủ câu hỏi + đáp án + lời giải vào `de_bai_tap.json` →
   `de_minh_hoa`. Mỗi câu khai `chu_de`, `don_vi`, `muc_do`, `dang`, `diem`
   đúng như đã phân bổ trong ma trận.
2. Chạy:
   ```bash
   python "<SKILL_DIR>/scripts/build_all.py" "<OUT>"
   ```
3. **Không được báo hoàn thành khi validate còn lỗi.** Sửa JSON và chạy lại
   tới khi `Tong so loi: 0`, rồi mới bàn giao 3 file docx.

### Đầu ra bàn giao

| File | Nội dung |
|------|----------|
| `1_Cac_dang_bai_tap.docx` | Mục tiêu cần đạt · Hệ thống dạng bài tập · Đề minh hoạ · Đáp án – hướng dẫn chấm |
| `2_Bang_ma_tran.docx` | Ma trận, khổ A4 ngang, đúng form mẫu |
| `3_Bang_dac_ta.docx` | Bảng đặc tả, khổ A4 ngang, đúng form mẫu |

Kèm 3 file JSON nguồn để người dùng chỉnh sửa và tái sinh docx bất cứ lúc nào.

---

## Ví dụ tham chiếu có sẵn

`output/KHTN6_MoDau_DaDangChat/` — bộ đề KHTN lớp 6, chủ đề *Mở đầu về Khoa học
tự nhiên* và *Đa dạng chất – Các thể của chất*:

- Cấu trúc: **12 câu loại 1 + 4 câu loại 2 + 2 câu loại 3 + 3 câu loại 4**
  (mỗi câu tự luận 2 ý a, b) → 12 + 16 + 2 + 6 = **36 lệnh hỏi**
- Tỉ lệ: **Nhận biết 50% – Thông hiểu 30% – Vận dụng 10% – Liên hệ thực tế 10%**
- Thang điểm: 3,0 + 4,0 + 1,0 + 2,0 = **10,0 điểm**
- `validate.py` báo **0 lỗi**

Khi làm bộ đề mới, sao chép thư mục này rồi thay nội dung là cách nhanh nhất.

## Lỗi thường gặp

| Triệu chứng | Nguyên nhân & cách xử lí |
|-------------|--------------------------|
| `Danh sach chu de/don vi kien thuc KHONG khop` | Tên đơn vị kiến thức trong 2 file JSON khác nhau dù chỉ 1 dấu cách. Copy–paste chuỗi từ ma trận sang đặc tả. |
| `o so lenh hoi lech giua ma tran va dac ta` | Tổng `so_lenh_hoi` của các YCCĐ cùng mức độ chưa bằng ô ma trận. |
| `Ty le ... khong dat` | Điều chỉnh phân bổ mức độ hoặc thang điểm; ưu tiên đổi số câu loại 1 vì mỗi câu chỉ 0,25 điểm nên dễ tinh chỉnh. |
| `Tong diem != 10` | Câu loại 4 phải khai `diem` tường minh trong `bang_ma_tran.json` (khoá `diem`), vì `diem_moi_lenh` của nhóm Tự luận là `null`. |
| Bảng tràn quá nhiều trang | Rút gọn tên đơn vị kiến thức, hoặc giảm số mức độ xuống 3 (Biết – Hiểu – Vận dụng) như form mẫu gốc. |


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
