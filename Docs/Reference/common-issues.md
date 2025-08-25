# SuperClaude よくある問題 - クイックリファレンス 🚀

**問題解決ガイド**: 実用的解決策付きの最も頻繁な問題。

## トップ5クイック修正（問題の90%）

### 1. Claude Codeでコマンドが動作しない ⚡
```
Problem: /sc:brainstorm doesn't work
Solution: Restart Claude Code completely
Test: /sc:brainstorm "test" should ask questions
```

### 2. インストール確認
```bash
python3 -m SuperClaude --version    # Should show 4.0.8

# If not working:
# For pipx users
pipx upgrade SuperClaude

# For pip users
pip install --upgrade SuperClaude

# Then reinstall
python3 -m SuperClaude install
```

### 3. 権限問題
```bash
# Permission denied / PEP 668 errors:
# Option 1: Use pipx (recommended)
pipx install SuperClaude

# Option 2: Use pip with --user
pip install --user SuperClaude

# Option 3: Fix permissions
sudo chown -R $USER ~/.claude
```

### 4. MCPサーバー問題
```bash
/sc:analyze . --no-mcp              # Test without MCP servers
node --version                      # Check Node.js 16+ if needed
```

### 5. コンポーネント不足
```bash
python3 -m SuperClaude install --components core commands agents modes --force
```

## プラットフォーム固有の問題

**Windows:**
```cmd
set CLAUDE_CONFIG_DIR=%USERPROFILE%\.claude
python -m SuperClaude install --install-dir "%CLAUDE_CONFIG_DIR%"
```

**macOS:**
```bash
brew install python3 node
pip3 install SuperClaude
```

**Linux:**
```bash
sudo apt install python3 python3-pip nodejs
pip3 install SuperClaude
```

## 確認チェックリスト
- [ ] `python3 -m SuperClaude --version` returns 4.0.8
- [ ] `/sc:brainstorm "test"` works in Claude Code
- [ ] `SuperClaude install --list-components` shows components

## クイック修正が効かない場合
高度な診断については[トラブルシューティングガイド](troubleshooting.md)を参照してください。
