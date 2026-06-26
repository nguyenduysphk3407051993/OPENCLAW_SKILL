# Format Markdown cho câu hỏi giáo dục VN → DOCX

## Nguyên tắc chung

- **Tiền tố câu hỏi** ("Câu N.", "Bài N.", "Ví dụ N.") phải nằm **CÙNG DÒNG** với nội dung
- **Phương án A-D**: mỗi phương án **một dòng riêng**, bắt đầu bằng `A.`, `B.`, `C.`, `D.`
- **Ý nhỏ a-d**: mỗi ý **một dòng riêng**, bắt đầu bằng `a)`, `b)`, `c)`, `d)`
- Công thức inline: `$...$`
- Công thức display (riêng dòng): `\[...\]` — **KHÔNG** dùng `$$...$$`
- Số thập phân: dùng `{,}` thay `.` → `$3{,}14$`
- Tiếng Việt **giữ nguyên dấu**, không dịch
- **KHÔNG** đưa chữ tiếng Việt vào trong `$...$` hoặc `\[...\]`
- Nếu bắt buộc phải có chữ trong công thức, dùng ASCII không dấu trong `\text{...}`

---

## Loại 1: Trắc nghiệm nhiều lựa chọn

```markdown
Câu 1. Phản ứng oxi hóa - khử là phản ứng hóa học trong đó có sự thay đổi đại lượng nào?
A. Số khối
B. Số oxi hóa
C. Số electron lớp ngoài cùng
D. Số nơtron trong hạt nhân

Lời giải.

- Phản ứng oxi hóa - khử là phản ứng trong đó có sự chuyển dịch electron giữa các chất phản ứng.
- Khi có sự chuyển dịch electron, số oxi hóa của các nguyên tố sẽ thay đổi.
  + Chất khử nhường electron -> số oxi hóa tăng.
  + Chất oxi hóa nhận electron -> số oxi hóa giảm.

Đáp án.

Chọn B
```

**Quy tắc:**
- Đủ 4 phương án A, B, C, D
- Mỗi phương án **một dòng riêng**
- **Không có dấu chấm** ở cuối phương án
- Script sẽ tự động layout 4-cột/2-cột/1-dòng tùy độ dài

---

## Loại 2: Đúng/sai

```markdown
Câu 1. Xét phản ứng $Ca + Cl_2 \rightarrow CaCl_2$. Đánh giá tính đúng/sai:
a) Mỗi nguyên tử Ca nhường 2e
b) Số oxi hóa của Ca trước phản ứng là +2
c) Nếu dùng 4 gam Ca thì số mol electron Cl nhận là 0,4 mol
d) Liên kết trong $CaCl_2$ là liên kết ion

Lời giải.

- a) Đúng: Ca thuộc nhóm IIA, nhường 2 electron để đạt cấu hình electron bền vững của khí hiếm.
- b) Sai: Ca là đơn chất nên có số oxi hóa bằng 0. Trước phản ứng số oxi hóa của Ca là 0, sau phản ứng mới là +2.
- c) Đúng: 
  + $n_{Ca} = \frac{4}{40} = 0{,}1 \text{ mol}$.
  + Số mol electron Ca nhường: $n_{e} = 2 \times 0{,}1 = 0{,}2 \text{ mol}$.
  + Vì số mol electron nhường bằng số mol electron nhận nên số mol electron Cl nhận là 0,2 mol.
- d) Đúng: Ca là kim loại điển hình, Cl là phi kim điển hình, liên kết giữa chúng là liên kết ion.
```

**Quy tắc:**
- 4 ý a), b), c), d) — mỗi ý một dòng riêng
- Nội dung phải chứa **kiến thức** (không chỉ ghi "đúng"/"sai")

---

## Loại 3: Trả lời ngắn

```markdown
Câu 1. Một vật có khối lượng $5$ kg chuyển động với vận tốc $4$ m/s. Tính động năng (đơn vị J).

Lời giải.

- Áp dụng công thức tính động năng: $W_d = \frac{1}{2} m v^2$
  + Trong đó $m = 5 \text{ kg}$, $v = 4 \text{ m/s}$.
- Thay số ta được: $W_d = \frac{1}{2} \times 5 \times 4^2 = 40 \text{ J}$.

Đáp án.

40
```

**Quy tắc:**
- Câu hỏi cho ra đáp án dạng **con số**
- Số thập phân: `$2{,}3$`

---

## Loại 4: Tự luận

```markdown
Bài 1. Cân bằng phương trình hóa học sau bằng phương pháp thăng bằng electron:
\[Fe + HNO_3 \rightarrow Fe(NO_3)_3 + NO + H_2O\]

Lời giải.

- Xác định sự thay đổi số oxi hóa:
  + $Fe^0 \rightarrow Fe^{+3} + 3e$ (quá trình oxi hóa)
  + $N^{+5} + 3e \rightarrow N^{+2}$ (quá trình khử)
- Thăng bằng electron: hệ số của Fe là 1, hệ số của NO là 1.
- Phương trình cân bằng:
  \[Fe + 4HNO_3 \rightarrow Fe(NO_3)_3 + NO + 2H_2O\]
```

**Quy tắc:**
- Dùng tiền tố "Bài" (không phải "Câu")
- Nội dung chi tiết, có thể nhiều dòng
- Công thức nhiều dòng: dùng nhiều `\[...\]` liên tiếp

---

## Ví dụ đề thi hoàn chỉnh (markdown)

```markdown
# ĐỀ KIỂM TRA GIỮA KỲ 1
## Môn: Khoa học tự nhiên 9 — Thời gian: 45 phút

### Phần I. Trắc nghiệm (4 điểm)

Câu 1. Liên kết hóa học trong phân tử $H_2$ thuộc loại liên kết nào?
A. Liên kết ion
B. Liên kết cho nhận
C. Liên kết cộng hóa trị không cực
D. Liên kết cộng hóa trị có cực

Câu 2. Số oxi hóa của Fe trong $Fe_2O_3$ là bao nhiêu?
A. +1
B. +2
C. +3
D. +4

### Phần II. Đúng/sai (2 điểm)

Câu 3. Về liên kết hóa học, đánh giá các phát biểu sau:
a) Liên kết ion hình thành do lực hút tĩnh điện giữa các ion
b) Liên kết cộng hóa trị hình thành do sự góp chung electron
c) NaCl có liên kết cộng hóa trị
d) $H_2O$ có liên kết ion

### Phần III. Trả lời ngắn (1 điểm)

Câu 4. Tính khối lượng mol của $CaCO_3$ (đơn vị g/mol). Cho Ca = 40, C = 12, O = 16.

### Phần IV. Tự luận (3 điểm)

Bài 5. Cân bằng phương trình phản ứng sau:
\[Al + HCl \rightarrow AlCl_3 + H_2\]
Cho biết chất oxi hóa, chất khử trong phản ứng trên.
```
