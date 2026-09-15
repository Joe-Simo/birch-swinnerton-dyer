from __future__ import annotations
from collections import deque
import json


def inv(a: int, p: int) -> int:
    return pow(a % p, -1, p)

Point = tuple[int,int] | None

def add(P: Point,Q: Point,p: int) -> Point:
    if P is None:return Q
    if Q is None:return P
    x1,y1=P;x2,y2=Q
    if x1==x2 and (y1+y2)%p==0:return None
    if P==Q:
        if y1%p==0:return None
        lam=((3*x1*x1-1)*inv(2*y1,p))%p
    else:
        lam=((y2-y1)*inv(x2-x1,p))%p
    x3=(lam*lam-x1-x2)%p
    return x3,(lam*(x1-x3)-y1)%p

def neg(P: Point,p: int)->Point:
    return None if P is None else (P[0],(-P[1])%p)

def mul(n: int,P: Point,p: int)->Point:
    if n<0:return mul(-n,neg(P,p),p)
    R=None;A=P
    while n:
        if n&1:R=add(R,A,p)
        A=add(A,A,p);n//=2
    return R

def order(P: Point,p: int)->int:
    R=None
    for n in range(1,5000):
        R=add(R,P,p)
        if R is None:return n
    raise AssertionError('order bound')

def seed(p: int,s: int)->tuple[Point,Point]:
    P=((197+17*s)*inv(2,p)%p,(1393+119*s)%p)
    Q=((-1173+47*s)*inv(2738,p)%p,(-27377+329*s)*inv(50653,p)%p)
    return P,Q

def qt(P: Point,e: int,p: int)->int:
    assert P is not None and P[1]%p!=0
    return (P[0]+e)*inv(P[1],p)%p

def fplus(t: int,p: int)->int:
    return (pow(t,4,p)+6*t*t+1)%p

def phix(x: int,y: int,p: int)->tuple[int,int,int,int]:
    gap=(x*x-y*y+6)%p
    assert gap!=0
    C=(x*x*y*y+1)*inv(gap,p)%p
    if C==0:
        xo=(-inv(pow(x,3,p),p))%p
        return xo,fplus(xo,p),gap,1
    K=(6*C-1)%p;a=C;b=(C*C+K)%p;d=C*K%p
    N=(-x*(a*a*pow(x,8,p)-6*a*d*pow(x,4,p)-4*b*d*x*x-3*d*d))%p
    D0=(3*a*a*pow(x,8,p)+4*a*b*pow(x,6,p)+6*a*d*pow(x,4,p)-d*d)%p
    assert D0!=0
    xo=N*inv(D0,p)%p
    return xo,fplus(xo,p),gap,D0

def hmv_rows(p: int,s: int)->dict:
    P,Q=seed(p,s)
    per=order(mul(2,Q,p),p)
    rows=[]
    for m in range(per):
        Pm=add(P,mul(-2*m,Q,p),p)
        Qm=add(Q,mul(2,Pm,p),p)
        x=qt(Pm,1,p);y=qt(Qm,-1,p)
        xo,F,gap,D0=phix(x,y,p)
        rows.append([m,x,y,xo,F,gap,D0])
    return {'p':p,'sqrt137':s,'ordP':order(P,p),'ordQ':order(Q,p),'period':per,'rows':rows}

def closure(p: int,s: int)->dict:
    P0,Q0=seed(p,s)
    opP=order(P0,p);opQ=order(Q0,p)
    oddP=list(range(1,opP,2));oddQ=list(range(1,opQ,2))
    start=(P0,Q0)
    seen={start}
    q=deque([start])
    while q:
        P,Q=q.popleft()
        nxts=[
            (add(P,mul(-2,Q,p),p),Q),(add(P,mul(2,Q,p),p),Q),
            (P,add(Q,mul(-2,P,p),p)),(P,add(Q,mul(2,P,p),p)),
        ]
        nxts += [(mul(a,P,p),Q) for a in oddP]
        nxts += [(P,mul(d,Q,p)) for d in oddQ]
        for st in nxts:
            if st not in seen:
                seen.add(st);q.append(st)
    zeros=0;ambiguous=0
    for P,Q in seen:
        try:
            x=qt(P,1,p);y=qt(Q,-1,p)
            _,F,_,_=phix(x,y,p)
            if F==0:zeros+=1
        except (AssertionError,ValueError):
            ambiguous+=1
    return {'p':p,'sqrt137':s,'ordP':opP,'ordQ':opQ,'states':len(seen),'zeros':zeros,'ambiguous':ambiguous}

assert (44*44-137)%257==0 and (213*213-137)%257==0
assert (78*78-137)%313==0 and (235*235-137)%313==0
rows=[hmv_rows(257,44),hmv_rows(257,213),hmv_rows(313,78),hmv_rows(313,235)]
expected257=[[0,202,47,137,113],[1,187,175,98,87],[2,55,47,120,113],[3,70,175,159,87]]
expected313=[[0,246,300,112,95],[1,67,300,201,95]]
for rec in rows[:2]:
    assert rec['ordP']==16 and rec['ordQ']==8 and rec['period']==4
    assert [r[:5] for r in rec['rows']]==expected257
for rec in rows[2:]:
    assert rec['ordP']==24 and rec['ordQ']==4 and rec['period']==2
    assert [r[:5] for r in rec['rows']]==expected313
assert all(r[5] and r[6] for rec in rows for r in rec['rows'])
assert all(r[4]!=257%257 for rec in rows[:2] for r in rec['rows'])
assert all(r[4]!=313%313 for rec in rows[2:] for r in rec['rows'])
closures=[closure(313,78),closure(313,235),closure(257,44),closure(257,213)]
for rec in closures[:2]:
    assert rec['states']==576 and rec['zeros']==0 and rec['ambiguous']==0
for rec in closures[2:]:
    assert rec['states']==1024 and rec['zeros']==96 and rec['ambiguous']==16
summary={'status':'passed','hmv':rows,'closures':closures}
print(json.dumps(summary,indent=2))
