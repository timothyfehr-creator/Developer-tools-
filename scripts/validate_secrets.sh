#!/usr/bin/env bash
set -euo pipefail

# Check staged changes for accidental secret commits.
# Usage:
#   scripts/validate_secrets.sh          # check staged files
#   scripts/validate_secrets.sh --last   # check last commit

MODE="staged"
if [ "${1:-}" = "--last" ]; then
    MODE="commit"
fi

ERRORS=()
WARNINGS=()

# --- 1. Check for .env files being committed ---
if [ "$MODE" = "staged" ]; then
    ENV_FILES=$(git diff --cached --name-only | grep -E '(^|/)\.env$' || true)
else
    ENV_FILES=$(git diff HEAD~1 --name-only | grep -E '(^|/)\.env$' || true)
fi

if [ -n "$ENV_FILES" ]; then
    ERRORS+=("Committing .env file(s): $ENV_FILES")
fi

# --- 2. Check that .env is in .gitignore ---
if [ -f .gitignore ]; then
    if ! grep -qE '^\s*\.env\s*$' .gitignore; then
        WARNINGS+=(".env is not listed in .gitignore")
    fi
else
    WARNINGS+=("No .gitignore found")
fi

# --- 3. High-confidence secret patterns in diff ---
if [ "$MODE" = "staged" ]; then
    DIFF=$(git diff --cached -U0 2>/dev/null || true)
else
    DIFF=$(git diff HEAD~1 -U0 2>/dev/null || true)
fi

# Only check added lines (starting with +, not ++)
ADDED_LINES=$(echo "$DIFF" | grep '^+[^+]' || true)
if [ -n "$ADDED_LINES" ]; then
    # Match high-confidence patterns: actual key values, not just variable names
    if echo "$ADDED_LINES" | grep -qiE '(sk-[a-zA-Z0-9]{20,}|ghp_[a-zA-Z0-9]{36}|AKIA[0-9A-Z]{16})'; then
        ERRORS+=("Possible API key/token detected in diff")
    fi
fi

# --- Report ---
if [ ${#WARNINGS[@]} -gt 0 ]; then
    for w in "${WARNINGS[@]}"; do
        echo "  warning: $w"
    done
fi

if [ ${#ERRORS[@]} -eq 0 ]; then
    echo "validate_secrets: all checks passed"
    exit 0
else
    echo "validate_secrets: ${#ERRORS[@]} issue(s) found:"
    for err in "${ERRORS[@]}"; do
        echo "  - $err"
    done
    exit 1
fi
