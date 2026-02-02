---
description: Review last commit against standards
allowed-tools: Read, Bash(git:*)
---

Review the last commit against CONTRIBUTING.md standards.

1. Run `git diff HEAD~1` to get the full diff.
2. Read `CONTRIBUTING.md` for the project standards.
3. Check every item on this checklist against the diff:

- [ ] Commit message follows conventional format (`type(scope): description`)
- [ ] Commit message subject is under 72 characters
- [ ] No commented-out code added
- [ ] No unused imports added
- [ ] No hardcoded secrets or credentials
- [ ] Error handling is present (no silent swallowing)
- [ ] New functions have appropriate tests
- [ ] No `console.log` / `print` debugging left in
- [ ] Types are correct (no `any` in TypeScript, no untyped params in Python)
- [ ] File names follow project conventions
- [ ] No unrelated changes bundled into the commit

Output a table with columns: Item | Status (PASS/FAIL) | Details.
For any FAIL, include `file:line` references.
