import sys

# Console Windows mặc định là cp1252/cp437 -> in tiếng Việt sẽ ném
# UnicodeEncodeError. Ép UTF-8 để chạy giống nhau trên Windows lẫn Linux.
for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass

def format_latex(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    out = []
    in_env = False
    in_loigiai = False
    
    for line in lines:
        s = line.strip()
        if not s:
            out.append("\n")
            continue
            
        if s.startswith(r"\end{ex}") or s.startswith(r"\end{bt}"):
            in_env = False
            out.append(s + "\n")
            continue
            
        if s == r"}" and in_loigiai:
            in_loigiai = False
            out.append("    " + s + "\n")
            continue
            
        if s.startswith(r"%%%"):
            in_env = False
            in_loigiai = False
            
        indent = ""
        if in_env:
            indent = "    "
            if s.startswith("{") or s.startswith(r"{\True"):
                # Inside \choice usually, indent more
                indent = "        "
            if in_loigiai:
                indent = "        "
                
        out.append(indent + s + "\n")
        
        if s.startswith(r"\begin{ex}") or s.startswith(r"\begin{bt}"):
            in_env = True
        elif s.startswith(r"\loigiai{"):
            in_loigiai = True

    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(out)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        format_latex(sys.argv[1])
