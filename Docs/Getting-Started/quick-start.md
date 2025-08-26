<div align="center">

# 🚀 SuperClaude クイックスタートガイド

### **Claude Code用コンテキストエンジニアリングフレームワーク**

<p align="center">
  <img src="https://img.shields.io/badge/Framework-Context_Engineering-purple?style=for-the-badge" alt="Framework">
  <img src="https://img.shields.io/badge/Version-4.0.8-blue?style=for-the-badge" alt="Version">
  <img src="https://img.shields.io/badge/Time_to_Start-5_Minutes-green?style=for-the-badge" alt="Quick Start">
</p>

> **💡 重要な洞察**: SuperClaudeはClaude Codeを置き換えるのではなく、動作コンテキスト注入を通じて**設定と強化**を行います

<p align="center">
  <a href="#-how-it-works">How It Works</a> •
  <a href="#-instant-start">Instant Start</a> •
  <a href="#-core-components">Components</a> •
  <a href="#-workflow-patterns">Workflows</a> •
  <a href="#-when-to-use">When to Use</a>
</p>

</div>

---

<div align="center">

## 📊 **フレームワーク機能**

| **コマンド** | **AIエージェント** | **動作モード** | **MCPサーバー** |
|:------------:|:-------------:|:-------------------:|:---------------:|
| **21** | **14** | **6** | **6** |
| `/sc:` トリガー | ドメイン専門家 | コンテキスト適応 | ツール統合 |

</div>

---

## 🎯 **動作原理**

<div align="center">

### **フレームワークアーキテクチャフロー**

```
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│  User Input     │────>│   Claude Code    │────>│  Context Files  │
│  /sc:command    │     │  Reads Context   │     │  (.md behaviors)│
└─────────────────┘     └──────────────────┘     └─────────────────┘
                               │                          │
                               ▼                          ▼
┌─────────────────┐      ┌──────────────────┐     ┌─────────────────┐
│   Enhanced      │<─────│    Behavioral    │<────│   MCP Servers   │
│   Response      │      │    Activation    │     │ (if configured) │
└─────────────────┘      └──────────────────┘     └─────────────────┘
```

**魔法**: `/sc:brainstorm`と入力すると、Claudeはインストールされた`.md`ファイルから動作指示を読み取り、強化された機能で応答します

</div>

---

## ⚡ **即座開始**

<div align="center">

### **インストールから最初のコマンドまで5分の旅**

</div>

<table>
<tr>
<th width="50%">📦 ステップ1: インストール（ターミナル）</th>
<th width="50%">💬 ステップ2: 使用（Claude Code）</th>
</tr>
<tr>
<td valign="top">

```bash
# Quick install with pipx
pipx install SuperClaude && SuperClaude install

# Or traditional pip
pip install SuperClaude && SuperClaude install

# Or via npm
npm install -g @bifrost_inc/superclaude && superclaude install
```

</td>
<td valign="top">

```text
# Interactive discovery
/sc:brainstorm "web app for task management"

# Analyze existing code
/sc:analyze src/

# Generate implementation
/sc:implement "user authentication"

# Activate specialist
@agent-security "review auth flow"
```

</td>
</tr>
</table>

<details>
<summary><b>🎥 舞台裏で起こること</b></summary>

1. **コンテキスト読み込み**: Claude Codeが`CLAUDE.md`経由で動作`.md`ファイルをインポート
2. **パターン認識**: `/sc:`と`@agent-`トリガーパターンを認識
3. **動作活性化**: コンテキストファイルから対応する指示を適用
4. **MCP統合**: 利用可能な場合は設定された外部ツールを使用
5. **応答強化**: 包括的応答のためフレームワークパターンに従う

</details>

---

## 🔧 **Core Components**

<div align="center">

### **Four Pillars of SuperClaude**

<table>
<tr>
<td align="center" width="25%">

### 📝 **Commands**
<h2>21</h2>

**Slash Commands**

`/sc:brainstorm`  
`/sc:implement`  
`/sc:analyze`  
`/sc:workflow`

*Workflow automation*

</td>
<td align="center" width="25%">

### 🤖 **Agents**
<h2>14</h2>

**AI Specialists**

`@agent-architect`  
`@agent-security`  
`@agent-frontend`  
`@agent-backend`

*Domain expertise*

</td>
<td align="center" width="25%">

### 🎯 **Modes**
<h2>6</h2>

**Behavioral Modes**

Brainstorming  
Introspection  
Orchestration  
Task Management

*Context adaptation*

</td>
<td align="center" width="25%">

### 🔌 **MCP**
<h2>6</h2>

**Server Integration**

Context7 (docs)  
Sequential (analysis)  
Magic (UI)  
Playwright (testing)

*Enhanced tools*

</td>
</tr>
</table>

</div>

---

## 📚 **Workflow Patterns**

<div align="center">

### **Complete Development Lifecycle**

</div>

### **🌟 First Project Session**

<table>
<tr>
<th>Step</th>
<th>Command</th>
<th>What Happens</th>
</tr>
<tr>
<td><b>1. Discovery</b></td>
<td><code>/sc:brainstorm "e-commerce app"</code></td>
<td>Interactive requirements exploration</td>
</tr>
<tr>
<td><b>2. Load Context</b></td>
<td><code>/sc:load src/</code></td>
<td>Import existing project structure</td>
</tr>
<tr>
<td><b>3. Analysis</b></td>
<td><code>/sc:analyze --focus architecture</code></td>
<td>Deep architectural review</td>
</tr>
<tr>
<td><b>4. Planning</b></td>
<td><code>/sc:workflow "payment integration"</code></td>
<td>Generate implementation roadmap</td>
</tr>
<tr>
<td><b>5. Implementation</b></td>
<td><code>/sc:implement "Stripe checkout"</code></td>
<td>Build with best practices</td>
</tr>
<tr>
<td><b>6. Validation</b></td>
<td><code>/sc:test --coverage</code></td>
<td>Comprehensive testing</td>
</tr>
<tr>
<td><b>7. Save Session</b></td>
<td><code>/sc:save "payment-complete"</code></td>
<td>Persist for next session</td>
</tr>
</table>

### **🎨 Domain-Specific Workflows**

<div align="center">

| Domain | Trigger | Specialist Activation | MCP Server |
|--------|---------|----------------------|------------|
| **Frontend** | UI component request | `@agent-frontend` | Magic |
| **Backend** | API endpoint creation | `@agent-backend` | Sequential |
| **Security** | Auth implementation | `@agent-security` | Context7 |
| **Testing** | E2E test scenarios | `@agent-qa` | Playwright |
| **DevOps** | Deployment setup | `@agent-devops` | Morphllm |

</div>

---

## 🎯 **When to Use**

<div align="center">

### **SuperClaude vs Standard Claude Code**

<table>
<tr>
<th width="50%">✅ Use SuperClaude</th>
<th width="50%">💭 Use Standard Claude</th>
</tr>
<tr>
<td valign="top">

**Perfect for:**
- 🏗️ Building complete software projects
- 📊 Systematic workflows with quality gates
- 🔄 Complex, multi-component systems
- 💾 Long-term projects needing persistence
- 👥 Team collaboration with standards
- 🎯 Domain-specific expertise needs

**Examples:**
- "Build a full-stack application"
- "Implement secure authentication"
- "Refactor legacy codebase"
- "Create comprehensive test suite"

</td>
<td valign="top">

**Better for:**
- 💡 Simple questions or explanations
- ⚡ One-off coding tasks
- 📚 Learning programming concepts
- 🧪 Quick prototypes or experiments
- 🔍 Code snippet generation
- ❓ General programming help

**Examples:**
- "Explain how async/await works"
- "Write a sorting function"
- "Debug this error message"
- "Convert this loop to functional"

</td>
</tr>
</table>

</div>

---

## 🎓 **Learning Path**

<div align="center">

### **Your 4-Week Journey to Mastery**

<table>
<tr>
<th>Week</th>
<th>Focus</th>
<th>Skills</th>
<th>Milestone</th>
</tr>
<tr>
<td align="center"><b>1</b><br/>🌱</td>
<td><b>Core Commands</b></td>
<td>
• <code>/sc:brainstorm</code><br/>
• <code>/sc:analyze</code><br/>
• <code>/sc:implement</code>
</td>
<td>Complete first project</td>
</tr>
<tr>
<td align="center"><b>2</b><br/>🌿</td>
<td><b>Behavioral Modes</b></td>
<td>
• Mode combinations<br/>
• Flag usage<br/>
• Context optimization
</td>
<td>Optimize workflows</td>
</tr>
<tr>
<td align="center"><b>3</b><br/>🌿</td>
<td><b>MCP Servers</b></td>
<td>
• Server configuration<br/>
• Tool integration<br/>
• Enhanced capabilities
</td>
<td>Full tool utilization</td>
</tr>
<tr>
<td align="center"><b>4</b><br/>🌲</td>
<td><b>Advanced Patterns</b></td>
<td>
• Custom workflows<br/>
• Session management<br/>
• Team patterns
</td>
<td>Framework mastery</td>
</tr>
</table>

</div>

---

## 💡 **Key Insights**

<div align="center">

### **Understanding SuperClaude's Value**

<table>
<tr>
<td width="33%" align="center">

### 🧠 **Not Software**
**It's a Framework**

SuperClaude is behavioral configuration, not standalone software. Everything runs through Claude Code.

</td>
<td width="33%" align="center">

### 🔄 **Systematic**
**Not Ad-hoc**

Transforms random requests into structured workflows with quality gates and validation.

</td>
<td width="33%" align="center">

### 🚀 **Progressive**
**Not Complex**

Start simple with basic commands. Complexity emerges naturally as needed.

</td>
</tr>
</table>

</div>

---

## 📖 **Next Steps**

<div align="center">

### **Continue Your Learning Journey**

<table>
<tr>
<th>🌱 Beginner</th>
<th>🌿 Intermediate</th>
<th>🌲 Advanced</th>
</tr>
<tr>
<td valign="top">

**First Week:**
- [Installation Guide](installation.md)
- [Commands Reference](../User-Guide/commands.md)
- [Examples Cookbook](../Reference/examples-cookbook.md)

Start with `/sc:brainstorm`

</td>
<td valign="top">

**Growing Skills:**
- [Behavioral Modes](../User-Guide/modes.md)
- [Agents Guide](../User-Guide/agents.md)
- [Session Management](../User-Guide/session-management.md)

Explore mode combinations

</td>
<td valign="top">

**Expert Usage:**
- [MCP Servers](../User-Guide/mcp-servers.md)
- [Technical Architecture](../Developer-Guide/technical-architecture.md)
- [Contributing](../Developer-Guide/contributing-code.md)

Create custom workflows

</td>
</tr>
</table>

<p align="center">
  <a href="../User-Guide/commands.md">
    <img src="https://img.shields.io/badge/📚_Explore-All_21_Commands-blue?style=for-the-badge" alt="Commands">
  </a>
  <a href="../Reference/examples-cookbook.md">
    <img src="https://img.shields.io/badge/🍳_Try-Real_Examples-green?style=for-the-badge" alt="Examples">
  </a>
</p>

</div>

---

<div align="center">

### **🎉 Ready to Transform Your Development Workflow?**

<p align="center">
  <b>Start now with</b> <code>/sc:brainstorm</code> <b>in Claude Code!</b>
</p>

<p align="center">
  <sub>SuperClaude v4.0.8 - Context Engineering for Claude Code</sub>
</p>

</div>
