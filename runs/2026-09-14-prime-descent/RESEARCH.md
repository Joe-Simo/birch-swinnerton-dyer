# We have not solved the Birch–Swinnerton-Dyer problem yet.

Private supplemental checkpoint: 2026-09-14, primes 17, 41 and 113.

No complete BSD candidate exists. These are known special cases and elementary auxiliary obstructions, not a novelty claim or an independent expert/formal verification. The target remains ord_(s=1)L(E,s)=rank_Z E(Q) for every elliptic curve E/Q, in the arithmetic normalization with center 1.

## Preservation and relation to existing work

The repository was empty at the first inspection. At the pre-write refresh, main contained commit d6471b2df33e51ce2c60c18a43d0e260a8f855df and RESEARCH.md, blob 30e8470ca4bbce7d215d9dd88b7259a4821d7448. That file was read in full and is preserved unchanged. Its 209-curve scan and other experiment counts are not adopted as verified coverage of this run. The independent local working copy is /mnt/data/birch-swinnerton-dyer. This supplement and its code occupy a separate run subtree/branch to avoid a concurrent overwrite.

This run tested three mechanisms: a characteristic-multiplicity specialization argument; rational points combined with descent bounds; and exact central coefficients compared with finite Selmer data. The E17/E41 examples and the basic length obstruction overlap the existing record. The added result is the stronger E41/E113 comparison: even Sel2, Sel4 and the first Cassels pairing can agree while the ranks differ. The full local checkpoint, source ledger and all logs are also included in the conversation's evidence archive. Nothing here is a background process or a public submission.

## Exact analytic data and bounded coverage

Let E_n:y^2=x^3-n^2x with n positive, odd and squarefree and origin at infinity. Its discriminant is 64n^6, so all these models are nonsingular. No model transformation is used.

Define A(n) as the number of integer triples x^2+2y^2+8z^2=n and B(n) for x^2+2y^2+32z^2=n. All signs and zero coordinates are counted. Tunnell's coefficient is a(n)=B(n)-A(n)/2, also the coefficient of q^n in

    q product_(m>=1)(1-q^(8m))(1-q^(16m)) sum_(j in Z) q^(2j^2).

Tunnell, Theorem 3, gives L(E_n,1)=a(n)^2 beta/(4 sqrt(n)), with beta=integral_1^infinity dx/sqrt(x^3-x)>0. Positivity is exact: the integrand is positive, its endpoint singularity is integrable and its tail is O(x^(-3/2)). Nonzero a(n) certifies analytic order zero; a(n)=0 certifies only central vanishing, not an exact positive order.

All primes 1<p<=200 with p=1 mod8 were checked:

| p | A | B | a | pure Sel2 dimension |
|---:|---:|---:|---:|---:|
|17|16|4|-4|2|
|41|32|16|0|2|
|73|16|12|4|2|
|89|48|20|-4|2|
|97|16|4|-4|2|
|113|32|24|8|2|
|137|32|16|0|2|
|193|16|4|-4|2|

TypeScript uses bigint and enumerates y,z with exact square testing of the residual. Wolfram independently enumerates full triples and computes a truncated symbolic product. They agree on every row. Every term in the positive quadratic form is bounded by n, proving the enumeration box exhaustive. Product factors of degree above 200 cannot affect these coefficients. This proves finite coverage, not universal BSD. An early mental count at 17 omitted y=0 triples and was discarded before acceptance. Tunnell's printed table divides by sigma0(n); its -2 at 17 means a(17)=-4.

## Descent conventions and E41 rank certificate

Use Zhang's odd Monsky matrix M=[[A+D2,D2],[D2,A+D(-2)]], where A_ij=[p_j/p_i] off the diagonal, A_ii=[(n/p_i)/p_i], and [u/p]=(1-(u/p))/2. The vector order is valuations of d2 followed by valuations of d1. Wang reverses these blocks; we do not mix conventions. The pure dimension is 2k-rank_F2 M. This is an established theorem as restated in Zhang; the original Monsky appendix was not inspected and a from-scratch local descent is not claimed.

For every prime p=1 mod8, M is the zero 2-by-2 matrix, so dim Sel2=4 and the rank upper bound is two. The exact sequence is

    0 -> E(Q)/2E(Q) -> Sel2(E/Q) -> Sha(E/Q)[2] -> 0.

The Kummer map, with kernel 2E(Q), is delta(x,y)=(x-n,x+n,x) modulo rational squares. Its special values are delta(O)=(1,1,1), delta(n,0)=(2,2n,n), delta(0,0)=(-n,n,-1), delta(-n,0)=(-2n,2,-n). None of the three nonzero torsion classes is trivial, because a coordinate is 2 or -1. Thus E[4](Q)=E[2](Q) has order four, with no higher rational 2-power torsion.

On E41, P=(-9,120) and Q=(841,24360) satisfy the equation exactly. Along with T+=(41,0), T0=(0,0), their Kummer triples are

    (2,82,41), (-41,41,-1), (-50,32,-9), (800,882,841).

The last two reduce to (-2,2,-1) and (2,2,1). In the squareclass basis (-1,2,41), separately for each coordinate, the four vectors are

    T+  0 1 0 | 0 1 1 | 0 0 1
    T0  1 0 1 | 0 0 1 | 1 0 0
    P   1 1 0 | 0 1 0 | 1 0 0
    Q   0 1 0 | 0 1 0 | 0 0 0

Their rank is four: in a relation, coordinate one's 41-valuation eliminates T0, coordinate three's 41-valuation eliminates T+, coordinate one's sign eliminates P, and its 2-valuation eliminates Q. Consequently rank E41>=2; the Monsky bound gives equality. The exact sequence gives Sha(E41)[2]=0 and hence Sha(E41)[2^infinity]=0. No saturated basis is asserted. Analytically this run has only L(E41,1)=0, not an exact order-two certificate.

## E17 algebraic baseline without analytic rank

Zhang's Theorem 3.2 proof provides the first Cassels pairing on the pure basis Lambda=(1,p,p), Lambda'=(p,1,p). For p=1 mod8, the Redei matrices are R_p=[0], R_(-p)=0_(2x2), yielding h4(p)=0, h4(-p)=1. The unique nontrivial divisor in the norm condition is d=p. For the tested primes it is a norm explicitly: 17=1^2+4^2, 41=5^2+4^2, 113=7^2+8^2 and (p/a)^2-p(b/a)^2=p when p=a^2+b^2.

Choose p=2mu^2-tau^2 with mu=p mod4. Then the off-diagonal pairing sign is (-mu/p). The pairing is alternating, not just symmetric in characteristic two; Fisher-Schaefer-Stoll Section 4 explicitly states the diagonal +1 and its Sel4-image kernel.

For 17 use mu=-3,tau=1. The sign (3/17)=-1 gives a nondegenerate pairing. The local calculation can be reconstructed: put u=2mu-tau=-7, w=-mu+tau=4. The Lambda-covering equations are

    -t^2+u2^2-u3^2=0,
    -17t^2+17u3^2-u1^2=0,
    34t^2+u1^2-17u2^2=0.

The needed tangent factors are L1=u2-u3 and L3=8t+u1+7u2. At 17 choose (1,0,sqrt(2),1) with sqrt(2)=6 mod17; Hensel lifting applies. Then L1*L3=12 mod17 and (12,17)_17=(3/17)=-1. At 2, 17 is a square in Q2, so the symbol is +1; at infinity it is positive. At the other primes the integral good-prime tangent lemma applies. This gives the global sign without a numerical L-value.

Rational-point classes lie in the pairing radical. Its pure radical is zero, so rank E17=0 and Sha(E17)[2]=(Z/2)^2.

Let S=Sel2, U=Sel4 and I=Im(U->S). Wang (1.1) gives

    0 -> E[2](Q)/2E[4](Q) -> S -> U -> I -> 0.

The pure radical is I/E[2](Q), using the Kummer image. If the pure dimension is two and the pairing rank is rho, then |I|=4*2^(2-rho) and |U|=(16/4)|I|=2^(6-rho). For E17, |Sel4|=16. The point quotient modulo four has size four, so |Sha[4]|=4 and Sha[4]=Sha[2]. This excludes elements of order four, hence all higher 2-power orders. Therefore Sha(E17)[2^infinity]=(Z/2)^2 without an assumption of finiteness. Independently a(17)=-4 gives L(E17,1)=4 beta/sqrt(17)>0. This is a known rank-zero equality checked by separately interpreted analytic and algebraic evidence.

## Executed follow-up: same Sel2, Sel4 and first pairing, different ranks

|p|mu|tau|(-mu/p)|pairing rank|Sel2 order|Sel4 order|
|---:|---:|---:|---:|---:|---:|---:|
|17|-3|1|-1|2|16|16|
|41|5|3|+1|0|16|64|
|113|9|7|+1|0|16|64|

The norm identities, sign conventions and residue symbols were checked in both implementations; Wolfram also enumerated quadratic residues independently of JacobiSymbol.

For 113, a(113)=8 certifies a nonzero L-value. The established Coates-Wiles consequence in Tunnell pp.329-330 gives rank E113=0. This rank is analytically derived, not an independent algebraic cross-check. It nevertheless refutes a proposed data-only rank rule when compared with rank E41=2.

The abstract groups agree, not just their sizes. For both curves the pairing is zero, so pi:U->S is onto. The inclusion-induced j:S->U has kernel of order four, and j*pi=[2] on U. Hence |2U|=4, |U|=64, and 4U=0. Writing U=(Z/4)^a+(Z/2)^b gives a=b=2. Thus both have Sel2=(Z/2)^4 and Sel4=(Z/4)^2+(Z/2)^2 with identical zero first pairing but different ranks. Marked rational-point images are not retained in this coarse data.

For E41, Sha[4]=0. For E113, the point quotient modulo four has order four, giving |Sha[4]|=16, while |Sha[2]|=4. Since its exponent divides four, Sha(E113)[4]=(Z/4)^2. Sha(E113)[8] and the full 2-primary group have not been determined here.

For all m>=1, the established E17 and E41 certificates further imply

    |Sel_(2^m)(E17)|=16,
    |Sel_(2^m)(E41)|=4*2^(2m).

This uses the point/Sha exact sequence and proved torsion/ranks, not extrapolation from four numerical examples. Wolfram checked the first four values only as arithmetic sanity checks.

## Specialization route and its precise limitation

For R=k[[T]] and a finite-length module M=sum R/(T^e_i), length(M)=sum e_i, dim_k(M/TM)=number of factors, and their difference is sum(e_i-1). Equality holds exactly when TM=0. Each cyclic factor has the basis 1,T,...,T^(e_i-1), proving these formulas and the filtration identity length(M)=sum_(j>=1)dim(T^(j-1)M/T^j M).

Perfect alternating duality does not suffice to enforce equality. On M_e=(R/(T^e))^2, the pairing T^(-e)(x1*y2-x2*y1) modulo R in k((T))/R is well-defined, alternating and perfect: changing lifts changes only an element of R, and opposite basis vectors detect every nonzero coordinate. Both the module and its dual have length 2e. Its skew presentation [[0,T^e],[-T^e,0]] has determinant T^(2e) and fiber dimension two. Taking e=1 versus e=2 keeps dimension, perfect duality and even parity but changes length.

These are algebra-only countermodels, not asserted realizations of elliptic-curve Selmer modules. Actual Iwasawa pairings may have additional involutive structures; the existing root checkpoint separately discusses such examples. Neither calculation proves that arithmetic nondegeneracy is impossible. Similarly, (Z/2^h)^2 and (Q2/Z2)^2 have the same 2^m-torsion for m<=h but different divisible corank; no Sha realization is asserted.

The current Burungale-Tian theorem is a CM rank-zero p-converse for every prime p, not a higher-rank theorem. Its input is infinite Selmer corank zero. Reading its proof locates the first failed attempted extension: vanishing of the finite Selmer space yields a rationalized H2 vanishing, then a one-dimensional global space and a specialized zeta basis; localization outside the finite local condition gives L-nonvanishing by reciprocity. Positive rank does not supply those implications. E17 meets the input at p=2; E41 does not. We audited this implication, not the complete original Kato/Rubin proofs.

## Sources actually used

Tunnell, Invent. Math. 72 (1983), 323-334, DOI 10.1007/BF01389327; scanned original at https://sites.math.rutgers.edu/~zeilberg/EM22/JT1983.pdf, especially pp.328-330.

Shenxing Zhang, arXiv:2111.11618v1 (23 November 2021; internal date November 24), https://arxiv.org/pdf/2111.11618; pp.3-8, equations (2.2)-(2.5), (2.8)-(2.10), Lemmas 2.1/3.1 and Theorem 3.2 proof. The original Monsky appendix remains an unaudited foundational dependency of the restated descent theorem.

Zhangjie Wang, arXiv:1511.03810v2 (11 June 2016; fetched PDF also has internal July 20, 2021 date), https://arxiv.org/pdf/1511.03810; p.2 equation (1.1) and pp.4-5 pairing kernel. Journal DOI 10.1007/s11425-015-0741-3.

Fisher, Schaefer and Stoll, The yoga of the Cassels-Tate pairing, author PDF dated March 4, 2009, https://www.mathe2.uni-bayreuth.de/stoll/papers/yoga.pdf; Sections 2-4 and Theorem 6.3 with its concluding proof. Diagonal +1, Sel4-image radical, Kummer sequence and identification with the pairing trivial on rational points. No Sha finiteness assumption is needed.

Burungale-Tian, arXiv:2506.03465v2 (11 October 2025), https://arxiv.org/pdf/2506.03465; Theorems 1.1, 2.6, 3.1 and pp.5-6 deduction. Annals of Mathematics 203 (2026), 1-13, DOI 10.4007/annals.2026.203.1.1, metadata independently checked at https://annals.math.princeton.edu/2026/203-1/p01.

CMI current BSD page https://www.claymath.org/millennium/birch-and-swinnerton-dyer-conjecture/ still labels the problem Unsolved. Wiles's official target https://www.claymath.org/wp-content/uploads/2022/05/birchswin.pdf and the currently posted four-page rules https://www.claymath.org/wp-content/uploads/2022/03/millennium_prize_rules_0.pdf were read. $1m allocation, qualifying publication, at least two years, acceptance and CMI discretion remain separate from mathematical work. BSD counterexamples fall under rule 5(c); no direct submissions, publication or contact were made. No award is promised.

## Execution and next checkpoint

Observed Node 22.16.0, TypeScript 5.8.3 and Wolfram Language 15.0.1. The code is exact and dependency-free at runtime. Run npm run lint, npm run typecheck, npm test, then node dist/src/run.js. The lint script uses compiler unused/unreachable diagnostics, not a separate ESLint/Biome tool. One native Node test file contains 32 explicit assertions. Tests include deliberate bad inputs. Wolfram code is separately written; agreement is an implementation cross-check, not independent expert verification. The symbolic module invocation returned an undefined-T warning, retained in its transcript; the paper proof does not depend on that warning-free execution. Failed optional package provisioning (EAI_AGAIN) is recorded rather than represented as a successful install.

False auxiliary routes are preserved: full first-stage data does not determine rank; adding the first Cassels pairing and Sel4 abstract group does not suffice; perfect alternating duality alone does not determine characteristic length. None falsifies BSD.

The next mathematical step is already chosen: reconstruct a genuine 4-to-8 descent obstruction for E113, starting from the generalized Sel4-by-Sel2 pairing in Fisher-Schaefer-Stoll, and compare its liftable classes with E41. Specify covering functions and local certificates rather than guessing higher Sha orders. In parallel the all-rank mechanism still needs arithmetic control of higher augmentation layers and a comparison with the complex order. This supplement does not repeat the existing root checkpoint's larger scan or claim its results as independently checked.

All jobs reported here completed. No process is continuing in the background. No full solution, formal proof, independent expert review, publication, prize submission, or new spending occurred.
