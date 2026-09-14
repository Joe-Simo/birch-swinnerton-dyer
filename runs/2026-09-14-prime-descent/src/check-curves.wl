ClearAll[q, count, coefficient, monsky, squareClass];
limit = 200;
count[n_Integer, c_Integer] := Total[Flatten[Table[Boole[x^2 + 2 y^2 + c z^2 == n], {x, -Floor[Sqrt[n]], Floor[Sqrt[n]]}, {y, -Floor[Sqrt[n/2]], Floor[Sqrt[n/2]]}, {z, -Floor[Sqrt[n/c]], Floor[Sqrt[n/c]]}]]];
g = Fold[Normal[Series[#1 (1 - q^#2), {q, 0, limit}]] &, q, Join[Range[8, limit, 8], Range[16, limit, 16]]];
f = Normal[Series[g Sum[q^(2 j^2), {j, -Floor[Sqrt[limit/2]], Floor[Sqrt[limit/2]]}], {q, 0, limit}]];
monsky[p_Integer] := With[{d2 = (1 - JacobiSymbol[2, p])/2, dm2 = (1 - JacobiSymbol[-2, p])/2}, {{d2, d2}, {d2, dm2}}];
primes = Select[Prime[Range[PrimePi[limit]]], Mod[#, 8] == 1 &];
rows = Table[With[{a = count[p, 8], b = count[p, 32], c = Coefficient[f, q, p]}, <|"p" -> p, "A" -> a, "B" -> b, "a_p" -> c, "count_identity" -> (c == b - a/2), "Monsky" -> monsky[p], "pure_selmer_dimension" -> 2 - MatrixRank[monsky[p], Modulus -> 2]|>], {p, primes}];
points = {{-9,120},{841,24360}};
pointResiduals = (#[[2]]^2 - #[[1]]^3 + 41^2 #[[1]]) & /@ points;
squareClass[a_Integer] := Join[{Boole[a < 0]}, Table[Mod[IntegerExponent[Abs[a], p], 2], {p, {2,41}}]];
kummer = {{2,82,41},{-41,41,-1},{-50,32,-9},{800,882,841}};
vectors = (Flatten[squareClass /@ #] &) /@ kummer;
<|"version" -> $Version, "rows" -> rows, "point_residuals" -> pointResiduals, "kummer_vectors" -> vectors, "kummer_rank" -> MatrixRank[vectors, Modulus -> 2], "pairing_signs" -> {{17, -3, 1, JacobiSymbol[3,17]}, {41, 5, 3, JacobiSymbol[-5,41]}}, "tests" -> {And @@ Lookup[rows,"count_identity"], pointResiduals == {0,0}, MatrixRank[vectors, Modulus -> 2] == 4, Coefficient[f,q,1] == 1, Coefficient[f,q,17] == -4, Coefficient[f,q,41] == 0}|>
