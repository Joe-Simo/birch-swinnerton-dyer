"""H4 exact checks, independently expressed from the TypeScript enumeration.

Polynomial identities are generic. Finite-group checks are abstract models, not
asserted elliptic-curve realizations. No analytic rank is estimated numerically.
"""
from __future__ import annotations
import itertools
import json
import math
import platform
import sympy as sp

checks: list[str] = []

def check(condition: bool, label: str) -> None:
    if not condition:
        raise AssertionError(label)
    checks.append(label)

u, v, ell, m, s, t, r, x, y, z = sp.symbols('u v ell m s t r x y z')
b = 2*v
p = u**2 + 16*v**2
f = u*(ell**2-m**2) - 4*b*ell*m
g = b*(ell**2-m**2) + u*ell*m
h = p*(ell**2+m**2)
L = r-u*s**2-4*b*t**2
M = b*s**2-u*t**2
check(sp.expand(h**2-p*(f**2+4*g**2)) == 0, 'generic conic parametrization')
check(sp.expand(h-u*f-4*b*g-2*p*m**2) == 0, 'generic tangent pullback')
check(sp.expand(L*(r+u*s**2+4*b*t**2)-4*M**2-(r**2-p*(s**4+4*t**4))) == 0,
      'norm identity modulo covering equation')
check(sp.det(sp.Matrix([[u, 4*b], [b, -u]])) == -p, 'good-prime unit determinant')
# The source pushout f/m^2 equals 2p*s^2/L on the conic, modulo the projective scaling.
check(sp.cancel(2*p*f/(h-u*f-4*b*g)-f/m**2) == 0, 'pushout and tangent rational-function dictionary')
check(sp.series(sp.sqrt(1+z), z, 0, 4).removeO() == 1+z/2-z**2/8+z**3/16,
      'binomial coefficients for the 2-adic unit calculation')
check(sp.expand((h-u*f-4*b*g).subs({u:7,v:2})-226*m**2) == 0, 'H3 normalization specializes correctly')

# Tate invariants of E_1 after x=X+1,y=Y+X; two independent substitutions.
X,Y=sp.symbols('X Y')
check(sp.expand(((Y+X)**2 - ((X+1)**3-(X+1))) - (Y**2+2*X*Y-X**3-2*X**2-2*X)) == 0,
      'E1 integral coordinate change at2')
a1,a2,a3,a4,a6 = 2,2,0,2,0
b2=a1*a1+4*a2; b4=2*a4+a1*a3; b6=a3*a3+4*a6
b8=a1*a1*a6+4*a2*a6-a1*a3*a4+a2*a3*a3-a4*a4
check((b2,b4,b6,b8)==(12,4,0,-4), 'Tate type-III input invariants')
check(sp.factor(x**3-x)==x*(x-1)*(x+1), 'odd-prime I0-star auxiliary cubic')
check(sp.discriminant(x**3-x,x)==4, 'three auxiliary roots are distinct at every odd prime')

# Direct full triple enumeration, not the residual-square method in verify.ts.
def triple_count(n: int, k: int) -> int:
    return sum(1 for a in range(-math.isqrt(n), math.isqrt(n)+1)
               for b in range(-math.isqrt(n//2), math.isqrt(n//2)+1)
               for c in range(-math.isqrt(n//k), math.isqrt(n//k)+1)
               if a*a+2*b*b+k*c*c==n)

fixtures = [(17,16,4,-4,1,1),(41,32,16,0,5,1),
            (113,32,24,8,7,2),(1153,64,48,16,33,2)]
rows=[]
for prime, A, B, coeff, uu, vv in fixtures:
    a,bcount=triple_count(prime,8),triple_count(prime,32)
    check((a,bcount,bcount-a//2)==(A,B,coeff), f'full triple enumeration p={prime}')
    check(uu*uu+16*vv*vv==prime, f'norm certificate p={prime}')
    # Independent exact two-squares decomposition of the ternary coefficient.
    decomposed = 0
    for xx in range(1,math.isqrt(prime)+1,2):
        n=(prime-xx*xx)//8
        reps=[(aa,bb) for aa in range(-math.isqrt(n),math.isqrt(n)+1)
              for bb in range(-math.isqrt(n),math.isqrt(n)+1) if aa*aa+bb*bb==n]
        decomposed += 2*sum(bb%2==0 for _,bb in reps)-len(reps)
    check(decomposed==coeff, f'two-squares orbit decomposition p={prime}')
    tangent_roots=[rr for rr in range(64) if (rr*rr-prime)%64==0 and (rr+uu)%8==0]
    bits={(((rr-uu)//2)**2-1)//8%2 for rr in tangent_roots}
    expected=((uu*uu-1)//8+vv)%2
    check(bits=={expected} and expected==coeff//4%2, f'local tangent sign p={prime}')
    rows.append({'p':prime,'A':a,'B':bcount,'coefficient':coeff,'u':uu,'v':vv,'first_pairing_bit':expected})

# Enumerate the abstract pairs A=(Z/2^h)^2, C=2A to check the filtration formulas.
abstract=[]
for depth in range(1,5):
    modulus=2**depth
    A=set(itertools.product(range(modulus),repeat=2))
    C={((2*a)%modulus,(2*b)%modulus) for a,b in A}
    def scale(k: int, pt: tuple[int,int]) -> tuple[int,int]:
        return ((k*pt[0])%modulus,(k*pt[1])%modulus)
    sizes=[]
    for index in range(1,2*depth+3):
        if index%2:
            n=(index-1)//2
            image={scale(2**n,pt) for pt in A if scale(2**(n+1),pt)==(0,0)}
        else:
            n=index//2
            image={scale(2**(n-1),pt) for pt in C if scale(2**n,pt)==(0,0)}
        sizes.append(len(image))
    check(sizes==[4 if i<2*depth else 1 for i in range(1,2*depth+3)],f'abstract paired filtration h={depth}')
    check(len(C)==2**(2*(depth-1)),f'abstract isogenous group order h={depth}')
    abstract.append({'h':depth,'filtration_orders':sizes,'A_order':len(A),'B_order':len(C)})
# Algebraic growth identity in the persistent case, for all three unexcluded ranks.
growth=[]
for rank in (0,1,2):
    sizes=[4*2**(rank*level)*2**((2-rank)*level) for level in range(1,7)]
    check(sizes==[4*4**level for level in range(1,7)],f'persistent growth identity rank={rank}')
    growth.append({'rank':rank,'sha_divisible_corank':2-rank,'finite_selmer_orders_levels1to6':sizes})

print(json.dumps({'status':'PASS','python':platform.python_version(),'sympy':sp.__version__,
    'assertions':len(checks),'checks':checks,'fixed_prime_certificates':rows,
    'abstract_finite_group_models':abstract,'abstract_persistent_growth':growth,
    'nonclaims':['No abstract group model is claimed realized by an elliptic curve.',
                 'Higher pairing values in the main result require the cited CM theorems; no higher covering was constructed in H4.']},indent=2))
