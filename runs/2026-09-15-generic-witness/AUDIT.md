# H9 self-review — generic construction mechanism

**Normalized claim:** for K=Q(t), E:y^2=x^3-t^2x and the two explicitly
specified genus-one coverings, E(K(X_epsilon))=Z*pi(generic point) plus E[2](K).
The complementary covering has no point over this field or a finite odd-degree
extension, but has index two and the explicit K(i)-companion has trace zero.

**Verdict: proved as written**, using the standard external curve/cohomology
results listed in sources/REGISTER.md. This verdict is a self-review, not an
independent referee or formal proof. It applies to this generic statement,
not to a universal statement about arithmetic specialization or BSD.

## Dependency graph

- Smooth quartic/quadric geometry -> genus one, degree-four map, V4 deck group.
- Genus-one map -> Jacobian isogeny; V4 kernel -> kernel J[2] -> unique
  K-isomorphism J to E through which the linear map becomes multiplication by2.
- Twist trivialization + Riemann--Hurwitz + descent -> E(K)=E[2](K).
- Explicit i automorphism + characteristic-zero endomorphism classification,
  integrality and Galois invariants -> End_K(E)=Z.
- Exact Kummer sequence + actual torsion triples + four independent rows ->
  two independent order-two classes in H^1(K,E).
- Origin-preserving morphism theorem + cocycle equivariance -> [D]=phi_*[C].
- End_K=Z and those classes -> no map between coverings; maps to E are [m]pi+T.
- Restriction/corestriction -> odd-degree nonexistence.
- Explicit z -> iz isomorphism -> quadratic splitting; conjugation -> trace zero.

## Obligation review

| Obligation | Outcome and reason |
|---|---|
| Keep the original problem over Q separate from K | Passed: RESEARCH §§1,8 explicitly limit the mechanism tested. |
| No hidden analytic or Sha-finiteness premise | Passed: neither theorem occurs in the proof dependencies. |
| Degree-four map versus four-covering confusion | Passed: the map has degree4 and linear part[2], not[4]. |
| Smoothness and geometric integrality | Passed: squarefree quartic plus its inverse parametrization; gradient check covers projective boundary. |
| Constant maps with no rational origin | Passed: geometric integrality makes constants descend to K; a constant map to the target would supply a K-point. |
| Actual torsor classes, not merely different triples | Passed: quotient by all E(K)/2 is explicitly computed via the two torsion rows. |
| Number-field formula over K | Passed: only split divisor square-root construction and perfect-field Kummer exactness are used; no Monsky formula over K. |
| Torsor-equivariant versus arbitrary maps | Passed: cocycle proof handles induced Jacobian isogeny; Milne IV.7.5 is not applied to arbitrary curve maps. |
| Saturated generator in the generic rank claim | Passed: all linear parts are even and pi has part2; difference is one of four K-points. |
| Negative/zero multiplication and torsion | Passed: n=0 is constant; negative n allowed; nonzero multiples of a nonconstant map cannot be torsion. |
| Endomorphism field | Passed: i acts only after adjoining i; fixed endomorphism ring is Z. |
| Odd-degree extension scope | Passed: applies to points on the complementary torsor, not all new points of E over odd-degree fields. |
| Sharp quadratic exception | Passed: geometric integrality ensures i is not in the input field; projective companion map supplies degree2 point. |
| Trace cancellation | Passed for the explicit CM-generated point and its CM multiples; not asserted for every possible quadratic point. |
| Seven rank-two fibers | Passed: no claim that generic rank stays unchanged on specialization. |
| Generic formulas versus arithmetic algorithms | Passed: arithmetic specialization/persistence can introduce information outside a fixed rational map. |
| Computational proof scope | Passed: identities and 16 fixed rational group operations are checked, not universal quantifiers by finite enumeration. |
| All-prime rational construction / full BSD | Not addressed; the prime-specific existence argument remains missing. |

## Cheapest decisive checks and boundary examples

The determinant-one Kummer minor is the decisive finite algebra check. For the
no-map theorem, the decisive geometric check is not a sampled formula: the
cocycle condition requires alpha_other=n*alpha_input, impossible in their
rank-two span. Adjoining i deliberately tests the degree restriction and
produces a genuine map, so the obstruction cannot be overextended to all
algebraic constructions. The E41 arithmetic fixture verifies that actual
multiplication and torsion translation respect the claimed Kummer span.

All test commands and versions are recorded in results/checks.log and
results/verification-summary.json. The proof's universal content remains the
written argument using the named external foundations. No novel theorem or
independent expert/formal verification is claimed.
