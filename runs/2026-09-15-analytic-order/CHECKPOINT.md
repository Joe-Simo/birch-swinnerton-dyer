# We have not solved the Birch–Swinnerton-Dyer problem yet.

## H7: exact analytic-order certificates

Parent: 7705e9b1104679ff9b2a47cc946be8f6bd87ace8, private research/h2-endpoint-20260914. H3-H6 corrections remain authoritative. Previous files are preserved. The expanded derivation, all slab intervals, two coefficient lists/implementations, genuine outputs and preservation hashes are in the conversation archive BSD_H7_analytic_order_2026-09-15.zip under /mnt/data/04-birch-swinnerton-dyer. The archive is not claimed mirrored remotely.

RESULT: ord_(s=1) L(E_p,s)=2 for E_p:y^2=x^3-p^2*x and exactly p=41,137,257,313,353,457,761. These seven curves were the fixed zero-coefficient population of H4, not a larger scan. Combining the independent Kummer/descent certificate below with the analytic computation proves the known core rank equality for E41. The other six algebraic ranks, the refined formula and general BSD are not certified here. No novelty, expert review or proof-assistant verification is claimed.

### Source/model dictionary

[T] Tunnell, Invent. Math.72 (1983),323-334, DOI10.1007/BF01389327; https://sites.math.rutgers.edu/~zeilberg/EM22/JT1983.pdf, printed pp.325,328-329, Theorem3; scanned formulas were read as screenshots. E_p is the positive quadratic twist of E1. Its full Dirichlet coefficients have a1=1, arithmetic center1, additive factors1 at2,p, and good-prime factors 1-a_l*l^-s+l^(1-2s). The discriminant64p^6 is nonzero.

[MO] Martin-Ono, Eta-quotients and elliptic curves, Proc.AMS125 (1997),3169-3176; author manuscript https://uva.theopenscholar.com/files/ken-ono/files/026_8.pdf, Theorem2, physicalpage5 table (screenshotted). The conductor32 eta product belongs to Y^2=X^3+4X. The explicit degree2 isogeny X=(x^2-1)/x, Y=-y*(x^2+1)/x^2 from E1 identifies their L-functions. Hence f1(q)=q*product_m(1-q^(4m))^2(1-q^(8m))^2, and a_n(E_p)=a_n(E1)*(n/p).

The conductor is N=32p^2: p=1mod8 is a Q2 square, so the exponent at2 stays5; at p a tame ramified quadratic twist of the good two-dimensional Tate representation has no inertia invariants and conductor exponent2. Elsewhere reduction stays good. These are standard conductor/modularity/isogeny facts, not BSD input.

[R] Cowland Kellock-Dokchitser, arXiv:2303.07883v1, Theorem2.15, physicalpage9 (screenshotted), published DOI10.1112/blms.12931. The coprime-conductor twist formula gives w(E_p)=w(E1)*sign(p)*(p/32)=+1. Here w(E1)=+1 follows already from Tunnell's nonzero E1 central value. This uses the stated theorem, not the adjacent algebraic parity conjecture. The 2005 original result is identified in the expanded ledger, but its full proof was not reacquired; the exact readable formulation used is by the theorem's author.

### Exact zeros and integral

A_p counts all integer triples x^2+2y^2+8z^2=p; B_p uses32 instead of8. Tunnell gives L(E_p,1)=c_p^2*beta/(4sqrt(p)), c_p=B_p-A_p/2, beta=integral_1^infinity dx/sqrt(x^3-x)>0. Every row below has A_p=2B_p. No numerical near-zero is used.

Put alpha=2*pi/sqrt(N), F(t)=sum_(n>=1)a_n exp(-alpha*n*t), Lambda(s)=alpha^-s Gamma(s)L(s). The modular transformation F(1/t)=t^2F(t) gives

    Lambda(s)=integral_1^infinity F(t)*(t^(s-1)+t^(1-s)) dt,
    Lambda''(1)=2 integral_1^infinity F(t)*(log t)^2 dt.

This is also the weight2 specialization of the Mellin-splitting method in T.Dokchitser, arXiv:math/0207280v1, equations(8)-(9), https://arxiv.org/pdf/math/0207280. The relevant formulas were read; ComputeL was not run. Hasse/Euler recurrences give |a_n|<=d(n)sqrt(n)<=2n, ensuring absolute convergence of all needed derivatives. Exact L(1)=0 and even Lambda force L'(1)=0; therefore L''(1)=alpha*Lambda''(1). A positive enclosure proves exact order2, not just an upper bound inferred from approximate zero values.

### Both infinite tails are bounded

On each [A,2A], A a power of2, use K=max(1,ceil(16p/A)) terms and32 equal subintervals. Interval Horner evaluation of P_K(exp(-alpha*t)), multiplied by2(log t)^2 and the exact width, encloses every integrand value, so its rectangular sum is rigorous. The discarded Fourier contribution on a slab [A,B] has absolute value at most

    R_A=4(log B)^2/alpha * exp(-alpha*A*(K+1))/(1-exp(-alpha*A)).

Proof: bound |a_n| by2n and integrate each exponential from A to infinity; the factor n cancels. Stop at the first power of2 T>=128p. Since (log t)^2<=t^2, the remaining integral is at most

    R_inf=4 exp(-alpha*T)/(1-exp(-alpha*T))
          *(T^2/alpha+2T/alpha^2+2/alpha^3).

Integrating t^2 exp(-alpha*n*t) exactly and bounding 1/n,1/n^2 by1 proves this. Enlarge the finite interval by plus/minus an upper endpoint of sum R_A+R_inf.

### Two separately implemented enclosures

verify.ts uses only bigint endpoints in units2^-80, with signed outward floor/ceiling for every arithmetic operation. Integer square root encloses sqrt32. Machin pi=16atan(1/5)-4atan(1/239) uses24 alternating terms and the next positive term as remainder. For log, reduce x=2^k*r, 1<=r<=2, and put y=(r-1)/(r+1). Use24 terms of 2 sum y^(2j+1)/(2j+1); the remainder is bounded by 2y^49/[49(1-y^2)]. For exp(-x), 0<=x<128, use (1-x/m)^m<=exp(-x)<=(1+x/m)^(-m), m=2^24, via24 repeated outward squarings. For x>=128, e>2 bounds it in[0,2^-80]. No floating transcendental function or guessed numerical error is involved. Exact downward eta-product multiplication and Legendre twists produce the coefficients.

coefficients.py independently computes finite-field traces and Euler recurrences. integrate_iv.py repeats the entire range integration in mpmath1.3.0 iv at25 decimal digits. This context is documented as experimental; the integer checker avoids a single-library dependency. verify_independent.py compares all37,104 retained coefficients, independently counts full triples, reruns each enclosure and checks containment inside the bigint enclosure. The same researcher wrote both implementations. No ordinary quadrature output is accepted as proof.

Every interval below bounds the derivative L''(1), not its Taylor coefficient L''/2. Decimal endpoints are outward-rounded rationals.

|p|A_p|B_p|initial K|T|L'' lower|L'' upper|
|--:|--:|--:|--:|--:|--:|--:|
|41|32|16|656|8192|15.824797|17.046590|
|137|32|16|2192|32768|36.650104|38.780383|
|257|64|32|4112|65536|53.557096|56.414885|
|313|32|16|5008|65536|56.000591|58.992879|
|353|64|32|5648|65536|48.009683|51.132721|
|457|32|16|7312|65536|48.868009|52.440431|
|761|160|80|12176|131072|33.434042|37.500299|

### Independent E41 arithmetic and limitations

P=(-9,120), Q=(841,24360) satisfy E41 exactly. Their Kummer triples, together with T+=(41,0), T0=(0,0), reduce to (2,82,41),(-41,41,-1),(-2,2,-1),(2,2,1) in ordering(x-41,x+41,x). In basis(-1,2,41) coordinatewise the rank is4: coordinate1's 41-valuation kills T0, coordinate3's 41-valuation kills T+, coordinate1's sign kills P, and its2-valuation kills Q. Kummer exactness gives MW rank>=2. Zhang, arXiv:2111.11618v1 Section2.1 (2.2)-(2.5),(2.8), gives a zero2x2 Monsky matrix at41 because(2/41)=(-2/41)=1, so pure Sel2 dimension2 bounds the rank above. Thus rank E41=2 independently of L. A saturated basis, regulator, full Sha finiteness and refined BSD are not established here.

Current rank2 literature does not fill H6's gap. Castella arXiv:2204.09608v3 (February13,2026), TheoremB, was inspected with its auxiliary good-ordinary prime>=5 and character hypotheses. It concerns generalized Kato classes, Selmer dimension and localization; it does not remove the Tate-Sha quotient or construct H6's small rational representatives. It is not a dependency of the seven certificates.

### Actual execution and continuation

Commands passed: npm run lint; npm run typecheck; npm test; node dist/verify.js > results/exact-rational.json; python verify_independent.py p for each of the seven p; python verify_algebra.py. Lint is the stated compiler unused/unreachable check, not ESLint. The37,134 TypeScript assertions include37,104 coefficient-bound checks; this is seven certificates, not thousands of curves. Python's largest accepted independent rerun took23.54 seconds. Wolfram checked coefficient prefixes, isogeny/point residuals, Kummer rank and two symbolic integral identities; its X/Y warning is preserved. It did not run the interval quadrature.

Node22.16.0, TypeScript5.8.3, Python3.13.5, mpmath1.3.0, Wolfram15.0.1. A free python-flint install failed DNS; none was installed. An interrupted exploratory batch was rerun for its unfinished case. SciPy discovery is explicitly noncertifying. No spending, external contact, public posting or background process occurred.

Next structural question: can c_p=0 yield a uniform sign decomposition of the derivative integral without assuming BSD or rational points? Seven finite enclosures do not supply that theorem. Even analytic order2 alone does not settle the remaining rational-point/height implication. All-rank, non-CM and complete BSD remain unresolved.
