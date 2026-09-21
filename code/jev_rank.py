"""Standard per-candidate Jev triage and ranking for the Birch–Swinnerton-Dyer loop.

Usage:
    python3 code/jev_rank.py --selftest      # verify connectivity with live Jev
    python3 code/jev_rank.py --text "..."    # rank a specific mathematical claim/candidate
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "code"))
import jev

CONJECTURE = (
    "Birch and Swinnerton-Dyer Conjecture: For every nonsingular elliptic curve E over Q, "
    "ord_(s=1) L(E, s) = rank_Z E(Q). Current target work: testing congruent number family "
    "E_n: y^2 = x^3 - n^2 x, evaluating Tunnell modular forms, Monsky matrices / 2-descent, "
    "Burungale-Tian 2-converse, higher derivative certification L''(E,1) != 0, and Howard derived heights."
)

QUESTIONS = {
    "relevance": jev.score(
        "How directly does this candidate bear on Birch and Swinnerton-Dyer itself?",
        [
            "level 0: unrelated or peripheral, proving it does not advance BSD",
            "level 1: general elliptic curve arithmetic but resolves no rank or analytic order case",
            "level 2: settles analytic order or rank for a bounded family of curves",
            "level 3: establishes the BSD rank formula for an infinite family (e.g. all congruent curves)",
            "level 4: establishes the full BSD conjecture for all elliptic curves over Q"
        ]
    ),
    "novelty": jev.score(
        "How novel is the proposed mechanism compared to standard descent or known p-converse theorems?",
        [
            "level 0: identical mechanism to existing literature, differing only in numerical range",
            "level 1: standard descent or Euler system applied to a previously computed curve",
            "level 2: combines established theorems with a new algebraic bridge or nondegeneracy criterion",
            "level 3: introduces a genuinely new source of analytic or arithmetic nonvanishing"
        ]
    ),
    "proof_leverage": jev.score(
        "Assuming the candidate claim is true as a black box, how much of BSD follows?",
        [
            "level 0: no open BSD case becomes easier",
            "level 1: resolves a finite batch of curve ranks but leaves infinite families open",
            "level 2: proves rank equality for an entire rank regime (e.g. all rank 2 curves in a family)",
            "level 3: proves rank equality for all elliptic curves unconditionally"
        ]
    ),
    "flaw_risk": jev.choice(
        "Does the candidate risk falling into a known BSD fallacy?",
        criteria={
            "clean": "Explicit, rigorous hypotheses respecting known barriers",
            "selmer_risk": "Risks conflating finite Selmer dimension with rational rank",
            "duality_risk": "Risks assuming duality forces Iwasawa semisimplicity",
            "derivative_risk": "Risks claiming order 2 without computing L''(1)"
        }
    )
}


def rank_text(text: str) -> dict:
    state = {
        "conjecture": CONJECTURE,
        "candidate_text": text
    }
    return jev.ask(state, QUESTIONS)


def main():
    parser = argparse.ArgumentParser(description="Jev BSD Ranking Tool")
    parser.add_argument("--selftest", action="store_true", help="Run quick connectivity test")
    parser.add_argument("--text", help="Text of candidate claim to rank")
    args = parser.parse_args()

    if args.selftest:
        print("Running Jev BSD self-test...")
        res = rank_text("Verify E_41 has analytic order 2 by computing L''(E_41, 1) and comparing with Kummer rank 2.")
        print(json.dumps(res, indent=2))
        return

    if not args.text:
        parser.print_help()
        sys.exit(1)

    res = rank_text(args.text)
    print(json.dumps(res, indent=2))


if __name__ == "__main__":
    main()
