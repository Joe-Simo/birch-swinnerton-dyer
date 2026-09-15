# We have not solved the Birch–Swinnerton-Dyer problem yet.

## H10 final state — simultaneous family, followed by exact prime exclusion

Parent:24a88b4b32c41115bd2b9e3dbdcef97cc50ac9b5, private branch research/h2-endpoint-20260914. Work is confined to this BSD project. The complete local record and checker outputs are in the conversation archive BSD_H10_simultaneous_family_2026-09-15.zip; the archive itself is not claimed mirrored into GitHub.

**Established:** for all coprime nonzero integers a,b, the squarefree kernel n of

    D=a^8-56a^4b^4+1296b^8

is positive, greater than1, and supported on primes1 modulo8. The formulas below give two rational points independent modulo torsion on E_n:y^2=x^3-n^2x. Infinitely many distinct n occur. **The completed follow-up proves that41 is the only prime kernel in this entire family**, reached exactly at a/b=+/-2,+/-3. Hence infinitely many distinct composite kernels occur, but this construction cannot address a new prime case beyond41.

### Source of the two points

Write D=n*s^2 and set, for e=-1,+1,

    A_e=a^2-6e*b^2, B=2ab,
    u=n*s, v_e=A_e^2-e*B^2, w_e=A_e^2+e*B^2, z_e=2A_eB,
    P_e=(n*w_e^2/z_e^2, n*u*v_e*w_e/z_e^3).

Direct polynomial identities give

    A_e^4+6e*A_e^2B^2+B^4=D,
    v_e^2-w_e^2+e*z_e^2=0,
    u^2-n*w_e^2-e*n*z_e^2=0.

All needed factors are nonzero. Their full Kummer classes in order(x-n,x+n,x) are(1,n,n) and(n,1,n); together with the rational torsion classes(2,2n,n),(-n,n,-1), they have a determinant-one binary minor. The core proof establishes nonsquareness by square-area descent, prime support by two norm identities, and infinitude by fresh prime divisors at exact odd valuation. These are written all-parameter arguments, not extrapolations from a finite scan.

The established Monsky upper bound becomes2k-2rank(A) when n has k prime factors and A is the additive Legendre matrix with row sum zero. If rank(A)=k-1, rank E_n(Q)=2 and its2-primary Sha vanishes. Two accepted finite examples have upper bound4, so they are reported only as rank between2 and4. No analytic order is asserted for the infinite family.

### Completed prime filter

The factorization D=F_minus*F_plus and exact gcd c^2, with

    F_e=a^4+4e*a^3b+8a^2b^2+24e*ab^3+36b^4,
    c=2^{[2 divides a]}*3^{[3 divides a]},

show that a prime kernel requires one normalized factor to be a square. PRIME_FILTER.md proves that all affine rational points of

    w^2=t^4-4t^3+8t^2-24t+36

are(0,+/-6),(2,+/-2),(3,+/-3). The proof explicitly maps it to E0:Y^2=X(X-1)(X+3), proves rank E0(Q)=0 by a2-isogeny descent, bounds torsion by exact good-reduction counts8 at5 and7, and handles the exceptional fibre in the map. It is not a bounded rational search. Replacing t by-t handles the other factor, so nonzero admissible parameters are exactly+/-2,+/-3 and each yields41.

### Verification and authoritative record

The core experiment has exactly8 parameter pairs and16 family points. It passes198 TypeScript and213 Python assertions. The focused prime-filter follow-up adds34 TypeScript and30 Python assertions: **232 and243 total**. Both TypeScript outputs replay byte-identically. Three actual Wolfram calls agree; the first two contain preserved symbol warnings and the supplementary call has none. The first auxiliary Python run found an overinclusive expected-residue fixture, corrected to{2,6,8}; the note is preserved and the valuation proof did not change.

Run npm run lint, npm run typecheck, npm test, npm run test:symbolic. Lint means TypeScript strict unused/unreachable diagnostics, not ESLint/Biome. Results/ contains execution evidence; these counts do not measure progress toward a complete BSD proof. All18 original local hashes remain unchanged.

On GitHub, RESEARCH.md and AUDIT.md preserve the core snapshot before the final prime classification; their Section7 remaining-filter language is superseded by this checkpoint and PRIME_FILTER.md. The full revised local RESEARCH.md, expanded contract, source register and logs are in the conversation archive. PRIME_SOURCES.md pins the follow-up inputs. The root research-history index points here as the current H10 state.

**Outcome:** a self-reviewed restricted algebraic construction, followed by a proved obstruction to its use on any new prime case. No novelty, independent expert verification, formal proof, analytic-order theorem for this family, all-prime construction, publication or complete BSD solution is claimed. The next mathematical step must use a genuinely different construction or a persistence-sensitive global argument; enlarging this parameter scan cannot overcome the prime exclusion. No process continues in the background.
