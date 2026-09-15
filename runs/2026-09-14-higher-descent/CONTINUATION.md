# We have not solved the Birch–Swinnerton-Dyer problem yet.

Continuation checkpoint after H2. This file records only what has been established in the current continuation; it does not replace CHECKPOINT.md.

## Executed literature follow-up

The next route in CHECKPOINT.md was checked directly against T. Fisher, *Higher descents on an elliptic curve with a rational 2-torsion point*, Math. Comp. 86 (2017), 2493–2518 (preprint arXiv:1509.03234v1). The source explicitly develops practical 8-descent for elliptic curves over Q with full rational 2-torsion.

The exact generic equations needed for the next construction have now been authenticated from Fisher Section 5, equations (7)–(14). For

    E: y^2 = x(x^2+a x+b), T=(0,0),

and a squareclass xi1 for the 2-isogeny connecting map, the first covering is

    C1: r^2 = xi1*s^4 + a*s^2*t^2 + (b/xi1)*t^4.

After parametrising the conic, Fisher writes

    (s^2:t^2:r)=(f(l,m):g(l,m):h(l,m)),
    f(l,m)=xi2*s^2, g(l,m)=xi2*t^2,

then parametrises those two conics by binary quadratics p_i(c,d), q_i(theta,psi), and imposes

    p1(c,d)=xi3*q1(theta,psi),
    p2(c,d)=xi3*q2(theta,psi).

Over L=K(sqrt(b/xi1)), a final conic parametrisation gives binary quadratics Q_i(lambda,mu); writing lambda=x+beta*y, mu=u+beta*v and expanding pi*Q1, pi*Q2 in the basis 1,beta produces quadratic forms F1,F2,G1,G2. The 4-covering is the quadric intersection

    C4: F2(x,y,u,v)=G2(x,y,u,v)=0.

Fisher states that only finitely many squareclasses xi_j can be everywhere locally soluble at each stage. The covering maps and pushout functions are explicit: f1=x, f2=f(l,m)/m^2, f3=(alpha*q1+beta*q2+gamma*s)/psi^2, and f4=ell*ellbar/psi^2, with the linear coefficients obtained from the displayed conic parametrisations.

Section 7 supplies the next-stage geometry. For a nonsingular quadric intersection C in P^3, singular fibres in its pencil give conics Gamma_i. Tangent planes at suitable points on a pair of these conics yield a pushout form f=ell1*ell2. The resulting double cover D is again a nonsingular quadric intersection, and Theorem 7.2 gives the degree-2 map D->C explicitly after parametrising the conic. Companion intersections C4 and C4^dagger then provide the new pushout forms needed for the next pairing. Section 8 states that, when E has full rational 2-torsion, repeating this for all three nonzero 2-torsion points produces exactly the functions required for the S^(4) x S^(2) Cassels-Tate calculation used in 8-descent.

## Specialization to E_113

For

    E_113: y^2=x^3-113^2*x=x(x^2-12769),

Fisher's equation (7) has a=0 and b=-12769=-113^2. Thus for a candidate squareclass xi1 the authenticated first covering is

    r^2 = xi1*s^4 - (12769/xi1)*t^4.

This is now an exact starting equation, not a guessed covering. It is nonsingular for nonzero xi1 because Fisher's discriminant condition 2*b*(a^2-4b) != 0 holds.

This does NOT yet identify which xi1 represents the chosen nonzero pure Sel_2(E_113) class in the particular isogeny filtration, and it does not select the locally soluble xi2,xi3,xi4. The existing Monsky/Kummer description is a full [2]-descent description, whereas Fisher Section 5 is organised as alternating phi and dual-phi descents. An explicit translation between these conventions is required before choosing xi1. Treating an arbitrary coordinate of a Monsky class as xi1 would be an unjustified convention change.

## What remains missing

No explicit everywhere-locally-soluble C4 for E_113 has yet been certified. We still need:

1. fix one rational 2-isogeny phi and its dual and translate a nonzero pure full-2-Selmer class into Fisher's S_m/S'_m filtration;
2. determine the correct locally soluble squareclasses xi1,xi2,xi3,xi4 rather than guessing them;
3. solve and parametrise the required conics, producing explicit p_i,q_i,Q_i and hence F2,G2;
4. verify nonsingularity and the covering map algebraically;
5. construct the companion intersection/pushout forms and certify local points at every relevant place before evaluating Hilbert symbols.

The previously established global endpoint remains only a test oracle: the second pure pairing for E_113 has rank 2, whereas E_41 gives zero. It must not be fed into the explicit local construction.

## Methodological results

The earlier shortcut remains rejected: pulling first-stage functions back to the higher cover makes them squares and cannot detect the nonzero second pairing. Fisher Section 7 explicitly constructs new pushout forms from tangent planes to the singular-fibre conics, confirming why new functions are mathematically necessary.

A second potential error has now been blocked: the full [2]-Selmer coordinates used in the Monsky calculation cannot be silently identified with Fisher's first 2-isogeny squareclass xi1. The translation through a chosen rational 2-isogeny must be proved first.

## Next executable step

Choose T=(0,0) on E_113 and write down the corresponding 2-isogenous curve E' and the two connecting homomorphisms explicitly. Compute their Selmer squareclasses by exact local conditions at the finite set of relevant places {2,113,infinity}. Match their images to the already-certified full 2-Selmer basis. Only after that translation is certified, instantiate r^2=xi1*s^4-(12769/xi1)t^4 and continue Fisher's equations (9)–(13).

No complete BSD candidate, formal proof, independent expert review, publication, submission, or prize claim exists.