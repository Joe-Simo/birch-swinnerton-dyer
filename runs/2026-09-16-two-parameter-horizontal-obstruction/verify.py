from __future__ import annotations
from dataclasses import dataclass
from math import lcm
import json


def leg(a:int,p:int)->int:
    a%=p
    if a==0:return 0
    return 1 if pow(a,(p-1)//2,p)==1 else -1

def inv(a:int,p:int)->int:return pow(a%p,-1,p)

def modsqrt(a:int,p:int)->int:
    a%=p
    if a==0:return 0
    if p%4==3:return pow(a,(p+1)//4,p)
    q=p-1;s=0
    while q%2==0:s+=1;q//=2
    z=2
    while leg(z,p)!=-1:z+=1
    c=pow(z,q,p);x=pow(a,(q+1)//2,p);t=pow(a,q,p);m=s
    while t!=1:
        i=1;t2=t*t%p
        while t2!=1:
            t2=t2*t2%p;i+=1
            if i>=m:raise ValueError('sqrt')
        b=pow(c,1<<(m-i-1),p)
        x=x*b%p;t=t*b*b%p;c=b*b%p;m=i
    return x

@dataclass(frozen=True)
class F2:
    a:int;b:int;p:int;d:int
    def c(self,o):return o if isinstance(o,F2) else F2(o%self.p,0,self.p,self.d)
    def __add__(self,o):
        o=self.c(o);return F2((self.a+o.a)%self.p,(self.b+o.b)%self.p,self.p,self.d)
    __radd__=__add__
    def __neg__(self):return F2((-self.a)%self.p,(-self.b)%self.p,self.p,self.d)
    def __sub__(self,o):return self+(-self.c(o))
    def __rsub__(self,o):return self.c(o)-self
    def __mul__(self,o):
        o=self.c(o);return F2((self.a*o.a+self.d*self.b*o.b)%self.p,(self.a*o.b+self.b*o.a)%self.p,self.p,self.d)
    __rmul__=__mul__
    def inverse(self):
        den=(self.a*self.a-self.d*self.b*self.b)%self.p
        if den==0:raise ZeroDivisionError
        z=inv(den,self.p);return F2(self.a*z%self.p,-self.b*z%self.p,self.p,self.d)
    def __truediv__(self,o):return self*self.c(o).inverse()
    def __rtruediv__(self,o):return self.c(o)/self

Point=tuple[F2,F2]|None

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

def order(P:Point,maxn:int=500000)->int:
    R=None
    for k in range(1,maxn+1):
        R=add(R,P)
        if R is None:return k
    raise RuntimeError('order bound')

def seed(p:int)->tuple[Point,Point]:
    s=F2(0,1,p,137%p)
    return ((197+17*s)/2,1393+119*s),((-1173+47*s)/2738,(-27377+329*s)/50653)

def q_to_E(t:int,r:F2,e:int)->Point:
    T=r.c(t);tt=T*T
    return (r+1+e*tt)/(2*tt),(r+1+3*e*tt)/(2*tt*T)

def E_to_q(P:Point,e:int)->tuple[int,F2]:
    if P is None:raise ZeroDivisionError
    u,v=P;t=(u+e)/v;r=(2*u-e)*t*t-1
    if t.b!=0:raise ValueError('descent')
    return t.a,r

def fplus(t:int,p:int)->int:return (pow(t,4,p)+6*t*t+1)%p

def phi(x:int,y:int,w:int,p:int)->tuple[int,int,int]:
    gap=(x*x-y*y+6)%p
    if gap==0:raise ZeroDivisionError('gap')
    c=(x*x*y*y+1)*inv(gap,p)%p;k=(6*c-1)%p;a=c;b=(c*c+k)%p
    z=y*(x*x+c)%p
    if z==0:raise ZeroDivisionError('z')
    f1=(4*a*x**3+2*b*x)%p;f2=(12*a*x*x+2*b)%p;f3=24*a*x%p
    h1=f1*inv(2*z,p)%p;h2=(f2*inv(2,p)-h1*h1)*inv(2*z,p)%p
    r3=(f3*inv(6,p)-2*h1*h2)%p;r4=(c-h2*h2)%p
    if r4==0:raise ZeroDivisionError('r4')
    dx=-r3*inv(r4,p)%p;xo=(x+dx)%p;zo=(z+h1*dx+h2*dx*dx)%p
    den=(xo*xo+c)%p
    if den==0:raise ZeroDivisionError('return')
    yo=zo*inv(den,p)%p;wo=w*(xo*xo-yo*yo+6)*inv(gap,p)%p
    if wo*wo%p != fplus(xo,p)*(pow(yo,4,p)-6*yo*yo+1)%p:raise AssertionError('surface')
    return xo,yo,wo

def lift_surface(x:int,y:int,w:int,p:int)->tuple[Point,Point]:
    d=fplus(x,p)
    if d==0:raise ZeroDivisionError('branch')
    if leg(d,p)==1:
        r=modsqrt(d,p);D=2
        while leg(D,p)!=-1:D+=1
        rp=F2(r,0,p,D);rm=F2(w*inv(r,p)%p,0,p,D)
    else:
        rp=F2(0,1,p,d);rm=F2(0,w*inv(d,p)%p,p,d)
    return q_to_E(x,rp,1),q_to_E(y,rm,-1)

def first_stage(p:int,m:int):
    P,Q=seed(p);Pm=add(P,mul(-2*m,Q));x,rp=E_to_q(Pm,1);y,rm=E_to_q(Q,-1);W=rp*rm
    if W.b:raise ValueError('W')
    return phi(x,y,W.a,p)

def local_constraint(p:int):
    assert leg(137,p)==-1
    P,Q=seed(p);M=order(mul(-2,Q));records={};Ns=[];amb_m=0;amb_n=0
    for m in range(M):
        try:
            x1,y1,w1=first_stage(p,m);P1,Q1=lift_surface(x1,y1,w1,p);N=order(mul(-2,Q1));Ns.append(N)
            good=set();amb=set()
            for n in range(N):
                try:
                    Pn=add(P1,mul(-2*n,Q1));xs,rps=E_to_q(Pn,1);ys,rms=E_to_q(Q1,-1);WW=rps*rms
                    if WW.b:raise ValueError('WW')
                    x2,_,_=phi(xs,ys,WW.a,p);F=fplus(x2,p)
                    if F!=0 and leg(F,p)==leg(313,p):good.add(n)
                except Exception:amb.add(n);amb_n+=1
            records[m]=(N,good|amb)
        except Exception:records[m]=None;amb_m+=1
    Np=1
    for N in Ns:Np=lcm(Np,N)
    allow={}
    for m,r in records.items():
        if r is None:allow[m]=None
        else:
            N,g=r;allow[m]={n for n in range(Np) if n%N in g}
    return {'p':p,'M':M,'N':Np,'allow':allow,'amb_m':amb_m,'amb_n':amb_n}

def combine(states:set[tuple[int,int]],GM:int,GN:int,c):
    LM=lcm(GM,c['M']);LN=lcm(GN,c['N']);out=set()
    for m0,n0 in states:
        for m in range(m0,LM,GM):
            al=c['allow'][m%c['M']]
            for n in range(n0,LN,GN):
                if al is None or n%c['N'] in al:out.add((m,n))
    return out,LM,LN

def fast_filter(p:int,states:set[tuple[int,int]],GM:int,GN:int):
    assert leg(137,p)==-1
    P,Q=seed(p)
    if mul(-2*GM,Q) is not None:raise AssertionError('m period does not divide global modulus')
    cache={};unresolved=set()
    for m,_ in states:
        mm=m%GM
        if mm in cache or mm in unresolved:continue
        try:
            x1,y1,w1=first_stage(p,mm);P1,Q1=lift_surface(x1,y1,w1,p)
            if mul(-2*GN,Q1) is not None:raise AssertionError('n period does not divide global modulus')
            cache[mm]=(P1,Q1)
        except (ZeroDivisionError,ValueError):unresolved.add(mm)
    out=set();elim=[]
    for m,n in states:
        mm=m%GM
        if mm in unresolved:out.add((m,n));continue
        P1,Q1=cache[mm]
        try:
            Pn=add(P1,mul(-2*n,Q1));xs,rps=E_to_q(Pn,1);ys,rms=E_to_q(Q1,-1);WW=rps*rms
            if WW.b:raise ValueError('WW')
            x2,_,_=phi(xs,ys,WW.a,p);F=fplus(x2,p)
            if F!=0 and leg(F,p)==leg(313,p):out.add((m,n))
            else:elim.append((m,n))
        except (ZeroDivisionError,ValueError):out.add((m,n))
    return out,elim,len(unresolved)

# Complete p=313 target check is preserved separately in target313.py.
# Four regular zero classes and eight singular classes are all retained here.
states={(0,n) for n in (0,27,54,56,76,96,101,112,123,128,148,168)};GM=1;GN=170
base=[]
for p in (13,31,29,23,71,79,127,157,179,191,239,359):
    c=local_constraint(p);states,GM,GN=combine(states,GM,GN,c)
    base.append({'p':p,'local_M':c['M'],'local_N':c['N'],'ambiguous_m':c['amb_m'],'ambiguous_n':c['amb_n'],'global_M':GM,'global_N':GN,'survivors':len(states)})
assert (GM,GN,len(states))==(360,24480,152)
final=[]
for p in (1151,1549,2719,4561):
    before=len(states);states,elim,unres=fast_filter(p,states,GM,GN)
    final.append({'p':p,'legendre_137':leg(137,p),'legendre_313':leg(313,p),'before':before,'eliminated':len(elim),'after':len(states),'unresolved_m':unres})
assert len(states)==0
print(json.dumps({'status':'passed','global_moduli':[GM,GN],'base':base,'final':final,'conclusion':'No integer pair (m,n) in H^m Phi H^n Phi can have final squareclass 313.'},indent=2))
