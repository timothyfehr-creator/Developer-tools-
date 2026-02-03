#!/usr/bin/env bash
set -e

# Run structural validations before commit
if [ -f "scripts/validate_commit.sh" ]; then
    bash scripts/validate_commit.sh --staged || exit 1
fi
if [ -f "scripts/validate_secrets.sh" ]; then
    bash scripts/validate_secrets.sh || exit 1
fi

# Detect language and run tests
if [ -f "package.json" ]; then npm test; fi
if [ -f "requirements.txt" ] || [ -f "pytest.ini" ]; then python -m pytest; fi

# Update context map
if [ -f "scripts/pack_context.sh" ]; then bash scripts/pack_context.sh; fi
