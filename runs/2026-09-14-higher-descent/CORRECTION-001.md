# We have not solved the Birch–Swinnerton-Dyer problem yet.

Corrects the user-facing bounded-search claim immediately following CONTINUATION.md commit 804b72d65a320ecb16bea407ccc364433edf5cf1. The durable CONTINUATION.md itself did not contain that false numerical claim.

## Correction

The reported statement that a Wolfram search found no integral points for all eight squareclasses xi in {±1,±2,±113,±226} was invalid and must not be used.

There are two independent defects.

First, xi=1 already has the trivial primitive solution (s,t,r)=(1,0,1) to Fisher's authenticated equation

    r^2 = xi*s^4 - (12769/xi)*t^4.

Likewise xi=-1 has (s,t,r)=(0,1,113). Thus the claimed empty search contradicted immediate exact substitutions and should have been rejected by a baseline fixture.

Second, for xi not dividing 12769 (for example ±2,±226), the displayed equation has rational coefficients. A modular search that silently replaces 12769/xi by integer division or treats the right-hand side as an integral residue is not a valid Q_p solubility test. The correct homogeneous equation after clearing denominators is

    xi*r^2 = xi^2*s^4 - 12769*t^4,

but local Q_p solubility still requires valuation/unit analysis or a projectively correct p-adic search; it is not equivalent to asking whether the cleared right-hand side itself is a square modulo p^k.

Wolfram exact substitution independently confirmed the xi=1 fixture. An attempted larger residue computation timed out/returned an upstream error and is not evidence either way.

## Surviving research state

Fisher's equation and the convention blocker in CONTINUATION.md remain valid. No isogeny-Selmer squareclass has yet been selected. No local-solubility classification at 2 or 113 is claimed. The next route remains: write the chosen 2-isogeny and dual explicitly, derive the connecting maps and homogeneous spaces, and impose mathematically correct local conditions at {2,113,infinity} before constructing the 4-cover.

Evidence classification: the previous bounded-search result is refuted by the smallest counterexample xi=1, (s,t,r)=(1,0,1). This correction is durable and should be consulted before any later use of that search.