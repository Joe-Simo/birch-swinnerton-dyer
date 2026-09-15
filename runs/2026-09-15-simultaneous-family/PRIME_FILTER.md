# We have not solved the Birch–Swinnerton-Dyer problem yet.

## H10 follow-up — the only prime squarefree kernel is 41

**Statement.** For coprime nonzero integers a,b, let n be the positive squarefree kernel of D=a^8-56a^4b^4+1296b^8. Then n is prime if and only if a/b belongs to {2,3,-2,-3}; in every such case n=41. This is a restriction on this particular simultaneous-witness family, not on congruent-number curves in general. Together with the core construction, it gives infinitely many distinct composite kernels with rational rank at least two, but no new prime kernels beyond41.

This follow-up was chosen after Section7 of RESEARCH.md produced an auxiliary genus-one curve. It uses no analytic rank computation or BSD conjecture. The proofs below and the core factor-gcd proof are necessary; a list of small rational points is not a completeness argument.

### 1. Reduction to a fixed quartic

The core record proved D=F_minus*F_plus, with

    F_e=a^4+4e*a^3*b+8a^2b^2+24e*a*b^3+36b^4,
    gcd(F_minus,F_plus)=c^2,
    c=2^{[2 divides a]}*3^{[3 divides a]}.

Both normalized factors G_e=F_e/c^2 are positive coprime integers. If n is prime, exactly one of their squarefree kernels is1, so one G_e is an integer square. Because c^2 is itself a square, the corresponding F_e is a square as well. Conversely this condition alone would not imply a prime n.

Put t=a/b. For F_minus, the necessary condition is a rational point on

    C: w^2=g(t)=t^4-4t^3+8t^2-24t+36.                       (P1)

For F_plus it is the same condition with t replaced by -t. There is no search cutoff in this reduction.

### 2. Exact rational map, with inverse and exceptional fibres

Define

    X=(w+t^2-2t)/2,
    Y=(X+1)(t-1)-2.                                        (P2)

Direct expansion gives

    Y^2-X(X-1)(X+3)
       =-(t^2-2t+w+2)*(w^2-g(t))/8.                        (P3)

Every affine rational point of C therefore maps to the nonsingular curve

    E0: Y^2=X(X-1)(X+3)=X^3+2X^2-3X.

For X != -1 the inverse formulas are

    t=1+(Y+2)/(X+1),
    w=2X+1-((Y+2)/(X+1))^2.                               (P4)

Both compositions are identities on their domains. Substituting (P4) into w^2-g(t) gives -4*(Y^2-X(X-1)(X+3))/(X+1), so the inverse is checked directly, not inferred solely from matching j-invariants.

At X=-1, (P2) implies w=-(t^2-2t+2). Since

    g(t)=(t^2-2t+2)^2+16(2-t),

equation(P1) forces t=2,w=-2, and then Y=-2. Thus there is exactly one affine point in this exceptional fibre. The point(-1,2) of E0 has no affine preimage. Neither does its point at infinity. These facts avoid silently counting exceptional points through a birational map.

As a separate invariant check, not a needed completeness premise, the binary quartic has I=208,J=-4480 in [FQ, Section2]. The standard Jacobian y^2=x^3-27Ix-27J becomes E0 under x=36X+24,y=216Y. The polynomial discriminant of g is2^16*3^2; [FQ]'s binary-model discriminant convention is16 times this, not the same number. Both are nonzero.

### 3. Algebraic rank-zero proof for E0

The standard 2-isogeny with kernel {O,(0,0)} has target

    E0': V^2=U^3-4U^2+16U.

The connecting squareclass on either target curve is its x-coordinate away from O,(0,0); the special values are1 and the linear coefficient b, respectively. Denote the two injective quotient maps by

    alpha: E0(Q)/phihat E0'(Q) -> Q^*/Q^{*2},
    alpha': E0'(Q)/phi E0(Q) -> Q^*/Q^{*2}.

These conventions, the homogeneous quartic, and the rank formula follow the established isogeny descent in [FI, Sections2 and5], not the obsolete early H2 computations.

Here is the required squareclass support argument. For an integral model y^2=x^3+a*x^2+b*x and a prime q not dividing b, a negative v_q(x) makes x^3 the unique least-valuation term, while a positive v_q(x) makes b*x the unique least-valuation term. The valuation of y^2 is even, so in either case v_q(x) is even. Thus an x squareclass is supported only on the sign and the primes dividing b; the two special values obey the same support rule.

For E0, b=-3, so Im(alpha) is contained in {1,-1,3,-3}. The rational points(-1,2) and(3,6) show that -1 and3 occur, respectively. The image is a subgroup, so it equals all four classes.

For E0', b=16, the possible classes are {1,-1,2,-2}. Since U^2-4U+16=(U-2)^2+12 is strictly positive over R, any real nonkernel point has U>0. The kernel value16 is positive too. Thus negative classes do not occur.

The remaining class2 would require a nonzero rational solution of the quartic

    r^2=2s^4-4s^2t^2+8t^4
       =2(s^4-2s^2t^2+4t^4).                              (P5)

There is no Q_2 point. Use the weighted scaling (r,s,t)->(lambda^2*r,lambda*s,lambda*t) so s,t are 2-adic integers with at least one odd; then r is integral as well. If s is odd, the bracket on the right is odd and the right side has valuation1. If s is even, t is odd and the bracket is4 modulo8, so the right side has valuation3. An exact square cannot have either odd valuation. This proves the exclusion for all Q_2, not just for a finite residue range.

Consequently Im(alpha')={1}. The exact rank formula from [FI] gives

    rank E0(Q)=dim_F2 Im(alpha)+dim_F2 Im(alpha')-1-1
               =2+0-2=0.                                 (P6)

Both isogeny kernels are rational of order2, accounting for the two subtracted ones. No finiteness assertion about Sha is used.

### 4. All rational points, not just some points

The discriminant of the displayed E0 model is2304=2^8*3^2. At the good primes5 and7 direct finite-field enumeration gives

    #E0(F5)=8,  #E0(F7)=8.

Prime-to-reduction-characteristic torsion injects under good reduction [M, II Corollary4.2]. Reduction at5 bounds every primary torsion component except the5-primary one by a group of order8; reduction at7 also excludes5-primary torsion. Hence the rational torsion group has order at most8. This use of two primes does not incorrectly assume injectivity for p-primary torsion at p.

There are already eight distinct rational points:

    O, (0,0), (1,0), (-3,0), (3,6), (3,-6), (-1,2), (-1,-2).

Together with rank zero, they are all of E0(Q). Their existence, field counts and discriminant are exact finite certificates.

Using the inverse(P4) where X!=-1, and including the separately checked exceptional fibre, gives precisely the six affine points

    C(Q)_affine={(0,6),(0,-6),(2,2),(2,-2),(3,3),(3,-3)}.

More explicitly, five E0 points with X!=-1 yield five of them; the exceptional fibre supplies(2,-2). O and(-1,2) have no affine preimage. The smooth projective completion of C adds its two rational points at infinity because its leading coefficient is1. No rational point with any larger denominator is being omitted by a numerical search.

### 5. Prime conclusion and its significance

If F_minus is a square, t is0,2 or3; if F_plus is a square, t is0,-2 or-3. The admitted parameters have a,b nonzero, so t=0 and infinity are excluded. Thus prime n forces

    a/b in {2,3,-2,-3}.

At t=+/-2, primitiveness gives D=656=16*41; at t=+/-3 it gives D=3321=81*41. Each therefore has squarefree kernel41, which is prime. This proves both directions of the stated classification.

The core infinite-family proof survives unchanged, but almost all its distinct kernels must be composite. The tempting interpretation that this construction could provide infinitely many prime cases is now refuted for this exact family. It does not resolve any of the other prime cases, the remaining uniform rational-point argument, the analytic orders of the infinite composite family, or general BSD.

### 6. Audit and computation scope

Evidence class: self-reviewed proof with established isogeny/torsion-reduction inputs, plus exact implementation checks. The supplementary tests verify(P3)-(P4), the Jacobian normalization, the complete claimed eight-point list on E0, the two finite-field orders, and the primitive congruence obstruction modulo16. The latter confirms arithmetic used in the valuation proof; it is not the sole argument for infinite Q_2 coverage. Rational completeness follows from(P6), the torsion bound and the map, not from enumerating rational parameters.

See sources/REGISTER.md for [FI], [FQ] and [M]. No novelty, independent expert review, formal verification, publication or complete BSD claim is made.
