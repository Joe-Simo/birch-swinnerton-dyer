"""Pairwise combination & salvage screener for Birch–Swinnerton-Dyer using Jev.

Evaluates:
1. Pairwise synergy: which candidate pairs are mathematically compatible and compensate for each other's gaps.
2. Salvage: extracts genuinely proved, reusable sub-lemmas from refuted or blocked routes.
"""
from __future__ import annotations

import itertools
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "code"))
import jev
import pool

COMBINE_QUESTIONS = {
    "compatibility": jev.noul(
        "Are these two BSD candidates mathematically compatible without contradictory hypotheses?",
        true="Compatible frameworks that can be combined into a hybrid approach",
        false="Contradictory assumptions (e.g. CM vs general, conflicting rank regimes)"
    ),
    "combination_value": jev.score(
        "How much value does combining these two candidates create?",
        [
            "level 0: no synergy; combining them solves nothing new",
            "level 1: minor computational convenience",
            "level 2: one candidate's output directly supplies the other's missing input",
            "level 3: breakthrough synergy that bypasses a major bottleneck (e.g. higher blocks or rank upper bound)"
        ]
    ),
    "shared_failure_mode": jev.choice(
        "Do both candidates share a common underlying failure mode?",
        criteria={
            "none": "Orthogonal failure modes; one may succeed where the other fails",
            "selmer_trap": "Both rely on equating Selmer dimension to rank",
            "duality_trap": "Both assume duality forces semisimplicity",
            "derivative_trap": "Both rely on uncertified higher derivatives"
        }
    )
}

SALVAGE_QUESTIONS = {
    "reusable_theorems": jev.noul(
        "Does this artifact contain genuinely proved, reusable mathematical lemmas despite its status?",
        true="Contains verified sub-lemmas, explicit formulas, or exact computational invariants",
        false="Entirely heuristic or invalid; nothing salvageable"
    ),
    "salvage_category": jev.choice(
        "What type of reusable component is extracted?",
        criteria={
            "algebraic_lemma": "General algebraic or matrix lemma (e.g. Lemma A, Lemma B)",
            "descent_data": "Exact point coordinates and verified Kummer square classes",
            "modular_bound": "Exact modular coefficients or conductor bounds",
            "none": "No salvageable component"
        }
    )
}


def run_pairwise_screen():
    db = pool.load()
    cands = [c for c in db["candidates"] if c.get("status") in ("ACTIVE", "PROMISING")]
    pairs = list(itertools.combinations(cands, 2))
    print(f"Running Jev pairwise combination screen over {len(pairs)} candidate pairs...")

    states = []
    for c1, c2 in pairs:
        states.append({
            "project": "Birch–Swinnerton-Dyer Pairwise Synthesis",
            "candidate_1": f"{c1['id']}: {c1['claim']}",
            "candidate_2": f"{c2['id']}: {c2['claim']}"
        })

    results = jev.ask_many(states, COMBINE_QUESTIONS, concurrency=12)
    for (c1, c2), res in zip(pairs, results):
        if "error" in res:
            continue
        answers = res.get("answers", {})
        score_val = answers.get("combination_value", {}).get("score", 0)
        compat = answers.get("compatibility", {}).get("noul", 0)
        print(f"[{c1['id']} + {c2['id']}] Compat: {compat:.2f} | Value: {score_val:.2f} | Shared Trap: {answers.get('shared_failure_mode',{}).get('choice','')}")



def run_salvage_screen():
    db = pool.load()
    print("\nRunning Jev Salvage extraction on all candidate artifacts...")
    states = []
    for c in db["candidates"]:
        states.append({
            "project": "Birch–Swinnerton-Dyer Reusable Sub-Lemma Salvage",
            "candidate_id": c["id"],
            "claim": c["claim"],
            "extracted": "; ".join(c.get("extracted", []))
        })
    results = jev.ask_many(states, SALVAGE_QUESTIONS, concurrency=12)
    for c, res in zip(db["candidates"], results):
        if "error" in res:
            continue
        ans = res.get("answers", {})
        reusable = ans.get("reusable_theorems", {}).get("noul", 0)
        category = ans.get("salvage_category", {}).get("choice", "none")
        print(f"[{c['id']}] Reusable Score: {reusable:.2f} | Category: {category} | Items: {', '.join(c.get('extracted', []))}")


def main():
    run_pairwise_screen()
    run_salvage_screen()


if __name__ == "__main__":
    main()

