# Sổ tay API Scrapling 0.4.13 — tra nhanh

Nguồn: [GitHub D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) · [Docs chính thức](https://scrapling.readthedocs.io/en/latest/) (bản `main`, khớp version cài đặt 0.4.13 xác nhận qua `pyproject.toml`).

```python
from scrapling.fetchers import (
    Fetcher, AsyncFetcher, StealthyFetcher, DynamicFetcher,
    FetcherSession, AsyncStealthySession, StealthySession,
    DynamicSession, AsyncDynamicSession, ProxyRotator
)
```

## 1. Ba fetcher — bảng so sánh

| Tiêu chí | `Fetcher` | `DynamicFetcher` | `StealthyFetcher` |
|---|---|---|---|
| Mở trình duyệt | Không (HTTP thuần qua `curl_cffi`) | Có (Chromium/Chrome qua Playwright) | Có (Chromium/Chrome qua Playwright, patchright) |
| Tốc độ tương đối | 🐇🐇🐇🐇🐇 | 🐇🐇🐇 | 🐇🐇🐇 |
| RAM tiêu tốn | Rất thấp (⭐) | Trung bình-cao (⭐⭐⭐) | Trung bình-cao (⭐⭐⭐) |
| Chạy JavaScript | Không | Có | Có |
| Vượt chặn | Header giả + TLS impersonate (chặn nhẹ) | Chặn nhẹ-trung bình, một số stealth cơ bản | Cloudflare Turnstile/Interstitial, canvas/WebRTC fingerprint, chặn nặng |
| Dùng khi | Trang tĩnh, API JSON nội bộ, hầu hết đề thi/tài liệu công khai | Trang SPA/React/Vue cần render JS, không bị chặn nặng | Trang có Cloudflare/anti-bot mạnh |

Nguồn bảng: [Fetchers basics](https://scrapling.readthedocs.io/en/latest/fetching/choosing.html) (docs/fetching/choosing.md).

Máy 8 GB RAM → luôn thử `Fetcher` trước, chỉ lên `DynamicFetcher`/`StealthyFetcher` khi thật sự cần (xem `fetcher-selection.md`).

## 2. `Fetcher` — HTTP thuần (curl_cffi)

```python
Fetcher.get(url, params=None, headers=None, cookies=None,
            stealthy_headers=True, impersonate=None, http3=False,
            proxy=None, proxy_auth=None, proxies=None, proxy_rotator=None,
            follow_redirects="safe", timeout=30, retries=3, retry_delay=1,
            max_redirects=30, verify=True, cert=None, selector_config=None, ...)
Fetcher.post(url, data=None, json=None, params=None, ...)
Fetcher.put(url, data=None, ...)
Fetcher.delete(url, ...)
```
Chỉ hỗ trợ GET/POST/PUT/DELETE — **không** có OPTIONS/HEAD.

Tham số quan trọng:
| Tham số | Mặc định | Ý nghĩa |
|---|---|---|
| `stealthy_headers` | `True` | Tự tạo header trình duyệt thật + referer Google |
| `impersonate` | `None` (dùng bản Chrome mới nhất) | Giả TLS fingerprint: `"chrome110"`, `"firefox102"`, `"safari"`, `"edge"`, `"chrome_android"`, `"tor"`... hoặc list để random mỗi request |
| `timeout` | 30s | Giây chờ mỗi request |
| `retries` / `retry_delay` | 3 / 1s | Số lần thử lại / khoảng nghỉ |
| `follow_redirects` | `"safe"` | `"safe"` chặn redirect tới IP nội bộ (chống SSRF); `True` theo mọi redirect; `False` tắt hẳn |
| `http3` | `False` | Bật HTTP/3 (có thể xung đột với `impersonate`) |
| `proxy` | `None` | `"http://user:pass@host:port"` |
| `verify` | `True` | Kiểm tra chứng chỉ HTTPS |
| `selector_config` | `None` | dict cấu hình riêng cho `Selector`/`Response` của request này |

Ví dụ:
```python
page = Fetcher.get('https://example.com', impersonate='chrome')
page = Fetcher.get('https://example.com/search', params={'q': 'de thi'})
page = Fetcher.post('https://example.com/api', json={'key': 'value'})
if page.status == 200:
    title = page.css('title::text').get()
```

Async: đổi `Fetcher` → `AsyncFetcher`, `await` mọi call. Xem mục 6.

## 3. `FetcherSession` — tái dùng phiên (HTTP)

Dùng khi gọi nhiều request tới cùng site: giữ cookie, connection pool, nhanh hơn ~10 lần so với tạo phiên mới mỗi lần.

```python
from scrapling.fetchers import FetcherSession

with FetcherSession(impersonate='chrome', stealthy_headers=True,
                     timeout=30, retries=3) as session:
    page1 = session.get('https://example.com/get')
    page2 = session.post('https://example.com/post', data={'k': 'v'})
```

`FetcherSession` tự nhận biết sync/async — dùng `async with FetcherSession(...) as session: await session.get(...)` không cần import khác.

Có thể xoay proxy qua `ProxyRotator`:
```python
from scrapling.fetchers import FetcherSession, ProxyRotator
rotator = ProxyRotator(["http://proxy1:8080", "http://proxy2:8080"])
with FetcherSession(proxy_rotator=rotator, impersonate='chrome') as session:
    page1 = session.get('https://example.com/page1')  # tự xoay proxy
    page2 = session.get('https://example.com/page2', proxy='http://khac:9090')  # ghi đè riêng request này
```

## 4. `DynamicFetcher` / `StealthyFetcher` — trình duyệt (Playwright)

```python
DynamicFetcher.fetch(url, headless=True, disable_resources=False, cookies=None,
                      useragent=None, network_idle=False, load_dom=True,
                      timeout=30000, wait=0, page_action=None, page_setup=None,
                      wait_selector=None, wait_selector_state="attached",
                      google_search=True, extra_headers=None, proxy=None,
                      real_chrome=False, locale=None, timezone_id=None,
                      cdp_url=None, user_data_dir=None, extra_flags=None,
                      additional_args=None, selector_config=None,
                      blocked_domains=None, block_ads=False, dns_over_https=False,
                      proxy_rotator=None, retries=3, retry_delay=1,
                      capture_xhr=None, executable_path=None)
```
`StealthyFetcher.fetch(...)` nhận **tất cả** tham số trên, cộng thêm:
`solve_cloudflare=False`, `block_webrtc=False`, `hide_canvas=False`, `allow_webgl=True`.

Tham số hay dùng nhất:
| Tham số | Mặc định | Ý nghĩa |
|---|---|---|
| `headless` | `True` | `False` để xem trình duyệt (debug) |
| `network_idle` | `False` | Chờ tới khi không còn request mạng trong ≥500ms — cần cho SPA tải dữ liệu chậm |
| `disable_resources` | `False` | Chặn font/image/media/stylesheet... nhanh hơn ~25%, tiết kiệm RAM/băng thông |
| `timeout` | 30000 (ms) | Timeout mọi thao tác trên trang |
| `wait` | 0 (ms) | Chờ thêm sau khi mọi thứ xong, trước khi trả response |
| `wait_selector` | `None` | CSS selector cần chờ xuất hiện (dùng `wait_selector_state`) |
| `wait_selector_state` | `"attached"` | `attached` / `detached` / `visible` / `hidden` |
| `page_action` | `None` | hàm nhận `page` (Playwright), chạy SAU khi điều hướng — dùng để scroll/click |
| `page_setup` | `None` | hàm nhận `page`, chạy TRƯỚC khi điều hướng — đăng ký listener/route |
| `real_chrome` | `False` | Dùng Chrome thật đã cài thay vì Chromium bundled |
| `stealthy_headers`/`solve_cloudflare` (chỉ Stealthy) | `False` | Tự động giải Cloudflare Turnstile/Interstitial |
| `capture_xhr` | `None` | regex URL để bắt các request XHR/fetch nền — truy cập qua `response.captured_xhr` |
| `proxy` | `None` | string hoặc dict `{'server','username','password'}` |

Ví dụ cơ bản:
```python
from scrapling.fetchers import DynamicFetcher, StealthyFetcher

page = DynamicFetcher.fetch('https://example.com', network_idle=True,
                             wait_selector='.content')

page = StealthyFetcher.fetch('https://nopecha.com/demo/cloudflare',
                              solve_cloudflare=True)  # timeout nên >=60000ms khi giải Cloudflare
```

Ví dụ `page_action` (Playwright Page API):
```python
from playwright.sync_api import Page

def scroll_page(page: Page):
    page.mouse.wheel(10, 0)
    page.mouse.move(100, 400)

page = DynamicFetcher.fetch('https://example.com', page_action=scroll_page)
```

### Session cho browser fetcher
```python
from scrapling.fetchers import DynamicSession, StealthySession

with DynamicSession(headless=True, disable_resources=True) as session:
    p1 = session.fetch('https://a.com')
    p2 = session.fetch('https://b.com')   # tái dùng cùng browser, nhanh hơn nhiều
```
`AsyncDynamicSession`/`AsyncStealthySession` nhận thêm `max_pages` — pool tab xoay vòng để fetch song song trong CÙNG một trình duyệt (tiết kiệm RAM hơn nhiều so với mở nhiều browser).

Nguồn: [Fetching dynamic websites](https://scrapling.readthedocs.io/en/latest/fetching/dynamic.html), [StealthyFetcher](https://scrapling.readthedocs.io/en/latest/fetching/stealthy.html).

## 5. Cú pháp chọn phần tử

### CSS (qua `cssselect`, hỗ trợ CSS3) và XPath (qua `lxml`)
```python
page.css('.product')                    # -> Selectors (list các Selector)
page.xpath('//*[@class="product"]')     # tương đương

title = page.css('h1::text').get()      # pseudo-element không chuẩn của Scrapling
title = page.xpath('//h1//text()').get()
link  = page.css('a::attr(href)').get() # lấy attribute
link  = page.xpath('//a/@href').get()

page.css('.product')[0].css('h1::text').get()   # nối chuỗi selector
```
- `::text` — lấy text node.
- `::attr(name)` — lấy giá trị attribute `name`.
- `.get()` → 1 kết quả (hoặc `None`); `.getall()` → list tất cả.
- CSS ưu tiên hơn XPath khi lọc theo class (XPath `@class="x"` chỉ khớp khi class DUY NHẤT là x).

### Điều hướng DOM (thuộc tính trên `Selector`)
| Thuộc tính/method | Ý nghĩa |
|---|---|
| `.parent` | phần tử cha |
| `.children` | list con trực tiếp |
| `.siblings` | phần tử cùng cha |
| `.next` / `.previous` | sibling kế tiếp/trước |
| `.below_elements` | mọi hậu duệ (đệ quy) |
| `.iterancestors()` | duyệt hết tổ tiên |
| `.find_ancestor(fn)` | tìm tổ tiên đầu tiên khớp điều kiện |
| `.attrib` | dict attribute (`AttributesHandler`) |
| `.tag` | tên thẻ (text node trả về `"#text"`) |
| `.text` | text trực tiếp (không đệ quy con) |
| `.get_all_text()` | text đệ quy toàn bộ, có `strip`, `separator` |
| `.html_content` | HTML string của phần tử |

### Tìm theo bộ lọc (`find_all`/`find`) — dễ học hơn selector, kiểu BeautifulSoup
```python
page.find_all('div')
page.find_all('div', class_='quote')
page.find_all('div', {'class': 'quote'})
page.find_all({'href*': '/author/'})           # href CHỨA chuỗi
page.find_all({'href$': 'Einstein'})           # href KẾT THÚC bằng chuỗi
page.find_all(lambda e: "world" in e.text)     # hàm lọc tuỳ ý
page.find_all('span', re.compile(r'world'))    # lọc theo regex nội dung
```

### Tìm theo nội dung text/regex
```python
page.find_by_text('Tipping the Velvet')                       # khớp chính xác, phần tử đầu
page.find_by_text('the', partial=True, first_match=False)     # chứa 'the', trả list
page.find_by_regex(r'£[\d\.]+')
```
Tham số chung: `first_match=True`, `case_sensitive=False`, `clean_match=False`, `partial=False` (chỉ `find_by_text`).

### Regex trực tiếp trên kết quả (`re`/`re_first`)
Có mặt trên `Selector`/`Selectors`/`TextHandler`/`TextHandlers`:
```python
page.css('.price_color')[0].re_first(r'[\d\.]+')   # '51.77'
page.css('.price_color').re(r'[\d\.]+')             # list toàn bộ
```

## 6. Adaptive element tracking (tính năng đặc trưng)

Tự tìm lại phần tử khi cấu trúc trang thay đổi (đổi tên, thứ tự, thêm bớt thẻ bọc), dựa trên fuzzy-matching tag/attributes/vị trí, lưu vào SQLite cục bộ.

**Bật toàn cục:**
```python
from scrapling.fetchers import Fetcher
Fetcher.adaptive = True
page = Fetcher.get('https://example.com')
```
hoặc `Selector(html, adaptive=True, url='example.com')`.

**Cách 1 — qua CSS/XPath (tự động dùng selector làm identifier):**
```python
el = page.css('#p1', auto_save=True)      # lần đầu: lưu lại vị trí/đặc điểm phần tử
...
el = page.css('#p1', adaptive=True)       # lần sau (web đã đổi cấu trúc): tự tìm phần tử tương tự
```

**Cách 2 — thủ công, dùng identifier tuỳ ý:**
```python
el = page.find_by_text('Tipping the Velvet', first_match=True)
page.save(el, 'my_special_element')
...
saved = page.retrieve('my_special_element')
el2 = page.relocate(saved, selector_type=True)
```

Khi nào đáng dùng: scraper chạy định kỳ dài hạn (VD: crawl đề thi từ 1 trang mỗi tuần) mà trang hay đổi giao diện — tránh phải sửa code liên tục. Không cần cho script chạy 1 lần.

Lưu ý: nếu selector khớp NHIỀU phần tử, `auto_save` chỉ lưu phần tử ĐẦU TIÊN.

Nguồn: [Adaptive scraping](https://scrapling.readthedocs.io/en/latest/parsing/adaptive.html) (docs/parsing/adaptive.md).

## 7. Async

```python
from scrapling.fetchers import AsyncFetcher, AsyncStealthySession, AsyncDynamicSession
import asyncio

async def main():
    page = await AsyncFetcher.get('https://example.com')

    async with AsyncStealthySession(headless=True, max_pages=3) as session:
        pages = await asyncio.gather(
            session.fetch('https://a.com'),
            session.fetch('https://b.com'),
        )

asyncio.run(main())
```
Mọi fetcher browser đều có `async_fetch` (bản async của `.fetch`); `page_action`/`page_setup` khi dùng với async fetch cũng phải là hàm `async def`.

## 8. Bẫy đã biết (Known gotchas)

### 8.1 `TypeError: Text nodes do not have attributes`
`page.css('...::text')` trả về `Selectors` — mỗi phần tử trong đó (khi lấy qua index `[0]`, CHƯA gọi `.get()`) là một `Selector` **bọc text node**, không phải string thô. Selector này định nghĩa `__getitem__` để cho phép cú pháp rút gọn `elem['href']` lấy attribute — nhưng nếu `elem` là text-node Selector, `__getitem__` (kể cả khi bạn truyền **slice** như `elem[:50]`) sẽ raise ngay `TypeError: Text nodes do not have attributes` (xem `scrapling/parser.py`, method `__getitem__`).

```python
# SAI — elem là Selector bọc text-node, [:50] gọi __getitem__ -> TypeError
elem = page.css('h1::text')[0]
elem[:50]     # TypeError: Text nodes do not have attributes

# ĐÚNG — gọi .get() để lấy TextHandler (str subclass) rồi mới cắt chuỗi
text = page.css('h1::text').get()          # TextHandler hoặc None
if text is not None:
    short = text[:50]                      # OK, TextHandler hỗ trợ slicing, trả về TextHandler
# hoặc ép kiểu tường minh cho chắc
short = str(page.css('h1::text').get() or '')[:50]
```
**Quy tắc an toàn:** luôn gọi `.get()`/`.getall()` trước khi thao tác chuỗi (cắt, nối, so sánh), và luôn kiểm tra `None` vì `.get()` trả `None` khi không khớp — `None[:50]` cũng raise `TypeError`.

### 8.2 `TextHandler` là str subclass — chain method thoải mái
`.re()`, `.re_first()`, `.json()`, `.clean()`, `.sort()` đều trả `TextHandler` mới, có thể chain tiếp. Nhưng phải xử lý trường hợp `.get()` trả `None` trước khi gọi bất kỳ method chuỗi nào.

### 8.3 `Response.body` luôn là `bytes` (từ v0.4), khác `Selector.body`
Khi tải file nhị phân (PDF, ảnh) qua fetcher, dùng `page.body` (bytes) — không dùng `.text`/`.get_all_text()`.

### 8.4 `find_all()`/`css()`/`xpath()` gọi trên text-node Selector → trả `Selectors()` rỗng, không raise lỗi
Khác với `__getitem__`/`.attrib` (raise), các method truy vấn tiếp tục trên text-node sẽ âm thầm trả rỗng — dễ gây bug logic khó thấy (không có exception để bắt).

Nguồn xác nhận trực tiếp từ mã nguồn: `scrapling/parser.py` (đọc qua GitHub raw ngày 2026-08-10), các dòng định nghĩa `_is_text_node`, `__getitem__`, `attrib`, `tag`, `text`.
