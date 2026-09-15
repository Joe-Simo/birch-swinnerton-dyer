# We have not solved the Birch–Swinnerton-Dyer problem yet.

## H4 — an all-prime first-descent identity and a stopping-depth classification

**Outcome.** The corrected H3 example extends to a uniform first-pairing calculation for every prime p congruent to 1 modulo 8. With the fixed normalizations below,

\[
\boxed{\Theta_1(p,2)=c_p/4\pmod2.}
\]

Here c_p is an exact signed Tunnell coefficient. The first-pairing derivation uses local algebra and a classical binary-quadratic-form identity, **not** an analytic rank theorem or the refined BSD formula. A separate finite-group argument describes every possible stopping depth of this isogeny descent. Applying established CM theorems afterward identifies that depth when c_p is nonzero. These are source-dependent, self-reviewed deductions and known-theorem consequences, not a novelty claim or a solution of general BSD.

The new test case p=1153 has c_p=16. Its rank zero and groups Sha(E_p)[2^infinity]=(Z/8)^2 and Sha(E'_p)[2^infinity]=(Z/4)^2 follow from the audited theorem chain. Unlike H3 at 113, **H4 has not explicitly constructed the higher covering or evaluated the fifth pairing at 1153.** The data files label this distinction.

## 1. Scope, preservation, and exact conventions

The universal target is still ord_(s=1)L(E,s)=rank E(Q) for every elliptic curve E/Q. This run is restricted to the prime subfamily

\[
E_p:y^2=x^3-p^2x,\qquad E'_p:Y^2=X^3+4p^2X,\qquad p\equiv1\pmod8.
\]

All new local work is in `runs/2026-09-15-stopping-depth`. The old H3 archive and every other preexisting BSD file were hashed before execution and left unchanged. `preserved-inputs.json` records the inventory. The H3 archive SHA256 is `f0f24cf26c29b8d5f3f99594da36b9284405907f4e4ba144f4ce9eb237295c97`. Its 17 TypeScript and 25 Python checks were replayed successfully from byte-preserved sources; see `h3-replay.log`. This rechecks the executable certificates, not every foundational theorem in H3.

The remote branch was read at `e1f48dbd080fbb00725d82ca251f6aa2bd7a1323`. All corrected H3 conventions are retained. In particular, S is on the E' coordinate side:

\[
S_1=\operatorname{Sel}^{\phi}(E_p/\mathbf Q)=\langle2,p\rangle,
\quad
S'_1=\operatorname{Sel}^{\widehat\phi}(E'_p/\mathbf Q)=\langle-1,p\rangle.
\]

Both spaces have dimension two. The earlier order-two groups and the proposed single Theta_2(113,2) obstruction are withdrawn by H3 and are not inputs here. Fisher's f_2 is a function on C1, not on C2 [F, Section 5].

For completeness, the first-stage description is uniform: the x-coordinate has even valuation away from the coefficient b in y^2=x(x^2+a x+b), giving the stated support. On E all four classes in S' come from rational 2-torsion. On E', positivity excludes negative classes. The four positive classes have local points at 2 because p and (p^2+1)/2 are odd squares in Q_2. At p, 2 is a square and the equations s^4=-1 and s^4=-4 have simple roots because 8 divides p-1: with a generator g of F_p^*, g^((p-1)/8) is a fourth root of -1, and multiplying it by a square root of 2 gives a fourth root of -4. At every other odd prime the smooth genus-one quartic has good reduction, a finite-field point by the Hasse bound, and a Hensel lift.

Every class in S' is rational-point-derived and therefore survives every filtration stage. Fisher's even pairings are consequently zero. Each odd pairing on S_m is alternating, so, while S_m has dimension two, its kernel has dimension two or zero. Thus the first nonzero odd pairing, if one occurs, kills S entirely; the other side remains S'. These facts use [F, Theorem 2.1] with its actual filtration, not a relabeled full-Selmer pairing.

## 2. An explicit first-pairing formula valid for every prime in the family

There is a unique representation

\[
p=u^2+16v^2,\qquad u,v>0.
\]

This is the positive, odd-coordinate convention in the usual unique representation of a prime by two squares; the even coordinate is divisible by four. Put b=2v, so p=u^2+4b^2. On the correct isogeny side the class p has covering

\[
C_1:\quad r^2=p(s^4+4t^4).
\]

The associated conic has the rational point (S:T:R)=(u:b:p). Define

\[
f=u(l^2-m^2)-4blm,\quad g=b(l^2-m^2)+ulm,\quad h=p(l^2+m^2).
\]

Direct expansion gives h^2=p(f^2+4g^2). The tangent expression and a second quadratic expression are

\[
L=r-us^2-4bt^2,\qquad M=bs^2-ut^2.
\]

They satisfy, on C1,

\[
L(r+us^2+4bt^2)=4M^2.
\tag{1}
\]

The tangent pulls back to h-uf-4bg=2pm^2 on the parametrized conic. Therefore Fisher's actual pushout function f(l,m)/m^2 corresponds on C1 to

\[
f_2=\frac{2p\,s^2}{L}.
\tag{2}
\]

This is an equality of rational functions using the projective conic parametrization. Local points are chosen away from zeroes and poles. Multiplying by a global rational constant changes the individual local symbols but not their product, by Hilbert reciprocity; inverses and squares have the usual trivial effect. Consequently the global pairing against 2 can be evaluated using (L,2)_w. This supplies the missing divisor/function comparison rather than guessing a tangent function.

### 2.1 All places other than 2

At p, 2 is a square in Q_p, so the symbol is +1. At the real place the second entry 2 is positive, also giving +1.

At an odd prime q distinct from p normalize s,t to integral coordinates with at least one a unit, and scale r with weight two. Then r is integral. If both L and r+us^2+4bt^2 were divisible by q, equation (1) would make M divisible by q. The equations

\[
us^2+4bt^2\equiv0,\qquad bs^2-ut^2\equiv0\pmod q
\]

have coefficient determinant -p, a unit. They force s=t=0 modulo q, a contradiction. Thus whenever L has positive q-adic valuation, its other factor in (1) is a unit. Its valuation is therefore even. For an odd q, an even-valuation first entry and the unit second entry 2 have Hilbert symbol +1. This proves the claim at **every** such q, including any primes dividing u or v; no finite prime sweep is substituted for that argument. Changing weighted normalization multiplies L by a square.

### 2.2 The 2-adic contribution

Take s=1,t=0 and choose

\[
r=-u\sqrt{1+16v^2/u^2}.
\]

The square root is the 2-adic branch near 1. The binomial series converges since v_2(16v^2/u^2)>=4. Its first terms give

\[
L/2\equiv-u-4v^2/u\equiv-u\,5^v\pmod8.
\]

In particular v_2(L)=1. For an odd unit w, (2^k w,2)_2=(-1)^((w^2-1)/8). Since the associated character takes 5 to -1 and is unchanged by negation or inversion, the local contribution is

\[
\boxed{\Theta_1(p,2)=\frac{u^2-1}{8}+v\pmod2.}
\tag{3}
\]

All statements in this section are uniform identities and valuation arguments. The computer checks verify their polynomial algebra and four local scalar specializations; they are not the proof of the all-prime quantifier.

## 3. Relating the same bit to an exact representation count

Use the original signed counts, including every sign and every zero coordinate:

\[
A_p=\#\{(x,y,z)\in\mathbf Z^3:x^2+2y^2+8z^2=p\},
\]
\[
B_p=\#\{(x,y,z)\in\mathbf Z^3:x^2+2y^2+32z^2=p\},
\qquad c_p=B_p-A_p/2.
\]

Tunnell identifies c_p with the coefficient of q^p in

\[
q\prod_{m\ge1}(1-q^{8m})(1-q^{16m})\sum_{j\in\mathbf Z}q^{2j^2}.
\]

The following parity calculation needs only the counts, not their L-function interpretation.

In each ternary representation, x is odd and y is even. For a positive odd x with x^2<p, put n_x=(p-x^2)/8. Let R(n) count representations n=a^2+b^2 with all signs, and let D(n) count those with b even. Then

\[
c_p=\sum_x(2D(n_x)-R(n_x)).
\tag{4}
\]

When n is odd, swapping a and b shows D=R/2, so the summand is zero. For n divisible by four, both a,b are even and the summand is R. For n congruent to two modulo four, both are odd and the summand is -R. There are no representations when n is three modulo four.

Quarter-turn rotation acts freely on the representations of each positive n, so R(n) is divisible by four. Complex conjugation acts on the rotation orbits. A fixed orbit consists precisely of an axis representation, n=a^2, or a diagonal representation, n=2a^2. There is one such orbit in each exceptional case; all other orbits are paired. Thus

\[
R(n)/4\text{ is odd}\quad\Longleftrightarrow\quad n\text{ is a square or twice a square}.
\]

The two possibilities for an even n_x yield respectively p=x^2+32z^2 and p=x^2+16z^2. If N_k(p) counts positive solutions to p=x^2+kz^2, equation (4) gives

\[
4\mid c_p,\qquad c_p/4\equiv N_{16}(p)+N_{32}(p)\pmod2.
\tag{5}
\]

Here N_16=1, and N_32 is zero or one. The uniqueness statements follow from unique factorization of prime norms in Z[i] and Z[sqrt(-2)]; both are norm-Euclidean (rounding errors have norm at most 1/2 and 3/4 respectively).

The needed representation comparison is Kaplansky's theorem, used through Mortenson's own proof [M, Theorem 2.1, Section 4, pp.10-11]. For p congruent to 1 modulo16, representations by x^2+32z^2 and x^2+64z^2 occur together; for p congruent to9, precisely one occurs. Since N_64=1 exactly when v in p=u^2+16v^2 is even, this implies

\[
1+N_{32}(p)\equiv\frac{u^2-1}{8}+v\pmod2.
\]

Combining (3) and (5) proves

\[
\boxed{\Theta_1(p,2)=c_p/4\pmod2\quad\text{for every prime }p\equiv1\pmod8.}
\tag{6}
\]

This proof keeps the arithmetic pairing and count calculation separate until their final comparison. Mortenson's representation theorem is a named source dependency; it has not been replaced by bounded numerical agreement. Kaplansky's original article was not itself inspected.

## 4. What finite stopping actually proves, at arbitrary depth

Set r=rank E_p(Q), A=Sha(E_p)[2^infinity] and B=Sha(E'_p)[2^infinity]. The rank is at most two. Since every element of S' is rational-point-derived, B[phihat]=0. Thus g=phihat:B->A is injective. Write f=phi:A->B; then gf=[2] and fg=[2]. Identify C=gB with a subgroup of A. We have

\[
2A\subset C\subset A,\qquad A[2]=\ker f,\qquad \dim A[2]=2-r.
\]

The last equality follows from the rational-point/Sha sequence for S and the isogeny rank formula: E'(Q)/phi E(Q) has dimension r, since the other quotient has dimension two.

Fisher's images in the Sha filtration now become

\[
X_{2n+1}=2^n A[2^{n+1}],\qquad
X_{2n}=2^{n-1}C[2^n],\qquad \dim S_m=r+\dim X_m.
\tag{7}
\]

These formulas follow by applying g to f and using gf=2; in particular ker(2^n f)=A[2^{n+1}]. They are not inferred from example tables.

Suppose the first nonzero odd pairing is Theta_(2h-1). Then S_m has dimension two for m<2h and S_(2h)=0. The latter forces r=0. Equation (7) shows that A has two cyclic factors, both of length h, and no divisible part. More explicitly, 2^h A[2^(h+1)]=0 excludes every element of order greater than 2^h, while the odd-stage dimensions count how many cyclic factors have order at least 2^(n+1). These counts are two up to h and zero afterward. Hence

\[
A\simeq(\mathbf Z/2^h)^2.
\]

Also X_(2h)=0 means 2^(h-1)C=0. Within A=(Z/2^h)^2 the subgroup killed by2^(h-1) is 2A. As 2A is already contained in C, C=2A. Since g is injective,

\[
\boxed{B\simeq(\mathbf Z/2^{h-1})^2.}
\tag{8}
\]

For h=1, B is trivial. This argument proves finiteness rather than assuming it. The standard cofinite-generation of p-primary Sha from Selmer finiteness can be used to phrase the cyclic decomposition; bounded exponent and finite A[2] also give finiteness directly.

## 5. Persistent descent does not prove rational rank two

If no odd pairing becomes nondegenerate, every S_m has dimension two. A 2-primary group with finite A[2] is a sum of a divisible part (Q_2/Z_2)^delta and finitely many cyclic factors. One can see the needed structure here without presupposing finiteness of Sha: if element orders are unbounded, the finite branching of the doubling-preimage tree above the finitely many nonzero elements of A[2] gives an infinite compatible chain and hence a Prüfer subgroup. A divisible subgroup splits off; repeat, decreasing dim A[2] each time. The remaining bounded-exponent group is finite, since |A[2^n]| is at most |A[2]|^n. In (7), the dimensions of 2^n A[2^(n+1)] eventually equal delta. They equal 2-r for every n here, including n=0. Consequently there are **no nonzero finite cyclic factors**, and

\[
\boxed{A\simeq B\simeq(\mathbf Q_2/\mathbf Z_2)^{2-r}.}
\tag{9}
\]

Indeed 2A=A in this case, so C=A as well. The argument alone does not distinguish r=2 and Sha[2^infinity]=0 from r=0 or1 accompanied by a divisible Sha contribution. No actual elliptic curve realizing either unwanted alternative is asserted.

H3's Kummer torsion calculation shows that E_p has no rational point of order four: none of the three nonzero 2-torsion Kummer classes is trivial, because one coordinate is 2 or -1. Thus the rational 2-power torsion always has size four. From the finite Selmer exact sequence, the persistent case gives, for every m>=1,

\[
|\operatorname{Sel}_{2^m}(E_p)|
=4\cdot2^{rm}\cdot2^{(2-r)m}=4\cdot4^m.
\tag{10}
\]

This is the same full sequence of **orders**, not merely a finite prefix, for all three values of r left open by this argument. It rules out the attempted deduction “this Selmer growth pattern proves rank two.” It does not rule out additional arithmetic constructions distinguishing the cases.

## 6. A separate, source-dependent comparison at every depth

This section uses established CM theorems. It is deliberately not labeled an independent explicit higher-descent computation.

Tunnell's Theorem 3 supplies

\[
L(E_p,1)=\frac{c_p^2\beta}{4\sqrt p},\qquad
\beta=\int_1^\infty\frac{dx}{\sqrt{x^3-x}}>0.
\]

The minimal differential is dx/(2y). Its period on the identity component is beta/sqrt(p); the real curve has two components, so the full real period is Omega_p=2beta/sqrt(p). Therefore L(E_p,1)/Omega_p=c_p^2/8.

The finite local factors are c_2=2, c_p=4 and one elsewhere; in this paragraph c_q denotes a Tamagawa number rather than the coefficient. To avoid ambiguity elsewhere we refer to them by name. These factors and rational torsion order four are stated explicitly in Tunnell's final remark on p.330 [T]. An algebra check also verifies the inputs: at2 E_p is isomorphic over Q_2 to E_1 by a unit scaling, and E_1 after x=X+1,y=Y+X has coefficients (2,2,0,2,0), with b_8=-4, the type-III case of Tate's algorithm. At the odd prime p the I0-star auxiliary cubic is T^3-T, with three distinct roots. The discriminant valuations are six at2 and p, so the displayed model is minimal. We use Tunnell's authenticated local-factor calculation rather than claim to have reread Tate's entire original algorithm.

For c_p nonzero, Burungale-Flach [BF, Theorem 1.1 and Corollary 2] proves rank zero, finiteness of Sha and the refined BSD formula for these CM curves, including the prime2 contribution. There is no omitted bad-reduction or unit-prime exception in this corollary. Its application can be checked explicitly over K=Q(i): [i](x,y)=(-x,iy), the endomorphism ring is Z[i], and the torsion extension over K is abelian by CM. The -1 quadratic twist is Q-isomorphic to E_p, so L(E_p/K,s)=L(E_p/Q,s)^2. Complex conjugation fixes Q. The authors also explicitly note after Corollary 2 that any CM E/Q with nonzero central value satisfies its assumptions.

Substituting the period, torsion and local factors gives

\[
|\Sha(E_p)|=c_p^2/4,\qquad
v_2|\Sha(E_p)|=2v_2(c_p)-2.
\]

Combining this **proved rank-zero formula** with (8), not with a conjectural prediction, yields

\[
\boxed{h=v_2(c_p)-1,\qquad
\text{first nonzero odd pairing index}=2v_2(c_p)-3.}
\tag{11}
\]

Conversely, finite stopping gives rank zero and finite 2-primary Sha, hence 2-infinity-Selmer corank zero. Burungale-Tian [BT, Theorem 1.1; the rational descent assertion, or its CM-newform formulation] applies at2 and proves a nonzero central value. Thus, within this prime family,

\[
c_p=0\quad\Longleftrightarrow\quad\text{the filtration never stops}.
\tag{12}
\]

Equations (9)-(10) then apply, but neither BT's **rank-zero** converse nor BF's **central-nonvanishing** theorem proves r=2 or exact complex order two in these remaining cases. Extending either theorem outside its hypotheses would be the same error the earlier audit was intended to prevent.

## 7. Executed finite experiment and a genuinely deeper test case

The accepted computational domain is every prime p congruent to1 modulo8 with 1<p<=1200: **44 primes, no omitted primes in that domain**. An earlier exploratory count below3000 suggested the formula and the cutoff case; this was disclosed in CONTRACT.md before acceptance, not misrepresented as preregistration before discovery.

The TypeScript checker independently computes signed ternary counts by enumerating y,z and testing the residual square, and an exactly truncated integer q-product. Both agree at all44 primes. It verifies (6), the representation-form dictionary, and independently selected 2-adic tangent residues. It also checks the rotation-orbit parity lemma for all positive integers up to150. There are669 assertions total: 11 boundary/invalid-input checks, 300 orbit checks, and358 normalization/prime-population checks. These are assertions in one executable, not669 independent proofs or curves.

| p | A_p | B_p | c_p | (u,v) | Theta_1(p,2) | h when nonzero |
|---:|---:|---:|---:|---|---:|---:|
|17|16|4|-4|(1,1)|1|1|
|41|32|16|0|(5,1)|0|not finite|
|113|32|24|8|(7,2)|0|2|
|1153|64|48|16|(33,2)|0|3|

The population contains24 cases with h=1,12 with h=2, one with h=3, and seven zero coefficients. The latter primes are41,137,257,313,353,457,761; no rank certification for that list is inferred from its coefficients.

For1153=33^2+16*2^2=1^2+32*6^2, the nonzero coefficient16 is the first coefficient divisible by16 among these primes. Since every lower eligible prime is in the iterator, this also certifies its minimality among positive primes in this residue class. Equation (11) gives Theta_1=Theta_3=0 and a nondegenerate Theta_5, with the groups stated at the beginning of this record. **The fifth pairing is theorem-derived; its local functions were not constructed.** This is a useful next arithmetic benchmark beyond113, not evidence that one new example resolves the zero-coefficient family.

The Python/SymPy checker has38 passing assertions: generic conic, tangent and norm identities; Tate input substitutions; independent full-triple counts at the four displayed primes; and finite abstract group checks. Wolfram separately returned four zero polynomial residuals and the same four exact count/sign rows, with all three grouped tests true and no warning. The finite group models are not asserted arithmetic realizations.

## 8. Verification, source scope, and what to do next

Observed versions: Node22.16.0, TypeScript5.8.3, Python3.13.5, SymPy1.14.0, Wolfram15.0.1. Run `npm run lint`, `npm run typecheck`, `npm test`, and `npm run test:symbolic`. Lint here means TypeScript's strict unused/unreachable diagnostics, not an installed ESLint/Biome run. Genuine outputs, exact Wolfram input/output, timings and replay hashes are preserved. No package provisioning or new payment was necessary.

See `sources/REGISTER.md` for source versions, theorem-to-project translations and unsuccessful acquisitions. BF and BT are checked as external theorem inputs; their complete Iwasawa-theoretic proofs were not independently reconstructed. Mortenson supplies his own proof of the precise representation theorem used. A September2026 preprint by Shisong Xu addresses a broader coefficient/Cassels-pairing comparison using CM BSD; it is recorded as overlap context, not as a dependency or a fully audited theorem here. We make no claim that the identity, stopping formula or case1153 is new to mathematics.

**Next mathematical objective:** attack the remaining implication “persistent descent forces its surviving classes to come from rational points,” rather than run an undirected larger coefficient scan. The completed dichotomy shows exactly what must be ruled out: the divisible group in (9), while also controlling the complex order at its zero. An explicit Theta_5 calculation at1153 would be an independent implementation benchmark but would not settle that implication. No all-rank/non-CM comparison, general Sha finiteness theorem, or complete BSD candidate has been obtained.

All computations described in H4 have completed. No job is continuing in the background; no publication, external contact, public repository, or prize submission was made.
