<div align="center">

# 🚀 SuperClaude Framework

### **Claude Codeを構造化された開発プラットフォームに変換**

<p align="center">
  <img src="https://img.shields.io/badge/version-4.0.8-blue" alt="Version">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License">
  <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg" alt="PRs Welcome">
</p>

<p align="center">
  <a href="https://superclaude.netlify.app/">
    <img src="https://img.shields.io/badge/🌐_ウェブサイト-blue" alt="Website">
  </a>
  <a href="https://pypi.org/project/SuperClaude/">
    <img src="https://img.shields.io/pypi/v/SuperClaude.svg?" alt="PyPI">
  </a>
  <a href="https://www.npmjs.com/package/@bifrost_inc/superclaude">
    <img src="https://img.shields.io/npm/v/@bifrost_inc/superclaude.svg" alt="npm">
  </a>
</p>

<p align="center">
  <a href="#-クイックインストール">クイックスタート</a> •
  <a href="#-プロジェクトをサポート">サポート</a> •
  <a href="#-v4の新機能">機能</a> •
  <a href="#-ドキュメント">ドキュメント</a> •
  <a href="#-コントリビューション">コントリビューション</a>
</p>

</div>

---

<div align="center">

## 📊 **Framework Statistics**

| **Commands** | **Agents** | **Modes** | **MCP Servers** |
|:------------:|:----------:|:---------:|:---------------:|
| **21** | **14** | **5** | **6** |
| Slash Commands | Specialized AI | Behavioral | Integrations |

</div>

---

<div align="center">

## 🎯 **Overview**

SuperClaude is a **meta-programming configuration framework** that transforms Claude Code into a structured development platform through behavioral instruction injection and component orchestration. It provides systematic workflow automation with powerful tools and intelligent agents.

## ⚡ **Quick Installation**

### **Choose Your Installation Method**

| Method | Command | Best For |
|:------:|---------|----------|
| **🐍 pipx** | `pipx install SuperClaude && pipx upgrade SuperClaude && SuperClaude install` | **✅ Recommended** - Linux/macOS |
| **📦 pip** | `pip install SuperClaude && pip upgrade SuperClaude && SuperClaude install` | Traditional Python environments |
| **🌐 npm** | `npm install -g @bifrost_inc/superclaude && superclaude install` | Cross-platform, Node.js users |

</div>

<details>
<summary><b>⚠️ 重要：SuperClaude V3からのアップグレード</b></summary>

**SuperClaude V3がインストールされている場合、V4をインストールする前にアンインストールしてください：**

```bash
# 最初にV3をアンインストール
関連するすべてのファイルとディレクトリを削除：
*.md *.json および commands/

# その後V4をインストール
pipx install SuperClaude && pipx upgrade SuperClaude && SuperClaude install
```

**✅ アップグレード時に保持されるもの：**
- ✓ カスタムスラッシュコマンド（`commands/sc/`外）
- ✓ `CLAUDE.md`内のカスタムコンテンツ
- ✓ Claude Codeの`.claude.json`、`.credentials.json`、`settings.json`、`settings.local.json`
- ✓ 追加したカスタムエージェントとファイル

**⚠️ 注意：** V3の他のSuperClaude関連`.json`ファイルは競合を引き起こす可能性があるため、削除してください。

</details>

<details>
<summary><b>💡 PEP 668エラーのトラブルシューティング</b></summary>

```bash
# オプション1：pipxを使用（推奨）
pipx install SuperClaude

# オプション2：ユーザーインストール
pip install --user SuperClaude

# オプション3：強制インストール（注意して使用）
pip install --break-system-packages SuperClaude
```
</details>

---

<div align="center">

## 💖 **Support the Project**

> Hey, let's be real - maintaining SuperClaude takes time and resources.
> 
> *The Claude Max subscription alone runs $100/month for testing, and that's before counting the hours spent on documentation, bug fixes, and feature development.*
> *If you're finding value in SuperClaude for your daily work, consider supporting the project.*
> *Even a few dollars helps cover the basics and keeps development active.*
> 
> Every contributor matters, whether through code, feedback, or support. Thanks for being part of this community! 🙏

<table>
<tr>
<td align="center" width="33%">
  
### ☕ **Ko-fi**
[![Ko-fi](https://img.shields.io/badge/Support_on-Ko--fi-ff5e5b?logo=ko-fi)](https://ko-fi.com/superclaude)

*One-time contributions*

</td>
<td align="center" width="33%">

### 🎯 **Patreon**
[![Patreon](https://img.shields.io/badge/Become_a-Patron-f96854?logo=patreon)](https://patreon.com/superclaude)

*Monthly support*

</td>
<td align="center" width="33%">

### 💜 **GitHub**
[![GitHub Sponsors](https://img.shields.io/badge/GitHub-Sponsor-30363D?logo=github-sponsors)](https://github.com/sponsors/SuperClaude-Org)

*Flexible tiers*

</td>
</tr>
</table>

### **Your Support Enables:**

| Item | Cost/Impact |
|------|-------------|
| 🔬 **Claude Max Testing** | $100/month for validation & testing |
| ⚡ **Feature Development** | New capabilities & improvements |
| 📚 **Documentation** | Comprehensive guides & examples |
| 🤝 **Community Support** | Quick issue responses & help |
| 🔧 **MCP Integration** | Testing new server connections |
| 🌐 **Infrastructure** | Hosting & deployment costs |

> **Note:** No pressure though - the framework stays open source regardless. Just knowing people use and appreciate it is motivating. Contributing code, documentation, or spreading the word helps too! 🙏

</div>

---

<div align="center">

## 🎉 **V4の新機能**

> *バージョン4では、コミュニティのフィードバックと実際の使用パターンに基づいて大幅な改善が行われました。*

<table>
<tr>
<td width="50%">

### 🤖 **よりスマートなエージェントシステム**
**14の専門エージェント**とドメイン専門知識：
- セキュリティエンジニアが実際の脆弱性を発見
- フロントエンドアーキテクトがUIパターンを理解
- コンテキストに基づく自動調整
- オンデマンドのドメイン固有専門知識

</td>
<td width="50%">

### 📝 **改善された名前空間**
すべてのコマンドに**`/sc:`プレフィックス**：
- カスタムコマンドとの競合なし
- 全ライフサイクルをカバーする21のコマンド
- ブレインストーミングからデプロイメントまで
- 整理されたクリーンなコマンド構造

</td>
</tr>
<tr>
<td width="50%">

### 🔧 **MCPサーバー統合**
**6つの強力なサーバー**が連携：
- **Context7** → 最新のドキュメント
- **Sequential** → 複雑な分析
- **Magic** → UIコンポーネント生成
- **Playwright** → ブラウザテスト
- **Morphllm** → 一括変換
- **Serena** → セッション永続化

</td>
<td width="50%">

### 🎯 **動作モード**
異なるコンテキストに対応する**5つの適応モード**：
- **Brainstorming** → 適切な質問を投げかける
- **Orchestration** → 効率的なツール調整
- **Token-Efficiency** → 30-50%のコンテキスト節約
- **Task Management** → 体系的な整理
- **Introspection** → メタ認知分析

</td>
</tr>
<tr>
<td width="50%">

### ⚡ **最適化されたパフォーマンス**
**小さなフレームワーク、大きなプロジェクト**：
- フレームワークのフットプリント削減
- コードにより多くのコンテキスト
- より長い会話が可能
- 複雑な操作を実現

</td>
<td width="50%">

### 📚 **ドキュメントの全面改訂**
開発者向けの**完全な書き直し**：
- 実際の例と使用例
- よくある落とし穴を文書化
- 実用的なワークフローを含む
- より良いナビゲーション構造

</td>
</tr>
</table>

</div>

---

<div align="center">

## 📚 **ドキュメント**

### **SuperClaudeの完全ガイド**

<table>
<tr>
<th align="center">🚀 はじめに</th>
<th align="center">📖 ユーザーガイド</th>
<th align="center">🛠️ 開発者リソース</th>
<th align="center">📋 リファレンス</th>
</tr>
<tr>
<td valign="top">

- 📝 [**クイックスタートガイド**](Docs/Getting-Started/quick-start.md)  
  *素早く始める*

- 💾 [**インストールガイド**](Docs/Getting-Started/installation.md)  
  *詳細なセットアップ手順*

</td>
<td valign="top">

- 🎯 [**コマンドリファレンス**](Docs/User-Guide/commands.md)  
  *全21のスラッシュコマンド*

- 🤖 [**エージェントガイド**](Docs/User-Guide/agents.md)  
  *14の専門エージェント*

- 🎨 [**動作モード**](Docs/User-Guide/modes.md)  
  *5つの適応モード*

- 🚩 [**フラグガイド**](Docs/User-Guide/flags.md)  
  *動作制御*

- 🔧 [**MCPサーバー**](Docs/User-Guide/mcp-servers.md)  
  *6つのサーバー統合*

- 💼 [**セッション管理**](Docs/User-Guide/session-management.md)  
  *状態の保存と復元*

</td>
<td valign="top">

- 🏗️ [**技術アーキテクチャ**](Docs/Developer-Guide/technical-architecture.md)  
  *システム設計の詳細*

- 💻 [**コード貢献**](Docs/Developer-Guide/contributing-code.md)  
  *開発ワークフロー*

- 🧪 [**テストとデバッグ**](Docs/Developer-Guide/testing-debugging.md)  
  *品質保証*

</td>
<td valign="top">

- ✨ [**ベストプラクティス**](Docs/Reference/quick-start-practices.md)  
  *プロのヒントとパターン*

- 📓 [**実例集**](Docs/Reference/examples-cookbook.md)  
  *実世界のレシピ*

- 🔍 [**トラブルシューティング**](Docs/Reference/troubleshooting.md)  
  *よくある問題と修正*

</td>
</tr>
</table>

</div>

---

<div align="center">

## 🤝 **Contributing**

### **Join the SuperClaude Community**

We welcome contributions of all kinds! Here's how you can help:

| Priority | Area | Description |
|:--------:|------|-------------|
| 📝 **High** | Documentation | Improve guides, add examples, fix typos |
| 🔧 **High** | MCP Integration | Add server configs, test integrations |
| 🎯 **Medium** | Workflows | Create command patterns & recipes |
| 🧪 **Medium** | Testing | Add tests, validate features |
| 🌐 **Low** | i18n | Translate docs to other languages |

<p align="center">
  <a href="CONTRIBUTING.md">
    <img src="https://img.shields.io/badge/📖_Read-Contributing_Guide-blue" alt="Contributing Guide">
  </a>
  <a href="https://github.com/SuperClaude-Org/SuperClaude_Framework/graphs/contributors">
    <img src="https://img.shields.io/badge/👥_View-All_Contributors-green" alt="Contributors">
  </a>
</p>

</div>

---

<div align="center">

## ⚖️ **ライセンス**

このプロジェクトは**MITライセンス**の下でライセンスされています。詳細は[LICENSE](LICENSE)ファイルをご覧ください。

<p align="center">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg?" alt="MIT License">
</p>

</div>

---

<div align="center">

## ⭐ **Star History**

<a href="https://www.star-history.com/#SuperClaude-Org/SuperClaude_Framework&Timeline">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=SuperClaude-Org/SuperClaude_Framework&type=Timeline&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=SuperClaude-Org/SuperClaude_Framework&type=Timeline" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=SuperClaude-Org/SuperClaude_Framework&type=Timeline" />
 </picture>
</a>


</div>

---

<div align="center">

### **🚀 SuperClaudeコミュニティによって情熱を込めて構築**

<p align="center">
  <sub>境界を押し広げる開発者のために❤️で作られました</sub>
</p>

<p align="center">
  <a href="#-superclaude-framework">トップに戻る ↑</a>
</p>

</div>
