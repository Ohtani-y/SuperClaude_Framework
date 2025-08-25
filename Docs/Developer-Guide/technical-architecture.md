# SuperClaude コンテキストアーキテクチャガイド

## 概要

このガイドは、SuperClaudeのコンテキスト指向設定フレームワークがどのように構造化され、Claude Codeがこれらのコンテキストファイルをどのように解釈して動作を変更するかを文書化します。

**重要**: SuperClaudeは実行プロセス、実行レイヤー、またはパフォーマンスシステムを持つスタンドアロンソフトウェアではありません。Claude Codeが読み取って専門的な動作を採用する`.md`命令ファイルのコレクションです。

## 目次

1. [コンテキストファイルアーキテクチャ](#context-file-architecture)
2. [インポートシステム](#the-import-system)
3. [エージェントコンテキスト構造](#agent-context-structure)
4. [コマンドコンテキスト構造](#command-context-structure)
5. [モードコンテキスト構造](#mode-context-structure)
6. [MCPサーバー設定](#mcp-server-configuration)
7. [Claude Codeがコンテキストを読み取る方法](#how-claude-code-reads-context)
8. [フレームワークの拡張](#extending-the-framework)

## コンテキストファイルアーキテクチャ

### ディレクトリ構造

```
~/.claude/ (SuperClaude Framework Files Only)
├── CLAUDE.md                       # Main context file with imports
├── FLAGS.md                        # Flag definitions and triggers  
├── RULES.md                        # Core behavioral rules
├── PRINCIPLES.md                   # Guiding principles
├── ZIG.md                          # Zig language integration
├── MCP_Context7.md                 # Context7 MCP integration
├── MCP_Magic.md                    # Magic MCP integration
├── MCP_Morphllm.md                 # Morphllm MCP integration
├── MCP_Playwright.md               # Playwright MCP integration
├── MCP_Sequential.md               # Sequential MCP integration
├── MCP_Serena.md                   # Serena MCP integration
├── MCP_Zig.md                      # Zig MCP integration
├── MODE_Brainstorming.md           # Collaborative discovery mode
├── MODE_Introspection.md           # Transparent reasoning mode
├── MODE_Orchestration.md           # Tool coordination mode
├── MODE_Task_Management.md         # Task orchestration mode
├── MODE_Token_Efficiency.md        # Compressed communication mode
├── agents/                         # Domain specialist contexts (14 total)
│   ├── backend-architect.md        # Backend expertise
│   ├── devops-architect.md         # DevOps expertise
│   ├── frontend-architect.md       # Frontend expertise
│   ├── learning-guide.md           # Educational expertise
│   ├── performance-engineer.md     # Performance expertise
│   ├── python-expert.md            # Python expertise
│   ├── quality-engineer.md         # Quality assurance expertise
│   ├── refactoring-expert.md       # Code quality expertise
│   ├── requirements-analyst.md     # Requirements expertise
│   ├── root-cause-analyst.md       # Problem diagnosis expertise
│   ├── security-engineer.md        # Security expertise
│   ├── socratic-mentor.md          # Educational expertise
│   ├── system-architect.md         # System design expertise
│   └── technical-writer.md         # Documentation expertise
└── commands/                       # Workflow pattern contexts
    └── sc/                         # SuperClaude command namespace (21 total)
        ├── analyze.md              # Analysis patterns
        ├── brainstorm.md           # Discovery patterns
        ├── build.md                # Build patterns
        ├── cleanup.md              # Cleanup patterns
        ├── design.md               # Design patterns
        ├── document.md             # Documentation patterns
        ├── estimate.md             # Estimation patterns
        ├── explain.md              # Explanation patterns
        ├── git.md                  # Git workflow patterns
        ├── implement.md            # Implementation patterns
        ├── improve.md              # Improvement patterns
        ├── index.md                # Index patterns
        ├── load.md                 # Context loading patterns
        ├── reflect.md              # Reflection patterns
        ├── save.md                 # Session persistence patterns
        ├── select-tool.md          # Tool selection patterns
        ├── spawn.md                # Multi-agent patterns
        ├── task.md                 # Task management patterns
        ├── test.md                 # Testing patterns
        ├── troubleshoot.md         # Troubleshooting patterns
        └── workflow.md             # Workflow planning patterns

注意: その他のディレクトリ（backups/、logs/、projects/、serena/など）はClaude Code
運用ディレクトリであり、SuperClaudeフレームワークコンテンツの一部ではありません。
```

### コンテキストファイルタイプ

| ファイルタイプ | 目的 | 活性化 | 例 |
|-----------|---------|------------|---------|
| **コマンド** | ワークフローパターンを定義 | `/sc:[command]` (コンテキストトリガー) | ユーザーが `/sc:implement` と入力 → `implement.md` を読み取り |
| **エージェント** | ドメイン専門知識を提供 | `@agent-[name]` または自動 | `@agent-security` → `security-engineer.md` を読み取り |
| **モード** | インタラクションスタイルを変更 | フラグまたはトリガー | `--brainstorm` → ブレインストーミングモードを活性化 |
| **コア** | 基本ルールを設定 | 常に活性 | `RULES.md` 常に読み込み |

## インポートシステム

### CLAUDE.mdの動作方法

メイン`CLAUDE.md`ファイルは複数のコンテキストファイルを読み込むためのインポートシステムを使用します：

```markdown
# CLAUDE

*MANDATORY*
@FLAGS.md                  # Flag definitions and triggers
@RULES.md                  # Core behavioral rules
@PRINCIPLES.md             # Guiding principles
*SECONDARY*
@MCP_Context7.md           # Context7 MCP integration
@MCP_Magic.md              # Magic MCP integration
@MCP_Morphllm.md           # Morphllm MCP integration
@MCP_Playwright.md         # Playwright MCP integration
@MCP_Sequential.md         # Sequential MCP integration
@MCP_Serena.md             # Serena MCP integration
@MCP_Zig.md                # Zig MCP integration
*CRITICAL*
@MODE_Brainstorming.md     # Collaborative discovery mode
@MODE_Introspection.md     # Transparent reasoning mode
@MODE_Task_Management.md   # Task orchestration mode
@MODE_Orchestration.md     # Tool coordination mode
@MODE_Token_Efficiency.md  # Compressed communication mode
*LANGUAGE SPECIFIC*
@ZIG.md                    # Zig language integration
```

### Import Processing

1. Claude Code reads `CLAUDE.md`
2. Encounters `@import` statements
3. Loads referenced files into context
4. Builds complete behavioral framework
5. Applies relevant contexts based on user input

## Agent Context Structure

### Anatomy of an Agent File

Each agent `.md` file follows this structure:

```markdown
---
name: agent-name
description: Brief description
category: specialized|architecture|quality
tools: Read, Write, Edit, Bash, Grep
---

# Agent Name

## Triggers
- Keywords that activate this agent
- File types that trigger activation
- Complexity thresholds

## Behavioral Mindset
Core philosophy and approach

## Focus Areas
- Domain expertise area 1
- Domain expertise area 2

## Key Actions
1. Specific behavior pattern
2. Problem-solving approach
```

### Agent Activation Logic

- **Manual**: User types `@agent-python-expert "task"`
- **Automatic**: Keywords in request trigger agent loading
- **Contextual**: File types or patterns activate relevant agents

## Command Context Structure

### Anatomy of a Command File

```markdown
---
name: command-name
description: Command purpose
category: utility|orchestration|analysis
complexity: basic|enhanced|advanced
mcp-servers: [context7, sequential]
personas: [architect, engineer]
---

# /sc:command-name

## Triggers
- When to use this command
- Context indicators

## Usage
/sc:command-name [target] [--options]

## Workflow Pattern
1. Step 1: Initial action
2. Step 2: Processing
3. Step 3: Validation

## Examples
Practical usage examples
```

### Command Processing

When user types `/sc:implement "feature"` in Claude Code conversation:
1. Claude reads `commands/sc/implement.md`
2. Adopts implementation workflow pattern
3. May auto-activate related agents
4. Follows defined workflow steps

## Mode Context Structure

### Behavioral Modes

Modes modify Claude's interaction style:

```markdown
# MODE_[Name].md

## Activation Triggers
- Flag: --mode-name
- Keywords: [triggers]
- Complexity: threshold

## Behavioral Modifications
- Communication style changes
- Decision-making adjustments
- Output format modifications

## Interaction Patterns
- How to respond
- What to prioritize
```

## MCP Server Configuration

### Configuration Location

MCP servers are configured in `~/.claude.json` (NOT part of SuperClaude context):

```json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp@latest"]
    },
    "sequential-thinking": {
      "command": "npx",
      "args": ["-y", "sequential-thinking-mcp@latest"]
    }
  }
}
```

### MCP Integration

- **MCP Servers**: Actual software providing tools
- **SuperClaude**: Context that tells Claude when to use them
- **Activation**: Flags or keywords trigger MCP usage

## How Claude Code Reads Context

### Context Loading Sequence

```
User Input (in Claude Code): "/sc:analyze src/ --focus security"
                    ↓
1. Parse Command: identify 'analyze' command
                    ↓
2. Load Context: read commands/sc/analyze.md
                    ↓
3. Check Flags: --focus security
                    ↓
4. Auto-Activation: load security-engineer.md
                    ↓
5. Apply Patterns: follow analysis workflow
                    ↓
6. Generate Output: using loaded contexts
```

### Context Priority

1. **Explicit Commands**: `/sc:` commands take precedence
2. **Manual Agents**: `@agent-` override auto-activation
3. **Flags**: Modify behavior of commands/agents
4. **Auto-Activation**: Based on keywords/context
5. **Default Behavior**: Standard Claude Code

## Extending the Framework

### Adding New Commands

1. Create `~/.claude/commands/sc/new-command.md`
2. Define metadata, triggers, and workflow
3. No code changes needed - just context

### Adding New Agents

1. Create `~/.claude/agents/new-specialist.md`
2. Define expertise, triggers, and behaviors
3. Agent becomes available

### Adding New Modes

1. Create `~/.claude/MODE_NewMode.md`
2. Define activation triggers and modifications
3. Mode activates based on triggers

### Best Practices

- **Keep Context Focused**: One concept per file
- **Clear Triggers**: Define when context activates
- **Workflow Patterns**: Provide step-by-step guidance
- **Examples**: Include practical usage examples
- **Metadata**: Use frontmatter for configuration

## Important Clarifications

### What SuperClaude Is NOT

- ❌ **No Execution Engine**: No code runs, no processes execute
- ❌ **No Performance System**: No optimization possible (it's just text)
- ❌ **No Detection Engine**: Claude Code does pattern matching
- ❌ **No Orchestration Layer**: Context files guide, not control
- ❌ **No Quality Gates**: Just instructional patterns

### What SuperClaude IS

- ✅ **Context Files**: `.md` instructions for Claude Code
- ✅ **Behavioral Patterns**: Workflows and approaches
- ✅ **Domain Expertise**: Specialized knowledge contexts
- ✅ **Configuration**: Settings for actual tools (MCP)
- ✅ **Framework**: Structured prompt engineering

## Summary

SuperClaude's architecture is intentionally simple: it's a well-organized collection of context files that Claude Code reads to modify its behavior. The power comes from the careful crafting of these contexts and their systematic organization, not from any executing code or running processes.

The framework's elegance lies in its simplicity - by providing Claude Code with structured instructions through context files, we can achieve sophisticated behavioral modifications without any software complexity.
