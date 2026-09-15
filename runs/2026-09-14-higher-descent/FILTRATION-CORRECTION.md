# We have not solved the Birch–Swinnerton-Dyer problem yet.

## Route correction from primary source

The previous checkpoint treated an explicit embedding of the two first-stage isogeny Selmer groups into the full [2]-Selmer group as the next required step. Fisher's primary-source formulation shows that this is unnecessary for his higher-isogeny algorithm.

In Section 2 Fisher defines S_1=Sel^(phi)(E/K) and S'_1=Sel^(phihat)(E'/K), then nested subspaces S_m subset S_1 and S'_m subset S'_1 as images of alternating higher 2-power/isogeny Selmer groups. Theorem 2.1 states that for odd m the pairing Theta_m on S_m is alternating with kernel S_(m+1); for even m, Theta_m:S_m x S'_m has left and right kernels S_(m+1),S'_(m+1). Section 4 then says that at each stage one keeps a basis for S_m directly in K^*/K^{*2}, together with equations for the corresponding higher isogeny coverings. Thus a detour through full Kummer triples is not a prerequisite for continuing Fisher's construction.

## Immediate consequence for E_113

Our authenticated local calculations give

    S_1 = {1,113},  dim_F2 S_1 = 1,
    S'_1 = {1,2},   dim_F2 S'_1 = 1.

Because Theta_1 and Theta'_1 are alternating bilinear forms on one-dimensional F2 spaces, each is identically zero. Fisher Theorem 2.1 therefore gives, without any analytic-rank input,

    S_2 = S_1 = <113>,
    S'_2 = S'_1 = <2>.

This is a genuine algebraic advance: both nontrivial first-stage generators are certified to lift one stage in the higher-isogeny filtration. It does NOT determine S_3 or the rank. The next decisive object is the even pairing

    Theta_2 : S_2 x S'_2 -> F_2.

Since both spaces are one-dimensional, a single value Theta_2(113,2) determines the entire pairing. If it is nonzero, S_3=S'_3=0; if zero, both generators survive to the next stage. Computing this value requires the explicit 4-cover/pushout-function data described by Fisher, not the full-Selmer embedding.

## Source

T. Fisher, Higher descents on an elliptic curve with a rational 2-torsion point, arXiv:1509.03234, especially Section 2 (definitions of S_m,S'_m and Theorem 2.1) and Section 4 (basis in K^*/K^{*2} plus higher covering equations).

No complete BSD candidate or new theorem is claimed.