#!/usr/bin/env python3
"""
ocr_to_docx.py — Trích xuất text và hình ảnh từ file PDF chạy hoàn toàn offline (không dùng API key).
Sau đó chuyển đổi text sang file .docx đẹp mắt.

Usage:
    python ocr_to_docx.py --input document.pdf --output result.docx
    python ocr_to_docx.py --input document.pdf --output result.docx --dpi 200
"""
from __future__ import annotations

import argparse
import io
import os
import re
import sys
from pathlib import Path

# Đảm bảo console trên Windows không bị lỗi UnicodeEncodeError khi in tiếng Việt
if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except AttributeError:
        pass

from PIL import Image

# Import script build_exam_docx cùng thư mục
_SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(_SCRIPT_DIR))
from build_exam_docx import markdown_to_docx


# ============================================================
# PDF → Text (Offline)
# ============================================================

def extract_pdf_text_local(pdf_bytes: bytes) -> list[dict]:
    """Trích xuất text kỹ thuật số thô trực tiếp từ file PDF (offline)."""
    import fitz  # PyMuPDF

    doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    pages = []
    try:
        for page_index in range(len(doc)):
            page_num = page_index + 1
            page = doc.load_page(page_index)
            text = page.get_text("text").strip()
            pages.append({"page": page_num, "markdown": text, "error": None})
        return pages
    finally:
        doc.close()


# ============================================================
# PDF → Images (Offline)
# ============================================================

def extract_pdf_images(pdf_bytes: bytes, output_images_dir: Path) -> dict[int, list[str]]:
    """Trích xuất tất cả các hình vẽ/ảnh gốc từ file PDF và lưu vào thư mục output_images_dir.
    Trả về dict dạng {page_num: [image_paths]}
    """
    import fitz  # PyMuPDF
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    output_images_dir.mkdir(parents=True, exist_ok=True)
    
    extracted = {}
    for page_index in range(len(doc)):
        page_num = page_index + 1
        page = doc.load_page(page_index)
        image_list = page.get_images(full=True)
        
        page_images = []
        for img_idx, img in enumerate(image_list):
            try:
                xref = img[0]
                base_image = doc.extract_image(xref)
                image_bytes = base_image["image"]
                image_ext = base_image["ext"]
                
                # Bỏ qua những ảnh quá nhỏ (như icon, vạch phân tách, trang trí)
                if len(image_bytes) < 2048:
                    continue
                    
                img_name = f"page_{page_num}_img_{img_idx + 1}.{image_ext}"
                img_path = output_images_dir / img_name
                img_path.write_bytes(image_bytes)
                
                # Lưu đường dẫn tương đối (với thư mục chứa file docx đầu ra)
                page_images.append(f"images/{img_name}")
            except Exception as e:
                print(f"Warning: Lỗi trích xuất ảnh xref {img[0]} ở trang {page_num}: {e}")
                
        if page_images:
            extracted[page_num] = page_images
            
    doc.close()
    return extracted


def combine_markdown_pages(pages: list[dict], extracted_images: dict[int, list[str]]) -> str:
    """Ghép markdown nhiều trang, bổ sung các hình ảnh đã trích xuất nếu có."""
    chunks = []
    for page in sorted(pages, key=lambda x: x["page"]):
        page_num = page["page"]
        text = page.get("markdown", "").strip()
        
        # Nhúng các ảnh trích xuất được vào cuối trang text
        page_imgs = extracted_images.get(page_num, [])
        img_markdown = ""
        if page_imgs:
            img_markdown = "\n\n" + "\n\n".join(f"![Hình minh họa]({img_path})" for img_path in page_imgs)

        if text:
            chunks.append(f"# Page {page_num}\n\n{text}{img_markdown}")
        else:
            if img_markdown:
                chunks.append(f"# Page {page_num}\n\n*Trang này không chứa text kỹ thuật số, chỉ có hình ảnh:*\n{img_markdown}")
            else:
                chunks.append(f"# Page {page_num}\n\n*Trang trống hoặc là ảnh quét/PDF scan. Hãy dùng AI Assistant để số hóa thủ công trang này.*")

    return "\n\n\\newpage\n\n".join(chunks)


# ============================================================
# CLI
# ============================================================

def main():
    parser = argparse.ArgumentParser(
        description="Trích xuất text và hình ảnh từ PDF chạy offline (không dùng API key) → .docx đẹp mắt"
    )
    parser.add_argument("--input", "-i", nargs="+", required=True, help="File PDF/ảnh đầu vào")
    parser.add_argument("--output", "-o", default="output.docx", help="File docx đầu ra")
    parser.add_argument("--dpi", type=int, default=200, help="DPI khi render (không dùng khi chạy offline)")
    parser.add_argument("--mode", default="page", help="Chế độ chạy (giữ tương thích ngược)")
    parser.add_argument("--toggle-tex", action="store_true", default=True, help="Giữ công thức TeX text")
    parser.add_argument("--equation", action="store_true", help="Chuyển công thức sang OMML")
    args = parser.parse_args()

    all_markdown = []
    output_path_obj = Path(args.output)
    images_dir = output_path_obj.parent / "images"

    for input_path in args.input:
        p = Path(input_path)
        if not p.exists():
            print(f"ERROR: File không tồn tại: {p}", file=sys.stderr)
            sys.exit(1)

        ext = p.suffix.lower()

        if ext == ".pdf":
            print(f"Đang trích xuất offline PDF: {p.name} ({len(p.read_bytes()) // 1024} KB)")
            pdf_bytes = p.read_bytes()
            
            # Trích xuất ảnh gốc
            extracted_images = extract_pdf_images(pdf_bytes, images_dir)
            print(f"  -> Đã trích xuất {sum(len(v) for v in extracted_images.values())} hình ảnh.")
            
            # Trích xuất text kỹ thuật số
            pages = extract_pdf_text_local(pdf_bytes)
            non_empty = sum(1 for pg in pages if pg.get("markdown"))
            print(f"  -> Tìm thấy {non_empty}/{len(pages)} trang chứa văn bản kỹ thuật số.")
            
            md = combine_markdown_pages(pages, extracted_images)
            all_markdown.append(md)
        else:
            print(f"WARNING: Bỏ qua file '{p.name}'. OCR ngoại tuyến cho ảnh chưa được hỗ trợ.", file=sys.stderr)
            print("Vui lòng gửi ảnh trực tiếp vào chat để AI Assistant tự động số hóa và viết Markdown.", file=sys.stderr)
            continue

    if not all_markdown:
        print("ERROR: Không trích xuất được nội dung nào từ các file đầu vào.", file=sys.stderr)
        sys.exit(1)

    combined = "\n\n\\newpage\n\n".join(all_markdown)
    
    # Ghi lại file markdown thô để người dùng chỉnh sửa nếu cần
    raw_md_path = output_path_obj.parent / "extracted_raw.md"
    raw_md_path.write_text(combined, encoding="utf-8")
    print(f"  -> Đã lưu văn bản trích xuất thô vào: {raw_md_path.resolve()}")

    use_toggle_tex = not args.equation
    markdown_to_docx(combined, output_path_obj, toggle_tex=use_toggle_tex)
    print(f"OK: Đã xuất file Word: {output_path_obj.resolve()}")


if __name__ == "__main__":
    main()
