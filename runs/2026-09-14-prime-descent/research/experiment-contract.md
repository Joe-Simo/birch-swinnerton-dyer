# BSD checkpoint 1 — pre-execution contract

Status: No complete solution or counterexample candidate.
Target: ord_{s=1} L(E,s) = rank_Z E(Q), for every elliptic curve E/Q.
Scope: confirmed private repository Joe-Simo/birch-swinnerton-dyer only.

## Questions and routes

A. Can a characteristic-ideal equality alone identify a specialization rank?
Test finite-length modules over k[[T]]: same dimension modulo T, different
lengths. Prove the exact missing semisimplicity condition; these are auxiliary
algebra examples, not elliptic curves and not counterexamples to BSD.

B. Can the full Monsky matrix alone determine rank in the congruent-number
family E_n: y^2=x^3-n^2*x? First audit n=17 independently by algebraic
2-descent/Cassels pairing and by Tunnell's exact central-value formula.
Then test n=41 using two explicitly supplied rational points, their Kummer
classes and the 2-Selmer upper bound. No point-search-based upper bounds.

C. Can equal finite 2-Selmer data determine central vanishing?
Run all primes p=1 mod 8 with 1<p<=200. Compute the Monsky matrix, ternary
counts and the coefficient of q^p in q*prod((1-q^(8m))*(1-q^(16m)))*theta_2.
This finite domain tests a proposed data-reduction shortcut, not the universal
conjecture. Values outside this domain are not claimed checked.

## Definitions and arithmetic

A(n)=# {(x,y,z) in Z^3: x^2+2y^2+8z^2=n}.
B(n)=# {(x,y,z) in Z^3: x^2+2y^2+32z^2=n}.
Tunnell coefficient a(n)=B(n)-A(n)/2 for odd n.
For positive odd squarefree n, Tunnell Theorem 3 gives
L(E_n,1)=a(n)^2*beta/(4*sqrt(n)), with beta>0 explicitly a convergent integral.
All polynomial coefficients, counts, point coordinates and modular operations
are exact integers (TypeScript bigint). Number-valued array indexes are bounded
by 200, not used for large integer arithmetic. No floating L-values.

Coverage proof for counts: each nonnegative term <=n, so
|x|<=floor(sqrt(n)), |y|<=floor(sqrt(n/2)), |z|<=floor(sqrt(n/c)).
The implementation enumerates y,z and tests the remaining square, counting
both signs for nonzero x. Independent Wolfram checking will enumerate triples.
For q-series through degree 200, factors with exponent>200 contribute only
constant 1; descending updates exactly implement each polynomial factor.

## Intended evidence and limits

Algebraic rank 17 must not be inferred from the analytic coefficient.
Algebraic rank 41 must follow Kummer independence plus Monsky upper bound.
Analytic a(41)=0, if obtained, certifies only L(E_41,1)=0, not exact order 2.
Functional equation parity, if used, requires its own cited sign certificate.
The rank-zero p-converse must not be applied to positive corank.
A nonzero finite Sha[2] dimension does not imply positive infinite Selmer corank.

Tests will include squarefree/domain rejections, known small prime Monsky
matrices, exact Tunnell coefficients, invalid points and dependent Kummer
classes. Important calculations will have a separately written Wolfram check.
Results are classical theorems rederived or auxiliary obstructions; no claim of
novelty, formal-kernel verification, independent expert review, or full BSD.

## Source audits before execution

Read Tunnell (1983), pp. 323, 328-330: central-value normalization and the
conjectural nature of the converse are separate. An initial mental tally for
n=17 omitted triples with y=0; no tally is accepted without enumeration.
Read Zhang, arXiv:2111.11618v1, pp. 4-8: Monsky convention, Kummer coordinates,
Cassels pairing, Theorem 3.2 and its proof. Read Burungale–Tian,
arXiv:2506.03465v2, Theorem 1.1 and pp. 5-6 proof of Theorem 3.1.

## Follow-up registered after the first completed run

The first run returned a(113)=8 while a(41)=0; both have zero Monsky matrices.
Test the stronger shortcut that adding the first Cassels pairing suffices.
Use only p=17,41,113 with explicit (mu,tau)=(-3,1),(5,3),(9,7).
Check p=2mu^2-tau^2, mu=p mod4 and (-mu/p). Apply the pairing formula
in the proof of Zhang Theorem 3.2, not its converse for a vanishing pairing.
Use Wang arXiv:1511.03810v2 equation (1.1) and its pairing-kernel statement
to infer the exact order of Sel_4. Rank zero for p=113, if inferred, is from
Tunnell's established nonvanishing theorem; it is NOT an independently
algebraic cross-check against the same L-value.
