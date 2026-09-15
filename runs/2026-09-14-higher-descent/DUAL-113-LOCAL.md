# We have not solved the Birch–Swinnerton-Dyer problem yet.

Continuation of the dual first-stage descent on E'_113:Y^2=X^3+4*113^2 X. The homogeneous spaces are d r^2=d^2 s^4+4*113^2 t^4.

## Q_113 certificates

For d=1 and d=2, reduce modulo 113. The t-term vanishes, leaving d r^2=d^2 s^4. Exact finite-field search found nonsingular affine points (r,s)=(1,1) for d=1 and (1,12) for d=2. At each point at least one partial derivative 2 d r or -4 d^2 s^3 is nonzero modulo 113, so ordinary Hensel lifting gives a Q_113 point (take any integral t, e.g. t=1, and lift r,s).

For d divisible by 113 write d=113e and divide the integral equation by 113:

    e r^2 = 113 e^2 s^4 + 4*113 t? [CORRECTION BELOW]

Careful algebra from d r^2=d^2 s^4+4*113^2 t^4 gives after division by 113^2, using d=113e:

    (e/113) r^2 = e^2 s^4 + 4 t^4,

which is not integral in r. Instead divide only by 113:

    e r^2 = 113 e^2 s^4 + 4*113 t^4.

Thus modulo 113 the right side is zero, forcing r divisible by 113; this reduction is singular and the preliminary Wolfram check that used e r^2=113 e^2 s^4+4 t^4 was based on an incorrect division. It is explicitly rejected here and no Q_113 certificate for d=113 or 226 is claimed from that check.

## Status

Certified at Q_113: d=1,2. Unresolved at Q_113: d=113,226 because the natural reduction is singular and requires valuation analysis/rescaling. The prior Q_2 status also remains unresolved for positive d=2,226: compatible residues through powers of two are evidence only, not a Hensel proof because all derivatives have positive 2-adic valuation.

This record deliberately preserves the caught algebra error rather than silently promoting it. No complete dual Selmer group, no complete BSD candidate, and no publication claim exists.