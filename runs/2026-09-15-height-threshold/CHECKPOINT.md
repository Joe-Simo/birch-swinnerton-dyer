# We have not solved the Birch–Swinnerton-Dyer problem yet.

## H6: sharp height rigidity and exact congruence reconstruction

Continuation of H5 at a340e2213a834fdfc45dd68874fab8501e8256ce, private branch research/h2-endpoint-20260914. Earlier H3/H4 corrections remain authoritative; obsolete isogeny computations are not premises. The expanded derivation and preservation receipts are in the conversation artifact BSD_H6_height_threshold_2026-09-15.zip, under /mnt/data/04-birch-swinnerton-dyer. That archive is not claimed mirrored into GitHub. This checkpoint and the executable checkers preserve the core proofs and actual finite evidence.

### 1. Sharp threshold for a compatible rational Kummer tower

Let M=E(Q), T its torsion subgroup, Lambda=M/T. Use H5's full logarithmic x-height normalization of the canonical quadratic height hhat. In positive rank let lambda=min{hhat(P)>0}; this exists and is positive because Lambda is a lattice with norm sqrt(hhat). These are established Mordell-Weil/Neron-Tate foundations, not new theorems.

For a compatible z_m in Sel_(2^m)(E), define H_m as the minimum canonical height of a rational Kummer representative, or infinity if none exists. Then

    limsup H_m/4^m < lambda/9

forces a single rational representative at every level. In particular H_m=o(4^m) suffices.

Proof: choose c<lambda/9 and minimizing representatives R_m with H_m<=c4^m eventually. Compatibility implies R_(m+1)-R_m=2^m Q_m. If Q_m has nonzero free part, its norm gives a lower bound 2^m sqrt(lambda) for this difference. The triangle inequality gives an upper bound (2+1)2^m sqrt(c), a contradiction. Free parts stabilize. Beyond the exponent of rational 2-primary torsion, a torsion difference in 2^mM belongs to odd torsion, invisible in all these quotients. One late representative works at every level. In rank zero the rational completion is finite rational 2-primary torsion, so the same diagonal conclusion for rational-representative towers is immediate without lambda.

Sharpness: choose a shortest P, with hhat(P)=lambda. Its free class is primitive. The 2-adic tower P/3 has representatives a_m P, a_m=(1-(-2)^m)/3. These are centered modulo 2^m. A competing representative a_m P+2^mQ with nonzero free Q has norm at least (2^m-|a_m|)sqrt(lambda)>=|a_m|sqrt(lambda). Hence the exact minimum over ALL rational representatives is H_m=a_m^2 lambda, and H_m/4^m tends to lambda/9. A diagonal R would satisfy 3R-P in odd torsion and hhat(R)=lambda/9, impossible. The strict constant cannot be increased.

A liminf is insufficient. Put alpha=sum_(j>=1)2^(2^j) in Z2 and z=alpha P. The binary digits are neither eventually zero nor eventually one, so alpha is not an integer; primitivity of P implies that z is not diagonal. Centered coefficients again give the exact minima. At m=2^(j+1) the coefficient is at most j*2^(2^j), yielding normalized height tending to zero. At m=2^j+1 its ratio to 2^m tends to -1/2. Thus liminf H_m/4^m=0 and limsup H_m/4^m=lambda/4. Also 2^N P/3 has a zero prefix of arbitrary prescribed finite length without being diagonal.

LIMIT: finiteness of H_m already demands rational representatives. A nonzero Tate-Sha component makes H_m eventually infinite. The theorem is not a method for silently replacing Selmer classes by rational points.

### 2. A certificate defined without rational points

For fixed homogeneous integral quadrics Q_i defining X in projective space, choose C such that |Q_i(v)|<=C*||v||_infinity^2. Define B_X(M) as the minimum radius among integer vectors with Q_i(v)=0 mod M and gcd(v_1,...,v_N,M)=1, or infinity if absent. Local points at the primes dividing M and CRT make this finite without assuming global points.

If C*B_X(M)^2<M, every integer residual is a multiple of M of absolute value less than M, hence zero. The vector is nonzero and defines an exact rational point. Consequently for any M_j tending to infinity:

    X(Q) nonempty
      iff B_X(M_j) is bounded
      iff liminf B_X(M_j)^2/M_j=0
      iff the strict certificate holds for some j.

The forward implications use a fixed primitive rational point; converses use the residual certificate. This is an equivalence and a finite verification mechanism, NOT a proof that a persistent torsor crosses the threshold. Ordinary local solubility yields at most a crude centered bound M/2, not the required order smaller than sqrt(M).

### 3. Exact congruent-number covering controls

For p=17 or41 use ordinary homogeneous coordinates (u:v:w:z):

    Q1=v^2-w^2-z^2,
    Q2=u^2-p*w^2+p*z^2.

The map x=p*w^2/z^2, y=p*u*v*w/z^3 has generic degree four and lands on E_p:y^2=x^3-p^2*x. It is the full 2-covering class (1,p,p) in ordering (x-p,x+p,x). Its Hessian pencil determinant is 16ab(a^2-p^2b^2). Away from characteristic2,p, a gradient dependence forces bu=av=(a+pb)w=(a-pb)z=0; at most one coordinate could survive, contrary to the equations. Thus this is a smooth genus-one intersection with good reduction outside2,p.

Here |Q1|<=2B^2 and |Q2|<=(p+1)B^2. The explicit residual constant is C=p+1. For primitive rational points, gcd(w,z)=1, |w|<=B<=sqrt(p)|w|, and the reduced multiplicative x-height is p*w^2/g with g=gcd(p,z^2) equal to1 orp. Therefore |h_x(image)-2logB|<=logp. This comparison assumes an actual rational point and does not provide one.

Do not confuse the degree-four embedding with the displayed degree-four MAP: the latter is a 2-covering. The standard [4]-covering associated with a degree-four genus-one model has degree16. A height formula with factor8 cannot be assigned to our displayed map just from its ambient P3 model.

X17 is everywhere locally soluble: at2 take (sqrt(-255),sqrt(17),1,4), at17 take (0,sqrt2,1,1), and at the real place take (sqrt17,1,1,0). The needed local square tests are exact. At all other primes smooth genus-one reduction has a finite-field point and it Hensel-lifts. To justify finite-field existence, identify the curve geometrically with its Jacobian. Frobenius acts as Jacobian Frobenius plus a translation; Frobenius-minus-identity has nonzero derivative and is a surjective morphism of projective curves, so a fixed point exists.

X17 has no rational point by H4's ALGEBRAIC rank-zero certificate and E17(Q)=(Z/2)^2: z=0 would require sqrt17 rational; with z!=0 the image cannot be torsion because w=0 gives u^2=-17z^2, v=0 gives w=z=0, and u=0 gives w^2=z^2 and v^2=2z^2. Thus B_X17(M)^2>=M/18 for all M. It is a NONPERSISTENT negative control and does not refute a bound that uses persistence. At M=18 the primitive vector(1,1,0,1) has residuals(0,18), proving that equality in the residual threshold is insufficient.

X41 has the exact primitive point(41,29,21,20), mapping to (18081/400,1023729/8000). This is a known point, not a new BSD case. Its radius41 crosses the certificate at M=2^17 because 42*41^2=70602<131072.

The exhaustive accepted finite population is p17 at levels k1..16 with cap512, and p41 at k1..17 with cap41. Minimum radii:

    17: 1,1,1,1,5,5,5,11,11,11,11,55,81,83,107,115
    41: 1,1,1,3,3,5,5,5,5,5,41,41,41,41,41,41,41.

At p17,k12: (55,15,9,12), residuals(0,4096); at k16: (115,85,77,36), residuals(0,-65536). At p41,k11 and17 the exact point above is a minimizer. The fixed point and monotonicity under divisibility of moduli prove B_X41(2^k)=41 for EVERY k>=11, not by extrapolation.

TypeScript enumerates(w,z) and least square roots; Python independently enumerates(u,v) and retains both lifts when dividing square congruences by2. Four small full-coordinate brute-force checks validate the reduction. All signs are represented since the equations use squares. A found solution certifies absolute minimality because any smaller vector is inside the searched cap; a cap miss would be inconclusive. There were no misses among these33 instances.

For any primitive rational point when p=1 mod8, w is odd and z even. The primitive Pythagorean parametrization w=A^2-B^2,z=2AB,v=A^2+B^2, with u=pc, leaves the exact global equation

    p*c^2=A^4-6*A^2*B^2+B^4,

where A>B>0 are coprime of opposite parity. Conversely such a solution gives a point. The41 control is(A,B,c)=(5,2,1). Parametrizing one conic has not solved this remaining quartic.

### 4. Source audit and next objective

Silverman's author exposition, An Introduction to the Theory of Elliptic Curves (Wyoming2006), https://www.math.brown.edu/~jhs/Presentations/WyomingEllipticCurve.pdf , physicalpage80/printedslide69 supplies the canonical-height foundations (successfully screenshotted).

Fisher-Sills, arXiv:1103.4944v1, Theorem4.1(iv), physicalpage22, https://arxiv.org/pdf/1103.4944 , bounds 2n*h_C(P)-h_E(piP) for P ALREADY in C(K). Its product-formula proof does not create a global point or supply an all-level uniform rate. Cremona-Fisher-Stoll, arXiv:0908.1741v1, Theorem1.1 and Section6, https://arxiv.org/pdf/0908.1741v1 , minimize model discriminants and reduce coordinates for locally soluble degree2,3,4 models under the stated class-number-one hypothesis. These results do not bound a nonexistent global representative. Exact locators and acquisition limits are in the expanded source register. No claim that our elementary constants or certificates are new to mathematics is made.

The next objective is a persistence-sensitive global construction or estimate on a FIXED torsor, strong enough to cross the residual threshold and valid without a pre-existing rational point or saturated Mordell-Weil basis. A larger undirected local search does not prove it. The general rank argument, possible divisible Sha, the complex-order comparison, and all-rank/non-CM BSD remain unresolved.

### 5. Actual execution and preservation

545 TypeScript assertions,256 Python/SymPy assertions, and one Wolfram call returning six grouped true checks passed. Wolfram checked four selected minima, generic pencil/map identities, the rational image and12 scalar coefficients, not the infinite propositions. Scalar tower fixtures run through64 levels. No floating heights or random sampling are used.

Observed Node22.16.0,TypeScript5.8.3,Python3.13.5,SymPy1.14.0,Wolfram15.0.1. Commands: npm run lint; npm run typecheck; npm test; node dist/verify.js > results/integer-results.json; npm run test:symbolic. Lint here is TypeScript strict unused/unreachable diagnostics, not ESLint/Biome. The Python checker reads the TypeScript output and recomputes minima independently. All ten preexisting local file hashes remained unchanged. No extra spending, publication, contact, background process, formal-kernel proof or independent expert review occurred.
