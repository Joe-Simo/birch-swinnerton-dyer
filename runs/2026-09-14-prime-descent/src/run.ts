import { casselsPrimeCertificate, binaryRank, isPrime, jsonExact, kummer, kummerMask, legendre, monsky, onCurve, specializationProfile, squareClass, ternaryWitnesses, tunnellCoefficients } from "./exact.js";

const bound = 200;
const coefficients = tunnellCoefficients(bound);
function curveRow(p: bigint) {
  const A = BigInt(ternaryWitnesses(p, 8).length);
  const B = BigInt(ternaryWitnesses(p, 32).length);
  const qCoefficient = coefficients[Number(p)]; // bounded positive integer <=200.
  if (qCoefficient === undefined || 2n * qCoefficient !== 2n * B - A) {
    throw new Error(`Independent exact coefficient formulas disagree at ${p}.`);
  }
  return { p, A, B, a: qCoefficient, centralValueZero: qCoefficient === 0n, ...monsky(p) };
}
const baseline = curveRow(17n);
const rows = [];
for (let p = 3n; p <= BigInt(bound); p += 2n) {
  if (p % 8n === 1n && isPrime(p)) rows.push(curveRow(p));
}
const points = [{ x: 41n, y: 0n }, { x: 0n, y: 0n }, { x: -9n, y: 120n }, { x: 841n, y: 24360n }];
const pointCertificates = points.map((point) => {
  const tuple = kummer(41n, point);
  return { point, onCurve: onCurve(41n, point), kummer: tuple, squareClasses: tuple.map(squareClass), mask: kummerMask(tuple, [2n, 41n]) };
});
console.log(jsonExact({
  status: "completed bounded checks; no complete BSD candidate",
  integerEncoding: "decimal strings; dimensions and binary entries are small exact JSON numbers",
  baseline,
  baselineAlgebraicCertificate: {
    n: "17", mu: "-3", tau: "1", d: "17",
    pellIdentity: 2n * (-3n) ** 2n - 1n === 17n,
    congruence: ((-3n - 17n) % 4n) === 0n,
    pairingSign: legendre(3n, 17n),
    source: "Zhang arXiv:2111.11618v1, Theorem 3.2; applicability proved in checkpoint"
  },
  domain: "all primes p congruent to 1 mod 8, 1<p<=200",
  rows,
  firstHigherDescent: [casselsPrimeCertificate(17n, -3n, 1n), casselsPrimeCertificate(41n, 5n, 3n), casselsPrimeCertificate(113n, 9n, 7n)],
  pointCertificates,
  kummerRank: binaryRank(pointCertificates.map((p) => p.mask)),
  baselineCountWitnesses: { A: ternaryWitnesses(17n, 8), B: ternaryWitnesses(17n, 32) },
  specializationExamples: [[], [1, 1], [2, 2], [1, 2]].map((exponents) => ({ exponents, ...specializationProfile(exponents) })),
  limitations: [
    "Tunnell zero coefficients are not exact analytic-rank certificates.",
    "Rank claims use the separate written descent proof, not numerical labels.",
    "The module examples are not asserted to arise from elliptic curves.",
    "Neither bounded agreement nor these known special cases solves universal BSD."
  ]
}));
