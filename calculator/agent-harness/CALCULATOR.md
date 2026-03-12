# Calculator: Software-Specific Analysis

## Architecture Analysis

The calculator is a pure Python module (`calculator.py`) with:
- **No external dependencies** — Uses only Python builtins (`math`, `typing`)
- **12 public functions** organized into 5 logical groups
- **1 dataclass** (`CalculatorState`) for state management
- **Stateful memory** via module-level `_state` variable

## Function → GUI Action Mapping

| Function | Group | Widget Type | Parameters |
|----------|-------|-------------|------------|
| `add(a, b)` | Arithmetic | 2× number-input | float, float |
| `subtract(a, b)` | Arithmetic | 2× number-input | float, float |
| `multiply(a, b)` | Arithmetic | 2× number-input | float, float |
| `divide(a, b)` | Arithmetic | 2× number-input | float, float |
| `power(base, exp)` | Scientific | 2× number-input | float, float |
| `sqrt(n)` | Scientific | 1× number-input | float |
| `factorial(n)` | Scientific | 1× number-input | int |
| `get_history()` | History | (no params) | — |
| `clear_history()` | History | (no params, confirm) | — |
| `export_history(path, fmt)` | Export | file-picker + select | str, str |
| `memory_store(val)` | Memory | 1× number-input | float |
| `memory_recall()` | Memory | (no params) | — |

## Data Model

- `CalculatorState` dataclass with `history: list[str]`, `memory: float`, `last_result: float`
- State persists across calls via module-level `_state`
- History stored as formatted strings (`"add(1, 2) = 3"`)

## GUI Layout Decision

**Sidebar + Panel** — 5 groups fit perfectly into sidebar navigation.

## Rendering Gap

None — Calculator is pure computation, no rendering pipeline needed.
The backend executes Python functions directly and returns numeric results.
