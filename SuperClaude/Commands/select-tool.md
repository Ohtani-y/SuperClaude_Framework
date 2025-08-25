---
name: select-tool
description: "複雑性スコアリングと操作分析に基づくインテリジェントMCPツール選択"
category: special
complexity: high
mcp-servers: [serena, morphllm]
personas: []
---

# /sc:select-tool - インテリジェントMCPツール選択

## トリガー
- SerenaとMorphllm間の最適なMCPツール選択が必要な操作
- 複雑性分析と機能マッチングが必要なメタシステム決定
- パフォーマンス対精度のトレードオフが必要なツールルーティング決定
- インテリジェントツール機能評価の恩恵を受ける操作

## 使用法
```
/sc:select-tool [操作] [--analyze] [--explain]
```

## 動作フロー
1. **解析**: 操作タイプ、スコープ、ファイル数、複雑性指標を分析
2. **スコア**: 様々な操作要因にわたって多次元複雑性スコアリングを適用
3. **マッチング**: SerenaとMorphllm機能に対する操作要件を比較
4. **選択**: スコアリングマトリックスとパフォーマンス要件に基づいて最適ツールを選択
5. **検証**: 選択精度を確認し、信頼度メトリクスを提供

主要動作:
- ファイル数、操作タイプ、言語、フレームワーク要件に基づく複雑性スコアリング
- 最適選択のための速度対精度トレードオフを評価するパフォーマンス評価
- 直接マッピングと閾値ベースルーティングルールを持つ決定ロジックマトリックス
- Serena（セマンティック操作）対Morphllm（パターン操作）のツール機能マッチング

## MCP Integration
- **Serena MCP**: Optimal for semantic operations, LSP functionality, symbol navigation, and project context
- **Morphllm MCP**: Optimal for pattern-based edits, bulk transformations, and speed-critical operations
- **Decision Matrix**: Intelligent routing based on complexity scoring and operation characteristics

## Tool Coordination
- **get_current_config**: System configuration analysis for tool capability assessment
- **execute_sketched_edit**: Operation testing and validation for selection accuracy
- **Read/Grep**: Operation context analysis and complexity factor identification
- **Integration**: Automatic selection logic used by refactor, edit, implement, and improve commands

## Key Patterns
- **Direct Mapping**: Symbol operations → Serena, Pattern edits → Morphllm, Memory operations → Serena
- **Complexity Thresholds**: Score >0.6 → Serena, Score <0.4 → Morphllm, 0.4-0.6 → Feature-based
- **Performance Trade-offs**: Speed requirements → Morphllm, Accuracy requirements → Serena
- **Fallback Strategy**: Serena → Morphllm → Native tools degradation chain

## Examples

### Complex Refactoring Operation
```
/sc:select-tool "rename function across 10 files" --analyze
# Analysis: High complexity (multi-file, symbol operations)
# Selection: Serena MCP (LSP capabilities, semantic understanding)
```

### Pattern-Based Bulk Edit
```
/sc:select-tool "update console.log to logger.info across project" --explain
# Analysis: Pattern-based transformation, speed priority
# Selection: Morphllm MCP (pattern matching, bulk operations)
```

### Memory Management Operation
```
/sc:select-tool "save project context and discoveries"
# Direct mapping: Memory operations → Serena MCP
# Rationale: Project context and cross-session persistence
```

## Boundaries

**Will:**
- Analyze operations and provide optimal tool selection between Serena and Morphllm
- Apply complexity scoring based on file count, operation type, and requirements
- Provide sub-100ms decision time with >95% selection accuracy

**Will Not:**
- Override explicit tool specifications when user has clear preference
- Select tools without proper complexity analysis and capability matching
- Compromise performance requirements for convenience or speed

