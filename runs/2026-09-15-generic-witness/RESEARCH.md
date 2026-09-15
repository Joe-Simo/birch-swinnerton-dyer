# We have not solved the Birch–Swinnerton-Dyer problem yet.

## H9 — the generic one-witness obstruction and its quadratic escape

Continuation of H8, private branch `research/h2-endpoint-20260914`, pinned parent
`f04f51a515f786e1e842f6a30208b17c0814ea59`. Work is confined to the assigned
Birch–Swinnerton-Dyer folder and repository. No earlier mathematical record is
changed. This record tests a proposed construction mechanism; it does not
substitute BSD over a function field for the original problem over Q.

**Outcome.** A rational formula valid for the generic family cannot manufacture
H8's second covering witness from its first. In fact we compute the whole group
of points rational over the function field of either covering: it has rank
exactly one. The complementary covering still has no point after any finite
odd-degree extension. The degree restriction is sharp: adjoining i supplies an
explicit companion point, but its elliptic-curve image has trace zero, not a new
rational point.

These are self-reviewed consequences of standard curve, endomorphism and
Galois-cohomology facts, with the needed argument written below. No novelty,
independent expert verification, formal-kernel proof, new BSD case, or
counterexample to BSD is claimed. In particular the seven H8 rank-two fibers
remain rank two: their specialization does not contradict a generic rank-one
statement.

### 1. Exact question and conventions

Put K=Q(t), with t transcendental, and

    E/K: y^2=x^3-t^2*x, origin O at infinity.

Its discriminant is 64*t^6, nonzero in K. Define the smooth projective curves

    X_minus: v^2-w^2-z^2=0,  u^2-t*w^2+t*z^2=0;
    X_plus:  v^2-w^2+z^2=0,  u^2-t*w^2-t*z^2=0.

For either sign there is a map, written on z != 0,

    pi(u:v:w:z) = (t*w^2/z^2, t*u*v*w/z^3).

Use the fixed Kummer ordering (x-t,x+t,x). These are exactly the algebraic
covering equations used in H8, with its numerical p replaced by an
indeterminate, not an assertion about Selmer groups over K. A uniform rational
formula on a generic witness means a K-rational map of these curves, defined on
a nonempty open subset. No bound on its degree is imposed. This definition
excludes importing a second point as an additional constant, and does not
include arbitrary algorithms that make new arithmetic choices at individual
prime values.

The quartic witness of H8 is birationally the same input: in weighted
coordinates (A:B:c), weights (1,1,2), it is

    t*c^2=A^4+6*epsilon*A^2*B^2+B^4, epsilon in {-1,+1}.

Its map to X_epsilon is

    (u,v,w,z)=(t*c, A^2-epsilon*B^2, A^2+epsilon*B^2, 2*A*B).

On a dense open set A/B=(v+w)/z; the remaining coordinate c is recovered using
the projective scaling. Thus changing from the quadrics to the quartic does not
avoid the obstruction. Keeping an extra scale variable only adjoins a purely
transcendental variable, which also does not create points on a fixed
positive-genus curve.

### 2. Why these are the intended two-coverings over K

The binary quartic A^4+6*epsilon*A^2*B^2+B^4 has four distinct geometric roots
in characteristic zero. For example, in B=1 its derivative is
4*A*(A^2+3*epsilon); neither A=0 nor A^2=-3*epsilon is a root of the quartic.
Its double cover of P1 is geometrically integral and has genus one by
Riemann–Hurwitz. The conic parametrization above gives the stated projective
models. Direct gradient dependence gives another smoothness check: if a,b are
not both zero, dependence of the quadric gradients forces

    b*u=a*v=(a+b*t)*w=(a-b*t)*z=0.

Since t != 0, at most one coordinate can then be nonzero; neither pair of
quadrics admits such a point. The Hessian determinant, with the signs as above,
is -16*epsilon*a*b*(a^2-t^2*b^2).

The displayed pi satisfies E's equation. In ordinary cubic projective
coordinates it is (t*w^2*z : t*u*v*w : z^3), with no base point on either
covering: at z=0 the quadrics force u,v,w all nonzero. Its generic fiber consists of the
choices of three square roots, subject to their product being fixed, so has
four points. The four deck transformations change an even number of signs
among u,v,w. A nonconstant map between these genus-one curves in characteristic
zero is unramified. With any geometric point over O as origin, pi is an isogeny
with kernel the full two-torsion. Factoring its induced Jacobian isogeny through
multiplication by two identifies the Jacobian with E, over K; pi is therefore
an actual [2]-covering, not a map labeled from its ambient degree.

Under full two-descent their classes in H^1(K,E[2]) are

    lambda_minus=(1,t,t),   lambda_plus=(t,1,t).

One can read these labels directly on the function fields: on X_minus the
three functions (x-t,x+t,x) are respectively (u/z)^2, t*(v/z)^2,
t*(w/z)^2. On X_plus they are t*(v/z)^2, (u/z)^2, t*(w/z)^2.
The split two-descent construction uses the square roots of functions whose
divisors are 2*(T_j)-2*(O); it and the Kummer exact sequence are valid over any
characteristic-zero field. Zhang's formula fixes the coordinate convention;
no number-field local-solubility or Monsky theorem is being extended to K.

### 3. Compute E(K) and its K-endomorphism ring first

**Lemma 1.** E(Q(t))=E[2](Q(t))={O,(0,0),(t,0),(-t,0)}.

Write t=s^2 and pass to Q(s). The change X=x/s^2, Y=y/s^3 identifies E with
E_1: Y^2=X^3-X. Any point of E_1(Q(s)) is a rational map P1 -> E_1, extending
to a morphism because the source is smooth and the target proper. A nonconstant
map is impossible by Riemann–Hurwitz: -2 would equal a nonnegative ramification
sum. Consequently the point is constant and belongs to E_1(Q). This step does
NOT need a rank-zero theorem for E_1.

The involution s -> -s acts on the transformed point by (X,Y) -> (X,-Y),
because the original x,y belong to Q(t). On a constant Q-point it acts
trivially. Therefore that constant point is its own negative, and is
2-torsion. Transforming back proves the lemma.

**Lemma 2.** End_K(E)=Z, though End_K(i)(E)=Z[i].

The explicit automorphism [i](x,y)=(-x,i*y) squares to [-1]. In
characteristic zero the geometric endomorphism algebra of an elliptic curve
is Q or an imaginary quadratic field [M, II.6.9]. Here it contains Q(i), so it
is Q(i). Endomorphisms are algebraic integers [M, II.6.2] (also seen from their
integral action on the complex period lattice). The full geometric ring contains the
maximal order Z[i] and is contained in it, hence equals Z[i]. The formula for
[i] is defined over K(i), and conjugation i -> -i acts on this ring by complex
conjugation. Its fixed ring is precisely Z. All integer multiplication maps
are defined over K. This proves both assertions.

In particular a complex-multiplication operation not defined over Q cannot be
counted as a second rational direction over Q.

### 4. The two torsors really are distinct nonzero classes

The Kummer exact sequence over K gives

    0 -> E(K)/2E(K) -> H^1(K,E[2]) -> H^1(K,E)[2] -> 0.

By Lemma 1 the kernel is generated by the torsion Kummer classes

    kappa(T_plus)=(2,2t,t),   kappa(T_zero)=(-t,t,-1).

The squareclasses -1,2,t are independent in K^*/K^*2: valuation at t=0
excludes an odd power of t, and a rational function whose square is a rational
constant is itself constant; none of -1,2,-2 is a rational square.

In this three-bit basis, separately for each coordinate, the four rows are

    T_plus       0 1 0 | 0 1 1 | 0 0 1
    T_zero       1 0 1 | 0 0 1 | 1 0 0
    lambda_minus 0 0 0 | 0 0 1 | 0 0 1
    lambda_plus  0 0 1 | 0 0 0 | 0 0 1.

Their columns 0,1,2,5 have determinant 1 over the integers. Equivalently, the
first-coordinate sign kills a T_zero coefficient, its 2-valuation kills
T_plus, its t-valuation kills lambda_plus, and the second-coordinate
t-valuation kills lambda_minus. Thus the images

    alpha_minus=[X_minus], alpha_plus=[X_plus] in H^1(K,E)[2]

are independent and nonzero. They have order two. Neither covering has a
K-point. This argument uses the actual torsor classes, not merely the fact
that the displayed full Kummer triples differ.

### 5. The functorial obstruction, including its cocycle proof

Let C,D be genus-one torsors under an elliptic curve E over a characteristic-zero
field k. Any nonconstant k-map f:C->D has, after choosing geometric origins,
the form

    f(c_0+P)=d_0+phi(P)+Q,

where phi is an isogeny of their Jacobians and Q is a geometric point. This is
obtained by subtracting the value at the origin and applying the
origin-preserving morphism theorem [M, II.1.5]. The induced Jacobian map is
defined over k, independently of those origin choices.

Write sigma(c_0)=c_0+a_sigma and sigma(d_0)=d_0+b_sigma. Galois equivariance of
f gives

    phi(a_sigma)+Q = b_sigma+sigma(Q).

Thus b_sigma-phi(a_sigma)=Q-sigma(Q), a coboundary, and

    [D]=phi_*[C] in H^1(k,E).

This is a necessary condition for arbitrary curve maps, not just
E-equivariant maps. We do not misapply Milne's statement that an E-equivariant
torsor morphism is an isomorphism to all curve maps.

Apply this with k=K and C,D the two different X's. Lemma 2 says phi=[n]. Since
alpha_C has order two, n*alpha_C is either zero or alpha_C, never the independent
alpha_D. Nonconstant maps are impossible. A constant K-map would provide a
K-point on D, also impossible. Consequently

    X_minus(K(X_plus))=empty,   X_plus(K(X_minus))=empty.       (1)

Indeed a point over a curve's function field is a rational map from that
curve; it extends to a morphism. Restricting a proposed formula to a smaller
nonempty open set does not evade (1).

### 6. Exact generic rank: the first witness supplies one direction, not two

Let F_epsilon=K(X_epsilon), and let P_epsilon be the generic point's image under
pi_epsilon. Then

    E(F_epsilon) = Z*P_epsilon direct-sum E[2](K).              (2)

To prove this, a point of E(F_epsilon) is a K-map f:X_epsilon->E. Its Jacobian
map is [n]. The cocycle argument, now with the trivial target torsor, says
n*alpha_epsilon=0, so n=2m. The morphism [m]pi_epsilon has the same Jacobian
map. Their difference is constant and defined over K, hence is a point T in
E(K). By Lemma 1 it is 2-torsion. Thus f=[m]pi_epsilon+T.

Conversely all these maps exist. The map pi is nonconstant, so no nonzero
multiple of P_epsilon can be torsion: otherwise a nonconstant map would have
finite image. This proves the direct sum and that P_epsilon is a generator,
not just a finite-index generator. The degree of a nonconstant map in (2) is
4*m^2; m=0 gives exactly the four constant maps.

Modulo two, all rational formulas applied to that one witness lie in the
span of its own lambda class and the two rational torsion classes. They can
never yield the other lambda class. This is an exact all-degree classification,
not a bounded search over formulas.

A separate caution for a fixed rational specialization p: every rational
self-map E_p->E_p is [n]+Q_0, but Q_0 may be an independent rational point.
Such a formula does not construct a new point from nothing if its coefficients
already encode Q_0. Our generic calculation prevents this hidden input because
E(K) has only the four torsion points. We do not claim the rank-one formula
(2) survives every specialization; H8 supplies concrete rank-two fibers.

### 7. Follow-up: odd-degree extensions fail, degree two succeeds

Fix F=K(X_plus), and let eta be the class of X_minus over F. Equation (1) proves
eta != 0, and 2*eta=0. If a finite odd-degree extension L/F supplied a point on
X_minus, its restriction would be zero. But restriction followed by
corestriction is multiplication by [L:F] [M, IV.1, p.108]. Therefore

    0=Cor(Res(eta))=[L:F]*eta=eta,

a contradiction. The same proof works with the signs reversed. No separability
exception occurs in characteristic zero. Geometrically, there is no dominant
correspondence supplying a complementary witness with odd degree over the
input curve.

This is sharp, not an obstruction to all algebraic extensions. Over F(i), the
explicit linear coordinate change

    J:X_plus -> X_minus,  (u:v:w:z) |-> (u:v:w:i*z)            (3)

is an isomorphism, with inverse obtained by -i. Substitution in the quadrics
verifies it, and

    pi_minus(J(P)) = [i]pi_plus(P)=(-x,i*y).                   (4)

Geometric integrality makes F/K a regular function-field extension, so i is
not in F; F(i)/F has degree two. Equations (3)-(4) thus give a genuinely
quadratic complementary witness. Together with odd-degree impossibility,
the complementary torsor has period and index exactly two over F. An
alternative degree-two splitting field is F(sqrt(t)), using the point
(sqrt(t):1:1:0); this boundary point is valid on the projective covering even
though the affine formula for pi has a pole there.

However (4) does not descend a second rational point. For P in E(F), conjugation
sends [i]P to [-i]P, so

    Tr_F(i)/F([i]P)=[i]P+[-i]P=O.                             (5)

For integers a,b, the trace of [a+b*i]P is [2a]P. Adding torsion changes the
trace only by torsion. For non-torsion P, P and [i]P are independent over Z in
the quadratic extension (a nonzero a+b*i is an isogeny with finite kernel),
but the second direction is anti-invariant and disappears under trace. This
explains exactly why invoking CM alone is not the desired rational
rank-two construction.

### 8. What this advances, and what it does not

The proposed route “solve one quartic, then obtain the other through a fixed
rational transformation” is refuted in its generically valid sense. The
stronger odd-degree variant is also refuted. A quadratic construction is
explicitly available, but its natural elliptic trace is zero. The seven H8
certificates are not retracted or enlarged.

This says nothing against arithmetic algorithms that use the particular prime,
new norm equations, a distinct rational point, analytic data, or higher-descent
information not expressible as one generic rational map. A formula valid only
on a special arithmetic subset is not automatically a generic map. In
particular zero Tunnell coefficient and persistent descent are arithmetic
conditions on rational fibers, not hypotheses we have transferred to the
function field. The function-field obstruction is a test of one proof mechanism,
not a counterexample to any rational BSD assertion.

**Next mathematical target:** use the prime-specific persistence information to
construct a second rational direction outside the group generated by the first
witness; do not reuse rational self-maps or the trace of CM multiples as that
construction. The unresolved square conditions, exclusion of divisible Sha,
and uniform analytic-order comparison remain. General elliptic curves over Q
and all ranks are still outside this partial result.

### 9. Verification and preservation

The proof of (1)-(2) and the odd-degree obstruction is geometric/cohomological;
no finite computation proves their quantifiers. The companion checkers verify
the generic covering and quartic polynomial identities, their smoothness
polynomials, the four Kummer rows and their spans, the explicit quadratic map,
and the trace cancellation. Exact rational arithmetic on the existing E41
witness checks that multiplication and torsion translation really stay in the
predicted Kummer span. These are small, focused consistency checks, not a new
scan or independent mathematical discoveries.

The completed runs passed 36 TypeScript assertions and 71 Python/SymPy
assertions. A separately written Wolfram invocation returned all expected
zero residuals, squarefree gcds equal to one, rank four and determinant one.
Its initial uppercase-symbol variant emitted warnings; that input and output
are preserved, and the renamed rerun returned the same values without warnings.

See CONTRACT.md, sources/REGISTER.md and results/verification-summary.json for
execution scope, actual outcomes and source limitations. This is self-review;
Wolfram is a separately written algebraic cross-check, not an independent
researcher or a formal proof kernel. All preexisting file hashes are retained
in inputs/preserved-files.json and checked before delivery. No paid service,
publication, external contact or background process is involved.
