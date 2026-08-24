---
name: web-scraper
description: "Skill cào dữ liệu web tự động sử dụng Scrapling (Fetcher, DynamicFetcher, StealthyFetcher), tối ưu RAM, tuân thủ robots.txt và quy tắc cào có trách nhiệm. Hỗ trợ tự động chẩn đoán website, trích xuất dữ liệu theo cấu trúc CSS Selector và xuất ra file CSV (UTF-8-SIG tiếng Việt) hoặc JSON."
allowed-tools: Read, Write, Edit, Glob, Grep, Bash, WebFetch
argument-hint: "[URL hoặc cấu hình] [file xuất]"
---

# Web Scraper — Cào dữ liệu web thông minh và tối ưu

Skill cào dữ liệu web an toàn, hiệu quả, sử dụng thư viện **Scrapling** kết hợp quy tắc kiểm tra `robots.txt`, tự động chọn Fetcher phù hợp nhất để tiết kiệm RAM (tối ưu cho môi trường RAM hạn chế như 8 GB).

---

## 1. Nguyên tắc cốt lõi

1. **Tôn trọng `robots.txt`**: Luôn kiểm tra quyền truy cập trước khi cào dữ liệu.
2. **Tiết kiệm tài nguyên (Tối ưu RAM)**:
   - Ưu tiên `Fetcher` (HTTP thuần) trước tiên.
   - Chỉ dùng `DynamicFetcher` / `StealthyFetcher` (Headless Browser) khi trang web bắt buộc render bằng JavaScript hoặc có cơ chế chống bot phức tạp.
   - Tái sử dụng một phiên trình duyệt duy nhất (`Session`) cho toàn bộ lượt cào thay vì khởi động lại nhiều lần.
3. **Giãn cách an toàn (`delay` & `jitter`)**: Nghỉ tối thiểu 0.5s – 1.5s giữa các request (kèm độ trễ ngẫu nhiên ±30%) để tránh gây tải cho server mục tiêu.
4. **Hỗ trợ tiếng Việt chuẩn**: Xuất CSV với encoding `utf-8-sig` để hiển thị tiếng Việt hoàn hảo trên Microsoft Excel.

---

## 2. Cấu trúc thư mục

```
web-scraper/
├── SKILL.md                          ← Hướng dẫn sử dụng skill
├── assets/
│   └── config-example.json           ← Mẫu cấu hình JSON chi tiết
├── references/
│   ├── fetcher-selection.md          ← Hướng dẫn chọn Fetcher tối ưu RAM
│   ├── scraping-ethics.md            ← Quy tắc đạo đức & tuân thủ robots.txt
│   └── scrapling-api.md              ← Tra cứu cú pháp API Scrapling
└── scripts/
    ├── _common.py                    ← Tiện ích dùng chung (robots, stdout, encoding)
    ├── diagnose_site.py              ← Script chẩn đoán nhanh loại Fetcher cần dùng
    └── scrape.py                     ← Script cào dữ liệu chính
```

---

## 3. Quy trình thực hiện

### Bước 1: Chẩn đoán website mục tiêu
Chạy công cụ chẩn đoán để xác định xem website có render qua JS không, có chặn bot không:

```bash
python web-scraper/scripts/diagnose_site.py "https://example.com"
```

### Bước 2: Tạo cấu hình cào dữ liệu
Tạo file `config.json` dựa trên mẫu tại `web-scraper/assets/config-example.json`:

```json
{
  "url_template": "https://quotes.toscrape.com/page/{page}/",
  "pages": [1, 2, 3],
  "fetcher": "auto",
  "item_selector": ".quote",
  "fields": {
    "noi_dung": ".text::text",
    "tac_gia": ".author::text",
    "the_loai": ".tags .tag::text"
  },
  "delay": 1.5,
  "output": "output.csv"
}
```

### Bước 3: Chạy cào dữ liệu

```bash
python web-scraper/scripts/scrape.py config.json -o ket_qua.csv
```
