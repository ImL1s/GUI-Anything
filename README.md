# 🖥️ GUI-Anything: Making ALL Software GUI-Controllable

> Transform any software into a cross-platform GUI controllable by AI agents and humans alike.

**GUI-Anything** is a plugin for AI coding agents (Claude Code, Codex, Gemini CLI)
that automatically generates rich graphical user interfaces for any software
application. Point it at source code, and the AI agent builds a complete React-based
GUI with MCP (Model Context Protocol) tools for agent control.

Inspired by [CLI-Anything](https://github.com/HKUDS/CLI-Anything) — where CLI-Anything
wraps software into command-line interfaces, GUI-Anything wraps software into **visual
graphical interfaces**.

## 🤔 Why GUI?

Most software is designed for humans — but even humans prefer GUIs over CLIs for
discovery, exploration, and visualization. GUI-Anything bridges both:

- **For Humans**: Rich visual interface with forms, previews, and interactive controls
- **For AI Agents**: Every GUI action is exposed as an MCP tool with JSON I/O
- **Cross-Platform**: Web → Desktop → Mobile from one codebase (React + Tauri v2)

## 🚀 Quick Start

### Prerequisites

- Node.js 20+
- Python 3.10+
- A supported AI coding agent: Claude Code | Codex | Gemini CLI

### Claude Code

```bash
# Clone the repository
git clone https://github.com/ImL1s/gui-anything.git

# Point Claude Code to the HARNESS.md
# Claude reads the SOP and follows the 7-phase pipeline
> Read gui-anything-plugin/HARNESS.md, then build a GUI for ./my-software
```

### Codex / Gemini CLI / Other Agents

```bash
# Clone the repository
git clone https://github.com/ImL1s/gui-anything.git

# Any AI coding agent can follow the SOP
> Read gui-anything-plugin/HARNESS.md and build a GUI for ./my-software
```

> **Note:** Plugin marketplace support is planned for a future release.
> Currently, agents read `HARNESS.md` directly from the local clone.

## ✨ How GUI-Anything Works

### 🏗️ Fully Automated 7-Phase Pipeline

From codebase analysis to npm packaging — the plugin guides the AI agent through
architecture design, React implementation, MCP tool generation, test planning,
and documentation completely automatically.

### 🎨 A2UI Schema-Driven

All GUIs are driven by a declarative `gui-schema.json` — the AI agent generates
it, React renders it, and agents control it via MCP tools. Adding a new action
means adding it to the schema — everything else follows.

### 🤖 MCP for Agent Control

Every GUI action is exposed as an MCP tool with structured JSON input/output.
Agents interact via `mcp-tools.json`, not pixel automation.

### 🖥️ Cross-Platform via Tauri v2

Generated GUIs run everywhere: web browser (dev mode), Windows, macOS, Linux,
Android, and iOS — all from the same React codebase.

## 📂 Project Structure

```
gui-anything/
├── gui-anything-plugin/         # The AI agent plugin
│   ├── HARNESS.md               # SOP — the AI reads this
│   ├── a2ui_skin.py             # Shared utility module
│   └── commands/
│       ├── gui-anything.md      # /gui-anything <path>
│       ├── refine.md            # /gui-anything:refine <path> [focus]
│       ├── test.md              # /gui-anything:test <path>
│       └── validate.md          # /gui-anything:validate <path>
├── calculator/agent-harness/    # Example: generated calculator GUI
├── examples/calculator/         # Example: source calculator app
├── LICENSE
└── README.md
```

## 🎯 Plugin Commands

| Command | Description |
|---------|-------------|
| `/gui-anything <path>` | Build a complete GUI for any software |
| `/gui-anything:refine <path> [focus]` | Expand coverage of existing GUI |
| `/gui-anything:test <path>` | Run validation tests |
| `/gui-anything:validate <path>` | Validate against HARNESS.md standards |

## 🎮 Demo: Calculator GUI

The `calculator/` directory shows a complete generated GUI for a Python calculator:

- **12 actions** across 5 groups (Arithmetic, Scientific, Memory, History, Export)
- **15 MCP tools** (12 actions + screenshot, state, navigate)
- **Dark theme** with indigo/purple palette
- **A2UI schema** driving all components

```bash
cd calculator/agent-harness
npm install
npm run dev
# → http://localhost:5173
```

## 🎯 What Can You Do with GUI-Anything?

| Software | What the GUI Does |
|----------|-------------------|
| Calculator | Forms for math operations, history viewer, export panel |
| Image Editor | Canvas preview, filter panels, batch processing |
| Video Tool | Timeline view, transcoding forms, preview player |
| API Client | Request builder, response viewer, collection manager |
| Database Tool | Query editor, result tables, schema browser |

## 📖 The Standard Playbook: HARNESS.md

`HARNESS.md` is the definitive SOP for making any software GUI-controllable via
automated React + MCP generation. It encodes proven patterns and methodologies
refined through building production-ready GUI harnesses.

Key principles:
- **Use the real software** — The GUI wraps, never reimplements
- **A2UI schema is the source of truth** — Declarative, LLM-friendly
- **MCP tools match actions 1:1** — Every button has an API
- **Theme via CSS custom properties** — Runtime switchable

## 📄 License

Apache-2.0
