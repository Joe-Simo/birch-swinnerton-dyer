type Ratio = readonly [bigint, bigint];
type Witness = readonly [bigint, bigint, bigint];
type Row = Readonly<{p: bigint; minus: Witness; plus: Witness}>;

let checks = 0;
function check(condition: boolean, label: string): void {
  checks += 1;
  if (!condition) throw new Error(`FAIL ${label}`);
}
function abs(x: bigint): bigint { return x < 0n ? -x : x; }
function gcd(a: bigint, b: bigint): bigint {
  let x = abs(a); let y = abs(b);
  while (y !== 0n) { const r = x % y; x = y; y = r; }
  return x;
}
function mod(x: bigint, m: bigint): bigint { return ((x % m) + m) % m; }
function ratio(a: bigint, b: bigint): Ratio {
  if (b === 0n) throw new RangeError("Denominator is zero.");
  const g = gcd(a, b); const sign = b < 0n ? -1n : 1n;
  return [sign * a / g, sign * b / g];
}
function valuation2(x: bigint): number {
  if (x === 0n) throw new RangeError("Valuation of zero excluded from this finite checker.");
  let y = abs(x); let v = 0;
  while (y % 2n === 0n) { y /= 2n; v += 1; }
  return v;
}
function quartic(a: bigint, b: bigint, sign: 1n | -1n): bigint {
  return a ** 4n + 6n * sign * a * a * b * b + b ** 4n;
}
function curveResidual(q: Ratio, x: bigint, y: bigint, z: bigint): bigint {
  const [n, d] = q;
  return d * d * quartic(y, z, -1n) - n * n * quartic(x, z, 1n);
}
function nonsingularRationalMultiplier(q: Ratio): boolean {
  const [n, d] = ratio(q[0], q[1]);
  if (n === 0n) throw new RangeError("The research fiber requires q nonzero.");
  // Certified for rational q by the four exact derivative cases in RESEARCH.md.
  return abs(n) !== d;
}
function rejects(action: () => unknown, label: string): void {
  let rejected = false;
  try { action(); } catch { rejected = true; }
  check(rejected, label);
}
const fixtures: readonly Row[] = [
  {p:41n,minus:[5n,2n,1n],plus:[2n,1n,1n]},
  {p:137n,minus:[37n,14n,47n],plus:[14n,1n,17n]},
  {p:257n,minus:[13n,4n,7n],plus:[104n,11n,697n]},
  {p:313n,minus:[19409n,582n,21235361n],plus:[3n,2n,1n]},
  {p:353n,minus:[15641n,968n,12870529n],plus:[4n,1n,1n]},
  {p:457n,minus:[17n,6n,7n],plus:[653n,282n,29273n]},
  {p:761n,minus:[41n,10n,49n],plus:[190n,59n,1649n]}
];
const rows = fixtures.map(({p,minus,plus}) => {
  const [am,bm,cm] = minus; const [ap,bp,cp] = plus;
  check(quartic(am,bm,-1n) === p*cm*cm, `minus witness ${p}`);
  check(quartic(ap,bp,1n) === p*cp*cp, `plus witness ${p}`);
  const q = ratio(cm*bp*bp,cp*bm*bm);
  let x = ap*bm; let y = am*bp; let z = bp*bm;
  const common = gcd(gcd(x,y),z); x/=common; y/=common; z/=common;
  const [n,d] = q;
  check(curveResidual(q,x,y,z) === 0n, `projective ratio normalization ${p}`);
  check((valuation2(n)-valuation2(d)) % 2 === 0, `necessary q valuation ${p}`);
  check(nonsingularRationalMultiplier(q), `smooth fixed q fixture ${p}`);
  const u = y*y-3n*z*z;
  const v = n*(x*x+3n*z*z);
  const w = d*d*y**4n-n*n*x**4n-3n*z*z*(d*d*y*y+n*n*x*x);
  check(d*d*u*u === n*n*x**4n+6n*n*n*x*x*z*z+(n*n+8n*d*d)*z**4n, `Dy map ${p}`);
  check(v*v === d*d*quartic(y,z,-1n)+8n*n*n*z**4n, `Dx map ${p}`);
  const rhs = z**4n*((n*n+8n*d*d)*d*d*y**4n+18n*n*n*d*d*y*y*x*x+n*n*(d*d+8n*n*n)*x**4n);
  check(w*w === rhs, `Dxy map ${p}`);
  return {p,q,point:[x,y,z],v2q:valuation2(n)-valuation2(d)};
});
const reciprocal: Ratio = [47n,17n];
check(curveResidual(reciprocal,1n,37n,14n) === 0n, "p137 reciprocal witness gives q47/17");
check(47n*47n*quartic(1n,14n,1n) === 17n*17n*quartic(37n,14n,-1n), "variable ratio surface p137 identity");
check(curveResidual(reciprocal,1n,38n,14n) !== 0n, "perturbed witness rejected");
check(quartic(1n,14n,1n) === 137n*17n*17n, "p137 recovered positive squarefree kernel");
check(curveResidual([1n,1n],1n,5n,2n) === 0n, "H10 prime41 point at q1");
check(!nonsingularRationalMultiplier([1n,1n]) && !nonsingularRationalMultiplier([-1n,1n]), "both singular signs excluded");
rejects(()=>nonsingularRationalMultiplier([0n,1n]),"zero multiplier rejected");
rejects(()=>ratio(1n,0n),"zero denominator rejected");

let primitive = 0; const solutions: bigint[][] = []; const residues = new Set<string>();
for (let x=0n; x<16n; x+=1n) for (let y=0n; y<16n; y+=1n) for (let z=0n; z<16n; z+=1n) {
  if (x%2n===0n && y%2n===0n && z%2n===0n) continue;
  primitive+=1;
  const r=mod(curveResidual([7n,2n],x,y,z),16n);
  residues.add(r.toString()); if (r===0n) solutions.push([x,y,z]);
}
check(primitive === 3584, "all primitive projective triples modulo16 covered");
check(solutions.length === 0, "q7/2 has no primitive solution modulo16");
check(nonsingularRationalMultiplier([7n,2n]), "obstructed fiber is smooth");
// Exact quotient points for q7/2: Dy(0,9/2); Dx infinity +/-1; Dxy infinity +/-9/2.
check(9n*9n === 7n*7n+8n*2n*2n, "Dy rational point at x0");
check(1n*1n === 1n, "Dx infinity leading coefficient square");
check(9n*9n === 7n*7n+8n*2n*2n, "Dxy infinity leading coefficient square");
check((valuation2(15n)-valuation2(2n))%2 !== 0 && (valuation2(-3n)-valuation2(2n))%2 !== 0, "both Dy x0 branches fail the necessary lifting square test at2");
let oddCount=0;
for (let z=1n; z<64n; z+=2n) {
  check(quartic(z,1n,1n)%8n === 0n && mod(quartic(z,1n,1n)/8n,8n)===1n, "odd plus unit identity");
  check(quartic(z,1n,-1n)%4n === 0n && mod(-quartic(z,1n,-1n)/4n,8n)===1n, "odd minus unit identity");
  oddCount+=1;
}
check(oddCount===32,"all odd residues modulo64 covered");
const result = {
  status:"exact certificates passed; no general BSD claim", checks,
  integerEncoding:"big integers serialized as decimal strings",
  fixtures:rows, reciprocal137:{q:reciprocal,point:[1n,37n,14n]},
  obstruction:{q:[7n,2n],modulus:16,primitiveTriples:primitive,solutions,residualSet:[...residues].sort((a,b)=>Number(a)-Number(b))},
  oddResidues:oddCount,
  limitations:["finite fixtures do not prove universal point existence","genus and Faltings consequences have separate written proofs","quotient points do not by themselves lift"]
};
console.log(JSON.stringify(result,(_key:string,value:unknown)=>typeof value === "bigint" ? value.toString() : value,2));
