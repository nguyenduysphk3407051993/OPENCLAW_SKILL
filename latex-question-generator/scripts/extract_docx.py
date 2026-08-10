import docx
import sys

# Console Windows mặc định là cp1252/cp437 -> in tiếng Việt sẽ ném
# UnicodeEncodeError. Ép UTF-8 để chạy giống nhau trên Windows lẫn Linux.
for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass

def read_docx(file_path):
    doc = docx.Document(file_path)
    full_text = []
    for para in doc.paragraphs:
        text = para.text.strip()
        if text:
            full_text.append(text)
    return '\n'.join(full_text)

if __name__ == "__main__":
    content = read_docx(r"d:\QUAN_NHIEM_BAN_TRU\ANTI_GRAVITY\INPUT\DE_CUONG_GIUA_HOC_KI_2_VAT_LY_6.docx")
    with open(r"d:\QUAN_NHIEM_BAN_TRU\ANTI_GRAVITY\tmp_read_docx.txt", "w", encoding="utf-8") as f:
        f.write(content)
