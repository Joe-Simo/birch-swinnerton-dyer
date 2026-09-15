Module[{c,d,t,z,l,m,a,b,w,ff,gg,p1,p2,p3,q1,q2,q3,e,al,ga,red,qq1,qq2,vars,mat1,mat2,det,nn,uu,vv,pt,jac,errs,dj,nval,val,conicCheck,ellCheck},
ff=7 l^2-16 l m-7 m^2; gg=4 l^2+7 l m-4 m^2;
p1=c^2+8 c d+23 d^2;p2=-c^2+7 d^2;p3=4 c^2+30 c d+28 d^2;
q1=t^2+4 z^2;q2=7 z^2-4 t z;q3=-2 t^2+7 t z+8 z^2;
qq1=p1-q1;qq2=p2-q2;vars={c,d,t,z};
mat1=Table[D[qq1,vars[[i]],vars[[j]]]/2,{i,4},{j,4}];mat2=Table[D[qq2,vars[[i]],vars[[j]]]/2,{i,4},{j,4}];
det=Factor[Det[a mat1+b mat2]];e=(8+w)/7;al=(15+w)/7;ga=(15-w)/4;
red[ex_]:=PolynomialRemainder[Expand[ex],w^2-113,w];
conicCheck=red[(q1-e q2-al ((1-w)/2)^2)/.{t->-6-w,z->1}];
ellCheck=red[p1-e p2-al(c+ga d)^2];
uu=49 c-14 d-26 t-350 z;vv=7 c+14 d-5 t-35 z;nn=Expand[uu^2-113 vv^2];
pt={c->15035/9471,d->2,t->-121505/9471,z->1};
jac={{D[qq1,c],D[qq1,t]},{D[qq2,c],D[qq2,t]}};errs=Together[{qq1,qq2}/.pt];dj=Together[Det[jac]/.pt];nval=Together[nn/.pt];
val[r_]:=If[r==0,Infinity,IntegerExponent[Abs[Numerator[r]],2]-IntegerExponent[Denominator[r],2]];
<|"version"->$Version,"base_conic_identity"->Expand[113(ff^2+4 gg^2)-113^2(l^2+m^2)^2],
"p_identity"->Expand[(ff/.{l->p1,m->p2})-p3^2],"q_identity"->Expand[(gg/.{l->q1,m->q2})-q3^2],
"C3_pencil"->det,"pencil_discriminant_factors"->FactorInteger[Discriminant[det/.b->1,a]],
"field_square_factor_identity"->ellCheck,"field_conic_point_residual"->conicCheck,
"C3_at_113_residuals"->({qq1,qq2}/.{c->21,d->-8,t->0,z->1}),
"C3_at_113_tz_jacobian_det"->(Det[{{D[qq1,t],D[qq1,z]},{D[qq2,t],D[qq2,z]}}]/.{t->0,z->1}),
"Q2_refined_errors"->errs,"Q2_error_valuations"->(val/@errs),"Q2_jacobian_det_valuation"->val[dj],
"Q2_norm_valuation"->val[nval],"Q2_norm_mod1024"->Mod[Numerator[nval] PowerMod[Denominator[nval],-1,1024],1024],
"local_fourth_roots"->{Mod[14^4+4,113],Mod[18^4+1,113]},
"trivial_negative_class_residual"->(113^2-(-1*0^4-12769/(-1)*1^4))|>]
