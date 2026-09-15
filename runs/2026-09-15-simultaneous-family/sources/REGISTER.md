# H10 source and implication record

Checked 2026-09-15. Original target: rank equality for all elliptic curves/Q; this run's new conclusion is only a rational-rank lower bound on a selected infinite family. Current CMI problem page was opened during this run and still labels BSD unresolved. No publication or prize action was attempted.

## [Z] Applicable established descent input

Shenxing Zhang, *On non-congruent numbers with 8a ± 1 type odd prime factors and tame kernels*, arXiv:2111.11618v1, submitted23 November2021; internal manuscript date24 November2021.
https://arxiv.org/pdf/2111.11618v1

Exact places: Section2.1, printed pages3-4; full Kummer triples immediately after equation(2.1); equations(2.2)-(2.5) for the odd Monsky matrix, and(2.8) for its pure dimension. Page2 also states the point/Selmer/Sha exact sequence. The source recalls Monsky's established theorem; its original appendix is not independently reconstructed here.

Dictionary: source curve E_n is y^2=x^3-n^2x with n positive squarefree. Coordinates are (x-n,x+n,x); the source torsion images are (2,2n,n),(-n,n,-1),(-2n,2,-n). Our n is proved positive odd squarefree with all prime factors1 mod8. Thus both source diagonal matrices D_2,D_{-2} vanish. Its M_n becomes diag(A,A), and its displayed s_2=rank+dim Sha[2] gives the conditional exact-rank criterion used in H10. No statement about analytic rank is imported.

Authentication: exact-version parsed PDF text, header, formulas and surrounding definitions inspected. Repeated screenshot requests for the exact-version page4 failed with cache-miss/internal-error responses; no unseen screenshot is claimed checked. The formula is explicit in parsed text and agrees with the previously pinned H8/H9 convention. No new PDF binary copy retained in this run.

## [RS] Related construction and a rejected specialization bridge

Karl Rubin and Alice Silverberg, *Rank frequencies for quadratic twists of elliptic curves*, arXiv:math/0010056v3,4 June2001.
https://arxiv.org/pdf/math/0010056

Corollary3.3, printed page5, was read in text and screenshot. It gives g(u)=-ab(u^2+b^2)(u^4+2b^2u^2-a^2bu^2+b^4) and explicit independent points for the chosen twist. The immediately preceding Theorem3.1 has an endomorphism-ring exception; it is not blindly applied to j=1728. The printed nonsingularity condition in Corollary3.3 appears in the source as b^2!=4a; we do not silently change that quotation into a different theorem. Our only numerical specialization is a=3,b=2, which satisfies that printed inequality and the actual discriminant condition a^2!=4b. The calculation producing -6(u^2+4)(u^2-2)(u^2-8) and its odd valuation at3 is elementary and is proved in H10. Its noncoverage does not disprove or contradict the source theorem.

Source role: contextual known rank-two families and motivation for a tested, rejected bridge. It is NOT the premise proving every member of the H10 degree-eight family has independent points. The two constructions have not been claimed identical.

## [HH] Adjacent literature, not a proof input

Lorenz Halbeisen and Norbert Hungerbuhler, *Congruent Number Elliptic Curves with Rank at Least Two*, arXiv:1809.02037v2,12 October2018.
https://arxiv.org/pdf/1809.02037

The paper supplies constructive families of congruent-number curves of rank at least two. Its discussed relation m^2=n^2+nl+l^2 was not identified with D(a,b). This is context showing that the broad goal of constructing rank-two subfamilies is already known, not a certificate for our exact polynomial or an assertion of disjoint novelty.

## Further inspected foundation/context

J.S. Milne, *Elliptic Curves*, second edition2021, author PDF https://www.jmilne.org/math/Books/EC2.pdf. Standard elliptic-curve foundations used in H8/H9 are unchanged. The Fermat note around printed page106 is historical context; H10 writes its own complete elementary square-area descent instead of relying on that note as a proof.

The elementary prime-divisor lemma and its simple-root lifting application are likewise written out. No appeal to squarefree-value conjectures, Faltings, a specialization theorem with an unexamined exceptional set, or a conjectural prime-values assertion is needed.

## Discovery/novelty boundary

Search queries included "congruent" "56" "1296", "elliptic" "-56" "1296", "congruent numbers" "1296", "congruent" "a^8" "56", and "rank two" "1296", plus rank-two quadratic-twist terminology. Rubin–Silverberg and Halbeisen–Hungerbuhler were inspected as primary adjacent sources. The bounded search did not establish an exact published match for D=a^8-56a^4b^4+1296b^8, but this is NOT evidence of mathematical novelty. No exhaustive citation-chain or independent novelty review occurred. Consensus was already known to be at its monthly quota and was not repeatedly called or upgraded.

Classification: explicit self-derived construction using known descent; overlap with broad known rank-two constructions; no novelty claim. The source-dependent upper bound is an application of an established theorem, while analytic BSD and coverage of arbitrary prime targets remain unproved.
