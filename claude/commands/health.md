---
description: Assess codebase structural health and surface technical debt
allowed-tools: Read, Bash(git:*), Grep, Glob
---

Perform a focused codebase health check. This is NOT a bug hunt (use `/audit` for that). This surfaces **structural problems**: complexity hotspots, staleness, documentation gaps, and accumulating debt.

## Step 1: Identify Hotspots

Run `git log --format=format: --name-only --since="90 days ago" | sort | uniq -c | sort -rn | head -15` to find the most-changed files. These are where debt hurts most — high churn means high interest payments.

## Step 2: Inspect Hotspot Files

Read each of the top 10-15 most-changed files. For each, assess:

- **Size**: Files over 300 lines or functions over 50 lines suggest poor separation of concerns
- **Nesting depth**: More than 4 levels of nesting suggests refactoring is needed
- **Responsibility count**: Does this file/class do too many unrelated things?
- **Clarity**: Could a new team member understand this without a walkthrough?

## Step 3: Scan for Debt Markers

Search the codebase for `TODO`, `FIXME`, `HACK`, `XXX`, and `WORKAROUND` comments. Count them and note clusters — a file with 5+ markers is a red flag.

## Step 4: Check Dependency Freshness

Read `package.json`, `requirements.txt`, `Gemfile`, or equivalent. Note:
- Any pinned versions more than 2 major versions behind current
- Any dependencies that look unused (not imported anywhere)
- Do NOT run `npm audit` or `pip-audit` — that belongs in CI, not here

## Step 5: Documentation Gaps

Check for:
- Missing or stub README
- Missing setup/install instructions
- `CLAUDE.md` with unfilled template placeholders
- Public-facing modules with no docstrings or comments on non-obvious logic

## Step 6: Check Accepted Debt

Read `docs/DEBT.md` if it exists. Any items listed there are **intentionally accepted** — note them but do not flag them as findings. Flag any with a past review-by date as overdue.

## Output Format

Produce a ranked inventory:

```
# Codebase Health Report

**Repository**: [name]
**Date**: [date]
**Hotspot files analyzed**: [count]

## Findings

### [CRITICAL/HIGH/MEDIUM/LOW] — Short description
- **File**: path/to/file.ext:line
- **What**: Concrete description of the problem
- **Why it matters**: Impact on development velocity, bug risk, or onboarding
- **Suggested action**: Specific next step (not "refactor this")

[Repeat for each finding, ordered by severity]

## Debt Markers Summary
- TODOs: [count]
- FIXMEs: [count]
- HACKs: [count]
- Clusters: [list files with 3+ markers]

## Accepted Debt Status
- [count] items in DEBT.md
- [count] overdue for review
```

**Ranking guidance** (use qualitative judgment, not formulas):
- **CRITICAL**: Actively blocking work or causing repeated bugs
- **HIGH**: Slowing down every sprint — high-churn files with poor structure
- **MEDIUM**: Will become a problem as the codebase grows
- **LOW**: Worth noting but not urgent

Keep the report concise. 10-15 findings maximum. Prioritize actionability over completeness.
