# SuperClaude `/sc`コマンド セットアップガイド

## 問題の概要
Claude Code内で`/sc`コマンドが使用できない問題の解決方法

## セットアップ手順

### 1. SuperClaude Pythonパッケージのインストール
```bash
# pip経由でインストール（既に完了済み）
pip install superclaude
```

### 2. SuperClaudeフレームワークのインストール
```bash
# 対話的インストーラーの実行
superclaude install

# 選択オプション：
# Stage 1: MCP Server Selection → 7 (Skip)
# Stage 2: Framework Components → 1,2,3,4 (core, modes, commands, agents)
# 既存インストールの更新確認 → y
# インストール実行確認 → y
```

### 3. インストール内容の確認

#### インストールされたコンポーネント
- **Core Framework** (`~/.claude/`)
  - FLAGS.md - 動作フラグ定義
  - PRINCIPLES.md - 原則定義
  - RULES.md - ルール定義

- **Behavioral Modes** (`~/.claude/`)
  - MODE_Brainstorming.md
  - MODE_Introspection.md
  - MODE_Orchestration.md
  - MODE_Task_Management.md
  - MODE_Token_Efficiency.md

- **Commands** (`~/.claude/commands/sc/`)
  - 21個のコマンド定義ファイル
  - analyze, build, test, document など

- **Agents** (`~/.claude/agents/`)
  - 14個の特殊エージェント定義

### 4. CLAUDE.mdファイルの生成
SuperClaudeインストーラーが自動的に`~/.claude/CLAUDE.md`を生成し、以下の内容を含む：
```markdown
# SuperClaude Entry Point

# Core Framework
@FLAGS.md
@PRINCIPLES.md
@RULES.md

# Behavioral Modes
@MODE_Brainstorming.md
@MODE_Introspection.md
@MODE_Orchestration.md
@MODE_Task_Management.md
@MODE_Token_Efficiency.md
```

## 重要な注意事項

### `/sc`コマンドの使用方法
1. **Claude Code内でのみ使用可能** - 通常のターミナルでは動作しない
2. **再起動が必要** - インストール後、Claude Codeの再起動が必要
3. **直接入力** - Bashツールを使わず、Claude Codeのチャット内で直接`/sc`と入力

### トラブルシューティング

#### npm installのハング問題
```bash
# 問題: npm install github:... がハングする
# 解決策: リポジトリを直接クローンしてローカルインストール
git clone https://github.com/Ohtani-y/SuperClaude_Framework.git temp_repo
npm install ./temp_repo
rm -rf temp_repo
```

#### npmキャッシュの問題
```bash
# git-cloneの一時ファイルがロックされている場合
rm -rf "C:\Users\Ohtani\AppData\Local\npm-cache\_cacache\tmp\git-clone*"
```

## 最終確認手順

### 1. インストール状態の確認
```bash
# SuperClaudeバージョン確認
superclaude --version  # 出力: SuperClaude 4.0.8

# Pythonパッケージの確認
pip show superclaude

# CLAUDE.mdファイルの確認
cat ~/.claude/CLAUDE.md

# コマンドファイルの確認
ls ~/.claude/commands/sc/
```

### 2. Claude Codeの再起動
1. Claude Codeセッションを終了
2. 新しいセッションを開始
3. `/sc`コマンドを直接入力してテスト

## 期待される結果
再起動後、Claude Code内で`/sc`と入力すると、利用可能なSuperClaudeコマンドのリストが表示される。

## 追加オプション

### MCP Serverの追加（オプション）
後からMCP Serverを追加する場合：
```bash
superclaude install
# Stage 1で必要なサーバーを選択
# API keyが必要なサーバー（magic, morphllm）は設定が必要
```

### アンインストール
```bash
superclaude uninstall
```

### バックアップとリストア
```bash
# バックアップ作成
superclaude backup create

# リストア
superclaude backup restore
```