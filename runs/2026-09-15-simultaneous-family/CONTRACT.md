# H10 — simultaneous-family verification contract

Target: continue H9 by constructing special rational parameter families that supply BOTH H8 covering classes, without pretending that H9 permits a generic companion formula over Q(t). Universal BSD remains the project objective; this run only attempts algebraic rank lower bounds and a conditional descent upper bound.

## Discovery already performed

Before this contract, algebraic manipulation produced D(a,b)=a^8-56a^4b^4+1296b^8 and A_e=a^2-6e b^2, B=2ab. SymPy returned both quartic identities and exploratory factorizations for b=1,a=1..15. Those observations are discovery, not a preregistered experiment. They motivate the proofs; they do not prove all-parameter existence or infinitude. An earlier Rubin–Silverberg degree-six specialization was discarded as a bridge to primes 1 mod8 because every rational parameter has an odd valuation at3.

## Accepted mathematical and finite claims

Prove for ALL coprime nonzero integers a,b: D>0, D nonsquare, its squarefree kernel n is odd with every prime divisor1 mod8, and two explicit points of E_n:y^2=x^3-n^2x have independent free classes. Prove infinitely many DISTINCT squarefree kernels using a fresh prime divisor and a simple-root lift, not by counting parameter values. Apply the known Monsky matrix only when its exact hypotheses hold; this gives rank2 when its reduced matrix has rank k-1. No analytic rank is computed or inferred.

Finite population: exactly eight pairs (a,b)=(1,1),(2,1),(3,1),(4,1),(5,1),(7,1),(1,2),(3,2). These exercise odd/even a, valuation at3, rational nonintegral parameters, duplicate twists, and both rank-upper-bound2 and4 cases. Separate sign/scaling checks use (-2,1) and (6,3); they do not enlarge the population. Reject zero/nonprimitive parameters in the certificate constructor.

TypeScript: exact bigint arithmetic, trial factorization with reconstruction, square-root floor by integer bisection, finite-field Gaussian elimination, Legendre symbols via Euler's criterion; no Number conversion of large integers. Points are checked by integer cross-products, not floating coordinates or numerical heights. Finite assertion count is reported mechanically. Expected squarefree kernels and upper bounds are validation fixtures disclosed above, not discoveries.

Python: SymPy polynomial identities plus separately computed Fraction points, factorint and finite-field elimination. It recomputes from the eight parameters rather than accepting the TypeScript results, then compares final certificates. It also tests the simple-root lifting mechanism at two specific primes; those tests do not prove Schur's lemma or infinitude, which are proved in the paper record.

Wolfram: separately written exact polynomial/point/matrix checks, stateless Module variables, including squarefree normalization and the prime-factor residue test. Not an independent expert or formal-kernel verification.

## Success, failure and limits

Success: complete all-parameter derivation with explicit nondegeneracy, independence and infinity proofs, and reproducible finite certificates. Failure: either identity fails, the two points differ only by torsion/multiplication, or squarefree normalization loses the claimed classes. A generic construction is not automatically a covering of every desired prime. Prime members require additional arithmetic; no claim of infinitely many prime members, all-prime coverage, novelty, analytic-order equality, refined BSD, full saturation or universal BSD.

Work is confined to this new run subtree and the existing private BSD branch; old records and all18 existing local files are preserved. Any correction to this contract is appended, never represented as pre-discovery registration.
