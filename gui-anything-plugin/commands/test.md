# gui-anything:test Command

Run tests for a GUI harness and update TEST.md with results.

## CRITICAL: Read HARNESS.md First

**Before running tests, read `./HARNESS.md`.** It defines the test standards,
expected structure, and what constitutes a passing test suite.

## Usage

```bash
/gui-anything:test <software-path-or-repo>
```

## Arguments

- `<software-path-or-repo>` - **Required.** Either:
  - A **local path** to the software source code
  - A **GitHub repository URL**

  The software name is derived from the directory name. The agent locates the
  GUI harness at `<software-name>/agent-harness/`.

## What This Command Does

1. **Locates the GUI harness** — Finds the harness based on the software path
2. **Validates schema** — Checks `gui-schema.json` for required fields and valid types
3. **Validates structure** — Checks all required files exist per HARNESS.md spec
4. **Validates theme** — Checks `theme.json` for valid CSS values
5. **Validates MCP tools** — Checks `mcp-tools.json` for completeness
6. **Runs test suite** — Executes any test files in the tests/ directory
7. **Updates TEST.md** — Appends results to the Test Results section
8. **Reports status** — Shows pass/fail summary

## Test Output Format

The command appends to TEST.md:

```markdown
## Test Results

Last run: 2025-01-15 14:30:00

```
Schema validation: PASS (15 checks)
Structure validation: PASS (12 files)
Theme validation: PASS (8 properties)
MCP tools validation: PASS (18 tools)
```

**Summary**: All 4 validation layers passed
```

## Example

```bash
# Run all tests for calculator GUI
/gui-anything:test ./calculator

# Run tests for image editor
/gui-anything:test https://github.com/user/image-editor
```

## Success Criteria

- All validation layers pass
- TEST.md is updated with full results
- No validation errors
- Schema actions count matches MCP tools count

## Failure Handling

If tests fail:
1. Shows which validations failed with details
2. Does NOT update TEST.md (keeps previous passing results)
3. Suggests fixes based on error messages
4. Offers to re-run after fixes
