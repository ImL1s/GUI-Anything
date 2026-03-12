# /gui-anything:list — List Existing Harnesses

List all GUI-Anything harnesses in the current repository.

## Usage

```
/gui-anything:list
```

## Procedure

1. Scan all top-level directories for `agent-harness/` subdirectories
2. For each harness found, read `gui-schema.json` and `agent-harness/mcp-tools.json`
3. Display summary table:

```
Software     | Actions | MCP Tools | Status
-------------|---------|-----------|--------
calculator   | 12      | 15        | ✓ valid
```

4. If no harnesses found, suggest using `/gui-anything <path>` to create one

## Output Format

- Markdown table for human readability
- JSON array for `--json` mode
