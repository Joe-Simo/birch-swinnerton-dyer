# We have not solved the Birch–Swinnerton-Dyer problem yet.

## Dual first-stage equation

For E'_113:Y^2=X^3+4*113^2 X, Fisher's same homogeneous-space formula gives

    r^2 = d s^4 + (4*113^2/d) t^4,

or integrally

    d r^2 = d^2 s^4 + 4*113^2 t^4.

Candidate squareclasses supported at 2 and 113 are d in {+/-1,+/-2,+/-113,+/-226}.

## Exact Q2 elimination of all negative classes

A Q2 point can be scaled, by homogeneity, to a primitive Z2 triple (r,s,t). Its reduction modulo 32 must therefore be a primitive solution of the integral equation. Wolfram exhaustively enumerated all 32^3 residue triples for each candidate and required at least one coordinate odd. It found no primitive solution modulo 32 for d=-1,-2,-113,-226. Thus all four negative squareclasses are rigorously excluded from the dual Selmer group at Q2.

For d=1,2,113,226 primitive solutions modulo 32 exist, so this modulus gives no obstruction. This is only a necessary local screen for the positive classes, not a Q2-solubility certificate.

## Current dual candidates

The dual first-stage candidate set is reduced to {1,2,113,226}. Further Q2/Q113 analysis is required for d=2,113,226. The class d=1 is trivial and globally soluble using t=0,s=1,r=1.

## Next step

For d=113, Q2 solubility on the t=0 patch reduces to r^2=113 s^4; since 113 is congruent to 1 mod 8 it is a Q2 square, giving a direct Q2 point. For d=2 and 226, construct explicit Hensel-liftable Q2 points or eliminate them at a higher congruence. Then impose Q113 conditions. Do not promote mod-32 survival to local solubility.

Evidence classification: negative classes are proved Q2-insoluble by exhaustive primitive reduction modulo 32; positive survivors are unresolved except d=1 globally and the stated d=113 Q2 observation. No complete BSD candidate exists.