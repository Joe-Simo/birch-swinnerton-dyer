"""Independent exact coefficient/count audit and directed-interval cross-check."""
from __future__ import annotations
import json
import sys
from fractions import Fraction
from math import isqrt
from pathlib import Path
from time import perf_counter
from coefficients import coefficients
from integrate_iv import enclose

ROOT = Path(__file__).resolve().parent


def count_triples(n: int, c: int) -> int:
    return sum(x*x + 2*y*y + c*z*z == n
               for x in range(-isqrt(n), isqrt(n)+1)
               for y in range(-isqrt(n//2), isqrt(n//2)+1)
               for z in range(-isqrt(n//c), isqrt(n//c)+1))


def endpoint(text: str) -> Fraction:
    # The iv output records each directed endpoint as a singleton interval.
    lo, hi = text.strip('[]').split(',')
    assert Fraction(lo.strip()) == Fraction(hi.strip())
    return Fraction(lo.strip())


def verify(p: int) -> dict:
    start = perf_counter()
    data = json.loads((ROOT/'results/exact-rational.json').read_text())
    row = next(r for r in data['results'] if r['p'] == p)
    independent = coefficients(p, row['coefficient_bound'])
    assert [int(v) for v in row['coefficients']] == independent
    A, B = count_triples(p, 8), count_triples(p, 32)
    assert (A, B) == (int(row['A']), int(row['B'])) and A == 2*B
    iv_result = enclose(p)
    assert iv_result['positive']
    L2 = row['L2']; scale = int(L2['scale'])
    lo, hi = Fraction(int(L2['lo_scaled']), scale), Fraction(int(L2['hi_scaled']), scale)
    iv_lo, iv_hi = map(endpoint, iv_result['L2_interval'])
    assert 0 < lo <= iv_lo <= iv_hi <= hi
    assert Fraction(row['L2_decimal_outer'][0]) <= lo <= hi <= Fraction(row['L2_decimal_outer'][1])
    assert len(independent)-1 == 16*p
    # These are seven logically distinct audit groups, not a new curve for each coefficient.
    return {'p': p, 'coefficient_entries_compared': len(independent)-1,
            'coefficient_construction': 'finite-field Legendre counts and Euler recurrence',
            'full_triple_counts': [A, B], 'independent_iv': iv_result,
            'exact_rational_outer_interval': row['L2_decimal_outer'],
            'audit_groups_passed': 7, 'seconds': perf_counter()-start}


if __name__ == '__main__':
    p = int(sys.argv[1])
    result = verify(p)
    (ROOT/f'results/independent-{p}.json').write_text(json.dumps(result, indent=2)+'\n')
    print(p, 'PASS coefficient comparison, central zero, directed integration and enclosure containment', result['seconds'])
