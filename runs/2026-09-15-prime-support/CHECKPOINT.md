# We have not solved the Birch–Swinnerton-Dyer problem yet.

## H15: exact prime-support transfer and infinitely many outputs without137

Parent b90104c61825ce0ab4f7c767b30d4f6c3bea11f9, private branch research/h2-endpoint-20260914. This compact checkpoint and the executable checkers preserve the core proof. The expanded source audit, all274 local rows, preservation hashes and discovery records are in the conversation artifact BSD_H15_prime_support_2026-09-15.zip under /mnt/data/04-birch-swinnerton-dyer; that archive is not claimed mirrored here. The29 preexisting local files were verified unchanged. Evidence is source-dependent self-review, not expert/formal verification or a novelty claim.

**Result.** Apply H^m to the137 seed, then Phi, with H(P,Q)=(P-2Q,Q) as in H14. An exact degree24 polynomial controls the output squareclass. We certify removal of137 in128 classes modulo274 and retention in136; ten classes remain unresolved at the chosen precision. The progression m=1 modulo274 gives infinitely many distinct positive squarefree output parameters, none divisible by137, with rank E_n(Q)>=2. Infinitude uses the established finiteness theorem for genus at least two after the genus25 calculation below. The explicit first output is composite, not257. No prescribed-prime or general BSD result follows.

### 1. Rational slice and non-torsion input

Write F_e(t)=t^4+6e*t^2+1 and S:W^2=F_+(x)F_-(y). The seed is

    x0=1/14, y0=37/14, W0=137*17*47/196^2.

Over K=Q(sqrt137), the lifts r_+=17*sqrt137/196 and r_-=47*sqrt137/196 identify with P,Q on E0:v^2=u^3-u by

    u=(r+1+e*t^2)/(2t^2), v=(r+1+3e*t^2)/(2t^3),
    t=(u+e)/v, r=(2u-e)*t^2-1.

The deck map is P->T_e-P with T_e=(-e,0). Hence H^m(P,Q)=(P-2mQ,Q) commutes with simultaneous deck conjugation. On the valid chart it yields rational x_m,y0,W_m and F_+(x_m)=137*c_m^2. It is not a putative rational point inferred from local data.

Q is non-torsion independently of BSD. The checker verifies that -[2]Q, under (u,v)->(137u,137sqrt137*v), is the rational E137 point

    X=137*(t^2-1)^2/(4t^2),
    Y=137^2*(47/196)*(t^4-1)/(8t^3), t=37/14,

with Y nonzero. Direct counts give #E137(F3)=#E137(F5)=4. Good-reduction prime-to-characteristic torsion injectivity, using each prime to handle the other's primary part, bounds rational torsion by4. The visible two-torsion exhausts it. Thus Q has infinite order, the points P-2mQ are distinct, and any infinite progression in m yields infinitely many distinct x_m, since each quartic x has at most two preimages. Zeros/poles of the finitely many rational chart functions exclude only finitely many inputs; m=1 verifies this open set is nonempty.

### 2. Exact global transfer law

For y=37/14, substitute C=(x^2*y^2+1)/(x^2-y^2+6), K=6C-1 into H14's cancelled Phi. Its output x-coordinate is R(x)=A/B, where

    A=-x*(52591504*x^6-727141576*x^4-6145143927*x^2-1102006668),
    B=157774512*x^6+519995448*x^4-2460543401*x^2-367335556.

A,B are coprime of degrees7,6. Define J by the exact integral polynomial identity

    A^4+6A^2 B^2+B^4=F_+(x)*J(x).

The left side is squarefree of degree28, J is squarefree of degree24 and coprime to F_+; it is also coprime to B. Exact SymPy polynomial arithmetic checks all identities; a separately written F11 polynomial Euclidean algorithm checks squarefreeness/coprimality with the degrees retained. This is not a test of F11 roots. Full coefficients are generated in results/global-certificate.json.

For F_+(x)=137*c^2,

    F_+(R(x))=137*c^2*J(x)/B(x)^4,
    [n_out]=[137*J(x)] in Q*/Q*^2.

At a valid slice input, a prescribed squareclass n occurs exactly when 137J(x)/n is a rational square. The identity itself does not prove such an input exists in the chosen orbit.

### 3. Local retention under explicit hypotheses

Let l be odd, let x,y be integral, and suppose v_l(F_+(x))=v_l(F_-(y))=1 and gap=x^2-y^2+6 is a unit. Set

    C=(x^2*y^2+1)/gap, K=6C-1,
    epsilon=x^2+C=F_+(x)/gap,
    beta=W/gap, theta=beta/epsilon=W/F_+(x).

Then C,x,y,theta are units; v_l(epsilon)=1; C^2-K=beta^2; x^2=-C+epsilon; K=C^2-theta^2*epsilon^2. In the cancelled Phi expression x'=x*N/D, substitution gives

    D=-epsilon^3*(4C^2+C*theta^4*epsilon-6C*theta^2*epsilon
                   -3C*epsilon+4theta^2*epsilon^2),
    N= epsilon^3*(4C^2-C*theta^4*epsilon-6C*theta^2*epsilon
                   -C*epsilon+4theta^4*epsilon^2).

These are exact polynomial identities. Cancelling epsilon^3 gives a unit denominator and

    x'/x=-1-(1-theta^4)*epsilon/(2C)+O(epsilon^2),
    x'^2+C=theta^4*epsilon+O(epsilon^2).

Since C^2-6C+1=theta^2*epsilon^2 and the polynomial C^2-6C+1 has discriminant32, its derivative6-2C is a unit at every such odd l. Expanding F_+(x') yields F_+(x')/F_+(x)=theta^4 modulo l. Thus v_l(F_+(x'))=1: l is retained. This lemma does not cover a gap divisible by l, and is not an unconditional prime-retention invariant.

### 4. All-exponent ramified local certificate at137

Use R=O_(Q137(pi))/(pi^3), pi^2=137. Each element is uniquely a+b*pi, a modulo137^2, b modulo137, with multiplication

    (a,b)*(c,d)=(ac+137bd modulo137^2,ad+bc modulo137).

Invert by the norm a^2-137b^2; nonunits throw an error. Reduce the actual P,Q and iterate P-2mQ for ALL m=0,...,273. Every addition and quartic-conversion denominator is a unit. The FULL elliptic state returns to P at274. This proves the finite period applies to every m>=0 by induction and compatibility of reduction, rather than by extrapolating a prefix.

Retain x,y modulo137^2 and the coefficient of pi in r_+. For unit gap and exact valuation1 of F_+, use Section3. If gap has exact valuation1, divide both its integer residue and that of x^2*y^2+1 by137, obtaining C modulo137. Certify removal only when the cancelled Phi x denominator, return denominator x'^2+C and F_+(x') are units. Residues zero modulo137^2 are not assigned an exact valuation.

All274 outcomes:

    136 retained classes, all even except158;
    128 removed classes, all odd except the nine odd exceptions below;
     10 unresolved classes at this precision:
    21,59,89,111,115,158,201,205,227,257 modulo274.

The full local table is regenerated by verify.ts. At m=1, C=115, x'=82 and F_+(x')=51 modulo137, all relevant denominators units. Among the128 removals, the output unit is a square in86 classes and a nonsquare in42. Both257 and313 are squares modulo137; this character check does not exclude them and does not establish global reachability.

Independent Python reconstruction uses the exactly verified pullback du/(2v)=-dt/r. Put xi_m=49 for even m and123 for odd m, bP=17/196 and bQ=47/196 modulo137. Translation of tangent parameters gives

    b_m=F_+'(xi_m)*(bP/F_+'(49)-2m*bQ/F_-'(32)) modulo137.

Reconstruct x=xi_m+137u from F_+(x)=137*b_m^2 modulo137^2. This agrees with all274 ring-recurrence rows. A first failing checker reduced y0 only modulo137 before dividing gap by137; retaining y0 modulo137^2 corrected the discrepancy C=3 versus115 at m=1. This checker error was caught before accepting results; no earlier research file or accepted mathematical conclusion relied on it. Ten precision exceptions remain explicitly unresolved.

### 5. Exact short example and independent points

At m=1, H gives (x,y,W)=(6127/1862,37/14,25815863383/679540624). Phi then gives

    x'=43527762774033482635941503/35975915953349079904919842,
    y'=473803727686237153030517/190678075129432137281146.

The exact W', all three surface residuals and the specialized-map comparison are regenerated by Python. Write x'=a/b in lowest terms and G=a^4+6a^2*b^2+b^4. Its104-digit value is in results/global-certificate.json. Exact divisions give

    v137(G)=0, v17(G)=5, v257(G)=1, v281(G)=1, v7369(G)=1.

All four latter divisors are prime by exhaustive trial division through their square roots. The squarefree kernel n is therefore composite. A factor257 is NOT the prime parameter257. No complete factorization or analytic order is claimed.

Both quartic witnesses on parameterG are rational: u_+=1/b^2, u_-=W'*b^2/G. For F_e(t)=G*u_e^2 set

    X_e=G*(t^2+e)^2/(4t^2),
    Y_e=G^2*u_e*(t^4-1)/(8t^3).

They lie on E_G:Y^2=X^3-G^2X and have Kummer classes (G,1,G) and (1,G,G) in ordering(X-G,X+G,X). Add the visible torsion classes (2,2G,G),(-G,G,-1). The raw minor in coordinatewise basis(-1,2,G) is

    0 1 0 1
    1 0 1 1
    0 0 0 1
    0 0 1 0,

with determinant1. Since G is positive odd nonsquare and the Kummer kernel is2E_G(Q), these two free directions are independent. E_G is Q-isomorphic to E_n after removing G's square factor. The conclusion is rank>=2, not exact rank or saturation.

### 6. Infinitely many distinct outputs with137 removed

For fixed positive squareclass n, every valid input producing it yields a rational point on the smooth projective normalization D_n of

    137*s^2=F_+(x), n*z^2=137*J(x).

Over an algebraic closure, the first cover has four branch points and genus1. The24 distinct roots of J are disjoint from those four; each has two preimages, so the second double cover is branched at48 simple points. Its poles at infinity have even order24, so there is no extra branch there. Odd valuations at the48 points prove geometric connectedness. Riemann-Hurwitz gives

    2g(D_n)-2=2*(2*1-2)+48=48, hence g(D_n)=25.

The established finiteness theorem for rational points on curves of genus at least two therefore makes D_n(Q) finite for each n. This theorem is applied to the connected smooth projective normalization, not a singular affine presentation. Constants137,n do not affect the geometric branch count.

The progression m=1 modulo274 has infinitely many distinct inputs by Section1 and has137 removed by Section4. The finitely many chart exceptions may be discarded. Since each fixed n has only finitely many inputs, infinitely many distinct n occur, with137 dividing none of them.

Every nonbranch rational surface point has an odd positive common squareclass supported on primes1 modulo8. Indeed F_+ is positive, and for coprime integers a,b,

    F_+(a,b)=(a^2+b^2)^2+(2ab)^2=(a^2+3b^2)^2-8b^4.

An odd prime dividing it divides neither a nor b, so both -1 and2 are quadratic residues. If a,b are both odd the plus form has v2=3; a primitive minus form has v2=0 or2. Equality of squareclasses excludes the even case. Discard n=1 and the finitely many degenerate output charts. The Kummer argument of Section5 proves rank E_n(Q)>=2 for the remaining infinite set. This does not assert prime parameters; the displayed first example is composite.

### 7. External inputs, audit, verification and next obligation

Bombieri, The Mordell Conjecture Revisited, Annali SNS Pisa17(1990),615-640, theorem printed615, with1991 erratum at18,473: https://www.numdam.org/item/ASNSP_1990_4_17_4_615_0.pdf and https://www.numdam.org/item/ASNSP_1991_4_18_3_473_0.pdf . Printed615-616 were read and screenshotted; the erratum was read in full parsed text, but its screenshot failed. Its enlarged exceptional set and degree-one-divisor correction do not remove finiteness. A rational point on D_n supplies that divisor; if absent, finiteness is immediate. Only pointwise finiteness is used, not an effective or uniform bound.

Stacks Project, Section53.12, tag0C1B: https://stacks.math.columbia.edu/tag/0C1B , characteristic-zero Riemann-Hurwitz and Lemmas53.12.2/4. Our covers are separable and tame; the48 branches and genus25 are derived above.

Silverman, Wyoming2006 author exposition, addition formulas PDF25-29 and torsion injectivity PDF72/printed64: https://www.math.brown.edu/~jhs/Presentations/WyomingEllipticCurve.pdf . The torsion page was screenshotted; actual finite-field orders are recomputed. H14 supplies the quartic/shear/Phi conventions; the Kummer kernel and elliptic group law are established inputs. Their foundational proofs were not formally reconstructed.

23 grouped TypeScript and41 Python assertions passed. Reproduction, in this directory: npm run lint; npm run typecheck; npm test; node dist/verify.js > results/local-cycle.json; npm run test:symbolic. Lint is TypeScript unused/unreachable diagnostics, not ESLint. Observed Node22.16.0,TypeScript5.8.3,Python3.13.5,SymPy1.14.0. Three generated JSON certificates replayed byte-identically. Wolfram15.0.1 returned the136/128/10 table, ten exceptions, branch degrees, zero transfer/local residuals and exact prime valuations, but emitted undefined-symbol warnings. It did not check the final86/42 character count, full ramified-ring recurrence or all rational coordinates. Warnings and exact scope are preserved.

Self-review checked composition order; conjugation; unit denominators; full-state closure; precision loss upon division; explicit unresolved classes; simple branching at infinity; non-torsion input independent of BSD; prime factor versus prime parameter; and rank lower bound versus exact rank. No step assumes Sha finiteness, BSD or prime distribution. This is not independent expert or formal verification.

Next target: control J(x_m) sufficiently to obtain a prescribed PRIME squareclass, equivalently a rational point on this genus25 cover lying in the chosen cyclic input orbit, or use a different slice. Removing one factor or admitting a target locally does not prove its global existence. No classification for the full enlarged semigroup, uniform prescribed-prime existence, all-rank/non-CM analytic comparison or complete BSD candidate has been obtained. No publication, outside contact, spending or background process occurred.
