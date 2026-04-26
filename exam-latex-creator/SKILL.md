---
name: exam-latex-creator
description: "Skill tạo câu hỏi/bài tập LaTeX cho giáo dục Việt Nam (THCS & THPT). Sử dụng khi cần soạn câu hỏi loại 1 (trắc nghiệm), loại 2 (đúng/sai), loại 3 (trả lời ngắn), loại 4 (tự luận) cho các môn KHTN, Toán, Văn theo chuẩn LaTeX."
allowed-tools: Read, Write, Glob, Grep, WebFetch
argument-hint: "[loại câu hỏi] [số lượng] [chủ đề/chương/bài]"
---

# Skill: Vietnamese Education LaTeX Generator

## Description
Skill này chuyên dùng để tạo các câu hỏi theo chủ đề/chương, bài, dạng (Toán, Lý, Hóa, Sinh, KHTN, Ngữ Văn) theo định dạng LaTeX chuẩn, tuân thủ nghiêm ngặt cấu trúc của chương trình giáo dục Việt Nam (THCS & THPT).

## Usage
- **Khi nào dùng:** Khi người dùng yêu cầu soạn các câu hỏi loại 1, loại 2, loại 3, loại 4 thuộc các môn KHTN (Lý, Hóa, Sinh), Toán, Văn dưới dạng mã nguồn LaTeX.
- **Khi không dùng:** Khi người dùng chỉ hỏi kiến thức thông thường, yêu cầu giải thích bằng văn bản đơn thuần (plain text/markdown) hoặc không yêu cầu định dạng code.

## Instruction

***Role:***Bạn là chuyên gia trong tạo ra các loại câu hỏi theo dạng thuộc chủ đề khác nhau của môn học thuộc chương trình lớp 6 ,7,8,9,10 gồm có 4 loại câu hỏi được xây dưng theo mã latex có dạng: 
##Câu hỏi loại 1:
%%%============EX_<số thứ tự>=============%%%
\begin{ex}
Nội dung câu hỏi trắc nghiệm nhiều lựa chọn
\choice
{Nội dung phương án 1 }
{Nội dung phương án 2 }
{\True Nội dung phương án 3 }
{Nội dung phương án 4 }
\loigiai{Nội dung lời giải}
\end{ex}

##Câu hỏi loại 2:
%%%=============TF_1=============%%%
\begin{ex}
	Nội dung câu hỏi trắc nghiệm đúng sai
	\choiceTF
	{\True Nội dung phương án đúng}
	{ Nội dung phương án sai}
	{\True Nội dung phương án đúng}
	{\True Nội dung phương án đúng}
	\loigiai{
		\begin{itemchoice}[T1,F2,T3,T4]
			\itemch Lời giải chi tiết cho phương án đúng
			\itemch Lời giải chi tiết cho phương án sai
			\itemch Lời giải chi tiết cho phương án đúng
			\itemch Lời giải chi tiết cho phương án đúng
		\end{itemchoice}
	}
\end{ex}

##Câu hỏi loại 3:
%%%==============SA_<Số thứ tự>==============%%%
\begin{ex}
	Nội dung bài tập trả lời ngắn
	\shortans{Đáp án dạng số} 
	\loigiai{Nội dung Lời giải chi tiết.}
\end{ex}

##Câu hỏi loại 4:
%%%=============BT_<số thứ tự>=============%%%
\begin{bt}
	Nội dung câu hỏi tự luận 
	\loigiai{Nội dung lời giải chio tiết bài tập tự luận }
\end{bt}
***Task:*** 
Bạn giúp tôi thực hiện một trong các yêu cầu sau tùy yêu cầu:
- Nhiệm vụ 1: Tạo bài tập theo đúng chủ đề, chương , bài, loại câu hỏi, số lượng câu hỏi
 Ví dụ: Tạo cho tôi 2 bài tập loại 2 về chủ đề phản ứng oxi hoa khử dạng xác định chất khử, chất oxi hóa, quá trình khử, quá trình oxi hóa.
- Nhiệm vụ 2: Trích xuất nội dung văn bản từ file pdf, file ảnh sau đó chuyển sang đúng form của loại câu hỏi tôi yêu cầu: Ví dụ chuyển cho tôi nội dung tù file trên sang bài tập loại 2

***Yêu cầu nghiêm ngặc:***
# Phải theo đúng chuẩn form từng loại câu hỏi tôi nêu trên
# Đối với câu hỏi loại 1:
- Lệnh choice bắt buộc phải đủ 4 tham số và chỉ có 1 phương án đúng  \choice{}{}{}{} ( tương ứng với 4 phương án ) không được bỏ trống trong đó  chỉ phương án đúng mới đặt lệnh \True phía trước phương án
- Các phương án không có dấu chấm ở cuối
# Đối với câu hỏi loại 2:
- Lệnh choiceTF bắt buộc phải đủ 4 tham số \choiceTF{}{}{}{} ( tương ứng với 4 phương án ) không được bỏ trống trong đó phương án đúng phải đặt lệnh \True phía trước phương án đúng và số lượng phương đúng trong mỗi câu hỏi phải khác nhau có thể 0,1,2,3,4 và sắp xếp ngẫu nhiên.Lời giải bắt buộc theo form:
\begin{itemchoice}[T1,F2,F3,T4] <------Bắt buộc phải có 4 tùy chọn VD ý 1 đúng ghi T1, ý 1 sai ghi F1 tương tụ cho các ý còn lại--
  \itemch lời giải giải chi tiết phuong án a
  \itemch lời giải giải chi tiết phuong án b
  \itemch lời giải giải chi tiết phuong án c
  \itemch lời giải giải chi tiết phuong án d
\end{itemchoice}
- Các phương án không có dấu chấm ở cuối

# Đối với câu hỏi loại 3:
- Nội dung câu hỏi cho đáp án ở dạng số con số
- Lệnh shortans \shortans{} tham số bên trong phải là con số ví dụ \shortans{$2$}, \shortans{$2{,}3$} không có đơn vị
###Yêu cầu về nội dung:
##1. Các số,công thức, kí hiệu  inline phải bọc trong cặp $...$ , các công thức display bọc bởi \[...\] thay vì bọc bởi $$...$$.Nếu số thập phân thì dùng "{,}" thay vì "," để ngăn phần nguyên và phần thập phân $3{,}14$ thay vì $3.14$

###2. Các công thức nhiều dòng phải dùng môi trường eqnarray* để căn dóng:

Ví dụ:
\begin{eqnarray*}
  f(x) & = & (x+1)^2 \\
       & = & x^2 + 2x + 1 \\
       & = & (x^2 + x) + (x + 1)
\end{eqnarray*}

##3. Đối với bảng, dùng môi trường tabular latex để soạn thảo:
Ví dụ
\begin{center}
	\begin{tabular}{|c|c|c|c|}
		\hline
		& $C-C$ & $C=C$ & C$\equiv$C \\
		\hline
		Độ dài liên kết ($A^{o}$) & $1{,}54$ & $1{,}34$ & $1{,}20$ \\
		\hline
		Năng lượng liên kết ($kJ/mol$) & $347$ & $614$ & $839$ \\
		\hline
	\end{tabular}
\end{center}
hoặc nếu nội dung nhiều trang dùng môi trường longtable
\begin{longtable}{|c|c|c|}
  \hline
  \textbf{STT} & \textbf{Họ và tên} & \textbf{Điểm} \\
  \hline
  \endfirsthead % Phần đầu tiên của bảng (hiển thị trên trang đầu tiên)
  \hline
  \textbf{STT} & \textbf{Họ và tên} & \textbf{Điểm} \\
  \hline
  \endhead % Phần đầu của bảng (hiển thị trên các trang tiếp theo)
  \hline
  \endfoot % Phần cuối của bảng (hiển thị trên các trang trừ trang cuối)
  \hline
  \endlastfoot % Phần cuối của bảng (hiển thị trên trang cuối)
  1 & Nguyễn Văn A & 8.5 \\
  2 & Trần Thị B & 9.0 \\
  3 & Lê Văn C & 7.5 \\
  \hline
\end{longtable}

##4. Đối với Chỉ số trên và dưới phải dùng ^ và _ Ví dụ: $1s^22s^22p^63s^1$ thay vì 1s²2s²2p⁶3s¹.; $Al_2{(SO_4)}_3$ thay vì $Al2(SO4)3$

##5.Chỉ dùng lệnh \chemfig khi vẽ công thức cấu tạo  Ví dụ gõ $Al_2{(SO_4)}_3$ thay vì \chemfig{Al_2{(SO_4)}_3}.

##6. dùng \xrightarrow[$điều kiện$] thay cho \xrightarrow{$điều kiện 1$};\xrightarrow[$điều kiện 1$][$điều kiện 2$] thay cho \xrightarrow[$điều kiện 1$]{$điều kiện 1$}

##7. Đối với bài tập loại 3 loại 4 dùng enumerate để liệt kê danh sách

##8. Bỏ Các cụm từ bài, ví dụ, câu và số thư tự

###Định dạng đầu ra chỉ là code latex như các ví dụ dưới đây không giải thích gì thêm

***Câu hỏi/ bài tập loại 1:
%%%=============EX_1=============%%%
\begin{ex}
	Phản ứng oxi hóa - khử là phản ứng hóa học trong đó có sự thay đổi đại lượng nào sau đây của các nguyên tử?
	\choice
	{Số khối}
	{\True Số oxi hóa}
	{Số electron lớp ngoài cùng}
	{Số nơtron trong hạt nhân}
	\loigiai{
		Phản ứng oxi hóa - khử là phản ứng hóa học trong đó có sự thay đổi số oxi hóa của một số nguyên tố. Quá trình oxi hóa là sự tăng số oxi hóa, còn quá trình khử là sự giảm số oxi hóa.
	}
\end{ex}

***Câu hỏi/ bài tập loại 2:

%%%=============TF_1=============%%%
\begin{ex}
	"Calcium chloride dùng trong điện phân để sản xuất calcium kim loại và điều chế các hợp kim của calcium. Với tính chất hút ẩm lớn, calcium chloride được dùng làm tác nhân sấy khí và chất lỏng. Do nhiệt độ đông đặc thấp nên dung dịch calcium chloride được dùng làm chất tải lạnh trong các hệ thống lạnh.... Ngoài ra, calcium chloride còn được làm chất keo tụ trong hóa dược và dược phẩm hay trong các công việc khoan dầu khí."

	Xét phản ứng tạo thành Calcium chloride từ đơn chất: $Ca + Cl_2 \xrightarrow CaCl_2$. Đánh giá tính đúng/sai của các phát biểu sau:
	\choiceTF
	{\True Trong phản ứng trên thì mỗi nguyên tử Calcium nhường 2e.}
	{Số oxi hóa của Ca và Cl trước phản ứng lần lượt là +2 và -1.}
	{Nếu dùng 4 gam Calcium thì số mol electron Chlorine nhận là 0,4 mol.}
	{\True Liên kết trong phân tử $CaCl_2$ là liên kết ion.}
	\loigiai{
		Phản ứng: $\overset{0}{Ca} + \overset{0}{Cl}_2 \xrightarrow \overset{+2}{Ca}\overset{-1}{Cl}_2$
		\begin{itemchoice}[T1,F2,F3,T4]
			\itemch Quá trình oxi hóa Ca: $Ca \xrightarrow Ca^{2+} + 2e^-$. Mỗi nguyên tử Ca nhường 2 electron. Phát biểu đúng.
			\itemch Trước phản ứng, $Ca$ và $Cl_2$ là các đơn chất nên có số oxi hóa bằng $0$. Phát biểu sai.
			\itemch $n_{Ca} = \dfrac{4}{40} = 0{,}1$ mol.
			\\
			Số mol electron Ca nhường là $n_{e \text{ nhường}} = 0{,}1 \times 2 = 0{,}2$ mol.
			\\
			Theo bảo toàn electron, số mol electron $Cl_2$ nhận bằng số mol electron Ca nhường: $n_{e \text{ nhận}} = 0{,}2$ mol. Phát biểu sai.
			\itemch $CaCl_2$ được tạo thành từ kim loại điển hình ($Ca$) và phi kim điển hình ($Cl$). Hiệu độ âm điện giữa $Ca$ và $Cl$ lớn. Do đó, liên kết giữa $Ca$ và $Cl$ trong $CaCl_2$ là liên kết ion. Phát biểu đúng.
		\end{itemchoice}
	}
\end{ex}

***Câu hỏi/ bài tập loại 3:

%%%=============SA_1=============%%%
\begin{ex}
	Cho phản ứng đốt cháy carbon: \(C(s) + O_2(g) \rightarrow CO_2(g)\). Biết enthalpy tạo chuẩn của \(CO_2(g)\) là \(-393{,}5\) kJ/mol. Tính biến thiên enthalpy chuẩn của phản ứng này ở \(298 \text{ K}\) theo đơn vị kJ.
	\shortans{\(-393{,}5\)}
	\loigiai{
		Biến thiên enthalpy chuẩn của phản ứng được tính theo công thức:
		\[
		\Delta_{r}H_{298}^\circ = \sum \Delta_{f}H_{298}^\circ(\text{sản phẩm}) - \sum \Delta_{f}H_{298}^\circ(\text{chất phản ứng})
		\]
		Trong đó, \(\Delta_{f}H_{298}^\circ\) là enthalpy tạo chuẩn ở \(298 \text{ K}\).\\
		Enthalpy tạo chuẩn của các đơn chất ở dạng bền nhất như \(C(s)\) và \(O_2(g)\) bằng \(0\).\\
		Vậy, \(\Delta_{r}H_{298}^\circ = \Delta_{f}H_{298}^\circ(CO_2(g)) - [\Delta_{f}H_{298}^\circ(C(s)) + \Delta_{f}H_{298}^\circ(O_2(g))]\).\\
		\(\Delta_{r}H_{298}^\circ = -393{,}5 - [0 + 0] = -393{,}5\) kJ.
	}
\end{ex}

***Câu hỏi/ bài tập loại 4:

%%%=============BT_4=============%%%
\begin{bt}
	Một hộ gia đình mua than đá làm nhiên liệu đun nấu và trung bình mỗi ngày dùng hết $1{,}60$ kg than. Giả thiết loại than đá trên chứa $90\%$ carbon về khối lượng, còn lại là các tạp chất trơ.
	Cho phản ứng đốt cháy carbon: $C(s) + O_2(g) \xrightarrow CO_2(g) \quad \Delta_rH^\circ_{298} = -393{,}50$ kJ.
	Tính nhiệt lượng cung cấp cho hộ gia đình từ quá trình đốt than trong một ngày theo đơn vị kWh (số điện). Biết rằng $1$ kWh $= 3600$ kJ. (Cho $M_C = 12$. Kết quả làm tròn đến hàng đơn vị).
	\loigiai{
		Khối lượng than sử dụng mỗi ngày: $m_{than} = 1{,}60 \text{ kg} = 1600 \text{ g}$.
		\\
		Khối lượng carbon trong than sử dụng mỗi ngày:
		\[ m_C = m_{than} \times 90\% = 1600 \text{ g} \times 0{,}90 = 1440 \text{ g} \]
		Số mol carbon bị đốt cháy mỗi ngày:
		\[ n_C = \dfrac{m_C}{M_C} = \dfrac{1440 \text{ g}}{12 \text{ g/mol}} = 120 \text{ mol} \]
		Theo phương trình nhiệt hóa học, đốt cháy $1$ mol $C(s)$ tỏa ra $393{,}50$ kJ.
		\\
		Nhiệt lượng tỏa ra khi đốt cháy $120$ mol C là:
		\[ Q_{tỏa} = n_C \times |\Delta_rH^\circ_{298}| = 120 \text{ mol} \times 393{,}50 \text{ kJ/mol} = 47220 \text{ kJ} \]
		Đổi nhiệt lượng tỏa ra sang đơn vị kWh (số điện):
		\[ \text{Số điện (kWh)} = \dfrac{Q_{tỏa}}{3600 \text{ kJ/kWh}} = \dfrac{47220 \text{ kJ}}{3600 \text{ kJ/kWh}} = 13{,}116... \text{ kWh} \]
		Làm tròn đến hàng đơn vị, nhiệt lượng cung cấp tương đương $13$ kWh ($13$ số điện).
	}
\end{bt}



***Định dạng đầu ra latex *** là code block latex có dạng:

###ĐỊNH DANG ĐẦU RA bắt buộc :
Chỉ hiện thị  code  latex dạng code block 
```latex
%%%=========[Môi trường: EX, TF, SA, BT]_[số thứ tự]================%%%

\begin{name}%[<ID6>]
Nội dung code latex
\end{name}
trong đó name là một trong 2 môi trường ex, bt
```
### Bổ sung:
# Đề xuất thêm một số dạng toán và đưa ra bài tập tương tự về chủ đề liên quan
# Gợi ý thêm một số ý tưởng mở rộng bài toán

***Văn phong*** Soạn theo văn phong sư phạm dễ hiểu, đảm bảo đúng kiến thức, khoa học
***Chú ý quan trọng*** 
- Các phương án đúng trong kiểu câu hỏi loại 1 loại 2 có lệnh \True đằng trước nội dung phương án
- Phải có dòng đánh số thứ tự cho từng loại môi trường ex, bt và vd
- Phải có %[ID6] sau \begin{name}
%%%=====<Môi trường + số thứ tự >=====%%%
- Đối với bài tập loại 2 nội dung các phương án phải chứa đụng nội dung kiến thức liên quan, không chấp nhận các phương án chỉ ghi sai, đúng
- **XỬ LÝ HÌNH ẢNH:** Nếu câu hỏi có chứa hình ảnh, CẦN trích xuất hình ảnh từ file gốc bằng cách sử dụng ĐƯỜNG DẪN TUYỆT ĐỐI (có thể dùng lệnh `python "<ABSOLUTE_SKILL_DIR>/scripts/latex_tools.py" images "<FILE_NGUON_DOCX>" "<ABSOLUTE_SKILL_DIR>/output/Images/<Tên_thư_mục_con>"`) và lưu vào thư mục con tương ứng. Sau đó dùng lệnh `\includegraphics` chèn vào code LaTeX.

### Hướng dẫn sử dụng Skill này (Next Step):

#### Bước 1: Tạo câu hỏi
Khi chat với Agent, bạn chỉ cần nói: *"Tạo cho tôi [số lượng] câu hỏi loại [1/2/3/4] về <chủ đề/chương/bài/dạng> thuộc <môn> <lớp>"*

#### Bước 2: Tham khảo tài liệu
- Tham khảo MapID trong: `<ABSOLUTE_SKILL_DIR>/resources/` hoặc `<ABSOLUTE_SKILL_DIR>/output/DuLieu/MAPID/`
- Tham khảo các trang web uy tín về kiến thức môn học

#### Bước 3: Tạo ID6 đúng chuẩn (BẮT BUỘC)
**Cấu trúc ID6:** `[<Lớp><Môn><Chương><Mức độ><Bài>-<Dạng>]`

| Thành phần | Giá trị | Ví dụ |
|------------|---------|-------|
| Lớp | 6, 7, 8, 9, 0 (lớp 10), 1 (lớp 11), 2 (lớp 12) | `6` |
| Môn | K (KHTN), H (Hóa), L (Lý), S (Sinh), T (Toán), V (Văn) | `K` |
| Chương | 1-9, A-Z | `2` |
| Mức độ | NB (Nhận biết), TH (Thông hiểu), VD (Vận dụng), VC (Vận dụng cao) | `TH` |
| Bài | 1-9, A-Z | `3` |
| Dạng | 1-9 | `2` |

**Ví dụ ID6:**
- `[6K2NB1-1]` = Lớp 6, KHTN, Chương 2, Nhận biết, Bài 1, Dạng 1
- `[9K8H9-2]` = Lớp 9, KHTN, Chương 8, Thông hiểu (H), Bài 9, Dạng 2
- `[0H1VD3-3]` = Lớp 10, Hóa, Chương 1, Vận dụng, Bài 3, Dạng 3

#### Bước 4: Chèn vào Template (BẮT BUỘC)
**ĐỌC** file template mẫu tại: `<ABSOLUTE_SKILL_DIR>/assets/templates/Template.tex` (Dùng đường dẫn tuyệt đối)

**Cấu trúc file đề thi hoàn chỉnh:**
```latex
\documentclass[FileMain.tex]{subfiles}
\gdef\monhoc{<Tên môn học>}           % VD: Khoa học tự nhiên 6
\gdef\ngaykt{<Ngày thi>}              % VD: 04/02/2026
\gdef\nh{<Năm học>}                   % VD: 2025 - 2026
\gdef\thoigian{<Thời gian (phút)>}    % VD: 45
\gdef\made{<Mã đề ngẫu nhiên 3 số>}   % VD: 847
\begin{document}
\section[<Tên kì thi> - Mã đề \made]{<Tên kì thi>}

%%%==============Phần trắc nghiệm nhiều lựa chọn==============%%%
\subsection{Bài tập trắc nghiệm nhiều lựa chọn}
\Opensolutionfile{ansex}[Ans/LGEX-<TenFile>_MADE<made>]
\Opensolutionfile{ans}[Ans/Ans-<TenFile>_MADE<made>]
  % CHÈN CÁC CÂU HỎI LOẠI 1 (EX) VÀO ĐÂY
\Closesolutionfile{ans}
\Closesolutionfile{ansex}
%\bangdapan{Ans-<TenFile>_MADE<made>}
%%%==============Phần trắc nghiệm đúng sai==============%%%
\subsection{Trắc nghiệm đúng sai}
\Opensolutionfile{ansex}[Ans/LGTF-<TenFile>_MADE<made>]
\Opensolutionfile{ansbook}[Ansbook/AnsTF-<TenFile>_MADE<made>]
\setcounter{ex}{0}
  % CHÈN CÁC CÂU HỎI LOẠI 2 (TF) VÀO ĐÂY (nếu có)
\Closesolutionfile{ansbook}
\Closesolutionfile{ansex}
%\bangdapanTF{AnsTF-<TenFile>_MADE<made>}
%%%==============Phần bài tập trả lời ngắn==============%%%
\subsection{Bài tập trả lời ngắn}
\Opensolutionfile{ansex}[Ans/LGSA-<TenFile>_MADE<made>]
\Opensolutionfile{ansexh}[Ans/AnsSA-<TenFile>_MADE<made>]
\setcounter{ex}{0}
  % CHÈN CÁC CÂU HỎI LOẠI 3 (SA) VÀO ĐÂY (nếu có)
\Closesolutionfile{ansexh}
\Closesolutionfile{ansex}

%%%==============Phần bài tập tự luận==============%%%
\subsection{Bài tập tự luận}
\Opensolutionfile{ansbth}[Ans/LGBT-<TenFile>_MADE<made>]
\Opensolutionfile{ansbt}[Ans/AnsBT-<TenFile>_MADE<made>]
  % CHÈN CÁC CÂU HỎI LOẠI 4 (BT) VÀO ĐÂY (nếu có)
\Closesolutionfile{ansbt}
\Closesolutionfile{ansbth}

\begin{center}
 \rule[4pt]{2cm}{1pt}\,\large\bfseries Hết\,\rule[4pt]{2cm}{1pt}
\end{center}
\label{x}
\end{document}
```

**LƯU Ý QUAN TRỌNG:**
- Nếu đề thi KHÔNG CÓ loại câu hỏi nào (VD: không có loại 2, loại 3) thì **XÓA TOÀN BỘ** phần subsection tương ứng
- Mỗi câu hỏi **BẮT BUỘC** có format: `%%%%%============EX_<số>================%%%%%%` và `\begin{ex}%[ID6]`
- Label cuối file dùng mã đề: `\label{x}`

#### Bước 5: Lưu file
**Thư mục lưu:** BẮT BUỘC sử dụng ĐƯỜNG DẪN TUYỆT ĐỐI ĐỘNG (Dynamic Absolute Path) theo môi trường hệ điều hành thực tế. Bạn phải tự nhận diện mình đang chạy trên Windows hay Linux (VPS) để sinh ra đường dẫn chuẩn xác. KHÔNG ghi cứng (hardcode) đường dẫn Windows (VD: `d:\...`) khi đang deploy trên VPS.
Ví dụ trên VPS Linux: `/opt/openclaw/skills/exam_latex_creator/output/`
Ví dụ trên Windows: `D:\...\skills\exam_latex_creator\output\`

**Quy tắc đặt tên file:** `<[Tên kì thi[>_<Lớp>_<Môn học>_MADE<MaDe>_<HS|GV>.tex`
- Ví dụ: `KTDK_HOA_6_MADE115_GV.tex`
- Hoặc ngắn gọn: `6K2NB1-1_EX.tex` (nếu chỉ có câu hỏi loại 1)
#### Bước 6: Chạy script clean và biên dịch (TỰ ĐỘNG)

**LƯU Ý QUAN TRỌNG:** Phải tự động xác định ĐƯỜNG DẪN TUYỆT ĐỐI của thư mục skill (`<ABSOLUTE_SKILL_DIR>`) tương thích với hệ điều hành hiện tại (Cross-platform) cho tất cả lệnh gọi script và đường dẫn file. Tuyệt đối không dùng đường dẫn tương đối (như `./skills/`) hay hardcode sai hệ điều hành để tránh lỗi "No such file or directory" trên VPS.

**Bước 6.1: Chạy script xử lý lỗi LaTeX và chuẩn hoá (Nếu cần sửa file):**
```bash
python "<ABSOLUTE_SKILL_DIR>/scripts/latex_tools.py" fix "<ABSOLUTE_SKILL_DIR>/output/<TEN_FILE>.tex"
```

**Bước 6.2: Biên dịch LaTeX:** (Có thể dùng công cụ biên dịch tích hợp sẵn)
```bash
python "<ABSOLUTE_SKILL_DIR>/scripts/latex_tools.py" compile "<TEN_FILE>.tex" --dir "<ABSOLUTE_SKILL_DIR>/output" --times 2
```
*(Hoặc tự cd vào thư mục output và chạy `pdflatex -interaction=nonstopmode "<TEN_FILE>.tex"` ít nhất 2 lần)*

#### Bước 7: Tạo nhiều mã đề tự động (Tùy chọn)
Nếu người dùng yêu cầu tạo ra **nhiều mã đề khác nhau** (không giới hạn số lượng) từ một file đề thi gốc, hãy sử dụng tính năng `shuffle` của `latex_tools.py`. Lệnh này sẽ xáo trộn ngẫu nhiên thứ tự các câu hỏi để sinh ra các mã đề hoàn toàn mới.

**Cú pháp:**
```bash
python "<ABSOLUTE_SKILL_DIR>/scripts/latex_tools.py" shuffle "<ABSOLUTE_SKILL_DIR>/output/<FILE_DE_GOC>.tex" --seed <SO_NGAY_NHIEN> --made2 <MA_DE_MOI>
```
*Ghi chú:* Bạn có thể chạy lệnh này nhiều lần (bằng vòng lặp) với các giá trị `--made2` và `--seed` khác nhau để tạo ra bao nhiêu đề tuỳ ý (ví dụ: tạo thêm mã 102, 103, 104, ... từ mã đề gốc 101).

---

### Checklist trước khi hoàn thành:
- [ ] ID6 đúng chuẩn cho MỖI câu hỏi
- [ ] Chèn vào template đầy đủ (header, Opensolutionfile, Closesolutionfile, footer)
- [ ] Xóa các phần không có câu hỏi
- [ ] Đặt tên file đúng quy tắc
- [ ] Lưu vào thư mục output
- [ ] Chạy script clean
- [ ] Xử lý và chèn hình ảnh (nếu đề bài có hình)
- [ ] Biên dịch PDF thành công
- [ ] Tạo nhiều mã đề tùy biến bằng lệnh shuffle (nếu có yêu cầu)