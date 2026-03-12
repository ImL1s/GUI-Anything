# gui-anything Command

Build a complete GUI harness for any software application.

## CRITICAL: Read HARNESS.md First

**Before doing anything else, you MUST read `./HARNESS.md`.** It defines the complete
methodology, architecture standards, and implementation patterns. Every phase below
follows HARNESS.md. Do not improvise — follow the harness specification.

## Usage

```bash
/gui-anything <software-path-or-repo>
```

## Arguments

- `<software-path-or-repo>` - **Required.** Either:
  - A **local path** to the software source code (e.g., `/home/user/calculator`, `./image-editor`)
  - A **GitHub repository URL** (e.g., `https://github.com/user/project`)

  If a GitHub URL is provided, the agent clones the repo locally first, then works on
  the local copy.

  **Note:** Software names alone (e.g., "calculator") are NOT accepted. You must
  provide the actual source code path or repository URL so the agent can analyze
  the codebase.

## What This Command Does

This command implements the complete gui-anything methodology to build a
production-ready GUI harness for any application. **All phases follow the standards
defined in HARNESS.md.**

### Phase 0: Source Acquisition
- If `<software-path-or-repo>` is a GitHub URL, clone it to a local working directory
- Verify the local path exists and contains source code
- Derive the software name from the directory name

### Phase 1: Codebase Analysis
- Analyze the local source code to identify functions, classes, and data models
- Map functions to potential GUI actions
- Identify parameter types for widget selection
- Catalog the data model and file formats
- Document findings in `<SOFTWARE>.md`

### Phase 2: GUI Architecture Design
- Choose layout pattern based on number of action groups
- Design the A2UI schema with surfaces, components, and actions
- Map parameters to appropriate widget types
- Design the visual theme (colors, typography, spacing)
- Plan MCP tool definitions for agent control

### Phase 3: Implementation
- Create the directory structure per HARNESS.md spec
- Generate `gui-schema.json` (A2UI schema)
- Generate `theme.json` (visual design tokens)
- Create React components (`App.tsx`, `A2UIRenderer.tsx`, `ActionPanel.tsx`,
  `PreviewPane.tsx`, `StatusBar.tsx`)
- Create `global.css` with responsive theme using CSS custom properties
- Generate `mcp-tools.json` (MCP tool definitions)
- Create `screenshot.py` (agent feedback module)
- Create `utils/<software>_backend.py` (backend integration)
- Copy `a2ui_skin.py` from the plugin to `utils/`
- Set up `package.json`, `vite.config.ts`, `tsconfig.json`, `index.html`
- All component paths use `gui_anything/<software>/` namespace

### Phase 4: Test Planning
- Create `TEST.md` with comprehensive test plan
- Plan schema validation tests
- Plan structure validation tests
- Plan MCP tool validation tests

### Phase 5: Test Implementation
- Write schema validation tests
- Write structure validation tests
- Write theme validation tests
- Write MCP tool validation tests
- Write E2E tests if possible

### Phase 6: Test Documentation
- Run all tests
- Append full results to `TEST.md`
- Document coverage and gaps

### Phase 7: Packaging and Installation
- Create `package.json` with all dependencies
- Run `npm install`
- Verify `npm run dev` starts the dev server
- Document installation in `README.md`

## Output Structure

```
<software-name>/
└── agent-harness/
    ├── <SOFTWARE>.md              # Software-specific analysis
    ├── package.json               # npm configuration
    ├── vite.config.ts
    ├── tsconfig.json
    ├── index.html
    └── gui_anything/
        └── <software>/
            ├── README.md
            ├── gui-schema.json
            ├── theme.json
            ├── src/
            │   ├── App.tsx
            │   ├── main.tsx
            │   ├── components/
            │   └── styles/
            ├── agent-harness/
            │   ├── mcp-tools.json
            │   └── screenshot.py
            ├── utils/
            └── tests/
                ├── TEST.md
                └── test_schema.ts
```

## Example

```bash
# Build a GUI for a calculator from local source
/gui-anything ./calculator

# Build from a GitHub repo
/gui-anything https://github.com/user/image-editor
```

## Success Criteria

The command succeeds when:
1. A2UI schema is generated with all actions mapped
2. React frontend renders without errors
3. MCP tools cover all actions + built-in tools
4. All tests pass (100% pass rate)
5. TEST.md contains both plan and results
6. README.md documents installation and usage
7. `npm run dev` starts the dev server successfully
