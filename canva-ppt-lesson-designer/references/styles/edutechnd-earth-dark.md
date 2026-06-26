# Style: EduTechND Earth (Dark)

**Vibe.** Nền tối học thuật, tông vàng đất ấm — gợi bảng phấn cũ gặp thiết kế đương đại. Sang trọng, dễ đọc trên máy chiếu, phù hợp lớp học ban ngày lẫn phòng tối. Tham chiếu trực tiếp từ bộ slide ANKENE.pptx (file thực tế đang dùng tại EduTechND).

**Best for.** Bài giảng KHTN (Vật lý, Hoá học, Sinh học) THCS theo GDPT 2018, slide EduTechND thương hiệu, bài giảng tiếng Việt trên nền tối.

## Canvas

**20" × 11.25"** (tỉ lệ 16:9, kích thước mở rộng). Đây là canvas chuẩn đang dùng tại EduTechND — mọi font size, toạ độ shape trong file này đều tính theo canvas này.

```python
prs.slide_width  = Inches(20)
prs.slide_height = Inches(11.25)
```

## Palette

| Role | Hex | Tên | Tỉ lệ |
|---|---|---|---|
| Background / text chính (trên nền sáng) | `#3F2313` | Nâu đậm sô-cô-la | ~40% (nền section + text chính) |
| Surface / khối nền phụ, vàng đất | `#D7A550` | Vàng đất / gold | ~25% |
| Accent (shape, fill, nhấn mạnh) | `#D28119` | Amber / cam đất | ~20% |
| Ink sáng (chữ trên nền tối) | `#FCFBF9` | Trắng kem | text trên nền tối |
| Ink sáng 2 | `#F2F3EC` | Trắng ngà | text section header |
| Nâu trung (hỗ trợ) | `#75502C` | Nâu trung | fill phụ |
| Amber tối (label, phụ đề) | `#6A4115` / `#6B4408` | Nâu amber | text phụ, label |

Quy tắc dùng màu:
- **Nền section header / title bar:** `#3F2313` (nâu đậm) với text `#F2F3EC` (trắng ngà)
- **Fill shape / panel nổi bật:** `#D7A550` (vàng đất) hoặc `#D28119` (amber)
- **Text chính trên nền sáng:** `#3F2313`
- **Text sáng trên nền tối:** `#FCFBF9` hoặc `#F2F3EC`
- **Label / phụ đề / accent text:** `#6A4115`
- Nếu cần phân biệt thêm, dùng opacity (70%, 50%) thay vì thêm màu ngoài gam.

## Typography (font 9Slide — BẮT BUỘC)

Ưu tiên font 9Slide, bổ sung Noto Sans/Serif cho heading có tính cách riêng.

### Font 9Slide (chính — dùng cho body, label, caption)

| Vai trò | Font | Điều kiện |
|---|---|---|
| Tiêu đề ngắn (≤ 25 ký tự) | `#9Slide01 Tieu de ngan` | Slide title, label video |
| Tiêu đề dài (26–50 ký tự) | `#9Slide02 Tieu de dai` | Tên bài, mục tiêu, chương dài |
| Tiêu đề rất dài (> 50 ký tự) | `#9Slide02 Tieu de rat dai 01` hoặc `02` | Câu hỏi dài, tên chủ đề kép |
| Nội dung ngắn | `#9Slide01 Noi dung ngan` | Bullet ngắn, label, caption |
| Nội dung dài | `#9Slide02 Noi dung dai` | Đoạn văn, giải thích, nội dung chính |
| Nội dung rất dài | `#9Slide02 Noi dung rat dai` | Đoạn dài trên slide nội dung chuyên sâu |

### Font phụ (heading có tính cách — tạo tương phản với 9Slide)

| Vai trò | Font | Ghi chú |
|---|---|---|
| Section title lớn | `Noto Sans Bold` | Cho tên bài, tên chương — kích thước 63–95pt |
| Sub-heading học thuật | `Noto Serif Bold` | Cho "Định nghĩa", "Công thức chung" — serif trang nghiêm |

**Quy tắc tương phản font:** BẮT BUỘC kết hợp serif cho TIÊU ĐỀ + sans-serif cho NỘI DUNG (hoặc ngược lại). Trong file ANKENE: `Noto Sans Bold` (sans) cho heading + `#9Slide02 Noi dung dai` cho body; hoặc `Noto Serif Bold` (serif) cho sub-label + `#9Slide02 Noi dung dai` cho body.

### Font sizes (canvas 20" × 11.25")

| Element | Size | Font |
|---|---|---|
| Section title (tên chủ đề lớn) | 63–95pt bold | Noto Sans Bold |
| Slide title (tên mục) | 44–72pt bold | #9Slide01 Tieu de ngan / #9Slide02 Tieu de dai |
| Sub-heading (định nghĩa, khái niệm) | 40–46pt bold | Noto Serif Bold |
| Body text | 36pt regular | #9Slide02 Noi dung dai |
| Body text (nhỏ hơn) | 28–32pt | Noto Sans / #9Slide02 Noi dung dai |
| Caption / label | 24–28pt | #9Slide02 Noi dung dai / #9Slide01 Noi dung ngan |
| Footnote | 18pt muted | #9Slide01 Noi dung ngan |

## Nghệ thuật sếp chữ (Typography Art)

Slide chuyên nghiệp phân biệt với slide nghiệp dư chủ yếu ở cách sếp chữ. Mục này hướng dẫn nguyên tắc phân cấp, tương phản, và nhịp điệu chữ trong hệ thiết kế EduTechND Earth.

### 1. Phân cấp chính — phụ (Visual Hierarchy)

Mỗi slide có **tối đa 4 tầng chữ**, từ quan trọng nhất đến ít quan trọng nhất:

| Tầng | Vai trò | Font | Size | Weight | Màu |
|---|---|---|---|---|---|
| **Tầng 1** — Headline | Tên bài / tên chủ đề lớn | `Noto Sans Bold` | 63–95pt | **Bold** | `#F2F3EC` trên nền `#3F2313` |
| **Tầng 2** — Slide title | Tên mục kiến thức | `#9Slide01 Tieu de ngan` | 44–72pt | **Bold** | `#FCFBF9` trên nền tối, hoặc `#3F2313` trên nền sáng |
| **Tầng 3** — Sub-heading | Định nghĩa, khái niệm, nhãn nhóm | `Noto Serif Bold` | 40–46pt | **Bold** | `#6A4115` (amber tối) |
| **Tầng 4** — Body | Nội dung chính, giải thích | `#9Slide02 Noi dung dai` | 36pt | Regular | `#3F2313` trên panel sáng |

Bổ sung:
- **Caption / label**: `#9Slide01 Noi dung ngan` 24–28pt regular, màu `#75502C` (nâu trung)
- **Footnote**: 18pt regular, opacity 60%

**Quy tắc vàng:** Tỉ lệ kích thước giữa các tầng phải ≥ 1.3×. Ví dụ: Headline 63pt → Title 48pt → Sub-heading 40pt → Body 36pt. Nếu 2 tầng cùng size, mắt không phân biệt được → mất phân cấp.

### 2. Tương phản Sans-serif × Serif (Không chân × Có chân)

Đây là nguyên tắc cốt lõi: **KHÔNG BAO GIỜ dùng cùng loại font cho heading và body trên cùng slide.**

| Cặp ghép | Heading (chữ LỚN) | Body (chữ NHỎ) | Hiệu ứng |
|---|---|---|---|
| **Cặp A — Chuẩn ANKENE** | `Noto Sans Bold` (sans) | `#9Slide02 Noi dung dai` (sans mềm) | Hiện đại, rõ ràng, dễ scan |
| **Cặp B — Học thuật** | `Noto Serif Bold` (serif) | `#9Slide02 Noi dung dai` (sans mềm) | Trang nghiêm, định nghĩa, công thức |
| **Cặp C — Tương phản tối đa** | `Noto Sans Bold` (sans cứng) | `Noto Serif Bold` (serif mềm) — chỉ cho sub-label | Nhấn mạnh sự khác biệt giữa tiêu đề và chú thích |

**Giải mã "sans mềm" vs "sans cứng":**
- `Noto Sans Bold` = **sans cứng** — nét đều, góc vuông, khẳng định, mạnh mẽ, thích hợp làm headline
- `#9Slide02 Noi dung dai` = **sans mềm** — nét mảnh hơn, bo tròn nhẹ, thân thiện, dễ đọc đoạn dài
- `Noto Serif Bold` = **serif cứng** — chân chữ rõ ràng, học thuật, cổ điển, uy quyền
- `#9Slide01 Noi dung ngan` = **sans mềm nhỏ** — gọn, nhẹ, phù hợp caption và label

### 3. Tương phản Bold × Regular (In đậm × Không in đậm)

Bold không chỉ là "tô đậm" — nó tạo **trọng lượng thị giác** (visual weight).

**Nguyên tắc:**
- **Tầng 1–3 (Headline → Sub-heading): LUÔN Bold.** Đây là điểm mắt nhìn đầu tiên.
- **Tầng 4 (Body): LUÔN Regular.** Chữ đậm liên tục → mắt mệt, không biết nhìn đâu.
- **Nhấn trong body:** Nếu cần nhấn 1 từ/cụm trong đoạn body, dùng **Bold + màu accent `#D28119`** cho riêng cụm đó — KHÔNG bôi đậm cả dòng.

| Tình huống | Cách làm đúng | Cách làm sai |
|---|---|---|
| Tiêu đề bài | `Noto Sans Bold` 63pt **Bold** | Regular 63pt (yếu, không phân biệt) |
| Body giải thích | `#9Slide02` 36pt Regular | Bold 36pt (nặng, mệt mắt) |
| Nhấn 1 từ khoá | "...có một liên kết **C = C**" (bold + accent) | Cả dòng bold |
| Caption | Regular 24pt, màu nâu trung | Bold 24pt (quá nặng cho vai phụ) |

### 4. Font cứng × Font mềm mại (Personality Contrast)

Mỗi font có "tính cách" — kết hợp đúng tạo nhịp thở cho slide.

| Tính cách | Font trong hệ thống | Đặc điểm | Dùng khi |
|---|---|---|---|
| **Cứng, mạnh** | `Noto Sans Bold` | Nét đều, tỉ lệ đều, không trang trí | Headline, section — cần SỰ CHÚ Ý |
| **Trang nghiêm, uy quyền** | `Noto Serif Bold` | Chân chữ, nét thanh đậm xen kẽ | Định nghĩa, công thức, trích dẫn — cần SỰ TIN CẬY |
| **Mềm, thân thiện** | `#9Slide02 Noi dung dai` | Bo tròn nhẹ, nét mảnh, thư giãn | Body, giải thích — cần SỰ THOẢI MÁI KHI ĐỌC |
| **Nhẹ, gọn** | `#9Slide01 Noi dung ngan` | Compact, nét đều, tiết kiệm chỗ | Caption, label, ghi chú — cần SỰ KHIÊM TỐN |

**Công thức ghép tính cách trên 1 slide:**

```
Headline = CỨNG (Noto Sans Bold) — thu hút, ra lệnh
    ↓
Sub-heading = TRANG NGHIÊM (Noto Serif Bold) — xác nhận, đặt nền
    ↓
Body = MỀM (9Slide02 Noi dung dai) — giải thích, kể chuyện
    ↓
Caption = NHẸ (9Slide01 Noi dung ngan) — bổ sung, không tranh chấp
```

Bốn tầng này tạo **nhịp điệu thị giác**: mắt đi từ mạnh → vừa → nhẹ → rất nhẹ, giống nhịp đọc sách (tiêu đề → đề mục → nội dung → chú thích).

### 5. Quy tắc cấm (Typography Anti-patterns)

- **KHÔNG** dùng cùng 1 font + size cho heading và body → mất phân cấp
- **KHÔNG** Bold toàn bộ body → mọi thứ đều quan trọng = không gì quan trọng
- **KHÔNG** mix > 3 font families trên 1 slide → hỗn loạn
- **KHÔNG** dùng serif cho body dài (> 4 dòng) trên slide chiếu — serif đọc tốt trên giấy, không tốt trên màn chiếu khoảng cách xa
- **KHÔNG** scale heading nhỏ hơn 1.3× body — tương phản quá yếu, mắt không nhận ra phân cấp
- **KHÔNG** dùng italic thay bold để nhấn trên slide — italic khó đọc ở khoảng cách chiếu

### 6. Ví dụ áp dụng trên slide thực tế

```
┌─────────────────────────────────────────────────────────┐
│  [Title bar #3F2313]                                    │
│  KHÁI NIỆM ALKENE          ← Noto Sans Bold 63pt BOLD  │
│                                #F2F3EC (trắng ngà)      │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  Định nghĩa                ← Noto Serif Bold 44pt BOLD │
│                                #6A4115 (amber tối)      │
│                                                         │
│  ┌──────────────────────────────────────────────┐       │
│  │ Panel #D7A550                                │       │
│  │                                              │       │
│  │ Alkene là hydrocarbon không no, mạch hở,     │       │
│  │ phân tử có một liên kết đôi C = C            │       │
│  │        ← 9Slide02 Noi dung dai 36pt Regular  │       │
│  │           #3F2313 (nâu đậm)                  │       │
│  │                                              │       │
│  │ Công thức chung: CₙH₂ₙ (n ≥ 2)              │       │
│  │        ← 9Slide02 Noi dung dai 36pt          │       │
│  │           "CₙH₂ₙ" BOLD + #D28119 (accent)   │       │
│  │                                              │       │
│  │ Nguồn: SGK Hoá 9, tr.45                      │       │
│  │        ← 9Slide01 Noi dung ngan 24pt Regular │       │
│  │           #75502C (nâu trung)                │       │
│  └──────────────────────────────────────────────┘       │
└─────────────────────────────────────────────────────────┘
```

Trong ví dụ trên:
- **4 tầng phân cấp** rõ ràng: 63pt → 44pt → 36pt → 24pt
- **Sans × Serif**: Noto Sans Bold (headline) ↔ Noto Serif Bold (sub-heading)
- **Bold × Regular**: heading bold, body regular, chỉ bold cụm "CₙH₂ₙ"
- **Cứng × Mềm**: Noto Sans (cứng) → Noto Serif (trang nghiêm) → 9Slide02 (mềm) → 9Slide01 (nhẹ)

## Motif

**Thanh title bar nền tối + khối nền vàng đất cho nội dung.** Mỗi content slide có:
- Phía trên: title bar group nền `#3F2313` chứa tên chủ đề font `Noto Sans Bold` 63pt màu `#F2F3EC`
- Bên dưới: panel nội dung `#D7A550` hoặc group shape chứa text `#3F2313`
- Các shape trang trí dùng `#D28119` (amber) cho accent, viền, nút
- Trang trí: hình tròn nhỏ `#D7A550`, `#AB7E41`, `#3F2313`, `#75502C`, `#C7B5A5` xếp dọc làm motif palette bên trái (tham khảo slide 5 ANKENE)

```python
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

# --- Hằng số màu (đồng bộ ANKENE.pptx) ---
BG_DARK  = "3F2313"   # nền tối / text chính
SURFACE  = "D7A550"   # vàng đất, panel nội dung
ACCENT   = "D28119"   # amber, fill shape, nhấn
INK_LIGHT = "FCFBF9"  # text sáng trên nền tối
INK_LIGHT2 = "F2F3EC" # text section header
BROWN_MID = "75502C"  # fill phụ
AMBER_DARK = "6A4115" # text phụ, label

# --- Canvas ---
prs.slide_width  = Inches(20)
prs.slide_height = Inches(11.25)

# --- Title bar (group ở top) ---
title_bar = slide.shapes.add_shape(
    MSO_SHAPE.ROUNDED_RECTANGLE,
    Inches(6.2), Inches(0.4), Inches(8.6), Inches(1.5)
)
title_bar.fill.solid()
title_bar.fill.fore_color.rgb = RGBColor.from_string(BG_DARK)
title_bar.line.fill.background()
title_bar.adjustments[0] = 0.15

# --- Section title ---
title_box = slide.shapes.add_textbox(
    Inches(6.7), Inches(0.5), Inches(7.5), Inches(1.2)
)
tf = title_box.text_frame; tf.word_wrap = True
run = tf.paragraphs[0].add_run()
run.text = "Khái niệm alkene"
run.font.name = "Noto Sans Bold"
run.font.size = Pt(63); run.font.bold = True
run.font.color.rgb = RGBColor.from_string(INK_LIGHT2)

# --- Panel nội dung (vàng đất) ---
panel = slide.shapes.add_shape(
    MSO_SHAPE.ROUNDED_RECTANGLE,
    Inches(0.8), Inches(6.1), Inches(18.1), Inches(4.7)
)
panel.fill.solid()
panel.fill.fore_color.rgb = RGBColor.from_string(SURFACE)
panel.line.fill.background()
panel.adjustments[0] = 0.02

# --- Body text trong panel ---
body = slide.shapes.add_textbox(
    Inches(1.7), Inches(7.4), Inches(14.7), Inches(0.7)
)
body.text_frame.word_wrap = True
r = body.text_frame.paragraphs[0].add_run()
r.text = "1. Các công thức cấu tạo trên đều mạch hở, có một liên kết C = C"
r.font.name = "#9Slide02 Noi dung dai"
r.font.size = Pt(36)
r.font.color.rgb = RGBColor.from_string(BG_DARK)

# --- Motif palette dots (cạnh trái) ---
dot_colors = [SURFACE, "AB7E41", BG_DARK, BROWN_MID, "C7B5A5"]
for i, c in enumerate(dot_colors):
    dot = slide.shapes.add_shape(
        MSO_SHAPE.OVAL,
        Inches(-1.3), Inches(1.3 + i*1.0), Inches(0.7), Inches(0.7)
    )
    dot.fill.solid()
    dot.fill.fore_color.rgb = RGBColor.from_string(c)
    dot.line.fill.background()
```

## Layout DNA (6 mẫu layout chính)

Rút từ DNA thiết kế ANKENE.pptx + 9Slide (bảng phấn, flat, infographic). Canvas 20" × 11.25".

### Layout 1: Slide Tiêu đề (Title / Cover) — ref: ANKENE slide 2
- Nền: freeform shape trang trí kín slide
- Tiêu đề bài giảng: `Noto Sans Bold` 157pt bold, màu `#1A1713`, đặt giữa-phải
- Group graphic minh hoạ bên trái (icon, phân tử, hình tượng)
- Công thức chung nhỏ phía dưới (VD: CₙH₂ₙ)
- KHÔNG dùng subtitle — chỉ tên chủ đề lớn + visual

### Layout 2: Mục tiêu bài học (Objectives) — ref: ANKENE slide 3
- Panel `#D7A550` (vàng đất) bo góc chiếm gần toàn slide
- Title bar nhỏ `#3F2313` ở trên, text "MỤC TIÊU BÀI HỌC" font `#9Slide02 Tieu de dai` 72pt bold
- Mỗi mục tiêu 1 dòng, bắt đầu bằng emoji (🎯🔬🏭⚙️) + text `#9Slide02 Tieu de dai` 32pt
- Icon graphic atom nhỏ ở góc phải

### Layout 3: Nội dung bài / Mục lục (Agenda) — ref: ANKENE slide 4
- Title lớn `Noto Sans Bold` 95pt, màu `#6A4115`
- Đường kẻ ngang mỏng phân cách
- 3 group box xếp dọc, mỗi box chứa tên mục (icon + text), khoảng cách đều nhau

### Layout 4: Một đơn vị kiến thức (Single Concept) — ref: ANKENE slide 5-7
- Title bar nền `#3F2313` ở góc trên phải, text `Noto Sans Bold` 63pt màu `#F2F3EC`
- Palette dots (5 chấm tròn dọc cạnh trái) làm motif
- Panel nội dung nền `#D7A550` ở nửa dưới, text `#9Slide02 Noi dung dai` 36pt màu `#3F2313`
- Vùng giữa: 2–3 group shape (hình minh hoạ, CTCT, icon) xếp hàng ngang
- Margin ≥ 0.8", gap giữa group = 0.5"

### Layout 5: So sánh / 2 cột (Comparison)
- Title bar nền `#3F2313` chuẩn ở top
- 2–3 group box ngang, mỗi box nền `#D7A550` bo góc, chứa CTCT hoặc so sánh
- Label bên dưới mỗi box: font `Noto Sans Bold` 32pt, màu `#3F2313`
- Mũi tên / dấu +CH₂ nối giữa các box, font `Noto Sans Bold` 28pt, màu `#6A4115`

### Layout 6: Slide phản ứng hoá học (Reaction) — ref: ANKENE slide 19-25
- Title bar chuẩn
- Phương trình hoá học ở giữa: font `#9Slide02 Tieu de dai` 48–64pt, màu `#3F2313`
- Mũi tên phản ứng `#D28119`
- Box điều kiện (tₒ, p, xt) nhỏ phía trên mũi tên
- Nhận xét / ý nghĩa: font `#9Slide02 Noi dung dai` 36pt, panel `#D7A550` bên dưới

### Layout 7: Video — ref: ANKENE slide 9, 15-16
- Media shape chiếm ~75% giữa slide
- Label "Video" phía trên: `#9Slide01 Tieu de ngan` 44pt, màu `#3F2313`
- Nguồn: footer nhỏ `#9Slide01 Tieu de ngan` 44pt

### Layout 8: Trắc nghiệm / Củng cố (Quiz) — ref: ANKENE slide 35-40
- Câu hỏi ở trên: bold 36pt
- 4 ô đáp án (A, B, C, D) xếp 2×2, nền `#D28119` hoặc `#D7A550`
- Mỗi ô: chữ cái lớn + nội dung đáp án
- Nút ">" để chuyển slide (hoặc animation)

## Signature slide: Slide đơn vị kiến thức (canvas 20" × 11.25")

```python
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN

prs = Presentation()
prs.slide_width = Inches(20); prs.slide_height = Inches(11.25)
blank = prs.slide_layouts[6]
slide = prs.slides.add_slide(blank)

BG_DARK = "3F2313"; SURFACE = "D7A550"; ACCENT = "D28119"
INK_LIGHT = "FCFBF9"; INK_LIGHT2 = "F2F3EC"
BROWN_MID = "75502C"; AMBER_DARK = "6A4115"

# --- Title bar (nền tối, góc trên phải) ---
title_bar = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,
    Inches(6.2), Inches(0.4), Inches(8.6), Inches(1.5))
title_bar.fill.solid()
title_bar.fill.fore_color.rgb = RGBColor.from_string(BG_DARK)
title_bar.line.fill.background()
title_bar.adjustments[0] = 0.15

# --- Section title ---
ttl = slide.shapes.add_textbox(Inches(6.7), Inches(0.5), Inches(7.5), Inches(1.2))
ttl.text_frame.word_wrap = True
r = ttl.text_frame.paragraphs[0].add_run()
r.text = "Khái niệm alkene"
r.font.name = "Noto Sans Bold"; r.font.size = Pt(63)
r.font.bold = True; r.font.color.rgb = RGBColor.from_string(INK_LIGHT2)

# --- Palette dots motif (cạnh trái) ---
dots = [SURFACE, "AB7E41", BG_DARK, BROWN_MID, "C7B5A5"]
for i, c in enumerate(dots):
    d = slide.shapes.add_shape(MSO_SHAPE.OVAL,
        Inches(0.3), Inches(1.3 + i*1.0), Inches(0.7), Inches(0.7))
    d.fill.solid(); d.fill.fore_color.rgb = RGBColor.from_string(c)
    d.line.fill.background()

# --- Panel nội dung (vàng đất, nửa dưới) ---
panel = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,
    Inches(0.8), Inches(6.6), Inches(18.1), Inches(4.0))
panel.fill.solid()
panel.fill.fore_color.rgb = RGBColor.from_string(SURFACE)
panel.line.fill.background()
panel.adjustments[0] = 0.02

# --- Body text ---
body = slide.shapes.add_textbox(Inches(1.7), Inches(7.4), Inches(14.7), Inches(2.5))
body.text_frame.word_wrap = True
items = [
    "1. Các công thức cấu tạo trên đều mạch hở, có một liên kết C = C",
    "2. Công thức chung của các alkene là: CₙH₂ₙ (n ≥ 2)."
]
for i, txt in enumerate(items):
    p = body.text_frame.paragraphs[0] if i == 0 else body.text_frame.add_paragraph()
    p.space_before = Pt(12)
    r = p.add_run()
    r.text = txt
    r.font.name = "#9Slide02 Noi dung dai"; r.font.size = Pt(36)
    r.font.color.rgb = RGBColor.from_string(BG_DARK)

# --- Vùng hình minh hoạ (giữa slide, 3 group boxes) ---
for j, (x, w) in enumerate([(3.0, 3.6), (7.0, 4.4), (11.8, 5.1)]):
    box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,
        Inches(x), Inches(2.5), Inches(w), Inches(3.6))
    box.fill.solid()
    box.fill.fore_color.rgb = RGBColor.from_string(SURFACE)
    box.line.fill.background()
    box.adjustments[0] = 0.05
```

## Gợi ý từ khoá tìm kiếm (icon, hình ảnh, video)

Khi dùng design system này cho bài giảng KHTN, luôn kèm từ khoá tìm kiếm phù hợp:

### Từ khoá icon (Canva / Flaticon / Noun Project)
- `atom icon flat`, `molecule icon dark background`, `science education icon set`
- `chemistry flask icon`, `biology cell icon`, `physics force diagram icon`
- `process arrow icon`, `comparison icon`, `checklist icon education`
- `experiment lab icon`, `microscope icon flat`, `periodic table icon`

### Từ khoá hình ảnh (Unsplash / Pexels / Canva)
- `dark science background`, `chemistry lab dark aesthetic`, `atom model 3D render`
- `biology cell microscope`, `physics experiment classroom`, `earth tone science`
- `laboratory equipment dark`, `molecular structure visualization`
- `student science experiment`, `STEM education dark background`

### Từ khoá video (YouTube / Canva Video)
- `atom structure animation`, `chemical reaction slow motion`
- `biology cell division timelapse`, `physics experiment demonstration`
- `science education animated explainer`, `molecular 3D animation`

### Từ khoá background (Canva)
- `dark brown texture background`, `earth tone gradient dark`
- `chalkboard dark background education`, `dark academia aesthetic`
- `brown leather texture`, `dark wood grain background`

## Do

- Dùng canvas 20" × 11.25" — scale mọi toạ độ theo canvas này.
- Ưu tiên font 9Slide cho body/label + Noto Sans Bold / Noto Serif Bold cho heading.
- Giữ đúng gam vàng đất: `#3F2313`, `#D7A550`, `#D28119`, `#FCFBF9` + các màu phụ.
- Mỗi slide chỉ MỘT đơn vị kiến thức — tách slide nếu nội dung tràn.
- Chừa khoảng trắng rộng rãi: margin ≥ 0.8", gap = 0.5" (tỉ lệ với canvas 20").
- Dùng panel `#D7A550` cho nội dung chính, text `#3F2313` trên panel sáng.
- Title bar `#3F2313` với text `#F2F3EC` cho section header.
- Mỗi slide nên có ít nhất 1 icon hoặc hình minh hoạ.
- Dùng palette dots motif (5 chấm tròn cạnh trái) trên content slide.
- Emoji (🎯🔬🏭⚙️) OK cho slide mục tiêu — đây là phong cách đang dùng thực tế.
- Phân cấp typography 4 tầng: Headline (cứng) → Title (bold) → Sub-heading (trang nghiêm) → Body (mềm). Tỉ lệ size ≥ 1.3×.
- Heading LUÔN Bold, body LUÔN Regular. Nhấn trong body = bold + accent cho 1 cụm.

## Don't

- KHÔNG dùng canvas 13.333" × 7.5" — sai kích thước sẽ lệch toàn bộ layout.
- KHÔNG thay font 9Slide / Noto Sans / Noto Serif bằng Calibri/Cambria/Arial.
- KHÔNG nhồi chữ: nếu > 6 dòng trên slide → tách.
- KHÔNG mix quá 7 màu trong gam — giữ đúng palette đã định.
- KHÔNG dùng font nhỏ hơn 24pt trên canvas 20" — sẽ không đọc được khi chiếu.
- KHÔNG dùng shadow, bevel, gradient kiểu Office 2007.
- KHÔNG bỏ title bar `#3F2313` trên content slide — đây là motif nhận diện.
- KHÔNG dùng cùng 1 font + size cho heading và body → mất phân cấp.
- KHÔNG Bold toàn bộ body text → mọi thứ đều quan trọng = không gì quan trọng.
- KHÔNG mix > 3 font families trên 1 slide → hỗn loạn thị giác.
- KHÔNG dùng italic thay bold để nhấn trên slide chiếu — italic khó đọc ở khoảng cách xa.
- KHÔNG dùng serif cho body dài trên slide — serif đọc tốt trên giấy, không tốt trên màn chiếu.
