"""H15: rational arithmetic, symbolic transfer law, and an independent local reconstruction."""
from dataclasses import dataclass
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
import json
import sympy as sp

ROOT=Path(__file__).resolve().parent
checks=[]
def check(ok,label):
    if not ok:raise AssertionError(label)
    checks.append(label)
@dataclass(frozen=True)
class Quad:
    a:F
    b:F=F(0)
    def __add__(self,other):
        o=other if isinstance(other,Quad) else Quad(F(other))
        return Quad(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self):return Quad(-self.a,-self.b)
    def __sub__(self,o):return self+-o
    def __rsub__(self,o):return -self+o
    def __mul__(self,other):
        o=other if isinstance(other,Quad) else Quad(F(other))
        return Quad(self.a*o.a+137*self.b*o.b,self.a*o.b+self.b*o.a)
    __rmul__=__mul__
    def inverse(self):
        n=self.a*self.a-137*self.b*self.b
        if n==0:raise ZeroDivisionError('Zero norm')
        return Quad(self.a/n,-self.b/n)
    def __truediv__(self,o):
        o=o if isinstance(o,Quad) else Quad(F(o))
        return self*o.inverse()
    def __pow__(self,n):
        if n<0:return self.inverse()**(-n)
        z=Quad(F(1))
        for _ in range(n):z=z*self
        return z

def add(P,Q):
    if P is None:return Q
    if Q is None:return P
    x,y=P;u,v=Q
    if x==u and y==-v:return None
    slope=(3*x*x-1)/(2*y) if P==Q else (v-y)/(u-x)
    xx=slope*slope-x-u
    return xx,slope*(x-xx)-y

def from_quartic(t,e,c):
    r=Quad(F(0),c)
    P=((r+1+e*t*t)/(2*t*t),(r+1+3*e*t*t)/(2*t**3))
    check(P[1]**2==P[0]**3-P[0],'exact quartic-to-E0 identity')
    return P

def to_quartic(P,e):
    if P is None:raise ValueError('Outside affine chart')
    u,v=P;t=(u+e)/v;r=(2*u-e)*t*t-1
    check(t.b==0 and r.a==0,'rationality and conjugation')
    check(t.a**4+6*e*t.a*t.a+1==137*r.b*r.b,'137 quartic witness')
    return t.a,r.b

def phi_contact(x,y,w):
    gap=x*x-y*y+6;c=(x*x*y*y+1)/gap;k=6*c-1
    z=y*(x*x+c);h1=(4*c*x**3+2*(c*c+k)*x)/(2*z)
    h2=(6*c*x*x+c*c+k-h1*h1)/(2*z)
    d=-(4*c*x-2*h1*h2)/(c-h2*h2)
    xx=x+d;zz=z+h1*d+h2*d*d;yy=zz/(xx*xx+c)
    return xx,yy,w*(xx*xx-yy*yy+6)/gap

def ff(t,e=1):return t**4+6*e*t*t+1

def valuation(v,p):
    v=F(v)
    if v==0:raise ValueError('Infinite valuation')
    a,b=v.numerator,v.denominator;n=0
    while a%p==0:a//=p;n+=1
    while b%p==0:b//=p;n-=1
    return n

# Independent algebraic derivation of the specialized map from the even-quartic formulas.
x,C,eps,h,z=sp.symbols('x C eps h z')
y0=sp.Rational(37,14)
c=(x*x*y0*y0+1)/(x*x-y0*y0+6);k=6*c-1;b=c*c+k
num=-x*(c*x**8-6*c*k*x**4-4*b*k*x*x-3*c*k*k)
den=3*c*x**8+4*b*x**6+6*c*k*x**4-c*k*k
R=sp.cancel(num/den)
A=-x*(52591504*x**6-727141576*x**4-6145143927*x*x-1102006668)
B=157774512*x**6+519995448*x**4-2460543401*x*x-367335556
check(sp.cancel(R-A/B)==0,'degree-seven map derived from Phi')
Fplus=sp.Poly(ff(x),x)
G=sp.Poly(A**4+6*A*A*B*B+B**4,x)
J=G.exquo(Fplus)
check(sp.gcd(sp.Poly(A,x),sp.Poly(B,x)).degree()==0,'map has no rational cancellation')
check(G.degree()==28 and J.degree()==24,'correct branch polynomial degrees')
check(sp.gcd(G,G.diff()).degree()==0,'all28 branch numerator zeros are simple')
check(sp.gcd(J,Fplus).degree()==0,'24 new branch zeros disjoint from four old ones')
check(sp.gcd(G,sp.Poly(B,x)).degree()==0,'no cancellation at output denominator')
check(G==Fplus*J,'exact global transfer identity')
# Generic invariant differential and node-retention identities.
for e in (-1,1):
    u=(z+1+e*x*x)/(2*x*x);v=(z+1+3*e*x*x)/(2*x**3)
    derivative=sp.diff(u,x)+sp.diff(u,z)*sp.diff(ff(x,e),x)/(2*z)
    numerator=sp.fraction(sp.cancel(derivative/(2*v)+1/z))[0]
    check(sp.rem(numerator,z*z-ff(x,e),z)==0,'invariant differential pullback -dt/r')
s=-C+eps;K=C*C-h*h*eps*eps;bb=C*C+K
D=3*C*s**4+4*bb*s**3+6*C*K*s*s-C*K*K
N=-(C*s**4-6*C*K*s*s-4*bb*K*s-3*C*K*K)
expectedD=-eps**3*(4*C*C+C*h**4*eps-6*C*h*h*eps-3*C*eps+4*h*h*eps*eps)
expectedN=eps**3*(4*C*C-C*h**4*eps-6*C*h*h*eps-C*eps+4*h**4*eps*eps)
check(sp.expand(D-expectedD)==0 and sp.expand(N-expectedN)==0,'node blow-up cancellation identities')
ratio=sp.cancel(N/D)
check(sp.simplify(ratio.subs(eps,0)+1)==0,'node x changes sign at first order')
eps_out=sp.cancel((-C+eps)*ratio**2+C)
check(sp.simplify(sp.diff(eps_out,eps).subs(eps,0)-h**4)==0,'node leading multiplier is fourth power')

# Closed-form tangent calculation, independent of the TypeScript ring recurrence.
p=137;p2=p*p
inv=lambda a:pow(a%p,-1,p)
xroot=49;yroot=32;bP=17*inv(196)%p;bQ=47*inv(196)%p
fp=lambda t,e:(4*t**3+12*e*t)%p
seed_y=37*pow(14,-1,p2)%p2
rows=[]
for m in range(274):
    root=xroot if m%2==0 else -inv(xroot)%p
    coefficient=fp(root,1)*(bP*inv(fp(xroot,1))-2*m*bQ*inv(fp(yroot,-1)))%p
    # Hensel: F(root+p*u)=p*coefficient^2 modulo p^2.
    lifted=(root+p*((coefficient*coefficient-ff(root)//p)*inv(fp(root,1))%p))%p2
    value=ff(lifted)%p2;gap=(lifted*lifted-seed_y*seed_y+6)%p2
    cv=lambda a:None if a==0 else (1 if a%p==0 else 0)
    row={'m':m,'x_mod_p2':str(lifted),'r_coefficient':str(coefficient),'Fplus_valuation_capped':cv(value),'gap_valuation_capped':cv(gap),'status':'exception'}
    if cv(gap)==0 and cv(value)==1:row['status']='retains'
    elif cv(gap)==1:
        n=(lifted*lifted*seed_y*seed_y+1)%p2
        if n%p:raise AssertionError('Bad integral division')
        c=(n//p)*inv(gap//p)%p;k=(6*c-1)%p;b=(c*c+k)%p;t=lifted%p
        row['C_mod_p']=str(c)
        D=(3*c*t**8+4*b*t**6+6*c*k*t**4-c*k*k)%p
        if D:
            xx=-t*(c*t**8-6*c*k*t**4-4*b*k*t*t-3*c*k*k)*inv(D)%p
            jd=(xx*xx+c)%p;value_out=ff(xx)%p
            row.update(output_x=str(xx),map_denominator=str(D),return_denominator=str(jd),output_Fplus=str(value_out))
            if value_out and jd:row['status']='removes'
    rows.append(row)
primary=json.loads((ROOT/'results/local-cycle.json').read_text())
check(rows==primary['rows'],'all274 local rows match independent tangent/Hensel reconstruction')
check(sum(r['status']=='removes' for r in rows)==128,'128 whole progressions certify removal')
check(sum(r['status']=='retains' for r in rows)==136,'136 whole progressions certify retention')
check(sum(r['status']=='exception' for r in rows)==10,'precision exceptions remain unresolved')

characters=[pow(int(row['output_Fplus']),68,137) for row in rows if row['status']=='removes']
check(characters.count(1)==86 and characters.count(136)==42 and pow(257,68,137)==pow(313,68,137)==1,'both local unit classes occur and both targets pass this character screen')

# Genuine global word H,Phi, not merely an admissible local point.
P=from_quartic(F(1,14),1,F(17,196));Q=from_quartic(F(37,14),-1,F(47,196))
Q2=add(Q,Q)
if Q2 is None:raise AssertionError('Unexpected torsion')
QeX=137*(F(37,14)**2-1)**2/(4*F(37,14)**2)
QeY=137**2*F(47,196)*(F(37,14)**4-1)/(8*F(37,14)**3)
check(Q2[0].b==0 and Q2[1].a==0 and 137*Q2[0].a==QeX and -137**2*Q2[1].b==QeY,'minus doubleQ descends to explicit rational point')
check(QeY!=0 and QeY*QeY==QeX**3-137**2*QeX,'non-torsion seed image using four-element torsion bound')
x1,c1=to_quartic(add(P,(Q2[0],-Q2[1])),1)
y1,d1=to_quartic(Q,-1);W1=137*c1*d1
check(x1==F(6127,1862),'short shear input')
xx,yy,ww=phi_contact(x1,y1,W1)
check(ww*ww==ff(xx,1)*ff(yy,-1),'exact output lies on surface')
check(F(R.subs(x,sp.Rational(x1.numerator,x1.denominator)))==xx,'specialized map matches osculating implementation')
check(xx==F(43527762774033482635941503,35975915953349079904919842),'explicit short output x')
Gout=xx.numerator**4+6*xx.numerator**2*xx.denominator**2+xx.denominator**4
check(valuation(Gout,137)==0,'input prime137 removed globally')
primes=[17,257,281,7369]
check(all(all(q%d for d in range(2,isqrt(q)+1)) for q in primes),'four trial-division primality certificates')
vals={q:valuation(Gout,q) for q in primes}
check(vals=={17:5,257:1,281:1,7369:1},'odd valuations certify composite kernel without complete factorization')
uplus=F(1,xx.denominator**2);uminus=ww*xx.denominator**2/Gout
check(ff(xx)==Gout*uplus*uplus and ff(yy,-1)==Gout*uminus*uminus,'two exact output quartic witnesses')
for t,e,u in [(xx,1,uplus),(yy,-1,uminus)]:
    X=Gout*(t*t+e)**2/(4*t*t);Y=Gout*Gout*u*(t**4-1)/(8*t**3)
    check(Y*Y==X**3-Gout**2*X and Y!=0,'exact free-point output certificate')
    if e==1:
        check(X-Gout==Gout*((t*t-1)/(2*t))**2 and X+Gout==(Gout*u/(2*t))**2,'plus Kummer factors')
    else:
        check(X-Gout==(Gout*u/(2*t))**2 and X+Gout==Gout*((t*t+1)/(2*t))**2,'minus Kummer factors')
    check(X==Gout*((t*t+e)/(2*t))**2,'third Kummer factor')
raw=sp.Matrix([[0,1,0,1],[1,0,1,1],[0,0,0,1],[0,0,1,0]])
check(raw.det()==1,'two witnesses plus rational2-torsion independent in Kummer quotient')
check((Gout%2)==1 and Gout>0,'positive odd nonsquare output')
summary={'status':'passed','assertions':len(checks),'checks':checks,'local_rows_compared':274,'sympy':sp.__version__,'map_degrees':[7,6],'branch_degrees':[4,24],'fixed_output_genus':25,'scope':'Polynomial, local-cycle and exact rational certificates; no analytic-rank, general reachability, novelty or formal verification claim.'}
(ROOT/'results/symbolic-summary.json').write_text(json.dumps(summary,indent=2)+'\n')
(ROOT/'results/global-certificate.json').write_text(json.dumps({'word':['H','Phi'],'input':list(map(str,(x1,y1,W1))),'output':list(map(str,(xx,yy,ww))),'G':str(Gout),'v137':0,'odd_prime_valuations':{str(q):v for q,v in vals.items()},'A_coefficients':[str(v) for v in sp.Poly(A,x).all_coeffs()],'B_coefficients':[str(v) for v in sp.Poly(B,x).all_coeffs()],'J_coefficients':[str(v) for v in J.all_coeffs()],'no_full_factorization_claim':True},indent=2)+'\n')
print(json.dumps(summary,indent=2))
