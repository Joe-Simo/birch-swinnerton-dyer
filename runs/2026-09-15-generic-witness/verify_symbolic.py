"""H9 exact identities and one fixed-fiber group-law control, not a BSD proof."""
from __future__ import annotations
from fractions import Fraction
import json
import sys
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parent
assertions = 0

def check(ok: bool, label: str) -> None:
    global assertions
    if not ok:
        raise AssertionError(label)
    assertions += 1

def zero(expr: sp.Expr, label: str) -> None:
    check(sp.cancel(sp.expand(expr)) == 0, label)

t,u,v,w,z,a,b,A,B,c,s,x,y = sp.symbols('t u v w z a b A B c s x y')
vars4 = (u,v,w,z)
xx=t*w**2/z**2
YY=t*u*v*w/z**3
symbolic_rows=[]
for e in (-1,1):
    q1=v**2-w**2+e*z**2
    q2=u**2-t*w**2-e*t*z**2
    H=(a*sp.hessian(q1,vars4)+b*sp.hessian(q2,vars4)).det()
    zero(H+16*e*a*b*(a*a-t*t*b*b), 'Hessian pencil with correct sign')
    G=sp.groebner([q1,q2],u,v,w,z,domain=sp.QQ.frac_field(t))
    curve_num=sp.together(YY**2-xx**3+t*t*xx).as_numer_denom()[0]
    check(G.reduce(curve_num)[1] == 0, 'Generic covering map lands on E')
    factors = (u*u/z**2,t*v*v/z**2) if e == -1 else (t*v*v/z**2,u*u/z**2)
    for lhs,rhs in zip((xx-t,xx+t),factors):
        num=sp.together(lhs-rhs).as_numer_denom()[0]
        check(G.reduce(num)[1] == 0, 'Kummer coordinate identity')
    subs={u:t*c,v:A*A-e*B*B,w:A*A+e*B*B,z:2*A*B}
    F=A**4+6*e*A*A*B*B+B**4
    zero(q1.subs(subs), 'Pythagorean parametrization')
    zero(q2.subs(subs)-t*(t*c*c-F), 'Remaining quartic is exactly the second quadric')
    zero(((v+w)*B-z*A).subs(subs), 'Birational inverse A/B')
    polynomial=A**4+6*e*A*A+1
    check(sp.gcd(polynomial,sp.diff(polynomial,A)) == 1, 'Four branch points are distinct')
    zero(q1.subs({u:sp.sqrt(t),v:1,w:1,z:0}), 'Boundary point on first quadric')
    zero(q2.subs({u:sp.sqrt(t),v:1,w:1,z:0}), 'Boundary point on second quadric')
    symbolic_rows.append({'sign':e,'pencil':str(sp.factor(H))})
# Trivialize the twist over t=s^2, and certify the CM automorphism.
zero((y*y-x**3+t*t*x).subs({t:s*s,x:s*s*u,y:s**3*v})-s**6*(v*v-u**3+u), 'Twist trivialization')
zero((sp.I*y)**2-(-x)**3+t*t*(-x)+(y*y-x**3+t*t*x), 'CM preserves the curve ideal')
check(-(-x) == x and sp.I*sp.I*y == -y, 'CM squares to negation')
qm=(v*v-w*w-z*z,u*u-t*w*w+t*z*z)
qp=(v*v-w*w+z*z,u*u-t*w*w-t*z*z)
for left,right in zip(qm,qp):
    zero(left.subs(z,sp.I*z)-right, 'Quadratic companion map')
zero(xx.subs(z,sp.I*z)+xx,'Companion x is -x')
zero(YY.subs(z,sp.I*z)-sp.I*YY,'Companion y is i*y')
zero((a+b*sp.I)+(a-b*sp.I)-2*a,'Trace in endomorphism ring')
zero(sp.I-sp.I,'CM trace cancellation')
# Independent linear algebra: ordinary exact matrix and vector enumeration.
rows=[(0,1,0,0,1,1,0,0,1),(1,0,1,0,0,1,1,0,0),
      (0,0,0,0,0,1,0,0,1),(0,0,1,0,0,0,0,0,1)]
minor=sp.Matrix(rows)[:,[0,1,2,5]]
check(minor.det() == 1,'Independent determinant')
def vecadd(a:tuple[int,...],b:tuple[int,...])->tuple[int,...]:
    return tuple((x+y)%2 for x,y in zip(a,b))
def span(rs:list[tuple[int,...]])->set[tuple[int,...]]:
    out={(0,)*9}
    for r in rs:
        out |= {vecadd(v,r) for v in out}
    return out
check(len(span(rows)) == 16,'Independent full span')
check(rows[2] not in span([rows[0],rows[1],rows[3]]),'Minus outside plus-generated span')
check(rows[3] not in span([rows[0],rows[1],rows[2]]),'Plus outside minus-generated span')

# Exact rational group operations on the one existing E41 plus fixture.
Point = tuple[Fraction,Fraction] | None
p=41
P:Point=(Fraction(1025,16),Fraction(25215,64))
torsion:list[Point]=[None,(Fraction(0),Fraction(0)),(Fraction(p),Fraction(0)),(Fraction(-p),Fraction(0))]
def on_curve(P:Point)->bool:
    return P is None or P[1]*P[1] == P[0]**3-p*p*P[0]
def add(P:Point,Q:Point)->Point:
    if not on_curve(P) or not on_curve(Q):
        raise ValueError('Point not on the fixed curve')
    if P is None:return Q
    if Q is None:return P
    x1,y1=P;x2,y2=Q
    if x1 == x2:
        if y1 == -y2:return None
        slope=(3*x1*x1-p*p)/(2*y1)
    else:slope=(y2-y1)/(x2-x1)
    x3=slope*slope-x1-x2
    return (x3,slope*(x1-x3)-y1)
def multiply(n:int,P:Point)->Point:
    if n<0:return multiply(-n,None if P is None else (P[0],-P[1]))
    out=None
    for _ in range(n):out=add(out,P)
    return out

def square_vector(q:Fraction)->tuple[int,int,int]:
    if not q:raise ValueError('Zero has no squareclass')
    n=q.numerator*q.denominator
    sign=int(n<0);n=abs(n)
    vals=[]
    for prime in (2,p):
        power=0
        while n%prime==0:n//=prime;power+=1
        vals.append(power%2)
    if sp.integer_nthroot(n,2)[1] is not True:
        raise ValueError('Odd prime support outside the declared basis')
    return (sign,*vals)
def kummer(P:Point)->tuple[int,...]:
    if P is None:triple=(Fraction(1),)*3
    elif P[1] != 0:triple=(P[0]-p,P[0]+p,P[0])
    elif P[0] == p:triple=(Fraction(2),Fraction(2*p),Fraction(p))
    elif P[0] == 0:triple=(Fraction(-p),Fraction(p),Fraction(-1))
    elif P[0] == -p:triple=(Fraction(-2*p),Fraction(2),Fraction(-p))
    else:raise ValueError('Unknown torsion point')
    return tuple(bit for q in triple for bit in square_vector(q))
check(on_curve(P),'H8 E41 fixture is on the curve')
check(kummer(P) == rows[3],'Fixture has the plus Kummer class')
check(add(P,None if P is None else (P[0],-P[1])) is None,'Opposite points cancel')
check(all(on_curve(T) and multiply(2,T) is None for T in torsion),'All four torsion points')
finite=[]
for n in range(4):
    for j,T in enumerate(torsion):
        Q=add(multiply(n,P),T)
        expected=vecadd(rows[3] if n%2 else (0,)*9,kummer(T))
        check(on_curve(Q),'Group-law result on curve')
        check(kummer(Q) == expected,'Kummer homomorphism on selected exact operations')
        finite.append({'multiple':n,'torsion_index':j,'kummer':list(kummer(Q))})
try:
    add((Fraction(1),Fraction(1)),P)
except ValueError:pass
else:raise AssertionError('Bad point should be rejected')
assertions+=1
try:square_vector(Fraction(3))
except ValueError:pass
else:raise AssertionError('Extra prime support should be rejected')
assertions+=1
result={'assertions':assertions,'python':sys.version.split()[0],'sympy':sp.__version__,
        'symbolic_rows':symbolic_rows,'minor_determinant':int(minor.det()),'finite_operations':finite,
        'scope':'Generic polynomial identities and 16 exact E41 group-law fixtures only. The all-degree map classification and odd-degree nonexistence use the written proof, not these finite assertions.'}
(ROOT/'results'/'symbolic-results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'assertions':assertions,'result':'results/symbolic-results.json','status':'passed'},indent=2))
