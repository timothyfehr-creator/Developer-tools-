# Review: Technical Debt Manager (aitmpl.com Agent Template)

**Source**: https://www.aitmpl.com/component/agent/technical-debt-manager
**Reviewed**: 2026-02-07
**Rating**: 7/10

## What It Is

An AI agent prompt template that defines a "Technical Debt Manager" — a system prompt for an AI assistant specialized in codebase health analysis, debt quantification, prioritization, and refactoring planning. It targets engineering teams using AI-assisted development workflows.

## Summary

The template covers the full debt management lifecycle across 7 categories (Code Quality, Test, Documentation, Dependency, Design, Infrastructure, Performance), with a severity scoring formula, prioritization framework, deliverable templates, and communication guidelines for different stakeholders.

---

## Strengths

### 1. Comprehensive Categorization Framework
The 7-category taxonomy is thorough and well-aligned with industry standards. Each category includes concrete detection methods and tooling suggestions — not just theory. This gives an AI agent (or human) a structured checklist to work from.

### 2. Pragmatic Prioritization Model
The severity formula `(Change Frequency × Bug Density × Complexity) / Test Coverage` is a reasonable proxy for engineering pain. Weighting by change frequency is smart — debt in rarely-touched code is cheap debt. The four priority levels (Critical/High/Medium/Low) with clear criteria make triage actionable.

### 3. Communication Guidelines (Best Section)
The section on framing findings for different audiences — engineers, managers, product — is the most valuable part. Most debt tools dump metrics. This one teaches the agent to translate metrics into business language:
- Engineers: "This module is a hotspot for bugs"
- Managers: "Reduces bug fix time by 2 days per sprint"
- Product: "QA cycles drop from 3 days to 1 day"

This is how debt work actually gets funded.

### 4. Production-Ready Deliverable Templates
The output templates (inventory report, sprint-ready work items, quarterly roadmap, metrics dashboard) are well-structured. They could be imported directly into Jira, Linear, or GitHub Projects with minimal adaptation.

### 5. Prevention-First Mindset
The proactive section (pre-commit hooks, CI quality gates, review checklists, Definition of Done enhancements) shows maturity. Most debt templates focus only on remediation. Including a PR template addition for debt impact is a practical touch.

### 6. Fowler Quadrant Integration
Referencing the Reckless/Prudent × Deliberate/Inadvertent quadrant provides a shared vocabulary for teams discussing debt trade-offs.

---

## Weaknesses

### 1. Severity Formula Is Fragile
- Division by test coverage: 0% coverage → infinity, causing low-coverage files to dominate rankings regardless of actual risk
- A file with 1% coverage, zero complexity, and no recent changes would outscore genuinely dangerous hotspots
- No normalization, floor values, or weighting adjustments
- Bug density data is often unavailable (requires issue tracker integration)

**Fix**: Add floor values (e.g., min coverage = 10%), normalize each factor to 0-1, and make the formula configurable per team.

### 2. Analysis Workflow Assumes Ideal Setup
The bash-heavy Steps 1-5 assume:
- `cloc`, `eslint`, `pytest`, `npm audit`, etc. are installed and configured
- `node_modules` exists (required for `npm audit`)
- Standard project layouts (fails on monorepos, workspaces, Nx/Turborepo)
- Local environment matches CI

No fallback paths or graceful degradation when tools are missing.

**Fix**: Add a discovery phase that detects available tooling first, then adapts the workflow accordingly.

### 3. Narrow Language Coverage
Tooling examples lean heavily on JavaScript/Python/Ruby. Missing:
- Go (staticcheck, golangci-lint)
- Rust (clippy, cargo-audit)
- Java/Kotlin (SpotBugs, Checkstyle, OWASP dependency-check)
- C# (.NET analyzers, dotnet-outdated)
- Swift (SwiftLint)

For a general-purpose template, this limits applicability.

### 4. No Concept of "Accepted Debt"
All debt is framed as something to reduce. In practice, some debt is strategic:
- A prototype proving market fit
- A workaround for a vendor bug with a known fix date
- Intentional shortcuts with documented expiration dates

The closing line acknowledges this philosophically, but the workflow doesn't operationalize it — there's no mechanism to tag debt as "accepted" with a rationale and review date.

### 5. Missing Effort Estimation Methodology
Deliverable templates show "Estimated Effort: Y days" but provide no guidance on *how* to estimate. This is a hard problem (complexity of the change, team familiarity, test requirements, risk of regressions), and without a methodology, roadmaps risk being aspirational.

### 6. Naive Git Churn Analysis
`git log --name-only | sort | uniq -c` counts file touches, not meaningful changes. Files frequently reformatted, touched by dependency bumps, or modified by automated tools will show high churn without representing real debt. Better approaches:
- Filter to non-trivial diffs (e.g., > 5 lines changed)
- Correlate with bug-fix commits (conventional commit messages or linked issues)
- Weight by lines changed, not just touch count

### 7. Metrics Targets Presented as Universal
"Test coverage < 80%" and "Cyclomatic complexity > 15" are reasonable defaults, but presented as absolutes. Context matters:
- A data pipeline with 60% coverage and excellent integration tests may be healthier than a CRUD app with 90% coverage on trivial getters
- A DSL parser will naturally have higher complexity than a REST controller
- Different languages have different complexity norms

### 8. No Programmatic Integration
For all the talk of "sprint-ready work items," the output is Markdown. A production-grade debt manager would push items to GitHub Issues, Jira, or Linear via API — or at minimum provide structured JSON output that automation can consume.

---

## Compatibility with This Repository (Developer-tools-)

This repo already has overlap with the template's goals:

| Capability | Developer-tools- | Debt Manager Template |
|---|---|---|
| Code quality standards | CONTRIBUTING.md | Category 1 (Code Quality) |
| Commit-level review | `/review` command | Not covered (holistic, not per-commit) |
| Bug detection | `/audit` command | Category 1 + Severity scoring |
| CI quality gates | ci.yml workflows | Proactive Prevention section |
| Test standards | CONTRIBUTING.md | Category 2 (Test Debt) |
| Dependency management | Not explicit | Category 4 (Dependencies) |
| Architecture review | Not covered | Category 5 (Design Debt) |

**Complementary value**: The debt manager adds periodic, holistic codebase analysis that the existing per-commit tools don't cover. It's a strategic layer on top of the tactical tools already in this repo.

**Integration opportunity**: The template's PR template addition and Definition of Done enhancements could be added to this repo's `templates/common/` directory.

---

## Recommendations for Adoption

1. **Use the categorization and communication frameworks as-is** — they're well-designed
2. **Replace the severity formula** with a normalized, configurable version
3. **Add a tooling discovery phase** before running analysis commands
4. **Extend language support** to match your team's stack
5. **Add "accepted debt" tracking** with rationale and review dates
6. **Output structured data** (JSON) alongside Markdown for automation
7. **Customize metric thresholds** per project type and team maturity

## Verdict

A solid reference architecture for AI-assisted technical debt management. Strong on frameworks, communication, and deliverable structure. Needs real-world hardening on the analysis workflow, formula robustness, and tooling breadth before running on production repositories.

Best used as a starting point to customize, not a drop-in solution.
