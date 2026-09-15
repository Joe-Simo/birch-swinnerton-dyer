/** H13: exact finite certificates; infinite conclusions require RESEARCH.md. */
type Point = readonly [bigint, bigint] | null;
type Rat = readonly [bigint, bigint];
let assertions = 0;
function check(ok: boolean, label: string): void {
  assertions++;
  if (!ok) throw new Error(label);
}
function rejects(f: () => unknown, label: string): void {
  let failed = false;
  try { f(); } catch { failed = true; }
  check(failed, label);
}
function mod(n: bigint, p: bigint): bigint { return ((n % p) + p) % p; }
function isPrime(n: bigint): boolean {
  if (n < 2n) return false;
  for (let d = 2n; d * d <= n; d++) if (n % d === 0n) return false;
  return true;
}
function inv(n: bigint, p: bigint): bigint {
  let a = mod(n, p), b = p, x = 1n, y = 0n;
  while (b !== 0n) { const q = a / b; [a, b] = [b, a - q*b]; [x, y] = [y, x - q*y]; }
  if (a !== 1n) throw new RangeError("Noninvertible denominator");
  return mod(x, p);
}
function residue(r: Rat, p: bigint): bigint { return mod(r[0] * inv(r[1], p), p); }
function pointEqual(P: Point, Q: Point): boolean {
  return P === null ? Q === null : Q !== null && P[0] === Q[0] && P[1] === Q[1];
}
class FiniteCurve {
  readonly a2: bigint;
  readonly a4: bigint;
  constructor(readonly p: bigint, readonly c: bigint, readonly k: bigint) {
    if (p < 3n || !isPrime(p)) throw new RangeError("Odd prime required");
    this.a2 = mod(c*c+k, p); this.a4 = mod(c*c*k, p);
    if (mod(16n*c**4n*k*k*(c*c-k)**2n, p) === 0n) throw new RangeError("Bad reduction");
  }
  contains(P: Point): boolean {
    return P === null || mod(P[1]**2n - P[0]*(P[0]+this.c**2n)*(P[0]+this.k), this.p) === 0n;
  }
  add(P: Point, Q: Point): Point {
    if (!this.contains(P) || !this.contains(Q)) throw new RangeError("Not on curve");
    if (P === null) return Q;
    if (Q === null) return P;
    const p = this.p, [x,y] = P, [u,v] = Q;
    if (x === u && mod(y+v,p) === 0n) return null;
    const slope = x === u
      ? mod((3n*x*x+2n*this.a2*x+this.a4)*inv(2n*y,p),p)
      : mod((v-y)*inv(u-x,p),p);
    const xx = mod(slope*slope-this.a2-x-u,p);
    return [xx, mod(slope*(x-xx)-y,p)];
  }
  times(P: Point, n: number): Point {
    if (!Number.isSafeInteger(n) || n < 0) throw new RangeError("Nonnegative small multiplier required");
    let out: Point = null;
    for (let j=0;j<n;j++) out=this.add(out,P);
    return out;
  }
  points(): Point[] {
    const out: Point[] = [null];
    for (let x=0n;x<this.p;x++) for (let y=0n;y<this.p;y++) if (this.contains([x,y])) out.push([x,y]);
    return out;
  }
}
const C: Rat = [-39785n,37632n], K: Rat = [-46057n,6272n];
const seed = [[1n,14n],[37n,14n]] as const;
const next = [[-16890371n,79256324n],[210069683n,77723044n]] as const;
function quotient(P: readonly [Rat,Rat], p: bigint, c: bigint): Point {
  const x=residue(P[0],p), y=residue(P[1],p), z=mod(y*(x*x+c),p);
  return [mod(c*x*x,p),mod(c*x*z,p)];
}
rejects(()=>inv(0n,13n),"zero denominator");
rejects(()=>residue([1n,13n],13n),"bad rational reduction");
rejects(()=>new FiniteCurve(15n,6n,4n),"composite modulus");
rejects(()=>new FiniteCurve(13n,0n,9n),"singular reduction");
const rows=[];
for (const [p,expected] of [[13n,16],[19n,24],[31n,40]] as const) {
  const c=residue(C,p), k=residue(K,p), E=new FiniteCurve(p,c,k);
  const R0=quotient(seed,p,c), R1=quotient(next,p,c);
  check(E.contains(R0)&&E.contains(R1),"two inherited points on elliptic quotient");
  if (R0===null) throw new Error("Affine seed vanished");
  const delta=E.add(R1,[R0[0],mod(-R0[1],p)]);
  const pts=E.points();
  check(pts.length===expected,"complete finite-field count");
  check(E.contains(delta),"difference lies on quotient");
  check(E.times(delta,expected)===null,"Lagrange control");
  const eight=E.times(delta,8);
  if (p===31n) {
    check(pointEqual(delta,[28n,5n]),"mod31 difference");
    check(E.times(delta,5)===null&&delta!==null,"exact order5");
    check(pointEqual(eight,[4n,28n]),"not killed by8");
    rejects(()=>E.add([0n,1n],delta),"false elliptic point rejected");
  }
  rows.push({p,c,k,count:pts.length,R0,R1,delta,eight});
}
check(16%8===0&&24%8===0&&16%16===0&&24%16!==0,"gcd of torsion bounds is8");
const p=13n,c=residue(C,p),k=residue(K,p);
check(c===6n&&k===9n,"local coefficient reductions");
const sq=new Set<bigint>();for(let j=0n;j<p;j++)sq.add(j*j%p);
const table=[];
for(let x=0n;x<p;x++) {
  const f=mod((x*x+c)*(c*x*x+k),p),g=mod(x**4n+6n*x*x+1n,p);
  table.push({x,f,g,lifts:sq.has(f)});
  if(sq.has(f))check(g!==0n&&!sq.has(g),"every soluble residue has nonsquare g");
}
check(!sq.has(c),"nonintegral/infinity leading coefficient obstruction");
check(table.filter(r=>r.lifts).length===8,"all8 admissible affine x residues counted");
for(const n of [257n,313n])check(sq.has(n%p),"known rank2 target excluded at13");
check(!sq.has(137n%p),"seed passes local squareclass necessity");
// Branch-changing control. Tripling on the minus quartic is evaluated modulo13.
const y=residue(seed[1],p),x=residue(seed[0],p);
const N=mod(y*(y**8n-6n*y**4n+24n*y*y-3n),p);
const D=mod(3n*y**8n-24n*y**6n+6n*y**4n-1n,p);
const y3=mod(N*inv(D,p),p),U=mod(x*x+3n,p),V=mod(y3*y3-3n,p);
const c3=mod((U*V-8n)*inv(U-V,p)+3n,p),k3=mod(6n*c3-1n,p);
check(y3===9n&&c3===1n&&k3===5n,"product tripling changes the base fiber");
for(const [n,r] of [[257n,6n],[313n,3n]] as const) {
  const xx=5n,zz=0n;
  const f=mod((xx*xx+c3)*(c3*xx*xx+k3),p),g=mod(xx**4n+6n*xx*xx+1n,p);
  check(mod(zz*zz-f,p)===0n&&mod(n*r*r-g,p)===0n,"changed-fiber local simultaneous point");
  const fp=mod(4n*c3*xx**3n+2n*(c3*c3+k3)*xx,p);
  check(mod(-fp*2n*n*r,p)!==0n,"nonsingular two-equation Hensel minor");
}
// Numerical consequences of the proved ramification counts, not genus proofs.
check(2*5-2===8,"double cover ramification arithmetic");
check(2*37-2===8*9,"one-step inverse image ramification arithmetic");
const coefficients=Array.from({length:12},(_,j)=>(1n-(-3n)**BigInt(j))/4n);
check(coefficients.every((a,j)=>j===0||a===1n-3n*coefficients[j-1]!),"orbit coefficient recurrence");
check(new Set(coefficients).size===12,"finite distinct-coefficient sanity check");
console.log(JSON.stringify({assertions,rows,local13:{table,squares:[...sq].sort((a,b)=>a<b?-1:a>b?1:0)},changedFiber:{c:c3,k:k3,y:y3},coefficients,scope:"Exact checks at13,19,31; all13 local x residues; one product-tripling control. Infinite orbit, genus and finiteness claims use the written proof, not extrapolation."},(_key:string,v:unknown)=>typeof v==="bigint"?v.toString():v,2));
