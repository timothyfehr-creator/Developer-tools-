#!/usr/bin/env python3
"""Pre-PR checklist: run all checks before creating a pull request."""
import json
import shutil
import subprocess
import sys
from pathlib import Path


def run(cmd):
    """Run command, return success bool."""
    try:
        r = subprocess.run(cmd, capture_output=True, timeout=300)
        return r.returncode == 0
    except (subprocess.TimeoutExpired, FileNotFoundError, OSError):
        return False


def can_run(cmd):
    """Check if command exists."""
    if cmd[0] == "bash":
        return Path(cmd[1]).exists() if len(cmd) > 1 else False
    if cmd[0] == "npm":
        return shutil.which("npm") is not None and Path("package.json").exists()
    return shutil.which(cmd[0]) is not None


def detect_langs():
    """Detect project languages from marker files."""
    langs = set()
    if any(Path(f).exists() for f in ["pytest.ini", "pyproject.toml", "requirements.txt"]):
        langs.add("python")
    if Path("tsconfig.json").exists():
        langs.add("typescript")
    elif Path("package.json").exists():
        try:
            pkg = json.loads(Path("package.json").read_text())
            deps = {**pkg.get("dependencies", {}), **pkg.get("devDependencies", {})}
            if "typescript" in deps:
                langs.add("typescript")
        except (json.JSONDecodeError, OSError):
            pass
    return langs


def main():
    langs = detect_langs()
    print(f"Detected: {', '.join(sorted(langs)) or 'unknown'}\n")

    # Build checks: (name, cmd)
    checks = []
    if "python" in langs:
        checks.append(("Python tests", ["python", "-m", "pytest", "-q", "--tb=no"]))
        checks.append(("Python lint", ["ruff", "check", "."]))
    if "typescript" in langs:
        checks.append(("TypeScript tests", ["npm", "test", "--", "--run"]))
        checks.append(("TypeScript lint", ["npm", "run", "lint"]))

    checks.append(("Secrets check", ["bash", "scripts/validate_secrets.sh"]))
    checks.append(("Commit check", ["bash", "scripts/validate_commit.sh", "--staged"]))

    # Run checks
    passed = failed = skipped = 0
    for name, cmd in checks:
        if not can_run(cmd):
            print(f"- {name} (skipped: {cmd[0]} not found)")
            skipped += 1
            continue

        ok = run(cmd)
        sym = "\u2713" if ok else "\u2717"
        print(f"{sym} {name}")

        if ok:
            passed += 1
        else:
            failed += 1

    # Summary
    total = passed + failed
    print()
    if failed == 0:
        print(f"{passed}/{total} checks passed. Ready for PR!")
    else:
        print(f"{passed}/{total} checks passed. Fix failures before PR.")
    if skipped:
        print(f"({skipped} skipped)")

    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
