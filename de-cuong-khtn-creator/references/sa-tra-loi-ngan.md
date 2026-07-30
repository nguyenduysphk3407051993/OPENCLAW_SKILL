# Loại 3: Trả lời ngắn (SA)

## Cấu trúc LaTeX

```latex
%%%==============SA_<số thứ tự>==============%%%
\begin{ex}%[<ID6>]
	Nội dung bài tập trả lời ngắn
	\shortans{$<đáp án dạng số>$}
	\loigiai{Nội dung lời giải chi tiết.}
\end{ex}
```

## Quy tắc bắt buộc

1. Đáp án trong `\shortans{}` phải là **con số**, bọc trong `$...$`
2. **Không có đơn vị** trong `\shortans{}` — chỉ số thuần
3. Nội dung câu hỏi phải cho ra đáp án ở dạng số
4. Số thập phân dùng `{,}`: `\shortans{$2{,}3$}`
5. Dùng `enumerate` để liệt kê danh sách (nếu có)

## Ví dụ

```latex
%%%=============SA_1=============%%%
\begin{ex}%[0H2V3-3]
	Cho phản ứng đốt cháy carbon: $C(s) + O_2(g) \rightarrow CO_2(g)$. Biết enthalpy tạo chuẩn của $CO_2(g)$ là $-393{,}5$ kJ/mol. Tính biến thiên enthalpy chuẩn của phản ứng này ở $298$ K theo đơn vị kJ.
	\shortans{$-393{,}5$}
	\loigiai{
		Biến thiên enthalpy chuẩn của phản ứng được tính theo công thức:
		\[
		\Delta_{r}H_{298}^\circ = \sum \Delta_{f}H_{298}^\circ(\text{sản phẩm}) - \sum \Delta_{f}H_{298}^\circ(\text{chất phản ứng})
		\]
		Enthalpy tạo chuẩn của các đơn chất ở dạng bền nhất như $C(s)$ và $O_2(g)$ bằng $0$.\\
		Vậy $\Delta_{r}H_{298}^\circ = -393{,}5 - [0 + 0] = -393{,}5$ kJ.
	}
\end{ex}

%%%=============SA_2=============%%%
\begin{ex}%[6K3N2-3]
	Một vật có khối lượng $5$ kg đang chuyển động với vận tốc $4$ m/s. Tính động năng của vật theo đơn vị J.
	\shortans{$40$}
	\loigiai{
		Động năng của vật được tính theo công thức:
		\[
		W_đ = \dfrac{1}{2}mv^2 = \dfrac{1}{2} \times 5 \times 4^2 = 40 \text{ J}
		\]
	}
\end{ex}
```
