# H12 checker corrections

The initial matrix fixture had a zero in row 1, column 4. The raw Kummer minor at columns (0,1,2,5) has a one there; the initial matrix is obtained by adding the lambda-minus row to the torsion row. Both determinants are one, so the independence conclusion survives. The accepted TypeScript and Python checks now build the raw minor directly from the squareclass triples, without an unstated row operation. Initial logs are retained, not represented as the accepted final run.

The first Wolfram call rejected an invalid destructuring Table iterator in its final two-witness subcalculation. Its other returned identities are usable only at their exact scope. A separate focused Map call checked the two integer witness residuals. A final raw-minor call checks the corrected connection to the full squareclass vectors.

The original contract proposed extra bounded integer-matrix and torsion-translation fixtures. These were not run: the accepted population checks all 16 mod-2 matrices, while the complete integer-matrix/translation classification is a written proof using the affine-morphism theorem. No such unexecuted fixtures are included in a test count.
