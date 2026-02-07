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
- **.cursorrules** — Mirror of CLAUDE.md for Cursor IDE
- **.coderabbit.yaml** — Automated PR review config
- **.gitignore** — Comprehensive ignores (Python, Node, secrets, AI artifacts)
- **.env.example** — Template for required environment variables
- **CI workflows** — GitHub Actions for your chosen language
- **docs/memory/** — Session memory bank (active context, decisions, patterns)
- **docs/DEBT.md** — Tracker for intentionally accepted technical debt
- **.github/PULL_REQUEST_TEMPLATE.md** — PR template with technical debt awareness
- **.claude/** — Claude Code commands (`/review`, `/implement`, `/audit`, `/explain`, `/health`), hooks, and MCP settings
- **scripts/pack_context.sh** — Generates a file tree map for AI context

## Supported Languages

- **Python** — pytest, ruff, venv setup
- **TypeScript** — vitest, eslint, strict tsconfig
- **Both** — all of the above

## Updating Standards

Run `sync.sh` in an existing project to pull the latest CONTRIBUTING.md, PR template, and optionally refresh .cursorrules and context map:

```bash
bash /path/to/Developer-tools-/sync.sh
```

## Claude Code Commands

After scaffolding, use these in Claude Code:

| Command | Description |
|---------|-------------|
| `/review` | Review last commit against CONTRIBUTING.md |
| `/implement [feature]` | Implement, test, and commit a feature |
| `/audit` | Find bugs ranked by severity |
| `/health` | Assess codebase structural health and surface technical debt |
| `/explain [file]` | Explain code in plain language |

## Technical Debt Management

Scaffolded projects include built-in support for tracking and managing technical debt:

- **`/health` command** — Analyzes the most-changed files for complexity hotspots, scans for TODO/FIXME/HACK markers, checks dependency freshness, and flags documentation gaps. Produces a prioritized report with severity levels and actionable next steps.
- **`docs/DEBT.md`** — A simple table for logging intentionally accepted debt with rationale, owner, and review-by date. The `/health` command reads this to avoid re-flagging accepted items.
- **PR template** — Every pull request prompts contributors to declare whether it introduces, reduces, or avoids technical debt.
- **CI dependency auditing** — `pip-audit` (Python) and `npm audit` (TypeScript) run automatically in CI and fail the build on high/critical vulnerabilities.
- **CodeRabbit rules** — Automated PR reviews flag long functions (>100 lines), large files (>500 lines), new debt markers, and unjustified dependency additions.

## File Structure

```
templates/common/    — shared files for all projects
templates/python/    — Python-specific config and CI
templates/typescript/ — TypeScript-specific config and CI
claude/              — Claude Code settings, commands, and hooks
scripts/             — utility scripts (pack_context.sh)
```
