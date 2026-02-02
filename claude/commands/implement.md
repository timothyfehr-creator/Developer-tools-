---
description: Implement feature, test, commit if green
argument-hint: [feature description]
---

Implement the following feature: $ARGUMENTS

Steps:
1. Read CLAUDE.md to understand the project context, tech stack, and conventions.
2. Plan the implementation — identify which files to create or modify.
3. Write the code, following CONTRIBUTING.md standards.
4. Run the test command from CLAUDE.md.
5. If tests pass, commit with conventional commit format: `feat: description` (scope optional).
6. If tests fail, read the error output, fix the code, and retry (max 3 attempts).
7. If still failing after 3 attempts, report what went wrong and leave the code uncommitted.

Always update `docs/memory/active_context.md` with what was implemented.
