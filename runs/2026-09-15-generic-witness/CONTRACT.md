# H9: generic one-witness construction test

No complete BSD candidate. Parent: f04f51a515f786e1e842f6a30208b17c0814ea59,
private branch research/h2-endpoint-20260914. Work stays in the assigned BSD folder.

Question: can an algebraically uniform rational formula produce an independent
H8 minus witness from a generic plus witness (or conversely)? This tests a
possible global-construction mechanism; it is not a replacement of BSD over Q
by a function-field conjecture.

Objects: K=Q(t), E/K: y^2=x^3-t^2*x. X_minus: v^2=w^2+z^2,
u^2=t(w^2-z^2). X_plus: w^2=v^2+z^2, u^2=t(w^2+z^2).
Map pi=(t*w^2/z^2,t*u*v*w/z^3); Kummer ordering (x-t,x+t,x).

Success for the proposed construction: an actual K-rational map from one
covering to the other, with verified image equations and complementarity.
Refutation criterion: prove the second torsor has no point over the function
field of the first. Candidate route: compute the generic Mordell-Weil group,
endomorphism ring, and the two torsor classes, then classify morphisms.
Follow-up: determine whether odd-degree algebraic extensions evade this
obstruction; give an explicit even-degree extension as a boundary check.

Accepted finite checks will verify generic polynomial identities with SymPy;
the four full Kummer vectors over the independent squareclasses (-1,2,t);
their span and deliberate rank failures; and a few exact group-law operations
on the H8 E41 point. No enumeration can prove the classification of all
morphisms: that requires the written geometric/cohomological proof. No new
prime scan, floating-point rank, model-Sha example or novel BSD case is claimed.

Sources: primary author text for morphism/isogeny rigidity, genus-one torsors,
restriction/corestriction; H8 and its cited Kummer construction for the covering
coordinates. Any extension of a rational-field formula to K is to be justified
from its construction, not attributed blindly to an assertion only over Q.
No novelty claim; self-review and independent scalar implementations remain
different from expert/formal verification. No paid service or publication.
