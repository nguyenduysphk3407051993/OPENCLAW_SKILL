# Bảng phân loại Extension đầy đủ

Tài liệu tham khảo cho `gdrive-openclaw-uploader`. Đọc file này khi gặp file có extension không có trong bảng chính của SKILL.md, hoặc khi cần xử lý edge case.

## Bảng đầy đủ theo từng subfolder

### 01_Documents (Văn bản, tài liệu đọc)

| Extension | Mô tả |
|-----------|-------|
| `.pdf` | Portable Document Format |
| `.docx`, `.doc` | Microsoft Word |
| `.odt` | OpenDocument Text |
| `.rtf` | Rich Text Format |
| `.txt` | Plain text |
| `.md`, `.markdown` | Markdown |
| `.tex`, `.ltx` | LaTeX source (quan trọng với context giáo dục VN) |
| `.epub` | eBook format |
| `.mobi`, `.azw`, `.azw3` | Kindle eBook |
| `.pages` | Apple Pages |
| `.djvu` | Tài liệu scan |

### 02_Images (Hình ảnh)

| Extension | Mô tả |
|-----------|-------|
| `.jpg`, `.jpeg`, `.jpe`, `.jfif` | JPEG |
| `.png` | Portable Network Graphics |
| `.gif` | Graphics Interchange Format |
| `.webp` | WebP (Google) |
| `.svg`, `.svgz` | Scalable Vector Graphics |
| `.bmp` | Bitmap |
| `.tiff`, `.tif` | TIFF (thường dùng cho scan chất lượng cao) |
| `.heic`, `.heif` | iPhone photo format |
| `.ico` | Icon |
| `.psd` | Photoshop (lưu ý: file lớn) |
| `.ai` | Adobe Illustrator |
| `.eps` | Encapsulated PostScript |
| `.raw`, `.cr2`, `.nef`, `.arw` | RAW từ máy ảnh |

### 03_Videos (Video)

| Extension | Mô tả |
|-----------|-------|
| `.mp4`, `.m4v` | MPEG-4 |
| `.avi` | Audio Video Interleave |
| `.mov`, `.qt` | QuickTime |
| `.mkv` | Matroska |
| `.wmv` | Windows Media Video |
| `.flv` | Flash Video |
| `.webm` | WebM |
| `.mpg`, `.mpeg`, `.mpe` | MPEG |
| `.3gp`, `.3g2` | Mobile video |
| `.ogv` | Ogg Video |
| `.ts`, `.mts`, `.m2ts` | Transport Stream |
| `.vob` | DVD Video |

### 04_Audio (Âm thanh)

| Extension | Mô tả |
|-----------|-------|
| `.mp3` | MPEG Audio Layer 3 |
| `.wav`, `.wave` | Waveform Audio |
| `.flac` | Free Lossless Audio Codec |
| `.aac` | Advanced Audio Coding |
| `.ogg`, `.oga` | Ogg Vorbis |
| `.m4a` | MPEG-4 Audio |
| `.wma` | Windows Media Audio |
| `.opus` | Opus |
| `.aiff`, `.aif` | Audio Interchange |
| `.alac` | Apple Lossless |
| `.amr` | Adaptive Multi-Rate (ghi âm điện thoại cũ) |
| `.mid`, `.midi` | MIDI |

### 05_Presentations (Bài thuyết trình)

| Extension | Mô tả |
|-----------|-------|
| `.pptx`, `.ppt` | Microsoft PowerPoint |
| `.pptm` | PowerPoint có macro |
| `.key` | Apple Keynote |
| `.odp` | OpenDocument Presentation |
| `.pps`, `.ppsx` | PowerPoint Slideshow |

### 06_Spreadsheets (Bảng tính)

| Extension | Mô tả |
|-----------|-------|
| `.xlsx`, `.xls` | Microsoft Excel |
| `.xlsm` | Excel có macro |
| `.csv` | Comma-Separated Values |
| `.tsv` | Tab-Separated Values |
| `.ods` | OpenDocument Spreadsheet |
| `.numbers` | Apple Numbers |

### 07_Archives (File nén)

| Extension | Mô tả |
|-----------|-------|
| `.zip` | ZIP archive |
| `.rar` | RAR archive |
| `.7z` | 7-Zip |
| `.tar` | TAR archive |
| `.gz`, `.gzip` | Gzip |
| `.bz2`, `.bzip2` | Bzip2 |
| `.xz` | XZ |
| `.tar.gz`, `.tgz` | Tarball gzip (xử lý đặc biệt — xem Edge Cases) |
| `.tar.bz2`, `.tbz2` | Tarball bzip2 |
| `.tar.xz`, `.txz` | Tarball xz |
| `.iso` | Disk image |
| `.dmg` | macOS disk image |

### 08_Others (Còn lại)

Mọi extension không có trong các bảng trên. Bao gồm:

- **Code/Data**: `.json`, `.xml`, `.yaml`, `.yml`, `.sql`, `.html`, `.css`, `.js`, `.py`, `.cpp`, `.java`...
- **Executable**: `.exe`, `.msi`, `.deb`, `.rpm`, `.apk`, `.app`
- **Font**: `.ttf`, `.otf`, `.woff`, `.woff2`
- **3D/CAD**: `.obj`, `.fbx`, `.stl`, `.dwg`
- **Database**: `.db`, `.sqlite`, `.mdb`
- **Email**: `.eml`, `.msg`
- **File không có extension**: README, Makefile, LICENSE...

## Edge Cases (xử lý đặc biệt)

### 1. File có 2 phần mở rộng (`.tar.gz`, `.tar.bz2`...)

```python
# ĐÚNG: kiểm tra compound extension trước
if filename.lower().endswith(('.tar.gz', '.tar.bz2', '.tar.xz')):
    return '07_Archives'

# Sau đó mới fallback về extension đơn
ext = filename.rsplit('.', 1)[-1].lower()
```

Sai lầm thường gặp: `lesson.tar.gz` → tách thành `tar.gz` thay vì gặp `.gz` trước → vẫn vào Archives nhưng đặt tên file lưu trữ có thể bị nhầm.

### 2. File không có extension

Ví dụ: `Makefile`, `Dockerfile`, `LICENSE`, `README` (không có `.md`).

→ Mặc định: vào `08_Others`. Không cố đoán mime-type vì có thể sai và ảnh hưởng tổ chức folder.

### 3. File ẩn (bắt đầu bằng `.`)

Ví dụ: `.bashrc`, `.gitignore`, `.env`, `.htaccess`.

→ Cảnh báo người dùng: "File ẩn `.bashrc` thường là file cấu hình hệ thống — bạn có chắc muốn upload lên Drive không?". Nếu user xác nhận, cho vào `08_Others`.

### 4. Extension viết HOA (`.PDF`, `.PPTX`)

Luôn `.lower()` extension trước khi so sánh với bảng. File gốc giữ nguyên tên (không rename viết thường).

### 5. File có MIME type không khớp extension

Ví dụ: file đặt tên `.txt` nhưng nội dung thực là binary, hoặc `.pdf` thực ra là file ảnh được rename.

→ Skill này phân loại theo **extension**, không sniff content. Đây là quyết định có chủ ý: nhanh, dự đoán được, không cần đọc file. Nếu người dùng cần phân loại theo nội dung thật, đó là use-case khác — không phải skill này.

### 6. File dạng symlink hoặc shortcut

→ Cảnh báo và bỏ qua. Không upload symlink (không có ý nghĩa trên cloud) và không tự follow để upload target (rủi ro upload nhầm file lớn ngoài ý muốn).

### 7. File đang được mở/khoá

→ Trên Windows (môi trường local của user): file Word/Excel đang mở thường bị lock. Thử đọc, nếu lỗi `PermissionError` thì báo và bỏ qua, tiếp tục các file còn lại.

### 8. File quá lớn

| Ngưỡng | Hành vi |
|--------|---------|
| < 100 MB | Upload bình thường |
| 100 MB – 1 GB | Upload nhưng dùng resumable upload (tránh mất kết nối) |
| 1 GB – 5 GB | Cảnh báo người dùng trước, hỏi confirm |
| > 5 GB | TỪ CHỐI — vượt giới hạn nhiều account, gợi ý chia nhỏ hoặc nén trước |

### 9. Tên file có ký tự đặc biệt

Google Drive cho phép hầu hết ký tự, nhưng tránh:
- Ký tự `/` trong tên (Drive sẽ hiểu là path)
- Tên file > 255 ký tự

→ Nếu phát hiện, sanitize: thay `/` bằng `-`, cắt ngắn nếu quá dài (giữ extension).

### 10. File tiếng Việt có dấu

Drive xử lý Unicode tốt — KHÔNG strip dấu khỏi tên file. Tên `bài_giảng_chương_3.pdf` giữ nguyên dấu khi upload.

## Code template — Logic phân loại

```python
COMPOUND_EXTS = ('.tar.gz', '.tar.bz2', '.tar.xz', '.tar.zst')

EXT_MAP = {
    '01_Documents': {'.pdf', '.docx', '.doc', '.txt', '.md', '.markdown',
                     '.rtf', '.odt', '.tex', '.ltx', '.epub', '.mobi',
                     '.azw', '.azw3', '.pages', '.djvu'},
    '02_Images':    {'.jpg', '.jpeg', '.jpe', '.jfif', '.png', '.gif',
                     '.webp', '.svg', '.svgz', '.bmp', '.tiff', '.tif',
                     '.heic', '.heif', '.ico', '.psd', '.ai', '.eps',
                     '.raw', '.cr2', '.nef', '.arw'},
    '03_Videos':    {'.mp4', '.m4v', '.avi', '.mov', '.qt', '.mkv',
                     '.wmv', '.flv', '.webm', '.mpg', '.mpeg', '.mpe',
                     '.3gp', '.3g2', '.ogv', '.ts', '.mts', '.m2ts', '.vob'},
    '04_Audio':     {'.mp3', '.wav', '.wave', '.flac', '.aac', '.ogg',
                     '.oga', '.m4a', '.wma', '.opus', '.aiff', '.aif',
                     '.alac', '.amr', '.mid', '.midi'},
    '05_Presentations': {'.pptx', '.ppt', '.pptm', '.key', '.odp',
                         '.pps', '.ppsx'},
    '06_Spreadsheets':  {'.xlsx', '.xls', '.xlsm', '.csv', '.tsv',
                         '.ods', '.numbers'},
    '07_Archives':  {'.zip', '.rar', '.7z', '.tar', '.gz', '.gzip',
                     '.bz2', '.bzip2', '.xz', '.tgz', '.tbz2', '.txz',
                     '.iso', '.dmg'},
}

def classify(filename: str) -> str:
    """Trả về tên subfolder phù hợp."""
    name_lower = filename.lower()

    # Bước 1: kiểm tra compound extensions trước
    for compound in COMPOUND_EXTS:
        if name_lower.endswith(compound):
            return '07_Archives'

    # Bước 2: extension đơn
    if '.' not in filename:
        return '08_Others'

    ext = '.' + name_lower.rsplit('.', 1)[-1]
    for folder, exts in EXT_MAP.items():
        if ext in exts:
            return folder

    return '08_Others'
```
