/** Exact routines for the explicitly bounded experiment in research/experiment-contract.md. */
export const MAX_BOUND = 200;

export function isqrt(n: bigint): bigint {
  if (n < 0n) throw new RangeError("Square root requires n >= 0.");
  if (n < 2n) return n;
  let lo = 0n;
  let hi = n + 1n;
  while (hi - lo > 1n) {
    const mid = (lo + hi) / 2n;
    if (mid * mid <= n) lo = mid;
    else hi = mid;
  }
  return lo;
}

export function factor(n: bigint): ReadonlyArray<readonly [bigint, number]> {
  if (n < 1n) throw new RangeError("Factorization requires a positive integer.");
  const factors: Array<readonly [bigint, number]> = [];
  let remaining = n;
  for (let p = 2n; p * p <= remaining; p += p === 2n ? 1n : 2n) {
    let exponent = 0;
    while (remaining % p === 0n) {
      remaining /= p;
      exponent += 1;
    }
    if (exponent > 0) factors.push([p, exponent]);
  }
  if (remaining > 1n) factors.push([remaining, 1]);
  return factors;
}

export function isPrime(n: bigint): boolean {
  if (n < 2n) return false;
  for (let d = 2n; d * d <= n; d += 1n) if (n % d === 0n) return false;
  return true;
}

function modPow(a: bigint, exponent: bigint, modulus: bigint): bigint {
  let base = ((a % modulus) + modulus) % modulus;
  let result = 1n;
  let e = exponent;
  while (e > 0n) {
    if (e % 2n === 1n) result = (result * base) % modulus;
    base = (base * base) % modulus;
    e /= 2n;
  }
  return result;
}

export function legendre(a: bigint, p: bigint): bigint {
  if (p === 2n || !isPrime(p)) throw new RangeError("An odd prime is required.");
  const value = modPow(a, (p - 1n) / 2n, p);
  if (value === p - 1n) return -1n;
  if (value === 0n || value === 1n) return value;
  throw new Error("Euler criterion returned an invalid value.");
}

/** Rank over F_2 of nonnegative integer bit masks. */
export function binaryRank(rows: readonly bigint[]): number {
  const basis = new Map<number, bigint>();
  for (const row of rows) {
    if (row < 0n) throw new RangeError("Binary rows must be nonnegative.");
    let v = row;
    while (v !== 0n) {
      let pivot = -1;
      for (let w = v; w !== 0n; w >>= 1n) pivot += 1;
      const existing = basis.get(pivot);
      if (existing === undefined) {
        basis.set(pivot, v);
        break;
      }
      v ^= existing;
    }
  }
  return basis.size;
}

export function monsky(n: bigint): { primes: bigint[]; matrix: number[][]; rank: number; pureDimension: number } {
  if (n < 1n || n % 2n === 0n) throw new RangeError("n must be positive and odd.");
  const factors = factor(n);
  if (factors.some(([, e]) => e !== 1)) throw new RangeError("n must be squarefree.");
  const primes = factors.map(([p]) => p);
  const k = primes.length;
  const a = primes.map((p, i) => primes.map((q, j) =>
    (1n - legendre(i === j ? n / p : q, p)) / 2n));
  const d2 = primes.map((p) => (1n - legendre(2n, p)) / 2n);
  const dm2 = primes.map((p) => (1n - legendre(-2n, p)) / 2n);
  const matrix: number[][] = [];
  const rows: bigint[] = [];
  for (let i = 0; i < 2 * k; i += 1) {
    const row: number[] = [];
    let mask = 0n;
    for (let j = 0; j < 2 * k; j += 1) {
      const r = i % k;
      const c = j % k;
      let value: bigint;
      if ((i < k) === (j < k)) {
        const diagonal = i < k ? d2 : dm2;
        value = ((a[r]?.[c] ?? 0n) + (r === c ? (diagonal[r] ?? 0n) : 0n)) % 2n;
      } else value = r === c ? (d2[r] ?? 0n) : 0n;
      row.push(Number(value)); // value is proved to be exactly 0 or 1.
      mask |= value << BigInt(j);
    }
    matrix.push(row);
    rows.push(mask);
  }
  const rank = binaryRank(rows);
  return { primes, matrix, rank, pureDimension: 2 * k - rank };
}

function validateBound(bound: number): void {
  if (!Number.isSafeInteger(bound) || bound < 0 || bound > MAX_BOUND) {
    throw new RangeError(`Bound must be an integer in [0, ${MAX_BOUND}].`);
  }
}

export function ternaryWitnesses(n: bigint, zCoefficient: 8 | 32): Array<readonly [bigint, bigint, bigint]> {
  if (n < 0n || n > BigInt(MAX_BOUND)) throw new RangeError("Count is outside the registered domain.");
  const out: Array<readonly [bigint, bigint, bigint]> = [];
  const by = isqrt(n / 2n);
  const bz = isqrt(n / BigInt(zCoefficient));
  for (let y = -by; y <= by; y += 1n) {
    for (let z = -bz; z <= bz; z += 1n) {
      const remainder = n - 2n * y * y - BigInt(zCoefficient) * z * z;
      if (remainder < 0n) continue;
      const x = isqrt(remainder);
      if (x * x !== remainder) continue;
      out.push([x, y, z]);
      if (x !== 0n) out.push([-x, y, z]);
    }
  }
  return out;
}

export function tunnellCoefficients(bound: number): bigint[] {
  validateBound(bound);
  const g = Array<bigint>(bound + 1).fill(0n);
  if (bound >= 1) g[1] = 1n;
  for (const step of [8, 16]) {
    for (let exponent = step; exponent <= bound; exponent += step) {
      // Descending order multiplies by (1-q^exponent), once and exactly.
      for (let degree = bound; degree >= exponent; degree -= 1) {
        g[degree] = (g[degree] ?? 0n) - (g[degree - exponent] ?? 0n);
      }
    }
  }
  const out = Array<bigint>(bound + 1).fill(0n);
  const thetaBound = isqrt(BigInt(bound) / 2n);
  for (let j = -thetaBound; j <= thetaBound; j += 1n) {
    const shift = Number(2n * j * j); // 0 <= shift <= bound <= 200.
    for (let degree = shift; degree <= bound; degree += 1) {
      out[degree] = (out[degree] ?? 0n) + (g[degree - shift] ?? 0n);
    }
  }
  return out;
}

export type Point = Readonly<{ x: bigint; y: bigint }>;

export function onCurve(n: bigint, point: Point): boolean {
  return n > 0n && point.y ** 2n === point.x ** 3n - n ** 2n * point.x;
}

export function kummer(n: bigint, point: Point | null): readonly [bigint, bigint, bigint] {
  if (n < 1n) throw new RangeError("A nonsingular curve with n>0 is required.");
  if (point === null) return [1n, 1n, 1n];
  if (!onCurve(n, point)) throw new RangeError("Point is not on the supplied curve.");
  const { x, y } = point;
  if (y !== 0n) return [x - n, x + n, x];
  if (x === n) return [2n, 2n * n, n];
  if (x === -n) return [-2n * n, 2n, -n];
  if (x === 0n) return [-n, n, -1n];
  throw new Error("Unclassified 2-torsion point.");
}

export function squareClass(n: bigint): bigint {
  if (n === 0n) throw new RangeError("Zero has no multiplicative squareclass.");
  let result = n < 0n ? -1n : 1n;
  for (const [p, e] of factor(n < 0n ? -n : n)) if (e % 2 === 1) result *= p;
  return result;
}

export function kummerMask(tuple: readonly bigint[], primeBasis: readonly bigint[]): bigint {
  if (primeBasis.some((p) => !isPrime(p)) || new Set(primeBasis).size !== primeBasis.length) {
    throw new RangeError("Squareclass basis must contain distinct primes.");
  }
  let mask = 0n;
  let index = 0n;
  for (const coordinate of tuple) {
    let value = squareClass(coordinate);
    if (value < 0n) {
      mask |= 1n << index;
      value = -value;
    }
    index += 1n;
    for (const p of primeBasis) {
      if (value % p === 0n) {
        mask |= 1n << index;
        value /= p;
      }
      index += 1n;
    }
    if (value !== 1n) throw new RangeError("Squareclass support omitted by basis.");
  }
  return mask;
}

export function specializationProfile(exponents: readonly number[]): { length: number; fiberDimension: number; excess: number; gradedDimensions: number[] } {
  if (exponents.some((e) => !Number.isSafeInteger(e) || e < 1 || e > MAX_BOUND)) {
    throw new RangeError("Exponents must be positive bounded integers.");
  }
  const length = exponents.reduce((s, e) => s + e, 0);
  const fiberDimension = exponents.length;
  const max = Math.max(0, ...exponents);
  const gradedDimensions = Array.from({ length: max }, (_, j) => exponents.filter((e) => e > j).length);
  return { length, fiberDimension, excess: length - fiberDimension, gradedDimensions };
}

export function jsonExact(value: unknown): string {
  return JSON.stringify(value, (_key: string, item: unknown) => typeof item === "bigint" ? item.toString() : item, 2);
}

/** Uses the explicit prime specialization of Zhang's audited Cassels formula. */
export function casselsPrimeCertificate(p: bigint, mu: bigint, tau: bigint) {
  if (!isPrime(p) || p % 8n !== 1n) throw new RangeError("A prime p=1 mod8 is required.");
  if (2n * mu * mu - tau * tau !== p || (mu - p) % 4n !== 0n) {
    throw new RangeError("Invalid norm/congruence witness for Cassels formula.");
  }
  const sign = legendre(-mu, p);
  if (sign !== 1n && sign !== -1n) throw new Error("Degenerate residue input.");
  const pairingRank = sign === -1n ? 2 : 0;
  // s2=2; no rational points of order 4. Wang (1.1) gives this order.
  const selmer4Order = 2n ** BigInt(6 - pairingRank);
  return { p, mu, tau, sign, pairingRank, selmer2Order: 16n, selmer4Order };
}
