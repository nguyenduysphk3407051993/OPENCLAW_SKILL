#!/usr/bin/env python3
"""
TikZ Validator - Kiểm tra cú pháp code TikZ

Usage:
    python validate_tikz.py input.tex
    python validate_tikz.py --code "\\draw (0,0) -- (1,1);"
    python validate_tikz.py input.tex --fix --output fixed.tex

Features:
    - Kiểm tra cặp ngoặc {} [] ()
    - Kiểm tra môi trường tikzpicture
    - Kiểm tra lệnh phổ biến
    - Gợi ý sửa lỗi
"""

import argparse
import re
import sys
from pathlib import Path
from typing import List, Tuple

# Console Windows mặc định là cp1252/cp437 -> in tiếng Việt sẽ ném
# UnicodeEncodeError. Ép UTF-8 để chạy giống nhau trên Windows lẫn Linux.
for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass


class TikZValidator:
    """Validator for TikZ/LaTeX code."""
    
    COMMON_COMMANDS = [
        r'\draw', r'\fill', r'\node', r'\coordinate', r'\path',
        r'\foreach', r'\begin', r'\end', r'\usetikzlibrary',
        r'\tikzset', r'\pgfmathsetmacro', r'\def', r'\shade'
    ]
    
    BRACKET_PAIRS = {
        '{': '}',
        '[': ']',
        '(': ')'
    }
    
    def __init__(self):
        self.errors: List[Tuple[int, str, str]] = []  # (line, type, message)
        self.warnings: List[Tuple[int, str, str]] = []
    
    def validate(self, code: str) -> bool:
        """
        Validate TikZ code.
        
        Returns:
            True if valid, False if errors found
        """
        self.errors = []
        self.warnings = []
        
        lines = code.split('\n')
        
        # Check brackets
        self._check_brackets(code, lines)
        
        # Check environments
        self._check_environments(code, lines)
        
        # Check common issues
        self._check_common_issues(code, lines)
        
        # Check semicolons
        self._check_semicolons(code, lines)
        
        return len(self.errors) == 0
    
    def _check_brackets(self, code: str, lines: List[str]):
        """Check matching brackets."""
        stack = []
        
        for line_num, line in enumerate(lines, 1):
            # Skip comments
            comment_pos = line.find('%')
            if comment_pos >= 0:
                line = line[:comment_pos]
            
            for i, char in enumerate(line):
                if char in self.BRACKET_PAIRS:
                    stack.append((char, line_num, i))
                elif char in self.BRACKET_PAIRS.values():
                    if not stack:
                        self.errors.append((
                            line_num, 
                            'BRACKET',
                            f"Unmatched closing bracket '{char}' at column {i+1}"
                        ))
                    else:
                        open_bracket, _, _ = stack.pop()
                        expected = self.BRACKET_PAIRS[open_bracket]
                        if char != expected:
                            self.errors.append((
                                line_num,
                                'BRACKET',
                                f"Mismatched brackets: expected '{expected}', got '{char}'"
                            ))
        
        # Check unclosed brackets
        for bracket, line_num, col in stack:
            self.errors.append((
                line_num,
                'BRACKET',
                f"Unclosed bracket '{bracket}' at column {col+1}"
            ))
    
    def _check_environments(self, code: str, lines: List[str]):
        """Check LaTeX environments."""
        env_stack = []
        
        begin_pattern = re.compile(r'\\begin\{(\w+)\}')
        end_pattern = re.compile(r'\\end\{(\w+)\}')
        
        for line_num, line in enumerate(lines, 1):
            for match in begin_pattern.finditer(line):
                env_name = match.group(1)
                env_stack.append((env_name, line_num))
            
            for match in end_pattern.finditer(line):
                env_name = match.group(1)
                if not env_stack:
                    self.errors.append((
                        line_num,
                        'ENVIRONMENT',
                        f"\\end{{{env_name}}} without matching \\begin"
                    ))
                else:
                    expected_env, start_line = env_stack.pop()
                    if env_name != expected_env:
                        self.errors.append((
                            line_num,
                            'ENVIRONMENT',
                            f"Mismatched environment: expected \\end{{{expected_env}}}, got \\end{{{env_name}}}"
                        ))
        
        for env_name, line_num in env_stack:
            self.errors.append((
                line_num,
                'ENVIRONMENT',
                f"Unclosed environment \\begin{{{env_name}}}"
            ))
    
    # Lệnh vẽ đứng đầu dòng thì bắt buộc kết thúc bằng dấu ';'
    STARTERS = (r'\draw', r'\fill', r'\filldraw', r'\shade', r'\shadedraw',
                r'\path', r'\coordinate', r'\node', r'\clip', r'\useasboundingbox')

    def _check_semicolons(self, code: str, lines: List[str]):
        """Thiếu dấu ';' cuối lệnh vẽ.

        Lệnh TikZ được phép trải nhiều dòng, nên chỉ báo lỗi khi một lệnh chưa
        đóng ';' mà dòng kế tiếp đã mở một lệnh mới — lúc đó chắc chắn lệnh
        trước bị thiếu ';'. Cách này tránh báo oan cho lệnh xuống dòng.
        """
        in_pic = False
        cho_dau_cham_phay = 0          # số dòng của lệnh đang mở, 0 = không có

        for line_num, raw in enumerate(lines, 1):
            if r'\begin{tikzpicture}' in raw:
                in_pic = True
            if r'\end{tikzpicture}' in raw:
                if cho_dau_cham_phay:
                    self.errors.append((
                        cho_dau_cham_phay, 'SEMICOLON',
                        "Lệnh vẽ không có dấu ';' trước \\end{tikzpicture}"))
                    cho_dau_cham_phay = 0
                in_pic = False
                continue
            if not in_pic:
                continue

            line = raw.split('%')[0] if not raw.strip().startswith(r'\%') else raw
            stripped = line.strip()
            if not stripped:
                continue

            mo_lenh = stripped.startswith(self.STARTERS)
            if mo_lenh and cho_dau_cham_phay:
                self.errors.append((
                    cho_dau_cham_phay, 'SEMICOLON',
                    "Lệnh vẽ thiếu dấu ';' ở cuối"))
                cho_dau_cham_phay = 0

            if ';' in line:
                cho_dau_cham_phay = 0
            elif mo_lenh:
                cho_dau_cham_phay = line_num


    def _check_common_issues(self, code: str, lines: List[str]):
        """Check common TikZ issues."""
        
        for line_num, line in enumerate(lines, 1):
            # Check for common typos
            if r'\daw' in line:
                self.errors.append((line_num, 'TYPO', "Possible typo: '\\daw' should be '\\draw'"))
            
            if r'\nod' in line and r'\node' not in line:
                self.errors.append((line_num, 'TYPO', "Possible typo: '\\nod' should be '\\node'"))
            
            # Check coordinate format
            coord_pattern = re.compile(r'\(([^)]+)\)')
            for match in coord_pattern.finditer(line):
                content = match.group(1)
                # Check for invalid coordinate (e.g., missing comma)
                if re.match(r'^\d+\s+\d+$', content.strip()):
                    self.warnings.append((
                        line_num,
                        'COORDINATE',
                        f"Coordinate '{content}' might be missing comma: use (x,y) format"
                    ))
            
            # Nối hai toạ độ bằng một dấu '-' thay vì '--'.
            #
            # Chỉ cảnh báo khi dấu '-' nằm đúng giữa hai dấu ngoặc, kiểu
            # `(A)-(B)`. Không được bắt các trường hợp hợp lệ rất phổ biến:
            # số âm `++(-1,0)`, phép trừ trong toạ độ `(\x-0.8, 0)`, hay mũi
            # tên `[|<->|]`, `[->]`, `[-{Stealth}]`.
            if r'\draw' in line and re.search(r'\)\s*-\s*\(', line):
                self.warnings.append((
                    line_num,
                    'PATH',
                    "Nối hai toạ độ bằng một dấu '-'. Đường thẳng phải dùng '--'."
                ))
    
    def get_report(self) -> str:
        """Generate validation report."""
        report = []
        
        if self.errors:
            report.append("❌ ERRORS:")
            for line, err_type, msg in sorted(self.errors):
                report.append(f"   Line {line} [{err_type}]: {msg}")
        
        if self.warnings:
            report.append("\n⚠️  WARNINGS:")
            for line, warn_type, msg in sorted(self.warnings):
                report.append(f"   Line {line} [{warn_type}]: {msg}")
        
        if not self.errors and not self.warnings:
            report.append("✅ No issues found!")
        
        return '\n'.join(report)


def main():
    parser = argparse.ArgumentParser(
        description="Validate TikZ/LaTeX code syntax"
    )
    
    parser.add_argument(
        "input",
        nargs='?',
        help="Input .tex file"
    )
    
    parser.add_argument(
        "--code", "-c",
        type=str,
        help="TikZ code string"
    )
    
    parser.add_argument(
        "--quiet", "-q",
        action="store_true",
        help="Only show errors, not warnings"
    )
    
    args = parser.parse_args()
    
    if args.code:
        code = args.code
    elif args.input:
        path = Path(args.input)
        if not path.exists():
            print(f"❌ File not found: {args.input}")
            sys.exit(1)
        code = path.read_text(encoding='utf-8')
    else:
        parser.error("Either input file or --code is required")
        return
    
    validator = TikZValidator()
    is_valid = validator.validate(code)
    
    if args.quiet:
        if validator.errors:
            for line, err_type, msg in sorted(validator.errors):
                print(f"Line {line}: {msg}")
    else:
        print(validator.get_report())
    
    sys.exit(0 if is_valid else 1)


if __name__ == "__main__":
    main()
