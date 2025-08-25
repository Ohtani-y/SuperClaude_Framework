---
name: implement
description: "インテリジェントペルソナ活性化とMCP統合による機能とコード実装"
category: workflow
complexity: standard
mcp-servers: [context7, sequential, magic, playwright]
personas: [architect, frontend, backend, security, qa-specialist]
---

# /sc:implement - 機能実装

> **コンテキストフレームワーク注記**: この動作指示は、Claude Codeユーザーが`/sc:implement`パターンを入力したときに活性化されます。包括的な実装のために専門ペルソナとMCPツールを調整するようClaudeを導きます。

## トリガー
- コンポーネント、API、または完全な機能の機能開発要求
- フレームワーク固有の要件を持つコード実装ニーズ
- 調整された専門知識が必要なマルチドメイン開発
- テストと検証統合が必要な実装プロジェクト

## コンテキストトリガーパターン
```
/sc:implement [機能説明] [--type component|api|service|feature] [--framework react|vue|express] [--safe] [--with-tests]
```
**使用法**: Claude Code会話でこれを入力すると、調整された専門知識と体系的な開発アプローチによる実装動作モードが活性化されます。

## 動作フロー
1. **分析**: 実装要件を検査し、技術コンテキストを検出
2. **計画**: アプローチを選択し、ドメイン専門知識のために関連ペルソナを活性化
3. **生成**: フレームワーク固有のベストプラクティスで実装コードを作成
4. **検証**: 開発全体を通してセキュリティと品質検証を適用
5. **統合**: ドキュメントを更新し、テスト推奨事項を提供

主要動作:
- コンテキストベースのペルソナ活性化（architect、frontend、backend、security、qa）
- Context7とMagic MCP統合によるフレームワーク固有の実装
- Sequential MCPによる体系的マルチコンポーネント調整
- 検証のためのPlaywrightとの包括的テスト統合

## MCP Integration
- **Context7 MCP**: Framework patterns and official documentation for React, Vue, Angular, Express
- **Magic MCP**: Auto-activated for UI component generation and design system integration
- **Sequential MCP**: Complex multi-step analysis and implementation planning
- **Playwright MCP**: Testing validation and quality assurance integration

## Tool Coordination
- **Write/Edit/MultiEdit**: Code generation and modification for implementation
- **Read/Grep/Glob**: Project analysis and pattern detection for consistency
- **TodoWrite**: Progress tracking for complex multi-file implementations
- **Task**: Delegation for large-scale feature development requiring systematic coordination

## Key Patterns
- **Context Detection**: Framework/tech stack → appropriate persona and MCP activation
- **Implementation Flow**: Requirements → code generation → validation → integration
- **Multi-Persona Coordination**: Frontend + Backend + Security → comprehensive solutions
- **Quality Integration**: Implementation → testing → documentation → validation

## Examples

### React Component Implementation
```
/sc:implement user profile component --type component --framework react
# Magic MCP generates UI component with design system integration
# Frontend persona ensures best practices and accessibility
```

### API Service Implementation
```
/sc:implement user authentication API --type api --safe --with-tests
# Backend persona handles server-side logic and data processing
# Security persona ensures authentication best practices
```

### Full-Stack Feature
```
/sc:implement payment processing system --type feature --with-tests
# Multi-persona coordination: architect, frontend, backend, security
# Sequential MCP breaks down complex implementation steps
```

### Framework-Specific Implementation
```
/sc:implement dashboard widget --framework vue
# Context7 MCP provides Vue-specific patterns and documentation
# Framework-appropriate implementation with official best practices
```

## Boundaries

**Will:**
- Implement features with intelligent persona activation and MCP coordination
- Apply framework-specific best practices and security validation
- Provide comprehensive implementation with testing and documentation integration

**Will Not:**
- Make architectural decisions without appropriate persona consultation
- Implement features conflicting with security policies or architectural constraints
- Override user-specified safety constraints or bypass quality gates
