# SuperClaude 動作モードガイド 🧠

## ✅ クイック検証
`/sc:` コマンドを使用してモードをテストします - タスクの複雑さに基づいて自動的に活性化されます。完全なコマンドリファレンスについては、[コマンドガイド](commands.md)を参照してください。

## クイックリファレンステーブル

| モード | 目的 | 自動トリガー | 主要動作 | 最適用途 |
|------|---------|---------------|---------------|---------------|
| **🧠 ブレインストーミング** | インタラクティブ発見 | "brainstorm", "maybe", 曖昧な要求 | ソクラテス式質問、要件引き出し | 新プロジェクト計画、不明確な要件 |
| **🔍 内省** | メタ認知分析 | エラー回復、"推論分析" | 透明思考マーカー (🤔, 🎯, 💡) | デバッグ、学習、最適化 |
| **📋 タスク管理** | 複雑調整 | 3ステップ以上、2ディレクトリ以上 | フェーズ分解、メモリ永続化 | マルチステップ操作、プロジェクト管理 |
| **🎯 オーケストレーション** | インテリジェントツール選択 | マルチツール操作、高リソース使用 | 最適ツールルーティング、並列実行 | 複雑分析、パフォーマンス最適化 |
| **⚡ トークン効率** | 圧縮コミュニケーション | 高コンテキスト使用、`--uc`フラグ | シンボルシステム、推定30-50%トークン削減 | リソース制約、大規模操作 |


---

## はじめに（2分概要）

**モードは動作指示により活性化** - Claude Codeはコンテキストファイルを読み取り、タスクパターンと複雑さに基づいてどのモード動作を採用するかを決定します。

**クイック例:**
```bash
# 自動活性化の例
/sc:brainstorm "モバイルアプリ"        # → ソクラテス式発見質問
/sc:implement "認証システム"        # → マルチフェーズ連携  
"--uc analyze 大規模コードベース/"     # → 圧縮されたシンボル出力
```

**手動フラグを使用する場合:**
- 特定動作が必要: `--brainstorm`, `--introspect`, `--uc`
- 学習/デバッグのための自動検出を上書き
- 特定制約の最適化（メモリ、時間、明確性）

---

## Mode Details

### 🧠 ブレインストーミングモード - インタラクティブ発見

**目的**: 協力的な発見を通じて曖昧なアイデアを構造化された要件に変換します。

**自動活性化トリガー:**
- 曖昧なプロジェクトリクエスト: "作りたい...", "作成を考えている..."
- 探索キーワード: brainstorm, explore, discuss, figure out, よくわからない
- 不確実性指標: "たぶん", "おそらく", "できるでしょうか"
- 手動フラグ: `--brainstorm`, `--bs`

**行動変化:**
- **ソクラテス式質問**: 隠された要件を明らかにするための調査質問を行う
- **非推定アプローチ**: 推測を避け、発見の方向をユーザーに導かせる
- **協力的パートナーシップ**: 指示的コンサルティングではなく、探索で協力する
- **要件統合**: 洞察を構造化された技術ブリーフに変換する
- **クロスセッションメモリ**: フォローアップ討論のための発見コンテキストを維持する

**体験例:**
```
標準アプローチ: "JWTトークンでユーザー認証システムを構築します..."
ブレインストーミングアプローチ: 
"🤔 一緒に探索してみましょう:
 - 認証がアプリのために解決する具体的なユーザー問題は何ですか？
 - ユーザーは誰で、技術的な使いやすさのレベルはどうですか？  
 - 統合する既存システムやソーシャルログインはありますか？
 - どのようなセキュリティ/コンプライアンス要件がありますか？
 📝 結果: 実装準備ができた詳細な認証要件ブリーフ"
```

#### 成功基準  
- [ ] 即座の解決策ではなく質問で応答する
- [ ] 質問がユーザーのニーズ、技術制約、ビジネス目標を探索する
- [ ] 発見プロセス全体を通して協力的なトーンを維持する
- [ ] 結果として構造化された要件や技術ブリーフを作成する

**検証:** `/sc:brainstorm "Webアプリ"` でユーザー、機能、技術について質問すること  
**テスト:** 曖昧なリクエストは推測ではなく発見質問をトリガーすること  
**チェック:** 同じ会話内でのフォローアップ質問全体でモードが持続すること

**最適な組み合わせ:**
- **→ タスク管理**: 要件発見 → 体系的な実装計画
- **→ オーケストレーション**: 要件の明確化 → 実装のための最適ツール選択
- **手動オーバーライド**: "明確な"要件に対しても発見を強制するには `--brainstorm` を使用

---

### 🔍 Introspection Mode - Meta-Cognitive Analysis

**Purpose**: Expose reasoning process for learning optimization and transparent decision-making.

**Auto-Activation Triggers:**
- Self-analysis requests: "analyze my reasoning", "reflect on decision"
- Error recovery scenarios and unexpected results requiring investigation
- Complex problem solving with multiple viable approaches
- Pattern recognition needs for optimization opportunities
- Manual flag: `--introspect`

**Behavioral Changes:**
- **Reasoning Transparency**: Exposes thinking process with clear markers (🤔, 🎯, ⚡, 📊, 💡)
- **Decision Analysis**: Evaluates choice logic and considers alternative approaches
- **Pattern Recognition**: Identifies recurring behaviors and improvement opportunities
- **Meta-Learning**: Extracts insights for continuous framework improvement
- **Framework Compliance**: Validates actions against SuperClaude principles and quality gates

**Example Experience:**
```
Standard Approach: "I'll analyze this code structure and suggest improvements..."
Introspective Approach:
"🧠 Meta-Analysis: Why did I choose structural analysis over functional flow?
 🎯 Decision Logic: Saw class hierarchy → assumed OOP pattern dominance
 🔄 Alternative Considered: Data flow analysis might reveal hidden dependencies
 📊 Evidence Check: File imports suggest functional composition, not OOP
 💡 Learning: Need to analyze imports before choosing analysis strategy
 ⚡ Correction: Switching to functional flow analysis approach"
```

**Works Best With:**
- **→ Task Management**: Provides transparent reasoning for complex phase decisions
- **Any Mode**: Adds reasoning transparency layer to any other mode's operation
- **Manual Override**: Use `--introspect` for learning sessions and debugging workflows

---

### 📋 Task Management Mode - Complex Coordination

**Purpose**: Hierarchical task organization with session persistence for multi-step operations.

**Auto-Activation Triggers:**
- Operations requiring >3 coordinated steps
- Multiple file/directory scope (>2 directories OR >3 files)
- Complex dependencies requiring phases and checkpoints
- Quality improvement requests: polish, refine, enhance
- Manual flags: `--task-manage`, `--delegate`

**Behavioral Changes:**
- **Hierarchical Planning**: Breaks complex work into Plan → Phase → Task → Todo structure
- **Session Persistence**: Maintains project context and progress across interruptions
- **Memory Integration**: Uses write_memory/read_memory for state preservation
- **Progress Orchestration**: Coordinates TodoWrite with memory updates for tracking
- **Quality Gates**: Implements systematic validation checkpoints between phases

**Example Experience:**
```
Standard Approach: "I'll implement user authentication..." → Direct implementation
Task Management Approach:
"📋 Multi-Phase Implementation Plan:
 🎯 Phase 1: Security Requirements Analysis (Session 1)
 🎯 Phase 2: API Design & Documentation (Session 2)  
 🎯 Phase 3: Implementation & Testing (Session 3-4)
 🎯 Phase 4: Integration & Validation (Session 5)
 💾 Session persistence: Resume context automatically
 ✓ Quality gates: Validation before each phase transition"
```

**Works Best With:**
- **Brainstorming →**: Requirements discovery then systematic implementation
- **+ Orchestration**: Task coordination with optimal tool selection
- **+ Introspection**: Transparent reasoning for complex phase decisions

---

### 🎯 Orchestration Mode - Intelligent Tool Selection

**Purpose**: Optimize task execution through intelligent tool routing and parallel coordination.

**Auto-Activation Triggers:**
- Multi-tool operations requiring sophisticated coordination
- Performance constraints (high resource usage)
- Parallel execution opportunities (>3 independent files/operations)
- Complex routing decisions with multiple valid tool approaches

**Behavioral Changes:**
- **Intelligent Tool Routing**: Selects optimal MCP servers and native tools for each task type
- **Resource Awareness**: Adapts approach based on system constraints and availability
- **Parallel Optimization**: Identifies independent operations for concurrent execution
- **Coordination Focus**: Optimizes tool selection and usage through coordinated execution
- **Adaptive Fallback**: Switches tools gracefully when preferred options are unavailable

**Example Experience:**
```
Standard Approach: Sequential file-by-file analysis and editing
Orchestration Approach:
"🎯 Multi-Tool Coordination Strategy:
 🔍 Phase 1: Serena (semantic analysis) + Sequential (architecture review)
 ⚡ Phase 2: Morphllm (pattern edits) + Magic (UI components) 
 🧪 Phase 3: Playwright (testing) + Context7 (documentation patterns)
 🔄 Parallel execution: 3 tools working simultaneously
\"
```

**Works Best With:**
- **Task Management →**: Provides tool coordination for complex multi-phase plans
- **+ Token Efficiency**: Optimal tool selection with compressed communication
- **Any Complex Task**: Adds intelligent tool routing to enhance execution

---

### ⚡ Token Efficiency Mode - Compressed Communication

**Purpose**: Achieve estimated 30-50% token reduction through symbol systems while preserving information quality.

**Auto-Activation Triggers:**
- High context usage approaching limits
- Large-scale operations requiring resource efficiency
- User explicit flags: `--uc`, `--ultracompressed`
- Complex analysis workflows with multiple outputs

**Behavioral Changes:**
- **Symbol Communication**: Uses visual symbols for logic flows, status, and technical domains
- **Technical Abbreviation**: Context-aware compression for repeated technical terms
- **Structured Density**: Bullet points, tables, and concise formatting over verbose paragraphs
- **Information Preservation**: Maintains ≥95% information quality despite compression
- **Structured Format**: Organized for clarity and task completion

**Example Experience:**
```
Standard Approach: "The authentication system implementation shows a security vulnerability in the user validation function that needs immediate attention..."
Token Efficient Approach:
"🛡️ Security Alert:
 auth.js:45 → user val() → critical vuln
 📊 Impact: ❌ token bypass possible
 ⚡ Action: fix validation + audit ∵ high sev
 🔧 Est: 2h impl + 1h test"
```

**Works Best With:**
- **Any Mode**: Adds compression layer while preserving mode-specific behaviors
- **Orchestration →**: Compressed tool coordination and status updates
- **Manual Override**: Use `--uc` when context pressure or efficiency is priority

---

### 🎨 Standard Mode - Balanced Default

**Purpose**: Provide clear, professional communication for straightforward development tasks.

**Auto-Activation Triggers:**
- Simple, well-defined tasks without complexity indicators
- Single-file operations with clear requirements
- Basic explanations and standard development workflows
- No other mode triggers detected (default fallback)

**Behavioral Changes:**
- **Professional Communication**: Clear, concise technical language without compression
- **Moderate Detail**: Balanced information depth suitable for most development tasks
- **Standard Tool Selection**: Uses native Claude capabilities and basic tools
- **Quality Focus**: Maintains code quality without complex orchestration overhead
- **Responsive Adaptation**: Ready to switch to specialized modes when complexity increases

**Example Experience:**
```
Standard Approach: Consistent, professional baseline for all tasks
"I'll implement the login function with proper error handling:
 
 1. Validate user input (email format, password requirements)
 2. Authenticate against database with secure hashing
 3. Generate JWT token with appropriate expiration
 4. Return success response with user data
 
 The implementation will follow security best practices and include comprehensive error handling."
```

**Works Best With:**
- **→ Any Mode**: Serves as baseline that other modes enhance
- **Mode Switching**: Automatically escalates to specialized modes when needed
- **Clarity Priority**: When straightforward communication is more important than optimization

---

## Advanced Usage

### Mode Combinations

**Multi-Mode Workflows:**
```bash
# Discovery → Planning → Implementation
/sc:brainstorm "microservices architecture" --task-manage
# → Brainstorming: requirement discovery
# → Task Management: multi-phase coordination

# Analysis with transparency and efficiency
/sc:analyze legacy-system/ --introspect --uc
# → Introspection: transparent reasoning
# → Token Efficiency: compressed output
```

### Manual Mode Control

**Force Specific Behaviors:**
- `--brainstorm`: Force collaborative discovery for any task
- `--introspect`: Add reasoning transparency to any mode
- `--task-manage`: Enable hierarchical coordination
- `--orchestrate`: Optimize tool selection and parallel execution
- `--uc`: Compress communication for efficiency

**Override Examples:**
```bash
# Force brainstorming on "clear" requirements
/sc:implement "user login" --brainstorm

# Add reasoning transparency to debugging
/sc:fix auth-issue --introspect

# Enable task management for simple operations
/sc:update styles.css --task-manage
```

### Mode Boundaries and Priority

**When Modes Activate:**
1. **Complexity Threshold**: >3 files → Task Management
2. **Resource Pressure**: High context usage → Token Efficiency  
3. **Multi-Tool Need**: Complex analysis → Orchestration
4. **Uncertainty**: Vague requirements → Brainstorming
5. **Error Recovery**: Problems → Introspection

**Priority Rules:**
- **Safety First**: Quality and validation always override efficiency
- **User Intent**: Manual flags override automatic detection
- **Context Adaptation**: Modes stack based on complexity
- **Resource Management**: Efficiency modes activate under pressure

---

## Real-World Examples

### Complete Workflow Examples

**New Project Development:**
```bash
# Phase 1: Discovery (Brainstorming Mode auto-activates)
"I want to build a productivity app"
→ 🤔 Socratic questions about users, features, platform choice
→ 📝 Structured requirements brief

# Phase 2: Planning (Task Management Mode auto-activates)  
/sc:implement "core productivity features"
→ 📋 Multi-phase breakdown with dependencies
→ 🎯 Phase coordination with quality gates

# Phase 3: Implementation (Orchestration Mode coordinates tools)
/sc:develop frontend + backend
→ 🎯 Magic (UI) + Context7 (patterns) + Sequential (architecture)
→ ⚡ Parallel execution optimization
```

**Debugging Complex Issues:**
```bash
# Problem analysis (Introspection Mode auto-activates)
"Users getting intermittent auth failures"
→ 🤔 Transparent reasoning about potential causes
→ 🎯 Hypothesis formation and evidence gathering
→ 💡 Pattern recognition across similar issues

# Systematic resolution (Task Management coordinates)
/sc:fix auth-system --comprehensive
→ 📋 Phase 1: Root cause analysis
→ 📋 Phase 2: Solution implementation  
→ 📋 Phase 3: Testing and validation
```

### Mode Combination Patterns

**High-Complexity Scenarios:**
```bash
# Large refactoring with multiple constraints
/sc:modernize legacy-system/ --introspect --uc --orchestrate
→ 🔍 Transparent reasoning (Introspection)
→ ⚡ Compressed communication (Token Efficiency)  
→ 🎯 Optimal tool coordination (Orchestration)
→ 📋 Systematic phases (Task Management auto-activates)
```

---

## Quick Reference

### Mode Activation Patterns

| Trigger Type | Example Input | Mode Activated | Key Behavior |
|--------------|---------------|----------------|--------------|
| **Vague Request** | "I want to build an app" | 🧠 Brainstorming | Socratic discovery questions |
| **Complex Scope** | >3 files or >2 directories | 📋 Task Management | Phase coordination |
| **Multi-Tool Need** | Analysis + Implementation | 🎯 Orchestration | Tool optimization |
| **Error Recovery** | "This isn't working as expected" | 🔍 Introspection | Transparent reasoning |
| **Resource Pressure** | High context usage | ⚡ Token Efficiency | Symbol compression |
| **Simple Task** | "Fix this function" | 🎨 Standard | Clear, direct approach |

### Manual Override Commands

```bash
# Force specific mode behaviors
/sc:command --brainstorm    # Collaborative discovery
/sc:command --introspect    # Reasoning transparency
/sc:command --task-manage   # Hierarchical coordination
/sc:command --orchestrate   # Tool optimization
/sc:command --uc           # Token compression

# Combine multiple modes
/sc:command --introspect --uc    # Transparent + efficient
/sc:command --task-manage --orchestrate  # Coordinated + optimized
```

---

## Troubleshooting

For troubleshooting help, see:
- [Common Issues](../Reference/common-issues.md) - Quick fixes for frequent problems
- [Troubleshooting Guide](../Reference/troubleshooting.md) - Comprehensive problem resolution

### Common Issues
- **Mode not activating**: Use manual flags: `--brainstorm`, `--introspect`, `--uc`
- **Wrong mode active**: Check complexity triggers and keywords in request
- **Mode switching unexpectedly**: Normal behavior based on task evolution
- **Execution impact**: Modes optimize tool usage, shouldn't affect execution
- **Mode conflicts**: Check flag priority rules in [Flags Guide](flags.md)

### Immediate Fixes
- **Force specific mode**: Use explicit flags like `--brainstorm` or `--task-manage`
- **Reset mode behavior**: Restart Claude Code session to reset mode state
- **Check mode indicators**: Look for 🤔, 🎯, 📋 symbols in responses
- **Verify complexity**: Simple tasks use Standard mode, complex tasks auto-switch

### Mode-Specific Troubleshooting

**Brainstorming Mode Issues:**
```bash
# Problem: Mode gives solutions instead of asking questions
# Quick Fix: Check request clarity and use explicit flag
/sc:brainstorm "web app" --brainstorm         # Force discovery mode
"I have a vague idea about..."                # Use uncertainty language
"Maybe we could build..."                     # Trigger exploration
```

**Task Management Mode Issues:**
```bash
# Problem: Simple tasks getting complex coordination
# Quick Fix: Reduce scope or use simpler commands
/sc:implement "function" --no-task-manage     # Disable coordination
/sc:simple-fix bug.js                         # Use basic commands
# Check if task really is complex (>3 files, >2 directories)
```

**Token Efficiency Mode Issues:**
```bash
# Problem: Output too compressed or unclear
# Quick Fix: Disable compression for clarity
/sc:command --no-uc                           # Disable compression
/sc:command --verbose                         # Force detailed output
# Use when clarity is more important than efficiency
```

**Introspection Mode Issues:**
```bash
# Problem: Too much meta-commentary, not enough action
# Quick Fix: Disable introspection for direct work
/sc:command --no-introspect                   # Direct execution
# Use introspection only for learning and debugging
```

**Orchestration Mode Issues:**
```bash
# Problem: Tool coordination causing confusion
# Quick Fix: Simplify tool usage
/sc:command --no-mcp                          # Native tools only
/sc:command --simple                          # Basic execution
# Check if task complexity justifies orchestration
```

### Error Code Reference

| Mode Error | Meaning | Quick Fix |
|------------|---------|-----------|
| **B001** | Brainstorming failed to activate | Use explicit `--brainstorm` flag |
| **T001** | Task management overhead | Use `--no-task-manage` for simple tasks |
| **U001** | Token efficiency too aggressive | Use `--verbose` or `--no-uc` |
| **I001** | Introspection mode stuck | Use `--no-introspect` for direct action |
| **O001** | Orchestration coordination failed | Use `--no-mcp` or `--simple` |
| **M001** | Mode conflict detected | Check flag priority rules |
| **M002** | Mode switching loop | Restart session to reset state |
| **M003** | Mode not recognized | Update SuperClaude or check spelling |

### Progressive Support Levels

**Level 1: Quick Fix (< 2 min)**
- Use manual flags to override automatic mode selection
- Check if task complexity matches expected mode behavior
- Try restarting Claude Code session

**Level 2: Detailed Help (5-15 min)**
```bash
# Mode-specific diagnostics
/sc:help modes                            # List all available modes
/sc:reflect --type mode-status            # Check current mode state
# Review request complexity and triggers
```
- See [Common Issues Guide](../Reference/common-issues.md) for mode installation problems

**Level 3: Expert Support (30+ min)**
```bash
# Deep mode analysis
SuperClaude install --diagnose
# Check mode activation patterns
# Review behavioral triggers and thresholds
```
- See [Diagnostic Reference Guide](../Reference/diagnostic-reference.md) for behavioral mode analysis

**Level 4: Community Support**
- Report mode issues at [GitHub Issues](https://github.com/SuperClaude-Org/SuperClaude_Framework/issues)
- Include examples of unexpected mode behavior
- Describe desired vs actual mode activation

### Success Validation

After applying mode fixes, test with:
- [ ] Simple requests use Standard mode (clear, direct responses)
- [ ] Complex requests auto-activate appropriate modes (coordination, reasoning)
- [ ] Manual flags override automatic detection correctly
- [ ] Mode indicators (🤔, 🎯, 📋) appear when expected
- [ ] Performance remains good across different modes

## Quick Troubleshooting (Legacy)
- **Mode not activating** → Use manual flags: `--brainstorm`, `--introspect`, `--uc`
- **Wrong mode active** → Check complexity triggers and keywords in request
- **Mode switching unexpectedly** → Normal behavior based on task evolution  
- **Execution impact** → Modes optimize tool usage, shouldn't affect execution
- **Mode conflicts** → Check flag priority rules in [Flags Guide](flags.md)

## Frequently Asked Questions

**Q: How do I know which mode is active?**
A: Look for these indicators in communication patterns:
- 🤔 Discovery questions → Brainstorming
- 🎯 Reasoning transparency → Introspection  
- Phase breakdowns → Task Management
- Tool coordination → Orchestration
- Symbol compression → Token Efficiency

**Q: Can I force specific modes?**
A: Yes, use manual flags to override automatic detection:
```bash
/sc:command --brainstorm     # Force discovery
/sc:command --introspect     # Add transparency
/sc:command --task-manage    # Enable coordination
/sc:command --uc            # Compress output
```

**Q: Do modes affect execution?**
A: Modes optimize tool usage through coordination:
- **Token Efficiency**: 30-50% context reduction
- **Orchestration**: Parallel processing
- **Task Management**: Prevents rework through systematic planning

**Q: Can modes work together?**
A: Yes, modes are designed to complement each other:
- **Task Management** coordinates other modes
- **Token Efficiency** compresses any mode's output
- **Introspection** adds transparency to any workflow

---

## Summary

SuperClaude's 5 behavioral modes create an **intelligent adaptation system** that matches your needs automatically:

- **🧠 Brainstorming**: Transforms vague ideas into clear requirements
- **🔍 Introspection**: Provides transparent reasoning for learning and debugging
- **📋 Task Management**: Coordinates complex multi-step operations
- **🎯 Orchestration**: Optimizes tool selection and parallel execution
- **⚡ Token Efficiency**: Compresses communication while preserving clarity
- **🎨 Standard**: Maintains professional baseline for straightforward tasks

**The key insight**: You don't need to think about modes - they work transparently to enhance your development experience. Simply describe what you want to accomplish, and SuperClaude automatically adapts its approach to match your needs.

---

## 関連ガイド

**学習の進行:**

**🌱 基本 (第1週)**
- [クイックスタートガイド](../Getting-Started/quick-start.md) - モード活性化の例
- [コマンドリファレンス](commands.md) - コマンドが自動的にモードを活性化
- [インストールガイド](../Getting-Started/installation.md) - 行動モードのセットアップ

**🌿 中級 (第2-3週)**  
- [エージェントガイド](agents.md) - モードが専門家とどう連携するか
- [フラグガイド](flags.md) - 手動モード制御と最適化
- [例のクックブック](../Reference/examples-cookbook.md) - 実践でのモードパターン

**🌲 上級 (2ヶ月目以降)**
- [MCPサーバー](mcp-servers.md) - 強化機能とのモード統合
- [セッション管理](session-management.md) - タスク管理モードのワークフロー  
- [はじめに](../Getting-Started/quick-start.md) - モード使用パターン

**🔧 エキスパート**
- [技術アーキテクチャ](../Developer-Guide/technical-architecture.md) - モード実装の詳細
- [コード貢献](../Developer-Guide/contributing-code.md) - モード機能の拡張

**モード固有のガイド:**
- **ブレインストーミング**: [要件発見パターン](../Reference/examples-cookbook.md#requirements)
- **タスク管理**: [セッション管理ガイド](session-management.md)
- **オーケストレーション**: [MCPサーバーガイド](mcp-servers.md)
- **トークン効率**: [コマンド基礎](commands.md#token-efficiency)
