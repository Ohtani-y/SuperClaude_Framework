---
name: cleanup
description: "コードの体系的なクリーンアップ、デッドコードの削除、プロジェクト構造の最適化"
category: workflow
complexity: standard
mcp-servers: [sequential, context7]
personas: [architect, quality, security]
---

# /sc:cleanup - コードとプロジェクトのクリーンアップ

## トリガー
- コードメンテナンスと技術的負債削減の要求
- デッドコード削除とインポート最適化のニーズ
- プロジェクト構造改善と整理要件
- コードベースの衛生と品質改善イニシアチブ

## 使用法
```
/sc:cleanup [対象] [--type code|imports|files|all] [--safe|--aggressive] [--interactive]
```

## 動作フロー
1. **分析**: 対象範囲でのクリーンアップ機会と安全性考慮事項を評価
2. **計画**: クリーンアップアプローチを選択し、ドメイン専門知識のために関連ペルソナを活性化
3. **実行**: インテリジェントなデッドコード検出と削除による体系的クリーンアップを適用
4. **検証**: テストと安全性検証により機能損失がないことを確認
5. **報告**: 継続的メンテナンスの推奨事項を含むクリーンアップサマリーを生成

主要動作:
- クリーンアップタイプに基づくマルチペルソナ調整（architect、quality、security）
- Context7 MCP統合によるフレームワーク固有のクリーンアップパターン
- 複雑なクリーンアップ操作のためのSequential MCPによる体系的分析
- バックアップとロールバック機能を備えた安全第一のアプローチ

## MCP Integration
- **Sequential MCP**: Auto-activated for complex multi-step cleanup analysis and planning
- **Context7 MCP**: Framework-specific cleanup patterns and best practices
- **Persona Coordination**: Architect (structure), Quality (debt), Security (credentials)

## Tool Coordination
- **Read/Grep/Glob**: Code analysis and pattern detection for cleanup opportunities
- **Edit/MultiEdit**: Safe code modification and structure optimization
- **TodoWrite**: Progress tracking for complex multi-file cleanup operations
- **Task**: Delegation for large-scale cleanup workflows requiring systematic coordination

## Key Patterns
- **Dead Code Detection**: Usage analysis → safe removal with dependency validation
- **Import Optimization**: Dependency analysis → unused import removal and organization
- **Structure Cleanup**: Architectural analysis → file organization and modular improvements
- **Safety Validation**: Pre/during/post checks → preserve functionality throughout cleanup

## Examples

### Safe Code Cleanup
```
/sc:cleanup src/ --type code --safe
# Conservative cleanup with automatic safety validation
# Removes dead code while preserving all functionality
```

### Import Optimization
```
/sc:cleanup --type imports --preview
# Analyzes and shows unused import cleanup without execution
# Framework-aware optimization via Context7 patterns
```

### Comprehensive Project Cleanup
```
/sc:cleanup --type all --interactive
# Multi-domain cleanup with user guidance for complex decisions
# Activates all personas for comprehensive analysis
```

### Framework-Specific Cleanup
```
/sc:cleanup components/ --aggressive
# Thorough cleanup with Context7 framework patterns
# Sequential analysis for complex dependency management
```

## Boundaries

**Will:**
- Systematically clean code, remove dead code, and optimize project structure
- Provide comprehensive safety validation with backup and rollback capabilities
- Apply intelligent cleanup algorithms with framework-specific pattern recognition

**Will Not:**
- Remove code without thorough safety analysis and validation
- Override project-specific cleanup exclusions or architectural constraints
- Apply cleanup operations that compromise functionality or introduce bugs
