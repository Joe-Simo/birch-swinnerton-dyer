from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction
from hashlib import sha256
from math import isqrt
import json

D = 137

@dataclass(frozen=True)
class K:
    a: Fraction
    b: Fraction = Fraction(0)
    @staticmethod
    def coerce(x: K | Fraction | int) -> K:
        return x if isinstance(x, K) else K(Fraction(x))
    def __add__(self, other: K | Fraction | int) -> K:
        o = K.coerce(other); return K(self.a + o.a, self.b + o.b)
    __radd__ = __add__
    def __neg__(self) -> K: return K(-self.a, -self.b)
    def __sub__(self, other: K | Fraction | int) -> K: return self + (-K.coerce(other))
    def __rsub__(self, other: K | Fraction | int) -> K: return K.coerce(other) - self
    def __mul__(self, other: K | Fraction | int) -> K:
        o = K.coerce(other); return K(self.a*o.a + D*self.b*o.b, self.a*o.b + self.b*o.a)
    __rmul__ = __mul__
    def inv(self) -> K:
        den = self.a*self.a - D*self.b*self.b
        if den == 0: raise ZeroDivisionError
        return K(self.a/den, -self.b/den)
    def __truediv__(self, other: K | Fraction | int) -> K: return self * K.coerce(other).inv()
    def __rtruediv__(self, other: K | Fraction | int) -> K: return K.coerce(other) / self

Point = tuple[K, K] | None

def add(P: Point, Q: Point) -> Point:
    if P is None: return Q
    if Q is None: return P
    x1,y1=P; x2,y2=Q
    if x1 == x2 and y1 == -y2: return None
    if P == Q:
        if y1 == K(Fraction(0)): return None
        lam=(3*x1*x1-1)/(2*y1)
    else:
        lam=(y2-y1)/(x2-x1)
    x3=lam*lam-x1-x2
    return x3, lam*(x1-x3)-y1

def neg(P: Point) -> Point: return None if P is None else (P[0],-P[1])

def mul(n: int, P: Point) -> Point:
    if n < 0: return mul(-n,neg(P))
    R=None; A=P
    while n:
        if n & 1: R=add(R,A)
        A=add(A,A); n//=2
    return R

def quartic_to_E(t: Fraction, r: K, e: int) -> Point:
    T=K(t)
    return (r+1+e*T*T)/(2*T*T), (r+1+3*e*T*T)/(2*T*T*T)

def E_to_quartic(P: Point, e: int) -> tuple[Fraction,K]:
    assert P is not None
    u,v=P
    t=(u+e)/v
    assert t.b == 0
    r=(2*u-e)*t*t-1
    assert r.a == 0
    return t.a,r

def phi(x: Fraction,y: Fraction,W: Fraction) -> tuple[Fraction,Fraction,Fraction]:
    gap=x*x-y*y+6
    C=(x*x*y*y+1)/gap
    K0=6*C-1
    a=C; b=C*C+K0; d=C*K0
    z=y*(x*x+C)
    fp=4*a*x**3+2*b*x
    fpp=12*a*x*x+2*b
    fppp=24*a*x
    h1=fp/(2*z)
    h2=(fpp/2-h1*h1)/(2*z)
    r3=fppp/6-2*h1*h2
    r4=C-h2*h2
    dx=-r3/r4
    xo=x+dx
    zo=z+h1*dx+h2*dx*dx
    yo=zo/(xo*xo+C)
    Wo=W*(xo*xo-yo*yo+6)/gap
    assert Wo*Wo == (xo**4+6*xo*xo+1)*(yo**4-6*yo*yo+1)
    return xo,yo,Wo

def frac_mod(q: Fraction,p: int) -> int:
    return (q.numerator % p) * pow(q.denominator % p,-1,p) % p

def fp(t: int,p: int) -> int: return (t**4+6*t*t+1)%p

def leg(a: int,p: int) -> int:
    a%=p
    if a==0:return 0
    return 1 if pow(a,(p-1)//2,p)==1 else -1

s=K(Fraction(0),Fraction(1))
P=quartic_to_E(Fraction(1,14),K(Fraction(0),Fraction(17,196)),1)
Q=quartic_to_E(Fraction(37,14),K(Fraction(0),Fraction(47,196)),-1)
assert P is not None and Q is not None
assert P[1]*P[1] == P[0]*P[0]*P[0]-P[0]
assert Q[1]*Q[1] == Q[0]*Q[0]*Q[0]-Q[0]

# H,H,v: P2=P-4Q, Q2=Q+2P2.
P2=add(P,mul(-4,Q)); assert P2 is not None
Q2=add(Q,mul(2,P2)); assert Q2 is not None
x,rp=E_to_quartic(P2,1)
y,rm=E_to_quartic(Q2,-1)
Wk=rp*rm
assert Wk.b == 0
W=Wk.a
assert W*W == (x**4+6*x*x+1)*(y**4-6*y*y+1)
xo,yo,Wo=phi(x,y,W)

# Exact local reductions agree with the finite checker and target characters.
assert (frac_mod(x,13),frac_mod(y,13),frac_mod(xo,13),fp(frac_mod(xo,13),13)) == (7,10,5,9)
assert (frac_mod(x,47),frac_mod(y,47),frac_mod(xo,47),fp(frac_mod(xo,47),47)) == (37,7,10,26)
assert leg(257,13)==leg(313,13)==1
assert leg(257,47)==leg(313,47)==-1
assert leg(9,13)==1 and leg(26,47)==-1

A=abs(xo.numerator); B=xo.denominator
G=A**4+6*A*A*B*B+B**4
assert G % 257 != 0
assert G % 313 != 0
for prime in (257,313):
    if G % prime == 0:
        q=G//prime
        assert isqrt(q)**2 != q

summary={
    "status":"passed",
    "word":"H,H,v,Phi",
    "pre_phi_mod_13":[frac_mod(x,13),frac_mod(y,13)],
    "post_phi_mod_13":[frac_mod(xo,13),fp(frac_mod(xo,13),13)],
    "pre_phi_mod_47":[frac_mod(x,47),frac_mod(y,47)],
    "post_phi_mod_47":[frac_mod(xo,47),fp(frac_mod(xo,47),47)],
    "x_num_digits":len(str(A)),
    "x_den_digits":len(str(B)),
    "G_digits":len(str(G)),
    "G_sha256":sha256(str(G).encode()).hexdigest(),
    "v257":0,
    "v313":0
}
print(json.dumps(summary,indent=2))
