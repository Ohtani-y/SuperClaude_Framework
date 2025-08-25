<div align="center">

# 📦 SuperClaude Installation Guide

### **Transform Claude Code with 21 Commands, 14 Agents & 6 MCP Servers**

<p align="center">
  <img src="https://img.shields.io/badge/version-4.0.8-blue?style=for-the-badge" alt="Version">
  <img src="https://img.shields.io/badge/Python-3.8+-green?style=for-the-badge" alt="Python">
  <img src="https://img.shields.io/badge/Platform-Linux%20|%20macOS%20|%20Windows-orange?style=for-the-badge" alt="Platform">
</p>

<p align="center">
  <a href="#-quick-installation">Quick Install</a> •
  <a href="#-requirements">Requirements</a> •
  <a href="#-installation-methods">Methods</a> •
  <a href="#-verification">Verify</a> •
  <a href="#-troubleshooting">Troubleshoot</a>
</p>

</div>

---

## ⚡ **クイックインストール**

<div align="center">

### **お好みの方法を選択**

| Method | Command | Platform | Best For |
|:------:|---------|:--------:|----------|
| **🐍 pipx** | `pipx install SuperClaude && SuperClaude install` | Linux/macOS | **✅ Recommended** - Isolated environment |
| **📦 pip** | `pip install SuperClaude && SuperClaude install` | All | Traditional Python setups |
| **🌐 npm** | `npm install -g @bifrost_inc/superclaude && superclaude install` | All | Node.js developers |
| **🔧 Dev** | `git clone ... && pip install -e ".[dev]"` | All | Contributors & developers |

</div>

---

## 📋 **要件**

<div align="center">

<table>
<tr>
<td align="center" width="50%">

### ✅ **必須**

| Component | Version | Check Command |
|-----------|---------|---------------|
| **Python** | 3.8+ | `python3 --version` |
| **pip** | Latest | `pip --version` |
| **Claude Code** | Latest | `claude --version` |
| **Disk Space** | 50MB | `df -h` |

</td>
<td align="center" width="50%">

### 💡 **オプション**

| Component | Purpose | Check Command |
|-----------|---------|---------------|
| **Node.js** | MCP Servers | `node --version` |
| **Git** | Version Control | `git --version` |
| **pipx** | Isolated Install | `pipx --version` |
| **RAM** | Performance | 1GB recommended |

</td>
</tr>
</table>

</div>

<details>
<summary><b>🔍 Quick System Check</b></summary>

```bash
# すべての要件を一度にチェックするには以下を実行
python3 --version && echo "✅ Python OK" || echo "❌ Python missing"
claude --version && echo "✅ Claude Code OK" || echo "❌ Claude Code missing"
node --version 2>/dev/null && echo "✅ Node.js OK (optional)" || echo "⚠️ Node.js missing (optional)"
git --version 2>/dev/null && echo "✅ Git OK (optional)" || echo "⚠️ Git missing (optional)"
```

</details>

---

## 🚀 **インストール方法**

<div align="center">

### **詳細インストール手順**

</div>

### **Method 1: pipx (Recommended)**

<table>
<tr>
<td width="60%">

```bash
# pipxがない場合はインストール
python3 -m pip install --user pipx
python3 -m pipx ensurepath

# SuperClaudeをインストール
pipx install SuperClaude

# Run the installer
SuperClaude install
```

</td>
<td width="40%">

**✅ Advantages:**
- Isolated environment
- No dependency conflicts
- Clean uninstall
- Automatic PATH setup

**📍 Best for:**
- Linux/macOS users
- Clean system installs
- Multiple Python projects

</td>
</tr>
</table>

### **Method 2: pip (Traditional)**

<table>
<tr>
<td width="60%">

```bash
# 標準インストール
pip install SuperClaude

# またはユーザーインストール
pip install --user SuperClaude

# Run the installer
SuperClaude install
```

</td>
<td width="40%">

**✅ Advantages:**
- Works everywhere
- Familiar to Python users
- Direct installation

**📍 Best for:**
- Windows users
- Virtual environments
- Quick setup

</td>
</tr>
</table>

### **Method 3: npm (Cross-platform)**

<table>
<tr>
<td width="60%">

```bash
# グローバルインストール
npm install -g @bifrost_inc/superclaude

# Run the installer
superclaude install
```

</td>
<td width="40%">

**✅ Advantages:**
- Cross-platform
- NPM ecosystem
- JavaScript familiar

**📍 Best for:**
- Node.js developers
- NPM users
- Cross-platform needs

</td>
</tr>
</table>

### **Method 4: Development Installation**

<table>
<tr>
<td width="60%">

```bash
# リポジトリをクローン
git clone https://github.com/SuperClaude-Org/SuperClaude_Framework.git
cd SuperClaude_Framework

# 開発モードでインストール
pip install -e ".[dev]"

# インストールをテスト
SuperClaude install --dry-run
```

</td>
<td width="40%">

**✅ Advantages:**
- Latest features
- Contribute to project
- Full source access

**📍 Best for:**
- Contributors
- Custom modifications
- Testing new features

</td>
</tr>
</table>

---

## 🎛️ **インストールオプション**

<div align="center">

### **インストールをカスタマイズ**

| Option | Command | Description |
|--------|---------|-------------|
| **Interactive** | `SuperClaude install` | Guided setup with prompts |
| **Specific Components** | `SuperClaude install --components core mcp modes` | Install only what you need |
| **Preview Mode** | `SuperClaude install --dry-run` | See what will be installed |
| **Force Install** | `SuperClaude install --force --yes` | Skip all confirmations |
| **List Components** | `SuperClaude install --list-components` | View available components |

</div>

---

## ✅ **Verification**

<div align="center">

### **インストール成功を確認**

</div>

### **Step 1: Check Installation**

```bash
# Verify SuperClaude version
python3 -m SuperClaude --version
# Expected: SuperClaude 4.0.8

# List installed components
SuperClaude install --list-components
# Expected: List of available components
```

### **Step 2: Test in Claude Code**

```bash
# Open Claude Code and try these commands:
/sc:brainstorm "test project"     # Should trigger discovery questions
/sc:analyze README.md              # Should provide structured analysis
@agent-security "review code"     # Should activate security specialist
```

### **Step 3: What's Installed**

<div align="center">

| Location | Contents | Size |
|----------|----------|------|
| `~/.claude/` | Framework files | ~50MB |
| `~/.claude/CLAUDE.md` | Main entry point | ~2KB |
| `~/.claude/*.md` | Behavioral instructions | ~200KB |
| `~/.claude/claude-code-settings.json` | MCP configurations | ~5KB |

</div>

---

## 🛠️ **管理**

<div align="center">

<table>
<tr>
<th>📦 Update</th>
<th>💾 Backup</th>
<th>🗑️ Uninstall</th>
</tr>
<tr>
<td>

```bash
# 最新版に更新
pip install --upgrade SuperClaude
SuperClaude update
```

</td>
<td>

```bash
# バックアップを作成
SuperClaude backup --create

# バックアップを復元
SuperClaude backup --restore [file]
```

</td>
<td>

```bash
# フレームワークを削除
SuperClaude uninstall

# パッケージをアンインストール
pip uninstall SuperClaude
```

</td>
</tr>
</table>

</div>

---

## 🔧 **トラブルシューティング**

<details>
<summary><b>❌ PEP 668 Error (Python Package Management)</b></summary>

This error occurs on systems with externally managed Python environments.

**解決策（優先順）:**

```bash
# オプション1: pipxを使用（推奨）
pipx install SuperClaude

# オプション2: ユーザーインストール
pip install --user SuperClaude

# オプション3: 仮想環境
python3 -m venv superclaude-env
source superclaude-env/bin/activate  # Linux/macOS
# or
superclaude-env\Scripts\activate  # Windows
pip install SuperClaude

# オプション4: 強制実行（注意して使用）
pip install --break-system-packages SuperClaude
```

</details>

<details>
<summary><b>❌ Command Not Found</b></summary>

If `SuperClaude` command is not found after installation:

```bash
# Check if package is installed
python3 -m pip show SuperClaude

# Run using Python module
python3 -m SuperClaude install

# Add to PATH (if using --user)
export PATH="$HOME/.local/bin:$PATH"
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc  # Linux
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc   # macOS
```

</details>

<details>
<summary><b>❌ Claude Code Not Found</b></summary>

Claude CodeがインストールされていないかPATHにない場合:

1. Download from [https://claude.ai/code](https://claude.ai/code)
2. Install following platform instructions
3. Verify with: `claude --version`
4. Restart terminal after installation

</details>

<details>
<summary><b>❌ Permission Denied</b></summary>

インストール中の権限エラーの場合:

```bash
# ユーザーインストールを使用
pip install --user SuperClaude

# またはsudoを使用（非推奨）
sudo pip install SuperClaude

# より良い方法: pipxを使用
pipx install SuperClaude
```

</details>

<details>
<summary><b>❌ Missing Python or pip</b></summary>

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

**macOS:**
```bash
# Install Homebrew first if needed
brew install python3
```

**Windows:**
- Download from [python.org](https://python.org)
- Check "Add Python to PATH" during installation
- Restart terminal after installation

</details>

---

## 📚 **Next Steps**

<div align="center">

### **Your Learning Journey**

<table>
<tr>
<th>🌱 Start Here</th>
<th>🌿 Expand Skills</th>
<th>🌲 Master Framework</th>
</tr>
<tr>
<td valign="top">

**First Week:**
- [Quick Start Guide](quick-start.md)
- [Commands Reference](../User-Guide/commands.md)
- Try `/sc:brainstorm`

</td>
<td valign="top">

**Week 2-3:**
- [Behavioral Modes](../User-Guide/modes.md)
- [Agents Guide](../User-Guide/agents.md)
- [Examples Cookbook](../Reference/examples-cookbook.md)

</td>
<td valign="top">

**Advanced:**
- [MCP Servers](../User-Guide/mcp-servers.md)
- [Technical Architecture](../Developer-Guide/technical-architecture.md)
- [Contributing Code](../Developer-Guide/contributing-code.md)

</td>
</tr>
</table>

</div>

---

<div align="center">

### **🎉 Installation Complete!**

You now have access to:

<p align="center">
  <b>21 Commands</b> • <b>14 AI Agents</b> • <b>6 Behavioral Modes</b> • <b>6 MCP Servers</b>
</p>

**Ready to start?** Try `/sc:brainstorm` in Claude Code for your first SuperClaude experience!

<p align="center">
  <a href="quick-start.md">
    <img src="https://img.shields.io/badge/📖_Continue_to-Quick_Start_Guide-blue?style=for-the-badge" alt="Quick Start">
  </a>
</p>

</div>
