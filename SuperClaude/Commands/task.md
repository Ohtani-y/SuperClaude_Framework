---
name: task
description: "インテリジェントなワークフロー管理と委任による複雑なタスクの実行"
category: special
complexity: advanced
mcp-servers: [sequential, context7, magic, playwright, morphllm, serena]
personas: [architect, analyzer, frontend, backend, security, devops, project-manager]
---

# /sc:task - 拡張タスク管理

## トリガー
- マルチエージェント調整と委任が必要な複雑なタスク
- 構造化されたワークフロー管理とセッション間永続化が必要なプロジェクト
- インテリジェントなMCPサーバールーティングとドメイン専門知識が必要な操作
- 体系的実行と段階的強化の恩恵を受けるタスク

## 使用法
```
/sc:task [アクション] [ターゲット] [--strategy systematic|agile|enterprise] [--parallel] [--delegate]
```

## 動作フロー
1. **分析**: タスク要件を解析し、最適な実行戦略を決定
2. **委任**: 適切なMCPサーバーにルーティングし、関連ペルソナを活性化
3. **調整**: インテリジェントなワークフロー管理と並列処理でタスクを実行
4. **検証**: 品質ゲートと包括的タスク完了検証を適用
5. **最適化**: パフォーマンスを分析し、強化推奨事項を提供

主要動作:
- architect、frontend、backend、security、devopsドメインにわたるマルチペルソナ調整
- インテリジェントなMCPサーバールーティング（Sequential、Context7、Magic、Playwright、Morphllm、Serena）
- 段階的タスク強化とセッション間永続化による体系的実行
- 階層的分解と依存関係管理による高度なタスク委任

## MCP Integration
- **Sequential MCP**: Complex multi-step task analysis and systematic execution planning
- **Context7 MCP**: Framework-specific patterns and implementation best practices
- **Magic MCP**: UI/UX task coordination and design system integration
- **Playwright MCP**: Testing workflow integration and validation automation
- **Morphllm MCP**: Large-scale task transformation and pattern-based optimization
- **Serena MCP**: Cross-session task persistence and project memory management

## Tool Coordination
- **TodoWrite**: Hierarchical task breakdown and progress tracking across Epic → Story → Task levels
- **Task**: Advanced delegation for complex multi-agent coordination and sub-task management
- **Read/Write/Edit**: Task documentation and implementation coordination
- **sequentialthinking**: Structured reasoning for complex task dependency analysis

## Key Patterns
- **Task Hierarchy**: Epic-level objectives → Story coordination → Task execution → Subtask granularity
- **Strategy Selection**: Systematic (comprehensive) → Agile (iterative) → Enterprise (governance)
- **Multi-Agent Coordination**: Persona activation → MCP routing → parallel execution → result integration
- **Cross-Session Management**: Task persistence → context continuity → progressive enhancement

## Examples

### Complex Feature Development
```
/sc:task create "enterprise authentication system" --strategy systematic --parallel
# Comprehensive task breakdown with multi-domain coordination
# Activates architect, security, backend, frontend personas
```

### Agile Sprint Coordination
```
/sc:task execute "feature backlog" --strategy agile --delegate
# Iterative task execution with intelligent delegation
# Cross-session persistence for sprint continuity
```

### Multi-Domain Integration
```
/sc:task execute "microservices platform" --strategy enterprise --parallel
# Enterprise-scale coordination with compliance validation
# Parallel execution across multiple technical domains
```

## Boundaries

**Will:**
- Execute complex tasks with multi-agent coordination and intelligent delegation
- Provide hierarchical task breakdown with cross-session persistence
- Coordinate multiple MCP servers and personas for optimal task outcomes

**Will Not:**
- Execute simple tasks that don't require advanced orchestration
- Compromise quality standards for speed or convenience
- Operate without proper validation and quality gates
