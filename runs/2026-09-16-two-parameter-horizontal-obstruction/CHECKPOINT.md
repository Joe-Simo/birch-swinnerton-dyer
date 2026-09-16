# We have not solved the Birch–Swinnerton-Dyer problem yet.

## H22: every `H^m Phi H^n Phi` output misses squareclass 313

Continuation of H21 on the private branch `research/h2-endpoint-20260914`. The universal target remains `ord_{s=1} L(E,s)=rank E(Q)` for every elliptic curve over Q. H22 closes one two-parameter rational-point construction family; it is not a complete BSD candidate.

### 1. Family and necessary local condition

Start from the authenticated 137 seed on the simultaneous quartic surface. Lift its two quartic witnesses to points `P,Q` on `E0:v^2=u^3-u`. For arbitrary integers `m,n`, apply

    H^m(P,Q)=(P-2mQ,Q),

then the authenticated nonlinear osculating map `Phi`. On the new common-squareclass surface, lift again to the appropriate quadratic field, apply the second horizontal shear

    H^n(P1,Q1)=(P1-2nQ1,Q1),

and apply `Phi` once more. This is the full family

    H^m · Phi · H^n · Phi.

If its final common squareclass were exactly 313, then at every auxiliary odd prime ell != 313 where the local chart is regular the final value

    F_+(x)=x^4+6x^2+1

must be nonzero and satisfy

    (F_+(x)/ell)=(313/ell).

A local zero at ell != 313 is also incompatible with squareclass 313. Every local chart exception is retained as potentially admissible; no pole, zero denominator, split ambiguity, or failed inversion is used as evidence against a parameter pair.

### 2. Complete target-prime calculation at 313

Since `137` is a square modulo 313, both embeddings are checked separately:

    sqrt(137)=78 or 235 mod313.

For either embedding the first horizontal parameter has exact period 2. For both `m=0,1`, after the first `Phi` the second horizontal translation has exact period 170. Complete enumeration gives regular final zeros

    n = 0,54,56,168 mod170,

and eight singular/ambiguous second-Phi residues

    n = 27,76,96,101,112,123,128,148 mod170.

The two embeddings give the same lists. H22 therefore conservatively starts from all twelve residues

    {0,27,54,56,76,96,101,112,123,128,148,168} mod170.

The eight ambiguous classes are deliberately kept rather than silently discarded.

### 3. Auxiliary-prime sieve with all ambiguities retained

For each auxiliary prime below, `137` is a quadratic nonresidue, so the original seed lives in the genuine field `F_ell(sqrt(137))`. The checker computes the exact first translation period and, for every first-stage residue, the exact second translation period after the first `Phi`. It enumerates every regular second-stage residue and retains every local exception.

Starting from the twelve target-prime classes, the following sequence produces a common rectangular period

    m mod360, n mod24480.

The number of conservatively surviving residue pairs after each prime is:

| ell | local m period | common local n period | survivors |
|---:|---:|---:|---:|
|13|10|10|54|
|31|8|8|404|
|29|10|10|196|
|23|2|6|480|
|71|18|18|5840|
|79|20|20|4088|
|127|8|32|5236|
|157|30|510|2956|
|179|90|90|1168|
|191|12|48|752|
|239|20|60|408|
|359|10|90|152|

Counts can increase when a new prime enlarges the common modulus; each row denotes the complete surviving set in that new modulus. All local singular states are retained.

Thus only 152 residue classes remain modulo `(360,24480)`.

### 4. Final exhaustive elimination without enlarging the global period

Four additional primes have translation periods dividing the already established global moduli for every residue class that reaches them. Hence they can test the 152 classes without introducing any new `(m,n)` lifts.

The exact elimination chain is

| ell | (137/ell) | (313/ell) | before | eliminated | after |
|---:|---:|---:|---:|---:|---:|
|1151|-1|-1|152|20|132|
|1549|-1|+1|132|60|72|
|2719|-1|+1|72|48|24|
|4561|-1|-1|24|24|0|

For these four primes the first-stage translation has period dividing 360 and every relevant second-stage translation has period dividing 24480. Any evaluation exception is kept, not eliminated. The final empty set therefore means that every original integer pair `(m,n)` violates a regular necessary local condition at at least one audited prime.

Consequently

> No integers `m,n` can make the output of `H^m Phi H^n Phi` from the 137 seed have common squareclass exactly 313.

This is an all-parameter obstruction for this architecture, not a bounded search.

### 5. Verification

Two separately written exact implementations agree on the entire sieve.

The Python checker uses only the standard library, exact finite-field arithmetic, explicit arithmetic in `F_ell[s]/(s^2-137)`, Tonelli-Shanks for split second-stage lifts, the elliptic group law, exact period enumeration, the authenticated quartic maps and both `Phi` evaluations. `python -m py_compile verify.py` and `python verify.py` passed. Its conservative counts are exactly the table above and the final survivor set is empty.

The TypeScript checker uses `bigint` arithmetic and an independently written finite-field, elliptic-group, square-root, period and CRT-residue implementation. Strict `tsc --noEmit` with unused/unreachable diagnostics passed, compilation passed, and the executable independently reproduced the same global moduli, all twelve intermediate survivor counts, and the final chain `152 -> 132 -> 72 -> 24 -> 0`.

A separate long Wolfram cross-check was attempted, but the service returned HTTP 502 before producing a result; it supplies no evidence for H22 and is not counted as verification.

No BSD assumption, analytic-rank input, Sha-finiteness assumption, database rank field or unproved random extrapolation enters this finite obstruction.

### 6. Consequence and next obligation

H22 strengthens H20: not only `H^m Phi^2`, but the entire two-parameter family with an arbitrary horizontal shear inserted between the two nonlinear maps is excluded from producing squareclass 313. H21's exact `H Phi H^{-2} Phi` composite output is therefore representative of an architecture that can introduce 313 as a factor but can never remove every other squareclass factor.

The next route must use a genuinely different interposed operation. The simplest remaining family is a vertical shear after the first `Phi`, `H^m Phi V^n Phi`; a conservative target-prime calculation already leaves fourteen possible `n mod170` classes (eight regular zeros plus six ambiguous classes), so that family requires a separate two-parameter audit rather than being inferred from H22. General BSD remains unresolved.