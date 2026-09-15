# We have not solved the Birch–Swinnerton-Dyer problem yet.

The dual first-stage homogeneous spaces for E'_113:Y^2=X^3+4*113^2 X are

    d r^2 = d^2 s^4 + 4*113^2 t^4.

The support restriction gives d in {+/-1,+/-2,+/-113,+/-226}. Negative classes were previously eliminated over Q2 modulo 32.

## Positive classes at Q2

For d=2e with e=1 or113, divide by2:

    e r^2 = 2(e^2 s^4+113^2 t^4).

Take s=t=1 and r=2R. Then

    R^2=(e^2+113^2)/(2e).

For e=1 this is 6385, an odd 2-adic unit congruent 1 mod8; for e=113 this is 113, also congruent 1 mod8. Every odd Q2 unit congruent 1 mod8 is a square. Hence d=2 and d=226 have explicit Q2 points. The d=1 class is trivial and d=113 also has a Q2 point since 113 is a Q2 square. Thus all four positive candidates survive Q2.

## Classes divisible by 113 at Q113

Write d=113e, e=1 or2. Dividing the equation by113 gives

    e r^2 = 113(e^2 s^4+4*113 t^4).

Scale any hypothetical Q113 point to a primitive integral triple (r,s,t).

If s is a unit, the bracket is a unit, so the right side has valuation 1 while the left has even valuation 2v(r), impossible.

Therefore 113 divides s. If t is a unit, the bracket has exact valuation 1, so r is divisible by113. Put r=113R and s=113S. After dividing by113^2 one obtains

    e*113 R^2 = e^2*113^3 S^4 + 4 t^4,

whose left side is divisible by113 while the right side is a unit modulo113, contradiction.

If t is also divisible by113, primitiveness forces r to be a unit, but the displayed equation e r^2=113(...) has positive valuation on the right and zero on the left, again impossible.

Thus C_113(Q113)=C_226(Q113)=empty.

## Completed dual first-stage group

The previously certified nonsingular Hensel points show d=1,2 survive Q113. Combining all relevant places, the dual first-stage locally soluble squareclasses are exactly

    {1,2}.

Together with the other isogeny stage already proved to be {1,113}, both first-stage isogeny Selmer groups now have order two. This is consistent with, but does not by itself identify, the four-dimensional full [2]-Selmer group; the exact sequence and embedding conventions must be applied next.

All claims here are elementary local arguments plus the previously authenticated homogeneous-space formula. No BSD solution is claimed.