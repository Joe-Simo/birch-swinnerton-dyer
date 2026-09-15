"""H13: symbolic proof obligations and an independently interpreted exact replay."""
from fractions import Fraction as Q
from pathlib import Path
from math import gcd
import json
import sympy as s

checks=0
def check(condition,label):
    global checks
    checks+=1
    if not condition:raise AssertionError(label)
def zero(expression,label):check(s.cancel(expression)==0,label)
x,c,k,z,h,n=s.symbols('x c k z h n')
f=(x*x+c)*(c*x*x+k)
g=x**4+6*x*x+1
zero(s.discriminant(f,x)-16*c*c*k*(c*c-k)**4,'quartic discriminant')
zero(s.resultant(f.subs(k,6*c-1),g,x)-(c*c-6*c+1)**4,'disjoint branch sets')
check(s.discriminant(g,x)==2**14,'simple four roots of g')
X=c*x*x;Y=c*x*z
zero((Y*Y-X*(X+c*c)*(X+k)).subs(z*z,f),'degree2 elliptic quotient identity')
# Osculation is checked by polynomial division, not the TS modular group routine.
cc=Q(-39785,37632);kk=Q(-46057,6272)
x0=Q(1,14);y0=Q(37,14);z0=y0*(x0*x0+cc)
poly=s.Poly(f.subs({c:s.Rational(cc),k:s.Rational(kk)}),x)
xq=s.Rational(x0);zq=s.Rational(z0)
q1=poly.diff().eval(xq)/(2*zq)
q2=(poly.diff().diff().eval(xq)/2-q1*q1)/(2*zq)
quad=zq+q1*(x-xq)+q2*(x-xq)**2
quot,rem=s.div(poly-s.Poly(quad**2,x),s.Poly((x-xq)**3,x))
check(rem.is_zero,'triple contact')
check(quot.degree()==1,'unique fourth intersection on open chart')
x1=Q(-quot.nth(0)/quot.nth(1));z1=Q(quad.subs(x,s.Rational(x1)));y1=z1/(x1*x1+cc)
check((x1,y1)==(Q(-16890371,79256324),Q(210069683,77723044)),'reconstruct H12 output')
check(z0*z0==(x0*x0+cc)*(cc*x0*x0+kk),'seed on fiber')
check(z1*z1==(x1*x1+cc)*(cc*x1*x1+kk),'output on same fiber')

def quotient(x,z):return (cc*x*x,cc*x*z)
R0=quotient(x0,z0);R1=quotient(x1,z1)
a2=cc*cc+kk;a4=cc*cc*kk
for P in (R0,R1):
    xx,yy=P;check(yy*yy==xx*(xx+cc*cc)*(xx+kk),'rational elliptic quotient point')
slope=(R1[1]-R0[1]*(-1))/(R1[0]-R0[0]) # R1 + (-R0)
dx=slope*slope-a2-R1[0]-R0[0]
dy=slope*(R1[0]-dx)-R1[1]
Delta=(dx,dy)
check(dy*dy==dx*(dx+cc*cc)*(dx+kk),'rational Delta is valid')

def modq(r,p):
    r=Q(r)
    return r.numerator*pow(r.denominator,-1,p)%p

def add(P,R,p,A2,A4):
    if P is None:return R
    if R is None:return P
    xx,yy=P;uu,vv=R
    if xx==uu and (yy+vv)%p==0:return None
    t=((3*xx*xx+2*A2*xx+A4)*pow(2*yy,-1,p) if xx==uu else (vv-yy)*pow(uu-xx,-1,p))%p
    xx2=(t*t-A2-xx-uu)%p
    return (xx2,(t*(xx-xx2)-yy)%p)
rows=[]
for p in (13,19,31):
    C=modq(cc,p);K=modq(kk,p)
    # Count via the quadratic character, independently of TS's x,y enumeration.
    count=p+1+sum(0 if (v:=xx*(xx+C*C)*(xx+K)%p)==0 else (1 if pow(v,(p-1)//2,p)==1 else -1) for xx in range(p))
    check(16*C**4*K*K*(C*C-K)**2%p!=0,'good reduction')
    check(count=={13:16,19:24,31:40}[p],'independent character-sum count')
    dpt=tuple(modq(a,p) for a in Delta) if all(a.denominator%p for a in Delta) else None
    # At 13 and19 Delta reduces to infinity, as seen in its x-denominator.
    if p in (13,19):check(dx.denominator%p==0,'rational difference reduces to infinity')
    if p==31:
        check(dpt==(28,5),'reduce exact rational difference')
        multiples=[];P=None
        for j in range(1,9):P=add(P,dpt,p,(C*C+K)%p,C*C*K%p);multiples.append(P)
        check(multiples[4] is None and multiples[0] is not None,'order5 certificate')
        check(multiples[7]==(4,28),'8Delta nonzero')
    rows.append({'p':p,'count':count,'Delta':dpt})
check(gcd(16,24)==8,'rational torsion order bound')
# Full local chart check, x affine and the leading coefficient at infinity.
p=13;squares={j*j%p for j in range(p)}
allowed=[]
for xx in range(p):
    vals=[zz for zz in range(p) if (zz*zz-(xx*xx+6)*(6*xx*xx+9))%p==0]
    gg=(xx**4+6*xx*xx+1)%p
    if vals:
        check(gg!=0 and pow(gg,6,13)==12,'admissible local value is nonsquare unit')
        allowed.append(xx)
check(allowed==[1,3,4,6,7,9,10,12],'complete admissible residue list')
check(6 not in squares and 7 not in squares,'infinity and x^2+C chart absent')
for target in (257,313):check(pow(target%13,6,13)==1,'prescribed target violates fixed-fiber symbol')
# Independent unchanged-squareclass map: validate its full generic identity.
t=s.symbols('t');e=-1
N=t*(t**8-6*t**4-24*e*t*t-3);D=3*t**8+24*e*t**6+6*t**4-1
H=t**16+24*e*t**14+28*t**12+168*e*t**10+582*t**8+168*e*t**6+28*t**4+24*e*t*t+1
zero(N**4+6*e*N*N*D*D+D**4-(t**4+6*e*t*t+1)*H*H,'minus tripling retains squareclass')
y3=Q((N/D).subs(t,s.Rational(y0)))
U=x0*x0+3;V=y3*y3-3
c3=(U*V-8)/(U-V)+3;k3=6*c3-1
check(c3==Q(-61708285879386802434260270825,2683974129278159984546892312288),'exact changed fiber coefficient')
check((modq(c3,13),modq(k3,13))==(1,5),'changed fiber reduction')
for target,r in ((257,6),(313,3)):
    check((target*r*r-(5**4+6*25+1))%13==0,'changed-fiber target equation')
    check((5*5+1)*(5*5+5)%13==0,'changed-fiber genus-one equation')
    fp=(4*5**3+12*5)%13
    check((-fp*2*target*r)%13!=0,'joint Hensel derivative determinant')
# All prime-support / parity assertions in the prose have algebraic identities.
a,b=s.symbols('a b')
Gp=a**4+6*a*a*b*b+b**4
zero(Gp-(a*a+b*b)**2-4*a*a*b*b,'minus-one residue identity')
zero(Gp-(a*a-b*b)**2-8*a*a*b*b,'minus-two residue identity')
check({(aa**4+6*aa*aa*bb*bb+bb**4)%16 for aa in (1,3,5,7) for bb in (1,3,5,7)}=={8},'plus odd-odd 2-adic valuation3')
check({(aa**4-6*aa*aa*bb*bb+bb**4)%16 for aa in (1,3,5,7) for bb in (1,3,5,7)}=={12},'minus odd-odd 2-adic valuation2')
# Two rational point identities for arbitrary nonzero n.
for eps in (-1,1):
    A,B,cv=s.symbols('A B cv');UU=n*cv;VV=A*A-eps*B*B;TT=A*A+eps*B*B;ZZ=2*A*B
    xx=n*TT*TT/(ZZ*ZZ);yy=n*UU*VV*TT/(ZZ**3)
    residual=s.together(yy*yy-xx**3+n*n*xx)
    residual=residual.subs(cv*cv,(A**4+6*eps*A*A*B*B+B**4)/n)
    zero(residual,'generic E_n point from quartic witness')
minor=s.Matrix([[0,1,0,1],[1,0,1,1],[0,0,0,1],[0,0,1,0]])
check(minor.det()==1,'same raw independence minor as H12')
# Validate small coefficient fixtures without treating them as an infinite proof.
coefs=[(1-(-3)**j)//4 for j in range(12)]
check(all(coefs[j+1]==1-3*coefs[j] for j in range(11)),'orbit scalar recurrence')
check(len(set(coefs))==12,'distinct finite coefficient prefix')
run=Path(__file__).resolve().parent
saved=json.loads((run/'results/integer-results.json').read_text())
check([r['count'] for r in rows]==[r['count'] for r in saved['rows']],'independent finite counts agree with TS')
check([int(r['x']) for r in saved['local13']['table'] if r['lifts']]==allowed,'independent local population agrees')
out={'assertions':checks,'C':str(cc),'K':str(kk),'x1':str(x1),'y1':str(y1),'Delta':[str(a) for a in Delta],'finite_rows':rows,'resultant':str(s.factor(s.resultant(f.subs(k,6*c-1),g,x))),'changed_C':str(c3),'scope':'Generic polynomial identities; exact rational difference; independent finite-field counts and complete local13 screen. No formal/expert verification of infinite statements.'}
(run/'results/symbolic-results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
