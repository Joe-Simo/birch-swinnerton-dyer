# We have not solved the Birch–Swinnerton-Dyer problem yet.

## Verified 2-isogeny specialization

For E:y^2=x^3+a x^2+b x with T=(0,0), the standard degree-2 isogeny has target E':Y^2=X^3-2a X^2+(a^2-4b)X and, away from the kernel, coordinates X=y^2/x^2 and Y=y(b-x^2)/x^2. A direct symbolic substitution was executed in Wolfram; after imposing the source equation the target residual is zero.

For E_113:y^2=x^3-12769x this gives

    E'_113: Y^2=X^3+51076 X,
    X=(x^2-12769)/x,
    Y=-(x^2+12769)y/x^2.

Applying the same formula to E'_113 gives E'':v^2=u^3-204304u. The change u=4x,v=8y identifies E'' with E_113. This fixes the isogeny/dual-isogeny models needed for Fisher's alternating descent and removes the previous convention ambiguity at the level of curves and maps. The connecting squareclass maps themselves still require an exact source audit before they are used.

## Local screen executed

For candidate squareclasses d in {+/-1,+/-2,+/-113,+/-226}, the first Fisher quartic was cleared integrally as

    d r^2 = d^2 s^4 - 12769 t^4.

An exhaustive finite-field screen searched nonzero projective triples modulo p for p=3,5,7,11,13,17,113. Every candidate has a mod-p solution at every tested prime. Therefore none is eliminated by these elementary residue obstructions. This is deliberately only a one-way screen: many returned points, especially modulo 113, are singular and their existence is NOT a Q_p solubility certificate. No Hensel conclusion is drawn from them.

## Consequence

The next load-bearing step is now smaller and cleaner: authenticate the two connecting homomorphisms for the chosen 2-isogeny and its dual, including their values at the kernel points, then impose genuine Q_2 and Q_113 local conditions on the corresponding homogeneous spaces. Do not infer the Selmer groups from the finite-field screen. Once the isogeny Selmer groups and their maps into the full [2]-Selmer group are certified, choose the nontrivial lift and instantiate Fisher equations (9)-(13).

Evidence classification: the isogeny formulas are symbolically verified algebraic identities; the finite-field computation is exhaustive only for the stated candidates and primes and is not a local-solubility theorem. No complete BSD candidate exists.