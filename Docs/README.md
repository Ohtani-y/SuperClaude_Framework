# SuperClaude ドキュメント

## 🎯 基本的な理解

**SuperClaudeはClaude Code用のコンテキストフレームワーク**です。Claude Codeが読み取って機能を強化する動作指示ファイルをインストールします。

### 動作原理
1. **インストール**: Python CLIがコンテキストファイルを`~/.claude/`にインストール
2. **コマンド**: `/sc:analyze`と入力 → Claude Codeが`analyze.md`指示ファイルを読み取り
3. **動作**: Claudeがコンテキストファイルで定義された動作を採用
4. **結果**: コンテキスト切り替えによる強化された開発ワークフロー

## 🚀 クイックスタート（5分）

**新規ユーザー**: [クイックスタートガイド →](Getting-Started/quick-start.md)
```bash
# Linux/macOS推奨
pipx install SuperClaude && SuperClaude install

# 従来の方法
pip install SuperClaude && SuperClaude install

# その後Claude Codeで試してください: /sc:brainstorm "ウェブアプリのアイデア"
```

**問題がある場合**: [クイック修正 →](Reference/common-issues.md) | [トラブルシューティング →](Reference/troubleshooting.md)

## 📚 Documentation Structure

### 🌱 Start Here (New Users)
| Guide | Purpose |
|-------|---------|
| **[Quick Start](Getting-Started/quick-start.md)** | Setup and first commands |
| **[Installation](Getting-Started/installation.md)** | Detailed setup instructions |
| **[Commands Guide](User-Guide/commands.md)** | All 21 `/sc:` commands |

### 🌿 Daily Usage (Regular Users)
| Guide | Purpose | Use For |
|-------|---------|---------|
| **[Commands Guide](User-Guide/commands.md)** | Master all `/sc:` commands | Daily development |
| **[Agents Guide](User-Guide/agents.md)** | 14 domain specialists (`@agent-*`) | Expert assistance |
| **[Flags Guide](User-Guide/flags.md)** | Command behavior modification | Optimization |
| **[Modes Guide](User-Guide/modes.md)** | 5 behavioral modes | Workflow optimization |

### 🌲 Reference & Advanced (Power Users)
| Guide | Purpose | Use For |
|-------|---------|---------|
| **[Troubleshooting](Reference/troubleshooting.md)** | Problem resolution | When things break |
| **[Examples Cookbook](Reference/examples-cookbook.md)** | Practical usage patterns | Learning workflows |
| **[MCP Servers](User-Guide/mcp-servers.md)** | 6 enhanced capabilities | Advanced features |

### 🔧 Development & Contributing
| Guide | Purpose | Audience |
|-------|---------|----------|
| **[Technical Architecture](Developer-Guide/technical-architecture.md)** | System design | Contributors |
| **[Contributing](Developer-Guide/contributing-code.md)** | Development workflow | Developers |

## 🔑 主要概念

### インストールされるもの
- **Python CLIツール** - フレームワークインストールの管理
- **コンテキストファイル** - `~/.claude/`内の`.md`動作指示
- **MCP設定** - オプションの外部ツール設定

### フレームワークコンポーネント
- **21のコマンド**（`/sc:*`） - ワークフロー自動化パターン
- **14のエージェント**（`@agent-*`） - ドメイン専門家
- **5つのモード** - 動作変更パターン
- **6つのMCPサーバー** - オプションの外部ツール

## 🚀 クイックコマンドリファレンス

### ターミナルで（インストール）
```bash
# フレームワークをインストール（いずれかを選択）
pipx install SuperClaude       # Linux/macOS推奨
pip install SuperClaude        # 従来の方法
npm install -g @bifrost_inc/superclaude  # クロスプラットフォーム

# 設定と維持
SuperClaude install            # Claude Codeを設定
SuperClaude update             # フレームワークを更新
python3 -m SuperClaude --version  # インストール確認
```

### Claude Codeで（使用）
```bash
/sc:brainstorm "プロジェクトアイデア"              # 新しいプロジェクトを開始
/sc:implement "機能"                    # 機能を構築
/sc:analyze src/                           # コードを分析
@agent-python-expert "これを最適化"      # 手動専門家
@agent-security "認証をレビュー"   # セキュリティレビュー
```

## 📊 Framework vs Software Comparison

| Component | Type | Where It Runs | What It Does |
|-----------|------|---------------|--------------|
| **SuperClaude Framework** | Context Files | Read by Claude Code | Modifies AI behavior |
| **Claude Code** | Software | Your computer | Executes everything |
| **MCP Servers** | Software | Node.js processes | Provide tools |
| **Python CLI** | Software | Python runtime | Manages installation |

## 🔄 How Everything Connects

```
User Input → Claude Code → Reads SuperClaude Context → Modified Behavior → Enhanced Output
                ↓
        May use MCP Servers
         (if configured)
```

## 🆘 Getting Help

**Quick Issues** (< 2 min): [Common Issues →](Reference/common-issues.md)  
**Complex Problems**: [Full Troubleshooting Guide →](Reference/troubleshooting.md)  
**Installation Issues**: [Installation Guide →](Getting-Started/installation.md)  
**Command Help**: [Commands Guide →](User-Guide/commands.md)  
**Community Support**: [GitHub Discussions](https://github.com/SuperClaude-Org/SuperClaude_Framework/discussions)

## 🤔 Common Misconceptions Clarified

❌ **"SuperClaude is an AI assistant"**  
✅ SuperClaude is a configuration framework that enhances Claude Code

❌ **"I'm running SuperClaude"**  
✅ You're running Claude Code with SuperClaude context loaded

❌ **"Claude Code executes; SuperClaude provides context my commands"**  
✅ Claude Code executes everything; SuperClaude provides the instructions

❌ **"The .md files are documentation"**  
✅ The .md files ARE the framework - active instruction sets

---

*Remember: SuperClaude enhances Claude Code through context - it doesn't replace it or run alongside it. Everything happens within Claude Code itself.*
