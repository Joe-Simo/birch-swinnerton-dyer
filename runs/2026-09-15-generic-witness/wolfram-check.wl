Module[{t,u,v,w,z,a,b,aa,bb,c,s,x,y,xx0,yy0,vars,rows,q1,q2,mat,pencils,paramchecks,mapchecks,squarefree,jchecks,xx,yy,poly,e,i,j},
vars={u,v,w,z};
rows={{0,1,0,0,1,1,0,0,1},{1,0,1,0,0,1,1,0,0},{0,0,0,0,0,1,0,0,1},{0,0,1,0,0,0,0,0,1}};
pencils=Table[q1=v^2-w^2+e*z^2;q2=u^2-t*w^2-e*t*z^2;mat=Table[D[a*q1+b*q2,vars[[i]],vars[[j]]],{i,4},{j,4}];Factor[Det[mat]+16*e*a*b*(a^2-t^2*b^2)],{e,{-1,1}}];
paramchecks=Table[{Expand[(v^2-w^2+e*z^2)/.{v->aa^2-e*bb^2,w->aa^2+e*bb^2,z->2*aa*bb}],Expand[((u^2-t*w^2-e*t*z^2)/.{u->t*c,w->aa^2+e*bb^2,z->2*aa*bb})-t*(t*c^2-aa^4-6*e*aa^2*bb^2-bb^4)]},{e,{-1,1}}];
poly=t^2*u^2*v^2*w^2-t^3*w^6+t^3*w^2*z^4;
mapchecks=Table[Factor[poly/.{u^2->t*(w^2+e*z^2),v^2->w^2-e*z^2}],{e,{-1,1}}];
squarefree=Table[PolynomialGCD[aa^4+6*e*aa^2+1,4*aa^3+12*e*aa],{e,{-1,1}}];
xx=t*w^2/z^2;yy=t*u*v*w/z^3;
jchecks={Expand[((v^2-w^2-z^2)/.z->I*z)-(v^2-w^2+z^2)],Expand[((u^2-t*w^2+t*z^2)/.z->I*z)-(u^2-t*w^2-t*z^2)],Together[(xx/.z->I*z)+xx],Together[(yy/.z->I*z)-I*yy]};
<|"version"->$Version,"pencil_residuals"->pencils,"quartic_parametrization_residuals"->paramchecks,"covering_map_residuals"->mapchecks,"quartic_gcds"->squarefree,"Kummer_rank"->MatrixRank[rows,Modulus->2],"Kummer_minor"->Det[rows[[All,{1,2,3,6}]]],"quadratic_companion_residuals"->jchecks,"twist_residual"->Expand[((y^2-x^3+t^2*x)/.{t->s^2,x->s^2*xx0,y->s^3*yy0})-s^6*(yy0^2-xx0^3+xx0)],"trace_ring_identity"->Expand[(a+I*b)+(a-I*b)-2*a],"E41_point_residual"->((25215/64)^2-(1025/16)^3+41^2*(1025/16)),"scope"->"Exact generic polynomial and four-row matrix certificates only; not a formal proof of the all-degree morphism classification, generic Mordell-Weil group, or odd-degree nonexistence."|>
]
