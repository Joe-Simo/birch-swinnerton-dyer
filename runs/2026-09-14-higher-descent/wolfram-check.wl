Module[{q,x,n,z,g,f,ct,rows,delta,transform,tab},
ct[d_Integer,c_Integer]:=Total[Flatten[Table[Boole[u^2+2v^2+c w^2==d],{u,-Floor[Sqrt[d]],Floor[Sqrt[d]]},{v,-Floor[Sqrt[d/2]],Floor[Sqrt[d/2]]},{w,-Floor[Sqrt[d/c]],Floor[Sqrt[d/c]]}]]];
g=Fold[Normal[Series[#1(1-q^#2),{q,0,113}]]&,q,Join[Range[8,113,8],Range[16,113,16]]];
f=Normal[Series[g Sum[q^(2z^2),{z,-7,7}],{q,0,113}]];
rows=Table[With[{a=Coefficient[f,q,d],aa=ct[d,8],bb=ct[d,32]},<|"n"->d,"A"->aa,"B"->bb,"a"->a,"count_identity"->(2a==2bb-aa),"sha_order_from_rank_zero_theorem"->If[a==0,"not applicable",a^2/If[d==1,1,4]]|>],{d,{1,17,41,113}}];
delta=Factor[16Discriminant[x^3-n^2 x,x]];
transform=Expand[(y+x)^2-(x+1)^3+n^2(x+1)-(y^2+2x y-x^3-2x^2-(3-n^2)x-(1-n^2))];
tab=Table[<|"m"->m,"Sel_E17"->16,"Sel_E41"->4 2^(2m),"Sel_E113"->4 2^(2Min[m,2])|>,{m,1,4}];
<|"version"->$Version,"rows"->rows,"discriminant"->delta,"coordinate_residual"->transform,"tower_consequences"->tab,"tests"->{And@@Lookup[rows,"count_identity"],delta==64 n^6,transform==0,rows[[4,"sha_order_from_rank_zero_theorem"]]==16,tab[[3,"Sel_E41"]]!=tab[[3,"Sel_E113"]]}|>]
