# We have not solved the Birch–Swinnerton-Dyer problem yet.

## H10 — a simultaneous rational-point family beyond the generic obstruction

Continuation of H9 at private commit `24a88b4b32c41115bd2b9e3dbdcef97cc50ac9b5`, branch `research/h2-endpoint-20260914`. The universal target remains equality of complex analytic order at1 and rational rank for every elliptic curve over Q. H10 proves an algebraic construction on a restricted family, not that equality. It does not use analytic rank, a conjectural BSD formula, or Sha finiteness as an input.

**Result.** For every pair of coprime nonzero integers a,b, put

    D = a^8 - 56 a^4 b^4 + 1296 b^8 = n s^2,

where n is positive squarefree and s is a positive integer. Then n>1, every prime divisor of n is1 modulo8, and explicit points P_minus,P_plus of E_n:y^2=x^3-n^2x are linearly independent modulo torsion. Infinitely many distinct n occur. In particular rank E_n(Q)>=2 throughout this family. The Monsky matrix gives an exact rank2 conclusion for a member when the additional matrix condition in Section6 holds; that condition is not asserted for every member.

These are self-reviewed mathematical deductions using established Kummer/descent foundations, with exact symbolic and finite implementation checks. No assertion of mathematical novelty, formal-kernel verification, independent expert review, or complete BSD solution is made. General rank-two twist constructions already occur in the literature [RS, HH]; the exact scope of their overlap with the displayed polynomial has not been established.

### 1. The new restriction, and why it does not contradict H9

H8 converts two quartic witnesses

    n c_e^2 = A_e^4 + 6 e A_e^2 B_e^2 + B_e^4,  e=-1,+1,

into the two independent pure Kummer classes (1,n,n) and (n,1,n). H9 ruled out producing a companion from one generic witness over Q(t); it did not rule out restricting the parameter to a subfamily where both witnesses have been imposed.

Write F_plus(x)=x^4+6x^2+1 and F_minus(y)=y^4-6y^2+1. The relation y^2-x^2=6 gives F_minus(y)=F_plus(x). Parametrize it by

    x=(t-6/t)/2,  y=(t+6/t)/2,  t=a/b !=0.

After clearing the common denominator B=2ab, set

    A_e=a^2-6e b^2,  B=2ab.

Direct expansion gives the two simultaneous identities

    A_minus^4-6 A_minus^2 B^2+B^4 = D,
    A_plus^4+6 A_plus^2 B^2+B^4 = D.                         (1)

Thus both witnesses are rational from the start, not points over Q(i) whose traces cancel. The passage x=(t-6/t)/2 is a degree-two restriction in the first witness parameter; it is not an identity constructing a second witness for every previously given parameter. In particular, no claim is made that every eligible prime or every zero-coefficient case is represented by D.

An earlier attempted bridge used the explicit degree-six family in [RS, Corollary3.3], after shifting E_1 to y^2=x^3+3x^2+2x. Its parameter is

    g(t)=-6(t^2+4)(t^2-2)(t^2-8).

For t=a/b in lowest terms, all three numerator factors are a^2+b^2 modulo3, which is nonzero for a primitive pair. Therefore v_3(g)=1-6v_3(b) is odd. This particular bridge cannot produce a squareclass equal to a prime1 mod8. This is a restriction on that chosen specialization, not on all constructions in [RS]. It motivated (1), which has no fixed factor3 in its squarefree kernel.

### 2. Explicit points and all denominator checks

For each e=-1,+1 define

    u=n s,
    v_e=A_e^2-e B^2,
    w_e=A_e^2+e B^2,
    z_e=2 A_e B.

Equation(1) implies the ordinary homogeneous quadric identities

    v_e^2-w_e^2+e z_e^2=0,
    u^2-n w_e^2-e n z_e^2=0.                               (2)

The associated map, with the origin of E_n at infinity, is

    P_e=(n w_e^2/z_e^2, n u v_e w_e/z_e^3).                 (3)

Substitution using (2) gives y_e^2=x_e^3-n^2x_e exactly. Its discriminant is64n^6, so n>0 makes the curve nonsingular. Equivalently first construct on E_D and use the rational isomorphism x_n=x_D/s^2,y_n=y_D/s^3; no model or squareclass is silently changed.

There are no excluded nonzero rational parameters hidden in these formulas. B!=0; A_minus=a^2+6b^2>0; and A_plus=0 would require (a/b)^2=6. The numbers v_minus and w_plus are sums of two nonzero squares. Also

    w_minus=a^4+8a^2b^2+36b^4>0.

Finally v_plus=0 would mean a^2-6b^2=+/-2ab, whose roots a/b are +/-1+/-sqrt(7), not rational. Hence u,v_e,w_e,z_e are all nonzero once n,s>0. The displayed points have nonzero y and finite coordinates.

### 3. Positivity, nonsquareness, and prime support

The identity

    D=(a^4-28b^4)^2+512b^8                                 (4)

proves strict positivity. Nonsquareness is not inferred from the finite factorizations.

Here is a self-contained use of Fermat's square-area descent. A rational right triangle of square area can be scaled to a primitive integer right triangle still of square area. Write its legs as2uv,u^2-v^2, where u>v>0 are coprime of opposite parity. Its area uv(u+v)(u-v) is a square. The four factors are pairwise coprime, hence u=r^2,v=s_0^2,u+v=h^2,u-v=k^2. Both h,k are odd. The positive integers U=(h+k)/2,V=(h-k)/2 satisfy U^2+V^2=u=r^2, and their area UV/2=v/4=(s_0/2)^2. Since UV=v/2 is integral, v and s_0 are even; thus this is again an integer right triangle of square area. Its hypotenuse r is strictly smaller than u^2+v^2. Descent contradicts a least positive hypotenuse. Therefore no such rational triangle exists.

Apply (2)-(3) with n=D,s=1 before squarefree normalization. The point has y!=0, and the usual directly verified transformation

    (2D x/y, (x^2-D^2)/y, (x^2+D^2)/y)

gives, after taking positive lengths, a rational right triangle of area D. If D were a rational square the preceding descent would be contradicted. D is therefore a nonsquare integer and its squarefree kernel satisfies n>1. This argument does not assume the rank conclusion it will support.

The primes2 and3 occur to even orders in D. If a is odd, D=1 mod8. If a=2k and b odd, then

    D=16(16k^8-56k^4b^4+81b^8),

with the bracket1 mod8. Thus v_2(D) is0 or4, and the odd unit is1 mod8. If3 does not divide a, then3 does not divide D. If a=3k, primitiveness gives3 does not divide b, and

    D=81(81k^8-56k^4b^4+16b^8).

The bracket is1 mod3 when3 divides k, and2 mod3 otherwise. Thus v_3(D)=4 in this case. Consequently neither2 nor3 divides n.

Let q>3 divide D. Then q divides neither a nor b, since D modulo a or b leaves1296b^8 or a^8. With A=A_plus, equation(1) can be rewritten

    D=(A^2+B^2)^2+(2AB)^2.

Here q does not divide AB: if q divided A then D=B^4 modq, a contradiction. It follows that -1 is a nonzero quadratic residue modulo q. Equation(4), with q not dividing16b^4, similarly shows that -2 is a quadratic residue. The elementary supplementary laws for quadratic residues then give q=1 mod8. This actually controls every prime divisor of D outside2,3, not just those with odd exponent. In particular all prime divisors of n are1 mod8.

### 4. Independence, rather than merely two point formulas

Use the standard full Kummer map in coordinate order (x-n,x+n,x), with kernel2E_n(Q), as recalled in [Z, Section2.1]. Its values at T_plus=(n,0) and T_zero=(0,0) are

    delta(T_plus)=(2,2n,n),   delta(T_zero)=(-n,n,-1).

For e=-1, (2) gives

    x_minus-n=(u/z_minus)^2,
    x_minus+n=n(v_minus/z_minus)^2,
    x_minus=n(w_minus/z_minus)^2.

For e=+1 the first two roles switch. Therefore

    delta(P_minus)=(1,n,n),   delta(P_plus)=(n,1,n).          (5)

The classes -1,2,n are independent in Q^*/Q^{*2}, because n is positive, odd and nonsquare. In their three-dimensional span, the four Kummer vectors are

    T_plus:  0 1 0 | 0 1 1 | 0 0 1
    T_zero:  1 0 1 | 0 0 1 | 1 0 0
    P_minus: 0 0 0 | 0 0 1 | 0 0 1
    P_plus:  0 0 1 | 0 0 0 | 0 0 1.

They are independent: in a relation, the sign of the first coordinate eliminates T_zero, its2-component eliminates T_plus, its n-component eliminates P_plus, and the second coordinate's n-component eliminates P_minus. The minor in columns1,2,3,6 has determinant1. The calculation does not require n to be prime.

The third nonzero rational2-torsion point has class(-2n,2,-n). None of the three nonzero torsion classes is a square triple, so no nonzero rational2-torsion point is divisible by2, and there is no rational4-torsion. Odd torsion is invisible modulo2. The images of T_plus,T_zero thus span the entire torsion contribution. Any nonzero integer relation between P_minus and P_plus modulo torsion can be divided by a common power of2 in the free quotient until an odd coefficient remains; reducing then modulo2 contradicts the four independent Kummer vectors. Hence the two points are independent modulo torsion and rational rank is at least2. Mordell-Weil and the Kummer exact sequence are established inputs, not new foundational theorems proved here.

### 5. Infinitely many distinct twists, not just infinitely many parameters

It is not enough that a/b has infinitely many values: for example D(2,1)=16*41 and D(3,1)=81*41 produce the same squarefree kernel.

Put f(T)=D(T,1). A nonconstant integer polynomial with nonzero constant term has infinitely many prime divisors of its nonzero integer values. To prove the needed elementary lemma, assume those primes form a finite set S containing every prime divisor of c=f(0). Let M be their product. The integer f(cMk)/c is1 modulo M for every integer k; for sufficiently large k its absolute value exceeds1. Any prime divisor of this integer is outside S but divides a value of f, a contradiction.

Now fix any finite set S of already-used prime divisors, including2 and3. Choose a new q outside S dividing f(t_0). The root t_0 modulo q is simple, because

    f'(T)=8T^3(T^4-28),
    f(0)=1296,   f(T) mod(T^4-28)=512.

For q>3 these identities rule out a common root of f and f'. Among the q choices t=t_0+qj modulo q^2, exactly one makes f(t)=0 modq^2, by first-order expansion. Choose any other j. Then v_q(f(t))=1, and q divides the squarefree kernel of f(t). Choosing a nonzero integer in this residue class preserves that valuation. This kernel has a prime factor outside all the previous kernels, so it is new.

Iteration gives infinitely many distinct positive squarefree n, all supported on primes1 mod8, with the two rational points in (3). This infinitude proof neither assumes a squarefree-values conjecture nor asserts that f is irreducible. Indeed f factors, as Section7 emphasizes.

### 6. Exact rank when the independent upper bound applies

Let n=q_1...q_k be any member's squarefree kernel. Define the binary matrix A by off-diagonal entries

    A_ij=(1-(q_j/q_i))/2,

and choose each diagonal entry so its row sum is0 modulo2. The supplementary laws above give D_2=D_{-2}=0 in [Z, equations(2.2)-(2.5)]. Monsky's pure2-Selmer matrix is therefore diag(A,A), so

    rank E_n(Q) <= dim pure Sel_2(E_n)=2k-2 rank_F2(A).

If rank_F2(A)=k-1, the upper bound is2 and agrees with the independent lower bound. The point/Sha exact sequence then gives Sha(E_n)[2]=0, hence Sha(E_n)[2^infinity]=0 without any finiteness assumption. For prime n the matrix is the one-by-one zero matrix and this criterion always holds. There is no prime-infinitude conclusion.

Exact finite certificates in the accepted population:

| (a,b) | D | n | prime factors of n | certified rational rank |
|---|---:|---:|---|---|
| (1,1) |1241|1241|17*73|2|
| (2,1) |656|41|41|2|
| (3,1) |3321|41|41|2|
| (4,1) |52496|3281|17*193|2|
| (5,1) |356921|356921|241*1481|2|
| (7,1) |5631641|5631641|17*257*1289|between2 and4|
| (1,2) |330881|330881|409*809|between2 and4|
| (3,2) |265761|3281|17*193|2|

For the41 specialization the two points are exactly

    P_minus=(18081/400,1023729/8000),
    P_plus=(1025/16,25215/64).

The first reproduces the earlier covering control; both have the different Kummer classes (5). The cases with upper bound4 are deliberately retained: two formulas do not prove exact rank2 when the independently computed upper bound is larger. No new analytic-order certificate is evaluated in H10, even for members with exact algebraic rank2. Earlier analytic evidence for41 remains a separate dependency.

### 7. Executed next check: why prime coverage is still arithmetic

The polynomial factors as D=F_minus*F_plus, where

    F_e=a^4+4e a^3b+8a^2b^2+24e ab^3+36b^4
       =(a^2+2e ab)^2+4b^2(a+3e b)^2.

Both factors are positive for nonzero primitive a,b. Set c=2 if2 divides a, otherwise1, and additionally multiply c by3 if3 divides a. Then

    gcd(F_minus,F_plus)=c^2.                               (6)

Proof: a common prime q>3 would divide their difference8ab(a^2+6b^2). It divides neither a nor b; hence a^2=-6b^2 modq. Substitution into the common even part gives24b^4=0 modq, impossible. If a is even, both factors have exact2-adic valuation2; if a is odd, both are odd. If3 divides a, both have exact3-adic valuation2; otherwise neither is divisible by3. The latter statements follow by substituting a=2k or3k and using primitiveness. This proves (6).

Thus G_minus=F_minus/c^2 and G_plus=F_plus/c^2 are coprime positive integers. Their squarefree kernels are coprime and multiply to n. For n to be prime, one G_e must be a square, and the other must have prime squarefree kernel. Equivalently the first necessary condition requires a rational point on

    Y^2=T^4-4T^3+8T^2-24T+36,

or its T -> -T counterpart. This quartic has discriminant2^16*3^2, so its smooth completion is genus one. The point (0,6) makes the auxiliary curve soluble, but does not establish infinitely many suitable prime kernels or representation of an arbitrary target prime. This is a precise remaining arithmetic filter, not a solved coverage claim.

### 8. Evidence, sources, and limits

The complete source record is `sources/REGISTER.md`. [Z] is Shenxing Zhang, arXiv:2111.11618v1, Section2.1, printed pages3-4 and equation(2.8); it recalls Monsky's theorem and the fixed full-Kummer conventions. We authenticated and applied that recalled theorem, not independently re-proved the original Monsky appendix. [RS] is Rubin–Silverberg, arXiv:math/0010056v3, Corollary3.3; [HH] is Halbeisen–Hungerbuhler, arXiv:1809.02037v2, contextual evidence that rank-two congruent-number families are established mathematics. Neither [RS] nor [HH] is substituted for the displayed all-parameter independence proof. Our elementary infinity and square-area arguments are written out rather than imported from search snippets.

TypeScript uses198 explicit assertions on the eight registered parameter pairs, sixteen points, a shared Kummer matrix, and boundary checks. Python/SymPy independently recomputes exact fractions, factorization, matrices and symbolic identities; 213 assertions passed. Wolfram separately evaluates the polynomial and point certificates; both returned calls included a global-symbol warning, which is preserved together with their matching results. These are implementation cross-checks, not multiple independent proofs of the universal theorem. In particular the infinity proof is not certified by testing two lifting examples.

All18 previously existing local file hashes remain checked against `inputs/preserved-files.json`; old conclusions and failed routes are not overwritten. Commands, versions, raw local checker outputs and remote receipts are preserved in `results/`. No new payment, publication, external contact, background task, manuscript submission or independent expert verification occurred.

**Next mathematical target:** exploit the explicit prime-coverage filter or find another persistence-sensitive construction for the originally given curve, rather than confuse an infinite selected subfamily with every zero-coefficient prime. H10 does not establish an all-prime existence theorem, the analytic order for its infinite family, an all-rank/non-CM theorem, or a complete BSD candidate.
