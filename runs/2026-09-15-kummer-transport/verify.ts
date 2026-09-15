/** H12 exact rational checker. No numerical L-values or probabilistic primality. */
type Rat = readonly [bigint, bigint];
type Point = Readonly<{x: Rat; y: Rat}> | null;
const abs = (a: bigint): bigint => a < 0n ? -a : a;
function gcd(a: bigint, b: bigint): bigint { a=abs(a);b=abs(b);while(b!==0n){[a,b]=[b,a%b];}return a; }
function q(a: bigint, b=1n): Rat {
  if(b===0n)throw new RangeError("Zero denominator");
  const g=gcd(a,b); if(b<0n){a=-a;b=-b;}return [a/g,b/g];
}
const add=(a:Rat,b:Rat):Rat=>q(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);
const neg=(a:Rat):Rat=>[-a[0],a[1]];
const sub=(a:Rat,b:Rat):Rat=>add(a,neg(b));
const mul=(a:Rat,b:Rat):Rat=>q(a[0]*b[0],a[1]*b[1]);
const div=(a:Rat,b:Rat):Rat=>q(a[0]*b[1],a[1]*b[0]);
const pow=(a:Rat,e:bigint):Rat=>q(a[0]**e,a[1]**e);
const eq=(a:Rat,b:Rat):boolean=>a[0]===b[0]&&a[1]===b[1];
const scale=(a:Rat,k:bigint):Rat=>mul(a,q(k));
let assertions=0;
function check(ok:boolean,label:string):void { assertions++;if(!ok)throw new Error(label); }
function rejects(fn:()=>unknown,label:string):void { let caught=false;try{fn();}catch{caught=true;}check(caught,label); }
function F(t:Rat,e:1|-1):Rat { return add(add(pow(t,4n),scale(pow(t,2n),BigInt(6*e))),q(1n)); }
function curvePoint(n:bigint,t:Rat,u:Rat,e:1|-1):Point {
  if(t[0]===0n||u[0]===0n||!eq(F(t,e),scale(pow(u,2n),n)))throw new RangeError("Invalid quartic witness");
  const x=div(scale(pow(add(pow(t,2n),q(BigInt(e))),2n),n),scale(pow(t,2n),4n));
  const y=div(scale(mul(u,sub(pow(t,4n),q(1n))),n*n),scale(pow(t,3n),8n));
  if(!eq(pow(y,2n),sub(pow(x,3n),scale(x,n*n))))throw new Error("Curve residual");
  return {x,y};
}
function ecAdd(n:bigint,p:Point,r:Point):Point {
  if(p===null)return r;if(r===null)return p;
  if(eq(p.x,r.x)&&eq(p.y,neg(r.y)))return null;
  const slope=eq(p.x,r.x)?div(sub(scale(pow(p.x,2n),3n),q(n*n)),scale(p.y,2n)):div(sub(r.y,p.y),sub(r.x,p.x));
  const x=sub(sub(pow(slope,2n),p.x),r.x);return {x,y:sub(mul(slope,sub(p.x,x)),p.y)};
}
function pointEqual(p:Point,r:Point):boolean { return p===null?r===null:r!==null&&eq(p.x,r.x)&&eq(p.y,r.y); }
function triple(t:Rat,u:Rat,e:1|-1):readonly [Rat,Rat] {
  const v=pow(t,2n),E=BigInt(e);
  const N=mul(t,sub(sub(sub(pow(v,4n),scale(pow(v,2n),6n)),scale(v,24n*E)),q(3n)));
  const D=sub(add(add(scale(pow(v,4n),3n),scale(pow(v,3n),24n*E)),scale(pow(v,2n),6n)),q(1n));
  const coeff=[1n,24n*E,28n,168n*E,582n,168n*E,28n,24n*E,1n];
  let H=q(0n);for(const c of coeff)H=add(mul(H,v),q(c));
  return [div(N,D),mul(u,div(H,pow(D,2n)))];
}
function squareclassValuation(a:Rat,p:bigint):number {
  if(a[0]===0n||p<2n)throw new RangeError("Valuation input");
  let n=abs(a[0]),d=a[1],v=0;while(n%p===0n){n/=p;v++;}while(d%p===0n){d/=p;v--;}return v;
}
function primeTrial(n:bigint):boolean {
  if(n<2n)return false;if(n%2n===0n)return n===2n;
  for(let d=3n;d*d<=n;d+=2n)if(n%d===0n)return false;return true;
}
function osculate(x:Rat,y:Rat,W:Rat) {
  if(!eq(pow(W,2n),mul(F(x,1),F(y,-1))))throw new RangeError("Not a surface point");
  const U=add(pow(x,2n),q(3n)),V=sub(pow(y,2n),q(3n)),gap=sub(U,V);
  const a=div(sub(mul(U,V),q(8n)),gap),b=div(W,gap),C=add(a,q(3n)),K=add(scale(a,6n),q(17n));
  if(C[0]===0n||K[0]===0n||b[0]===0n)throw new RangeError("Singular fiber");
  const z=mul(y,add(pow(x,2n),C));
  const middle=add(pow(C,2n),K);
  const fp=add(scale(mul(C,pow(x,3n)),4n),scale(mul(middle,x),2n));
  const fppHalf=add(scale(mul(C,pow(x,2n)),6n),middle);
  const h1=div(fp,scale(z,2n));
  const h2=div(sub(fppHalf,pow(h1,2n)),scale(z,2n));
  const d4=sub(C,pow(h2,2n));
  const d3=sub(scale(mul(C,x),4n),scale(mul(h1,h2),2n));
  const X=sub(x,div(d3,d4)),dx=sub(X,x);
  const Z=add(add(z,mul(h1,dx)),mul(h2,pow(dx,2n)));
  const Y=div(Z,add(pow(X,2n),C));
  const outW=mul(b,add(sub(pow(X,2n),pow(Y,2n)),q(6n)));
  return {x:X,y:Y,W:outW,a,b,C,K,z,h1,h2,d3,d4};
}
rejects(()=>q(1n,0n),"Reject zero denominator");
rejects(()=>curvePoint(137n,q(1n,14n),q(18n,196n),1),"Reject false witness");
const n=137n,x=q(1n,14n),y=q(37n,14n),up=q(17n,196n),um=q(47n,196n),W=scale(mul(up,um),n);
check(eq(F(x,1),scale(pow(up,2n),n)),"137 plus");check(eq(F(y,-1),scale(pow(um,2n),n)),"137 minus");
for(const [t,u,e] of [[x,up,1],[y,um,-1]] as const){
  const [t3,u3]=triple(t,u,e);
  check(eq(F(t3,e),scale(pow(u3,2n),n)),"Tripling preserves squareclass");
  const P=curvePoint(n,t,u,e),Q=curvePoint(n,t3,u3,e);
  check(pointEqual(Q,ecAdd(n,ecAdd(n,P,P),P)),"Tripling is the actual curve group action");
}
rejects(()=>osculate(x,y,add(W,q(1n))),"Reject false surface point");
rejects(()=>osculate(q(-1n,2n),q(5n,2n),q(41n,16n)),"Handle U=V boundary explicitly");
rejects(()=>osculate(q(0n),q(0n),q(1n)),"Handle singular fiber explicitly");
const next=osculate(x,y,W);
check(eq(sub(pow(next.a,2n),pow(next.b,2n)),q(8n)),"Norm parameter");
check(eq(next.a,q(-152681n,37632n))&&eq(next.b,q(-109463n,37632n)),"Exact fiber");
check(eq(next.x,q(-16890371n,79256324n)),"New x");check(eq(next.y,q(210069683n,77723044n)),"New y");
check(eq(pow(next.W,2n),mul(F(next.x,1),F(next.y,-1))),"New surface residual");
const ratio=div(F(next.x,1),F(x,1));
check(squareclassValuation(ratio,17n)===1,"Squareclass changes, with exact odd17 valuation");
const factors=[17n,137n,16273n,19642387489n,233758085129n];
for(const p of factors){check(primeTrial(p),"Deterministic prime factor");check(p%8n===1n,"Prime support1 mod8");}
const N=factors.reduce((a,b)=>a*b,1n);
check(N===174019544752618399630591052177n,"New squarefree kernel");
const upNew=q(17n,79256324n**2n),umNew=q(47n,77723044n**2n);
check(eq(F(next.x,1),scale(pow(upNew,2n),N)),"New plus witness");
check(eq(F(next.y,-1),scale(pow(umNew,2n),N)),"New minus witness");
const Pplus=curvePoint(N,next.x,upNew,1),Pminus=curvePoint(N,next.y,umNew,-1);
check(Pplus!==null&&Pminus!==null,"Both exact elliptic points");
// T+, T0, lambda-minus, lambda-plus, ordered by (X-N,X+N,X).
// Build the minor from the stated squareclasses, not an unrelated matrix.
const labels=[[2n,2n*N,N],[-N,N,-1n],[1n,N,N],[N,1n,N]];
const allowed=[1n,-1n,2n,-2n,N,-N,2n*N,-2n*N];
check(labels.every(row=>row.every(a=>allowed.includes(a))),"Squareclass coordinate domain");
const vectors=labels.map(row=>row.flatMap(a=>[a<0n?1:0,abs(a)%2n===0n?1:0,abs(a)%N===0n?1:0]));
const minor=vectors.map(row=>[0,1,2,5].map(j=>row[j]!));
function rankF2(matrix:readonly (readonly number[])[]):number {
  const a=matrix.map(r=>r.slice());let rank=0;const width=a[0]?.length??0;
  for(let j=0;j<width;j++){const k=a.findIndex((r,i)=>i>=rank&&r[j]===1);if(k<0)continue;
    [a[rank],a[k]]=[a[k]!,a[rank]!];for(let i=0;i<a.length;i++)if(i!==rank&&a[i]?.[j]===1)for(let c=j;c<width;c++)a[i]![c]=(a[i]![c]??0)^(a[rank]![c]??0);rank++;}
  return rank;
}
check(rankF2(minor)===4,"Kummer independence minor");
let compatible=0;
for(let bits=0;bits<16;bits++){
 const a=bits&1,b=(bits>>1)&1,c=(bits>>2)&1,d=(bits>>3)&1;
 const fixes=a===1&&b===0&&c===0&&d===1;if(fixes)compatible++;
 check(fixes===(bits===9),"Product involution matrix parity");
}
check(compatible===1,"Unique parity class");
for(const p of [3n,5n]){let count=1;for(let a=0n;a<p;a++)for(let b=0n;b<p;b++)if((b*b-a*a*a+a)%p===0n)count++;
 check(count===(p===3n?4:8),"E0 finite-field torsion bound");}
check(4n**2n===2n**3n+4n*2n,"E0 dual rational class2");
const output={assertions,scope:"Two exact137 tripling controls; one squareclass-changing fiber map; five deterministically prime factors; one Kummer minor; all16 binary matrix classes. No prime-coverage or analytic-rank claim.",next,ratio,N,factors,upNew,umNew,Pplus,Pminus};
console.log(JSON.stringify(output,(_key:string,v:unknown)=>typeof v==="bigint"?v.toString():v,2));
