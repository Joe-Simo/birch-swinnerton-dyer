# We have not solved the Birch–Swinnerton-Dyer problem yet.

## H23: the vertical interposed-shear route remains open, but its first regular short slice has a 41-adic obstruction

Continuation of H22 on the private branch `research/h2-endpoint-20260914`. H22 excludes every output of `H^m Phi H^n Phi` from having common squareclass exactly 313. H23 changes the operation inserted between the two nonlinear maps to the vertical shear

    V(P,Q)=(P,Q-2P)

and begins the separate family `H^m Phi V^n Phi`. This is a restricted rational-point construction investigation, not a complete BSD candidate.

### 1. Complete target-prime calculation at 313

At `p=313`, both embeddings `sqrt(137)=78,235` give the same result. The first horizontal parameter has exact period 2. For each `m=0,1`, after the first `Phi` the vertical translation `Q -> Q-2P` has exact period 170.

Exhaustive evaluation of all 170 classes gives eight regular final zeros

    n = 0,74,76,80,92,152,164,168 mod170,

and six singular/ambiguous classes

    n = 12,37,62,86,122,158 mod170.

Thus any exact squareclass-313 output in this vertical architecture must lie in one of these fourteen classes. The six ambiguous classes are retained; no singular local chart is treated as an exclusion.

### 2. A short exact regular word

The smallest negative regular target class near zero is `n=-2`, and further tests showed that `n=-6` is useful because it removes several nuisance factors seen in earlier horizontal words. The exact word selected here is

    H^{-1} · Phi · V^{-6} · Phi.

Here `H^{-1}` sends `P -> P+2Q` on the original 137 surface. After the first `Phi`, the checker reconstructs the new common-squareclass quadratic field, applies `V^{-6}`, i.e. `Q -> Q+12P`, converts back to rational quartic coordinates, and applies `Phi` a second time. All operations are performed with exact rational/quadratic arithmetic, not by lifting finite-field states.

Writing the final plus coordinate as `x=A/B` in lowest terms and

    G=A^4+6A^2B^2+B^4,

the exact result has

    digits(A)=65009,
    digits(B)=65008,
    digits(G)=260033,
    SHA256(decimal G)
      = 7aa299919d89963657a1896d0785e0357941452f493295b90fafcd2b2160ea15.

The decisive exact valuations are

    v_137(G)=0,
    v_313(G)=1,
    v_41(G)=1,
    v_17(G)=2.

The checker also finds valuation zero at the previously exposed nuisance primes `73,113,193,241,257,281,353,1409,1657,2017,2473,2833,4481,7057,7577,190537`.

Thus this word removes 137 and retains 313, but it still does **not** have squareclass 313 because 41 occurs to odd valuation. In particular `G/313` is not a square.

### 3. A local explanation for the factor 41

At `ell=41`, `137` is a quadratic nonresidue and `(313/41)=-1`. For the first parameter class `m=-1`, the exact first translation period is 26 and the exact second vertical period is 52. Conservative enumeration of the regular second-stage classes shows that the necessary squareclass-313 character condition at 41 is satisfied only for odd `n mod52`.

Every *regular* target-zero class at 313 listed in Section 1 is even. Therefore, for `m=-1`, no regular p=313 target class can simultaneously satisfy the regular 41-adic condition. The exact `n=-6` output realizes this conflict as `v_41(G)=1`.

This does not eliminate the six ambiguous p=313 classes, and it does not eliminate other values of `m`. It is a genuine obstruction to one slice, not a theorem for the full two-parameter vertical family.

### 4. Rank information and verification scope

As in H15/H18/H21, the final rational surface point gives two rational quartic witnesses for the same positive squareclass. The established determinant-one Kummer calculation therefore gives two independent free directions on the squarefree-normalized congruent-number curve, hence rank at least two for that composite output.

`verify.py` reconstructs the complete exact word with Python `Fraction` arithmetic and exact quadratic-field arithmetic, checks both surface identities, forms the 260033-digit integer G, verifies the hash and the stated valuations, and checks directly that `G/313` is not a square. A separate finite-field checker verifies the complete p=313 regular/ambiguous lists and the p=41 parity condition. No analytic-rank input, BSD assumption, Sha-finiteness assumption or database rank field is used.

### 5. Literature audit of the rank-two analytic bridge

A parallel audit checked the February 2026 version of Francesc Castella, *Generalised Kato classes on CM elliptic curves of rank 2*. Its Theorem B proves, under its hypotheses, `kappa_p != 0 => dim Sel(Q,V_pE)=2`, and characterizes the converse by the nonzero localization map. It assumes the complex L-function already vanishes to positive even order; it does not prove that a two-dimensional Selmer group has complex analytic order exactly two. The same paper's Theorem C instead assumes specified orders of **p-adic** L-functions to obtain a two-dimensional Selmer group, and Remark 1.3.1 identifies nondegeneracy of a p-adic height pairing as the equality condition for the p-adic orders. Consequently this current rank-two Kato technology does not supply the missing universal complex-order comparison in this project.

### 6. Next obligation

Two facts now guide the next step. First, the horizontal two-parameter architecture is completely closed by H22. Second, the vertical architecture survives globally, but even a short regular target word encounters an independent local cofactor obstruction. The next executable step is therefore a conservative all-parameter local sieve for `H^m Phi V^n Phi`, keeping every p=313 ambiguous class; if that family survives, the remaining classes should be tested with exact rational reconstruction rather than increasingly large blind searches. General BSD remains unresolved.