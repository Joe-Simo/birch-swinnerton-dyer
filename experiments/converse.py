"""F2: audit a precise implication of the current CM 2-converse on F1 data.

Not an independent recomputation of F1; theorem and parity bridges are in
RESEARCH.md. Positive finite Selmer dimension is never called positive corank.
"""
from pathlib import Path
import json

root = Path(__file__).resolve().parent.parent
family = json.loads((root / 'results/family.json').read_text())
zero_selmer = [r for r in family['rows'] if r['pureSelmerNullity'] == 0]
failures = [r['n'] for r in zero_selmer if int(r['a']) == 0]
assert not failures, f'CM 2-converse check failed: {failures}'
zero_coefficient = [r for r in family['rows'] if int(r['a']) == 0]
even_zero = [r for r in zero_coefficient if int(r['n']) % 8 in (1, 3)]
odd_zero = [r for r in zero_coefficient if int(r['n']) % 8 in (5, 7)]
assert len(even_zero) + len(odd_zero) == len(zero_coefficient)
assert any(r['n'] == '41' for r in even_zero)
report = {
    'experiment': 'F2', 'status': 'completed', 'new_curve_inputs': 0,
    'zero_finite_selmer_dimension': len(zero_selmer),
    'zero_selmer_inputs': [r['n'] for r in zero_selmer],
    'conflicts_with_CM_2_converse': failures,
    'exact_analytic_order_even_and_at_least_2': [r['n'] for r in even_zero],
    'exact_analytic_order_odd_and_at_least_1': [r['n'] for r in odd_zero],
    'order_41': 'even and >=2; no certified upper bound in this run',
    'scope': 'Known theorem application with separately recorded source dependencies; no universal BSD proof.'
}
(root / 'results/converse.json').write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps({
    'experiment': 'F2', 'zero_Selmer_dimension_inputs': len(zero_selmer),
    'conflicts': len(failures), 'even_order_at_least_2': len(even_zero),
    'odd_order_at_least_1': len(odd_zero)
}))
