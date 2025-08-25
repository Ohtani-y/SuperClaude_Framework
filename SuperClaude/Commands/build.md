---
name: build
description: "インテリジェントなエラーハンドリングと最適化によるプロジェクトのビルド、コンパイル、パッケージング"
category: utility
complexity: enhanced
mcp-servers: [playwright]
personas: [devops-engineer]
---

# /sc:build - プロジェクトビルドとパッケージング

## トリガー
- 異なる環境でのプロジェクトコンパイルとパッケージング要求
- ビルド最適化とアーティファクト生成のニーズ
- ビルドプロセス中のエラーデバッグ
- デプロイメント準備とアーティファクトパッケージング要件

## 使用法
```
/sc:build [target] [--type dev|prod|test] [--clean] [--optimize] [--verbose]
```

## 動作フロー
1. **分析**: プロジェクト構造、ビルド設定、依存関係マニフェスト
2. **検証**: ビルド環境、依存関係、必要なツールチェーンコンポーネント
3. **実行**: リアルタイム監視とエラー検出を伴うビルドプロセス
4. **最適化**: ビルドアーティファクト、最適化の適用、バンドルサイズの最小化
5. **パッケージング**: デプロイメントアーティファクトと包括的ビルドレポートの生成

主要動作:
- 依存関係検証を伴う設定駆動ビルドオーケストレーション
- 実行可能な解決ガイダンスを伴うインテリジェントエラー分析
- 環境固有の最適化（dev/prod/test設定）
- タイミングメトリクスとアーティファクト分析を伴う包括的ビルドレポート

## MCP Integration
- **Playwright MCP**: Auto-activated for build validation and UI testing during builds
- **DevOps Engineer Persona**: Activated for build optimization and deployment preparation
- **Enhanced Capabilities**: Build pipeline integration, performance monitoring, artifact validation

## Tool Coordination
- **Bash**: Build system execution and process management
- **Read**: Configuration analysis and manifest inspection
- **Grep**: Error parsing and build log analysis
- **Glob**: Artifact discovery and validation
- **Write**: Build reports and deployment documentation

## Key Patterns
- **Environment Builds**: dev/prod/test → appropriate configuration and optimization
- **Error Analysis**: Build failures → diagnostic analysis and resolution guidance
- **Optimization**: Artifact analysis → size reduction and performance improvements
- **Validation**: Build verification → quality gates and deployment readiness

## Examples

### Standard Project Build
```
/sc:build
# Builds entire project using default configuration
# Generates artifacts and comprehensive build report
```

### Production Optimization Build
```
/sc:build --type prod --clean --optimize
# Clean production build with advanced optimizations
# Minification, tree-shaking, and deployment preparation
```

### Targeted Component Build
```
/sc:build frontend --verbose
# Builds specific project component with detailed output
# Real-time progress monitoring and diagnostic information
```

### Development Build with Validation
```
/sc:build --type dev --validate
# Development build with Playwright validation
# UI testing and build verification integration
```

## Boundaries

**Will:**
- Execute project build systems using existing configurations
- Provide comprehensive error analysis and optimization recommendations
- Generate deployment-ready artifacts with detailed reporting

**Will Not:**
- Modify build system configuration or create new build scripts
- Install missing build dependencies or development tools
- Execute deployment operations beyond artifact preparation
