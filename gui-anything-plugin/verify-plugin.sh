#!/usr/bin/env bash
# Verify gui-anything plugin structure

echo "Verifying gui-anything plugin structure..."
echo ""

ERRORS=0

check_file() {
    if [ -f "$1" ]; then
        echo "✓ $1"
    else
        echo "✗ $1 (MISSING)"
        ERRORS=$((ERRORS + 1))
    fi
}

check_dir() {
    if [ -d "$1" ]; then
        echo "✓ $1/"
    else
        echo "✗ $1/ (MISSING)"
        ERRORS=$((ERRORS + 1))
    fi
}

echo "Required files:"
check_file ".claude-plugin/plugin.json"
check_file "README.md"
check_file "LICENSE"
check_file "QUICKSTART.md"
check_file "PUBLISHING.md"
check_file "HARNESS.md"
check_file "a2ui_skin.py"
check_file "commands/gui-anything.md"
check_file "commands/refine.md"
check_file "commands/test.md"
check_file "commands/validate.md"
check_file "commands/list.md"
check_file "scripts/setup-gui-anything.sh"

echo ""
echo "Required directories:"
check_dir ".claude-plugin"
check_dir "commands"
check_dir "scripts"

echo ""
echo "Checking plugin.json validity..."
if python3 -c "import json; json.load(open('.claude-plugin/plugin.json'))" 2>/dev/null; then
    echo "✓ plugin.json is valid JSON"
else
    echo "✗ plugin.json is invalid JSON"
    ERRORS=$((ERRORS + 1))
fi

echo ""
echo "Checking script permissions..."
if [ -x "scripts/setup-gui-anything.sh" ]; then
    echo "✓ setup-gui-anything.sh is executable"
else
    echo "✗ setup-gui-anything.sh is not executable"
    ERRORS=$((ERRORS + 1))
fi

echo ""
if [ $ERRORS -eq 0 ]; then
    echo "✓ All checks passed! Plugin is ready."
    exit 0
else
    echo "✗ $ERRORS error(s) found. Please fix before publishing."
    exit 1
fi
