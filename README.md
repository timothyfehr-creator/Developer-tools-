# Developer Tools

A reusable project scaffolding and lifecycle management toolkit for AI-assisted development.

## Quick Start

Scaffold a new project without cloning this repo:

```bash
bash <(curl -sL https://raw.githubusercontent.com/timothyfehr-creator/Developer-tools-/main/init.sh)
```

Or clone and run locally:

```bash
git clone https://github.com/timothyfehr-creator/Developer-tools-.git
cd Developer-tools-
./init.sh /path/to/new-project
```

## What It Does

`init.sh` interactively creates a project directory with:

- **CLAUDE.md** — AI context file with project-specific info
- **CONTRIBUTING.md** — Enforced development standards
- **.coderabbit.yaml** — Automated PR review config
- **.gitignore** — Comprehensive ignores (Python, Node, secrets, AI artifacts)
- **.env.example** — Template for required environment variables
- **CI workflows** — GitHub Actions for your chosen language
- **docs/memory/** — Session memory bank (active context, decisions, patterns)
- **.claude/** — Claude Code commands (`/review`, `/implement`, `/audit`, `/explain`) and hooks
- **scripts/pack_context.sh** — Generates a file tree map for AI context
- **scripts/pre_pr.py** — Pre-PR checklist (tests, lint, secrets, diff size)
- **scripts/check_deps.py** — Check dependencies are pinned to exact versions
- **scripts/validate_*.sh** — Structural validation scripts

## Supported Languages

- **Python** — pytest, ruff, venv setup
- **TypeScript** — vitest, eslint, strict tsconfig
- **Both** — all of the above

## Updating Standards

Run `sync.sh` in an existing project to pull the latest CONTRIBUTING.md and optionally refresh the context map:

```bash
bash /path/to/Developer-tools-/sync.sh
```

## Pre-PR Checklist

Before creating a pull request, run the pre-PR checklist:

```bash
python scripts/pre_pr.py
```

This runs all checks and reports pass/fail:

```
Detected: python

✓ Python tests
✓ Python lint
✓ Secrets check
✓ Commit check

4/4 checks passed. Ready for PR!
```

The script auto-detects your project language and runs appropriate checks. Missing tools are skipped gracefully.

## Dependency Pinning Check

Ensure all dependencies are pinned to exact versions for reproducible builds:

```bash
python scripts/check_deps.py
```

Example output:

```
Found 2 unpinned dependencies:

  ✗ requirements.txt: requests (not pinned)
  ✗ package.json: lodash@^4.17.0 (semver range)

Pin versions for reproducible builds.
```

## Claude Code Commands

After scaffolding, use these in Claude Code:

| Command | Description |
|---------|-------------|
| `/review` | Review last commit against CONTRIBUTING.md |
| `/implement [feature]` | Implement, test, and commit a feature |
| `/audit` | Find bugs ranked by severity |
| `/explain [file]` | Explain code in plain language |

## File Structure

```
templates/common/    — shared files for all projects
templates/python/    — Python-specific config and CI
templates/typescript/ — TypeScript-specific config and CI
claude/              — Claude Code settings, commands, and hooks
scripts/             — utility scripts (pre_pr.py, check_deps.py, validate_*.sh, pack_context.sh)
```
