"""
Calculator Backend — Wraps the Python calculator for GUI-Anything.

This module invokes the actual calculator.py for all computations.
The calculator is a hard dependency — if not found, this module raises
a clear error with install instructions.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from typing import Any


def _load_calculator() -> Any:
    """Load the calculator module from the examples directory."""
    calc_path = Path(__file__).resolve().parents[4] / "examples" / "calculator" / "calculator.py"
    if not calc_path.exists():
        raise FileNotFoundError(
            f"Calculator not found at {calc_path}\n"
            "Install: ensure examples/calculator/calculator.py exists in the project root."
        )
    spec = importlib.util.spec_from_file_location("calculator", calc_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load calculator from {calc_path}")
    mod = importlib.util.module_from_spec(spec)
    sys.modules["calculator"] = mod
    spec.loader.exec_module(mod)
    return mod


_calc = _load_calculator()


def execute(action_id: str, params: dict[str, Any]) -> dict[str, Any]:
    """Execute a calculator action and return the result as JSON."""
    _, func_name = action_id.split(".", 1)

    # Map action names to calculator functions
    func_map: dict[str, str] = {
        "add": "add",
        "subtract": "subtract",
        "multiply": "multiply",
        "divide": "divide",
        "power": "power",
        "sqrt": "sqrt",
        "factorial": "factorial",
        "store": "memory_store",
        "recall": "memory_recall",
        "get": "get_history",
        "clear": "clear_history",
        "history": "export_history",
    }

    mapped_name = func_map.get(func_name, func_name)
    func = getattr(_calc, mapped_name, None)
    if func is None:
        return {"error": f"Unknown action: {action_id}", "available": list(func_map.keys())}

    try:
        result = func(**params)
        return {"status": "ok", "result": result, "action": action_id}
    except Exception as e:
        return {"status": "error", "error": str(e), "action": action_id}
