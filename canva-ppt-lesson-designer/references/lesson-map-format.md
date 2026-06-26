# Lesson Map Format — chuẩn bản đồ bài học (slide-oriented)

Tài liệu này định nghĩa **định dạng chuẩn** cho các file bản đồ bài học trong `references/maps/`.
Mục tiêu: để nội dung text mỗi slide **bám sát từng đơn vị bài học** của chương trình GDPT 2018,
súc tích, đúng kiến thức — thay vì để skill tự bịa nội dung.

Đây là tương đương khái niệm "MAPID" trong skill exam-latex-creator, nhưng định hướng **slide** (đơn vị
kiến thức để trình chiếu) thay vì **câu hỏi** (dạng bài để ra đề).

---

## 1. Quy ước đặt tên file

```
references/maps/MAP_<MÔN><LỚP>.md
```

| Mã môn | Môn |
|---|---|
| `KHTN` | Khoa học tự nhiên |
| `HOA` | Hóa học (THPT) |
| `LY` | Vật lý (THPT) |
| `SINH` | Sinh học (THPT) |
| `TOAN` | Toán |
| `VAN` | Ngữ văn |

Ví dụ: `MAP_KHTN6.md`, `MAP_KHTN9.md`, `MAP_HOA10.md`, `MAP_TOAN8.md`.

---

## 2. Cấu trúc một file map

Mỗi file gồm: **header** (nguồn + cách dùng + quy ước) → các **Chương** → các **Bài** → khối nội dung bài.

### 2.1. Header bắt buộc (đầu file)

```markdown
# MAP_<MÔN><LỚP> — Bản đồ bài học <Môn> lớp <Lớp> (slide-oriented)

> Nguồn: Chương trình GDPT 2018 môn <Môn> lớp <Lớp>.
> Mục đích: nội dung mỗi slide BÁM SÁT từng đơn vị bài học, súc tích, đúng chuẩn.
> Cách dùng: xác định Chương → Bài người dùng yêu cầu → lấy `Đơn vị KT` làm outline slide nội dung,
>            `Trọng tâm` để chọn slide nhấn mạnh, `Visual` để tra `assets/visual-keyword-library.json`.

## Quy ước đọc map
- `Đơn vị KT` : mỗi gạch đầu dòng = 1 ý có thể thành 1 slide nội dung (hoặc 1 khối trong slide).
- `Trọng tâm` : điểm cốt lõi / dễ nhầm → ưu tiên slide riêng hoặc đánh accent.
- `Visual`    : key trong `assets/visual-keyword-library.json` + shape gợi ý.
- `Liên hệ`   : ví dụ thực tế dùng để mở đầu hoặc làm hoạt động.
- `Accent`    : môn để chọn màu accent (`vat_ly | hoa_hoc | sinh_hoc | chung`) — tra `brand-standard.json`.
```

### 2.2. Khối Chương

```markdown
## C<n>. <Tên chương>  [accent: <hoa_hoc|vat_ly|sinh_hoc|chung>]
```

### 2.3. Khối Bài (đơn vị lặp lại chính)

```markdown
### Bài <n>.<m> — <Tên bài>
- Đơn vị KT:
  - <ý kiến thức 1, viết dạng cụm slide-ready, ≤ 12 từ>
  - <ý kiến thức 2>
  - <ý kiến thức 3>
- Trọng tâm: <1–2 điểm cốt lõi/dễ nhầm>
- Liên hệ: <ví dụ thực tế ngắn>
- Visual: <key1>, <key2> (shape: <gợi ý shape>); fallback: <từ khóa EN nếu chưa có key>
- Slide gợi ý: <số slide nội dung hợp lý cho bài>
```

---

## 3. Quy tắc nội dung khi viết map

1. **Đơn vị KT phải là kiến thức, không phải dạng câu hỏi.** Gộp các "dạng" chi tiết thành
   ý kiến thức trình chiếu được. Mỗi gạch đầu dòng = một ý đủ để làm 1 slide hoặc 1 khối.
2. **Súc tích.** Mỗi đơn vị KT là một cụm ngắn (≤ 12 từ), không viết câu dài. Skill sẽ mở rộng
   khi dựng slide, nhưng map giữ "xương sống" đúng và gọn.
3. **Đúng chuẩn chương trình.** Bám tên chương/bài theo SGK & khung GDPT 2018. Không thêm kiến thức
   ngoài chương trình của lớp.
4. **Visual khớp key.** Mỗi bài nên trỏ tới ≥ 1 key có thật trong `visual-keyword-library.json`.
   Nếu chưa có key phù hợp → ghi `fallback:` kèm từ khóa EN, và (khuyến nghị) bổ sung concept mới
   vào `visual-keyword-library.json`.
5. **Accent theo môn con.** Chương thiên Vật lý → `vat_ly`; Hóa → `hoa_hoc`; Sinh → `sinh_hoc`;
   tổng hợp/đo lường/kỹ năng → `chung`.

---

## 4. Cách THÊM map mới (mở rộng skill về sau)

1. Tạo file `references/maps/MAP_<MÔN><LỚP>.md` theo header + cấu trúc mục 2.
2. Điền đủ Chương → Bài → khối nội dung. Có thể seed dần từng chương; đánh dấu phần chưa làm bằng
   `<!-- TODO: bổ sung -->` để lần sau hoàn thiện.
3. Thêm một dòng vào bảng index trong `references/maps/README.md`.
4. Nếu map dùng concept hình ảnh chưa có → bổ sung vào `assets/visual-keyword-library.json`
   (giữ đúng schema: `key`, `match`, `vi`, `en_keywords`, `icon_id`, `shape`, `subjects`).

> Nhờ tách map theo từng file `MAP_<MÔN><LỚP>.md`, có thể mở rộng sang lớp/môn mới mà **không
> đụng** tới SKILL.md hay các file khác — đúng tinh thần cấu trúc thư mục chuẩn, dễ cập nhật.

---

## 5. Tự cập nhật map khi phát hiện đơn vị mới

Khi tạo slide cho một bài mà phát hiện đơn vị kiến thức quan trọng **chưa có** trong map (hoặc bài
chưa được seed) → **tự động thêm** dòng `Đơn vị KT` / khối `Bài` mới vào đúng vị trí trong file map,
giữ đúng định dạng. Map là tài liệu sống, lớn dần theo lần dùng.
