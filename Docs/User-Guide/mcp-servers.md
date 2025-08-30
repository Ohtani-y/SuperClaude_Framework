# SuperClaude MCPサーバーガイド 🔌

## 概要

MCP（Model Context Protocol）サーバーは、専門ツールを通じてClaude Codeの機能を拡張します。SuperClaudeは6つのMCPサーバーを統合し、タスクに基づいて適切なサーバーを活性化するための指示をClaudeに提供します。

### 🔍 現実確認
- **MCPサーバーとは**: 追加ツールを提供する外部Node.jsプロセス
- **MCPサーバーではないもの**: 組み込みSuperClaude機能
- **活性化の仕組み**: Claudeがコンテキストに基づいて適切なサーバーを使用する指示を読み取り
- **提供するもの**: Claude Codeのネイティブ機能を拡張する実際のツール

**コアサーバー:**
- **context7**: 公式ライブラリドキュメントとパターン
- **sequential-thinking**: マルチステップ推論と分析  
- **magic**: モダンUIコンポーネント生成
- **playwright**: ブラウザ自動化とE2Eテスト
- **morphllm-fast-apply**: パターンベースコード変換
- **serena**: セマンティックコード理解とプロジェクトメモリ

## クイックスタート

**セットアップ確認**: MCPサーバーは自動的に活性化されます。インストールとトラブルシューティングについては、[インストールガイド](../Getting-Started/installation.md)と[トラブルシューティング](../Reference/troubleshooting.md)を参照してください。

**自動活性化ロジック:**

| リクエスト内容 | 活性化サーバー |
|-----------------|------------------|
| ライブラリインポート、API名 | **context7** |
| `--think`、デバッグ | **sequential-thinking** |  
| `component`、`UI`、フロントエンド | **magic** |
| `test`、`e2e`、`browser` | **playwright** |
| マルチファイル編集、リファクタリング | **morphllm-fast-apply** |
| 大規模プロジェクト、セッション | **serena** |

## サーバー詳細

### context7 📚
**目的**: 公式ライブラリドキュメントアクセス
**トリガー**: インポート文、フレームワークキーワード、ドキュメント要求
**要件**: Node.js 16+、APIキー不要

```bash
# Automatic activation
/sc:implement "React authentication system"
# → Provides official React patterns

# Manual activation  
/sc:analyze auth-system/ --c7
```

### sequential-thinking 🧠
**目的**: 構造化マルチステップ推論と体系的分析
**トリガー**: 複雑デバッグ、`--think`フラグ、アーキテクチャ分析
**要件**: Node.js 16+、APIキー不要

```bash
# Automatic activation
/sc:troubleshoot "API performance issues"
# → Enables systematic root cause analysis

# Manual activation
/sc:analyze --think-hard architecture/
```

### magic ✨
**Purpose**: Modern UI component generation from 21st.dev patterns
**Triggers**: UI requests, `/ui` commands, component development
**Requirements**: Node.js 16+, TWENTYFIRST_API_KEY ()

```bash
# Automatic activation
/sc:implement "responsive dashboard component"
# → Generates accessible UI with modern patterns

# API key setup
export TWENTYFIRST_API_KEY="your_key_here"
```

### playwright 🎭
**Purpose**: Real browser automation and E2E testing
**Triggers**: Browser testing, E2E scenarios, visual validation
**Requirements**: Node.js 16+, no API key

```bash
# Automatic activation
/sc:test --type e2e "user login flow"
# → Enables browser automation testing

# Manual activation
/sc:validate "accessibility compliance" --play
```

### morphllm-fast-apply 🔄
**Purpose**: Efficient pattern-based code transformations
**Triggers**: Multi-file edits, refactoring, framework migrations
**Requirements**: Node.js 16+, MORPH_API_KEY

```bash
# Automatic activation
/sc:improve legacy-codebase/ --focus maintainability
# → Applies consistent patterns across files

# API key setup
export MORPH_API_KEY="your_key_here"
```

### serena 🧭
**Purpose**: Semantic code understanding with project memory
**Triggers**: Symbol operations, large codebases, session management
**Requirements**: Python 3.9+, uv package manager, no API key

```bash
# Automatic activation  
/sc:load existing-project/
# → Builds project understanding and memory

# Manual activation
/sc:refactor "extract UserService" --serena
```

## Configuration

**MCP Configuration File (`~/.claude.json`):**
```json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp@latest"]
    },
    "sequential-thinking": {
      "command": "npx", 
      "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"]
    },
    "magic": {
      "command": "npx",
      "args": ["@21st-dev/magic"],
      "env": {"TWENTYFIRST_API_KEY": "${TWENTYFIRST_API_KEY}"}
    },
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp@latest"]
    },
    "morphllm-fast-apply": {
      "command": "npx",
      "args": ["@morph-llm/morph-fast-apply"],
      "env": {"MORPH_API_KEY": "${MORPH_API_KEY}"}
    },
    "serena": {
      "command": "uv",
      "args": ["run", "serena", "start-mcp-server", "--context", "ide-assistant"],
      "cwd": "$HOME/.claude/serena"
    }
  }
}
```

## Usage Patterns

**Server Control:**
```bash
# Enable specific servers
/sc:analyze codebase/ --c7 --seq

# Disable all MCP servers
/sc:implement "simple function" --no-mcp

# Enable all servers
/sc:design "complex architecture" --all-mcp
```

**Multi-Server Coordination:**
```bash
# Full-stack development
/sc:implement "e-commerce checkout"
# → Sequential: workflow analysis
# → Context7: payment patterns  
# → Magic: UI components
# → Serena: code organization
# → Playwright: E2E testing
```

## Troubleshooting

**Common Issues:**
- **No servers connected**: Check Node.js: `node --version` (need v16+)
- **Context7 fails**: Clear cache: `npm cache clean --force`
- **Magic/Morphllm errors**: Expected without API keys (paid services)
- **Server timeouts**: Restart Claude Code session

**Quick Fixes:**
```bash
# Reset connections
# Restart Claude Code session

# Check dependencies  
node --version  # Should show v16+

# Test without MCP
/sc:command --no-mcp

# Check configuration
ls ~/.claude.json
```

**API Key Configuration:**
```bash
# For Magic server (required for UI generation)
export TWENTYFIRST_API_KEY="your_key_here"

# For Morphllm server (required for bulk transformations)
export MORPH_API_KEY="your_key_here"

# Add to shell profile for persistence
echo 'export TWENTYFIRST_API_KEY="your_key"' >> ~/.bashrc
echo 'export MORPH_API_KEY="your_key"' >> ~/.bashrc
```

**Environment Variable Usage:**
- ✅ `TWENTYFIRST_API_KEY` - Required for Magic MCP server functionality
- ✅ `MORPH_API_KEY` - Required for Morphllm MCP server functionality  
- ❌ Other env vars in docs - Examples only, not used by framework
- 📝 Both are paid service API keys, framework works without them

## サーバーの組み合わせ

**APIキーなし(無料)**:
- context7 + sequential-thinking + playwright + serena

**APIキー1個**:
- プロフェッショナルUI開発のためにmagicを追加

**APIキー2個**:
- 大規模リファクタリングのためにmorphllm-fast-applyを追加

**一般的なワークフロー:**
- **学習**: context7 + sequential-thinking
- **Web開発**: magic + context7 + playwright  
- **エンタープライズリファクタリング**: serena + morphllm + sequential-thinking
- **複雑な分析**: sequential-thinking + context7 + serena

## 統合

**SuperClaudeコマンドとの連携:**
- 分析コマンドは自動的にSequential + Serenaを使用
- 実装コマンドはMagic + Context7を使用
- テストコマンドはPlaywright + Sequentialを使用

**行動モードとの連携:**
- ブレインストーミングモード: 発見のためのSequential
- タスク管理: 永続化のためのSerena
- オーケストレーションモード: 最適なサーバー選択

**パフォーマンス制御:**
- システム負荷に基づく自動リソース管理
- 同時実行制御: `--concurrency N` (1-15)
- 制約下での優先度ベースサーバー選択

## 関連リソース

**必須文書:**
- [コマンドガイド](commands.md) - MCPサーバーを活性化するコマンド
- [クイックスタートガイド](../Getting-Started/quick-start.md) - MCPセットアップガイド

**上級使用法:**
- [行動モード](modes.md) - モード-MCP連携
- [エージェントガイド](agents.md) - エージェント-MCP統合
- [セッション管理](session-management.md) - Serenaワークフロー

**技術リファレンス:**
- [例のクックブック](../Reference/examples-cookbook.md) - MCPワークフローパターン
- [技術アーキテクチャ](../Developer-Guide/technical-architecture.md) - 統合の詳細
