---
description: Find bugs ranked by severity
---

Audit the entire codebase for bugs. **Assume AI-generated code has subtle bugs. Treat every file as an untrusted junior engineer's PR.**

Systematically check for these bug categories:

1. **Silent error swallowing** — `except: pass`, empty catch blocks, ignored Promise rejections
2. **Off-by-one errors** — in loops, slices, ranges, array indexing
3. **Race conditions** — in async/concurrent code, shared mutable state
4. **Unvalidated external inputs** — user input, API responses, file reads
5. **Hardcoded secrets or credentials** — API keys, passwords, tokens in source
6. **Missing null/undefined checks** — accessing properties on potentially null values
7. **Incorrect type coercions** — string-to-number, truthy/falsy surprises
8. **Stale cache or state after mutations** — UI not reflecting data changes
9. **Wrong units in calculations** — seconds vs milliseconds, bytes vs kilobytes
10. **Dead code paths that mask bugs** — unreachable branches hiding logic errors

Output a ranked list using severity levels: **CRITICAL** / **HIGH** / **MEDIUM** / **LOW**.
Each finding must include `file:line` references and a brief explanation.
