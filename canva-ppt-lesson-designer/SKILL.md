---
name: canva-ppt-lesson-designer
description: Plan and design educational PowerPoint or Canva lesson decks slide by slide with detailed Vietnamese guidance and English search keywords. Use when a user wants to build a teaching presentation, lecture PPT, classroom slide deck, lesson visual plan, or needs per-slide suggestions for titles, core content, layouts, images, icons, videos, colors, fonts, interaction, speaker notes, accessibility, and preparation checklists.
---

# Canva PPT Lesson Designer

Viet toan bo phan huong dan, giai thich, goi y, ghi chu va cau truc bai giang bang tieng Viet.
Chi dung tieng Anh cho:
- tu khoa tim kiem
- cum tim kiem copy-paste
- ten phong cach hoac loai tai nguyen khi can giu nguyen de tra cuu

## Khi yêu cầu chưa đủ cụ thể — PHẢN BIỆN TRƯỚC, LÀM SAU

Yêu cầu chung chung luôn cho ra sản phẩm kém. **Không đoán bừa, cũng không hỏi
lể tể từng ý.** Hãy nêu rõ đang thiếu gì, rồi đưa **một prompt mẫu đã điền sẵn
giá trị mặc định hợp lý** để người dùng sửa và gửi lại trong đúng một lượt.

Thiếu từ **2 tiêu chí trở lên** thì bắt buộc phản biện. Thiếu **đúng 1** tiêu chí
thì tự chọn mặc định, làm tiếp, và nói rõ đã chọn gì.

**Tiêu chí bắt buộc:** môn · lớp · bài/chủ đề · số slide · thời lượng tiết · phong cách thiết kế

**Mẫu phản biện:**

> Yêu cầu hiện thiếu: **số slide**, **phong cách thiết kế**. Nếu làm luôn thì tôi phải đoán, dễ lệch
> ý bạn. Bạn copy prompt dưới đây, sửa chỗ in đậm rồi gửi lại:
>
> ```
> Thiết kế deck bài giảng môn **KHTN** lớp **8**,
> bài **Định luật bảo toàn khối lượng**.
> Số slide: **12** · Thời lượng: **1 tiết 45 phút**
> Phong cách: **tối giản, nền sáng, nhiều hình minh hoạ, ít chữ**
> Đối tượng: **học sinh đại trà** · Ngôn ngữ slide: **tiếng Việt**
> ```

---

## Muc tieu cua skill

- Bien chu de bai giang thanh ke hoach thiet ke PPT hoac Canva hoan chinh.
- Dam bao moi slide deu co huong dan chi tiet, khong chi liet ke tieu de.
- Ket hop logic su pham voi goi y thiet ke truc quan.
- Tao bo tu khoa tieng Anh du rong de tim hinh, icon, vector, video, background va layout.
- Luu ket qua thanh file Markdown de tai su dung.

## Design systems

Khi nguoi dung yeu cau design system cu the hoac bai giang thuoc KHTN / EduTechND,
chon dung system tuong ung. Doc chi tiet trong `references/styles/`.

| System | Vibe | Best for |
|---|---|---|
| **Editorial Minimalist** | NYT / Atlantic, whitespace tu tin | Phan tich, bao cao, tu duy lanh dao |
| **Silicon Modern** | Stripe / Linear, toi cao cap | Tech, SaaS, AI/ML |
| **Keynote Clean** | Apple big-reveal | Pitch, keynote, cong bo |
| **Academic Editorial** | Giang duong dai hoc, trang nghiem | Giao duc, bai giang STEM, dai hoc |
| **Bold Magazine** | Tap chi sang tao, mau manh | Marketing, brand, van hoa |
| **Scientific Data** | Bieu do la chinh, chinh xac | Phan tich, tai chinh, du lieu |
| **Warm Human** | Tong am, hinh anh la chinh | Phi loi nhuan, cong dong, K-12 |
| **EduTechND Earth (Dark)** | Nen toi vang dat, thuong hieu EduTechND | KHTN THCS, GDPT 2018, bai giang nen toi |

Khi khong chac: mac dinh **Academic Editorial** (dai hoc / THPT) hoac **EduTechND Earth** (THCS KHTN).
Khi nguoi dung nhac "EduTechND", "nen toi", "vang dat", "KHTN THCS" → chon **EduTechND Earth (Dark)**.

## Design anchors (ap dung cho moi system)

**Slide canvas.** Mac dinh 16:9 `Inches(13.333) x Inches(7.5)`. Voi EduTechND Earth: `Inches(20) x Inches(11.25)`. Margin toi thieu 0.5" moi ben.

**Phan cap typography.** Mac dinh: Title 36-54pt bold, Section 22-28pt bold, Body 14-18pt regular, Caption 10-12pt muted. Voi EduTechND Earth (canvas 20"): Section 63-95pt, Title 44-72pt, Body 36pt, Caption 24-28pt. Dung do dam (bold vs regular) truoc khi dung mau / kich thuoc. Ti le size giua cac tang >= 1.3x.

**Tuong phan font.** Ket hop sans-serif (khong chan) voi serif (co chan) tao phan cap ro: heading dung font cung (Noto Sans Bold), sub-heading dung font trang nghiem (Noto Serif Bold), body dung font mem (9Slide). KHONG dung cung 1 font/style cho heading va body. Heading LUON bold, body LUON regular — chi bold cum can nhan trong body. Doc chi tiet "Nghe thuat sep chu" trong `references/styles/edutechnd-earth-dark.md`.

**Vai tro mau.** Dominant (60-70% dien tich, thuong la nen). Supporting (1-2 tone hoa hop). Accent (1 mau noi bat, dung it — tieu de, so lieu, 1 shape). Khong bao gio chia deu mau.

**Nhip khoang cach.** Chon 0.3" hoac 0.5" lam don vi gap, dung nhat quan xuyen suot.

**Mot motif cho ca deck.** Moi style file dinh nghia mot yeu to lap lai (thanh doc mong, icon trong hinh tron, so lon...). Ap dung tren moi content slide.

## Quy trinh lam viec

### 1. Thu thap thong tin toi thieu

Neu nguoi dung chua cung cap du, hay hoi ngan gon cac thong tin quan trong nhat:
- mon hoc
- ten bai hoac chu de cu the
- lop hoac nhom doi tuong hoc sinh
- thoi luong bai day
- muc tieu hoc tap chinh
- yeu cau dac biet ve phong cach, muc do, hoac tai nguyen

Neu da co du ngu canh de lam tiep:
- chu dong dua ra gia dinh hop ly
- neu ro gia dinh trong phan mo dau
- khong dung lai chi de hoi them neu van co the tao ban dau tien huu ich

### 2. Phan tich bai giang

- Tach noi dung thanh cac phan kien thuc logic.
- Xac dinh trong tam, diem kho, cho can minh hoa truc quan.
- Goi y so luong slide theo thoi luong:
- 20-30 phut: khoang 6-8 slide
- 35-45 phut: khoang 8-12 slide
- 60 phut tro len: khoang 12-18 slide

### 3. Dung cau truc bai giang

Uu tien cau truc chuan sau va linh hoat dieu chinh theo mon hoc:
- Slide mo dau
- Slide muc tieu hoc tap
- Slide kien thuc nen hoac goi nho
- Nhom slide noi dung chinh
- Slide vi du hoac luyen tap
- Slide tong ket
- Slide ket thuc hoac giao nhiem vu

### 4. Thiet ke chi tiet tung slide

Bat buoc mo ta chi tiet cho tung slide. Moi slide phai co du cac muc sau:

- `Muc dich slide`
- `Noi dung chinh`
- `Bo cuc de xuat`
- `Goi y hinh anh`
- `Goi y video` hoac neu ro `Khong can video`
- `Mau sac va font`
- `Hoat dong tuong tac` hoac neu ro `Khong bat buoc`
- `Ghi chu giang vien`

### 5. Tong hop tai nguyen va luu file

- Tong hop checklist hinh anh, video va tai nguyen bo sung o cuoi.
- Luu toan bo dau ra vao file `.md` trong workspace hien tai neu nguoi dung khong chi dinh noi khac.
- Dung ten file theo mau:
`tai_nguyen_thiet_ke_bai_giang_[ten_bai_giang]_[mon-lop].md`
- Chuan hoa ten file:
- viet thuong
- bo dau tieng Viet
- thay khoang trang va dau cau bang `_`
- gom cac dau gach duoi lap lai
- dung nhan mon-lop ngan gon nhu `khtn-6`, `toan-8`, `ngu_van-9`

## Quy tac noi dung

- Moi slide chi giu mot y chinh noi bat.
- Toi da khoang 6-7 dong noi dung trinh bay tren slide.
- Uu tien gach dau dong, tranh doan van dai.
- Chi de xuat video khi video that su giup tang hieu bai.
- Luon nhac toi phuong an du phong neu kho tim dung tai nguyen.
- Voi bai giang tieng Viet, tuyet doi khong viet doan huong dan dai bang tieng Anh.

## Quy tac thiet ke

### Ve van ban

- Font hien thi nen de doc, toi thieu 24pt neu la slide trinh chieu.
- Tach ro tieu de, y chinh, va vi du.
- Tranh nhoi qua nhieu chu vao mot slide.

### Ve hinh anh

- Hinh phai lien quan truc tiep den noi dung cua slide.
- Uu tien anh ro net, sang, de nhin khi chieu lop hoc.
- Neu khong tim duoc anh phu hop, de xuat icon, so do hoac infographic thay the.

### Ve video

- Uu tien video ngan, truc tiep, de chen vao bai day.
- Neu ro thoi luong, nguon, cach dung va luu y ky thuat.
- Goi y phu de hoac mo ta thay the khi phu hop.

### Ve mau sac

- Thuong chi dung 2-3 mau chu dao (hoac 4 mau voi EduTechND Earth).
- Giu tuong phan tot giua chu va nen.
- Goi y mau theo tinh chat mon hoc neu phu hop.
- Voi EduTechND Earth: chi dung dung mau trong palette ANKENE (#3F2313, #D7A550, #D28119, #FCFBF9, #F2F3EC, #75502C, #6A4115), accent < 10% dien tich.

## Cau truc dau ra bat buoc

Luon to chuc cau tra loi theo khung sau:

### 1. Thong tin chung

- Mon hoc
- Chu de bai giang
- Doi tuong hoc sinh
- Thoi luong
- So luong slide de xuat
- Design system duoc chon (neu ap dung)
- Gia dinh dang dung, neu co

### 2. Muc tieu hoc tap

- Liet ke 3-5 muc tieu ngan gon, do duoc neu co the.

### 3. Cau truc bai giang theo tung slide

Voi moi slide, dung dinh dang sau:

#### Slide X: [Tieu de slide]

**Muc dich slide**
- Neu slide nay dung de dan nhap, giai thich, luyen tap, tong ket hay chuyen y.

**Noi dung chinh**
- Liet ke 3-6 y cot loi se hien thi tren slide.

**Bo cuc de xuat**
- Mo ta layout cu the nhu 1 cot, 2 cot, anh nen toan man hinh, anh ben trai chu ben phai, so do o giua, the thong tin...
- Neu dung EduTechND Earth: chi ro layout nao trong 6 mau (Title, Single Concept, Comparison, Process, Big Number, Quote).

**Goi y hinh anh**
- Loai tai nguyen: anh thuc, icon, vector, infographic, so do, bieu do...
- Mo ta anh can tim bang tieng Viet.
- Tu khoa tim kiem bang tieng Anh, it nhat 5 cum.
- Nguon goi y: Canva, Unsplash, Pexels, Pixabay, Freepik, YouTube thumbnail stills neu phu hop.
- Vi tri de xuat tren slide.
- Kich thuoc tuong doi.
- Alt text ngan bang tieng Viet.
- Phuong an thay the neu khong tim ra anh dung y.

**Goi y video**
- Neu khong can, ghi ro `Khong can video`.
- Neu can, neu:
- loai video
- muc dich su dung
- thoi luong phu hop
- tu khoa tim kiem bang tieng Anh
- nguon de xuat
- cach dung trong lop
- luu y ky thuat va ban quyen

**Mau sac va font**
- Goi y 2-3 huong mau (hoac chi ro 4 mau EduTechND neu ap dung system do).
- Goi y nhom font hoac phong cach font, khong can khoa cung neu nguoi dung chua yeu cau.
- Voi EduTechND Earth: BAT BUOC dung font 9Slide, chon theo do dai chuoi text.

**Hoat dong tuong tac**
- Cau hoi nhanh, thao luan, doan hinh, keo tha, so sanh, bai tap nhom...
- Neu khong bat buoc, ghi ro `Khong bat buoc`.

**Ghi chu giang vien**
- Neu diem nhan khi noi, loi hoc sinh hay gap, hoac meo chuyen sang slide sau.

---

### 4. Checklist chuan bi

- Hinh anh can tim
- Video can tim
- Icon hoac so do can tao
- Tai lieu bo sung neu co

### 5. Goi y hoan thien bai giang

- Goi y chuyen tiep giua cac slide
- Goi y nhip trinh bay
- Luu y ban quyen, ky thuat, kha nang trinh chieu

## Quy tac tu khoa

- Tat ca tu khoa tim kiem phai bang tieng Anh.
- Khong dung cac tu khoa qua chung chung nhu `beautiful image` hoac `nice video`.
- Uu tien tu khoa 2-6 tu va du ngu canh.
- Voi moi slide, uu tien tach nhom tu khoa theo:
- hinh anh chinh
- icon hoac yeu to bo tro
- background
- video neu co

## Khi can mo rong tim kiem

Doc [references/keyword-expansion-framework.md](references/keyword-expansion-framework.md) de mo rong tu khoa theo style, doi tuong, hanh dong, bo cuc va loai tai nguyen.

Doc [references/slide-design-framework.md](references/slide-design-framework.md) de chon mau cau truc slide, bo cuc su pham va cach phan vai hinh anh, van ban, hoat dong.

## File map

- `SKILL.md` — file chinh, huong dan tong quat va quy trinh
- `references/styles/edutechnd-earth-dark.md` — design system EduTechND Earth (Dark)
- `references/keyword-expansion-framework.md` — khung mo rong tu khoa
- `references/slide-design-framework