# We have not solved the Birch–Swinnerton-Dyer problem yet.

## H16: orthogonal shear obstructions and a mixed local escape

Continuation of private branch `research/h2-endpoint-20260914` after H15. This run keeps the exact BSD target unchanged. The new statements concern only the 137-seeded quartic transport route; they do not establish prescribed-prime reachability, an analytic-order theorem, a universal rank theorem, or BSD.

### 1. Setup

Put

    F_+(t)=t^4+6t^2+1,   F_-(t)=t^4-6t^2+1,

and use the H15 seed

    x0=1/14, y0=37/14,
    r_+=17*sqrt(137)/196, r_-=47*sqrt(137)/196.

On `E0: v^2=u^3-u`, the quartic maps are

    u=(r+1+e t^2)/(2t^2),
    v=(r+1+3e t^2)/(2t^3),
    t=(u+e)/v, r=(2u-e)t^2-1.

Write the resulting points as `P` for `e=+1` and `Q` for `e=-1`. The deck involution is `(P,Q)->(T_+-P,T_--Q)` with `T_e=(-e,0)`. Therefore the horizontal shear

    H(P,Q)=(P-2Q,Q)

and vertical inverse shear

    v(P,Q)=(P,Q+2P)

commute with deck conjugation and descend to rational maps on the quotient surface. The same holds for odd multiplication on either factor.

`Phi` is the H12/H14 osculating surface map. For its output x-coordinate it is enough to use the cancelled formula from H14. If

    gap=x^2-y^2+6,
    C=(x^2 y^2+1)/gap, K=6C-1,
    a=C, b=C^2+K, d=CK,

then away from the cancelled boundary

    x'=-x*(a^2 x^8-6ad x^4-4bd x^2-3d^2)
          /(3a^2 x^8+4ab x^6+6ad x^4-d^2).

At `C=0`, the authenticated cancellation gives `x'=-1/x^3`. All local rows below have nonzero gap and nonzero final `F_+(x')`; the displayed denominators are units in the relevant residue fields.

### 2. Horizontal family: an all-odd-multiplier obstruction at 47

Reduce the exact `P,Q` in `F_47(sqrt(137))`. The checker derives

    ord(Q)=4.

Let `d` be any odd integer and `m` any integer. Before applying `Phi`, take

    (P_m,Q_d)=(P-2m[d]Q,[d]Q).

Because `ord(Q)=4`, the only possibilities are `dQ=Q` or `-Q`, while `2dQ=2Q`; hence only `d mod 4` and `m mod 2` matter. Converting back to the two quartics gives the complete residue table

    x in {37,33},   y in {6,41}={+6,-6} mod 47.

Since `Phi` depends on `y` through `y^2` in its x-coordinate, the four cases collapse to two:

| x | y | Phi x' | F_+(x') mod 47 | character |
|---:|---:|---:|---:|---:|
| 37 | ±6 | 41 | 9 | +1 |
| 33 | ±6 | 7  | 17 | +1 |

Both output values are nonzero squares. Consequently every nondegenerate output squareclass `n` from this entire horizontal/odd-multiplier family satisfies

    47 does not divide n,   (n/47)=+1.

But

    (257/47)=(313/47)=-1.

Therefore **no choice of odd pre-multiplier d and horizontal exponent m, followed by one Phi, can produce squareclass 257 or 313.** This includes H15's `d=1` slice and the `d=3` pre-tripling used in H14 before its horizontal shear. It is a route obstruction, not a statement about those curves themselves; H8 already certifies their rank separately.

### 3. Vertical family: a complementary obstruction at 13

Now hold `P` fixed and use

    (P,Q_m)=(P,Q-2mP).

Modulo 13 the exact reduction has `ord(P)=4`, so only `m mod 2` matters. The two quartic residues are

    x=1,   y in {11,2}={-2,+2} mod 13.

For both cases the cancelled `Phi` formula gives

    x'=12,   F_+(x')=8 mod 13,

and `8` is a nonsquare. Hence every nondegenerate output squareclass from this vertical family has

    13 does not divide n,   (n/13)=-1.

On the other hand

    (257/13)=(313/13)=+1.

Thus **no vertical-shear exponent m followed by one Phi can produce 257 or 313.** The horizontal and vertical one-parameter routes fail for different local reasons.

### 4. A mixed shear removes both of those local obstructions

The shortest regular mixed word found by exact finite-state search is

    H, H, v, Phi,

that is

    P2=P-4Q,
    Q2=Q+2P2=2P-7Q,

followed by `Phi`. Its exact rational pre-Phi coordinates reduce as follows:

| prime | x | y | Phi x' | F_+(x') | target character |
|---:|---:|---:|---:|---:|---:|
| 13 | 7 | 10 | 5 | 9  | +1 |
| 47 | 37 | 7 | 10 | 26 | -1 |

At 13 the input has `C=0`, so the already-proved H14 cancellation `x'=-1/x^3` is used; at 47 the ordinary cancelled denominator is a unit. These are exactly the character pair required by both 257 and 313:

    ((p/13),(p/47))=(+1,-1),  p in {257,313}.

Therefore the mixed word is locally admissible at both obstruction primes simultaneously. This proves that neither Section 2 nor Section 3 is an invariant of the full two-shear system.

### 5. Exact global execution of the mixed word

The independent exact checker executes `H,H,v` over `Q(sqrt(137))`, converts back to rational quartic coordinates, forms the rational surface `W`, and applies the full rational `Phi` formulas. The final x-coordinate has a 461-digit numerator and 461-digit denominator. If `x'=A/B` in lowest terms, put

    G=A^4+6A^2B^2+B^4.

Then `G` has 1843 decimal digits and

    SHA256(decimal G)
      = 58038f034eec7bb737d72472cbd522b62d01ba1a39d25343e8f32e5d5f375408.

Exact divisibility gives

    v_257(G)=0,   v_313(G)=0.

Thus this shortest two-prime local escape does **not** attain either prescribed prime squareclass. Local admissibility was informative but insufficient, exactly as required by the project rules.

### 6. Verification

`verify.ts` independently derives the seed reductions on `E0`, checks `ord(Q mod47)=4` and `ord(P mod13)=4`, exhausts the horizontal four-row reduction and vertical two-row reduction, and checks the mixed word at both primes. It reports 24 assertions passed.

`verify_independent.py` uses exact `Fraction` arithmetic in `Q(sqrt(137))`, independently executes the elliptic group law for `H,H,v`, reconstructs the quartic surface, applies `Phi`, checks the exact surface identity, reproduces both local residue rows, and proves the final `G` is not divisible by 257 or 313. It records the exact size and hash above.

Commands completed successfully with Node 22.16.0, TypeScript 5.8.3 and Python 3.13.5:

    npm run lint
    npm run typecheck
    npm test
    npm run test:independent

A separate Wolfram Language calculation reproduced the four horizontal rows, both vertical rows, the mixed residues `(13,7,10)->x'=5,F_+=9` and `(47,37,7)->x'=10,F_+=26`, and the four target Legendre symbols, with no warnings on the accepted rerun. The earlier exploratory Wolfram call emitted symbol/Table warnings and is not evidence; the corrected rerun is the accepted cross-check.

CMI's current BSD page was rechecked on 2026-09-15 and still labels the problem `Unsolved`. This status check is external context only; it is not evidence for any internal lemma.

### 7. What changed and next obligation

H15's prescribed-prime gap is sharper now. A whole family obtained by arbitrary odd multiplication of the minus factor plus arbitrary horizontal shear is excluded by a 47-adic character, while the orthogonal vertical family is excluded by a 13-adic character. Mixing the shears can satisfy both local characters, but the first exact mixed escape still misses 257 and 313 globally.

The next executable target is the one-parameter mixed family

    (P-2mQ, Q+2(P-2mQ))

followed by `Phi`. Its reductions already show regular target-compatible classes `m=2,7 mod10` at 13 and no 47-character obstruction; the boundary classes must not be guessed through. Derive its global squareclass-transfer function and use exact local sieving at additional primes before any larger rational search. A successful prescribed-prime hit would still be only a rank-construction step, not a complete BSD solution.
