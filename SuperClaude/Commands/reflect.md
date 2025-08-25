---
name: reflect
description: "Serena MCP分析機能を使用したタスクリフレクションと検証"
category: special
complexity: standard
mcp-servers: [serena]
personas: []
---

# /sc:reflect - タスクリフレクションと検証

## トリガー
- 検証と品質評価が必要なタスク完了
- セッション進捗分析と達成した作業のリフレクション
- プロジェクト改善のためのセッション間学習と洞察キャプチャ
- 包括的なタスク遵守検証が必要な品質ゲート

## 使用法
```
/sc:reflect [--type task|session|completion] [--analyze] [--validate]
```

## 動作フロー
1. **分析**: Serenaリフレクションツールを使用して現在のタスク状態とセッション進捗を調査
2. **検証**: タスク遵守、完了品質、要件充足を評価
3. **リフレクション**: 収集された情報とセッション洞察の深い分析を適用
4. **文書化**: セッションメタデータを更新し、学習洞察をキャプチャ
5. **最適化**: プロセス改善と品質向上のための推奨事項を提供

主要動作:
- 包括的リフレクション分析とタスク検証のためのSerena MCP統合
- TodoWriteパターンと高度なSerena分析機能間のブリッジ
- セッション間永続化と学習キャプチャによるセッションライフサイクル統合
- 200ms未満のコアリフレクションと検証によるパフォーマンス重視操作
## MCP Integration
- **Serena MCP**: Mandatory integration for reflection analysis, task validation, and session metadata
- **Reflection Tools**: think_about_task_adherence, think_about_collected_information, think_about_whether_you_are_done
- **Memory Operations**: Cross-session persistence with read_memory, write_memory, list_memories
- **Performance Critical**: <200ms for core reflection operations, <1s for checkpoint creation

## Tool Coordination
- **TodoRead/TodoWrite**: Bridge between traditional task management and advanced reflection analysis
- **think_about_task_adherence**: Validates current approach against project goals and session objectives
- **think_about_collected_information**: Analyzes session work and information gathering completeness
- **think_about_whether_you_are_done**: Evaluates task completion criteria and remaining work identification
- **Memory Tools**: Session metadata updates and cross-session learning capture

## Key Patterns
- **Task Validation**: Current approach → goal alignment → deviation identification → course correction
- **Session Analysis**: Information gathering → completeness assessment → quality evaluation → insight capture
- **Completion Assessment**: Progress evaluation → completion criteria → remaining work → decision validation
- **Cross-Session Learning**: Reflection insights → memory persistence → enhanced project understanding

## Examples

### Task Adherence Reflection
```
/sc:reflect --type task --analyze
# Validates current approach against project goals
# Identifies deviations and provides course correction recommendations
```

### Session Progress Analysis
```
/sc:reflect --type session --validate
# Comprehensive analysis of session work and information gathering
# Quality assessment and gap identification for project improvement
```

### Completion Validation
```
/sc:reflect --type completion
# Evaluates task completion criteria against actual progress
# Determines readiness for task completion and identifies remaining blockers
```

## Boundaries

**Will:**
- Perform comprehensive task reflection and validation using Serena MCP analysis tools
- Bridge TodoWrite patterns with advanced reflection capabilities for enhanced task management
- Provide cross-session learning capture and session lifecycle integration

**Will Not:**
- Operate without proper Serena MCP integration and reflection tool access
- Override task completion decisions without proper adherence and quality validation
- Bypass session integrity checks and cross-session persistence requirements

