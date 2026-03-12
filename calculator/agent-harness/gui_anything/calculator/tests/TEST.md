# Calculator GUI — Test Plan & Results

## Test Inventory Plan

- Schema validation: 5 tests planned
- Structure validation: 4 tests planned
- Theme validation: 3 tests planned
- MCP tools validation: 5 tests planned

## Schema Test Plan

1. Required fields present (`metadata`, `surfaces`, `actions`)
2. All 12 actions have `handler`, `group`, `params`
3. Component types are valid A2UI types
4. Parameter types match source function signatures
5. Action IDs follow `group.name` format

## Structure Test Plan

1. All required directories exist (`src/`, `agent-harness/`, `tests/`)
2. Required files present (schema, theme, mcp-tools)
3. README.md exists with installation instructions
4. CALCULATOR.md exists with analysis

## Theme Test Plan

1. Required color fields present (primary, accent, background, surface, text)
2. Font configuration valid
3. All color values are valid CSS

## MCP Tools Test Plan

1. Tool count = 15 (12 actions + 3 special)
2. All action tools use `__` separator
3. Special tools present (take_screenshot, get_gui_state, navigate_to)
4. Every schema action has a matching tool
5. All tools have valid inputSchema

## Test Results

Last run: 2026-03-12

```
Schema validation:     PASS (5/5 checks)
Structure validation:  PASS (4/4 checks)
Theme validation:      PASS (3/3 checks)
MCP tools validation:  PASS (5/5 checks)
```

**Summary**: All 17 validation checks passed ✅
