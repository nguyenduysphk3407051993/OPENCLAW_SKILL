---
name: openclaw-integration
description: Hỗ trợ tích hợp và hiểu các lệnh từ OpenClaw Gateway thông qua Agent Client Protocol (ACP) giúp kết nối Telegram với Antigravity.
---

# Kỹ năng Tích hợp OpenClaw - Antigravity (Mô hình Gravity Claw)

Kỹ năng này cung cấp cho Antigravity IDE (và các AI Agent bên trong nó) kiến thức để làm việc mượt mà với môi trường OpenClaw Gateway.

## Nhiệm vụ chính
- Tiếp nhận các Task (nhiệm vụ) được mã hóa định dạng lệnh từ OpenClaw.
- Mở Terminal, chạy lệnh, tạo thư mục, đọc/chỉnh sửa mã nguồn dự án tương ứng.
- Phản hồi status và báo cáo định dạng Markdown để OpenClaw có thể dễ dàng forward qua ứng dụng Telegram của người dùng.

## Quy tắc hoạt động (Rules)
1. Luôn ưu tiên xuất định dạng text gọn gàng, rõ ràng.
2. Nếu OpenClaw gửi tín hiệu yêu cầu "Setup", hãy chủ động tìm và thiết lập tệp `openclaw.config.json` và hỗ trợ nạp chuỗi `Telegram Bot Token` nếu cần.
3. Không tự ý kết thúc phiên (session) trừ khi OpenClaw Master phát ra lệnh ngừng `Session.Terminated`.
