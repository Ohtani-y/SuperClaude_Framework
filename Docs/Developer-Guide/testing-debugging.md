# SuperClaude 検証とトラブルシューティングガイド

## 概要

このガイドでは、SuperClaudeインストールの検証方法と、コンテキストファイルと設定の一般的な問題のトラブルシューティング方法について説明します。

**重要**: SuperClaudeは実行可能ソフトウェアではなく、コンテキストファイルの集合です。このガイドでは、コンテキストファイルが適切にインストールされ、Claude Codeからアクセス可能であることの検証に焦点を当てています。

## 目次

1. [インストール検証](#installation-verification)
2. [コンテキストファイル検証](#context-file-verification)
3. [MCPサーバー検証](#mcp-server-verification)
4. [一般的な問題](#common-issues)
5. [トラブルシューティングコマンド](#troubleshooting-commands)

## インストール検証

### インストール状態確認

```bash
# Verify SuperClaude installation system is available
python3 -m SuperClaude --version
# Expected: SuperClaude Framework installation help

# Verify Claude Code CLI integration
claude --version
# Expected: Claude Code version info

# Check if context files were installed
ls ~/.claude/
# Expected: CLAUDE.md, FLAGS.md, RULES.md, agents/, commands/, modes/

# Verify main context file
head ~/.claude/CLAUDE.md
# Expected: Should show import statements
```

### ディレクトリ構造確認

```bash
# Check all directories exist
for dir in agents commands modes; do
    if [ -d ~/.claude/$dir ]; then
        echo "✅ $dir directory exists"
        ls ~/.claude/$dir | wc -l
    else
        echo "❌ $dir directory missing"
    fi
done
```

### インストール済みコンポーネント数確認

```bash
# Should have 14 agents
ls ~/.claude/agents/*.md | wc -l

# Should have 21 commands  
ls ~/.claude/commands/*.md | wc -l

# Should have 5 modes
ls ~/.claude/modes/*.md | wc -l
```

## コンテキストファイル検証

### コアファイル確認

```bash
# Check core context files exist
for file in CLAUDE.md FLAGS.md RULES.md PRINCIPLES.md; do
    if [ -f ~/.claude/$file ]; then
        echo "✅ $file exists ($(wc -l < ~/.claude/$file) lines)"
    else
        echo "❌ $file missing"
    fi
done
```

### インポートシステム確認

```bash
# Check CLAUDE.md has correct imports
grep "@import" ~/.claude/CLAUDE.md
# Expected output:
# @import commands/*.md
# @import agents/*.md
# @import modes/*.md
# @import FLAGS.md
# @import RULES.md
# @import PRINCIPLES.md
```

### ファイル整合性確認

```bash
# Verify files are readable text files
file ~/.claude/CLAUDE.md
# Expected: ASCII text or UTF-8 text

# Check for corruption
for file in ~/.claude/**/*.md; do
    if file "$file" | grep -q "text"; then
        echo "✅ $file is valid text"
    else
        echo "❌ $file may be corrupted"
    fi
done
```

## MCPサーバー検証

### MCP設定確認

```bash
# Verify .claude.json exists
if [ -f ~/.claude.json ]; then
    echo "✅ MCP configuration file exists"
    # Check which servers are configured
    grep -o '"[^"]*":' ~/.claude.json | grep -v mcpServers
else
    echo "❌ No MCP configuration found"
fi
```

### MCPサーバー可用性テスト

```bash
# Check if Node.js is available (required for MCP)
node --version
# Expected: v16.0.0 or higher

# Check if npx is available
npx --version
# Expected: Version number

# Test Context7 MCP (if configured)
npx -y @upstash/context7-mcp@latest --help 2>/dev/null && echo "✅ Context7 available" || echo "❌ Context7 not available"
```

## 一般的な問題

### 問題: コマンドが動作しない

**症状**: `/sc:` コンテキストトリガーが期待されるClaude Code動作を生成しない

**検証**:
```bash
# Check if command file exists
ls ~/.claude/commands/implement.md
# If missing, reinstall SuperClaude

# Verify file content
head -20 ~/.claude/commands/implement.md
# Should show command metadata and instructions
```

**Solution**:
```bash
# Reinstall commands component
PYTHONPATH=/path/to/SuperClaude_Framework python3 -m setup install --components commands --force
```

### 問題: エージェントが活性化しない

**症状**: `@agent-` 呼び出しがClaude Codeで動作しない

**検証**:
```bash
# List all agents
ls ~/.claude/agents/

# Check specific agent
cat ~/.claude/agents/python-expert.md | head -20
```

**Solution**:
```bash
# Reinstall agents
PYTHONPATH=/path/to/SuperClaude_Framework python3 -m setup install --components agents --force
```

### 問題: コンテキストが読み込まれない

**症状**: Claude CodeがSuperClaudeコンテキストを読み取らない

**検証**:
```bash
# Check CLAUDE.md is in correct location
ls -la ~/.claude/CLAUDE.md

# Verify Claude Code can access the directory
# In Claude Code, check if context is loading properly
```

**Solution**:
1. Restart Claude Code
2. Ensure you're in a project directory
3. Check file permissions: `chmod 644 ~/.claude/*.md`

### 問題: MCPサーバーが動作しない

**症状**: MCP機能が利用できない

**検証**:
```bash
# Check Node.js installation
which node

# Verify .claude.json syntax
python3 -c "import json; json.load(open('$HOME/.claude.json'))" && echo "✅ Valid JSON" || echo "❌ Invalid JSON"
```

**Solution**:
```bash
# Install Node.js if missing
# Ubuntu: sudo apt install nodejs npm
# macOS: brew install node
# Windows: Download from nodejs.org

# Fix JSON syntax if invalid
PYTHONPATH=/path/to/SuperClaude_Framework python3 -m setup install --components mcp --force
```

## トラブルシューティングコマンド

### クイック診断

```bash
#!/bin/bash
# SuperClaude Quick Diagnostic Script

echo "=== SuperClaude Diagnostic ==="
echo ""

# Check installation system
echo "1. Installation System:"
if command -v SuperClaude &> /dev/null; then
    echo "   ✅ SuperClaude installation available"
    python3 -m SuperClaude --version
else
    echo "   ❌ SuperClaude not found - install with: pipx install SuperClaude (or pip install SuperClaude)"
fi

# Check context files
echo ""
echo "2. Context Files:"
if [ -d ~/.claude ]; then
    echo "   ✅ ~/.claude directory exists"
    echo "   - Agents: $(ls ~/.claude/agents/*.md 2>/dev/null | wc -l)"
    echo "   - Commands: $(ls ~/.claude/commands/*.md 2>/dev/null | wc -l)"
    echo "   - Modes: $(ls ~/.claude/modes/*.md 2>/dev/null | wc -l)"
else
    echo "   ❌ ~/.claude directory not found"
fi

# Check MCP
echo ""
echo "3. MCP Configuration:"
if [ -f ~/.claude.json ]; then
    echo "   ✅ MCP configuration exists"
else
    echo "   ❌ No MCP configuration"
fi

# Check Node.js
echo ""
echo "4. Node.js (for MCP):"
if command -v node &> /dev/null; then
    echo "   ✅ Node.js installed: $(node --version)"
else
    echo "   ⚠️  Node.js not installed (optional, needed for MCP)"
fi

echo ""
echo "=== Diagnostic Complete ==="
```

### ファイル権限修正

```bash
# Fix permissions on all context files
chmod 644 ~/.claude/*.md
chmod 644 ~/.claude/**/*.md
chmod 755 ~/.claude ~/.claude/agents ~/.claude/commands ~/.claude/modes
```

### 完全再インストール

```bash
# Backup existing configuration
cp -r ~/.claude ~/.claude.backup.$(date +%Y%m%d)

# Remove existing installation
rm -rf ~/.claude

# Reinstall everything
PYTHONPATH=/path/to/SuperClaude_Framework python3 -m setup install

# Restore any customizations from backup if needed
```

## 重要な注意事項

### 検証しないもの

- **コード実行なし**: コンテキストファイルは実行されないため、ランタイム検証は不要
- **パフォーマンスメトリクスなし**: コードが実行されないため、測定するパフォーマンスなし
- **ユニットテストなし**: コンテキストファイルは関数ではなく指示
- **統合テストなし**: Claude Codeがファイルを読み取る；検証は動作的

### 検証するもの

- **ファイル存在**: コンテキストファイルが正しい場所に存在
- **ファイル整合性**: ファイルが有効なテキストで読み取り可能
- **ディレクトリ構造**: 適切な組織が維持されている
- **設定有効性**: JSONファイルが構文的に正しい
- **依存関係利用可能**: MCPサーバー用Node.js（オプション）
- **動作テスト**: コンテキストファイルが期待されるClaude Code動作を生成

## まとめ

SuperClaudeの検証は、コンテキストファイルが適切にインストールされ、Claude Codeからアクセス可能であることの確認に焦点を当てています。SuperClaudeはソフトウェアではなく設定フレームワークであるため、検証はファイル存在、整合性、およびClaude Code会話での動作テストを中心としています。
