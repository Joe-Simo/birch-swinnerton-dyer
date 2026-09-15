# We have not solved the Birch–Swinnerton-Dyer problem yet.

## H3: repaired descent, explicit higher pairing, known algebraic endpoint

This compact remote record preserves the decisive proof and executable certificates. The expanded 3,740-word derivation, complete source audit, preservation hashes and genuine outputs are in the conversation artifact BSD_H3_exact_descent_2026-09-15.zip (SHA256 f0f24cf26c29b8d5f3f99594da36b9284405907f4e4ba144f4ce9eb237295c97), under /mnt/data/04-birch-swinnerton-dyer. The archive itself is not claimed mirrored here. Source-dependent, self-reviewed mathematics is not independent expert review or formal verification.

**Result:** for E:y^2=x^3-113^2 x and E':Y^2=X^3+4*113^2 X, the argument below proves rank E(Q)=rank E'(Q)=0 and

    Sha(E/Q)[2^infinity]=(Z/4Z)^2,
    Sha(E'/Q)[2^infinity]=(Z/2Z)^2.

This is a known special case, not a new BSD theorem. No analytic rank theorem or refined BSD formula is an input to the algebraic proof. General BSD remains unresolved.

### Preservation and corrections

All existing files are preserved. This record supersedes the false isogeny-group claims in CONNECTING_MAP.md, Q2-OBSTRUCTION.md, DUAL-COMPLETE.md, EMBEDDING-AUDIT.md, FILTRATION-CORRECTION.md and THETA2-CONSTRUCTION.md under runs/2026-09-14-higher-descent. Their order-two groups and one-dimensional pairing argument must not be reused. The older H2 analytic-theorem endpoint has a separate dependency chain.

For r^2=d s^4-(113^2/d)t^4, negative d does NOT make both terms negative: d=-1 has (s,t,r)=(0,1,113), and d=-113 has (1,1,0). The claimed real obstruction is false. On the positive curve, d=113e gives e r^2=113(e^2 s^4+4t^4), not 113(e^2 s^4+4*113*t^4). The extra factor created the false 113-adic obstruction. Also, quartic scaling has weights (2,1,1), not ordinary triple scaling. Fisher's f2 belongs on C1; f3 belongs on C2, and f4 on C3. The old p-class on the negative curve is rational-torsion-derived and cannot be killed by the proposed pairing.

### Correct first groups and conventions

Put p=113 and fix phi:E->E' and its dual:

    phi(x,y)=((x^2-p^2)/x,-(x^2+p^2)y/x^2),
    phihat(X,Y)=((X^2+4p^2)/(4X),(4p^2-X^2)Y/(8X^2)).

They extend over their kernels (0,0) and compose to [2]. Use Fisher's Section 2 convention

    S=Sel^phi(E/Q), with E'(Q)/phi E(Q) injecting into S;
    S'=Sel^phihat(E'/Q), with E(Q)/phihat E'(Q) injecting into S'.

The connecting maps are the respective x-coordinate modulo squares; at O use 1, at (0,0) use b in y^2=x(x^2+a x+b). For q not dividing b, vq(x) is even: the valuations of the right side are vq(x) or 3vq(x) when x has positive or negative valuation. Hence S' is supported only on -1,p; its four classes are all attained by rational 2-torsion. For S the support is -1,2,p; negative classes are excluded over R on the positive quartics.

The four positive classes all survive. At 2, for d=1,2,p,2p use respectively r^2=1,4*6385,113,4*113, with (s,t)=(1,0),(1,1),(1,0),(1,1). The odd units are 1 mod8. At 113, d=2 uses sqrt(2) with 51^2=2 mod113; d=p and 2p use r=0,t=1 and simple roots s=14 of s^4+4 and s=18 of s^4+1 modulo113. All indicated derivatives are units. At every other odd prime the quartics have smooth genus-one reduction; the Hasse bound gives a point and Hensel lifts it. Thus, rigorously at ALL places,

    S=<2,p>={1,2,p,2p},   S'=<-1,p>={1,-1,p,-p}.

Both dimensions are TWO. All of S' consists of rational-point classes, so S'_m=S' for every m.

For full Kummer order (x-p,x+p,x), the map S->Sel2(E) is d->(d,d,1), and the map to S' is projection to the third coordinate. Indeed under phihat,

    x-p=(X-2p)^2/(4X), x+p=(X+2p)^2/(4X), x=(Y/(2X))^2.

The cohomology inclusion has zero kernel because phi(E[2](Q))=E'[phihat](Q). Rational torsion surjects to S'. Therefore |Sel2(E)|=16, with independent basis (2,2,1),(p,p,1),(2,2p,p),(-p,p,-1).

### Actual covering on the non-torsion-derived side

Start with p in S, on E': C1:r^2=p(s^4+4t^4). Define

    f=7l^2-16lm-7m^2, g=4l^2+7lm-4m^2, h=113(l^2+m^2).

Then 113(f^2+4g^2)=h^2. Take xi2=1 to obtain C2:f=s^2,g=t^2. Its pencil is -(113/4)ab(4a^2+b^2). It has local points (l,m,s,t)=(1,-1,4,sqrt(-7)) at2, (1,1,4sqrt(-1),sqrt(7)) at113, and (1,0,sqrt(7),2) over R; the good primes follow from the pencil and Hasse.

Parametrize its separate conics by

    p1=c^2+8cd+23d^2; p2=-c^2+7d^2; p3=4c^2+30cd+28d^2;
    q1=theta^2+4psi^2; q2=7psi^2-4theta psi; q3=-2theta^2+7theta psi+8psi^2.

The identities f(p1,p2)=p3^2 and g(q1,q2)=q3^2 hold exactly. Taking xi3=1 gives

    C3: F1=c^2+8cd+23d^2-theta^2-4psi^2=0,
        F2=-c^2+7d^2-7psi^2+4theta psi=0.

Its map to C2 is (p1,p2,p3,q3). Fisher's construction identifies C3 as a (2phi)-covering of E', with Jacobian E and degree eight over E'; it is NOT a multiplication-by-4 covering of E. It represents p in S3.

### Complete local-solubility certificates

The C3 pencil is (7a^2-16ab-7b^2)(4a^2+7ab-4b^2), with discriminant 4*113^6. This proves smooth genus-one reduction at every odd prime except113; Hasse and Hensel handle all of them.

At113, (c,d,theta,psi)=(21,-8,0,1) has residual (565,0) and Jacobian minor in theta,psi equal32, a unit. Over R take d=1,psi=0,c=sqrt7,theta=sqrt(30+8sqrt7).

At2 use the integral approximation A=(15035,18942,-121505,9471). Its residuals are (-4365484032,-2945449984), with valuations (18,20). The Jacobian determinant in c,theta has valuation2. Hold d,psi fixed. The strong multivariable Hensel criterion gives an exact point P2=A mod2^16: if F(a) lies in pi^n and detJ has valuation delta with n>2delta, the adjugate formula gives Newton corrections in pi^(n-delta), the new residual in pi^(2(n-delta)), and a stable determinant valuation. Iteration converges. Here n=18,delta=2. Mere compatible residues are not the justification.

### New pushout and its exact all-place product

Over L=Q(w), w^2=113, set epsilon=(8+w)/7, alpha=(15+w)/7, gamma=(15-w)/4. Then

    p1-epsilon*p2=alpha(c+gamma*d)^2.

The conic Gamma:q1-epsilon*q2=alpha*Z^2 has the verified L-point (theta,psi,Z)=(-6-w,1,(1-w)/2). Seven times its half-gradient tangent, after Z=c+gamma*d, is ell=U+wV, where

    U=49c-14d-26theta-350psi,
    V=7c+14d-5theta-35psi.

F=(U^2-113V^2)/psi^2 is Fisher's f4 on C3, up to a rational norm constant. A conic tangent pulls back to a constant times the square of a linear form under parametrization, identifying this with Fisher's normalization. A rational constant does not change the global Hilbert product, by reciprocity.

At A the numerator N=-47126055328128 has valuation7 and is 640 mod1024=2^7*5. The exact P2 agrees mod2^16, so it has the same residue; psi is odd. The formula (2^k*u,2)_2=(-1)^((u^2-1)/8) gives -1 because u=5 mod8.

At7,113 and infinity, 2 is a local square (roots3 mod7 and51 mod113, and positivity), so the symbols are +1. Points can be chosen away from finite zeros and poles; the real psi=0 point only certified solubility.

Every remaining prime is accounted for. L is unramified outside113. The norm of Gamma's symmetric determinant is -16*113^2/7^3, so the conic, its point and primitive tangent have good reduction away2,7,113. On a smooth pointed conic a tangent has even valuation at every primitive point where nonzero: in integral coordinates XZ=Y^2, near its tangency point X is a unit and Z=Y^2/X. The conic projections remain primitive because theta,psi cannot both vanish modulo q: resultant_c(p1,p2)=4*113*d^4, with no basepoint also on d=0. At split q the two tangent valuations are even; at inert q the norm valuation is automatically even. Dividing by psi^2 preserves evenness. Thus (F(Pq),2)_q=Legendre(2,q)^vq(F(Pq))=+1 for every remaining odd q.

Consequently the complete product is -1, and

    Theta3(113,2)=1.

### Rank and primary groups, without analytic input

C3 proves p in S3, hence a nonzero radical element for the alternating first pairing on two-dimensional S1. Thus S2=S1. The even pairing is zero because S' is entirely rational-point-derived, so S3=S2=S1. Theta3 is nondegenerate with matrix [[0,1],[1,0]] in basis(p,2); its kernel S4=0.

The rational quotient E'(Q)/phiE(Q) is therefore zero, while E(Q)/phihatE'(Q) has dimension2. Both isogeny kernels have dimension1. Fisher's rank identity gives rank0+2-1-1=0 on both curves.

In Fisher's Sha-image notation, |X1|=|X2|=|X3|=4 and Xm=0 for m>=4; X'_m=0 always. In particular Sha(E')[phihat]=0. The injectivity of phihat and X2=phihat Sha(E')[2], X4=2phihat Sha(E')[4]=0 show Sha(E')[2^infinity]=(Z/2)^2. Also Sha(E)[2]=Sha(E)[phi] has order4, and X3=2Sha(E)[2phi] has order4 with kernel Sha(E)[2], giving a subgroup of order16. Every 2-primary class of Sha(E) maps into the four-element primary group of E', with kernel of order4, so the whole primary group has order16. Its exponent is at most4 and its 2-torsion has order4, forcing (Z/4)^2. No finite-whole-Sha assumption, odd-primary claim, or BSD formula enters this argument.

### Uniform feature and remaining gap

For every prime p=1 mod8, the same first-stage groups are <2,p> and <-1,p>, with the latter entirely torsion-derived. The necessary fourth roots at p exist since -1 is a fourth power and 2 is a square. Thus all even Fisher pairings for this kernel vanish; finite stopping occurs through odd self-pairings. Persistent classes at every finite stage still do not supply rational points or rule out divisible Sha. There is no general higher-rank, non-CM, or complex-order bridge here.

A separate exact Tunnell comparison gives A8(113)=32,A32(113)=24,a(113)=8, so L(E,1)=a(113)^2*beta/(4sqrt113)>0. This verifies the rank equality for the known example, independently of the preceding algebraic derivation. Next: investigate a uniform relation between odd-pairing stopping and central coefficients without using the analytic rank-zero theorem as an input to the local construction.

### Sources and execution

[F] Tom Fisher, arXiv:1509.03234v1 (10 September2015), https://arxiv.org/pdf/1509.03234v1 . Sections2-5; Theorems2.1,3.1 (no Sha finiteness needed), rank and image sequences pp4-5, equations8-14, pushout paragraph p13. Key equation pages visually inspected. General Magma implementation not run.
[T] Tunnell, Invent.Math72(1983),323-334, Theorem3 p328, original scan https://sites.math.rutgers.edu/~zeilberg/EM22/JT1983.pdf . Used only for the separate analytic comparison. Other inputs: Kummer exact sequences, local square and Hilbert formulas, reciprocity, Hasse, smooth-pencil criterion; strong Hensel proved above.

Actual versions: Node22.16.0, TypeScript5.8.3, Python3.13.5, SymPy1.14.0, Wolfram15.0.1. Commands successfully run: tsc --noEmit -p tsconfig.json; tsc -p tsconfig.json; node build/verify.js; python -m py_compile verify_symbolic.py; python verify_symbolic.py. The strict compiler is the native lint equivalent, not a separate lint program. There are 17 exact TypeScript checks and25 symbolic/rational Python checks, including negative controls; Wolfram independently agreed on the stated finite identities and local certificates. Code does not re-prove Fisher or formalize the all-place argument. No background process, spending, public release or submission occurred.
