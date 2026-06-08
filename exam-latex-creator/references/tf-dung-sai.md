# Loại 2: Trắc nghiệm đúng sai (TF)

## Cấu trúc LaTeX

```latex
%%%=============TF_<số thứ tự>=============%%%
\begin{ex}%[<ID6>]
	Nội dung câu hỏi trắc nghiệm đúng sai
	\choiceTF
	{\True Nội dung phương án đúng}
	{Nội dung phương án sai}
	{\True Nội dung phương án đúng}
	{Nội dung phương án sai}
	\loigiai{
		\begin{itemchoice}[T1,F2,T3,F4]
			\itemch Lời giải chi tiết phương án a
			\itemch Lời giải chi tiết phương án b
			\itemch Lời giải chi tiết phương án c
			\itemch Lời giải chi tiết phương án d
		\end{itemchoice}
	}
\end{ex}
```

## Quy tắc bắt buộc

1. Lệnh `\choiceTF` phải đủ **4 tham số** `\choiceTF{}{}{}{}` — không được bỏ trống
2. Phương án đúng đặt `\True` phía trước nội dung
3. Số lượng phương án đúng trong mỗi câu phải **khác nhau** (có thể 0,1,2,3,4) và **sắp xếp ngẫu nhiên**
4. Các phương án **không có dấu chấm** ở cuối
5. Nội dung các phương án phải chứa **nội dung kiến thức** — không chấp nhận chỉ ghi "đúng" hoặc "sai"

## Lời giải — format bắt buộc

```latex
\loigiai{
	\begin{itemchoice}[T1,F2,F3,T4]
		\itemch Lời giải chi tiết phương án a
		\itemch Lời giải chi tiết phương án b
		\itemch Lời giải chi tiết phương án c
		\itemch Lời giải chi tiết phương án d
	\end{itemchoice}
}
```

- Bắt buộc **4 tùy chọn** trong `[...]`: ý đúng ghi `T` + số, ý sai ghi `F` + số
  - VD: `[T1,F2,F3,T4]` = ý 1 đúng, ý 2 sai, ý 3 sai, ý 4 đúng
- Bắt buộc **4 `\itemch`** tương ứng 4 phương án

## Ví dụ hoàn chỉnh

```latex
%%%=============TF_1=============%%%
\begin{ex}%[9K8H1-2]
	"Calcium chloride dùng trong điện phân để sản xuất calcium kim loại và điều chế các hợp kim của calcium."

	Xét phản ứng tạo thành Calcium chloride từ đơn chất: $Ca + Cl_2 \xrightarrow CaCl_2$. Đánh giá tính đúng/sai của các phát biểu sau:
	\choiceTF
	{\True Trong phản ứng trên thì mỗi nguyên tử Calcium nhường 2e}
	{Số oxi hóa của Ca và Cl trước phản ứng lần lượt là +2 và -1}
	{Nếu dùng 4 gam Calcium thì số mol electron Chlorine nhận là 0,4 mol}
	{\True Liên kết trong phân tử $CaCl_2$ là liên kết ion}
	\loigiai{
		Phản ứng: $\overset{0}{Ca} + \overset{0}{Cl}_2 \xrightarrow \overset{+2}{Ca}\overset{-1}{Cl}_2$
		\begin{itemchoice}[T1,F2,F3,T4]
			\itemch Quá trình oxi hóa Ca: $Ca \xrightarrow Ca^{2+} + 2e^-$. Mỗi nguyên tử Ca nhường 2 electron. Phát biểu đúng.
			\itemch Trước phản ứng, $Ca$ và $Cl_2$ là các đơn chất nên có số oxi hóa bằng $0$. Phát biểu sai.
			\itemch $n_{Ca} = \dfrac{4}{40} = 0{,}1$ mol. Số mol electron Ca nhường là $0{,}1 \times 2 = 0{,}2$ mol. Theo bảo toàn electron, số mol electron $Cl_2$ nhận = $0{,}2$ mol. Phát biểu sai.
			\itemch $CaCl_2$ được tạo từ kim loại điển hình ($Ca$) và phi kim điển hình ($Cl$), hiệu độ âm điện lớn. Liên kết là liên kết ion. Phát biểu đúng.
		\end{itemchoice}
	}
\end{ex}
```
