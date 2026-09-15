type Point = readonly [number,number] | null;
function assert(x:boolean,m:string):asserts x{if(!x)throw new Error(m)}
function mod(a:number,p:number):number{const r=a%p;return r<0?r+p:r}
function inv(a:number,p:number):number{let t=0,nt=1,r=p,nr=mod(a,p);while(nr){const q=Math.floor(r/nr);[t,nt]=[nt,t-q*nt];[r,nr]=[nr,r-q*nr]}if(r!==1)throw new Error('nonunit');return mod(t,p)}
function add(P:Point,Q:Point,p:number):Point{if(P===null)return Q;if(Q===null)return P;const[x1,y1]=P,[x2,y2]=Q;if(x1===x2&&mod(y1+y2,p)===0)return null;let l:number;if(x1===x2&&y1===y2){if(y1===0)return null;l=mod((3*x1*x1-1)*inv(2*y1,p),p)}else l=mod((y2-y1)*inv(x2-x1,p),p);const x3=mod(l*l-x1-x2,p);return[x3,mod(l*(x1-x3)-y1,p)]}
function neg(P:Point,p:number):Point{return P===null?null:[P[0],mod(-P[1],p)]}
function mul(n:number,P:Point,p:number):Point{if(n<0)return mul(-n,neg(P,p),p);let R:Point=null,A=P,k=n;while(k){if(k&1)R=add(R,A,p);A=add(A,A,p);k=Math.floor(k/2)}return R}
function order(P:Point,p:number):number{let R:Point=null;for(let n=1;n<5000;n++){R=add(R,P,p);if(R===null)return n}throw new Error('order')}
function seed(p:number,s:number):readonly[Point,Point]{return[[mod((197+17*s)*inv(2,p),p),mod(1393+119*s,p)],[mod((-1173+47*s)*inv(2738,p),p),mod((-27377+329*s)*inv(50653,p),p)]]}
function qt(P:Point,e:1|-1,p:number):number{assert(P!==null&&P[1]!==0,'quartic chart');return mod((P[0]+e)*inv(P[1],p),p)}
function pw(a:number,n:number,p:number):number{let b=mod(a,p),r=1,k=n;while(k){if(k&1)r=mod(r*b,p);b=mod(b*b,p);k=Math.floor(k/2)}return r}
function fp(t:number,p:number):number{return mod(pw(t,4,p)+6*mod(t*t,p)+1,p)}
function phix(x:number,y:number,p:number):readonly[number,number,number,number]{const gap=mod(x*x-y*y+6,p);assert(gap!==0,'gap');const C=mod((x*x*y*y+1)*inv(gap,p),p);if(C===0){const xo=mod(-inv(pw(x,3,p),p),p);return[xo,fp(xo,p),gap,1]}const K=mod(6*C-1,p),a=C,b=mod(C*C+K,p),d=mod(C*K,p),x2=pw(x,2,p),x4=pw(x,4,p),x6=pw(x,6,p),x8=pw(x,8,p);const N=mod(-x*mod(mod(a*a,p)*x8-6*mod(a*d,p)*x4-4*mod(b*d,p)*x2-3*d*d,p),p);const D0=mod(3*mod(a*a,p)*x8+4*mod(a*b,p)*x6+6*mod(a*d,p)*x4-d*d,p);assert(D0!==0,'D0');const xo=mod(N*inv(D0,p),p);return[xo,fp(xo,p),gap,D0]}
function hmv(p:number,s:number){const[P,Q]=seed(p,s),per=order(mul(2,Q,p),p),rows:number[][]=[];for(let m=0;m<per;m++){const Pm=add(P,mul(-2*m,Q,p),p),Qm=add(Q,mul(2,Pm,p),p),x=qt(Pm,1,p),y=qt(Qm,-1,p),[xo,F,g,d]=phix(x,y,p);rows.push([m,x,y,xo,F,g,d])}return{p,s,ordP:order(P,p),ordQ:order(Q,p),period:per,rows}}
function key(P:Point):string{return P===null?'O':`${P[0]},${P[1]}`}
function closure(p:number,s:number){const[P0,Q0]=seed(p,s),oP=order(P0,p),oQ=order(Q0,p),oddP=Array.from({length:oP/2},(_,i)=>2*i+1),oddQ=Array.from({length:oQ/2},(_,i)=>2*i+1),start:readonly[Point,Point]=[P0,Q0],seen=new Map<string,readonly[Point,Point]>([[`${key(P0)}|${key(Q0)}`,start]]),queue:Array<readonly[Point,Point]>=[start];for(let i=0;i<queue.length;i++){const[P,Q]=queue[i]!,next:Array<readonly [Point,Point]> =[[add(P,mul(-2,Q,p),p),Q],[add(P,mul(2,Q,p),p),Q],[P,add(Q,mul(-2,P,p),p)],[P,add(Q,mul(2,P,p),p)],...oddP.map(a=>[mul(a,P,p),Q] as const),...oddQ.map(d=>[P,mul(d,Q,p)] as const)];for(const st of next){const k=`${key(st[0])}|${key(st[1])}`;if(!seen.has(k)){seen.set(k,st);queue.push(st)}}}let zeros=0,amb=0;for(const[P,Q]of seen.values()){try{const x=qt(P,1,p),y=qt(Q,-1,p),[,F]=phix(x,y,p);if(F===0)zeros++}catch{amb++}}return{p,s,ordP:oP,ordQ:oQ,states:seen.size,zeros,ambiguous:amb}}
assert(mod(44*44-137,257)===0&&mod(213*213-137,257)===0,'roots257');assert(mod(78*78-137,313)===0&&mod(235*235-137,313)===0,'roots313');
const rows=[hmv(257,44),hmv(257,213),hmv(313,78),hmv(313,235)],e257=[[0,202,47,137,113],[1,187,175,98,87],[2,55,47,120,113],[3,70,175,159,87]],e313=[[0,246,300,112,95],[1,67,300,201,95]];
for(const r of rows.slice(0,2)){assert(r.ordP===16&&r.ordQ===8&&r.period===4,'orders257');assert(JSON.stringify(r.rows.map(x=>x.slice(0,5)))===JSON.stringify(e257),'rows257')}
for(const r of rows.slice(2)){assert(r.ordP===24&&r.ordQ===4&&r.period===2,'orders313');assert(JSON.stringify(r.rows.map(x=>x.slice(0,5)))===JSON.stringify(e313),'rows313')}
for(const r of rows)for(const row of r.rows)assert(row[5]!==0&&row[6]!==0,'regular row');
const cs=[closure(313,78),closure(313,235),closure(257,44),closure(257,213)];for(const c of cs.slice(0,2))assert(c.states===576&&c.zeros===0&&c.ambiguous===0,'closure313');for(const c of cs.slice(2))assert(c.states===1024&&c.zeros===96&&c.ambiguous===16,'closure257');
console.log(JSON.stringify({status:'passed',hmv:rows,closures:cs},null,2));
