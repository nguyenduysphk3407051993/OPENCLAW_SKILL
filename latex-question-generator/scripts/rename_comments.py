import sys
import re

# Console Windows mặc định là cp1252/cp437 -> in tiếng Việt sẽ ném
# UnicodeEncodeError. Ép UTF-8 để chạy giống nhau trên Windows lẫn Linux.
for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass

def update_comments(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Matches %%%=========[Môi trường: EX]_[1]================%%%
    # and replaces with %%%=========[EX_01]================%%%
    
    def replacer(match):
        env = match.group(1)
        num = int(match.group(2))
        return f"%%%=========[{env}_{num:02d}]================%%%"

    new_content = re.sub(r"%%%=========\[Môi trường: (EX|TF|SA|BT)\]_\[(\d+)\]================%%%", replacer, content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        update_comments(sys.argv[1])
