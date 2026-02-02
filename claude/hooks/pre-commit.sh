#!/usr/bin/env bash
set -e

# --- Enforce commit size limits (CONTRIBUTING.md rules) ---
MAX_FILES="${MAX_COMMIT_FILES:-8}"
MAX_LINES="${MAX_COMMIT_LINES:-500}"

file_count=$(git diff --cached --name-only | wc -l | tr -d ' ')
if [ "$file_count" -gt "$MAX_FILES" ]; then
    echo "ERROR: Commit touches $file_count files (max $MAX_FILES). Split it up."
    exit 1
fi

# Count added lines, skipping binary files (which show - in numstat)
added_lines=$(git diff --cached --numstat | grep -v '^-' | awk '{sum+=$1} END {print sum+0}')
if [ "$added_lines" -gt "$MAX_LINES" ]; then
    echo "ERROR: Commit adds $added_lines lines (max $MAX_LINES). Split it up."
    exit 1
fi

# --- Detect language and run tests ---
if [ -f "package.json" ]; then npm test; fi
if [ -f "requirements.txt" ] || [ -f "pytest.ini" ]; then python -m pytest; fi

# --- Update context map ---
if [ -f "scripts/pack_context.sh" ]; then bash scripts/pack_context.sh; fi
