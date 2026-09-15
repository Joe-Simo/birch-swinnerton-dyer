import { witnesses } from "./witnesses.js";

type Witness = Readonly<{ p: bigint; sign: -1 | 1; A: bigint; B: bigint; c: bigint }>;
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
function gcd(a: bigint, b: bigint): bigint {
  let x = a < 0n ? -a : a;
  let y = b < 0n ? -b : b;
  while (y !== 0n) [x, y] = [y, x % y];
  return x;
}
function isPrime(p: bigint): boolean {
  if (p < 2n) return false;
  for (let d = 2n; d * d <= p; d += 1n) if (p % d === 0n) return false;
  return true;
}
function modPow(a: bigint, exponent: bigint, p: bigint): bigint {
  let b = ((a % p) + p) % p;
  let e = exponent;
  let value = 1n;
  while (e > 0n) {
    if (e % 2n === 1n) value = (value * b) % p;
    b = (b * b) % p;
    e /= 2n;
  }
  return value;
}
function fraction(num: bigint, den: bigint): Readonly<{ num: bigint; den: bigint }> {
  if (den === 0n) throw new RangeError("Zero denominator");
  const g = gcd(num, den);
  const s = den > 0n ? 1n : -1n;
  return { num: s * num / g, den: s * den / g };
}
function squareClassBits(n: bigint, p: bigint): bigint {
  if (n === 0n) throw new RangeError("Zero squareclass");
  let a = n < 0n ? -n : n;
  let bits = n < 0n ? 1n : 0n;
  for (const [q, bit] of [[2n, 2n], [p, 4n]] as const) {
    while (a % q === 0n) { a /= q; bits ^= bit; }
  }
  if (a !== 1n) throw new RangeError("Not a supported squarefree label");
  return bits;
}
function tupleMask(tuple: readonly bigint[], p: bigint): bigint {
  return tuple.reduce((mask, x, i) => mask | (squareClassBits(x, p) << BigInt(3 * i)), 0n);
}
function rankF2(rows: readonly bigint[]): number {
  const pivots = new Map<number, bigint>();
  for (const row of rows) {
    if (row < 0n) throw new RangeError("Negative bit vector");
    let v = row;
    while (v !== 0n) {
      let i = -1;
      for (let t = v; t !== 0n; t >>= 1n) i += 1;
      const pivot = pivots.get(i);
      if (pivot === undefined) { pivots.set(i, v); break; }
      v ^= pivot;
    }
  }
  return pivots.size;
}
function certificate(witness: Witness) {
  const { p, sign, A, B, c } = witness;
  if (!isPrime(p) || p % 8n !== 1n) throw new RangeError("Require prime p=1 mod8");
  if (A <= B || B <= 0n || c <= 0n || gcd(A, B) !== 1n || (A - B) % 2n === 0n) {
    throw new RangeError("Require coprime opposite-parity A>B>0 and c>0");
  }
  const quartic = A ** 4n + BigInt(sign) * 6n * A * A * B * B + B ** 4n;
  if (quartic !== p * c * c) throw new Error("False quartic witness");
  const u = p * c;
  const z = 2n * A * B;
  const v = A * A - BigInt(sign) * B * B;
  const w = A * A + BigInt(sign) * B * B;
  check(gcd(gcd(u, v), gcd(w, z)) === 1n, "Primitive projective point");
  check(v * v - w * w + BigInt(sign) * z * z === 0n, "First quadric");
  check(u * u - p * w * w - BigInt(sign) * p * z * z === 0n, "Second quadric");
  const X = p * w * w;
  const Y = p * u * v * w;
  check(Y * Y === X ** 3n - p * p * X * z ** 4n, "Exact elliptic-curve equation");
  const classes = sign === -1 ? [1n, p, p] : [p, 1n, p];
  const roots = sign === -1 ? [u, v, w] : [v, u, w];
  const numerators = [X - p * z * z, X + p * z * z, X];
  for (let i = 0; i < 3; i += 1) {
    const d = classes[i], r = roots[i], a = numerators[i];
    if (d === undefined || r === undefined || a === undefined) throw new Error("Coordinate mismatch");
    check(a === d * r * r && r !== 0n, "Explicit Kummer square factor");
  }
  check(modPow(2n, (p - 1n) / 2n, p) === 1n, "Legendre(2,p)=1");
  check(modPow(-2n, (p - 1n) / 2n, p) === 1n, "Legendre(-2,p)=1");
  const radius = [u, v, w, z].reduce((a, b) => a > b ? a : b);
  const C = sign === -1 ? p + 1n : 2n * p;
  const threshold = C * radius * radius;
  let k = 0;
  let modulus = 1n;
  while (modulus <= threshold) { modulus *= 2n; k += 1; }
  check(threshold < modulus && modulus / 2n <= threshold, "Minimal power for this witness threshold");
  check([u, v, w, z].some(x => x % 2n === 1n), "Primitive at modulus 2^k");
  return {
    ...witness, point: { x: fraction(X, z * z), y: fraction(Y, z ** 3n) },
    projective: [u, v, w, z], kummer: classes,
    kummer_square_roots: roots.map(r => fraction(r, z)), mask: tupleMask(classes, p),
    reconstruction: { radius, C, threshold, k, modulus },
    residuals: [0n, 0n],
  };
}
const points = witnesses.map(certificate);
const expected = [41n, 137n, 257n, 313n, 353n, 457n, 761n];
const curves = expected.map(p => {
  const pair = points.filter(point => point.p === p);
  check(pair.length === 2 && pair.some(w => w.sign === -1) && pair.some(w => w.sign === 1), "One point on each fixed covering");
  const torsion = [[2n, 2n * p, p], [-p, p, -1n]];
  const masks = [...torsion.map(t => tupleMask(t, p)), ...pair.map(c => c.mask)];
  check(rankF2(masks) === 4, "Kummer rank including torsion is four");
  const first = pair[0], tplus = masks[0], tzero = masks[1];
  if (first === undefined || tplus === undefined || tzero === undefined) throw new Error("Missing certificate row");
  check(rankF2([tplus, tzero, first.mask, first.mask]) === 3, "Repeated class cannot certify rank two");
  return { p, masks, binary_rank: 4, monsky_matrix: [[0, 0], [0, 0]], points: pair };
});
check(points.length === 14, "Exactly the 14 fixed point certificates");
check(rankF2([0n, 1n, 2n, 3n]) === 2, "Binary dependence boundary");
rejects(() => certificate({ p: 41n, sign: -1, A: 5n, B: 2n, c: 2n }), "Incorrect square root rejected");
rejects(() => certificate({ p: 49n, sign: -1, A: 5n, B: 2n, c: 1n }), "Composite parameter rejected");
rejects(() => certificate({ p: 41n, sign: -1, A: 10n, B: 4n, c: 4n }), "Nonprimitive parameter rejected");
rejects(() => certificate({ p: 41n, sign: 1, A: 1n, B: 0n, c: 1n }), "Degenerate parameter rejected");
rejects(() => squareClassBits(0n, 41n), "Zero Kummer coordinate rejected");
rejects(() => rankF2([-1n]), "Negative binary input rejected");
console.log(JSON.stringify({
  status: "Exact seven-curve arithmetic certificates; not general BSD or full saturation",
  assertions, arithmetic: "bigint integers and reduced rational pairs; no floating values", curves,
}, (_key: string, value: unknown) => typeof value === "bigint" ? value.toString() : value, 2));
