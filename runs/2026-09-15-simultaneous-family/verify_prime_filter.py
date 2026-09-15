"""Independent exact symbolic and finite prime-filter certificates."""
from pathlib import Path
import json
import sympy as sp

ROOT=Path(__file__).resolve().parent
checks=0

def check(ok: bool, label: str) -> None:
    global checks
    checks+=1
    if not ok:
        raise AssertionError(label)

t,w,x,y=sp.symbols('t w x y')
g=t**4-4*t**3+8*t**2-24*t+36
xx=(w+t*t-2*t)/2
yy=(xx+1)*(t-1)-2
ti=1+(y+2)/(x+1)
wi=2*x+1-((y+2)/(x+1))**2
check(sp.expand(yy*yy-xx*(xx-1)*(xx+3)+(t*t-2*t+w+2)*(w*w-g)/8)==0,'generic forward identity')
check(sp.factor(wi*wi-g.subs(t,ti)+4*(y*y-x*(x-1)*(x+3))/(x+1))==0,'generic inverse residual')
check(sp.simplify(xx.subs({t:ti,w:wi})-x)==0,'inverse then forward x')
check(sp.simplify(yy.subs({t:ti,w:wi})-y)==0,'inverse then forward y')
check(sp.factor(1+(yy+2)/(xx+1)-t)==0,'forward then inverse t')
check(sp.factor(2*xx+1-((yy+2)/(xx+1))**2-w)==0,'forward then inverse w')
check(sp.expand(g-(t*t-2*t+2)**2-16*(2-t))==0,'exceptional fibre identity')
I=12*36-3*(-4)*(-24)+8**2
J=72*8*36-27*(-24)**2-27*(-4)**2*36+9*(-4)*8*(-24)-2*8**3
check((I,J)==(208,-4480),'quartic invariants')
check(sp.discriminant(g,t)==2**16*3**2,'polynomial discriminant')
check(sp.expand((36*x+24)**3-27*I*(36*x+24)-27*J-216**2*x*(x-1)*(x+3))==0,'Jacobian scaling')
check(16*sp.discriminant(x*(x-1)*(x+3),x)==2304,'elliptic discriminant')
# Two-isogeny target, with source equation imposed by polynomial remainder.
fx=x*x+2*x-3
phiX=x+2-3/x
phiY=y*(-3-x*x)/(x*x)
num=sp.together(phiY**2-phiX**3+4*phiX**2-16*phiX).as_numer_denom()[0]
check(sp.rem(sp.Poly(num,y),sp.Poly(y*y-x*fx,y)).as_expr()==0,'isogeny equation')
pts=[(0,0),(1,0),(-3,0),(3,6),(3,-6),(-1,2),(-1,-2)]
check(len(set(pts))==7 and all(b*b==a*(a-1)*(a+3) for a,b in pts),'seven affine points')
saved=json.loads((ROOT/'results/prime-filter-integer.json').read_text())
reductions=[]
for p,ts in zip([5,7],saved['reductions'],strict=True):
    # Count via Legendre symbols, unlike the two-coordinate TypeScript iterator.
    order=1+sum(1+int(sp.legendre_symbol(a*(a-1)*(a+3),p)) for a in range(p))
    check(order==8 and order==ts['order'],'independent finite field order')
    reductions.append({'prime':p,'order':order})
residues={r*r%16 for r in range(16)}
possible={ (2*s**4-4*s*s*t*t+8*t**4)%16 for s in range(16) for t in range(16) if s%2 or t%2}
check(not possible.intersection(residues),'primitive quartic square-residue exclusion')
check(possible=={2,6,8},'exact primitive right-hand-side residues')
check(all((s**4-2*s*s*t*t+4*t**4)%2==1 for s in [1,3,5,7] for t in range(8)),'odd s valuation one')
check(all((s**4-2*s*s*t*t+4*t**4)%8==4 for s in [0,2,4,6] for t in [1,3,5,7]),'even s valuation three')
# Apply the explicit inverse to the finite E0 list, not a rational search.
affine=[]
for a,b in pts:
    if a==-1:
        continue
    tt=sp.cancel(ti.subs({x:a,y:b}))
    ww=sp.cancel(wi.subs({x:a,y:b}))
    check(sp.expand(ww*ww-g.subs(t,tt))==0,'inverse point equation')
    affine.append((int(tt),int(ww)))
affine.append((2,-2))
expected={(0,6),(0,-6),(2,2),(2,-2),(3,3),(3,-3)}
check(set(affine)==expected and len(affine)==6,'affine completeness from eight-point list')
check(xx.subs({t:2,w:-2})==-1 and yy.subs({t:2,w:-2})==-2,'exceptional image')
for tt in [-3,-2,2,3]:
    dd=tt**8-56*tt**4+1296
    fac=sp.factorint(dd)
    nn=int(sp.prod(q for q,e in fac.items() if e%2))
    check(nn==41,'prime kernel at each allowed parameter')
result={'status':'passed symbolic and finite prime-filter checks','assertions':checks,'invariants':{'I':I,'J':J},'finiteFields':reductions,'primitiveRHSmod16':sorted(possible),'affineQuarticPoints':sorted(expected),'scope':'Completeness uses the prose rank-zero and torsion argument; no general BSD claim.'}
(ROOT/'results/prime-filter-symbolic.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
