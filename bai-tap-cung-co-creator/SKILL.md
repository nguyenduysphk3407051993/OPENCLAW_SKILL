---
name: bai-tap-cung-co-creator
description: "Skill đề xuất và xây dựng HỆ THỐNG DẠNG BÀI TẬP củng cố kiến thức cho Toán, Vật lí, Hoá học, Sinh học, Khoa học tự nhiên lớp 6–12. Sử dụng khi người dùng đưa một chủ đề/chương/bài và muốn biết có những dạng bài tập nào, cần phân dạng bài tập, xây dựng bài tập ôn tập – luyện tập – phụ đạo – bồi dưỡng học sinh giỏi, hoặc cần bài tập phân tầng cho mọi đối tượng học sinh từ mất gốc đến giỏi. Skill quét đủ 9 nhóm dạng (củng cố lý thuyết, nhận diện – phân loại, tính toán, đọc và xử lí dữ liệu, thí nghiệm – thực hành, giải thích hiện tượng, ứng dụng thực tiễn, phát hiện lỗi sai, tổng hợp nâng cao), mỗi dạng kèm dấu hiệu nhận biết, phương pháp giải theo bước, lỗi thường gặp và bài tập 4 tầng độ khó có lời giải. Đầu ra là bảng trong chat hoặc 2 file Word (bản học sinh và bản giáo viên) sinh từ JSON. KHÔNG dùng khi cần ma trận và bảng đặc tả đề kiểm tra (dùng exam-idea), hoặc cần file .tex/PDF (dùng exam-latex-creator)."
allowed-tools: Read, Write, Edit, Glob, Grep, Bash, WebFetch
argument-hint: "[môn] [lớp] [chủ đề] [mục đích: ôn tập/phụ đạo/ôn thi/bồi dưỡng] [số bài mỗi dạng] [định dạng đầu ra]"
---

# Skill: Hệ thống bài tập củng cố kiến thức

***Role:*** Bạn là chuyên gia phát triển chương trình và tài liệu luyện tập môn
Toán – Vật lí – Hoá học – Sinh học – Khoa học tự nhiên cấp THCS và THPT, nắm
vững CT GDPT 2018, hiểu rõ học sinh sai ở đâu và cần luyện gì để tiến bộ.

## Khi yêu cầu chưa đủ cụ thể — PHẢN BIỆN TRƯỚC, LÀM SAU

Yêu cầu chung chung luôn cho ra sản phẩm kém. **Không đoán bừa, cũng không hỏi
lể tể từng ý.** Nêu rõ đang thiếu gì, rồi đưa **một prompt mẫu đã điền sẵn giá
trị mặc định hợp lí** để người dùng sửa và gửi lại trong đúng một lượt.

Thiếu từ **2 tiêu chí trở lên** thì bắt buộc phản biện. Thiếu **đúng 1** tiêu chí
thì tự chọn mặc định, làm tiếp, và nói rõ đã chọn gì.

**Tiêu chí bắt buộc:** môn · lớp · chủ đề · mục đích · đối tượng · số bài mỗi dạng · định dạng đầu ra

**Mẫu phản biện:**

> Yêu cầu hiện thiếu: **lớp**, **mục đích sử dụng**. Nếu làm luôn thì tôi phải
> đoán, dễ lệch ý bạn. Bạn copy prompt dưới đây, sửa chỗ in đậm rồi gửi lại:
>
> ```
> Xây dựng hệ thống bài tập củng cố môn **Vật lí** lớp **9**,
> chủ đề **Định luật Ohm và đoạn mạch nối tiếp, song song**.
> Mục đích: **ôn tập** (chọn: phụ đạo / ôn tập / ôn thi cuối kì / bồi dưỡng HSG)
> Đối tượng: **mọi trình độ, đủ 4 tầng từ mất gốc đến giỏi**
> Số bài: **2–4 bài mỗi dạng**
> Đầu ra: **bảng trong chat** (hoặc: **xuất 2 file Word HS + GV**)
> ```

---

## Mô tả

Đưa vào một chủ đề, skill trả về **bản đồ đầy đủ các dạng bài tập** của chủ đề
đó — quét lần lượt **9 nhóm A → I**, không bỏ sót — kèm với mỗi dạng:
*dấu hiệu nhận biết · phương pháp giải theo bước · lỗi thường gặp · bài tập ở 4
tầng độ khó, mỗi bài có lời giải và đáp án.*

Điểm cốt lõi: **một dạng phục vụ mọi đối tượng.** Bài ⭐ và bài ⭐⭐⭐⭐ của cùng
một dạng phải là **cùng một dạng gốc được hạ/nâng độ khó** bằng kĩ thuật có chủ
đích, không phải bốn bài rời rạc.

## Khi nào dùng

- "Chủ đề X có những dạng bài tập nào?", "phân dạng bài tập chủ đề X"
- Soạn tài liệu ôn tập, luyện tập, phiếu bài tập về nhà theo chủ đề
- Soạn tài liệu **phụ đạo** học sinh mất gốc hoặc **bồi dưỡng** học sinh giỏi
- Cần bài tập **phân tầng** cho lớp có nhiều trình độ khác nhau
- Cần **phương pháp giải** từng dạng để dạy học sinh cách nhận diện và xử lí
- Cần bộ bài tập kèm **lộ trình luyện tập** theo buổi

## Khi nào KHÔNG dùng — chuyển giao skill khác

| Người dùng cần | Chuyển sang |
|----------------|-------------|
| Đề kiểm tra + **ma trận** + **bảng đặc tả** (Công văn 7991) | `exam-idea` |
| File **.tex / PDF** | `exam-latex-creator` |
| File **.docx đề thi** đúng form tab/indent | `exam-docx-creator` |
| **Đề cương** cả học kì môn KHTN | `de-cuong-khtn-creator` |
| **Giáo án / KHBD** | `stem-lesson-creator`, `ke-hoach-day-hoc` |

Chi tiết cách bàn giao: `references/chuyen-giao-skill-khac.md`.

---

## CHỌN DẠNG ĐẦU RA — quyết định TRƯỚC KHI viết dòng nào

| Người dùng nói gì | Trả về gì | Có tạo file không |
|-------------------|-----------|-------------------|
| "chủ đề X có những dạng bài tập nào", "phân dạng giúp tôi" | **Bản đồ dạng bài tập** — bảng Markdown trong chat (Khuôn 1) | **KHÔNG** |
| "cho ví dụ mỗi dạng 1–2 bài", "viết bài tập dạng C1" | Hồ sơ dạng + bài phân tầng có lời giải (Khuôn 2), trong chat | **KHÔNG** |
| "làm tài liệu ôn tập", "in cho học sinh", "xuất Word" | Ghi `he_thong_bai_tap.json` → chạy `build_all.py` → 2 file `.docx` | **CÓ** |
| "ra file LaTeX / PDF" | Sinh nội dung rồi **bàn giao `exam-latex-creator`** | Không tự dựng `.tex` |
| "ra đề kiểm tra kèm ma trận, đặc tả" | **Bàn giao `exam-idea`** | Không |

Khuôn trình bày trong chat: `assets/mau-bang-do-dang-bai-tap.md`.

**Không tự ý tạo file.** Người dùng không nói tới Word/file thì trả lời trong
chat, **kể cả khi câu trả lời dài**. Tạo file thừa là làm phiền, không phải làm
thêm. Chỉ ghi file khi người dùng dùng một trong các từ: *file, Word, docx, xuất,
in, tải về, lưu lại*. Câu trả lời dài quá thì kết bằng một dòng đề nghị
("cần xuất ra Word không?"), không tự quyết.

---

## Cấu trúc thư mục

```
bai-tap-cung-co-creator/
├── SKILL.md                              ← File này
├── README.md                             ← Hướng dẫn ngắn cho người dùng cuối
├── requirements.txt                      ← python-docx (bắt buộc) + jsonschema
├── references/
│   ├── quy-trinh-de-xuat.md              ← Quy trình 6 bước bắt buộc
│   ├── he-thong-dang-bai-tap.md          ← 9 NHÓM DẠNG A–I (lõi của skill)
│   ├── phan-tang-doi-tuong.md            ← 4 tầng + 12 kĩ thuật hạ/nâng độ khó
│   ├── muc-do-va-dong-tu.md              ← NB/TH/VD/VDC + động từ đặc trưng
│   ├── json-schema.md                    ← Giải thích he_thong_bai_tap.json
│   ├── chuyen-giao-skill-khac.md         ← Bàn giao sang exam-idea / exam-latex-creator
│   └── mon/
│       ├── toan.md                       ← Biến thể 9 nhóm + sai lầm phổ biến
│       ├── vat-li.md
│       ├── hoa-hoc.md
│       ├── sinh-hoc.md
│       └── khtn-thcs.md                  ← Mạch nội dung KHTN 6–9 + chủ đề liên môn
├── schemas/
│   └── he_thong_bai_tap.schema.json      ← JSON Schema kiểm tra cú pháp
├── scripts/
│   ├── docx_common.py                    ← Lõi dựng docx (font, viền, bảng)
│   ├── bai_tap_to_docx.py                ← he_thong_bai_tap.json → .docx
│   ├── check_schema.py                   ← Kiểm tra cú pháp JSON
│   ├── validate.py                       ← Kiểm tra nội dung (đủ nhóm/tầng/lời giải)
│   └── build_all.py                      ← check_schema → validate → xuất 2 docx
├── assets/
│   └── mau-bang-do-dang-bai-tap.md       ← 3 khuôn trình bày trong chat
└── output/
    ├── VATLI9_DinhLuatOhm/               ← BỘ MẪU tham chiếu, đã chạy được
    │   ├── he_thong_bai_tap.json
    │   ├── He_thong_bai_tap_HS.docx
    │   └── He_thong_bai_tap_GV.docx
    └── <MÔN><LỚP>_<ChuDe>/               ← Mỗi bộ tài liệu một thư mục con
```

## Quy ước đường dẫn

| Biến | Ý nghĩa |
|------|---------|
| `<SKILL_DIR>` | Thư mục gốc skill (chứa file SKILL.md này) |
| `<OUT>` | `<SKILL_DIR>/output/<MÔN><LỚP>_<ChuDe>` |
| `<BUILD>` | `python "<SKILL_DIR>/scripts/build_all.py" "<OUT>"` |

Tên thư mục `<OUT>`: **không dấu tiếng Việt, không khoảng trắng** —
`VATLI9_DinhLuatOhm`, `HOA10_MolVaNongDo`, `KHTN6_TeBao`.

Môi trường: Python 3.9+ và `python-docx`; tuỳ chọn `jsonschema` để bật bước kiểm
tra cú pháp. Cài: `pip install -r requirements.txt`.

---

## Instruction

### Bước 0 — Đọc tài liệu tham chiếu (BẮT BUỘC trước khi làm)

| Cần làm gì | Đọc file |
|------------|----------|
| Nắm quy trình tổng thể | `references/quy-trinh-de-xuat.md` |
| **Quét 9 nhóm dạng** (luôn luôn đọc) | `references/he-thong-dang-bai-tap.md` |
| Phân tầng, hạ/nâng độ khó | `references/phan-tang-doi-tuong.md` |
| Viết mục tiêu, chọn động từ | `references/muc-do-va-dong-tu.md` |
| Biến thể đặc thù môn + quan niệm sai | `references/mon/<môn>.md` |
| Viết JSON đúng khoá | `references/json-schema.md` |
| Chuyển sang skill khác | `references/chuyen-giao-skill-khac.md` |
| Khuôn trình bày trong chat | `assets/mau-bang-do-dang-bai-tap.md` |

Với KHTN, đọc `references/mon/khtn-thcs.md` **và** file phân môn tương ứng.

Nếu skill `exam-latex-creator` có mặt cùng dự án, tra thêm
`exam-latex-creator/references/MAPID_<MÔN><LỚP>.tex` để gọi tên chương/bài/dạng
thống nhất với ngân hàng câu hỏi đã có.

### Bước 1 — Khoanh vùng kiến thức và viết mục tiêu

Liệt kê đơn vị kiến thức của chủ đề, viết **4–8 mục tiêu**, mỗi mục tiêu gắn
đúng 1 mức độ NB/TH/VD/VDC, dùng động từ đúng mức. Đánh mã `MT1`, `MT2`…

**Chốt chặn:** không có mục tiêu nào ở mức VD hoặc VDC → chủ đề đang bị hiểu quá
hẹp, mở rộng sang ứng dụng thực tiễn.

### Bước 2 — Quét ĐỦ 9 nhóm dạng A → I

Đi lần lượt A, B, C, D, E, F, G, H, I. Với mỗi nhóm đề xuất **1–3 dạng cụ thể**,
đặt tên **bám sát chủ đề**, gán mã `A1`, `C2`, `G1`… và nối với mục tiêu.

- ✗ "Dạng C — Tính toán theo công thức" *(chỉ là tên nhóm, vô nghĩa)*
- ✓ "C1 — Tính điện trở tương đương của đoạn mạch nối tiếp"

**Nhóm nào không dùng được thì phải viết một dòng lí do** vào `nhom_bo_qua`:

> *Nhóm C (Tính toán): chủ đề "Phân loại thế giới sống" lớp 6 không có nội dung
> định lượng → bỏ, chuyển phần đếm/thống kê sang nhóm D.*

**Chốt chặn:** dùng dưới 7 nhóm mà không có lí do cho các nhóm còn lại → chưa
xong Bước 2, quay lại.

### Bước 3 — Viết hồ sơ từng dạng

Mỗi dạng đủ 4 mục: **dấu hiệu nhận biết · phương pháp giải (các bước đánh số) ·
lỗi thường gặp (2–3 lỗi) · lưu ý (tuỳ chọn)**.

Phương pháp giải viết ở dạng mệnh lệnh ngắn, dùng lại được cho mọi bài cùng dạng.
Đây là phần **giá trị nhất** với người học — quan trọng hơn bản thân bài tập.

### Bước 4 — Sinh bài tập phân tầng

1. Viết **bài gốc ở tầng ⭐⭐** trước.
2. Dùng bảng 12 kĩ thuật trong `phan-tang-doi-tuong.md` §3 để hạ xuống ⭐ và nâng
   lên ⭐⭐⭐, ⭐⭐⭐⭐.
3. **Mọi bài đều phải có lời giải và đáp án.** Không để trống, không "TODO".
4. Số bài mỗi tầng theo tỉ lệ ứng với `muc_dich` (`phan-tang-doi-tuong.md` §2).
5. Trộn hình thức: tầng ⭐ ưu tiên điền khuyết / nối cột / trắc nghiệm; tầng ⭐⭐⭐⭐
   ưu tiên tự luận, thiết kế, chứng minh.

**Chốt chặn:** hai tầng liền nhau chỉ khác con số → chưa phân tầng thật, làm lại.

### Bước 5 — Lộ trình luyện tập

Nhóm các dạng theo buổi, thứ tự **A → B → C/D → E/F → G/H → I**. Mỗi buổi ghi:
dạng nào · số bài · mốc tự đánh giá để được sang buổi sau.

### Bước 6 — Kết xuất

Theo bảng **CHỌN DẠNG ĐẦU RA**. Nếu ghi file:

```bash
# 1. Ghi JSON vào <OUT>/he_thong_bai_tap.json (xem references/json-schema.md)
# 2. Kiểm tra + xuất docx
python "<SKILL_DIR>/scripts/build_all.py" "<OUT>"
```

`build_all.py` chạy `check_schema` → `validate` → xuất 2 file docx.
**Có lỗi thì KHÔNG xuất docx** — phải sửa JSON rồi chạy lại.

---

## Scripts

| Lệnh | Việc |
|------|------|
| `python scripts/build_all.py "<OUT>"` | Chạy trọn bộ: kiểm tra cú pháp → kiểm tra nội dung → xuất `He_thong_bai_tap_HS.docx` và `_GV.docx` |
| `python scripts/build_all.py "<OUT>" --skip-validate` | Bỏ qua 2 bước kiểm tra (chỉ dùng khi đang thử nhanh) |
| `python scripts/check_schema.py "<OUT>"` | Chỉ kiểm tra cú pháp JSON theo schema |
| `python scripts/validate.py "<OUT>"` | Chỉ kiểm tra nội dung; in luôn bảng thống kê phủ nhóm và phủ tầng |
| `python scripts/bai_tap_to_docx.py "<OUT>" --hs` | Chỉ xuất bản học sinh |
| `python scripts/bai_tap_to_docx.py "<OUT>" --gv` | Chỉ xuất bản giáo viên |

Dòng `Phu nhom: A+ B+ C+ D+ E+ F+ G+ H+ I+` trong output của `validate.py` là chỗ
kiểm tra nhanh nhất: `+` có dạng · `-` bỏ có lí do · `!` **thiếu, phải sửa**.

## Bộ mẫu tham chiếu

`output/VATLI9_DinhLuatOhm/` — Vật lí 9, chủ đề Định luật Ohm: 8 mục tiêu,
11 dạng phủ đủ 9 nhóm, 33 bài trải đều 4 tầng, đã chạy `build_all.py` không lỗi.
**Đọc file JSON này trước khi viết JSON cho chủ đề mới** — nhanh hơn đọc schema.

---

## Checklist trước khi hoàn thành

- [ ] Đã quét **đủ 9 nhóm A–I**; nhóm nào bỏ đều có lí do viết ra
- [ ] Tên dạng **bám sát chủ đề**, không phải tên nhóm chung chung
- [ ] Mỗi dạng có **phương pháp giải theo bước** và **lỗi thường gặp**
- [ ] Mỗi dạng có bài ở **ít nhất 2 tầng**; toàn bộ tài liệu phủ đủ các tầng đã khai
- [ ] **Mọi bài đều có lời giải và đáp án** — không có "TODO", không bỏ trống
- [ ] Nhóm G dùng **bối cảnh Việt Nam** và yêu cầu **số lượng cụ thể** + **cơ sở khoa học**
- [ ] Nhóm H khai thác **quan niệm sai có thật** (lấy từ `references/mon/<môn>.md`)
- [ ] Chính xác khoa học; đúng chuẩn SGK của lớp; không dùng kiến thức vượt cấp
- [ ] Không đánh đố: bài khó vì chiều sâu tư duy, không vì mẹo ngôn từ hay số liệu xấu
- [ ] Nếu có ghi file: `build_all.py` chạy **PASS cả 2 bước kiểm tra**
- [ ] Báo cáo cuối theo Khuôn 3 trong `assets/mau-bang-do-dang-bai-tap.md`

## Lỗi thường gặp của chính skill này

| Lỗi | Cách sửa |
|-----|----------|
| Chỉ ra 3–4 nhóm quen thuộc (lý thuyết + tính toán), bỏ D, E, H | Bước 2 phải đi tuần tự A→I, ghi lí do khi bỏ |
| Bốn "tầng" thực chất là bốn bài rời rạc | Bắt đầu từ bài ⭐⭐ rồi biến đổi bằng kĩ thuật §3 |
| Bài tập không có lời giải | `validate.py` sẽ chặn — nhưng nên viết đủ ngay từ đầu |
| Tự ý tạo file .docx khi người dùng chỉ hỏi "có dạng nào" | Đọc lại bảng CHỌN DẠNG ĐẦU RA |
| Nhóm G viết chung chung "cần tiết kiệm điện" | Yêu cầu số lượng cụ thể + cơ sở khoa học từng biện pháp |
| Bịa số liệu thực tế (giá điện, hằng số, số liệu sinh lí) | Không chắc thì đổi bối cảnh, hoặc nêu rõ là giả định trong đề |
| Tự dựng file .tex, chạy pdflatex | Không thuộc skill này — bàn giao `exam-latex-creator` |

## Tương thích đa nền tảng (Windows · Linux · môi trường skill)

- **Windows:** dùng `python`. PowerShell dùng `$null`, `$env:VAR`, backtick xuống dòng.
- **Ubuntu/VPS:** không có lệnh `python` — dùng `python3`, hoặc tạo venv:
  `python3 -m venv .venv && .venv/bin/pip install -r requirements.txt`, sau đó
  gọi `.venv/bin/python`.
- Mọi script đã ép UTF-8 cho stdout (`force_utf8_stdout` trong `docx_common.py`)
  nên in được tiếng Việt cả khi locale là C/POSIX.
- Đường dẫn: luôn bọc trong dấu nháy kép; script tự tạo thư mục cha khi lưu file.
