#!/usr/bin/env bash
set -euo pipefail

# --- macOS/Linux sed compatibility ---
sedi() {
  if [[ "$OSTYPE" == "darwin"* ]]; then
    sed -i '' "$@"
  else
    sed -i "$@"
  fi
}

# --- Locate templates (supports curl-piped usage) ---
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CLEANUP=false
if [ ! -d "$SCRIPT_DIR/templates" ]; then
    TEMP_DIR=$(mktemp -d)
    echo "Downloading templates..."
    git clone --depth 1 https://github.com/timothyfehr-creator/Developer-tools- "$TEMP_DIR" >/dev/null 2>&1
    SCRIPT_DIR="$TEMP_DIR"
    CLEANUP=true
fi

cleanup() {
  if [ "$CLEANUP" = true ] && [ -n "${TEMP_DIR:-}" ]; then
    rm -rf "$TEMP_DIR"
  fi
}
trap cleanup EXIT

# --- Interactive prompts ---
TARGET_DIR="${1:-}"
if [ -z "$TARGET_DIR" ]; then
    read -rp "Target directory: " TARGET_DIR
fi

# Expand ~ and make absolute
TARGET_DIR="${TARGET_DIR/#\~/$HOME}"
TARGET_DIR="$(cd "$(dirname "$TARGET_DIR")" 2>/dev/null && pwd)/$(basename "$TARGET_DIR")" || TARGET_DIR="$(pwd)/$TARGET_DIR"

read -rp "Project name: " PROJECT_NAME
read -rp "Language (python/typescript/both) [python]: " LANGUAGE
LANGUAGE="${LANGUAGE:-python}"

case "$LANGUAGE" in
    python)     DEFAULT_TEST="pytest" ;;
    typescript) DEFAULT_TEST="npm test" ;;
    both)       DEFAULT_TEST="pytest && npm test" ;;
    *) echo "Unknown language: $LANGUAGE"; exit 1 ;;
esac

read -rp "Test command [$DEFAULT_TEST]: " TEST_COMMAND
TEST_COMMAND="${TEST_COMMAND:-$DEFAULT_TEST}"

read -rp "Main entry point: " ENTRY_POINT

# --- Create target directory ---
mkdir -p "$TARGET_DIR"

# --- 1. Copy .gitignore FIRST ---
cp "$SCRIPT_DIR/templates/common/.gitignore" "$TARGET_DIR/.gitignore"

# --- 2. Copy common templates (preserving structure) ---
cp "$SCRIPT_DIR/templates/common/CONTRIBUTING.md" "$TARGET_DIR/CONTRIBUTING.md"
cp "$SCRIPT_DIR/templates/common/.coderabbit.yaml" "$TARGET_DIR/.coderabbit.yaml"
cp "$SCRIPT_DIR/templates/common/.env.example" "$TARGET_DIR/.env.example"

mkdir -p "$TARGET_DIR/.github/workflows"
cp "$SCRIPT_DIR/templates/common/.github/workflows/ci.yml" "$TARGET_DIR/.github/workflows/ci.yml"

mkdir -p "$TARGET_DIR/docs/memory"
cp "$SCRIPT_DIR/templates/common/docs/memory/active_context.md" "$TARGET_DIR/docs/memory/active_context.md"
cp "$SCRIPT_DIR/templates/common/docs/memory/decisions.md" "$TARGET_DIR/docs/memory/decisions.md"
cp "$SCRIPT_DIR/templates/common/docs/memory/system_patterns.md" "$TARGET_DIR/docs/memory/system_patterns.md"

# --- 3. Copy language-specific templates ---
if [ "$LANGUAGE" = "python" ] || [ "$LANGUAGE" = "both" ]; then
    cp "$SCRIPT_DIR/templates/python/requirements.txt" "$TARGET_DIR/requirements.txt"
    cp "$SCRIPT_DIR/templates/python/pytest.ini" "$TARGET_DIR/pytest.ini"
    cp "$SCRIPT_DIR/templates/python/setup_venv.sh" "$TARGET_DIR/setup_venv.sh"
    chmod +x "$TARGET_DIR/setup_venv.sh"
    mkdir -p "$TARGET_DIR/tests"
    # Language-specific CI overwrites common CI
    cp "$SCRIPT_DIR/templates/python/.github/workflows/ci.yml" "$TARGET_DIR/.github/workflows/ci.yml"
fi

if [ "$LANGUAGE" = "typescript" ] || [ "$LANGUAGE" = "both" ]; then
    cp "$SCRIPT_DIR/templates/typescript/package.json" "$TARGET_DIR/package.json"
    cp "$SCRIPT_DIR/templates/typescript/tsconfig.json" "$TARGET_DIR/tsconfig.json"
    cp "$SCRIPT_DIR/templates/typescript/vitest.config.ts" "$TARGET_DIR/vitest.config.ts"
    mkdir -p "$TARGET_DIR/src"
    # Language-specific CI overwrites common CI (typescript wins if "both")
    cp "$SCRIPT_DIR/templates/typescript/.github/workflows/ci.yml" "$TARGET_DIR/.github/workflows/ci.yml"
fi

# --- 4. Generate CLAUDE.md from template ---
cp "$SCRIPT_DIR/templates/common/CLAUDE.md.template" "$TARGET_DIR/CLAUDE.md"
sedi "s/{{PROJECT_NAME}}/$PROJECT_NAME/g" "$TARGET_DIR/CLAUDE.md"
sedi "s/{{LANGUAGE}}/$LANGUAGE/g" "$TARGET_DIR/CLAUDE.md"
sedi "s|{{TEST_COMMAND}}|$TEST_COMMAND|g" "$TARGET_DIR/CLAUDE.md"
sedi "s|{{ENTRY_POINT}}|$ENTRY_POINT|g" "$TARGET_DIR/CLAUDE.md"

# --- 5. Copy CLAUDE.md content into .cursorrules ---
cp "$TARGET_DIR/CLAUDE.md" "$TARGET_DIR/.cursorrules"

# --- 6. Copy claude/ directory as .claude/ ---
mkdir -p "$TARGET_DIR/.claude/commands" "$TARGET_DIR/.claude/hooks"
cp "$SCRIPT_DIR/claude/settings.json" "$TARGET_DIR/.claude/settings.json"
cp "$SCRIPT_DIR/claude/commands/"*.md "$TARGET_DIR/.claude/commands/"
cp "$SCRIPT_DIR/claude/hooks/"*.sh "$TARGET_DIR/.claude/hooks/"
chmod +x "$TARGET_DIR/.claude/hooks/"*.sh

# --- 7. Copy pack_context.sh ---
mkdir -p "$TARGET_DIR/scripts"
cp "$SCRIPT_DIR/scripts/pack_context.sh" "$TARGET_DIR/scripts/pack_context.sh"
chmod +x "$TARGET_DIR/scripts/pack_context.sh"

# --- 8. Initialize git ---
(cd "$TARGET_DIR" && git init -q)

# --- Summary ---
echo ""
echo "=== Project scaffolded ==="
echo "  Directory:  $TARGET_DIR"
echo "  Project:    $PROJECT_NAME"
echo "  Language:   $LANGUAGE"
echo "  Test cmd:   $TEST_COMMAND"
echo "  Entry:      $ENTRY_POINT"
echo ""
echo "Next steps:"
echo "  cd $TARGET_DIR"
echo "  git add -A && git commit -m 'chore: initial scaffold'"
if [ "$LANGUAGE" = "python" ] || [ "$LANGUAGE" = "both" ]; then
    echo "  bash setup_venv.sh"
fi
if [ "$LANGUAGE" = "typescript" ] || [ "$LANGUAGE" = "both" ]; then
    echo "  npm install"
fi
