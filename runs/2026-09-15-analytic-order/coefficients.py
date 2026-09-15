"""Independent exact Euler coefficients; no floating-point or analytic-rank input."""
from __future__ import annotations
from math import isqrt


def coefficients(p: int, bound: int) -> list[int]:
    if p < 3 or p % 8 != 1 or any(p % d == 0 for d in range(2, isqrt(p) + 1)):
        raise ValueError('A prime congruent to 1 modulo 8 is required.')
    if bound < 1:
        raise ValueError('The coefficient bound must be positive.')
    a = [0] * (bound + 1)
    a[1] = 1
    spf = list(range(bound + 1))
    for ell in range(2, bound + 1):
        if spf[ell] != ell:
            continue
        for m in range(ell, bound + 1, ell):
            if spf[m] == m:
                spf[m] = ell
        trace = 0
        if ell not in (2, p):
            for x in range(ell):
                value = pow((x*x*x - p*p*x) % ell, (ell-1)//2, ell)
                trace -= 0 if value == 0 else 1 if value == 1 else -1
        a[ell] = trace
    for n in range(2, bound + 1):
        ell = spf[n]
        if n == ell:
            continue
        m = n // ell
        a[n] = a[ell] * a[m]
        if m % ell == 0 and ell not in (2, p):
            a[n] -= ell * a[m//ell]
    return a
