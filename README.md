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
- **.claude/** — Claude Code commands (`/review`, `/implement`, `/audit`, `/explain`) and hooks
- **scripts/pack_context.sh** — Generates a file tree map for AI context (local-only, gitignored)

## Supported Languages

- **Python** — pytest, ruff, venv setup
- **TypeScript** — vitest, eslint, strict tsconfig
- **Both** — all of the above

## Updating Standards

Run `sync.sh` in an existing project to pull the latest CONTRIBUTING.md and Claude commands, and optionally refresh .cursorrules and context map:

```bash
bash /path/to/Developer-tools-/sync.sh /path/to/your-project
```

## Claude Code Commands

After scaffolding, use these in Claude Code:

| Command | Description |
|---------|-------------|
| `/review` | Review last commit against CONTRIBUTING.md |
| `/implement [feature]` | Implement, test, and commit a feature |
| `/audit` | Find bugs ranked by severity |
| `/explain [file]` | Explain code in plain language |

## Git Hooks

Scaffolded projects use `core.hooksPath` to run `.claude/hooks/` as git hooks. This means commit-size enforcement and test running apply to both Claude Code and human `git commit`.

**Skip tests for a single commit:**

```bash
SKIP_TESTS=1 git commit -m "wip: checkpoint"
```

Commit-size limits (500 lines / 8 files) always run and cannot be skipped.

**Note:** `core.hooksPath` overrides `.git/hooks/`. If you use a hook manager like husky or lefthook, you will need to either integrate `.claude/hooks/pre-commit.sh` into your manager's config, or disable `core.hooksPath`:

```bash
git config --unset core.hooksPath
```

## File Structure

```
templates/common/    — shared files for all projects
templates/python/    — Python-specific config and CI
templates/typescript/ — TypeScript-specific config and CI
claude/              — Claude Code commands and hooks
scripts/             — utility scripts (lib.sh, pack_context.sh)
```
