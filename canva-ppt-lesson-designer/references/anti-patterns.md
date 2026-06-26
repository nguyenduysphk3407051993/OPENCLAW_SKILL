# Anti-Patterns

Cac loi thiet ke thuong gap lam slide tro nen nghiep du hoac "nhu AI lam". Danh sach nay
ap dung chung cho moi design system, voi phan bo sung rieng cho EduTechND Earth (Dark).

## Category 1: Loi trang tri thua

### Duong accent duoi tieu de
Duong ke ngang mau ngay duoi moi tieu de slide. Dau hieu nhan dien slide AI ro nhat.
**Thay bang:** Khoang trang 0.5-0.8". Neu can tach, dung nen mau nhe cho vung tieu de.

### Thanh mau day tren/duoi slide
Hinh chu nhat mau trai dai toan bo top/bottom moi slide, thuong co logo hoac tieu de.
**Thay bang:** Tieu de dat cung vung noi dung. So trang o goc la du.

### Dai ruy-bang doc canh
Thanh mau doc o canh trai/phai, giong nhau moi slide.
**Thay bang:** Mot yeu to accent moi slide, bien doi. Hoac khong co gi.

### Bevel, shadow, gradient kieu Office 2007
Shape co bong do, canh vat, gradient mac dinh.
**Thay bang:** Fill phang. Neu can tach, dung khoang trang hoac vien mong 0.5pt mau muted.

## Category 2: Loi mau sac

### Nen kem / be mac dinh
`F5F5DC`, `FAF0E6`, `FAEBD7` dung lam nen khong co ly do. Doc cu ky nhat la 2010.
**Thay bang:** Trang (#FFFFFF) hoac toi cam ket theo style. Voi EduTechND Earth: #3F2313.

### Xanh Office mac dinh
Dung `4472C4` cho accent bat ke chu de gi.
**Thay bang:** Chon palette tu style file phu hop chu de.

### Moi mau deu nhu nhau
5 mau dung deu, khong mau nao noi bat.
**Thay bang:** 60% dominant, 30% supporting, 10% accent.

### Tuong phan thap
Chu xam nhat tren nen trang, hoac chu toi tren nen toi.
**Thay bang:** Body text phai doc duoc cach xa. Muted chi cho caption.

## Category 3: Loi bo cuc

### Moi slide deu la tieu de + 3 bullet
Cung mot khung xuyen suot.
**Thay bang:** Bien doi: stat callout, quote, hinh anh, grid, 2 cot.

### Canh giua doan van
Body text va bullet canh giua.
**Thay bang:** Canh trai. Chi tieu de, so lon, ket luan moi canh giua.

### Nhoi sat 4 canh
Text cham 0.1-0.2" tu canh slide.
**Thay bang:** Margin toi thieu 0.5" moi canh. Thuong 0.75" tren va 2 ben.

## Category 4: Loi font

### Calibri toan bo
Mac dinh body font khong ghep voi header font co ca tinh.
**Thay bang:** Ghep header font (Georgia, Cambria) voi body font (Calibri).

### Tieu de va section cung kich thuoc
Tuong phan kich thuoc yeu.
**Thay bang:** Title 36-54pt, section 22-28pt, body 14-18pt. Phan cap phai ro.

## Category 5: Tran chu

### Text tran ra ngoai shape
Noi dung chay qua day textbox hoac ra canh slide.
**Fix:** Do → giam font 2pt, hoac tach slide, hoac mo rong box. Khong bao gio xuat ban khi tran.

---

## Category DAC BIET: Loi rieng voi EduTechND Earth (Dark)

### LOI 1: Nen sang mac dinh
Dung nen trang hoac kem nhac khi design system yeu cau nen toi #3F2313.
**Fix:** LUON set slide background = #3F2313. Khong bao gio de nen sang voi system nay.

### LOI 2: Dung sai font — thay 9Slide bang Calibri/Cambria/Arial
Font 9Slide la nhan dien thuong hieu. Thay font khac = mat nhan dien.
**Fix:** Chi dung font 9Slide + Noto Sans Bold / Noto Serif Bold theo bang:
- Section title: `Noto Sans Bold` (63-95pt)
- Slide title: `#9Slide01 Tieu de ngan` hoac `#9Slide02 Tieu de dai` (44-72pt)
- Sub-heading: `Noto Serif Bold` (40-46pt)
- Body ngan: `#9Slide01 Noi dung ngan` (28-32pt)
- Body dai: `#9Slide02 Noi dung dai` (36pt)
Chon theo do dai chuoi text, khong mac dinh Calibri.

### LOI 3: Accent #D28119 qua nhieu
Dung mau cam/accent cho toan bo tieu de, vien, icon. Vi pham quy tac < 10%.
**Fix:** Accent chi cho 1 chi tiet nhan moi slide: 1 tu khoa, 1 so lieu, 1 thanh nho.
Tieu de section dung #F2F3EC (ink_light2), khong phai accent.

### LOI 4: Them mau ngoai bang mau thuong hieu
Them xanh duong, do, xanh la... vao slide EduTechND Earth.
**Fix:** Chi dung mau trong palette: #3F2313, #D7A550, #D28119, #FCFBF9, #F2F3EC, #75502C, #6A4115.
Neu can phan biet them → dung opacity (70%, 50%) cua ink.

### LOI 5: Dung cung kieu font cho title va body
Ca title lan body deu dung serif hoac deu sans-serif, hoac cung 1 font cho moi tang.
**Fix:** BAT BUOC tuong phan:
- Headline: Noto Sans Bold (sans cung, 63-95pt bold)
- Sub-heading: Noto Serif Bold (serif trang nghiem, 40-46pt bold)
- Body: 9Slide02 Noi dung dai (sans mem, 36pt regular)
- Caption: 9Slide01 Noi dung ngan (sans nhe, 24-28pt regular)
Ti le size giua cac tang phai >= 1.3x. Doc "Nghe thuat sep chu" trong style file.

### LOI 5b: Bold toan bo body text
Boi dam ca doan van → mat trong luong thi giac, moi thu deu quan trong = khong gi quan trong.
**Fix:** Chi heading BOLD, body REGULAR.