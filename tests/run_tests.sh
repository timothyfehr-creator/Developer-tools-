#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PASS=0
FAIL=0

run_test() {
  local test_file="$1"
  local test_name
  test_name="$(basename "$test_file")"
  echo "--- $test_name ---"
  if bash "$test_file"; then
    echo "PASS: $test_name"
    PASS=$((PASS + 1))
  else
    echo "FAIL: $test_name"
    FAIL=$((FAIL + 1))
  fi
  echo ""
}

for test_file in "$SCRIPT_DIR"/test_*.sh; do
  run_test "$test_file"
done

echo "=== Results: $PASS passed, $FAIL failed ==="
if [ "$FAIL" -gt 0 ]; then
  exit 1
fi
