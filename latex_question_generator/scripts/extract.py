import sys
import io

# Console Windows mặc định là cp1252/cp437 -> in tiếng Việt sẽ ném
# UnicodeEncodeError. Ép UTF-8 để chạy giống nhau trên Windows lẫn Linux.
for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass

def extract_text(pdf_path, out_path):
    try:
        import fitz
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            text += page.get_text()
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(text)
    except Exception as e:
        print(f"PyMuPDF Error: {e}")
        try:
            import PyPDF2
            with open(pdf_path, 'rb') as f:
                reader = PyPDF2.PdfReader(f)
                text = ""
                for page in reader.pages:
                    text += page.extract_text()
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(text)
        except Exception as e2:
            print(f"PyPDF2 Error: {e2}")

if __name__ == "__main__":
    if len(sys.argv) > 2:
        extract_text(sys.argv[1], sys.argv[2])
