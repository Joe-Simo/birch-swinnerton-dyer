"""Exact symbolic certificate checking, not a general descent implementation.
Domain: Q-polynomials, Q(sqrt(113)), fixed p-adic starting points, n=113 counts.
The written proof supplies Hensel convergence, all-prime coverage, and interpretation.
"""
from __future__ import annotations
import json
import platform
import time
from math import isqrt
import sympy as sp

start = time.perf_counter()
c,d,t,z,l,m,a,b,w,x,y,X,Y = sp.symbols('c d theta psi l m a b w x y X Y')
p = 113
checks: list[str] = []
def check(condition: bool, label: str) -> None:
    if not condition:
        raise AssertionError(label)
    checks.append(label)
def zero(expr: sp.Expr, label: str) -> None:
    check(sp.cancel(expr) == 0, label)
def val(q: sp.Expr, prime: int) -> int | float:
    q = sp.Rational(q)
    if q == 0:
        return float('inf')
    def vint(n: int) -> int:
        n=abs(n); v=0
        while n%prime == 0:
            v+=1; n//=prime
        return v
    return vint(int(q.p))-vint(int(q.q))
def residue(q: sp.Expr, modulus: int) -> int:
    q=sp.Rational(q)
    return int(q.p)*pow(int(q.q),-1,modulus)%modulus

def red(expr: sp.Expr) -> sp.Expr:
    return sp.rem(sp.together(expr).expand(),w*w-p,w)
f=7*l*l-16*l*m-7*m*m; g=4*l*l+7*l*m-4*m*m; h=p*(l*l+m*m)
P=[c*c+8*c*d+23*d*d,-c*c+7*d*d,4*c*c+30*c*d+28*d*d]
Q=[t*t+4*z*z,7*z*z-4*t*z,-2*t*t+7*t*z+8*z*z]
F=[P[0]-Q[0],P[1]-Q[1]]
zero(h*h-p*(f*f+4*g*g),'base conic identity')
zero(f.subs({l:P[0],m:P[1]})-P[2]**2,'first rational conic parametrization')
zero(g.subs({l:Q[0],m:Q[1]})-Q[2]**2,'second rational conic parametrization')
zero(sp.Rational(15,226)*P[0]-sp.Rational(1,226)*P[1]-sp.Rational(2,113)*P[2]-d*d,'pushout f3 normalization')
vars4=[c,d,t,z]
A=sp.hessian(F[0],vars4)/2; B=sp.hessian(F[1],vars4)/2
pencil=sp.factor((a*A+b*B).det())
expected=(7*a*a-16*a*b-7*b*b)*(4*a*a+7*a*b-4*b*b)
zero(pencil-expected,'C3 pencil determinant')
check(sp.discriminant(pencil.subs(b,1),a)==4*p**6,'C3 discriminant = 4*113^6')
C2=[f-sp.Symbol('s')**2,g-sp.Symbol('r')**2]
variables2=[l,m,sp.Symbol('s'),sp.Symbol('r')]
pencil2=sp.factor((a*sp.hessian(C2[0],variables2)/2+b*sp.hessian(C2[1],variables2)/2).det())
zero(pencil2+sp.Rational(p,4)*a*b*(4*a*a+b*b),'C2 smooth pencil')
zero(sp.resultant(P[0],P[1],c)-4*p*d**4,'no projection basepoint away from 2,113')
eps=(8+w)/7; alpha=(15+w)/7; gamma=(15-w)/4
zero(red(P[0]-eps*P[1]-alpha*(c+gamma*d)**2),'quadratic-field square factor')
conic=Q[0]-eps*Q[1]-alpha*sp.Symbol('Z')**2
zero(red(conic.subs({t:-6-w,z:1,sp.Symbol('Z'):(1-w)/2})),'point on field conic')
U=49*c-14*d-26*t-350*z; V=7*c+14*d-5*t-35*z
norm=sp.expand(U*U-p*V*V)
# Half-gradient tangent at the verified point, multiplied by 7.
Z=sp.Symbol('Z')
pointL={t:-6-w,z:1,Z:(1-w)/2}
tangent=sum(sp.diff(conic,k).subs(pointL)*k/2 for k in[t,z,Z])
zero(red(7*tangent.subs(Z,c+gamma*d)-(U+w*V)),'tangent form and rational norm')
conic_det=sp.factor((sp.hessian(conic,[t,z,Z])/2).det())
conic_det=red(conic_det)
conic_norm=red(conic_det*conic_det.subs(w,-w))
zero(conic_norm+sp.Rational(16*p*p,7**3),'field conic good primes')
pt2={c:sp.Rational(15035,9471),d:2,t:sp.Rational(-121505,9471),z:1}
errors=[sp.factor(q.subs(pt2)) for q in F]
jac=sp.Matrix(F).jacobian([c,t])
delta=val(jac.det().subs(pt2),2)
check([val(q,2) for q in errors]==[18,20] and delta==2,'strict two-variable Hensel certificate')
norm_value=sp.factor(norm.subs(pt2))
check(val(norm_value,2)==7 and residue(norm_value,1024)==640,'2-adic Hilbert unit certificate')
pt113={c:21,d:-8,t:0,z:1}
check([q.subs(pt113) for q in F]==[565,0],'113-adic local residuals')
check(sp.Matrix(F).jacobian([t,z]).det().subs(pt113)==32,'113-adic nonsingular minor')
# Exact real point; reduce successively by theta^2=30+8c and c^2=7, d=1, psi=0.
for q in F:
    q=q.subs({d:1,z:0})
    q=sp.rem(q,t*t-30-8*c,t)
    zero(sp.rem(q,c*c-7,c),'real point residual')
# Independent direct check of the isogeny and Kummer-coordinate diagram.
phiX=(x*x-p*p)/x; phiY=-(x*x+p*p)*y/x**2
isog_res=sp.together(phiY**2-phiX**3-4*p*p*phiX)
zero(sp.rem(sp.fraction(isog_res)[0],y*y-x**3+p*p*x,y),'isogeny identity modulo source equation')
hatX=(X*X+4*p*p)/(4*X)
zero(hatX-p-(X-2*p)**2/(4*X),'first Kummer coordinate pullback')
zero(hatX+p-(X+2*p)**2/(4*X),'second Kummer coordinate pullback')
zero((hatX-(Y/(2*X))**2).subs(Y**2,X**3+4*p*p*X),'third Kummer coordinate pullback')

def count(coef: int) -> int:
    answer=0
    for xx in range(-isqrt(p),isqrt(p)+1):
        for yy in range(-isqrt(p//2),isqrt(p//2)+1):
            for zz in range(-isqrt(p//coef),isqrt(p//coef)+1):
                answer += int(xx*xx+2*yy*yy+coef*zz*zz==p)
    return answer
counts=[count(8),count(32)]
check(counts==[32,24] and counts[1]-counts[0]//2==8,'Tunnell exact signed counts')
for wrong,label in [(red(P[0]-eps*P[1]+alpha*(c+gamma*d)**2),'wrong factor sign'),
                    (sp.expand((norm+1)-(U*U-p*V*V)),'changed norm form')]:
    check(wrong != 0,'negative control: '+label)
report={'status':'passed fixed exact checks','python':platform.python_version(),'sympy':sp.__version__,
        'checks':checks,'number_of_checks':len(checks),'runtime_seconds':time.perf_counter()-start,
        'C3_pencil':str(pencil),'C2_pencil':str(pencil2),'field_conic_det_norm':str(conic_norm),
        'Q2_errors':[str(q) for q in errors],'Q2_norm':str(norm_value),'Q2_norm_residue_mod1024':640,
        'counts_8_32':counts,'Tunnell_coefficient':8,
        'limitations':'Not a proof-assistant verification or a universal BSD computation; see written source-dependent proof.'}
print(json.dumps(report,indent=2))
