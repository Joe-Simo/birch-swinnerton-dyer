/** H5 exact finite certificates; proofs and non-claims are in RESEARCH.md. */
type Point = Readonly<{x: bigint; y: bigint}> | null;
type TowerPoint = readonly [bigint, bigint, bigint, bigint];
const assertions: string[] = [];
function check(condition: boolean, label: string): void {
  if (!condition) throw new Error(label);
  assertions.push(label);
}
function rejects(action: () => unknown, label: string): void {
  let threw = false;
  try { action(); } catch { threw = true; }
  check(threw, label);
}
function mod(n: bigint, q: bigint): bigint {
  if (q <= 0n) throw new RangeError('Positive modulus required.');
  return ((n % q) + q) % q;
}
function inverse(n: bigint, q: bigint): bigint {
  let r = q, s = mod(n, q), a = 0n, b = 1n;
  while (s !== 0n) {
    const k = r / s;
    [r, s] = [s, r - k * s];
    [a, b] = [b, a - k * b];
  }
  if (r !== 1n) throw new RangeError('Element is not invertible.');
  return mod(a, q);
}
function key(p: Point): string { return p === null ? 'O' : `${p.x},${p.y}`; }
function onCurve(p: Point, q: bigint): boolean {
  return p === null || mod(p.y ** 2n - p.x ** 3n + 1681n * p.x, q) === 0n;
}
function points(q: bigint): Point[] {
  if (![3n, 5n, 7n, 11n].includes(q)) throw new RangeError('Only registered good-prime fields are enumerated.');
  const out: Point[] = [null];
  for (let x = 0n; x < q; x += 1n) for (let y = 0n; y < q; y += 1n) {
    if (onCurve({x, y}, q)) out.push({x, y});
  }
  return out;
}
function add(p: Point, r: Point, q: bigint): Point {
  if (!onCurve(p, q) || !onCurve(r, q)) throw new RangeError('Point is off the curve.');
  if (p === null) return r;
  if (r === null) return p;
  if (p.x === r.x && mod(p.y + r.y, q) === 0n) return null;
  const slope = p.x === r.x
    ? mod((3n * p.x ** 2n - 1681n) * inverse(2n * p.y, q), q)
    : mod((r.y - p.y) * inverse(r.x - p.x, q), q);
  const x = mod(slope ** 2n - p.x - r.x, q);
  return {x, y: mod(slope * (p.x - x) - p.y, q)};
}
function multiply(n: bigint, p: Point, q: bigint): Point {
  if (n < 0n) return multiply(-n, p === null ? null : {x: p.x, y: mod(-p.y, q)}, q);
  let acc: Point = null, cur = p, k = n;
  while (k > 0n) {
    if (k % 2n !== 0n) acc = add(acc, cur, q);
    cur = add(cur, cur, q); k /= 2n;
  }
  return acc;
}
function coefficient(level: number): bigint {
  if (!Number.isSafeInteger(level) || level < 1 || level > 64) throw new RangeError('Registered levels are 1..64.');
  const numerator = 1n - (-2n) ** BigInt(level);
  if (numerator % 3n !== 0n) throw new Error('Coefficient is not integral.');
  return numerator / 3n;
}
function absolute(n: bigint): bigint { return n < 0n ? -n : n; }
function tower(level: number): TowerPoint[] {
  if (!Number.isInteger(level) || level < 1 || level > 4) throw new RangeError('Registered abstract levels are 1..4.');
  const modulus = 2n ** BigInt(level), out: TowerPoint[] = [];
  for (let x = 0n; x < modulus; x += 1n) for (let y = 0n; y < modulus; y += 1n) {
    for (let t = 0n; t < 2n; t += 1n) for (let u = 0n; u < 2n; u += 1n) out.push([x,y,t,u]);
  }
  return out;
}
function towerKey(p: TowerPoint): string { return p.join(','); }
function down(p: TowerPoint, targetLevel: number): TowerPoint {
  const n = 2n ** BigInt(targetLevel);
  return [mod(p[0], n), mod(p[1], n), p[2], p[3]];
}
function up(p: TowerPoint): TowerPoint { return [2n * p[0], 2n * p[1], 0n, 0n]; }
function twice(p: TowerPoint, level: number): TowerPoint {
  const n = 2n ** BigInt(level);
  return [mod(2n * p[0], n), mod(2n * p[1], n), 0n, 0n];
}
function marked(p: TowerPoint, rank: 0 | 1 | 2): boolean {
  return rank === 2 || (rank === 1 ? p[1] === 0n : p[0] === 0n && p[1] === 0n);
}

check(inverse(-2n, 11n) === 5n, 'signed modular inversion');
rejects(() => inverse(0n, 11n), 'zero inverse rejected');
rejects(() => inverse(3n, 9n), 'nonunit inverse rejected');
rejects(() => points(41n), 'unregistered or bad field excluded');
rejects(() => coefficient(0), 'zero tower level excluded');
rejects(() => coefficient(65), 'unregistered level excluded');
rejects(() => add({x:0n,y:1n},null,11n), 'invalid point rejected');
check(120n ** 2n === (-9n) ** 3n - 1681n * (-9n), 'P is exactly on E41');
const finiteRows = [];
for (const q of [3n,5n,7n,11n]) {
  const group = points(q), p = {x:mod(-9n,q), y:mod(120n,q)};
  const image = [...new Set(group.map(r => key(multiply(3n,r,q))))].sort();
  check(mod(64n * 41n ** 6n, q) !== 0n, `good reduction q=${q}`);
  check(group.every(r => key(add(r,null,q)) === key(r)), `identity q=${q}`);
  check(group.every(r => multiply(2n,r,q) === null || onCurve(multiply(2n,r,q),q)), `doubling closure q=${q}`);
  check(group.every(r => key(multiply(-1n,r,q)) === key(r === null ? null : {x:r.x,y:mod(-r.y,q)})), `negation q=${q}`);
  check(group.every(r => group.every(s => onCurve(add(r,s,q),q) && key(add(r,s,q)) === key(add(s,r,q)))), `addition closure and commutativity q=${q}`);
  check(group.length === (q === 3n ? 4 : q === 11n ? 12 : 8), `exact group order q=${q}`);
  check(image.includes(key(p)) === (q !== 11n), `tripling membership q=${q}`);
  finiteRows.push({q, point: p, groupOrder:group.length, triplingImage:image, pointInImage:image.includes(key(p)), points:group});
}
const e11=points(11n);
let associative = true;
for (const p of e11) for (const q of e11) for (const r of e11) {
  associative &&= key(add(add(p,q,11n),r,11n)) === key(add(p,add(q,r,11n),11n));
}
check(associative, 'all 12^3 associativity identities at certificate prime');
check([...new Set(e11.map(p=>key(multiply(3n,p,11n))))].sort().join('|') === ['0,0','3,0','8,0','O'].join('|'), 'complete mod11 tripling image');
check(e11.every(p=>multiply(6n,p,11n)===null),'finite group exponent divides six');
const coefficientRows=[];
for (let m=1;m<=64;m+=1) {
  const a=coefficient(m), n=2n**BigInt(m);
  check(mod(3n*a,n)===1n,`inverse-three residue m=${m}`);
  check(absolute(a)<=n/2n,`centered coefficient m=${m}`);
  if(m<64) check(coefficient(m+1)-a===(-2n)**BigInt(m),`compatibility m=${m}`);
  if(m<=10) {
    const candidates=[];
    for(let k=-n;k<=n;k+=1n) if(mod(3n*k,n)===1n)candidates.push(k);
    check(candidates.every(k=>absolute(k)>=absolute(a)),`exhaustive centered minimality m=${m}`);
  }
  coefficientRows.push({level:m,a,modulus:n,heightFactor:a*a});
}
const abstractRows=[];
for(let m=1;m<=4;m+=1) {
  const group=tower(m), n=2n**BigInt(m);
  check(BigInt(group.length)===4n*n*n,`abstract full order m=${m}`);
  for(const rank of [0,1,2] as const) {
    const kummer=group.filter(p=>marked(p,rank));
    const projected=new Set(group.map(p=>rank===2?'zero':rank===1?String(p[1]):`${p[0]},${p[1]}`));
    check(BigInt(kummer.length)===4n*n**BigInt(rank),`marked Kummer order r=${rank},m=${m}`);
    check(BigInt(projected.size)===n**BigInt(2-rank),`abstract Sha torsion quotient r=${rank},m=${m}`);
    abstractRows.push({level:m,rank,divisibleCorank:2-rank,selmerOrder:group.length,kummerOrder:kummer.length,shaQuotientOrder:projected.size});
  }
  if(m<4) {
    const higher=tower(m+1);
    check(new Set(higher.map(p=>towerKey(down(p,m)))).size===group.length,`down map surjective m=${m}`);
    check(higher.every(p=>towerKey(up(down(p,m)))===towerKey(twice(p,m+1))),`inclusion after reduction equals two m=${m}`);
    check(group.every(p=>towerKey(down(up(p),m))===towerKey(twice(p,m))),`reduction after inclusion equals two m=${m}`);
    check(group.filter(p=>towerKey(up(p))==='0,0,0,0').length===4,`inclusion kernel is marked rational torsion m=${m}`);
  }
}
console.log(JSON.stringify({status:'PASS',assertions:assertions.length,checks:assertions,finiteFields:finiteRows,coherentInverseThree:coefficientRows,abstractTowers:abstractRows,scope:{finite:'E41 at q=3,5,7,11; coefficients m=1..64; centered minimality m<=10; abstract levels1..4',proof:'Infinite-depth and height statements are separately proved in RESEARCH.md',nonclaims:'Abstract rank0 and rank1 models are not claimed realized by elliptic curves; no canonical heights numerically estimated; no universal BSD proof.'}},(_k:string,v:unknown)=>typeof v==='bigint'?v.toString():v,2));
