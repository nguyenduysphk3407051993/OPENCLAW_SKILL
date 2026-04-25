# Upload Google Drive Workflow

File này hướng dẫn cách `scripts/upload_drive.py` upload ảnh lên Drive theo quy ước OpenClaw.

## Naming Convention (BẮT BUỘC)

```
OPENCLAW/IMAGES/<TYPE>_<n>_<HH-mm-ss_dd-MM-yyyy>.<ext>
```

**Ví dụ thực tế**:
```
OPENCLAW/IMAGES/INFOGRAPHIC_quang_hop_lop6_14-32-05_25-04-2026.png
OPENCLAW/IMAGES/MINDMAP_chuong_3_hinh_hoc_09-15-22_25-04-2026.png
OPENCLAW/IMAGES/POSTER_an_toan_giao_thong_20-05-30_24-04-2026.png
```

**Quy tắc**:
- `<TYPE>` UPPERCASE, là 1 trong 12 mã: `INFOGRAPHIC`, `MINDMAP`, `ILLUSTRATION`, `DIAGRAM`, `PHOTO`, `COMIC`, `POSTER`, `BANNER`, `ICON`, `SCIENTIFIC`, `WORKSHEET`, `SLIDE_HERO`.
- `<n>` lowercase, không dấu, dùng `_` thay khoảng trắng. Tối đa 50 ký tự.
- `<HH-mm-ss_dd-MM-yyyy>` giờ địa phương (Asia/Ho_Chi_Minh, UTC+7), 24h, padding 0.
- `<ext>` = `png` | `jpg` | `webp` (theo `output_format` của API call).

**Tại sao dùng quy ước này**:
- Sort theo TYPE → giáo viên dễ tìm theo loại ảnh.
- Timestamp giúp phiên bản gần nhất luôn ở cuối (sort theo ngày).
- Format `dd-MM-yyyy` thay vì `yyyy-MM-dd` theo thói quen Việt Nam.
- Underscore thay vì khoảng trắng → an toàn với mọi tool xử lý file.

## Cấu trúc folder trên Drive

Script tự đảm bảo cấu trúc sau tồn tại:

```
[Drive root]
└─ OPENCLAW/
    └─ IMAGES/
       ├─ INFOGRAPHIC_*.png
       ├─ MINDMAP_*.png
       └─ ...
```

Nếu chưa có, script tự tạo (idempotent — chạy nhiều lần không sao).

**Lưu ý**: Drive root đây là root của **service account**, không phải My Drive của user. Để user truy cập được:
- Hoặc service account share folder `OPENCLAW/` về My Drive của user (xem mục Permissions).
- Hoặc dùng Shared Drive (Team Drive) — đặt `OPENCLAW/` làm con của Shared Drive, service account là member.

## Service Account Setup (one-time, đã có thể đã làm)

User đã chọn "Google Drive API + service account JSON". Skill giả định **đã** có sẵn:

1. Service account JSON file ở một trong các vị trí (theo thứ tự ưu tiên):
   - `--credentials` argument
   - Env `GOOGLE_APPLICATION_CREDENTIALS` (path tới JSON)
   - File `~/.config/openclaw/gdrive-service-account.json`
   - File `/etc/openclaw/gdrive-service-account.json`

2. Service account có quyền `https://www.googleapis.com/auth/drive.file` (tối thiểu) hoặc `https://www.googleapis.com/auth/drive` (đầy đủ).

3. Folder gốc `OPENCLAW/` đã được share cho service account email với quyền Editor — **HOẶC** dùng Shared Drive.

**Cách lấy service account JSON** (nếu user chưa có):
1. Vào Google Cloud Console → IAM & Admin → Service Accounts → Create.
2. Tạo key JSON, download.
3. Bật Drive API trong Cloud Console.
4. Vào My Drive, tạo folder `OPENCLAW/`, share với email service account (có dạng `xyz@xyz.iam.gserviceaccount.com`) với role Editor.
5. Đặt file JSON vào đường dẫn skill đọc được.

## Permissions (chia sẻ link)

Sau khi upload, script set quyền cho file:

- **Default**: `anyoneWithLink` + `reader` → user nhận link là xem được, không cần đăng nhập.
- **Tuỳ chọn `--private`**: chỉ service account và những người được share riêng mới xem được.

Trả về `webViewLink` dạng `https://drive.google.com/file/d/<FILE_ID>/view?usp=sharing`.

## Trigger upload (≥4MB)

Theo lựa chọn của user, **chỉ upload nếu file > 4MB**:

```python
file_size_mb = os.path.getsize(local_path) / (1024 * 1024)
if file_size_mb > 4:
    upload_to_drive(...)
else:
    # giữ local, gửi trong chat
    pass
```

Lý do ngưỡng 4MB:
- Limit upload file của Claude/OpenClaw chat thường ~5MB.
- gpt-image-2 quality `high` 1024×1536 thường ~3-5MB → border case.
- Quality `high` size 2K hoặc nhiều chi tiết có thể tới 8-15MB → cần upload.

## Xử lý lỗi

| Lỗi | Nguyên nhân | Cách xử lý |
|---|---|---|
| `403 Forbidden` khi upload | Service account chưa được share folder | Báo user, in email service account để user share |
| `404 Not Found` folder OPENCLAW/IMAGES | Folder chưa tồn tại | Script tự tạo, retry |
| `Quota exceeded` | Drive đầy hoặc API quota | Báo user, lưu local, đợi reset |
| `invalid_grant` | JSON expired/không hợp lệ | Báo user kiểm tra lại file credentials |
| Network timeout | Mạng chậm | Retry 3 lần với exponential backoff |

## Output cho user

Sau khi upload thành công, hiển thị:

```
✅ Đã upload: INFOGRAPHIC_quang_hop_lop6_14-32-05_25-04-2026.png (4.2 MB)
🔗 Link xem: https://drive.google.com/file/d/1abc.../view?usp=sharing
📁 Vị trí Drive: OPENCLAW/IMAGES/
```

Nếu file ≤ 4MB:

```
ℹ️ File 2.8MB (≤4MB), giữ local, không upload.
📍 /tmp/quang_hop_lop6.png
```

## Test connection (debug)

User có thể chạy nhanh để kiểm tra credentials:

```bash
python /mnt/skills/user/image-creator/scripts/upload_drive.py --test
```

Output mong đợi:
```
✓ Service account: openclaw-images@xyz.iam.gserviceaccount.com
✓ Drive accessible
✓ OPENCLAW/IMAGES/ folder exists (id: 1ABC...)
✓ Service account quota: 14.2 GB / 15 GB used
```
