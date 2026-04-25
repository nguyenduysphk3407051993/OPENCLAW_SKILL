#!/usr/bin/env python3
"""
check_and_upload.py — Kiểm tra kích thước ảnh local, upload Drive nếu > 4MB.

Đây là wrapper đơn giản dùng SAU khi Claude (host OpenClaw) đã sinh ảnh
bằng tool image-gen có sẵn và lưu ra file. Script này chỉ:
1. Kiểm tra file tồn tại + đọc size.
2. Nếu > THRESHOLD_MB → gọi upload_drive.py.
3. Trả JSON tổng hợp gồm local path + (nếu có) Drive link.

Usage:
    python check_and_upload.py \\
        --file /tmp/quang_hop_lop6.png \\
        --type INFOGRAPHIC \\
        --name quang_hop_lop6
"""

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

THRESHOLD_MB = 4.0
SCRIPT_DIR = Path(__file__).resolve().parent


def main():
    parser = argparse.ArgumentParser(description="Check size & upload to Drive if > threshold.")
    parser.add_argument("--file", required=True, help="File ảnh đã sinh ra")
    parser.add_argument("--type", required=True,
                        help="TYPE code (INFOGRAPHIC, MINDMAP, ...)")
    parser.add_argument("--name", required=True, help="Tên file gợi ý")
    parser.add_argument("--credentials", help="Service account JSON path")
    parser.add_argument("--private", action="store_true",
                        help="Upload private (không public link)")
    parser.add_argument("--keep-diacritics", action="store_true",
                        help="Giữ dấu tiếng Việt trong tên file")
    parser.add_argument("--threshold-mb", type=float, default=THRESHOLD_MB)
    parser.add_argument("--always-upload", action="store_true",
                        help="Luôn upload kể cả khi nhỏ")
    parser.add_argument("--never-upload", action="store_true",
                        help="Không upload, chỉ giữ local")
    args = parser.parse_args()

    if args.always_upload and args.never_upload:
        parser.error("Không dùng đồng thời --always-upload và --never-upload.")

    local_path = Path(args.file)
    if not local_path.exists():
        print(f"ERROR: File không tồn tại: {local_path}", file=sys.stderr)
        sys.exit(2)

    size_bytes = local_path.stat().st_size
    size_mb = round(size_bytes / (1024 * 1024), 2)

    # Quyết định upload
    if args.always_upload:
        should_upload = True
        reason = "force-upload"
    elif args.never_upload:
        should_upload = False
        reason = "never-upload-flag"
    elif size_mb > args.threshold_mb:
        should_upload = True
        reason = f"size {size_mb}MB > threshold {args.threshold_mb}MB"
    else:
        should_upload = False
        reason = f"size {size_mb}MB <= threshold {args.threshold_mb}MB"

    print(f"→ File: {local_path} ({size_mb} MB)", file=sys.stderr)
    print(f"→ Upload: {should_upload} ({reason})", file=sys.stderr)

    upload_result = None
    if should_upload:
        cmd = [
            sys.executable, str(SCRIPT_DIR / "upload_drive.py"),
            "--file", str(local_path),
            "--type", args.type,
            "--name", args.name,
        ]
        if args.credentials:
            cmd.extend(["--credentials", args.credentials])
        if args.private:
            cmd.append("--private")
        if args.keep_diacritics:
            cmd.append("--keep-diacritics")

        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            # Tìm JSON line cuối
            for line in reversed(result.stdout.strip().splitlines()):
                line = line.strip()
                if line.startswith("{"):
                    upload_result = json.loads(line)
                    break
        except subprocess.CalledProcessError as e:
            print(f"⚠ Upload thất bại: {e.stderr}", file=sys.stderr)
            upload_result = {"ok": False, "error": e.stderr}

    final = {
        "ok": True,
        "local": {
            "path": str(local_path.resolve()),
            "size_mb": size_mb,
            "size_bytes": size_bytes,
        },
        "uploaded": should_upload,
        "upload_reason": reason,
        "drive": upload_result if should_upload else None,
        "type": args.type.upper(),
        "name": args.name,
    }

    # Pretty summary
    print("\n" + "=" * 60, file=sys.stderr)
    print(f"✅ {local_path.name} ({size_mb} MB)", file=sys.stderr)
    if should_upload and upload_result and upload_result.get("ok"):
        print(f"📁 {upload_result['drive_path']}", file=sys.stderr)
        print(f"🔗 {upload_result['web_view_link']}", file=sys.stderr)
    elif not should_upload:
        print(f"📍 Local only: {local_path}", file=sys.stderr)
    print("=" * 60 + "\n", file=sys.stderr)

    print(json.dumps(final, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
