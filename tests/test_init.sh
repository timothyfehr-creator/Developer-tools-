#!/usr/bin/env bash
set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TMPDIR=$(mktemp -d)
trap 'rm -rf "$TMPDIR"' EXIT

ERRORS=0
assert() {
    local desc="$1"; shift
    if ! "$@"; then
        echo "  FAIL: $desc"
        ERRORS=$((ERRORS + 1))
    fi
}

# --- Test 1: Non-interactive Python scaffold creates expected files ---
echo "Test 1: Python scaffold creates expected files"
OUT="$TMPDIR/test-py"
DEVTOOLS_NAME=myproject DEVTOOLS_LANG=python DEVTOOLS_TEST_CMD=pytest DEVTOOLS_ENTRY=main.py \
    FORCE=1 bash "$REPO_DIR/init.sh" "$OUT" >/dev/null 2>&1

assert "CLAUDE.md exists"       [ -f "$OUT/CLAUDE.md" ]
assert "CONTRIBUTING.md exists" [ -f "$OUT/CONTRIBUTING.md" ]
assert ".gitignore exists"      [ -f "$OUT/.gitignore" ]
assert ".coderabbit.yaml exists" [ -f "$OUT/.coderabbit.yaml" ]
assert "pytest.ini exists"      [ -f "$OUT/pytest.ini" ]
assert "requirements.txt exists" [ -f "$OUT/requirements.txt" ]
assert "setup_venv.sh exists"   [ -f "$OUT/setup_venv.sh" ]
assert "CI workflow exists"     [ -f "$OUT/.github/workflows/ci.yml" ]
assert ".claude/commands exist" [ -d "$OUT/.claude/commands" ]
assert "validate_commit.sh copied" [ -f "$OUT/scripts/validate_commit.sh" ]
assert "validate_secrets.sh copied" [ -f "$OUT/scripts/validate_secrets.sh" ]
assert ".git initialized"       [ -d "$OUT/.git" ]

# --- Test 2: TypeScript scaffold creates expected files ---
echo "Test 2: TypeScript scaffold creates expected files"
OUT2="$TMPDIR/test-ts"
DEVTOOLS_NAME=tsproject DEVTOOLS_LANG=typescript DEVTOOLS_TEST_CMD="npm test" DEVTOOLS_ENTRY=src/index.ts \
    FORCE=1 bash "$REPO_DIR/init.sh" "$OUT2" >/dev/null 2>&1

assert "package.json exists"    [ -f "$OUT2/package.json" ]
assert "tsconfig.json exists"   [ -f "$OUT2/tsconfig.json" ]
assert "vitest.config.ts exists" [ -f "$OUT2/vitest.config.ts" ]
assert "src/ dir exists"        [ -d "$OUT2/src" ]
assert "no pytest.ini"          [ ! -f "$OUT2/pytest.ini" ]

# --- Test 3: Dry run creates no files ---
echo "Test 3: Dry run creates no files"
OUT3="$TMPDIR/test-dry"
DRY_RUN=1 DEVTOOLS_NAME=drytest DEVTOOLS_LANG=python DEVTOOLS_TEST_CMD=pytest DEVTOOLS_ENTRY=main.py \
    FORCE=1 bash "$REPO_DIR/init.sh" "$OUT3" >/dev/null 2>&1

assert "no directory created"   [ ! -d "$OUT3" ]

# --- Test 4: Re-run without FORCE skips existing files ---
echo "Test 4: Idempotency without FORCE"
OUT4="$TMPDIR/test-idem"
DEVTOOLS_NAME=idem DEVTOOLS_LANG=python DEVTOOLS_TEST_CMD=pytest DEVTOOLS_ENTRY=main.py \
    FORCE=1 bash "$REPO_DIR/init.sh" "$OUT4" >/dev/null 2>&1

# Modify a file to check it's NOT overwritten without FORCE
echo "custom" > "$OUT4/CONTRIBUTING.md"
RESULT=$(DEVTOOLS_NAME=idem DEVTOOLS_LANG=python DEVTOOLS_TEST_CMD=pytest DEVTOOLS_ENTRY=main.py \
    bash "$REPO_DIR/init.sh" "$OUT4" 2>&1 || true)
CONTENT=$(cat "$OUT4/CONTRIBUTING.md")
assert "modified file not overwritten" [ "$CONTENT" = "custom" ]

# --- Test 5: "both" language creates separate CI files ---
echo "Test 5: Both languages scaffold"
OUT5="$TMPDIR/test-both"
DEVTOOLS_NAME=bothproject DEVTOOLS_LANG=both DEVTOOLS_TEST_CMD="pytest && npm test" DEVTOOLS_ENTRY=main.py \
    FORCE=1 bash "$REPO_DIR/init.sh" "$OUT5" >/dev/null 2>&1

assert "python-ci.yml exists"   [ -f "$OUT5/.github/workflows/python-ci.yml" ]
assert "node-ci.yml exists"     [ -f "$OUT5/.github/workflows/node-ci.yml" ]
assert "no generic ci.yml"      [ ! -f "$OUT5/.github/workflows/ci.yml" ]
assert "package.json exists"    [ -f "$OUT5/package.json" ]
assert "pytest.ini exists"      [ -f "$OUT5/pytest.ini" ]

# --- Result ---
if [ "$ERRORS" -gt 0 ]; then
    echo "test_init: $ERRORS assertion(s) failed"
    exit 1
fi
echo "test_init: all assertions passed"
