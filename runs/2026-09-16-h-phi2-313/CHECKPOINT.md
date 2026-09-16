# We have not solved the Birch–Swinnerton-Dyer problem yet.

## H19: a horizontal shear removes 137 before the second Phi introduces 313

Continuation of H18 on the private BSD branch `research/h2-endpoint-20260914`. The exact target remains the universal equality `ord_{s=1}L(E,s)=rank E(Q)` for every elliptic curve over Q. H19 is a restricted rational-point construction result; it is not a complete BSD candidate.

### 1. Word and exact input

Start from the authenticated 137 seed and apply one horizontal shear

    H(P,Q)=(P-2Q,Q)

on the two copies of `E0:v^2=u^3-u`. H15 already reconstructed the resulting rational quartic-surface point as

    x=6127/1862,
    y=37/14,
    W=25815863383/679540624,

with

    W^2=(x^4+6x^2+1)(y^4-6y^2+1).

Now apply the authenticated H12/H13 osculating map `Phi` twice. The first Phi output agrees exactly with H15's recorded x-coordinate

    x1=43527762774033482635941503/
       35975915953349079904919842.

The second Phi output is exact and remains on the same intermediate genus-one fiber; the two computed fiber parameters are equal.

### 2. 137 is removed and 313 is introduced

Write the final second-Phi coordinate as `x2=A/B` in lowest terms and define

    G=A^4+6A^2B^2+B^4,

so that `F_+(x2)=G/B^4`. The exact checker gives

    digits(A)=226,
    digits(B)=225,
    digits(G)=901,
    SHA256(decimal G)
      = cf1d1f9d59882115393945b02b6492049757b201cb58106b9ced71313c95194e.

Exact valuations include

    v_137(G)=0,
    v_313(G)=1,
    v_257(G)=0.

Thus this word succeeds at the specific cofactor task left by H18: the inherited odd factor 137 is gone, while 313 occurs to odd valuation in the output squareclass.

This is stronger than the plain `Phi^2` word from H18, where both 137 and 313 had odd valuation. It also shows H17's one-Phi obstruction can be bypassed without retaining the original 137 factor.

### 3. The output is still not squareclass 313

The same exact integer G has

    v_17(G)=4,
    v_73(G)=1,
    v_113(G)=1,
    v_13873(G)=2,
    v_28657(G)=1,
    v_69457(G)=1,
    v_176809(G)=1,
    v_1389623369(G)=1.

The primes 73,113,313,28657,69457,176809 and 1389623369 were independently certified prime. In particular `v_73(G)=1`, so `G/313` is not a square and the final squareclass is not 313 alone. No complete factorization of the remaining 901-digit cofactor is required for this conclusion.

### 4. Rank information retained

The final rational surface point supplies two rational quartic witnesses of the same positive squareclass. Using the established H8/H15 map, these give the Kummer classes `(G,1,G)` and `(1,G,G)` on `E_G:Y^2=X^3-G^2X`. Together with rational 2-torsion, the same determinant-one Kummer minor used in H15 proves two independent free directions. After removing the square factor of G, the squarefree-normalized curve therefore satisfies

    rank E_n(Q) >= 2.

This is a lower bound for a composite n containing 313, not an exact rank or an analytic-order certificate.

### 5. Verification

`verify.py` reconstructs both Phi steps with exact `Fraction` arithmetic, checks both surface identities, verifies the H15 first-Phi x-coordinate, recomputes G, checks all listed valuations, certifies the stated small primes, and verifies that `G/313` is not a square. The accepted run passes.

A separate stateless Wolfram Language calculation independently returns

    {fiber_equal=True, digits(A)=226, digits(B)=225, digits(G)=901,
     v17=4, v73=1, v113=1, v137=0, v257=0, v313=1,
     v13873=2, v28657=1, v69457=1, v176809=1,
     v1389623369=1, surface_residual=True}

and `PrimeQ=True` for each listed prime certificate. The accepted Wolfram run emitted no warnings.

### 6. Next obligation

H19 changes the bottleneck from `remove 137 while keeping 313` to the sharper problem `remove every remaining odd cofactor while keeping 313`. The next executable route is to vary the horizontal exponent m in `H^m Phi^2`, use exact local sieves to keep `v_313` odd and `v_137` even, and then test the resulting cofactor squareclass rather than blindly enlarging integer sizes. A successful squareclass-313 hit would still establish only this rank-construction benchmark, not the universal BSD theorem.
