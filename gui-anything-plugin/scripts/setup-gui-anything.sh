#!/usr/bin/env bash
# Setup gui-anything development environment
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PLUGIN_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
REPO_ROOT="$(cd "${PLUGIN_DIR}/.." && pwd)"

echo "╔══════════════════════════════════════════════════╗"
echo "║          GUI-Anything Environment Setup          ║"
echo "╚══════════════════════════════════════════════════╝"
echo ""

# Check Python
if command -v python3 &>/dev/null; then
    PYTHON_VERSION=$(python3 --version 2>&1 | cut -d' ' -f2)
    echo "✓ Python ${PYTHON_VERSION}"
else
    echo "✗ Python 3 not found. Install Python 3.10+"
    exit 1
fi

# Check Node.js
if command -v node &>/dev/null; then
    NODE_VERSION=$(node --version)
    echo "✓ Node.js ${NODE_VERSION}"
else
    echo "✗ Node.js not found. Install Node.js 20+"
    exit 1
fi

# Check npm
if command -v npm &>/dev/null; then
    NPM_VERSION=$(npm --version)
    echo "✓ npm ${NPM_VERSION}"
else
    echo "✗ npm not found"
    exit 1
fi

# Check Rust/Cargo (optional for Tauri)
if command -v cargo &>/dev/null; then
    CARGO_VERSION=$(cargo --version | cut -d' ' -f2)
    echo "✓ Cargo ${CARGO_VERSION} (Tauri ready)"
else
    echo "⊘ Cargo not found (optional — needed for Tauri desktop builds)"
fi

echo ""
echo "Setting up calculator example..."

CALC_DIR="${REPO_ROOT}/calculator/agent-harness"
if [ -d "${CALC_DIR}" ]; then
    cd "${CALC_DIR}"
    if [ ! -d "node_modules" ]; then
        echo "  Installing npm dependencies..."
        npm install --silent
    else
        echo "  ✓ Dependencies already installed"
    fi
    echo "  ✓ Calculator example ready: npm run dev"
else
    echo "  ⊘ Calculator example not found"
fi

echo ""
echo "╔══════════════════════════════════════════════════╗"
echo "║                  Setup Complete                  ║"
echo "╚══════════════════════════════════════════════════╝"
echo ""
echo "Next steps:"
echo "  cd calculator/agent-harness && npm run dev"
echo "  # Or ask an AI agent to read HARNESS.md"
