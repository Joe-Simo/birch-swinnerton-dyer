from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction
from hashlib import sha256
from math import isqrt

@dataclass(frozen=True)
class K:
    a: Fraction
    b: Fraction
    D: int
    @staticmethod
    def c(x, D): return x if isinstance(x,K) else K(Fraction(x),Fraction(0),D)
    def __add__(self,o):
        o=K.c(o,self.D); return K(self.a+o.a,self.b+o.b,self.D)
    __radd__=__add__
    def __neg__(self): return K(-self.a,-self.b,self.D)
    def __sub__(self,o): return self+(-K.c(o,self.D))
    def __rsub__(self,o): return K.c(o,self.D)-self
    def __mul__(self,o):
        o=K.c(o,self.D); return K(self.a*o.a+self.D*self.b*o.b,self.a*o.b+self.b*o.a,self.D)
    __rmul__=__mul__
    def inv(self):
        den=self.a*self.a-self.D*self.b*self.b
        if den==0: raise ZeroDivisionError
        return K(self.a/den,-self.b/den,self.D)
    def __truediv__(self,o): return self*K.c(o,self.D).inv()
    def __rtruediv__(self,o): return K.c(o,self.D)/self

Point=tuple[K,K]|None

def add(P:Point,Q:Point)->Point:
    if P is None:return Q
    if Q is None:return P
    x1,y1=P;x2,y2=Q
    if x1==x2 and y1==-y2:return None
    if P==Q:
        if y1==0:return None
        lam=(3*x1*x1-1)/(2*y1)
    else:lam=(y2-y1)/(x2-x1)
    x3=lam*lam-x1-x2
    return x3,lam*(x1-x3)-y1

def neg(P:Point)->Point:return None if P is None else(P[0],-P[1])
def mul(n:int,P:Point)->Point:
    if n<0:return mul(-n,neg(P))
    R=None;A=P
    while n:
        if n&1:R=add(R,A)
        A=add(A,A);n//=2
    return R

def q_to_E(t:Fraction,r:K,e:int)->Point:
    T=K(t,Fraction(0),r.D)
    return (r+1+e*T*T)/(2*T*T),(r+1+3*e*T*T)/(2*T*T*T)

def E_to_q(P:Point,e:int)->tuple[Fraction,K]:
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
    c=(x*x*y*y+1)/gap;k=6*c-1;a,b=c,c*c+k
    z=y*(x*x+c); assert z!=0
    fp=4*a*x**3+2*b*x;fpp=12*a*x*x+2*b;fppp=24*a*x
    h1=fp/(2*z);h2=(fpp/2-h1*h1)/(2*z)
    r3=fppp/6-2*h1*h2;r4=c-h2*h2;assert r4!=0
    dx=-r3/r4;xo=x+dx;zo=z+h1*dx+h2*dx*dx
    den=xo*xo+c;assert den!=0
    yo=zo/den;wo=w*(xo*xo-yo*yo+6)/gap
    assert wo*wo==fplus(xo)*fminus(yo)
    return xo,yo,wo

def surface_points(x:Fraction,y:Fraction,w:Fraction):
    A=abs(x.numerator);B=x.denominator
    G=A**4+6*A*A*B*B+B**4
    rp=K(Fraction(0),Fraction(1,B*B),G)
    rm=K(Fraction(0),w*B*B/G,G)
    P=q_to_E(x,rp,1);Q=q_to_E(y,rm,-1)
    return G,P,Q

def vp(n:int,p:int)->int:
    n=abs(n);k=0
    while n%p==0:n//=p;k+=1
    return k

def is_prime_trial(n:int)->bool:
    if n<2:return False
    if n%2==0:return n==2
    q=3
    while q*q<=n:
        if n%q==0:return False
        q+=2
    return True

# Authenticated 137 seed and first H.
D0=137
P=q_to_E(Fraction(1,14),K(Fraction(0),Fraction(17,196),D0),1)
Q=q_to_E(Fraction(37,14),K(Fraction(0),Fraction(47,196),D0),-1)
P=add(P,mul(-2,Q))
x0,rp=E_to_q(P,1);y0,rm=E_to_q(Q,-1)
W0=rp*rm;assert W0.b==0
w0=W0.a
assert (x0,y0,w0)==(Fraction(6127,1862),Fraction(37,14),Fraction(25815863383,679540624))
assert w0*w0==fplus(x0)*fminus(y0)

# First nonlinear Phi.
x1,y1,w1=phi(x0,y0,w0)

# Rebuild the changed quadratic field and apply H^{-2}: P -> P+4Q.
G1,P1,Q1=surface_points(x1,y1,w1)
P1=add(P1,mul(4,Q1))
xs,rps=E_to_q(P1,1);ys,rms=E_to_q(Q1,-1)
Ws=rps*rms;assert Ws.b==0
ws=Ws.a
assert ws*ws==fplus(xs)*fminus(ys)

# Second Phi and final squareclass numerator.
x2,y2,w2=phi(xs,ys,ws)
A=abs(x2.numerator);B=x2.denominator
G=A**4+6*A*A*B*B+B**4
assert Fraction(G,B**4)==fplus(x2)
assert w2*w2==fplus(x2)*fminus(y2)

vals={p:vp(G,p) for p in [113,137,241,257,281,313,353,2113,2473,2657,50417,180097]}
assert vals[137]==0 and vals[313]==1
assert vals[113]==vals[241]==vals[2113]==vals[2657]==0
assert vals[281]==vals[353]==vals[2473]==vals[190537]==1
for p in [281,313,353,2473,190537]: assert is_prime_trial(p)
assert G%313==0 and isqrt(G//313)**2!=G//313
assert len(str(A))==3233 and len(str(B))==3233 and len(str(G))==12932
assert sha256(str(G).encode()).hexdigest()=="84ba591f89728a39b4a4ed84e23f0d860eef93d2884298ab962c5db3868c9725"
print({"status":"passed","word":"H Phi H^-2 Phi","digits_G":12932,"valuations":vals})
