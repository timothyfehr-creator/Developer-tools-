#!/usr/bin/env bash
set -e

# Detect language and run tests
if [ -f "package.json" ]; then npm test; fi
if [ -f "requirements.txt" ] || [ -f "pytest.ini" ]; then python -m pytest; fi

# Update context map
if [ -f "scripts/pack_context.sh" ]; then bash scripts/pack_context.sh; fi
