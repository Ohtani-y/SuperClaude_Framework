# SuperClaude フラグガイド 🏁

**ほとんどのフラグは自動的に活性化されます** - Claude Codeは動作指示を読み取り、リクエスト内のキーワードとパターンに基づいて適切なコンテキストを有効にします。

## 必須自動活性化フラグ（使用例の90%）

### コア分析フラグ
| フラグ | 活性化タイミング | 機能 |
|------|---------------|--------------|
| `--think` | 5+ files OR complex analysis | Standard structured analysis (~4K tokens) |
| `--think-hard` | Architectural analysis, system dependencies | Deep analysis (~10K tokens) with enhanced tools |
| `--ultrathink` | Critical system redesign, legacy modernization | Maximum depth analysis (~32K tokens) with all tools |

### MCPサーバーフラグ
| フラグ | サーバー | 目的 | 自動トリガー |
|------|---------|---------|---------------|
| `--c7` / `--context7` | Context7 | 公式ドキュメント、フレームワークパターン | ライブラリのインポート、フレームワークに関する質問 |
| `--seq` / `--sequential` | Sequential | 多段階推論、デバッグ | 複雑なデバッグ、システム設計 |
| `--magic` | Magic | UIコンポーネント生成 | `/ui`コマンド、フロントエンドキーワード |
| `--play` / `--playwright` | Playwright | ブラウザテスト、E2E検証 | テストリクエスト、視覚的検証 |
| `--morph` / `--morphllm` | Morphllm | 一括変換、パターン編集 | 一括操作、スタイル適用 |
| `--serena` | Serena | プロジェクトメモリ、シンボル操作 | シンボル操作、大規模コードベース |

### 行動モードフラグ
| フラグ | 活性化タイミング | 機能 |
|------|---------------|--------------|
| `--brainstorm` | 曖昧なリクエスト、探索キーワード | 協力的な発見のマインドセット |
| `--introspect` | 自己分析、エラー回復 | 透明性を持って推論プロセスを公開 |
| `--task-manage` | 3ステップ超、複雑なスコープ | 委任によるオーケストレーション |
| `--orchestrate` | マルチツール操作、パフォーマンス要求 | ツール選択と並列実行の最適化 |
| `--token-efficient` / `--uc` | コンテキスト75%超、効率要求 | シンボル強化通信、30-50%削減 |

### 実行制御フラグ
| フラグ | 活性化タイミング | 機能 |
|------|---------------|--------------|
| `--loop` | "improve", "polish", "refine" キーワード | 反復改善サイクル |
| `--safe-mode` | 本番環境、リソース使用率85%超 | 最大限の検証、保守的実行 |
| `--validate` | リスク0.7超、本番環境 | 実行前リスク評価 |
| `--delegate` | ディレクトリ7個超 または ファイル50個超 | サブエージェント並列処理 |

## Command-Specific Flags

### 分析コマンドフラグ (`/sc:analyze`)
| フラグ | 目的 | 値 |
|------|---------|--------|
| `--focus` | 特定ドメインをターゲット | `security`, `performance`, `quality`, `architecture` |
| `--depth` | 分析の徹底度 | `quick`, `deep` |
| `--format` | 出力形式 | `text`, `json`, `report` |

### ビルドコマンドフラグ (`/sc:build`)
| フラグ | 目的 | 値 |
|------|---------|--------|
| `--type` | ビルド設定 | `dev`, `prod`, `test` |
| `--clean` | ビルド前のクリーン | ブール値 |
| `--optimize` | 最適化を有効化 | ブール値 |
| `--verbose` | 詳細出力 | ブール値 |

### 設計コマンドフラグ (`/sc:design`)
| フラグ | 目的 | 値 |
|------|---------|--------|
| `--type` | 設計対象 | `architecture`, `api`, `component`, `database` |
| `--format` | 出力形式 | `diagram`, `spec`, `code` |

### 説明コマンドフラグ (`/sc:explain`)
| フラグ | 目的 | 値 |
|------|---------|--------|
| `--level` | 複雑さレベル | `basic`, `intermediate`, `advanced` |
| `--format` | 説明スタイル | `text`, `examples`, `interactive` |
| `--context` | ドメインコンテキスト | 任意のドメイン (例: `react`, `security`) |

### 改善コマンドフラグ (`/sc:improve`)
| フラグ | 目的 | 値 |
|------|---------|--------|
| `--type` | 改善の焦点 | `quality`, `performance`, `maintainability`, `style`, `security` |
| `--safe` | 保守的なアプローチ | ブール値 |
| `--interactive` | ユーザーガイダンス | ブール値 |
| `--preview` | 実行せずに表示 | ブール値 |

### Task Command Flags (`/sc:task`)
| Flag | Purpose | Values |
|------|---------|--------|
| `--strategy` | Task approach | `systematic`, `agile`, `enterprise` |
| `--parallel` | Parallel execution | Boolean |
| `--delegate` | Sub-agent coordination | Boolean |

### Workflow Command Flags (`/sc:workflow`)
| Flag | Purpose | Values |
|------|---------|--------|
| `--strategy` | Workflow approach | `systematic`, `agile`, `enterprise` |
| `--depth` | Analysis depth | `shallow`, `normal`, `deep` |
| `--parallel` | Parallel coordination | Boolean |

### Troubleshoot Command Flags (`/sc:troubleshoot`)
| Flag | Purpose | Values |
|------|---------|--------|
| `--type` | Issue category | `bug`, `build`, `performance`, `deployment` |
| `--trace` | Include trace analysis | Boolean |
| `--fix` | Apply fixes | Boolean |

### Cleanup Command Flags (`/sc:cleanup`)
| Flag | Purpose | Values |
|------|---------|--------|
| `--type` | Cleanup target | `code`, `imports`, `files`, `all` |
| `--safe` / `--aggressive` | Cleanup intensity | Boolean |
| `--interactive` | User guidance | Boolean |
| `--preview` | Show without executing | Boolean |

### Estimate Command Flags (`/sc:estimate`)
| Flag | Purpose | Values |
|------|---------|--------|
| `--type` | Estimate focus | `time`, `effort`, `complexity` |
| `--unit` | Time unit | `hours`, `days`, `weeks` |
| `--breakdown` | Detailed breakdown | Boolean |

### Index Command Flags (`/sc:index`)
| Flag | Purpose | Values |
|------|---------|--------|
| `--type` | Index target | `docs`, `api`, `structure`, `readme` |
| `--format` | Output format | `md`, `json`, `yaml` |

### Reflect Command Flags (`/sc:reflect`)
| Flag | Purpose | Values |
|------|---------|--------|
| `--type` | Reflection scope | `task`, `session`, `completion` |
| `--analyze` | Include analysis | Boolean |
| `--validate` | Validate completeness | Boolean |

### Spawn Command Flags (`/sc:spawn`)
| Flag | Purpose | Values |
|------|---------|--------|
| `--strategy` | Coordination approach | `sequential`, `parallel`, `adaptive` |
| `--depth` | Analysis depth | `normal`, `deep` |

### Git Command Flags (`/sc:git`)
| Flag | Purpose | Values |
|------|---------|--------|
| `--smart-commit` | Generate commit message | Boolean |
| `--interactive` | Guided operations | Boolean |

### Select-Tool Command Flags (`/sc:select-tool`)
| Flag | Purpose | Values |
|------|---------|--------|
| `--analyze` | Tool analysis | Boolean |
| `--explain` | Explain selection | Boolean |

### Test Command Flags (`/sc:test`)
| Flag | Purpose | Values |
|------|---------|--------|
| `--coverage` | Include coverage | Boolean |
| `--type` | Test type | `unit`, `integration`, `e2e` |
| `--watch` | Watch mode | Boolean |

## Advanced Control Flags

### Scope and Focus
| Flag | Purpose | Values |
|------|---------|--------|
| `--scope` | Analysis boundary | `file`, `module`, `project`, `system` |
| `--focus` | Domain targeting | `performance`, `security`, `quality`, `architecture`, `accessibility`, `testing` |

### Execution Control
| Flag | Purpose | Values |
|------|---------|--------|
| `--concurrency [n]` | Control parallel ops | 1-15 |
| `--iterations [n]` | Improvement cycles | 1-10 |
| `--all-mcp` | Enable all MCP servers | Boolean |
| `--no-mcp` | Native tools only | Boolean |

### System Flags (SuperClaude Installation)
| Flag | Purpose | Values |
|------|---------|--------|
| `--verbose` / `-v` | Verbose logging | Boolean |
| `--quiet` / `-q` | Suppress output | Boolean |
| `--dry-run` | Simulate operation | Boolean |
| `--force` | Skip checks | Boolean |
| `--yes` / `-y` | Auto-confirm | Boolean |
| `--install-dir` | Target directory | Path |
| `--legacy` | Use legacy script | Boolean |
| `--version` | Show version | Boolean |
| `--help` | Show help | Boolean |

## Common Usage Patterns

### フロントエンド開発
```bash
/sc:implement "レスポンシブダッシュボード" --magic --c7
/sc:design コンポーネントライブラリ --type component --format code
/sc:test ui-components/ --magic --play
/sc:improve legacy-ui/ --magic --morph --validate
```

### バックエンド開発
```bash
/sc:analyze api/ --focus performance --seq --think
/sc:design 決済API --type api --format spec
/sc:troubleshoot "APIタイムアウト" --type performance --trace
/sc:improve 認証サービス --type security --validate
```

### 大規模プロジェクト
```bash
/sc:analyze . --ultrathink --all-mcp --safe-mode
/sc:workflow エンタープライズシステム --strategy enterprise --depth deep
/sc:cleanup . --type all --safe --interactive
/sc:estimate "マイクロサービスに移行" --type complexity --breakdown
```

### 品質とメンテナンス
```bash
/sc:improve src/ --type quality --safe --interactive
/sc:cleanup インポート --type imports --preview
/sc:reflect --type completion --validate
/sc:git commit --smart-commit
```

## Flag Interactions

### 互換性のある組み合わせ
- `--think` + `--c7`: ドキュメント付き分析
- `--magic` + `--play`: テスト付きUI生成
- `--serena` + `--morph`: 変換付きプロジェクトメモリ
- `--safe-mode` + `--validate`: 最大限の安全性
- `--loop` + `--validate`: 検証付き反復改善

### 競合するフラグ
- `--all-mcp` vs 個別MCPフラグ (どちらか一方を使用)
- `--no-mcp` vs 任意のMCPフラグ (--no-mcpが勝つ)
- `--safe` vs `--aggressive` (クリーンアップの強度)
- `--quiet` vs `--verbose` (出力レベル)

### 自動有効化関係
- `--safe-mode` が `--uc` と `--validate` を自動有効化
- `--ultrathink` がすべてのMCPサーバーを自動有効化
- `--think-hard` が `--seq` + `--c7` を自動有効化
- `--magic` がUI特化エージェントをトリガー

## Troubleshooting Flags

### 一般的な問題
- **ツールが多すぎる**: ネイティブツールのみでテストするには `--no-mcp` を使用
- **操作が遅すぎる**: 出力を圧縮するには `--uc` を追加
- **検証がブロックしている**: 開発時は `--safe-mode` の代わりに `--validate` を使用
- **コンテキスト圧迫**: 使用率75%超で `--token-efficient` が自動活性化

### デバッグフラグ
```bash
/sc:analyze . --verbose                      # 決定ロジックとフラグ活性化を表示
/sc:select-tool "操作" --explain        # ツール選択プロセスを説明
/sc:reflect --type session --analyze         # 現在のセッションの決定をレビュー
```

### クイックフィックス
```bash
/sc:analyze . --help                         # コマンドで利用可能なフラグを表示
/sc:analyze . --no-mcp                       # ネイティブ実行のみ
/sc:cleanup . --preview                      # クリーンアップされる内容を表示
```

## Flag Priority Rules

1. **安全第一**: `--safe-mode` > `--validate` > 最適化フラグ
2. **明示的オーバーライド**: ユーザーフラグ > 自動検出
3. **深度階層**: `--ultrathink` > `--think-hard` > `--think`  
4. **MCP制御**: `--no-mcp` がすべての個別MCPフラグをオーバーライド
5. **スコープ優先度**: system > project > module > file

## Related Resources
- [コマンドガイド](commands.md) - これらのフラグを使用するコマンド
- [MCPサーバーガイド](mcp-servers.md) - MCPフラグ活性化の理解
- [セッション管理](session-management.md) - 永続セッションでのフラグ使用
