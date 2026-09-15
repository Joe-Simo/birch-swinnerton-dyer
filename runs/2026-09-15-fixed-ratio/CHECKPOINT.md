# We have not solved the Birch–Swinnerton-Dyer problem yet.

## H11: fixed exact ratio obstruction and explicit quotient lifting

The expanded proof and evidence archive are BSD_H11_fixed_ratio_2026-09-15.zip, stored only in the assigned project folder unless separately mirrored. Base: bd4fc335fd24ea7e685330c5d41785256926c16e. Old proofs remain unchanged. This compact record contains the decisive derivations; the infinite conclusions are self-reviewed source-dependent mathematics, not formal or independent expert verification.

Write F_+(x)=x^4+6x^2+1 and F_-(y)=y^4-6y^2+1. H8's witnesses F_+(A_+/B_+)=p(c_+/B_+^2)^2 and F_-(A_-/B_-)=p(c_-/B_-^2)^2 determine the EXACT rational ratio

    q=c_- B_+^2/(c_+ B_-^2),  q!=0.

### Fixed-fiber theorem

The projective curve C_q:F_-(Y,Z)=q^2 F_+(X,Z) is smooth of genus3 for every rational q other than0,+/-1. Let k=q^2. Its derivatives in X,Y are -4kX(X^2+3Z^2),4Y(Y^2-3Z^2). At Z=0 these cannot vanish simultaneously at a projective point. At Z=1 the critical squares (X^2,Y^2) range over {0,-3}x{0,3}, giving equation values 1-k,-8-k,1+8k,8(k-1). The only positive singular k is1. Smoothness implies geometric integrality by Bezout; the plane-quartic genus formula gives3.

Faltings' theorem therefore makes C_q(Q) finite for each nonexceptional q. At k=1 the equation factors (Y^2+X^2)(Y^2-X^2-6Z^2). The first component yields only kernel1 over Q. On the second, t=y+x gives x=(t-6/t)/2,y=(t+6/t)/2, exactly H10's family. H10's complete prime filter permits only41. Thus any FINITE SET OF EXACT RATIONAL RATIOS yields only finitely many prime kernels. This is not an assertion about finitely many squareclasses of ratios, nor about varying q; it provides no effective height bound. If infinitely many distinct prime kernels are realized by witness pairs, their chosen ratio heights escape every fixed bound. This last formulation does not itself assert infinitude of eligible primes.

There is no nonconstant rational parametrization of a nonexceptional fiber: a map P1->C_q would extend to a finite morphism, contradicting -2=4d+ramification in Riemann-Hurwitz.

### Three genus-one quotients and Jacobians

The sign involutions give degree2 quotients

    D_y: U^2=k x^4+6k x^2+k+8, U=y^2-3;
    D_x: V^2=y^4-6y^2+1+8k, V=q(x^2+3);
    D_xy: W^2=(k+8)t^4+18k t^2+k(1+8k),
          t=y/x, W=(t^4-k)x^2-3(t^2+k).

The last formula is on x!=0; all maps extend to smooth projective models. Their quartics are separable for k>0,k!=1. With I=12AC+B^2,J=72ABC-2B^3 for At^4+Bt^2+C, the Jacobian model is v^2=u^3-27Iu-27J. Scaling u=36a,v=216b yields

    J_y: b^2=a^3-k(k+2)a-2k^2;
    J_x: b^2=a^3-(1+2k)a+2k;
    J_xy: b^2=a^3-k(2k^2+23k+2)a-6k^2(k^2+7k+1).

For the affine equation G=F_-(y)-kF_+(x), a canonical differential basis is dx/G_y,x dx/G_y,y dx/G_y. Pullbacks of dx/U,dy/V,dt/W are respectively4y dx/G_y,4q x dx/G_y,-4 dx/G_y. Independence proves Jac(C_q) is Q-isogenous to the product of the three displayed Jacobians. It does not identify rational points of C_q with arbitrary triples of quotient points.

### Exact local counterexample to omitting the lift

If z is a Q2 nonunit or0, both F_+(z),F_-(z) are squares: for positive valuation they are1 modulo8, and for negative valuation use F(z)=z^4F(1/z). If z is a unit, z^2=1+8a gives

    F_+(z)=8(1+8a+8a^2), F_-(z)=-4(1+8a-16a^2).

These have squareclasses2 and-1. Thus C_q(Q2) forces both affine x,y to be nonunits; valuation comparison then forces v2(q) even. Infinity gives (Y/X)^4=q^2 and the same restriction.

Take q=7/2. C_q(Q2) is empty. Yet D_y has (x,U)=(0,9/2), D_x has rational infinity points with normalized value+/-1, and D_xy has rational infinity points with value+/-9/2, since k+8=81/4. These are points on the actual smooth genus-one quotient curves, not merely Jacobians. The finite certificate enumerates all3584 primitive triples modulo16 in 4F_-(Y,Z)-49F_+(X,Z): residual set {3,4,7,8,11,12,15}, never0. Ordinary homogeneous scaling makes this a genuine Q2 obstruction. A separate Python enumeration covers448 normalized projective residue classes, each with8 unit multiples.

The omitted lift on D_y is the square condition y^2=U+3. At x=0 its two branches give15/2 and-3/2, both nonsquares in Q2. Similarly D_x needs V/q-3 square; D_xy needs (W+3(t^2+k))/(t^4-k) square on the nondegenerate chart, with the t^4=k cases handled separately.

### Positive control and the remaining variable-ratio problem

The reciprocal version of the H8 p137 pair gives (X:Y:Z)=(1:37:14),q=47/17. Directly F_+(1,14)=137*17^2 and F_-(37,14)=137*47^2. Thus relaxing q=1 reaches a prime outside H10's list, but this is a known witness, not a new rank result.

With q varying, W=qF_+(x) identifies the open surface with W^2=F_+(x)F_-(y). It is the function-field quotient of U^2=F_+(x),V^2=F_-(y) under simultaneous sign change, W=UV. Both base quartics have Jacobian b^2=a^3-a. A rational surface point can require Q(sqrt(n)) to lift to the product; no unjustified rational lift or Q-isomorphism to an untwisted Kummer model is used. A curve-finiteness theorem does not settle this surface. The remaining objective is a construction for prescribed primes retaining the squareclass and the compatible quotient lifts with q genuinely varying.

### Verification and sources

136 TypeScript assertions and88 Python/SymPy assertions passed. Wolfram independently returned zero generic residuals and the same local counterexample and137 witness. They do not verify Faltings' theorem or constitute formal verification. Run npm run lint; npm run typecheck; npm test; node dist/verify.js > results/integer-results.json; npm run test:symbolic. Lint here means compiler unused/unreachable diagnostics, not ESLint. Observed Node22.16.0,TypeScript5.8.3,Python3.13.5,SymPy1.14.0,Wolfram15.0.1.

[B] E.Bombieri, The Mordell conjecture revisited, Ann.Scuola Norm.Sup.Pisa17(1990),615-640, introduction615-616; Errata-Corrige18(1991),473. Primary theorem statement and its erratum authenticated, not full proof reconstructed. https://www.numdam.org/item/ASNSP_1990_4_17_4_615_0.pdf and https://www.numdam.org/item/ASNSP_1991_4_18_3_473_0.pdf .
[F] T.Fisher, On binary quartics and the Cassels-Tate pairing, Res.Number Theory8,74(2022), version of record28September2022, Section2 equations(1)-(2), DOI10.1007/s40993-022-00376-z .
H10 PRIME_FILTER.md remains the inherited exceptional-fiber completeness input. No general BSD, novelty, new analytic-order result, publication, extra spending or background work is claimed.
