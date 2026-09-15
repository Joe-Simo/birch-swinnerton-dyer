/** Exact finite certificates for H9; the generic conclusions are proved in RESEARCH.md. */
type Bit = 0 | 1;
let assertions = 0;
function check(ok: boolean, label: string): void {
  if (!ok) throw new Error(label);
  assertions += 1;
}
function rejects(action: () => unknown, label: string): void {
  let threw = false;
  try { action(); } catch { threw = true; }
  check(threw, label);
}
function encode(bits: readonly number[]): bigint {
  if (bits.length !== 9 || bits.some((b) => b !== 0 && b !== 1)) {
    throw new RangeError("Expected nine binary entries.");
  }
  return bits.reduce((mask, b, j) => mask | (BigInt(b) << BigInt(j)), 0n);
}
function span(rows: readonly bigint[]): Set<bigint> {
  let values = new Set([0n]);
  for (const row of rows) {
    if (row < 0n) throw new RangeError("Nonnegative bit masks required.");
    values = new Set([...values, ...[...values].map((v) => v ^ row)]);
  }
  return values;
}
function det(matrix: readonly (readonly bigint[])[]): bigint {
  const n = matrix.length;
  if (matrix.some((r) => r.length !== n)) throw new RangeError("Square matrix required.");
  if (n === 0) return 1n;
  const first = matrix[0];
  if (first === undefined) throw new Error("Missing first row.");
  return first.reduce((total, value, j) => total + (j % 2 === 0 ? 1n : -1n) * value *
    det(matrix.slice(1).map((r) => r.filter((_v, k) => k !== j))), 0n);
}
const rows = {
  Tplus: [0,1,0, 0,1,1, 0,0,1],
  Tzero: [1,0,1, 0,0,1, 1,0,0],
  minus: [0,0,0, 0,0,1, 0,0,1],
  plus:  [0,0,1, 0,0,0, 0,0,1],
} as const satisfies Record<string, readonly Bit[]>;
const masks = {
  Tplus: encode(rows.Tplus), Tzero: encode(rows.Tzero),
  minus: encode(rows.minus), plus: encode(rows.plus),
};
check(span([]).size === 1, "Nullary span is the zero space");
check(det([]) === 1n, "Empty determinant convention");
rejects(() => encode([1,2]), "Malformed coordinates rejected");
rejects(() => span([-1n]), "Negative mask rejected");
rejects(() => det([[1n,2n]]), "Nonsquare determinant rejected");
for (const row of Object.values(rows)) {
  for (let j = 0; j < 3; j += 1) {
    check(((row[j] ?? 0) ^ (row[j+3] ?? 0) ^ (row[j+6] ?? 0)) === 0,
      "Each triple has square product in each basis coordinate");
  }
}
const minor = Object.values(rows).map((r) => [0,1,2,5].map((j) => BigInt(r[j] ?? 0)));
check(det(minor) === 1n, "Four-row Kummer minor has determinant one");
check(span(Object.values(masks)).size === 16, "Four independent classes");
check(span([masks.Tplus,masks.Tzero,masks.minus,masks.minus]).size === 8,
  "Duplicating a class cannot supply a fourth independent row");
const torsion = span([masks.Tplus,masks.Tzero]);
check(torsion.size === 4, "Torsion image has four elements");
const quotientRepresentatives = [0n,masks.minus,masks.plus,masks.minus^masks.plus];
const cosets = quotientRepresentatives.map((q) => new Set([...torsion].map((v) => v^q)));
check(new Set(cosets.flatMap((s) => [...s])).size === 16, "Four distinct torsor cosets");
for (const [source,target] of [[masks.plus,masks.minus],[masks.minus,masks.plus]] as const) {
  const oneWitness = span([masks.Tplus,masks.Tzero,source]);
  check(oneWitness.size === 8 && !oneWitness.has(target), "Complement outside one-witness Kummer span");
  check(!torsion.has(target) && !torsion.has(source^target), "Complement is neither zero nor source modulo torsion");
}
// These are existing H8 fixtures, not a new point search or a generic rank proof.
const fixtures = [
  {p:41n, sign:-1, A:5n, B:2n, c:1n},
  {p:41n, sign:1, A:2n, B:1n, c:1n},
] as const;
const fixtureResults = fixtures.map(({p,sign,A,B,c}) => {
  const e=BigInt(sign), u=p*c, v=A*A-e*B*B, w=A*A+e*B*B, z=2n*A*B;
  check(p*c*c === A**4n+6n*e*A*A*B*B+B**4n, "Quartic fixture");
  check(v*v-w*w+e*z*z === 0n && u*u-p*w*w-e*p*z*z === 0n, "Both quadric identities");
  const xNumerator=p*w*w, xDenominator=z*z;
  const yNumerator=p*u*v*w, yDenominator=z**3n;
  check(yNumerator*yNumerator === xNumerator**3n-p*p*xNumerator*z**4n, "Curve image homogeneous identity");
  const k1=sign === -1 ? u*u : p*v*v;
  const k2=sign === -1 ? p*v*v : u*u;
  check(xNumerator-p*z*z === k1 && xNumerator+p*z*z === k2, "Ordered Kummer factors");
  check((u+1n)**2n-p*w*w-e*p*z*z !== 0n, "Perturbed point rejected");
  return {p,sign,coordinates:[u,v,w,z],x:[xNumerator,xDenominator],y:[yNumerator,yDenominator]};
});
console.log(JSON.stringify({
  assertions, masks, minorDeterminant:det(minor), fullSpanSize:16, oneWitnessSpanSize:8,
  fixtureResults,
  scope:"Exact Kummer-vector algebra and two existing E41 point fixtures only; no finite check proves the generic group, morphism, or odd-degree assertions.",
}, (_key:string,value:unknown) => typeof value === "bigint" ? value.toString() : value, 2));
