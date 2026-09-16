# H23 source register

## Francesc Castella, *Generalised Kato classes on CM elliptic curves of rank 2*

Author-hosted current PDF inspected 2026-09-16:
https://web.math.ucsb.edu/~castella/Kato-Schoen.pdf

The file identifies the February 2026 version of the paper. Relevant exact statements:

- Theorem B, PDF p.4: assumes `L(E,s)` vanishes to positive even order at `s=1`; proves `kappa_p != 0 => dim_Qp Sel(Q,V_pE)=2`, and when the Selmer dimension is 2 characterizes `kappa_p != 0` by nonvanishing of the localization map. This theorem does **not** deduce the complex analytic order from Selmer dimension 2.
- Theorem C, PDF p.5: additionally assumes finiteness of the p-primary Sha and specified orders of two p-adic L-functions (`ord L_p=2`, `ord L_p^*=1`) to construct a two-dimensional Selmer basis.
- Remark 1.3.1, PDF p.5: states the predicted p-adic equivalence and records only a lower bound on the p-adic orders from Selmer dimension 2; equality is tied to nondegeneracy of a p-adic height pairing (and extra conditions on the starred side).

Project implication: this paper is relevant rank-two technology but does not supply the missing unconditional comparison `dim Sel=2 => ord_{s=1} L(E,s)=2` for the complex Hasse-Weil L-function. It therefore cannot close BSD for the rank-two congruent-number families constructed in this repository.

Older contextual paper checked through the published/author-hosted text:
Francesc Castella and Ming-Lun Hsieh, *On the non-vanishing of generalized Kato classes for elliptic curves of rank 2*, Forum of Mathematics, Sigma 10 (2022), e12, DOI 10.1017/fms.2021.85. Its rank-two Selmer results likewise do not identify Selmer dimension 2 with complex analytic order 2.
