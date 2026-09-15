# We have not solved the Birch–Swinnerton-Dyer problem yet.

Both first-stage isogeny Selmer groups have now been computed locally: one is {1,113}, the dual is {1,2}. The next task is their embedding into the full [2]-Selmer group.

## Full Kummer torsion coordinates rechecked

For E_113:y^2=x^3-113^2 x, with delta(x,y)=(x-113,x+113,x) away from 2-torsion, the previously audited special triples are

    T+=(113,0): (2,226,113)
    T0=(0,0): (-113,113,-1)
    T-=(-113,0): (-226,2,-113).

In the squareclass basis (-1,2,113), coordinate by coordinate, Wolfram gives

    T+ : 0 1 0 | 0 1 1 | 0 0 1
    T0 : 1 0 1 | 0 0 1 | 1 0 0
    T- : 1 1 1 | 0 1 0 | 1 0 1.

Their F2 rank is two, as required by T+ + T0 = T- in E[2]. This is a consistency check only.

## Important boundary

It is NOT valid to identify the isogeny squareclass generator 113 or 2 with one of these full Kummer triples merely by matching a coordinate. The maps between the phi- and phihat-Selmer groups and Sel_2(E) arise from the cohomology exact sequence attached to 0 -> E[phi] -> E[2] -> E'[phihat] -> 0 (with conventions depending on which isogeny is named phi). An explicit cocycle/coordinate map must be authenticated before choosing the higher-descent lift.

Thus the local computation has genuinely reduced the input groups, but it has not yet selected a unique nonzero pure full-Selmer class. The next step is to extract the exact embedding map from Fisher's Section 5 notation (or another primary source), translate it to the fixed models E_113 and E'_113, and verify it on the three rational 2-torsion classes above. Only after that verification should Fisher equations (9)-(13) be instantiated.

No BSD solution or new theorem is claimed.