---
name: docker-expert
description: "Skill chuyên sử dụng Docker từ cơ bản đến nâng cao dành cho AI Agent. Cung cấp quy trình chuẩn để phân tích yêu cầu, viết Dockerfile tối ưu, cấu hình Docker Compose, quản lý container, network, volume và xử lý lỗi (troubleshooting)."
allowed-tools: Read, Write, RunCommand, Glob, Grep
argument-hint: "[yêu cầu cấu hình/quản lý Docker] [thông tin metadata]"
---

# Docker Expert Skill

Skill chuyên dụng cho AI Agent thực hiện các thao tác liên quan đến Docker từ mức độ cơ bản (chạy container) đến nâng cao (tối ưu hóa image, bảo mật, multi-stage build, docker-compose phức tạp).

## Quy trình làm việc chuẩn cho AI Agent

### Bước 1: Khảo sát môi trường và yêu cầu
Trước khi bắt đầu bất kỳ thao tác Docker nào, Agent cần:
1. Xác định rõ ngôn ngữ/framework của dự án (Node.js, Python, Go, Java...).
2. Kiểm tra xem file `Dockerfile` hoặc `docker-compose.yml` đã tồn tại chưa bằng công cụ `Glob` hoặc `Read`.
3. Xác định port cần expose, biến môi trường (ENV) cần thiết, và các thư mục cần map (Volume).
4. (Tùy chọn nếu cần thiết) Kiểm tra Docker daemon có đang chạy không bằng lệnh `docker info`.

### Bước 2: Viết/Tối ưu Dockerfile (Cơ bản đến Nâng cao)
Khi tạo mới hoặc sửa `Dockerfile`, phải tuân thủ các **Best Practices** sau:

1. **Sử dụng Official và Lightweight Base Image**:
   - Tốt: `node:20-alpine`, `python:3.11-slim`
   - Kém: `node:20`, `ubuntu:latest`

2. **Sử dụng Multi-stage builds** để giảm dung lượng file cuối cùng (rất quan trọng cho môi trường Production):
   ```dockerfile
   # Stage 1: Build
   FROM node:20-alpine AS builder
   WORKDIR /app
   COPY package*.json ./
   RUN npm ci
   COPY . .
   RUN npm run build

   # Stage 2: Production
   FROM node:20-alpine
   WORKDIR /app
   COPY --from=builder /app/dist ./dist
   COPY --from=builder /app/node_modules ./node_modules
   COPY package.json ./
   EXPOSE 3000
   CMD ["npm", "start"]
   ```

3. **Tận dụng Layer Caching**:
   - COPY các file configuration (`package.json`, `requirements.txt`) và chạy cài đặt dependencies *trước khi* COPY toàn bộ source code.

4. **Bảo mật (Chạy với Non-root user)**:
   ```dockerfile
   RUN addgroup -S appgroup && adduser -S appuser -G appgroup
   USER appuser
   ```

5. **Giảm thiểu số lượng layers**:
   - Gộp các lệnh `RUN` bằng `&&` và xóa cache/tệp tạm thời trong cùng một layer.
   ```dockerfile
   RUN apt-get update && apt-get install -y pnpm \
       && rm -rf /var/lib/apt/lists/*
   ```

### Bước 3: Cấu hình Docker Compose
Đối với các ứng dụng đa dịch vụ (Frontend + Backend + Database), luôn sử dụng `docker-compose.yml`:

```yaml
version: '3.8'

services:
  web:
    build: 
      context: .
      dockerfile: Dockerfile
    ports:
      - "3000:3000"
    environment:
      - NODE_ENV=production
      - DB_HOST=database
    depends_on:
      - database
    networks:
      - app-network

  database:
    image: postgres:15-alpine
    environment:
      - POSTGRES_USER=myuser
      - POSTGRES_PASSWORD=secret
      - POSTGRES_DB=mydb
    volumes:
      - pgdata:/var/lib/postgresql/data
    networks:
      - app-network

volumes:
  pgdata:

networks:
  app-network:
    driver: bridge
```
*Lưu ý: Luôn sử dụng named volumes cho database để đảm bảo persistent data.*

### Bước 4: Thực thi và Quản lý CLI (RunCommand)
Sử dụng công cụ thực thi lệnh để quản lý vòng đời của Docker.

- **Build image**: `docker build -t <image_name>:<tag> .`
- **Chạy container (Cơ bản)**: `docker run -d -p 8080:80 --name <container_name> <image_name>`
- **Xóa dọn dẹp (Prune)**: `docker system prune -f` (Lưu ý: Chỉ dùng khi người dùng yêu cầu dọn dẹp)
- **Compose UP**: `docker-compose up -d --build`
- **Compose DOWN**: `docker-compose down -v` (Thêm `-v` nếu muốn xóa volumes)

### Bước 5: Troubleshooting (Khắc phục sự cố)
Nếu gặp lỗi, Agent MẶC ĐỊNH phải thực hiện các bước sau để điều tra:
1. Đọc logs của container bị lỗi: `docker logs <container_name_or_id> --tail 50`
2. Kiểm tra trạng thái hiện tại: `docker ps -a`
3. Inspect chi tiết để tìm lỗi network/mount: `docker inspect <container_name_or_id>`
4. Nếu container crash liên tục, chạy shell tương tác (nếu có thể): `docker exec -it <container_name> /bin/sh` hoặc thay đổi entrypoint tạm thời để debug.

## Checklist dành cho AI Agent
- [ ] Base image đã được tối ưu (alpine/slim)?
- [ ] Dependencies cache có được áp dụng đúng thứ tự không (`COPY package.json` -> `RUN npm install` -> `COPY . .`)?
- [ ] File `.dockerignore` đã được tạo để loại bỏ `node_modules`, `.git`, file rác chưa?
- [ ] Port exposure có phù hợp với application config không?
- [ ] Data quan trọng có được lưu trữ vào Volume thay vì trong container layer không?
- [ ] Ứng dụng có được chạy dưới quyền non-root user không (nếu yêu cầu security cao)?

## Hướng dẫn xử lý một số case cụ thể

### 1. Tạo file `.dockerignore`
Luôn tạo file `.dockerignore` nằm cùng cấp với Dockerfile để tránh copy những file không cần thiết, làm nặng build context:
```text
node_modules/
dist/
.git/
.env
Dockerfile
docker-compose*.yml
npm-debug.log*
```

### 2. Xử lý lỗi cấp quyền trong Volume
Nếu database (như postgres/mysql) báo lỗi permissions khi mount volume trên Windows/Linux, hướng dẫn người dùng check lại ownership hoặc thêm biến môi trường phù hợp (`PUID`/`PGID` nếu hình ảnh hỗ trợ sửa quyền).

---
**LƯU Ý:** Khi phản hồi người dùng, hãy giải thích NGẮN GỌN lý do chọn base image, tại sao lại dùng multi-stage (nếu có), và cung cấp ngay câu lệnh CLI để họ copy & paste nhanh chóng.
