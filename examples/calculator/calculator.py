"""
Example: Simple Calculator

A minimal Python calculator to demonstrate GUI-Anything's
codebase → GUI transformation pipeline.
"""

from dataclasses import dataclass


@dataclass
class CalculatorState:
    """Current calculator state."""
    display: str = "0"
    memory: float = 0.0
    history: list[str] = None

    def __post_init__(self):
        if self.history is None:
            self.history = []


def add(a: float, b: float) -> float:
    """Add two numbers together."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Subtract b from a."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b


def divide(a: float, b: float) -> float:
    """Divide a by b. Raises ValueError if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(base: float, exponent: float) -> float:
    """Calculate base raised to exponent."""
    return base ** exponent


def square_root(value: float) -> float:
    """Calculate the square root of a value."""
    import math
    if value < 0:
        raise ValueError("Cannot take square root of negative number")
    return math.sqrt(value)


def percentage(value: float, percent: float) -> float:
    """Calculate percentage of a value."""
    return value * (percent / 100)


def memory_store(value: float) -> float:
    """Store a value in memory."""
    return value


def memory_recall() -> float:
    """Recall value from memory."""
    return 0.0  # Placeholder


def clear_display() -> str:
    """Clear the calculator display."""
    return "0"


def get_history() -> list[str]:
    """Get calculation history."""
    return []


def export_history(path: str, format: str = "txt") -> None:
    """Export calculation history to a file."""
    pass


if __name__ == "__main__":
    print(f"2 + 3 = {add(2, 3)}")
    print(f"10 / 3 = {divide(10, 3):.4f}")
    print(f"2^8 = {power(2, 8)}")
