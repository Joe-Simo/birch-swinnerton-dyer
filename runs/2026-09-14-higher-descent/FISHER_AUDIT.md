# We have not solved the Birch–Swinnerton-Dyer problem yet.

## Fisher higher-descent audit — 2026-09-14

Purpose: continue the E_113 4-to-8 descent without using BSD or the previously used analytic rank-zero theorem as the algebraic certificate.

Primary source inspected: Tom Fisher, *Higher descents on an elliptic curve with a rational 2-torsion point*, arXiv:1509.03234v1 (10 Sep 2015), especially Sections 1–3, Theorems 7.2–7.4, and Section 9. Peer-reviewed metadata: Math. Comp. 86 (2017), 2493–2518.

### What the source establishes

1. Selmer elements are everywhere locally soluble n-coverings. For the map alpha from an n^2-Selmer group to the n-Selmer group, Im(alpha) is the kernel of the Cassels–Tate pairing. Thus a second descent computes the fibre above a covering; an empty fibre proves the original covering has no rational point.

2. Fisher defines descending subspaces S_m. Theorem 2.1 gives higher pairings whose kernels are exactly S_{m+1}; Lemma 2.2 identifies the resulting bound with ordinary p^n-descent. With full rational 2-torsion, the method reaches the bound obtained by 8-descent.

3. A required next-stage covering is not obtained by simply adjoining square roots of the old first-stage functions. Theorem 7.2 constructs a nonsingular quadric intersection D from parametrisations of two conics; Theorem 7.3 proves D -> C is the required dual-2-isogeny covering. Theorem 7.4 identifies the divisor H-H^dagger with the nontrivial rational 2-torsion class on Pic^0(D). This confirms the previous checkpoint's warning that genuinely new divisor/pushout data on the higher covering are required.

4. Section 9 replaces conic solving over quadratic extensions with solving a quadric surface over Q. It requires companion quadric intersections and an explicit coordinate change between their 2-uple embeddings. The construction iterates C1,C2,C3,C4. Fisher explicitly notes that the method as presented reaches a 4-covering C4; a further 2-cover of C4 (an 8-covering of E) requires solving conics over a degree-4 field or using the separate explicit 8-descent machinery.

### Consequence for E_113

The prior global endpoint says the second pure pairing for E_113 has rank two and hence the nontrivial pure Sel_2 classes do not survive to the 8-level. That endpoint is useful as a non-circular expected output only because it was derived from a separate established rank-zero theorem. It is NOT the desired independent algebraic certificate.

A direct certificate must therefore contain, for at least a basis of the surviving Sel_4 fibre:

- an explicit locally soluble 4-covering C (intersection of two quadrics), with its map to the lower covering/elliptic curve checked algebraically;
- the companion intersection C^dagger and the coordinate change between the 2-uple embeddings;
- the rank-3 quadrics/conics Gamma_i, with exact rational or quadratic-field points where required;
- the resulting new pushout forms and divisors on C, not pullbacks of old functions;
- local points at every relevant place and exact Hilbert-symbol products, or equivalently an exact proof that the next fibre is empty/nonempty;
- a final identification of the computed higher pairing kernel with the image of Sel_8 -> Sel_4.

### Current blocker and next executable calculation

The repository contains the abstract Selmer/Kummer data and the theorem-derived group endpoint, but it does not yet contain explicit equations for an E_113 4-covering C or its companion C^dagger. Fisher's construction needs those equations before the conics Gamma_i and new pushout functions are defined. Guessing them from the old 2-covering functions would be invalid and was already disproved by the endpoint.

The next mathematical task is therefore narrowed to **constructing an explicit Sel_4 representative above a chosen nonzero pure Sel_2(E_113) class**, in Fisher's quadric-intersection format, and verifying its covering map. Only after that should the Section 7/9 companion-quadric machinery be applied. This is a substantive reduction of the problem, but it is not yet the independent algebraic rank certificate and it has no implication for universal BSD by itself.

No complete solution, counterexample, publication, prize claim, or expert/formal verification is asserted.