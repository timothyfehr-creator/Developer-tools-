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

# --- Safe sed replacement (escapes \, &, |) ---
escape_sed_repl() {
  local s="$1"
  s=${s//\\/\\\\}
  s=${s//&/\\&}
  s=${s//|/\\|}
  printf '%s' "$s"
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

if [ -z "$TARGET_DIR" ]; then
    echo "Error: target directory cannot be empty."
    exit 1
fi

# Expand ~ and make absolute
TARGET_DIR="${TARGET_DIR/#\~/$HOME}"
if [[ "$TARGET_DIR" != /* ]]; then
    TARGET_DIR="$(pwd)/$TARGET_DIR"
fi
TARGET_DIR="${TARGET_DIR%/}"

# Canonicalize if GNU realpath is available (macOS realpath lacks -m)
if realpath -m / >/dev/null 2>&1; then
    TARGET_DIR="$(realpath -m "$TARGET_DIR")"
fi

# --- Warn if target is non-empty (before collecting remaining prompts) ---
if [ -d "$TARGET_DIR" ] && [ "$(ls -A "$TARGET_DIR" 2>/dev/null)" ]; then
    echo "Warning: $TARGET_DIR is not empty."
    read -rp "Continue and overwrite existing files? [y/N]: " CONFIRM
    if [[ ! "$CONFIRM" =~ ^[Yy]$ ]]; then
        echo "Aborted."
        exit 0
    fi
fi

read -rp "Project name: " PROJECT_NAME
if [ -z "$PROJECT_NAME" ]; then
    echo "Error: project name cannot be empty."
    exit 1
fi
if [[ ! "$PROJECT_NAME" =~ ^[a-zA-Z0-9_-]+$ ]]; then
    echo "Error: project name must contain only letters, numbers, hyphens, and underscores."
    exit 1
fi

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
if [ -z "$ENTRY_POINT" ]; then
    echo "Error: entry point cannot be empty."
    exit 1
fi

# --- Create target directory ---
mkdir -p "$TARGET_DIR"

# --- 1. Copy .gitignore FIRST ---
cp "$SCRIPT_DIR/templates/common/.gitignore" "$TARGET_DIR/.gitignore"

# --- 2. Copy common templates (preserving structure) ---
cp "$SCRIPT_DIR/templates/common/CONTRIBUTING.md" "$TARGET_DIR/CONTRIBUTING.md"
cp "$SCRIPT_DIR/templates/common/.coderabbit.yaml" "$TARGET_DIR/.coderabbit.yaml"
cp "$SCRIPT_DIR/templates/common/.env.example" "$TARGET_DIR/.env.example"

mkdir -p "$TARGET_DIR/.github/workflows"

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
fi

if [ "$LANGUAGE" = "typescript" ] || [ "$LANGUAGE" = "both" ]; then
    cp "$SCRIPT_DIR/templates/typescript/package.json" "$TARGET_DIR/package.json"
    sedi "s|{{PROJECT_NAME}}|$(escape_sed_repl "$PROJECT_NAME")|g" "$TARGET_DIR/package.json"
    cp "$SCRIPT_DIR/templates/typescript/tsconfig.json" "$TARGET_DIR/tsconfig.json"
    cp "$SCRIPT_DIR/templates/typescript/vitest.config.ts" "$TARGET_DIR/vitest.config.ts"
    cp "$SCRIPT_DIR/templates/typescript/eslint.config.js" "$TARGET_DIR/eslint.config.js"
    mkdir -p "$TARGET_DIR/src"
fi

# --- CI workflows: single language gets ci.yml, "both" gets separate files ---
case "$LANGUAGE" in
    python)
        cp "$SCRIPT_DIR/templates/python/.github/workflows/ci.yml" "$TARGET_DIR/.github/workflows/ci.yml" ;;
    typescript)
        cp "$SCRIPT_DIR/templates/typescript/.github/workflows/ci.yml" "$TARGET_DIR/.github/workflows/ci.yml" ;;
    both)
        cp "$SCRIPT_DIR/templates/python/.github/workflows/ci.yml" "$TARGET_DIR/.github/workflows/python-ci.yml"
        cp "$SCRIPT_DIR/templates/typescript/.github/workflows/ci.yml" "$TARGET_DIR/.github/workflows/node-ci.yml" ;;
esac

# --- 4. Generate CLAUDE.md from template (safe substitution) ---
cp "$SCRIPT_DIR/templates/common/CLAUDE.md.template" "$TARGET_DIR/CLAUDE.md"
sedi "s|{{PROJECT_NAME}}|$(escape_sed_repl "$PROJECT_NAME")|g" "$TARGET_DIR/CLAUDE.md"
sedi "s|{{LANGUAGE}}|$(escape_sed_repl "$LANGUAGE")|g" "$TARGET_DIR/CLAUDE.md"
sedi "s|{{TEST_COMMAND}}|$(escape_sed_repl "$TEST_COMMAND")|g" "$TARGET_DIR/CLAUDE.md"
sedi "s|{{ENTRY_POINT}}|$(escape_sed_repl "$ENTRY_POINT")|g" "$TARGET_DIR/CLAUDE.md"

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
if [ "$LANGUAGE" = "python" ] || [ "$LANGUAGE" = "both" ]; then
    echo "  bash setup_venv.sh"
fi
if [ "$LANGUAGE" = "typescript" ] || [ "$LANGUAGE" = "both" ]; then
    echo "  npm install"
fi
echo "  git add -A && git commit -m 'chore: initial scaffold'"
