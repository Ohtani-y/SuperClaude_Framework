# セッション管理ガイド

SuperClaudeはSerena MCPサーバーを通じて永続的なセッション管理を提供し、Claude Codeの会話間での真のコンテキスト保持と長期プロジェクト継続性を実現します。

## 永続メモリ付きコアセッションコマンド

### `/sc:load` - 永続メモリ付きコンテキスト読み込み
**目的**: 以前のセッションからのプロジェクトコンテキストと永続メモリでセッションを初期化  
**MCP統合**: Serena MCPをトリガーして保存されたプロジェクトメモリを読み取り  
**構文**: `/sc:load [project_path]`

**実行内容**:
- Serena MCPが以前のセッションからの永続メモリファイルを読み取り
- 保存されたメモリからプロジェクトコンテキストを復元
- 以前の決定、パターン、進捗が読み込まれる
- 履歴コンテキストでセッション状態を初期化

**使用例**:
```bash
# 永続メモリから既存プロジェクトコンテキストを読み込み
/sc:load src/

# 完全な履歴で特定のプロジェクト作業を再開
/sc:load "認証システム"

# コードベース分析と以前の洞察で初期化
/sc:load . --analyze
```

### `/sc:save` - メモリへのセッション永続化
**目的**: 現在のセッション状態と決定を永続メモリに保存  
**MCP統合**: Serena MCPをトリガーしてメモリファイルを書き込み  
**構文**: `/sc:save "session_description"`

**実行内容**:
- 現在のコンテキストと決定がSerenaメモリに書き込まれる
- プロジェクト状態と進捗が会話間で永続化される
- 重要な洞察とパターンが将来のセッション用に保存される
- 取得用のタイムスタンプ付きセッション要約が作成される

**使用例**:
```bash
# 将来の参照のために完成した機能作業を保存
/sc:save "JWTでユーザー認証を実装"

# 複雑な作業中のチェックポイント
/sc:save "API設計フェーズ完了、実装準備完了"

# アーキテクチャの決定を永続的に保存
/sc:save "マイクロサービスアーキテクチャ決定、サービス境界定義"
```

### `/sc:reflect` - メモリコンテキスト付き進捗評価
**目的**: 保存されたメモリに対する現在の進捗を分析し、セッション完全性を検証  
**MCP統合**: Serena MCPを使用して現在の状態を保存されたメモリと比較  
**構文**: `/sc:reflect [--scope project|session]`

**実行内容**:
- Serena MCPが以前のメモリと現在のコンテキストを読み取り
- 保存された目標とマイルストーンに対して進捗が評価される
- 履歴コンテキストを使用してギャップと次のステップが特定される
- プロジェクトメモリに対してセッション完全性が検証される

**使用例**:
```bash
# 保存されたマイルストーンに対してプロジェクトの進捗を評価
/sc:reflect --scope project

# 現在のセッションの完全性を検証
/sc:reflect

# メモリに基づいて次のフェーズに進む準備ができているかチェック
/sc:reflect --scope session
```

## Persistent Memory Architecture

### Serena MCPが真の永続性を実現する方法

**メモリストレージ**:
- セッションコンテキストが構造化されたメモリファイルとして保存される
- プロジェクトの決定とアーキテクチャパターンが永続的に保存される
- コード分析結果と洞察が会話間で保持される
- 進捗追跡とマイルストーンデータが長期維持される

**クロスセッション継続性**:
- 以前のセッションコンテキストが新しい会話で自動的に利用可能
- 決定と理由が会話間で保存され、アクセス可能
- 過去のパターンと解決策からの学習が維持される
- 一貫したプロジェクト理解が無期限に維持される

**メモリタイプ**:
- **プロジェクトメモリ**: 長期プロジェクトコンテキストとアーキテクチャ
- **セッションメモリ**: 特定の会話の結果と決定  
- **パターンメモリ**: 再利用可能な解決策とアーキテクチャパターン
- **進捗メモリ**: マイルストーン追跡と完成状態

## Session Lifecycle Patterns with Persistence

### New Project Initialization
```bash
# 1. 新しいプロジェクトを開始
/sc:brainstorm "Eコマースプラットフォームの要件"

# 2. 初期決定を永続メモリに保存
/sc:save "プロジェクトスコープと要件定義完了"

# 3. 実装計画を開始
/sc:workflow "ユーザー認証システム"

# 4. アーキテクチャの決定を永続的に保存
/sc:save "認証アーキテクチャ: JWT + リフレッシュトークン + レート制限"
```

### Resuming Existing Work (Cross-Conversation)
```bash
# 1. 永続メモリから以前のコンテキストを読み込み
/sc:load "Eコマースプロジェクト"

# 2. 保存された進捗に対して現在の状態を評価  
/sc:reflect --scope project  

# 3. 保存されたコンテキストを使用して次のフェーズを継続
/sc:implement "決済処理統合"

# 4. 進捗チェックポイントをメモリに保存
/sc:save "Stripe APIと決済システムを統合"
```

### Long-Term Project Management
```bash
# 永続性付き週次チェックポイントパターン
/sc:load プロジェクト名
/sc:reflect --scope project
# ... 機能作業 ...
/sc:save "第N週進捗: 機能X, Y, Z完成"

# メモリ付きフェーズ完成パターン
/sc:reflect --scope project
/sc:save "フェーズ1完了: コア認証とユーザー管理"
/sc:workflow "フェーズ2: 決済と注文処理"
```

## クロス会話継続性

### 永続性を伴う新しい会話の開始

新しいClaude Code会話を開始するとき、永続メモリシステムは以下を可能にします:

1. **自動コンテキスト復元**
   ```bash
   /sc:load プロジェクト名
   # 以前のすべてのコンテキスト、決定、進捗を自動的に復元
   ```

2. **進捗継続**
   - 以前のセッションの決定が即座に利用可能
   - アーキテクチャパターンとコードの洞察が保存される
   - プロジェクトの履歴と理由が維持される

3. **インテリジェントコンテキスト構築**
   - Serena MCPが現在の作業に基づいて関連メモリを提供
   - 過去の解決策とパターンが新しい実装に情報を提供
   - プロジェクトの進化が追跡され理解される

### メモリ最適化

**効果的なメモリ使用**:
- 説明的で検索可能なメモリ名を使用
- プロジェクトフェーズとタイムスタンプコンテキストを含める
- 特定の機能やアーキテクチャの決定を参照
- 将来の取得を直感的にする

**メモリコンテンツ戦略**:
- 単なる結果ではなく決定と理由を保存
- 検討された代替アプローチを含める
- 統合パターンと依存関係を文書化
- 将来の参照のために学習と洞察を保存

**メモリライフサイクル管理**:
- 時代遅れのメモリの定期クリーンアップ
- 関連セッションメモリの統合
- 完了したプロジェクトフェーズのアーカイブ
- 時代遅れのアーキテクチャ決定の剥摘

## 永続セッションのベストプラクティス

### セッション開始プロトコル
1. 既存プロジェクトでは必ず `/sc:load` で開始
2. `/sc:reflect` を使用してメモリから現在の状態を理解
3. 永続コンテキストと保存されたパターンに基づいて作業を計画
4. 以前の決定とアーキテクチャの選択をベースに構築

### セッション終了プロトコル
1. `/sc:reflect` を使用して保存された目標に対して完全性を評価
2. 将来のセッションのために `/sc:save` で重要な決定を保存
3. 次のステップと未解決の質問をメモリに文書化
4. シームレスな将来の継続のためにコンテキストを保存

### メモリ品質維持
- 簡単な取得のために明確で説明的なメモリ名を使用
- 決定と代替アプローチに関するコンテキストを含める
- 特定のコード位置とパターンを参照
- セッション間でメモリ構造の一貫性を維持

## Integration with Other SuperClaude Features

### MCP Server Coordination
- **Serena MCP**: Provides the persistent memory infrastructure
- **Sequential MCP**: Uses stored memories for enhanced complex analysis
- **Context7 MCP**: References stored patterns and documentation approaches
- **Morphllm MCP**: Applies stored refactoring patterns consistently

### Agent Collaboration with Memory
- Agents access persistent memories for enhanced context
- Previous specialist decisions are preserved and referenced
- Cross-session agent coordination through shared memory
- Consistent specialist recommendations based on project history

### Command Integration with Persistence
- All `/sc:` commands can reference and build on persistent context
- Previous command outputs and decisions are available across sessions
- Workflow patterns are stored and reusable
- Implementation history guides future command decisions

## Troubleshooting Persistent Sessions

### Common Issues

**Memory Not Loading**:
- Verify Serena MCP is configured and running properly
- Check memory file permissions and accessibility
- Ensure consistent project naming conventions
- Validate memory file integrity and format

**Context Loss Between Sessions**:  
- Always use `/sc:save` before ending sessions
- Use descriptive memory names for easy retrieval
- Regular `/sc:reflect` to validate memory completeness
- Backup important memory files periodically

**Memory Conflicts**:
- Use timestamped memory names for version control
- Regular cleanup of obsolete memories
- Clear separation between project and session memories
- Consistent memory naming conventions across sessions

### Quick Fixes

**Reset Session State**:
```bash
/sc:load --fresh  # Start without previous context
/sc:reflect       # Assess current state
```

**Memory Cleanup**:
```bash
/sc:reflect --cleanup  # Remove obsolete memories
/sc:save --consolidate # Merge related memories
```

**Context Recovery**:
```bash
/sc:load --recent     # Load most recent memories
/sc:reflect --repair  # Identify and fix context gaps
```

## Advanced Persistent Session Patterns

### Multi-Phase Projects
- Use phase-specific memory naming for organization
- Maintain architectural decision continuity across phases
- Cross-phase dependency tracking through persistent memory
- Progressive complexity management with historical context

### Team Collaboration
- Shared memory conventions and naming standards
- Decision rationale preservation for team context
- Integration pattern documentation accessible to all team members
- Consistent code style and architecture enforcement through memory

### Long-Term Maintenance
- Memory archiving strategies for completed projects
- Pattern library development through accumulated memories
- Reusable solution documentation built over time
- Knowledge base building through persistent memory accumulation

## Key Benefits of Persistent Session Management

### Project Continuity
- Seamless work continuation across multiple conversations
- No context loss between Claude Code sessions
- Preserved architectural decisions and technical rationale
- Long-term project evolution tracking

### Enhanced Productivity
- Reduced need to re-explain project context
- Faster startup time for continued work
- Building on previous insights and patterns
- Cumulative project knowledge growth

### Quality Consistency
- Consistent architectural patterns across sessions
- Preserved code quality decisions and standards
- Reusable solutions and best practices
- Maintained technical debt awareness

---

**Key Takeaway**: Session management through Serena MCP transforms SuperClaude from single-conversation assistance to persistent project partnership, maintaining context, decisions, and learning across all development phases and Claude Code conversations.
