# /gui-anything-refine — Expand an Existing Harness

Gap-analyze and expand an existing GUI-Anything harness.

## Usage

```
/gui-anything-refine <path> [focus-area]
```

## Behavior

1. Inventory current actions and MCP tools
2. Gap-analyze against target software capabilities
3. Prioritize high-impact missing features
4. Add new actions, components, and MCP tools
5. Update TEST.md with new test cases
6. Re-validate schema/theme/MCP/structure

## Rules

- Never remove existing actions unless explicitly asked
- New actions must follow existing group/naming patterns
- Update gui-schema.json, mcp-tools.json, and React components in sync
