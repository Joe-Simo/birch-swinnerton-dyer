"""Jev BSD Genius: specialized AI triage and hypothesis screening for Birch–Swinnerton-Dyer.

Screens research candidates against known BSD bottlenecks and mathematical traps:
1. Finite Selmer vs. corank conflation (finite Sel_2 dimension does not equal rank).
2. Duality vs. semisimplicity (anti-Hermitian duality alone cannot rule out higher blocks).
3. Central vanishing vs. exact higher analytic order (L(1)=0 does not certify L''(1)!=0).
4. Howard derived-height nondegeneracy scope.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "code"))
import jev


def build_questions() -> dict[str, dict[str, Any]]:
    return {
        "avoids_selmer_rank_conflation": jev.noul(
            "Does the argument avoid equating finite-level Selmer dimension (e.g. dim Sel_2) with Mordell-Weil rank?",
            true="Explicitly accounts for the difference r = dim Sel_2 - dim E[2] - dim Sha[2], or only claims an inequality",
            false="Assumes or implies that positive finite Selmer dimension implies positive rank without checking Sha"
        ),
        "avoids_duality_semisimplicity_trap": jev.noul(
            "Does the hypothesis avoid assuming that anti-Hermitian duality alone forces length equal to specialized dimension?",
            true="Recognizes paired skew-symmetric blocks can double determinant order while preserving duality",
            false="Claims duality or parity forces semisimplicity or eliminates higher augmentation blocks"
        ),
        "higher_order_certification": jev.choice(
            "How does the proposal handle curves with L(E,1) = 0 and even sign?",
            criteria={
                "explicit_derivative": "Proposes explicit computation or bound for L''(E,1) to certify order 2",
                "parity_only": "Relies solely on root number without certifying the second derivative is nonzero",
                "unaddressed": "Does not address curves with analytic order >= 2"
            }
        ),
        "viability_score": jev.score(
            "Score the research candidate's rigor and potential for BSD progress",
            criteria=[
                "Mathematically sound, explicit hypotheses, respects proven barriers",
                "Clear proof path, relies on established external theorems with stated scope",
                "Exploratory but contains identifiable gaps or unverified dependencies",
                "Contains a known fatal flaw, circularity, or unproved shortcut"
            ]
        )
    }


def screen_candidate(candidate_id: str, text: str) -> dict[str, Any]:
    questions = build_questions()
    state = {
        "project": "Birch–Swinnerton-Dyer",
        "target": "ord_(s=1) L(E,s) = rank_Z E(Q)",
        "candidate_id": candidate_id,
        "proposal_text": text
    }
    resp = jev.ask(state, questions)
    jev.persist(candidate_id, state, questions, resp)
    return resp


def main() -> None:
    parser = argparse.ArgumentParser(description="Jev BSD Hypothesis Screener")
    parser.add_argument("command", choices=["screen", "cache-stats", "clear-cache"])
    parser.add_argument("--id", default="candidate", help="Candidate identifier")
    parser.add_argument("--text", help="Candidate text or hypothesis summary")
    args = parser.parse_args()

    if args.command == "cache-stats":
        print(json.dumps(jev.cache_stats(), indent=2))
        return
    elif args.command == "clear-cache":
        count = jev.clear_cache()
        print(f"Cleared {count} cache entries")
        return
    elif args.command == "screen":
        if not args.text:
            print("Error: --text required for screen", file=sys.stderr)
            sys.exit(1)
        res = screen_candidate(args.id, args.text)
        print(json.dumps(res, indent=2))


if __name__ == "__main__":
    main()
