# Contributing & Development Standards

These rules apply to all contributors — human or AI. They are enforceable constraints, not suggestions.

## Mission Discipline

- **Anchor on the project's stated purpose.** Prefer changes that improve the project's core decision-making or primary output — not changes that merely make the system more general, sophisticated, or impressive.
- **Treat the project's purpose and non-goals as constraints.** Before adding major new capability, ask: does this improve the thing the project exists to produce, or is it infrastructure/optionality nobody asked for?
- **If the goal is unclear and the change could materially broaden scope, stop and clarify** before building. Mission drift is the most common failure mode when iterating with AI.
- **Within scope, be thorough — but don't expand scope.** Boil the lake (full coverage of changed behavior, invariants, failure modes); flag oceans (full system rewrites) as out of scope.

## Commit Rules

- **Size commits by complexity and blast radius, not line count.** As a default heuristic, target ≤500 lines added and ≤8 files changed per commit — but exceed these freely for low-complexity additions (new schema definitions, fixtures, generated code) and tighten them for high-blast-radius changes (cross-layer edits, production logic, shared utilities). 50 lines touching the production function, the procurement model, and test fixtures is too much for one commit; 500 lines of new schema in one file is fine.
- **Each commit does one logical thing.** Separate refactors from behavior changes. Split cross-layer changes only when each commit is independently correct and green.
- **Every commit must leave the codebase green** — relevant tests pass and a representative smoke path runs. Full pipeline runs are not required on every commit.
- **Commit messages use conventional format:** `feat:`, `fix:`, `refactor:`, `docs:`, `test:`, `chore:`.
- **Message body explains WHY, not WHAT.** The diff shows what changed. The message says why.
- **No empty or ceremony commits.** Every commit must contain meaningful work.
- **Docs updates go in the same commit as the feature**, not as a separate follow-up commit.

## Branch & PR Rules

- **One feature per branch.** Don't combine unrelated changes.
- **PRs should be under 1,000 lines.** If larger, split into stacked PRs that each stand alone.
- **Branch names use format:** `feat/short-description`, `fix/short-description`, `refactor/short-description`.
- **Delete branches after merge.** No stale branches lingering.

## Code Quality

- **Tests must pass before committing.** Verify green before every push.
- **No silent error swallowing.** Every `except` block must either log the error, re-raise, or return a value that the caller explicitly handles. Never `except: pass`.
- **Graceful degradation over hard crashes.** External dependencies (APIs, websites, files) will fail. Code must warn and fall back to defaults, not raise and kill the pipeline.
- **Math must be verified.** Any computation involving probabilities, rates, or time conversions should have a unit test that checks the actual math with known inputs/outputs.
- **Frontend and backend types must match.** If the backend emits a field, the frontend TypeScript interface must declare it. If a field is renamed or added on one side, update the other in the same commit.
- **No dead code.** No unused imports, no unused constants, no commented-out blocks, no "TODO: remove later." Delete it or use it.

## Search Before Building

For substantive new logic, unfamiliar methods, or material assumption changes, search before writing:

1. **Local patterns** — search the current repo for existing implementations, conventions, and utilities before writing anything new.
2. **Standard patterns** — for code, check well-known libraries. For domain models, check established methodologies in the relevant literature.
3. **Recent best practices** — evaluate newer approaches critically.
4. **First-principles** — only go custom when you understand why existing approaches fail.

Small fixes and mechanical changes do not require this process.

## Testing

- **Unit tests for logic.** Any function with branching, math, or state transitions gets a unit test with known inputs and expected outputs.
- **Integration tests for pipelines.** End-to-end flows (ingest → extract → compile → simulate) get at least one happy-path integration test.
- **No tests that call external APIs.** Mock all HTTP calls. Tests must pass offline and in CI without credentials.
- **Tests must be deterministic.** Seed all randomness. No flaky tests that pass sometimes.
- **Test the error paths, not just the happy path.** Missing data, malformed input, network failures, empty responses.

## Reproducibility

Persisted artifacts from Monte Carlo, scenario, or LLM-assisted pipelines must record:

- **RNG seed(s)** used.
- **Config/version hash or run manifest.**
- **As-of date** for any external data fetched. Record immutable snapshot IDs, raw artifact paths, or content hashes when available.
- **Code version** (commit SHA or tag).
- **For LLM-assisted steps:** model name, model version, prompt version, and temperature.

In code: no unseeded RNG, no unpinned external data fetches in deterministic pipelines, no state mutations of frozen structures, and no magic numbers without source citations.

## Dependencies

- **Don't add dependencies without justification.** Every new package in requirements.txt or package.json needs a reason. Prefer standard library when possible.
- **Pin major versions.** Use `>=2.31.0,<3.0.0` not just `>=2.31.0` to avoid surprise breaking changes.
- **No unused dependencies.** If you remove code that used a package, remove the package too.

## Secrets & Security

- **Never commit secrets.** No API keys, tokens, passwords, or credentials in the repo. Use environment variables and `.env` files.
- **`.env` must be in `.gitignore`.** Always. No exceptions.
- **Use `.env.example` for templates.** Show what variables are needed without the actual values.
- **No hardcoded URLs with API keys** in source code. Externalize to config or environment.

## Data Resilience

- **Every external fetcher must have retry logic** with exponential backoff (minimum 3 retries).
- **Every fetcher must have a timeout** (max 30s for HTTP requests).
- **Staleness detection must compare against current time**, not against the fetch timestamp itself.
- **Missing data must produce a warning and a fallback**, not a crash. Pipelines must be runnable with partial data.

## Epistemic Discipline

- **Never fabricate data or parameters.** If a value is unknown, flag it — do not estimate silently.
- **Distinguish clearly between model assumptions, empirical inputs, and outputs.** Label each.
- **Source-cite every parameter** in economic, political, or scientific models — or tag it `ASSUMED — needs calibration`.
- **Prefer ranges or distributions** when uncertainty is material. State units, base year, as-of date, and baseline/counterfactual for every scenario comparison. Do not report more precision than the inputs justify.
- **Do not tune assumptions to make a preferred scenario win.** Label parameter changes as source-driven, calibration-driven, or exploratory.

## Metrics & Model Integrity

- **Aggregate metrics must be meaningful.** Don't OR together categorically different events into a single rate. Split by tier or weight by impact.
- **Every probability in the output should be sanity-checked.** If a key event rate exceeds 80%, verify that it represents something real and not a modeling artifact.
- **Label fields accurately.** Field names must describe what they actually contain, not what they were copied from.

## AI-Specific Rules

- **No AI scaffolding in the repo.** No skill files, agent briefings, migration handoffs, swarm docs, or model-specific instructions. These belong in prompts, not in version control.
- **CLAUDE.md is the only exception** — it provides project context for Claude Code sessions and must be kept concise and accurate.
- **Review every diff before committing.** If using AI to generate code, the diff must be read and understood before it is committed. The review agent (or human) must explicitly approve.
- **AI-generated code is not trusted by default.** Treat it as a junior engineer's PR — assume subtle bugs exist and look for them actively.
- **Never claim a failure is "not related to our changes" without proving it on the base branch.**

## LLM Pipeline Discipline

- **When changing prompts, models, temperatures, or extractors, version the change** and run fixture/gold-set checks — or create a minimal fixed evaluation set — before trusting new outputs.
- **Flag cost implications before adding LLM API calls or expanding prompts.**

## Review Checklist

Before any commit is approved, verify:

1. [ ] **Mission alignment** — change improves the project's core output, not just adds optionality
2. [ ] Tests pass
3. [ ] **Commit scoped to one logical thing**, sized by complexity (heuristic: ≤500 lines / ≤8 files unless low-complexity additions like schema or fixtures)
4. [ ] No dead code or unused imports introduced
5. [ ] Frontend/backend types are consistent
6. [ ] Error handling is present for all external calls
7. [ ] Metrics and computed values make semantic sense
8. [ ] Field names accurately describe their contents
9. [ ] **Reproducibility manifest present** for persisted artifacts (seeds, code SHA, as-of date, LLM version where applicable)
10. [ ] **Schema changes are backward-compatible** with existing serialized data, or migration steps are explicit
11. [ ] **Sensitivity check** for modeling work — key results robust to reasonable input perturbations
12. [ ] **Parameters source-cited or tagged `ASSUMED`** — no silently fabricated values
13. [ ] No secrets, credentials, or .env files included
14. [ ] No AI artifacts or scaffolding included
15. [ ] New dependencies are justified and version-pinned
16. [ ] Tests cover error paths, not just happy paths
