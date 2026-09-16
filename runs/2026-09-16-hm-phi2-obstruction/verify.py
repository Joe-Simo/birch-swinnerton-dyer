from __future__ import annotations
from math import lcm

class F2:
    __slots__=("a","b","p")
    def __init__(self,a:int,b:int,p:int): self.a=a%p; self.b=b%p; self.p=p
    def __add__(self,o):
        if not isinstance(o,F2): o=F2(o,0,self.p)
        return F2(self.a+o.a,self.b+o.b,self.p)
    __radd__=__add__
    def __neg__(self): return F2(-self.a,-self.b,self.p)
    def __sub__(self,o): return self+(-o if isinstance(o,F2) else -F2(o,0,self.p))
    def __rsub__(self,o): return F2(o,0,self.p)-self
    def __mul__(self,o):
        if not isinstance(o,F2): o=F2(o,0,self.p)
        return F2(self.a*o.a+(137%self.p)*self.b*o.b,self.a*o.b+self.b*o.a,self.p)
    __rmul__=__mul__
    def inv(self):
        den=(self.a*self.a-(137%self.p)*self.b*self.b)%self.p
        return F2(self.a*pow(den,-1,self.p),-self.b*pow(den,-1,self.p),self.p)
    def __truediv__(self,o):
        if not isinstance(o,F2): o=F2(o,0,self.p)
        return self*o.inv()
    def __eq__(self,o):
        if not isinstance(o,F2): o=F2(o,0,self.p)
        return self.p==o.p and self.a==o.a and self.b==o.b

Point=tuple[F2,F2]|None

def add(P:Point,Q:Point,p:int)->Point:
    if P is None:return Q
    if Q is None:return P
    x1,y1=P;x2,y2=Q
    if x1==x2 and y1==-y2:return None
    if P==Q:
        if y1==F2(0,0,p):return None
        lam=(3*x1*x1-1)/(2*y1)
    else: lam=(y2-y1)/(x2-x1)
    x3=lam*lam-x1-x2
    return x3,lam*(x1-x3)-y1

def neg(P:Point)->Point: return None if P is None else (P[0],-P[1])
def mul(n:int,P:Point,p:int)->Point:
    if n<0:return mul(-n,neg(P),p)
    R=None;A=P
    while n:
        if n&1:R=add(R,A,p)
        A=add(A,A,p);n//=2
    return R

def order(P:Point,p:int)->int:
    R=None
    for n in range(1,20000):
        R=add(R,P,p)
        if R is None:return n
    raise AssertionError('order bound')

def seed(p:int)->tuple[Point,Point]:
    s=F2(0,1,p)
    P=((197+17*s)/2,1393+119*s)
    Q=((-1173+47*s)/2738,(-27377+329*s)/50653)
    return P,Q

def quartic_t(P:Point,e:int,p:int)->int:
    assert P is not None
    t=(P[0]+e)/P[1]
    assert t.b==0
    return t.a

def fplus(t:int,p:int)->int:return (pow(t,4,p)+6*t*t+1)%p

def chi(a:int,p:int)->int:
    a%=p
    if a==0:return 0
    return 1 if pow(a,(p-1)//2,p)==1 else -1

def phi(x:int,y:int,p:int)->tuple[int,int]:
    gap=(x*x-y*y+6)%p; assert gap!=0
    c=(x*x*y*y+1)*pow(gap,-1,p)%p
    k=(6*c-1)%p; a=c; b=(c*c+k)%p
    z=y*(x*x+c)%p; assert z!=0
    fp=(4*a*pow(x,3,p)+2*b*x)%p
    fpp=(12*a*x*x+2*b)%p
    fppp=(24*a*x)%p
    h1=fp*pow(2*z,-1,p)%p
    h2=((fpp*pow(2,-1,p)-h1*h1)%p)*pow(2*z,-1,p)%p
    r3=(fppp*pow(6,-1,p)-2*h1*h2)%p
    r4=(c-h2*h2)%p; assert r4!=0
    dx=-r3*pow(r4,-1,p)%p
    xo=(x+dx)%p
    zo=(z+h1*dx+h2*dx*dx)%p
    den=(xo*xo+c)%p; assert den!=0
    yo=zo*pow(den,-1,p)%p
    return xo,yo

def allowed(ell:int):
    assert chi(137,ell)==-1
    P,Q=seed(ell)
    step=neg(add(Q,Q,ell))
    assert step is not None
    period=order(step,ell)
    target=chi(313,ell)
    out=[]
    current=P
    for m in range(period):
        x=quartic_t(current,1,ell)
        y=quartic_t(Q,-1,ell)
        x1,y1=phi(x,y,ell)
        x2,y2=phi(x1,y1,ell)
        v=fplus(x2,ell)
        if v!=0 and chi(v,ell)==target: out.append(m)
        current=add(current,step,ell)
    assert current==P
    return period,out

expected={
    251:(14,[0,1,3,7,11,13]),
    127:(8,[0,1,4,5]),
    239:(20,[1,3,5,6,7,11,13,15,16,17]),
    31:(8,[0,2,3,4,6,7]),
    457:(10,[3]),
}
rows={}
for ell,want in expected.items():
    got=allowed(ell)
    assert got==want
    rows[ell]=got
L=1
for period,_ in rows.values():L=lcm(L,period)
assert L==280
survivors=[]
for m in range(L):
    if all(m%period in set(ok) for period,ok in rows.values()):survivors.append(m)
assert survivors==[]
print({'status':'passed','rows':rows,'lcm':L,'survivors':survivors})
