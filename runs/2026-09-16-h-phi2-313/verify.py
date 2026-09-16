from __future__ import annotations
from fractions import Fraction
from hashlib import sha256
from math import isqrt
import json


def fplus(t: Fraction) -> Fraction:
    return t**4 + 6*t*t + 1

def fminus(t: Fraction) -> Fraction:
    return t**4 - 6*t*t + 1

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
    assert wo*wo == fplus(xo)*fminus(yo)
    return xo, yo, wo, c


def vp(n: int, p: int) -> int:
    n = abs(n)
    k = 0
    while n and n % p == 0:
        n //= p
        k += 1
    return k


def is_prime_trial(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    q = 3
    while q*q <= n:
        if n % q == 0:
            return False
        q += 2
    return True

x0 = Fraction(6127,1862)
y0 = Fraction(37,14)
w0 = Fraction(25815863383,679540624)
assert w0*w0 == fplus(x0)*fminus(y0)

x1,y1,w1,c1 = phi(x0,y0,w0)
assert x1 == Fraction(43527762774033482635941503,35975915953349079904919842)
x2,y2,w2,c2 = phi(x1,y1,w1)
assert c1 == c2

A = abs(x2.numerator)
B = x2.denominator
G = A**4 + 6*A*A*B*B + B**4
assert Fraction(G,B**4) == fplus(x2)

vals = {p: vp(G,p) for p in [2,13,17,73,113,137,257,313,13873,28657,69457,176809,1389623369]}
expected = {2:0,13:0,17:4,73:1,113:1,137:0,257:0,313:1,13873:2,28657:1,69457:1,176809:1,1389623369:1}
assert vals == expected
for p in [73,113,313,28657,69457,176809,1389623369]:
    assert is_prime_trial(p)
assert G % 313 == 0
q = G // 313
assert isqrt(q)**2 != q

summary = {
    "status":"passed",
    "word":"H,Phi,Phi",
    "fiber_equal": c1 == c2,
    "digits":{"A":len(str(A)),"B":len(str(B)),"G":len(str(G))},
    "G_sha256":sha256(str(G).encode()).hexdigest(),
    "valuations":{str(k):v for k,v in vals.items()},
    "G_over_313_is_square":False,
    "conclusion":"137 is absent, 313 occurs to odd valuation, but 73 also occurs to odd valuation so the squareclass is not 313 alone"
}
print(json.dumps(summary,indent=2))
