# We have not solved the Birch–Swinnerton-Dyer problem yet.

H2: theorem-derived endpoint for E_113; no complete candidate, no independent local 8-descent, no novelty claim. Target remains ord_(s=1)L(E,s)=rank_Z E(Q) for every E/Q.

## Preservation

This is a compact remote checkpoint, not the entire local evidence archive. The full derivation, strict TypeScript checker, independent Python checker, contracts and genuine logs are in the conversation artifact BSD_H2_endpoint_2026-09-14.zip, under /mnt/data/04-birch-swinnerton-dyer. Wolfram source and its literal successful output accompany this checkpoint remotely. Nothing is running in the background.

Main was inspected at 34ce06f420f4616cc4091b01a04d91c920ee3123 and refreshed to d5737af24bfe1c3d8d62e9533c73e270f77aa363 before preservation. Its unchanged root research record and the later CHECKPOINT.json were read. The prime-descent branch 725f3be6a370bcd510dc61b3405c7437f5f884b8 was also observed, and its outstanding 4-to-8 step read. This run uses a separate branch/subtree; it does not overwrite either history. The local root record was left unchanged.

## 1. Exact endpoint

Use E_n:y^2=x^3-n^2*x, O at infinity. Tunnell [T] proves

    a(n)=A_32(n)-A_8(n)/2,
    L(E_n,1)=beta*a(n)^2/(4*sqrt(n)),
    beta=integral_1^infinity dx/sqrt(x^3-x)>0,

where A_c counts all integer triples x^2+2y^2+c*z^2=n. Exact results independently reproduced in TypeScript, Python and Wolfram:

    n     A_8 A_32 a(n)
    1      2    2   1
    17    16    4  -4
    41    32   16   0
    113   32   24   8

Burungale-Flach [BF, Corollary 2, pp.4-5] proves finiteness and the full rank-zero formula for CM E/Q with L(E,1)!=0, including the prime 2. E_n has full CM by Z[i], with [i](x,y)=(-x,iy) over Q(i). The corollary explicitly applies to CM curves over Q. Nonzero a(n) verifies its analytic hypothesis. The n=41 branch must be excluded. This uses an established special-case theorem, NOT general BSD as an assumption or an independent algebraic rank calculation.

The integral model is minimal: Delta=64*n^6 has valuations 6 at all bad primes for odd squarefree n; an integral smaller discriminant would subtract at least 12. The invariant differential is dx/(2y). There are two real components of equal invariant volume, each beta/sqrt(n), so the total real period is Omega=2*beta/sqrt(n).

At 2, x_old=X+1,y_old=Y+X gives coefficients (2,2,0,3-n^2,1-n^2). They meet the type-III branch of [CS], v_2(a4)=1, giving c_2=2 and conductor exponent 5. Shifting x alone does NOT meet that branch's stated coefficient conditions. At an odd q|n, the I0* residual cubic is Z^3-(n/q)^2 Z with three distinct roots; hence c_q=4 and conductor exponent 2. For a prime n=p, the finite Tamagawa product is 8 and conductor 32*p^2.

For primes p=1 mod8, reduction at 3 and 7 gives group orders 4 and 8. The quadratic-character sums cancel in x,-x pairs. Prime-to-characteristic torsion injectivity at both primes and the visible four 2-torsion points prove E_p(Q)_tors=(Z/2)^2. The same holds for n=1.

Consequently the correctly normalized rank-zero formula gives

    |Sha(E_p)|=a(p)^2/4  (p=1 mod8 prime, a(p)!=0).

For n=1 it gives |Sha|=1. Thus |Sha(E_17)|=4 and |Sha(E_113)|=16, with finiteness proved by [BF]. No period, component or omitted prime-2 factor is inferred from a numerical fit.

## 2. Group structure and higher lifting

Monsky's matrix as restated in [Z, (2.4)-(2.8)] is zero 2-by-2 for p=1 mod8. With rank zero, the Selmer exact sequence gives dim Sha[2]=2. The original Monsky appendix was not inspected; this is an established-theorem invocation, not a reconstructed local descent.

The finite Cassels-Tate group has a perfect alternating pairing [PS,Y]. Such a finite 2-group is a sum of pairs of equal cyclic factors: choose a maximal-order x, use perfectness to choose y pairing primitively with x, split off the nondegenerate pair, and repeat. Two-dimensional 2-torsion forces a single pair. Therefore

    Sha(E_113/Q)=(Z/4Z)^2,
    Sha(E_17/Q)=(Z/2Z)^2.

The E_41 point argument was recomputed: P=(-9,120), Q=(841,24360), together with (41,0),(0,0), have independent Kummer images in coordinate order (x-41,x+41,x). Their triples are (2,82,41),(-41,41,-1),(-50,32,-9),(800,882,841). The four squareclass vectors have rank 4; the Monsky bound gives rank E_41=2 and Sha(E_41)[2^infinity]=0. Its odd Sha and exact analytic order are not determined here.

For all m>=1, by the exact sequence and rational torsion,

    |Sel_(2^m)(E_17)|=16,
    |Sel_(2^m)(E_41)|=4*2^(2m),
    |Sel_(2^m)(E_113)|=4*2^(2*min(m,2)).

Thus E_41 and E_113 have Selmer orders (16,64,256,1024) and (16,64,64,64) at levels (2,4,8,16). This all-m statement follows from group structure, not extrapolation. No unproved splitting of Sel_8 is asserted.

The image Sel_8->Sel_4 is the inverse image of 2Sha[8] in Sha[4]: the rational-point quotient map is surjective, so a diagram chase proves both inclusions. Its order is 16 for E_113 and 64 for E_41. The quotient for E_113 is (Z/2)^2. Only rational torsion classes of its Sel_2 survive from Sel_8; all Sel_2 classes of E_41 survive.

For A=Sha(E_113)=(Z/4)^2, the first pairing on A[2]=2A is zero. For x,y in A[2], define B_2(x,y)=<u,y> with 2u=x. It is independent of u, alternating, and nondegenerate: annihilator(A[2])=2A, so a radical element has x=0. Hence the second pure pairing has rank 2, whereas E_41 gives zero. This is a global theorem-derived determination of the generalized pairing of [Y], NOT a computed local Hilbert-symbol product.

The same argument proves a restricted-family consequence: for every p=1 mod8 prime with a(p)!=0,

    Sha(E_p)[2^infinity]=(Z/2^h)^2, h=v_2(a(p))-1>=1.

Its nonzero pure Sel_2 classes survive projections from level 2^m exactly for m<=h. Level 2^(h+1) eliminates them. This excludes every zero-coefficient curve and supplies no all-rank BSD mechanism.

## 3. A rejected next-stage shortcut

If first-stage functions f_j define a 2-cover pi:D->C by adjoining their square roots, then pi^*f_j=g_j^2. Every local symbol (pi^*f_j(P_v),b_j)_v is therefore +1 wherever defined. Reusing these pullbacks would always predict a zero next pairing, contradicting the nonzero second pairing just established for E_113. New functions representing the nonzero Pic^0(D)[2] classes are needed on the 4-covering itself. This rejects a method, not BSD.

## 4. Tests and remaining obligation

Local TypeScript: 46 exact assertions and strict compiler lint/type checks passed after a unary-minus/exponentiation syntax error was fixed; the original failed diagnostic is retained. Independent Python/SymPy: eight complete signed counts, symbolic coordinate/discriminant checks, all seven scalar symplectic models of (Z/2^h)^2 for h=1,2,3, and 1520 lift checks passed. Two deliberately corrupted reports were rejected. Wolfram independently agreed on the counts, coefficients and arithmetic. These are implementation checks and self-review, not formal or expert verification.

The direct algebraic certificate is still missing. Next: construct a genuine locally soluble 4-covering lifting a nonzero pure Sel_2(E_113) class using Fisher's higher-descent companion quadrics (arXiv:1509.03234v1, Sections 5,7,8). Verify the map, local points, divisors and new pushout functions before evaluating symbols. The second pairing must have rank 2; that known endpoint now supplies a non-circular test of the implementation. The universal higher-rank arithmetic/complex-order bridge remains unproved. No background process, spending, public release, contact or submission occurred.

## Sources actually inspected

[BF] Burungale-Flach, arXiv:2206.09874v3 (4 Sep 2023), Corollary 2 and proof pp.4-5; Cambridge J. Math. 12 (2024),357-415, DOI 10.4310/CJM.2024.v12.n2.a2. Audited text: https://arxiv.org/pdf/2206.09874 . Final journal PDF retrieval failed; publication metadata was corroborated separately. The whole paper was not independently re-proved.

[T] Tunnell, Invent. Math.72(1983),323-334, Theorem3 p.328; https://sites.math.rutgers.edu/~zeilberg/EM22/JT1983.pdf . Relevant original scanned pages visually inspected.

[CS] Cremona-Sadek, arXiv:2003.08454v3 (18 Oct 2021), Section5.1 pp.26-27, specified Tate-algorithm branches; https://arxiv.org/pdf/2003.08454 . Screenshots inspected.

[Z] Shenxing Zhang, arXiv:2111.11618v1 (23 Nov 2021), pp.3-4, (2.1)-(2.8); https://arxiv.org/pdf/2111.11618 . Monsky restatement and exact Kummer conventions.

[Y] Fisher-Schaefer-Stoll, The yoga of the Cassels-Tate pairing, author version 4 March2009, (2.1), Section4, Lemma6.1, Theorem6.3; https://www.mathe2.uni-bayreuth.de/stoll/papers/yoga.pdf .

[PS] Poonen-Stoll, Annals150(1999),1109-1149, arXiv:math/9911267v1; https://arxiv.org/pdf/math/9911267 . Nondegeneracy modulo maximal divisible subgroup; finite specialization used here.

CMI's official BSD page still lists the problem as unsolved. This is partial research only, with no complete candidate or prize claim.
