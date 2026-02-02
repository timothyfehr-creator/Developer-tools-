---
description: Explain code in plain language
argument-hint: [file or function name]
allowed-tools: Read, Glob, Grep
---

Explain the following code: $ARGUMENTS

1. Find and read the specified file or function.
2. Explain what it does in plain language suitable for a new team member.
3. Cover:
   - **Purpose**: What problem does this code solve?
   - **Key data flows**: What goes in, what comes out, what gets transformed?
   - **Non-obvious behavior**: Edge cases, side effects, implicit dependencies.
   - **How it fits**: Where does this sit in the broader architecture?
