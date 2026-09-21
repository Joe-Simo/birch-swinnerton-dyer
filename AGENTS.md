# Birch–Swinnerton-Dyer Conjecture Research — Working Instructions

**The Birch–Swinnerton-Dyer Conjecture is not solved.** Treat every claim of a general solution
or unconditional rank equality as unverified until audited against the primary source dependencies
in `sources/REGISTER.md`. `RESEARCH.md` is the authoritative record of verified truth.

## HARD RULE: Every research cycle STARTS with a Jev call

Not "consider using Jev" — **the first tool call of every research turn is a Jev batch.** If you are
about to read, audit, compare, or choose between multiple candidate hypotheses or papers, write the
screen first using `python3 code/jev_genius.py` or `python3 code/jev_bsd.py`.

Jev decisions that are fast, cheap, and mandatory:
- **Triage & ranking**: screen every candidate hypothesis with `code/jev_genius.py triage`.
- **Failure mode check**: verify arguments against the 5 canonical BSD traps.
- **Statement fidelity**: for formal Lean 4 files, audit statement fidelity with `code/jev_genius.py lean-audit`.

## Canonical BSD Failure Modes to Reject Immediately

1. **Finite Selmer vs. Rank Conflation**:
   Conflating $\dim \text{Sel}_2(E/\mathbb{Q})$ with $\text{rank}_{\mathbb{Z}} E(\mathbb{Q})$. The Selmer sequence is:
   $$0 \to E(\mathbb{Q})/2E(\mathbb{Q}) \to \text{Sel}_2(E/\mathbb{Q}) \to \Sha(E/\mathbb{Q})[2] \to 0$$
   A positive Selmer nullity can be pure $\Sha[2]$ torsion (as proven on $E_{17}$). Never conclude positive rank without computing independent rational points or ruling out $\Sha[2]$.
2. **Duality / Semisimplicity Conflation**:
   Claiming that anti-Hermitian duality or parity forces the characteristic ideal vanishing order $\operatorname{ord}_T L_p(E, T)$ to equal the specialized Selmer dimension. Paired skew-symmetric matrices satisfy all duality constraints while doubling determinant order ($\delta = \sum(e_i - 1) > 0$).
3. **Uncertified Higher Derivatives**:
   Concluding exact analytic order 2 merely from central vanishing $L(E_n, 1) = 0$ and even root number $\epsilon = +1$. Parity proves order is *at least* 2, but does not prove order *equals* 2 unless $L''(E_n, 1) \ne 0$ is explicitly certified.
4. **CM Scope Leakage**:
   Applying CM-specific theorems (such as Burungale–Tian 2026 Annals) to general non-CM elliptic curves without justification.
5. **Heuristic / Conditional Laundering**:
   Relabeling GRH-conditional bounds or unproved $p$-adic height nondegeneracy as unconditional theorems.

## Tools & Files

| Path | Role |
|---|---|
| `code/jev.py` | Stdlib-only Jev client. Reads key from `$TYPESAFE_API_KEY` or `.env.local`. Never log or commit the key. |
| `code/jev_genius.py` | Multi-tier Jev mathematical intelligence engine for BSD. |
| `code/jev_bsd.py` | Focused BSD hypothesis and failure-mode screener. |
| `code/jev_rank.py` | Per-candidate relevance and novelty ranker. |
| `code/congruent_sieve_fast.c` | OpenMP-accelerated ternary quadratic form sieve for congruent curves. |
| `sources/REGISTER.md` | Primary source register tracking every cited theorem and paper. |
| `CHECKPOINT.json` | Persistent machine-readable project state. |
| `RESEARCH.md` | Authoritative human-readable research log. |

## Standing Discipline

- Exact integer arithmetic for anything affecting mathematical validity. No floating-point rounding where exactness matters. Large integers as decimal strings.
- Never claim BSD is solved without a complete, machine-checked Lean 4 formalization covering all curves and ranks.
