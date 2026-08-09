---
name: ke-hoach-day-hoc
description: >-
  Tạo kế hoạch bài dạy (KHBD) chuẩn theo Công văn 5512/BGDĐT-GDTrH cho môn
  Khoa học tự nhiên lớp 9 (Vật lí, Hóa học, Sinh học) theo bộ sách Kết nối tri
  thức với cuộc sống (KNTT). Đầu ra là file Word (.docx) đầy đủ các thành phần:
  Mục tiêu, Thiết bị dạy học, Tiến trình dạy học với 4 hoạt động (Khởi động,
  Hình thành kiến thức, Luyện tập, Vận dụng), mỗi hoạt động có bảng 2 cột
  Hoạt động của GV và HS.
---

# Kế Hoạch Bài Dạy (KHBD) - Khoa học tự nhiên 9 KNTT

## Khi yêu cầu chưa đủ cụ thể — PHẢN BIỆN TRƯỚC, LÀM SAU

Yêu cầu chung chung luôn cho ra sản phẩm kém. **Không đoán bừa, cũng không hỏi
lể tể từng ý.** Hãy nêu rõ đang thiếu gì, rồi đưa **một prompt mẫu đã điền sẵn
giá trị mặc định hợp lý** để người dùng sửa và gửi lại trong đúng một lượt.

Thiếu từ **2 tiêu chí trở lên** thì bắt buộc phản biện. Thiếu **đúng 1** tiêu chí
thì tự chọn mặc định, làm tiếp, và nói rõ đã chọn gì.

**Tiêu chí bắt buộc:** môn · lớp · bộ sách · số tiết/tuần · học kì hay cả năm · khung thời gian

**Mẫu phản biện:**

> Yêu cầu hiện thiếu: **bộ sách**, **số tiết**. Nếu làm luôn thì tôi phải đoán, dễ lệch
> ý bạn. Bạn copy prompt dưới đây, sửa chỗ in đậm rồi gửi lại:
>
> ```
> Lập kế hoạch dạy học môn **KHTN** lớp **8**,
> bộ sách **Kết nối tri thức với cuộc sống**.
> Phạm vi: **cả năm học 2026–2027** · **4** tiết/tuần, **35** tuần
> Cần có: **phân phối chương trình, thiết bị dạy học, kiểm tra định kì**
> ```

---

## Overview

Skill này tạo **Kế Hoạch Bài Dạy (KHBD)** chuẩn theo Phụ lục IV, Công văn số
5512/BGDĐT-GDTrH ngày 18/12/2020 của Bộ GDĐT, dành cho môn **Khoa học tự
nhiên lớp 9** theo bộ sách **Kết nối tri thức với cuộc sống (KNTT)**.

Đầu ra là file **Microsoft Word (.docx)** với định dạng bảng chuẩn, sẵn sàng
in ấn, bao gồm đầy đủ:
- **I. MỤC TIÊU**: Kiến thức, Năng lực (chung + KHTN), Phẩm chất
- **II. THIẾT BỊ DẠY HỌC VÀ HỌC LIỆU**: Dụng cụ, hóa chất, phiếu học tập
- **III. TIẾN TRÌNH DẠY HỌC**: 4 hoạt động với bảng GV–HS

## Dependencies

Không yêu cầu skill đặc biệt nào khác từ science bundle.
Yêu cầu thư viện Python: `python-docx>=1.1.0` (tự động cài khi dùng `uv run`).

## Portability — Không hardcode đường dẫn

> [!IMPORTANT]
> Skill này **KHÔNG có đường dẫn cố định** (không hardcode). Tất cả đường dẫn
> đều được truyền qua tham số dòng lệnh. Skill hoạt động trên **mọi máy tính**
> (Windows, macOS, Linux) mà không cần chỉnh sửa bất kỳ file nào.

### Cách agent xác định đường dẫn script (bước bắt buộc đầu tiên)

Trước khi gọi bất kỳ subcommand nào, agent **PHẢI** chạy lệnh `locate` để
lấy đường dẫn tuyệt đối của script trên máy hiện tại:

```bash
# Bước 0 luôn làm trước: tìm đường dẫn script
python "<SKILL_INSTALL_DIR>/scripts/khbd_generator.py" locate
```

Kết quả trả về:
```
[SCRIPT]     /absolute/path/to/scripts/khbd_generator.py
[SKILL_DIR]  /absolute/path/to/ke_hoach_day_hoc/
[REFERENCES] /absolute/path/to/ke_hoach_day_hoc/references/
[EXAMPLES]   /absolute/path/to/ke_hoach_day_hoc/examples/
```

Sau đó dùng `[SCRIPT]` path đó cho tất cả các lệnh tiếp theo thay cho `<SCRIPT>`.

**Để tìm `<SKILL_INSTALL_DIR>`**, agent tìm trong danh sách skill đã cài:

```bash
# Windows PowerShell
Get-ChildItem -Recurse -Filter "khbd_generator.py" $env:USERPROFILE\.gemini

# macOS / Linux
find ~/.gemini -name "khbd_generator.py" 2>/dev/null
```

## Quick Start

### Bước 1: Cung cấp thông tin bài học

Người dùng cần cung cấp (hoặc AI tự suy luận từ tên bài):
```
- Tên bài / chủ đề: "Bài 21. Sự khác nhau cơ bản giữa phi kim và kim loại"
- Môn học: Hóa học / Vật lí / Sinh học
- Số tiết: 2 tiết
- Lớp: 9
- Thư mục KHBD tham chiếu (tùy chọn): hỏi người dùng đường dẫn thực tế trên máy của họ
- Thư mục đầu ra: hỏi người dùng nếu chưa cung cấp, hoặc dùng thư mục hiện tại
```

> **Lưu ý về đường dẫn**: Skill này KHÔNG có đường dẫn cố định. Agent cần
> **hỏi người dùng** thư mục tham chiếu KHBD và thư mục đầu ra trước khi chạy
> lệnh. Đường dẫn script luôn là đường dẫn tuyệt đối đến file
> `scripts/khbd_generator.py` trong thư mục cài đặt skill.

### Bước 2: Xác định đường dẫn script

Agent cần tìm đường dẫn tuyệt đối của script trước khi chạy:

```python
# Agent tự xác định bằng cách tìm trong thư mục skill:
import os
skill_dir = os.path.dirname(os.path.abspath(__file__))
script_path = os.path.join(skill_dir, 'scripts', 'khbd_generator.py')
```

Hoặc agent dùng lệnh shell để tìm:
```bash
# Windows PowerShell
$scriptPath = Join-Path $PSScriptRoot "scripts\khbd_generator.py"

# macOS / Linux
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SCRIPT_PATH="$SCRIPT_DIR/scripts/khbd_generator.py"
```

### Bước 3: Chạy script sinh KHBD

Thay `<SCRIPT>` bằng đường dẫn thực đến `scripts/khbd_generator.py`,
`<OUTPUT_DIR>` bằng thư mục đầu ra người dùng cung cấp:

```bash
uv run <SCRIPT> generate \
  --ten-bai "Bài 21. Sự khác nhau cơ bản giữa phi kim và kim loại" \
  --mon-hoc "Hóa học" \
  --so-tiet 5 \
  --lop 9 \
  --output "<OUTPUT_DIR>/KHBD_Bai21.docx"
```

### Bước 4 (Tùy chọn): Phân tích file KHBD mẫu để lấy nội dung

Nếu người dùng có thư mục chứa file KHBD mẫu:
```bash
uv run <SCRIPT> analyze \
  --input "<THU_MUC_MAU>/Bài 21.docx" \
  --output "<OUTPUT_DIR>/analysis_Bai21.json"
```

### Bước 5: Tạo KHBD đầy đủ với nội dung từ file phân tích

```bash
uv run <SCRIPT> generate \
  --ten-bai "Bài 21. Sự khác nhau cơ bản giữa phi kim và kim loại" \
  --mon-hoc "Hóa học" \
  --so-tiet 5 \
  --lop 9 \
  --content-json "<OUTPUT_DIR>/analysis_Bai21.json" \
  --output "<OUTPUT_DIR>/KHBD_Bai21_full.docx"
```

## Utility Scripts

### `scripts/khbd_generator.py`

#### Subcommand: `generate`

Tạo file Word KHBD từ đầu hoặc từ nội dung JSON đã phân tích.

**Arguments:**

| Argument | Bắt buộc | Mô tả |
|----------|----------|-------|
| `--ten-bai` | ✅ | Tên bài học đầy đủ |
| `--mon-hoc` | ✅ | Môn học: "Hóa học", "Vật lí", hoặc "Sinh học" |
| `--so-tiet` | ✅ | Số tiết dạy (số nguyên) |
| `--lop` | ✅ | Lớp học (ví dụ: 9) |
| `--output` | ✅ | Đường dẫn file Word đầu ra (.docx) |
| `--content-json` | ❌ | Đường dẫn JSON từ lệnh `analyze` để điền nội dung |
| `--ten-gv` | ❌ | Tên giáo viên (mặc định: để trống) |
| `--truong` | ❌ | Tên trường (mặc định: để trống) |
| `--to-bo-mon` | ❌ | Tên tổ bộ môn (mặc định: để trống) |

**Ví dụ:**
```bash
uv run <SCRIPT> generate \
  --ten-bai "Bài 38. Nucleic acid và gene" \
  --mon-hoc "Sinh học" \
  --so-tiet 3 \
  --lop 9 \
  --output "<OUTPUT_DIR>/KHBD_Bai38.docx" \
  --ten-gv "Nguyễn Văn A" \
  --truong "THCS ..."
```

#### Subcommand: `analyze`

Đọc file KHBD Word mẫu (.docx) và trích xuất nội dung ra file JSON.

**Arguments:**

| Argument | Bắt buộc | Mô tả |
|----------|----------|-------|
| `--input` | ✅ | Đường dẫn file Word KHBD mẫu (.docx) |
| `--output` | ✅ | Đường dẫn file JSON đầu ra |

**Ví dụ:**
```bash
uv run <SCRIPT> analyze \
  --input "<THU_MUC_MAU>/Bài 21.docx" \
  --output "<OUTPUT_DIR>/analysis.json"
```

#### Subcommand: `list-samples`

Liệt kê tất cả file KHBD mẫu trong thư mục tham chiếu.

**Arguments:**

| Argument | Bắt buộc | Mô tả |
|----------|----------|-------|
| `--ref-dir` | ✅ | Đường dẫn thư mục chứa các file KHBD mẫu |
| `--output` | ✅ | Đường dẫn file JSON lưu danh sách |

**Ví dụ:**
```bash
uv run <SCRIPT> list-samples \
  --ref-dir "<THU_MUC_MAU>" \
  --output "<OUTPUT_DIR>/sample_list.json"
```

## Workflow

### Quy trình tạo KHBD hoàn chỉnh

**Kịch bản 1: Tạo từ đầu (AI tự sinh nội dung)**

```
1. Người dùng cung cấp: tên bài, môn học, số tiết
2. Agent chạy lệnh generate với nội dung AI tự sinh
3. Agent mở file docx đầu ra và thông báo cho người dùng
```

**Kịch bản 2: Tái sử dụng từ KHBD mẫu có sẵn (khuyến nghị)**

```
1. Người dùng cung cấp: tên bài, thư mục mẫu
2. Agent chạy list-samples để tìm file tương ứng
3. Agent chạy analyze để trích xuất nội dung
4. Agent chạy generate với --content-json để tạo file Word
5. Agent kiểm tra và thông báo hoàn thành
```

### Quy trình chi tiết khi AI sinh nội dung

Khi không có file mẫu, AI cần tự tạo nội dung theo hướng dẫn trong
`references/khbd_structure.md` và `references/sample_activities.md`.

Các bước AI thực hiện:
1. **Xác định mục tiêu** dựa trên môn học và tên bài
2. **Xác định thiết bị** phù hợp với nội dung bài
3. **Lập 4 hoạt động** theo chuỗi: Khởi động → HTKM → Luyện tập → Vận dụng
4. **Sinh bảng GV–HS** cho mỗi hoạt động với 4 bước: Giao nhiệm vụ →
   Hướng dẫn → Báo cáo → Tổng kết/Chốt kiến thức
5. **Tạo file Word** bằng lệnh generate

### Cấu trúc JSON nội dung (--content-json)

```json
{
  "truong": "...",
  "to_bo_mon": "...",
  "ten_gv": "...",
  "ten_bai": "...",
  "mon_hoc": "Hóa học",
  "lop": 9,
  "so_tiet": 5,
  "muc_tieu": {
    "kien_thuc": ["...", "..."],
    "nang_luc_chung": ["...", "..."],
    "nang_luc_khtn": ["...", "..."],
    "pham_chat": ["...", "..."]
  },
  "thiet_bi": {
    "dung_cu_hoa_chat": ["...", "..."],
    "phieu_hoc_tap": ["...", "..."]
  },
  "phuong_phap": ["...", "..."],
  "hoat_dong": [
    {
      "so_thu_tu": 1,
      "ten": "Khởi động",
      "muc_tieu": "...",
      "noi_dung": "...",
      "san_pham": "...",
      "to_chuc": [
        {"gv": "Nội dung hoạt động GV...", "hs": "Nội dung hoạt động HS..."},
        {"gv": "...", "hs": "..."}
      ]
    },
    {
      "so_thu_tu": 2,
      "ten": "Hình thành kiến thức mới",
      "muc_tieu": "...",
      "noi_dung": "...",
      "san_pham": "...",
      "to_chuc": [
        {"gv": "...", "hs": "..."}
      ]
    },
    {
      "so_thu_tu": 3,
      "ten": "Luyện tập",
      "muc_tieu": "...",
      "noi_dung": "...",
      "san_pham": "...",
      "to_chuc": [
        {"gv": "...", "hs": "..."}
      ]
    },
    {
      "so_thu_tu": 4,
      "ten": "Vận dụng",
      "muc_tieu": "...",
      "noi_dung": "...",
      "san_pham": "...",
      "to_chuc": [
        {"gv": "...", "hs": "..."}
      ]
    }
  ]
}
```

## Rate Limiting

Skill này không gọi API bên ngoài — không cần rate limiting.

## Common Mistakes

1. **Không cung cấp đủ 4 hoạt động**: KHBD chuẩn theo CV5512 PHẢI có đủ 4
   hoạt động: Khởi động, Hình thành kiến thức, Luyện tập, Vận dụng. Không
   được bỏ bớt hoạt động nào.

2. **Bảng GV–HS thiếu 4 bước**: Mỗi hoạt động trong bảng Tổ chức thực hiện
   cần có đủ 4 bước: (1) Giao nhiệm vụ, (2) Hướng dẫn thực hiện, (3) Báo cáo
   kết quả, (4) Tổng kết/Nhận định. Đây là yêu cầu chuẩn của CV5512.

3. **Quên phần Phiếu học tập**: Mục II phải có cả phần dụng cụ/hóa chất VÀ
   phiếu học tập nếu bài có thí nghiệm hoặc hoạt động nhóm.


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
