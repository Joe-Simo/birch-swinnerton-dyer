# We have not solved the Birch–Swinnerton-Dyer problem yet.

## H24: every `H^m Phi V^n Phi` output misses squareclass 313

Continuation of H23 on the private branch `research/h2-endpoint-20260914`. The universal target remains `ord_{s=1} L(E,s)=rank E(Q)` for every elliptic curve over Q. H24 closes the vertical two-parameter rational-point construction family left open by H23; it is not a complete BSD candidate.

### 1. Family and inherited target-prime classes

Start from the authenticated 137 seed, lift to the two points `P,Q` on `E0:v^2=u^3-u`, and for arbitrary integers `m,n` apply

    H^m(P,Q)=(P-2mQ,Q),
    Phi,
    V^n(P1,Q1)=(P1,Q1-2nP1),
    Phi.

Thus the family is

    H^m · Phi · V^n · Phi.

H23's complete calculation at `p=313`, under both embeddings `sqrt(137)=78,235`, gives first-parameter period 2, second vertical period 170, eight regular final zeros

    n = 0,74,76,80,92,152,164,168 mod170,

and six singular/ambiguous classes

    n = 12,37,62,86,122,158 mod170.

Both first-parameter residues and both embeddings give the same lists, so the target prime imposes no restriction on `m`. H24 therefore begins conservatively from all fourteen classes

    {0,12,37,62,74,76,80,86,92,122,152,158,164,168} mod170.

Every ambiguous class is retained. No pole, singular chart, failed inversion or branch boundary is counted as evidence against a parameter pair.

### 2. Necessary auxiliary-prime condition

If the final common squareclass were exactly 313, then for every audited odd auxiliary prime `ell != 313` at which the construction is regular,

    F_+(x)=x^4+6x^2+1

must be nonzero and satisfy

    (F_+(x)/ell)=(313/ell).

A nonzero mismatch or a zero at `ell` excludes the pair. An evaluation exception is always kept. For the full-constraint primes below, `137` is a quadratic nonresidue, so the seed is evaluated in the genuine field `F_ell(sqrt(137))`; after the first Phi, the checker reconstructs the correct quadratic field for the changed squareclass and computes the exact order of the vertical translation `-2P1`.

### 3. Conservative exact sieve

The accepted finite certificate alternates complete local-period intersections with cheaper filters at primes whose translation periods are explicitly checked to divide the already established global moduli. Counts may increase only when a complete constraint enlarges a modulus.

Starting with `m mod1`, `n mod170`, the complete-intersection stage is:

| ell | local m period | local n period | global m modulus | global n modulus | survivors |
|---:|---:|---:|---:|---:|---:|
|13|10|10|10|170|64|
|31|8|16|40|1360|1652|
|29|10|10|40|1360|1444|
|23|2|12|40|4080|3788|
|71|18|36|360|12240|49630|
|79|20|40|360|12240|22782|
|127|8|64|360|48960|53948|
|157|30|510|360|48960|35870|
|179|90|90|360|48960|17504|
|191|12|96|360|48960|8916|
|239|20|120|360|48960|3870|
|359|10|180|360|48960|1632|

With the current periods explicitly verified, `1151` and `2719` reduce the set

    1632 -> 986 -> 436.

A complete constraint at `53` enlarges the `m` modulus to 6120 while leaving the `n` modulus 48960, producing 4618 lifted survivors. Period-verified filters then give

    ell=67:     4618 -> 2774,
    ell=271:    2774 -> 1158,
    ell=349:    1158 -> 598,
    ell=1223:    598 -> 288,
    ell=4079:    288 -> 108,
    ell=12239:   108 -> 60.

A complete constraint at `199` enlarges the `n` modulus to 244800 and gives 276 lifted survivors; `599` reduces these to 216. A complete constraint at `113` enlarges the `m` modulus to 30600 and gives 584 lifted survivors, after which

    1699:   584 -> 248,
    2399:   248 -> 120,
    15299:  120 -> 86,
    89:      86 -> 60,
    122399:  60 -> 52.

At prime 89, ten first-stage residue classes are locally exceptional; they are retained. No conclusion depends on treating them as failures.

A complete constraint at `83` introduces the remaining factor 7 in the periods, giving final global moduli

    m mod 214200,
    n mod 1713600,

and 1396 lifted survivors. The final period-verified chain is

    1427:   1396 -> 370,
    11423:   370 -> 166,
    21419:   166 -> 86,
    5711:     86 -> 40,
    1399:     40 -> 14,
    1259:     14 -> 8,
    42101:     8 -> 0.

Thus the conservative survivor set is empty.

### 4. Final eight-state certificate

Before the final prime 42101, the eight remaining classes modulo `(214200,1713600)` are

    (85172,203272), (85172,631672),
    (85172,1060072), (85172,1488472),
    (192272,203272), (192272,631672),
    (192272,1060072), (192272,1488472).

At `ell=42101`, the checker verifies directly that `214200` is a period of the first horizontal translation and `1713600` is a period of the relevant second vertical translation. All eight evaluations are regular and all eight give the same final data

    x = 15355 mod42101,
    F_+(x) = 38394 mod42101,
    (38394/42101)=+1,
    (313/42101)=-1.

Hence all eight are excluded by a regular character mismatch; no boundary case is used in the final elimination.

### 5. Conclusion

Therefore

> No integers `m,n` can make the output of `H^m Phi V^n Phi` from the 137 seed have common squareclass exactly 313.

This is an all-parameter local obstruction for this architecture, not a bounded search. Together with H22, both pure horizontal and pure vertical interposed-shear families between two Phi maps are now closed.

The result does **not** say that `E_313` lacks rational points—H8 already certifies its rational rank 2. It says only that these two-shear transport architectures cannot be the mechanism producing the prime squareclass 313 from the selected 137 seed.

### 6. Verification scope and next obligation

`verify.py` implements exact finite-field arithmetic, the elliptic group law, the authenticated quartic maps and Phi, complete local periods for every modulus-enlarging prime, conservative treatment of all exceptions, and explicit period checks for every filtering prime. Replaying the accepted chain gives the counts above and an empty set. A separate Wolfram final-eight cross-check was attempted but returned HTTP 502 and therefore supplies no evidence; that failure is preserved rather than counted as agreement.

No BSD assumption, analytic-rank input, Sha-finiteness assumption, database rank field or probabilistic extrapolation enters H24.

The next route must mix the two factors more substantially between nonlinear steps—e.g. a two-parameter horizontal-plus-vertical word after the first Phi—or pivot back to the independent analytic/Selmer comparison bottleneck. Merely increasing `m` or `n` in either closed H22/H24 architecture cannot help. General BSD remains unresolved.
