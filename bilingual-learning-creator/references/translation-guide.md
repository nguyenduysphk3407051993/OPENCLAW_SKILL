# Cẩm nang dịch song ngữ Việt–Anh
<!-- Translation Guide — dùng nội bộ cho AI agent -->
<!-- Phục vụ chức năng "dịch phân tích từng câu" của bilingual-learning-creator -->
<!-- Ngữ cảnh: giáo viên phổ thông Việt Nam dạy học sinh THCS–THPT -->

---

## HƯỚNG DẪN ĐỌC

- Mục 1: Cấu trúc khác biệt Việt–Anh — đọc để hiểu "tại sao không dịch từng chữ"
- Mục 2: Quy trình dịch 4 bước — agent theo từng bước khi xử lý câu người dùng đưa vào
- Mục 3: Bảng dịch so sánh — kho mẫu 15+ cặp, dùng khi soạn tài liệu hoặc giải thích cho GV
- Mục 4: Cách chú giải một câu dịch — format chuẩn khi agent phân tích từng câu
- Mục 5: Bẫy dịch văn bản khoa học — số liệu, đơn vị, thuật ngữ hai nghĩa

---

## 1. KHÁC BIỆT CẤU TRÚC VIỆT–ANH

> Đây là lý do dịch máy từng chữ luôn cho kết quả gượng hoặc sai. Agent cần áp dụng các nguyên tắc này TRƯỚC khi dịch.

---

### 1.1 Tiếng Việt không chia thì — tiếng Anh bắt buộc chọn thì

**Tiếng Việt** không có hình thái chia động từ theo thời gian. Người nghe suy ra thời gian từ **trạng từ** (*hôm qua, đang, sẽ, vừa*) hoặc **ngữ cảnh**.

**Tiếng Anh** bắt buộc chọn thì ngay trong hình thái động từ, dù đã có trạng từ.

| Tiếng Việt | Manh mối thì | Tiếng Anh đúng |
|---|---|---|
| Hôm qua tôi học bài. | *hôm qua* → quá khứ xác định | *Yesterday I studied.* |
| Nước sôi ở 100°C. | sự thật khoa học → hiện tại đơn | *Water boils at 100°C.* |
| Chúng tôi đang tiến hành thí nghiệm. | *đang* → đang diễn ra | *We are conducting the experiment.* |
| Tôi vừa tìm ra kết quả. | *vừa* → vừa xảy ra | *I have just found the result.* |

**Cách suy ra thì đúng từ trạng từ chỉ thời gian:**

| Trạng từ tiếng Việt | Thì tiếng Anh |
|---|---|
| hôm qua, năm ngoái, vào năm..., lúc đó | Quá khứ đơn (Simple Past) |
| vừa, mới, vừa mới | Hiện tại hoàn thành (Present Perfect) + *just* |
| từ trước đến nay, đã từng | Hiện tại hoàn thành + *ever/never* |
| từ năm... đến nay | Hiện tại hoàn thành + *since* |
| sẽ, sắp | Tương lai đơn (*will*) hoặc *be going to* |
| đang | Thì tiếp diễn tương ứng |
| mỗi ngày, thường xuyên, luôn | Hiện tại đơn |
| quy luật / sự thật (không có trạng từ) | Hiện tại đơn |

---

### 1.2 Tiếng Việt không có mạo từ và không đánh dấu số nhiều

Tiếng Việt phân biệt số nhiều qua **từ chỉ lượng** (*những, các, vài*) hoặc ngữ cảnh, không qua biến tố từ. Tiếng Anh dùng **mạo từ a/an/the** và **đuôi -s/-es**.

| Câu tiếng Việt | Cạm bẫy | Câu tiếng Anh đúng |
|---|---|---|
| Tế bào là đơn vị cơ bản của sự sống. | lần đầu đề cập, số ít | *A cell is the basic unit of life.* |
| Tế bào có màng bao quanh. | đã nhắc đến → *the* | *The cell has a membrane surrounding it.* |
| Nguyên tử rất nhỏ. | khái niệm chung, số nhiều → không mạo từ | *Atoms are very small.* |
| Ba nguyên tử hydrogen kết hợp... | số lượng cụ thể → không mạo từ | *Three hydrogen atoms combine...* |

**Bảng tra nhanh mạo từ trong câu khoa học:**

| Tình huống | Mạo từ | Ví dụ |
|---|---|---|
| Danh từ đếm được, số ít, lần đầu nhắc đến | a / an | *an atom, a reaction* |
| Đã nhắc đến hoặc cả hai bên đều biết | the | *the atom (vừa nêu), the Sun* |
| Số nhiều / không đếm được, nghĩa tổng quát | (không) | *Metals conduct electricity.* |
| Tên nguyên tố, chất hóa học | (không) | *Oxygen reacts with iron.* |

---

### 1.3 Trật tự tính từ và danh từ ngược nhau

Tiếng Việt: **danh từ + bổ ngữ** (*dung dịch axit loãng*)
Tiếng Anh: **tính từ + danh từ** (*dilute acid solution*)

| Tiếng Việt | Dịch sát (SAI) | Dịch đúng |
|---|---|---|
| axit loãng | acid dilute | dilute acid |
| dung dịch muối bão hòa | solution salt saturated | saturated salt solution |
| ống nghiệm thủy tinh nhỏ | tube glass small | small glass test tube |
| thí nghiệm đơn giản và rẻ tiền | experiment simple cheap | a simple, inexpensive experiment |

Khi có nhiều tính từ, áp dụng quy tắc thứ tự: **Đánh giá → Kích thước → Hình dạng → Màu → Xuất xứ → Vật liệu → Mục đích + Danh từ**.

---

### 1.4 Tiếng Việt thích chủ động và câu không chủ ngữ; tiếng Anh khoa học thích bị động

Câu khoa học tiếng Anh (đặc biệt báo cáo thí nghiệm) dùng **bị động** để tránh nêu chủ thể và để nhấn mạnh quy trình.

| Tiếng Việt | Chủ động (thường dùng) | Bị động (tiêu chuẩn học thuật) |
|---|---|---|
| Chúng tôi đun nóng dung dịch đến 80°C. | *We heated the solution to 80°C.* | *The solution was heated to 80°C.* |
| Người ta tiến hành thí nghiệm vào năm 2020. | *They conducted the experiment in 2020.* | *The experiment was conducted in 2020.* |
| Thêm 5 mL axit vào cốc. | *Add 5 mL of acid to the beaker.* | *5 mL of acid is added to the beaker.* |

**Câu không chủ ngữ trong tiếng Việt** phải thêm chủ ngữ khi dịch sang tiếng Anh:

| Tiếng Việt | Lỗi hay mắc | Đúng |
|---|---|---|
| Đun nóng 10 phút, rồi lọc. | *Heat 10 minutes, then filter.* | *Heat the mixture for 10 minutes, then filter it.* |
| Kết luận: nhiệt độ ảnh hưởng đến tốc độ phản ứng. | *Conclusion: temperature affects...* | *In conclusion, temperature affects the rate of reaction.* |

---

### 1.5 Đại từ xưng hô và quan hệ họ hàng không ánh xạ 1-1

Tiếng Việt có hệ thống đại từ xưng hô phức tạp theo quan hệ xã hội: *tôi, mình, em, con, tớ, chúng ta, chúng tôi, mình, chúng mình*...

Tiếng Anh chỉ có **I / we / you / they**. Khi dịch:

| Tiếng Việt | Ngữ cảnh | Tiếng Anh |
|---|---|---|
| Chúng ta làm thí nghiệm. | GV và HS cùng làm (bao gồm người nghe) | *We do the experiment.* |
| Chúng tôi đã thu được kết quả. | Nhóm báo cáo (không bao gồm người nghe) | *We obtained the results.* |
| Em không hiểu ạ. | HS nói với GV | *I don't understand.* |
| Thầy có thể giải thích không? | HS hỏi GV | *Could you explain that, please?* |

Tên gọi quan hệ như *bác sĩ Smith, cô giáo Lan* → trong tiếng Anh dùng **Dr Smith, Ms Lan** hoặc chỉ **she/he**.

---

### 1.6 Câu ghép dài tiếng Việt — nên tách câu trong tiếng Anh

Tiếng Việt thường nối nhiều mệnh đề bằng dấu phẩy hoặc từ nối ngắn. Tiếng Anh học thuật ưu tiên câu ngắn, rõ ràng.

| Tiếng Việt (1 câu dài) | Cách dịch tự nhiên hơn (tách câu) |
|---|---|
| Khi nhiệt độ tăng, các phân tử dao động mạnh hơn, va chạm thường xuyên hơn, làm tốc độ phản ứng tăng lên. | *As temperature rises, the molecules vibrate more vigorously. They collide more frequently, which increases the rate of reaction.* |
| Quang hợp xảy ra ở lục lạp, cần ánh sáng mặt trời, nước và CO₂ để tổng hợp glucose và thải ra O₂. | *Photosynthesis occurs in chloroplasts. It requires sunlight, water, and CO₂ to produce glucose, releasing oxygen as a by-product.* |

---

## 2. QUY TRÌNH DỊCH 4 BƯỚC

> Agent thực hiện theo đúng thứ tự này khi được yêu cầu dịch một câu từ tiếng Việt sang tiếng Anh hoặc ngược lại.

---

### Bước 1 — Xác định thì và thể

- Tìm trạng từ chỉ thời gian trong câu (xem bảng 1.1).
- Nếu không có trạng từ: xét ngữ cảnh (sự thật khoa học → hiện tại đơn; kể lại thí nghiệm → quá khứ đơn; báo cáo → bị động).
- Xác định câu chủ động hay bị động theo văn phong (học thuật → ưu tiên bị động; hội thoại → chủ động).

### Bước 2 — Xác định chủ ngữ thật

- Câu tiếng Việt không chủ ngữ → thêm chủ ngữ phù hợp (*the mixture, the solution, students, we*).
- Câu bị động tiếng Anh → chủ ngữ là đối tượng chịu tác động, không phải tác nhân.
- Cẩn thận với câu *It is...* (chủ ngữ hình thức) — thường dùng cho sự thật/ý kiến chung: *It is estimated that..., It is known that...*

### Bước 3 — Chọn từ vựng theo văn cảnh

- Văn bản học thuật / báo cáo khoa học: dùng từ học thuật (*conduct, obtain, analyse, demonstrate*) thay vì từ thường (*do, get, look at, show*).
- Hội thoại lớp học: dùng từ thông thường hơn, câu ngắn hơn.
- Kiểm tra nghĩa của thuật ngữ hai nghĩa trước khi dùng (xem Mục 5).

### Bước 4 — Rà lại mạo từ, số nhiều và giới từ

Sau khi có bản dịch sơ bộ, kiểm tra theo danh sách:

| Hạng mục kiểm tra | Câu hỏi |
|---|---|
| Mạo từ | Danh từ đếm được số ít có mạo từ chưa? Đã dùng trước *the* đúng chưa? |
| Số nhiều | Danh từ số nhiều có đuôi -s/-es chưa? Có dùng số nhiều bất quy tắc đúng không? |
| Giới từ | *at* nhiệt độ/tốc độ/áp suất; *in* đơn vị đo; *for* khoảng thời gian; *since* mốc thời gian |
| Động từ | Đúng thì chưa? Chia đúng ngôi chưa? Stative verb có dùng tiếp diễn không? |
| Thứ tự tính từ | Đặt tính từ trước danh từ chưa? Thứ tự đúng chưa? |

---

## 3. BẢNG "DỊCH MÁY MÓC vs DỊCH TỰ NHIÊN"

> Đây là phần có giá trị dạy học cao nhất. Dùng khi agent soạn tài liệu minh họa hoặc khi GV muốn giải thích cho HS thấy sự khác biệt.
>
> **Cột 2 (Dịch máy móc)** = dịch sát từng chữ hoặc Google Translate cơ bản.  
> **Cột 3 (Dịch tự nhiên)** = bản dịch một người bản ngữ có học thức sẽ viết.

| # | Tiếng Việt | Dịch máy móc (SAI / gượng) | Dịch tự nhiên |
|---|---|---|---|
| 1 | Nước sôi ở 100 độ C. | *Water is boiling at 100 degrees C.* | *Water boils at 100°C.* |
| 2 | Học sinh tiến hành thí nghiệm hôm qua. | *Students have conducted experiment yesterday.* | *Students conducted an experiment yesterday.* |
| 3 | Thêm axit từ từ vào dung dịch bazơ. | *Add acid slowly to base solution.* | *Add the acid slowly to the base solution.* |
| 4 | Kết quả cho thấy nhiệt độ ảnh hưởng đến tốc độ phản ứng. | *The result shows temperature affects to the reaction speed.* | *The results show that temperature affects the rate of reaction.* |
| 5 | Nguyên tử carbon có 6 proton trong hạt nhân. | *Carbon atom has 6 proton in the nucleus.* | *A carbon atom has six protons in its nucleus.* |
| 6 | Tôi vừa tìm ra câu trả lời. | *I just find out the answer.* | *I have just found out the answer.* |
| 7 | Phản ứng hoá học xảy ra khi trộn hai chất này. | *Chemical reaction happens when mix these two substances.* | *A chemical reaction occurs when these two substances are mixed.* |
| 8 | Người ta đun nóng hỗn hợp đến khi sôi. | *People heated the mixture until it boils.* | *The mixture was heated until it boiled.* |
| 9 | Cây cần ánh sáng, nước và CO₂ để quang hợp. | *The tree needs the light, the water and CO₂ for photosynthesis.* | *Plants need light, water, and CO₂ for photosynthesis.* |
| 10 | Nhiệt độ càng cao, phản ứng xảy ra càng nhanh. | *Temperature higher, reaction happens faster.* | *The higher the temperature, the faster the reaction.* |
| 11 | Em không hiểu bài hôm nay lắm. | *I don't understand lesson today much.* | *I didn't quite understand today's lesson.* |
| 12 | Chúng tôi thấy rằng kết quả phù hợp với giả thuyết. | *We see that the result is suitable with the hypothesis.* | *We found that the results were consistent with the hypothesis.* |
| 13 | Lực ma sát cản trở chuyển động của vật. | *Friction force prevents the movement of the object.* | *Friction opposes the motion of the object.* |
| 14 | Thí nghiệm này giúp học sinh hiểu rõ hơn về phản ứng hoá học. | *This experiment helps students to understand more clearly about chemical reaction.* | *This experiment helps students develop a better understanding of chemical reactions.* |
| 15 | Dung dịch đổi màu từ xanh sang đỏ khi thêm axit. | *The solution changes colour from blue to red when add acid.* | *The solution changes colour from blue to red when acid is added.* |
| 16 | Mặc dù khối lượng thay đổi, thể tích vẫn như cũ. | *Although the mass changes, volume still the same.* | *Although the mass changes, the volume remains the same.* |
| 17 | Tốc độ ánh sáng rất lớn — khoảng 300 000 km/s. | *The speed of light is very big — about 300 000 km per second.* | *The speed of light is very high — approximately 300,000 km/s.* |
| 18 | Học sinh không được chạm vào hóa chất bằng tay trần. | *Students are not allowed to touch chemicals by bare hand.* | *Students must not handle chemicals with bare hands.* |
| 19 | Kết luận: ánh sáng cần thiết cho quang hợp. | *Conclusion: light is necessary for photosynthesis.* | *In conclusion, light is essential for photosynthesis to occur.* |
| 20 | Chất xúc tác làm tăng tốc độ phản ứng mà không bị tiêu hao. | *Catalyst makes increase the reaction speed without being consumed.* | *A catalyst increases the rate of reaction without being used up.* |

---

## 4. CÁCH CHÚ GIẢI MỘT CÂU DỊCH

> Agent dùng format này khi người dùng yêu cầu "dịch và phân tích từng câu". Mỗi câu cho ra một khối chú giải gồm 5 thành phần.

---

### Format chuẩn

```
[Câu tiếng Việt gốc]
→ [Bản dịch tiếng Anh]

Thì & Cấu trúc: [tên thì + lý do chọn + cấu trúc ngữ pháp nổi bật]

Từ vựng đáng học:
  • [từ 1] /IPA/ (từ loại) — nghĩa + ghi chú nếu có
  • [từ 2] /IPA/ (từ loại) — nghĩa + ghi chú nếu có
  (tối đa 4 từ; chỉ chọn từ ở trình độ phù hợp — xem nguyên tắc bên dưới)

Cụm đáng nhớ: [cụm từ đặc biệt trong câu, giải thích tại sao không dịch từng chữ]

Lưu ý dịch: [chỉ ghi khi có điều khác biệt đáng học; bỏ trống nếu không có]
```

---

### Ví dụ áp dụng

**Câu gốc:** *Chất xúc tác làm tăng tốc độ phản ứng mà không bị tiêu hao.*

→ *A catalyst increases the rate of reaction without being used up.*

**Thì & Cấu trúc:** Hiện tại đơn — sự thật khoa học, không phụ thuộc thời gian. Cấu trúc: *without + V-ing* (sau *without* dùng danh động từ).

**Từ vựng đáng học:**
- *catalyst* /ˈkætəlɪst/ (danh từ) — chất xúc tác; lưu ý: số nhiều *catalysts*, không có *the* khi nói chung
- *rate* /reɪt/ (danh từ) — tốc độ, tỉ lệ; trong khoa học hay gặp *rate of reaction* (không nói *reaction speed*)
- *used up* /juːzd ʌp/ (phrasal verb, bị động) — bị tiêu hao hết; [tách được]: *use sth up*

**Cụm đáng nhớ:** *without being used up* — cấu trúc *without + being + V3* (bị động sau *without*). Dịch sát: "không có bị dùng hết" → tự nhiên: "without being used up".

**Lưu ý dịch:** "tiêu hao" = *used up* (hết sạch) chứ không phải *consumed* một mình — *consumed* trong hoá học thường ngụ ý phản ứng hóa học; *used up* trung tính hơn và phổ biến hơn ở THCS.

---

### Nguyên tắc chọn từ để chú giải

Chỉ chú giải từ khi đáp ứng ÍT NHẤT một tiêu chí:

| Tiêu chí | Ví dụ từ nên chú giải |
|---|---|
| Học sinh ở trình độ đó chưa chắc biết | *consistent with, opposes, approximately* |
| Từ có IPA dễ nhầm / phát âm sai | *catalyst* /ˈkætəlɪst/, *rhythm* /ˈrɪðəm/ |
| Từ học thuật thay thế từ thông thường | *obtain* (thay *get*), *demonstrate* (thay *show*) |
| Từ có nghĩa khác trong khoa học | *solution, power, volume, matter* |
| Cụm từ không thể dịch từng chữ | *used up, come up with, as a result of* |

**KHÔNG chú giải** các từ: *and, but, the, is, are, have, water, big, school, today* — quá dễ, không có giá trị dạy học.

**KHÔNG chú giải** từ quá chuyên sâu vượt trình độ người học mà không thật sự cần cho bài học đó.

---

## 5. BẪY DỊCH RIÊNG CỦA VĂN BẢN KHOA HỌC

### 5a. Số và đơn vị đo

| Quy tắc | Ví dụ đúng | Lỗi hay gặp |
|---|---|---|
| Đơn vị viết tắt không có dấu chấm (trừ đầu câu) | *25 cm, 3 kg, 100°C* | *25 cm., 3 kg.* |
| Để khoảng trắng giữa số và đơn vị (trừ °C, %) | *25 cm, 80 kJ* nhưng *37°C, 40%* | *25cm, 80kJ* |
| Số từ 1–9 viết bằng chữ trong văn xuôi; ≥ 10 viết số | *three atoms, 12 electrons* | *3 atoms, twelve electrons* |
| Số đầu câu viết bằng chữ | *Two hundred students...* | *200 students...* |
| Không dùng dấu phẩy làm dấu thập phân | *3.14* | *3,14* (sai trong tiếng Anh) |
| Nhiệt độ: *at 100°C* hoặc *at 100 degrees Celsius* | *at 100°C* | *in 100°C, on 100°C* |
| Khoảng giá trị: dùng *from ___ to ___* hoặc *between ___ and ___* | *from 20°C to 80°C* | *from 20 to 80°C* (đơn vị phải ghi ở cả hai đầu hoặc chỉ cuối nếu dùng *to*) |

### 5b. Tên nguyên tố theo IUPAC

Tham chiếu bảng đầy đủ trong `clil-science-glossary.md`, Mục "Danh pháp IUPAC". Các điểm bổ sung khi dịch:

- **Tên nguyên tố không có mạo từ** khi nói đến nguyên tố nói chung: *Oxygen is a gas at room temperature.* (không phải *The oxygen*)
- **Tên nguyên tố có mạo từ** khi nói đến mẫu cụ thể trong thí nghiệm: *Add the sodium to the water carefully.* (natri cụ thể trong thí nghiệm này)
- **Ký hiệu hóa học không phiên âm** trong câu tiếng Anh: viết *H₂O* hoặc *water*, không viết *"H two O"* trong văn bản in ấn.

### 5c. Thuật ngữ có nghĩa thường ngày khác nghĩa khoa học

> ⚠️ Đây là nguồn nhầm lẫn nghiêm trọng nhất. Agent PHẢI kiểm tra ngữ cảnh trước khi dịch các từ sau.

| Từ tiếng Anh | Nghĩa thường ngày | Nghĩa khoa học | Ví dụ phân biệt |
|---|---|---|---|
| **solution** /səˈluːʃən/ | giải pháp, đáp án | dung dịch (hoá học) | *The solution to the problem is... / Salt solution is a mixture.* |
| **mass** /mæs/ | đám đông; nhiều | khối lượng (kg) | *a mass of people / The mass of the object is 5 kg.* |
| **power** /ˈpaʊə/ | sức mạnh; quyền lực | công suất (W); lũy thừa (toán) | *political power / The power of the motor is 500 W.* |
| **volume** /ˈvɒljuːm/ | âm lượng; tập sách | thể tích (ml, L, m³) | *Turn up the volume. / The volume of gas is 2 L.* |
| **matter** /ˈmætə/ | vấn đề; quan trọng | vật chất (vật lí, hoá) | *It doesn't matter. / All matter is made of atoms.* |
| **work** /wɜːk/ | công việc; làm việc | công (J = newton × mét) | *I go to work. / No work is done if there is no displacement.* |
| **force** /fɔːs/ | bắt buộc; lực lượng | lực (N) | *I forced him to leave. / The net force on the object is 10 N.* |
| **energy** /ˈɛnədʒi/ | năng lượng; sự hăng hái | năng lượng (J) | *She has lots of energy. / Kinetic energy = ½mv².* |
| **cell** /sɛl/ | phòng giam; điện thoại | tế bào (sinh học); pin điện | *a prison cell / Red blood cells carry oxygen. / a solar cell* |
| **conductor** /kənˈdʌktə/ | nhạc trưởng; người soát vé | vật dẫn điện/nhiệt | *the orchestra conductor / Copper is a good conductor.* |
| **organic** /ɔːˈɡænɪk/ | hữu cơ (tự nhiên, không hóa chất) | hợp chất hữu cơ (có carbon) | *organic food / Organic chemistry studies carbon compounds.* |
| **theory** /ˈθɪəri/ | giả thuyết (ngôn ngữ thường) | lý thuyết được kiểm chứng | *That's just a theory (= opinion). / The theory of evolution is well-supported by evidence.* |
| **significant** /sɪɡˈnɪfɪkənt/ | quan trọng | có ý nghĩa thống kê; đáng kể | *a significant discovery / a statistically significant result* |
| **negative** /ˈnɛɡətɪv/ | tiêu cực | âm (điện, số học, kết quả) | *a negative attitude / a negative charge / a negative result* |

### 5d. Lưu ý đặc biệt: "theory" trong khoa học

Trong tiếng nói thông thường, *theory* = phỏng đoán, giả thuyết chưa chắc chắn.

Trong khoa học, *theory* = hệ thống giải thích đã được kiểm chứng nhiều lần (*the theory of evolution, cell theory, atomic theory*) — **không phải suy đoán**.

Khi học sinh dịch "thuyết tiến hóa là một lý thuyết" thành *"the theory of evolution is just a theory"*, câu này có thể bị hiểu sai nghĩa trong tiếng Anh.

Dịch tốt hơn: *"The theory of evolution is a well-established scientific explanation."*

---

## PHỤ LỤC: DANH SÁCH TỪ HAI NGHĨA — TRA NHANH

| Từ | Kiểm tra ngữ cảnh | Nghĩa khoa học cần dùng |
|---|---|---|
| solution | Hoá học? → dung dịch | *salt solution, dilute solution* |
| mass | Vật lí? → khối lượng | *mass = 5 kg* |
| power | Vật lí? → công suất; Toán? → lũy thừa | *power = 100 W / 2 to the power of 3* |
| volume | Khoa học? → thể tích | *volume = 250 mL* |
| matter | Vật lí/Hoá? → vật chất | *states of matter* |
| work | Vật lí? → công | *W = F × d* |
| force | Vật lí? → lực | *net force, resultant force* |
| cell | Sinh học? → tế bào; Điện? → pin | *plant cell / solar cell* |
| organic | Hoá học? → hữu cơ (có carbon) | *organic compound* |
| theory | Khoa học? → lý thuyết có căn cứ | *the cell theory* |
| negative | Điện/toán? → âm | *negative charge, negative value* |
| significant | Thống kê? → có ý nghĩa thống kê | *statistically significant* |
