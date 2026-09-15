"""Exact arithmetic recheck of the already-known algebraic E41 rank certificate."""
from fractions import Fraction
import json
from pathlib import Path


def squareclass(a: int) -> int:
    if a == 0:
        raise ValueError('Zero is not a multiplicative squareclass.')
    sign = -1 if a < 0 else 1
    a = abs(a)
    d = 2
    while d*d <= a:
        while a % (d*d) == 0:
            a //= d*d
        d += 1
    return sign*a


def binary_rank(rows: list[list[int]]) -> int:
    rows = [row.copy() for row in rows]
    rank = 0
    for j in range(len(rows[0])):
        pivot = next((i for i in range(rank, len(rows)) if rows[i][j]), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        for i in range(len(rows)):
            if i != rank and rows[i][j]:
                rows[i] = [a ^ b for a, b in zip(rows[i], rows[rank])]
        rank += 1
        if rank == len(rows):
            break
    return rank


p = 41
points = [(-9,120),(841,24360)]
assert all(y*y == x*x*x-p*p*x for x,y in points)
assert 121**2 != (-9)**3-p*p*(-9)
triples = [(2,82,41),(-41,41,-1),(-50,32,-9),(800,882,841)]
classes = [list(map(squareclass,t)) for t in triples]
basis = [-1,2,41]
rows = [[int(v<0) if b == -1 else int(abs(v)%b == 0) for v in t for b in basis] for t in classes]
assert binary_rank(rows) == 4
assert all(abs(v) in (1,2,41,82) for t in classes for v in t)
assert pow(2,20,p) == 1 and pow(-2,20,p) == 1
assert Fraction(120*239-119,119*239+120) == 1
out = {'p':41,'points':points,'squareclasses':classes,'Kummer_vectors':rows,
       'Kummer_rank':binary_rank(rows),'Monsky_matrix':[[0,0],[0,0]],
       'rank_lower':2,'rank_upper':2,
       'dependency':'Kummer exactness and Monsky pure-Selmer formula in Zhang 2111.11618v1, Section 2.1; no L-value input',
       'scope':'Known E41 rank-two certificate, not a saturation certificate.'}
Path(__file__).with_name('results').joinpath('algebra-41.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS E41 equations, Kummer independence, residue-symbol inputs and invalid-point control')
