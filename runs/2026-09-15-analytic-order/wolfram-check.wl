Module[{q,f,n,t,a,tt,s,x,y,X,Y,res,pts,triples,vec,rr},
f=Fold[Normal[Series[#1 (1-q^#2)^2,{q,0,64}]]&,q,Join[Range[4,64,4],Range[8,64,8]]];
X=(x^2-1)/x; Y=-y*(x^2+1)/x^2;
res=PolynomialRemainder[Expand[Numerator[Together[Y^2-X^3-4X]]],y^2-x^3+x,y];
pts={{-9,120},{841,24360}};
triples={{2,82,41},{-41,41,-1},{-50,32,-9},{800,882,841}};
vec=Flatten[({Boole[#<0],Mod[IntegerExponent[Abs[#],2],2],Mod[IntegerExponent[Abs[#],41],2]}&)/@#]&;
rr=Integrate[t^2 Exp[-a t],{t,tt,Infinity},Assumptions->a>0&&tt>0];
<|"version"->$Version,
"eta_nonzero_prefix"->Select[Table[{n,Coefficient[f,q,n]},{n,1,25}],Last[#]!=0&],
"twisted_41_prefix"->Table[{n,Coefficient[f,q,n]*JacobiSymbol[n,41]},{n,{1,5,9,13,17,25}}],
"isogeny_polynomial_residual"->res,
"E41_point_residuals"->((#[[2]]^2-#[[1]]^3+41^2*#[[1]])&/@pts),
"E41_Kummer_rank"->MatrixRank[vec/@triples,Modulus->2],
"tail_antiderivative_check"->FullSimplify[rr-Exp[-a tt]*(tt^2/a+2tt/a^2+2/a^3),a>0&&tt>0],
"Mellin_derivative_check"->FullSimplify[(D[t^(s-1)+t^(1-s),{s,2}]/.s->1)-2Log[t]^2,t>0],
"scope"->"Symbolic formulas, six eta coefficients, two points and Kummer matrix; not an interval-integral or BSD proof."|>]
