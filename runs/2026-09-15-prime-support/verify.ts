/** H15: exact ramified local-ring cycle and an independent modular branch certificate. */
export {};
type R = readonly [bigint,bigint];
type E = readonly [R,R];
const p=137n,p2=p*p;
const mod=(a:bigint,n:bigint):bigint=>(a%n+n)%n;
function inv(a:bigint,n:bigint):bigint {
 let t=0n,u=1n,r=n,s=mod(a,n);
 while(s!==0n){const q=r/s;[t,u]=[u,t-q*u];[r,s]=[s,r-q*s];}
 if(r!==1n)throw new RangeError('Attempted nonunit inverse');
 return mod(t,n);
}
const rr=(a:bigint,b=0n):R=>[mod(a,p2),mod(b,p)];
const plus=(a:R,b:R):R=>rr(a[0]+b[0],a[1]+b[1]);
const neg=(a:R):R=>rr(-a[0],-a[1]);
const sub=(a:R,b:R):R=>plus(a,neg(b));
const times=(a:R,b:R):R=>rr(a[0]*b[0]+p*a[1]*b[1],a[0]*b[1]+a[1]*b[0]);
const scale=(a:R,n:bigint):R=>rr(a[0]*n,a[1]*n);
const ri=(a:R):R=>{const u=inv(a[0]*a[0]-p*a[1]*a[1],p2);return rr(a[0]*u,-a[1]*u);};
const div=(a:R,b:R):R=>times(a,ri(b));
const same=(a:R,b:R):boolean=>a[0]===b[0]&&a[1]===b[1];
const samePoint=(a:E,b:E):boolean=>same(a[0],b[0])&&same(a[1],b[1]);
const rational=(a:bigint,b=1n):R=>rr(a*inv(b,p2));
function onCurve(P:E):boolean {const[x,y]=P;return same(times(y,y),sub(times(times(x,x),x),x));}
function add(P:E,Q:E,doubling=false):E {
 const[x,y]=P,[u,v]=Q;
 const slope=doubling?div(sub(scale(times(x,x),3n),rr(1n)),scale(y,2n)):div(sub(v,y),sub(u,x));
 const nx=sub(sub(times(slope,slope),x),u);
 return[nx,sub(times(slope,sub(x,nx)),y)];
}
function quarticToE(t:R,e:bigint,c:R):E {
 const z=rr(0n,c[0]),tt=times(t,t);
 return[div(plus(plus(z,rr(1n)),scale(tt,e)),scale(tt,2n)),div(plus(plus(z,rr(1n)),scale(tt,3n*e)),scale(times(tt,t),2n))];
}
function fromE(P:E):readonly [bigint,bigint] {
 const[u,v]=P,t=div(plus(u,rr(1n)),v),z=sub(times(sub(scale(u,2n),rr(1n)),times(t,t)),rr(1n));
 if(t[1]!==0n||z[0]!==0n)throw new Error('Conjugation descent failed');
 return[t[0],z[1]];
}
function cappedVal(a:bigint):0|1|null {a=mod(a,p2);return a===0n?null:(a%p===0n?1:0);}
function phiResidue(x:bigint,c:bigint):readonly [bigint,bigint,bigint]|null {
 const k=mod(6n*c-1n,p),b=mod(c*c+k,p);
 const D=mod(3n*c*x**8n+4n*b*x**6n+6n*c*k*x**4n-c*k*k,p);
 if(D===0n)return null;
 const xx=mod(-x*(c*x**8n-6n*c*k*x**4n-4n*b*k*x*x-3n*c*k*k)*inv(D,p),p);
 return[xx,D,mod(xx*xx+c,p)];
}
type Row={m:number;x_mod_p2:bigint;r_coefficient:bigint;Fplus_valuation_capped:0|1|null;gap_valuation_capped:0|1|null;status:'retains'|'removes'|'exception';C_mod_p?:bigint;output_x?:bigint;map_denominator?:bigint;return_denominator?:bigint;output_Fplus?:bigint};
let checks=0;
function check(ok:boolean,label:string):void {checks++;if(!ok)throw new Error(label);}
function rejects(fn:()=>unknown,label:string):void {let failed=false;try{fn();}catch{failed=true;}check(failed,label);}
rejects(()=>inv(0n,p),'zero denominator rejected');rejects(()=>ri(rr(p)),'nonunit ring denominator rejected');
check(same(times(rr(0n,1n),rr(0n,1n)),rr(p)),'pi squared is137');
check(same(times(rr(p),rr(0n,1n)),rr(0n)),'pi cubed vanishes');
check(same(times(rr(3n,5n),ri(rr(3n,5n))),rr(1n)),'ring inverse identity');
const P0=quarticToE(rational(1n,14n),1n,rational(17n,196n));
const Q=quarticToE(rational(37n,14n),-1n,rational(47n,196n));
check(onCurve(P0)&&onCurve(Q),'seed points on E0 in ramified ring');
const doubleQ=add(Q,Q,true),step:E=[doubleQ[0],neg(doubleQ[1])];
check(onCurve(step),'translation step on E0');
const y=rational(37n,14n)[0];
const rows:Row[]=[];
let current=P0;
for(let m=0;m<274;m++){
 if(!onCurve(current))throw new Error(`Invalid state ${m}`);
 const[x,r]=fromE(current),fp=mod(x**4n+6n*x*x+1n,p2),gap=mod(x*x-y*y+6n,p2);
 const row:Row={m,x_mod_p2:x,r_coefficient:r,Fplus_valuation_capped:cappedVal(fp),gap_valuation_capped:cappedVal(gap),status:'exception'};
 if(row.gap_valuation_capped===0&&row.Fplus_valuation_capped===1)row.status='retains';
 else if(row.gap_valuation_capped===1){
  const numerator=mod(x*x*y*y+1n,p2);
  if(numerator%p!==0n)throw new Error('Division by137 is not exact');
  const c=mod((numerator/p)*inv(gap/p,p),p);row.C_mod_p=c;
  const output=phiResidue(mod(x,p),c);
  if(output!==null){
   const[xx,D,J]=output;row.output_x=xx;row.map_denominator=D;row.return_denominator=J;
   row.output_Fplus=mod(xx**4n+6n*xx*xx+1n,p);
   if(row.output_Fplus!==0n&&J!==0n)row.status='removes';
  }
 }
 rows.push(row);current=add(current,step);
}
check(samePoint(current,P0),'entire elliptic state closes after274 steps');
check(rows.filter(r=>r.status==='retains').length===136,'136 certified retention classes');
check(rows.filter(r=>r.status==='removes').length===128,'128 certified removal classes');
const exceptional=rows.filter(r=>r.status==='exception').map(r=>r.m);
check(exceptional.join(',')==='21,59,89,111,115,158,201,205,227,257','ten explicitly unresolved classes');
const first=rows[1];check(first!==undefined&&first.status==='removes'&&first.output_x===82n&&first.output_Fplus===51n,'m1 removes137');
check(rows.every(r=>r.status!=='retains'||r.m%2===0),'retention classes are even');
check(rows.every(r=>r.status!=='removes'||r.m%2===1),'removal classes are odd');

const removalCharacters=rows.filter(r=>r.status==='removes').map(r=>{if(r.output_Fplus===undefined)throw new Error('Missing local unit');return mod(r.output_Fplus**68n,p);});
check(removalCharacters.filter(c=>c===1n).length===86&&removalCharacters.filter(c=>c===136n).length===42,'both local unit squareclasses occur after removal');
check(mod(257n**68n,p)===1n&&mod(313n**68n,p)===1n,'neither target is excluded by the137 unit character');

// Polynomial operations over F11. Coefficients are ascending; no root sampling.
const ell=11n;
type Poly=bigint[];
function trim(a:Poly):Poly {const b=a.map(x=>mod(x,ell));while(b.length>1&&b[b.length-1]===0n)b.pop();return b;}
const coeff=(a:Poly,i:number):bigint=>a[i]??0n;
function padd(a:Poly,b:Poly):Poly {return trim(Array.from({length:Math.max(a.length,b.length)},(_,i)=>coeff(a,i)+coeff(b,i)));}
function pmul(a:Poly,b:Poly):Poly {const c=Array<bigint>(a.length+b.length-1).fill(0n);for(let i=0;i<a.length;i++)for(let j=0;j<b.length;j++)c[i+j]=coeff(c,i+j)+coeff(a,i)*coeff(b,j);return trim(c);}
function prem(a:Poly,b:Poly):Poly {
 let r=trim(a);b=trim(b);const leading=b[b.length-1];if(leading===undefined||leading===0n)throw new Error('Zero polynomial divisor');
 while(r.length>=b.length&&!(r.length===1&&r[0]===0n)){
  const j=r.length-b.length,q=mod(coeff(r,r.length-1)*inv(leading,ell),ell);
  for(let i=0;i<b.length;i++)r[i+j]=coeff(r,i+j)-q*coeff(b,i);
  r=trim(r);
 }
 return r;
}
function pgcd(a:Poly,b:Poly):Poly {a=trim(a);b=trim(b);while(!(b.length===1&&b[0]===0n)){const r=prem(a,b);a=b;b=r;}return a;}
function derivative(a:Poly):Poly {return trim(a.slice(1).map((x,i)=>BigInt(i+1)*x));}
const A:Poly=[0n,1102006668n,0n,6145143927n,0n,727141576n,0n,-52591504n];
const B:Poly=[-367335556n,0n,-2460543401n,0n,519995448n,0n,157774512n];
const a2=pmul(A,A),b2=pmul(B,B),G=padd(padd(pmul(a2,a2),pmul(a2,b2).map(x=>6n*x)),pmul(b2,b2));
const Fplus:Poly=[1n,0n,6n,0n,1n];
check(trim(A).length===8&&trim(B).length===7,'degree-seven rational map mod11');
check(pgcd(A,B).length===1,'map numerator and denominator coprime mod11');
check(G.length===29,'degree28 numerator retained mod11');
check(pgcd(G,derivative(G)).length===1,'degree28 numerator squarefree mod11');
check(prem(G,Fplus).every(x=>x===0n),'Fplus divides numerator mod11');
check(pgcd(G,B).length===1,'no branch cancellation with denominator mod11');
const finiteOrders=[3n,5n].map(q=>{let n=1;for(let x=0n;x<q;x++)for(let y=0n;y<q;y++)if(mod(y*y-x*x*x+137n**2n*x,q)===0n)n++;return{prime:q,order:n};});
check(finiteOrders.every(r=>r.order===4),'E137 reductions at3 and5 have order4');
console.log(JSON.stringify({status:'passed',assertions:checks,ring:'O_(Q137(sqrt137))/(sqrt137)^3',period:274,retains:136,removes:128,exceptions:exceptional,removal_unit_characters:{square:86,nonsquare:42},rows,polynomial_certificate_prime:11,finiteOrders,scope:'Exact local cycle and modular polynomial certificates; the infinite implications are proved separately.'},(_k:string,v:unknown)=>typeof v==='bigint'?v.toString():v,2));
