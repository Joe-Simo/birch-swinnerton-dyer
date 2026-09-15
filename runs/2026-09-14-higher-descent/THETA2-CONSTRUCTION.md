# We have not solved the Birch–Swinnerton-Dyer problem yet.

Primary-source continuation using T. Fisher, arXiv:1509.03234v1, Sections 2-5.

## Correction to the previous target description

The previous checkpoint correctly reduced the next arithmetic datum to the even pairing Theta_2 on the one-dimensional spaces S_2=<113> and S'_2=<2>. However its wording suggested immediately constructing a 4-covering. Fisher's definitions show that for m=2, an element of S_2 is represented by a lift in Sel(2), i.e. a 2-covering at this stage. The 4-coverings in Section 5 occur later in the alternating chain C1,...,C4. This stage distinction is now fixed.

Theorem 2.1(ii) states that Theta_2:S_2 x S'_2 -> F_2 has left kernel S_3 and right kernel S'_3. Since both spaces are one-dimensional, one nonzero value Theta_2(113,2)=1 kills both next stages; value zero leaves both unchanged.

## Exact construction to execute

Fisher Section 3 gives the computational formula. If x is represented by an everywhere locally soluble covering C and f is a pushout function with div(f)=2b for the rational 2-torsion divisor class, then for y represented by a squareclass one evaluates local Hilbert norm residue symbols (f(P_v),y)_v and sums over v. Section 5 gives the concrete covering chain for E:y^2=x(x^2+a x+b). For the connecting squareclass xi_1 the first curve is

    C1: r^2=xi_1 s^4+a s^2 t^2+(b/xi_1)t^4.

A conic parametrisation gives (s^2:t^2:r)=(f(l,m):g(l,m):h(l,m)), and the next pushout function is f_2=f(l,m)/m^2. Thus to compute Theta_2 for the present generators we must:

1. fix which side of Fisher's alternating E/E' convention carries xi_1=113 and which carries the test squareclass 2;
2. construct an everywhere locally soluble Sel(2) lift of 113 by parametrising the appropriate conic associated to C1;
3. obtain the authenticated pushout function f_2 from that parametrisation;
4. choose local points P_v only at the finite set of potentially nontrivial places (at minimum 2,113 and infinity, with any extra primes introduced by the chosen model/function included rather than assumed away);
5. compute the Hilbert symbols (f_2(P_v),2)_v exactly and sum them in F_2.

The source explicitly warns that the covering/lift must be built before the pairing is evaluated; finite residue searches are not substitutes for local points on the actual covering.

## Source audit

Fisher Theorem 2.1: odd m gives alternating self-pairings with next-stage kernels; even m gives S_m x S'_m with left/right kernels S_{m+1},S'_{m+1}. Section 4 Algorithm 4.1 describes lifting through Sel(m). Section 5 equations (8)-(14) give C1 through C4 and pushout functions f1 through f4. In particular C1 is the binary quartic above and f2 is obtained only after a conic parametrisation.

No value of Theta_2(113,2) is claimed yet. No BSD solution or new theorem is claimed.