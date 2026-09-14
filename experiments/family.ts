// Exact bounded BSD auxiliary audit. Scope and interpretations: CONTRACT.md.
// No numerical L-values and no use of BSD to infer either rank.
type Matrix = readonly (readonly number[])[];

function at<T>(xs: readonly T[], i: number): T {
  const value = xs[i];
  if (value === undefined) throw new RangeError(`Missing index ${i}`);
  return value;
}
function check(condition: boolean, message: string): asserts condition {
  if (!condition) throw new Error(message);
}
function rejects(action: () => unknown): boolean {
  try { action(); return false; } catch { return true; }
}
function isqrt(n: bigint): bigint {
  if (n < 0n) throw new RangeError("Negative square root");
  if (n < 2n) return n;
  let x = n;
  let y = (x + 1n) / 2n;
  while (y < x) { x = y; y = (x + n / x) / 2n; }
  return x;
}
function mod(a: bigint, p: bigint): bigint { return ((a % p) + p) % p; }
function powmod(a: bigint, e: bigint, p: bigint): bigint {
  if (p <= 1n || e < 0n) throw new RangeError("Invalid modular power");
  let b = mod(a, p);
  let k = e;
  let result = 1n;
  while (k > 0n) {
    if (k % 2n !== 0n) result = (result * b) % p;
    b = (b * b) % p; k /= 2n;
  }
  return result;
}
function factorSquarefree(n: bigint): bigint[] | null {
  if (n < 1n) throw new RangeError("Expected positive input");
  const factors: bigint[] = [];
  let remaining = n;
  for (let p = 2n; p * p <= remaining; p++) {
    if (remaining % p === 0n) {
      factors.push(p); remaining /= p;
      if (remaining % p === 0n) return null;
    }
  }
  if (remaining > 1n) factors.push(remaining);
  return factors;
}
function additiveLegendre(a: bigint, p: bigint): number {
  if (p < 3n || p % 2n === 0n || mod(a, p) === 0n)
    throw new RangeError("Nonzero symbol at an odd prime required");
  const euler = powmod(a, (p - 1n) / 2n, p);
  check(euler === 1n || euler === p - 1n, "Input is not a prime");
  // Independent residue enumeration: all p supplied by exact trial division.
  let isResidue = false;
  for (let x = 1n; x < p; x++) if ((x * x) % p === mod(a, p)) isResidue = true;
  check(isResidue === (euler === 1n), "Legendre implementations disagree");
  return euler === 1n ? 0 : 1;
}
function counts(n: bigint, zCoefficient: bigint): bigint {
  check(n >= 0n && zCoefficient > 0n, "Invalid ternary count");
  let total = 0n;
  for (let z = 0n; zCoefficient * z * z <= n; z++) {
    for (let x = 0n; 2n * x * x + zCoefficient * z * z <= n; x++) {
      const remainder = n - 2n * x * x - zCoefficient * z * z;
      const y = isqrt(remainder);
      if (y * y === remainder)
        total += (x === 0n ? 1n : 2n) * (y === 0n ? 1n : 2n) * (z === 0n ? 1n : 2n);
    }
  }
  return total;
}
function signedTripleChecker(n: bigint, zCoefficient: bigint): bigint {
  let total = 0n;
  // Deliberately looser bounds; no shared square-root implementation.
  let bound = 0n;
  while (bound * bound <= n) bound++;
  for (let x = -bound; x <= bound; x++)
    for (let y = -bound; y <= bound; y++)
      for (let z = -bound; z <= bound; z++)
        if (2n * x * x + y * y + zCoefficient * z * z === n) total++;
  return total;
}
function coefficients(limit: number): bigint[] {
  check(Number.isSafeInteger(limit) && limit >= 1 && limit <= 511, "Declared degree bound exceeded");
  const product = Array<bigint>(limit + 1).fill(0n);
  product[1] = 1n;
  for (const step of [8, 16])
    for (let exponent = step; exponent <= limit; exponent += step)
      for (let j = limit; j >= exponent; j--)
        product[j] = at(product, j) - at(product, j - exponent);
  const answer = product.slice();
  for (let z = 1; 2 * z * z <= limit; z++) {
    const shift = 2 * z * z;
    for (let j = shift; j <= limit; j++)
      answer[j] = at(answer, j) + 2n * at(product, j - shift);
  }
  return answer;
}
function monsky(factors: readonly bigint[]): Matrix {
  const m = factors.length;
  const f = Array.from({ length: m }, () => Array<number>(m).fill(0));
  const d2 = factors.map((p) => additiveLegendre(2n, p));
  const dm2 = factors.map((p) => additiveLegendre(-2n, p));
  for (let i = 0; i < m; i++) {
    let sum = 0;
    for (let j = 0; j < m; j++) if (i !== j) {
      const entry = additiveLegendre(at(factors, j), at(factors, i));
      at(f, i)[j] = entry; sum ^= entry;
    }
    at(f, i)[i] = sum;
  }
  return Array.from({ length: 2 * m }, (_, i) =>
    Array.from({ length: 2 * m }, (_, j) => {
      const a = i % m, b = j % m;
      if (i < m && j < m) return a === b ? at(d2, a) : 0;
      if (i >= m && j >= m) return a === b ? at(d2, a) : 0;
      const diagonal = i < m ? d2 : dm2;
      return at(at(f, a), b) ^ (a === b ? at(diagonal, a) : 0);
    }));
}
function rankF2(matrix: Matrix): number {
  const n = matrix.length;
  check(matrix.every((r) => r.length === n && r.every((v) => v === 0 || v === 1)), "Expected square F2 matrix");
  const rows = matrix.map((r) => r.reduce((mask, entry, j) => mask | (BigInt(entry) << BigInt(j)), 0n));
  let rank = 0;
  for (let j = 0; j < n; j++) {
    const bit = 1n << BigInt(j);
    let pivot = rank;
    while (pivot < n && (at(rows, pivot) & bit) === 0n) pivot++;
    if (pivot === n) continue;
    const saved = at(rows, pivot);
    rows[pivot] = at(rows, rank); rows[rank] = saved;
    for (let i = rank + 1; i < n; i++)
      if ((at(rows, i) & bit) !== 0n) rows[i] = at(rows, i) ^ saved;
    rank++;
  }
  return rank;
}
function kernelSizeChecker(matrix: Matrix): bigint {
  const n = matrix.length;
  check(n <= 8, "Exhaustive checker resource bound exceeded");
  let count = 0n;
  for (let mask = 0n; mask < (1n << BigInt(n)); mask++) {
    const zero = matrix.every((row) => {
      let sum = 0n;
      for (let j = 0; j < n; j++) sum += BigInt(at(row, j)) * ((mask >> BigInt(j)) & 1n);
      return sum % 2n === 0n;
    });
    if (zero) count++;
  }
  return count;
}
function squareclass(n: bigint): bigint {
  if (n === 0n) throw new RangeError("Zero has no multiplicative square class");
  let remaining = n < 0n ? -n : n;
  let result = n < 0n ? -1n : 1n;
  for (let p = 2n; p * p <= remaining; p++) {
    let odd = false;
    while (remaining % p === 0n) { odd = !odd; remaining /= p; }
    if (odd) result *= p;
  }
  return result * remaining;
}
function finiteFieldCount(n: bigint, p: bigint): bigint {
  check(mod(64n * n ** 6n, p) !== 0n, "Bad reduction prime");
  let result = 1n;
  for (let x = 0n; x < p; x++)
    for (let y = 0n; y < p; y++)
      if (mod(y * y - x ** 3n + n * n * x, p) === 0n) result++;
  return result;
}
function auditPoint(n: bigint, x: bigint, y: bigint) {
  check(y * y === x ** 3n - n * n * x, "Point not on curve");
  return { x, y, kummer: [squareclass(x), squareclass(x - n), squareclass(x + n)] };
}
function preflight(): void {
  check(isqrt(0n) === 0n && isqrt(2n) === 1n && isqrt(49n) === 7n, "Square-root fixtures");
  const huge = 10n ** 40n;
  check(isqrt(huge * huge + huge) === huge, "Large exact square root");
  check(rejects(() => isqrt(-1n)), "Negative-root rejection");
  check(factorSquarefree(9n) === null && factorSquarefree(45n) === null, "Squarefree rejection");
  check(rejects(() => factorSquarefree(0n)), "Domain rejection");
  check(counts(1n, 32n) === 2n && counts(1n, 8n) === 2n && at(coefficients(1), 1) === 1n, "Authenticated E1 baseline");
  check(rankF2([]) === 0 && kernelSizeChecker([]) === 1n, "Empty matrix");
  for (const [p, expected] of [[3n, 0], [5n, 1], [7n, 1], [17n, 2]] as const) {
    const matrix = monsky([p]);
    check(matrix.length - rankF2(matrix) === expected, `Prime matrix fixture ${p}`);
  }
  check(rejects(() => rankF2([[2]])), "Malformed matrix rejection");
  check(rejects(() => auditPoint(41n, -9n, 121n)), "Off-curve rejection");
  for (const n of [0n, 1n, 3n, 17n, 41n])
    for (const c of [8n, 32n]) check(counts(n, c) === signedTripleChecker(n, c), "Signed baseline count disagreement");
}

preflight();
const limit = 511;
const series = coefficients(limit);
const rows = [];
for (let index = 1; index <= limit; index += 2) {
  const n = BigInt(index);
  const factors = factorSquarefree(n);
  if (factors === null) continue;
  const a32 = counts(n, 32n), b8 = counts(n, 8n), a = at(series, index);
  check(2n * a32 - b8 === 2n * a, `Ternary/product disagreement at ${n}`);
  check(a32 === signedTripleChecker(n, 32n) && b8 === signedTripleChecker(n, 8n), `Signed enumeration disagreement at ${n}`);
  const matrix = monsky(factors);
  const nullity = matrix.length - rankF2(matrix);
  const kernelSize = kernelSizeChecker(matrix);
  check(kernelSize === (1n << BigInt(nullity)), `F2 checker disagreement at ${n}`);
  rows.push({ n, factors, A32: a32, B8: b8, a, matrix, pureSelmerNullity: nullity, kernelSize,
    analyticEvidence: a === 0n ? "L(1)=0; exact order not certified" : "L(1)>0 by Tunnell Theorem 3",
    algebraicEvidence: a === 0n ? "Matrix gives rank upper bound only" : "Rank 0 by Tunnell's stated Coates-Wiles implication" });
}
const points41 = [auditPoint(41n, -9n, 120n), auditPoint(41n, 841n, 24360n)];
const torsionKummer = [[1n, 1n, 1n], [-1n, -41n, 41n], [41n, 2n, 82n], [-41n, -82n, 2n]];
const pointClasses = points41.map((p) => p.kummer);
const productClass = at(pointClasses, 0).map((v, i) => squareclass(v * at(at(pointClasses, 1), i)));
for (const image of [...pointClasses, productClass])
  check(!torsionKummer.some((t) => t.every((v, i) => v === at(image, i))), "Point independence certificate failed");
const nonzeroWithGap = rows.filter((r) => r.a !== 0n && r.pureSelmerNullity > 0);
const report = {
  experiment: "F1", status: "completed", bound: String(limit), preflight: "passed before scan",
  numberOfOddSquarefreeInputs: rows.length,
  coefficientZero: rows.filter((r) => r.a === 0n).length,
  coefficientNonzero: rows.filter((r) => r.a !== 0n).length,
  nonzeroCoefficientPositiveSelmerNullity: nonzeroWithGap.map((r) => ({ n: r.n, a: r.a, pureSelmerNullity: r.pureSelmerNullity })),
  pointFollowup41: { points: points41, productClass, torsionKummer,
    finiteFieldOrders: [3n, 5n].map((p) => ({ p, order: finiteFieldCount(41n, p) })),
    interpretation: "Independence requires the Kummer homomorphism and torsion argument in RESEARCH.md, not just on-curve checks." },
  rows,
};
console.log(JSON.stringify(report, (_key: string, value: unknown) => typeof value === "bigint" ? value.toString() : value, 2));
