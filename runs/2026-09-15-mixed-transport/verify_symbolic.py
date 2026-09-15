"""H14 exact rational extension arithmetic and independently reconstructed finite certificates."""
from fractions import Fraction as F
from dataclasses import dataclass
@dataclass(frozen=True)
class Q2:
 a:F;b:F=F(0)
 def __add__(self,o):
  o=o if isinstance(o,Q2) else Q2(F(o));return Q2(self.a+o.a,self.b+o.b)
 __radd__=__add__
 def __neg__(self):return Q2(-self.a,-self.b)
 def __sub__(self,o):return self+-o
 def __rsub__(self,o):return -self+o
 def __mul__(self,o):
  o=o if isinstance(o,Q2) else Q2(F(o));return Q2(self.a*o.a+137*self.b*o.b,self.a*o.b+self.b*o.a)
 __rmul__=__mul__
 def inv(self):
  n=self.a*self.a-137*self.b*self.b
  return Q2(self.a/n,-self.b/n)
 def __truediv__(self,o):
  o=o if isinstance(o,Q2) else Q2(F(o));return self*o.inv()
 def __pow__(self,k):
  if k<0:return self.inv()**(-k)
  r=Q2(F(1));s=self
  while k:
   if k&1:r=r*s
   k//=2;s=s*s
  return r

def add(p,q):
 if p is None:return q
 if q is None:return p
 x,y=p;xx,yy=q
 if x==xx and y==-yy:return None
 m=(3*x*x-1)/(2*y) if p==q else (yy-y)/(xx-x)
 nx=m*m-x-xx;return nx,m*(x-nx)-y

def mul(p,k):
 r=None
 while k:
  if k&1:r=add(r,p)
  k//=2;p=add(p,p)
 return r

def odd(t,e,c,m):
 r=Q2(F(0),c)
 u=(r+1+e*t*t)/(2*t*t);v=(r+1+3*e*t*t)/(2*t**3)
 assert v*v==u**3-u
 p=mul((u,v),m)
 if p is None:raise ValueError('infinite elliptic output')
 u,v=p
 tt=(u+e)/v;rr=(2*u-e)*tt**2-1
 assert tt.b==0 and rr.a==0
 return tt.a,rr.b

def phirat(x,y,w):
 a=((x*x+3)*(y*y-3)-8)/(x*x-y*y+6);b=w/(x*x-y*y+6);c=a+3;k=6*c-1
 z=y*(x*x+c)
 f1=4*c*x**3+2*(c*c+k)*x;f2=12*c*x*x+2*(c*c+k)
 h1=f1/(2*z);h2=(f2/2-h1*h1)/(2*z)
 r3=4*c*x-2*h1*h2;r4=c-h2*h2
 nx=x-r3/r4;d=nx-x;nz=z+h1*d+h2*d*d
 ny=nz/(nx*nx+c);nw=b*(nx*nx-ny*ny+6)
 assert nw*nw==(nx**4+6*nx*nx+1)*(ny**4-6*ny*ny+1)
 return nx,ny,nw

def vunit(t,p):
 a,b=t.numerator,t.denominator;v=0
 while a%p==0:a//=p;v+=1
 while b%p==0:b//=p;v-=1
 return v,a*pow(b,-1,p)%p

import json
from pathlib import Path
import sympy as sp

checks=[]
def ck(condition,label):
    if not condition:raise AssertionError(label)
    checks.append(label)

def fg(x,e):return x**4+6*e*x*x+1

def toE(t,e,c):
    r=Q2(F(0),c)
    p=((r+1+e*t*t)/(2*t*t),(r+1+3*e*t*t)/(2*t**3))
    ck(p[1]**2==p[0]**3-p[0],'exact quartic to E0')
    return p

def fromE(p,e):
    if p is None:raise ValueError('Point at infinity outside affine chart')
    u,v=p;t=(u+e)/v;r=(2*u-e)*t*t-1
    ck(t.b==0 and r.a==0,'Galois invariant t and anti-invariant r')
    ck(fg(t.a,e)==137*r.b*r.b,'exact rational twist witness')
    return t.a,r.b

# The rational Q(sqrt(137)) calculation is performed without reducing first.
p=toE(F(1,14),1,F(17,196));q=toE(F(37,14),-1,F(47,196))
q3=mul(q,3)
x,c=fromE(p,1);y,d=fromE(q3,-1)
stages=[(x,y,137*c*d)]
q6=add(q3,q3)
if q6 is None:raise AssertionError('Unexpected torsion')
x,c=fromE(add(p,(q6[0],-q6[1])),1)
stages.append((x,y,137*c*d))
cc=(x*x*y*y+1)/(x*x-y*y+6)
ck(cc!=0 and 6*cc-1!=0 and cc*cc-6*cc+1!=0,'genuine rational fiber is smooth despite C=0 reduction')
stages.append(phirat(*stages[-1]))
for state in stages:
    x,y,w=state;ck(w*w==fg(x,1)*fg(y,-1),'exact surface point')

def residue(v,p=13):return v.numerator*pow(v.denominator,-1,p)%p
rows=[]
for label,state in zip(['Y','YH','YHPhi'],stages):
    x,y,w=state
    rows.append({'label':label,'x':str(x),'y':str(y),'W':str(w),'Fplus':str(fg(x,1)),
                 'residue13':[residue(v) for v in state],
                 'Fplus_v13':vunit(fg(x,1),13)[0],'Fplus_unit13':vunit(fg(x,1),13)[1]})
ck([r['residue13'] for r in rows]==[[1,9,12],[11,9,6],[5,12,9]],'exact rational word reduces to escape')
ck([r['Fplus_unit13'] for r in rows]==[8,2,9],'exact character transition')
x,y,w=stages[-1]
A,B=x.numerator,x.denominator
G=A**4+6*A*A*B*B+B**4
ck(G>0 and G%2==1,'positive odd output parameter')
valuations={ell:vunit(F(G),ell)[0] for ell in [17,2473,3329]}
ck(valuations=={17:3,2473:1,3329:1},'three certified odd valuations')
ck(all(all(p%d for d in range(2,sp.integer_nthroot(p,2)[0]+1)) for p in valuations),'trial-division prime certificates')
ck(G%13==1 or pow(G%13,6,13)==1,'output squareclass is square at 13')
up=F(1,B*B);um=w*B*B/G
ck(fg(x,1)==G*up*up and fg(y,-1)==G*um*um,'both rational quartic witnesses on output parameter')
for t,e,u in [(x,1,up),(y,-1,um)]:
    X=G*(t*t+e)**2/(4*t*t)
    Y=G*G*u*(t**4-1)/(8*t**3)
    ck(Y*Y==X**3-G*G*X,'exact output elliptic point')
    if e==1:
        ck(X-G==G*((t*t-1)/(2*t))**2,'plus Kummer first coordinate')
        ck(X+G==(G*u/(2*t))**2,'plus Kummer second coordinate')
    else:
        ck(X-G==(G*u/(2*t))**2,'minus Kummer first coordinate')
        ck(X+G==G*((t*t+1)/(2*t))**2,'minus Kummer second coordinate')
    ck(t not in [0,1,-1] and Y!=0,'nondegenerate free-point witness')

# Symbolic removal of the apparent bad-reduction singularity.
X,a,b,d,C,Z=sp.symbols('X a b d C Z')
f=a*X**4+b*X**2+d
N=2*f*sp.diff(f,X,2)-sp.diff(f,X)**2
r3=sp.diff(f,X,3)/6-sp.diff(f,X)*N/(8*f*f)
r4=a-N*N/(64*f**3)
Dx=3*a*a*X**8+4*a*b*X**6+6*a*d*X**4-d*d
NX=-X*(a*a*X**8-6*a*d*X**4-4*b*d*X**2-3*d*d)/Dx
ck(sp.cancel(NX-(X-r3/r4))==0,'generic cancelled x-map')
delta=NX-X
ratio=1+sp.diff(f,X)*delta/(2*f)+N*delta**2/(8*f*f)
H=a**4*X**16+4*a**3*b*X**14+28*a**3*d*X**12+28*a*a*b*d*X**10+(6*a*a*d*d+16*a*b*b*d)*X**8+28*a*b*d*d*X**6+28*a*d**3*X**4+4*b*d**3*X**2+d**4
ck(sp.cancel(ratio-H/Dx**2)==0,'generic cancelled z-multiplier')
K=6*C-1
nx=sp.cancel(NX.subs({a:C,b:C*C+K,d:C*K}))
rz=sp.cancel((H/Dx**2).subs({a:C,b:C*C+K,d:C*K}))
ck(sp.cancel(nx.subs(C,0)+1/X**3)==0,'C=0 x specialization')
ck(sp.cancel(rz.subs(C,0)+1/X**4)==0,'C=0 z specialization')

# Independently generate Omega using the two coordinate strips and square roots.
def qf(t,e):return fg(t,e)%13
def square(a):return any(v*v%13==a%13 for v in range(13))
omega=set()
for x in range(13):
    for y in range(13):
        specialx=(x*x-1)%13==0;specialy=(y*y+1)%13==0
        if specialx==specialy:continue
        if square(qf(x,1)) or square(qf(y,-1)):continue
        for w in range(13):
            if w*w%13==qf(x,1)*qf(y,-1)%13:omega.add((x,y,w))
ck(len(omega)==64,'independent Omega population')

def phi_poly(state):
    x,y,w=state
    iv=lambda a:pow(a%13,-1,13)
    gap=(x*x-y*y+6)%13;c=(x*x*y*y+1)*iv(gap)%13;k=(6*c-1)%13
    z=y*(x*x+c)%13
    fp=sp.Poly((X*X+c)*(c*X*X+k),X,modulus=13)
    l=int(fp.diff().eval(x))*iv(2*z)%13
    h=(int(fp.diff().diff().eval(x))*iv(2)-l*l)*iv(2*z)%13
    residual=fp-sp.Poly((z+l*(X-x)+h*(X-x)**2)**2,X,modulus=13)
    linear=residual.exquo(sp.Poly((X-x)**3,X,modulus=13))
    xx=-int(linear.nth(0))*iv(int(linear.nth(1)))%13
    zz=(z+l*(xx-x)+h*(xx-x)**2)%13;yy=zz*iv(xx*xx+c)%13
    return xx,yy,w*(xx*xx-yy*yy+6)*iv(gap)%13

def trip(state,e,side):
    t=state[side]
    den=3*t**8+24*e*t**6+6*t**4-1
    num=t*(t**8-6*t**4-24*e*t*t-3)
    hh=sum(co*t**(2*j) for j,co in enumerate([1,24*e,28,168*e,582,168*e,28,24*e,1]))
    vals=list(state);vals[side]=num*pow(den%13,-1,13)%13;vals[2]=state[2]*hh*pow(den%13,-2,13)%13
    return tuple(vals)

def action(state,name):
    x,y,w=state
    if name=='X':return trip(state,1,0)
    if name=='Y':return trip(state,-1,1)
    if name=='Phi':return phi_poly(state)
    if name=='invertX':return pow(x,-1,13),y,w*pow(x,-2,13)%13
    if name=='invertY':return x,pow(y,-1,13),w*pow(y,-2,13)%13
    if name=='negX':return -x%13,y,w
    if name=='negY':return x,-y%13,w
    if name=='negW':return x,y,-w%13
    raise ValueError(name)
primary=json.loads(Path('results/finite-certificate.json').read_text())
ck({tuple(map(int,r['point'])) for r in primary['omega_transitions']}==omega,'TS population matches independent generation')
comparisons=0
for row in primary['omega_transitions']:
    s=tuple(map(int,row['point']))
    for entry in row['images']:
        out=action(s,entry['name'])
        if out not in omega or out!=tuple(map(int,entry['image'])):raise AssertionError('transition mismatch')
        comparisons+=1
ck(comparisons==512,'all transitions independently reconstructed')
ck([list(map(int,r)) for r in primary['escape']][1:]==[r['residue13'] for r in rows],'TS finite word matches rational output')
raw=sp.Matrix([[0,1,0,1],[1,0,1,1],[0,0,0,1],[0,0,1,0]])
ck(raw.det()==1,'four-class Kummer minor')
Path('results/rational-certificate.json').write_text(json.dumps({'field':'Q(sqrt(137))','word':['Y','H','Phi'],'stages':rows,'G':str(G),'odd_prime_valuations':{str(p):v for p,v in valuations.items()},'normalization':'E_G is isomorphic over Q to E_n for n the positive squarefree kernel of G; n has not been fully factored.'},indent=2)+'\n')
summary={'status':'passed','assertions':len(checks),'checks':checks,'independent_transition_comparisons':comparisons,'symbolic_engine':sp.__version__,'output_numerator_digits':len(str(A)),'G_digits':len(str(G)),'scope':'Exact finite closure, symbolic cancellation, rational escape and rank-lower-bound witnesses; no analytic-order or prescribed-prime result.'}
Path('results/python-summary.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
