---
name: workflow
description: "PRDと機能要件から構造化された実装ワークフローを生成"
category: orchestration
complexity: advanced
mcp-servers: [sequential, context7, magic, playwright, morphllm, serena]
personas: [architect, analyzer, frontend, backend, security, devops, project-manager]
---

# /sc:workflow - 実装ワークフロージェネレーター

## トリガー
- 実装計画のためのPRDと機能仕様分析
- 開発プロジェクトの構造化ワークフロー生成
- 複雑な実装戦略のマルチペルソナ調整
- セッション間ワークフロー管理と依存関係マッピング

## 使用法
```
/sc:workflow [prd-file|feature-description] [--strategy systematic|agile|enterprise] [--depth shallow|normal|deep] [--parallel]
```

## 動作フロー
1. **分析**: PRDと機能仕様を解析して実装要件を理解
2. **計画**: 依存関係マッピングとタスクオーケストレーションを含む包括的ワークフロー構造を生成
3. **調整**: ドメイン専門知識と実装戦略のために複数のペルソナを活性化
4. **実行**: 自動化されたタスク調整を含む構造化されたステップバイステップワークフローを作成
5. **検証**: 品質ゲートを適用し、ドメイン間でワークフローの完全性を確保

主要動作:
- アーキテクチャ、フロントエンド、バックエンド、セキュリティ、devopsドメインにわたるマルチペルソナオーケストレーション
- 専門ワークフロー分析のためのインテリジェントルーティングによる高度なMCP調整
- 段階的ワークフロー強化と並列処理による体系的実行
- 包括的依存関係追跡によるセッション間ワークフロー管理

## MCP Integration
- **Sequential MCP**: Complex multi-step workflow analysis and systematic implementation planning
- **Context7 MCP**: Framework-specific workflow patterns and implementation best practices
- **Magic MCP**: UI/UX workflow generation and design system integration strategies
- **Playwright MCP**: Testing workflow integration and quality assurance automation
- **Morphllm MCP**: Large-scale workflow transformation and pattern-based optimization
- **Serena MCP**: Cross-session workflow persistence, memory management, and project context

## Tool Coordination
- **Read/Write/Edit**: PRD analysis and workflow documentation generation
- **TodoWrite**: Progress tracking for complex multi-phase workflow execution
- **Task**: Advanced delegation for parallel workflow generation and multi-agent coordination
- **WebSearch**: Technology research, framework validation, and implementation strategy analysis
- **sequentialthinking**: Structured reasoning for complex workflow dependency analysis

## Key Patterns
- **PRD Analysis**: Document parsing → requirement extraction → implementation strategy development
- **Workflow Generation**: Task decomposition → dependency mapping → structured implementation planning
- **Multi-Domain Coordination**: Cross-functional expertise → comprehensive implementation strategies
- **Quality Integration**: Workflow validation → testing strategies → deployment planning

## Examples

### Systematic PRD Workflow
```
/sc:workflow ClaudeDocs/PRD/feature-spec.md --strategy systematic --depth deep
# Comprehensive PRD analysis with systematic workflow generation
# Multi-persona coordination for complete implementation strategy
```

### Agile Feature Workflow
```
/sc:workflow "user authentication system" --strategy agile --parallel
# Agile workflow generation with parallel task coordination
# Context7 and Magic MCP for framework and UI workflow patterns
```

### Enterprise Implementation Planning
```
/sc:workflow enterprise-prd.md --strategy enterprise --validate
# Enterprise-scale workflow with comprehensive validation
# Security, devops, and architect personas for compliance and scalability
```

### Cross-Session Workflow Management
```
/sc:workflow project-brief.md --depth normal
# Serena MCP manages cross-session workflow context and persistence
# Progressive workflow enhancement with memory-driven insights
```

## Boundaries

**Will:**
- Generate comprehensive implementation workflows from PRD and feature specifications
- Coordinate multiple personas and MCP servers for complete implementation strategies
- Provide cross-session workflow management and progressive enhancement capabilities

**Will Not:**
- Execute actual implementation tasks beyond workflow planning and strategy
- Override established development processes without proper analysis and validation
- Generate workflows without comprehensive requirement analysis and dependency mapping  