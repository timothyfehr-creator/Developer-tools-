#!/usr/bin/env bash
set -euo pipefail

mkdir -p docs

EXCLUDE='node_modules|__pycache__|.venv|venv|.git|dist|build|.next|.egg-info'

if command -v tree &>/dev/null; then
    tree -I "$EXCLUDE" --dirsfirst > docs/context_map.txt
else
    find . \
        \( -path './.git' -o -path './node_modules' -o -path './__pycache__' \
           -o -path './.venv' -o -path './venv' -o -path './dist' \
           -o -path './build' -o -path './.next' -o -path './.egg-info' \) -prune \
        -o -print \
        | sort > docs/context_map.txt
fi

echo "Updated docs/context_map.txt"
