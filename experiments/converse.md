# Follow-up F2: a valid use of the CM 2-converse

This follow-up refines checkpoint 1's central-zero classification. It does not produce a complete BSD candidate or certify an exact positive analytic rank.

Let s2=dim_F2 Sel_2(E/Q)-dim_F2 E(Q)[2]. Put B=Sel_(2^infinity)(E/Q), and let r=rank E(Q). The two Kummer exact sequences give

    s2 = r + dim_F2 Sha(E/Q)[2],
    0 -> E(Q) tensor Q_2/Z_2 -> B -> Sha(E/Q)[2^infinity] -> 0.

The left group in the second sequence is (Q_2/Z_2)^r, so multiplication by 2 on it is surjective. The kernel/cokernel exact sequence for multiplication by 2 therefore gives

    0 -> (Z/2)^r -> B[2] -> Sha(E/Q)[2] -> 0.

Consequently dim_F2 B[2]=s2. If s2=0, then B[2]=0, hence B=0: any nonzero element of a 2-primary torsion group has a nonzero multiple of order 2. This proves corank_Z2 B=0 without assuming Sha finite. The CM rank-zero 2-converse in Burungale–Tian, Theorem 1.1 [S4], now applies to every E_n in our family, including at the bad prime 2. Its conclusion is L(E_n,1)!=0. The original Monsky-proof access qualification in checkpoint 1 still applies to identifying the matrix nullity with s2.

On the existing 209 F1 inputs, exactly 58 matrices have nullity zero. All 58 have nonzero Tunnell coefficient. There is no conflicting case. This applies a known theorem with its actual hypothesis; it is not proof by matching two database labels.

**Why the converse shortcut remains false.** For s>0, the abstract groups (Z/2)^s and (Q_2/Z_2)^s have 2-torsion dimension s but coranks 0 and s. Thus positive finite-level dimension alone cannot identify the corank. More generally, (Z/2^m)^s and (Q_2/Z_2)^s have identical torsion subgroups killed by 2^j for every j<=m, but different coranks. These are information-theoretic group examples, not assertions that every group is realized by an elliptic curve.

## Exact parity refinement

The root-number rule explicitly recorded in [S4, footnote 2, citing Birch–Stephens] is epsilon(E_n)=+1 precisely for positive squarefree n congruent to 1,2,3 modulo 8. Only odd n occur here. The completed L-function satisfies

    Lambda(1+z)=epsilon*Lambda(1-z).

Its other completion factors are nonzero at s=1. A positive sign makes its Taylor series even; a negative sign makes it odd. A Tunnell coefficient equal to zero proves that its constant term is zero. Therefore among the 126 zero coefficients in F1:

- 18 have certified even analytic order at least 2;
- 108 have certified odd analytic order at least 1.

E_41 is in the first group. Thus the run now has algebraic rank 2 (with the recorded external descent dependency) and independent analytic order >=2, even. An order-2 upper bound has NOT been proved. In particular, central vanishing plus parity is not a certificate that its second derivative is nonzero.

Reproduce this follow-up with `python3 experiments/converse.py` after F1. Exact classification lists are in `results/converse.json`. This script consumes F1's checked output; it is not a new independent implementation of the original arithmetic.
