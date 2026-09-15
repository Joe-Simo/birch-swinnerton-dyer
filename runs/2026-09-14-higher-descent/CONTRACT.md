# Higher-descent continuation: registered experiment

Status: no complete BSD candidate. Existing checkpoint 001 and archived inputs are preserved.
Target is unchanged: ord_(s=1)L(E,s)=rank E(Q) for every elliptic curve over Q.

Specific question: reconstruct an algebraic obstruction beyond the identical Sel2/Sel4
coarse data of E41 and E113. Start from the Sel4-by-Sel2 Cassels–Tate pairing,
using Fisher's rational-2-isogeny factorization (arXiv:1509.03234v1, Sections 2–5)
to produce explicit covering curves and pushout functions. This is not a claim
that matching the known rank-zero answer proves BSD, and no analytic rank is used
to certify an algebraic obstruction.

Models: E_p:y^2=x^3-p^2 x; quotient by (0,0) is E'_p:y^2=x^3+4p^2 x.
Both are nonsingular; the standard 2-isogeny and its dual will be recorded.
Investigate only p=113, with p=41 as a possible rational-point control.

Initial covering construction for target E'_113, square class xi1=2:
C1: r^2=2s^4+2*113^2*t^4.
Conic parametrization f=113*(-l^2+2lm+m^2), g=l^2+2lm-m^2,
h=226*(l^2+m^2); verify 2f^2+2*113^2*g^2=h^2 exactly.
Attempt xi2=xi3=1 first; prove local solubility rather than assume it.
Use 113=2*9^2-7^2 to parametrize f=s^2 and the standard norm parametrization
for g=t^2. The resulting C3 is an intersection of two quadrics in P3.
Find a rational point on the required conic over Q(sqrt(2)), then compute its
norm-tangent pushout form and verify it by exact polynomial identities.

Arithmetic: exact Python integers/Fractions and SymPy symbolic polynomials;
TypeScript bigint or independently supplied Wolfram checks for decisive results.
A finite point search is discovery only, never evidence of nonexistence.
All local computations must include an exact Hensel argument, a proved exhaustive
residue test, or a cited applicable good-reduction lemma. A modular point by itself
is not a local-solubility certificate. Do not infer a higher Sha order from its
predicted refined BSD value. Bound individual searches and preserve failures.

## Executed revision after the first twist failed

The xi2=1 intermediate covering has no primitive solution modulo 16; this is
an exhaustive local obstruction, not failure of the overall route. Switched to
xi2=2, xi3=1 and obtained the explicit intersection of quadrics in RESEARCH.md.
A supplied-certificate checker (rather than the discovery search) verifies its
identities, norm-tangent pushout, finite local witnesses and all-place coverage
inputs. The local coverage proof uses Hasse–Weil and degree bounds at all primes
q>=23 other than 113. Success criterion is a nonzero Theta3 pairing on the full
two-dimensional S3, using no analytic rank. Consequences for rank, Sha exponent
and Sel8 must follow the written exact sequences and pairing argument, not an
extrapolation from group orders. The E41 comparison reuses its earlier algebraic
rank-two certificate and is not a claim to have computed its exact analytic order.
