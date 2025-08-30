# SuperClaude コマンドガイド

SuperClaudeはClaude Code用に21のコマンドを提供：ワークフロー用の`/sc:*`コマンドと専門家用の`@agent-*`。

## コマンドタイプ

| タイプ | 使用場所 | 形式 | 例 |
|------|------------|--------|---------|
| **スラッシュコマンド** | Claude Code | `/sc:[command]` | `/sc:implement "feature"` |
| **エージェント** | Claude Code | `@agent-[name]` | `@agent-security "review"` |
| **インストール** | ターミナル | `SuperClaude [command]` | `SuperClaude install` |

## クイックテスト
```bash
# ターミナル: インストールの確認
python3 -m SuperClaude --version
# Claude Code CLIの確認: claude --version

# Claude Code: コマンドのテスト
/sc:brainstorm "テストプロジェクト"    # 発見のための質問を行うはず
/sc:analyze README.md           # 分析を提供するはず
```

**ワークフロー**: `/sc:brainstorm "idea"` → `/sc:implement "feature"` → `/sc:test`

## 🎯 SuperClaudeコマンドの理解

## SuperClaudeの動作原理

SuperClaudeは、Claude Codeが専門的な動作を採用するために読み取る動作コンテキストファイルを提供します。`/sc:implement`と入力すると、Claude Codeは`implement.md`コンテキストファイルを読み取り、その動作指示に従います。

**SuperClaudeコマンドはソフトウェアによって実行されません** - これらはフレームワークから専門的な指示ファイルを読み取ることでClaude Codeの動作を変更するコンテキストトリガーです。

### コマンドタイプ:
- **スラッシュコマンド** (`/sc:*`): ワークフローパターンと動作モードをトリガー
- **エージェント呼び出し** (`@agent-*`): 特定のドメイン専門家を手動で活性化
- **フラグ** (`--think`, `--safe-mode`): コマンドの動作と深度を変更

### コンテキストメカニズム:
1. **ユーザー入力**: `/sc:implement "auth system"`と入力
2. **コンテキスト読み込み**: Claude Codeが`~/.claude/SuperClaude/Commands/implement.md`を読み取り
3. **動作採用**: Claudeがドメイン専門知識、ツール選択、検証パターンを適用
4. **強化された出力**: セキュリティ考慮事項とベストプラクティスを含む構造化実装

**重要ポイント**: これは従来のソフトウェア実行ではなく、コンテキスト管理を通じて洗練された開発ワークフローを作成します。

### インストールコマンド vs 使用コマンド

**🖥️ ターミナルコマンド** (実際のCLIソフトウェア):
- `SuperClaude install` - フレームワークコンポーネントをインストール
- `SuperClaude update` - 既存のインストールを更新  
- `SuperClaude uninstall` - フレームワークのインストールを削除
- `python3 -m SuperClaude --version` - インストール状態を確認

**💬 Claude Codeコマンド** (コンテキストトリガー):
- `/sc:brainstorm` - 要件発見コンテキストを活性化
- `/sc:implement` - 機能開発コンテキストを活性化
- `@agent-security` - セキュリティ専門家コンテキストを活性化
- すべてのコマンドはClaude Codeチャットインターフェース内でのみ動作


> **クイックスタート**: `/sc:brainstorm "プロジェクトアイデア"` → `/sc:implement "機能名"` → `/sc:test` でコアワークフローを体験してみてください。

## 🧪 Testing Your Setup

### 🖥️ Terminal Verification (Run in Terminal/CMD)
```bash
# SuperClaudeが動作しているか確認（主要な方法）
python3 -m SuperClaude --version
# 出力例: SuperClaude 4.0.8

# Claude Code CLIバージョンチェック
claude --version

# インストール済みコンポーネントの確認
python3 -m SuperClaude install --list-components | grep mcp
# 出力例: インストール済みMCPコンポーネントを表示
```

### 💬 Claude Code Testing (Type in Claude Code Chat)
```
# 基本的な /sc: コマンドのテスト
/sc:brainstorm "テストプロジェクト"
# 期待される動作: インタラクティブな要件発見が開始

# コマンドヘルプのテスト
/sc:help
# 期待される動作: 利用可能なコマンドのリスト表示
```

**テストが失敗した場合**: [インストールガイド](../Getting-Started/installation.md) または [トラブルシューティング](#troubleshooting) を確認してください

### 📝 Command Quick Reference

| Command Type | Where to Run | Format | Purpose | Example |
|-------------|--------------|--------|---------|----------|
| **🖥️ Installation** | Terminal/CMD | `SuperClaude [command]` | Setup and maintenance | `SuperClaude install` |
| **🔧 Configuration** | Terminal/CMD | `python3 -m SuperClaude [command]` | Advanced configuration | `python3 -m SuperClaude --version` |
| **💬 Slash Commands** | Claude Code | `/sc:[command]` | Workflow automation | `/sc:implement "feature"` |
| **🤖 Agent Invocation** | Claude Code | `@agent-[name]` | Manual specialist activation | `@agent-security "review"` |
| **⚡ Enhanced Flags** | Claude Code | `/sc:[command] --flags` | Behavior modification | `/sc:analyze --think-hard` |

> **重要**: すべての `/sc:` コマンドと `@agent-` 呼び出しは、ターミナルではなくClaude Codeチャット内で動作します。これらはClaude CodeがSuperClaudeフレームワークから特定のコンテキストファイルを読み取るようトリガーします。

## Table of Contents

- [必須コマンド](#essential-commands) - ここから始める（8つのコアコマンド）
- [一般的なワークフロー](#common-workflows) - 有効なコマンドの組み合わせ
- [完全なコマンドリファレンス](#full-command-reference) - カテゴリ別に整理された21のコマンドすべて
- [トラブルシューティング](#troubleshooting) - 一般的な問題と解決策
- [コマンドインデックス](#command-index) - カテゴリ別にコマンドを検索

---

## Essential Commands

**即座に生産性を向上させるコアワークフローコマンド:**

### `/sc:brainstorm` - Project Discovery
**Purpose**: Interactive requirements discovery and project planning  
**Syntax**: `/sc:brainstorm "your idea"` `[--strategy systematic|creative]`  

**使用例**: 
- 新規プロジェクト計画: `/sc:brainstorm "Eコマースプラットフォーム"`
- 機能探索: `/sc:brainstorm "ユーザー認証システム"`  
- 問題解決: `/sc:brainstorm "遅いデータベースクエリ"`

### `/sc:implement` - Feature Development  
**Purpose**: Full-stack feature implementation with intelligent specialist routing  
**Syntax**: `/sc:implement "feature description"` `[--type frontend|backend|fullstack] [--focus security|performance]`  

**使用例**:
- 認証: `/sc:implement "JWTログインシステム"`
- UIコンポーネント: `/sc:implement "レスポンシブダッシュボード"`
- API: `/sc:implement "RESTユーザーエンドポイント"`
- データベース: `/sc:implement "リレーション付きユーザースキーマ"`

### `/sc:analyze` - Code Assessment
**Purpose**: Comprehensive code analysis across quality, security, and performance  
**Syntax**: `/sc:analyze [path]` `[--focus quality|security|performance|architecture]`

**使用例**:
- プロジェクトの健全性: `/sc:analyze .`
- セキュリティ監査: `/sc:analyze --focus security`
- パフォーマンスレビュー: `/sc:analyze --focus performance`

### `/sc:troubleshoot` - Problem Diagnosis
**Purpose**: Systematic issue diagnosis with root cause analysis  
**Syntax**: `/sc:troubleshoot "issue description"` `[--type build|runtime|performance]`

**使用例**:
- ランタイムエラー: `/sc:troubleshoot "ログイン時の500エラー"`
- ビルド失敗: `/sc:troubleshoot --type build`
- パフォーマンス問題: `/sc:troubleshoot "ページ読み込みが遅い"`

### `/sc:test` - Quality Assurance
**Purpose**: Comprehensive testing with coverage analysis  
**Syntax**: `/sc:test` `[--type unit|integration|e2e] [--coverage] [--fix]`

**使用例**:
- 完全なテストスイート: `/sc:test --coverage`
- ユニットテスト: `/sc:test --type unit --watch`
- E2E検証: `/sc:test --type e2e`

### `/sc:improve` - Code Enhancement  
**Purpose**: Apply systematic code improvements and optimizations  
**Syntax**: `/sc:improve [path]` `[--type performance|quality|security] [--preview]`

**使用例**:
- 一般的な改善: `/sc:improve src/`
- パフォーマンス最適化: `/sc:improve --type performance`
- セキュリティ強化: `/sc:improve --type security`

### `/sc:document` - Documentation Generation
**Purpose**: Generate comprehensive documentation for code and APIs  
**Syntax**: `/sc:document [path]` `[--type api|user-guide|technical] [--format markdown|html]`

**使用例**:
- APIドキュメント: `/sc:document --type api`
- ユーザーガイド: `/sc:document --type user-guide`
- 技術ドキュメント: `/sc:document --type technical`

### `/sc:workflow` - Implementation Planning
**Purpose**: Generate structured implementation plans from requirements  
**Syntax**: `/sc:workflow "feature description"` `[--strategy agile|waterfall] [--format markdown]`

**使用例**:
- 機能計画: `/sc:workflow "ユーザー認証"`
- スプリント計画: `/sc:workflow --strategy agile`
- アーキテクチャ計画: `/sc:workflow "マイクロサービス移行"`

---

## Common Workflows

**実証済みのコマンドの組み合わせ:**

### New Project Setup
```bash
/sc:brainstorm "プロジェクトコンセプト"     # 要件を定義
/sc:design "システムアーキテクチャ"        # 技術設計を作成  
/sc:workflow "実装計画"                 # 開発ロードマップを生成
```

### Feature Development
```bash
/sc:implement "機能名"                 # 機能を構築
/sc:test --coverage                   # テストで検証
/sc:document --type api               # ドキュメントを生成  
```

### Code Quality Improvement
```bash
/sc:analyze --focus quality           # 現在の状態を評価
/sc:improve --preview                 # 改善をプレビュー
/sc:test --coverage                   # 変更を検証
```

### Bug Investigation
```bash
/sc:troubleshoot "問題の説明"          # 問題を診断
/sc:analyze --focus problem-area      # 深い分析
/sc:improve --fix --safe-mode         # ターゲット修正を適用
```

## Full Command Reference

### Development Commands
| Command | Purpose | Best For |
|---------|---------|----------|
| **workflow** | Implementation planning | Project roadmaps, sprint planning |
| **implement** | Feature development | Full-stack features, API development |
| **build** | Project compilation | CI/CD, production builds |
| **design** | System architecture | API specs, database schemas |

### Analysis Commands  
| Command | Purpose | Best For |
|---------|---------|----------|
| **analyze** | Code assessment | Quality audits, security reviews |
| **troubleshoot** | Problem diagnosis | Bug investigation, performance issues |
| **explain** | Code explanation | Learning, code reviews |

### Quality Commands
| Command | Purpose | Best For |
|---------|---------|----------|
| **improve** | Code enhancement | Performance optimization, refactoring |
| **cleanup** | Technical debt | Dead code removal, organization |
| **test** | Quality assurance | Test automation, coverage analysis |
| **document** | Documentation | API docs, user guides |

### Project Management
| Command | Purpose | Best For |
|---------|---------|----------|
| **estimate** | Project estimation | Timeline planning, resource allocation |
| **task** | Task management | Complex workflows, task tracking |
| **spawn** | Meta-orchestration | Large-scale projects, parallel execution |

### Utility Commands
| Command | Purpose | Best For |
|---------|---------|----------|
| **git** | Version control | Commit management, branch strategies |
| **index** | Command discovery | Exploring capabilities, finding commands |

### Session Commands  
| Command | Purpose | Best For |
|---------|---------|----------|
| **load** | Context loading | Session initialization, project onboarding |
| **save** | Session persistence | Checkpointing, context preservation |
| **reflect** | Task validation | Progress assessment, completion validation |
| **select-tool** | Tool optimization | Performance optimization, tool selection |

---

## Command Index

**機能別:**
- **計画**: brainstorm, design, workflow, estimate
- **開発**: implement, build, git
- **分析**: analyze, troubleshoot, explain  
- **品質**: improve, cleanup, test, document
- **管理**: task, spawn, load, save, reflect
- **ユーティリティ**: index, select-tool

**複雑さ別:**
- **初級**: brainstorm, implement, analyze, test
- **中級**: workflow, design, improve, document  
- **上級**: spawn, task, select-tool, reflect

## Troubleshooting

**コマンドの問題:**
- **コマンドが見つからない**: インストールを確認: `python3 -m SuperClaude --version`
- **応答なし**: Claude Codeセッションを再起動
- **処理の遅延**: MCPサーバーなしでテストするには `--no-mcp` を使用

**クイックフィックス:**
- セッションをリセット: `/sc:load` で再初期化
- ステータス確認: `SuperClaude install --list-components`
- ヘルプを取得: [トラブルシューティングガイド](../Reference/troubleshooting.md)

## Next Steps

- [フラグガイド](flags.md) - コマンドの動作を制御
- [エージェントガイド](agents.md) - 専門家の活性化
- [例のクックブック](../Reference/examples-cookbook.md) - 実際の使用パターン
