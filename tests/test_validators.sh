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

assert_fails() {
    local desc="$1"; shift
    if "$@" >/dev/null 2>&1; then
        echo "  FAIL (should have failed): $desc"
        ERRORS=$((ERRORS + 1))
    fi
}

# --- Setup: create a temp git repo with a commit ---
setup_repo() {
    local dir="$1"
    mkdir -p "$dir"
    cd "$dir"
    git init -q
    git config user.email "test@test.com"
    git config user.name "Test"
    git config commit.gpgsign false
    echo ".env" > .gitignore
    echo "init" > file.txt
    git add -A && git commit -q -m "feat: initial commit"
}

# --- Test 1: validate_commit passes on good conventional commit ---
echo "Test 1: validate_commit passes on good commit"
REPO1="$TMPDIR/repo1"
setup_repo "$REPO1"
echo "change" >> file.txt
git add -A && git commit -q -m "fix: correct a bug"
assert "good commit passes" bash "$REPO_DIR/scripts/validate_commit.sh"

# --- Test 2: validate_commit fails on bad commit message ---
echo "Test 2: validate_commit fails on bad message"
REPO2="$TMPDIR/repo2"
setup_repo "$REPO2"
echo "change" >> file.txt
git add -A && git commit -q -m "added some stuff"
assert_fails "bad commit fails" bash "$REPO_DIR/scripts/validate_commit.sh"

# --- Test 3: validate_commit fails on long subject ---
echo "Test 3: validate_commit fails on long subject"
REPO3="$TMPDIR/repo3"
setup_repo "$REPO3"
echo "change" >> file.txt
LONG_MSG="feat: $(printf 'x%.0s' {1..80})"
git add -A && git commit -q -m "$LONG_MSG"
assert_fails "long subject fails" bash "$REPO_DIR/scripts/validate_commit.sh"

# --- Test 4: validate_secrets fails on staged .env ---
echo "Test 4: validate_secrets detects .env"
REPO4="$TMPDIR/repo4"
setup_repo "$REPO4"
echo "SECRET=foo" > .env
git add -f .env
assert_fails "staged .env fails" bash "$REPO_DIR/scripts/validate_secrets.sh"

# --- Test 5: validate_secrets passes when clean ---
echo "Test 5: validate_secrets passes when clean"
REPO5="$TMPDIR/repo5"
setup_repo "$REPO5"
echo "clean change" >> file.txt
git add file.txt
assert "clean staged passes" bash "$REPO_DIR/scripts/validate_secrets.sh"

# --- Test 6: validate_commit --staged checks diff size ---
echo "Test 6: validate_commit --staged checks diff size"
REPO6="$TMPDIR/repo6"
setup_repo "$REPO6"
# Generate >500 lines
for i in $(seq 1 510); do echo "line $i" >> bigfile.txt; done
git add bigfile.txt
assert_fails "large diff fails" bash "$REPO_DIR/scripts/validate_commit.sh" --staged

# --- Result ---
cd /
if [ "$ERRORS" -gt 0 ]; then
    echo "test_validators: $ERRORS assertion(s) failed"
    exit 1
fi
echo "test_validators: all assertions passed"
