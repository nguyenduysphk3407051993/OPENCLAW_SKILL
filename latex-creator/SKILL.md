---
name: latex-creator
description: "Tạo bài giảng, chuyên đề, bài tập và đề kiểm tra cho chương trình giáo dục Việt Nam (THCS & THPT) theo định dạng LaTeX chuẩn với cấu trúc nghiêm ngặt. Hỗ trợ đầy đủ 3 phần: Mở đầu, Lý thuyết, Bài tập."
allowed-tools: Read, Write, Glob, Grep
argument-hint: "[loại tài liệu: bài giảng/chuyên đề] [chủ đề/bài học]"
---

# Skill: Vietnamese Education General LaTeX Creator

## Khi yêu cầu chưa đủ cụ thể — PHẢN BIỆN TRƯỚC, LÀM SAU

Yêu cầu chung chung luôn cho ra sản phẩm kém. **Không đoán bừa, cũng không hỏi
lể tể từng ý.** Hãy nêu rõ đang thiếu gì, rồi đưa **một prompt mẫu đã điền sẵn
giá trị mặc định hợp lý** để người dùng sửa và gửi lại trong đúng một lượt.

Thiếu từ **2 tiêu chí trở lên** thì bắt buộc phản biện. Thiếu **đúng 1** tiêu chí
thì tự chọn mặc định, làm tiếp, và nói rõ đã chọn gì.

**Tiêu chí bắt buộc:** loại tài liệu · môn · lớp · chủ đề · độ dài · có bài tập kèm hay không

**Mẫu phản biện:**

> Yêu cầu hiện thiếu: **độ dài**, **phạm vi bài tập**. Nếu làm luôn thì tôi phải đoán, dễ lệch
> ý bạn. Bạn copy prompt dưới đây, sửa chỗ in đậm rồi gửi lại:
>
> ```
> Tạo **chuyên đề** LaTeX môn **Vật lí** lớp **10**,
> chủ đề **Động lượng và định luật bảo toàn động lượng**.
> Độ dài: **khoảng 12 trang** · Bài tập kèm: **10 câu trắc nghiệm + 5 bài tự luận**
> Mức độ: **từ nhận biết đến vận dụng cao** · Có lời giải: **có**
> ```

---

## Description
Skill này chuyên dùng để soạn bài giảng, chuyên đề, bài tập và đề kiểm tra cho chương trình giáo dục Việt Nam (THCS & THPT) theo định dạng LaTeX chuẩn. Hỗ trợ các môn Toán, Vật lý, Hóa học, Sinh học, KHTN (tích hợp Lý-Hóa-Sinh), Ngữ Văn. 
Các tài liệu được tạo ra bao gồm đầy đủ 3 phần: Mở đầu (chương, bài, mục tiêu, khởi động), Lý thuyết (trình bày kiến thức, hình ảnh, câu hỏi tư duy, tóm tắt) và Bài tập (dạng toán, phương pháp, ví dụ mẫu, bài tập tự luyện với 4 loại câu hỏi).

## Usage
- **Khi nào dùng:** Khi người dùng yêu cầu soạn bài giảng, chuyên đề, đề kiểm tra, hoặc bài tập theo form LaTeX giáo dục Việt Nam cho các môn KHTN, Toán, Ngữ Văn. Trigger keywords: "soạn bài giảng", "chuyên đề", "đề kiểm tra LaTeX", "bài tập LaTeX", "skill latex creator", "tạo bài giảng LaTeX".
- **Khi không dùng:** Khi người dùng chỉ hỏi kiến thức thông thường, yêu cầu giải thích bằng văn bản đơn thuần (plain text/markdown) hoặc không yêu cầu định dạng code LaTeX.

## Instruction

***Role:*** Bạn là chuyên gia trong lĩnh vực tạo bài giảng theo định dạng LaTeX với cấu trúc phân cấp nghiêm ngặt của chương trình giáo dục Việt Nam.

***Task:*** Tạo ra bài giảng/chuyên đề theo một chủ đề thuộc các môn: Toán, Vật lý, Hóa học, Sinh học, KHTN, Ngữ Văn. Bài giảng BẮT BUỘC gồm 3 phần chính: Phần mở đầu, Phần lý thuyết và Phần bài tập.

---

### CẤU TRÚC BÀI GIẢNG / CHUYÊN ĐỀ

#### 1. Phần mở đầu
Thể hiện thông tin chương, bài, mục tiêu và câu hỏi khởi động.

```latex
\documentclass[Main.tex]{subfiles} 
\begin{document}
%%%Phần mở đầu
\chapter{Nội dung chương} % VD: \chapter{Năng lượng hóa học} (KHÔNG ghi "Chương 5:")
\section{Nội dung bài} % VD: \section{Phản ứng Hóa học và entanpy} (KHÔNG ghi "Bài 1:")

\begin{Muctieu}
	\begin{itemize}
		\item Nội dung mục tiêu 1
		\item Nội dung mục tiêu 2
		\item Nội dung mục tiêu ...
	\end{itemize}
\end{Muctieu}

\begin{kd}
	\immini{Nội dung câu hỏi khởi động}{Chèn prompt tạo ảnh minh họa vào đây}
\end{kd}
```

#### 2. Phần lý thuyết
Trình bày nội dung bài học đầy đủ theo từng mục sắp xếp theo cấp độ. **BẮT BUỘC bắt đầu bằng `\subsection{Nội dung bài học}`**.

```latex
\subsection{Nội dung bài học}
\subsubsection{Mục con cấp 1 lần 1}
	\Noibat[\maunhan][][][]{Mục con cấp 2 lần 1}
	\begin{ghinho}
		Nội dung cần ghi nhớ (có thể dùng enumerate nếu cần liệt kê)
	\end{ghinho}
	
\subsubsection{Mục con cấp 1 lần 2}
	\Noibat[\maunhan][][][]{Mục con cấp 2 lần 1}
		\begin{tomtat}
			Nội dung tóm tắt
		\end{tomtat}
```

**Các môi trường sử dụng trong phần lý thuyết:**
- `\begin{tongket}{Tóm tắt bài học}...\end{tongket}`: Nội dung kiến thức tổng kết khối lượng lớn.
- `\begin{tomtat}...\end{tomtat}`: Tóm tắt nội dung ngắn gọn.
- `\begin{cacbuoc} \item ... \end{cacbuoc}`: Liệt kê các bước thực hiện/phương pháp.
- `\begin{hopdongian}...\end{hopdongian}`: Nội dung/hoạt động đơn giản.
- `\begin{hoivadap}...\end{hoivadap}`: **BẮT BUỘC** có ít nhất 1 câu hỏi kích thích tư duy/đặt vấn đề trong mỗi đơn vị kiến thức.
- `\begin{Bancobiet}...\end{Bancobiet}`: Kiến thức mở rộng, đọc thêm.

**Lưu ý phần lý thuyết:**
- Trong các mục ngoài text, phải đa dạng cung cấp bảng, đồ thị, hình ảnh.
- Tại vị trí cần hình ảnh minh họa: hãy thay bằng prompt sinh ảnh chi tiết (gồm đối tượng, bối cảnh, phong cách) sát với nội dung kiến thức.

#### 3. Phần bài tập
**BẮT BUỘC bắt đầu bằng `\subsection{Bài tập}`**.
Phần bài tập chia thành các dạng. Mỗi dạng gồm: Phương pháp giải -> Ví dụ mẫu -> Bài tập tự luyện (gồm 4 loại câu hỏi, mỗi loại 5 câu).

```latex
\subsection{Bài tập}
\begin{dang}{Tên dạng bài tập} % VD: \begin{dang}{Tính biến thiên enthalpy}
\end{dang}
\begin{phuongphap}
    Nội dung phương pháp. (dùng \begin{cacbuoc} \item ... \end{cacbuoc} nếu có các bước)
\end{phuongphap}

\Noibat[\maunhan][][\faBookmark][]{Ví dụ mẫu}
%%%%%==========VD_01==========%%%%%
\begin{vd}
    % Nếu là trắc nghiệm: dùng \choice{}{}{}{}
    % Nếu tự luận: chép đề và nhập lời giải
	Nội dung ví dụ mẫu
	\loigiai{Nội dung lời giải chi tiết (dùng enumerate nếu nhiều bước)}
\end{vd}

\Noibat[\maunhan][][\faBook][]{Bài tập tự luyện}

%%%------------- 1. Tự luận -------------%%%
\phan{Bài tập tự luận}
\Opensolutionfile{ansbth}[Ans/LGBT-C<chương>B<bài>_Dang<dạng>] % VD: C04B01_Dang1
\Opensolutionfile{ansbt}[Ans/AnsBT-C<chương>B<bài>_Dang<dạng>]
    % SOẠN 5 CÂU LOẠI 4 (BT) VÀO ĐÂY
\Closesolutionfile{ansbt}
\Closesolutionfile{ansbth}

%%%------------- 2. Trả lời ngắn -------------%%%
\phan{Bài tập trả lời ngắn}
\Opensolutionfile{ansbth}[Ans/LGSA-C<chương>B<bài>_Dang<dạng>]
\Opensolutionfile{ansbt}[Ans/AnsSA-C<chương>B<bài>_Dang<dạng>]
    % SOẠN 5 CÂU LOẠI 3 (SA) VÀO ĐÂY
\Closesolutionfile{ansbt}
\Closesolutionfile{ansbth}

%%%------------- 3. Trắc nghiệm nhiều lựa chọn -------------%%%
\phan{Trắc nghiệm nhiều lựa chọn}
\Opensolutionfile{ansex}[Ans/LGEX-C<chương>B<bài>_Dang<dạng>]
\Opensolutionfile{ans}[Ans/Ans-C<chương>B<bài>_Dang<dạng>]
    % SOẠN 5 CÂU LOẠI 1 (EX) VÀO ĐÂY
\Closesolutionfile{ans}
\Closesolutionfile{ansex}

%%%------------- 4. Trắc nghiệm Đúng/Sai -------------%%%
\phan{Bài tập trắc nghiệm Đúng Sai}
\Opensolutionfile{ansex}[Ans/LGTF-C<chương>B<bài>_Dang<dạng>]
\Opensolutionfile{ansbook}[Ansbook/AnsTF-C<chương>B<bài>_Dang<dạng>]
\Opensolutionfile{ans}[Ans/Tempt-C<chương>B<bài>_Dang<dạng>]
    % SOẠN 5 CÂU LOẠI 2 (TF) VÀO ĐÂY
\Closesolutionfile{ans}
\Closesolutionfile{ansbook}
\Closesolutionfile{ansex}

\end{document}
```

---

### FORM 4 LOẠI CÂU HỎI TIÊU CHUẨN

#### Loại 1: Trắc nghiệm 4 lựa chọn (EX)
```latex
%%%%%============EX_<Số thứ tự>================%%%%%%
\begin{ex}
	Nội dung Câu hỏi trắc nghiệm nhiều lựa chọn
	\choice
	{Phương án sai}
	{Phương án sai}
	{\True Phương án đúng}
	{Phương án sai}
	\loigiai{Nội dung lời giải chi tiết}
\end{ex}
```

#### Loại 2: Trắc nghiệm Đúng/Sai (TF)
```latex
%%%%%============TF_<Số thứ tự>================%%%%%%
\begin{ex}
	Nội dung Câu hỏi trắc nghiệm đúng sai
	\choiceTF
	{\True Phương án 1 (đúng)}
	{Phương án 2 (sai)}
	{\True Phương án 3 (đúng)}
	{Phương án 4 (sai)}
	\loigiai{
		\begin{itemchoice}[T1,F2,T3,F4]
			\itemch Lời giải chi tiết cho ý 1
			\itemch Lời giải chi tiết cho ý 2
			\itemch Lời giải chi tiết cho ý 3
			\itemch Lời giải chi tiết cho ý 4
		\end{itemchoice}
	}
\end{ex}
```
*Lưu ý:* Các phương án phải chứa nội dung kiến thức liên quan (không ghi "đúng", "sai"). Số lượng `\True` có thể là từ 0 đến 4 ngẫu nhiên.

#### Loại 3: Trả lời ngắn (SA)
```latex
%%%%%============SA_<Số thứ tự>================%%%%%%
\begin{ex}
	Nội dung bài tập trả lời ngắn (chỉ lấy số).
	\shortans{$2{,}5$} % KHÔNG chứa đơn vị, chỉ để số, KHÔNG dùng phẩy (dùng {,} thập phân), bọc $...$
	\loigiai{Lời giải chi tiết}
\end{ex}
```

#### Loại 4: Tự luận (BT)
```latex
%%%%%============BT_<Số thứ tự>================%%%%%%
\begin{bt}
	Nội dung bài tập tự luận.
	\loigiai{Lời giải chi tiết (nên dùng \begin{enumerate} cho nhiều bước)}
\end{bt}
```

---

### QUY TẮC SOẠN THẢO LaTeX (NGHIÊM NGẶT)

1. **Toán học và Công thức:**
   - Inline bọc trong `$...$`, hiển thị display bọc trong `\[...\]`.
   - **Tuyệt đối KHÔNG dùng `$$...$$`**.
   - Dấu phẩy thập phân dùng `{,}` (rất quan trọng: `$3{,}14$`).
   - Mũ và chỉ số dưới dùng `^` và `_` (KHÔNG dùng unicode ², ₃...).
   - Chỉ dùng `\chemfig` khi biểu diễn cấu tạo hóa học, công thức phân tử thì dùng `$...$` (VD: `$Al_2{(SO_4)}_3$`).
   
2. **Căn dóng và Môi trường:**
   - Công thức nhiều dòng **chỉ dùng** môi trường `eqnarray*`.
   - Bảng biểu dùng `tabular` (ít dòng) hoặc `longtable` (nhiều trang).
   
3. **Mũi tên phản ứng & Ký hiệu:**
   - Dùng `\xrightarrow[$dưới$][$trên$]` (ngoặc vuông). **KHÔNG dùng ngoặc nhọn `{}`** cho xrightarrow.
   
4. **Viết văn bản:**
   - KHÔNG dùng "Bài X:", "Chương X:", "Dạng X:", "Câu X:", "Ví dụ X:" trong các tiêu đề (chỉ ghi nội dung).
   - KHÔNG có dấu chấm cuối các phương án trắc nghiệm (`\choice`, `\choiceTF`).
   - Văn phong sư phạm, dễ hiểu, logic khoa học mạch lạc.
   - Thêm `%%%=====<Môi trường>_<Số thứ tự>=====%%%` (VD: `%%%%%==========VD_01==========%%%%%`) trước mỗi bài tập/ví dụ.

---

### ĐỊNH DẠNG ĐẦU RA (OUTPUT)
Đầu ra chỉ chứa **một block code LaTeX duy nhất**, không giải thích hoặc bổ sung văn bản ngoài lề.
```latex
\documentclass[Main.tex]{subfiles} 
\begin{document}
  ... (Toàn bộ code LaTeX) ...
\end{document}
```


---

## Tương thích đa nền tảng (Windows · Linux · môi trường skill)

Các script Python của skill này đã xử lý sẵn những chỗ hay vỡ khi đổi máy:

| Vấn đề | Đã xử lý thế nào |
|--------|-------------------|
| Console Windows là cp1252/cp437 → in tiếng Việt ném `UnicodeEncodeError` | Mỗi script tự `reconfigure` stdout/stderr sang UTF-8 ngay sau phần import |
| Đọc/ghi file | Luôn khai báo `encoding="utf-8"`; đọc thêm `utf-8-sig` để nuốt BOM của Notepad |
| Ghép đường dẫn | Dùng `os.path.join` / `pathlib`, không nối chuỗi `\` hay `/` |

Khi tự gõ lệnh, tuân thủ thêm 4 điểm sau:

1. **Bọc mọi đường dẫn trong dấu nháy kép** — thư mục tiếng Việt hay có dấu cách.
2. **Linux phân biệt HOA/thường.** `output/` khác `Output/`, `Khaibao/HeaderFooter`
   khác `Khaibao/Headerfooter`. Đặt tên file đầu ra **không dấu, không khoảng trắng**.
3. **Ubuntu không có lệnh `python`**, chỉ có `python3`. Dùng venv
   (`python3 -m venv .venv && source .venv/bin/activate`) để các lệnh trong tài
   liệu này chạy nguyên văn, hoặc thay `python` bằng `python3`.
4. **Không hard-code đường dẫn tuyệt đối** kiểu `D:\...` hay `/home/...` vào file
   cấu hình; luôn tính tương đối từ `<SKILL_DIR>`.

Khi chạy trong bash sandbox, dùng đường dẫn VM mount thay cho đường dẫn Windows.
