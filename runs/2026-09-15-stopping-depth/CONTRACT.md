# H4: coefficient and descent stopping depth

Status: no complete BSD candidate. Preserve H3 unchanged.

Questions: (1) Derive, independently of analytic rank theorems, the first Fisher pairing for every prime p=1 mod8 from p=a^2+16c^2; compare it with the parity of the signed Tunnell coefficient A_p/4. (2) Prove the all-depth finite-stopping/persistent-group dichotomy; only afterward compare with established CM theorems. No circular claim that analytically inferred higher pairings were explicitly constructed.

Success: an all-prime proof of the first coefficient/pairing congruence; a correctly normalized, hypothesis-audited relation between nonzero coefficients and stopping depth, with zero-coefficient cases kept separate. Failure: a convention counterexample or missing load-bearing source invalidates only that implication.

Discovery already occurred: a direct exploratory signed-count script below p=3000 suggested the parity formula and first nonzero coefficient divisible by 16 at p=1153. The accepted reproducibility run will cover exactly every prime p=1 mod8 with 1<p<=1200. This bound includes the first deeper regime, not an attempt to prove an infinite statement by enumeration.

Independent arithmetic: TypeScript bigint signed y,z enumeration and exact truncated q-product; Python/SymPy generic polynomial identities and fixed direct x,y,z counts; a separate Wolfram check when available. Rational and integer values stay exact; no numerical L-values or point-search rank bounds. Coefficients with value zero do not prove an exact positive analytic order.

Read and rerun archived H3 checkers before new acceptance. Run strict tsc typecheck/unused diagnostics, compiled checks, Python compile and symbolic checks. Preserve genuine logs and report the actual current versions. Mathematician self-review and separate software checks are not expert review or formal verification.

Notation at acceptance: the report uses c_p for the signed coefficient and A_p,B_p for the two ternary counts. This renames the contract's coefficient A_p; its normalization is unchanged.
