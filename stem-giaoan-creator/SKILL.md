---
name: stem-giaoan-creator
description: >
  Soạn KẾ HOẠCH BÀI DẠY STEM (giáo án STEM, chuẩn GDPT 2018 / Công văn 5512) hoàn chỉnh, chi tiết
  và xuất ra file Word (.docx). MẶC ĐỊNH theo cấu trúc 5512: mỗi tiết là một bài dạy có I. MỤC TIÊU
  (Kiến thức / Năng lực chung + KHTN / Phẩm chất), II. THIẾT BỊ DẠY HỌC VÀ HỌC LIỆU (GV/HS),
  III. TIẾN TRÌNH DẠY HỌC với bảng 2 cột HOẠT ĐỘNG CỦA GIÁO VIÊN – HOẠT ĐỘNG CỦA HỌC SINH theo 4 bước
  (Chuyển giao → Thực hiện → Báo cáo → Kết luận) + "Sản phẩm cần đạt", IV. ĐÁNH GIÁ TRONG TIẾT HỌC,
  V. PHỤ LỤC (phiếu học tập); cuối bài có TIÊU CHÍ ĐÁNH GIÁ CHI TIẾT (rubric chấm điểm, tổng 100) và
  PHIẾU TỔNG HỢP KẾT QUẢ. Vẫn giữ tùy chọn cấu trúc EDP (khung A–E + bảng thử nghiệm) khi được yêu cầu.
  Hỗ trợ toàn bộ KHTN (Hóa/Lý/Sinh) chủ trì, tích hợp Toán/Công nghệ/Tin; số tiết linh hoạt.
  Dùng khi người dùng nói "soạn giáo án STEM", "kế hoạch bài dạy STEM", "thiết kế bài dạy STEM",
  "làm giáo án STEM về một chủ đề", hoặc nêu một chủ đề chế tạo/thực hành STEM (bình chữa cháy, pin
  chanh, lọc nước, làm xà phòng, lên men rượu, tên lửa nước...) và muốn xuất Word.
---

# STEM Giáo án Creator — Soạn Kế hoạch bài dạy STEM chuẩn 2018 (Công văn 5512)

## Khi yêu cầu chưa đủ cụ thể — PHẢN BIỆN TRƯỚC, LÀM SAU

Yêu cầu chung chung luôn cho ra sản phẩm kém. **Không đoán bừa, cũng không hỏi
lể tể từng ý.** Hãy nêu rõ đang thiếu gì, rồi đưa **một prompt mẫu đã điền sẵn
giá trị mặc định hợp lý** để người dùng sửa và gửi lại trong đúng một lượt.

Thiếu từ **2 tiêu chí trở lên** thì bắt buộc phản biện. Thiếu **đúng 1** tiêu chí
thì tự chọn mặc định, làm tiếp, và nói rõ đã chọn gì.

**Tiêu chí bắt buộc:** môn · lớp · tên bài · số tiết · bộ sách · hình thức tổ chức hoạt động

**Mẫu phản biện:**

> Yêu cầu hiện thiếu: **số tiết**, **bộ sách**. Nếu làm luôn thì tôi phải đoán, dễ lệch
> ý bạn. Bạn copy prompt dưới đây, sửa chỗ in đậm rồi gửi lại:
>
> ```
> Soạn giáo án STEM môn **KHTN** lớp **7**, bài **Quang hợp ở thực vật**.
> Số tiết: **2** · Bộ sách: **Cánh Diều**
> Hình thức: **hoạt động nhóm + thí nghiệm quan sát**
> Cần có: **mục tiêu theo phẩm chất – năng lực, phiếu học tập, rubric đánh giá**
> ```

---

## Mục tiêu của skill
Khi người dùng đưa ra MỘT CHỦ ĐỀ DỰ ÁN STEM (ví dụ: "lên men rượu từ trái cây", "chế tạo pin chanh",
"máy lọc nước mini", "tên lửa nước"...), skill này tạo ra một **giáo án STEM hoàn chỉnh, chi tiết, hấp dẫn**,
xuất ra **file Word (.docx)**.

**Cấu trúc đầu ra MẶC ĐỊNH = "5512"** — giống file mẫu "THIẾT KẾ BÀI DẠY STEM: LÊN MEN RƯỢU TỪ TRÁI CÂY":
mỗi TIẾT là một kế hoạch bài dạy đầy đủ với **I. MỤC TIÊU / II. THIẾT BỊ DẠY HỌC VÀ HỌC LIỆU /
III. TIẾN TRÌNH DẠY HỌC (bảng 2 cột GV–HS, 4 bước) / IV. ĐÁNH GIÁ TRONG TIẾT HỌC / V. PHỤ LỤC**,
và cuối bài có **TIÊU CHÍ ĐÁNH GIÁ CHI TIẾT** (rubric chấm điểm) + **PHIẾU TỔNG HỢP KẾT QUẢ**.

Vẫn **giữ tùy chọn cấu trúc cũ "edp"** (khung A–E theo quy trình thiết kế kỹ thuật + bảng thử nghiệm
Đạt/Không đạt). Chỉ dùng khi người dùng yêu cầu rõ ("theo EDP", "khung A–E", "có bảng thử nghiệm sản phẩm").

## Phạm vi
- Môn chủ trì: **toàn bộ KHTN** — Hóa học, Vật lý, Sinh học.
- Tích hợp: **Toán học, Công nghệ, Tin học** khi chủ đề cần.
- Cấp học: THCS và THPT (tự suy ra theo độ khó chủ đề và yêu cầu người dùng).
- Số tiết: **LINH HOẠT** — skill tự đề xuất số tiết phù hợp (thường 4–8 tiết). KHÔNG cứng nhắc 6 tiết.

## Quy trình làm việc (BẮT BUỘC theo thứ tự)

### Bước 0 — Xác định thông tin đầu vào
Nếu người dùng đã nêu chủ đề, BẮT ĐẦU NGAY. Chỉ hỏi lại khi thiếu thông tin tối thiểu.
Thông tin nên có (suy luận hợp lý nếu thiếu, KHÔNG hỏi dồn dập):
- Tên dự án / chủ đề.
- **Cấu trúc đầu ra**: mặc định **5512**; chỉ chuyển sang **edp** khi người dùng yêu cầu rõ.
- Môn chủ trì (suy ra từ chủ đề: cháy→Hóa, mạch điện→Lý, lên men→Sinh/Hóa...).
- Lớp / cấp học (mặc định suy theo độ phù hợp kiến thức CT 2018).
- Số tiết (nếu không nêu → tự đề xuất, ghi rõ lý do phân bổ).
- Thông tin trường/GV (header; nếu không có thì để placeholder `[Tên trường]`, `[Họ tên GV]`).

### Bước 1 — Nghiên cứu kiến thức nền (BẮT BUỘC kết hợp cào dữ liệu + nguồn quốc tế)
Phần kiến thức nền (đặc biệt **Phụ lục kiến thức liên quan**) phải dựa trên tài liệu THỰC, uy tín,
KHÔNG bịa số liệu kỹ thuật. Kết hợp 2 hướng:

**(a) Cào dữ liệu giáo dục Việt Nam — dùng skill `edu-scraper`:** thu thập lý thuyết, bài tập, ví dụ
liên quan chủ đề từ vietjack, loigiaihay, hoc247... Dùng cho ngữ liệu tiếng Việt, bám chương trình
(Cánh diều / Kết nối tri thức / Chân trời sáng tạo) và đúng cách diễn đạt SGK.

**(b) Tài liệu UY TÍN NƯỚC NGOÀI — dùng WebSearch + mcp__workspace__web_fetch:** tra cứu & trích dẫn
nguồn quốc tế tin cậy: Britannica, Khan Academy, LibreTexts, OpenStax, MIT OCW, RSC, NCBI/PubMed,
Nature, FAO, WHO, USDA, NASA... và tên miền `.edu`/`.gov`/`.org`. Lấy: định nghĩa chuẩn, phương
trình/cơ chế, số liệu định lượng (nhiệt độ, nồng độ, pH...), lưu ý an toàn.

**Yêu cầu:** đối chiếu ≥2 nguồn cho mỗi số liệu kỹ thuật quan trọng; cuối phần kiến thức thêm mục
**"Nguồn tham khảo"** (≥1–2 nguồn quốc tế, có link); diễn đạt lại tiếng Việt phù hợp HS nhưng giữ đúng
số liệu/cơ chế. Nếu không truy cập được nguồn, KHÔNG bịa — báo người dùng và dùng nguồn thay thế.

### Bước 2 — Thiết kế khung tiến trình
Đọc `references/cau_truc_giao_an.md` để lấy ĐẦY ĐỦ khung, câu chữ chuẩn, schema JSON và checklist.

**Với format 5512 (mặc định):** chia dự án thành các tiết/cụm tiết (xem gợi ý phân bổ trong references,
mẫu 6 tiết: Khởi động → Kiến thức nền & phương án → Hướng dẫn quy trình & an toàn → Thực hiện sản phẩm →
Trưng bày & đánh giá). Mỗi hoạt động trong III. Tiến trình bám đủ **4 bước**: Chuyển giao nhiệm vụ →
Thực hiện nhiệm vụ → Báo cáo, thảo luận → Kết luận, nhận định; trình bày bằng **bảng 2 cột GV–HS**;
kết mỗi hoạt động bằng **"Sản phẩm cần đạt"**.

**Với format edp:** bám quy trình EDP 6 bước, mỗi tiết khung A–E, tiết chế tạo có bảng thử nghiệm.

### Bước 3 — Viết nội dung từng tiết (format 5512)
Mỗi tiết PHẢI đủ:
- **I. MỤC TIÊU** — 1. Kiến thức; 2. Năng lực (a) chung, b) KHTN); 3. Phẩm chất. (Riêng đầu bài có
  **II. Mục tiêu CHUNG** cả dự án: thêm mục 4. Mục tiêu đối với sản phẩm STEM.)
- **II. THIẾT BỊ DẠY HỌC VÀ HỌC LIỆU** — 1. Giáo viên; 2. Học sinh.
- **III. TIẾN TRÌNH DẠY HỌC** — các HOẠT ĐỘNG có mốc thời gian; mỗi hoạt động có a) Mục tiêu,
  b) Tổ chức thực hiện (bảng 2 cột GV–HS, 4 bước), "Sản phẩm cần đạt". Viết lời dẫn GV cụ thể, câu hỏi
  định hướng, thao tác/câu trả lời mong đợi của HS.
- **IV. ĐÁNH GIÁ TRONG TIẾT HỌC** — 1. Phương pháp; 2. Công cụ (bảng Biểu hiện | Đạt | Chưa đạt).
- **V. PHỤ LỤC** — phiếu học tập riêng của tiết (PHIẾU HỌC TẬP SỐ n), có câu hỏi đánh số, chỗ điền,
  bảng để HS điền.

### Bước 4 — Viết phần đánh giá tổng & phụ lục kiến thức (format 5512)
- **TIÊU CHÍ ĐÁNH GIÁ CHI TIẾT** — các rubric chấm điểm (vd Sổ nhật kí 20đ, Sản phẩm 30đ, Poster 25đ,
  Thuyết trình 25đ), mỗi bảng cột `STT | Tiêu chí | Điểm tối đa` + dòng Tổng; kết bằng **PHIẾU TỔNG HỢP
  KẾT QUẢ** (tổng 100). Điều chỉnh hạng mục/điểm cho hợp chủ đề.
- **Phụ lục kiến thức liên quan** (tùy chọn nhưng nên có) — nguyên lý, PTHH, bảng yếu tố ảnh hưởng,
  lưu ý an toàn; xây từ edu-scraper + nguồn quốc tế (Bước 1); kết bằng "Nguồn tham khảo".

### Bước 5 — Xuất file Word
Dùng `scripts/build_giaoan.py` (python-docx) để render .docx. **SINH file JSON bằng một script Python**
(không viết tay) theo schema trong `references/cau_truc_giao_an.md` — để giữ nguyên dấu `\` của LaTeX.
Đặt `"format": "5512"` (hoặc `"edp"`). Lưu .docx ra thư mục làm việc, rồi CHÉP sang thư mục người dùng
đã chọn và chia sẻ qua present_files.

Lệnh: `python scripts/build_giaoan.py noi_dung.json "Giao_an_STEM_<TenDuAn>.docx"`

> File xuất ra từ `build_giaoan.py` ĐÃ tự chuẩn hóa (thụt lề bằng indent treo, font đồng bộ Times New
> Roman, không khoảng trắng rác) — KHÔNG cần chạy thêm bước chuẩn hóa cho file tự sinh.
>
> CHỈ chạy `scripts/normalize_format.py` khi file giáo án ĐẾN TỪ NGUỒN NGOÀI (convert từ PDF/Word khác,
> ghép nhiều nguồn) — vì các file đó hay dính đoạn trống, số trang rác, dòng bị dồn và thụt lề bằng dấu
> cách/tab. Lệnh: `python scripts/normalize_format.py input.docx [output.docx]`.

### Bước 6 — Kiểm tra (verification)
Rà checklist trong `references/cau_truc_giao_an.md` (đúng theo format đang dùng). Mở lại file .docx vừa
tạo để chắc chắn không lỗi định dạng và LaTeX còn nguyên dấu `\`. Kiểm tra nhanh: KHÔNG còn đoạn trống
thừa/số trang lạc; ý chính (–) và ý phụ (+) thụt lề đều bằng indent treo; toàn bộ chữ là Times New Roman.

## QUY TẮC ĐỊNH DẠNG (CHỐNG LỖI — BẮT BUỘC)
Để giáo án không phát sinh lỗi định dạng, LUÔN tuân thủ:
1. **Thụt lề bằng indent, KHÔNG bằng dấu cách/tab.** Renderer tự đặt dấu đầu dòng và indent treo (hanging)
   để dòng xuống dòng thẳng hàng. Tuyệt đối không gõ nhiều dấu cách/`\t` để căn lề trong nội dung JSON.
2. **Mỗi ý một phần tử riêng.** Không nhồi nhiều gạch đầu dòng vào một chuỗi; không chèn `\n` giữa chuỗi.
   Ý phụ: dùng dict `{"text": "...", "sub": ["..."]}` hoặc cho phần tử bắt đầu bằng `+`/`•`.
3. **Không tự thêm `– `/`- `/`+ ` vào đầu chuỗi bullet** — renderer tự thêm (nếu lỡ thêm, script tự bỏ).
4. **Không để đoạn trống thừa hay số trang** trong nội dung.
5. **Font:** chỉ Times New Roman; cỡ chữ và in đậm do renderer quyết định theo cấp tiêu đề.
6. Với file nhập từ ngoài: BẮT BUỘC chạy `scripts/normalize_format.py` trước khi giao cho người dùng.

## Quy ước CÔNG THỨC (LaTeX) — BẮT BUỘC
Mọi công thức hóa học, phương trình, biểu thức toán/lý viết ở dạng **LaTeX**:
- **Inline**: `$...$` — vd glucose $C_6H_{12}O_6$, khí $CO_2$, $28\text{–}32^\circ C$, $15\%\text{–}22\%$, pH $4{,}0\text{–}4{,}5$.
- **Display**: `\[...\]` — vd `\[C_6H_{12}O_6 \xrightarrow{\text{nấm men, yếm khí}} 2C_2H_5OH + 2CO_2\]`
- Lưu ý: `%`→`\%`, độ là `^\circ`, chỉ số dưới `_{...}`, chỉ số trên `^{...}`.

**CỰC KỲ QUAN TRỌNG — không để mất dấu `\`:** KHÔNG viết tay JSON cho chuỗi chứa LaTeX. Hãy tạo JSON
bằng một script Python: viết LaTeX bằng **raw string** `r"..."` rồi `json.dump(..., ensure_ascii=False)`.
`json.dump` tự nhân đôi `\`→`\\` khi ghi, `json.load` đọc lại đúng một `\`. (Xem ví dụ trong references.)

## Nguyên tắc chất lượng
- **Bám thực tiễn**: nêu thực trạng/vấn đề đời sống ở phần Mô tả chủ đề.
- **Vật liệu dễ kiếm, rẻ, an toàn**; ưu tiên tái chế.
- **Đúng chuẩn năng lực CT 2018**: năng lực KHTN + năng lực chung (tự chủ, giao tiếp–hợp tác, GQVĐ–sáng tạo) + phẩm chất.
- **Có định lượng**: PTHH, khối lượng/nồng độ/thể tích, tính toán tích hợp Toán.
- **Lời văn sư phạm, mạch lạc**; có lời dẫn GV, thao tác/câu trả lời HS, mốc thời gian.
- Bảng 2 cột GV–HS và các bảng phải dùng đúng renderer của script (không nhồi gạch đầu dòng lan man).

## Tài nguyên
- `references/cau_truc_giao_an.md` — khung đầy đủ cả 2 format (5512 & edp), schema JSON, rubric, checklist.
- `scripts/normalize_format.py` — chuẩn hóa định dạng cho MỌI .docx (xóa rác, thụt lề indent treo, đồng
  bộ font, tô header bảng); dùng cho file nhập từ ngoài hoặc khi cần “dọn” lại một giáo án cũ.
- `scripts/build_giaoan.py` — sinh file .docx từ JSON (tự nhận `format`: 5512 mặc định, hoặc edp).


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
