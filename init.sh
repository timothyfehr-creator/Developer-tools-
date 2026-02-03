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

# --- Idempotent file operations ---
DRY_RUN="${DRY_RUN:-false}"
FORCE="${FORCE:-false}"

do_mkdir() {
  if [ "$DRY_RUN" = "true" ] || [ "$DRY_RUN" = "1" ]; then
    echo "[dry-run] mkdir -p $*"
  else
    mkdir -p "$@"
  fi
}

do_cp() {
  local src="$1" dest="$2"
  if [ -f "$dest" ] && cmp -s "$src" "$dest"; then
    return 0  # identical, skip
  fi
  if [ -f "$dest" ] && [ "$FORCE" != "true" ] && [ "$FORCE" != "1" ]; then
    echo "  skip (exists, use FORCE=1 to overwrite): $dest"
    return 0
  fi
  if [ "$DRY_RUN" = "true" ] || [ "$DRY_RUN" = "1" ]; then
    echo "[dry-run] cp $src -> $dest"
  else
    cp "$src" "$dest"
  fi
}

do_chmod() {
  if [ "$DRY_RUN" = "true" ] || [ "$DRY_RUN" = "1" ]; then
    echo "[dry-run] chmod $*"
  else
    chmod "$@"
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

# --- Resolve target directory (positional arg or env var or interactive) ---
TARGET_DIR="${1:-${DEVTOOLS_DIR:-}}"
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

# --- Collect project settings (env vars or interactive) ---
PROJECT_NAME="${DEVTOOLS_NAME:-}"
if [ -z "$PROJECT_NAME" ]; then
    read -rp "Project name: " PROJECT_NAME
fi
if [ -z "$PROJECT_NAME" ]; then
    echo "Error: project name cannot be empty."
    exit 1
fi

LANGUAGE="${DEVTOOLS_LANG:-}"
if [ -z "$LANGUAGE" ]; then
    read -rp "Language (python/typescript/both) [python]: " LANGUAGE
fi
LANGUAGE="${LANGUAGE:-python}"

case "$LANGUAGE" in
    python)     DEFAULT_TEST="pytest" ;;
    typescript) DEFAULT_TEST="npm test" ;;
    both)       DEFAULT_TEST="pytest && npm test" ;;
    *) echo "Unknown language: $LANGUAGE"; exit 1 ;;
esac

TEST_COMMAND="${DEVTOOLS_TEST_CMD:-}"
if [ -z "$TEST_COMMAND" ]; then
    read -rp "Test command [$DEFAULT_TEST]: " TEST_COMMAND
fi
TEST_COMMAND="${TEST_COMMAND:-$DEFAULT_TEST}"

ENTRY_POINT="${DEVTOOLS_ENTRY:-}"
if [ -z "$ENTRY_POINT" ]; then
    read -rp "Main entry point: " ENTRY_POINT
fi
if [ -z "$ENTRY_POINT" ]; then
    echo "Error: entry point cannot be empty."
    exit 1
fi

# --- Warn if target is non-empty ---
if [ -d "$TARGET_DIR" ] && [ "$(ls -A "$TARGET_DIR" 2>/dev/null)" ]; then
    if [ "$FORCE" = "true" ] || [ "$FORCE" = "1" ]; then
        echo "Warning: $TARGET_DIR is not empty (continuing with FORCE)."
    else
        echo "Warning: $TARGET_DIR is not empty."
        read -rp "Continue and overwrite existing files? [y/N]: " CONFIRM
        if [[ ! "$CONFIRM" =~ ^[Yy]$ ]]; then
            echo "Aborted."
            exit 0
        fi
    fi
fi

# --- Create target directory ---
do_mkdir "$TARGET_DIR"

# --- 1. Copy .gitignore FIRST ---
do_cp "$SCRIPT_DIR/templates/common/.gitignore" "$TARGET_DIR/.gitignore"

# --- 2. Copy common templates (preserving structure) ---
do_cp "$SCRIPT_DIR/templates/common/CONTRIBUTING.md" "$TARGET_DIR/CONTRIBUTING.md"
do_cp "$SCRIPT_DIR/templates/common/.coderabbit.yaml" "$TARGET_DIR/.coderabbit.yaml"
do_cp "$SCRIPT_DIR/templates/common/.env.example" "$TARGET_DIR/.env.example"

do_mkdir "$TARGET_DIR/.github/workflows"

do_mkdir "$TARGET_DIR/docs/memory"
do_cp "$SCRIPT_DIR/templates/common/docs/memory/active_context.md" "$TARGET_DIR/docs/memory/active_context.md"
do_cp "$SCRIPT_DIR/templates/common/docs/memory/decisions.md" "$TARGET_DIR/docs/memory/decisions.md"
do_cp "$SCRIPT_DIR/templates/common/docs/memory/system_patterns.md" "$TARGET_DIR/docs/memory/system_patterns.md"

# --- 3. Copy language-specific templates ---
if [ "$LANGUAGE" = "python" ] || [ "$LANGUAGE" = "both" ]; then
    do_cp "$SCRIPT_DIR/templates/python/requirements.txt" "$TARGET_DIR/requirements.txt"
    do_cp "$SCRIPT_DIR/templates/python/pytest.ini" "$TARGET_DIR/pytest.ini"
    do_cp "$SCRIPT_DIR/templates/python/setup_venv.sh" "$TARGET_DIR/setup_venv.sh"
    do_chmod +x "$TARGET_DIR/setup_venv.sh"
    do_mkdir "$TARGET_DIR/tests"
    if [ "$LANGUAGE" = "python" ]; then
        do_cp "$SCRIPT_DIR/templates/python/.github/workflows/ci.yml" "$TARGET_DIR/.github/workflows/ci.yml"
    fi
fi

if [ "$LANGUAGE" = "typescript" ] || [ "$LANGUAGE" = "both" ]; then
    do_cp "$SCRIPT_DIR/templates/typescript/package.json" "$TARGET_DIR/package.json"
    do_cp "$SCRIPT_DIR/templates/typescript/tsconfig.json" "$TARGET_DIR/tsconfig.json"
    do_cp "$SCRIPT_DIR/templates/typescript/vitest.config.ts" "$TARGET_DIR/vitest.config.ts"
    do_mkdir "$TARGET_DIR/src"
    if [ "$LANGUAGE" = "typescript" ]; then
        do_cp "$SCRIPT_DIR/templates/typescript/.github/workflows/ci.yml" "$TARGET_DIR/.github/workflows/ci.yml"
    fi
fi

# For "both", install separate CI workflows for each language
if [ "$LANGUAGE" = "both" ]; then
    do_cp "$SCRIPT_DIR/templates/python/.github/workflows/ci.yml" "$TARGET_DIR/.github/workflows/python-ci.yml"
    do_cp "$SCRIPT_DIR/templates/typescript/.github/workflows/ci.yml" "$TARGET_DIR/.github/workflows/node-ci.yml"
    if [ "$DRY_RUN" != "true" ] && [ "$DRY_RUN" != "1" ]; then
        rm -f "$TARGET_DIR/.github/workflows/ci.yml"
    fi
fi

# --- 4. Generate CLAUDE.md from template (safe substitution) ---
if [ "$DRY_RUN" = "true" ] || [ "$DRY_RUN" = "1" ]; then
    echo "[dry-run] generate CLAUDE.md from template"
else
    cp "$SCRIPT_DIR/templates/common/CLAUDE.md.template" "$TARGET_DIR/CLAUDE.md"
    sedi "s|{{PROJECT_NAME}}|$(escape_sed_repl "$PROJECT_NAME")|g" "$TARGET_DIR/CLAUDE.md"
    sedi "s|{{LANGUAGE}}|$(escape_sed_repl "$LANGUAGE")|g" "$TARGET_DIR/CLAUDE.md"
    sedi "s|{{TEST_COMMAND}}|$(escape_sed_repl "$TEST_COMMAND")|g" "$TARGET_DIR/CLAUDE.md"
    sedi "s|{{ENTRY_POINT}}|$(escape_sed_repl "$ENTRY_POINT")|g" "$TARGET_DIR/CLAUDE.md"
fi

# --- 5. Copy claude/ directory as .claude/ ---
do_mkdir "$TARGET_DIR/.claude/commands" "$TARGET_DIR/.claude/hooks"
for f in "$SCRIPT_DIR/claude/commands/"*.md; do
    do_cp "$f" "$TARGET_DIR/.claude/commands/$(basename "$f")"
done
for f in "$SCRIPT_DIR/claude/hooks/"*.sh; do
    do_cp "$f" "$TARGET_DIR/.claude/hooks/$(basename "$f")"
done
if [ "$DRY_RUN" != "true" ] && [ "$DRY_RUN" != "1" ]; then
    chmod +x "$TARGET_DIR/.claude/hooks/"*.sh 2>/dev/null || true
fi

# --- 6. Copy validation scripts ---
do_mkdir "$TARGET_DIR/scripts"
do_cp "$SCRIPT_DIR/scripts/pack_context.sh" "$TARGET_DIR/scripts/pack_context.sh"
do_chmod +x "$TARGET_DIR/scripts/pack_context.sh"
do_cp "$SCRIPT_DIR/scripts/pre_pr.py" "$TARGET_DIR/scripts/pre_pr.py"
do_chmod +x "$TARGET_DIR/scripts/pre_pr.py"
do_cp "$SCRIPT_DIR/scripts/check_deps.py" "$TARGET_DIR/scripts/check_deps.py"
do_chmod +x "$TARGET_DIR/scripts/check_deps.py"
for f in "$SCRIPT_DIR/scripts/validate_"*.sh; do
    [ -f "$f" ] || continue
    do_cp "$f" "$TARGET_DIR/scripts/$(basename "$f")"
    do_chmod +x "$TARGET_DIR/scripts/$(basename "$f")"
done

# --- 7. Initialize git ---
if [ "$DRY_RUN" = "true" ] || [ "$DRY_RUN" = "1" ]; then
    echo "[dry-run] git init"
else
    (cd "$TARGET_DIR" && git init -q)
fi

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
