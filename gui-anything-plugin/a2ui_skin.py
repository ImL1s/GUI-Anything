"""
A2UI Skin — Shared utility module for GUI-Anything generated projects.

This module provides common patterns and helpers used by all generated GUIs:
- A2UI schema loading and validation
- Theme CSS custom property generation
- MCP tool registry helpers
- Screenshot capture (cross-platform)

Copy this file into your project's utils/ directory:
  gui_anything/<software>/utils/a2ui_skin.py

Usage:
  from gui_anything.<software>.utils.a2ui_skin import A2UISkin

  skin = A2UISkin("<software>", version="1.0.0")
  schema = skin.load_schema("gui-schema.json")
  theme = skin.load_theme("theme.json")
  skin.validate_schema(schema)
  css_vars = skin.theme_to_css_vars(theme)
  tools = skin.load_mcp_tools("agent-harness/mcp-tools.json")
"""

from __future__ import annotations

import json
import platform
import re
import subprocess
import shutil
from pathlib import Path
from typing import Any


class A2UISkin:
    """Shared A2UI skin for all GUI-Anything generated projects."""

    REQUIRED_SCHEMA_FIELDS = {"metadata", "surfaces", "actions"}
    REQUIRED_THEME_FIELDS = {"colors", "fonts"}
    REQUIRED_COLOR_FIELDS = {"primary", "accent", "background", "surface", "text"}
    SPECIAL_MCP_TOOLS = {"take_screenshot", "get_gui_state", "navigate_to"}
    TOOL_NAME_SEPARATOR = "__"

    def __init__(self, software_name: str, version: str = "1.0.0"):
        self.software_name = software_name
        self.version = version

    def load_schema(self, path: str | Path) -> dict[str, Any]:
        """Load and return the A2UI schema."""
        p = Path(path)
        if not p.exists():
            raise FileNotFoundError(f"Schema not found: {p}")
        return json.loads(p.read_text(encoding="utf-8"))

    def load_theme(self, path: str | Path) -> dict[str, Any]:
        """Load and return the theme configuration."""
        p = Path(path)
        if not p.exists():
            raise FileNotFoundError(f"Theme not found: {p}")
        return json.loads(p.read_text(encoding="utf-8"))

    def load_mcp_tools(self, path: str | Path) -> list[dict[str, Any]]:
        """Load and return MCP tool definitions."""
        p = Path(path)
        if not p.exists():
            raise FileNotFoundError(f"MCP tools not found: {p}")
        data = json.loads(p.read_text(encoding="utf-8"))
        return data.get("tools", [])

    def validate_schema(self, schema: dict[str, Any]) -> list[str]:
        """Validate A2UI schema. Returns list of errors (empty = valid)."""
        errors: list[str] = []
        for field in self.REQUIRED_SCHEMA_FIELDS:
            if field not in schema:
                errors.append(f"Missing required field: {field}")
        if "surfaces" in schema:
            if not isinstance(schema["surfaces"], list):
                errors.append("'surfaces' must be a list")
            elif len(schema["surfaces"]) == 0:
                errors.append("'surfaces' must have at least one surface")
        if "actions" in schema:
            if not isinstance(schema["actions"], dict):
                errors.append("'actions' must be a dict")
            elif len(schema["actions"]) == 0:
                errors.append("'actions' must have at least one action")
        return errors

    def validate_theme(self, theme: dict[str, Any]) -> list[str]:
        """Validate theme configuration. Returns list of errors."""
        errors: list[str] = []
        for field in self.REQUIRED_THEME_FIELDS:
            if field not in theme:
                errors.append(f"Missing required field: {field}")
        if "colors" in theme:
            for color in self.REQUIRED_COLOR_FIELDS:
                if color not in theme["colors"]:
                    errors.append(f"Missing color: {color}")
        return errors

    def validate_mcp_tools(
        self, tools: list[dict], schema: dict[str, Any]
    ) -> list[str]:
        """Validate MCP tools against schema actions. Returns list of errors."""
        errors: list[str] = []
        tool_names = {t["name"] for t in tools}

        # Check special tools
        for special in self.SPECIAL_MCP_TOOLS:
            if special not in tool_names:
                errors.append(f"Missing special tool: {special}")

        # Check action tools use __ separator
        app_tools = tool_names - self.SPECIAL_MCP_TOOLS
        for name in app_tools:
            if self.TOOL_NAME_SEPARATOR not in name:
                errors.append(
                    f"Tool '{name}' missing '{self.TOOL_NAME_SEPARATOR}' separator"
                )

        # Check 1:1 mapping with schema actions
        if "actions" in schema:
            schema_actions = set(schema["actions"].keys())
            expected_tools = {
                a.replace(".", self.TOOL_NAME_SEPARATOR) for a in schema_actions
            }
            missing = expected_tools - app_tools
            extra = app_tools - expected_tools
            if missing:
                errors.append(f"Missing MCP tools for actions: {missing}")
            if extra:
                errors.append(f"Extra MCP tools not in schema: {extra}")

        return errors

    def theme_to_css_vars(self, theme: dict[str, Any]) -> str:
        """Convert theme.json to CSS custom properties."""
        lines: list[str] = [":root {"]
        if "colors" in theme:
            for key, val in theme["colors"].items():
                lines.append(f"  --color-{key}: {val};")
        if "fonts" in theme:
            if "family" in theme["fonts"]:
                lines.append(f"  --font-family: {theme['fonts']['family']};")
            if "sizes" in theme["fonts"]:
                for key, val in theme["fonts"]["sizes"].items():
                    lines.append(f"  --font-size-{key}: {val};")
        if "spacing" in theme:
            for key, val in theme["spacing"].items():
                lines.append(f"  --spacing-{key}: {val};")
        if "radius" in theme:
            for key, val in theme["radius"].items():
                lines.append(f"  --radius-{key}: {val};")
        lines.append("}")
        return "\n".join(lines)

    def take_screenshot(self, output_path: str = "screenshot.png") -> str:
        """Take a screenshot (cross-platform). Returns the output path."""
        # Sanitize path to prevent injection
        safe_path = str(Path(output_path).resolve())
        if not re.match(r'^[\w\s./\\:-]+$', safe_path):
            raise ValueError(f"Unsafe screenshot path: {output_path}")

        system = platform.system()
        if system == "Windows":
            try:
                import mss
                with mss.mss() as sct:
                    sct.shot(output=safe_path)
            except ImportError:
                # Use PowerShell with -File to avoid injection
                ps_script = (
                    "Add-Type -AssemblyName System.Windows.Forms;\n"
                    "$bounds = [System.Windows.Forms.Screen]::PrimaryScreen.Bounds;\n"
                    "$bmp = New-Object System.Drawing.Bitmap($bounds.Width, $bounds.Height);\n"
                    "$g = [System.Drawing.Graphics]::FromImage($bmp);\n"
                    "$g.CopyFromScreen(0,0,0,0,$bmp.Size);\n"
                    f'$bmp.Save("{safe_path}");\n'
                )
                subprocess.run(
                    ["powershell", "-NoProfile", "-Command", ps_script],
                    check=True,
                )
        elif system == "Darwin":
            subprocess.run(["screencapture", "-x", safe_path], check=True)
        else:
            if shutil.which("scrot"):
                subprocess.run(["scrot", safe_path], check=True)
            elif shutil.which("gnome-screenshot"):
                subprocess.run(
                    ["gnome-screenshot", "-f", safe_path], check=True
                )
            else:
                raise RuntimeError(
                    "No screenshot tool found. Install scrot: "
                    "apt install scrot"
                )
        return safe_path

    def encode_tool_name(self, group: str, action: str) -> str:
        """Encode group.action into MCP tool name using __ separator."""
        return f"{group}{self.TOOL_NAME_SEPARATOR}{action}"

    def decode_tool_name(self, tool_name: str) -> tuple[str, str]:
        """Decode MCP tool name back to (group, action)."""
        parts = tool_name.split(self.TOOL_NAME_SEPARATOR, 1)
        if len(parts) != 2:
            raise ValueError(f"Invalid tool name format: {tool_name}")
        return parts[0], parts[1]

    def validate_structure(self, harness_root: str | Path) -> list[str]:
        """Validate directory structure per HARNESS.md spec. Returns errors."""
        errors: list[str] = []
        root = Path(harness_root)

        required_dirs = [
            "src",
            "src/components",
            "src/styles",
            "agent-harness",
            "utils",
            "tests",
        ]
        for d in required_dirs:
            if not (root / d).is_dir():
                errors.append(f"Missing directory: {d}")

        required_files = [
            "README.md",
            "gui-schema.json",
            "theme.json",
            "src/App.tsx",
            "src/main.tsx",
            "src/components/A2UIRenderer.tsx",
            "src/components/ActionPanel.tsx",
            "src/components/PreviewPane.tsx",
            "src/components/StatusBar.tsx",
            "src/styles/global.css",
            "agent-harness/mcp-tools.json",
            "tests/TEST.md",
        ]
        for f in required_files:
            if not (root / f).is_file():
                errors.append(f"Missing file: {f}")

        return errors

    def print_banner(self) -> None:
        """Print a branded banner for the GUI harness."""
        width = 50
        title = f"GUI-Anything: {self.software_name}"
        version_line = f"v{self.version}"
        print("╔" + "═" * width + "╗")
        print(f"║{title:^{width}}║")
        print(f"║{version_line:^{width}}║")
        print("╚" + "═" * width + "╝")
