# Ví Dụ Sử Dụng Skill ke-hoach-day-hoc

> **Lưu ý về đường dẫn**: Các lệnh dưới đây dùng các placeholder:
> - `<SCRIPT>` → đường dẫn tuyệt đối đến `scripts/khbd_generator.py` trong thư mục skill
> - `<THU_MUC_MAU>` → thư mục chứa file KHBD mẫu (hỏi người dùng)
> - `<OUTPUT_DIR>` → thư mục đầu ra (hỏi người dùng)
> - `<CONTENT_JSON>` → file JSON đầu vào (xuất từ lệnh `analyze`)

## Ví dụ 1: Tạo KHBD Hóa học - Bài 21

### Input (JSON nội dung)

Khi sử dụng `--content-json`, file JSON cần có cấu trúc như sau:

```json
{
  "truong": "THCS Nguyễn Du",
  "to_bo_mon": "Khoa học tự nhiên",
  "ten_gv": "Nguyễn Thị Lan",
  "ten_bai": "Bài 21. Sự khác nhau cơ bản giữa phi kim và kim loại",
  "mon_hoc": "Hóa học",
  "lop": 9,
  "so_tiet": 5,
  "muc_tieu": {
    "kien_thuc": [
      "- Nêu được ứng dụng của một số đơn chất phi kim thiết thực trong cuộc sống (carbon, lưu huỳnh, khí chlorine,...).",
      "- Chỉ ra được sự khác nhau cơ bản về một số tính chất giữa phi kim và kim loại: Khả năng dẫn điện, nhiệt độ nóng chảy, nhiệt độ sôi, khối lượng riêng; khả năng tạo ion dương, ion âm; phản ứng với oxygen tạo oxide acid, oxide base."
    ],
    "nang_luc_chung": [
      "- Tự chủ và tự học: Chủ động tìm kiếm thông tin, đọc SGK, nêu được ứng dụng của một số phi kim phổ biến trong thực tiễn.",
      "- Giao tiếp và hợp tác: Hoạt động nhóm một cách hiệu quả theo đúng yêu cầu của GV, đảm bảo các thành viên trong nhóm đều được tham gia.",
      "- Giải quyết vấn đề và sáng tạo: Giải quyết vấn đề kịp thời với các thành viên trong nhóm để thảo luận hiệu quả."
    ],
    "nang_luc_khtn": [
      "- Nhận thức khoa học tự nhiên: Nêu được ứng dụng của một số đơn chất phi kim thiết thực trong cuộc sống.",
      "- Tìm hiểu tự nhiên: Quan sát và so sánh các dữ liệu, nhận xét, rút ra được sự khác nhau cơ bản giữa phi kim và kim loại.",
      "- Vận dụng kiến thức: Giải thích được hiện tượng thực tế liên quan đến tính chất phi kim."
    ],
    "pham_chat": [
      "- Chăm chỉ: Chủ động tích cực đọc tài liệu, nghiên cứu SGK.",
      "- Trách nhiệm: Chủ động hoàn thành các nhiệm vụ được giao khi làm việc nhóm."
    ]
  },
  "thiet_bi": {
    "dung_cu_hoa_chat": [
      "Máy chiếu, bảng nhóm, bảng phụ.",
      "GV chia lớp học thành các nhóm. Mỗi nhóm bốc thăm trước để tìm hiểu ở nhà và làm báo cáo (poster giấy hoặc slide)."
    ],
    "phieu_hoc_tap": [
      "PHT số 1: Phiếu so sánh tính chất phi kim và kim loại (bảng 2 cột: Kim loại | Phi kim).",
      "PHT số 2: Bài tập trắc nghiệm 10 câu về phi kim và kim loại."
    ]
  },
  "phuong_phap": [
    "- Dạy học theo nhóm, nhóm cặp đôi.",
    "- Kĩ thuật công não, động não, khăn trải bàn.",
    "- Dạy học nêu và giải quyết vấn đề thông qua câu hỏi trong SGK."
  ],
  "hoat_dong": [
    {
      "so_thu_tu": 1,
      "ten": "Khởi động",
      "muc_tieu": "HS hứng thú, ham thích khám phá, tìm hiểu về phi kim.",
      "noi_dung": "GV cho học sinh nêu một số ứng dụng của kim loại và phi kim mà đã được biết.",
      "san_pham": "Các ứng dụng HS biết: Chất tẩy rửa, sản xuất dược phẩm... Oxygen, Carbon hoạt tính, Lưu huỳnh, Chlorine,...",
      "to_chuc": [
        {
          "gv": "Giao nhiệm vụ:\nGiáo viên đặt vấn đề: Bên cạnh sự phổ biến của kim loại trong cuộc sống, một số phi kim cũng có nhiều ứng dụng thiết thực.\nGV chia lớp thành 4 nhóm, các nhóm có 3 phút thảo luận và liệt kê các ứng dụng của phi kim mà em biết.",
          "hs": "HS thảo luận nhóm thực hiện theo yêu cầu của GV."
        },
        {
          "gv": "Hướng dẫn HS thực hiện nhiệm vụ:\nHS thảo luận, viết các nội dung theo yêu cầu lên bảng nhóm.",
          "hs": "Nhận nhiệm vụ, thảo luận và ghi kết quả."
        },
        {
          "gv": "Báo cáo, thảo luận:\nHS suy nghĩ, có thể thảo luận với nhau. Giáo viên nhận xét câu trả lời của học sinh và dẫn dắt vào bài học mới.",
          "hs": "Thực hiện nhiệm vụ. Đại diện nhóm trình bày."
        },
        {
          "gv": "Chốt lại và đặt vấn đề vào bài:\nBên cạnh sự phổ biến của kim loại, phi kim cũng có nhiều ứng dụng thiết thực. Dựa vào sự khác biệt về tính chất mà mỗi loại có những ứng dụng phù hợp. Bài hôm nay chúng ta sẽ tìm hiểu chi tiết hơn...",
          "hs": "Lắng nghe, xác định vấn đề cần tìm hiểu."
        }
      ]
    },
    {
      "so_thu_tu": 2,
      "ten": "Hình thành kiến thức mới",
      "muc_tieu": "- Nêu được ứng dụng của một số đơn chất phi kim thiết thực.\n- Chỉ ra được sự khác nhau cơ bản về tính chất giữa phi kim và kim loại.",
      "noi_dung": "HS trình bày báo cáo đã chuẩn bị ở nhà về các phi kim (Carbon, Lưu huỳnh, Chlorine, Oxygen). Sau đó nghiên cứu SGK và hoàn thành bảng so sánh tính chất kim loại - phi kim.",
      "san_pham": "Báo cáo của HS về từng phi kim. Bảng so sánh tính chất kim loại và phi kim hoàn chỉnh.",
      "to_chuc": [
        {
          "gv": "Giao nhiệm vụ:\nGV yêu cầu lần lượt các nhóm HS trình bày báo cáo về đề tài đã chọn (Carbon, Lưu huỳnh, Chlorine, Oxygen). Thời gian mỗi nhóm: 12-15 phút.",
          "hs": "HS nhận nhiệm vụ. Nhóm được gọi chuẩn bị trình bày."
        },
        {
          "gv": "Hướng dẫn HS thực hiện nhiệm vụ:\nCác nhóm HS báo cáo theo thứ tự. GV quan sát, lắng nghe và ghi nhận.",
          "hs": "Thảo luận nhóm, trình bày báo cáo."
        },
        {
          "gv": "Báo cáo kết quả:\nGọi 1 nhóm đại diện trình bày kết quả. Các nhóm khác bổ sung. GV nhận xét, đánh giá dựa trên mức độ chính xác và chi tiết của báo cáo.",
          "hs": "Nhóm khác nhận xét phần trình bày. Bổ sung ý kiến."
        },
        {
          "gv": "Tổng kết:\nI. ỨNG DỤNG CỦA MỘT SỐ PHI KIM QUAN TRỌNG\nII. SỰ KHÁC NHAU GIỮA PHI KIM VÀ KIM LOẠI\nGV chiếu bảng tóm tắt so sánh, chốt kiến thức trọng tâm.",
          "hs": "Ghi nhớ kiến thức. Hoàn thiện bảng so sánh vào PHT."
        }
      ]
    },
    {
      "so_thu_tu": 3,
      "ten": "Luyện tập",
      "muc_tieu": "Vận dụng kiến thức của bài học vào việc làm bài tập cụ thể. Giải thích được sự khác nhau trong tính chất hóa học của kim loại với phi kim.",
      "noi_dung": "GV cho học sinh làm việc cá nhân và trả lời một số câu hỏi trắc nghiệm trên phần mềm Quizziz/LMS 360 hoặc bảng nhóm.",
      "san_pham": "Đáp án: 1-A, 2-C, 3-B, 4-A, 5-A, 6-C, 7-D, 8-A, 9-A, 10-A.",
      "to_chuc": [
        {
          "gv": "Giao nhiệm vụ:\nTổ chức vận dụng trên phần mềm Quizziz. Có 10 câu hỏi. Mỗi câu có thời gian suy nghĩ và trả lời là 20-30 giây.",
          "hs": "Học sinh sử dụng điện thoại quét mã QR đăng nhập và vào tham gia trò chơi trực tuyến."
        },
        {
          "gv": "HS thực hiện nhiệm vụ:\nGV quan sát màn hình, theo dõi kết quả từng câu.",
          "hs": "Học sinh trả lời câu hỏi."
        },
        {
          "gv": "Báo cáo kết quả:\nCho cả lớp xem kết quả; mời đại diện giải thích đáp án các câu sai nhiều nhất. GV kết luận về nội dung kiến thức.",
          "hs": "Trình bày giải thích đáp án. Lắng nghe nhận xét."
        },
        {
          "gv": "Tổng kết:\nNhận xét chung về kết quả luyện tập. Nhấn mạnh các điểm HS hay nhầm lẫn.",
          "hs": "Ghi nhớ kiến thức. Sửa bài vào vở."
        }
      ]
    },
    {
      "so_thu_tu": 4,
      "ten": "Vận dụng",
      "muc_tieu": "Vận dụng kiến thức về tính chất vật lí của phi kim (carbon hoạt tính) để giải thích vấn đề trong thực tế.",
      "noi_dung": "Học sinh làm bài tập vận dụng thực tế:\nCâu 1: Nêu ứng dụng của than chì. Giải thích tại sao than hoạt tính được dùng trong lọc nước.\nCâu 2: Tính nhiệt lượng tỏa ra khi đốt 5 kg than có 90% carbon.",
      "san_pham": "Câu 1: a) Ứng dụng than chì: điện cực, ruột bút chì, lọc nước,... b) Than hoạt tính hút bám chất bẩn, độc tố.\nCâu 2: m(C) = 4,5 kg; Nhiệt lượng = (4500/12) × 394 kJ",
      "to_chuc": [
        {
          "gv": "Giao nhiệm vụ:\nGV hướng dẫn HS về nhà tìm hiểu:\nCâu 1: a) Nêu ứng dụng của than chì trong đời sống.\nb) Giải thích cơ chế lọc nước của than hoạt tính.\nCâu 2: Tính nhiệt lượng khi đốt 5 kg than 90% carbon.",
          "hs": "HS ghi chép những câu hỏi và lời dặn của GV để về nhà tìm hiểu thêm."
        },
        {
          "gv": "Hướng dẫn thực hiện:\nGV hướng dẫn nguồn tìm kiếm: SGK, sách bài tập, internet (trang tin cậy).",
          "hs": "Thực hiện nhiệm vụ ở nhà."
        },
        {
          "gv": "Báo cáo kết quả (buổi sau):\nHS báo cáo kết quả, trả lời câu hỏi. GV nhận xét, chấm điểm.",
          "hs": "Nộp bài. Trình bày kết quả nếu được gọi."
        },
        {
          "gv": "Kết luận, nhận định:\nNhận xét ý thức làm bài của HS. Nhắc nhở HS không nộp bài (nếu có). Dặn dò chuẩn bị bài học sau.",
          "hs": "Lắng nghe nhận xét. Ghi chép bài học tiếp theo."
        }
      ]
    }
  ]
}
```

### Lệnh tạo KHBD

```bash
# Lưu nội dung JSON trên vào file: content_bai21.json
# Sau đó chạy:

uv run <SCRIPT> generate \
  --ten-bai "Bài 21. Sự khác nhau cơ bản giữa phi kim và kim loại" \
  --mon-hoc "Hóa học" \
  --so-tiet 5 \
  --lop 9 \
  --content-json "<CONTENT_JSON>" \
  --output "<OUTPUT_DIR>/KHBD_Bai21_HoaHoc_KNTT.docx"
```

### Kết quả đầu ra

File `KHBD_Bai21_HoaHoc_KNTT.docx` với:
- Header thông tin trường/GV
- I. MỤC TIÊU (Kiến thức, Năng lực, Phẩm chất)
- II. THIẾT BỊ DẠY HỌC (Dụng cụ, PHT)
- III. TIẾN TRÌNH (Phương pháp + 4 Hoạt động với bảng GV-HS)

---

## Ví dụ 2: Tạo KHBD nhanh (AI tự sinh nội dung)

```bash
uv run <SCRIPT> generate \
  --ten-bai "Bài 37. Các quy luật di truyền của Menđen" \
  --mon-hoc "Sinh học" \
  --so-tiet 4 \
  --lop 9 \
  --ten-gv "Trần Văn B" \
  --truong "THCS Lê Quý Đôn" \
  --output "<OUTPUT_DIR>/KHBD_Bai37_Sinh.docx"
```

---

## Ví dụ 3: Phân tích file mẫu rồi tạo KHBD mới

*Lưu ý: Bạn có thể thay thế `<THU_MUC_MAU>` và `<OUTPUT_DIR>` bằng đường dẫn thực tế trên máy tính của bạn để đảm bảo tính di động.*

```bash
# Bước 1: Liệt kê file mẫu trong thư mục tham chiếu
uv run <SCRIPT> list-samples \
  --ref-dir "<THU_MUC_MAU>" \
  --output "<OUTPUT_DIR>/vat_li_files.json"

# Bước 2: Chọn file mẫu phù hợp từ danh sách, rồi phân tích
uv run <SCRIPT> analyze \
  --input "<THU_MUC_MAU>/KNTT_BÀI 11 - ĐIỆN TRỞ. ĐỊNH LUẬT OHM.docx" \
  --output "<OUTPUT_DIR>/analysis_Bai11.json"

# Bước 3: Tạo KHBD mới từ nội dung đã phân tích
uv run <SCRIPT> generate \
  --ten-bai "Bài 11. Điện trở. Định luật Ohm" \
  --mon-hoc "Vật lí" \
  --so-tiet 3 \
  --lop 9 \
  --content-json "<OUTPUT_DIR>/analysis_Bai11.json" \
  --output "<OUTPUT_DIR>/KHBD_Bai11_VatLi.docx"
```
