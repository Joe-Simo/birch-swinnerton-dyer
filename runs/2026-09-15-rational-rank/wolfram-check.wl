Module[{data, rows, r, p, e, a, b, c, u, v, w, z, xx, yy, f, g, generic, bits, matrix},
 data={{41,-1,5,2,1},{41,1,2,1,1},{137,-1,37,14,47},{137,1,14,1,17},{257,-1,13,4,7},{257,1,104,11,697},{313,-1,19409,582,21235361},{313,1,3,2,1},{353,-1,15641,968,12870529},{353,1,4,1,1},{457,-1,17,6,7},{457,1,653,282,29273},{761,-1,41,10,49},{761,1,190,59,1649}};
 rows=Table[p=r[[1]];e=r[[2]];a=r[[3]];b=r[[4]];c=r[[5]];u=p c;v=a^2-e b^2;w=a^2+e b^2;z=2 a b;xx=p w^2/z^2;yy=p u v w/z^3;
  <|"p"->p,"sign"->e,"quartic_residual"->(a^4+6 e a^2 b^2+b^4-p c^2),"quadrics"->{v^2-w^2+e z^2,u^2-p w^2-e p z^2},"curve_residual"->Together[yy^2-xx^3+p^2 xx],"primitive"->(GCD[a,b]==1&&OddQ[a-b]&&a>b>0&&GCD[u,v,w,z]==1),"kummer_residuals"->If[e==-1,{xx-p-(u/z)^2,xx+p-p(v/z)^2,xx-p(w/z)^2},{xx-p-p(v/z)^2,xx+p-(u/z)^2,xx-p(w/z)^2}],"prime_and_Monsky"->{PrimeQ[p],JacobiSymbol[2,p],JacobiSymbol[-2,p]}|>,{r,data}];
 Clear[p,a,b,c];
 generic=Table[u=p c;v=a^2-e b^2;w=a^2+e b^2;z=2 a b;xx=p w^2;yy=p u v w;f=a^4+6 e a^2 b^2+b^4-p c^2;
  {Expand[v^2-w^2+e z^2],PolynomialRemainder[yy^2-xx^3+p^2 xx z^4,f,c],PolynomialRemainder[u^2-p w^2-e p z^2,f,c]},{e,{-1,1}}];
 bits[n_,q_]:={Boole[n<0],Mod[IntegerExponent[Abs[n],2],2],Mod[IntegerExponent[Abs[n],q],2]};
 matrix=Flatten[bits[#,41]&/@#,1]&/@{{2,82,41},{-41,41,-1},{1,41,41},{41,1,41}};
 <|"version"->$Version,"rows"->rows,"generic_residuals"->generic,"Kummer_rank"->MatrixRank[matrix,Modulus->2],"minor_determinant"->Det[matrix[[All,{1,2,3,6}]]],"scope"->"Fourteen exact point witnesses, their Kummer factors, generic identities and one shared minor; no all-prime existence theorem or analytic certificate evaluated."|>
]
