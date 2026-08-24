# Chọn đúng Fetcher — máy chỉ 8 GB RAM, đừng mở trình duyệt bừa bãi

Nguồn API tham số: xem `scrapling-api.md`. Nguồn gốc: [Fetchers basics — Scrapling docs](https://scrapling.readthedocs.io/en/latest/fetching/choosing.html), [DynamicFetcher docs](https://scrapling.readthedocs.io/en/latest/fetching/dynamic.html), [StealthyFetcher docs](https://scrapling.readthedocs.io/en/latest/fetching/stealthy.html).

## 1. Cây quyết định

```
BẮT ĐẦU
  │
  ▼
Thử Fetcher.get(url) trước — LUÔN LUÔN, không ngoại lệ
  │
  ▼
HTML trả về có chứa nội dung cần cào không? (đọc "Dấu hiệu cần JS" bên dưới)
  │
  ├── CÓ  → Dùng Fetcher (RAM ~vài chục MB, xong)
  │
  └── KHÔNG → Trước khi mở trình duyệt: có API JSON nội bộ không?
                (xem mục 3 "Mẹo tránh mở trình duyệt")
        │
        ├── CÓ  → Gọi thẳng API bằng Fetcher.get()/post() → xong, KHÔNG mở trình duyệt
        │
        └── KHÔNG → Bắt buộc render JS
                │
                ▼
        Trang có bị chặn nặng không? (403/429/503 lặp lại dù đổi header,
        Cloudflare challenge, captcha xuất hiện)
                │
                ├── KHÔNG → DynamicFetcher (RAM trung bình, đủ dùng cho SPA thường)
                │
                └── CÓ    → StealthyFetcher (RAM cao nhất, chỉ dùng khi thực sự cần
                             vượt Cloudflare Turnstile/anti-bot mạnh)
```

**Nguyên tắc với máy 8 GB RAM:** mỗi phiên trình duyệt (`DynamicFetcher`/`StealthyFetcher`) có thể chiếm 200–500+ MB tuỳ trang; mở nhiều tab/nhiều phiên song song rất dễ khiến máy treo/swap. Luôn ưu tiên nhánh trái của cây quyết định.

## 2. Dấu hiệu nhận biết trang CẦN JavaScript

Sau khi `Fetcher.get(url)`, kiểm tra `page.css(...)`. Nếu gặp MỘT trong các dấu hiệu sau, khả năng cao trang render bằng JS phía client:

| Dấu hiệu | Cách kiểm tra nhanh |
|---|---|
| Nội dung chính rỗng | `page.css('.product, .article, .content')` trả `[]` dù trang hiển thị đầy nội dung trên trình duyệt thật |
| Có `<div id="root">` hoặc `<div id="app">` rỗng | `page.css('#root, #app')[0].get_all_text().strip()` là chuỗi rỗng |
| Dữ liệu nằm trong `<script>` dạng JSON | Thấy `<script id="__NEXT_DATA__">`, `<script type="application/json">`, hoặc biến `window.__INITIAL_STATE__ = {...}` trong HTML thô — đây là dấu hiệu TỐT (xem mục 3, có thể lấy trực tiếp không cần trình duyệt) |
| Framework SPA | HTML chứa `data-reactroot`, `ng-app`, `v-app`, thẻ `<script src=".../vue.js">`, `.../react-dom...`, hoặc bundle Webpack/Vite (`/_next/`, `/assets/index-*.js`) |
| HTML rất ngắn (< 5–10 KB) nhưng trang hiển thị nhiều nội dung khi mở bằng trình duyệt | So sánh `len(page.html_content)` với những gì thấy trên trình duyệt |

Nếu KHÔNG gặp dấu hiệu nào ở trên và `page.css(...)` đã lấy được dữ liệu mong muốn → dùng `Fetcher`, dừng ở đây, không cần đọc tiếp.

## 3. Mẹo tránh mở trình duyệt: tìm API JSON nội bộ (giá trị cao nhất)

Rất nhiều trang "động" thực chất chỉ render khung rỗng bằng JS rồi gọi một API JSON nội bộ để lấy dữ liệu thật. Gọi thẳng API đó bằng `Fetcher` nhanh hơn `DynamicFetcher`/`StealthyFetcher` hàng chục lần và tốn RAM gần như bằng 0.

### Quy trình tìm endpoint bằng DevTools (Chrome/Edge/Firefox)

1. Mở trang web trong trình duyệt thường (không phải qua Scrapling).
2. Nhấn `F12` (hoặc chuột phải → *Kiểm tra*) → mở tab **Network**.
3. Lọc theo loại `Fetch/XHR` (Chrome) hoặc `XHR` (Firefox) — bỏ qua ảnh, CSS, font.
4. Tick **Preserve log** (giữ log khi chuyển trang) nếu cần.
5. Tải lại trang (`F5`) hoặc thực hiện thao tác sinh ra dữ liệu (cuộn, bấm "Xem thêm", tìm kiếm...).
6. Quan sát danh sách request mới xuất hiện — tìm request có:
   - Đuôi phản hồi là `.json` hoặc header `Content-Type: application/json`.
   - Tên gợi ý dữ liệu: `/api/`, `/graphql`, `/search`, `/questions`, `/exams`, `/v1/...`.
7. Click vào request đó → tab **Response**/**Preview** để xem cấu trúc JSON có đúng dữ liệu cần không.
8. Click phải request → **Copy → Copy as cURL** (hoặc xem tab **Headers**) để lấy:
   - URL đầy đủ (kể cả query string).
   - Method (GET/POST).
   - Header cần thiết (thường chỉ cần `Accept`, đôi khi cần `Referer`, `X-Requested-With`, hoặc token trong header/cookie — nếu có token đăng nhập riêng tư thì KHÔNG dùng, xem `scraping-ethics.md`).
   - Body (nếu POST) — thường là JSON hoặc form data chứa tham số phân trang (`page`, `limit`, `offset`).

### Gọi thẳng bằng Fetcher sau khi tìm được endpoint

```python
from scrapling.fetchers import Fetcher

# Ví dụ: trang SPA hiển thị danh sách đề thi, DevTools cho thấy nó gọi:
# GET https://example.edu.vn/api/exams?subject=khtn&page=1
page = Fetcher.get(
    'https://example.edu.vn/api/exams',
    params={'subject': 'khtn', 'page': 1},
    stealthy_headers=True,
)
data = page.json()          # Response hỗ trợ .json() trực tiếp nếu là JSON hợp lệ
for item in data['items']:
    print(item['title'], item['download_url'])
```

Nếu API yêu cầu header đặc biệt (không phải auth cá nhân, ví dụ `Referer` hoặc `X-Requested-With: XMLHttpRequest`):
```python
page = Fetcher.get(
    'https://example.edu.vn/api/exams',
    headers={'Referer': 'https://example.edu.vn/de-thi', 'X-Requested-With': 'XMLHttpRequest'},
)
```

### Khi không tìm được endpoint rõ ràng nhưng thấy JSON nhúng trong HTML

Một số trang (Next.js, Nuxt) nhúng toàn bộ dữ liệu vào `<script id="__NEXT_DATA__" type="application/json">`. Lấy trực tiếp bằng `Fetcher`, không cần trình duyệt:
```python
page = Fetcher.get(url)
script = page.css('script#__NEXT_DATA__::text').get()
import json
data = json.loads(str(script)) if script else None
```

### Nếu vẫn phải dùng capture_xhr (khi endpoint khó tái tạo thủ công)

Trường hợp API có chữ ký/token động phức tạp, khó gọi lại bằng `Fetcher`, có thể để `DynamicFetcher`/`StealthyFetcher` tự "nghe" và bắt response XHR khi tải trang một lần, rồi tái sử dụng dữ liệu — đỡ phải mở trình duyệt lại lần sau:
```python
from scrapling.fetchers import DynamicSession
with DynamicSession(capture_xhr=r"https://example\.edu\.vn/api/.*") as session:
    page = session.fetch('https://example.edu.vn/de-thi')
    for xhr in page.captured_xhr:
        print(xhr.url, xhr.status)
```

## 4. Dấu hiệu bị chặn và cách xử lý

| Dấu hiệu | Ý nghĩa | Xử lý |
|---|---|---|
| HTTP 403 Forbidden | Server từ chối theo IP/header/User-Agent | Thử `stealthy_headers=True` hoặc `impersonate='chrome'` trong `Fetcher` trước; nếu vẫn 403 → có thể trang chặn cào, cân nhắc dừng lại (xem `scraping-ethics.md`) |
| HTTP 429 Too Many Requests | Bị rate-limit vì gửi quá nhanh | **Giảm tốc độ** — tăng khoảng nghỉ giữa request, KHÔNG đổi sang fetcher mạnh hơn để né |
| HTTP 503 Service Unavailable | Server quá tải, hoặc chặn tạm thời (đôi khi kèm Cloudflare) | Thử lại sau, giãn cách dài hơn; nếu luôn 503 kèm nội dung "Checking your browser" → là Cloudflare challenge, xem dòng dưới |
| Trang chỉ có tiêu đề "Just a moment...", "Checking your browser", hoặc HTML chứa `cf-browser-verification`/`cf_chl_` | Cloudflare challenge (JS/managed) | Cần `StealthyFetcher(solve_cloudflare=True, timeout=60000)` — bắt buộc trình duyệt, không có cách nào dùng `Fetcher` thuần |
| Xuất hiện captcha (reCAPTCHA, hCaptcha, ảnh chọn ô) | Chặn bằng captcha tương tác | Scrapling KHÔNG giải captcha ảnh/tương tác — đây là ranh giới KHÔNG được vượt (xem `scraping-ethics.md`), dừng cào trang đó |

Không nâng cấp fetcher để "né" 429 — rate-limit là tín hiệu cần giảm tốc độ, không phải cần ngụy trang mạnh hơn.

## 5. Mẹo tiết kiệm RAM khi buộc phải dùng trình duyệt

| Kỹ thuật | Cách làm | Lợi ích |
|---|---|---|
| Luôn `headless=True` | Mặc định đã là `True`; chỉ đặt `False` khi debug thủ công rồi trả lại `True` | Trình duyệt ẩn nhẹ hơn, không tốn RAM render giao diện |
| Tái dùng phiên | Dùng `DynamicSession`/`StealthySession` (context manager) thay vì gọi `.fetch()` rời rạc nhiều lần | 1 browser instance cho nhiều URL thay vì mở/đóng nhiều lần → tiết kiệm RAM + nhanh hơn nhiều |
| Giới hạn concurrency | Với `AsyncDynamicSession`/`AsyncStealthySession`, đặt `max_pages` nhỏ (2–3) trên máy 8 GB | Giới hạn số tab mở song song trong CÙNG 1 browser, tránh nổ RAM khi `asyncio.gather` nhiều URL |
| Chặn tài nguyên không cần thiết | `disable_resources=True` khi chỉ cần text | Chặn font/image/media/stylesheet — nhanh hơn ~25%, giảm RAM lẫn băng thông |
| Chặn quảng cáo/tracker | `block_ads=True` hoặc `blocked_domains={"ads.example.com"}` | Giảm request và bộ nhớ lãng phí cho domain không liên quan |
| Đóng session ngay khi xong | Luôn dùng `with ... as session:` để browser tự đóng, tránh rò rỉ tiến trình Chromium chạy nền | Tránh tích luỹ nhiều tiến trình Chromium ngầm ăn RAM |
| Không chạy song song nhiều StealthyFetcher độc lập | Nếu cần nhiều URL, gom vào 1 `StealthySession` với `max_pages` nhỏ thay vì mở nhiều instance riêng | 1 browser dùng chung nhẹ hơn nhiều so với N browser riêng |

Ví dụ kết hợp tiết kiệm RAM:
```python
from scrapling.fetchers import DynamicSession

with DynamicSession(headless=True, disable_resources=True, block_ads=True) as session:
    for url in urls:
        page = session.fetch(url, network_idle=True)
        # xử lý ngay, không giữ nhiều `page` lớn trong bộ nhớ cùng lúc
```

## 6. Tóm tắt quyết định 1 dòng

- Có dữ liệu qua `Fetcher.get()` bình thường → dùng `Fetcher`.
- Không thấy dữ liệu nhưng DevTools lộ ra API JSON → vẫn dùng `Fetcher`, gọi thẳng API.
- Web SPA thật sự cần render, không bị chặn nặng → `DynamicFetcher`.
- Bị Cloudflare/anti-bot mạnh chặn → `StealthyFetcher(solve_cloudflare=True)`, chấp nhận tốn RAM hơn vì không còn lựa chọn khác.
- Gặp captcha tương tác/đăng nhập → dừng, không cố vượt (ranh giới đạo đức).
