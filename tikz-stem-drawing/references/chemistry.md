# Mẫu TikZ - Công thức cấu tạo Hóa học

## Preamble chuẩn cho Hóa học

```latex
\documentclass{article}
\usepackage[utf8]{vietnam}
\usetikzlibrary{calc,angles,intersections,positioning,shapes.geometric,arrows,decorations.markings,arrows.meta,patterns.meta,patterns,quotes}
\usetikzlibrary{hobby}
\usepackage{tikz-3dplot,pgfplots}
\pgfplotsset{compat=1.15}
\usepgfplotslibrary{polar}
\usepackage{tkz-tab}
\usepackage{amsmath}
\usepackage{chemfig}

\begin{document}
% Code chemfig hoặc tikz ở đây
\end{document}
```

---

## CƠ BẢN CHEMFIG

### Quy ước góc trong chemfig

```
        2 (90°)
         |
    3 ---|--- 1 (30°)
   (150°)|    
    4 ---|--- 0 (0°, mặc định)
   (210°)|
    5 ---|--- 7 (-30°)
         |
        6 (270°)
```

### Các loại liên kết

```latex
% Liên kết đơn
\chemfig{A-B}

% Liên kết đôi
\chemfig{A=B}

% Liên kết ba
\chemfig{A~B}

% Liên kết theo góc
\chemfig{A-[1]B}   % góc 30°
\chemfig{A-[2]B}   % góc 90° (lên)
\chemfig{A-[6]B}   % góc 270° (xuống)
```

---

## HYDROCARBON

### 1. Metan (CH₄)

```latex
\chemfig{C(-[2]H)(-[4]H)(-[6]H)-H}
```

### 2. Etan (C₂H₆)

```latex
\chemfig{H-C(-[2]H)(-[6]H)-C(-[2]H)(-[6]H)-H}
```

### 3. Propan (C₃H₈)

```latex
\chemfig{H-C(-[2]H)(-[6]H)-C(-[2]H)(-[6]H)-C(-[2]H)(-[6]H)-H}
```

### 4. Butan (C₄H₁₀) - mạch thẳng

```latex
\chemfig{H_3C-CH_2-CH_2-CH_3}
% Hoặc chi tiết:
\chemfig{H-C(-[2]H)(-[6]H)-C(-[2]H)(-[6]H)-C(-[2]H)(-[6]H)-C(-[2]H)(-[6]H)-H}
```

### 5. Isobutan (C₄H₁₀) - mạch nhánh

```latex
\chemfig{H_3C-C(-[2]CH_3)(-[6]H)-CH_3}
```

### 6. Etilen (C₂H₄) - liên kết đôi

```latex
\chemfig{H-C(-[2]H)=C(-[2]H)-H}
% Hoặc đơn giản:
\chemfig{H_2C=CH_2}
```

### 7. Propilen (C₃H₆)

```latex
\chemfig{H_2C=CH-CH_3}
```

### 8. Axetilen (C₂H₂) - liên kết ba

```latex
\chemfig{H-C~C-H}
```

### 9. Propin (C₃H₄)

```latex
\chemfig{H-C~C-CH_3}
```

---

## HỢP CHẤT VÒNG

### 10. Benzen (C₆H₆)

```latex
% Vòng benzen với liên kết đôi xen kẽ
\chemfig{*6(=-=-=-)}

% Vòng benzen với vòng tròn bên trong (biểu diễn cộng hưởng)
\chemfig{**6(------)}
```

### 11. Benzen với H hiển thị

```latex
\chemfig{*6(-H=-H=-H=-H=-H=-H)}
```

### 12. Toluen (C₆H₅CH₃)

```latex
\chemfig{*6(=-=(-CH_3)-=-)}
```

### 13. Xilen (C₆H₄(CH₃)₂)

```latex
% ortho-Xilen (1,2)
\chemfig{*6(=-(-CH_3)=(-CH_3)-=-)}

% meta-Xilen (1,3)
\chemfig{*6(=-=(-CH_3)=-(-CH_3)=)}

% para-Xilen (1,4)
\chemfig{*6(=-=(-CH_3)-=-(-CH_3))}
```

### 14. Naphtalen (C₁₀H₈)

```latex
\chemfig{*6(=-=(-*6(=-=-=-))-=-)}
```

### 15. Xiclohexan (C₆H₁₂)

```latex
\chemfig{*6(------)}
```

---

## ANCOL - PHENOL - ETE

### 16. Metanol (CH₃OH)

```latex
\chemfig{H-C(-[2]H)(-[6]H)-O-H}
% Hoặc:
\chemfig{H_3C-OH}
```

### 17. Etanol (C₂H₅OH)

```latex
\chemfig{H-C(-[2]H)(-[6]H)-C(-[2]H)(-[6]H)-O-H}
% Hoặc:
\chemfig{H_3C-CH_2-OH}
```

### 18. Propan-1-ol và Propan-2-ol

```latex
% Propan-1-ol
\chemfig{H_3C-CH_2-CH_2-OH}

% Propan-2-ol (isopropanol)
\chemfig{H_3C-CH(-[6]OH)-CH_3}
```

### 19. Glixerol (C₃H₅(OH)₃)

```latex
\chemfig{HO-CH_2-CH(-[6]OH)-CH_2-OH}
```

### 20. Phenol (C₆H₅OH)

```latex
\chemfig{*6(=-=(-OH)-=-)}
```

### 21. Đimetyl ete (CH₃OCH₃)

```latex
\chemfig{H_3C-O-CH_3}
```

### 22. Đietyl ete (C₂H₅OC₂H₅)

```latex
\chemfig{H_3C-CH_2-O-CH_2-CH_3}
```

---

## ANĐEHIT - XETON - AXIT

### 23. Fomanđehit (HCHO)

```latex
\chemfig{H-C(=[2]O)-H}
```

### 24. Axetanđehit (CH₃CHO)

```latex
\chemfig{H_3C-C(=[2]O)-H}
```

### 25. Axeton (CH₃COCH₃)

```latex
\chemfig{H_3C-C(=[2]O)-CH_3}
```

### 26. Axit fomic (HCOOH)

```latex
\chemfig{H-C(=[2]O)-O-H}
```

### 27. Axit axetic (CH₃COOH)

```latex
\chemfig{H_3C-C(=[2]O)-O-H}
```

### 28. Axit benzoic (C₆H₅COOH)

```latex
\chemfig{*6(=-=(-C(=[2]O)-OH)-=-)}
```

---

## ESTE - CHẤT BÉO

### 29. Metyl fomat (HCOOCH₃)

```latex
\chemfig{H-C(=[2]O)-O-CH_3}
```

### 30. Etyl axetat (CH₃COOC₂H₅)

```latex
\chemfig{H_3C-C(=[2]O)-O-CH_2-CH_3}
```

### 31. Metyl axetat (CH₃COOCH₃)

```latex
\chemfig{H_3C-C(=[2]O)-O-CH_3}
```

---

## AMIN - AMINO AXIT

### 32. Metylamin (CH₃NH₂)

```latex
\chemfig{H_3C-N(-[2]H)-H}
% Hoặc:
\chemfig{H_3C-NH_2}
```

### 33. Đimetylamin ((CH₃)₂NH)

```latex
\chemfig{H_3C-N(-[2]H)-CH_3}
```

### 34. Anilin (C₆H₅NH₂)

```latex
\chemfig{*6(=-=(-NH_2)-=-)}
```

### 35. Glyxin (H₂N-CH₂-COOH)

```latex
\chemfig{H_2N-CH_2-C(=[2]O)-OH}
```

### 36. Alanin (CH₃-CH(NH₂)-COOH)

```latex
\chemfig{H_3C-CH(-[6]NH_2)-C(=[2]O)-OH}
```

---

## SƠ ĐỒ PHẢN ỨNG

### 37. Phản ứng đơn giản

```latex
\schemestart
\chemfig{CH_4} \+ \chemfig{Cl_2}
\arrow{->[\text{as}]}
\chemfig{CH_3Cl} \+ \chemfig{HCl}
\schemestop
```

### 38. Phản ứng với điều kiện

```latex
\schemestart
\chemfig{C_2H_4} \+ \chemfig{H_2O}
\arrow{->[$H^+$][$t^\circ$]}
\chemfig{C_2H_5OH}
\schemestop
```

### 39. Phản ứng thuận nghịch

```latex
\schemestart
\chemfig{N_2} \+ 3\chemfig{H_2}
\arrow{<=>[$t^\circ,p$][$\text{Fe}$]}
2\chemfig{NH_3}
\schemestop
```

### 40. Chuỗi phản ứng

```latex
\schemestart
\chemfig{CH_4}
\arrow{->[\chemfig{Cl_2}][as]}
\chemfig{CH_3Cl}
\arrow{->[\chemfig{NaOH}][$t^\circ$]}
\chemfig{CH_3OH}
\arrow{->[\chemfig{CuO}][$t^\circ$]}
\chemfig{HCHO}
\schemestop
```

### 41. Sơ đồ phản ứng bằng TikZ thuần

```latex
\begin{tikzpicture}[
    chem/.style={draw, rounded corners, minimum height=0.8cm, minimum width=1.2cm, font=\small},
    arr/.style={->, >=Stealth, thick}
]
    \node[chem] (a) at (0,0) {$\mathrm{CH_4}$};
    \node[chem] (b) at (3,0) {$\mathrm{CH_3Cl}$};
    \node[chem] (c) at (6,0) {$\mathrm{CH_3OH}$};
    \node[chem] (d) at (9,0) {$\mathrm{HCHO}$};
    
    \draw[arr] (a) -- node[above, font=\scriptsize] {$+\mathrm{Cl_2}$} 
                      node[below, font=\scriptsize] {as} (b);
    \draw[arr] (b) -- node[above, font=\scriptsize] {$+\mathrm{NaOH}$} (c);
    \draw[arr] (c) -- node[above, font=\scriptsize] {$+\mathrm{CuO}$} 
                      node[below, font=\scriptsize] {$t^\circ$} (d);
\end{tikzpicture}
```

---

## POLIME

### 42. Polyetilen (PE)

```latex
\chemfig{-[@{op,.75}]CH_2-CH_2-[@{cl,.25}]}
\polymermark{op}{cl}{n}
```

### 43. Polyvinyl clorua (PVC)

```latex
\chemfig{-[@{op,.75}]CH_2-CH(-[6]Cl)-[@{cl,.25}]}
\polymermark{op}{cl}{n}
```

### 44. Polipropilen (PP)

```latex
\chemfig{-[@{op,.75}]CH_2-CH(-[6]CH_3)-[@{cl,.25}]}
\polymermark{op}{cl}{n}
```

### 45. Polistiren (PS)

```latex
\chemfig{-[@{op,.75}]CH_2-CH(-[6]*6(=-=-=-))-[@{cl,.25}]}
\polymermark{op}{cl}{n}
```

---

## MẸO VÀ LƯU Ý

### Rút gọn công thức

```latex
% Thay vì viết đầy đủ H
\chemfig{H_3C-CH_2-OH}  % Tốt hơn
\chemfig{H-C(-[2]H)(-[6]H)-C(-[2]H)(-[6]H)-O-H}  % Chi tiết
```

### Điều chỉnh kích thước

```latex
% Nhỏ hơn
\chemfig[atom sep=1.5em]{H_3C-CH_2-OH}

% Lớn hơn
\chemfig[atom sep=2.5em]{H_3C-CH_2-OH}
```

### Màu sắc

```latex
\chemfig{H_3C-\textcolor{red}{C}(=[2]\textcolor{blue}{O})-OH}
```

### Đánh số carbon

```latex
\chemfig{
    \chembelow{C}{1}H_3
    -\chembelow{C}{2}H_2
    -\chembelow{C}{3}H_2
    -\chembelow{C}{4}H_3
}
```
