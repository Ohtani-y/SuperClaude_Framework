---
name: estimate
description: "インテリジェント分析によるタスク、機能、プロジェクトの開発見積もりを提供"
category: special
complexity: standard
mcp-servers: [sequential, context7]
personas: [architect, performance, project-manager]
---

# /sc:estimate - 開発見積もり

## トリガー
- 時間、工数、複雑さの見積もりが必要な開発計画
- プロジェクトスコープとリソース配分の決定
- 体系的な見積もり手法が必要な機能分解
- リスク評価と信頼区間分析の要件

## 使用法
```
/sc:estimate [対象] [--type time|effort|complexity] [--unit hours|days|weeks] [--breakdown]
```

## 動作フロー
1. **分析**: スコープ、複雑さ要因、依存関係、フレームワークパターンを調査
2. **計算**: 履歴ベンチマークと複雑さスコアリングによる見積もり手法を適用
3. **検証**: プロジェクトパターンとドメイン専門知識で見積もりを相互参照
4. **提示**: 信頼区間とリスク評価を含む詳細な内訳を提供
5. **追跡**: 継続的な手法改善のための見積もり精度を文書化

主要動作:
- 見積もりスコープに基づくマルチペルソナ調整（architect、performance、project-manager）
- 体系的分析と複雑さ評価のためのSequential MCP統合
- フレームワーク固有パターンと履歴ベンチマークのためのContext7 MCP統合
- 信頼区間とリスク要因を含むインテリジェント内訳分析

## MCP Integration
- **Sequential MCP**: Complex multi-step estimation analysis and systematic complexity assessment
- **Context7 MCP**: Framework-specific estimation patterns and historical benchmark data
- **Persona Coordination**: Architect (design complexity), Performance (optimization effort), Project Manager (timeline)

## Tool Coordination
- **Read/Grep/Glob**: Codebase analysis for complexity assessment and scope evaluation
- **TodoWrite**: Estimation breakdown and progress tracking for complex estimation workflows
- **Task**: Advanced delegation for multi-domain estimation requiring systematic coordination
- **Bash**: Project analysis and dependency evaluation for accurate complexity scoring

## Key Patterns
- **Scope Analysis**: Project requirements → complexity factors → framework patterns → risk assessment
- **Estimation Methodology**: Time-based → Effort-based → Complexity-based → Cost-based approaches
- **Multi-Domain Assessment**: Architecture complexity → Performance requirements → Project timeline
- **Validation Framework**: Historical benchmarks → cross-validation → confidence intervals → accuracy tracking

## Examples

### Feature Development Estimation
```
/sc:estimate "user authentication system" --type time --unit days --breakdown
# Systematic analysis: Database design (2 days) + Backend API (3 days) + Frontend UI (2 days) + Testing (1 day)
# Total: 8 days with 85% confidence interval
```

### Project Complexity Assessment
```
/sc:estimate "migrate monolith to microservices" --type complexity --breakdown
# Architecture complexity analysis with risk factors and dependency mapping
# Multi-persona coordination for comprehensive assessment
```

### Performance Optimization Effort
```
/sc:estimate "optimize application performance" --type effort --unit hours
# Performance persona analysis with benchmark comparisons
# Effort breakdown by optimization category and expected impact
```

## Boundaries

**Will:**
- Provide systematic development estimates with confidence intervals and risk assessment
- Apply multi-persona coordination for comprehensive complexity analysis
- Generate detailed breakdown analysis with historical benchmark comparisons

**Will Not:**
- Guarantee estimate accuracy without proper scope analysis and validation
- Provide estimates without appropriate domain expertise and complexity assessment
- Override historical benchmarks without clear justification and analysis

