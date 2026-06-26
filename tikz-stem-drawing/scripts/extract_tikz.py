#!/usr/bin/env python3
"""
TikZ Extractor - Trích xuất và tổ chức code TikZ từ file LaTeX

Usage:
    python extract_tikz.py input.tex --output figures/
    python extract_tikz.py document.tex --list
    python extract_tikz.py input.tex --index 2 --output figure2.tex

Features:
    - Trích xuất tất cả tikzpicture từ document
    - Xuất thành file standalone riêng lẻ
    - Liệt kê các hình trong document
"""

import argparse
import re
from pathlib import Path
from typing import List, Tuple, Optional


STANDALONE_WRAPPER = r"""\documentclass[tikz,border=5pt]{{standalone}}
\usepackage[utf8]{{inputenc}}
\usepackage{{tikz}}
\usepackage{{pgfplots}}
\usepackage{{chemfig}}
\usepackage{{circuitikz}}
\pgfplotsset{{compat=1.18}}
\usetikzlibrary{{
    calc, arrows.meta, angles, quotes, positioning,
    patterns, shapes.geometric, decorations.pathmorphing
}}

\begin{{document}}
{content}
\end{{document}}
"""


def extract_tikz_pictures(latex_content: str) -> List[Tuple[int, int, str]]:
    """
    Extract all tikzpicture environments from LaTeX content.
    
    Returns:
        List of tuples: (start_line, end_line, tikz_code)
    """
    results = []
    
    # Pattern to match tikzpicture environment
    pattern = re.compile(
        r'(\\begin\{tikzpicture\}.*?\\end\{tikzpicture\})',
        re.DOTALL
    )
    
    lines = latex_content.split('\n')
    
    for match in pattern.finditer(latex_content):
        tikz_code = match.group(1)
        start_pos = match.start()
        end_pos = match.end()
        
        # Calculate line numbers
        start_line = latex_content[:start_pos].count('\n') + 1
        end_line = latex_content[:end_pos].count('\n') + 1
        
        results.append((start_line, end_line, tikz_code))
    
    return results


def extract_chemfig(latex_content: str) -> List[Tuple[int, str]]:
    """
    Extract all chemfig commands from LaTeX content.
    
    Returns:
        List of tuples: (line_number, chemfig_code)
    """
    results = []
    
    # Pattern for chemfig
    pattern = re.compile(r'(\\chemfig\{[^}]+\})')
    
    for match in pattern.finditer(latex_content):
        chemfig_code = match.group(1)
        line_num = latex_content[:match.start()].count('\n') + 1
        results.append((line_num, chemfig_code))
    
    return results


def create_standalone(tikz_code: str) -> str:
    """Wrap TikZ code in standalone document."""
    return STANDALONE_WRAPPER.format(content=tikz_code)


def list_figures(latex_content: str) -> str:
    """Generate a list of all figures in the document."""
    tikz_pics = extract_tikz_pictures(latex_content)
    chemfigs = extract_chemfig(latex_content)
    
    report = []
    report.append(f"📊 Found {len(tikz_pics)} tikzpicture(s):")
    report.append("-" * 40)
    
    for i, (start, end, code) in enumerate(tikz_pics, 1):
        # Get first meaningful line for preview
        preview_lines = [l.strip() for l in code.split('\n') if l.strip() and not l.strip().startswith('%')]
        preview = preview_lines[1] if len(preview_lines) > 1 else preview_lines[0] if preview_lines else ""
        preview = preview[:50] + "..." if len(preview) > 50 else preview
        
        report.append(f"  [{i}] Lines {start}-{end}: {preview}")
    
    if chemfigs:
        report.append(f"\n🧪 Found {len(chemfigs)} chemfig(s):")
        report.append("-" * 40)
        for i, (line, code) in enumerate(chemfigs, 1):
            preview = code[:50] + "..." if len(code) > 50 else code
            report.append(f"  [{i}] Line {line}: {preview}")
    
    return '\n'.join(report)


def extract_to_files(
    latex_content: str, 
    output_dir: Path, 
    prefix: str = "figure"
) -> List[Path]:
    """Extract all tikzpictures to separate files."""
    output_dir.mkdir(parents=True, exist_ok=True)
    
    tikz_pics = extract_tikz_pictures(latex_content)
    created_files = []
    
    for i, (start, end, code) in enumerate(tikz_pics, 1):
        filename = f"{prefix}_{i:02d}.tex"
        filepath = output_dir / filename
        
        standalone_content = create_standalone(code)
        filepath.write_text(standalone_content, encoding='utf-8')
        created_files.append(filepath)
        print(f"✅ Created: {filepath}")
    
    return created_files


def extract_single(
    latex_content: str, 
    index: int, 
    output_path: Optional[Path] = None
) -> Optional[str]:
    """Extract a single tikzpicture by index."""
    tikz_pics = extract_tikz_pictures(latex_content)
    
    if index < 1 or index > len(tikz_pics):
        print(f"❌ Invalid index: {index}. Found {len(tikz_pics)} figures.")
        return None
    
    _, _, code = tikz_pics[index - 1]
    standalone_content = create_standalone(code)
    
    if output_path:
        output_path.write_text(standalone_content, encoding='utf-8')
        print(f"✅ Extracted figure {index} to: {output_path}")
    
    return standalone_content


def main():
    parser = argparse.ArgumentParser(
        description="Extract TikZ figures from LaTeX documents",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    %(prog)s document.tex --list
    %(prog)s document.tex --output figures/
    %(prog)s document.tex --index 2 --output figure2.tex
        """
    )
    
    parser.add_argument(
        "input",
        type=str,
        help="Input LaTeX file"
    )
    
    parser.add_argument(
        "--list", "-l",
        action="store_true",
        help="List all figures in the document"
    )
    
    parser.add_argument(
        "--output", "-o",
        type=str,
        help="Output file or directory"
    )
    
    parser.add_argument(
        "--index", "-i",
        type=int,
        help="Extract specific figure by index (1-based)"
    )
    
    parser.add_argument(
        "--prefix", "-p",
        type=str,
        default="figure",
        help="Prefix for output filenames (default: figure)"
    )
    
    args = parser.parse_args()
    
    input_path = Path(args.input)
    if not input_path.exists():
        print(f"❌ File not found: {args.input}")
        return 1
    
    content = input_path.read_text(encoding='utf-8')
    
    if args.list:
        print(list_figures(content))
        return 0
    
    if args.index:
        output_path = Path(args.output) if args.output else None
        result = extract_single(content, args.index, output_path)
        if result and not output_path:
            print(result)
        return 0 if result else 1
    
    if args.output:
        output_path = Path(args.output)
        if output_path.suffix == '.tex':
            # Single file output for first figure
            extract_single(content, 1, output_path)
        else:
            # Directory output for all figures
            extract_to_files(content, output_path, args.prefix)
        return 0
    
    # Default: list figures
    print(list_figures(content))
    return 0


if __name__ == "__main__":
    exit(main())
