/** Exact F13 certificate. A failed inverse throws; no pole is silently skipped. */
export {};
type S = readonly [bigint,bigint,bigint];
type K = readonly [bigint,bigint];
type E = readonly [K,K] | null;
const modulus=13n;
const m=(a:bigint):bigint=>(a%modulus+modulus)%modulus;
function pw(a:bigint,n:bigint):bigint { let r=1n;for(let i=0n;i<n;i++)r=m(r*a);return r; }
function inv(a:bigint):bigint { if(m(a)===0n)throw new RangeError('Nonunit denominator');return pw(m(a),11n); }
const f=(t:bigint,e:bigint):bigint=>m(t**4n+6n*e*t*t+1n);
const character=(a:bigint):bigint=>pw(a,6n);
const key=(s:S):string=>s.join(',');
const same=(a:S,b:S):boolean=>key(a)===key(b);
function onSurface(s:S):boolean { return m(s[2]*s[2]-f(s[0],1n)*f(s[1],-1n))===0n; }
function requireSurface(s:S):void { if(!onSurface(s))throw new RangeError('Not a surface point'); }
function triple(s:S,side:0|1):S {
 requireSurface(s);const t=s[side],e=side===0?1n:-1n;
 const A=t*(t**8n-6n*t**4n-24n*e*t*t-3n);
 const D=3n*t**8n+24n*e*t**6n+6n*t**4n-1n;
 const H=t**16n+24n*e*t**14n+28n*t**12n+168n*e*t**10n+582n*t**8n+168n*e*t**6n+28n*t**4n+24n*e*t*t+1n;
 const tt=m(A*inv(D)),ww=m(s[2]*H*inv(D)**2n);
 return side===0?[tt,s[1],ww]:[s[0],tt,ww];
}
function fiber(s:S):readonly [bigint,bigint,bigint,bigint] {
 const [x,y]=s, gap=m(x*x-y*y+6n);
 const C=m((x*x*y*y+1n)*inv(gap)),K=m(6n*C-1n),B=m(C*C+K);
 return [C,K,B,gap];
}
function phiOriginal(s:S):S {
 requireSurface(s);const[x,y,w]=s,[C,K,B,gap]=fiber(s);
 if(m(C*K*w)===0n)throw new RangeError('Singular reduction in original chart');
 const z=m(y*(x*x+C));const h1=m((4n*C*x**3n+2n*B*x)*inv(2n*z));
 const h2=m((6n*C*x*x+B-h1*h1)*inv(2n*z));
 const delta=m(-(4n*C*x-2n*h1*h2)*inv(C-h2*h2));
 const xx=m(x+delta),zz=m(z+h1*delta+h2*delta*delta),yy=m(zz*inv(xx*xx+C));
 return [xx,yy,m(w*(xx*xx-yy*yy+6n)*inv(gap))];
}
function phiCancelled(s:S):S {
 requireSurface(s);const[x,y,w]=s,[C,K,B,gap]=fiber(s);
 const D=3n*C*x**8n+4n*B*x**6n+6n*C*K*x**4n-C*K*K;
 const A=-x*(C*x**8n-6n*C*K*x**4n-4n*B*K*x*x-3n*C*K*K);
 const xx=m(A*inv(D));
 const H=C*C*x**16n+4n*C*B*x**14n+28n*C*C*K*x**12n+28n*C*B*K*x**10n+(6n*C*C*K*K+16n*B*B*K)*x**8n+28n*C*B*K*K*x**6n+28n*C*C*K**3n*x**4n+4n*C*B*K**3n*x*x+C*C*K**4n;
 const yy=m(y*(x*x+C)*H*inv(D)**2n*inv(xx*xx+C));
 return [xx,yy,m(w*(xx*xx-yy*yy+6n)*inv(gap))];
}
const names=['X','Y','Phi','invertX','invertY','negX','negY','negW'] as const;
type Name=typeof names[number];
function act(s:S,name:Name):S {
 requireSurface(s);const[x,y,w]=s;
 switch(name) {
 case 'X':return triple(s,0);case 'Y':return triple(s,1);case 'Phi':return phiOriginal(s);
 case 'invertX':return [inv(x),y,m(w*inv(x)**2n)];
 case 'invertY':return [x,inv(y),m(w*inv(y)**2n)];
 case 'negX':return [m(-x),y,w];case 'negY':return [x,m(-y),w];case 'negW':return [x,y,m(-w)];
 }
}
const kk=(a:bigint,b=0n):K=>[m(a),m(b)];
const ka=(u:K,v:K):K=>kk(u[0]+v[0],u[1]+v[1]);
const kn=(u:K):K=>kk(-u[0],-u[1]);
const ks=(u:K,v:K):K=>ka(u,kn(v));
const km=(u:K,v:K):K=>kk(u[0]*v[0]+7n*u[1]*v[1],u[0]*v[1]+u[1]*v[0]);
const ki=(u:K):K=>{const n=inv(u[0]*u[0]-7n*u[1]*u[1]);return kk(u[0]*n,-u[1]*n);};
const kd=(u:K,v:K):K=>km(u,ki(v));
const ke=(u:K,v:K):boolean=>u[0]===v[0]&&u[1]===v[1];
function ea(p:E,q:E):E {
 if(p===null)return q;if(q===null)return p;
 const[x,y]=p,[xx,yy]=q;
 if(ke(x,xx)&&ke(y,kn(yy)))return null;
 const slope=ke(x,xx)?kd(ks(km(kk(3n),km(x,x)),kk(1n)),km(kk(2n),y)):kd(ks(yy,y),ks(xx,x));
 const nx=ks(ks(km(slope,slope),x),xx);
 return[nx,ks(km(slope,ks(x,nx)),y)];
}
function quarticToE(t:bigint,e:bigint,c:bigint):E {
 const r=kk(0n,c);
 return[kd(ka(r,kk(1n+e*t*t)),kk(2n*t*t)),kd(ka(r,kk(1n+3n*e*t*t)),kk(2n*t**3n))];
}
function eToQuartic(p:E,e:bigint):readonly [bigint,bigint] {
 if(p===null)throw new RangeError('Elliptic point at infinity outside chart');
 const[u,v]=p,t=kd(ka(u,kk(e)),v),r=ks(km(ks(km(kk(2n),u),kk(e)),km(t,t)),kk(1n));
 if(t[1]!==0n||r[0]!==0n)throw new Error('Failed descent to the base field');
 return [t[0],r[1]];
}
function shear(s:S):S {
 requireSurface(s);const[x,y,w]=s;
 let c:bigint|undefined;
 for(let a=1n;a<13n;a++)if(m(7n*a*a)===f(x,1n)){c=a;break;}
 if(c===undefined)throw new RangeError('Expected nonsquare twist class');
 const d=m(w*inv(7n*c)),p=quarticToE(x,1n,c),q=quarticToE(y,-1n,d),q2=ea(q,q);
 if(q2===null)throw new Error('Unexpected torsion chart');
 const [xx,cc]=eToQuartic(ea(p,[q2[0],kn(q2[1])]),1n);
 return [xx,y,m(7n*cc*d)];
}
let checks=0;
function check(ok:boolean,label:string):void { checks++;if(!ok)throw new Error(label); }
function rejects(fn:()=>unknown,label:string):void {let threw=false;try{fn();}catch{threw=true;}check(threw,label);}
check(character(7n)===12n,'7 is nonsquare');
check(m(-1n)===12n&&m(14n)===1n,'canonical residues');
rejects(()=>inv(0n),'zero division rejected');rejects(()=>act([1n,1n,1n],'X'),'invalid input rejected');
check(ke(km(kk(3n,4n),ki(kk(3n,4n))),kk(1n)),'quadratic-field inverse');
const omega:S[]=[];
for(let x=0n;x<13n;x++)for(let y=0n;y<13n;y++)for(let w=0n;w<13n;w++){
 const s:S=[x,y,w],u=m(x*x-1n),v=m(y*y+1n);
 if(onSurface(s)&&character(f(x,1n))===12n&&character(f(y,-1n))===12n&&m(u*v)===0n&&(u!==0n||v!==0n))omega.push(s);
}
check(omega.length===64,'exact Omega population');const omegaKeys=new Set(omega.map(key));
const transitions=omega.map(s=>({point:s,images:names.map(name=>({name,image:act(s,name)}))}));
check(transitions.every(r=>r.images.every(j=>omegaKeys.has(key(j.image)))),'all 512 transitions close, without a failed inverse');
check(omega.every(s=>same(phiOriginal(s),phiCancelled(s))),'original and cancelled charts agree on all Omega');
check(omega.every(s=>(['invertX','invertY','negX','negY','negW'] as const).every(name=>same(act(act(s,name),name),s))),'involutions checked');
const seed:S=[1n,11n,3n];check(omegaKeys.has(key(seed)),'seed is in Omega');
const orbit=new Map<string,{point:S;word:Name[]}>([[key(seed),{point:seed,word:[]}]]);
const queue:S[]=[seed];
for(let i=0;i<queue.length;i++){
 const s=queue[i];if(s===undefined)throw new Error('Queue boundary');
 const source=orbit.get(key(s));if(source===undefined)throw new Error('Missing orbit source');
 for(const name of ['X','Y','Phi'] as const){const out=act(s,name);if(!orbit.has(key(out))){orbit.set(key(out),{point:out,word:[...source.word,name]});queue.push(out);}}
}
check(orbit.size===32,'complete three-generator orbit');
check([...orbit.values()].every(r=>character(f(r.point[0],1n))===12n),'all orbit values are nonsquares');
check(character(257n)===1n&&character(313n)===1n,'target characters are excluded from restricted orbit');
const pY=act(seed,'Y'),pH=shear(pY),pPhi=phiCancelled(pH);
check(same(pY,[1n,9n,12n]),'Y residue');check(same(pH,[11n,9n,6n]),'shear residue');
check(same(pPhi,[5n,12n,9n]),'escaped residue');
check([seed,pY,pH,pPhi].every(onSurface),'all word points lie on S');
check(fiber(pH)[0]===0n,'escape passes through C=0 reduction');
rejects(()=>phiOriginal(pH),'old chart genuinely cannot certify this reduction');
check(pPhi[0]===m(-(inv(pH[0])**3n))&&pPhi[1]===m(-(pH[0]**4n)*pH[1]),'cancelled C=0 formulas');
check(character(f(pPhi[0],1n))===1n&&f(pPhi[0],1n)===9n,'quadratic character changes');
console.log(JSON.stringify({status:'completed exact finite certificates',checks,modulus:'13',omega_size:omega.length,transition_count:omega.length*names.length,orbit_size:orbit.size,orbit:[...orbit.values()],escape:[seed,pY,pH,pPhi],omega_transitions:transitions,scope:'Finite closure plus an exact residue escape; the rational-lifting proof is in RESEARCH.md.'},(_key:string,value:unknown)=>typeof value==='bigint'?value.toString():value,2));
