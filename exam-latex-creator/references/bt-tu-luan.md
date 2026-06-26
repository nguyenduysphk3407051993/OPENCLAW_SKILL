# Loại 4: Tự luận (BT)

## Cấu trúc LaTeX

```latex
%%%=============BT_<số thứ tự>=============%%%
\begin{bt}%[<ID6>]
	Nội dung câu hỏi tự luận
	\loigiai{Nội dung lời giải chi tiết bài tập tự luận}
\end{bt}
```

## Quy tắc bắt buộc

1. Dùng môi trường `bt` (không phải `ex`)
2. Lời giải chi tiết, trình bày đầy đủ các bước
3. Dùng `enumerate` để liệt kê danh sách (nếu có)
4. Công thức nhiều dòng dùng `eqnarray*`:
```latex
\begin{eqnarray*}
  f(x) & = & (x+1)^2 \\
       & = & x^2 + 2x + 1
\end{eqnarray*}
```

## Ví dụ hoàn chỉnh

```latex
%%%=============BT_1=============%%%
\begin{bt}%[0H2V1-4]
	Một hộ gia đình mua than đá làm nhiên liệu đun nấu và trung bình mỗi ngày dùng hết $1{,}60$ kg than. Giả thiết loại than đá trên chứa $90\%$ carbon về khối lượng, còn lại là các tạp chất trơ.
	Cho phản ứng đốt cháy carbon: $C(s) + O_2(g) \xrightarrow CO_2(g) \quad \Delta_rH^\circ_{298} = -393{,}50$ kJ.
	Tính nhiệt lượng cung cấp cho hộ gia đình từ quá trình đốt than trong một ngày theo đơn vị kWh. Biết rằng $1$ kWh $= 3600$ kJ. (Cho $M_C = 12$. Kết quả làm tròn đến hàng đơn vị).
	\loigiai{
		Khối lượng than sử dụng mỗi ngày: $m_{than} = 1{,}60 \text{ kg} = 1600 \text{ g}$.
		\\
		Khối lượng carbon trong than:
		\[ m_C = 1600 \times 0{,}90 = 1440 \text{ g} \]
		Số mol carbon bị đốt cháy:
		\[ n_C = \dfrac{1440}{12} = 120 \text{ mol} \]
		Nhiệt lượng tỏa ra khi đốt cháy $120$ mol C:
		\[ Q = 120 \times 393{,}50 = 47220 \text{ kJ} \]
		Đổi sang kWh:
		\[ \text{Số điện} = \dfrac{47220}{3600} \approx 13 \text{ kWh} \]
	}
\end{bt}

%%%=============BT_2=============%%%
\begin{bt}%[9K8V2-4]
	Cân bằng phương trình hóa học sau bằng phương pháp thăng bằng electron:
	\[ Fe + HNO_3 \xrightarrow Fe{(NO_3)}_3 + NO + H_2O \]
	\loigiai{
		Xác định số oxi hóa các nguyên tố thay đổi:
		\begin{itemize}
			\item $\overset{0}{Fe} \xrightarrow \overset{+3}{Fe}$: Fe nhường 3e (quá trình oxi hóa)
			\item $\overset{+5}{N} \xrightarrow \overset{+2}{N}$: N nhận 3e (quá trình khử)
		\end{itemize}
		Thăng bằng electron:
		\begin{eqnarray*}
			\text{Oxi hóa:} & Fe \xrightarrow Fe^{3+} + 3e & \times 1 \\
			\text{Khử:} & N^{+5} + 3e \xrightarrow N^{+2} & \times 1
		\end{eqnarray*}
		Phương trình cân bằng:
		\[ Fe + 4HNO_3 \xrightarrow Fe{(NO_3)}_3 + NO\uparrow + 2H_2O \]
	}
\end{bt}
```
