# We have not solved the Birch–Swinnerton-Dyer problem yet.

## H20: five local fields exclude squareclass 313 from every H^m Phi^2 output

Continuation of H19 on the private branch `research/h2-endpoint-20260914`. The exact universal BSD target remains unchanged. H20 closes one restricted rational-point construction family; it is not a complete BSD candidate.

### 1. Family under test

Start with the authenticated 137 seed on the simultaneous quartic surface and write its two elliptic lifts on

    E0: v^2=u^3-u

as P and Q. For every integer m apply

    H^m(P,Q)=(P-2mQ,Q),

convert back to rational quartic coordinates, and then apply the authenticated osculating map Phi twice. Denote the final plus coordinate by x_m^(2).

If the final common squareclass were exactly 313, then for every odd auxiliary prime ell != 313 at which the complete construction has good reduction and all denominators are units,

    F_+(x_m^(2)) = (x_m^(2))^4 + 6(x_m^(2))^2 + 1

would be a nonzero element with quadratic character

    (F_+(x_m^(2))/ell) = (313/ell).

Therefore any auxiliary prime supplies a necessary congruence condition on m. The point is to intersect complete local periods, not to extrapolate a finite prefix.

### 2. Exact finite-field setup

Choose the five primes

    ell = 251, 127, 239, 31, 457.

For every one of them

    (137/ell) = -1,

so `F_ell(sqrt(137))` is the genuine quadratic field with relation `s^2=137`; there is no split-algebra ambiguity. The exact seed points P,Q reduce to E0 over that field. The m-period is the exact order of `-2Q`, obtained by iterating until the first return of P under translation by `-2Q`.

For every residue in every period, both Phi applications are evaluated from the exact rational formulas reduced modulo ell. There are **zero ambiguous or singular chart states** for all five primes. Thus each allowed-residue set below is exhaustive.

### 3. Complete necessary residue sets

The independent Python and Wolfram implementations agree on:

| ell | (137/ell) | exact m-period | residues compatible with squareclass 313 |
|---:|---:|---:|---|
| 251 | -1 | 14 | {0,1,3,7,11,13} |
| 127 | -1 | 8  | {0,1,4,5} |
| 239 | -1 | 20 | {1,3,5,6,7,11,13,15,16,17} |
| 31  | -1 | 8  | {0,2,3,4,6,7} |
| 457 | -1 | 10 | {3} |

A residue is retained only when the final F_+ value is nonzero and its Legendre symbol equals `(313/ell)`. A zero value would introduce ell into the squareclass and is therefore incompatible with squareclass 313 because ell != 313.

The least common multiple of the five periods is

    lcm(14,8,20,8,10)=280.

Exhaustive intersection of the five necessary sets modulo 280 is empty.

Hence there is no integer m satisfying all five local conditions.

### 4. Conclusion

Therefore

> For every integer m, the rational output of H^m followed by Phi^2 from the 137 seed, whenever interpreted by the authenticated global formulas, cannot have common squareclass exactly 313.

This is a genuine all-m obstruction for this one-parameter family, not a bounded computation. H18 and H19 are consistent with it: they introduced 313 to odd valuation, but their outputs carried extra odd cofactors.

The theorem does **not** say that E_313 lacks rational points; H8 already certifies rank 2 for E_313. It says only that the particular family `H^m Phi^2` cannot be the mechanism producing squareclass 313.

### 5. Verification

`verify.py` independently implements arithmetic in each finite quadratic field `F_ell[s]/(s^2-137)`, the elliptic group law on E0, exact translation periods, quartic conversion, both Phi steps, Legendre-character filtering, and the final CRT-style residue intersection. Its accepted computation returns the five rows above, lcm 280 and no surviving residue.

A separate stateless Wolfram Language computation reproduces exactly the same five periods, allowed sets and empty intersection. That call also reports `(137/ell)=-1` and zero ambiguous states for each prime. The Wolfram service emitted a global-symbol diagnostic from its evaluator wrapper; the numerical output itself matched the independently derived Python certificate, so the warning is preserved rather than silently discarded.

No external theorem beyond ordinary finite-field arithmetic is used in this local obstruction. No BSD assumption, Sha finiteness, analytic-rank input or database rank field enters the argument.

### 6. Next obligation

H20 closes the exact H19 continuation `H^m Phi^2`. The next route must change the architecture rather than enlarge m: insert a nontrivial operation **between** the two nonlinear Phi steps. The first candidates are a horizontal/vertical shear on the new common-squareclass surface, or a different authenticated fiber map. Any candidate must still be checked globally; satisfying the five local conditions alone would not prove squareclass 313 or BSD.
