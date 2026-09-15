# H10 supplementary primary-source record

Checked2026-09-15; exact auxiliary prime classification, not a general BSD implication.

## [FI] Exact auxiliary isogeny-rank input

Tom Fisher, *Higher descents on an elliptic curve with a rational 2-torsion point*, arXiv:1509.03234v1,10 September2015. https://arxiv.org/pdf/1509.03234v1 . Section2, physical page4/printed4, supplies the quotient-rank formula; Section5, physical page11/printed11, supplies the x-coordinate connecting map and quartic equation(8). Apply with(a,b)=(2,-3), target coefficients(-4,16). Our proof determines rational connecting images, not guessed Selmer dimensions, and uses the two rational kernels of order2. Page11 was successfully screenshotted; repeated page4 screenshots returned internal errors, so the rank formula was authenticated from parsed text instead. The all-Q2 exclusion is proved in PRIME_FILTER.md and not imported as a theorem.

## [FQ] Quartic invariant cross-check, not a required completeness premise

Tom Fisher, *On binary quartics and the Cassels–Tate pairing*, Research in Number Theory8, article74(2022), published28 September2022, DOI10.1007/s40993-022-00376-z. https://link.springer.com/article/10.1007/s40993-022-00376-z . The full primary HTML article was opened. Section2 defines I,J and equation(2) gives the Jacobian y^2=x^3-27Ix-27J. For g=t^4-4t^3+8t^2-24t+36, I=208,J=-4480. Scaling(x,y)=(36X+24,216Y) gives E0. The article's binary-model discriminant has an extra factor16 relative to the univariate polynomial discriminant; the proof keeps these conventions separate. This is only an independent normalization check: our explicit map and inverse already compare the curves directly.

## [M] Exact auxiliary torsion-reduction input

J.S. Milne, *Elliptic Curves*, second edition2021, https://www.jmilne.org/math/Books/EC2.pdf . ChapterII Corollary4.2, printed page64/physical page69, proves the good-reduction isomorphism on torsion prime to the residue characteristic; its page was successfully screenshotted. At5 and7 our exact field counts are8, bounding every rational torsion primary component. ChapterIV Theorem7.19 and7.6 were also read as genus-one context, but the affine completeness proof uses explicit maps and does not need to guess a birational isomorphism from equal invariants. The standard Mordell-Weil theorem underlying the rank formula is unchanged.

The auxiliary curve computation is a self-derived application of these established inputs. No novelty or general-BSD conclusion is drawn. Its full rational classification shows that the H10 infinite family cannot furnish a new prime kernel beyond41.
