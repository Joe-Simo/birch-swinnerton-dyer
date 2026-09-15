Module[{a,b,t,eps,d,ap,bp,fp,fm,km,parameters,rows,ids},
 d=a^8-56a^4b^4+1296b^8; bp=2a b;
 ids=Table[ap=a^2-6eps b^2; Expand[ap^4+6eps ap^2 bp^2+bp^4-d],{eps,{-1,1}}];
 fm=a^4-4a^3b+8a^2b^2-24a b^3+36b^4;
 fp=a^4+4a^3b+8a^2b^2+24a b^3+36b^4;
 km={{0,1,0,0,1,1,0,0,1},{1,0,1,0,0,1,1,0,0},{0,0,0,0,0,1,0,0,1},{0,0,1,0,0,0,0,0,1}};
 parameters={{1,1},{2,1},{3,1},{4,1},{5,1},{7,1},{1,2},{3,2}};
 rows=Map[Function[ab,Module[{dv,fac,n,s,pnts,c},
   dv=d/.{a->ab[[1]],b->ab[[2]]}; fac=FactorInteger[dv];
   n=Times@@(First/@Select[fac,OddQ[Last[#]]&]); s=Sqrt[dv/n];
   c=If[EvenQ[ab[[1]]],2,1]*If[Divisible[ab[[1]],3],3,1];
   pnts=Table[Module[{A,B,u,v,w,z,x,y,labs,roots},
     A=ab[[1]]^2-6e ab[[2]]^2; B=2ab[[1]]ab[[2]];
     u=n s; v=A^2-e B^2; w=A^2+e B^2; z=2A B;
     x=n w^2/z^2; y=n u v w/z^3;
     labs=If[e==-1,{1,n,n},{n,1,n}]; roots=If[e==-1,{u,v,w},{v,u,w}];
     <|"sign"->e,"quadrics"->{v^2-w^2+e z^2,u^2-n w^2-e n z^2},"curve"->Together[y^2-x^3+n^2x],"Kummer"->Together[{x-n,x+n,x}-labs*(roots/z)^2],"nonzero"->(u v w z!=0)|>],{e,{-1,1}}];
   <|"parameter"->ab,"D"->dv,"n"->n,"normalization"->(n s^2==dv),"prime_support"->And@@(Mod[First[#],8]==1&/@Select[fac,OddQ[Last[#]]&]),"factor_gcd"->(GCD[fm/.{a->ab[[1]],b->ab[[2]]},fp/.{a->ab[[1]],b->ab[[2]]}]==c^2),"points"->pnts|>]],parameters];
 <|"version"->$Version,"quartic_identities"->ids,"factor_identity"->Expand[d-fm fp],"positive_norm_identity"->Expand[d-(a^4-28b^4)^2-512b^8],"discriminant_factorization"->FactorInteger[Discriminant[d/.{a->t,b->1},t]],"Kummer_rank"->MatrixRank[km,Modulus->2],"minor_determinant"->Det[km[[All,{1,2,3,6}]]],"rows"->rows,"scope"->"Two polynomial identities, eight parameters, sixteen point certificates and one shared minor; not a formal proof of infinitude, independence at every parameter, or BSD."|>
]
