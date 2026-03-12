# gui-anything:validate Command

Validate a GUI harness against HARNESS.md standards and best practices.

## CRITICAL: Read HARNESS.md First

**Before validating, read `./HARNESS.md`.** It is the single source of truth
for all validation checks below.

## Usage

```bash
/gui-anything:validate <software-path-or-repo>
```

## Arguments

- `<software-path-or-repo>` - **Required.** Either:
  - A **local path** to the software source code
  - A **GitHub repository URL**

## What This Command Validates

### 1. Directory Structure
- `agent-harness/gui_anything/<software>/` exists
- `src/`, `agent-harness/`, `utils/`, `tests/` subdirectories present
- `package.json` in agent-harness/ root

### 2. Required Files
- `README.md` — Installation and usage guide
- `gui-schema.json` — A2UI schema (source of truth)
- `theme.json` — Visual theme configuration
- `src/App.tsx` — Main application component
- `src/main.tsx` — React entry point
- `src/components/A2UIRenderer.tsx` — Schema renderer
- `src/components/ActionPanel.tsx` — Form generator
- `src/components/PreviewPane.tsx` — Output display
- `src/components/StatusBar.tsx` — Status indicator
- `src/styles/global.css` — Responsive theme
- `agent-harness/mcp-tools.json` — MCP tool definitions
- `tests/TEST.md` — Test plan and results
- `../<SOFTWARE>.md` — Software-specific SOP

### 3. A2UI Schema Standards
- Has `metadata` with title and description
- Has `surfaces` array with at least one surface
- Has `actions` object with at least one action
- Every action has `handler`, `group`, and parameter definitions
- All component types are valid A2UI types

### 4. MCP Tool Standards
- Every schema action has a matching MCP tool
- Tool names use `__` double-underscore as group separator
- Every tool has valid `inputSchema`
- Special tools present: `take_screenshot`, `get_gui_state`, `navigate_to`
- Tool count = action count + 3 (special tools)

### 5. Theme Standards
- Has `colors` with: primary, accent, background, surface, text
- Has `fonts` with: family, sizes
- Has `spacing` and `radius` values
- All color values are valid CSS (hex, hsl, or rgb)

### 6. React Component Standards
- `App.tsx` imports and uses schema
- Components use CSS custom properties for theming
- Forms generate action payloads with correct parameter names
- Responsive layout with mobile breakpoints

### 7. Test Standards
- `TEST.md` has both plan (Part 1) and results (Part 2)
- At least schema validation tests exist
- All tests pass (100% pass rate)

### 8. Documentation Standards
- `README.md` has: installation, usage, prerequisites
- `<SOFTWARE>.md` has: architecture analysis, action mapping
- No duplicate `HARNESS.md` (should reference plugin's HARNESS.md)

## Validation Report

The command generates a detailed report:

```
GUI Harness Validation Report
Software: calculator
Path: calculator/agent-harness/gui_anything/calculator

Directory Structure    (4/4 checks passed)
Required Files         (13/13 files present)
A2UI Schema            (5/5 standards met)
MCP Tools              (5/5 standards met)
Theme                  (4/4 standards met)
React Components       (4/4 standards met)
Test Standards         (3/3 standards met)
Documentation          (3/3 standards met)

Overall: PASS (41/41 checks)
```

## Example

```bash
# Validate calculator GUI
/gui-anything:validate ./calculator

# Validate from GitHub repo
/gui-anything:validate https://github.com/user/image-editor
```
