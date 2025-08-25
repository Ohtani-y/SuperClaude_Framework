---
name: spawn
description: "インテリジェントな分解と委任によるメタシステムタスクオーケストレーション"
category: special
complexity: high
mcp-servers: []
personas: []
---

# /sc:spawn - メタシステムタスクオーケストレーション

## トリガー
- インテリジェントなタスク分解が必要な複雑なマルチドメイン操作
- 複数の技術分野にまたがる大規模システム操作
- 並列調整と依存関係管理が必要な操作
- 標準コマンド機能を超えたメタレベルオーケストレーション

## 使用法
```
/sc:spawn [複雑なタスク] [--strategy sequential|parallel|adaptive] [--depth normal|deep]
```

## 動作フロー
1. **分析**: 複雑な操作要件を解析し、ドメイン間のスコープを評価
2. **分解**: 操作を調整されたサブタスク階層に分解
3. **オーケストレート**: 最適な調整戦略（並列/順次）を使用してタスクを実行
4. **監視**: 依存関係管理でタスク階層全体の進捗を追跡
5. **統合**: 結果を集約し、包括的なオーケストレーション要約を提供

主要動作:
- Epic → Story → Task → Subtaskの分解によるメタシステムタスク分解
- 操作特性に基づくインテリジェントな調整戦略選択
- 並列および順次実行パターンによるクロスドメイン操作管理
- タスク階層全体での高度な依存関係分析とリソース最適化
## MCP統合
- **ネイティブオーケストレーション**: メタシステムコマンドはMCP依存関係なしでネイティブ調整を使用
- **段階的統合**: 段階的強化のための体系的実行との調整
- **フレームワーク統合**: SuperClaudeオーケストレーション層との高度な統合

## ツール調整
- **TodoWrite**: Epic → Story → Taskレベルでの階層的タスク分解と進捗追跡
- **Read/Grep/Glob**: 複雑な操作のためのシステム分析と依存関係マッピング
- **Edit/MultiEdit/Write**: 並列および順次実行による調整されたファイル操作
- **Bash**: インテリジェントなリソース管理によるシステムレベル操作調整

## 主要パターン
- **階層分解**: Epicレベル操作 → Story調整 → Task実行 → Subtask粒度
- **戦略選択**: 順次（依存関係順） → 並列（独立） → 適応（動的）
- **メタシステム調整**: クロスドメイン操作 → リソース最適化 → 結果統合
- **段階的強化**: 体系的実行 → 品質ゲート → 包括的検証

## Examples

### Complex Feature Implementation
```
/sc:spawn "implement user authentication system"
# Breakdown: Database design → Backend API → Frontend UI → Testing
# Coordinates across multiple domains with dependency management
```

### Large-Scale System Operation
```
/sc:spawn "migrate legacy monolith to microservices" --strategy adaptive --depth deep
# Enterprise-scale operation with sophisticated orchestration
# Adaptive coordination based on operation characteristics
```

### Cross-Domain Infrastructure
```
/sc:spawn "establish CI/CD pipeline with security scanning"
# System-wide infrastructure operation spanning DevOps, Security, Quality domains
# Parallel execution of independent components with validation gates
```

## Boundaries

**Will:**
- Decompose complex multi-domain operations into coordinated task hierarchies
- Provide intelligent orchestration with parallel and sequential coordination strategies
- Execute meta-system operations beyond standard command capabilities

**Will Not:**
- Replace domain-specific commands for simple operations
- Override user coordination preferences or execution strategies
- Execute operations without proper dependency analysis and validation
