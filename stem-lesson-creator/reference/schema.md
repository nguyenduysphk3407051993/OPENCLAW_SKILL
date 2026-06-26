# Đặc tả content.json

File JSON mô tả toàn bộ nội dung giáo án. `build_docx.py` đọc file này và render.
Tất cả khoá đều khuyến nghị có; phần nào không dùng thì bỏ qua hoặc để mảng rỗng.

```jsonc
{
  "meta": {
    "title": "KẾ HOẠCH BÀI DẠY STEM",          // dòng tiêu đề cố định, có thể đổi
    "project_name": "TÊN DỰ ÁN IN HOA",
    "duration": "5 tiết (45 phút/tiết)",
    "lead_subject": "Hóa học",
    "integrated_subjects": "Vật lý, Toán học, Công nghệ",
    "scale": "Lớp học bình thường, dùng dụng cụ gia dụng thay thế."
  },

  "objectives": {
    // Mỗi nhóm kiến thức theo môn
    "knowledge": [
      { "subject": "a. Hóa học", "items": ["ý 1", "ý 2"] },
      { "subject": "b. Vật lý & Năng lượng", "items": ["..."] }
    ],
    "competencies": ["Năng lực Tìm hiểu tự nhiên: ...", "..."],
    "qualities": ["Chăm chỉ, Trung thực: ...", "Trách nhiệm: ..."]
  },

  "materials": {
    "organization": ["Chia nhóm 4-6 HS.", "Phân công vai trò:",
                     "+ Kỹ sư trưởng: ...", "+ Kỹ sư Hóa chất: ..."],
    "teacher": ["01 túi vôi tôi (5.000đ, mua ở tiệm VLXD)", "..."],
    "groups": ["1.5 lít nước mía thô", "200g bã mía tươi", "..."]
  },

  "periods": [
    {
      "title": "TIẾT 1: THIẾT LẬP BÀI TOÁN ...",
      "objectives": ["ý 1", "ý 2"],
      "activities": [
        {
          "name": "Hoạt động 1: Tình huống đảo ngược tư duy (10 phút)",
          "blocks": [
            { "role": "GV", "text": "Lời thoại GV nguyên văn..." },
            { "role": "HS", "text": "HS thực hiện: ..." },
            { "type": "note", "text": "Ghi chú/an toàn/kết quả trực quan..." }
          ]
        }
      ]
    }
  ],

  "formulas": [
    { "name": "Hiệu suất thu hồi đường (H%)",
      "formula": "H% = (m_thu được / m_lý thuyết) × 100%",
      "explain": "m_thu được: khối lượng đường rắn cân được (g); m_lý thuyết: ..." }
  ],

  "worksheets": [
    {
      "title": "PHIẾU HỌC TẬP SỐ 1",
      "subtitle": "BÁO CÁO THAO TÁC CHUẨN ĐỘ pH",
      "elements": [
        { "type": "field", "label": "Tên nhóm" },
        { "type": "field", "label": "Kỹ sư trưởng" },
        { "type": "paragraph", "text": "Đoạn dẫn hoặc câu hỏi..." },
        { "type": "blanks", "lines": 3 },              // 3 dòng kẻ chấm trống
        { "type": "table",
          "headers": ["Biến số", "Khối lượng (g)", "Hiệu suất (%)"],
          "rows": [ ["Cốc 1", "", ""], ["Cốc 2", "", ""] ] }  // "" = ô trống
      ]
    }
  ],

  "rubric": {
    "headers": ["Tiêu chí đánh giá", "Mức Tốt (8-10đ)", "Mức Khá (5-7đ)",
                "Mức Chưa Đạt (0-4đ)"],
    "rows": [
      ["Chất lượng sản phẩm (30%)", "mô tả tốt", "mô tả khá", "mô tả chưa đạt"],
      ["Xử lý số liệu & Notebook (30%)", "...", "...", "..."],
      ["Thuyết trình & Phản biện (40%)", "...", "...", "..."]
    ]
  }
}
```

## Các loại `block` trong activity
- `{"role":"GV","text":"..."}`  → in đậm nhãn "GV:" + lời thoại.
- `{"role":"HS","text":"..."}`  → nhãn "HS:" + thao tác.
- `{"type":"note","text":"..."}` → đoạn ghi chú thường (có thể gắn nhãn).
- `{"type":"plain","text":"..."}` → đoạn văn thường không nhãn.

## Các loại `element` trong worksheet
- `field`  : {label} → "Label: ......................." (1 dòng chấm).
- `paragraph` : {text} → đoạn văn thường.
- `blanks` : {lines} → n dòng kẻ chấm trống cho HS viết.
- `table`  : {headers, rows} → bảng; ô "" để trống cho HS điền.

## Quy ước
- Số tiết = số phần tử trong `periods` (linh hoạt 1..n).
- Có thể có nhiều worksheet; có thể bỏ `formulas` hoặc `rubric` nếu không cần.
