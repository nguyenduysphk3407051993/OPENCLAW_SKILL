# -*- coding: utf-8 -*-
"""Tiện ích dùng chung cho web-scraper: đọc/phân tích robots.txt, dấu hiệu chặn bot.

Không phụ thuộc Scrapling để robots.txt luôn tải được kể cả khi trang chính khó fetch.
"""

import sys
import re
from urllib.parse import urlparse, urljoin
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError


def force_utf8_stdout():
    """Console Windows mặc định cp1252 -> ép UTF-8 để không vỡ tiếng Việt / ký tự đặc biệt."""
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass


# Các dấu hiệu HTML cho thấy trang bị tường lửa bot / captcha chặn
_BLOCK_SIGNS = [
    "cloudflare",
    "cf-browser-verification",
    "cf-chl",  # cloudflare challenge
    "just a moment",
    "checking your browser",
    "attention required",
    "captcha",
    "recaptcha",
    "hcaptcha",
    "px-captcha",  # PerimeterX
    "access denied",
    "are you a robot",
    "enable javascript and cookies to continue",
]


def looks_blocked(status, html):
    """Trả về (bị_chặn: bool, lý_do: str) dựa vào HTTP status và nội dung HTML."""
    if status in (401, 403, 429, 503):
        return True, f"HTTP {status}"
    if not html:
        return False, ""
    low = html.lower()
    for sign in _BLOCK_SIGNS:
        if sign in low:
            return True, f"phát hiện dấu hiệu chặn/captcha ('{sign}')"
    return False, ""


class RobotsInfo:
    """Kết quả phân tích robots.txt cho một User-agent (mặc định '*')."""

    def __init__(self, fetched, status, disallow, allow, crawl_delay, error=None):
        self.fetched = fetched            # có tải được robots.txt không
        self.status = status              # HTTP status khi tải robots.txt
        self.disallow = disallow          # list các prefix bị cấm
        self.allow = allow                # list các prefix cho phép (ưu tiên hơn Disallow dài hơn)
        self.crawl_delay = crawl_delay    # float hoặc None
        self.error = error                # thông báo lỗi nếu có

    def is_allowed(self, url):
        """Kiểm tra url có được phép cào không theo quy tắc longest-match của robots.txt.

        Trả về (được_phép: bool, quy_tắc_khớp: str|None).
        Nếu không tải được robots.txt -> coi như được phép (chuẩn robots: không có file = cho phép).
        """
        if not self.fetched:
            return True, None
        path = urlparse(url).path or "/"

        # Tìm quy tắc Allow và Disallow khớp dài nhất (theo RFC/Google spec)
        def longest_match(rules):
            best = None
            for r in rules:
                if r == "":
                    # Disallow: rỗng nghĩa là cho phép tất cả -> khớp mọi thứ nhưng độ dài 0
                    if best is None:
                        best = ""
                    continue
                if _path_matches(path, r):
                    if best is None or len(r) > len(best):
                        best = r
            return best

        d = longest_match(self.disallow)
        a = longest_match(self.allow)

        if d is None:
            return True, None
        # Disallow: (rỗng) = cho phép tất cả
        if d == "":
            return True, None
        # Nếu có Allow khớp dài hơn hoặc bằng -> ưu tiên cho phép
        if a is not None and a != "" and len(a) >= len(d):
            return True, f"Allow: {a}"
        return False, f"Disallow: {d}"


def _path_matches(path, rule):
    """So khớp path với một rule robots.txt (hỗ trợ ký tự đại diện * và neo cuối $)."""
    # Chuyển rule robots thành regex
    anchored_end = rule.endswith("$")
    if anchored_end:
        rule = rule[:-1]
    # Escape mọi thứ trừ '*'
    parts = rule.split("*")
    regex = ".*".join(re.escape(p) for p in parts)
    pattern = "^" + regex
    if anchored_end:
        pattern += "$"
    return re.search(pattern, path) is not None


def fetch_robots(url, timeout=10, user_agent="*"):
    """Tải và phân tích robots.txt của domain chứa url. Trả về RobotsInfo.

    Chỉ lấy các quy tắc áp dụng cho user_agent chỉ định và cho '*'.
    """
    parsed = urlparse(url)
    robots_url = urljoin(f"{parsed.scheme}://{parsed.netloc}", "/robots.txt")
    req = Request(robots_url, headers={"User-Agent": "web-scraper-skill/1.0 (+robots-check)"})
    try:
        with urlopen(req, timeout=timeout) as resp:
            status = resp.status
            raw = resp.read().decode("utf-8", errors="replace")
    except HTTPError as e:
        # 404 = không có robots.txt = cho phép tất cả
        return RobotsInfo(False, e.code, [], [], None,
                          error=f"HTTP {e.code} khi tải robots.txt (coi như không có luật)")
    except (URLError, Exception) as e:
        return RobotsInfo(False, None, [], [], None,
                          error=f"không tải được robots.txt ({e})")

    disallow, allow, crawl_delay = _parse_robots(raw, user_agent)
    return RobotsInfo(True, status, disallow, allow, crawl_delay)


def _parse_robots(text, ua_target):
    """Phân tích nội dung robots.txt, gộp luật cho ua_target và cho '*'.

    Luật cho ua_target cụ thể (nếu có) được ưu tiên; nếu không có thì dùng '*'.
    """
    # Gom các nhóm theo user-agent
    groups = {}  # ua(lower) -> {'disallow':[], 'allow':[], 'crawl_delay':None}
    current_uas = []
    last_line_was_ua = False

    for raw_line in text.splitlines():
        line = raw_line.split("#", 1)[0].strip()
        if not line:
            continue
        if ":" not in line:
            continue
        field, _, value = line.partition(":")
        field = field.strip().lower()
        value = value.strip()

        if field == "user-agent":
            ua = value.lower()
            if not last_line_was_ua:
                current_uas = []
            current_uas.append(ua)
            groups.setdefault(ua, {"disallow": [], "allow": [], "crawl_delay": None})
            last_line_was_ua = True
            continue

        last_line_was_ua = False
        if not current_uas:
            continue
        for ua in current_uas:
            g = groups.setdefault(ua, {"disallow": [], "allow": [], "crawl_delay": None})
            if field == "disallow":
                g["disallow"].append(value)
            elif field == "allow":
                g["allow"].append(value)
            elif field == "crawl-delay":
                try:
                    g["crawl_delay"] = float(value.replace(",", "."))
                except ValueError:
                    pass

    ua_target = ua_target.lower()
    chosen = None
    if ua_target in groups and ua_target != "*":
        chosen = groups[ua_target]
    elif "*" in groups:
        chosen = groups["*"]
    elif groups:
        # không có '*' và không khớp ua -> theo spec là được phép tất cả
        chosen = None

    if chosen is None:
        return [], [], None
    return chosen["disallow"], chosen["allow"], chosen["crawl_delay"]
