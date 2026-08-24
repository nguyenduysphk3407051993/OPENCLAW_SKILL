# -*- coding: utf-8 -*-
"""Cào dữ liệu web theo file cấu hình JSON, xuất ra CSV hoặc JSON.

Dùng:
    python scripts/scrape.py <config.json> [-o output.csv]

Xem assets/config-example.json để biết cấu trúc config đầy đủ (có chú thích).

Điểm chính:
  - Tôn trọng robots.txt (dừng nếu bị Disallow, trừ khi "ignore_robots": true).
  - Nghỉ giữa các request theo "delay" (tối thiểu 0.5s, mặc định 1.5s) + jitter ±30%.
  - Với dynamic/stealthy: tái sử dụng MỘT phiên trình duyệt cho mọi trang (tiết kiệm RAM),
    đóng sạch trình duyệt kể cả khi lỗi (try/finally).
  - Lỗi một trang -> log và đi tiếp, không sập cả job.
  - CSV xuất encoding utf-8-sig để Excel mở tiếng Việt không vỡ font.
"""

import sys
import os
import json
import csv
import time
import random
import argparse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import force_utf8_stdout, fetch_robots, looks_blocked  # noqa: E402

force_utf8_stdout()

from scrapling.fetchers import Fetcher, DynamicFetcher, StealthyFetcher  # noqa: E402
from scrapling.fetchers import DynamicSession, StealthySession  # noqa: E402


DEFAULT_DELAY = 1.5
MIN_DELAY = 0.5


# --------------------------------------------------------------------------- #
# Cấu hình
# --------------------------------------------------------------------------- #
def load_config(path):
    with open(path, "r", encoding="utf-8") as f:
        cfg = json.load(f)

    # Xây danh sách URL
    urls = []
    if "urls" in cfg and cfg["urls"]:
        urls = list(cfg["urls"])
    elif "url_template" in cfg and cfg["url_template"]:
        pages = cfg.get("pages")
        if not pages:
            # pages có thể là số trang -> 1..N
            n = int(cfg.get("max_pages", 1))
            pages = list(range(1, n + 1))
        for p in pages:
            urls.append(cfg["url_template"].format(page=p))
    elif "url" in cfg and cfg["url"]:
        urls = [cfg["url"]]
    else:
        raise ValueError("Config phải có một trong: 'url', 'urls', hoặc 'url_template'.")

    # Giới hạn số trang
    max_pages = cfg.get("max_pages")
    if max_pages:
        urls = urls[: int(max_pages)]

    # delay: mặc định 1.5, tối thiểu 0.5 (không cho 0)
    delay = cfg.get("delay", DEFAULT_DELAY)
    try:
        delay = float(delay)
    except (TypeError, ValueError):
        delay = DEFAULT_DELAY
    if delay < MIN_DELAY:
        print(f"⚠ delay={delay}s quá thấp -> nâng lên tối thiểu {MIN_DELAY}s.")
        delay = MIN_DELAY

    cfg["_urls"] = urls
    cfg["_delay"] = delay
    cfg.setdefault("fetcher", "auto")
    cfg.setdefault("timeout", 30)
    cfg.setdefault("ignore_robots", False)
    cfg.setdefault("fields", {})
    if not cfg.get("item_selector"):
        raise ValueError("Config phải có 'item_selector' (CSS chọn từng bản ghi).")
    if not cfg["fields"]:
        raise ValueError("Config phải có 'fields' (ánh xạ tên_cột -> CSS selector).")
    return cfg


# --------------------------------------------------------------------------- #
# Trích xuất field
# --------------------------------------------------------------------------- #
def extract_field(item, selector):
    """Trích một field từ một item. Hỗ trợ ::text và ::attr(...).

    Bẫy Scrapling: phần tử ::text trả về TextHandler, KHÔNG cắt chuỗi trực tiếp được
    -> luôn str() trước khi xử lý.
    """
    try:
        vals = item.css(selector)
    except Exception:
        return ""
    if not vals:
        return ""
    # Gộp nhiều node text (ví dụ nhiều tag) thành 1 chuỗi, bỏ khoảng trắng thừa
    parts = []
    for v in vals:
        s = str(v).strip()
        if s:
            parts.append(s)
    return " ".join(parts)


def extract_item(item, fields):
    row = {}
    for col, selector in fields.items():
        row[col] = extract_field(item, selector)
    return row


# --------------------------------------------------------------------------- #
# Robots.txt gate
# --------------------------------------------------------------------------- #
def robots_gate(urls, cfg):
    """Kiểm tra robots.txt cho URL đầu tiên. Trả về delay đã điều chỉnh theo Crawl-delay.

    Nếu bị Disallow và không có ignore_robots -> raise SystemExit.
    """
    if not urls:
        return cfg["_delay"]
    first = urls[0]
    robots = fetch_robots(first)
    delay = cfg["_delay"]

    if not robots.fetched:
        print(f"[robots] Không có robots.txt ({robots.error or 'không tải được'}) -> coi như cho phép.")
        return delay

    allowed, rule = robots.is_allowed(first)
    if robots.crawl_delay is not None:
        print(f"[robots] Crawl-delay khai báo: {robots.crawl_delay}s")
        if robots.crawl_delay > delay:
            print(f"[robots] Nâng delay {delay}s -> {robots.crawl_delay}s theo robots.txt.")
            delay = robots.crawl_delay

    if not allowed:
        if cfg.get("ignore_robots"):
            print("!" * 64)
            print("⚠⚠⚠ CẢNH BÁO: URL BỊ CHẶN bởi robots.txt (" + str(rule) + ")")
            print("⚠⚠⚠ Đang BỎ QUA vì config đặt \"ignore_robots\": true")
            print("⚠⚠⚠ Chỉ nên dùng cho dữ liệu công khai bạn có quyền truy cập.")
            print("!" * 64)
        else:
            print(f"[robots] URL BỊ CHẶN bởi robots.txt ({rule}).")
            print("[robots] DỪNG. Nếu chắc chắn có quyền, thêm \"ignore_robots\": true vào config.")
            raise SystemExit(2)
    else:
        print(f"[robots] Được phép cào" + (f" (khớp {rule})" if rule else "") + ".")
    return delay


# --------------------------------------------------------------------------- #
# Auto-detect fetcher (chẩn đoán rút gọn)
# --------------------------------------------------------------------------- #
def auto_detect_fetcher(url, item_selector, timeout):
    """Chọn nhanh fetcher: thử HTTP; nếu bị chặn -> stealthy; nếu thiếu item -> dynamic."""
    try:
        page = Fetcher.get(url, stealthy_headers=True, timeout=timeout)
        blocked, reason = looks_blocked(page.status, str(page.html_content)[:8000])
        if blocked:
            print(f"[auto] HTTP bị chặn ({reason}) -> chọn stealthy.")
            return "stealthy"
        n = len(page.css(item_selector))
        if n > 0:
            print(f"[auto] HTTP thấy {n} item khớp '{item_selector}' -> chọn http (nhanh, nhẹ).")
            return "http"
        print(f"[auto] HTTP thấy 0 item -> thử dynamic (render JS).")
        return "dynamic"
    except Exception as e:
        print(f"[auto] HTTP lỗi ({e}) -> chọn dynamic.")
        return "dynamic"


# --------------------------------------------------------------------------- #
# Nghỉ giữa request
# --------------------------------------------------------------------------- #
def sleep_with_jitter(delay):
    """Nghỉ delay giây với jitter ngẫu nhiên ±30% cho tự nhiên."""
    if delay <= 0:
        return
    factor = random.uniform(0.7, 1.3)
    time.sleep(delay * factor)


# --------------------------------------------------------------------------- #
# Fetch một trang theo từng chế độ
# --------------------------------------------------------------------------- #
def fetch_http(url, timeout):
    return Fetcher.get(url, stealthy_headers=True, timeout=timeout)


# --------------------------------------------------------------------------- #
# Vòng cào chính
# --------------------------------------------------------------------------- #
def scrape(cfg):
    urls = cfg["_urls"]
    item_selector = cfg["item_selector"]
    fields = cfg["fields"]
    timeout = int(cfg["timeout"])

    delay = robots_gate(urls, cfg)

    # Xác định fetcher
    fetcher = cfg["fetcher"].lower()
    if fetcher == "auto":
        fetcher = auto_detect_fetcher(urls[0], item_selector, timeout)
    print(f"[fetcher] Dùng: {fetcher}")
    print(f"[plan] {len(urls)} trang, delay ~{delay}s (±30% jitter).\n")

    rows = []
    errors = 0
    ok_pages = 0

    if fetcher in ("dynamic", "stealthy"):
        rows, errors, ok_pages = _scrape_browser(fetcher, urls, item_selector,
                                                  fields, timeout, delay)
    else:
        rows, errors, ok_pages = _scrape_http(urls, item_selector, fields, timeout, delay)

    return rows, errors, ok_pages, len(urls)


def _process_page(page, url, item_selector, fields, idx, total):
    """Trích item từ một trang đã fetch. Trả về list row."""
    items = page.css(item_selector)
    page_rows = [extract_item(it, fields) for it in items]
    print(f"  [{idx}/{total}] {url}  ->  HTTP {page.status}, {len(page_rows)} bản ghi")
    return page_rows


def _scrape_http(urls, item_selector, fields, timeout, delay):
    rows, errors, ok_pages = [], 0, 0
    total = len(urls)
    for i, url in enumerate(urls, 1):
        try:
            page = fetch_http(url, timeout)
            page_rows = _process_page(page, url, item_selector, fields, i, total)
            rows.extend(page_rows)
            ok_pages += 1
        except Exception as e:
            errors += 1
            print(f"  [{i}/{total}] {url}  ->  LỖI: {e}  (bỏ qua, đi tiếp)")
        if i < total:
            sleep_with_jitter(delay)
    return rows, errors, ok_pages


def _scrape_browser(mode, urls, item_selector, fields, timeout, delay):
    """Cào bằng trình duyệt, TÁI SỬ DỤNG một session cho mọi trang. Đóng sạch ở finally."""
    rows, errors, ok_pages = [], 0, 0
    total = len(urls)

    if mode == "dynamic":
        session = DynamicSession(headless=True, network_idle=True)
    else:
        session = StealthySession(headless=True, network_idle=True)

    print(f"[browser] Mở 1 phiên {mode} (tái sử dụng cho cả {total} trang, tiết kiệm RAM)...")
    try:
        session.start()
        for i, url in enumerate(urls, 1):
            try:
                page = session.fetch(url)
                page_rows = _process_page(page, url, item_selector, fields, i, total)
                rows.extend(page_rows)
                ok_pages += 1
            except Exception as e:
                errors += 1
                print(f"  [{i}/{total}] {url}  ->  LỖI: {e}  (bỏ qua, đi tiếp)")
            if i < total:
                sleep_with_jitter(delay)
    finally:
        try:
            session.close()
            print("[browser] Đã đóng sạch phiên trình duyệt.")
        except Exception as e:
            print(f"[browser] Cảnh báo khi đóng trình duyệt: {e}")
    return rows, errors, ok_pages


# --------------------------------------------------------------------------- #
# Xuất kết quả
# --------------------------------------------------------------------------- #
def write_output(rows, out_path, fields, fmt):
    if fmt == "json":
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(rows, f, ensure_ascii=False, indent=2)
    else:  # csv
        cols = list(fields.keys())
        # utf-8-sig để Excel mở tiếng Việt không vỡ font
        with open(out_path, "w", encoding="utf-8-sig", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=cols)
            writer.writeheader()
            for r in rows:
                writer.writerow({c: r.get(c, "") for c in cols})


def resolve_output(cfg, cli_out):
    if cli_out:
        out = cli_out
    else:
        out = cfg.get("output", "output.csv")
    ext = os.path.splitext(out)[1].lower()
    fmt = cfg.get("output_format")
    if not fmt:
        fmt = "json" if ext == ".json" else "csv"
    fmt = fmt.lower()
    # đồng bộ đuôi file với format nếu người dùng không ghi rõ
    if fmt == "json" and ext != ".json":
        out = os.path.splitext(out)[0] + ".json"
    if fmt == "csv" and ext != ".csv":
        out = os.path.splitext(out)[0] + ".csv"
    return out, fmt


# --------------------------------------------------------------------------- #
def main():
    ap = argparse.ArgumentParser(description="Cào web theo config JSON, xuất CSV/JSON.")
    ap.add_argument("config", help="Đường dẫn file config JSON")
    ap.add_argument("-o", "--output", default=None, help="File xuất (.csv hoặc .json)")
    args = ap.parse_args()

    cfg = load_config(args.config)
    out_path, fmt = resolve_output(cfg, args.output)

    print("=" * 64)
    print("WEB-SCRAPER")
    print("=" * 64)

    rows, errors, ok_pages, total_pages = scrape(cfg)

    write_output(rows, out_path, cfg["fields"], fmt)

    print("\n" + "=" * 64)
    print("KẾT QUẢ")
    print("-" * 64)
    print(f"  Trang xử lý thành công : {ok_pages}/{total_pages}")
    print(f"  Trang lỗi              : {errors}")
    print(f"  Tổng bản ghi cào được  : {len(rows)}")
    print(f"  File xuất ({fmt.upper()})       : {os.path.abspath(out_path)}")
    print("=" * 64)


if __name__ == "__main__":
    main()
