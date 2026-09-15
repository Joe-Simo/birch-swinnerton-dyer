"""H5 separate exact certificates: division polynomials, rational arithmetic,
concrete finite groups and abstract tower maps. No infinite-depth proof is inferred
from these finite tests, and no canonical heights are estimated numerically.
"""
from __future__ import annotations
from fractions import Fraction as F
from itertools import product
import json
import platform
import sympy as sp

checks: list[str] = []
def check(condition: bool, label: str) -> None:
    if not condition:
        raise AssertionError(label)
    checks.append(label)

# Independently use division polynomials for x([3]Q), not the TS group-addition loop.
x, a, b = sp.symbols('x a b')
cubic = x**3 + a*x + b
psi3 = 3*x**4 + 6*a*x**2 + 12*b*x - a**2
G = x**6 + 5*a*x**4 + 20*b*x**3 - 5*a**2*x**2 - 4*a*b*x - 8*b**2 - a**3
N3 = sp.expand(x*psi3**2 - 8*cubic*G)
# Double first, then add Q; write the resulting slope squared without sqrt(y^2).
x2 = (3*x*x+a)**2/(4*cubic)-2*x
slope3_squared = ((3*x*x+a)*(x-x2)-4*cubic)**2/(4*cubic*(x2-x)**2)
x3_from_addition = slope3_squared-x2-x
check(sp.cancel(x3_from_addition-N3/psi3**2)==0, 'generic tripling x identity')
mod_rows=[]
for q, expected in [(3,4),(5,8),(7,8),(11,12)]:
    affine=[(xx,yy) for xx,yy in product(range(q),repeat=2) if (yy*yy-xx**3+1681*xx)%q==0]
    check(len(affine)+1==expected,f'independent full enumeration mod {q}')
    check(64*41**6%q!=0,f'discriminant nonzero mod {q}')
    mod_rows.append({'prime':q,'group_order':len(affine)+1,'points':affine})
    if q==11:
        image_x:set[int|str]={'O'}
        for xx,yy in affine:
            den=int(psi3.subs({a:-1681,b:0,x:xx}))%q
            num=int(N3.subs({a:-1681,b:0,x:xx}))%q
            if den==0:
                image_x.add('O')
            else:
                image_x.add(num*pow(den*den,-1,q)%q)
        check(image_x=={'O',0,3,8},'division-polynomial tripling image x coordinates mod11')
        check((-9)%11 not in image_x,'P reduction cannot be triple by independent polynomial method')
        tripling_certificate={'image_x':sorted(image_x,key=str),'P':[-9%11,120%11]}

Point = tuple[F,F] | None
def add(p: Point,q: Point) -> Point:
    if p is None:return q
    if q is None:return p
    xx,yy=p; u,v=q
    if xx==u and yy==-v:return None
    slope=(3*xx*xx-1681)/(2*yy) if p==q else (v-yy)/(u-xx)
    z=slope*slope-xx-u
    return z,-yy+slope*(xx-z)

def mul(k:int,p:Point)->Point:
    if k<0:return mul(-k,None if p is None else (p[0],-p[1]))
    # Deliberately repeated addition, independent of TS binary multiplication.
    out=None
    for _ in range(k):out=add(out,p)
    return out

def on_curve(p:Point)->bool:
    return p is None or p[1]**2==p[0]**3-1681*p[0]

def encode(p:Point)->list[str]|None:
    return None if p is None else [str(z) for z in p]

P=(F(-9),F(120))
check(on_curve(P),'rational P lies on E41')
check(add(P,(P[0],-P[1])) is None,'rational inverse law')
rational_rows=[]
for m in range(1,5):
    am=(1-(-2)**m)//3
    R=mul(am,P)
    check(on_curve(R),f'rational representative m={m} lies on E41')
    check(mul(3,R)==add(P,mul(-(-2)**m,P)),f'exact point relation 3R=P-(-2)^m P for m={m}')
    rational_rows.append({'m':m,'a':am,'point':encode(R),'height_factor':am*am})
check(mul(3,P) is not None and mul(3,P)[0]==F(N3.subs({x:-9,a:-1681,b:0}),psi3.subs({x:-9,a:-1681,b:0})**2),'rational P triple agrees with division polynomial')
# Build inverses recursively, independently of the closed formula.
residue=0
coefficient_rows=[]
for m in range(1,65):
    modulus=2**m
    if (3*residue-1)%modulus:
        residue+=modulus//2
    check((3*residue-1)%modulus==0,f'bit-lifted inverse-three m={m}')
    centered=residue if residue<=modulus//2 else residue-modulus
    closed=(1-(-2)**m)//3
    check(centered==closed,f'bit lifting and closed coefficient agree m={m}')
    if m<=10:
        good=[k for k in range(-modulus,modulus+1) if (3*k-1)%modulus==0]
        check(min(abs(k) for k in good)==abs(centered),f'exhaustive nearest coefficient m={m}')
    coefficient_rows.append({'level':m,'a':closed})

# Whole finite abstract systems, retaining both natural maps and marked subgroups.
def group(m:int)->set[tuple[int,int,int,int]]:
    return set(product(range(2**m),range(2**m),range(2),range(2)))
abstract=[]
for m in range(1,5):
    s=group(m); n=2**m
    check(len(s)==4*n*n,f'abstract order m={m}')
    for rank in (0,1,2):
        K={pt for pt in s if all(pt[i]==0 for i in range(rank,2))}
        quotient={pt[rank:2] for pt in s}
        check(len(K)*len(quotient)==len(s),f'abstract exact Kummer/Sha sizes r={rank},m={m}')
        abstract.append({'m':m,'r':rank,'selmer':len(s),'marked_kummer':len(K),'quotient':len(quotient)})
    if m<4:
        higher=group(m+1)
        down=lambda pt:(pt[0]%n,pt[1]%n,pt[2],pt[3])
        up=lambda pt:(2*pt[0],2*pt[1],0,0)
        check({down(pt) for pt in higher}==s,f'abstract inverse transitions onto m={m}')
        check(all(up(down(pt))==(2*pt[0]%(2*n),2*pt[1]%(2*n),0,0) for pt in higher),f'j after u equals two m={m}')
        check({pt for pt in s if up(pt)==(0,0,0,0)}==set(product([0],[0],range(2),range(2))),f'j kernel rational torsion m={m}')

print(json.dumps({'status':'PASS','python':platform.python_version(),'sympy':sp.__version__,
  'assertions':len(checks),'checks':checks,'tripling_numerator':str(N3),'tripling_denominator':str(psi3**2),
  'finite_groups':mod_rows,'nondivisibility_certificate':tripling_certificate,
  'rational_representatives':rational_rows,'coefficient_checks':coefficient_rows,'abstract_towers':abstract,
  'scope':'Exact polynomial identity; finite fields3,5,7,11; rational representatives m<=4; coefficients m<=64; abstract levels1..4. No estimated canonical heights or arithmetic realization of rank0/rank1 abstract scenarios.'},indent=2))
