# H5 contract: persistent towers and rational-point extraction

Target: continue H4's unresolved persistent-descent implication for E_p: y^2=x^3-p^2 x, p prime congruent to 1 modulo 8. General BSD rank equality remains the objective. No complete candidate exists.

New route beyond H4's same-order observation: retain the entire inverse system of full 2-power Selmer groups, reduction and coefficient-inclusion maps, and rational 2-torsion. Derive its normal form using the pro-Selmer exact sequence. Separately audit whether all-prime finite etale descent or the Brauer-Manin obstruction supplies an independent condition. Do not assert any actual curve has nonzero divisible Sha.

Point-extraction attempt: test whether compatible finite rational Kummer representatives have a uniformly bounded height. Candidate discriminating example is E_41 and P=(-9,120), with the formal 2-adic division P/3. First test non-3-divisibility by enumerating E_41(F_q) and the tripling image for q=3,5,7,11,13,17,19,23,29,31 (good primes only). Stop once a modular certificate is found. This is a search for a finite certificate, not an exhaustive search for rational points.

Accepted finite checks to implement: exact finite-field group law at the chosen certificate prime; fixed torsion checks at 3 and 5; independent exact residue formula a_m=(1-(-2)^m)/3 and compatibility for m=1..64; exhaustive nearest representative check for m<=10 in Z/(2^m); finitely many exact rational multiples P for m<=4. Check normalized abstract towers with r=0,1,2 and total corank two through m=1..4, identifying transition maps and the different marked Kummer subgroups. The abstract r=0,1 objects are not claimed arithmetic realizations.

Proof obligations: all-depth inverse limit exactness and natural maps; exact dependence on H4's persistent Sha classification; torsion subtleties (odd rational torsion invisible to the 2-adic completion); bounded-height criterion via Northcott; a global height-escape bound for all rational representatives, not only the cyclic subgroup. External inputs are to be verified in primary sources. No numerical L-values or estimated canonical heights as certificates.

Preserve existing BSD files and append new durable evidence in this run directory only. Re-run relevant archived H4 checkers, then new TypeScript lint/typecheck/tests and separate Python exact checks. Wolfram is an implementation cross-check, not an independent expert or proof assistant. No spending, publication or force push.
