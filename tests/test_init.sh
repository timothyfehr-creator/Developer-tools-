#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
FAILURES=0

fail() { echo "  FAIL: $1"; FAILURES=$((FAILURES + 1)); }
pass() { echo "  ok: $1"; }

# --- Test: Python scaffold ---
test_python_scaffold() {
  echo "test_python_scaffold"
  local tmpdir
  tmpdir=$(mktemp -d)

  printf 'my-py-app\npython\n\nmain.py\n' | bash "$REPO_ROOT/init.sh" "$tmpdir" >/dev/null 2>&1

  # Expected files
  for f in CLAUDE.md CONTRIBUTING.md .gitignore .env.example pytest.ini requirements.txt setup_venv.sh .github/workflows/ci.yml .claude/hooks/pre-commit.sh .claude/settings.json; do
    if [ -f "$tmpdir/$f" ]; then pass "$f exists"; else fail "$f exists"; fi
  done
  if [ -d "$tmpdir/tests" ]; then pass "tests/ dir exists"; else fail "tests/ dir exists"; fi

  # CLAUDE.md substitutions
  if grep -q "my-py-app" "$tmpdir/CLAUDE.md"; then pass "PROJECT_NAME substituted"; else fail "PROJECT_NAME substituted"; fi
  if grep -q "python" "$tmpdir/CLAUDE.md"; then pass "LANGUAGE substituted"; else fail "LANGUAGE substituted"; fi
  if grep -q "main.py" "$tmpdir/CLAUDE.md"; then pass "ENTRY_POINT substituted"; else fail "ENTRY_POINT substituted"; fi

  # hooksPath set
  local hooks_path
  hooks_path=$(cd "$tmpdir" && git config core.hooksPath)
  if [ "$hooks_path" = ".claude/hooks" ]; then pass "core.hooksPath set"; else fail "core.hooksPath set (got: $hooks_path)"; fi

  # No TypeScript files
  if [ ! -f "$tmpdir/package.json" ]; then pass "no package.json"; else fail "no package.json"; fi
  if [ ! -f "$tmpdir/tsconfig.json" ]; then pass "no tsconfig.json"; else fail "no tsconfig.json"; fi

  rm -rf "$tmpdir"
}

# --- Test: TypeScript scaffold ---
test_typescript_scaffold() {
  echo "test_typescript_scaffold"
  local tmpdir
  tmpdir=$(mktemp -d)

  printf 'my-ts-app\ntypescript\n\nsrc/index.ts\n' | bash "$REPO_ROOT/init.sh" "$tmpdir" >/dev/null 2>&1

  for f in package.json tsconfig.json vitest.config.ts eslint.config.js .github/workflows/ci.yml; do
    if [ -f "$tmpdir/$f" ]; then pass "$f exists"; else fail "$f exists"; fi
  done
  if [ -d "$tmpdir/src" ]; then pass "src/ dir exists"; else fail "src/ dir exists"; fi

  # package.json has project name
  if grep -q '"my-ts-app"' "$tmpdir/package.json"; then pass "package.json name substituted"; else fail "package.json name substituted"; fi

  # CLAUDE.md has entry point with /
  if grep -q "src/index.ts" "$tmpdir/CLAUDE.md"; then pass "entry point with / handled"; else fail "entry point with / handled"; fi

  # No Python files
  if [ ! -f "$tmpdir/pytest.ini" ]; then pass "no pytest.ini"; else fail "no pytest.ini"; fi

  rm -rf "$tmpdir"
}

# --- Test: Both scaffold ---
test_both_scaffold() {
  echo "test_both_scaffold"
  local tmpdir
  tmpdir=$(mktemp -d)

  printf 'my-full-app\nboth\n\napp/main.py\n' | bash "$REPO_ROOT/init.sh" "$tmpdir" >/dev/null 2>&1

  # Both language files present
  if [ -f "$tmpdir/package.json" ]; then pass "package.json exists"; else fail "package.json exists"; fi
  if [ -f "$tmpdir/pytest.ini" ]; then pass "pytest.ini exists"; else fail "pytest.ini exists"; fi
  if [ -f "$tmpdir/eslint.config.js" ]; then pass "eslint.config.js exists"; else fail "eslint.config.js exists"; fi

  # Separate CI workflows
  if [ -f "$tmpdir/.github/workflows/python-ci.yml" ]; then pass "python-ci.yml exists"; else fail "python-ci.yml exists"; fi
  if [ -f "$tmpdir/.github/workflows/node-ci.yml" ]; then pass "node-ci.yml exists"; else fail "node-ci.yml exists"; fi
  if [ ! -f "$tmpdir/.github/workflows/ci.yml" ]; then pass "no generic ci.yml"; else fail "no generic ci.yml"; fi

  rm -rf "$tmpdir"
}

# --- Test: Input validation ---
test_validation() {
  echo "test_validation"
  local tmpdir output
  tmpdir=$(mktemp -d)

  # Empty project name
  output=$(printf '\npython\n\nmain.py\n' | bash "$REPO_ROOT/init.sh" "$tmpdir/a" 2>&1 || true)
  if echo "$output" | grep -q "Error.*empty"; then pass "empty project name rejected"; else fail "empty project name rejected"; fi

  # Bad characters in name
  output=$(printf 'bad name!\npython\n\nmain.py\n' | bash "$REPO_ROOT/init.sh" "$tmpdir/b" 2>&1 || true)
  if echo "$output" | grep -q "Error.*letters"; then pass "bad chars in name rejected"; else fail "bad chars in name rejected"; fi

  # Empty entry point
  output=$(printf 'test-app\npython\n\n\n' | bash "$REPO_ROOT/init.sh" "$tmpdir/c" 2>&1 || true)
  if echo "$output" | grep -q "Error.*empty"; then pass "empty entry point rejected"; else fail "empty entry point rejected"; fi

  # Invalid language
  output=$(printf 'test-app\nrust\n\nmain.py\n' | bash "$REPO_ROOT/init.sh" "$tmpdir/d" 2>&1 || true)
  if echo "$output" | grep -q "Unknown"; then pass "invalid language rejected"; else fail "invalid language rejected"; fi

  # Empty target dir
  output=$(printf '\n' | bash "$REPO_ROOT/init.sh" 2>&1 || true)
  if echo "$output" | grep -q "Error.*empty"; then pass "empty target dir rejected"; else fail "empty target dir rejected"; fi

  rm -rf "$tmpdir"
}

# --- Run all tests ---
test_python_scaffold
test_typescript_scaffold
test_both_scaffold
test_validation

if [ "$FAILURES" -gt 0 ]; then
  echo "test_init: $FAILURES failure(s)"
  exit 1
fi
echo "test_init: all passed"
