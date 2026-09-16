# We have not solved the Birch–Swinnerton-Dyer problem yet.

## H21: an interposed inverse shear escapes H20 but still leaves odd cofactors

Continuation of H20 on the private branch `research/h2-endpoint-20260914`. H20 proved that the whole one-parameter family `H^m Phi^2` cannot have squareclass 313. H21 changes the architecture exactly as required by inserting a shear after the first nonlinear Phi.

### 1. Exact word

Start with the authenticated 137 seed. Apply

    H(P,Q)=(P-2Q,Q),

then one `Phi`. On that new common-squareclass surface, lift the two quartic witnesses to the corresponding quadratic field and apply

    H^{-2}(P,Q)=(P+4Q,Q).

Convert back to rational quartic coordinates and apply `Phi` a second time. Thus the exact word is

    H · Phi · H^{-2} · Phi.

The interposed shear is not performed in the original `Q(sqrt(137))`: after the first Phi the common squareclass has changed, so the checker reconstructs the correct new quadratic field from the exact plus quartic value before applying the shear.

### 2. Exact output

If the final plus coordinate is `x=A/B` in lowest terms, define

    G=A^4+6A^2B^2+B^4.

The exact computation gives

    digits(A)=3233,
    digits(B)=3233,
    digits(G)=12932,
    SHA256(decimal G)
      = 84ba591f89728a39b4a4ed84e23f0d860eef93d2884298ab962c5db3868c9725.

The decisive valuations are

    v_137(G)=0,
    v_313(G)=1.

So the inserted shear genuinely escapes the H20 obstruction and keeps 313 while removing 137.

It also removes several cofactors seen in the shorter mixed-shear trial:

    v_113(G)=v_241(G)=v_2113(G)=v_2657(G)=0.

### 3. But the squareclass is still not 313

Exact small-prime division finds

    v_281(G)=1,
    v_313(G)=1,
    v_353(G)=1,
    v_2473(G)=1,
    v_190537(G)=1.

All five displayed divisors are prime. In particular `v_281(G)=1`, so `G/313` is not a square and the output squareclass is not 313.

This is not a failed local test: it is a complete exact rational execution of the stated word. The remaining obstruction is again global cofactor control.

### 4. Rank information

As in H15/H18/H19, the final rational surface point supplies two rational quartic witnesses for the same positive squareclass. The established determinant-one Kummer calculation therefore gives two independent free directions on the squarefree-normalized congruent-number curve. Hence the output curve has rational rank at least two.

No exact rank, analytic order, refined BSD formula or general BSD consequence is claimed.

### 5. Verification and next obligation

The accepted exact Python computation reconstructs the first H shear, the first Phi, the changed quadratic field, the interposed `H^{-2}`, the second Phi, the final surface identity, G, the displayed valuations, the primality of the listed small divisors, and the direct test that `G/313` is not a square.

A separate local sieve over the fixed first-Phi surface identified `H^{-2}` as the shortest tested interposed shear that simultaneously keeps the 313 divisibility condition while avoiding the previously observed local factors 137, 113, 241, 2113 and 2657. That search was bounded and is discovery evidence only; the exact global word above is the accepted mathematical certificate.

H21 shows that H20 was an architectural obstruction rather than a universal one. The next executable step is to treat the newly exposed factors 281,353,2473,190537 as nuisance primes in an exact local sieve for the two-parameter interposed-shear family before attempting another huge rational reconstruction. A successful squareclass-313 hit would still be only a rank-construction benchmark, not a complete BSD solution.
