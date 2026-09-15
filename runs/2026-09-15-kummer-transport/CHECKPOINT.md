# We have not solved the Birch–Swinnerton-Dyer problem yet.

## H12: squareclass-changing Kummer transport

Continue H11 at 2ab68433f9f2df049e3200f6c7667c90f088a56a in the private BSD repository and /mnt/data/04-birch-swinnerton-dyer. All 23 preexisting local files were hash-checked unchanged. The expanded derivation, source register, exact transcripts and preservation receipts are in the local conversation package BSD_H12_kummer_transport_2026-09-15.zip; that archive is not asserted mirrored remotely. This compact record and the executable checkers preserve the core argument. Evidence is source-dependent self-review, not expert or formal verification; no novelty claim.

**Result.** A rational map of generic degree9 on S:W^2=F_+(x)F_-(y), where F_e(t)=t^4+6e*t^2+1, changes the common squareclass in an exactly verified137 example. It produces two independent points on E_N:Y^2=X^3-N^2X, where

    N=174019544752618399630591052177
     =17*137*16273*19642387489*233758085129.

This is a composite output with rank at least2, not exact rank, analytic order, prime coverage or BSD.

### 1. Restricted transport and the correct involution

The smooth quartic C_e:r^2=F_e(t), with origin(0,1), is isomorphic to E0:v^2=u^3-u by

    u=(r+1+e*t^2)/(2*t^2), v=(r+1+3e*t^2)/(2*t^3),
    t=(u+e)/v, r=(2u-e)*t^2-1.

The omitted points extend as follows: (0,1)->O, (0,-1)->T_e=(-e,0), and infinity with r/t^2->eta maps to ((eta+e)/2,0). The deck map r->-r becomes P->T_e-P, not plain negation. Its affine coordinates are u->-e+2/(u+e), v->2v/(u+e)^2.

E0(Q)=E0[2](Q): elementary two-isogeny x-squareclass descent on E0 and E0':v^2=u^3+4u gives rational images {1,-1} and {1,2}. Valuation comparison restricts prime support to divisors of b=-1 or4; real positivity excludes negative classes on E0', and (2,4) realizes2. The standard isogeny rank formula gives rank0. Good reductions at3 and5 have orders4 and8, bounding rational torsion to the four visible two-torsion points. End_Q(E0)=Z: the action on a rational differential is rational and, by complex uniformization, preserves a lattice, hence is an algebraic integer; a zero derivative endomorphism is zero in characteristic0.

Let B=E0^2, T=(T_+,T_-), iota(P)=T-P. S is birational to B/iota. A dominant Q-rational map of B is affine h(P)=MP+R by Milne I.3.7; here M is an integer matrix and R is rational two-torsion. Descent through this quotient requires h*iota=iota*h (the alternative h*iota=h contradicts dominance), hence MT+2R=T. Independence of T_+,T_- gives exactly M=I mod2. Conversely this condition suffices. The degree is det(M)^2. This classification concerns ONLY maps lifting to this specified product over Q.

If a surface point has common squareclass n, its lift over Q(sqrt(n)) has conjugation iota. A commuting map retains that law, so its nonbranch output has the same n. For n=1 the lift stays rational. Moreover the H8 rational point

    Q_e=(n*(t^2+e)^2/(4*t^2), n^2*u_e*(t^4-1)/(8*t^3)),
    F_e(t)=n*u_e^2,

becomes -[2]P under (X,Y)->(X/n,Y/(n*sqrt(n))). Thus h replaces the rational pair by M times that pair; no new free span or mod2 class is created.

As an exact control, tripling uses t'=A_e/D_e and u_e'=u_e*H_e/D_e^2, where

    A_e=t*(t^8-6t^4-24e*t^2-3),
    D_e=3t^8+24e*t^6+6t^4-1,
    H_e=t^16+24e*t^14+28t^12+168e*t^10+582t^8
        +168e*t^6+28t^4+24e*t^2+1.

Polynomial identities give F_e(A_e/D_e)=F_e(t)*(H_e/D_e^2)^2, derivative(A_e/D_e)=3H_e/D_e^2, and gcd(A_e,D_e)=1. The origin is fixed, so this is multiplication by3. It varies witness ratios but not n.

### 2. Another fibration escapes the invariant

Set U=x^2+3,V=y^2-3. The identity

    (UV-8)^2-W^2=8(U-V)^2

gives, on U!=V,

    a=(UV-8)/(U-V), b=W/(U-V), a^2-b^2=8.

This base conic is rational: a=(tau^2+8)/(2tau), b=(tau^2-8)/(2tau). Put C=a+3,K=6a+17. Since (U+a)(V-a)=-b^2, the fiber is

    z^2=f(x)=(x^2+C)*(C*x^2+K), z=y*(x^2+C),
    y=z/(x^2+C), W=b*(x^2-y^2+6).

Its polynomial discriminant is16*C^2*K*(C^2-K)^4, and C^2-K=b^2. Fibers with C*K*b nonzero are smooth genus1. All displayed denominators and singular fibers are excluded.

At a point (x,z) with z nonzero, define

    h1=f'(x)/(2z), h2=(f''(x)/2-h1^2)/(2z),
    r3=f'''(x)/6-2h1*h2, r4=C-h2^2,
    x'=x-r3/r4, z'=z+h1*(x'-x)+h2*(x'-x)^2,
    y'=z'/(x'^2+C), W'=b*(x'^2-y'^2+6).

Require r4!=0 and x'^2+C!=0. The polynomial identity

    f(x+d)-(z+h1*d+h2*d^2)^2
      =f(x)-z^2+r3*d^3+r4*d^4

proves the new surface point exactly. On the smooth projective fiber, the osculating function has divisor3P+P'-2infinity_+-2infinity_-. The nonzero r4 prevents pole cancellation. The genus1 divisor law therefore describes P' as a fixed translation minus[3]P, so the map has generic degree9 in characteristic0. The base(a,b) is fixed, giving a dominant degree9 rational surface self-map, not a rational parametrization.

### 3. Exact arithmetic escape and independence

The inherited137 seed is

    x=1/14, y=37/14, u_+=17/196, u_-=47/196, W=137*u_+*u_-.

Its fiber has a=-152681/37632,b=-109463/37632,C=-39785/37632,K=-46057/6272. The map gives

    x'=-16890371/79256324, y'=210069683/77723044,
    F_+(x')/F_+(x)=1270215655128601457157598921
                    /1027125612178388895573957136.

The ratio has valuation1 at17, so it is NOT a rational square. This proves a change of n without factoring the ratio. Consequently this new map is outside the restricted product-liftable class, even though its degree is also9.

Full normalization was additionally certified: every factor in N is prime by exhaustive trial division through its exact square root, with the largest root below484000. Two primitive opposite-parity witnesses satisfy

    79256324^4+6*79256324^2*16890371^2+16890371^4=N*17^2,
    210069683^4-6*210069683^2*77723044^2+77723044^4=N*47^2.

For A^4+6e*A^2*B^2+B^4=N*c^2, put u=N*c,v=A^2-e*B^2,w=A^2+e*B^2,z=2AB. Then (X,Y)=(N*w^2/z^2,N*u*v*w/z^3) lies on E_N. Its Kummer class in ordering(X-N,X+N,X) is (1,N,N) for e=-1 and (N,1,N) for e=1, with exact square factors checked.

Adjoin torsion classes(2,2N,N),(-N,N,-1). With basis(-1,2,N) in each coordinate, the raw minor at columns0,1,2,5 is

    0 1 0 1
    1 0 1 1
    0 0 0 1
    0 0 1 0

and has determinant1. The Kummer kernel is2E_N(Q). Applying the resulting dimension bound to the subgroup generated by the four points proves that the two displayed free directions are independent. No saturated basis or exact-rank claim follows.

### 4. Sources, verification and next objective

Milne, Abelian Varieties v2.00, cover March16/revision-list March17,2008: https://www.jmilne.org/math/CourseNotes/AV.pdf , I.3.2 and I.3.7 (physical pages22/24, latter printed19); I.7.2 supplies multiplication degree. Fisher, arXiv:1509.03234v1, https://arxiv.org/pdf/1509.03234v1 , Sections2/5 supplies the established isogeny rank and connecting-map conventions. The surface identities, quotient compatibility and degree9 application are derived here, not imported as source statements.

Harpaz, Second descent and rational points on Kummer varieties, https://arxiv.org/pdf/1703.04992 : retrieved header v1 March15,2017, internal date November13,2018. Definition2.3/Theorem2.8 require odd multiplicative places and retain a Tate-Shafarevich hypothesis in their Hasse-principle consequence. The displayed E0 factors have no odd bad places (discriminant64), so that application does not give unconditional prescribed-prime existence. This is an applicability boundary, not a universal rejection of Kummer methods.

Accepted execution:53 TypeScript and56 Python/SymPy assertions; npm run lint, npm run typecheck, npm test, npm run test:symbolic all passed. Lint is TypeScript unused/unreachable diagnostics, not ESLint. Node22.16.0,TypeScript5.8.3,Python3.13.5,SymPy1.14.0,Wolfram15.0.1. The Python output uses polynomial division to find the fourth intersection, independently of the TypeScript derivative formula. Primary integer output replayed byte-identically. Wolfram checked generic identities and the exact137 output, with an invalid final Table iterator corrected by a focused Map call. A third call derived the raw minor. The initial isolated minor implicitly used a row operation; the accepted checkers build it directly from squareclasses. All corrections are retained in the local evidence package.

Next objective: characterize the squareclass image of this map, possibly combined with squareclass-preserving product transport, for prescribed primes while preserving both rational lifts. A composite output and surface dominance do not prove that every desired prime is reached. No analytic-order theorem, general rational-point existence, Sha-finiteness theorem or complete BSD candidate was obtained. No publication, external contact, spending, or background process occurred.
