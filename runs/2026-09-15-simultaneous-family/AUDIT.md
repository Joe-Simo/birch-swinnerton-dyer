# H10 adversarial self-review

**Claim audited:** for every coprime nonzero pair a,b, the squarefree kernel n of D(a,b)=a^8-56a^4b^4+1296b^8 is positive, odd and greater than1, with all prime factors1 mod8, and E_n(Q) contains the two independent points in RESEARCH.md; infinitely many distinct n occur. Exact rank2 requires the separately stated Monsky-matrix condition.

**Primary verdict: proved as written**, using the established Mordell-Weil/Kummer and Monsky inputs for their expressly stated roles. This is the author's self-review, not independent expert verification or a formal-kernel proof, and the claim is not the universal BSD target.

## Dependency and obligation check

- Passed — Simultaneous quartic identity: expansion on both signs; evaluated independently in three languages. No square roots enter the point construction except the integer s in the exact factorization D=n*s^2.
- Passed — Parameter boundary: a=0 or b=0 would make D a square and collapse denominators; both are explicitly excluded. A_plus=0 requires sqrt6, v_plus=0 requires sqrt7, and the other needed factors are nonzero sums of squares. Negative parameters change point signs but do not invalidate the identities.
- Passed — Squarefree normalization: y scales by s^3 and x by s^2 from E_D, not the reverse. The direct normalized covering uses u=n*s, not u=D. Exact Fraction certificates agree.
- Passed — Nonsquareness is independent of rank: construct on E_D first, transform to a triangle, and use the written infinite descent. In that descent UV=v/2 forces s_0 even before the smaller triangle's square area is asserted.
- Passed — Local prime support: the factors2 and3 have valuations0/4 in D; odd q>3 dividing D divides neither ab nor A_plus*B. The two norm identities then establish both (-1/q) and (-2/q) equal1. No classification from a finite residue scan is substituted for these arguments.
- Passed — Point independence: two distinct points alone would be insufficient. Their full Kummer classes, together with both rational torsion generators, have an explicit odd determinant minor. Absence of rational4-torsion is checked; odd torsion is invisible mod2. A primitive integer relation would therefore contradict the same minor.
- Passed — Infinity is not parameter counting: the duplicate parameters2 and3 both yield41. The proof instead supplies a new prime to odd valuation outside any finite set of previous supports. Simple roots are justified by the derivative and the exact remainder512, without a genericity assumption or squarefree-values conjecture.
- Passed — Rank upper bound: the source's odd squarefree hypotheses and its diagonal terms are checked. Two examples have upper bound4 and are NOT mislabeled rank2. No Sha finiteness is needed to deduce zero2-primary Sha where the dimension is exhausted by rank2.
- Passed — Prime filter: exact gcd of F_minus,F_plus is c^2, including the valuations at2,3. One normalized factor being a square is necessary but not alone sufficient for n to be prime. The auxiliary quartic's rational point does not solve prime coverage.
- Passed — H9 compatibility: the added equation y^2-x^2=6 changes the parameter family; the calculation does not claim a generic rational map between H9's two fixed torsors or use the trace of a point over Q(i).
- Not addressed — Exact analytic order on the new infinite family; existence for an arbitrary original prime; infinitely many prime members; exact rank when the matrix upper bound exceeds2; full saturation; general BSD.

## Computation boundary

Eight parameter pairs and sixteen point witnesses are the registered finite population. TypeScript and Python compute the same rationals and finite-field matrices by different implementations. Their assertion totals are test counts, not numbers of new theorems. Wolfram's returned expressions agree; its global-symbol warning is preserved rather than described as a warning-free run. None of the tools independently verifies the universal prose deductions or source theorems.

No source-level or mathematical failure was found in this review. The strongest surviving result is an infinite, explicitly selected rank-at-least-two family, not a solution of the input problem. The next relevant obstruction is arithmetic coverage, now narrowed by the factor-square condition in Section7.
