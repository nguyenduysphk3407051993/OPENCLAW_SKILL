---
name: bilingual-learning-creator
description: "Skill soạn tài liệu học tập SONG NGỮ Việt–Anh xuất ra file Word .docx cho giáo dục phổ thông Việt Nam. Hai chế độ: (1) CLIL — dạy nội dung Khoa học tự nhiên (Vật lí, Hoá học, Sinh học, KHTN lớp 6–12) bằng song ngữ với thuật ngữ đối chiếu, bài đọc 2 cột, mẫu câu học thuật; (2) English — học tiếng Anh THCS–THPT có đối chiếu tiếng Việt với bài đọc kèm dịch, ngữ pháp giải thích bằng tiếng Việt, bài tập song ngữ. Hỗ trợ dịch phân tích SONG SONG TỪNG CÂU hoặc TỪNG ĐOẠN, mỗi đơn vị kèm chú giải thì, cấu trúc ngữ pháp, từ vựng có từ loại và phiên âm IPA, cụm từ hay dùng. Sử dụng khi người dùng cần: tài liệu song ngữ, học song ngữ, dạy KHTN bằng tiếng Anh, bài đọc Anh–Việt đối chiếu, bảng thuật ngữ khoa học Việt–Anh, phiếu học tập song ngữ, dịch có phân tích ngữ pháp, glossary, phrasebook, hoặc bất kỳ tài liệu nào cần trình bày cả tiếng Việt lẫn tiếng Anh cạnh nhau."
allowed-tools: Read, Write, Edit, Glob, Grep, Bash, WebFetch
argument-hint: "[chế độ clil/english] [môn hoặc chủ đề] [lớp] [trình độ CEFR]"
---

# Bilingual Learning Creator — Tài liệu song ngữ Việt–Anh ra Word

Skill soạn tài liệu dạy học song ngữ và dựng thành file `.docx` phát được cho học sinh.

## Nguồn tra cứu bắt buộc — Cambridge Dictionary

**Mọi phiên âm IPA, từ loại, nghĩa và ví dụ tiếng Anh phải tra tại `https://dictionary.cambridge.org/`** bằng `WebFetch`, không được viết theo trí nhớ.

- Tra một từ: `https://dictionary.cambridge.org/dictionary/english/<từ>` (thay dấu cách bằng `-`).
- Tra nghĩa Anh–Việt: `https://dictionary.cambridge.org/dictionary/english-vietnamese/<từ>`.
- Lấy **IPA Anh–Anh (UK)** làm chuẩn, đúng như Cambridge ghi, giữ nguyên dấu `/.../`. Nếu cần cả UK và US thì ghi `UK /.../ · US /.../`.
- Từ loại lấy đúng nhãn Cambridge, rút gọn về: `n`, `v`, `adj`, `adv`, `prep`, `conj`, `phr.v`, `idiom`.
- Nếu Cambridge không có mục từ (thuật ngữ khoa học chuyên sâu như *photosynthesis rate*, danh pháp IUPAC), tra từng thành phần rồi **ghi rõ trong `note_vi` là IPA ghép, chưa kiểm chứng nguyên cụm**. Không bịa.

Quy tắc thực hành: gom danh sách từ cần tra rồi tra một lượt trước khi soạn, đừng tra rải rác giữa chừng. Với tài liệu nhiều từ, ưu tiên tra những từ đưa vào bảng `glossary`, `vocab` và `phrasebook` — đó là chỗ học sinh chép lại.

## Hai chế độ

| Chế độ | Dùng khi | Trọng tâm |
|---|---|---|
| `clil` | Dạy Vật lí / Hoá / Sinh / KHTN bằng song ngữ | Thuật ngữ khoa học chính xác, mẫu câu mô tả thí nghiệm, nội dung khoa học đúng |
| `english` | Dạy tiếng Anh THCS–THPT | Ngữ pháp giải thích bằng tiếng Việt, từ vựng theo CEFR, kỹ năng đọc dịch |

## Quy trình

1. **Xác định**: chế độ, môn/chủ đề, khối lớp, trình độ CEFR mục tiêu, độ dài, có cần đáp án không.
2. **Đọc tham chiếu** phù hợp trong `references/` trước khi soạn (xem bảng dưới).
3. **Soạn nội dung** thành file JSON trung gian theo đúng `assets/schema.json`.
4. **Tra Cambridge** cho toàn bộ IPA và từ loại đã dùng.
5. **Dựng file Word**:
   ```bash
   python scripts/build_bilingual_docx.py <input.json> -o output/<tên>.docx
   ```
6. **Verify**: file tồn tại, kích thước > 0, mở lại bằng `python-docx` kiểm tra tiếng Việt có dấu không vỡ. Chỉ báo xong sau khi verify.

Script tự validate JSON trước khi dựng — sai schema thì nó báo rõ section thứ mấy hỏng và thoát, không sinh file lỗi.

## Kho tham chiếu

| File | Đọc khi |
|---|---|
| `references/clil-science-glossary.md` | Cần thuật ngữ KHTN Việt–Anh (~200 mục, có IPA và **bẫy dịch**) |
| `references/clil-sentence-frames.md` | Cần mẫu câu mô tả thí nghiệm, nhân quả, so sánh, diễn giải số liệu |
| `references/english-grammar-vi.md` | Cần giải thích ngữ pháp bằng tiếng Việt, chọn điểm ngữ pháp theo CEFR |
| `references/phrasebook.md` | Cần collocation, phrasal verb, cụm nối ý, ngôn ngữ lớp học (158 cụm) |
| `references/translation-guide.md` | Làm section `translation` — khác biệt cấu trúc Việt–Anh, quy trình dịch 4 bước |

## Bảy loại section

Ghép tự do theo nhu cầu, không bắt buộc dùng hết.

| Loại | Công dụng |
|---|---|
| `glossary` | Bảng thuật ngữ đối chiếu. Có `group_by: "pos"` để tách bảng theo từ loại |
| `parallel_text` | Đọc đối chiếu 2 cột. `granularity` chọn `sentence` (căn từng câu) hay `paragraph` |
| `translation` | **Dịch phân tích từng đơn vị** — xem mục riêng bên dưới |
| `phrasebook` | Sổ tay cụm từ, tự nhóm theo `kind` |
| `sentence_frames` | Khung câu dùng lại được, nhóm theo `function_vi` |
| `grammar` | Điểm ngữ pháp: công thức, dấu hiệu nhận biết, `contrast_with` để so cặp dễ nhầm, `pitfalls_vi` |
| `exercise` | Bài tập. `task`: `mcq`, `fill`, `matching`, `translate_vi2en`, `translate_en2vi`, `writing` |

## Section `translation` — dịch song song có chú giải

Đây là phần đắt giá nhất của skill. Mỗi `unit` là một câu (hoặc một đoạn, tuỳ `granularity`) được dịch **và mổ xẻ**:

- `source` / `target` — câu gốc và bản dịch, `direction` quyết định chiều (`vi2en` hoặc `en2vi`).
- `literal` — dịch sát nghĩa đen, bật bằng `show_literal: true`. Dùng để chỉ cho học sinh thấy chỗ hai thứ tiếng lệch cấu trúc.
- `tense` — thì và thể của câu tiếng Anh, ghi cả tên Việt lẫn Anh: `"Hiện tại hoàn thành (Present Perfect)"`.
- `structures[]` — cấu trúc ngữ pháp: `pattern` (vd `S + be + V3 + by + O`), `name_vi`, `explain_vi`.
- `vocab[]` — từ đáng học: `word`, `pos`, `ipa`, `vi`, `forms`, `note_vi`.
- `phrases[]` — cụm đáng nhớ trong câu đó.
- `note_vi` — lưu ý dịch thuật riêng cho câu.

**Nguyên tắc chọn chú giải:** mỗi câu chỉ lấy **2–4 từ vựng đáng học ở đúng trình độ người học**. Đừng chú giải từ quá dễ (*water*, *big*) hay quá hiếm. Không nhồi hết mọi từ trong câu — tài liệu sẽ thành từ điển, học sinh không đọc.

## Nguyên tắc chất lượng

1. **Tiếng Anh sai là dạy sai cả lớp.** Không chắc thì tra Cambridge, không đoán.
2. **Nội dung khoa học phải đúng** ở chế độ `clil` — công thức, đơn vị, danh pháp IUPAC theo SGK Kết nối tri thức (*sodium*, *potassium*, không phải natri/kali).
3. **Cảnh báo bẫy dịch** ở `note_vi` khi gặp cặp dễ nhầm: *mass* ≠ *weight*, *temperature* ≠ *heat*, *respiration* ≠ *breathing*, *reaction* ≠ *reflex*, *transpiration* ≠ *evaporation*.
4. **Tiếng Việt dùng thuật ngữ SGK Kết nối tri thức với cuộc sống.**
5. **UTF-8 có dấu.** Đọc/ghi file phải chỉ định `encoding="utf-8"`.

## Ví dụ có sẵn

- `examples/clil_vat_li_8_dong_nang.json` — CLIL Vật lí 8, động năng, phủ đủ 7 loại section.
- `examples/english_unit_environment.json` — English A2, chủ đề môi trường, `answer_key: false`.
- `examples/translation_analysis_demo.json` — demo đầy đủ nhất của `translation` và `phrasebook`.

Đọc một file ví dụ trước khi soạn JSON mới — nhanh hơn đọc schema.

## Yêu cầu môi trường

`pip install -r requirements.txt` (cần `python-docx`).
