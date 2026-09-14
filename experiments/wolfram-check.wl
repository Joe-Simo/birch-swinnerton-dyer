ClearAll[q,t,count,jetNullity];
count[n_Integer,c_Integer]:=Total[Flatten[Table[Boole[2 x^2+y^2+c z^2==n],
 {x,-Floor[Sqrt[n]],Floor[Sqrt[n]]},{y,-Floor[Sqrt[n]],Floor[Sqrt[n]]},
 {z,-Floor[Sqrt[n]],Floor[Sqrt[n]]}]]];
poly=Expand[q Product[(1-q^(8 k))(1-q^(16 k)),{k,1,5}](1+2 Sum[q^(2 z^2),{z,1,4}])];
mats={{{t^2}},{{t,1},{0,t}},{{t^2,t},{t,1+t}},{{0,t^2},{-t^2,0}}};
jetNullity[a_,m_Integer]:=Module[{n=Length[a],b},
 b=Table[If[Quotient[i-1,n]>=Quotient[j-1,n],
 Coefficient[a[[Mod[i-1,n]+1,Mod[j-1,n]+1]],t,Quotient[i-1,n]-Quotient[j-1,n]],0],
 {i,n m},{j,n m}];n m-MatrixRank[b]];
ExportString[<|
 "coefficients"->Table[<|"n"->n,"A32"->count[n,32],"B8"->count[n,8],"a"->Coefficient[poly,q,n]|>,{n,{1,17,41}}],
 "points41"->Table[<|"x"->xy[[1]],"y"->xy[[2]],"residual"->xy[[2]]^2-xy[[1]]^3+41^2 xy[[1]]|>,{xy,{{-9,120},{841,24360}}}],
 "matrices"->Table[<|"determinant"->ToString[Factor[Det[a]],InputForm],
 "specializedNullity"->Length[a]-MatrixRank[a/.t->0],
 "jetNullities"->Table[jetNullity[a,m],{m,1,5}]|>,{a,mats}]|>,"RawJSON"]
