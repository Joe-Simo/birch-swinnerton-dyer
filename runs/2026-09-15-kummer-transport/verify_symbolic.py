"""Independent H12 checker: SymPy identities and Fraction certificate replay."""
from fractions import Fraction as Q
from pathlib import Path
import json
from math import gcd, isqrt, prod
import sympy as s

count=0
def check(ok,label):
    global count
    count+=1
    if not ok: raise AssertionError(label)
def zero(expr,label): check(s.cancel(expr)==0,label)
t,r,u,v,X,Y,W,a,b,C,K,h,z=s.symbols('t r u v X Y W a b C K h z')
for e in (1,-1):
    F=t**4+6*e*t*t+1
    rel=s.Poly(r*r-F,r,domain=s.QQ.frac_field(t))
    def red(expr):
        n,d=s.fraction(s.cancel(expr))
        return (s.Poly(n,r,domain=rel.domain).rem(rel)*s.invert(s.Poly(d,r,domain=rel.domain),rel)).rem(rel).as_expr()
    U=(r+1+e*t*t)/(2*t*t); V=(r+1+3*e*t*t)/(2*t**3)
    zero(red(V*V-U**3+U),'quartic to E0')
    tinv=(u+e)/v;rinv=(2*u-e)*tinv*tinv-1
    zero(red(tinv.subs({u:U,v:V}))-t,'inverse t')
    zero(red(rinv.subs({u:U,v:V}))-r,'inverse r')
    # T=(-e,0). T-P has x=-e+2/(u+e), y=+2v/(u+e)^2.
    zero(red(U.subs(r,-r)-(-e+2/(U+e))),'deck x')
    zero(red(V.subs(r,-r)-2*V/(U+e)**2),'deck y')
    u2=(u*u+1)**2/(4*u*(u*u-1))
    v2factor=s.diff(u2,u)/2
    zero(red(u2.subs(u,U))-(t*t+e)**2/(4*t*t),'old H8 x is doubling')
    zero(red(-V*v2factor.subs(u,U))-r*(t**4-1)/(8*t**3),'old H8 y is negative doubling')
    N=t*(t**8-6*t**4-24*e*t*t-3)
    D=3*t**8+24*e*t**6+6*t**4-1
    H=t**16+24*e*t**14+28*t**12+168*e*t**10+582*t**8+168*e*t**6+28*t**4+24*e*t*t+1
    check(s.gcd(N,D)==1,'tripling degree nine')
    zero(s.diff(N/D,t)/3-H/D**2,'tripling differential')
    zero(s.expand(N**4+6*e*N*N*D*D+D**4-F*H*H),'tripling square identity')

Fp=X**4+6*X*X+1; Fm=Y**4-6*Y*Y+1
U=X*X+3; V=Y*Y-3
zero((U*V-8)**2-Fp*Fm-8*(U-V)**2,'surface norm identity')
zero((U+a)*(V-a)-(U*V-8-a*(U-V))-(8-a*a),'factorization')
zero((a+3)**2-(6*a+17)-(a*a-8),'fiber determinant')
f=lambda T:(T*T+C)*(C*T*T+K)
f0=f(t)
d1=s.diff(f0,t)/(2*z)
d2=(s.diff(f0,t,2)/2-d1*d1)/(2*z)
p=s.expand(z+d1*h+d2*h*h)
R3=s.diff(f0,t,3)/6-2*d1*d2
R4=C-d2*d2
zero(f(t+h)-p*p-(f0-z*z)-R3*h**3-R4*h**4,'osculating fourth-intersection identity')
zero(s.discriminant(f(t),t)-16*C*C*K*(C*C-K)**4,'smooth-fiber discriminant')

# Independent numeric construction: compute the osculating polynomial via SymPy
# and find the remaining root from the quotient, not via the TypeScript formula.
x0=Q(1,14);y0=Q(37,14);w0=Q(137*17*47,196**2)
U0=x0*x0+3;V0=y0*y0-3
aa=(U0*V0-8)/(U0-V0);bb=w0/(U0-V0);cc=aa+3;kk=6*aa+17
z0=y0*(x0*x0+cc)
pol=s.Poly(f(t).subs({C:s.Rational(cc.numerator,cc.denominator),K:s.Rational(kk.numerator,kk.denominator)}),t)
xx=s.Rational(x0.numerator,x0.denominator);zz=s.Rational(z0.numerator,z0.denominator)
a1=pol.diff().eval(xx)/(2*zz)
a2=(pol.diff().diff().eval(xx)/2-a1*a1)/(2*zz)
quad=zz+a1*(t-xx)+a2*(t-xx)**2
remaining=s.div(pol-s.Poly(quad**2,t),s.Poly((t-xx)**3,t))
check(remaining[1].is_zero,'exact triple contact at137')
check(remaining[0].degree()==1,'fourth root unique in open chart')
x1=-remaining[0].nth(0)/remaining[0].nth(1)
z1=quad.subs(t,x1);y1=z1/(x1*x1+cc);w1=bb*(x1*x1-y1*y1+6)
check(x1==s.Rational(-16890371,79256324),'independent x')
check(y1==s.Rational(210069683,77723044),'independent y')
check(w1*w1==(x1**4+6*x1*x1+1)*(y1**4-6*y1*y1+1),'surface output')
check((x1*x1+3)*(y1*y1-3)-8==aa*(x1*x1-y1*y1+6),'same fiber')
factors=[17,137,16273,19642387489,233758085129]
for prime in factors:
    # Full trial division certifies every factor without a probabilistic oracle.
    check(prime>2 and prime%2!=0 and all(prime%d for d in range(3,isqrt(prime)+1,2)),f'prime {prime}')
N=prod(factors)
check(N==174019544752618399630591052177,'kernel product')
for e,A,B,c in [(1,79256324,16890371,17),(-1,210069683,77723044,47)]:
    check(A>B>0 and gcd(A,B)==1 and (A-B)%2==1,'primitive opposite-parity witness')
    check(A**4+6*e*A*A*B*B+B**4==N*c*c,'integer quartic')
    uu=N*c;vv=A*A-e*B*B;ww=A*A+e*B*B;zz=2*A*B
    check(vv*vv-ww*ww+e*zz*zz==0,'Pythagorean quadric')
    check(uu*uu-N*ww*ww-e*N*zz*zz==0,'second quadric')
    xp=Q(N*ww*ww,zz*zz);yp=Q(N*uu*vv*ww,zz**3)
    check(yp*yp==xp**3-N*N*xp,'elliptic image')
    labels=(N,1,N) if e==1 else (1,N,N)
    fs=(Q(vv,zz),Q(uu,zz),Q(ww,zz)) if e==1 else (Q(uu,zz),Q(vv,zz),Q(ww,zz))
    for target,label,square in zip((xp-N,xp+N,xp),labels,fs):check(target==label*square*square,'Kummer square factor')
labels=((2,2*N,N),(-N,N,-1),(1,N,N),(N,1,N))
vectors=[[bit for a in row for bit in (int(a<0),int(abs(a)%2==0),int(abs(a)%N==0))] for row in labels]
M=s.Matrix([[row[j] for j in (0,1,2,5)] for row in vectors])
check(abs(M.det())==1,'independence over F2')
ratio=s.factor((x1**4+6*x1*x1+1)/(xx**4+6*xx*xx+1))
num,den=map(int,s.fraction(ratio))
check(num%17==0 and num%(17*17)!=0 and den%17!=0,'odd17 valuation without factorization')
# Independent point counts used by the E0(Q) proof.
check([(p,1+sum((y*y-x*x*x+x)%p==0 for x in range(p) for y in range(p))) for p in (3,5)]==[(3,4),(5,8)],'finite field counts')

out={'assertions':count,'squareclass_change_ratio':str(ratio),'new_kernel':str(N),'new_xy':[str(x1),str(y1)],'fiber':[str(aa),str(bb)],'generic_discriminant':str(s.factor(s.discriminant(f(t),t))),'scope':'Generic polynomial certificates plus one137 transport, five trial-division prime proofs, and two independent point certificates. No arbitrary-prime existence or analytic-order theorem.'}
Path('results/symbolic-results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
