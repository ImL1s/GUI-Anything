# Agent Harness: Software-to-GUI for Any Application

## Purpose

This harness provides a standard operating procedure (SOP) and toolkit for coding
agents (Claude Code, Codex, Gemini CLI, etc.) to build powerful, cross-platform GUI
interfaces for any software application. The goal: let AI agents AND humans operate
software through a rich graphical interface that renders natively on web, desktop,
and mobile — all generated automatically from source code analysis.

Where CLI-Anything wraps software into command-line interfaces, GUI-Anything wraps
software into visual graphical interfaces using the A2UI (Agent-to-UI) protocol
and modern web technologies (React, Tauri v2).

## General SOP: Turning Any Software into an Agent-Controllable GUI

### Phase 1: Codebase Analysis

1. **Identify the backend engine** — Most applications separate presentation from
   logic. Find the core library/framework (e.g., NumPy for scientific tools,
   Pillow for image editors, FFmpeg for video tools).
2. **Map functions to GUI actions** — Every function, method, and API endpoint
   corresponds to a potential GUI control. Catalog these mappings.
3. **Identify the data model** — What file formats does it use? How is state
   represented? (JSON, YAML, database, in-memory?)
4. **Find existing CLI tools** — Many backends ship their own CLI (`ffmpeg`,
   `convert`, `sox`). These can be wrapped as action handlers.
5. **Catalog parameters** — For each function, document parameters with types,
   defaults, and constraints. These become GUI form fields.

### Phase 2: GUI Architecture Design

1. **Choose the layout pattern** based on the number of action groups:
   - **1-3 groups**: Tabbed interface (simple, focused)
   - **4-8 groups**: Sidebar + panel layout (the standard choice)
   - **9+ groups**: Sidebar with collapsible sections
   - **Wizard**: For sequential multi-step processes

2. **Define component groups** matching the app's logical domains:
   - Project management (new, open, save, import)
   - Core operations (the app's primary purpose)
   - Configuration & settings
   - Export/Output
   - Preview/Visualization

3. **Design the A2UI schema**:
   - Define `surfaces` (top-level layout containers)
   - Define `components` per surface (toolbar, sidebar, tabs, forms, preview)
   - Map each action to a `form` component with appropriate input widgets
   - Widget selection rules:
     - `str` → text-input
     - `int`/`float` → number-input
     - `bool` → toggle
     - `path`/`file` in name → file-picker
     - `color` in name → color-picker
     - `opacity`/`volume`/`scale` → slider (0-100)
     - Enum/limited options → select dropdown

4. **Design the theme**:
   - Colors: primary, accent, background, surface, text
   - Typography: font family, sizes, weights
   - Spacing, border radius, transitions
   - Support both light and dark modes
   - Use CSS custom properties for all values

5. **Plan MCP (Model Context Protocol) tools**:
   - One tool per GUI action (matching the form submissions)
   - Special tools: `take_screenshot`, `get_gui_state`, `navigate_to`
   - Every tool returns JSON for agent consumption

### Phase 3: Implementation

1. **Create the directory structure** (see Directory Structure below)
2. **Start with the A2UI schema** — `gui-schema.json` is the single source of truth
   defining all surfaces, components, actions, and their relationships
3. **Generate the theme** — `theme.json` with color palette, typography, spacing
4. **Build the React frontend**:
   - `App.tsx` — Main layout with sidebar navigation
   - `components/A2UIRenderer.tsx` — Declarative schema-to-UI renderer
   - `components/ActionPanel.tsx` — Dynamic form generation from schema
   - `components/PreviewPane.tsx` — Output display (text, JSON, images, HTML)
   - `components/StatusBar.tsx` — Status, progress, agent connection indicator
   - `styles/global.css` — Full responsive theme using CSS custom properties
5. **Copy `a2ui_skin.py`** from the plugin (`gui-anything-plugin/a2ui_skin.py`)
   into the project. This provides the shared A2UI component patterns that all
   generated GUIs use for consistent look and feel.
6. **Build the agent harness**:
   - `mcp-tools.json` — MCP tool definitions for all actions + built-in tools
   - `screenshot.py` — Cross-platform screenshot capture (Windows, macOS, Linux)
7. **Add backend integration** — A `utils/<software>_backend.py` module that
   wraps the real software's executable. This module handles:
   - Finding the software executable (`shutil.which()`)
   - Invoking it with proper arguments (`subprocess.run()`)
   - Error handling with clear install instructions if not found
8. **Configure the build system**:
   - `package.json` with React 19, Vite 6, Lucide React
   - `vite.config.ts` with dev server configuration
   - `tsconfig.json` for TypeScript paths

### Phase 4: Test Planning (TEST.md - Part 1)

**BEFORE writing any test code**, create a `TEST.md` file in the
`agent-harness/gui_anything/<software>/tests/` directory. This file serves as
your test plan and MUST contain:

1. **Test Inventory Plan** — List planned test files and estimated test counts:
   - `test_schema.test.ts`: XX tests planned (schema validation)
   - `test_components.test.ts`: XX tests planned (component rendering)
   - `test_mcp.test.ts`: XX tests planned (MCP tool validation)

2. **Schema Test Plan** — For the A2UI schema, describe what will be tested:
   - Required fields present (metadata, surfaces, actions)
   - Component types are valid
   - Action parameters match source function signatures
   - Theme colors are valid CSS values

3. **Component Test Plan** — For each React component:
   - Renders without errors
   - Responds to user interaction
   - Generates correct action payloads

4. **MCP Tool Test Plan** — For agent integration:
   - All tools have valid inputSchema
   - Tool names match action IDs
   - Special tools (screenshot, state, navigate) present

### Phase 5: Test Implementation

1. **Schema validation tests** — Validate gui-schema.json structure
2. **Structure validation tests** — Verify all required files exist
3. **Theme validation tests** — Check CSS custom property values
4. **MCP tool validation tests** — Verify tool definitions and counts
5. **Visual smoke tests** (optional) — Screenshot comparison if Playwright available

### Phase 6: Test Documentation (TEST.md - Part 2)

1. Run all tests with appropriate test runner
2. Append full test results to `TEST.md`
3. Document test coverage and any gaps
4. Include pass/fail summary with timestamps

### Phase 7: Packaging and Installation

1. **Create `package.json`** in the `agent-harness/` directory
2. **Install dependencies**: `npm install`
3. **Verify dev server**: `npm run dev` must start without errors
4. **For Tauri native builds** (optional):
   - Add `src-tauri/` configuration
   - Configure for target platforms (Windows, macOS, Linux, Android, iOS)
   - Test with `npm run tauri dev`

## Critical Lessons Learned

### Use the Real Software — Don't Reimplement It

The GUI MUST invoke the actual application for computation, rendering, and export.
If the target software is a calculator, use its math functions. If it's an image
editor, use its rendering pipeline. Never reimplement core logic in JavaScript.

**The software is a hard dependency** — Not optional, not gracefully degraded. If
the target software isn't available, the GUI must error clearly with install
instructions, not silently produce inferior output.

### The A2UI Schema Is the Source of Truth

All GUI components are driven by `gui-schema.json`. Adding a new action means
adding it to the schema — the React frontend renders it automatically. This is
what makes the GUI agent-controllable: the schema is both human-readable and
machine-parseable.

### MCP Tools Must Match Actions 1:1

Every action defined in `gui-schema.json` must have a corresponding MCP tool in
`mcp-tools.json`. Tool names use `__` (double underscore) to encode the
`group.action` hierarchy (e.g., `create__add` for `create.add`).

### Theme via CSS Custom Properties

All visual styling goes through CSS custom properties defined in `theme.json`.
This enables runtime theme switching and ensures consistent branding without
hardcoding colors in components.

## Key Principles

- **Use the real software** — The GUI MUST wrap the actual application. Generate
  valid inputs, invoke the real tool, display real outputs.
- **A2UI schema as data layer** — The JSON schema defines all UI components
  declaratively. Components render from schema, not hardcoded layouts.
- **MCP for agent control** — Every GUI action is exposed as an MCP tool.
  Agents interact via structured JSON, not pixel automation.
- **Tauri for native builds** — Cross-platform desktop + mobile from one codebase.
- **Verify output produces correct results** — E2E tests must produce real
  artifacts (rendered images, exported files). Never test only the schema.
- **Fail loudly and clearly** — Agents need unambiguous error messages.
- **JSON output mode** — Every MCP tool returns structured JSON.

## Rules

- **The real software MUST be a hard dependency.** The GUI must invoke the actual
  software for computation and rendering. The backend module must raise a clear
  error with install instructions if the software is missing.
- **Every `gui_anything/<software>/` directory MUST contain a `README.md`** that
  explains how to install the software dependency, install the GUI, and run it.
- **Every action in the schema MUST have a matching MCP tool definition.**
- **Tests MUST include schema validation** verifying all required fields,
  valid component types, and correct parameter mappings.
- **Every GUI MUST use the shared A2UI skin** (`a2ui_skin.py`). Copy from the
  plugin to `utils/a2ui_skin.py`. This ensures consistent look and feel.
- **Every `gui_anything/<software>/tests/` directory MUST contain a `TEST.md`**
  documenting what the tests cover and the full test results output.

## Directory Structure

```
<software>/
└── agent-harness/
    ├── <SOFTWARE>.md              # Software-specific analysis and SOP
    ├── package.json               # npm package configuration
    ├── vite.config.ts
    ├── tsconfig.json
    ├── index.html
    └── gui_anything/              # Namespace directory
        └── <software>/            # Sub-package for this GUI
            ├── README.md          # HOW TO RUN — required
            ├── gui-schema.json    # A2UI schema (source of truth)
            ├── theme.json         # Visual theme configuration
            ├── src/
            │   ├── App.tsx            # Main application layout
            │   ├── main.tsx           # React entry point
            │   ├── components/        # UI components
            │   │   ├── A2UIRenderer.tsx
            │   │   ├── ActionPanel.tsx
            │   │   ├── PreviewPane.tsx
            │   │   └── StatusBar.tsx
            │   └── styles/
            │       └── global.css     # Full responsive theme
            ├── agent-harness/
            │   ├── mcp-tools.json     # MCP tool definitions
            │   └── screenshot.py      # Screenshot feedback module
            ├── utils/
            │   ├── <software>_backend.py  # Backend: invokes the real software
            │   └── a2ui_skin.py       # Shared A2UI skin (copy from plugin)
            └── tests/
                ├── TEST.md            # Test plan and results — required
                ├── test_schema.test.ts  # Schema validation tests
                └── test_e2e.test.ts     # E2E tests
```

## Applying This to Other Software

This same SOP applies to any application:

| Software | Backend | GUI Actions | How the GUI Uses It |
|----------|---------|-------------|---------------------|
| Calculator | Python math | add, subtract, multiply... | GUI forms → Python functions |
| Image Editor | Pillow/GIMP | crop, resize, filter... | GUI panels → PIL operations |
| Video Editor | FFmpeg | cut, merge, transcode... | Timeline GUI → FFmpeg commands |
| Text Processor | pandoc | convert, format... | Drag-drop → pandoc pipeline |
| API Client | requests | GET, POST, PUT... | Form builder → HTTP requests |
| Database Tool | psycopg2 | query, insert, export... | Query editor → SQL execution |

**The software is a required dependency, not optional.** The GUI generates valid
inputs and hands them to the real software for processing. This is what makes the
GUI actually useful — it's a graphical interface TO the software, not a replacement.

The pattern is always the same: **build the form → call the real software → display
the output**.
