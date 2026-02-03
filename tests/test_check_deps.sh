#!/usr/bin/env bash
set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TMPDIR=$(mktemp -d)
trap 'rm -rf "$TMPDIR"' EXIT

ERRORS=0
assert_pass() {
    local desc="$1"; shift
    if ! "$@" >/dev/null 2>&1; then
        echo "  FAIL: $desc (expected pass)"
        ERRORS=$((ERRORS + 1))
    fi
}

assert_fail() {
    local desc="$1"; shift
    if "$@" >/dev/null 2>&1; then
        echo "  FAIL: $desc (expected fail)"
        ERRORS=$((ERRORS + 1))
    fi
}

# --- Test 1: Passes when no dep files exist ---
echo "Test 1: Passes when no dep files exist"
PROJ1="$TMPDIR/proj1"
mkdir -p "$PROJ1"
assert_pass "empty project passes" bash -c "cd '$PROJ1' && python '$REPO_DIR/scripts/check_deps.py'"

# --- Test 2: Passes with pinned requirements.txt ---
echo "Test 2: Passes with pinned requirements.txt"
PROJ2="$TMPDIR/proj2"
mkdir -p "$PROJ2"
cat > "$PROJ2/requirements.txt" << 'EOF'
requests==2.31.0
flask==2.3.0
pytest>=7.0.0,<8.0.0
EOF
assert_pass "pinned requirements passes" bash -c "cd '$PROJ2' && python '$REPO_DIR/scripts/check_deps.py'"

# --- Test 3: Fails with unpinned requirements.txt ---
echo "Test 3: Fails with unpinned requirements.txt"
PROJ3="$TMPDIR/proj3"
mkdir -p "$PROJ3"
cat > "$PROJ3/requirements.txt" << 'EOF'
requests
flask==2.3.0
EOF
assert_fail "unpinned requirements fails" bash -c "cd '$PROJ3' && python '$REPO_DIR/scripts/check_deps.py'"

# --- Test 4: Passes with pinned package.json ---
echo "Test 4: Passes with pinned package.json"
PROJ4="$TMPDIR/proj4"
mkdir -p "$PROJ4"
cat > "$PROJ4/package.json" << 'EOF'
{
  "dependencies": {
    "lodash": "4.17.21",
    "express": "4.18.2"
  }
}
EOF
assert_pass "pinned package.json passes" bash -c "cd '$PROJ4' && python '$REPO_DIR/scripts/check_deps.py'"

# --- Test 5: Fails with semver range in package.json ---
echo "Test 5: Fails with semver range in package.json"
PROJ5="$TMPDIR/proj5"
mkdir -p "$PROJ5"
cat > "$PROJ5/package.json" << 'EOF'
{
  "dependencies": {
    "lodash": "^4.17.21",
    "express": "~4.18.2"
  }
}
EOF
assert_fail "semver range fails" bash -c "cd '$PROJ5' && python '$REPO_DIR/scripts/check_deps.py'"

# --- Test 6: Handles both files together ---
echo "Test 6: Handles both files together"
PROJ6="$TMPDIR/proj6"
mkdir -p "$PROJ6"
echo "requests==2.31.0" > "$PROJ6/requirements.txt"
cat > "$PROJ6/package.json" << 'EOF'
{
  "dependencies": {
    "lodash": "4.17.21"
  }
}
EOF
assert_pass "both pinned passes" bash -c "cd '$PROJ6' && python '$REPO_DIR/scripts/check_deps.py'"

# --- Result ---
if [ "$ERRORS" -gt 0 ]; then
    echo "test_check_deps: $ERRORS assertion(s) failed"
    exit 1
fi
echo "test_check_deps: all assertions passed"
