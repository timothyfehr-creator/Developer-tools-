#!/usr/bin/env bash
set -euo pipefail

# Validate the last commit (or staged changes) against CONTRIBUTING.md structural rules.
# Usage:
#   scripts/validate_commit.sh          # validate last commit
#   scripts/validate_commit.sh --staged # validate staged changes (for pre-commit hooks)

MODE="commit"
if [ "${1:-}" = "--staged" ]; then
    MODE="staged"
fi

ERRORS=()

# --- 1. Conventional commit format ---
if [ "$MODE" = "commit" ]; then
    SUBJECT=$(git log -1 --format='%s')
    if ! echo "$SUBJECT" | grep -qE '^(feat|fix|refactor|docs|test|chore)(\(.+\))?: .+'; then
        ERRORS+=("Commit message must follow conventional format: type(scope): description")
    fi

    # --- 2. Subject line length ---
    if [ "${#SUBJECT}" -gt 72 ]; then
        ERRORS+=("Commit subject is ${#SUBJECT} chars (max 72)")
    fi
fi

# --- 3. Diff size (lines added) ---
if [ "$MODE" = "staged" ]; then
    LINES_ADDED=$(git diff --cached --numstat | awk '{ s += $1 } END { print s+0 }')
    FILES_CHANGED=$(git diff --cached --name-only | wc -l | tr -d ' ')
else
    LINES_ADDED=$(git diff HEAD~1 --numstat | awk '{ s += $1 } END { print s+0 }')
    FILES_CHANGED=$(git diff HEAD~1 --name-only | wc -l | tr -d ' ')
fi

if [ "$LINES_ADDED" -gt 500 ]; then
    ERRORS+=("Diff adds $LINES_ADDED lines (max 500 per commit)")
fi

# --- 4. Files changed limit ---
if [ "$FILES_CHANGED" -gt 8 ]; then
    ERRORS+=("$FILES_CHANGED files changed (max 8 per commit)")
fi

# --- Report ---
if [ ${#ERRORS[@]} -eq 0 ]; then
    echo "validate_commit: all checks passed"
    exit 0
else
    echo "validate_commit: ${#ERRORS[@]} issue(s) found:"
    for err in "${ERRORS[@]}"; do
        echo "  - $err"
    done
    exit 1
fi
