# We have not solved the Birch–Swinnerton-Dyer problem yet.

## H27: odd-prime synchronization is independent, so finite auxiliary character sieves cannot obstruct arbitrary mixed words

Continuation of H26. This checkpoint corrects the strategic expectation that synchronizing the target prime 313 with one or more distinct odd auxiliary primes might eventually produce an empty mixed-word orbit. For the full mixed shear group, the opposite happens at coprime odd moduli.

### 1. Exact group-theoretic statement

Let

    H=[[1,-2],[0,1]],   V=[[1,0],[-2,1]].

H26 independently checked that for each tested odd prime p the reductions of H and V generate all of `SL_2(F_p)`. More generally, because 2 is invertible modulo any odd modulus N, powers of H and V supply all elementary matrices

    E12(a)=[[1,a],[0,1]],   E21(b)=[[1,0],[b,1]]

for arbitrary residues a,b mod N: choose k with `-2k=a mod N` or `-2k=b mod N`. Over `Z/NZ`, these elementary matrices generate `SL_2(Z/NZ)` (prime-power reduction followed by CRT, or the standard elementary reduction argument).

Hence for every odd N,

    <H,V> mod N = SL_2(Z/NZ).

Now let M,N be coprime odd integers. CRT gives

    Z/(MN)Z ~= Z/MZ x Z/NZ

and therefore

    SL_2(Z/(MN)Z) ~= SL_2(Z/MZ) x SL_2(Z/NZ).

Since the mixed shear image modulo MN is the full left-hand group, **any prescribed pair of matrix residues at M and N is realized by one global mixed word**. The same holds for any finite collection of pairwise coprime odd moduli.

### 2. Consequence for H25/H26

Suppose a target-compatible matrix state exists at 313 and a character-compatible state exists at each auxiliary odd prime ell_i, with all moduli pairwise coprime. H25 already proves that target-compatible states at 313 exist abundantly: 592 regular final-Phi zeros plus 1128 boundary states in its local orbit. If each auxiliary acceptance set is nonempty, CRT synchronization cannot make the product empty. A global mixed word can realize the chosen local matrices simultaneously.

Therefore the H22/H24 strategy of adding independent odd-prime character constraints cannot possibly yield an all-mixed-word obstruction unless some **single local acceptance set is itself empty**, or unless the argument introduces coupled conditions not decomposing across coprime local matrix images.

This explains why H25's shortest-representative failures do not scale to arbitrary words: longer words have enough congruence freedom to repair every finite list of independent odd-prime conditions simultaneously.

### 3. Verification

`verify.py` independently enumerates the H/V matrix closure modulo 15, 21, 35 and 65. It checks that the sizes equal

    |SL2(Z/15)| = |SL2(F3)|*|SL2(F5)| = 2880,
    |SL2(Z/21)| = |SL2(F3)|*|SL2(F7)| = 8064,
    |SL2(Z/35)| = |SL2(F5)|*|SL2(F7)| = 40320,
    |SL2(Z/65)| = |SL2(F5)|*|SL2(F13)| = 262080.

The checker also explicitly constructs elementary powers `H^k=E12(a)` and `V^k=E21(b)` for every residue a,b for the small odd moduli 3,5,7,9,13,15, confirming the key invertibility-of-2 mechanism. These computations are finite cross-checks of the proof, not its basis.

### 4. Revised research obligation

The mixed route is not locally obstructed by any finite menu of independent odd-prime character tests once every local acceptance set is nonempty. The next useful question is therefore global and Diophantine rather than another auxiliary-prime sieve:

1. derive the rational squareclass-transfer function for a low-dimensional parametrized subfamily of mixed matrices (for example `H^a V^b H^c` between the two Phi maps);
2. impose the exact equation that its plus quartic value equals `313 * square`;
3. determine the resulting curve/surface geometry and search for a rational point or prove an obstruction using genuine global arithmetic.

This is a strategic narrowing, not progress toward the analytic-rank half of BSD. General BSD remains unresolved.
