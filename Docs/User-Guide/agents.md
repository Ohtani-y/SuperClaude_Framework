# SuperClaude エージェントガイド 🤖

SuperClaudeは、Claude Codeが専門知識のために呼び出すことができる14のドメイン専門エージェントを提供します。


## 🧪 エージェント活性化テスト

このガイドを使用する前に、エージェント選択が機能することを確認してください:

```bash
# 手動エージェント呼び出しのテスト
@agent-python-expert "デコレータについて説明してください"
# 期待される動作: Pythonエキスパートが詳細な説明で応答

# セキュリティエージェントの自動活性化テスト
/sc:implement "JWT認証"
# 期待される動作: セキュリティエンジニアが自動的に活性化

# フロントエンドエージェントの自動活性化テスト
/sc:implement "レスポンシブナビゲーションコンポーネント"  
# 期待される動作: フロントエンドアーキテクト + Magic MCPが活性化

# 体系的分析のテスト
/sc:troubleshoot "API パフォーマンスが遅い"
# 期待される動作: 根本原因分析エージェント + パフォーマンスエンジニアが活性化

# 手動と自動の組み合わせテスト
/sc:analyze src/
@agent-refactoring-expert "改善案を提案してください"
# 期待される動作: 分析に続いてリファクタリング提案
```

**テストが失敗した場合**: `~/.claude/agents/`にエージェントファイルが存在するか確認するか、Claude Codeセッションを再起動してください

## 中核概念

### SuperClaudeエージェントとは？
**エージェント**は、Claude Codeの動作を変更するコンテキスト指示として実装された専門AIドメインエキスパートです。各エージェントは、ドメイン固有の専門知識、行動パターン、問題解決アプローチを含む、`SuperClaude/Agents/`ディレクトリ内の慎重に作成された`.md`ファイルです。

**重要**: エージェントは別個のAIモデルやソフトウェアではありません - Claude Codeが専門的な動作を採用するために読み取るコンテキスト設定です。

### エージェントを使用する2つの方法

#### 1. @agent-プレフィックスによる手動呼び出し
```bash
# 特定のエージェントを直接呼び出す
@agent-security "認証実装をレビューしてください"
@agent-frontend "レスポンシブナビゲーションを設計してください"
@agent-architect "マイクロサービス移行を計画してください"
```

#### 2. 自動活性化（動作ルーティング）
「自動活性化」とは、Claude Codeがあなたのリクエスト内のキーワードとパターンに基づいて適切なコンテキストを関与させるために動作指示を読み取ることを意味します。SuperClaudeは、Claudeが最も適切な専門家にルーティングするために従う動作ガイドラインを提供します。

> **📝 エージェントの「自動活性化」の仕組み**: 
> エージェントの活性化は自動システムロジックではなく、コンテキストファイル内の行動指示です。
> ドキュメントでエージェントが「自動活性化」すると記載されている場合、Claude Codeがリクエスト内の
> キーワードとパターンに基づいて特定のドメイン専門知識を適用するための指示を読み取ることを意味します。
> これにより、基盤となるメカニズムについて透明性を保ちながら、インテリジェントなルーティングの体験を提供します。

```bash
# これらのコマンドは関連エージェントを自動活性化します
/sc:implement "JWT認証"             # → セキュリティエンジニアが自動活性化
/sc:design "Reactダッシュボード"     # → フロントエンドアーキテクトが自動活性化
/sc:troubleshoot "メモリリーク"      # → パフォーマンスエンジニアが自動活性化
```

**MCPサーバー**は、Context7（ドキュメント）、Sequential（分析）、Magic（UI）、Playwright（テスト）、Morphllm（コード変換）などの専門ツールを通じて強化された機能を提供します。

**ドメイン専門家**は、汎用アプローチよりも深く正確なソリューションを提供するために、狭い専門分野に焦点を当てます。

### エージェント選択ルール

**優先階層:**
1. **手動オーバーライド** - @agent-[名前] が自動活性化より優先されます
2. **キーワード** - ドメイン固有の用語が主要エージェントをトリガーします
3. **ファイルタイプ** - 拡張子が言語/フレームワークの専門家を活性化します  
4. **複雑性** - 複数ステップのタスクが調整エージェントを起動します
5. **コンテキスト** - 関連概念が補完的なエージェントをトリガーします

**競合解決:**
- 手動呼び出し → 指定されたエージェントが優先
- 複数の一致 → マルチエージェント調整
- 不明確なコンテキスト → 要件アナリストが活性化
- 高い複雑性 → システムアーキテクトの監督
- 品質の懸念 → 自動的にQAエージェントを含める

**選択決定ツリー:**
```
タスク分析 →
├─ 手動 @agent-? → 指定エージェントを使用
├─ 単一ドメイン? → 主要エージェントを活性化
├─ マルチドメイン? → 専門エージェントを調整  
├─ 複雑なシステム? → システムアーキテクトの監督を追加
├─ 品質重視? → セキュリティ + パフォーマンス + 品質エージェントを含める
└─ 学習重視? → 学習ガイド + テクニカルライターを追加
```

## Quick Start Examples

### Manual Agent Invocation
```bash
# @agent- プレフィックスで特定のエージェントを明示的に呼び出す
@agent-python-expert "このデータ処理パイプラインを最適化してください"
@agent-quality-engineer "包括的なテストスイートを作成してください"
@agent-technical-writer "このAPIを例付きでドキュメント化してください"
@agent-socratic-mentor "このデザインパターンを説明してください"
```

### Automatic Agent Coordination
```bash
# 自動活性化をトリガーするコマンド
/sc:implement "レート制限付きJWT認証"
# → トリガー: セキュリティエンジニア + バックエンドアーキテクト + 品質エンジニア

/sc:design "ドキュメント付きアクセシブルなReactダッシュボード"
# → トリガー: フロントエンドアーキテクト + 学習ガイド + テクニカルライター  

/sc:troubleshoot "断続的な障害を伴う遅いデプロイメントパイプライン"
# → トリガー: DevOpsアーキテクト + パフォーマンスエンジニア + 根本原因アナリスト

/sc:audit "決済処理のセキュリティ脆弱性"
# → トリガー: セキュリティエンジニア + 品質エンジニア + リファクタリングエキスパート
```

### Combining Manual and Auto Approaches
```bash
# コマンドから開始（自動活性化）
/sc:implement "ユーザープロファイルシステム"

# その後、専門家レビューを明示的に追加
@agent-security "プロファイルシステムのOWASP準拠をレビューしてください"
@agent-performance-engineer "データベースクエリを最適化してください"
```

---

## The SuperClaude Agent Team 👥

### Architecture & System Design Agents 🏗️

### system-architect 🏢
**Expertise**: Large-scale distributed system design with focus on scalability and service architecture

**Auto-Activation**:
- Keywords: "architecture", "microservices", "scalability", "system design", "distributed"
- Context: Multi-service systems, architectural decisions, technology selection
- Complexity: >5 components or cross-domain integration requirements

**Capabilities**:
- Service boundary definition and microservices decomposition
- Technology stack selection and integration strategy
- Scalability planning and performance architecture
- Event-driven architecture and messaging patterns
- Data flow design and system integration

**Examples**:
1. **E-commerce Platform**: Design microservices for user, product, payment, and notification services with event sourcing
2. **Real-time Analytics**: Architecture for high-throughput data ingestion with stream processing and time-series storage
3. **Multi-tenant SaaS**: System design with tenant isolation, shared infrastructure, and horizontal scaling strategies

### 成功基準
- [ ] レスポンスにシステムレベルの思考が明確に見られる
- [ ] サービス境界と統合パターンに言及している
- [ ] スケーラビリティと信頼性の考慮事項を含む
- [ ] テクノロジースタックの推奨を提供している

**検証:** `/sc:design "マイクロサービスプラットフォーム"` でsystem-architectが活性化すること  
**テスト:** 出力にサービス分解と統合パターンが含まれること  
**確認:** インフラの懸念事項についてdevops-architectと調整すること

**Works Best With**: devops-architect (infrastructure), performance-engineer (optimization), security-engineer (compliance)

---

### backend-architect ⚙️
**Expertise**: Robust server-side system design with emphasis on API reliability and data integrity

**Auto-Activation**:
- Keywords: "API", "backend", "server", "database", "REST", "GraphQL", "endpoint"
- File Types: API specs, server configs, database schemas
- Context: Server-side logic, data persistence, API development

**Capabilities**:
- RESTful and GraphQL API architecture and design patterns
- Database schema design and query optimization strategies
- Authentication, authorization, and security implementation
- Error handling, logging, and monitoring integration
- Caching strategies and performance optimization

**Examples**:
1. **User Management API**: JWT authentication with role-based access control and rate limiting
2. **Payment Processing**: PCI-compliant transaction handling with idempotency and audit trails
3. **Content Management**: RESTful APIs with caching, pagination, and real-time notifications

**Works Best With**: security-engineer (auth/security), performance-engineer (optimization), quality-engineer (testing)

---

### frontend-architect 🎨
**Expertise**: Modern web application architecture with focus on accessibility and user experience

**Auto-Activation**:
- Keywords: "UI", "frontend", "React", "Vue", "Angular", "component", "accessibility", "responsive"
- File Types: .jsx, .vue, .ts (frontend), .css, .scss
- Context: User interface development, component design, client-side architecture

**Capabilities**:
- Component architecture and design system implementation
- State management patterns (Redux, Zustand, Pinia)
- Accessibility compliance (WCAG 2.1) and inclusive design
- Performance optimization and bundle analysis
- Progressive Web App and mobile-first development

**Examples**:
1. **Dashboard Interface**: Accessible data visualization with real-time updates and responsive grid layout
2. **Form Systems**: Complex multi-step forms with validation, error handling, and accessibility features
3. **Design System**: Reusable component library with consistent styling and interaction patterns

**Works Best With**: learning-guide (user guidance), performance-engineer (optimization), quality-engineer (testing)

---

### devops-architect 🚀
**Expertise**: Infrastructure automation and deployment pipeline design for reliable software delivery

**Auto-Activation**:
- Keywords: "deploy", "CI/CD", "Docker", "Kubernetes", "infrastructure", "monitoring", "pipeline"
- File Types: Dockerfile, docker-compose.yml, k8s manifests, CI configs
- Context: Deployment processes, infrastructure management, automation

**Capabilities**:
- CI/CD pipeline design with automated testing and deployment
- Container orchestration and Kubernetes cluster management
- Infrastructure as Code with Terraform and cloud platforms
- Monitoring, logging, and observability stack implementation
- Security scanning and compliance automation

**Examples**:
1. **Microservices Deployment**: Kubernetes deployment with service mesh, auto-scaling, and blue-green releases
2. **Multi-Environment Pipeline**: GitOps workflow with automated testing, security scanning, and staged deployments
3. **Monitoring Stack**: Comprehensive observability with metrics, logs, traces, and alerting systems

**Works Best With**: system-architect (infrastructure planning), security-engineer (compliance), performance-engineer (monitoring)

### Quality & Analysis Agents 🔍

### security-engineer 🔒
**Expertise**: Application security architecture with focus on threat modeling and vulnerability prevention

**Auto-Activation**:
- Keywords: "security", "auth", "authentication", "vulnerability", "encryption", "compliance", "OWASP"
- Context: Security reviews, authentication flows, data protection requirements
- Risk Indicators: Payment processing, user data, API access, regulatory compliance needs

**Capabilities**:
- Threat modeling and attack surface analysis
- Secure authentication and authorization design (OAuth, JWT, SAML)
- Data encryption strategies and key management
- Vulnerability assessment and penetration testing guidance
- Security compliance (GDPR, HIPAA, PCI-DSS) implementation

**Examples**:
1. **OAuth Implementation**: Secure multi-tenant authentication with token refresh and role-based access
2. **API Security**: Rate limiting, input validation, SQL injection prevention, and security headers
3. **Data Protection**: Encryption at rest/transit, key rotation, and privacy-by-design architecture

**Works Best With**: backend-architect (API security), quality-engineer (security testing), root-cause-analyst (incident response)

---

### performance-engineer ⚡
**Expertise**: System performance optimization with focus on scalability and resource efficiency

**Auto-Activation**:
- Keywords: "performance", "slow", "optimization", "bottleneck", "latency", "memory", "CPU"
- Context: Performance issues, scalability concerns, resource constraints
- Metrics: Response times >500ms, high memory usage, poor throughput

**Capabilities**:
- Performance profiling and bottleneck identification
- Database query optimization and indexing strategies  
- Caching implementation (Redis, CDN, application-level)
- Load testing and capacity planning
- Memory management and resource optimization

**Examples**:
1. **API Optimization**: Reduce response time from 2s to 200ms through caching and query optimization
2. **Database Scaling**: Implement read replicas, connection pooling, and query result caching
3. **Frontend Performance**: Bundle optimization, lazy loading, and CDN implementation for <3s load times

**Works Best With**: system-architect (scalability), devops-architect (infrastructure), root-cause-analyst (debugging)

---

### root-cause-analyst 🔍
**Expertise**: Systematic problem investigation using evidence-based analysis and hypothesis testing

**Auto-Activation**:
- Keywords: "bug", "issue", "problem", "debugging", "investigation", "troubleshoot", "error"
- Context: System failures, unexpected behavior, complex multi-component issues
- Complexity: Cross-system problems requiring methodical investigation

**Capabilities**:
- Systematic debugging methodology and root cause analysis
- Error correlation and dependency mapping across systems
- Log analysis and pattern recognition for failure investigation
- Hypothesis formation and testing for complex problems
- Incident response and post-mortem analysis procedures

**Examples**:
1. **Database Connection Failures**: Trace intermittent failures across connection pools, network timeouts, and resource limits
2. **Payment Processing Errors**: Investigate transaction failures through API logs, database states, and external service responses
3. **Performance Degradation**: Analyze gradual slowdown through metrics correlation, resource usage, and code changes

**Works Best With**: performance-engineer (performance issues), security-engineer (security incidents), quality-engineer (testing failures)

---

### quality-engineer ✅
**Expertise**: Comprehensive testing strategy and quality assurance with focus on automation and coverage

**Auto-Activation**:
- Keywords: "test", "testing", "quality", "QA", "validation", "coverage", "automation"
- Context: Test planning, quality gates, validation requirements
- Quality Concerns: Code coverage <80%, missing test automation, quality issues

**Capabilities**:
- Test strategy design (unit, integration, e2e, performance testing)
- Test automation framework implementation and CI/CD integration
- Quality metrics definition and monitoring (coverage, defect rates)
- Edge case identification and boundary testing scenarios
- Accessibility testing and compliance validation

**Examples**:
1. **E-commerce Testing**: Comprehensive test suite covering user flows, payment processing, and inventory management
2. **API Testing**: Automated contract testing, load testing, and security testing for REST/GraphQL APIs
3. **Accessibility Validation**: WCAG 2.1 compliance testing with automated and manual accessibility audits

**Works Best With**: security-engineer (security testing), performance-engineer (load testing), frontend-architect (UI testing)

---

### refactoring-expert 🔧
**Expertise**: Code quality improvement through systematic refactoring and technical debt management

**Auto-Activation**:
- Keywords: "refactor", "clean code", "technical debt", "SOLID", "maintainability", "code smell"
- Context: Legacy code improvements, architecture updates, code quality issues
- Quality Indicators: High complexity, duplicated code, poor test coverage

**Capabilities**:
- SOLID principles application and design pattern implementation
- Code smell identification and systematic elimination
- Legacy code modernization strategies and migration planning
- Technical debt assessment and prioritization frameworks
- Code structure improvement and architecture refactoring

**Examples**:
1. **Legacy Modernization**: Transform monolithic application to modular architecture with improved testability
2. **Design Patterns**: Implement Strategy pattern for payment processing to reduce coupling and improve extensibility  
3. **Code Cleanup**: Remove duplicated code, improve naming conventions, and extract reusable components

**Works Best With**: system-architect (architecture improvements), quality-engineer (testing strategy), python-expert (language-specific patterns)

### Specialized Development Agents 🎯

### python-expert 🐍
**Expertise**: Production-ready Python development with emphasis on modern frameworks and performance

**Auto-Activation**:
- Keywords: "Python", "Django", "FastAPI", "Flask", "asyncio", "pandas", "pytest"
- File Types: .py, requirements.txt, pyproject.toml, Pipfile
- Context: Python development tasks, API development, data processing, testing

**Capabilities**:
- Modern Python architecture patterns and framework selection
- Asynchronous programming with asyncio and concurrent futures
- Performance optimization through profiling and algorithmic improvements
- Testing strategies with pytest, fixtures, and test automation
- Package management and deployment with pip, poetry, and Docker

**Examples**:
1. **FastAPI Microservice**: High-performance async API with Pydantic validation, dependency injection, and OpenAPI docs
2. **Data Pipeline**: Pandas-based ETL with error handling, logging, and parallel processing for large datasets
3. **Django Application**: Full-stack web app with custom user models, API endpoints, and comprehensive test coverage

**Works Best With**: backend-architect (API design), quality-engineer (testing), performance-engineer (optimization)

---

### requirements-analyst 📝
**Expertise**: Requirements discovery and specification development through systematic stakeholder analysis

**Auto-Activation**:
- Keywords: "requirements", "specification", "PRD", "user story", "functional", "scope", "stakeholder"
- Context: Project initiation, unclear requirements, scope definition needs
- Complexity: Multi-stakeholder projects, unclear objectives, conflicting requirements

**Capabilities**:
- Requirements elicitation through stakeholder interviews and workshops
- User story writing with acceptance criteria and definition of done
- Functional and non-functional specification documentation
- Stakeholder analysis and requirement prioritization frameworks
- Scope management and change control processes

**Examples**:
1. **Product Requirements Document**: Comprehensive PRD for fintech mobile app with user personas, feature specifications, and success metrics
2. **API Specification**: Detailed requirements for payment processing API with error handling, security, and performance criteria
3. **Migration Requirements**: Legacy system modernization requirements with data migration, user training, and rollback procedures

**Works Best With**: system-architect (technical feasibility), technical-writer (documentation), learning-guide (user guidance)

### Communication & Learning Agents 📚

### technical-writer 📚
**Expertise**: Technical documentation and communication with focus on audience analysis and clarity

**Auto-Activation**:
- Keywords: "documentation", "readme", "API docs", "user guide", "technical writing", "manual"
- Context: Documentation requests, API documentation, user guides, technical explanations
- File Types: .md, .rst, API specs, documentation files

**Capabilities**:
- Technical documentation architecture and information design
- Audience analysis and content targeting for different skill levels
- API documentation with working examples and integration guidance
- User guide creation with step-by-step procedures and troubleshooting
- Accessibility standards application and inclusive language usage

**Examples**:
1. **API Documentation**: Comprehensive REST API docs with authentication, endpoints, examples, and SDK integration guides
2. **User Manual**: Step-by-step installation and configuration guide with screenshots, troubleshooting, and FAQ sections
3. **Technical Specification**: System architecture documentation with diagrams, data flows, and implementation details

**Works Best With**: requirements-analyst (specification clarity), learning-guide (educational content), frontend-architect (UI documentation)

---

### learning-guide 🎓
**Expertise**: Educational content design and progressive learning with focus on skill development and mentorship

**Auto-Activation**:
- Keywords: "explain", "learn", "tutorial", "beginner", "teaching", "education", "training"
- Context: Educational requests, concept explanations, skill development, learning paths
- Complexity: Complex topics requiring step-by-step breakdown and progressive understanding

**Capabilities**:
- Learning path design with progressive skill development
- Complex concept explanation through analogies and examples
- Interactive tutorial creation with hands-on exercises
- Skill assessment and competency evaluation frameworks
- Mentorship strategies and personalized learning approaches

**Examples**:
1. **Programming Tutorial**: Interactive React tutorial with hands-on exercises, code examples, and progressive complexity
2. **Concept Explanation**: Database normalization explained through real-world examples with visual diagrams and practice exercises
3. **Skill Assessment**: Comprehensive evaluation framework for full-stack development with practical projects and feedback

**Works Best With**: technical-writer (educational documentation), frontend-architect (interactive learning), requirements-analyst (learning objectives)

---

## Agent Coordination & Integration 🤝

### Coordination Patterns

**Architecture Teams**:
- **Full-Stack Development**: frontend-architect + backend-architect + security-engineer + quality-engineer
- **System Design**: system-architect + devops-architect + performance-engineer + security-engineer
- **Legacy Modernization**: refactoring-expert + system-architect + quality-engineer + technical-writer

**Quality Teams**:
- **Security Audit**: security-engineer + quality-engineer + root-cause-analyst + requirements-analyst
- **Performance Optimization**: performance-engineer + system-architect + devops-architect + root-cause-analyst
- **Testing Strategy**: quality-engineer + security-engineer + performance-engineer + frontend-architect

**Communication Teams**:
- **Documentation Project**: technical-writer + requirements-analyst + learning-guide + domain experts
- **Learning Platform**: learning-guide + frontend-architect + technical-writer + quality-engineer
- **API Documentation**: backend-architect + technical-writer + security-engineer + quality-engineer

### MCP Server Integration

**Enhanced Capabilities through MCP Servers**:
- **Context7**: Official documentation patterns for all architects and specialists
- **Sequential**: Multi-step analysis for root-cause-analyst, system-architect, performance-engineer
- **Magic**: UI generation for frontend-architect, learning-guide interactive content
- **Playwright**: Browser testing for quality-engineer, accessibility validation for frontend-architect
- **Morphllm**: Code transformation for refactoring-expert, bulk changes for python-expert
- **Serena**: Project memory for all agents, context preservation across sessions

### Troubleshooting Agent Activation

## Troubleshooting

For troubleshooting help, see:
- [Common Issues](../Reference/common-issues.md) - Quick fixes for frequent problems
- [Troubleshooting Guide](../Reference/troubleshooting.md) - Comprehensive problem resolution

### Common Issues
- **No agent activation**: Use domain keywords: "security", "performance", "frontend"
- **Wrong agents selected**: Check trigger keywords in agent documentation
- **Too many agents**: Focus keywords on primary domain or use `/sc:focus [domain]`
- **Agents not coordinating**: Increase task complexity or use multi-domain keywords
- **Agent expertise mismatch**: Use more specific technical terminology

### Immediate Fixes
- **Force agent activation**: Use explicit domain keywords in requests
- **Reset agent selection**: Restart Claude Code session to reset agent state
- **Check agent patterns**: Review trigger keywords in agent documentation
- **Test basic activation**: Try `/sc:implement "security auth"` to test security-engineer

### Agent-Specific Troubleshooting

**No Security Agent:**
```bash
# Problem: Security concerns not triggering security-engineer
# Quick Fix: Use explicit security keywords
"implement authentication"              # Generic - may not trigger
"implement JWT authentication security" # Explicit - triggers security-engineer
"secure user login with encryption"    # Security focus - triggers security-engineer
```

**No Performance Agent:**
```bash
# Problem: Performance issues not triggering performance-engineer
# Quick Fix: Use performance-specific terminology
"make it faster"                       # Vague - may not trigger
"optimize slow database queries"       # Specific - triggers performance-engineer  
"reduce API latency and bottlenecks"   # Performance focus - triggers performance-engineer
```

**No Architecture Agent:**
```bash
# Problem: System design not triggering architecture agents
# Quick Fix: Use architectural keywords
"build an app"                         # Generic - triggers basic agents
"design microservices architecture"    # Specific - triggers system-architect
"scalable distributed system design"   # Architecture focus - triggers system-architect
```

**Wrong Agent Combination:**
```bash
# Problem: Getting frontend agent for backend tasks
# Quick Fix: Use domain-specific terminology
"create user interface"                # May trigger frontend-architect
"create REST API endpoints"            # Specific - triggers backend-architect
"implement server-side authentication" # Backend focus - triggers backend-architect
```

### Support Levels

**Quick Fix:**
- Use explicit domain keywords from agent trigger table
- Try restarting Claude Code session
- Focus on single domain to avoid confusion

**Detailed Help:**
- See [Common Issues Guide](../Reference/common-issues.md) for agent installation problems
- Review trigger keywords for target agents

**Expert Support:**  
- Use `SuperClaude install --diagnose`
- See [Diagnostic Reference Guide](../Reference/diagnostic-reference.md) for coordination analysis

**Community Support:**
- Report issues at [GitHub Issues](https://github.com/SuperClaude-Org/SuperClaude_Framework/issues)
- Include examples of expected vs actual agent activation

### Success Validation

After applying agent fixes, test with:
- [ ] Domain-specific requests activate correct agents (security → security-engineer)
- [ ] Complex tasks trigger multi-agent coordination (3+ agents)
- [ ] Agent expertise matches task requirements (API → backend-architect)
- [ ] Quality agents auto-include when appropriate (security, performance, testing)
- [ ] Responses show domain expertise and specialized knowledge

## Quick Troubleshooting (Legacy)
- **No agent activation** → Use domain keywords: "security", "performance", "frontend"
- **Wrong agents** → Check trigger keywords in agent documentation
- **Too many agents** → Focus keywords on primary domain
- **Agents not coordinating** → Increase task complexity or use multi-domain keywords

**Agent Not Activating?**
1. **Check Keywords**: Use domain-specific terminology (e.g., "authentication" not "login" for security-engineer)
2. **Add Context**: Include file types, frameworks, or specific technologies
3. **Increase Complexity**: Multi-domain problems trigger more agents
4. **Use Examples**: Reference concrete scenarios that match agent expertise

**Too Many Agents?**
- Focus keywords on primary domain needs
- Use `/sc:focus [domain]` to limit scope
- Start with specific agents, expand as needed

**Wrong Agents?**
- Review trigger keywords in agent documentation
- Use more specific terminology for target domain
- Add explicit requirements or constraints

## Quick Reference 📋

### Agent Trigger Lookup

| Trigger Type | Keywords/Patterns | Activated Agents |
|-------------|-------------------|------------------|
| **Security** | "auth", "security", "vulnerability", "encryption" | security-engineer |
| **Performance** | "slow", "optimization", "bottleneck", "latency" | performance-engineer |
| **Frontend** | "UI", "React", "Vue", "component", "responsive" | frontend-architect |
| **Backend** | "API", "server", "database", "REST", "GraphQL" | backend-architect |
| **Testing** | "test", "QA", "validation", "coverage" | quality-engineer |
| **DevOps** | "deploy", "CI/CD", "Docker", "Kubernetes" | devops-architect |
| **Architecture** | "architecture", "microservices", "scalability" | system-architect |
| **Python** | ".py", "Django", "FastAPI", "asyncio" | python-expert |
| **Problems** | "bug", "issue", "debugging", "troubleshoot" | root-cause-analyst |
| **Code Quality** | "refactor", "clean code", "technical debt" | refactoring-expert |
| **Documentation** | "documentation", "readme", "API docs" | technical-writer |
| **Learning** | "explain", "tutorial", "beginner", "teaching" | learning-guide |
| **Requirements** | "requirements", "PRD", "specification" | requirements-analyst |

### Command-Agent Mapping

| Command | Primary Agents | Supporting Agents |
|---------|----------------|-------------------|
| `/sc:implement` | Domain architects (frontend, backend) | security-engineer, quality-engineer |
| `/sc:analyze` | quality-engineer, security-engineer | performance-engineer, root-cause-analyst |
| `/sc:troubleshoot` | root-cause-analyst | Domain specialists, performance-engineer |
| `/sc:improve` | refactoring-expert | quality-engineer, performance-engineer |
| `/sc:document` | technical-writer | Domain specialists, learning-guide |
| `/sc:design` | system-architect | Domain architects, requirements-analyst |
| `/sc:test` | quality-engineer | security-engineer, performance-engineer |
| `/sc:explain` | learning-guide | technical-writer, domain specialists |

### Effective Agent Combinations

**Development Workflows**:
- Web application: frontend-architect + backend-architect + security-engineer + quality-engineer + devops-architect
- API development: backend-architect + security-engineer + technical-writer + quality-engineer  
- Data platform: python-expert + performance-engineer + security-engineer + system-architect

**Analysis Workflows**:
- Security audit: security-engineer + quality-engineer + root-cause-analyst + technical-writer
- Performance investigation: performance-engineer + root-cause-analyst + system-architect + devops-architect
- Legacy assessment: refactoring-expert + system-architect + quality-engineer + security-engineer + technical-writer

**Communication Workflows**:
- Technical documentation: technical-writer + requirements-analyst + domain experts + learning-guide
- Educational content: learning-guide + technical-writer + frontend-architect + quality-engineer

## Best Practices 💡

### Getting Started (Simple Approach)

**Natural Language First:**
1. **Describe Your Goal**: Use natural language with domain-specific keywords
2. **Trust Auto-Activation**: Let the system route to appropriate agents automatically  
3. **Learn from Patterns**: Observe which agents activate for different request types
4. **Iterate and Refine**: Add specificity to engage additional specialist agents

### Optimizing Agent Selection

**Effective Keyword Usage:**
- **Specific > Generic**: Use "authentication" instead of "login" for security-engineer
- **Technical Terms**: Include framework names, technologies, and specific challenges
- **Context Clues**: Mention file types, project scope, and complexity indicators
- **Quality Keywords**: Add "security", "performance", "accessibility" for comprehensive coverage

**Request Optimization Examples:**
```bash
# Generic (limited agent activation)
"Fix the login feature"

# Optimized (multi-agent coordination)  
"Implement secure JWT authentication with rate limiting and accessibility compliance"
# → Triggers: security-engineer + backend-architect + frontend-architect + quality-engineer
```

### Common Usage Patterns

**Development Workflows:**
```bash
# Full-stack feature development
/sc:implement "responsive user dashboard with real-time notifications"
# → frontend-architect + backend-architect + performance-engineer

# API development with documentation
/sc:create "REST API for payment processing with comprehensive docs"  
# → backend-architect + security-engineer + technical-writer + quality-engineer

# Performance optimization investigation
/sc:troubleshoot "slow database queries affecting user experience"
# → performance-engineer + root-cause-analyst + backend-architect
```

**Analysis Workflows:**
```bash
# Security assessment
/sc:analyze "authentication system for GDPR compliance vulnerabilities"
# → security-engineer + quality-engineer + requirements-analyst

# Code quality review  
/sc:review "legacy codebase for modernization opportunities"
# → refactoring-expert + system-architect + quality-engineer + technical-writer

# Learning and explanation
/sc:explain "microservices patterns with hands-on examples"
# → system-architect + learning-guide + technical-writer
```

### Advanced Agent Coordination

**Multi-Domain Projects:**
- **Start Broad**: Begin with system-level keywords to engage architecture agents
- **Add Specificity**: Include domain-specific needs to activate specialist agents  
- **Quality Integration**: Automatically include security, performance, and testing perspectives
- **Documentation Inclusion**: Add learning or documentation needs for comprehensive coverage

**Troubleshooting Agent Selection:**

**Problem: Wrong agents activating**
- Solution: Use more specific domain terminology
- Example: "database optimization" → performance-engineer + backend-architect

**Problem: Not enough agents**  
- Solution: Increase complexity indicators and cross-domain keywords
- Example: Add "security", "performance", "documentation" to requests

**Problem: Too many agents**
- Solution: Focus on primary domain with specific technical terms
- Example: Use "/sc:focus backend" to limit scope

### Quality-Driven Development

**Security-First Approach:**
Always include security considerations in development requests to automatically engage security-engineer alongside domain specialists.

**Performance Integration:**
Include performance keywords ("fast", "efficient", "scalable") to ensure performance-engineer coordination from the start.

**Accessibility Compliance:**
Use "accessible", "WCAG", or "inclusive" to automatically include accessibility validation in frontend development.

**Documentation Culture:**
Add "documented", "explained", or "tutorial" to requests for automatic technical-writer inclusion and knowledge transfer.

---

## Understanding Agent Intelligence 🧠

### What Makes Agents Effective

**Domain Expertise**: Each agent has specialized knowledge patterns, behavioral approaches, and problem-solving methodologies specific to their domain.

**Contextual Activation**: Agents analyze request context, not just keywords, to determine relevance and engagement level.

**Collaborative Intelligence**: Multi-agent coordination produces synergistic results that exceed individual agent capabilities.

**Adaptive Learning**: Agent selection improves based on request patterns and successful coordination outcomes.

### Agent vs. Traditional AI

**Traditional Approach**: Single AI handles all domains with varying levels of expertise
**Agent Approach**: Specialized experts collaborate with deep domain knowledge and focused problem-solving

**Benefits**:
- Higher accuracy in domain-specific tasks
- More sophisticated problem-solving methodologies  
- Better quality assurance through specialist review
- Coordinated multi-perspective analysis

### Trust the System, Understand the Patterns

**What to Expect**:
- Automatic routing to appropriate domain experts
- Multi-agent coordination for complex tasks
- Quality integration through automatic QA agent inclusion
- Learning opportunities through educational agent activation

**What Not to Worry About**:
- Manual agent selection or configuration
- Complex routing rules or agent management
- Agent configuration or coordination
- Micromanaging agent interactions

---

## Related Resources 📚

### Essential Documentation
- **[Commands Guide](commands.md)** - Master SuperClaude commands that trigger optimal agent coordination
- **[MCP Servers](mcp-servers.md)** - Enhanced agent capabilities through specialized tool integration  
- **[Session Management](session-management.md)** - Long-term workflows with persistent agent context

### Advanced Usage  
- **[Behavioral Modes](modes.md)** - Context optimization for enhanced agent coordination
- **[Getting Started](../Getting-Started/quick-start.md)** - Expert techniques for agent optimization
- **[Examples Cookbook](../Reference/examples-cookbook.md)** - Real-world agent coordination patterns

### Development Resources
- **[Technical Architecture](../Developer-Guide/technical-architecture.md)** - Understanding SuperClaude's agent system design
- **[Contributing](../Developer-Guide/contributing-code.md)** - Extending agent capabilities and coordination patterns

---

## Your Agent Journey 🚀

**Week 1: Natural Usage**
Start with natural language descriptions. Notice which agents activate and why. Build intuition for keyword patterns without overthinking the process.

**Week 2-3: Pattern Recognition**  
Observe agent coordination patterns. Understand how complexity and domain keywords influence agent selection. Begin optimizing request phrasing for better coordination.

**Month 2+: Expert Coordination**
Master multi-domain requests that trigger optimal agent combinations. Leverage troubleshooting techniques for effective agent selection. Use advanced patterns for complex workflows.

**The SuperClaude Advantage:**
Experience the power of 14 specialized AI experts working in coordinated response, all through simple, natural language requests. No configuration, no management, just intelligent collaboration that scales with your needs.

🎯 **Ready to experience intelligent agent coordination? Start with `/sc:implement` and discover the magic of specialized AI collaboration.**
