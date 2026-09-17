---
name: hermes-plugin-development
description: Create Hermes plugins that hook into the agent lifecycle (post_llm_call, pre_tool_call, on_session_end, etc.). Covers plugin structure, available hooks, and macOS notification pattern.
triggers:
  - "create a hermes plugin"
  - "hermes notification"
  - "hook into hermes"
  - "after response hook"
  - "post_llm_call"
---

# Hermes Plugin Development

## Plugin Location
```
~/.hermes/plugins/<plugin-name>/
├── plugin.yaml      # manifest
└── __init__.py      # must be exactly this name
```

## plugin.yaml Structure
```yaml
name: my-plugin
version: 1.0.0
description: "What this plugin does"
author: your-name
requires_env: []        # optional: ["MY_API_KEY"]
pip_dependencies: []    # optional: ["requests>=2.28"]
hooks:
  - post_llm_call       # list the hooks this plugin uses
```

## __init__.py Structure
```python
def register(ctx) -> None:
    ctx.register_hook("post_llm_call", my_callback)

def my_callback(session_id="", user_message="", assistant_response="",
                conversation_history=None, model="", platform="", **kwargs):
    pass  # your logic here
```

## Valid Hook Names (VALID_HOOKS in plugins.py)
| Hook | When fired | Key kwargs |
|------|-----------|------------|
| `post_llm_call` | After every completed AI response | `session_id`, `user_message`, `assistant_response`, `model`, `platform` |
| `pre_llm_call` | Before LLM is called | |
| `pre_tool_call` | Before tool execution | |
| `post_tool_call` | After tool execution | |
| `pre_api_request` | Before API request | |
| `post_api_request` | After API request | |
| `on_session_start` | Session begins | `session_id`, `platform` |
| `on_session_end` | Session ends (safety net) | `session_id`, `platform` |
| `on_session_finalize` | Session finalizes cleanly | `session_id`, `platform` |
| `on_session_reset` | Session reset via /reset | `session_id`, `platform` |

## Testing a Plugin
```python
# /tmp/test_plugin.py
import sys
sys.path.insert(0, os.path.expanduser('~/.hermes/hermes-agent'))
from hermes_cli.plugins import get_plugin_manager, invoke_hook

pm = get_plugin_manager()
pm.discover_and_load()   # ← correct method (NOT _discover_user_plugins)

print('Plugins:', pm.list_plugins())
print('Hooks:', {k: [c.__module__ for c in v] for k,v in pm._hooks.items()})

invoke_hook("post_llm_call",
    session_id="test",
    user_message="test question",
    assistant_response="test response that is long enough",
    conversation_history=[],
    model="claude-sonnet-4.6",
    platform="cli",
)
```
Run: `cd ~/.hermes/hermes-agent && source venv/bin/activate && python3 /tmp/test_plugin.py`

## macOS Notification Pattern（含点击跳转）

### 基础版：osascript + afplay（无点击功能）
```python
import subprocess, threading

def notify(title: str, message: str, sound: str = "Glass"):
    def _run():
        t = threading.Thread(target=lambda: subprocess.Popen(
            ["afplay", f"/System/Library/Sounds/{sound}.aiff"],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
        ), daemon=True)
        t.start()
        safe_title = title.replace('"', '\\"')
        safe_msg = message.replace('"', '\\"')
        subprocess.run(["osascript", "-e",
            f'display notification "{safe_msg}" with title "{safe_title}"'],
            timeout=5, capture_output=True)
        t.join(timeout=10)
    threading.Thread(target=_run, daemon=True).start()

# Available sounds: Basso Blow Bottle Frog Funk Glass Hero Morse Ping Pop Purr Sosumi Submarine Tink
```

### 高级版：terminal-notifier（支持点击跳转 URL 或激活终端）
`brew install terminal-notifier`

```python
import shutil, os, subprocess

def notify_with_click(title, message, open_url=None, terminal_app=None, sound="Glass"):
    tn = shutil.which("terminal-notifier") or "/opt/homebrew/bin/terminal-notifier"
    if not os.path.exists(tn):
        return  # fallback to osascript
    cmd = [tn, "-title", title, "-message", message, "-group", "hermes"]
    if sound:
        cmd += ["-sound", sound]
    if open_url:
        # Web UI 模式：打开 URL 并激活 Chrome
        cmd += ["-open", open_url, "-activate", "com.google.chrome"]
    elif terminal_app:
        # 终端模式：-execute 传可执行脚本（无扩展名！）
        script = "/tmp/hermes_activate_terminal"  # 不能用 .sh！
        with open(script, "w") as f:
            f.write(f'#!/bin/bash\nosascript -e \'tell application "{terminal_app}" to activate\'\n')
        os.chmod(script, 0o755)
        cmd += ["-execute", script]
    subprocess.run(cmd, timeout=5, capture_output=True)
```

**⚠️ 关键陷阱：`-execute` 脚本文件绝对不能有 `.sh` 扩展名！**
macOS 会把 `.sh` 文件用 Script Editor 打开，而不是执行它。文件名用无扩展名（如 `/tmp/hermes_activate_terminal`）。

**⚠️ macOS 15 上 NSUserNotificationCenter 已废弃**，`defaultUserNotificationCenter()` 返回 `None`，pyobjc 方案无法使用。坚持用 `terminal-notifier`。

**Web UI URL 格式**：`http://localhost:8648/#/hermes/chat`（不是 `/?session=xxx`）

## Pitfalls
1. **`__init__.py` filename** — when using `write_file` tool, escape as `\__init__.py` causes the file to be named `\\__init__.py`. Use `execute_code` + Python `open()` to write `__init__.py`, or use `terminal` with `cat >`.
   - Fix: `cp '\__init__.py' __init__.py` or use `execute_code` with `open(path, 'w')`
2. **`_discover_user_plugins()` does not exist** — use `pm.discover_and_load()` instead
3. **bell_on_complete** is just `\a` terminal bell, not a system notification — for real macOS banners you need the plugin approach
4. **macOS notification permissions** — if notifications don't appear, check System Settings → Notifications → Script Editor (or Terminal)
5. **Always use `**kwargs`** in hook callbacks — future versions may add new kwargs

## Working Example: hermes-notification
Full implementation at `~/.hermes/plugins/hermes-notification/`. Sends macOS banner + Glass sound after every Hermes response. Config via `~/.hermes/plugins/hermes-notification/config.json`.
