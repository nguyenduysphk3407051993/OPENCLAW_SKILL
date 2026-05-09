---
name: openzalo-setup
description: Use when setting up OpenZalo (Zalo personal account) as a messaging channel for OpenClaw. Covers installing openzca CLI, plugin, QR login, channel config, and troubleshooting.
metadata:
  {
    "openclaw":
      {
        "emoji": "💬",
        "requires": { "bins": ["npm", "git"] },
      },
  }
allowed-tools: ["exec", "read", "write", "edit"]
---

# OpenZalo Setup

Install and configure OpenZalo to use a personal Zalo account as a messaging channel for OpenClaw.

## Prerequisites

- OpenClaw installed and running
- Node.js v22+
- npm

## Step 1: Install openzca CLI

```bash
npm i -g openzca
openzca --version
```

**Note:** If permission denied, set npm prefix to user directory:
```bash
mkdir -p ~/.npm-global
npm config set prefix ~/.npm-global
echo 'export PATH=$HOME/.npm-global/bin:$PATH' >> ~/.bashrc
export PATH=$HOME/.npm-global/bin:$PATH
npm i -g openzca
```

## Step 2: Install OpenZalo Plugin

⚠️ **IMPORTANT:** Do NOT use `npm i -g @openclaw/openzalo` — must install via OpenClaw CLI.

```bash
cd /tmp
git clone https://github.com/darkamenosa/openzalo.git
openclaw plugins install /tmp/openzalo
```

**Alternative (if blocked by security scan):**
```bash
cp -r /tmp/openzalo ~/.openclaw/extensions/openzalo
cd ~/.openclaw/extensions/openzalo && npm install --production
```

## Step 3: Restart Gateway

```bash
openclaw gateway restart
openclaw plugins list
```

Verify: openzalo shows as **loaded/enabled**, no errors.

## Step 4: Login Zalo via QR Code

```bash
openclaw channels login --channel openzalo
```

QR code saves to file. Open Zalo app → Scan QR to login.

⚠️ **QR expires quickly** — scan immediately. If expired, re-run the command.

**Troubleshooting QR:**
- If `xdg-open ENOENT` error: create fake xdg-open:
  ```bash
  echo '#!/bin/sh' > ~/.npm-global/bin/xdg-open && chmod +x ~/.npm-global/bin/xdg-open
  ```
- If QR keeps expiring: run login in background with nohup

## Step 5: Add Channel Config

Edit `~/.openclaw/openclaw.json`, add to `channels`:

```json
"openzalo": {
  "enabled": true,
  "dmPolicy": "pairing",
  "groupPolicy": "allowlist",
  "textChunkLimit": 2000,
  "zcaBinary": "/path/to/openzca"
}
```

Also add to `plugins.allow` and `plugins.entries`:
```json
"plugins": {
  "allow": ["telegram", "moonshot", "openai", "browser", "openzalo"],
  "entries": {
    "openzalo": { "enabled": true }
  }
}
```

Add binding:
```json
"bindings": [
  { "agentId": "main", "match": { "channel": "telegram" } },
  { "agentId": "main", "match": { "channel": "openzalo" } }
]
```

⚠️ **Order matters:** Install plugin → restart → then add channel config.

**Important for container environments:**
If gateway can't find `openzca` binary (spawn ENOENT), set env in config:
```json
"env": {
  "OPENZCA_BINARY": "/home/node/.npm-global/lib/node_modules/openzca/dist/cli.js",
  "PATH": "/home/node/.npm-global/bin:/home/node/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
}
```

Then **restart the Docker container** (not just SIGUSR1) — env vars only load on full start.

## Step 6: Pairing

First message to bot on Zalo returns a pairing code. Approve with:
```bash
openclaw pairing approve openzalo XXXXXXXX
```

Done! Message again on Zalo — bot responds 🎉

## Step 7: Enable DB (Optional but Recommended)

```bash
openzca --profile default db enable
openzca --profile default db sync all --json
openzca --profile default db status --json
```

## Common Errors

| Error | Cause | Fix |
|---|---|---|
| `unknown channel id: openzalo` | Plugin not loaded | Install via `openclaw plugins install`, not npm |
| `plugin not found: openzalo` | Plugin not in extensions | Copy to `~/.openclaw/extensions/openzalo/` |
| `config invalid` | Wrong order | Install → restart → config |
| `spawn openzca ENOENT` | Binary not in PATH | Set `OPENZCA_BINARY` env + restart container |
| `openzca skill blocked` | `requires.bins` check fails | Fix bên dưới ↓ |
| `QR expired` | QR time limit | Re-run `openclaw channels login --channel openzalo` |
| Gateway crashes after config | Invalid JSON | Restore from `~/.openclaw/openclaw.json.bak` |

## Capabilities

| Direction | Text | Images | Voice | Files | Video |
|---|---|---|---|---|---|
| Send | ✅ | ✅ | ✅ | ✅ | ✅ |
| Receive | ✅ | ✅ | ✅* | ✅ | ✅ |

*Voice receive requires whisper plugin

### Fix: `openzca` skill báo blocked trong Docker container

Trong container, `openzca` không có trong PATH → skill `openzca` bị blocked do `requires: { bins: ["openzca"] }`.

**Cách 1 — Tạo wrapper script trong container (recommended):**

Trên host, chạy:
```bash
docker exec -u root openclaw-gateway sh -c 'cat > /usr/local/bin/openzca << '\''EOF'\''
#!/bin/sh
exec node /home/node/.npm-global/lib/node_modules/openzca/dist/cli.js "$@"
EOF
chmod +x /usr/local/bin/openzca'
docker exec openclaw-gateway openzca --version
```

**Cách 2 — Sửa skill metadata (nhanh, không cần root):**

Sửa `~/.openclaw/skills/openzca/SKILL.md`:
```diff
- "requires": { "bins": ["openzca"] },
+ "requires": {},
```
Rồi restart gateway.

**Cách 3 — Bỏ qua:**

Plugin OpenZalo dùng `OPENZCA_BINARY` env var → channel hoạt động bình thường.
Skill blocked chỉ ảnh hưởng các lệnh nâng cao qua `openzca` CLI (DB sync, group admin, poll...).
Nhắn tin Zalo cơ bản **không bị ảnh hưởng**.

## Tips

- Run multiple channels in parallel (Telegram + Zalo + Discord)
- Use `openclaw doctor --non-interactive` for health check
- Zalo limits 2000 chars/message — plugin auto-chunks
- Install openzca skill for advanced DB operations:
  ```bash
  cp -r /tmp/openzalo/skills/openzca ~/.openclaw/skills/openzca
  ```

## Verification Checklist

- [ ] `openzca --version` returns version
- [ ] `openclaw plugins list` shows openzalo enabled
- [ ] `openclaw status` shows OpenZalo ON/OK/configured
- [ ] `openzca auth status` shows logged in
- [ ] Message on Zalo → bot responds
- [ ] DB enabled and synced

---

**Credits:** Plugin by [@darkamenosa](https://github.com/darkamenosa/openzalo)
