type F2 = Readonly<{ a: number; b: number; p: number }>;
type Point = Readonly<{ x: F2; y: F2 }> | null;

function assert(condition: boolean, message: string): asserts condition {
  if (!condition) throw new Error(message);
}
function mod(a: number, p: number): number { const r = a % p; return r < 0 ? r + p : r; }
function inv(a: number, p: number): number {
  let t = 0, nt = 1, r = p, nr = mod(a, p);
  while (nr !== 0) { const q = Math.floor(r / nr); [t, nt] = [nt, t - q * nt]; [r, nr] = [nr, r - q * nr]; }
  if (r !== 1) throw new Error(`nonunit ${a} mod ${p}`); return mod(t, p);
}
function f2(a: number, b: number, p: number): F2 { return { a: mod(a,p), b: mod(b,p), p }; }
function eq(x:F2,y:F2):boolean{return x.p===y.p&&x.a===y.a&&x.b===y.b;}
function add2(x:F2,y:F2):F2{return f2(x.a+y.a,x.b+y.b,x.p);}
function neg2(x:F2):F2{return f2(-x.a,-x.b,x.p);}
function sub2(x:F2,y:F2):F2{return add2(x,neg2(y));}
function mul2(x:F2,y:F2):F2{const d=mod(137,x.p);return f2(x.a*y.a+d*x.b*y.b,x.a*y.b+x.b*y.a,x.p);}
function inv2(x:F2):F2{const d=mod(137,x.p),den=mod(x.a*x.a-d*x.b*x.b,x.p),di=inv(den,x.p);return f2(x.a*di,-x.b*di,x.p);}
function div2(x:F2,y:F2):F2{return mul2(x,inv2(y));}
function c(n:number,p:number):F2{return f2(n,0,p);}
function scale(n:number,x:F2):F2{return mul2(c(n,x.p),x);}
function pneg(P:Point):Point{return P===null?null:{x:P.x,y:neg2(P.y)};}
function peq(P:Point,Q:Point):boolean{if(P===null||Q===null)return P===Q;return eq(P.x,Q.x)&&eq(P.y,Q.y);}
function padd(P:Point,Q:Point,p:number):Point{
  if(P===null)return Q;if(Q===null)return P;if(eq(P.x,Q.x)&&eq(P.y,neg2(Q.y)))return null;
  let l:F2;
  if(peq(P,Q)){if(eq(P.y,c(0,p)))return null;l=div2(sub2(scale(3,mul2(P.x,P.x)),c(1,p)),scale(2,P.y));}
  else l=div2(sub2(Q.y,P.y),sub2(Q.x,P.x));
  const x3=sub2(sub2(mul2(l,l),P.x),Q.x);return {x:x3,y:sub2(mul2(l,sub2(P.x,x3)),P.y)};
}
function pmul(n:number,P:Point,p:number):Point{if(n<0)return pmul(-n,pneg(P),p);let k=n,A=P,R:Point=null;while(k>0){if((k&1)===1)R=padd(R,A,p);A=padd(A,A,p);k=Math.floor(k/2);}return R;}
function order(P:Point,p:number):number{let R:Point=null;for(let n=1;n<=10000;n+=1){R=padd(R,P,p);if(R===null)return n;}throw new Error("order limit");}
function seed(p:number):readonly[Point,Point]{
  const i2=inv(2,p),dx=inv(mod(2738,p),p),dy=inv(mod(50653,p),p);
  return [{x:f2(197*i2,17*i2,p),y:f2(1393,119,p)},{x:f2(-1173*dx,47*dx,p),y:f2(-27377*dy,329*dy,p)}];
}
function qt(P:Point,e:1|-1,p:number):number{if(P===null)return 0;if(eq(P.y,c(0,p)))throw new Error("branch chart");const t=div2(add2(P.x,c(e,p)),P.y);assert(t.b===0,`non-base coordinate mod ${p}`);return t.a;}
function mm(v:readonly number[],p:number):number{let o=1;for(const x of v)o=mod(o*mod(x,p),p);return o;}
function pw(b:number,e:number,p:number):number{let x=mod(b,p),o=1,k=e;while(k>0){if((k&1)===1)o=mod(o*x,p);x=mod(x*x,p);k=Math.floor(k/2);}return o;}
function fp(t:number,p:number):number{return mod(pw(t,4,p)+6*mod(t*t,p)+1,p);}
function leg(a:number,p:number):-1|0|1{const x=mod(a,p);if(x===0)return 0;return pw(x,(p-1)/2,p)===1?1:-1;}
function phix(x:number,y:number,p:number):number{
  const gap=mod(x*x-y*y+6,p);assert(gap!==0,`zero gap mod ${p}`);const C=mod((x*x*y*y+1)*inv(gap,p),p);
  if(C===0){assert(x!==0,"zero x");return mod(-inv(mod(x**3,p),p),p);}
  const K=mod(6*C-1,p),a=C,b=mod(C*C+K,p),d=mod(C*K,p),x2=pw(x,2,p),x4=pw(x,4,p),x6=pw(x,6,p),x8=pw(x,8,p);
  const inn=mod(mm([a,a,x8],p)-6*mm([a,d,x4],p)-4*mm([b,d,x2],p)-3*mm([d,d],p),p),N=mod(-x*inn,p);
  const D0=mod(3*mm([a,a,x8],p)+4*mm([a,b,x6],p)+6*mm([a,d,x4],p)-mm([d,d],p),p);assert(D0!==0,"zero denominator");return mod(N*inv(D0,p),p);
}
let assertions=0;function check(x:boolean,m:string):void{assertions+=1;assert(x,m);}
{
  const p=47,[P,Q]=seed(p);check(order(Q,p)===4,"Q order mod47");
  for(const d of [1,3]){const Qd=pmul(d,Q,p);for(const parity of [0,1]){const Pm=padd(P,pmul(-2*parity,Qd,p),p),x=qt(Pm,1,p),y=qt(Qd,-1,p),xo=phix(x,y,p),fo=fp(xo,p);check(leg(fo,p)===1,`horizontal d=${d},m=${parity}`);check(fo!==0,"unit mod47");}}
  check(leg(257,p)===-1,"257 mod47");check(leg(313,p)===-1,"313 mod47");
}
{
  const p=13,[P,Q]=seed(p);check(order(P,p)===4,"P order mod13");
  for(const parity of [0,1]){const Qm=padd(Q,pmul(-2*parity,P,p),p),x=qt(P,1,p),y=qt(Qm,-1,p),xo=phix(x,y,p),fo=fp(xo,p);check(x===1,"vertical x");check(xo===12,"vertical output x");check(fo===8&&leg(fo,p)===-1,"vertical character");}
  check(leg(257,p)===1,"257 mod13");check(leg(313,p)===1,"313 mod13");
}
for(const p of [13,47]){
  const [P0,Q0]=seed(p),P1=padd(P0,pmul(-2,Q0,p),p),P2=padd(P1,pmul(-2,Q0,p),p),Q2=padd(Q0,pmul(2,P2,p),p),x=qt(P2,1,p),y=qt(Q2,-1,p),xo=phix(x,y,p),fo=fp(xo,p);
  if(p===13){check(x===7&&y===10&&xo===5&&fo===9,"mixed mod13");check(leg(fo,p)===1,"mixed char13");}
  else{check(x===37&&y===7&&xo===10&&fo===26,"mixed mod47");check(leg(fo,p)===-1,"mixed char47");}
}
console.log(JSON.stringify({status:"passed",assertions},null,2));
