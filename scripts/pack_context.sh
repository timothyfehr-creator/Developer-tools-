#!/usr/bin/env bash
set -euo pipefail

mkdir -p docs

EXCLUDE='node_modules|__pycache__|.venv|venv|.git|dist|build|.next|.egg-info'

if command -v tree &>/dev/null; then
    tree -I "$EXCLUDE" --dirsfirst > docs/context_map.txt
else
    find . \
        -not -path '*/.git/*' \
        -not -path '*/node_modules/*' \
        -not -path '*/__pycache__/*' \
        -not -path '*/.venv/*' \
        -not -path '*/venv/*' \
        -not -path '*/dist/*' \
        -not -path '*/build/*' \
        -not -path '*/.next/*' \
        -not -path '*/.egg-info/*' \
        | sort > docs/context_map.txt
fi

echo "Updated docs/context_map.txt"
