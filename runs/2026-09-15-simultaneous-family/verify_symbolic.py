"""Exact independent checks for the finite contract, not a proof assistant."""
from fractions import Fraction
from math import gcd, isqrt
from pathlib import Path
import json
import sympy as sp

ROOT = Path(__file__).resolve().parent
checks = 0

def check(ok: bool, label: str) -> None:
    global checks
    checks += 1
    if not ok:
        raise AssertionError(label)

def rank2(matrix: list[list[int]]) -> int:
    a = [row[:] for row in matrix]
    if not a:
        return 0
    pivot = 0
    for j in range(len(a[0])):
        row = next((i for i in range(pivot, len(a)) if a[i][j] % 2), None)
        if row is None:
            continue
        a[pivot], a[row] = a[row], a[pivot]
        for i in range(len(a)):
            if i != pivot and a[i][j] % 2:
                a[i] = [(x+y) % 2 for x, y in zip(a[i], a[pivot], strict=True)]
        pivot += 1
    return pivot

a, b, t, n, s, A, B, x, y = sp.symbols('a b t n s A B x y')
d = a**8 - 56*a**4*b**4 + 1296*b**8
fm = a**4 - 4*a**3*b + 8*a*a*b*b - 24*a*b**3 + 36*b**4
fp = fm.subs(a, -a)
check(sp.expand(d - (a**4-28*b**4)**2-512*b**8) == 0, 'positive norm identity')
check(sp.expand(d-fm*fp) == 0, 'two quartic factors')
check(sp.expand(fp-fm-8*a*b*(a*a+6*b*b)) == 0, 'factor difference')
for e in [-1,1]:
    fe = fm if e == -1 else fp
    check(sp.expand(fe-(a*a+2*e*a*b)**2-4*b*b*(a+3*e*b)**2)==0,'positive factor identity')
check(sp.discriminant(fm.subs({a:t,b:1}),t)==2**16*3**2,'prime-filter quartic discriminant')

check(sp.rem(a**4+8*a*a*b*b+36*b**4, a*a+6*b*b, a) == 24*b**4, 'common-factor exclusion')
Dpoly = d.subs({a:t,b:1})
check(sp.factor(sp.diff(Dpoly,t)) == 8*t**3*(t**4-28), 'derivative structure')
check(sp.rem(Dpoly,t**4-28,t) == 512, 'all primes outside two and three give simple roots')
check(sp.discriminant(Dpoly,t) == 2**72*3**12, 'integer discriminant')
for eps in [-1,1]:
    Ap = a*a-6*eps*b*b
    Bp = 2*a*b
    check(sp.expand(Ap**4+6*eps*Ap*Ap*Bp*Bp+Bp**4-d) == 0, 'simultaneous identity')
    v = A*A-eps*B*B; w = A*A+eps*B*B; z = 2*A*B
    F = A**4+6*eps*A*A*B*B+B**4
    check(sp.expand(v*v-w*w+eps*z*z) == 0, 'generic first quadric')
    check(sp.expand(w*w+eps*z*z-F) == 0, 'generic second quadric')
    # Impose n*s^2=F only after forming the rational curve residual.
    xx = n*w*w/z**2; yy = n*n*s*v*w/z**3
    residual = sp.factor(yy*yy-xx**3+n*n*xx)
    check(sp.factor(residual - n**3*v*v*w*w*(n*s*s-F)/z**6) == 0, 'generic curve identity')
    check(sp.gcd(sp.Poly(Ap,a),sp.Poly(Bp,a)).as_expr() == 1, 'no common polynomial A/B factor over Q(b)')

# The discarded degree-six bridge has a fixed odd valuation at three.
check(all((aa*aa+bb*bb) % 3 != 0 for aa in range(3) for bb in range(3) if (aa,bb)!=(0,0)), 'anisotropy modulo three')
# Verify the finite residue arithmetic actually used in the valuation proof.
for aa in range(2):
    for bb in range(2):
        if (aa,bb)==(0,0):
            continue
        if aa:
            check((aa**8-56*aa**4*bb**4+1296*bb**8) % 8 == 1, 'odd a mod eight')
for k in range(8):
    for bb in [1,3,5,7]:
        check((16*k**8-56*k**4*bb**4+81*bb**8) % 8 == 1, 'even a normalized unit')
for k in range(3):
    for bb in [1,2]:
        check((81*k**8-56*k**4*bb**4+16*bb**8) % 3 != 0, 'exact fourth three-adic valuation')

params = [(1,1),(2,1),(3,1),(4,1),(5,1),(7,1),(1,2),(3,2)]
saved = json.loads((ROOT/'results/integer-results.json').read_text())
check([(int(r['a']),int(r['b'])) for r in saved['rows']] == params, 'exact finite population')
rows = []
for (aa,bb), tsrow in zip(params,saved['rows'],strict=True):
    dd = aa**8-56*aa**4*bb**4+1296*bb**8
    fac = sp.factorint(dd)
    nn = int(sp.prod(p for p,e in fac.items() if e%2))
    ss = isqrt(dd//nn)
    check(nn*ss*ss==dd and nn>1, 'normalization')
    check(nn == int(tsrow['n']), 'independent factorization agreement')
    primes = sorted(int(p) for p,e in fac.items() if e%2)
    check(all(p%8==1 for p in primes), 'prime support')
    p0 = int(fm.subs({a:aa,b:bb})); p1=int(fp.subs({a:aa,b:bb}))
    cc=(2 if aa%2==0 else 1)*(3 if aa%3==0 else 1)
    check(gcd(p0,p1)==cc*cc, 'factor gcd')
    check(gcd(p0//(cc*cc),p1//(cc*cc))==1, 'normalized factors coprime')
    for eps, tspt in zip([-1,1],tsrow['points'],strict=True):
        Ap=aa*aa-6*eps*bb*bb; Bp=2*aa*bb
        u=nn*ss; v=Ap*Ap-eps*Bp*Bp; w=Ap*Ap+eps*Bp*Bp; z=2*Ap*Bp
        check(v*v-w*w+eps*z*z == 0 and u*u-nn*w*w-eps*nn*z*z == 0,'both covering quadrics')
        xx=Fraction(nn*w*w,z*z); yy=Fraction(nn*u*v*w,z**3)
        check(yy*yy == xx**3-nn*nn*xx,'Fraction curve equation')
        check(yy != 0,'nontorsion candidate has nonzero y')
        labels = [1,nn,nn] if eps==-1 else [nn,1,nn]
        roots = [u,v,w] if eps==-1 else [v,u,w]
        check(all(q == label*Fraction(root,z)**2 for q,label,root in zip([xx-nn,xx+nn,xx],labels,roots,strict=True)), 'Kummer factors')
        check(xx == Fraction(int(tspt['x']['num']),int(tspt['x']['den'])) and yy == Fraction(int(tspt['y']['num']),int(tspt['y']['den'])),'independent point agreement')
        legs=[abs(2*nn*xx/yy),abs((xx*xx-nn*nn)/yy),abs((xx*xx+nn*nn)/yy)]
        check(legs[0]**2+legs[1]**2==legs[2]**2 and legs[0]*legs[1]/2==nn,'rational triangle certificate')
    mat=[[0 if i==j else (1-int(sp.legendre_symbol(q,p)))//2 for j,q in enumerate(primes)] for i,p in enumerate(primes)]
    for i,row in enumerate(mat): row[i]=sum(row)%2
    upper=2*(len(primes)-rank2(mat))
    check(mat == tsrow['matrix'] and upper == tsrow['rankUpper'], 'independent Monsky matrix')
    rows.append({'a':aa,'b':bb,'D':dd,'n':nn,'rankLower':2,'rankUpper':upper})

K=sp.Matrix([[0,1,0,0,1,1,0,0,1],[1,0,1,0,0,1,1,0,0],[0,0,0,0,0,1,0,0,1],[0,0,1,0,0,0,0,0,1]])
check(int(K[:,[0,1,2,5]].det())%2==1,'minor determinant')
# Two finite demonstrations of the universal simple-root lifting argument.
lifts=[]
for q,root in [(17,1),(41,2)]:
    value=lambda z:z**8-56*z**4+1296
    check(value(root)%q==0 and (8*root**3*(root**4-28))%q!=0,'simple root fixture')
    choices=[j for j in range(q) if value(root+q*j)%(q*q)==0]
    check(len(choices)==1,'unique bad lift')
    j=next(j for j in range(q) if j not in choices)
    t0=root+q*j
    check(value(t0)%q==0 and value(t0)%(q*q)!=0,'valuation one at a good lift')
    lifts.append({'q':q,'root':root,'badJ':choices[0],'chosenT':t0})

result={'status':'passed finite and symbolic checks; universal deductions remain written proofs','assertions':checks,'rows':rows,'simpleRootExamples':lifts,'versions':{'sympy':sp.__version__}}
(ROOT/'results/symbolic-results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
