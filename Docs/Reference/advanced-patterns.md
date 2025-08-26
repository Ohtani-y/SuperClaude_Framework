# SuperClaude 高度パターン

**高度コンテキスト使用パターン**: 複雑なプロジェクトに取り組む経験豊富なSuperClaudeユーザー向けのコマンド、エージェント、フラグの洗練された組み合わせ。

**注意**: SuperClaudeはClaude Codeにコンテキストを提供します。ここでのすべてのパターンは、コードの実行やプロセスの調整ではなく、コンテキストを通じてClaudeの動作を導くことに関するものです。

## 目次

### コンテキスト組み合わせパターン
- [マルチエージェントコンテキストパターン](#multi-agent-context-patterns) - 複数の専門コンテキストの組み合わせ
- [コマンドシーケンスパターン](#command-sequencing-patterns) - 効果的なコマンド組み合わせ
- [フラグ組み合わせ戦略](#flag-combination-strategies) - 高度なフラグ使用

### ワークフローパターン
- [複雑プロジェクトパターン](#complex-project-patterns) - 大規模プロジェクトアプローチ
- [移行パターン](#migration-patterns) - レガシーシステム現代化
- [レビューと監査パターン](#review-and-audit-patterns) - 包括的分析

## マルチエージェントコンテキストパターン

### 専門コンテキストの組み合わせ

**セキュリティ + バックエンドパターン:**
```bash
# Security-focused backend development
@agent-security "define authentication requirements"
@agent-backend-architect "design API with security requirements"
/sc:implement "secure API endpoints"

# What happens:
# 1. Security context loaded first
# 2. Backend context added
# 3. Implementation guided by both contexts
# Note: Contexts combine in Claude's understanding, not in execution
```

**フロントエンド + UX + アクセシビリティパターン:**
```bash
# 包括的フロントエンド開発
@agent-frontend-architect "コンポーネントアーキテクチャを設計"
/sc:implement "アクセシブルなReactコンポーネント" --magic
@agent-quality-engineer "アクセシビリティ準拠をレビュー"

# コンテキストレイヤリング:
# - フロントエンドパターンが構造をガイド
# - Magic MCPがUIコンポーネントを提供する可能性（設定されている場合）
# - 品質コンテキストが標準を保証
```

### 手動 vs 自動エージェント選択

**明示的制御パターン:**
```bash
# どのコンテキストを読み込むかを手動制御
@agent-python-expert "データパイプラインを実装"
# Pythonコンテキストのみ、自動活性化なし

# vs 自動選択
/sc:implement "Pythonデータパイプライン"
# キーワードに基づいて複数のエージェントが活性化される可能性
```

**自動選択の上書き:**
```bash
# 不要なエージェント活性化を防止
/sc:implement "シンプルユーティリティ" --no-mcp
@agent-backend-architect "シンプルに保つ"
# 指定されたエージェントのみにコンテキストを制限
```

## コマンドシーケンスパターン

### 段階的改良パターン

```bash
# Start broad, then focus
/sc:analyze project/
# General analysis

/sc:analyze project/core/ --focus architecture
# Focused on structure

/sc:analyze project/core/auth/ --focus security --think-hard
# Deep security analysis

# Each command builds on previous context within the conversation
```

### Discovery to Implementation Pattern

```bash
# Complete feature development flow
/sc:brainstorm "feature idea"
# Explores requirements

/sc:design "feature architecture"
# Creates structure

@agent-backend-architect "review design"
# Expert review

/sc:implement "feature based on design"
# Implementation follows design

/sc:test --validate
# Verification approach
```

### Iterative Improvement Pattern

```bash
# Multiple improvement passes
/sc:analyze code/ --focus quality
# Identify issues

/sc:improve code/ --fix
# First improvement pass

@agent-refactoring-expert "suggest further improvements"
# Expert suggestions

/sc:improve code/ --fix --focus maintainability
# Refined improvements
```

## Flag Combination Strategies

### Analysis Depth Control

```bash
# Quick overview
/sc:analyze . --overview --uc
# Fast, compressed output

# Standard analysis
/sc:analyze . --think
# Structured thinking

# Deep analysis
/sc:analyze . --think-hard --verbose
# Comprehensive analysis

# Maximum depth (use sparingly)
/sc:analyze . --ultrathink
# Exhaustive analysis
```

### MCP Server Selection

```bash
# Selective MCP usage
/sc:implement "React component" --magic --c7
# Only Magic and Context7 MCP

# Disable all MCP
/sc:implement "simple function" --no-mcp
# Pure Claude context only

# All available MCP
/sc:analyze complex-system/ --all-mcp
# Maximum tool availability (if configured)
```

## Complex Project Patterns

### Large Codebase Analysis

```bash
# Systematic exploration of large projects
# Step 1: Structure understanding
/sc:load project/
/sc:analyze . --overview --focus architecture

# Step 2: Identify problem areas
@agent-quality-engineer "identify high-risk modules"

# Step 3: Deep dive into specific areas
/sc:analyze high-risk-module/ --think-hard --focus quality

# Step 4: Implementation plan
/sc:workflow "improvement plan based on analysis"
```

### Multi-Module Development

```bash
# Developing interconnected modules
# Frontend module
/sc:implement "user interface module"
@agent-frontend-architect "ensure consistency"

# Backend module
/sc:implement "API module"
@agent-backend-architect "ensure compatibility"

# Integration layer
/sc:implement "frontend-backend integration"
# Context from both previous implementations guides this
```

### Cross-Technology Projects

```bash
# Projects with multiple technologies
# Python backend
@agent-python-expert "implement FastAPI backend"

# React frontend
@agent-frontend-architect "implement React frontend"

# DevOps setup
@agent-devops-architect "create deployment configuration"

# Integration documentation
/sc:document --type integration
```

## Migration Patterns

### Legacy System Analysis

```bash
# Understanding legacy systems
/sc:load legacy-system/
/sc:analyze . --focus architecture --verbose

@agent-refactoring-expert "identify modernization opportunities"
@agent-system-architect "propose migration strategy"

/sc:workflow "create migration plan"
```

### Incremental Migration

```bash
# Step-by-step migration approach
# Phase 1: Analysis
/sc:analyze legacy-module/ --comprehensive

# Phase 2: Design new architecture
@agent-system-architect "design modern replacement"

# Phase 3: Implementation
/sc:implement "modern module with compatibility layer"

# Phase 4: Validation
/sc:test --focus compatibility
```

## Review and Audit Patterns

### Security Audit Pattern

```bash
# Comprehensive security review
/sc:analyze . --focus security --think-hard
@agent-security "review authentication and authorization"
@agent-security "check for OWASP vulnerabilities"
/sc:document --type security-audit
```

### Code Quality Review

```bash
# Multi-aspect quality review
/sc:analyze src/ --focus quality
@agent-quality-engineer "review test coverage"
@agent-refactoring-expert "identify code smells"
/sc:improve --fix --preview
```

### Architecture Review

```bash
# System architecture assessment
@agent-system-architect "review current architecture"
/sc:analyze . --focus architecture --think-hard
@agent-performance-engineer "identify bottlenecks"
/sc:design "optimization recommendations"
```

## Important Clarifications

### What These Patterns Actually Do

- ✅ **Guide Claude's Thinking**: Provide structured approaches
- ✅ **Combine Contexts**: Layer multiple expertise areas
- ✅ **Improve Output Quality**: Better code generation through better context
- ✅ **Structure Workflows**: Organize complex tasks

### What These Patterns Don't Do

- ❌ **Execute in Parallel**: Everything is sequential context loading
- ❌ **Coordinate Processes**: No actual process coordination
- ❌ **Optimize Performance**: No code runs, so no performance impact
- ❌ **Persist Between Sessions**: Each conversation is independent

## Best Practices for Advanced Usage

### Context Management

1. **Layer Deliberately**: Add contexts in logical order
2. **Avoid Overload**: Too many agents can dilute focus
3. **Use Manual Control**: Override auto-activation when needed
4. **Maintain Conversation Flow**: Keep related work in same conversation

### Command Efficiency

1. **Progress Logically**: Broad → Specific → Implementation
2. **Reuse Context**: Later commands benefit from earlier context
3. **Document Decisions**: Use `/sc:save` for important summaries
4. **Scope Appropriately**: Focus on manageable chunks

### Flag Usage

1. **Match Task Complexity**: Simple tasks don't need `--ultrathink`
2. **Control Output**: Use `--uc` for concise results
3. **Manage MCP**: Only activate needed servers
4. **Avoid Conflicts**: Don't use contradictory flags

## Summary

Advanced SuperClaude patterns are about sophisticated context management and command sequencing. They help Claude Code generate better outputs by providing richer, more structured context. Remember: all "coordination" and "optimization" happens in how Claude interprets the context, not in any actual execution or parallel processing.
