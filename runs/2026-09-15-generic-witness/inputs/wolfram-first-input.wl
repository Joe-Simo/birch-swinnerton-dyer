Module[{t,u,v,w,z,a,b,A,B,c,s,x,y,X,Y,vars,rows,q1,q2,mat,pencils,paramChecks,mapChecks,kummerChecks,squarefree,Jchecks,xx,yy,poly,e,i,j},
vars={u,v,w,z};
rows={{0,1,0,0,1,1,0,0,1},{1,0,1,0,0,1,1,0,0},{0,0,0,0,0,1,0,0,1},{0,0,1,0,0,0,0,0,1}};
pencils=Table[q1=v^2-w^2+e*z^2;q2=u^2-t*w^2-e*t*z^2;mat=Table[D[a*q1+b*q2,vars[[i]],vars[[j]]],{i,4},{j,4}];Factor[Det[mat]+16*e*a*b*(a^2-t^2*b^2)],{e,{-1,1}}];
paramChecks=Table[{Expand[(v^2-w^2+e*z^2)/.{v->A^2-e*B^2,w->A^2+e*B^2,z->2*A*B}],Expand[((u^2-t*w^2-e*t*z^2)/.{u->t*c,w->A^2+e*B^2,z->2*A*B})-t*(t*c^2-A^4-6*e*A^2*B^2-B^4)]},{e,{-1,1}}];
poly=t^2*u^2*v^2*w^2-t^3*w^6+t^3*w^2*z^4;
mapChecks=Table[Factor[poly/.{u^2->t*(w^2+e*z^2),v^2->w^2-e*z^2}],{e,{-1,1}}];
kummerChecks={Expand[t*(w^2-z^2)-t*(w^2-z^2)],Expand[t*(w^2+z^2)-t*(w^2+z^2)]};
squarefree=Table[PolynomialGCD[A^4+6*e*A^2+1,4*A^3+12*e*A],{e,{-1,1}}];
xx=t*w^2/z^2;yy=t*u*v*w/z^3;
Jchecks={Expand[((v^2-w^2-z^2)/.z->I*z)-(v^2-w^2+z^2)],Expand[((u^2-t*w^2+t*z^2)/.z->I*z)-(u^2-t*w^2-t*z^2)],Together[(xx/.z->I*z)+xx],Together[(yy/.z->I*z)-I*yy]};
<|"version"->$Version,"pencil_residuals"->pencils,"quartic_parametrization_residuals"->paramChecks,"covering_map_residuals"->mapChecks,"quartic_gcds"->squarefree,"Kummer_rank"->MatrixRank[rows,Modulus->2],"Kummer_minor"->Det[rows[[All,{1,2,3,6}]]],"quadratic_companion_residuals"->Jchecks,"twist_residual"->Expand[((y^2-x^3+t^2*x)/.{t->s^2,x->s^2*X,y->s^3*Y})-s^6*(Y^2-X^3+X)],"trace_ring_identity"->Expand[(a+I*b)+(a-I*b)-2*a],"E41_point_residual"->((25215/64)^2-(1025/16)^3+41^2*(1025/16)),"scope"->"Exact generic polynomial and four-row matrix certificates only; not a formal proof of the all-degree morphism classification, generic Mordell-Weil group, or odd-degree nonexistence."|>
]
