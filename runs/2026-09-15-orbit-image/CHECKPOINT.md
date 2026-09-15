# We have not solved the Birch–Swinnerton-Dyer problem yet.

## H13: infinite transport orbit, genus-five fibers and a prescribed-prime obstruction

Continue ac5bb862d273db89512db7173bdd9384536324df in the private BSD repository, branch research/h2-endpoint-20260914. The full derivation, self-review, source audit and genuine outputs are in BSD_H13_orbit_image_2026-09-15.zip under /mnt/data/04-birch-swinnerton-dyer. That archive is not claimed mirrored remotely. No novelty, expert/formal verification, exact-rank or analytic-order claim is made.

**Result:** H12's degree-nine map has an infinite rational orbit from its137 seed. Its common squareclasses occupy an infinite set, with every individual class occurring only finitely often. All produce two independent rational points on the corresponding E_n. Nevertheless this fixed orbit can never reach257 or313. Changing the auxiliary fiber removes this particular local obstruction, without proving global reachability or BSD.

### 1. The map and an exact nontorsion certificate

Write g(x)=x^4+6x^2+1. The simultaneous surface is W^2=g(x)(y^4-6y^2+1). H12's base coordinates satisfy a^2-b^2=8; put C=a+3, K=6C-1, so C^2-K=b^2. Its smooth genus-one fiber is

    F: z^2=f(x)=(x^2+C)(Cx^2+K),
    y=z/(x^2+C), W=b(x^2-y^2+6).

The137 seed and first image are

    (x0,y0)=(1/14,37/14),
    (x1,y1)=(-16890371/79256324,210069683/77723044),
    C=-39785/37632, K=-46057/6272, b=-109463/37632,
    z_i=y_i(x_i^2+C).

The discriminant16C^2K(C^2-K)^4 is nonzero. The Python checker reconstructs the image by dividing the osculating residual by (x-x0)^3. For a general point, H12's formulas are

    h1=f'(x)/(2z), h2=(f''(x)/2-h1^2)/(2z),
    r3=f'''(x)/6-2h1h2, r4=C-h2^2,
    x'=x-r3/r4, z'=z+h1(x'-x)+h2(x'-x)^2.

The osculating divisor is 3P+Phi(P)-2infinity_plus-2infinity_minus. Use the actual rational P0 as origin, not an infinite point. If D=P1-P0, then

    Phi(P)-P0=D-3(P-P0).

The rational divisor at infinity suffices, even though its two points are not individually rational. Thus Phi extends to a translated [-3] on the smooth projective fiber, etale of degree9 in characteristic0 [M].

The degree-two map rho(x,z)=(Cx^2,Cxz) lands on

    A: V^2=U(U+C^2)(U+K).

Its generic pair is (x,z),(-x,-z). After translating R0=rho(P0) to zero, it is a homomorphism [M]. Set Q=rho(P1)-rho(P0). Independently computed exact rational coordinates are

    Q_U=64198947010139677695723481/661218006713885376537600,
    Q_V=-3979144651441292118283877187565950631693/
          4301371914284617625188551895252992000.

The model has good reduction at13,19,31, since its coefficients are integral and its discriminant16C^4K^2(C^2-K)^2 is nonzero there. Complete finite counts give respectively16,24,40 points. Good reduction injects prime-to-characteristic rational torsion [S]. Using the other prime handles13- and19-primary torsion; all remaining primary parts inject at both. Hence rational torsion has order dividing gcd(16,24)=8.

But Q mod31=(28,5), whose multiples are

    (28,5),(4,3),(4,28),(28,26),O.

It has order5, and [8]Q mod31=(4,28) is nonzero. Thus Q and D are nontorsion. For P_j=Phi^j(P0),

    rho(P_j)=R0+((1-(-3)^j)/4)Q.

The integers (1-(-3)^j)/4 are distinct, so the orbit is infinite. This is a proof, not extrapolation from the finite scalar prefix checked by the programs.

### 2. Fixed squareclass and infinitely many distinct outputs

For n in Q*, take the smooth projective normalization D_n of

    z^2=f(x), n r^2=g(x).

The identities

    disc(g)=2^14,
    Res_x(f,g)=(C^2-6C+1)^4=(C^2-K)^4=b^8 != 0

show that each of the four simple roots of g lifts to two unramified points on F. Thus g has eight simple geometric zeros on F. At its two infinite points it has poles of order4. Adjoining sqrt(g/n) gives a geometrically connected double cover with exactly eight branch points; the odd zeros exclude a geometric square. Riemann-Hurwitz [RH] gives genus5.

Faltings finiteness, using the primary proof [B] and erratum, implies D_n(Q) is finite for each fixed n. Therefore a fixed squareclass occurs at only finitely many distinct points on the orbit. The infinite orbit occupies infinitely many squareclasses. No effective bound or varying-n uniformity is inferred. This is a formal application of established finiteness, not a claimed new finiteness theorem.

For a rational x=A/B in lowest terms, an odd prime dividing the squarefree kernel of G_+=A^4+6A^2B^2+B^4 cannot divide AB. From

    G_+=(A^2+B^2)^2+4A^2B^2=(A^2-B^2)^2+8A^2B^2

both -1 and -2 are squares modulo that prime, forcing it to be1 mod8. If A,B are odd, G_+=8 mod16, with even squarefree kernel; the minus quartic is instead12 mod16 and always has odd kernel. The shared squareclass is consequently odd and supported only on primes1 mod8. Both witnesses have opposite parity, since an odd-odd minus witness after division by4 would be3 mod4 rather than1.

For each nondegenerate witness t^4+6e t^2+1=n u_e^2, the rational point on E_n is

    (n(t^2+e)^2/(4t^2), n^2 u_e(t^4-1)/(8t^3)).

The two Kummer triples are (1,n,n) and (n,1,n). Together with torsion triples(2,2n,n),(-n,n,-1), the raw minor in the basis(-1,2,n) is

    0 1 0 1
    1 0 1 1
    0 0 0 1
    0 0 1 0,

of determinant1. For odd positive squarefree n>1 these basis classes are independent. The Kummer kernel2E_n(Q), applied to the subgroup generated by the four points, proves independence of the two free points. Rank is at least2, not necessarily exactly2.

### 3. Full Q_13 obstruction for this fixed fiber

Modulo13, C=6,K=9. If x is nonintegral, (z/x^2)^2 reduces to6, a nonsquare. This also excludes infinite points. For integral x the complete admissible residue list is

    x:    1,3,4,6,7,9,10,12;
    g(x): 8,6,2,5,5,2, 6, 8.

All g-values are nonsquare units. Every rational point on this fiber therefore has common squarefree n with13 not dividing n and Legendre symbol(n/13)=-1. In particular n=1,257,313 are impossible:257=10 mod13 and313=1 mod13 are squares.

The nonintegral and infinite charts are part of this obstruction. It is not a bounded global search. The13-adic square obstruction also excludes x^2+C=0 since -C=7 mod13 is nonsquare. There is no rational z=0: its alternative root x^2=-K/C is negative over R. Because C<0, r4=C-h2^2 is never zero on rational input. Thus Phi is evaluable at every rational point on this fiber. Trivial or degenerate surface witnesses would have n=1 or2, or negative minus quartic; the parity and local conditions exclude them. All orbit terms give valid independent point certificates.

This excludes257 and313 from the fixed orbit even though H8 already has separate rational-rank certificates for both. It is a limitation of the route, not a BSD counterexample.

### 4. A checked change of fiber and the exact preimage genus

Apply the squareclass-preserving minus-quartic tripling to y0 while fixing x0:

    y3=y0(y0^8-6y0^4+24y0^2-3)/(3y0^8-24y0^6+6y0^4-1).

The full square identity is checked, so the squareclass remains137, but

    C3=-61708285879386802434260270825/
          2683974129278159984546892312288,
    C3=1 mod13, K3=5 mod13.

On z^2=(x^2+C3)(C3x^2+K3), n r^2=g(x), the points modulo13 are (5,0,6) for n257 and (5,0,3) for n313. The x,r Jacobian determinant is -f'(5)*2nr, nonzero because f'(5)=1 mod13. Hensel therefore gives actual Q_13 points for both targets on the changed fiber. Varying z slightly also supplies points off the return-map boundary. No global point or orbit-reachability conclusion follows.

Thus the local exclusion is not established for arbitrary fiber-changing compositions. That distinction is load-bearing.

For a fixed n and j, pulling D_n back along Phi^j pulls its eight branch points back to8*9^j distinct points, because Phi^j is etale of degree9^j. The resulting connected quadratic cover has genus

    1+4*9^j, including genus37 at j=1.

This is an exact formulation of the prescribed-output problem, not an existence theorem or effective solver.

### 5. Sources, verification and next implication

[B] Bombieri, The Mordell conjecture revisited, Annali SNS Pisa17(1990),615-640, https://www.numdam.org/item/ASNSP_1990_4_17_4_615_0.pdf ; erratum18(1991),473, https://www.numdam.org/item/ASNSP_1991_4_18_3_473_0.pdf . Printed615/616 were read and screenshotted. Erratum parsed; its screenshot failed. No effective heights or uniformity imported. If D_n has a rational point it supplies a degree-one divisor; otherwise finiteness is immediate.
[M] Milne, Abelian Varieties v2.00(2008), https://www.jmilne.org/math/CourseNotes/AV.pdf , I.3.2, I.3.7 and I.7.2. Morphism-plus-translation and multiplication degree/etaleness are the inputs; the particular divisor and quotient formulas are proved here.
[RH] Stacks Project,53.12, https://stacks.math.columbia.edu/tag/0C1B . Characteristic0 Riemann-Hurwitz applied after the complete branch and geometric-integrality check.
[S] Silverman, Wyoming2006 author exposition, https://www.math.brown.edu/~jhs/Presentations/WyomingEllipticCurve.pdf , PDF72/printed64: prime-to-characteristic torsion injects on good reduction.

44 TypeScript and56 Python assertions passed. Commands: npm run lint; npm run typecheck; npm test; npm run test:symbolic. Lint is TypeScript strict unused/unreachable checking. Versions: Node22.16.0,TypeScript5.8.3,Python3.13.5,SymPy1.14.0,Wolfram15.0.1. TypeScript enumerates all affine points at13,19,31; Python independently counts by quadratic characters and reconstructs the exact rational difference and osculating point. All13 local x residues and one changed-fiber control are checked. The primary integer output replays byte-identically. All25 preexisting local files remained unchanged.

Wolfram agreed on the finite counts, order-five sequence, generic resultant and local residues. Its first final Table iterator failed; a corrected call returned both target residuals zero but retained a global-symbol diagnostic. Both are preserved. No warning-free Wolfram result, expert review or formal proof is claimed.

Next question: can fiber-changing transports ensure rational solubility for a prescribed prime without assuming the wanted points, Sha finiteness or an unproved height bound? Infinite output and local solubility do not supply this implication. General BSD and new analytic comparisons remain unresolved. No spending, publication, external contact or background process occurred.
