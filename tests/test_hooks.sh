#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
FAILURES=0

fail() { echo "  FAIL: $1"; FAILURES=$((FAILURES + 1)); }
pass() { echo "  ok: $1"; }

# --- Test: pre-commit rejects >8 files ---
test_file_limit() {
  echo "test_file_limit"
  local tmpdir
  tmpdir=$(mktemp -d)

  (
    cd "$tmpdir" && git init -q
    cp "$REPO_ROOT/claude/hooks/pre-commit.sh" .git/hooks/pre-commit
    chmod +x .git/hooks/pre-commit
    for i in $(seq 1 9); do echo "file $i" > "file$i.txt"; done
    git add .
    output=$(bash .git/hooks/pre-commit 2>&1 || true)
    echo "$output" | grep -q "ERROR.*files"
  ) && pass "rejects >8 files" || fail "rejects >8 files"

  rm -rf "$tmpdir"
}

# --- Test: pre-commit rejects >500 lines ---
test_line_limit() {
  echo "test_line_limit"
  local tmpdir
  tmpdir=$(mktemp -d)

  (
    cd "$tmpdir" && git init -q
    cp "$REPO_ROOT/claude/hooks/pre-commit.sh" .git/hooks/pre-commit
    chmod +x .git/hooks/pre-commit
    python3 -c "print('\n'.join(f'line {i}' for i in range(501)))" > big.txt
    git add big.txt
    output=$(bash .git/hooks/pre-commit 2>&1 || true)
    echo "$output" | grep -q "ERROR.*lines"
  ) && pass "rejects >500 lines" || fail "rejects >500 lines"

  rm -rf "$tmpdir"
}

# --- Test: pre-commit passes normal commit ---
test_normal_commit() {
  echo "test_normal_commit"
  local tmpdir
  tmpdir=$(mktemp -d)

  (
    cd "$tmpdir" && git init -q
    cp "$REPO_ROOT/claude/hooks/pre-commit.sh" .git/hooks/pre-commit
    chmod +x .git/hooks/pre-commit
    echo "hello" > a.txt
    git add a.txt
    bash .git/hooks/pre-commit >/dev/null 2>&1
  ) && pass "normal commit passes" || fail "normal commit passes"

  rm -rf "$tmpdir"
}

# --- Test: SKIP_TESTS bypasses test execution ---
test_skip_tests() {
  echo "test_skip_tests"
  local tmpdir
  tmpdir=$(mktemp -d)

  # Without SKIP_TESTS: npm test exits 1, hook should fail
  (
    cd "$tmpdir" && git init -q
    cp "$REPO_ROOT/claude/hooks/pre-commit.sh" .git/hooks/pre-commit
    chmod +x .git/hooks/pre-commit
    mkdir -p node_modules
    echo '{"scripts":{"test":"exit 1"}}' > package.json
    git add package.json
    ! bash .git/hooks/pre-commit >/dev/null 2>&1
  ) && pass "tests run without SKIP_TESTS" || fail "tests run without SKIP_TESTS"

  # With SKIP_TESTS: should pass despite failing test command
  (
    cd "$tmpdir"
    SKIP_TESTS=1 bash .git/hooks/pre-commit >/dev/null 2>&1
  ) && pass "SKIP_TESTS bypasses tests" || fail "SKIP_TESTS bypasses tests"

  rm -rf "$tmpdir"
}

# --- Test: pack_context.sh produces output ---
test_pack_context() {
  echo "test_pack_context"
  local tmpdir
  tmpdir=$(mktemp -d)

  (
    cd "$tmpdir"
    mkdir -p src tests
    echo "hello" > src/main.py
    cp "$REPO_ROOT/scripts/pack_context.sh" .
    bash pack_context.sh >/dev/null 2>&1
    test -f docs/context_map.txt && test -s docs/context_map.txt
  ) && pass "context_map.txt generated" || fail "context_map.txt generated"

  rm -rf "$tmpdir"
}

# --- Run all tests ---
test_file_limit
test_line_limit
test_normal_commit
test_skip_tests
test_pack_context

if [ "$FAILURES" -gt 0 ]; then
  echo "test_hooks: $FAILURES failure(s)"
  exit 1
fi
echo "test_hooks: all passed"
