import { casselsPrimeCertificate, binaryRank, factor, isqrt, kummer, kummerMask, legendre, monsky, onCurve, specializationProfile, squareClass, ternaryWitnesses, tunnellCoefficients } from "../src/exact.js";

// Top-level assertions run as one file under Node's built-in test runner.
function check(condition: boolean, label: string): void {
  if (!condition) throw new Error(label);
  console.log(`PASS ${label}`);
}
function rejects(action: () => unknown, label: string): void {
  let threw = false;
  try { action(); } catch { threw = true; }
  check(threw, label);
}
check(isqrt(0n) === 0n && isqrt(1n) === 1n && isqrt(15n) === 3n && isqrt(16n) === 4n, "integer square-root boundaries");
check(isqrt(10n ** 40n - 1n) === 10n ** 20n - 1n, "large-integer square root is lossless");
rejects(() => isqrt(-1n), "negative square root rejected");
check(factor(41n ** 2n)[0]?.[1] === 2, "factor exponent retained");
check(legendre(3n, 17n) === -1n && legendre(-5n, 41n) === 1n, "independent small residue fixtures");
rejects(() => legendre(2n, 9n), "composite Legendre modulus rejected");
check(binaryRank([1n, 2n, 3n]) === 2 && binaryRank([]) === 0, "binary dependence and empty matrix");
rejects(() => binaryRank([-1n]), "negative row rejected");
check(monsky(1n).pureDimension === 0 && monsky(3n).pureDimension === 0, "Monsky rank-zero fixtures");
check(monsky(5n).pureDimension === 1 && monsky(7n).pureDimension === 1, "Monsky rank-one upper-bound fixtures");
check(monsky(17n).pureDimension === 2 && monsky(41n).pureDimension === 2, "identical rank-two Selmer fixtures");
rejects(() => monsky(9n), "nonsquarefree model excluded from Monsky formula");
rejects(() => monsky(2n), "even model excluded from odd Monsky formula");
const coefficients = tunnellCoefficients(200);
check(coefficients[1] === 1n && coefficients[3] === 2n && coefficients[17] === -4n && coefficients[41] === 0n, "authenticated Tunnell coefficient fixtures");
check(ternaryWitnesses(17n, 8).length === 16 && ternaryWitnesses(17n, 32).length === 4, "full sign-count fixtures");
check(ternaryWitnesses(0n, 8).length === 1, "zero-coordinate multiplicity fixture");
rejects(() => ternaryWitnesses(201n, 8), "unregistered counting bound rejected");
rejects(() => tunnellCoefficients(201), "unregistered polynomial bound rejected");
const points = [{ x: -9n, y: 120n }, { x: 841n, y: 24360n }];
check(points.every((p) => onCurve(41n, p)), "rank-two point witnesses satisfy exact equation");
rejects(() => kummer(41n, { x: -9n, y: 121n }), "incorrect point cannot yield a certificate");
check(squareClass(-50n) === -2n && squareClass(882n) === 2n, "squareclass square factors removed");
rejects(() => kummerMask([3n], [2n, 41n]), "omitted squareclass prime rejected");
const all = [{ x: 41n, y: 0n }, { x: 0n, y: 0n }, ...points];
const masks = all.map((p) => kummerMask(kummer(41n, p), [2n, 41n]));
check(binaryRank(masks) === 4, "torsion and rational Kummer classes independent");
check(binaryRank([masks[0] ?? 0n, masks[0] ?? 0n]) === 1, "duplicated point cannot prove independence");
const profile = specializationProfile([2, 2]);
check(profile.length === 4 && profile.fiberDimension === 2 && profile.excess === 2, "self-dual module length differs from fiber dimension");
check(profile.gradedDimensions.reduce((s, d) => s + d, 0) === profile.length, "graded length decomposition");
rejects(() => specializationProfile([0]), "invalid cyclic exponent rejected");

const paired41 = casselsPrimeCertificate(41n, 5n, 3n);
const paired113 = casselsPrimeCertificate(113n, 9n, 7n);
check(paired41.sign === 1n && paired113.sign === 1n, "same trivial first Cassels pairing at 41 and 113");
check(paired41.selmer4Order === 64n && paired113.selmer4Order === 64n, "same inferred Selmer-4 order at 41 and 113");
check(casselsPrimeCertificate(17n, -3n, 1n).selmer4Order === 16n, "nondegenerate first pairing separates 17");
rejects(() => casselsPrimeCertificate(113n, 9n, 5n), "false norm witness rejected");
rejects(() => casselsPrimeCertificate(17n, 3n, 1n), "wrong sign convention for mu rejected");
