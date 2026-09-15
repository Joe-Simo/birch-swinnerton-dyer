# H9 source/dependency audit — September 15, 2026

## M: J. S. Milne, Elliptic Curves, second edition

Author-hosted PDF: https://www.jmilne.org/math/Books/EC2.pdf . Title/copyright
pages identify the second edition, World Scientific, 2021. The fetched online
PDF has 241 physical pages; locators below use its printed numbering, not an
assumed pagination of the bound edition. No complete proof of this book is
claimed independently reconstructed.

* I.4.18-4.19, printed p.38 (physical page 43): passage between function fields
  and maps of smooth projective curves, and extension from open subsets.
  For constant maps use ordinary K-points; do not apply the field-embedding
  formulation, which concerns dominant maps, to a constant map.
* II.1.5-1.8, printed p.49 (physical page 54): an origin-preserving nonconstant
  map is a group homomorphism; factorization when one kernel is contained in
  another. The page and its diagram were inspected with a PDF screenshot.
  H9 subtracts the value at a chosen geometric origin before using this result.
* II.6.2, printed p.70 (physical page 75): each endomorphism satisfies a
  monic integral quadratic equation. Parsed text and screenshot were checked;
  this supplies the integrality step in H9 Lemma 2.
* II.6.9, printed p.73 (physical page 78): the endomorphism algebra is Q, an
  imaginary quadratic field, or a quaternion algebra, with the quaternion case
  excluded in characteristic zero. Statement and proof were inspected, also
  by screenshot. H9's explicit [i], integrality, and Galois-fixed-ring argument
  specialize this to End_Q(t)(E)=Z. The text does not itself assert H9's generic
  one-witness theorem.
* V.1, printed p.181 (physical page 186): Riemann--Hurwitz for finite maps
  of compact Riemann surfaces, including the degree-two elliptic example.
  Parsed text and screenshot checked. All curves and maps needed here are over
  characteristic-zero finitely generated fields that embed in C; base change
  preserves degree, genus, and ramification, so this supplies the geometric
  genus and no-P1-to-genus-one arguments.
* IV.1, printed p.108 (physical page 113): restriction and corestriction;
  Cor Res equals the subgroup index. Statement inspected by screenshot.
  This is applied to continuous Galois cohomology of a finite extension;
  H9 has characteristic zero and order-two classes.
* IV.2, equation (28), printed p.112 (physical page 117), gives Kummer
  exactness, displayed there over Q. The SAME exact sequence for a perfect
  field k is explicitly restated at IV.7, printed p.135 (physical page 140).
  Thus the use at k=Q(t) is supported, not a silent number-field extrapolation.
* IV.7.6-7.8, printed pp.137-138 (physical pages 142-143): torsors are trivial
  exactly when they have a rational point; their classification by H^1 with
  the explicit cocycle and descent proof. Parsed text read, including the
  cocycle change of origin. Screenshot of physical page 142 failed; no visual
  check of that page is claimed.

Important convention check: IV.7.5's word 'morphism' means E-equivariant
morphism of torsors. H9 does not infer that every curve map is an isomorphism.
It separately proves [D]=phi_*[C] for arbitrary nonconstant curve maps, using
II.1.5 and the explicit Galois cocycle calculation.

A direct container download of the author PDF failed; web access and the
listed screenshots succeeded. No local PDF or content hash is claimed and
no publisher PDF is redistributed. The unchanged primary URL, edition and
exact locators record the source used.

## Z: the existing full two-descent coordinate convention

Shenxing Zhang, On non-congruent numbers with 8a +/- 1 type odd prime factors
and tame kernels, arXiv:2111.11618v1 (November 23, 2021), Section 2.1,
equation (2.1) and the first paragraph of printed p.4.
https://arxiv.org/pdf/2111.11618v1 . Exact-version parsed text was read. Its
screenshot calls failed, while unversioned https://arxiv.org/pdf/2111.11618
successfully rendered printed pp.3-4; the formulas agree with the parsed
version and H8's pinned source record.

This source supplies the full Kummer ordering (x-n,x+n,x), the three special
torsion triples, and the explicit intersections of quadrics. Its Selmer and
Monsky discussion is about rational curves. H9 does not assert its Selmer
formula over Q(t). Instead H9 uses the algebraic split-two-descent
construction (adjoining square roots of the three divisor functions), proves
the degree-four map has full two-torsion kernel, and uses Kummer exactness
over a perfect field as in M. No BSD or Sha-finiteness input occurs.

## Prior local evidence

H8 CHECKPOINT.md and witness data are copied from the supplied H8 archive;
the full expanded local RESEARCH.md was read. H3-H7 are prior corrected
research, not the superseded initial first-isogeny computations. No additional
claim about their analytic outputs is needed to prove H9. The H8 E41 point is
used only as an exact arithmetic test fixture; no new rank is inferred from it.

## Literature scope and outcome classification

Queries used 'elliptic curves morphism translation isogeny', 'genus one torsor
map cohomology class', 'rational map between torsors endomorphism period', and
'quadratic twists rank one function field'. Most discovery hits were generic,
secondary, or unrelated. They are not proof inputs. The checked primary
source is Milne's author text, plus the already-fixed Zhang convention.

The generic obstruction is classified as a formal consequence of standard
morphism and torsor theory, with a project-specific application and explicit
quadratic map. There is no global novelty claim and no claim that a known
statement elsewhere was absent. Consensus's previously observed allowance
limit was not bypassed; no external paid or private source was used.
