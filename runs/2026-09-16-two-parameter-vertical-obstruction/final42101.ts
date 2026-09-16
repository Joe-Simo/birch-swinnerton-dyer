type Pair = readonly [bigint,bigint];
type Point = readonly [Pair,Pair] | null;
const p=42101n,d0=137n,GM=214200,GN=1713600;
const mod=(a:bigint)=>{const r=a%p;return r<0n?r+p:r};
function powm(a:bigint,n:bigint){let x=mod(a),r=1n,k=n;while(k){if(k&1n)r=mod(r*x);x=mod(x*x);k>>=1n;}return r;}
function inv(a:bigint){let t=0n,nt=1n,r=p,nr=mod(a);while(nr){const q=r/nr;[t,nt]=[nt,t-q*nt];[r,nr]=[nr,r-q*nr];}if(r!==1n)throw new Error('nonunit');return mod(t);}
const leg=(a:bigint)=>{const x=mod(a);return x===0n?0:(powm(x,(p-1n)/2n)===1n?1:-1);};
const qadd=(x:Pair,y:Pair):Pair=>[mod(x[0]+y[0]),mod(x[1]+y[1])];
const qneg=(x:Pair):Pair=>[mod(-x[0]),mod(-x[1])];
const qsub=(x:Pair,y:Pair):Pair=>qadd(x,qneg(y));
const qmul=(x:Pair,y:Pair,d:bigint):Pair=>[mod(x[0]*y[0]+d*x[1]*y[1]),mod(x[0]*y[1]+x[1]*y[0])];
function qinv(x:Pair,d:bigint):Pair{const z=inv(mod(x[0]*x[0]-d*x[1]*x[1]));return[mod(x[0]*z),mod(-x[1]*z)];}
const qdiv=(x:Pair,y:Pair,d:bigint)=>qmul(x,qinv(y,d),d);
const eq=(x:Pair,y:Pair)=>x[0]===y[0]&&x[1]===y[1];
function eadd(P:Point,Q:Point,d:bigint):Point{if(P===null)return Q;if(Q===null)return P;const[x1,y1]=P,[x2,y2]=Q;if(eq(x1,x2)&&eq(qadd(y1,y2),[0n,0n]))return null;let l:Pair;if(eq(x1,x2)&&eq(y1,y2)){if(eq(y1,[0n,0n]))return null;l=qdiv(qsub(qmul([3n,0n],qmul(x1,x1,d),d),[1n,0n]),qmul([2n,0n],y1,d),d);}else l=qdiv(qsub(y2,y1),qsub(x2,x1),d);const x3=qsub(qsub(qmul(l,l,d),x1),x2);return[x3,qsub(qmul(l,qsub(x1,x3),d),y1)];}
const eneg=(P:Point):Point=>P===null?null:[P[0],qneg(P[1])];
function emul(n:number,P:Point,d:bigint):Point{if(n<0)return emul(-n,eneg(P),d);let R:Point=null,A=P,k=n;while(k){if(k&1)R=eadd(R,A,d);A=eadd(A,A,d);k=Math.floor(k/2);}return R;}
function seed():readonly[Point,Point]{const P:Point=[[mod(197n*inv(2n)),mod(17n*inv(2n))],[mod(1393n),mod(119n)]];const Q:Point=[[mod(-1173n*inv(2738n)),mod(47n*inv(2738n))],[mod(-27377n*inv(50653n)),mod(329n*inv(50653n))]];return[P,Q];}
function etoq(P:Point,e:bigint,d:bigint){if(P===null)throw new Error('inf');const[u,v]=P,t=qdiv(qadd(u,[e,0n]),v,d),r=qsub(qmul(qsub(qmul([2n,0n],u,d),[e,0n]),qmul(t,t,d),d),[1n,0n]);if(t[1]!==0n)throw new Error('descent');return{t:t[0],r};}
function qtoe(t:bigint,r:Pair,e:bigint,d:bigint):Point{const T:Pair=[t,0n],tt=qmul(T,T,d);return[qdiv(qadd(qadd(r,[1n,0n]),qmul([e,0n],tt,d)),qmul([2n,0n],tt,d),d),qdiv(qadd(qadd(r,[1n,0n]),qmul([3n*e,0n],tt,d)),qmul([2n,0n],qmul(tt,T,d),d),d)];}
const fp=(t:bigint)=>mod(t**4n+6n*t*t+1n);
function phi(x:bigint,y:bigint,w:bigint){const gap=mod(x*x-y*y+6n);if(gap===0n)throw new Error('gap');const c=mod((x*x*y*y+1n)*inv(gap)),k=mod(6n*c-1n),a=c,b=mod(c*c+k),z=mod(y*(x*x+c));if(z===0n)throw new Error('z');const f1=mod(4n*a*x**3n+2n*b*x),f2=mod(12n*a*x*x+2n*b),f3=mod(24n*a*x);const h1=mod(f1*inv(2n*z)),h2=mod((f2*inv(2n)-h1*h1)*inv(2n*z)),r3=mod(f3*inv(6n)-2n*h1*h2),r4=mod(c-h2*h2);if(r4===0n)throw new Error('r4');const dx=mod(-r3*inv(r4)),xo=mod(x+dx),zo=mod(z+h1*dx+h2*dx*dx),den=mod(xo*xo+c);if(den===0n)throw new Error('return');const yo=mod(zo*inv(den)),wo=mod(w*(xo*xo-yo*yo+6n)*inv(gap));return{xo,yo,wo};}
function firstStage(m:number){const[P,Q]=seed(),Pm=eadd(P,emul(-2*m,Q,d0),d0),a=etoq(Pm,1n,d0),b=etoq(Q,-1n,d0),W=qmul(a.r,b.r,d0);if(W[1]!==0n)throw new Error('W');return phi(a.t,b.t,W[0]);}
function lift(x:bigint,y:bigint,w:bigint){const d=fp(x);if(d!==23163n||leg(d)!==-1)throw new Error('unexpected lift');const rp:Pair=[0n,1n],rm:Pair=[0n,mod(w*inv(d))];return{d,P:qtoe(x,rp,1n,d),Q:qtoe(y,rm,-1n,d)};}
const states:[[number,number],[number,number],[number,number],[number,number],[number,number],[number,number],[number,number],[number,number]]=[[85172,203272],[85172,631672],[85172,1060072],[85172,1488472],[192272,203272],[192272,631672],[192272,1060072],[192272,1488472]];
const out=[] as Array<{m:number,n:number,x:string,F:string,character:number,target:number}>;
for(const[m,n] of states){const[P,Q]=seed();if(emul(-2*GM,Q,d0)!==null)throw new Error('M period');const a=firstStage(m),L=lift(a.xo,a.yo,a.wo);if(emul(-2*GN,L.P,L.d)!==null)throw new Error('N period');const Qn=eadd(L.Q,emul(-2*n,L.P,L.d),L.d),xs=etoq(L.P,1n,L.d),ys=etoq(Qn,-1n,L.d),W=qmul(xs.r,ys.r,L.d);if(W[1]!==0n)throw new Error('W2');const z=phi(xs.t,ys.t,W[0]),F=fp(z.xo),c=leg(F),target=leg(313n);if(z.xo!==15355n||F!==38394n||c!==1||target!==-1)throw new Error('final mismatch');out.push({m,n,x:z.xo.toString(),F:F.toString(),character:c,target});}
console.log(JSON.stringify({status:'passed',prime:p.toString(),states:out},null,2));
