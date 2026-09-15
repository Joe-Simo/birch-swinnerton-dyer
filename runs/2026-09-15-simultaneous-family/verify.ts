/** Finite certificates for CONTRACT.md; the all-parameter proof is in RESEARCH.md. */
let assertions = 0;
function check(ok: boolean, label: string): void {
  assertions += 1;
  if (!ok) throw new Error(label);
}
function abs(n: bigint): bigint { return n < 0n ? -n : n; }
function gcd(a: bigint, b: bigint): bigint {
  let x = abs(a); let y = abs(b);
  while (y !== 0n) { const r = x % y; x = y; y = r; }
  return x;
}
function mod(a: bigint, m: bigint): bigint { return ((a % m) + m) % m; }
function sqrtFloor(n: bigint): bigint {
  if (n < 0n) throw new RangeError("Negative square root.");
  let lo = 0n; let hi = n + 1n;
  while (hi - lo > 1n) {
    const mid = (lo + hi) / 2n;
    if (mid * mid <= n) lo = mid; else hi = mid;
  }
  return lo;
}
function factor(n: bigint): Array<readonly [bigint, number]> {
  if (n < 1n) throw new RangeError("Positive integer required.");
  let rest = n; const out: Array<readonly [bigint, number]> = [];
  for (let p = 2n; p * p <= rest; p += p === 2n ? 1n : 2n) {
    let e = 0;
    while (rest % p === 0n) { rest /= p; e += 1; }
    if (e > 0) out.push([p, e]);
  }
  if (rest > 1n) out.push([rest, 1]);
  return out;
}
function isPrime(p: bigint): boolean {
  return p >= 2n && factor(p).length === 1 && factor(p)[0]?.[1] === 1;
}
function powerMod(a: bigint, e: bigint, p: bigint): bigint {
  let base = mod(a, p); let exponent = e; let result = 1n;
  while (exponent > 0n) {
    if (exponent % 2n === 1n) result = (result * base) % p;
    base = (base * base) % p; exponent /= 2n;
  }
  return result;
}
function legendre(a: bigint, p: bigint): number {
  if (p < 3n || !isPrime(p)) throw new RangeError("Odd prime required.");
  const r = powerMod(a, (p - 1n) / 2n, p);
  if (r === 0n) return 0;
  if (r === 1n) return 1;
  if (r === p - 1n) return -1;
  throw new Error("Euler criterion failed.");
}
function binaryRank(input: readonly (readonly number[])[]): number {
  const rows = input.map(row => {
    let mask = 0n;
    row.forEach((v, j) => {
      if (v !== 0 && v !== 1) throw new RangeError("Nonbinary matrix entry.");
      mask |= BigInt(v) << BigInt(j);
    });
    return mask;
  });
  const basis = new Map<number, bigint>();
  for (let v of rows) {
    while (v !== 0n) {
      const pivot = v.toString(2).length - 1;
      const existing = basis.get(pivot);
      if (existing === undefined) { basis.set(pivot, v); break; }
      v ^= existing;
    }
  }
  return basis.size;
}
function D(a: bigint, b: bigint): bigint { return a ** 8n - 56n * a ** 4n * b ** 4n + 1296n * b ** 8n; }
function factorForm(a: bigint, b: bigint, sign: bigint): bigint {
  return a ** 4n + sign * 4n * a ** 3n * b + 8n * a * a * b * b + sign * 24n * a * b ** 3n + 36n * b ** 4n;
}
function rational(num: bigint, den: bigint): { num: bigint; den: bigint } {
  if (den === 0n) throw new RangeError("Zero denominator.");
  const g = gcd(num, den); const sign = den < 0n ? -1n : 1n;
  return { num: sign * num / g, den: sign * den / g };
}
function certificate(a: bigint, b: bigint) {
  if (a === 0n || b === 0n || gcd(a, b) !== 1n) throw new RangeError("Nonzero coprime parameters required.");
  const d = D(a, b); const fac = factor(d);
  const n = fac.reduce((v, [p, e]) => e % 2 === 1 ? v * p : v, 1n);
  const s = fac.reduce((v, [p, e]) => v * p ** BigInt(Math.floor(e / 2)), 1n);
  const primes = fac.filter(([, e]) => e % 2 === 1).map(([p]) => p);
  check(d === n * s * s, "squarefree normalization");
  check(d > 0n && n > 1n && n % 8n === 1n, "positive nonsquare residue class");
  check(fac.every(([p]) => isPrime(p)), "factor primality");
  check(primes.every(p => p % 8n === 1n), "squarefree prime support");
  check(d === (a ** 4n - 28n * b ** 4n) ** 2n + 512n * b ** 8n, "norm identity");
  const fm = factorForm(a, b, -1n); const fp = factorForm(a, b, 1n);
  const c = (a % 2n === 0n ? 2n : 1n) * (a % 3n === 0n ? 3n : 1n);
  check(fm * fp === d, "factorization identity");
  check(gcd(fm, fp) === c * c, "factor gcd exact");
  const points = ([-1n, 1n] as const).map(eps => {
    const A = a * a - 6n * eps * b * b; const B = 2n * a * b;
    check(A ** 4n + 6n * eps * A * A * B * B + B ** 4n === d, "simultaneous quartic");
    const u = n * s; const v = A * A - eps * B * B;
    const w = A * A + eps * B * B; const z = 2n * A * B;
    check(u * v * w * z !== 0n, "no torsion or denominator degeneracy");
    check(v * v - w * w + eps * z * z === 0n, "first quadric");
    check(u * u - n * w * w - eps * n * z * z === 0n, "second quadric");
    const xn = n * w * w; const yn = n * u * v * w;
    check(yn * yn === xn ** 3n - n * n * xn * z ** 4n, "curve identity after clearing denominators");
    const classLabels = eps === -1n ? [1n, n, n] : [n, 1n, n];
    const roots = eps === -1n ? [u, v, w] : [v, u, w];
    const numerators = [xn - n * z * z, xn + n * z * z, xn];
    check(numerators.every((q, i) => q === (classLabels[i] ?? 0n) * (roots[i] ?? 0n) ** 2n), "three Kummer square factors");
    return { eps, A, B, c: s, covering: [u, v, w, z], x: rational(xn, z * z), y: rational(yn, z ** 3n), classes: classLabels };
  });
  const matrix = primes.map((p, i) => primes.map((q, j) => i === j ? 0 : (1 - legendre(q, p)) / 2));
  matrix.forEach((row, i) => { row[i] = row.reduce((v, x) => v + x, 0) % 2; });
  check(matrix.every(row => row.reduce((v, x) => v + x, 0) % 2 === 0), "Monsky row sum");
  const matrixRank = binaryRank(matrix); const upper = 2 * (primes.length - matrixRank);
  check(upper >= 2, "descent consistency with constructed points");
  return { a, b, D: d, n, squareFactor: s, factors: fac, factorGcd: c * c, matrix, matrixRank, rankLower: 2, rankUpper: upper, points };
}
function rejects(f: () => unknown, name: string): void {
  let failed = false; try { f(); } catch { failed = true; }
  check(failed, name);
}
const parameters = [[1n,1n],[2n,1n],[3n,1n],[4n,1n],[5n,1n],[7n,1n],[1n,2n],[3n,2n]] as const;
const expectedN = [1241n,41n,41n,3281n,356921n,5631641n,330881n,3281n];
const expectedUpper = [2,2,2,2,2,4,4,2];
const rows = parameters.map(([a,b], i) => {
  const row = certificate(a,b);
  check(row.n === expectedN[i], "disclosed squarefree fixture");
  check(row.rankUpper === expectedUpper[i], "disclosed upper-bound fixture");
  return row;
});
const kummer = [[0,1,0,0,1,1,0,0,1],[1,0,1,0,0,1,1,0,0],[0,0,0,0,0,1,0,0,1],[0,0,1,0,0,0,0,0,1]];
check(binaryRank(kummer) === 4, "full Kummer independence");
check(binaryRank(kummer.map(row => [row[0] ?? 0,row[1] ?? 0,row[2] ?? 0,row[5] ?? 0])) === 4, "shared four-column minor");
check(binaryRank([kummer[2] ?? [],kummer[2] ?? []]) === 1, "duplicate class must not look independent");
check(D(-2n,1n) === D(2n,1n), "parameter sign symmetry");
check(D(6n,3n) === 3n ** 8n * D(2n,1n), "homogeneous parameter scaling");
check(rows[1]?.n === rows[2]?.n, "different parameters can give identical twists");
check(rows[1]?.points[0]?.x.num === 18081n && rows[1]?.points[0]?.x.den === 400n, "E41 earlier covering coordinate");
check(sqrtFloor(16n) === 4n && sqrtFloor(17n) === 4n, "exact square-root boundaries");
rejects(() => certificate(0n,1n), "zero numerator excluded");
rejects(() => certificate(1n,0n), "zero denominator excluded");
rejects(() => certificate(6n,3n), "nonprimitive pair excluded");
rejects(() => legendre(2n,9n), "composite Legendre modulus rejected");
rejects(() => sqrtFloor(-1n), "negative root rejected");
rejects(() => binaryRank([[2]]), "nonbinary matrix rejected");
console.log(JSON.stringify({ status: "completed finite certificates; no analytic or universal BSD conclusion", assertions, population: rows.length, rows, kummerRank: 4 }, (_k: string,v: unknown) => typeof v === "bigint" ? v.toString() : v, 2));
