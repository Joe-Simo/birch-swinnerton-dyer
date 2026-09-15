# We have not solved the Birch–Swinnerton-Dyer problem yet.

## H14: mixed-transport obstruction and shear escape

Parent: 9c3de10b18c295b9678714855a01b3a252151ec0 on private branch research/h2-endpoint-20260914. Previous run files are unchanged. The expanded derivation and actual rational coordinates are in the conversation artifact BSD_H14_mixed_transport_2026-09-15.zip, under /mnt/data/04-birch-swinnerton-dyer. This remote checkpoint and its executable checkers preserve the core proof; the archive is not claimed mirrored. Self-reviewed, not expert/formal verification or a novelty claim.

**Result.** All words in separate quartic triplings X,Y and H12's osculating map Phi, starting from the137 seed, exclude squareclasses257 and313. Five elementary symmetries do not remove this obstruction. The new shear H(P,Q)=(P-2Q,Q) DOES remove this particular obstruction: the actual rational word Y,H,Phi changes the quadratic character at13. Its output is composite; neither prescribed prime is claimed reached. No general BSD result follows.

### 1. Fixed conventions and all-word obstruction

Write F_e(t)=t^4+6e*t^2+1 and S:W^2=F_+(x)F_-(y). The rational seed is (1/14,37/14,137*17*47/196^2), reducing to (1,11,3) modulo13. Quartic lifts have r_+=17*sqrt(137)/196 and r_-=47*sqrt(137)/196.

For separate tripling on coordinate t with sign e, put

    A=t*(t^8-6t^4-24e*t^2-3),
    D=3t^8+24e*t^6+6t^4-1,
    H=t^16+24e*t^14+28t^12+168e*t^10+582t^8
      +168e*t^6+28t^4+24e*t^2+1.

Replace t by A/D and W by W*H/D^2. For Phi set gap=x^2-y^2+6, C=(x^2*y^2+1)/gap, K=6C-1, z=y*(x^2+C), f(T)=(T^2+C)*(C*T^2+K). Then

    h1=f'(x)/(2z), h2=(f''(x)/2-h1^2)/(2z),
    r3=f'''(x)/6-2h1*h2, r4=C-h2^2, dx=-r3/r4,
    x'=x+dx, z'=z+h1*dx+h2*dx^2, y'=z'/(x'^2+C),
    W'=W*(x'^2-y'^2+6)/gap.

These are the authenticated H12 maps. The finite assertion below checks every denominator, not just the surface equation.

In F13 define Omega by W^2=F_+(x)F_-(y), both F-values nonsquare units, and exactly one of x^2=1 and y^2=-1. This set has64 elements: each of two coordinate strips has2*8 choices, with two W values per choice. Enumeration of all13^3 triples and an independent two-strip construction agree.

At every point, all eight operations X,Y,Phi, x-inversion with W/x^2, y-inversion with W/y^2, and the three separate sign changes are defined by unit denominators and stay inside Omega. All512 transitions are checked without omissions. Python reconstructs Phi by dividing the quartic-minus-osculating-square by (T-x)^3, independently of the TypeScript derivative quotient. Wolfram verifies the same closure. The X,Y,Phi orbit from the seed closes at exactly32 states.

Consequently every rational word in these operations remains13-adically integral with reduction in Omega: this is induction on word length, using the checked unit denominators. For its positive common squareclass n one has 13 not dividing n and (n/13)=-1. Both257 and313 have character+1 and are excluded for ALL such words, not merely a bounded search. Their separate known rational-point certificates from H8 are unaffected.

### 2. Shear and the necessary cancellation

The quartic r^2=F_e(t) identifies with E0:v^2=u^3-u via

    u=(r+1+e*t^2)/(2t^2), v=(r+1+3e*t^2)/(2t^3),
    t=(u+e)/v, r=(2u-e)*t^2-1.

Its deck involution is P->T_e-P, T_e=(-e,0). Thus simultaneous conjugation on the product is iota(P,Q)=(T_+-P,T_--Q). H(P,Q)=(P-2Q,Q) commutes with iota since 2T_-=0, and has inverse (P+2Q,Q). It descends to a rational surface map and preserves the common squareclass wherever the quartic coordinates are nondegenerate. Closure under separate triplings does not imply closure under this mixing operation.

The successful word encounters C=0 MODULO13, not C=0 over Q. The old osculating chart cannot be reduced there without simplifying. For f=a*x^4+b*x^2+d define N=2f*f''-(f')^2 and

    D0=3a^2*x^8+4a*b*x^6+6a*d*x^4-d^2.

The exact identities r3=-x*(4a*d-b^2)*(a*x^4-d)/f^2 and r4=-(4a*d-b^2)*D0/(4f^3) give

    x'=-x*(a^2*x^8-6a*d*x^4-4b*d*x^2-3d^2)/D0,
    z'/z=H0/D0^2,
    H0=a^4*x^16+4a^3*b*x^14+28a^3*d*x^12+28a^2*b*d*x^10
       +(6a^2*d^2+16a*b^2*d)*x^8+28a*b*d^2*x^6
       +28a*d^3*x^4+4b*d^3*x^2+d^4.

After a=C,b=C^2+K,d=C*K,K=6C-1, cancel common factors C and C^2 respectively. At C=0 these give x'=-1/x^3 and z'/z=-1/x^4, hence y'=-x^4*y. These are specializations of the SAME rational map, proved by symbolic cancellation before reduction, not a guessed replacement formula.

### 3. Exact rational escape and its limitation

Work in Q(sqrt(137)). Apply (P,Q)->(P,3Q)->(P-6Q,3Q), convert back to the quartics, then apply Phi with exact fractions. Each converted t is rational and each r is anti-invariant. The actual rational stages reduce to

    seed: (1,11,3), F_+=8;
    Y:    (1,9,12), F_+=8;
    YH:   (11,9,6), F_+=2;
    YHPhi:(5,12,9), F_+=9.

The last value is a square unit, unlike the previous values. At the YH residue, gap=7, C=0; the cancelled x denominator is4 and output return denominator is12. The simplified chart is therefore valid. The rational input fiber is smooth and the original rational formula also computes the same result. TypeScript separately performs the group law in F13(sqrt(7)); its word agrees with reduction of the Python exact rational output. This is a genuine rational escape, not a merely locally soluble target.

Write the final x=A/B in lowest terms and G=A^4+6A^2*B^2+B^4. A has400 decimal digits and G has1601. Exact divisions certify v17(G)=3, v2473(G)=1, v3329(G)=1; these three primes are verified by trial division. Hence the positive squarefree kernel n is composite, without claiming a full factorization.

Two witnesses for parameter G are u_+=1/B^2 and u_-=W*B^2/G. With F_e(t)=G*u_e^2, define

    X_e=G*(t^2+e)^2/(4t^2),
    Y_e=G^2*u_e*(t^4-1)/(8t^3).

They satisfy E_G:Y^2=X^3-G^2X. Their Kummer classes in ordering (X-G,X+G,X) are (G,1,G) and (1,G,G). Together with torsion classes (2,2G,G),(-G,G,-1), the raw minor in the coordinatewise basis(-1,2,G) is

    0 1 0 1
    1 0 1 1
    0 0 0 1
    0 0 1 0.

Its determinant is1. Since G is positive odd nonsquare and the Kummer kernel is2E_G(Q), the two free points are independent. Removing the square factor of G gives the isomorphic E_n, so rank E_n>=2. Exact rank, analytic order, saturated generators and BSD equality are NOT claimed.

### 4. Execution, sources, next implication

21 grouped TypeScript assertions and36 Python assertions passed, including independent comparisons of all512 transitions. Commands: npm run lint; npm run typecheck; npm test; node dist/verify.js > results/finite-certificate.json; npm run test:symbolic. Lint is TypeScript's strict unused/unreachable diagnostics, not ESLint. Node22.16.0,TypeScript5.8.3,Python3.13.5,SymPy1.14.0. Three generated certificate outputs replayed byte-identically and all27 preexisting local hashes remained unchanged.

Wolfram15.0.1 independently returned64 states,512 transitions,closure=True,orbit32. It did NOT verify the rational escape. One initial HTTP502 and three20-second escape-related timeouts supplied no evidence. These are recorded separately from the successful closure call. The accepted contract follows disclosed exploratory discovery, not purported preregistration. No random sample or finite timeout supports a universal conclusion.

External foundations: inherited H12/H13 quartic/Kummer conventions, ordinary elliptic group law and Kummer kernel; Milne, Abelian Varieties v2.00(2008), I.3.7, printed19/PDF24, https://www.jmilne.org/math/CourseNotes/AV.pdf, re-read in screenshot. The specific shear commutation and all-word argument are derived above. Huang arXiv:1806.07869v5 was inspected only at abstract/metadata level as a related density lead, NOT a theorem input. No novelty claim or independent reconstruction of external foundational proofs.

Next target: the GLOBAL squareclass image of the enlarged semigroup X,Y,H,Phi. Breaking one local obstruction does not prove a prescribed prime is attained, and infinite output does not imply prime coverage. General rational-point existence, divisible-Sha control, complex-order comparison and universal BSD remain unresolved. No publication, external contact, spending or background process occurred.
