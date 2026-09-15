"""Independent exact H6 checks: enumerate (u,v), not (w,z), for modular minima."""
from __future__ import annotations
import json
import math
import platform
from fractions import Fraction
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parent
ASSERTIONS = 0

def check(condition: bool, label: str) -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(label)


def residuals(p: int, vector: tuple[int, int, int, int]) -> tuple[int, int]:
    u, v, w, z = vector
    return v*v-w*w-z*z, u*u-p*w*w+p*z*z


def minimum_uv(p: int, k: int, cap: int) -> tuple[int, tuple[int, int, int, int]] | None:
    modulus = 2**k
    roots: dict[int, int] = {}
    for a in range(cap+1):
        roots.setdefault(a*a % modulus, a)
    inverse_p = pow(p, -1, modulus)
    winner = None
    for u in range(cap+1):
        up = inverse_p*u*u
        for v in range(cap+1):
            twice_w = (v*v+up) % modulus
            if twice_w % 2:
                continue
            # Dividing by 2 modulo an even modulus requires both lifts.
            for w2 in (twice_w//2, twice_w//2+modulus//2):
                w = roots.get(w2)
                z = roots.get((v*v-w2) % modulus)
                if w is None or z is None:
                    continue
                vector = (u, v, w, z)
                if math.gcd(*vector, modulus) != 1:
                    continue
                if any(e % modulus for e in residuals(p, vector)):
                    continue
                candidate = max(vector), vector
                if winner is None or candidate < winner:
                    winner = candidate
    return winner


def direct_minimum(p: int, k: int, cap: int) -> int | None:
    """Deliberately unoptimized independent control at a small registered subdomain."""
    from itertools import product
    candidates = [max(v) for v in product(range(cap+1), repeat=4)
                  if math.gcd(*v, 2**k) == 1
                  and all(e % 2**k == 0 for e in residuals(p, v))]
    return min(candidates) if candidates else None

for p in (17, 41):
    for k in (3, 4):
        found = minimum_uv(p, k, 7)
        check(found is not None and found[0] == direct_minimum(p, k, 7), 'four-variable control agrees')

u,v,w,z,p,a,b = sp.symbols('u v w z p a b')
q1 = v**2-w**2-z**2
q2 = u**2-p*w**2+p*z**2
hessian_pencil = (a*sp.hessian(q1,(u,v,w,z))+b*sp.hessian(q2,(u,v,w,z))).det()
check(sp.expand(hessian_pencil-16*a*b*(a*a-p*p*b*b)) == 0, 'generic Hessian determinant')
poly = p*p*u*u*v*v*w*w-p**3*w*w*(w**4-z**4)
reduced = sp.expand(poly.subs(u*u,p*(w*w-z*z)).subs(v*v,w*w+z*z))
check(reduced == 0, 'generic rational map to E_p')
point = (41,29,21,20)
check(residuals(41,point) == (0,0), 'C41 exact point')
x = Fraction(41*21**2,20**2)
y = Fraction(41*41*29*21,20**3)
check(y*y == x**3-41**2*x, 'rational image is on E41')
check(x == Fraction(18081,400) and y == Fraction(1023729,8000), 'image coordinates exact')
check(math.gcd(*point) == 1, 'positive witness is primitive')
check(42*41**2 == 70602 and 70602 < 2**17, 'positive threshold')
# Exact local square criteria for the negative control; no global solubility inferred.
check(17 % 8 == 1 and (-255) % 8 == 1, 'C17 2-adic square witnesses')
check((6*6-2) % 17 == 0 and (2*6) % 17 != 0, 'C17 17-adic Hensel witness')
check(((1*1-1)//8+1) % 2 == 1, 'inherited H4 first pairing bit at 17')

check(residuals(17,(1,1,0,1)) == (0,18), 'strictness counterexample residual')
check(math.gcd(1,1,0,1,18) == 1, 'strictness counterexample is primitive')
aa,bb,cc = sp.symbols('aa bb cc')
pyth = {u:p*cc,v:aa**2+bb**2,w:aa**2-bb**2,z:2*aa*bb}
fourth = aa**4-6*aa**2*bb**2+bb**4
check(sp.expand(q1.subs(pyth,simultaneous=True)) == 0, 'Pythagorean parametrisation of first conic')
check(sp.expand(q2.subs(pyth,simultaneous=True)-p*(p*cc**2-fourth)) == 0, 'remaining quartic has correct scale')
check(5**4-6*5**2*2**2+2**4 == 41, '41 quartic positive control')

integer_results = json.loads((ROOT/'results/integer-results.json').read_text())
rows = []
for row in integer_results['minima']:
    pp, k, cap = int(row['p']), row['k'], row['cap']
    found = minimum_uv(pp, k, cap)
    if found is None:
        check('height' not in row, 'both enumerators report cap miss')
        rows.append({'p': pp, 'k': k, 'height': None})
        continue
    height, witness = found
    check(height == int(row['height']), 'independent minimum agrees')
    check(all(e % 2**k == 0 for e in residuals(pp,witness)), 'independent vector solves congruences')
    check(math.gcd(*witness,2**k) == 1, 'independent vector is primitive')
    rows.append({'p': pp, 'k': k, 'height': height, 'witness': list(witness)})

# Construct the inverse of three bit by bit, independently of the closed formula.
inverse = 0
sparse = 0
for level in range(1,65):
    modulus = 2**level
    if (3*inverse-1) % modulus:
        inverse += 2**(level-1)
    centered = inverse if inverse <= modulus//2 else inverse-modulus
    if level-1 >= 2 and ((level-1) & (level-2)) == 0:
        sparse += 2**(level-1)
    sparse_centered = sparse % modulus
    if sparse_centered > modulus//2:
        sparse_centered -= modulus
    fixture = integer_results['tower'][level-1]
    check(centered == int(fixture['a']), 'bitwise inverse agrees')
    check(sparse_centered == int(fixture['sparse']), 'bitwise sparse digits agree')
# Strictness is necessary at the sharp boundary; exact normalized deviations vanish.
for level in range(1,11):
    aa = (1-(-2)**level)//3
    deviation = Fraction(aa*aa,4**level)-Fraction(1,9)
    expected = Fraction(1-2*(-2)**level,9*4**level)
    check(deviation == expected, 'sharp boundary exact error')

report = {'assertions': ASSERTIONS, 'python': platform.python_version(), 'sympy': sp.__version__,
          'pencil': str(sp.factor(hessian_pencil)), 'map_residual': str(reduced),
          'E41_image': [str(x),str(y)], 'minima': rows,
          'scope': 'Exact symbolic identities and registered finite domains, not infinite proof verification.'}
(ROOT/'results/symbolic-results.json').write_text(json.dumps(report,indent=2)+'\n')
print(f'PASS {ASSERTIONS} exact Python/SymPy assertions')
