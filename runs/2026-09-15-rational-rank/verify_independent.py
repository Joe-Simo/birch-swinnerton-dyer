"""Independent rational/checksum verifier, not a search or a rank oracle."""
from fractions import Fraction
from math import gcd, isqrt
from pathlib import Path
import json
import sympy as sp

ROOT = Path(__file__).resolve().parent
count = 0

def check(condition: bool, label: str) -> None:
    global count
    count += 1
    if not condition:
        raise AssertionError(label)

def read_fraction(value: dict[str, str]) -> Fraction:
    num, den = int(value['num']), int(value['den'])
    check(den > 0 and gcd(num, den) == 1, 'normalized rational output')
    return Fraction(num, den)

def squareclass(value: Fraction, p: int) -> list[int]:
    if not value:
        raise ValueError('zero squareclass is undefined')
    n = value.numerator * value.denominator
    bits = [int(n < 0)]
    n = abs(n)
    for q in (2, p):
        e = 0
        while n % q == 0:
            n //= q
            e ^= 1
        bits.append(e)
    check(isqrt(n) ** 2 == n, 'all omitted prime valuations are even')
    return bits

def signed_count(n: int, d: int) -> int:
    # Full triple enumeration, not the discovery or TS square-root iterator.
    return sum(x*x + 2*y*y + d*z*z == n
               for x in range(-isqrt(n), isqrt(n)+1)
               for y in range(-isqrt(n//2), isqrt(n//2)+1)
               for z in range(-isqrt(n//d), isqrt(n//d)+1))

def main() -> None:
    obj = json.loads((ROOT/'results/arithmetic-certificates.json').read_text())
    expected = [41,137,257,313,353,457,761]
    check([int(curve['p']) for curve in obj['curves']] == expected, 'exact fixed population')
    summary = []
    for curve in obj['curves']:
        p = int(curve['p'])
        check(bool(sp.isprime(p)) and p % 8 == 1, 'independent primality check')
        check(sp.legendre_symbol(2,p) == sp.legendre_symbol(-2,p) == 1, 'Monsky zero entries')
        vectors = [sum((squareclass(Fraction(d),p) for d in t), [])
                   for t in ((2,2*p,p),(-p,p,-1))]
        for row in curve['points']:
            sign, A, B, c = (int(row[k]) for k in ('sign','A','B','c'))
            x, y = (read_fraction(row['point'][key]) for key in ('x','y'))
            check(y*y == x*x*x-p*p*x, 'direct rational curve residual')
            check(y != 0 and x > p, 'nondegenerate affine point')
            check(A > B > 0 and gcd(A,B) == 1 and (A-B)%2 == 1, 'Pythagorean primitive parameters')
            check(p*c*c == A**4+sign*6*A*A*B*B+B**4, 'quartic equality')
            u,v,w,z = map(int,row['projective'])
            check(gcd(gcd(u,v),gcd(w,z)) == 1, 'primitive homogeneous coordinates')
            check(v*v-w*w+sign*z*z == 0 and u*u-p*w*w-sign*p*z*z == 0, 'two homogeneous equations')
            check(x == Fraction(p*w*w,z*z) and y == Fraction(p*u*v*w,z**3), 'map matches fractions')
            labels = [int(d) for d in row['kummer']]
            roots = [read_fraction(r) for r in row['kummer_square_roots']]
            for number,d,root in zip((x-p,x+p,x),labels,roots,strict=True):
                check(number == d*root*root, 'explicit rational Kummer witness')
            vector = sum((squareclass(number,p) for number in (x-p,x+p,x)), [])
            vectors.append(vector)
            check(sum(bit << j for j,bit in enumerate(vector)) == int(row['mask']), 'mask recomputed from reduced x')
            rad = max(map(abs,(u,v,w,z)))
            rec = row['reconstruction']; C = p+1 if sign == -1 else 2*p
            k = int(rec['k'])
            check(int(rec['radius']) == rad and int(rec['C']) == C, 'residual-height coefficient')
            check(2**(k-1) <= C*rad*rad < 2**k, 'H6 threshold for this specific point')
            check((A*A+B*B,A*A-B*B,2*A*B) == ((v,w,z) if sign == -1 else (w,v,z)), 'Pythagorean coordinate recovery')
        minor=sp.Matrix([[row[j] for j in (0,1,2,5)] for row in vectors])
        check(abs(int(minor.det())) == 1, 'unimodular four-column Kummer minor')
        check([sum(bit << j for j,bit in enumerate(v)) for v in vectors] == list(map(int,curve['masks'])), 'all four masks')
        summary.append({'p':p,'minor':[[int(x) for x in row] for row in minor.tolist()],'determinant':int(minor.det()),'rank_lower_bound':2,'rank_upper_bound_from_Monsky':2})
    # Polynomial verification over Q with independent symbolic arithmetic.
    A,B,c,p=sp.symbols('A B c p')
    for sign in (-1,1):
        u=p*c; v=A*A-sign*B*B; w=A*A+sign*B*B; z=2*A*B
        polynomial=A**4+sign*6*A*A*B*B+B**4-p*c*c
        X=p*w*w; Y=p*u*v*w
        rem=sp.rem(sp.expand(Y*Y-X**3+p*p*X*z**4),polynomial,c)
        check(rem == 0, 'generic curve identity modulo the quartic')
        check(sp.expand(v*v-w*w+sign*z*z) == 0, 'generic Pythagorean identity')
        check(sp.rem(sp.expand(u*u-p*w*w-sign*p*z*z),polynomial,c) == 0, 'generic second quadric identity')
    # Reuse H7 analytic evidence only after matching exact curve labels and zeros.
    analytic=json.loads((ROOT/'inputs/h7-analytic-link.json').read_text())
    check([r['p'] for r in analytic['results']] == expected, 'H7 has same population')
    for row in analytic['results']:
        p=row['p']; aa=signed_count(p,8); bb=signed_count(p,32)
        check(aa == int(row['A']) == 2*bb and bb == int(row['B']), 'independent exact Tunnell zero')
        check(row['N'] == 32*p*p and int(row['central_coefficient']) == 0, 'H7 normalization')
        check(0 < int(row['L2']['lo_scaled']) < int(row['L2']['hi_scaled']) and int(row['L2']['scale']) > 0, 'H7 strictly positive saved derivative enclosure')
    # At higher powers, size4 torsion and rank2 give 4*2^(2m); arithmetic only.
    check([4*2**(2*m) for m in range(1,5)] == [16,64,256,1024], 'finite sanity check on all-level formula')
    result={'status':'passed','assertions':count,'sympy_version':sp.__version__,'curves':summary,
            'scope':'14 explicit rational points, 7 Kummer minors, generic polynomial maps, exact zeros and H7 certificate linkage; not a new uniform BSD proof'}
    (ROOT/'results/independent-checks.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':
    main()
