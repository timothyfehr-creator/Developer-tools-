#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/scripts/lib.sh"

REMOTE_BASE="https://raw.githubusercontent.com/timothyfehr-creator/Developer-tools-/main/templates/common"
TARGET_DIR="${1:-.}"

echo "Syncing standards in: $TARGET_DIR"
echo ""

# --- Update CONTRIBUTING.md ---
if [ -f "$TARGET_DIR/CONTRIBUTING.md" ]; then
    REMOTE_CONTRIBUTING="$(fetch_with_retry "$REMOTE_BASE/CONTRIBUTING.md")" \
        || { echo "Failed to download CONTRIBUTING.md"; exit 1; }

    if [ -z "$REMOTE_CONTRIBUTING" ]; then
        echo "Remote CONTRIBUTING.md was empty; aborting."
        exit 1
    fi

    LOCAL_CONTRIBUTING=$(cat "$TARGET_DIR/CONTRIBUTING.md")

    if [ "$REMOTE_CONTRIBUTING" = "$LOCAL_CONTRIBUTING" ]; then
        echo "CONTRIBUTING.md is up to date."
    else
        echo "CONTRIBUTING.md has upstream changes:"
        diff <(echo "$LOCAL_CONTRIBUTING") <(echo "$REMOTE_CONTRIBUTING") || true
        echo ""
        read -rp "Overwrite local CONTRIBUTING.md? [y/N]: " CONFIRM
        if [[ "$CONFIRM" =~ ^[Yy]$ ]]; then
            echo "$REMOTE_CONTRIBUTING" > "$TARGET_DIR/CONTRIBUTING.md"
            echo "CONTRIBUTING.md updated."
        else
            echo "Skipped."
        fi
    fi
else
    echo "No CONTRIBUTING.md found — downloading."
    fetch_with_retry "$REMOTE_BASE/CONTRIBUTING.md" > "$TARGET_DIR/CONTRIBUTING.md" \
        || { echo "Failed to download CONTRIBUTING.md"; exit 1; }
    echo "CONTRIBUTING.md created."
fi

echo ""

# --- Optionally update .cursorrules from CLAUDE.md ---
if [ -f "$TARGET_DIR/CLAUDE.md" ]; then
    read -rp "Update .cursorrules from current CLAUDE.md? [y/N]: " CONFIRM
    if [[ "$CONFIRM" =~ ^[Yy]$ ]]; then
        cp "$TARGET_DIR/CLAUDE.md" "$TARGET_DIR/.cursorrules"
        echo ".cursorrules updated."
    fi
fi

echo ""

# --- Optionally re-run pack_context ---
if [ -f "$TARGET_DIR/scripts/pack_context.sh" ]; then
    read -rp "Re-generate docs/context_map.txt? [y/N]: " CONFIRM
    if [[ "$CONFIRM" =~ ^[Yy]$ ]]; then
        (cd "$TARGET_DIR" && bash scripts/pack_context.sh)
    fi
fi

echo ""
echo "Sync complete."
