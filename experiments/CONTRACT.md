# BSD bounded experiments — declared before execution

Scope: this project only. These are auxiliary-lemma tests, not a search that can certify BSD for all curves.

## F1 — exact congruent-number coefficients and descent matrices

- Domain: every odd squarefree integer 1 <= n <= 511, with E_n: y^2=x^3-n^2*x, origin at infinity, discriminant 64*n^6.
- Baseline: E_1, authenticated as LMFDB 32.a3 / Cremona 32a2. Reconstruct a(1)=1 exactly before the scan; do not use a numerical database L-value as a certificate.
- A32(n) counts integer triples with 2*x^2+y^2+32*z^2=n; B8(n) replaces 32 by 8. Enumerate nonnegative x,z with exact square-root testing and restore signs. Independent checker enumerates signed triples. Positivity of all three coefficients proves the coordinate bounds; there is no other pruning.
- Independently multiply q*product_{k>=1}(1-q^(8k))*(1-q^(16k))*sum_{z in Z}q^(2*z^2), truncated at degree 511. All factors have nonnegative degrees; factors/terms whose first positive degree exceeds the bound cannot affect a retained coefficient. Assert 2*A32-B8=2*a(n) for every retained n.
- For each n use the odd Monsky matrix as restated in Das–Mondal, arXiv:2604.26183v1, p.4, (3.2)–(3.3). F_ij=[p_j/p_i] for i!=j, diagonal is the row sum; D_l=diag([l/p_i]); M=[[D_2,F+D_2],[F+D_-2,D_2]]. The additive Legendre symbol is 0 for a square, 1 for a nonsquare. The empty matrix at n=1 has nullity zero.
- Exact F_2 row reduction is checked by exhaustive enumeration of all kernel vectors. Cross-check each Legendre symbol by enumerating nonzero quadratic residues, independently of Euler's criterion.
- Arithmetic: bigint for integer coefficients, inputs, point coordinates, counts and finite-field bit masks; bounded array indices and dimensions are exact JavaScript integers. Serialize mathematical integers as decimal strings.
- The matrix theorem identifies nullity with dim Sel_2(E_n/Q)-2, NOT with Mordell–Weil rank. Its original 1994 appendix was not accessible in this run; retain that provenance limit and do not call this an independently reconstructed full descent certificate.
- Tunnell's Theorem 3, Invent. Math.72 (1983), p.328, gives L(E_n,1)=beta*a(n)^2/(4*sqrt(n)), beta>0. Nonzero a certifies nonzero L, and his stated Coates–Wiles application gives algebraic rank zero. Zero a certifies only L(E_n,1)=0, not its exact vanishing order or positive algebraic rank.
- Named alternative: finite 2-Selmer rank can strictly exceed rational-point rank. A nonzero coefficient with positive matrix nullity refutes the shortcut, not BSD. No numerical analytic rank is computed.
- Follow-up: check exact points (-9,120),(841,24360) on E_41, square classes in the 2-descent map, and torsion bounds from good reduction at 3 and 5. Point independence requires the separately recorded Kummer homomorphism argument; an on-curve test alone is not independence.

## A1 — multiplicity, specialization, and finite jets

- Domain: matrices over Q[T] invertible over Q(T). Explicit boundary/negative fixtures plus U*diag(T^e_i)*V, dimensions 1..3, all e_i in {0,1,2,3,4}, fixed polynomial unimodular U,V defined in the checker. No random sampling.
- Examine orders det A, nullity A(0), first derivative induced from ker A(0) to coker A(0), and kernels modulo T^m for m=1..5.
- SymPy exact rational linear algebra. No floating-point tolerance.
- Assertions: ord(det A)>=dim ker A(0); equality iff the induced derivative is invertible; K_m=sum_i min(m,e_i). These finite checks test implementation only; the general statements require the separate algebraic proofs in RESEARCH.md.
- Negative cases: T^2 and paired skew-symmetric T^2 blocks must refute automatic semisimplicity; an identically zero determinant must be rejected, not assigned a finite order.
- Wolfram is an additional exact-arithmetic implementation check for selected cases, not independent expert review or kernel verification of BSD.

## F2 — apply the audited 2-converse without replacing corank by a finite dimension

Declared after F1 and before this follow-up: use the existing full 209-row output, not a larger bound. Test whether every zero Monsky nullity has nonzero Tunnell coefficient. Mathematical bridge: from the finite and infinite Kummer exact sequences, dim_F2 Sel_(2^infinity)(E/Q)[2]=r+dim_F2 Sha[2]=s2. Hence s2=0 makes the entire 2-primary Selmer group zero. Burungale–Tian Theorem 1.1 applies to these rational CM curves at p=2, despite bad reduction, and forces central nonvanishing. Positive s2 does not force positive corank. Separately, use its explicitly cited root-number rule (footnote 2) to classify exact parity: for odd n=1,3 modulo 8 the sign is +1, otherwise -1. With Tunnell's exact zero, a positive sign supplies order at least 2; a negative sign supplies at least 1. No numerical derivative upper bound is inferred. Source-level dependence of the Monsky identification remains unchanged.
