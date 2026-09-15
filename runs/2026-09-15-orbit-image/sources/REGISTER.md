# H13 source and application audit — 2026-09-15

The existing H12 source register and H11 finiteness entry were inspected first. The sources below were then checked directly online. This is theorem extraction and application checking, not independent reconstruction of the authors' complete proofs. No third-party PDF is redistributed. No novelty search conclusion is claimed. Consensus was not called again after its previously observed monthly exhaustion.

## [B] Finiteness, primary proof and correction

Enrico Bombieri, The Mordell conjecture revisited, Annali della Scuola Normale Superiore di Pisa, Ser.4,17(1990),615–640.
https://www.numdam.org/item/ASNSP_1990_4_17_4_615_0.pdf

Errata-Corrige, Ser.4,18(1991),473.
https://www.numdam.org/item/ASNSP_1991_4_18_3_473_0.pdf

The finiteness statement on printed615 and the separation from effective height bounds on616 were read in parsed text and screenshots (PDF pages1,2). The erratum was read in parsed text; its screenshot failed with a cache-miss error. The erratum enlarges an exceptional set and discusses the degree-one-divisor issue, without changing the finiteness theorem applied here. H13's internally verified branch calculation gives smooth projective geometrically integral genus-five curves over Q. For any such curve with a rational point, that point supplies a degree-one divisor; if empty, finiteness is immediate. No uniformity in n or bound for rational-point heights is imported.

## [M] Morphisms and multiplication

J. S. Milne, Abelian Varieties, v2.00, cover March16/revision entry March17,2008.
https://www.jmilne.org/math/CourseNotes/AV.pdf

I.3.2 and I.3.7 supply extension and homomorphism-plus-translation for rational maps to abelian varieties; I.3.7 was visually read on PDF page24, printed19. I.7.2, PDF page38, states multiplication by m has degree m^(2g) and is étale in characteristic zero. H13 proves its divisor-law formula before applying this to genus one and m=3. The quotient rho is checked explicitly and has degree two; it is not confused with an origin-preserving homomorphism before translating rho(P0) to zero.

## [RH] Riemann–Hurwitz

The Stacks Project, Section53.12, tag0C1B, especially Lemmas53.12.2/53.12.4 and the characteristic-zero formula.
https://stacks.math.columbia.edu/tag/0C1B

Read directly in full HTML. Use over the algebraic closure of Q for geometric ramification and genus: all residue degrees are then one, covers are separable, and ramification is tame. H13 separately counts all odd zero/pole orders and establishes geometric connectedness. The resulting genera are5 and1+4·9^j; the source does not state those particular applications.

## [S] Good reduction and torsion

Joseph H. Silverman, An Introduction to the Theory of Elliptic Curves, Wyoming2006 author exposition.
https://www.math.brown.edu/~jhs/Presentations/WyomingEllipticCurve.pdf

PDF page72, printed64, explicitly states that rational N-torsion injects on good reduction when gcd(N,p)=1. The exact statement was read in parsed text. H13 verifies good reduction at13 and19 on its displayed rational model and handles13- and19-primary torsion separately, using the other prime in each case. No analytic rank field, conjectural saturation bound or BSD implication is used.

## Current target and scope

CMI's current BSD page was checked; it still labels the problem Unsolved.
https://www.claymath.org/millennium/birch-and-swinnerton-dyer-conjecture/

No prize submission or eligibility decision is being made. The working target is the rank equality for every E/Q in the inherited complete project prompt, not merely construction of rank-at-least-two families. The source-driven H13 finiteness argument is partial research toward the prescribed-prime obstruction, not a resolution.

## Internal references

H12, parent ac5bb862d273db89512db7173bdd9384536324df: translated Kummer involution, osculating map and137 seed. Its current remote CHECKPOINT.md and local full RESEARCH.md were read. The seed/output geometry is recomputed here. The raw Kummer minor and both generic quartic-to-elliptic identities are rechecked, while the standard Kummer-kernel theorem remains the previously authenticated descent input. H8's positive-rank certificates for257,313 are context for explaining the local obstruction; their validity is not needed to prove that this fixed fiber excludes those squareclasses.
