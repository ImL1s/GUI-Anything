# gui-anything:refine Command

Expand and improve an existing GUI harness with additional coverage.

## CRITICAL: Read HARNESS.md First

**Before refining, read `./HARNESS.md`.** It defines the standards that all
refinements must follow.

## Usage

```bash
/gui-anything:refine <software-path> [focus]
```

## Arguments

- `<software-path>` - **Required.** Local path to the software source code.
- `[focus]` - **Optional.** Specific area to focus refinement on (e.g., "export
  workflows", "settings panel", "batch operations").

## What This Command Does

### Step 1: Inventory Current Coverage
- Read the existing `gui-schema.json` to catalog all current actions
- Read the existing `mcp-tools.json` to catalog all MCP tools
- Count components, actions, and tool definitions

### Step 2: Analyze Software Capabilities
- Re-analyze the source code for functions not yet mapped
- Identify missing parameter types or widget optimizations
- Find uncovered action groups

### Step 3: Gap Analysis
- Compare current GUI coverage against full software capabilities
- If `[focus]` is provided, narrow the gap analysis to that area
- List missing actions, incomplete forms, and uncovered features
- Prioritize gaps by user impact

### Step 4: Implement New Components
- Add new actions to `gui-schema.json`
- Add corresponding form components
- Update sidebar navigation if new groups are added
- Add matching MCP tools to `mcp-tools.json`

### Step 5: Expand Tests
- Add tests for new schema entries
- Add tests for new MCP tools
- Update TEST.md with new test plan entries

### Step 6: Update Documentation
- Update README.md with new features
- Update `<SOFTWARE>.md` with new analysis findings

## Example

```bash
# Broad gap analysis and expansion
/gui-anything:refine ./calculator

# Focus on specific area
/gui-anything:refine ./image-editor "batch processing and export presets"
```

## Success Criteria

- New actions added to schema and working
- MCP tools match all actions
- All existing + new tests pass
- Documentation updated
