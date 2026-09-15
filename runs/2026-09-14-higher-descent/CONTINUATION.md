# We have not solved the Birch–Swinnerton-Dyer problem yet.

Continuation checkpoint after H2. This file records only what has been established in the current continuation; it does not replace CHECKPOINT.md.

## Executed literature follow-up

The next route in CHECKPOINT.md was checked against T. Fisher, *Higher descents on an elliptic curve with a rational 2-torsion point*, Math. Comp. 86 (2017), 2493–2518 (preprint arXiv:1509.03234). The paper explicitly develops practical 8-descent for elliptic curves over Q with full rational 2-torsion. Thus the requested 4-to-8 calculation is a legitimate explicit-descent problem, not an invented construction.

## What remains missing

No explicit 4-covering of E_113 above a chosen nonzero pure Sel_2 class has yet been certified in this continuation. In particular, there is not yet a checked list of companion quadrics, a verified covering map to E_113, local points at every relevant place, or the new pushout functions on that 4-covering. Therefore no local Hilbert-symbol computation is being claimed.

The previously established global endpoint remains the test oracle: the second pure pairing for E_113 has rank 2, whereas for E_41 it is zero. Any explicit higher-descent implementation must reproduce that distinction without using the rank-zero analytic theorem as an input to the local calculation.

## Methodological result

The earlier rejected shortcut remains rejected: pulling first-stage functions back to the 4-cover makes them squares and cannot detect the nonzero second pairing. The explicit 8-descent must construct the new functions/divisors on the higher covering itself.

## Next executable step

Extract Fisher's exact equations for the full-rational-2-torsion 8-descent specialization and instantiate them for E_113:y^2=x^3-113^2 x. Choose one nonzero pure Sel_2 class, construct a locally soluble 4-covering representing a lift, and verify its map algebraically before attempting any local symbol. If the exact equations cannot be authenticated from the source, do not guess them; retain this as the blocker and move to a different independently certifiable BSD route.

No complete BSD candidate, formal proof, independent expert review, publication, submission, or prize claim exists.