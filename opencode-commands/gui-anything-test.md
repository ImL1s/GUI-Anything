# /gui-anything-test — Run Harness Tests

Run validation tests on a GUI-Anything harness and update TEST.md.

## Usage

```
/gui-anything-test <path>
```

## Behavior

1. Run `a2ui_skin.py` validation (schema, theme, MCP, structure)
2. Verify MCP tools match schema actions 1:1
3. Check all required files and directories exist
4. Update `tests/TEST.md` with results
5. Report pass/fail summary
