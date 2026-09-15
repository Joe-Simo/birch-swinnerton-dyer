/** Fixed exact certificates only; the infinite local and descent arguments are in RESEARCH.md. */
type Point = readonly [bigint, bigint, bigint, bigint];
const p = 113n;
let checks = 0;
function check(ok: boolean, label: string): void {
  if (!ok) throw new Error(label);
  checks += 1;
}
function mod(a: bigint, m: bigint): bigint { return ((a % m) + m) % m; }
function valuation(a: bigint, prime: bigint): number {
  if (prime < 2n) throw new RangeError("Prime must be at least two.");
  if (a === 0n) return Infinity;
  let n = a < 0n ? -a : a;
  let v = 0;
  while (n % prime === 0n) { n /= prime; v += 1; }
  return v;
}
function equations([c, d, t, z]: Point): readonly [bigint, bigint] {
  return [c*c + 8n*c*d + 23n*d*d - t*t - 4n*z*z,
    -c*c + 7n*d*d - 7n*z*z + 4n*t*z];
}
function normForm([c, d, t, z]: Point): bigint {
  const u = 49n*c - 14n*d - 26n*t - 350n*z;
  const v = 7n*c + 14n*d - 5n*t - 35n*z;
  return u*u - p*v*v;
}
function jacobianCT([c, d, t, z]: Point): bigint {
  return (2n*c + 8n*d)*(4n*z) - (-2n*t)*(-2n*c);
}
function hensel(point: Point): { errors: readonly [bigint, bigint]; n: number; delta: number; valid: boolean } {
  const errors = equations(point);
  const n = Math.min(...errors.map((e) => valuation(e, 2n)));
  const delta = valuation(jacobianCT(point), 2n);
  return { errors, n, delta, valid: Number.isFinite(delta) && n > 2*delta };
}
function rejected(action: () => void, label: string): void {
  let failed = false;
  try { action(); } catch { failed = true; }
  check(failed, label);
}
const point2: Point = [15035n, 18942n, -121505n, 9471n];
const point113: Point = [21n, -8n, 0n, 1n];
const h = hensel(point2);
check(h.valid, "strict multivariable Hensel inequality");
check(valuation(h.errors[0],2n) === 18 && valuation(h.errors[1],2n) === 20, "exact error orders");
check(h.delta === 2 && h.n-h.delta === 16, "root agrees through modulus 2^16");
const nv = normForm(point2);
const v = valuation(nv, 2n);
check(v === 7 && mod(nv,1024n) === 640n, "norm has order 7 and unit 5 mod8");
check(mod(point2[3],2n) === 1n, "denominator psi is a unit");
const unit = mod(nv/(2n**BigInt(v)),8n);
const hilbertExponent = ((unit*unit-1n)/8n) % 2n;
check(unit === 5n && hilbertExponent === 1n, "Hilbert symbol (norm/psi^2,2)_2 equals -1");
check(equations(point113)[0] === 565n && equations(point113)[1] === 0n, "113-adic starting residual");
// The determinant in variables theta,psi at (theta,psi)=(0,1) is 32.
check(32n % p !== 0n, "113-adic unit Jacobian minor");
check(mod(14n**4n+4n,p) === 0n && mod(4n*14n**3n,p) !== 0n, "nonsingular root for d=113");
check(mod(18n**4n+1n,p) === 0n && mod(4n*18n**3n,p) !== 0n, "nonsingular root for d=226");
check(mod(51n*51n-2n,p) === 0n, "2 is square at 113");
check(mod(3n*3n-2n,7n) === 0n, "2 is square at 7");
check(mod(6385n,8n) === 1n && mod(p,8n) === 1n, "positive dual 2-adic units");
check(p*p - ((-1n)*0n**4n - p*p/(-1n)) === 0n, "counterexample to negative-class exclusion");
rejected(() => check(hensel([5n,2n,1n,1n]).n >= 18, "unrefined point is insufficient for final precision"), "reject low-precision substitution");
rejected(() => check(hensel([15036n,18942n,-121505n,9471n]).valid, "corrupted certificate"), "reject corrupted point");
rejected(() => check(mod(14n**4n+1n,p) === 0n, "wrong quartic equation"), "reject wrong local equation");
console.log(JSON.stringify({status:"fixed exact certificates passed; consult written proof", checks,
  point2, point113, hensel: h, norm: nv, normValuation: v, normUnitMod8: unit,
  hilbertSign: -1, theoremNotCheckedByCode: "Fisher's descent/pushout interpretation and the written all-place proof"},
  (_key: string, value: unknown) => typeof value === "bigint" ? value.toString() : value, 2));
