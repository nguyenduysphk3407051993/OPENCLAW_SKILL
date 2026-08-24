# -*- coding: utf-8 -*-
"""Chẩn đoán một URL cần fetcher nào (Fetcher / DynamicFetcher / StealthyFetcher).

Mục đích: tránh mở trình duyệt vô ích (máy chỉ 8 GB RAM). Chạy Fetcher (HTTP thuần)
trước, rồi DynamicFetcher (Chromium), so sánh lượng nội dung lấy được để khuyến nghị.

Dùng:
    python scripts/diagnose_site.py <url> [--selector "css"]

Ví dụ:
    python scripts/diagnose_site.py https://quotes.toscrape.com/
    python scripts/diagnose_site.py https://quotes.toscrape.com/js/ --selector ".quote"
"""

import sys
import os
import time
import argparse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import force_utf8_stdout, fetch_robots, looks_blocked  # noqa: E402

force_utf8_stdout()

from scrapling.fetchers import Fetcher, DynamicFetcher  # noqa: E402


def _text_len(page):
    """Tổng độ dài text hữu ích trong <body> (đo lượng nội dung render được)."""
    try:
        texts = page.css("body ::text")
        total = 0
        for t in texts:
            s = str(t).strip()
            total += len(s)
        return total
    except Exception:
        return 0


def _count_selector(page, selector):
    try:
        return len(page.css(selector))
    except Exception:
        return -1


def _try_http(url, selector, timeout):
    """Lấy trang bằng Fetcher (HTTP thuần). Trả về dict kết quả."""
    res = {"ok": False, "status": None, "text_len": 0, "sel_count": None,
           "elapsed": 0.0, "blocked": False, "block_reason": "", "error": None,
           "html_snippet": ""}
    t0 = time.perf_counter()
    try:
        page = Fetcher.get(url, stealthy_headers=True, timeout=timeout)
        res["status"] = page.status
        res["text_len"] = _text_len(page)
        if selector:
            res["sel_count"] = _count_selector(page, selector)
        try:
            res["html_snippet"] = str(page.html_content)[:8000]
        except Exception:
            res["html_snippet"] = ""
        blocked, reason = looks_blocked(page.status, res["html_snippet"])
        res["blocked"] = blocked
        res["block_reason"] = reason
        res["ok"] = True
    except Exception as e:
        res["error"] = str(e)
    res["elapsed"] = time.perf_counter() - t0
    return res


def _try_dynamic(url, selector, timeout):
    """Lấy trang bằng DynamicFetcher (Chromium render JS)."""
    res = {"ok": False, "status": None, "text_len": 0, "sel_count": None,
           "elapsed": 0.0, "error": None}
    t0 = time.perf_counter()
    try:
        page = DynamicFetcher.fetch(url, headless=True, network_idle=True, timeout=timeout * 1000)
        res["status"] = page.status
        res["text_len"] = _text_len(page)
        if selector:
            res["sel_count"] = _count_selector(page, selector)
        res["ok"] = True
    except Exception as e:
        res["error"] = str(e)
    res["elapsed"] = time.perf_counter() - t0
    return res


def _recommend(http, dyn, selector):
    """Suy luận khuyến nghị fetcher. Trả về (fetcher, danh_sách_lý_do)."""
    reasons = []

    # 1) HTTP bị chặn -> StealthyFetcher
    if http["ok"] and http["blocked"]:
        reasons.append(f"Fetcher HTTP bị chặn ({http['block_reason']}).")
        reasons.append("Nội dung công khai nhưng có tường lửa bot/captcha -> cần bản chống phát hiện.")
        return "StealthyFetcher", reasons
    if not http["ok"]:
        reasons.append(f"Fetcher HTTP lỗi ({http['error']}).")
        if dyn["ok"]:
            reasons.append("DynamicFetcher lại lấy được -> trang cần trình duyệt thật.")
            return "DynamicFetcher", reasons
        reasons.append("Cả hai cách đều lỗi -> thử StealthyFetcher (chống phát hiện, nặng nhất).")
        return "StealthyFetcher", reasons

    # 2) Có selector -> tín hiệu chính xác nhất
    if selector and http["sel_count"] is not None and dyn["sel_count"] is not None:
        h, d = http["sel_count"], dyn["sel_count"]
        reasons.append(f"Selector '{selector}': HTTP khớp {h} phần tử, Dynamic khớp {d} phần tử.")
        if h <= 0 and d > 0:
            reasons.append("HTTP không thấy phần tử nào còn Dynamic thấy -> nội dung do JavaScript sinh ra.")
            return "DynamicFetcher", reasons
        if d > 0 and h < d * 0.5:
            reasons.append(f"HTTP thiếu hẳn ({h} so với {d}) -> phần lớn nội dung cần JS render.")
            return "DynamicFetcher", reasons
        if h >= d and h > 0:
            reasons.append("HTTP đã lấy đủ (bằng hoặc hơn Dynamic) -> không cần mở trình duyệt.")
            return "Fetcher", reasons

    # 3) So theo lượng text
    ht, dt = http["text_len"], dyn["text_len"]
    reasons.append(f"Lượng text hữu ích: HTTP {ht:,} ký tự, Dynamic {dt:,} ký tự.")
    if dt > 0 and ht < dt * 0.6:
        diff = dt - ht
        reasons.append(f"HTTP thiếu ~{diff:,} ký tự ({(1 - ht / dt) * 100:.0f}% nội dung) -> JS render.")
        return "DynamicFetcher", reasons
    reasons.append("HTTP lấy được tương đương Dynamic -> dùng bản nhanh/nhẹ.")
    return "Fetcher", reasons


def main():
    ap = argparse.ArgumentParser(
        description="Chẩn đoán URL cần fetcher nào (tránh mở trình duyệt vô ích).")
    ap.add_argument("url", help="URL cần chẩn đoán")
    ap.add_argument("--selector", default=None,
                    help="CSS selector để đếm số phần tử khớp (tín hiệu chính xác nhất)")
    ap.add_argument("--timeout", type=int, default=30, help="Timeout mỗi request (giây)")
    args = ap.parse_args()

    print("=" * 64)
    print(f"CHẨN ĐOÁN: {args.url}")
    if args.selector:
        print(f"Selector đo lường: {args.selector}")
    print("=" * 64)

    # --- robots.txt ---
    print("\n[robots.txt]")
    robots = fetch_robots(args.url)
    if not robots.fetched:
        print(f"  Không có/không đọc được robots.txt -> mặc định CHO PHÉP cào.")
        if robots.error:
            print(f"  ({robots.error})")
    else:
        print(f"  Tải robots.txt: HTTP {robots.status}")
        allowed, rule = robots.is_allowed(args.url)
        if allowed:
            print(f"  URL này: ĐƯỢC PHÉP cào" + (f" (khớp {rule})" if rule else ""))
        else:
            print(f"  URL này: BỊ CHẶN bởi robots.txt ({rule})  ⚠")
        if robots.crawl_delay is not None:
            print(f"  Crawl-delay khai báo: {robots.crawl_delay} giây")
        else:
            print(f"  Crawl-delay: không khai báo")

    # --- Fetcher (HTTP thuần) ---
    print("\n[1/2] Fetcher (HTTP thuần, curl-cffi) ...")
    http = _try_http(args.url, args.selector, args.timeout)
    if http["ok"]:
        line = f"  status HTTP {http['status']} | text {http['text_len']:,} ký tự"
        if args.selector:
            line += f" | selector khớp {http['sel_count']}"
        line += f" | {http['elapsed']:.2f}s"
        print(line)
        if http["blocked"]:
            print(f"  ⚠ Có dấu hiệu bị chặn: {http['block_reason']}")
    else:
        print(f"  LỖI: {http['error']} | {http['elapsed']:.2f}s")

    # --- DynamicFetcher (Chromium) ---
    print("\n[2/2] DynamicFetcher (Chromium, render JS) ...")
    dyn = _try_dynamic(args.url, args.selector, args.timeout)
    if dyn["ok"]:
        line = f"  status HTTP {dyn['status']} | text {dyn['text_len']:,} ký tự"
        if args.selector:
            line += f" | selector khớp {dyn['sel_count']}"
        line += f" | {dyn['elapsed']:.2f}s"
        print(line)
    else:
        print(f"  LỖI: {dyn['error']} | {dyn['elapsed']:.2f}s")

    # --- Kết luận ---
    fetcher, reasons = _recommend(http, dyn, args.selector)
    print("\n" + "=" * 64)
    print(f"KẾT LUẬN: dùng  →  {fetcher}")
    print("-" * 64)
    for r in reasons:
        print(f"  - {r}")
    # Nhắc RAM
    if fetcher == "Fetcher":
        print("  - Không cần mở Chromium, tiết kiệm RAM (tốt cho máy 8 GB).")
    else:
        print("  - Sẽ mở Chromium: nhớ tái sử dụng session khi cào nhiều trang.")
    print("=" * 64)


if __name__ == "__main__":
    main()
