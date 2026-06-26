#!/usr/bin/env python3
"""
TikZ Compiler - Biên dịch code TikZ ra PDF hoặc PNG

Usage:
    python compile_tikz.py input.tex --output output.pdf
    python compile_tikz.py input.tex --output output.png --dpi 300
    python compile_tikz.py --code "\\draw (0,0) -- (1,1);" --output test.pdf

Requirements:
    - pdflatex (TeX Live hoặc MiKTeX)
    - ImageMagick (cho PNG output)
"""

import argparse
import subprocess
import tempfile
import shutil
import os
from pathlib import Path

STANDALONE_TEMPLATE = r"""
\documentclass[tikz,border=5pt]{standalone}
\usepackage[utf8]{inputenc}
\usepackage{tikz}
\usepackage{pgfplots}
\usepackage{chemfig}
\usepackage{circuitikz}
\pgfplotsset{compat=1.18}
\usetikzlibrary{
    calc, arrows.meta, angles, quotes, positioning,
    patterns, shapes.geometric, decorations.pathmorphing,
    decorations.markings, intersections
}

\begin{document}
\begin{tikzpicture}
%TIKZ_CODE%
\end{tikzpicture}
\end{document}
"""


def compile_tikz(tikz_code: str, output_path: str, dpi: int = 300) -> bool:
    """
    Compile TikZ code to PDF or PNG.
    
    Args:
        tikz_code: TikZ code (without tikzpicture environment)
        output_path: Output file path (.pdf or .png)
        dpi: DPI for PNG output
    
    Returns:
        True if successful, False otherwise
    """
    output_path = Path(output_path)
    output_format = output_path.suffix.lower()
    
    if output_format not in ['.pdf', '.png']:
        print(f"❌ Unsupported format: {output_format}")
        return False
    
    # Create temporary directory
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)
        
        # Write LaTeX file
        tex_content = STANDALONE_TEMPLATE.replace('%TIKZ_CODE%', tikz_code)
        tex_file = tmpdir / "tikz_temp.tex"
        tex_file.write_text(tex_content, encoding='utf-8')
        
        # Compile with pdflatex
        try:
            result = subprocess.run(
                ['pdflatex', '-interaction=nonstopmode', '-output-directory', str(tmpdir), str(tex_file)],
                capture_output=True,
                text=True,
                timeout=30
            )
            
            pdf_file = tmpdir / "tikz_temp.pdf"
            
            if not pdf_file.exists():
                print("❌ Compilation failed!")
                print(result.stdout[-2000:] if len(result.stdout) > 2000 else result.stdout)
                return False
            
            if output_format == '.pdf':
                shutil.copy(pdf_file, output_path)
                print(f"✅ PDF saved: {output_path}")
                return True
            
            elif output_format == '.png':
                # Convert PDF to PNG using ImageMagick
                result = subprocess.run(
                    ['convert', '-density', str(dpi), str(pdf_file), '-quality', '100', str(output_path)],
                    capture_output=True,
                    text=True
                )
                
                if output_path.exists():
                    print(f"✅ PNG saved: {output_path}")
                    return True
                else:
                    print("❌ PNG conversion failed!")
                    print(result.stderr)
                    return False
                    
        except subprocess.TimeoutExpired:
            print("❌ Compilation timeout!")
            return False
        except FileNotFoundError as e:
            print(f"❌ Command not found: {e}")
            print("Make sure pdflatex and ImageMagick are installed.")
            return False


def compile_tex_file(tex_path: str, output_path: str, dpi: int = 300) -> bool:
    """Compile a complete .tex file."""
    tex_path = Path(tex_path)
    output_path = Path(output_path)
    
    if not tex_path.exists():
        print(f"❌ File not found: {tex_path}")
        return False
    
    content = tex_path.read_text(encoding='utf-8')
    
    # Extract tikzpicture content if standalone template
    if r'\begin{tikzpicture}' in content:
        import re
        match = re.search(r'\\begin{tikzpicture}.*?\\end{tikzpicture}', content, re.DOTALL)
        if match:
            # Use the full content as-is for tex files
            pass
    
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)
        temp_tex = tmpdir / tex_path.name
        shutil.copy(tex_path, temp_tex)
        
        try:
            result = subprocess.run(
                ['pdflatex', '-interaction=nonstopmode', '-output-directory', str(tmpdir), str(temp_tex)],
                capture_output=True,
                text=True,
                timeout=30
            )
            
            pdf_file = tmpdir / temp_tex.with_suffix('.pdf').name
            
            if pdf_file.exists():
                if output_path.suffix.lower() == '.pdf':
                    shutil.copy(pdf_file, output_path)
                    print(f"✅ PDF saved: {output_path}")
                    return True
                elif output_path.suffix.lower() == '.png':
                    subprocess.run(
                        ['convert', '-density', str(dpi), str(pdf_file), '-quality', '100', str(output_path)],
                        capture_output=True
                    )
                    if output_path.exists():
                        print(f"✅ PNG saved: {output_path}")
                        return True
            
            print("❌ Compilation failed!")
            return False
            
        except Exception as e:
            print(f"❌ Error: {e}")
            return False


def main():
    parser = argparse.ArgumentParser(
        description="Compile TikZ code to PDF or PNG",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    %(prog)s input.tex --output figure.pdf
    %(prog)s input.tex --output figure.png --dpi 300
    %(prog)s --code "\\draw (0,0) circle (1);" --output circle.pdf
        """
    )
    
    parser.add_argument(
        "input",
        nargs='?',
        help="Input .tex file"
    )
    
    parser.add_argument(
        "--code", "-c",
        type=str,
        help="TikZ code string (without tikzpicture environment)"
    )
    
    parser.add_argument(
        "--output", "-o",
        type=str,
        required=True,
        help="Output file path (.pdf or .png)"
    )
    
    parser.add_argument(
        "--dpi",
        type=int,
        default=300,
        help="DPI for PNG output (default: 300)"
    )
    
    args = parser.parse_args()
    
    if args.code:
        success = compile_tikz(args.code, args.output, args.dpi)
    elif args.input:
        success = compile_tex_file(args.input, args.output, args.dpi)
    else:
        parser.error("Either input file or --code is required")
        return
    
    exit(0 if success else 1)


if __name__ == "__main__":
    main()
