from __future__ import annotations
from fractions import Fraction
from hashlib import sha256
from math import isqrt
import json


def phi(x: Fraction, y: Fraction, w: Fraction):
    gap = x*x - y*y + 6
    assert gap != 0
    c = (x*x*y*y + 1) / gap
    k = 6*c - 1
    a, b, d = c, c*c + k, c*k
    z = y * (x*x + c)
    assert z != 0
    fp = 4*a*x**3 + 2*b*x
    fpp = 12*a*x*x + 2*b
    fppp = 24*a*x
    h1 = fp / (2*z)
    h2 = (fpp/2 - h1*h1) / (2*z)
    r3 = fppp/6 - 2*h1*h2
    r4 = c - h2*h2
    assert r4 != 0
    dx = -r3/r4
    xo = x + dx
    zo = z + h1*dx + h2*dx*dx
    den = xo*xo + c
    assert den != 0
    yo = zo / den
    wo = w * (xo*xo - yo*yo + 6) / gap
    assert wo*wo == (xo**4 + 6*xo*xo + 1) * (yo**4 - 6*yo*yo + 1)
    return xo, yo, wo, c


def vp(n: int, p: int) -> int:
    n = abs(n)
    out = 0
    while n % p == 0:
        out += 1
        n //= p
    return out


def is_prime_trial(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    q = 3
    while q <= isqrt(n):
        if n % q == 0:
            return False
        q += 2
    return True


def point_on_E(G: int, t: Fraction, u: Fraction, e: int):
    X = Fraction(G) * (t*t + e)**2 / (4*t*t)
    Y = Fraction(G*G) * u * (t**4 - 1) / (8*t**3)
    assert Y*Y == X**3 - G*G*X
    return X, Y

x0 = Fraction(1,14)
y0 = Fraction(37,14)
w0 = Fraction(137*17*47,196**2)
assert w0*w0 == (x0**4 + 6*x0*x0 + 1) * (y0**4 - 6*y0*y0 + 1)

x1,y1,w1,c1 = phi(x0,y0,w0)
x2,y2,w2,c2 = phi(x1,y1,w1)
assert c1 == c2

def modq(q: Fraction,p: int) -> int:
    return (q.numerator % p) * pow(q.denominator % p,-1,p) % p

assert (modq(x0,313),modq(y0,313)) == (246,25)
assert (modq(x1,313),modq(y1,313)) == (88,97)
assert (modq(x2,313),modq(y2,313)) == (105,119)
assert (pow(modq(x2,313),4,313) + 6*pow(modq(x2,313),2,313) + 1) % 313 == 0

A = abs(x2.numerator)
B = x2.denominator
assert A > 0 and B > 0
G = A**4 + 6*A*A*B*B + B**4
assert Fraction(G,B**4) == x2**4 + 6*x2*x2 + 1

vals = {p: vp(G,p) for p in (2,13,17,137,257,313,1409,2017)}
assert vals == {2:0,13:0,17:2,137:1,257:0,313:1,1409:1,2017:1}
assert is_prime_trial(137) and is_prime_trial(313) and is_prime_trial(1409) and is_prime_trial(2017)
assert G % (17**2 * 137 * 313 * 1409 * 2017) == 0

u_plus = Fraction(1,B*B)
u_minus = w2 * B*B / G
assert x2**4 + 6*x2*x2 + 1 == G*u_plus*u_plus
assert y2**4 - 6*y2*y2 + 1 == G*u_minus*u_minus
P_plus = point_on_E(G,x2,u_plus,+1)
P_minus = point_on_E(G,y2,u_minus,-1)
assert P_plus[1] != 0 and P_minus[1] != 0

summary = {
    'status':'passed',
    'word':'Phi^2',
    'fiber_C': [c1.numerator,c1.denominator],
    'mod313': {
        'seed':[modq(x0,313),modq(y0,313)],
        'after_phi':[modq(x1,313),modq(y1,313)],
        'after_phi2':[modq(x2,313),modq(y2,313)],
    },
    'x1_num_digits':len(str(abs(x1.numerator))),
    'x1_den_digits':len(str(x1.denominator)),
    'x2_num_digits':len(str(A)),
    'x2_den_digits':len(str(B)),
    'G_digits':len(str(G)),
    'G_sha256':sha256(str(G).encode()).hexdigest(),
    'valuations':{str(k):v for k,v in vals.items()},
    'conclusion':'squarefree kernel contains both 137 and 313; it is not 313 alone; inherited Kummer lemma gives rank at least 2 for its squarefree normalization'
}
print(json.dumps(summary,indent=2))
