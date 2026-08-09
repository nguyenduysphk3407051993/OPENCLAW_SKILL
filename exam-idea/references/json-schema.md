# Cấu trúc 3 file JSON

Mỗi bộ đề nằm trong một thư mục con của `output/` và gồm đúng 3 file JSON.
Script `build_all.py` đọc 3 file này và sinh ra 3 file `.docx`.

Bản đặc tả máy đọc được nằm ở `schemas/*.schema.json`.

---

## Khối `cau_hinh` — dùng chung cho ma trận và đặc tả

**Phải giống hệt nhau ở cả hai file**, nếu không `validate.py` sẽ báo lỗi.

```json
"cau_hinh": {
  "tong_diem": 10,
  "muc_do": [
    { "ma": "NB", "ten": "Nhận biết",       "ten_ngan": "Biết" },
    { "ma": "TH", "ten": "Thông hiểu",      "ten_ngan": "Hiểu" },
    { "ma": "VD", "ten": "Vận dụng",        "ten_ngan": "Vận dụng" },
    { "ma": "LH", "ten": "Liên hệ thực tế", "ten_ngan": "Liên hệ" }
  ],
  "ty_le_muc_tieu": { "NB": 50, "TH": 30, "VD": 10, "LH": 10 },
  "nhom_cau_hoi": [
    { "ma": "TN",  "ten": "Nhiều lựa chọn", "nhom_cha": "TNKQ",    "loai": 1, "diem_moi_lenh": 0.25 },
    { "ma": "DS",  "ten": "\"Đúng – Sai\"",  "nhom_cha": "TNKQ",    "loai": 2, "diem_moi_lenh": 0.25, "so_y_moi_cau": 4 },
    { "ma": "TLN", "ten": "Trả lời ngắn",   "nhom_cha": "TNKQ",    "loai": 3, "diem_moi_lenh": 0.5 },
    { "ma": "TL",  "ten": "Tự luận",        "nhom_cha": "Tự luận", "loai": 4, "diem_moi_lenh": null }
  ]
}
```

| Khoá | Ý nghĩa |
|------|---------|
| `muc_do[].ten_ngan` | Chữ hiển thị trên dòng tiêu đề thứ 4 của bảng |
| `ty_le_muc_tieu` | `validate.py` đối chiếu tỉ lệ điểm thực tế với giá trị này |
| `nhom_cha` | Gộp cột ở dòng tiêu đề thứ 2. Nhóm có đúng 1 con và `ten` trùng `nhom_cha` (ví dụ *Tự luận*) sẽ được gộp dọc 2 dòng như form mẫu |
| `diem_moi_lenh` | `null` ⇒ phải khai điểm tường minh qua khoá `diem` ở từng ô |

Đổi `muc_do` từ 4 xuống 3 phần tử là bảng tự co lại đúng form mẫu gốc.

---

## 1. `bang_ma_tran.json`

```json
{
  "tieu_de": "1. MA TRẬN ĐỀ KIỂM TRA ĐỊNH KÌ",
  "thong_tin": { "mon": "...", "lop": 6, "thoi_gian": "45 phút", "hinh_thuc": "..." },
  "cau_hinh": { ... },
  "chu_de": [
    {
      "tt": 1,
      "ten": "Mở đầu về Khoa học tự nhiên",
      "noi_dung": [
        {
          "ten": "1.1. Giới thiệu về Khoa học tự nhiên...",
          "so_lenh_hoi": { "TN": { "NB": 2, "TH": 1 }, "DS": { "NB": 2, "TH": 2 } },
          "diem":        { "TL": { "TH": 0.5 } }
        }
      ]
    }
  ],
  "ghi_chu": [ "(*) ..." ]
}
```

- `so_lenh_hoi[<mã nhóm>][<mã mức độ>]` = **số lệnh hỏi**, không phải số câu.
  Câu loại 2 đếm **4 lệnh hỏi** (4 ý a–d), câu loại 4 đếm **2 lệnh hỏi**
  (2 ý a, b); các ý trong cùng một câu có thể ở mức độ khác nhau.
- `diem` là tuỳ chọn, chỉ cần cho nhóm có `diem_moi_lenh: null` (Tự luận).
  Nếu có, giá trị này **ghi đè** phép nhân `số lệnh hỏi × diem_moi_lenh`.
- Bỏ trống ô nào thì không khai khoá đó (không cần ghi `0`).
- `ghi_chu` in thành các dòng chữ nghiêng dưới bảng.

### Cột tự sinh
Script tự tính và điền: cột `Tổng` (theo mức độ), cột `Tỷ lệ % điểm` (theo
dòng), và 3 dòng chân bảng `Tổng số câu/lệnh hỏi` – `Tổng số điểm` – `Tỷ lệ %`.
Không khai các giá trị này trong JSON.

---

## 2. `bang_dac_ta_ma_tran.json`

```json
{
  "tieu_de": "2. BẢNG ĐẶC TẢ ĐỀ KIỂM TRA ĐỊNH KÌ",
  "thong_tin": { ... },
  "cau_hinh": { ... },
  "chu_de": [
    {
      "tt": 1,
      "ten": "Mở đầu về Khoa học tự nhiên",
      "noi_dung": [
        {
          "ten": "1.1. Giới thiệu về Khoa học tự nhiên...",
          "yeu_cau_can_dat": [
            {
              "muc_do": "NB",
              "noi_dung": "– Nêu được khái niệm khoa học tự nhiên...",
              "so_lenh_hoi": { "TN": 1 }
            },
            {
              "muc_do": "TH",
              "noi_dung": "– Giải thích được cơ sở khoa học của...",
              "so_lenh_hoi": { "TL": 1 },
              "diem": { "TL": 0.5 }
            }
          ]
        }
      ]
    }
  ]
}
```

Khác với ma trận: `so_lenh_hoi` ở đây **phẳng một tầng** (`{ "<mã nhóm>": n }`)
vì mức độ đã nằm ở khoá `muc_do` của chính yêu cầu cần đạt. Khoá `diem` cũng
phẳng: `{ "TL": 0.5 }`.

### Ràng buộc đồng bộ (validate kiểm tra)

1. Danh sách `(chu_de.ten, noi_dung.ten)` **giống hệt** bên ma trận, đúng thứ tự
2. Với mọi (đơn vị, nhóm, mức độ):
   `Σ yeu_cau_can_dat[].so_lenh_hoi` = ô tương ứng trong ma trận

### Cách sinh dòng
Script nhóm các YCCĐ theo mức độ và tự chèn dòng nhãn in đậm
(`Nhận biết:`, `Thông hiểu:`, …) trước mỗi nhóm — giống form mẫu.

---

## 3. `de_bai_tap.json`

```json
{
  "tieu_de": "CÁC DẠNG BÀI TẬP VÀ ĐỀ MINH HOẠ",
  "thong_tin": { "mon": "...", "lop": 6, "chu_de_chung": "..." },
  "cau_hinh": { "muc_do": [ { "ma": "NB", "ten": "Nhận biết" }, ... ] },

  "muc_tieu": [
    { "chu_de": "Chủ đề 1. ...",
      "yeu_cau": [ { "muc_do": "NB", "noi_dung": "..." } ] }
  ],

  "dang_bai_tap": [
    { "loai": 1,
      "mo_ta": "...",
      "dang": [ { "ma": "1.1", "ten": "...", "muc_do": "NB", "mo_ta": "...", "vi_du": "..." } ] }
  ],

  "de_minh_hoa": {
    "cau_truc": "...",
    "phan": [ { "ten": "PHẦN I. ...", "huong_dan": "...", "loai": 1, "cau": [ ... ] } ]
  }
}
```

### Khoá chung của mọi câu hỏi

| Khoá | Bắt buộc | Ghi chú |
|------|----------|---------|
| `stt` | ✔ | đánh số liên tục toàn đề |
| `loai` | ✔ | 1 / 2 / 3 / 4 (kế thừa từ `phan.loai` nếu bỏ trống) |
| `chu_de`, `don_vi` | ✔ | **chuỗi giống hệt** trong ma trận — validate đối chiếu |
| `muc_do`, `dang`, `diem` | nên có | in thành ghi chú nghiêng cạnh đề bài |
| `de` | ✔ | phần dẫn |

### Riêng từng loại

```jsonc
// loại 1
"lua_chon": ["...", "...", "...", "..."],   // đúng 4 phần tử, thứ tự A B C D
"dap_an": "B",
"loi_giai": "..."

// loại 2
"y": [ { "nd": "...", "dap_an": true, "muc_do": "NB", "giai_thich": "..." }, ... ]  // đúng 4 phần tử

// loại 3
"dap_an": "400",
"loi_giai": "..."

// loại 4 — BẮT BUỘC đúng 2 ý a), b); mỗi ý là 1 lệnh hỏi
"y": [ { "nd": "a) ...", "diem": 0.25, "muc_do": "TH" },
       { "nd": "b) ...", "diem": 0.25, "muc_do": "TH" } ],
"huong_dan_cham": [ { "nd": "a) ...", "diem": 0.25 }, ... ]
```

`validate.py` đếm lệnh hỏi thực tế trong đề theo quy tắc: **số ý nếu câu có
khoá `y`, ngược lại là 1** — nên loại 2 thành 4 và loại 4 thành 2 một cách tự
động. Sau đó đối chiếu với tổng của ma trận theo từng nhóm, đồng thời kiểm tra
`số câu × so_y_moi_cau = số lệnh hỏi` nếu nhóm có khai `so_y_moi_cau`.

---

## Lệnh chạy

```bash
# kiểm tra đồng bộ
python scripts/validate.py output/<TÊN_BỘ_ĐỀ>

# kiểm tra + xuất cả 3 docx
python scripts/build_all.py output/<TÊN_BỘ_ĐỀ>

# xuất riêng lẻ
python scripts/ma_tran_to_docx.py output/<X>/bang_ma_tran.json output/<X>/2_Bang_ma_tran.docx
```
