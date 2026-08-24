# Quy tắc cào có trách nhiệm — RÀNG BUỘC, không phải gợi ý

Nguồn chuẩn robots.txt: [Google — How Google interprets the robots.txt spec](https://developers.google.com/search/docs/crawling-indexing/robots/robots_txt) (dựa trên chuẩn robots.txt gốc của Martijn Koster, xem thêm [robotstxt.org](https://www.robotstxt.org/)). Nguồn `urllib.robotparser`: [Python 3 docs](https://docs.python.org/3/library/urllib.robotparser.html).

## 1. Đọc và tuân thủ `robots.txt`

### Cú pháp chuẩn

File `robots.txt` nằm ở gốc domain (`https://example.com/robots.txt`), mã hoá UTF-8, mỗi dòng dạng `<field>: <value>`, dòng bắt đầu bằng `#` là comment.

| Directive | Ý nghĩa | Ví dụ |
|---|---|---|
| `User-agent` | Áp dụng rule cho crawler nào; `*` = mọi crawler | `User-agent: *` |
| `Disallow` | Đường dẫn KHÔNG được cào (phân biệt hoa/thường, tính từ gốc domain) | `Disallow: /admin/` |
| `Allow` | Ngoại lệ cho phép trong vùng bị `Disallow` — rule dài/cụ thể hơn thắng | `Allow: /admin/public/` |
| `Crawl-delay` | Số giây tối thiểu phải nghỉ giữa 2 request (không phải mọi bot tôn trọng, Google bỏ qua, nhưng **ta luôn tôn trọng**) | `Crawl-delay: 10` |
| `Sitemap` | URL tuyệt đối tới sitemap XML — có thể có nhiều dòng | `Sitemap: https://example.com/sitemap.xml` |
| Wildcard `*` | Khớp 0 hoặc nhiều ký tự trong path | `Disallow: /*.pdf$` |
| Wildcard `$` | Khớp cuối URL | như trên |

Quy tắc chọn rule khi nhiều rule khớp: rule có **path dài/cụ thể hơn** thắng; nếu bằng độ dài, rule ít hạn chế hơn thắng (theo cách Google diễn giải).

### Đọc bằng Python — `urllib.robotparser` (thư viện chuẩn, không cần cài thêm)

```python
import urllib.robotparser as robotparser

def kiem_tra_duoc_phep(url: str, user_agent: str = "*") -> bool:
    from urllib.parse import urlparse
    parsed = urlparse(url)
    robots_url = f"{parsed.scheme}://{parsed.netloc}/robots.txt"

    rp = robotparser.RobotFileParser()
    rp.set_url(robots_url)
    rp.read()  # tải và parse robots.txt; nếu 404 -> coi như cho phép tất cả

    return rp.can_fetch(user_agent, url)

def lay_crawl_delay(url: str, user_agent: str = "*"):
    from urllib.parse import urlparse
    parsed = urlparse(url)
    rp = robotparser.RobotFileParser()
    rp.set_url(f"{parsed.scheme}://{parsed.netloc}/robots.txt")
    rp.read()
    return rp.crawl_delay(user_agent)  # None nếu không có

# Sử dụng trước MỌI lần cào:
url = "https://example.edu.vn/de-thi/khtn-6"
if kiem_tra_duoc_phep(url):
    delay = lay_crawl_delay(url) or 2  # mặc định 2s nếu robots.txt không nói
    # ... tiến hành fetch, nghỉ `delay` giây giữa các request
else:
    print(f"robots.txt cấm cào: {url} — DỪNG, không cào")
```

**Bắt buộc:** gọi hàm kiểm tra này TRƯỚC mỗi lần cào một domain mới. Nếu `Disallow` áp dụng cho path cần cào → dừng, không tìm cách lách.

## 2. Rate limiting — vì sao và bao nhiêu là hợp lý

**Vì sao:** gửi request dồn dập có thể làm quá tải server (đặc biệt server nhỏ của trường/sở giáo dục), khiến trang chậm/sập cho người dùng thật, và khiến IP của bạn bị chặn vĩnh viễn.

**Đặt bao nhiêu:**
- Mặc định an toàn: **1 request mỗi 1–3 giây** cho site không có `Crawl-delay`.
- Nếu `robots.txt` có `Crawl-delay: N` → dùng đúng N giây, không rút ngắn.
- Site nhỏ/cá nhân (trường học, giáo viên tự làm web) → nên giãn cách rộng hơn (3–5 giây), vì hạ tầng thường yếu.
- Không chạy nhiều luồng/tab song song nhắm vào CÙNG một domain — tổng tốc độ request tới 1 domain phải giữ ở mức trên dù có bao nhiêu luồng.

**Jitter (độ trễ ngẫu nhiên):** cộng thêm nhiễu ngẫu nhiên vào delay để tránh pattern đều đặn dễ bị phát hiện là bot, đồng thời tránh gửi request đồng loạt đúng nhịp gây áp lực đỉnh (spike) lên server:
```python
import time, random

def nghi_giua_request(base_delay: float = 2.0, jitter: float = 1.0):
    time.sleep(base_delay + random.uniform(0, jitter))

# Trong vòng lặp cào nhiều trang:
for url in danh_sach_url:
    page = Fetcher.get(url)
    # ... xử lý page ...
    nghi_giua_request(base_delay=2.0, jitter=1.0)  # nghỉ 2.0–3.0 giây, ngẫu nhiên
```

## 3. Ranh giới rõ ràng — KHÔNG được làm

Dù kỹ thuật có khả thi, các hành vi sau đây **bị cấm tuyệt đối** khi dùng skill này:

1. **Vượt tường đăng nhập / paywall** — không dùng tài khoản (kể cả tài khoản hợp lệ của người dùng) để cào nội dung trả phí/riêng tư rồi lưu trữ hàng loạt hoặc phát tán.
2. **Giải captcha** — không viết code/gọi dịch vụ giải captcha (reCAPTCHA, hCaptcha, ảnh xác thực). Nếu gặp captcha, dừng lại.
3. **Cào dữ liệu cá nhân** — không thu thập tên/số điện thoại/email/địa chỉ của cá nhân (VD: danh sách học sinh, phụ huynh) trừ khi có sự đồng ý rõ ràng và mục đích hợp pháp cụ thể.
4. **Tải hàng loạt tài liệu có bản quyền để phát tán lại** — không tải toàn bộ SGK, sách tham khảo, ngân hàng đề có bản quyền rồi đăng lại/chia sẻ công khai/bán.
5. **Gửi request với tần suất gây hại** — không bỏ qua rate limiting, không chạy crawl song song ồ ạt vào 1 server nhỏ, không cố tình gây DoS.
6. **Giả mạo danh tính để lách chặn có chủ đích** — dùng `stealthy_headers`/`impersonate`/`StealthyFetcher` để trang web hiển thị bình thường (như trình duyệt thật) là chấp nhận được cho mục đích thu thập dữ liệu công khai hợp pháp, nhưng KHÔNG dùng các kỹ thuật này để cố tình vượt qua rào chắn mà chủ sở hữu đã dựng lên nhằm CẤM truy cập (khác với chặn vì lý do kỹ thuật/tối ưu bot xấu).

## 4. Dữ liệu công khai vs. dữ liệu có điều kiện truy cập

| Loại | Đặc điểm | Được cào? |
|---|---|---|
| Công khai, không cần đăng nhập, không bị `robots.txt` chặn | Ai cũng xem được khi mở link trực tiếp (VD: trang đề thi công khai của Sở GD&ĐT) | Được, tuân thủ rate limit |
| Công khai nhưng `robots.txt` disallow | Trang cho xem tự do nhưng chủ sở hữu đã nói rõ không muốn bị crawl | KHÔNG — tôn trọng `Disallow` dù kỹ thuật vẫn truy cập được |
| Cần đăng nhập / có phân quyền | Nội dung chỉ thấy sau khi login (VD: thư viện đề thi nội bộ trường, tài khoản LMS) | KHÔNG cào tự động kể cả khi dùng session đã đăng nhập, trừ khi đó là dữ liệu CỦA CHÍNH người dùng và họ tự thao tác thủ công |
| Trả phí (paywall) | Cần mua/trả tiền để xem | KHÔNG, kể cả khi có cách lách kỹ thuật |

## 5. Bối cảnh Việt Nam — giáo dục, SGK, đề thi

- **Bản quyền SGK:** sách giáo khoa (Kết nối tri thức, Cánh Diều, Chân trời sáng tạo...) có bản quyền thuộc nhà xuất bản. Cào ảnh/text/PDF từ trang bán sách điện tử hoặc trang lậu để LƯU DÙNG CÁ NHÂN (tham khảo khi soạn giáo án) khác về mức độ rủi ro so với TẢI HÀNG LOẠT rồi đăng lại công khai hoặc chia sẻ cho nhiều người — chỉ làm việc đầu, không làm việc sau.
- **Đề thi:** đề thi do trường/Sở/Phòng GD&ĐT công bố công khai (không robots.txt chặn, không cần đăng nhập) thường được xem là tài liệu phục vụ cộng đồng giáo viên — cào để tổng hợp/tham khảo là hợp lý. Đề thi từ các trang thương mại (bán đề, có tường phí) thì áp dụng đúng quy tắc paywall ở mục 4 — không lách.
- **Mục đích cá nhân vs. phát tán lại:** dùng dữ liệu cào được để giáo viên tự soạn bài, tự đối chiếu, tự lưu trữ tham khảo là mục đích cá nhân — chấp nhận được trong phạm vi hợp lý (fair use cho giáo dục). Đăng lại nguyên văn, bán, hoặc phát tán hàng loạt tài liệu có bản quyền cho người khác là VƯỢT ranh giới — không làm.
- Khi không chắc một nguồn có cho phép cào hay không (không có robots.txt rõ ràng, không có điều khoản sử dụng công khai) → mặc định thận trọng: cào ít, tần suất thấp, chỉ lấy phần cần thiết, không lưu trữ lâu dài/không phát tán.

## 6. Checklist ngắn — tự rà TRƯỚC mỗi lần cào

- [ ] Đã kiểm tra `robots.txt` của domain bằng `urllib.robotparser`, path cần cào không bị `Disallow`.
- [ ] Đã đọc `Crawl-delay` (nếu có) và đặt delay giữa các request >= giá trị đó (mặc định >= 2s + jitter nếu không có).
- [ ] Trang không yêu cầu đăng nhập/paywall để xem nội dung cần lấy.
- [ ] Không có captcha chặn đường — nếu có, đã dừng, không tìm cách giải.
- [ ] Dữ liệu lấy về không chứa thông tin cá nhân của học sinh/phụ huynh/giáo viên khác ngoài phạm vi công khai cần thiết.
- [ ] Mục đích sử dụng là cá nhân/giảng dạy, không phát tán hàng loạt/thương mại hoá tài liệu có bản quyền.
- [ ] Không chạy nhiều luồng song song dồn vào cùng 1 domain vượt quá rate limit đã đặt.
- [ ] Đã chọn fetcher tối thiểu cần thiết (ưu tiên `Fetcher`, chỉ nâng cấp khi bắt buộc — xem `fetcher-selection.md`) để không gây tải không cần thiết lên cả máy mình lẫn server đích.
