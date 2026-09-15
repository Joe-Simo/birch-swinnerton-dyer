# We have not solved the Birch–Swinnerton-Dyer problem yet.

## Source-authenticated connecting map

Fisher arXiv:1509.03234v1, Section 5, equation (7) and lines surrounding equation (8), fixes the convention needed here. For E:y^2=x(x^2+a x+b), with phi:E->E' having kernel {(O),(0,0)}, the connecting map for the dual isogeny is

    delta: E(K)/hat(phi)E'(K) -> K^*/K^{*2},
    P=(x,y) |-> x

away from O and T=(0,0). Fisher then writes x=xi1(s/t)^2 and obtains

    r^2=xi1 s^4+a s^2 t^2+(b/xi1)t^4.

A second source check (Silverman, Arithmetic of Elliptic Curves, X.4 Proposition 4.9 as exposed by the web source) gives the complementary connecting map on E': delta(O)=1, delta((0,0))=a^2-4b, delta((X,Y))=X for X nonzero, with homogeneous spaces C_d and the exact Selmer local-solubility criterion. This is used only to authenticate the convention and special kernel value; it is not a BSD input.

For E_113, a=0,b=-113^2. Thus Fisher's first covering is exactly

    r^2=d s^4-(113^2/d)t^4.

At the real place, if d<0 then both terms on the right are nonpositive and at least one is strictly negative for every nonzero projective pair (s,t). Therefore C_d(R) is empty for d<0. This is an exact proof, not a finite search. Consequently the four negative candidate squareclasses -1,-2,-113,-226 are excluded from this particular dual-isogeny Selmer group.

The only remaining squareclasses supported on the bad set {2,113,infinity} are

    d in {1,2,113,226}.

The kernel special value on E itself is b=-113^2, which is the squareclass -1; this belongs to the *other* connecting-map convention (E(Q)/hat(phi)E'(Q)) only if interpreted with its correct source/target. The apparent tension with the real exclusion is precisely why the two connecting maps must not be conflated. Fisher's delta on E is the dual-isogeny quotient and its special value at T was not supplied in the quoted line; do not infer it by swapping formulas without tracking the scaling in the dual model.

## Correction to earlier computation

The previous bounded integer search was not reliable evidence and remains refuted. The real-place argument above is the first rigorous elimination of candidate squareclasses in this continuation.

## Next step

Compute genuine Q_2 and Q_113 solubility for d=1,2,113,226 using the authenticated quartics. The d=1 class has the obvious rational point t=0,s=r=1 and is therefore globally soluble. The d=113 class has r^2=113(s^4-t^4), so t=s gives r=0 and a rational projective point; it too is globally soluble on the first covering. Thus only d=2 and d=226 require serious local analysis at this stage. Determine whether either survives at both 2 and 113. Then match the surviving isogeny classes into the full [2]-Selmer basis before constructing the 4-cover.

Evidence status: source-authenticated convention plus exact real-place proof. No complete BSD candidate.