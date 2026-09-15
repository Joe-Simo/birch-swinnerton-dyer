"""Independent symbolic and rational certificate checks, not a proof-assistant build."""
from __future__ import annotations

from fractions import Fraction
from itertools import product
from pathlib import Path
import json
import math
import platform
import sympy as sp

ROOT = Path(__file__).resolve().parent
checks = 0

def check(condition: bool, label: str) -> None:
    global checks
    checks += 1
    if not condition:
        raise AssertionError(label)

def zero(expr: sp.Expr, label: str) -> None:
    check(sp.cancel(expr) == 0, label)

x, y, z, k, t, a, jx, jy = sp.symbols('x y z k t a jx jy')
pplus = x**4+6*x**2+1
pminus = y**4-6*y**2+1
F = pminus-k*pplus
FH = y**4-k*x**4-6*y*y*z*z-6*k*x*x*z*z+(1-k)*z**4
zero(FH.subs(z,1)-F, 'homogenization')
zero(F.subs(k,1)-(x*x+y*y)*(y*y-x*x-6), 'exceptional fiber factorization')
zero(sp.diff(FH,x)+4*k*x*(x*x+3*z*z), 'X derivative')
zero(sp.diff(FH,y)-4*y*(y*y-3*z*z), 'Y derivative')
zero(sp.diff(FH,z)-(-12*y*y*z-12*k*x*x*z+4*(1-k)*z**3), 'Z derivative')
# Critical cases after setting Z=1; Euler's identity supplies F_Z when F=F_X=F_Y=0.
critical = []
for xsq, ysq in product([0,-3],[0,3]):
    v = sp.expand(ysq**2-6*ysq+1-k*(xsq**2+6*xsq+1))
    critical.append(v)
check(critical == [1-k,-8-k,1+8*k,8*k-8], 'four critical values')
zero(x*sp.diff(FH,x)+y*sp.diff(FH,y)+z*sp.diff(FH,z)-4*FH,'Euler identity')

# No rational square k can equal -8 or -1/8; k=0 excluded. The proof handles infinity separately.
U=y*y-3
V2=k*(x*x+3)**2
W=(y**4-k*x**4-3*y*y-3*k*x*x)/(x*x)
gy=k*t**4+6*k*t*t+k+8
gx=t**4-6*t*t+1+8*k
gxy=(k+8)*t**4+18*k*t*t+k*(1+8*k)
zero(U**2-gy.subs(t,x)-F,'Dy pullback residual')
zero(V2-gx.subs(t,y)+F,'Dx pullback residual')
# The W equation is reduced modulo the original defining equation.
gxy_res=sp.together((W**2-gxy.subs(t,y/x))*x**4)
check(sp.rem(gxy_res,F,y)==0,'Dxy pullback remainder')
zero((gy.subs(t,x)+6*U+9)-k*pplus-6*U-9-8,'Dy auxiliary accounting')
# Differential pullbacks onto the three independent canonical forms.
fx,fy=sp.diff(F,x),sp.diff(F,y)
dydx=-fx/fy
zero(1/U-4*y/fy,'Dy differential character')
# Use V=q(x²+3); after dividing by4q this is x dx/F_y, avoiding adjoining q.
zero(dydx/(4*k*(x*x+3))-x/fy,'Dx differential character')
zero(((x*dydx-y)/x**2)/W+4/fy,'Dxy differential character')

expected = [
    (48*k*(k+2),3456*k*k),
    (48*(1+2*k),-3456*k),
    (48*k*(2*k*k+23*k+2),10368*k*k*(k*k+7*k+1))
]
model_terms = [(-k*(k+2),-2*k*k),(-(1+2*k),2*k),(-k*(2*k*k+23*k+2),-6*k*k*(k*k+7*k+1))]
expected_factors=[(jx+k)*(jx*jx-k*jx-2*k),(jx-1)*(jx*jx+jx-2*k),(jx+3*k)*(jx*jx-3*k*jx-2*k*(k*k+7*k+1))]
quotients=[]
for name,g,ij,ab,factor in zip(['Dy','Dx','Dxy'],[gy,gx,gxy],expected,model_terms,expected_factors):
    poly=sp.Poly(g,t)
    A,B,C=poly.nth(4),poly.nth(2),poly.nth(0)
    I,J=12*A*C+B*B,72*A*B*C-2*B**3
    zero(I-ij[0],f'{name} I')
    zero(J-ij[1],f'{name} J')
    zero(-I/48-ab[0],f'{name} scaled A')
    zero(-J/1728-ab[1],f'{name} scaled B')
    zero(jx**3+ab[0]*jx+ab[1]-factor,f'{name} cubic factor')
    source=(216*jy)**2-(36*jx)**3+27*I*(36*jx)+27*J
    zero(source/216**2-(jy*jy-jx**3-ab[0]*jx-ab[1]),f'{name} Jacobian scaling')
    disc=sp.factor(sp.discriminant(g,t))
    # Values of the critical t² polynomial determinant preclude repeated roots for k>0,k!=1.
    delta=sp.factor(B*B-4*A*C)
    check(delta != 0,f'{name} generic separability')
    quotients.append({'name':name,'quartic':str(g),'I':str(sp.factor(I)),'J':str(sp.factor(J)),
                      'polynomial_discriminant':str(disc),'middle_discriminant':str(delta),
                      'Jacobian':[str(v) for v in ab],
                      'elliptic_discriminant':str(sp.factor(-16*(4*ab[0]**3+27*ab[1]**2)))})
# Preserve the varying-ratio surface instead of treating infinitely many fibers as one curve.
qvar, wvar = sp.symbols('qvar wvar')
zero((wvar*wvar-pplus*pminus).subs(wvar,qvar*pplus) + pplus*F.subs(k,qvar*qvar),
     'birational surface transformation W=q F_plus')
for g in [t**4+6*t*t+1,t**4-6*t*t+1]:
    poly=sp.Poly(g,t); A,B,C=poly.nth(4),poly.nth(2),poly.nth(0)
    check(12*A*C+B*B==48 and 72*A*B*C-2*B**3==0, 'two base quartics have Jacobian E1')

# Local all-unit polynomial identities; a encodes (z²-1)/8.
zero(((1+8*a)**2+6*(1+8*a)+1)/8-(1+8*a+8*a*a),'odd plus identity')
zero(-((1+8*a)**2-6*(1+8*a)+1)/4-(1+8*a-16*a*a),'odd minus identity')
zero((2*a)**4+6*(2*a)**2+1-(1+8*(2*a**4+3*a*a)),'even plus identity')
zero((2*a)**4-6*(2*a)**2+1-(1+8*(2*a**4-3*a*a)),'even minus identity')
zero(x**4*((1/x)**4+6/x**2+1)-pplus,'plus reciprocity')
zero(y**4*((1/y)**4-6/y**2+1)-pminus,'minus reciprocity')

# Independent modulo16 enumeration uses projective charts: first odd coordinate normalized to1.
# Every primitive triple can be scaled uniquely into one of these disjoint charts for its first odd slot.
q=Fraction(7,2)
charts=[[(1,Y,Z) for Y,Z in product(range(16),repeat=2)],
        [(X,1,Z) for X in range(0,16,2) for Z in range(16)],
        [(X,Y,1) for X,Y in product(range(0,16,2),repeat=2)]]
chart_solutions=[]
chart_counts=[]
for chart in charts:
    chart_counts.append(len(chart))
    for X,Y,Z in chart:
        res=4*(Y**4-6*Y*Y*Z*Z+Z**4)-49*(X**4+6*X*X*Z*Z+Z**4)
        if res%16==0:
            chart_solutions.append((X,Y,Z))
check(chart_counts == [256,128,64], 'disjoint primitive projective chart coverage')
check(chart_solutions == [], 'independent chart obstruction')
check(sum(chart_counts)*8==3584,'eight unit multiples per projective residue')

# The quotient points are on the actual genus-one models, not just their Jacobians.
qq=sp.Rational(7,2); kk=qq*qq
check(gy.subs({k:kk,t:0})==sp.Rational(9,2)**2,'Dy rational point')
check(sp.Poly(gx,t).nth(4).subs(k,kk)==1,'Dx rational infinity point')
check(sp.Poly(gxy,t).nth(4).subs(k,kk)==sp.Rational(9,2)**2,'Dxy rational infinity point')
check(sp.Rational(9,2)+3==sp.Rational(15,2),'positive Dy branch fails square lift')
check(-sp.Rational(9,2)+3==-sp.Rational(3,2),'negative Dy branch fails square lift')

# Read the exact certificate fields, then recompute using Fraction without the TS integer identities.
integer=json.loads((ROOT/'results/integer-results.json').read_text())
frac_rows=[]
for row in integer['fixtures']:
    p=int(row['p']); n,d=map(int,row['q']); X,Y,Z=map(int,row['point'])
    Xf,Yf=Fraction(X,Z),Fraction(Y,Z); qf=Fraction(n,d)
    fp=Xf**4+6*Xf**2+1; fm=Yf**4-6*Yf**2+1
    check(fm==qf*qf*fp,f'{p} independent affine ratio')
    rootn,rootd=math.isqrt((fp/p).numerator),math.isqrt((fp/p).denominator)
    check(Fraction(rootn*rootn,rootd*rootd)==fp/p,f'{p} exact common squarefree kernel')
    uf=Yf*Yf-3; vf=qf*(Xf*Xf+3); tf=Yf/Xf
    wf=(tf**4-qf*qf)*Xf*Xf-3*(tf*tf+qf*qf)
    check(uf*uf==qf*qf*Xf**4+6*qf*qf*Xf*Xf+qf*qf+8,f'{p} quotient y')
    check(vf*vf==Yf**4-6*Yf*Yf+1+8*qf*qf,f'{p} quotient x')
    check(wf*wf==(qf*qf+8)*tf**4+18*qf*qf*tf*tf+qf*qf*(1+8*qf*qf),f'{p} quotient xy')
    frac_rows.append({'p':p,'q':str(qf),'x':str(Xf),'y':str(Yf)})
check(F.subs({k:sp.Rational(47,17)**2,x:sp.Rational(1,14),y:sp.Rational(37,14)})==0,'p137 small reciprocal q47/17')

out={'status':'passed; no full BSD claim','checks':checks,'Python':platform.python_version(),'SymPy':sp.__version__,
     'critical_values':list(map(str,critical)),'quotients':quotients,
     'independent_local_charts':chart_counts,'primitive_projective_classes':sum(chart_counts),
     'chart_solutions':chart_solutions,'affine_witnesses':frac_rows,
     'scope':'generic polynomial identities, seven rational fixtures, and exact modulo16 obstruction; finiteness is a cited external theorem'}
(ROOT/'results/symbolic-results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
