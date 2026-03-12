---
name: gui-anything
description: Use when the user wants Codex to build, refine, test, or validate a GUI-Anything harness for any software or source repository. Adapts the GUI-Anything methodology to Codex without changing the generated React+Tauri harness format.
---

# GUI-Anything for Codex

Use this skill when the user wants Codex to act like the `GUI-Anything` builder.

If this skill is being used from inside the `GUI-Anything` repository, read `../gui-anything-plugin/HARNESS.md` before implementation. That file is the full methodology source of truth. If it is not available, follow the condensed rules below.

## Inputs

Accept either:

- A local source path such as `./calculator` or `/path/to/software`
- A GitHub repository URL

Derive the software name from the local directory name after cloning if needed.

## Modes

### Build

Use when the user wants a new harness.

Produce this structure:

```text
<software>/
└── agent-harness/
    ├── <SOFTWARE>.md
    ├── index.html
    ├── package.json
    ├── vite.config.ts
    ├── tsconfig.json
    └── gui_anything/
        └── <software>/
            ├── README.md
            ├── gui-schema.json
            ├── theme.json
            ├── src/
            │   ├── App.tsx
            │   ├── main.tsx
            │   ├── components/
            │   │   ├── A2UIRenderer.tsx
            │   │   ├── ActionPanel.tsx
            │   │   ├── PreviewPane.tsx
            │   │   └── StatusBar.tsx
            │   └── styles/global.css
            ├── agent-harness/
            │   ├── mcp-tools.json
            │   └── screenshot.py
            ├── utils/
            │   ├── <software>_backend.py
            │   └── a2ui_skin.py
            └── tests/
                └── TEST.md
```

Implement a React + Tauri v2 GUI with:

- A2UI schema driving all components
- MCP tools for every action (using `__` separator)
- Dark theme with CSS custom properties
- Cross-platform support (Web, Desktop, Mobile)

### Refine

Use when the harness already exists.

First inventory current actions and tests, then do gap analysis against the target software. Prefer:

- high-impact missing actions
- easy wrappers around existing backend APIs
- additions that compose well with existing action groups

Do not remove existing actions unless the user explicitly asks for a breaking change.

### Test

Plan tests before writing them. Keep both:

- `TEST.md` for test documentation and results
- Schema validation against `a2ui_skin.py`
- MCP tool mapping validation

### Validate

Check that the harness:

- uses the `gui_anything.<software>` namespace directory layout
- has all required React components
- has valid gui-schema.json, theme.json, mcp-tools.json
- MCP tools match schema actions 1:1
- documents usage and tests

## Backend Rules

Prefer the real software backend over reimplementation. Wrap the actual executable or scripting interface in `utils/<software>_backend.py`. Use synthetic reimplementation only when the project explicitly requires it or no viable native backend exists.

## Workflow

1. Acquire the source tree locally.
2. Analyze architecture, data model, existing APIs, and function-to-GUI mappings.
3. Design action groups, component layout, and A2UI schema.
4. Implement the harness (React components + backend).
5. Write `TEST.md`, then validate schema/theme/MCP.
6. Update README usage docs.
7. Verify with `npm run dev`.

## Output Expectations

When reporting progress or final results, include:

- target software and source path
- files added or changed
- validation results (schema, theme, MCP, structure)
- open risks or backend limitations
