# Loại 1: Trắc nghiệm nhiều lựa chọn (EX)

## Cấu trúc LaTeX

```latex
%%%============EX_<số thứ tự>=============%%%
\begin{ex}%[<ID6>]
Nội dung câu hỏi trắc nghiệm nhiều lựa chọn
\choice
{Nội dung phương án 1}
{Nội dung phương án 2}
{\True Nội dung phương án 3 (đáp án đúng)}
{Nội dung phương án 4}
\loigiai{Nội dung lời giải chi tiết}
\end{ex}
```

## Quy tắc bắt buộc

1. Lệnh `\choice` phải đủ **4 tham số** `\choice{}{}{}{}` — không được bỏ trống
2. Chỉ có **1 phương án đúng** duy nhất, đặt `\True` ngay trước nội dung phương án đúng
3. Các phương án **không có dấu chấm** ở cuối
4. Phải có dòng đánh số: `%%%============EX_<số>=============%%%`
5. Phải có `%[ID6]` sau `\begin{ex}`

## Ví dụ hoàn chỉnh

```latex
%%%=============EX_1=============%%%
\begin{ex}%[9K8H1-1]
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

%%%=============EX_2=============%%%
\begin{ex}%[0H1N2-1]
Liên kết hóa học trong phân tử $H_2$ thuộc loại liên kết nào?
\choice
{Liên kết ion}
{Liên kết cho nhận}
{\True Liên kết cộng hóa trị không cực}
{Liên kết cộng hóa trị có cực}
\loigiai{
	Phân tử $H_2$ được tạo thành từ hai nguyên tử cùng loại ($H$), có độ âm điện bằng nhau nên cặp electron dùng chung không lệch về phía nguyên tử nào. Do đó liên kết trong $H_2$ là liên kết cộng hóa trị không cực.
}
\end{ex}
```

## Lưu ý nội dung

- Các số, công thức, ký hiệu inline phải bọc trong `$...$`
- Công thức display bọc bởi `\[...\]` (không dùng `$$...$$`)
- Số thập phân dùng `{,}` thay vì `.`: `$3{,}14$`
- Dùng `\dfrac` thay cho `\frac`
- Chỉ số: `$Al_2{(SO_4)}_3$` (không dùng ký tự Unicode superscript)
