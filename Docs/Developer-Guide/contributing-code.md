# SuperClaude Frameworkへのコンテキストファイル貢献 🛠️

SuperClaude Framework開発へようこそ！このガイドでは、構造化プロンプトとMCPサーバー統合を通じてClaude Codeを強化するコンテキストファイルと動作指示の貢献に必要なすべてを提供します。

**プロジェクト目的**: SuperClaudeは構造化コンテキストファイルと動作指示をClaude Codeに提供します。インテリジェントプロンプトエンジニアリングを通じて次世代のAI支援開発を構築しています。

## 目次

1. [開発セットアップ](#開発セットアップ) - 前提条件と環境
2. [アーキテクチャ概要](#アーキテクチャ概要) - システムコンポーネントと設計  
3. [コンテキストファイルガイドライン](#コンテキストファイルガイドライン) - 標準と慣行
4. [開発ワークフロー](#開発ワークフロー) - Gitワークフローと提出
5. [コンポーネントへの貢献](#コンポーネントへの貢献) - エージェント、コマンド、モード
6. [ファイル検証](#ファイル検証) - 品質保証
7. [ヘルプの取得](#ヘルプの取得) - サポートとリソース

## 開発セットアップ

### 前提条件

**必須:**
- Python 3.8+ with pip
- バージョン管理用Git
- Claude Codeがインストールされ動作中
- Node.js 16+ (MCPサーバー設定用)

**環境セットアップ:**
```bash
# 最初にGitHubでSuperClaude_Frameworkをフォーク
git clone https://github.com/YOUR_USERNAME/SuperClaude_Framework.git
cd SuperClaude_Framework

# インストールシステムをテスト
PYTHONPATH=/path/to/SuperClaude_Framework python3 -m setup --help

# 開発場所にインストール
PYTHONPATH=/path/to/SuperClaude_Framework python3 -m setup install --components core
```

**検証チェック:**
```bash
# Pythonバージョンを確認
python3 --version  # 3.8+である必要があります

# MCP設定用Node.jsをチェック
node --version     # 16+である必要があります

# Claude Code統合をテスト
ls ~/.claude/      # Claude Codeディレクトリが表示される必要があります
```

## アーキテクチャ概要

### フレームワーク構造

SuperClaudeは**コンテキスト指向設定フレームワーク**です - 実行ソフトウェアではなく、Claude Codeが読み取って動作を変更する指示ファイルです。

```
SuperClaude_Framework/
├── SuperClaude/           # Framework components (the source of truth)
│   ├── Core/             # PRINCIPLES.md, RULES.md, FLAGS.md
│   ├── Agents/           # 15 specialized domain experts
│   ├── Commands/         # 21 context trigger patterns (/sc: behavioral instructions)
│   ├── Modes/            # 6 behavioral modification patterns
│   └── MCP/              # 6 MCP server configurations
├── setup/                # Python installation system
├── Docs/                 # Documentation (what you're reading)
└── tests/                # File validation scripts
```

**Key Concepts:**
- **Context Files**: .md instruction files that guide Claude Code behavior
- **Agents**: Domain specialists (e.g., security-engineer.md, python-expert.md)  
- **Commands**: Workflow patterns (e.g., implement.md, analyze.md)
- **Modes**: Interaction modifiers (e.g., brainstorming, introspection)
- **MCP Integration**: Configuration for Model Context Protocol servers

### How It Works

```
User Input → Claude Code → Reads SuperClaude Context → Modified Behavior → Enhanced Output
```

1. User types `/sc:implement "auth system"` **in Claude Code conversation** (not terminal)
2. Claude Code reads `SuperClaude/Commands/implement.md`
3. Command activates security-engineer agent context
4. Context7 MCP provides authentication patterns
5. Claude generates complete, secure implementation

## Context File Guidelines

### File Organization

**Context Files (`.md`):**
- Write clear, actionable instructions for Claude Code
- Use frontmatter metadata for configuration  
- Follow existing patterns and naming conventions
- Test instructions produce expected behaviors

**Installation Scripts (`.py`):**
- Follow PEP 8 style guidelines
- Include docstrings for functions and classes
- Add type hints where beneficial
- Focus on file copying and configuration

**Example Agent Structure:**
```markdown
---
name: new-specialist
description: Brief description of expertise
category: specialized|architecture|quality
tools: Read, Write, Edit, Bash, Grep
---

# Agent Name

## Triggers
- Keywords that activate this agent
- File types that trigger activation

## Behavioral Mindset
Core philosophy and approach

## Focus Areas
- Domain expertise area 1
- Domain expertise area 2

## Key Actions
1. Specific behavior pattern
2. Problem-solving approach
```

### Context File Standards

**Structure Requirements:**
- Clear, actionable instructions for Claude Code
- Specific triggers and activation patterns
- Examples demonstrating usage
- Boundaries defining scope

**Quality Standards:**
- Instructions are testable in Claude Code conversations
- Examples produce expected behavioral changes
- Clear activation triggers and context patterns
- Professional language and formatting

## Development Workflow

### Git Workflow

1. **Fork and Clone:**
   ```bash
   # Fork on GitHub, then:
   git clone https://github.com/YOUR_USERNAME/SuperClaude_Framework.git
   cd SuperClaude_Framework
   git remote add upstream https://github.com/SuperClaude-Org/SuperClaude_Framework.git
   ```

2. **Create Feature Branch:**
   ```bash
   git checkout -b feature/your-feature-name
   # Work on your changes
   git add .
   git commit -m "Add: descriptive commit message"
   ```

3. **Submit Pull Request:**
   ```bash
   git push origin feature/your-feature-name
   # Create PR on GitHub
   ```

### Pull Request Template

```markdown
## Description
Brief description of context file changes

## Type of Change
- [ ] Bug fix in context files
- [ ] New feature (agent, command, mode)
- [ ] Documentation improvement
- [ ] Installation system enhancement

## Testing
- [ ] Manual testing with Claude Code
- [ ] Context file validation passes
- [ ] Examples validated in Claude Code conversations

## Checklist
- [ ] Files follow SuperClaude conventions
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] No breaking changes to existing context
```

### Code Review Process

**Manual Review:**
- Context file clarity and effectiveness
- Agent/command logic and triggers  
- Documentation accuracy and completeness
- Integration with existing components
- Claude Code behavioral testing results

## Contributing to Components

### Adding New Agents

**Agent Development Process:**
1. Identify domain expertise gap
2. Create agent file in `SuperClaude/Agents/`
3. Define triggers, behaviors, and boundaries
4. Test with various Claude Code scenarios
5. Document usage patterns and examples

**Agent Template:**
```markdown
---
name: agent-name
description: Domain expertise description
category: specialized
tools: Read, Write, Edit, Bash
---

# Agent Name

## Triggers
- Specific keywords: domain, expertise, area
- File patterns: *.domain, specific frameworks
- Complexity indicators: architectural decisions

## Behavioral Mindset
- Focus on domain best practices
- Systematic approach to problem-solving
- Quality and security considerations

## Focus Areas
- Core domain expertise
- Related technical areas
- Integration patterns

## Key Actions
1. Analyze requirements within domain context
2. Apply domain-specific best practices
3. Coordinate with related specialists
4. Validate solutions meet domain standards
```

### Adding New Commands

**Command Structure:**
```markdown
---
name: command-name
description: Command purpose
category: workflow|utility|analysis
complexity: basic|standard|advanced
mcp-servers: [context7, sequential]
personas: [architect, engineer]
---

# /sc:command-name

## Triggers
- When to use this command
- Context indicators

## Usage
Type in Claude Code conversation:
```
/sc:command-name [target] [--options]
```
**Note**: This is a context trigger pattern, not a terminal command.

## Workflow Pattern
1. Initial analysis
2. Processing steps  
3. Validation and output

## Examples
Practical usage examples
```

### Adding New Modes

**Mode Development:**
- Define activation triggers
- Specify behavioral modifications
- Create interaction patterns
- Test across different Claude Code scenarios

## File Validation

### Context File Validation

**Manual Validation Process:**
1. Install development version in Claude Code
2. Test agent/command activation triggers in Claude Code conversations
3. Verify behavioral modifications occur as expected
4. Validate context file structure and formatting
5. Test edge cases and error conditions

**Validation Checklist:**
- [ ] Context files use valid markdown syntax
- [ ] Triggers activate correctly in Claude Code
- [ ] Behavior matches documentation
- [ ] No conflicts with existing components
- [ ] Examples produce expected results in Claude Code conversations

### File Structure Validation

```bash
# Check file structure
find ~/.claude -name "*.md" | head -10

# Verify context file format
head ~/.claude/agents/python-expert.md

# Test import system
grep "@import" ~/.claude/CLAUDE.md
```

## Getting Help

### Development Support

**Documentation:**
- [Technical Architecture](technical-architecture.md) - System design details  
- [Verification Guide](testing-debugging.md) - File validation procedures

**Community Channels:**
- GitHub Issues: Bug reports and feature requests
- GitHub Discussions: Development questions and ideas
- Pull Request Reviews: Context file feedback and collaboration

**Code Review Guidelines:**
- Provide constructive, specific feedback
- Test changes locally when possible
- Focus on maintainability and clarity
- Respect contributor efforts and learning

### Issue Reporting

**Bug Reports:**
1. Describe expected vs actual behavior in Claude Code
2. Provide steps to reproduce with context triggers
3. Include environment details and file versions
4. Share relevant context file configurations

**Feature Requests:**
1. Explain the behavioral enhancement being proposed
2. Describe how users would benefit
3. Consider integration with existing context patterns
4. Provide usage examples

## Contributing Guidelines Summary

### Do's
✅ **Follow existing patterns and conventions**
✅ **Test context files thoroughly with Claude Code**
✅ **Write clear, actionable behavioral instructions**  
✅ **Provide working examples**
✅ **Focus on user experience improvements**
✅ **Coordinate with related components**

### Don'ts
❌ **Don't break existing functionality**
❌ **Don't add untested context modifications**
❌ **Don't ignore style guidelines**
❌ **Don't create overly complex behavioral patterns**
❌ **Don't duplicate existing functionality**

### Quality Standards

**Context Files:**
- Clear activation triggers
- Specific behavioral instructions
- Practical examples
- Defined scope boundaries

**Documentation:**
- Accurate and up-to-date
- Working context examples
- Clear navigation structure
- Accessibility considerations

## License and Attribution

**MIT License**: SuperClaude Framework is licensed under the MIT License, providing maximum freedom for use, modification, and distribution.

By contributing to SuperClaude Framework, you agree that your contributions will be licensed under the same MIT License. You retain copyright to your contributions while granting the project perpetual rights to use, modify, and distribute your context files.

## Acknowledgments

SuperClaude Framework exists because of the collaborative effort of developers, users, and contributors who believe in advancing AI-assisted development. Every bug report, feature suggestion, documentation improvement, and context file contribution makes the framework better for everyone.

Your expertise and perspective make SuperClaude Framework better. Whether you're improving context files, adding features, or helping other users, every contribution advances the goal of more effective AI-assisted development.

---

**Welcome to the SuperClaude Framework contributor community!** Your contributions help build the future of AI-assisted development through intelligent context and behavioral programming.
