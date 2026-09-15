/** Narrow exact-rational certificate, not a general-purpose interval library.
 * Every endpoint is an integer multiple of 2^-80; all operations round outward.
 * The analytic integration/tail proof and elementary exp/log bounds are in CHECKPOINT.md.
 */
type Ball = Readonly<{ lo: bigint; hi: bigint }>;
const SCALE = 1n << 80n;
const one: Ball = { lo: SCALE, hi: SCALE };
const zero: Ball = { lo: 0n, hi: 0n };
let checks = 0;
function check(ok: boolean, label: string): void {
  checks += 1;
  if (!ok) throw new Error(label);
}
function floorDiv(a: bigint, b: bigint): bigint {
  if (b <= 0n) throw new RangeError('positive divisor required');
  const q = a / b;
  return a < 0n && a % b !== 0n ? q - 1n : q;
}
function ceilDiv(a: bigint, b: bigint): bigint { return -floorDiv(-a, b); }
function min(a: bigint, b: bigint): bigint { return a < b ? a : b; }
function max(a: bigint, b: bigint): bigint { return a > b ? a : b; }
function num(n: bigint): Ball { return { lo: n*SCALE, hi: n*SCALE }; }
function ratio(n: bigint, d: bigint): Ball { return { lo: floorDiv(n*SCALE,d), hi: ceilDiv(n*SCALE,d) }; }
function add(a: Ball,b: Ball): Ball { return { lo:a.lo+b.lo, hi:a.hi+b.hi }; }
function sub(a: Ball,b: Ball): Ball { return { lo:a.lo-b.hi, hi:a.hi-b.lo }; }
function mul(a: Ball,b: Ball): Ball {
  const p=[a.lo*b.lo,a.lo*b.hi,a.hi*b.lo,a.hi*b.hi];
  let lo=p[0]!,hi=lo;
  for (const v of p) {lo=min(lo,v);hi=max(hi,v);}
  return {lo:floorDiv(lo,SCALE),hi:ceilDiv(hi,SCALE)};
}
function div(a: Ball,b: Ball): Ball {
  if (b.lo<=0n) throw new RangeError('positive interval denominator required');
  return mul(a,{lo:floorDiv(SCALE*SCALE,b.hi),hi:ceilDiv(SCALE*SCALE,b.lo)});
}
function power(a:Ball,k:number):Ball {
  if(!Number.isSafeInteger(k)||k<0) throw new RangeError('nonnegative integer exponent required');
  let out=one,base=a;
  for(let e=k;e>0;e=Math.floor(e/2)){if(e%2===1)out=mul(out,base);base=mul(base,base);}
  return out;
}
function isqrt(n:bigint):bigint {
  if(n<0n)throw new RangeError('negative square root');
  let lo=0n,hi=n+1n;
  while(hi-lo>1n){const m=(lo+hi)/2n;if(m*m<=n)lo=m;else hi=m;}
  return lo;
}
function sqrt32():Ball {const k=isqrt(32n*SCALE*SCALE);return{lo:k,hi:k+1n};}
function atanReciprocal(d:bigint):Ball {
  const x=ratio(1n,d),x2=mul(x,x);let term=x,sum=zero;
  for(let j=0;j<24;j++){
    const v=div(term,num(BigInt(2*j+1)));sum=j%2===0?add(sum,v):sub(sum,v);term=mul(term,x2);
  }
  // Alternating series: the next positive term bounds the omitted remainder.
  return add(sum,{lo:0n,hi:div(term,num(49n)).hi});
}
const pi=sub(mul(num(16n),atanReciprocal(5n)),mul(num(4n),atanReciprocal(239n)));
/** exp(-x) for x >= 0. Bernoulli-log bounds with m=2^24, then repeated squaring. */
function expMinus(x:Ball):Ball {
  if(x.lo<0n)throw new RangeError('expMinus domain');
  const endpoint=(u:bigint):Ball=>{
    if(u===0n)return one;
    // e>2 implies e^-u <2^-128 <2^-80 here.
    if(u>=128n*SCALE)return {lo:0n,hi:1n};
    const y=ratio(u,SCALE*(1n<<24n));
    let low=sub(one,y),high=div(one,add(one,y));
    for(let i=0;i<24;i++){low=mul(low,low);high=mul(high,high);}
    return {lo:low.lo,hi:high.hi};
  };
  return{lo:endpoint(x.hi).lo,hi:endpoint(x.lo).hi};
}
/** log(x) for x>=1; argument reduction and the positive atanh series. */
function logUnit(x:Ball):Ball {
  const y=div(sub(x,one),add(x,one)),y2=mul(y,y);let term=y,sum=zero;
  for(let k=0;k<24;k++){sum=add(sum,div(term,num(BigInt(2*k+1))));term=mul(term,y2);}
  const tail=div(mul(num(2n),term),mul(num(49n),sub(one,y2)));
  return add(mul(num(2n),sum),{lo:0n,hi:tail.hi});
}
const log2=logUnit(num(2n));
function logPoint(u:bigint):Ball {
  if(u<SCALE)throw new RangeError('logPoint domain');
  let k=0,den=1n;
  while(u>=2n*den*SCALE){den*=2n;k++;}
  return add(mul(num(BigInt(k)),log2),logUnit(ratio(u,den*SCALE)));
}
function log(a:Ball):Ball {return{lo:logPoint(a.lo).lo,hi:logPoint(a.hi).hi};}
function powMod(a:bigint,e:bigint,m:bigint):bigint {
  let r=1n,b=((a%m)+m)%m;
  while(e>0n){if(e%2n)r=r*b%m;b=b*b%m;e/=2n;}
  return r;
}
function isPrime(p:number):boolean {if(p<2)return false;for(let d=2;d*d<=p;d++)if(p%d===0)return false;return true;}
/** q prod(1-q^(4m))^2(1-q^(8m))^2, calculated in q^4 to avoid zero slots. */
function etaCoefficients(bound:number):bigint[] {
  const d=Math.floor((bound-1)/4),b=Array<bigint>(d+1).fill(0n);b[0]=1n;
  for(const step of[1,2])for(let e=step;e<=d;e+=step)for(let copy=0;copy<2;copy++)
    for(let j=d;j>=e;j--)b[j]=b[j]!-b[j-e]!;
  const out=Array<bigint>(bound+1).fill(0n);
  for(let j=0;j<=d;j++)out[4*j+1]=b[j]!;
  return out;
}
function twist(base:readonly bigint[],p:number,bound:number):bigint[] {
  if(!isPrime(p)||p%8!==1)throw new RangeError('registered prime family only');
  return base.slice(0,bound+1).map((a,n)=>{
    const s=powMod(BigInt(n),BigInt((p-1)/2),BigInt(p));
    return a*(s===0n?0n:s===1n?1n:-1n);
  });
}
function ternary(p:number,c:8|32):bigint {
  let count=0n;const nn=BigInt(p),by=isqrt(nn/2n),bz=isqrt(nn/BigInt(c));
  for(let y=-by;y<=by;y++)for(let z=-bz;z<=bz;z++){
    const a=nn-2n*y*y-BigInt(c)*z*z;if(a<0n)continue;
    const x=isqrt(a);if(x*x===a)count+=x===0n?1n:2n;
  }
  return count;
}
function encode(a:Ball){return{lo_scaled:a.lo.toString(),hi_scaled:a.hi.toString(),scale:SCALE.toString()};}
function decimalOuter(a:Ball,places=6){
  const den=10n**BigInt(places);const l=floorDiv(a.lo*den,SCALE),h=ceilDiv(a.hi*den,SCALE);
  const fmt=(v:bigint)=>{const s=v<0n?'-':'';v=v<0n?-v:v;return `${s}${v/den}.${(v%den).toString().padStart(places,'0')}`;};
  return[fmt(l),fmt(h)];
}
function integrate(p:number,base:readonly bigint[],subdivisions:number){
  const alpha=div(mul(num(2n),pi),mul(sqrt32(),num(BigInt(p))));
  const bound=16*p,coef=twist(base,p,bound);let total=zero,err=zero,A=1;
  const slabs=[];
  while(A<128*p){
    const B=2*A,K=Math.max(1,Math.floor((bound+A-1)/A)),width=ratio(BigInt(A),BigInt(subdivisions));let local=zero;
    for(let j=0;j<subdivisions;j++){
      const left=ratio(BigInt(A*(subdivisions+j)),BigInt(subdivisions));
      const right=ratio(BigInt(A*(subdivisions+j+1)),BigInt(subdivisions));
      const t={lo:left.lo,hi:right.hi},q=expMinus(mul(alpha,t));let f=num(coef[K]!);
      for(let n=K-1;n>=0;n--)f=add(mul(f,q),num(coef[n]!));
      local=add(local,mul(mul(num(2n),width),mul(power(log(t),2),f)));
    }
    const aA=mul(alpha,num(BigInt(A))),q=expMinus(aA);
    const tail=div(mul(mul(num(4n),power(log(num(BigInt(B))),2)),expMinus(mul(aA,num(BigInt(K+1))))),mul(alpha,sub(one,q)));
    total=add(total,local);err=add(err,tail);slabs.push({A,B,K,integral:encode(local),tail:encode(tail)});A=B;
  }
  const T=num(BigInt(A)),q=expMinus(mul(alpha,T));
  const tail=mul(div(mul(num(4n),q),sub(one,q)),add(add(div(power(T,2),alpha),div(mul(num(2n),T),power(alpha,2))),div(num(2n),power(alpha,3))));
  err=add(err,tail);const result=add(total,{lo:-err.hi,hi:err.hi}),l2=mul(alpha,result);
  const ta=ternary(p,8),tb=ternary(p,32);check(2n*tb===ta,`exact central coefficient at ${p}`);
  check(result.lo>0n,`completed second derivative positive at ${p}`);
  for(let n=1;n<=bound;n++)check(coef[n]!*coef[n]!<=4n*BigInt(n)*BigInt(n),`finite Hasse bound ${p},${n}`);
  return{p,N:32*p*p,subdivisions,coefficient_bound:bound,T:A,A:ta.toString(),B:tb.toString(),central_coefficient:'0',alpha:encode(alpha),Lambda2:encode(result),L2:encode(l2),L2_decimal_outer:decimalOuter(l2),error_upper:encode(err),slabs,coefficients:coef.map(String)};
}
check(floorDiv(-1n,3n)===-1n&&ceilDiv(-1n,3n)===0n,'signed outward division');
check(pi.lo>ratio(31415926n,10000000n).hi&&pi.hi<ratio(31415927n,10000000n).lo,'Machin pi enclosure');
check(log2.lo>ratio(693147n,1000000n).hi&&log2.hi<ratio(693148n,1000000n).lo,'log2 enclosure');
check(logPoint(SCALE).lo===0n&&logPoint(SCALE).hi===0n,'log1');
check(expMinus(zero).lo===SCALE&&expMinus(zero).hi===SCALE,'exp0');
check(expMinus(num(1n)).lo>ratio(3678n,10000n).hi&&expMinus(num(1n)).hi<ratio(368n,1000n).lo,'exponential elementary bounds');
check(sqrt32().lo**2n<=32n*SCALE*SCALE&&sqrt32().hi**2n>=32n*SCALE*SCALE,'integer sqrt enclosure');
check(120n*239n-119n===119n*239n+120n,'Machin tangent identity');
function rejects(action:()=>unknown,label:string):void {
  let rejected=false;try{action();}catch{rejected=true;}check(rejected,label);
}
rejects(()=>floorDiv(1n,0n),'zero denominator rejected');
rejects(()=>div(one,{lo:-1n,hi:1n}),'interval containing zero rejected');
rejects(()=>expMinus(num(-1n)),'negative exponential argument rejected');
rejects(()=>logPoint(0n),'unsupported logarithm input rejected');
rejects(()=>power(one,-1),'negative integer power rejected');
rejects(()=>twist([0n,1n],9,1),'composite twist rejected');
check(2n*ternary(17,32)!==ternary(17,8),'nonzero central-value negative control');
const primes=[41,137,257,313,353,457,761],base=etaCoefficients(16*761);
check(base[1]===1n&&base[5]===-2n&&base[9]===-3n&&base[13]===6n&&base[17]===2n,'Tunnell base coefficient prefix');
const results=primes.map(p=>integrate(p,base,32));
console.log(JSON.stringify({status:'completed exact-rational enclosures; known finite cases only',checks,scale:SCALE.toString(),precision_bits:80,exp_power:24,atan_terms:24,log_terms:24,pi:encode(pi),results},null,2));
