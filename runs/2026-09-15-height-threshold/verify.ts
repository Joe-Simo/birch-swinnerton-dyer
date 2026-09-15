/** Exact finite certificates for H6. Infinite assertions are proved in RESEARCH.md. */
type Vector = readonly [bigint, bigint, bigint, bigint];
let assertions = 0;
function check(ok: boolean, label: string): void {
  assertions += 1;
  if (!ok) throw new Error(label);
}
function rejects(action: () => unknown, label: string): void {
  let failed = false;
  try { action(); } catch { failed = true; }
  check(failed, label);
}
function abs(x: bigint): bigint { return x < 0n ? -x : x; }
function mod(x: bigint, m: bigint): bigint { return ((x % m) + m) % m; }
function gcd(a: bigint, b: bigint): bigint {
  let x = abs(a), y = abs(b);
  while (y !== 0n) { const r = x % y; x = y; y = r; }
  return x;
}
function norm(v: Vector): bigint {
  return v.reduce((best, x) => abs(x) > best ? abs(x) : best, 0n);
}
function residuals(p: bigint, v: Vector): readonly [bigint, bigint] {
  const [u, vv, w, z] = v;
  return [vv * vv - w * w - z * z, u * u - p * w * w + p * z * z];
}
function valid(p: bigint, v: Vector, m: bigint): boolean {
  if (m < 2n || p < 3n || p % 2n !== 1n) return false;
  const primitive = v.reduce((g, x) => gcd(g, x), m) === 1n;
  return primitive && residuals(p, v).every((r) => mod(r, m) === 0n);
}
function center(x: bigint, m: bigint): bigint {
  if (m < 2n) throw new RangeError('Modulus must be at least two');
  const r = mod(x, m);
  return 2n * r <= m ? r : r - m;
}
function minimum(p: bigint, k: number, cap: number) {
  if (!Number.isInteger(k) || k < 1 || k > 17 || !Number.isInteger(cap) || cap < 1 || cap > 512) {
    throw new RangeError('Outside the registered finite domain');
  }
  if (p !== 17n && p !== 41n) throw new RangeError('Only the registered controls are allowed');
  const m = 1n << BigInt(k);
  // For each square residue, its least nonnegative root within the cap.
  const roots = new Map<bigint, bigint>();
  const squares = Array.from({ length: cap + 1 }, (_, i) => BigInt(i) ** 2n);
  for (let i = 0; i <= cap; i += 1) {
    const r = mod(squares[i] ?? 0n, m);
    if (!roots.has(r)) roots.set(r, BigInt(i));
  }
  let winner: Vector | undefined;
  let height: bigint | undefined;
  for (let wi = 0; wi <= cap; wi += 1) {
    for (let zi = 0; zi <= cap; zi += 1) {
      const w = BigInt(wi), z = BigInt(zi);
      const w2 = squares[wi] ?? 0n, z2 = squares[zi] ?? 0n;
      const u = roots.get(mod(p * (w2 - z2), m));
      const vv = roots.get(mod(w2 + z2, m));
      if (u === undefined || vv === undefined) continue;
      const candidate: Vector = [u, vv, w, z];
      if (!valid(p, candidate, m)) continue;
      const h = norm(candidate);
      if (height === undefined || h < height) { winner = candidate; height = h; }
    }
  }
  if (winner === undefined || height === undefined) {
    return { p, k, modulus: m, cap, status: 'no solution within cap; no insolubility conclusion' };
  }
  const errors = residuals(p, winner);
  const threshold = (p + 1n) * height * height < m;
  check(valid(p, winner, m), `primitive congruence witness p=${p}, k=${k}`);
  check(height <= BigInt(cap), 'reported witness is within cap');
  check(errors.every((r) => abs(r) <= (p + 1n) * height * height), 'quadratic residual bound');
  check(!threshold || errors.every((r) => r === 0n), 'strict threshold forces both residuals zero');
  return { p, k, modulus: m, cap, status: 'absolute minimum certified by bounded exhaustive search',
    height, witness: winner, residuals: errors, strictThreshold: threshold };
}

check(residuals(41n, [41n, 29n, 21n, 20n]).every((r) => r === 0n), 'explicit C41 point');
check(!valid(17n, [0n, 0n, 0n, 0n], 32n), 'zero vector is not a projective point');
check(!valid(17n, [8n, 8n, 8n, 8n], 16n), 'nonprimitive modular zero rejected');
check(!valid(41n, [41n, 29n, 21n, 21n], 131072n), 'perturbed positive witness rejected');
rejects(() => minimum(19n, 4, 8), 'unregistered curve rejected');
rejects(() => minimum(17n, 18, 8), 'unregistered level rejected');
rejects(() => center(1n, 0n), 'zero modulus rejected');

// Post-run adversarial boundary: equality is insufficient, even on the negative control.
check(valid(17n, [1n, 1n, 0n, 1n], 18n), 'equality-threshold congruence witness');
check(residuals(17n, [1n, 1n, 0n, 1n])[1] === 18n, 'equality threshold does not force a zero');
check(41n**2n <= 41n*18081n && 18081n <= 41n*41n**2n, 'explicit logarithmic height comparison in multiplicative form');

const tower: Array<{ m: number; a: bigint; sparse: bigint }> = [];
let previousA = 0n, previousSparse = 0n;
for (let m = 1; m <= 64; m += 1) {
  const modulus = 1n << BigInt(m);
  const a = (1n - (-2n) ** BigInt(m)) / 3n;
  let sparse = 0n;
  for (let exponent = 2; exponent < m; exponent *= 2) sparse += 1n << BigInt(exponent);
  sparse = center(sparse, modulus);
  check(mod(3n * a - 1n, modulus) === 0n, '1/3 residue identity');
  check(abs(a) <= modulus / 2n, '1/3 has a centered representative');
  check(3n * a === 1n - (-2n) ** BigInt(m), 'exact inverse formula');
  if (m > 1) {
    check(mod(a - previousA, modulus / 2n) === 0n, 'inverse residues are compatible');
    check(mod(sparse - previousSparse, modulus / 2n) === 0n, 'sparse residues are compatible');
    check(abs(a) + abs(previousA) === modulus / 2n, 'sharp adjacent-height triangle equality');
  }
  if (m <= 10) {
    const b = modulus / 2n;
    const available: bigint[] = [];
    for (let t = -b; t <= b; t += 1n) if (mod(3n * t - 1n, modulus) === 0n) available.push(t);
    check(available.every((t) => t * t >= a * a), 'exhaustive centered inverse minimality');
  }
  tower.push({ m, a, sparse }); previousA = a; previousSparse = sparse;
}
// Single-level low height is not a uniform all-level bound: a late nonintegral digit.
for (let m = 1; m <= 12; m += 1) {
  check(mod((1n << 12n) * tower[m - 1]!.a, 1n << BigInt(m)) === 0n, 'finite prefix can vanish');
}

const minima = [];
for (let k = 1; k <= 16; k += 1) minima.push(minimum(17n, k, 512));
for (let k = 1; k <= 17; k += 1) minima.push(minimum(41n, k, 41));
console.log(JSON.stringify({ assertions, tower, minima,
  scope: 'Exact finite certificates only; no numerical canonical heights or BSD solution.' },
  (_key: string, value: unknown) => typeof value === 'bigint' ? value.toString() : value, 2));
