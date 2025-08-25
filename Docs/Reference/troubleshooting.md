# SuperClaude トラブルシューティングガイド 🔧

SuperClaude Frameworkの問題に対するクイック修正から高度な診断まで。

## クイック修正（問題の90%）

**インストール確認:**
```bash
python3 -m SuperClaude --version    # Should show 4.0.8
SuperClaude install --list-components
```

**コマンド問題:**
```bash
# Test in Claude Code:
/sc:brainstorm "test project"        # Should ask discovery questions

# If no response: Restart Claude Code session
```

**解決チェックリスト:**
- [ ] Version commands work and show 4.0.8
- [ ] `/sc:` commands respond in Claude Code  
- [ ] MCP servers listed: `SuperClaude install --list-components | grep mcp`

## 一般的な問題

### インストール問題

**パッケージインストール失敗:**
```bash
# For pipx users
pipx uninstall SuperClaude
pipx install SuperClaude

# For pip users
pip uninstall SuperClaude
pip install --upgrade pip
pip install SuperClaude
```

**権限拒否 / PEP 668エラー:**
```bash
# Option 1: Use pipx (recommended)
pipx install SuperClaude

# Option 2: Use pip with --user flag
pip install --user SuperClaude

# Option 3: Fix permissions
sudo chown -R $USER ~/.claude

# Option 4: Force installation (use with caution)
pip install --break-system-packages SuperClaude
```

**コンポーネント不足:**
```bash
python3 -m SuperClaude install --components core commands agents modes --force
```

### コマンド問題

**コマンドが認識されない:**
1. Restart Claude Code completely
2. Verify: `python3 -m SuperClaude --version`
3. Test: `/sc:brainstorm "test"`

**エージェントが活性化しない:**
- Use specific keywords: `/sc:implement "secure JWT authentication"`
- Manual activation: `@agent-security "review auth code"`

**パフォーマンス低下:**
```bash
/sc:analyze . --no-mcp               # Test without MCP servers
/sc:analyze src/ --scope file        # Limit scope
```

### MCPサーバー問題

**サーバー接続失敗:**
```bash
ls ~/.claude/.claude.json            # Check config exists
node --version                       # Verify Node.js 16+
SuperClaude install --components mcp --force
```

**APIキー必須（Magic/Morphllm）:**
```bash
export TWENTYFIRST_API_KEY="your_key"
export MORPH_API_KEY="your_key"
# Or use: /sc:command --no-mcp
```

## 高度な診断

**システム分析:**
```bash
SuperClaude install --diagnose
cat ~/.claude/logs/superclaude.log | tail -50
```

**コンポーネント分析:**
```bash
ls -la ~/.claude/                    # Check installed files
grep -r "@" ~/.claude/CLAUDE.md      # Verify imports
```

**インストールリセット:**
```bash
SuperClaude backup --create          # Backup first
SuperClaude uninstall
SuperClaude install --fresh
```

## Get Help

**Documentation:**
- [Installation Guide](../Getting-Started/installation.md) - Setup issues
- [Commands Guide](../User-Guide/commands.md) - Usage issues

**Community:**
- [GitHub Issues](https://github.com/SuperClaude-Org/SuperClaude_Framework/issues)
- Include: OS, Python version, error message, steps to reproduce
