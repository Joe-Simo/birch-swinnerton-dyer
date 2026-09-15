Module[{c,k,x,z,cc=-39785/37632,kk=-46057/6272,seed={1/14,37/14},next={-16890371/79256324,210069683/77723044},f,g,red,rho,add,rows,p,squares,allowed,delta,mults,ratioC,y3,u,v,branch,quotient,P,R,a,b,q,pt,cv,kv,j},
f=(x^2+c)(c x^2+k);g=x^4+6x^2+1;
branch=Factor[Resultant[f/.k->6c-1,g,x]];
quotient=Expand[(c x z)^2-(c x^2)(c x^2+c^2)(c x^2+k)]/.z^2->f//Expand;
red[a_,q_]:=Mod[Numerator[a] PowerMod[Denominator[a],-1,q],q];
rho[pt_,q_]:=With[{cx=red[cc,q],xx=red[pt[[1]],q],yy=red[pt[[2]],q]},Mod[{cx xx^2,cx xx yy (xx^2+cx)},q]];
add[P_,R_,q_,cv_,kv_]:=Module[{a0,b0,d0,e0,sl,xx},If[P==="O",Return[R]];If[R==="O",Return[P]];{a0,b0}=P;{d0,e0}=R;If[a0==d0&&Mod[b0+e0,q]==0,Return["O"]];sl=If[a0==d0,Mod[(3a0^2+2(cv^2+kv)a0+cv^2 kv)PowerMod[2b0,-1,q],q],Mod[(e0-b0)PowerMod[d0-a0,-1,q],q]];xx=Mod[sl^2-(cv^2+kv)-a0-d0,q];{xx,Mod[sl(a0-xx)-b0,q]}];
rows=Table[Module[{cv0=red[cc,p],kv0=red[kk,p],r0=rho[seed,p],r1=rho[next,p],count,diff},count=1+Total[Flatten[Table[Boole[Mod[b^2-a(a+cv0^2)(a+kv0),p]==0],{a,0,p-1},{b,0,p-1}]]];diff=add[r1,Mod[{r0[[1]],-r0[[2]]},p],p,cv0,kv0];<|"p"->p,"C"->cv0,"K"->kv0,"order"->count,"difference"->diff|>],{p,{13,19,31}}];
delta={28,5};mults=Rest[NestList[add[#,delta,31,6,4]&,"O",8]];
squares=Sort[DeleteDuplicates[Mod[Range[0,12]^2,13]]];
allowed=Select[Table[{j,Mod[(j^2+6)(6j^2+9),13],Mod[j^4+6j^2+1,13]},{j,0,12}],MemberQ[squares,#[[2]]]&];
y3=With[{t=seed[[2]]},t(t^8-6t^4+24t^2-3)/(3t^8-24t^6+6t^4-1)];
u=seed[[1]]^2+3;v=y3^2-3;ratioC=(u v-8)/(u-v)+3;
<|"version"->$Version,"branch_resultant"->branch,"quotient_residual"->quotient,"finite_rows"->rows,"Delta_multiples_mod31"->mults,"local13_allowed"->allowed,"all_local_values_nonsquare"->And@@((JacobiSymbol[#[[3]],13]==-1)&/@allowed),"changed_fiber_C"->ratioC,"changed_fiber_C_mod13"->red[ratioC,13],"changed_fiber_target_residuals"->(Mod[#[[1]] #[[2]]^2-(5^4+6*5^2+1),13]&/@{{257,6},{313,3}}),"scope"->"Finite-field counts, exact rational coefficient and generic identities only; not a proof of infinite orbit, genus or BSD."|>]
