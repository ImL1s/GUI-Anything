# /gui-anything-list — List Existing Harnesses

List all GUI-Anything harnesses in the current repository.

## Usage

```
/gui-anything-list
```

## Behavior

1. Scan all top-level directories for `agent-harness/` subdirectories
2. For each harness found, display:
   - Software name
   - Number of actions in gui-schema.json
   - Number of MCP tools
   - Validation status (pass/fail)
   - Last modified date
3. Output as a formatted table
