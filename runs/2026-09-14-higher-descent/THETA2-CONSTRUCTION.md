# We have not solved the Birch–Swinnerton-Dyer problem yet.

Primary-source continuation using T. Fisher, arXiv:1509.03234v1, Sections 2-5.

## Correct stage and remaining bit

Theorem 2.1(ii) gives Theta_2:S_2 x S'_2 -> F_2 with left kernel S_3 and right kernel S'_3. We already proved S_2=<113> and S'_2=<2>. Hence Theta_2(113,2) is the single remaining bit at this stage. A nonzero value kills both next stages; zero leaves both one-dimensional.

## Explicit C1 and conic parametrisation

For E_113:y^2=x(x^2-113^2), Fisher equation (8) with a=0, b=-113^2 and xi1=113 is

    C1: r^2 = 113 s^4 - 113 t^4.

Put S=s^2 and T=t^2. The conic is

    R^2 = 113(S^2-T^2),

with rational point (S:T:R)=(1:1:0). Parametrising lines through this point gives the exact binary quadratic forms

    f(l,m)=l^2+113m^2,
    g(l,m)=l^2-113m^2,
    h(l,m)=226lm.

Wolfram independently simplified

    h^2 - 113(f^2-g^2)

to zero identically. Thus

    (s^2:t^2:r)=(f:g:h)

is an authenticated instance of Fisher equation (9), up to the common projective scale represented by xi2 in equation (10).

## Pushout function now explicit

Fisher's pushout-function paragraph following diagram (14) gives on C1

    f2 = f(l,m)/m^2.

For this E113 parametrisation,

    f2 = (l^2+113m^2)/m^2.

The next lift C2 therefore has simultaneous conics

    l^2+113m^2 = xi2 s^2,
    l^2-113m^2 = xi2 t^2,

for a squareclass xi2 chosen so that C2 is everywhere locally soluble. The abstract equality S2=S1 proves that at least one such lift exists, but it does not identify xi2; no value is guessed here.

## Next exact calculation

Determine xi2 by exact local analysis of these simultaneous conics at all relevant places. Once an everywhere locally soluble C2 lift is fixed, choose certified local points on C1/C2 in Fisher's convention and evaluate

    sum_v (f2(P_v),2)_v.

Only finitely many places contribute, but the bad set must be derived from the chosen integral model and f2 rather than assumed to be only {2,113,infinity}. This sum is Theta_2(113,2).

No analytic rank input, numerical L-value, BSD assumption, or guessed covering is used here. No complete BSD solution is claimed.