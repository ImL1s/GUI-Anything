# ⚡ Quick Start (5 minutes)

## 1. Clone & Enter

```bash
git clone https://github.com/ImL1s/gui-anything.git
cd gui-anything
```

## 2. Try the Calculator Example

```bash
cd calculator/agent-harness
npm install
npm run dev
# → Open http://localhost:5173
```

## 3. Build a GUI for YOUR Software

### With Claude Code
```bash
# Read the HARNESS.md and follow the SOP
# (Plugin marketplace coming soon)
cat gui-anything-plugin/HARNESS.md
```

### With Any AI Agent
```
> Read gui-anything-plugin/HARNESS.md, then build a GUI for ./my-software
```

The agent will:
1. Analyze your source code
2. Design the A2UI schema
3. Generate React components
4. Create MCP tools
5. Write tests
6. Set up the dev server

## 4. Available Commands

| Command | What it does |
|---------|-------------|
| `/gui-anything <path>` | Build GUI from source |
| `/gui-anything:refine <path>` | Expand coverage |
| `/gui-anything:test <path>` | Run tests |
| `/gui-anything:validate <path>` | Validate structure |

## Next

- Read [HARNESS.md](gui-anything-plugin/HARNESS.md) for the full methodology
- See [calculator/](calculator/) for a complete example
