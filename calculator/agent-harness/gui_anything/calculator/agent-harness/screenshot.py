"""
Screenshot Module — Cross-platform screenshot capture for agent feedback.

Usage:
    from screenshot import take_screenshot
    path = take_screenshot("output.png")
"""

from __future__ import annotations

import sys
from pathlib import Path

# Import shared A2UI skin
sys.path.insert(0, str(Path(__file__).parent.parent / "utils"))
from a2ui_skin import A2UISkin  # noqa: E402


def take_screenshot(output_path: str = "screenshot.png") -> str:
    """Take a screenshot and return the file path."""
    skin = A2UISkin("calculator")
    return skin.take_screenshot(output_path)


if __name__ == "__main__":
    import sys as _sys
    path = _sys.argv[1] if len(_sys.argv) > 1 else "screenshot.png"
    result = take_screenshot(path)
    print(f"Screenshot saved to: {result}")
