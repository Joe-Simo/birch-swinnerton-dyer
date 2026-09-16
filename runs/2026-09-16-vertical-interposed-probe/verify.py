from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction
from hashlib import sha256
from math import isqrt
import sys

sys.set_int_max_str_digits(1_000_000)

@dataclass(frozen=True)
class K:
    a: Fraction
    b: Fraction
    D: int
    @staticmethod
    def c(x, D):
        return x if isinstance(x, K) else K(Fraction(x), Fraction(0), D)
    def __add__(self, o):
        o=K.c(o,self.D); return K(self.a+o.a,self.b+o.b,self.D)
    __radd__=__add__
    def __neg__(self): return K(-self.a,-self.b,self.D)
    def __sub__(self,o): return self+(-K.c(o,self.D))
    def __rsub__(self,o): return K.c(o,self.D)-self
    def __mul__(self,o):
        o=K.c(o,self.D); return K(self.a*o.a+self.D*self.b*o.b,self.a*o.b+self.b*o.a,self.D)
    __rmul__=__mul__
    def inv(self):
        d=self.a*self.a-self.D*self.b*self.b
        if d==0: raise ZeroDivisionError
        return K(self.a/d,-self.b/d,self.D)
    def __truediv__(self,o): return self*K.c(o,self.D).inv()
    def __rtruediv__(self,o): return K.c(o,self.D)/self

Point=tuple[K,K]|None

def add(P:Point,Q:Point)->Point:
    if P is None:return Q
    if Q is None:return P
    x,y=P;u,v=Q
    if x==u and y==-v:return None
    lam=(3*x*x-1)/(2*y) if P==Q else (v-y)/(u-x)
    X=lam*lam-x-u
    return X,lam*(x-X)-y

def neg(P:Point)->Point:return None if P is None else(P[0],-P[1])
def mul(n:int,P:Point)->Point:
    if n<0:return mul(-n,neg(P))
    R=None
    while n:
        if n&1:R=add(R,P)
        P=add(P,P);n//=2
    return R

def q2e(t:Fraction,r:K,e:int)->Point:
    T=K(t,Fraction(0),r.D);tt=T*T
    return (r+1+e*tt)/(2*tt),(r+1+3*e*tt)/(2*tt*T)

def e2q(P:Point,e:int)->tuple[Fraction,K]:
    assert P is not None
    u,v=P;t=(u+e)/v
    assert t.b==0
    r=(2*u-e)*t*t-1
    assert r.a==0
    return t.a,r

def fplus(t:Fraction)->Fraction:return t**4+6*t*t+1
def fminus(t:Fraction)->Fraction:return t**4-6*t*t+1

def phi(x:Fraction,y:Fraction,w:Fraction):
    gap=x*x-y*y+6; assert gap!=0
    c=(x*x*y*y+1)/gap;k=6*c-1;a=c;b=c*c+k
    z=y*(x*x+c); assert z!=0
    f1=4*a*x**3+2*b*x;f2=12*a*x*x+2*b;f3=24*a*x
    h1=f1/(2*z);h2=(f2/2-h1*h1)/(2*z)
    r3=f3/6-2*h1*h2;r4=c-h2*h2;assert r4!=0
    dx=-r3/r4;X=x+dx;Z=z+h1*dx+h2*dx*dx;den=X*X+c;assert den!=0
    Y=Z/den;W=w*(X*X-Y*Y+6)/gap
    assert W*W==fplus(X)*fminus(Y)
    return X,Y,W

def surface_points(x:Fraction,y:Fraction,w:Fraction):
    A=abs(x.numerator);B=x.denominator;G=A**4+6*A*A*B*B+B**4
    rp=K(Fraction(0),Fraction(1,B*B),G)
    rm=K(Fraction(0),w*B*B/G,G)
    return G,q2e(x,rp,1),q2e(y,rm,-1)

def vp(n:int,p:int)->int:
    n=abs(n);k=0
    while n%p==0:k+=1;n//=p
    return k

# Original 137 surface, then H^{-1}: P -> P+2Q.
P=q2e(Fraction(1,14),K(Fraction(0),Fraction(17,196),137),1)
Q=q2e(Fraction(37,14),K(Fraction(0),Fraction(47,196),137),-1)
P=add(P,mul(2,Q))
x0,rp=e2q(P,1);y0,rm=e2q(Q,-1);w0=(rp*rm).a
assert w0*w0==fplus(x0)*fminus(y0)

# First Phi and reconstruction of the new squareclass field.
x1,y1,w1=phi(x0,y0,w0)
_,P1,Q1=surface_points(x1,y1,w1)

# V^{-6}: Q -> Q+12P.
Q2=add(Q1,mul(12,P1))
xs,rps=e2q(P1,1);ys,rms=e2q(Q2,-1);ws=(rps*rms).a
assert ws*ws==fplus(xs)*fminus(ys)

# Second Phi and final integer squareclass numerator.
x2,y2,w2=phi(xs,ys,ws)
A=abs(x2.numerator);B=x2.denominator
G=A**4+6*A*A*B*B+B**4
assert Fraction(G,B**4)==fplus(x2)
assert w2*w2==fplus(x2)*fminus(y2)
S=str(G)
vals={p:vp(G,p) for p in [2,13,17,41,73,113,137,193,241,257,281,313,353,1409,1657,2017,2473,2833,4481,7057,7577,190537]}
assert vals[137]==0 and vals[313]==1 and vals[41]==1 and vals[17]==2
for p in [73,113,193,241,257,281,353,1409,1657,2017,2473,2833,4481,7057,7577,190537]:
    assert vals[p]==0
assert isqrt(G//313)**2 != G//313
assert len(str(A))==65009 and len(str(B))==65008 and len(S)==260033
assert sha256(S.encode()).hexdigest()=="7aa299919d89963657a1896d0785e0357941452f493295b90fafcd2b2160ea15"
print({"status":"passed","word":"H^-1 Phi V^-6 Phi","digits_G":len(S),"valuations":vals,"G_over_313_is_square":False})
