---
name: hermes-web-ui
description: 启动、配置和排查 hermes-web-ui 面板，包括 Node.js 版本要求和 nvm 持久化配置。
tags: [hermes, web-ui, nodejs, nvm]
---

# hermes-web-ui

hermes-web-ui 是 Hermes Agent 的浏览器图形界面，默认端口 8648，通过 hermes api_server（默认端口 8642）与 agent 通信。

启动成功后输出带 token 的完整访问地址，格式：
  http://localhost:8648/#/?token=<your_token>

## 常用命令

  start / stop / status / restart

日志位置：HOME/.hermes-web-ui/server.log

## 已知问题：node:sqlite 报错导致启动失败

### 症状

日志报 ERR_UNKNOWN_BUILTIN_MODULE: No such built-in module: node:sqlite

### 原因

hermes-web-ui 依赖 node:sqlite，该内置模块在 Node.js v22.5.0 才引入，v20 及以下会直接崩溃。

### 修复步骤

1. 安装并切换 Node.js v22（通过 nvm）
2. 重装 hermes-web-ui（让 bin shebang 指向新 node 路径）
3. 验证 which hermes-web-ui 输出路径含 v22
4. 再次 start

### 持久化 nvm 版本

在 .zshrc 中 nvm 加载行之后追加：
  nvm use 22 --silent

同时执行：
  nvm alias default 22

--silent 参数避免每次开终端打印版本提示。

## 开机自启动（macOS LaunchAgent）

plist 路径：`~/Library/LaunchAgents/ai.hermes.web-ui.plist`

### 常见问题：plist 启动失败（exit code 1）

**原因1**：plist 里写的是旧版 node（如 v20）路径，但 hermes-web-ui 需要 v22+。  
检查：`launchctl list | grep hermes.web-ui` 看 exit code，exit code=1 即失败。  
修复：把 ProgramArguments 和 PATH 里的 node 路径改成 v22：
```
/Users/<用户名>/.nvm/versions/node/v22.x.x/bin/hermes-web-ui
```
查 v22 实际路径：`ls ~/.nvm/versions/node/v22*/bin/hermes-web-ui`

**原因2**：`hermes-web-ui start` 在服务已运行时返回 exit code 1（"already running"），LaunchAgent 会认为失败并不断重试。  
修复：用包装脚本替代直接调用：

```bash
# ~/.hermes/scripts/start-web-ui.sh
#!/bin/bash
HERMES_WEB_UI="/Users/<用户名>/.nvm/versions/node/v22.x.x/bin/hermes-web-ui"
if "$HERMES_WEB_UI" status 2>&1 | grep -q "is running"; then
    exit 0
fi
"$HERMES_WEB_UI" start
exit 0
```

plist ProgramArguments 改为：
```xml
<array>
    <string>/bin/bash</string>
    <string>/Users/<用户名>/.hermes/scripts/start-web-ui.sh</string>
</array>
```

重载 plist：
```bash
launchctl unload ~/Library/LaunchAgents/ai.hermes.web-ui.plist
launchctl load ~/Library/LaunchAgents/ai.hermes.web-ui.plist
launchctl list | grep hermes.web-ui  # exit code 应为 0
```

## api_server 配置（hermes 侧）

相关配置在 hermes config.yaml 的 platforms.api_server 节点下：
  enabled, host, port, key（token）, cors_origins

修改后执行 hermes gateway restart 生效。
