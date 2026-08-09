---
name: gdrive-openclaw-uploader
description: "Skill upload và tổ chức tài liệu đa phương tiện lên Google Drive trong thư mục gốc OPENCLAW với 8 thư mục con phân loại tự động (Documents, Images, Videos, Audio, Presentations, Spreadsheets, Archives, Others). Dùng skill này MỖI KHI người dùng yêu cầu: upload/tải file lên Drive, đẩy tài liệu lên cloud, sao lưu file giáo dục, tổ chức tài liệu KHTN/giáo án/đề thi/hình ảnh/video bài giảng lên Google Drive, sắp xếp file đa phương tiện vào thư mục, hoặc khi nhắc đến 'OPENCLAW folder' / 'thư mục OPENCLAW'. Skill tự xử lý: phát hiện folder gốc đã tồn tại chưa, tạo subfolder thiếu, phân loại file theo extension, upload, và báo cáo kết quả."
allowed-tools: Read, Write, Glob, Bash, mcp__gdrive__*
argument-hint: "[đường dẫn file/folder] [(tùy chọn) ghi chú/mô tả]"
---

# Skill: GDrive OPENCLAW Uploader & Organizer

## Description
Skill này tự động hóa việc upload và tổ chức tài liệu đa phương tiện lên Google Drive theo cấu trúc thư mục chuẩn của hệ sinh thái OpenClaw. Mọi file được phân loại theo extension và đặt vào đúng subfolder trong thư mục gốc `OPENCLAW`.

## Cấu trúc thư mục đích trên Google Drive

```
OPENCLAW/                          ← Thư mục gốc (My Drive > OPENCLAW)
├── 01_Documents/                  ← Văn bản, giáo án, đề thi
├── 02_Images/                     ← Hình ảnh minh họa, sơ đồ, infographic
├── 03_Videos/                     ← Video bài giảng, thí nghiệm
├── 04_Audios/                      ← Ghi âm, podcast, file âm thanh
├── 05_Presentations/              ← Slide thuyết trình, bài giảng
├── 06_Spreadsheets/               ← Bảng điểm, dữ liệu, ma trận đề
├── 07_Archives/                   ← File nén, backup
└── 08_Others/                     ← File không thuộc 7 loại trên
```

**Quy ước đặt tên:** Thư mục con có prefix số `01_` đến `08_` để Drive sắp xếp ổn định theo thứ tự, không phụ thuộc tên hiển thị.

## Bảng phân loại theo extension

| Subfolder | Extensions |
|-----------|------------|
| `01_Documents` | `.pdf`, `.docx`, `.doc`, `.txt`, `.md`, `.rtf`, `.odt`, `.tex`, `.epub`, `.mobi` |
| `02_Images` | `.jpg`, `.jpeg`, `.png`, `.gif`, `.webp`, `.svg`, `.bmp`, `.tiff`, `.tif`, `.heic`, `.heif`, `.ico` |
| `03_Videos` | `.mp4`, `.avi`, `.mov`, `.mkv`, `.wmv`, `.flv`, `.webm`, `.m4v`, `.mpg`, `.mpeg` |
| `04_Audios` | `.mp3`, `.wav`, `.flac`, `.aac`, `.ogg`, `.m4a`, `.wma`, `.opus` |
| `05_Presentations` | `.pptx`, `.ppt`, `.key`, `.odp` |
| `06_Spreadsheets` | `.xlsx`, `.xls`, `.csv`, `.tsv`, `.ods`, `.numbers` |
| `07_Archives` | `.zip`, `.rar`, `.7z`, `.tar`, `.gz`, `.bz2`, `.xz`, `.tar.gz`, `.tgz` |
| `08_Others` | Mọi extension không thuộc các loại trên (bao gồm `.json`, `.xml`, `.exe`, file không đuôi...) |

Bảng phân loại đầy đủ + edge cases ở `references/extension_map.md`.

## Workflow chuẩn (8 bước)

Khi người dùng yêu cầu upload, thực hiện đúng thứ tự:

### Bước 1: Xác định input
Người dùng có thể đưa input dưới các dạng:
- **Một file đơn**: `/path/to/file.pdf`
- **Nhiều file rời**: liệt kê path
- **Một thư mục**: upload toàn bộ file bên trong (mặc định: KHÔNG đệ quy. Hỏi người dùng nếu cần đệ quy.)
- **Glob pattern**: `*.pdf`, `lesson_*.pptx`

Nếu input không rõ, hỏi lại người dùng — đừng đoán mò.

### Bước 2: Liệt kê file và phân loại trước khi upload
Trước khi gọi bất kỳ Drive API nào, in ra bảng tóm tắt cho người dùng confirm:

```
Đã quét được 12 file. Phân loại như sau:
- 01_Documents:     5 file (de_thi_lop_8.pdf, giao_an_chuong_3.docx, ...)
- 02_Images:        3 file (so_do_te_bao.png, ...)
- 05_Presentations: 4 file (bai_4_tach_chat.pptx, ...)

Tổng dung lượng: 47.3 MB
Bạn có muốn tiếp tục upload? (y/n)
```

Bước này quan trọng vì giúp phát hiện sớm file phân loại sai (vd: file `.pdf` nhưng thực ra là scan ảnh, hoặc file đặt sai extension).

### Bước 3: Kiểm tra thư mục gốc OPENCLAW
Dùng tool Google Drive search để tìm folder tên `OPENCLAW` ở root của My Drive.

- **Nếu đã tồn tại**: Lưu lại `folder_id`, đi tiếp bước 4.
- **Nếu chưa tồn tại**: Tạo folder mới ở root với tên đúng `OPENCLAW` (viết HOA toàn bộ).
- **Nếu tồn tại nhiều folder cùng tên**: Cảnh báo người dùng và yêu cầu chọn ID nào để dùng.

### Bước 4: Đảm bảo các subfolder tồn tại
Liệt kê các thư mục con trong `OPENCLAW`. Với mỗi loại file CẦN dùng (chỉ tạo thư mục thực sự cần — không tạo cả 8 nếu không upload Audio):

- Nếu thư mục con đã tồn tại → dùng `folder_id` của nó.
- Nếu chưa → tạo mới với tên đúng theo bảng (ví dụ `01_Documents`).

Cache lại `{loại: folder_id}` trong session để không phải query lặp lại.

### Bước 5: Upload từng file vào đúng subfolder
Với mỗi file:
1. Xác định subfolder đích từ extension (lowercase trước khi so sánh).
2. Upload file vào subfolder đó với tên gốc.
3. Nếu file trùng tên đã tồn tại trong subfolder, **mặc định**: thêm hậu tố `_(N)` với N là số nguyên tăng dần (vd: `bai_4.pdf` → `bai_4_(1).pdf`). Hỏi người dùng nếu họ muốn `overwrite` thay vì rename.

### Bước 6: Gắn metadata (nếu người dùng cung cấp ghi chú)
Nếu người dùng truyền tham số ghi chú/mô tả, set field `description` của file trên Drive bằng nội dung đó. Hữu ích cho việc tra cứu sau này (vd: "Đề thi giữa kỳ KHTN 8 - 2024-2025").

### Bước 7: Báo cáo kết quả
In ra tóm tắt cuối cùng dạng bảng:

```
✅ Upload hoàn tất: 12/12 file thành công

📁 OPENCLAW/01_Documents (5 file):
   • de_thi_lop_8.pdf          → https://drive.google.com/file/d/...
   • giao_an_chuong_3.docx     → https://drive.google.com/file/d/...
   ...

📁 OPENCLAW/02_Images (3 file):
   ...

⚠️ Cảnh báo: 1 file đã được rename do trùng tên: so_do.png → so_do_(1).png
```

### Bước 8: Xử lý lỗi
- **Quota exceeded / file quá lớn (>5GB)**: Báo lỗi rõ ràng, không retry vô hạn.
- **Mất kết nối**: Retry tối đa 3 lần, mỗi lần backoff 2-4-8 giây.
- **Một file lỗi không làm gãy cả batch**: Tiếp tục upload các file còn lại, gom lỗi vào báo cáo cuối.

## Quy tắc quan trọng

### Luôn lowercase extension khi so sánh
File `BAITAP.PDF` và `baitap.pdf` đều phải vào `01_Documents`. Logic:

```python
ext = filename.rsplit('.', 1)[-1].lower() if '.' in filename else ''
```

Lưu ý đặc biệt với file 2 phần mở rộng như `.tar.gz`: kiểm tra `endswith('.tar.gz')` TRƯỚC khi tách extension đơn.

### Tên thư mục tuyệt đối không thay đổi
Tên `OPENCLAW`, `01_Documents`, ..., `08_Others` là **bất biến**. Người dùng có thể yêu cầu đổi tên, nhưng cảnh báo họ rằng việc này sẽ phá vỡ tương thích với các skill/workflow khác trong hệ sinh thái OpenClaw đang trỏ đến cấu trúc này.

### KHÔNG tự ý tạo subfolder con cấp 3
Skill này chỉ quản lý 2 cấp: `OPENCLAW/<category>/<file>`. Nếu người dùng muốn phân loại theo môn học, lớp, năm học... đó là use-case khác — gợi ý họ tạo skill riêng kế thừa từ skill này.

### Phân biệt khi file là Google Workspace native
Nếu người dùng yêu cầu upload file `.docx`/`.xlsx`/`.pptx` và muốn tự động convert sang Google Docs/Sheets/Slides, hỏi rõ trước khi convert. **Mặc định: KHÔNG convert** — giữ nguyên format gốc để bảo toàn nội dung (đặc biệt quan trọng với LaTeX trong file Word, biểu thức toán trong file giáo án KHTN).

## Khi nào KHÔNG dùng skill này

- Khi người dùng chỉ muốn **đọc/tìm** file trên Drive (dùng search/fetch tool trực tiếp, không cần skill này).
- Khi cần upload lên một thư mục Drive cụ thể KHÁC OPENCLAW (skill này hard-code đích là OPENCLAW).
- Khi upload sang dịch vụ khác (Dropbox, OneDrive, S3, VPS storage).
- Khi cần xử lý/biến đổi nội dung file trước khi upload (kết hợp với skill chuyên biệt khác trước, rồi mới gọi skill này ở bước cuối).

## Ví dụ sử dụng

**Ví dụ 1: Upload một file đơn**
```
User: "Upload file /home/duynt/de_thi_KHTN8_giua_ki_1.pdf lên OPENCLAW giúp tôi"
→ Skill phát hiện .pdf → đích: OPENCLAW/01_Documents/
→ Upload → trả link Drive
```

**Ví dụ 2: Upload cả thư mục giáo án**
```
User: "Đẩy toàn bộ folder /mnt/lessons/grade6 lên OPENCLAW"
→ Quét folder, tìm thấy 8 .pptx + 3 .docx + 5 .png
→ Phân loại: 05_Presentations (8), 01_Documents (3), 02_Images (5)
→ Hiện bảng confirm → Upload → Báo cáo
```

**Ví dụ 3: Upload có ghi chú**
```
User: "Backup file /tmp/bai_giang_tach_chat.pptx, ghi chú: Bài 4 KHTN 6 - phiên bản 2024"
→ Upload vào OPENCLAW/05_Presentations/
→ Set description = "Bài 4 KHTN 6 - phiên bản 2024"
```

## Reference files

- `references/extension_map.md` — Bảng mapping extension đầy đủ + edge cases (file không có extension, file ẩn `.bashrc`, file 2 phần mở rộng...).
- `scripts/upload_to_openclaw.py` — Script Python dự phòng dùng `google-api-python-client` khi MCP Google Drive không có sẵn upload tool. Dùng OAuth credentials từ biến môi trường `GDRIVE_CREDENTIALS_PATH`.


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
