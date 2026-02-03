#!/usr/bin/env python3
"""Check that dependencies are pinned to exact versions."""
import json
import sys
from pathlib import Path


def check_requirements_txt():
    """Check Python requirements.txt for unpinned deps."""
    issues = []
    path = Path("requirements.txt")
    if not path.exists():
        return issues

    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or line.startswith("-"):
            continue
        # Pinned: package==1.2.3 or package>=1.2.3,<2.0
        if "==" not in line and ">=" not in line:
            pkg = line.split("[")[0]  # handle extras like requests[security]
            issues.append(("requirements.txt", pkg, "not pinned"))

    return issues


def check_package_json():
    """Check package.json for semver ranges."""
    issues = []
    path = Path("package.json")
    if not path.exists():
        return issues

    try:
        pkg = json.loads(path.read_text())
    except json.JSONDecodeError:
        return [("package.json", "N/A", "invalid JSON")]

    for section in ["dependencies", "devDependencies"]:
        for name, version in pkg.get(section, {}).items():
            # Unpinned: ^1.0.0, ~1.0.0, >=1.0.0, *, latest
            if version.startswith(("^", "~", ">", "<", "*")) or version == "latest":
                issues.append(("package.json", f"{name}@{version}", "semver range"))

    return issues


def main():
    issues = check_requirements_txt() + check_package_json()

    if not issues:
        print("\u2713 All dependencies are pinned")
        sys.exit(0)

    print(f"Found {len(issues)} unpinned dependencies:\n")
    for source, pkg, reason in issues:
        print(f"  \u2717 {source}: {pkg} ({reason})")
    print("\nPin versions for reproducible builds.")
    sys.exit(1)


if __name__ == "__main__":
    main()
