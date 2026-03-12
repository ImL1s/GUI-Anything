# gui-anything Plugin

Build cross-platform GUI interfaces for any software using AI agents.

## What This Plugin Does

When installed, this plugin adds the following slash commands:

| Command | Description |
|---------|-------------|
| `/gui-anything <path>` | Build a complete GUI harness from source code |
| `/gui-anything:refine <path> [focus]` | Expand and improve an existing harness |
| `/gui-anything:test <path>` | Run tests and update TEST.md |
| `/gui-anything:validate <path>` | Validate harness against HARNESS.md (41 checks) |
| `/gui-anything:list` | List all existing GUI harnesses |

## Installation

```bash
# Clone the repository
git clone https://github.com/ImL1s/gui-anything.git

# The agent reads HARNESS.md and follows the 7-phase pipeline
```

## How It Works

1. **HARNESS.md** defines a 7-phase SOP for GUI generation
2. **a2ui_skin.py** provides shared validation and utilities
3. **Commands** guide the agent through build/refine/test/validate workflows
4. The agent generates React + Tauri v2 GUIs with MCP tool integration

## Architecture

```
gui-anything-plugin/
├── .claude-plugin/plugin.json    # Plugin metadata
├── HARNESS.md                    # Core 7-phase SOP
├── QUICKSTART.md                 # 5-minute guide
├── a2ui_skin.py                  # Shared utilities
├── commands/                     # Slash commands
│   ├── gui-anything.md
│   ├── refine.md
│   ├── test.md
│   ├── validate.md
│   └── list.md
├── scripts/
│   └── setup-gui-anything.sh     # Environment bootstrap
└── verify-plugin.sh              # Structure verification
```

## Key Concepts

- **A2UI Protocol**: Declarative schema (gui-schema.json) drives component rendering
- **MCP Tools**: Every GUI action exposed as structured JSON tool for agent control
- **Tauri v2**: Cross-platform (Web, Windows, macOS, Linux, Android, iOS)
- **Hard Dependencies**: GUIs wrap real software, never reimplement

## License

Apache-2.0
