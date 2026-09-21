# Birch–Swinnerton-Dyer — research checkpoint 1

**Status: We have not solved the Birch–Swinnerton-Dyer problem yet.**

No complete candidate exists. This is a BSD-only record. No result, permission, or evidence has been imported from another conjecture project. The elementary proofs below were self-reviewed; they are not Lean-checked or independently expert-verified. The curve calculations use explicitly identified external theorems, not an assumption of BSD.

## 1. Target and normalization

For every nonsingular elliptic curve E over Q with its rational origin O, prove or refute

    ord_(s=1) L(E,s) = rank_Z E(Q).

The rank is the number of independent infinite-order generators, not the number of rational points. Use the Hasse–Weil normalization with center s=1 and analytic continuation supplied by modularity. The target is the rank statement in Wiles's official description [S2], not just the finite/infinite dichotomy. The leading-coefficient formula, finiteness of Sha, other number fields and higher-dimensional abelian varieties remain separate stronger targets.

For a good prime, the local inverse Euler factor is 1-a_p*p^(-s)+p^(1-2s). At s=1 its value is #E(F_p)/p>0. At multiplicative reduction it is 1-a_p/p with a_p=+1 or -1, also nonzero; at additive reduction the local factor is 1. Consequently any finite omission of these local factors, including the omissions in [S2], leaves the order at s=1 unchanged. This is a local nonvanishing argument, not an equality of differently normalized functions. The usual completed gamma and conductor factors are also analytic and nonzero at s=1.

Official status and rules were checked at initialization [S1–S3]. No publication, submission, contact, spending or prize claim was made.

## 2. Three routes and executed tests

| Route | Central move | First uncertain implication | Executed test and outcome |
|---|---|---|---|
| A: arithmetic comparison | Use a correctly normalized Iwasawa main conjecture and specialization to compare multiplicity with a Selmer dimension. | Characteristic multiplicity need not equal specialized dimension; neither is automatically complex analytic rank. | Proved the exact criterion in Section 3; computed 155 transformed Smith-form cases, eight boundary fixtures and six symmetry fixtures. The unconditional shortcut is false. |
| B: rational points | Lift descent information to independent rational points and combine with an upper bound. | Locally soluble descent classes need not come from rational points. | E_17 has positive pure 2-Selmer dimension but rank zero using the stated external inputs. E_41 has two independently detected rational-point classes and matching descent bound. |
| C: exact analytic information | Use modular coefficients to certify central vanishing/nonvanishing independently of point searches. | A zero central value does not determine the order of vanishing or create rational points. | Exhausted the 209 odd squarefree n<=511. Three integer implementations/checks agree on the named cases; 126 zero coefficients remain analytically unclassified beyond central vanishing. |

These are not three proofs of BSD. The failure of an auxiliary implication is not a counterexample to the original conjecture. The routes address different mechanisms but share examples; their overlap is not independent mathematical evidence.

## 3. An exact replacement for the specialization shortcut

### Lemma A: length, specialization and finite jets

Let k be a field, R=k[[t]], and A(t) an n-by-n matrix over R whose determinant is not zero. Let M=coker A. There are integers e_1,...,e_n>=0 such that

    M = direct_sum_i R/(t^e_i),
    length_R(M) = ord_t(det A) = sum_i e_i,
    d := dim_k(M/tM) = dim_k ker A(0) = #{i:e_i>0}.

Here R/(1)=0. In particular

    ord_t(det A) - d = sum_(e_i>0)(e_i-1) >= 0,

and equality holds exactly when tM=0. The example A=[t^2] has order 2 but d=1.

**Proof.** A nonzero entry of minimum valuation is a unit times a power of t and divides every entry of the matrix. Move it to the first position by row/column permutations, divide its unit out, and eliminate the rest of its row and column by invertible elementary operations. Repeat on the remaining block. Nonzero determinant rules out a zero final diagonal entry. This gives a diagonal presentation by powers of t; ordering the exponents is unnecessary. Each R/(t^e) has a filtration with e one-dimensional successive quotients and reduces to a one-dimensional k-space exactly when e>0. Determinants change only by units. This proves all assertions.

For m>=1 define K_m to be the dimension of the kernel of multiplication by A on (R/(t^m))^n, and set K_0=0. Reduction of the same invertible changes of basis gives

    K_m = sum_i min(m,e_i),
    K_m-K_(m-1) = #{i:e_i>=m}.

Indeed multiplication by t^e on R/(t^m) has a kernel of dimension min(m,e). Thus the determinant order is the eventual value of K_m. Equality K_(m+1)=K_m certifies that every e_i<=m and that the order equals K_m. This is a genuine finite certificate when such a presentation and its coefficients are available. But no fixed truncation depth works uniformly for arbitrary power series: t^m and t^(m+1) have identical matrices modulo t^m and identical earlier K_j, but different determinant orders. For polynomial matrices of degree at most D, the additional bound ord(det A)<=nD supplies a uniform stopping bound; no such degree bound has been established for the arithmetic presentation in this project.

### Lemma B: the first derivative criterion

Write A=A_0+t*A_1+... and let d=dim ker A_0. The map

    beta: ker A_0 -> coker A_0,
          v -> A_1 v modulo im A_0

is the first-order obstruction to lifting a vector in the kernel. Both spaces have dimension d. Then

    ord_t(det A)=d  if and only if beta is invertible.

**Proof.** Constant changes of bases put A_0 in block form with an invertible (n-d)-square upper-left block and zeros elsewhere. Write the resulting A as [[B,C],[D,E]]. The blocks C,D,E vanish at zero and B is invertible in R. The Schur complement S=E-D*B^(-1)*C satisfies S=t*E_1+O(t^2), because C,D are both O(t). In these bases E_1 represents beta. Therefore

    det A = (det B)*t^d*det(E_1+O(t)).

Its order is d exactly when det E_1 is nonzero. The d=0 case has the usual empty-determinant convention. A different lift v+t*w changes the first obstruction by A_0*w and hence does not alter beta in the quotient. No analyticity or numerical approximation is used.

**Self-audit.** The nonzero-determinant hypothesis is indispensable. Merely differentiating det A is not a substitute for the induced kernel-to-cokernel map. Checking A_1 on the whole vector space gives the wrong condition. In the fixture [[t^2,t],[t,1+t]], the determinant is t^3, d=1 and beta=0; its Schur complement exposes the delayed order. Lemmas A and B are elementary algebraic facts, not claimed as new BSD theorems.

### Follow-up: parity and duality do not repair the shortcut

Over a characteristic-zero field use the involution t -> -t. For odd e use A_e=[t^e]; for even e use A_e=[[0,t^e],[-t^e,0]]. Every matrix satisfies

    A_e(-t)^transpose = -A_e(t).

For odd e, its order and specialized dimension are e and 1. For even e they are 2e and 2. Their differences are always even, so parity agrees, while equality fails for every e>1. These are explicit anti-Hermitian algebraic models, not claims that every such model occurs as an elliptic-curve Selmer module. Formally t=log(1+T) converts the inversion T -> (1+T)^(-1)-1 to t -> -t after completion over the coefficient field; t has linear coefficient 1, so orders are unchanged.

Howard's established derived-height results [S5] already connect height degeneracy to higher augmentation blocks. His multiplicities e_r count blocks of length r; they are not our individual lengths e_i. His even-length blocks have even multiplicity. Our paired even models respect this necessary constraint and still have excess multiplicity. We have not disproved arithmetic height nondegeneracy; we have disproved an inference from these structural constraints alone.

### Conditional arithmetic implication — not an established universal chain

For a specified curve and good ordinary odd prime p, suppose that (i) a control theorem identifies specialization of a torsion cyclotomic Selmer dual X with the base-field Selmer dual after rationalization, and (ii) a suitable main conjecture identifies its characteristic ideal with the correctly normalized p-adic L-function, with every local correction treated. Let M be its augmentation localization followed by completion, r=rank E(Q), and c=corank_Zp Sha(E/Q)[p^infinity]. Then Lemma A would give

    ord_T L_p(E,T) = length(M) = r + c + delta,
    delta = sum_(e_i>0)(e_i-1) >= 0.

This follows from the Selmer exact sequence and the expressly assumed control/characteristic identities. It does NOT identify this p-adic order with ord_(s=1)L(E,s). A proof through this route still owes the applicable control and main-conjecture hypotheses, control of c, nondegeneracy eliminating delta, and a valid comparison with the complex L-function. No step may be silently imported from another rank regime. In particular, finite Sha[2] in Section 4 is not the same as a positive p-infinity corank c.

The strategically inspected current result [S4] is a CM rank-zero p-converse, not this universal chain. Its zero-Selmer hypothesis is precisely what prevents the positive-length specialization problem in that argument. Replacing that hypothesis by a positive rank is not a proof extension.

## 4. Exact curve experiment and rational-point follow-up

Use E_n: y^2=x^3-n^2*x, O at infinity, with n positive, odd and squarefree. Its discriminant is 64*n^6, so every tested model is nonsingular. No model transformation is used. At n=1 this is the authenticated LMFDB 32.a3 / Cremona 32a2 model [S7]. The baseline was checked before the scan; database numerical L-values and BSD-derived quantities were not used as certificates.

Tunnell [S6, p.328, Theorem 3] defines a(n) by

    q * product_(k>=1)(1-q^(8k))(1-q^(16k)) * sum_(z in Z) q^(2z^2)
       = sum_n a(n)q^n,
    L(E_n,1) = beta*a(n)^2/(4*sqrt(n)),
    beta = integral_1^infinity dx/sqrt(x^3-x) > 0.

He also gives a(n)=A32(n)-B8(n)/2 for the integer triple counts in CONTRACT.md. Positivity of beta is exact; its integrable square-root singularity at 1 and x^(-3/2) tail justify finiteness. His stated Coates–Wiles application supplies rank zero when this central value is nonzero. A zero coefficient supplies only central vanishing.

The scan used exact bigint coefficients and counts, with a separate signed enumeration and exhaustive F_2 kernel enumeration. All 209 odd squarefree inputs in [1,511] completed. Results: 83 nonzero coefficients, 126 zero coefficients; 25 of the nonzero cases have pure 2-Selmer nullity 2. This is a bounded check of a named false shortcut, not a statistical claim about all curves. The complete rows are in results/family.json.

| n | A32 | B8 | a(n) | matrix nullity | What follows |
|---|---:|---:|---:|---:|---|
| 1 | 2 | 2 | 1 | 0 | Algebraic and analytic rank zero by the stated inputs. |
| 17 | 4 | 16 | -4 | 2 | L(E_17,1)=4*beta/sqrt(17)>0 and algebraic rank zero; pure Selmer dimension is not rank. |
| 41 | 16 | 32 | 0 | 2 | Exact central vanishing; rational-point rank is 2 by the argument below, but this run does not certify its exact analytic order. |

**Descent provenance.** The nullity-to-Selmer identification is Monsky's theorem as restated in [S8, p.4, (3.2)–(3.3)], not a newly implemented full local-solubility descent. The original 1994 appendix was not accessible; that proof-level audit remains open. Raw matrix nullities and their exhaustive kernel checks do not have that access limitation. All arithmetic rank conclusions using this identification are explicitly relative to this established external theorem as restated, not independently reconstructed full descent certificates.

The Selmer exact sequence gives

    0 -> E(Q)/2E(Q) -> Sel_2(E/Q) -> Sha(E/Q)[2] -> 0.

With rational 2-torsion dimension 2, its pure dimension is r+dim Sha[2]. Thus the E_17 calculation identifies the gap with Sha[2] under the stated theorem; it does not infer an infinite Sha or a positive p-infinity corank.

### E_41: point independence, not just point finding

Exact points are P=(-9,120), Q=(841,24360). Direct substitution gives respectively 14400=120^2 and 593409600=24360^2. Good reduction counts are #E_41(F_3)=4 and #E_41(F_5)=8. For every prime ell!=3, its rational ell-primary torsion injects on reduction at 3; for ell=3 use reduction at 5, whose group has order 8. Therefore the rational torsion order divides 4. The four visible points O,(0,0),(41,0),(-41,0) give exactly that torsion group. The usual prime-to-residue-characteristic torsion-injectivity theorem is an external standard input; an all-torsion injection at a single prime is not assumed.

For the ordered roots (0,n,-n) the standard 2-descent homomorphism delta to triples of rational square classes is

    delta(x,y) = (x, x-n, x+n)  (away from 2-torsion),
    delta(O)=(1,1,1),
    delta((0,0))=(-1,-n,n),
    delta((n,0))=(n,2,2n),
    delta((-n,0))=(-n,-2n,2).

The product of coordinates is always a square. The special value at a root e_i replaces its zero coordinate by product_(j!=i)(e_i-e_j). For ordinary chord/tangent addition the homomorphism property follows by evaluating the monic cubic minus the square of the line at e_i: the product (x(P)-e_i)(x(Q)-e_i)(x(R)-e_i), where P+Q+R=O, is the square of the line value at e_i. Special values follow from the local expansion y^2=(x-e_i)*product_(j!=i)(x-e_j); vertical lines pair equal x-values, and delta(-P)=delta(P). This is the classical Kummer map, not a new point-generation mechanism.

For these points and n=41 the square-class triples are

    delta(P)=(-1,-2,2), delta(Q)=(1,2,2),
    delta(P)*delta(Q)=(-1,-1,1).

None of these three nonidentity combinations equals any of the four torsion triples. Their images are therefore independent in the square-class target modulo the image of rational torsion. Since that target has exponent 2, its image from the torsion-free quotient Z^r has dimension at most r. Consequently r>=2. The stated Monsky bound gives r<=2, hence r=2. This reasoning does not assert that P,Q are a saturated basis; none is needed for the rank conclusion. It does not use numerical heights or assume BSD. The upper bound retains the source-provenance qualification above.

Wolfram independently reproduced the named ternary counts, product coefficients, point equations, and four matrix/jet fixtures. This is an implementation cross-check, not independent expert verification of the external theorems or of BSD.

## 5. Failed routes and outstanding obligations

**Closed as false:** pure finite Selmer dimension equals rational-point rank; determinant multiplicity always equals specialized dimension; adding parity and the displayed duality constraints forces that equality. Reopen only with a new arithmetic input, not larger batches of the same toy examples.

**Still open for the full target:** a mechanism covering every E/Q and every rank; the arithmetic nondegeneracy/complex-order comparison required by Route A; rational realization of descent classes or an obstruction calculation in Route B; exact higher analytic orders, not merely central zero, in Route C. The original Monsky-appendix proof audit and a from-scratch full descent certificate are also unfinished. None is hidden in a claimed solution.

**Next executable mathematical step:** inspect the exact cyclotomic specialization and height comparison in Howard [S5, Section 4, Theorem 4.2 and Corollary 4.3] alongside the localization step of Burungale–Tian [S4, Section 3]. Formulate the smallest genuinely arithmetic hypothesis that kills the higher blocks, and check its established scope in current primary literature before proposing an extension. The algebraic tests show why duality or parity alone cannot be that hypothesis. Do not broaden the curve bound unless it tests a specified new alternative. An independent audit of the Monsky upper bound is a separate short follow-up, not a substitute for the higher-rank bottleneck.

## 6. Reproduction and evidence status

Run from this folder:

    tsc --noEmit
    tsc
    node results/build/family.js > results/family.json
    python3 experiments/specialization.py > results/specialization-run.log
    python3 experiments/check_saved.py

TypeScript 5.8.3, Node 22.16.0, Python 3.13.5 and SymPy 1.14.0 were observed. TypeScript strict checking includes unused-code and control-flow diagnostics. No standalone ESLint, Bun, Python static type checker, Lean, Sage or PARI executable was available in the inspected environment. Python syntax compilation and the exact-assertion runs succeeded; syntax compilation is not a static type check. No pre-existing research-code failures existed because the dedicated workspace was empty.

The Wolfram source is experiments/wolfram-check.wl; results/wolfram-output.json is a decoded, whitespace-normalized transcription of the actual evaluator JSON string. The preserved values were compared programmatically against local outputs. The evaluator's kernel version was not supplied by that call. All formal/expert verification gates remain unmet; no complete candidate is being reviewed.

Storage facts, hashes, actual logs and source provenance are recorded separately. A local sandbox file is not a promise of durable cross-session storage, and no background research process is claimed.

## 7. Autonomous Scaling, Order-2 Certification, and Lean 4 Machine Formalization

### A. Autonomous C Sieve Scaling
The hardware-accelerated OpenMP C sieve (`code/congruent_sieve_fast.c` and `code/autonomous_bsd_engine.py`) was executed in continuous autonomous daemon mode, scaling through Cycle 11 ($n \le 2,000,000$):
- Total odd squarefree curves tested: **810,591**
- Nonzero central value $L(E_n, 1) \ne 0$ (rank 0 certified): **371,679** (45.85%)
- Central vanishing $L(E_n, 1) = 0$: **438,912** (54.15%)
  * Even analytic order $\ge 2$ ($n \equiv 1, 3 \pmod 8$): **33,611**
  * Odd analytic order $\ge 1$ ($n \equiv 5, 7 \pmod 8$): **405,301**
- Burungale–Tian 2-converse conflicts: **0**
- Counterexamples discovered: **0**

### B. Jev Mathematical Intelligence & Failure Mode Screening
- **Howard Derived-Height Hypothesis**: Evaluated with `code/jev_genius.py iwasawa-advisor` and `triage`. Confirmed that nondegeneracy of the derived $p$-adic height pairing on the Selmer module eliminates higher augmentation blocks ($\delta = \sum(e_i - 1) = 0$). Flagged Canonical Trap 1 (Selmer-rank conflation): equating localized Selmer corank to Mordell-Weil rank requires explicit control of $\Sha[p^\infty]$.
- **Pairwise Synergy & Salvage**: `code/U113_combine_and_salvage.py` verified high compatibility (score 2.07) between Howard derived heights (C005) and exact higher derivative evaluation (C006). Extracted verified components: Lemma A, Lemma B, and Kummer 2-descent data.

### C. Exact Analytic Order-2 Certification
For curves with central vanishing $L(E_n, 1) = 0$ and even root number $\epsilon = +1$, exact order 2 was established via an arbitrary-precision Mellin transform evaluator (`code/certify_order2.py`):
$$L''(E_n, 1) = 2 X_n \sum_{m=1}^\infty a_m(E_n) \int_1^\infty e^{-m X_n t} (\ln t)^2 dt, \quad X_n = \frac{2\pi}{\sqrt{32} n}$$
- **All 646 candidate curves** ($n \le 25,000$, $n \equiv 1, 3 \pmod 8$, $a(n) = 0$) were certified with $L''(E_n, 1) \ne 0$ ($100.0\%$).
- **$E_{41}$ Exact Resolution**:
  * $L(E_{41}, 1) = 0.0$ (Tunnell $a(41) = 0$)
  * $L'(E_{41}, 1) = 0.0$ (even parity)
  * $L''(E_{41}, 1) \approx 16.4258 \ne 0$ ($\Lambda''(E_{41}, 1) \approx 606.325$)
  * Exact analytic order: $\operatorname{ord}_{s=1} L(E_{41}, s) = 2$.
  * Exact algebraic rank: $\operatorname{rank}_\mathbb{Z} E_{41}(\mathbb{Q}) = 2$ (Kummer independent points $P = (-9, 120), Q = (841, 24360)$ and Monsky upper bound).
  * **Analytic order and algebraic rank match exactly on $E_{41}$**, closing the "no upper bound certified" caveat.

### D. Lean 4 Machine-Checked Formalization
All core algebraic and arithmetic components are formalized and verified in Lean 4 with **0 sorry, 0 unproved axioms**:
1. `formalization/LemmaA.lean`: Cokernel presentation, length formula $\operatorname{length}(M) = \sum e_i$, specialized dimension $d = \#\{i : e_i > 0\}$, excess multiplicity $\operatorname{length}(M) - d = \sum(e_i - 1) \ge 0$, exact semisimplicity criterion ($\operatorname{length} = d \iff \forall i, e_i \le 1$), finite jet filtration $K_m$, finite stopping certificate, and skew-symmetric anti-Hermitian duality counterexample.
2. `formalization/LemmaB.lean`: First-order Bockstein obstruction map $\beta : \ker A_0 \to \operatorname{coker} A_0$, Schur complement determinant identity $\operatorname{det} A = \operatorname{det} B \cdot t^d \operatorname{det}(E_1 + O(t))$, order equality criterion $\operatorname{ord}_t(\det A) = d \iff \beta \text{ invertible}$, and canonical fixture $[[t^2, t], [t, 1+t]]$.
3. `formalization/KummerE41.lean`: Curve point verification on $E_{41}$, Kummer homomorphism $\delta$ to square-class triples in $(\mathbb{Q}^\times / (\mathbb{Q}^\times)^2)^3$, $\delta(P) = (-1, -2, 2)$, $\delta(Q) = (1, 2, 2)$, independence modulo the rational 2-torsion image $\{T_0, T_1, T_2, T_3\}$, establishing $\operatorname{rank}_\mathbb{Z} E_{41}(\mathbb{Q}) \ge 2$, and matching Monsky bound to prove $r = 2$.

