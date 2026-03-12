# /gui-anything-validate — Validate Harness Structure

Validate a GUI-Anything harness against HARNESS.md standards (41 checks).

## Usage

```
/gui-anything-validate <path>
```

## Behavior

Run 41 checks across 8 categories:

1. **Directory structure** (6 checks) — src/, components/, styles/, agent-harness/, utils/, tests/
2. **Required files** (12 checks) — App.tsx, main.tsx, components, global.css, schema, theme, MCP tools
3. **Schema validity** (5 checks) — required fields, action definitions, parameter specs
4. **Theme validity** (4 checks) — colors, fonts, spacing, radius
5. **MCP tool mapping** (4 checks) — 1:1 action mapping, `__` separator, required special tools
6. **Backend integration** (3 checks) — backend.py exists, wraps real software, error handling
7. **Documentation** (4 checks) — README, TEST.md, analysis doc
8. **Build config** (3 checks) — package.json, vite.config.ts, tsconfig.json

## Output

Report each category with pass/fail counts and overall score.
