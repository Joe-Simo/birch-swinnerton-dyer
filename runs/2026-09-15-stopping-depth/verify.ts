/** H4 exact, bounded certificates. Mathematical scope and provenance: CONTRACT.md. */
const LIMIT = 1200;
let assertions = 0;
function check(value: boolean, label: string): void {
  assertions += 1;
  if (!value) throw new Error(label);
}
function rejects(action: () => unknown, label: string): void {
  let failed = false;
  try { action(); } catch { failed = true; }
  check(failed, label);
}
function mod(x: bigint, m: bigint): bigint { return ((x % m) + m) % m; }
function sqrtFloor(n: bigint): bigint {
  if (n < 0n) throw new RangeError('Nonnegative square-root input required.');
  let lo = 0n, hi = n + 1n;
  while (hi - lo > 1n) {
    const mid = (lo + hi) / 2n;
    if (mid * mid <= n) lo = mid; else hi = mid;
  }
  return lo;
}
function isPrime(n: bigint): boolean {
  if (n < 2n) return false;
  for (let d = 2n; d * d <= n; d += 1n) if (n % d === 0n) return false;
  return true;
}
function primeDomain(p: bigint): void {
  if (p > BigInt(LIMIT) || !isPrime(p) || p % 8n !== 1n) {
    throw new RangeError('Registered domain: primes p=1 mod8, 1<p<=1200.');
  }
}
function valuation2(n: bigint): number {
  if (n === 0n) throw new RangeError('Zero has no finite stopping depth.');
  let a = n < 0n ? -n : n, v = 0;
  while (a % 2n === 0n) { a /= 2n; v += 1; }
  return v;
}
function countTernary(p: bigint, k: 8 | 32): bigint {
  primeDomain(p);
  let count = 0n;
  const my = sqrtFloor(p / 2n), mz = sqrtFloor(p / BigInt(k));
  for (let y = -my; y <= my; y += 1n) {
    for (let z = -mz; z <= mz; z += 1n) {
      const rem = p - 2n * y * y - BigInt(k) * z * z;
      if (rem < 0n) continue;
      const x = sqrtFloor(rem);
      if (x * x === rem) count += x === 0n ? 1n : 2n;
    }
  }
  return count;
}
function representations(p: bigint, k: 16 | 32 | 64): Array<readonly [bigint, bigint]> {
  primeDomain(p);
  const out: Array<readonly [bigint, bigint]> = [];
  for (let z = 1n; BigInt(k) * z * z < p; z += 1n) {
    const x = sqrtFloor(p - BigInt(k) * z * z);
    if (x > 0n && x * x + BigInt(k) * z * z === p) out.push([x, z]);
  }
  return out;
}
function coefficientSeries(bound: number): bigint[] {
  if (!Number.isSafeInteger(bound) || bound < 1 || bound > LIMIT) throw new RangeError('Invalid bound.');
  const g = Array<bigint>(bound + 1).fill(0n); g[1] = 1n;
  for (const stride of [8, 16]) {
    for (let exponent = stride; exponent <= bound; exponent += stride) {
      for (let n = bound; n >= exponent; n -= 1) {
        g[n] = (g[n] ?? 0n) - (g[n - exponent] ?? 0n);
      }
    }
  }
  const a = Array<bigint>(bound + 1).fill(0n);
  for (let j = -sqrtFloor(BigInt(bound) / 2n); j <= sqrtFloor(BigInt(bound) / 2n); j += 1n) {
    const shift = Number(2n * j * j); // Proved <=1200, exact Number index only.
    for (let n = shift; n <= bound; n += 1) a[n] = (a[n] ?? 0n) + (g[n - shift] ?? 0n);
  }
  return a;
}
function squareCount(n: bigint): bigint {
  if (n <= 0n) throw new RangeError('Positive norm required.');
  let count = 0n;
  for (let a = -sqrtFloor(n); a <= sqrtFloor(n); a += 1n) {
    const b = sqrtFloor(n - a * a);
    if (a * a + b * b === n) count += b === 0n ? 1n : 2n;
  }
  return count;
}
function isSquare(n: bigint): boolean { return n >= 0n && sqrtFloor(n) ** 2n === n; }
function hilbertWithTwo(unit: bigint): bigint {
  if (unit % 2n === 0n) throw new RangeError('Odd unit required.');
  return mod((unit * unit - 1n) / 8n, 2n);
}

// Focused boundary and invalid-input checks.
check(sqrtFloor(0n) === 0n && sqrtFloor(1n) === 1n && sqrtFloor(15n) === 3n, 'integer square roots');
check(sqrtFloor(10n ** 40n - 1n) === 10n ** 20n - 1n, 'lossless large integer arithmetic');
rejects(() => sqrtFloor(-1n), 'negative input rejected');
rejects(() => primeDomain(9n), 'composite rejected');
rejects(() => primeDomain(7n), 'wrong residue class rejected');
rejects(() => primeDomain(1217n), 'outside registered domain rejected');
rejects(() => coefficientSeries(1201), 'unregistered truncation rejected');
rejects(() => valuation2(0n), 'zero is not assigned a finite stopping depth');
rejects(() => hilbertWithTwo(2n), 'Hilbert odd-unit precondition enforced');
check(valuation2(-16n) === 4 && valuation2(8n) === 3, 'signed valuations');
check(hilbertWithTwo(-1n) === 0n && hilbertWithTwo(5n) === 1n, 'Hilbert fixtures');
const boundaryAssertions = assertions;

// Independent orbit-parity check; auxiliary integers only, not additional elliptic curves.
for (let t = 1n; t <= BigInt(LIMIT) / 8n; t += 1n) {
  const R = squareCount(t);
  check(R % 4n === 0n, `rotation divisibility ${t}`);
  check(mod(R / 4n, 2n) === BigInt(isSquare(t) || (t % 2n === 0n && isSquare(t / 2n))), `conjugation orbit parity ${t}`);
}
const orbitAssertions = assertions - boundaryAssertions;
const coefficients = coefficientSeries(LIMIT);
check(coefficients[1] === 1n && coefficients[3] === 2n, 'q-series normalization');
const fixtures = new Map<bigint, bigint>([[17n, -4n], [41n, 0n], [113n, 8n], [1153n, 16n]]);
const rows = [];
for (let p = 17n; p <= BigInt(LIMIT); p += 8n) {
  if (!isPrime(p)) continue;
  const A = countTernary(p, 8), B = countTernary(p, 32), c = B - A / 2n;
  check(A % 2n === 0n && c % 4n === 0n, `coefficient divisibility ${p}`);
  check(c === coefficients[Number(p)], `counts and q-series agree ${p}`);
  const repr = representations(p, 16), r32 = representations(p, 32), r64 = representations(p, 64);
  check(repr.length === 1 && r32.length <= 1 && r64.length <= 1, `representation multiplicities ${p}`);
  const uv = repr[0]; if (uv === undefined) throw new Error('Missing prime norm representation.');
  const [u, v] = uv;
  const bit = mod((u * u - 1n) / 8n + v, 2n);
  check(mod(c / 4n, 2n) === bit, `coefficient and independent first-pairing formula ${p}`);
  check(mod(c / 4n, 2n) === mod(1n + BigInt(r32.length), 2n), `orbit and norm representation parity ${p}`);
  check((r64.length === 1) === (v % 2n === 0n), `64-form dictionary ${p}`);
  check(p % 16n === 1n ? r32.length === r64.length : r32.length + r64.length === 1, `Kaplansky/Mortenson identity ${p}`);
  // r=-sqrt(p) chosen with r=-u mod8. A root modulo64 determines (r-u)/2 modulo8.
  let root: bigint | undefined;
  for (let r = 0n; r < 64n; r += 1n) {
    if (mod(r * r - p, 64n) === 0n && mod(r + u, 8n) === 0n) { root = r; break; }
  }
  if (root === undefined) throw new Error(`Missing 2-adic root approximation at ${p}.`);
  check(hilbertWithTwo((root - u) / 2n) === bit, `explicit local tangent residue ${p}`);
  const fixture = fixtures.get(p);
  if (fixture !== undefined) check(c === fixture, `authenticated fixture ${p}`);
  const h = c === 0n ? null : valuation2(c) - 1;
  rows.push({ p, A, B, c, u, v, representation32: r32, firstPairingBit: bit,
    finiteStopping: h === null ? null : { h, oddPairingIndex: 2 * h - 1, shaE2CyclicOrders: [2n ** BigInt(h), 2n ** BigInt(h)], shaEprime2CyclicOrders: [2n ** BigInt(h - 1), 2n ** BigInt(h - 1)] } });
}
const firstDeep = rows.find(row => row.c !== 0n && valuation2(row.c) >= 4);
check(firstDeep?.p === 1153n, 'first nonzero coefficient divisible by16 in registered population');
const populationCount = rows.length;
const nonzeroCount = rows.filter(row => row.c !== 0n).length;
const firstBitOneCount = rows.filter(row => row.firstPairingBit === 1n).length;
const depthHistogram: Record<string, number> = {};
for (const row of rows) {
  const key = row.finiteStopping === null ? 'zero coefficient' : `h=${row.finiteStopping.h}`;
  depthHistogram[key] = (depthHistogram[key] ?? 0) + 1;
}
console.log(JSON.stringify({ status: 'PASS', domain: 'all primes p=1 mod8 with 1<p<=1200', limit: LIMIT,
  boundaryAssertions, orbitAssertions, assertions, populationCount, nonzeroCount, firstBitOneCount,
  depthHistogram, firstDeep,
  provenance: { computed: 'signed counts, exact q-series, norm representations, first-pairing scalar formula',
    higherDepth: 'THEOREM-DERIVED via cited CM rank-zero BSD and the written filtration lemma; NOT an explicit higher covering or local pairing computation',
    zero: 'null finiteStopping means zero coefficient; it does not certify rational rank2 or analytic order2' }, rows },
  (_key: string, value: unknown) => typeof value === 'bigint' ? value.toString() : value, 2));
