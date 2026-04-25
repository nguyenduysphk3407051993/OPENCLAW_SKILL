#!/usr/bin/env python3
"""
upload_to_openclaw.py
=====================

Script Python dự phòng dùng khi MCP Google Drive không có sẵn tool upload.
Sử dụng google-api-python-client + OAuth2 credentials.

Yêu cầu cài đặt:
    pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib

Cách dùng:
    python upload_to_openclaw.py <file_or_folder> [--note "Mô tả"] [--recursive]
    python upload_to_openclaw.py /home/duynt/de_thi.pdf
    python upload_to_openclaw.py /mnt/lessons/ --recursive --note "Giáo án KHTN 6"

Biến môi trường:
    GDRIVE_CREDENTIALS_PATH  Đường dẫn tới file credentials.json (OAuth client)
    GDRIVE_TOKEN_PATH        Đường dẫn lưu token.json (mặc định: ~/.openclaw/token.json)
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path
from typing import Iterable

try:
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from googleapiclient.discovery import build
    from googleapiclient.http import MediaFileUpload
except ImportError:
    sys.stderr.write(
        "Thiếu thư viện. Cài đặt:\n"
        "    pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib\n"
    )
    sys.exit(1)

# ----------------------------- Cấu hình -----------------------------

ROOT_FOLDER_NAME = "OPENCLAW"
SCOPES = ["https://www.googleapis.com/auth/drive.file"]

COMPOUND_EXTS = (".tar.gz", ".tar.bz2", ".tar.xz", ".tar.zst")

EXT_MAP = {
    "01_Documents": {".pdf", ".docx", ".doc", ".txt", ".md", ".markdown",
                     ".rtf", ".odt", ".tex", ".ltx", ".epub", ".mobi",
                     ".azw", ".azw3", ".pages", ".djvu"},
    "02_Images":    {".jpg", ".jpeg", ".jpe", ".jfif", ".png", ".gif",
                     ".webp", ".svg", ".svgz", ".bmp", ".tiff", ".tif",
                     ".heic", ".heif", ".ico", ".psd", ".ai", ".eps",
                     ".raw", ".cr2", ".nef", ".arw"},
    "03_Videos":    {".mp4", ".m4v", ".avi", ".mov", ".qt", ".mkv",
                     ".wmv", ".flv", ".webm", ".mpg", ".mpeg", ".mpe",
                     ".3gp", ".3g2", ".ogv", ".ts", ".mts", ".m2ts", ".vob"},
    "04_Audio":     {".mp3", ".wav", ".wave", ".flac", ".aac", ".ogg",
                     ".oga", ".m4a", ".wma", ".opus", ".aiff", ".aif",
                     ".alac", ".amr", ".mid", ".midi"},
    "05_Presentations": {".pptx", ".ppt", ".pptm", ".key", ".odp",
                         ".pps", ".ppsx"},
    "06_Spreadsheets":  {".xlsx", ".xls", ".xlsm", ".csv", ".tsv",
                         ".ods", ".numbers"},
    "07_Archives":  {".zip", ".rar", ".7z", ".tar", ".gz", ".gzip",
                     ".bz2", ".bzip2", ".xz", ".tgz", ".tbz2", ".txz",
                     ".iso", ".dmg"},
}

ALL_CATEGORIES = list(EXT_MAP.keys()) + ["08_Others"]

# ----------------------------- Phân loại -----------------------------

def classify(filename: str) -> str:
    """Trả về tên subfolder phù hợp dựa trên extension."""
    name_lower = filename.lower()
    for compound in COMPOUND_EXTS:
        if name_lower.endswith(compound):
            return "07_Archives"
    if "." not in filename or filename.startswith("."):
        return "08_Others"
    ext = "." + name_lower.rsplit(".", 1)[-1]
    for folder, exts in EXT_MAP.items():
        if ext in exts:
            return folder
    return "08_Others"


# ----------------------------- Auth & Drive -----------------------------

def get_drive_service():
    """Khởi tạo Drive API service. Tự refresh hoặc xin token nếu cần."""
    cred_path = os.environ.get("GDRIVE_CREDENTIALS_PATH")
    if not cred_path or not Path(cred_path).exists():
        sys.stderr.write(
            f"GDRIVE_CREDENTIALS_PATH chưa set hoặc file không tồn tại: {cred_path}\n"
            "Tải credentials.json từ Google Cloud Console và set biến môi trường.\n"
        )
        sys.exit(2)

    token_path = Path(
        os.environ.get("GDRIVE_TOKEN_PATH", str(Path.home() / ".openclaw" / "token.json"))
    )
    token_path.parent.mkdir(parents=True, exist_ok=True)

    creds = None
    if token_path.exists():
        creds = Credentials.from_authorized_user_file(str(token_path), SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(cred_path, SCOPES)
            creds = flow.run_local_server(port=0)
        token_path.write_text(creds.to_json())

    return build("drive", "v3", credentials=creds)


def find_or_create_folder(service, name: str, parent_id: str | None = None) -> str:
    """Trả về folder_id. Tạo mới nếu chưa tồn tại."""
    query_parts = [
        f"name = '{name}'",
        "mimeType = 'application/vnd.google-apps.folder'",
        "trashed = false",
    ]
    if parent_id:
        query_parts.append(f"'{parent_id}' in parents")
    else:
        query_parts.append("'root' in parents")

    query = " and ".join(query_parts)
    results = service.files().list(
        q=query, fields="files(id, name)", pageSize=10
    ).execute()
    files = results.get("files", [])

    if len(files) > 1:
        sys.stderr.write(
            f"⚠️  Có {len(files)} folder tên '{name}'. Dùng folder đầu tiên: {files[0]['id']}\n"
        )

    if files:
        return files[0]["id"]

    # Tạo mới
    metadata = {
        "name": name,
        "mimeType": "application/vnd.google-apps.folder",
    }
    if parent_id:
        metadata["parents"] = [parent_id]
    folder = service.files().create(body=metadata, fields="id").execute()
    print(f"  ➕ Đã tạo folder: {name} (id={folder['id']})")
    return folder["id"]


def file_exists_in_folder(service, name: str, parent_id: str) -> bool:
    """Kiểm tra file đã tồn tại trong folder."""
    safe_name = name.replace("'", "\\'")
    query = (
        f"name = '{safe_name}' and '{parent_id}' in parents "
        "and trashed = false and mimeType != 'application/vnd.google-apps.folder'"
    )
    results = service.files().list(q=query, fields="files(id)", pageSize=1).execute()
    return bool(results.get("files"))


def unique_name(service, original: str, parent_id: str) -> str:
    """Sinh tên duy nhất bằng cách thêm _(N) nếu trùng."""
    if not file_exists_in_folder(service, original, parent_id):
        return original
    stem = Path(original).stem
    suffix = "".join(Path(original).suffixes)
    n = 1
    while True:
        candidate = f"{stem}_({n}){suffix}"
        if not file_exists_in_folder(service, candidate, parent_id):
            return candidate
        n += 1


def upload_file(service, file_path: Path, parent_id: str, note: str | None = None) -> dict:
    """Upload một file. Trả dict {name, id, link, renamed_from}."""
    final_name = unique_name(service, file_path.name, parent_id)
    metadata = {"name": final_name, "parents": [parent_id]}
    if note:
        metadata["description"] = note

    media = MediaFileUpload(str(file_path), resumable=file_path.stat().st_size > 5 * 1024 * 1024)
    uploaded = service.files().create(
        body=metadata, media_body=media, fields="id, webViewLink"
    ).execute()

    return {
        "name": final_name,
        "id": uploaded["id"],
        "link": uploaded.get("webViewLink", ""),
        "renamed_from": file_path.name if final_name != file_path.name else None,
    }


# ----------------------------- Main flow -----------------------------

def collect_files(target: Path, recursive: bool) -> list[Path]:
    """Thu thập danh sách file từ input path."""
    if target.is_file():
        return [target]
    if target.is_dir():
        if recursive:
            return [p for p in target.rglob("*") if p.is_file() and not p.name.startswith(".")]
        return [p for p in target.iterdir() if p.is_file() and not p.name.startswith(".")]
    sys.stderr.write(f"Path không hợp lệ: {target}\n")
    sys.exit(3)


def humansize(nbytes: int) -> str:
    for unit in ("B", "KB", "MB", "GB"):
        if nbytes < 1024:
            return f"{nbytes:.1f} {unit}"
        nbytes /= 1024
    return f"{nbytes:.1f} TB"


def main():
    parser = argparse.ArgumentParser(description="Upload file lên OPENCLAW trên Google Drive.")
    parser.add_argument("path", help="File hoặc thư mục cần upload")
    parser.add_argument("--note", default=None, help="Ghi chú/mô tả (set vào field description)")
    parser.add_argument("--recursive", action="store_true", help="Đệ quy nếu path là thư mục")
    parser.add_argument("--yes", "-y", action="store_true", help="Bỏ qua confirm")
    args = parser.parse_args()

    target = Path(args.path).expanduser().resolve()
    files = collect_files(target, args.recursive)
    if not files:
        print("Không có file nào để upload.")
        return

    # Phân loại trước
    grouped: dict[str, list[Path]] = {}
    total_size = 0
    for f in files:
        cat = classify(f.name)
        grouped.setdefault(cat, []).append(f)
        total_size += f.stat().st_size

    # Hiển thị bảng phân loại
    print(f"\n📊 Đã quét được {len(files)} file. Phân loại:")
    for cat in ALL_CATEGORIES:
        if cat in grouped:
            print(f"  • {cat:20s}: {len(grouped[cat])} file")
    print(f"  Tổng dung lượng: {humansize(total_size)}\n")

    if not args.yes:
        confirm = input("Tiếp tục upload? (y/n): ").strip().lower()
        if confirm != "y":
            print("Huỷ.")
            return

    # Kết nối Drive
    print("🔌 Đang kết nối Google Drive...")
    service = get_drive_service()
    root_id = find_or_create_folder(service, ROOT_FOLDER_NAME)

    # Tạo subfolder cần thiết
    subfolder_ids: dict[str, str] = {}
    for cat in grouped:
        subfolder_ids[cat] = find_or_create_folder(service, cat, parent_id=root_id)

    # Upload
    results = {"success": [], "errors": []}
    for cat, file_list in grouped.items():
        parent = subfolder_ids[cat]
        for f in file_list:
            try:
                info = upload_file(service, f, parent, note=args.note)
                info["category"] = cat
                results["success"].append(info)
                marker = "↪" if info["renamed_from"] else "✓"
                print(f"  {marker} {cat}/{info['name']}")
            except Exception as e:
                results["errors"].append({"file": str(f), "error": str(e)})
                print(f"  ✗ {f.name}: {e}", file=sys.stderr)

    # Báo cáo
    print(f"\n✅ Hoàn tất: {len(results['success'])}/{len(files)} file thành công")
    renamed = [r for r in results["success"] if r["renamed_from"]]
    if renamed:
        print(f"⚠️  {len(renamed)} file đã rename do trùng tên:")
        for r in renamed:
            print(f"    {r['renamed_from']} → {r['name']}")
    if results["errors"]:
        print(f"❌ {len(results['errors'])} file lỗi:")
        for e in results["errors"]:
            print(f"    {e['file']}: {e['error']}")


if __name__ == "__main__":
    main()
