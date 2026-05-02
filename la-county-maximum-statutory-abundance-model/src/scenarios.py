"""
Scenario × variant composition.

Resolves a parameter dict by merging:
  base -> scenario override -> utility variant -> fiscal capture variant
"""

from __future__ import annotations
import json
from pathlib import Path
from typing import Dict, List, Tuple


def load_scenario_config(path: Path) -> dict:
    return json.loads(Path(path).read_text())


def load_baseline(path: Path) -> dict:
    return json.loads(Path(path).read_text())


def resolve_params(cfg: dict, scenario: str, util_variant: str, fiscal_variant: str) -> dict:
    if scenario not in cfg["scenarios"]:
        raise KeyError(f"Unknown scenario: {scenario}")
    if util_variant not in cfg["utility_variants"]:
        raise KeyError(f"Unknown utility variant: {util_variant}")
    if fiscal_variant not in cfg["fiscal_capture_variants"]:
        raise KeyError(f"Unknown fiscal capture variant: {fiscal_variant}")

    merged = dict(cfg["base"])
    merged.update(cfg["scenarios"][scenario])
    merged.update(cfg["utility_variants"][util_variant])
    merged.update(cfg["fiscal_capture_variants"][fiscal_variant])
    merged["scenario_id"] = scenario
    merged["utility_variant_id"] = util_variant
    merged["fiscal_capture_variant_id"] = fiscal_variant
    return merged


def all_scenario_combinations(cfg: dict) -> List[Tuple[str, str, str]]:
    combos = []
    for s in cfg["scenarios"]:
        for u in cfg["utility_variants"]:
            for f in cfg["fiscal_capture_variants"]:
                combos.append((s, u, f))
    return combos


def central_combinations(cfg: dict) -> List[Tuple[str, str, str]]:
    """Central util/fiscal pairing for the 6 scenarios — the headline view."""
    pairings = {
        "A_baseline": ("util_current_drag", "fcap_partial"),
        "B_moderate": ("util_current_drag", "fcap_partial"),
        "C_max_central": ("util_improved", "fcap_partial"),
        "D_max_high_build": ("util_improved", "fcap_high"),
        "E_max_drag": ("util_severe_bottleneck", "fcap_none"),
        "F_legal_collision": ("util_current_drag", "fcap_partial"),
    }
    return [(s, *pairings[s]) for s in pairings]
