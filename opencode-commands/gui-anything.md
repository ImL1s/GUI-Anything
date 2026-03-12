# /gui-anything — Build a GUI Harness

Build a complete GUI harness for any software using the GUI-Anything methodology.

## Usage

```
/gui-anything <path-or-url>
```

## Behavior

1. Read `gui-anything-plugin/HARNESS.md` — it defines the full 7-phase SOP
2. Analyze the target software's source code
3. Design the A2UI schema (gui-schema.json)
4. Generate React components, theme, and MCP tools
5. Create backend wrapper and tests
6. Validate all outputs

## Output Structure

```
<software>/agent-harness/gui_anything/<software>/
├── gui-schema.json, theme.json, README.md
├── src/ (React components)
├── agent-harness/ (MCP tools, screenshot)
├── utils/ (backend, a2ui_skin)
└── tests/ (TEST.md)
```

## Rules

- Always wrap the **real software** — never reimplement
- Use `__` separator for MCP tool names
- Generate dark theme with CSS custom properties
- Every schema action must have a matching MCP tool
