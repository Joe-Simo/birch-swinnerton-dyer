"""Cross-check the preserved Wolfram output against local exact results."""
from pathlib import Path
import json

root = Path(__file__).resolve().parent.parent
w = json.loads((root / 'results/wolfram-output.json').read_text())
f = json.loads((root / 'results/family.json').read_text())
a = json.loads((root / 'results/specialization.json').read_text())
for row in w['coefficients']:
    local = next(v for v in f['rows'] if v['n'] == str(row['n']))
    for field in ('A32', 'B8', 'a'):
        assert int(local[field]) == row[field], (row, field)
labels = ('double-zero', 'extension-with-unit-off-diagonal',
          'Schur-complement-delayed-order', 'paired-even-skew')
for row, label in zip(w['matrices'], labels, strict=True):
    local = next(v for v in a['explicitFixtures'] if v['label'] == label)
    assert local['nullity'] == row['specializedNullity']
    assert local['jetKernelDimensions'] == row['jetNullities']
for row, point in zip(w['points41'], f['pointFollowup41']['points'], strict=True):
    assert int(point['x']) == row['x'] and int(point['y']) == row['y']
    assert row['residual'] == 0
assert len(f['rows']) == 209
assert f['coefficientNonzero'] == 83 and f['coefficientZero'] == 126
assert len(f['nonzeroCoefficientPositiveSelmerNullity']) == 25
print('PASS: saved Wolfram values agree with local exact outputs; F1 coverage 209.')
