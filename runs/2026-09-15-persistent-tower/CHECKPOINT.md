# We have not solved the Birch–Swinnerton-Dyer problem yet.

## H5: complete abstract towers and a concrete failure of rational extraction

This compact checkpoint records the proof needed to resume from the private repository. The expanded argument, detailed source ledger, preserved-input hashes, complete logs and H4 replay are in this run's local RESEARCH.md and the conversation artifact BSD_H5_persistent_tower_2026-09-15.zip under /mnt/data/04-birch-swinnerton-dyer. The archive is not claimed mirrored on GitHub. None of these results is asserted new to mathematics or a full BSD resolution.

### Inherited hypothesis, not a new rank theorem

H4, at base commit1822d1e026016c4dd486e6d273fa1442c4a00721, treats E_p:y²=x³-p²x with p prime congruent1 modulo8. In its persistent case, with r=rank E_p(Q), A=Sha(E_p)[2-infinity] and D=Q_2/Z_2, it gives r in {0,1,2}, A=D^(2-r), and rational2-primary torsion F=(Z/2)^2. This classification and H4's separate CM theorem identification of persistence with c_p=0 are inherited inputs. No curve realizing r<2 with nonzero divisible Sha is exhibited. Old order-two isogeny-Selmer claims corrected by H3 remain rejected.

### Proposition1: both transition maps still fail to separate the ranks

Put M=E(Q), S_m=Sel_(2^m), K_m=M/2^mM. In the exact Kummer sequence 0->K_m->S_m->A[2^m]->0, the map u_m:S_(m+1)->S_m is reduction on Kummer classes and multiplication2 on Sha. Coefficient inclusion j_m:S_m->S_(m+1) is multiplication2 on Kummer classes and inclusion on Sha. Thus j_m u_m=[2] and u_m j_m=[2] on their respective domains.

Taking inverse limits gives 0->M^wedge_2->S->T_2A->0; surjectivity on the right follows because the Kummer transitions are onto. In the persistent case M^wedge_2=Z_2^r+F and T_2A=Z_2^(2-r). A free Z_2 quotient splits, so S=Z_2^2+F. Rational2-torsion is exactly the torsion subgroup of S.

Divisibility of A makes u_m onto. Hence S->S_m is onto and factors through S/2^mS. Both finite groups have order4*2^(2m), proving this factor map is an isomorphism. Consequently, simultaneously at all levels,

    S_m=(Z/2^m)^2+(Z/2)^2,
    u_m(a,b;e,f)=(a mod2^m,b mod2^m;e,f),
    j_m(a,b;e,f)=(2a,2b;0,0).

The j formula follows from j_m u_m=[2] and surjectivity of u_m. In particular j kills the rational2-torsion component. The marked Kummer subgroup is (Z/2^m)^r+F; it is the missing marking, not the unmarked tower, which carries r. This is an abstract normal-form obstruction, not an isomorphism of localizations, cocycles, geometric coverings or already-specified rational-point images.

More generally, if P_infinity is the intersection of images S_n->S_1, then

    0 -> M/2M -> P_infinity -> A_div[2] -> 0.

Finite branching gives a compatible lift of any class lying in every image. The pro-Selmer exact sequence maps its Sha component into the Tate module, whose level1 image is A_div[2]; conversely every such divisible class lifts. Finite Sha summands have zero Tate module. Thus the true finite-class extraction target is A_div[2]=0, not merely compatibility.

### Proposition2: all-prime finite étale descent leaves the same obstruction

For a smooth projective genus-one torsor X representing xi in Sha(E/Q), Stoll's paper p374 after Corollary6.3, together with Corollary7.3, gives

    X(A_Q)_bullet^(f-cov)=X(A_Q)_bullet^(f-ab)=X(A_Q)_bullet^Br,

nonempty exactly when xi is in the divisible subgroup of the full Sha. The f-cov set uses all finite étale torsors, not only2-power or abelian covers. The author's2017 errata Section2 item(6) explicitly repairs and retains this torsor statement; its restrictions on other general abelian-cover assertions must not be ignored.

If H4's bad alternative A=D^delta, delta>0, were realized, a nonzero xi in D^delta[2] would be divisible by every integer (odd multiplication is an automorphism). Its torsor would have no rational point but pass all the tests above. This is a conditional barrier to that strengthening of the method, not an actual infinite-Sha construction, and says nothing against ramified/auxiliary global constructions outside these tests.

### Proposition3: bounded-height criterion and an actual E41 counterexample

For z=(z_m) in pro-Selmer, let H_m(z) be the least canonical height of a rational point representing z_m, or infinity if none exists. Use h(P)=log H(x(P)) and the associated canonical height, with h(O)=0. Rational representatives are nested, and bounded canonical height has finitely many rational points. Therefore

    sup_m H_m(z)<infinity iff z is represented by one rational point.

Uniqueness is only modulo odd rational torsion in general. If z has nonzero Tate-Sha component, H_m is eventually infinity. If z lies in M^wedge_2 but outside the diagonal image of M, every H_m is finite and they are unbounded. Compatibility does not supply the missing height bound.

A concrete case has been proved exactly. On E41:y²=x³-1681x take P=(-9,120). At good primes3,5 the groups have orders4,8, respectively. Prime-to-characteristic torsion injectivity at those two primes, together with the four known2-torsion points, proves E41(Q)_tors=(Z/2)^2. Hence P is nontorsion. At the good prime11,

    #E41(F11)=12,
    [3]E41(F11)={O,(0,0),(3,0),(8,0)},
    P mod11=(2,10).

Thus P is not in3E41(Q). Independent group-law and division-polynomial methods verify the complete finite image, not a sampled point search.

For every m>=1 let a_m=(1-(-2)^m)/3 and R_m=a_m P. The integers a_m obey 3a_m=1-(-2)^m and a_(m+1)-a_m=(-2)^m. Thus the rational Kummer classes of R_m are compatible. They define the formal element P/3 in the2-adic completion, in which3 is invertible. A single rational representative R at all levels would force3R-P in the intersection of2^mM, which is0 by finite generation and the computed torsion. That contradicts mod11 nondivisibility. Every finite level is rational, but no one rational point represents the full tower.

This example does not exhibit a non-Kummer finite class or divisible Sha on E41. It refutes a stronger, false compactness inference even on an actual positive-rank curve. The pro-2 completion only localizes naturally to the2-primary completion of E(F11), not to its entire odd-order part; the mod11 certificate obstructs rational division without contradicting pro-2 divisibility.

There is also a lower bound for ALL representatives, not merely multiples of P. Put h_P=hat h(P)>0 and let lambda>0 be the least positive canonical height on E41(Q), whose existence follows from the Mordell-Weil lattice. If R represents z_m, then3R-P=2^m Q with Q nontorsion, since all rational torsion is killed by2^m and3R=P is impossible. The height norm triangle inequality gives

    ((2^m sqrt(lambda)-sqrt(h_P))_+/3)^2
        <= H_m(z) <= ((1-(-2)^m)/3)^2 h_P.

No numerical lambda, canonical-height estimate or saturated basis is claimed. This is a proved4^m height-escape estimate on a fixed curve, not an inference from finite computations.

### Verification and source audit

280 TypeScript assertions and185 Python/SymPy assertions passed. TypeScript enumerates E41 over3,5,7,11, all12^3 associativity cases at11, coefficients through64, centered minimality through10, and abstract towers with both maps through level4. Python independently uses the generic tripling division-polynomial identity, exact rational representatives through4, bit-by-bit coefficient lifts through64, and abstract maps. Wolfram reproduced all four finite groups and six true grouped tests. Finite programs do not prove the infinite-depth and height propositions; those are the arguments above. H4's669/38-check outputs replayed byte-for-byte; all eight original local files remained unchanged.

Observed Node22.16.0, TypeScript5.8.3, Python3.13.5, SymPy1.14.0 and Wolfram15.0.1. Run npm run lint, npm run typecheck, npm test, npm run test:symbolic. Lint is strict compiler unused/unreachable diagnostics. No extra package purchases were made. A transient parenthesis syntax error was corrected before acceptance.

Primary sources: Michael Stoll, Finite descent obstructions and rational points on curves, Algebra & Number Theory1(4)(2007),349-391, DOI10.2140/ant.2007.1.349, https://msp.org/ant/2007/1-4/ant-v1-n4-p01-p.pdf ; p352 inverse limits, p374 torsors, p379 Cor7.3. Essential errata dated March29,2017: https://www.mathe2.uni-bayreuth.de/stoll/papers/Errata-FiniteDescent-ANT.pdf , Section2(6). Joseph H. Silverman, author-hosted Wyoming2006 lectures, https://www.math.brown.edu/~jhs/Presentations/WyomingEllipticCurve.pdf , PDFpages69-72 reduction/torsion,75 heights,79 canonical-height theorem. Exact pages were parsed and publisher/author screenshots inspected; the errata was read in full. A local PDF download failed, so no cached full-paper hash is claimed. These are known inputs and formal/elementary consequences, not a global novelty result or expert/formal verification.

### Next mathematical obligation

For each persistent FINITE class alpha, seek a selected compatible lift whose rational representatives admit a uniform-in-level height bound; do not require this for every possible full tower, which the example disproves. Investigate whether explicit congruent-number covering equations give a global height-reduction construction without assuming a rational point or Mordell-Weil basis in advance. This is still unproved, not a promised algorithm. All-prime finite étale and ordinary Brauer-Manin repetition alone cannot fill the gap. Complex vanishing-order control remains separate. No complete BSD candidate, publication, external contact, force push, spending or background job exists.
