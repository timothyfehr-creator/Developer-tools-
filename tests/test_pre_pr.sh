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

assert_output_contains() {
    local desc="$1"
    local needle="$2"
    local output="$3"
    if ! echo "$output" | grep -q "$needle"; then
        echo "  FAIL: $desc (expected '$needle' in output)"
        ERRORS=$((ERRORS + 1))
    fi
}

# --- Test 1: Detects Python from pytest.ini ---
echo "Test 1: Detects Python from pytest.ini"
PROJ1="$TMPDIR/proj1"
mkdir -p "$PROJ1"
touch "$PROJ1/pytest.ini"
OUTPUT=$(cd "$PROJ1" && python "$REPO_DIR/scripts/pre_pr.py" 2>&1 || true)
assert_output_contains "detects python" "python" "$OUTPUT"

# --- Test 2: Detects TypeScript from tsconfig.json ---
echo "Test 2: Detects TypeScript from tsconfig.json"
PROJ2="$TMPDIR/proj2"
mkdir -p "$PROJ2"
touch "$PROJ2/tsconfig.json"
OUTPUT=$(cd "$PROJ2" && python "$REPO_DIR/scripts/pre_pr.py" 2>&1 || true)
assert_output_contains "detects typescript" "typescript" "$OUTPUT"

# --- Test 3: Detects both languages ---
echo "Test 3: Detects both languages"
PROJ3="$TMPDIR/proj3"
mkdir -p "$PROJ3"
touch "$PROJ3/pytest.ini" "$PROJ3/tsconfig.json"
OUTPUT=$(cd "$PROJ3" && python "$REPO_DIR/scripts/pre_pr.py" 2>&1 || true)
assert_output_contains "detects python" "python" "$OUTPUT"
assert_output_contains "detects typescript" "typescript" "$OUTPUT"

# --- Test 4: Skips missing tools gracefully ---
echo "Test 4: Skips missing tools gracefully"
PROJ4="$TMPDIR/proj4"
mkdir -p "$PROJ4"
touch "$PROJ4/pytest.ini"
# Run with restricted PATH so ruff/pytest aren't found
OUTPUT=$(cd "$PROJ4" && PATH="/usr/bin:/bin" python "$REPO_DIR/scripts/pre_pr.py" 2>&1 || true)
assert_output_contains "skips missing" "skipped" "$OUTPUT"

# --- Test 5: Reports unknown when no markers ---
echo "Test 5: Reports unknown when no language markers"
PROJ5="$TMPDIR/proj5"
mkdir -p "$PROJ5"
OUTPUT=$(cd "$PROJ5" && python "$REPO_DIR/scripts/pre_pr.py" 2>&1 || true)
assert_output_contains "reports unknown" "unknown" "$OUTPUT"

# --- Test 6: Exits 0 when checks pass (mock scenario) ---
echo "Test 6: Script runs without crashing on empty project"
PROJ6="$TMPDIR/proj6"
mkdir -p "$PROJ6/scripts"
# Create dummy validator scripts that pass
echo '#!/bin/bash' > "$PROJ6/scripts/validate_secrets.sh"
echo 'exit 0' >> "$PROJ6/scripts/validate_secrets.sh"
echo '#!/bin/bash' > "$PROJ6/scripts/validate_commit.sh"
echo 'exit 0' >> "$PROJ6/scripts/validate_commit.sh"
chmod +x "$PROJ6/scripts/"*.sh
OUTPUT=$(cd "$PROJ6" && python "$REPO_DIR/scripts/pre_pr.py" 2>&1 || true)
assert_output_contains "runs without crash" "checks passed" "$OUTPUT"

# --- Result ---
if [ "$ERRORS" -gt 0 ]; then
    echo "test_pre_pr: $ERRORS assertion(s) failed"
    exit 1
fi
echo "test_pre_pr: all assertions passed"
