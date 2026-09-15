/** Exact finite parts of PRIME_FILTER.md; no bounded rational search. */
export {};
let assertions = 0;
function check(ok: boolean, label: string): void {
  assertions += 1;
  if (!ok) throw new Error(label);
}
function positiveMod(x: bigint, m: bigint): bigint { return ((x % m) + m) % m; }
function cubic(x: bigint): bigint { return x * (x - 1n) * (x + 3n); }
function quartic(t: bigint): bigint { return t ** 4n - 4n * t ** 3n + 8n * t * t - 24n * t + 36n; }
const rationalPoints = [[0n,0n],[1n,0n],[-3n,0n],[3n,6n],[3n,-6n],[-1n,2n],[-1n,-2n]] as const;
check(new Set(rationalPoints.map(p => p.join(","))).size === 7, "seven distinct affine points plus O");
check(rationalPoints.every(([x,y]) => y*y === cubic(x)), "all seven affine points lie on E0");
const reductions = [5n,7n].map(p => {
  const points: Array<readonly [bigint,bigint]> = [];
  for (let x=0n; x<p; x+=1n) for (let y=0n; y<p; y+=1n) {
    if (positiveMod(y*y-cubic(x),p) === 0n) points.push([x,y]);
  }
  check(points.length+1 === 8, "finite field group order including O");
  check(2304n % p !== 0n, "good reduction prime");
  return { prime:p,order:points.length+1,affinePoints:points };
});
let primitiveResidues=0;
for (let r=0n;r<16n;r+=1n) for(let s=0n;s<16n;s+=1n) for(let t=0n;t<16n;t+=1n) {
  if ((s%2n !== 0n || t%2n !== 0n) && positiveMod(r*r-2n*s**4n+4n*s*s*t*t-8n*t**4n,16n)===0n) primitiveResidues+=1;
}
check(primitiveResidues===0,"complete primitive d=2 obstruction modulo16");
const quarticPoints = [[0n,6n],[0n,-6n],[2n,2n],[2n,-2n],[3n,3n],[3n,-3n]] as const;
const images=quarticPoints.map(([t,w])=>{
  check(w*w===quartic(t),"quartic point residual");
  const numerator=w+t*t-2n*t;
  check(numerator%2n===0n,"fixture image integral");
  const x=numerator/2n,y=(x+1n)*(t-1n)-2n;
  check(y*y===cubic(x),"forward map fixture");
  return {point:[t,w],image:[x,y]};
});
check(new Set(images.map(row=>row.image.join(","))).size===6,"six distinct forward images");
check(12n*36n-3n*(-4n)*(-24n)+8n**2n===208n,"quartic I invariant");
check(72n*8n*36n-27n*(-24n)**2n-27n*(-4n)**2n*36n+9n*(-4n)*8n*(-24n)-2n*8n**3n===-4480n,"quartic J invariant");
check(2n**8n*3n**2n===2304n,"elliptic discriminant normalization");
check(-2n*2n===-4n && 2n**2n-4n*(-3n)===16n,"two-isogeny target coefficients");
check(quartic(2n)===4n && quartic(3n)===9n,"nonzero parameter points");
check(2n**8n-56n*2n**4n+1296n===16n*41n,"t2 squarefree kernel witness");
check(3n**8n-56n*3n**4n+1296n===81n*41n,"t3 squarefree kernel witness");
check(2+0-1-1===0,"rank formula arithmetic only");
console.log(JSON.stringify({status:"exact finite prime-filter checks passed",assertions,reductions,primitiveResidues,images,scope:"Rational-point completeness is the written rank-zero/torsion proof, not finite parameter enumeration."},(_k:string,v:unknown)=>typeof v==="bigint"?v.toString():v,2));
