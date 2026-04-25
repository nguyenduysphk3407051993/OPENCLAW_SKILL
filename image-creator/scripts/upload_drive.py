#!/usr/bin/env python3
"""
upload_drive.py — Upload ảnh lên Google Drive theo quy ước OPENCLAW.

Quy ước file path trên Drive:
    OPENCLAW/IMAGES/<TYPE>_<n>_<HH-mm-ss_dd-MM-yyyy>.<ext>

Ví dụ:
    OPENCLAW/IMAGES/INFOGRAPHIC_quang_hop_lop6_14-32-05_25-04-2026.png

Đọc service account JSON theo thứ tự:
1. --credentials <path>
2. Env GOOGLE_APPLICATION_CREDENTIALS
3. ~/.config/openclaw/gdrive-service-account.json
4. /etc/openclaw/gdrive-service-account.json

Usage:
    # Test connection
    python upload_drive.py --test

    # Upload ảnh
    python upload_drive.py \\
        --file /tmp/quang_hop.png \\
        --type INFOGRAPHIC \\
        --name quang_hop_lop6
"""

import argparse
import json
import mimetypes
import os
import sys
import time
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

VALID_TYPES = (
    "INFOGRAPHIC", "MINDMAP", "ILLUSTRATION", "DIAGRAM",
    "PHOTO", "COMIC", "POSTER", "BANNER",
    "ICON", "SCIENTIFIC", "WORKSHEET", "SLIDE_HERO",
)

ROOT_FOLDER = "OPENCLAW"
IMAGES_FOLDER = "IMAGES"
SCOPES = ["https://www.googleapis.com/auth/drive"]
TIMEZONE = "Asia/Ho_Chi_Minh"

# Drive API mime type for folders
FOLDER_MIME = "application/vnd.google-apps.folder"


def find_credentials(arg_path: str | None) -> Path:
    """Tìm service account JSON theo thứ tự ưu tiên."""
    candidates = []
    if arg_path:
        candidates.append(Path(arg_path))

    env_path = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
    if env_path:
        candidates.append(Path(env_path))

    candidates.extend([
        Path.home() / ".config" / "openclaw" / "gdrive-service-account.json",
        Path("/etc/openclaw/gdrive-service-account.json"),
    ])

    for p in candidates:
        if p.exists() and p.is_file():
            return p

    print(
        "ERROR: Không tìm thấy service account JSON.\n"
        "Đặt 1 trong 4 cách:\n"
        "  1. --credentials /path/to/sa.json\n"
        "  2. export GOOGLE_APPLICATION_CREDENTIALS=/path/to/sa.json\n"
        "  3. ~/.config/openclaw/gdrive-service-account.json\n"
        "  4. /etc/openclaw/gdrive-service-account.json",
        file=sys.stderr,
    )
    sys.exit(2)


def build_service(cred_path: Path):
    """Tạo Drive service từ service account JSON."""
    try:
        from google.oauth2 import service_account
        from googleapiclient.discovery import build
    except ImportError:
        print(
            "ERROR: Thiếu thư viện. Chạy:\n"
            "  pip install --break-system-packages "
            "google-api-python-client google-auth google-auth-httplib2",
            file=sys.stderr,
        )
        sys.exit(2)

    creds = service_account.Credentials.from_service_account_file(
        str(cred_path), scopes=SCOPES
    )
    service = build("drive", "v3", credentials=creds, cache_discovery=False)
    return service, creds.service_account_email


def find_or_create_folder(service, name: str, parent_id: str | None = None) -> str:
    """Tìm folder theo tên trong parent, tạo nếu chưa có. Trả về folder ID."""
    query_parts = [
        f"mimeType='{FOLDER_MIME}'",
        f"name='{name}'",
        "trashed=false",
    ]
    if parent_id:
        query_parts.append(f"'{parent_id}' in parents")

    query = " and ".join(query_parts)

    try:
        results = service.files().list(
            q=query,
            fields="files(id, name)",
            supportsAllDrives=True,
            includeItemsFromAllDrives=True,
            pageSize=10,
        ).execute()
    except Exception as e:
        print(f"ERROR khi tìm folder '{name}': {e}", file=sys.stderr)
        raise

    files = results.get("files", [])
    if files:
        return files[0]["id"]

    # Tạo mới
    metadata = {"name": name, "mimeType": FOLDER_MIME}
    if parent_id:
        metadata["parents"] = [parent_id]

    folder = service.files().create(
        body=metadata, fields="id", supportsAllDrives=True
    ).execute()
    print(f"  → Đã tạo folder mới '{name}' (id={folder['id']})", file=sys.stderr)
    return folder["id"]


def ensure_folder_path(service):
    """Đảm bảo OPENCLAW/IMAGES tồn tại, trả về (root_id, images_id)."""
    root_id = find_or_create_folder(service, ROOT_FOLDER, parent_id=None)
    images_id = find_or_create_folder(service, IMAGES_FOLDER, parent_id=root_id)
    return root_id, images_id


def remove_vietnamese_diacritics(s: str) -> str:
    """Bỏ dấu tiếng Việt: 'Chương 3 Hình học' -> 'Chuong 3 Hinh hoc'."""
    import unicodedata
    # Bước 1: Tách diacritics chuẩn Unicode (á → a + ´)
    nfkd = unicodedata.normalize("NFKD", s)
    no_combining = "".join(c for c in nfkd if not unicodedata.combining(c))
    # Bước 2: Xử lý đ/Đ (không phải combining, phải map riêng)
    no_combining = no_combining.replace("đ", "d").replace("Đ", "D")
    return no_combining


def make_filename(type_code: str, name: str, ext: str,
                  ts: datetime | None = None,
                  keep_diacritics: bool = False) -> str:
    """
    Sinh tên file đúng quy ước:
        <TYPE>_<n>_<HH-mm-ss_dd-MM-yyyy>.<ext>

    Default bỏ dấu tiếng Việt để an toàn cross-platform.
    """
    if ts is None:
        ts = datetime.now(ZoneInfo(TIMEZONE))

    timestamp = ts.strftime("%H-%M-%S_%d-%m-%Y")

    cleaned = name.lower().strip()
    if not keep_diacritics:
        cleaned = remove_vietnamese_diacritics(cleaned)

    # Sanitize: giữ chữ cái ASCII (hoặc Unicode nếu keep_diacritics)/số/_
    safe_name = "".join(
        c if (c.isalnum() or c == "_") else "_" for c in cleaned
    )
    # Gom nhiều _ liên tiếp thành 1
    while "__" in safe_name:
        safe_name = safe_name.replace("__", "_")
    safe_name = safe_name.strip("_")[:50] or "image"

    return f"{type_code.upper()}_{safe_name}_{timestamp}.{ext.lower()}"


def upload_file(service, local_path: Path, remote_name: str,
                parent_id: str, make_public: bool = True) -> dict:
    """Upload file lên Drive, trả về dict thông tin."""
    from googleapiclient.http import MediaFileUpload

    mime_type, _ = mimetypes.guess_type(str(local_path))
    if not mime_type:
        ext = local_path.suffix.lower().lstrip(".")
        mime_type = {"png": "image/png", "jpg": "image/jpeg",
                     "jpeg": "image/jpeg", "webp": "image/webp"}.get(ext, "image/png")

    metadata = {"name": remote_name, "parents": [parent_id]}
    media = MediaFileUpload(str(local_path), mimetype=mime_type, resumable=False)

    file = service.files().create(
        body=metadata,
        media_body=media,
        fields="id, name, webViewLink, webContentLink, size",
        supportsAllDrives=True,
    ).execute()

    if make_public:
        try:
            service.permissions().create(
                fileId=file["id"],
                body={"type": "anyone", "role": "reader"},
                supportsAllDrives=True,
            ).execute()
        except Exception as e:
            print(f"  ⚠ Không set được public link: {e}", file=sys.stderr)

    return file


def cmd_test(args):
    """Test connection và quyền truy cập."""
    cred_path = find_credentials(args.credentials)
    print(f"✓ Credentials file: {cred_path}", file=sys.stderr)

    service, sa_email = build_service(cred_path)
    print(f"✓ Service account: {sa_email}", file=sys.stderr)

    # Test list
    try:
        about = service.about().get(fields="user, storageQuota").execute()
        quota = about.get("storageQuota", {})
        used = int(quota.get("usage", 0)) / (1024 ** 3)
        limit_raw = quota.get("limit")
        if limit_raw:
            limit_gb = int(limit_raw) / (1024 ** 3)
            print(f"✓ Quota: {used:.2f} GB / {limit_gb:.2f} GB used", file=sys.stderr)
        else:
            print(f"✓ Quota: {used:.2f} GB used (unlimited)", file=sys.stderr)
    except Exception as e:
        print(f"⚠ Không lấy được quota: {e}", file=sys.stderr)

    # Test folder
    try:
        root_id, images_id = ensure_folder_path(service)
        print(f"✓ {ROOT_FOLDER}/ id = {root_id}", file=sys.stderr)
        print(f"✓ {ROOT_FOLDER}/{IMAGES_FOLDER}/ id = {images_id}", file=sys.stderr)
    except Exception as e:
        print(f"✗ Lỗi truy cập folder: {e}", file=sys.stderr)
        sys.exit(1)

    print(json.dumps({
        "ok": True,
        "service_account": sa_email,
        "root_folder_id": root_id,
        "images_folder_id": images_id,
    }, ensure_ascii=False))


def cmd_upload(args):
    """Upload file."""
    local_path = Path(args.file)
    if not local_path.exists():
        print(f"ERROR: File không tồn tại: {local_path}", file=sys.stderr)
        sys.exit(2)

    type_code = args.type.upper()
    if type_code not in VALID_TYPES:
        print(f"ERROR: TYPE không hợp lệ '{args.type}'. Hợp lệ: {', '.join(VALID_TYPES)}",
              file=sys.stderr)
        sys.exit(2)

    cred_path = find_credentials(args.credentials)
    service, sa_email = build_service(cred_path)

    # Tạo cây thư mục nếu cần
    _, images_id = ensure_folder_path(service)

    # Tên file
    ext = local_path.suffix.lstrip(".") or "png"
    remote_name = make_filename(
        type_code, args.name, ext,
        keep_diacritics=args.keep_diacritics,
    )

    print(f"→ Uploading {local_path.name} → "
          f"{ROOT_FOLDER}/{IMAGES_FOLDER}/{remote_name}", file=sys.stderr)

    # Retry 3 lần với exponential backoff
    last_err = None
    for attempt in range(3):
        try:
            file_info = upload_file(
                service, local_path, remote_name, images_id,
                make_public=not args.private,
            )
            break
        except Exception as e:
            last_err = e
            wait = 2 ** attempt
            print(f"  ⚠ Lần {attempt+1} thất bại: {e}. Đợi {wait}s rồi retry...",
                  file=sys.stderr)
            time.sleep(wait)
    else:
        print(f"ERROR: Upload thất bại sau 3 lần. Lỗi cuối: {last_err}", file=sys.stderr)
        sys.exit(1)

    result = {
        "ok": True,
        "file_id": file_info["id"],
        "name": file_info["name"],
        "drive_path": f"{ROOT_FOLDER}/{IMAGES_FOLDER}/{file_info['name']}",
        "web_view_link": file_info.get("webViewLink"),
        "size_bytes": int(file_info.get("size", 0)) if file_info.get("size") else None,
        "service_account": sa_email,
    }
    print(f"✅ Uploaded: {result['drive_path']}", file=sys.stderr)
    print(f"🔗 Link: {result['web_view_link']}", file=sys.stderr)
    print(json.dumps(result, ensure_ascii=False))


def main():
    parser = argparse.ArgumentParser(description="Upload ảnh lên Google Drive (OpenClaw quy ước).")
    parser.add_argument("--credentials", help="Đường dẫn service account JSON")

    sub = parser.add_subparsers(dest="cmd")
    # Default = upload nếu có --file
    parser.add_argument("--file", help="File local cần upload")
    parser.add_argument("--type", help=f"Loại ảnh: {', '.join(VALID_TYPES)}")
    parser.add_argument("--name", help="Tên file gợi ý (sẽ sanitize)")
    parser.add_argument("--private", action="store_true",
                        help="Không set public, chỉ service account xem được")
    parser.add_argument("--keep-diacritics", action="store_true",
                        help="Giữ dấu tiếng Việt trong tên file (mặc định: bỏ dấu)")
    parser.add_argument("--test", action="store_true", help="Test connection rồi thoát")

    args = parser.parse_args()

    if args.test:
        cmd_test(args)
        return

    if not args.file or not args.type or not args.name:
        parser.error("Cần --file, --type, --name (hoặc --test).")

    cmd_upload(args)


if __name__ == "__main__":
    main()
