# H14 contract — mixed transport

Parent: 9c3de10b18c295b9678714855a01b3a252151ec0, private BSD branch research/h2-endpoint-20260914. Only /mnt/data/04-birch-swinnerton-dyer is writable for research. Prior files were hashed before this run.

Target: decide whether arbitrary words in H12's separate tripling maps X,Y and its osculating map Phi escape H13's quadratic-character obstruction at 13, then execute a mathematically different operation if they do not.

Discovery was performed before this accepted checker contract. Exploratory finite-field searches at 5,11,13,19,23,29,31,37,43,53,61 reported all affine pole encounters; they were NOT full projective-orbit certificates. At 13 alone the X,Y,Phi orbit closed with no poles. Auxiliary exact odd-multiplier tests were exploratory, not exhaustive. The accepted result concerns 13 and the stated maps only.

Accepted finite assertions: enumerate the precisely defined 64-point set Omega in F_13^3; check closure and unit denominators for X,Y,Phi, x/y inversion and three coordinate sign changes; independently enumerate the X,Y,Phi orbit of (1,11,3). All finite-field arithmetic is exact. No skipped pole can support closure. The universal conclusion is induction on word length, not extrapolation from a prefix.

Follow-up: mix the two E0 factors by H(P,Q)=(P-2Q,Q), which commutes with the translated Kummer involution. Check the word Y,H,Phi over Q(sqrt(137)) and independently modulo 13. The osculating chart has a removable common factor at C=0 mod13; cancellation must first be authenticated as a rational identity. A singular reduction is not automatically a globally singular fiber.

Exact rational escape scope: preserve all rational coordinates and surface residuals, verify rationality/anti-invariance, reduce the genuine output, and prove compositeness of its squarefree kernel by two or more exact odd prime valuations. No full factorization or exact rank is promised. No analytic L-value, prescribed-prime existence, semigroup surjectivity, or full BSD conclusion follows.

Use the existing Node/TypeScript and Python/SymPy installations, no new packages or spending. Run lint/typecheck/tests and a separately formulated Wolfram check. The reviews are self-review and implementation cross-checks, not expert or formal verification.
