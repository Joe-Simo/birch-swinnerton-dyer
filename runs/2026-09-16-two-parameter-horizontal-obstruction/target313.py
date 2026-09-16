from verify import inv,phi,lift_surface,add,mul,order,E_to_q,fplus
import json

P=313
ROOTS=(78,235)

def sadd(A,B):
    if A is None:return B
    if B is None:return A
    x1,y1=A;x2,y2=B
    if x1==x2 and (y1+y2)%P==0:return None
    if A==B:
        if y1%P==0:return None
        lam=(3*x1*x1-1)*inv(2*y1,P)%P
    else:lam=(y2-y1)*inv(x2-x1,P)%P
    x3=(lam*lam-x1-x2)%P
    return x3,(lam*(x1-x3)-y1)%P

def smul(n,A):
    if n<0:return smul(-n,None if A is None else(A[0],-A[1]%P))
    R=None
    while n:
        if n&1:R=sadd(R,A)
        A=sadd(A,A);n//=2
    return R

def sorder(A):
    R=None
    for n in range(1,10000):
        R=sadd(R,A)
        if R is None:return n
    raise RuntimeError('order')

def seed(root):
    A=((197+17*root)*inv(2,P)%P,(1393+119*root)%P)
    B=((-1173+47*root)*inv(2738,P)%P,(-27377+329*root)*inv(50653,P)%P)
    return A,B

def toq(A,e):
    if A is None or A[1]%P==0:raise ZeroDivisionError
    t=(A[0]+e)*inv(A[1],P)%P
    r=((2*A[0]-e)*t*t-1)%P
    return t,r

rows=[]
for root in ROOTS:
    A,B=seed(root)
    M=sorder(smul(-2,B))
    assert M==2
    for m in range(M):
        Am=sadd(A,smul(-2*m,B))
        x,rp=toq(Am,1);y,rm=toq(B,-1)
        x1,y1,w1=phi(x,y,rp*rm%P,P)
        P1,Q1=lift_surface(x1,y1,w1,P)
        N=order(mul(-2,Q1))
        assert N==170
        zeros=[];amb=[]
        for n in range(N):
            try:
                Pn=add(P1,mul(-2*n,Q1))
                xs,rps=E_to_q(Pn,1);ys,rms=E_to_q(Q1,-1);W=rps*rms
                if W.b:raise ValueError('descent')
                x2,_,_=phi(xs,ys,W.a,P)
                if fplus(x2,P)==0:zeros.append(n)
            except (ZeroDivisionError,ValueError):amb.append(n)
        assert zeros==[0,54,56,168]
        assert amb==[27,76,96,101,112,123,128,148]
        rows.append({'root':root,'m':m,'period_n':N,'zeros':zeros,'ambiguous':amb})
print(json.dumps({'status':'passed','p':313,'period_m':2,'rows':rows,'conservative_allowed':[0,27,54,56,76,96,101,112,123,128,148,168]},indent=2))
