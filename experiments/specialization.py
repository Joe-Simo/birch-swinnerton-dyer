"""Exact Q[T] computations for the specialization lemmas in RESEARCH.md.

Uses SymPy's native exact rational linear algebra; no numerical rank tolerance.
Contract and finite coverage are fixed in CONTRACT.md.
"""
from __future__ import annotations

import itertools
import json
from pathlib import Path

import sympy as sp

T = sp.Symbol("T")
ROOT = Path(__file__).resolve().parent.parent


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def order_at_zero(expression: sp.Expr) -> int:
    polynomial = sp.Poly(sp.expand(expression), T, domain=sp.QQ)
    if polynomial.is_zero:
        raise ValueError("The zero polynomial has no finite vanishing order")
    return min(monomial[0] for monomial, _ in polynomial.terms())


def coefficient_matrix(matrix: sp.MatrixBase, degree: int) -> sp.Matrix:
    return sp.Matrix(matrix.rows, matrix.cols,
                     lambda i, j: sp.expand(matrix[i, j]).coeff(T, degree))


def jet_nullity(matrix: sp.MatrixBase, depth: int) -> int:
    if depth < 1:
        raise ValueError("Positive truncation depth required")
    n = matrix.rows
    require(matrix.cols == n, "Square presentation required")
    coefficients = [coefficient_matrix(matrix, d) for d in range(depth)]
    # Coefficients of A(T)*v(T) in degrees 0,...,depth-1.
    toeplitz = sp.Matrix(n * depth, n * depth,
                        lambda i, j: coefficients[i // n - j // n][i % n, j % n]
                        if i // n >= j // n else 0)
    return n * depth - toeplitz.rank()


def bockstein_rank(matrix: sp.MatrixBase) -> int:
    a0, a1 = coefficient_matrix(matrix, 0), coefficient_matrix(matrix, 1)
    basis = a0.nullspace()
    if not basis:
        return 0
    image = a1 * sp.Matrix.hstack(*basis)
    # Dimension of (im A0 + A1 ker A0)/im A0, computed without a chosen quotient basis.
    return a0.row_join(image).rank() - a0.rank()


def record(label: str, matrix: sp.MatrixBase) -> dict[str, object]:
    determinant = sp.factor(matrix.det())
    order = order_at_zero(determinant)
    nullity = matrix.rows - coefficient_matrix(matrix, 0).rank()
    beta_rank = bockstein_rank(matrix)
    jets = [jet_nullity(matrix, m) for m in range(1, 6)]
    require(order >= nullity, f"Multiplicity inequality failed: {label}")
    require((order == nullity) == (beta_rank == nullity),
            f"First Bockstein criterion failed: {label}")
    increments = [jets[0]] + [b - a for a, b in zip(jets, jets[1:])]
    require(all(a >= b for a, b in zip(increments, increments[1:])),
            f"Jet increments must be nonincreasing: {label}")
    return {"label": label, "matrix": [[str(x) for x in row] for row in matrix.tolist()],
            "determinant": str(determinant), "order": order, "nullity": nullity,
            "bocksteinRank": beta_rank, "jetKernelDimensions": jets,
            "jetIncrements": increments}


def run() -> dict[str, object]:
    negative_rejections = 0
    for zero in [sp.Integer(0), sp.det(sp.Matrix([[T, T], [T, T]]))]:
        try:
            order_at_zero(zero)
        except ValueError:
            negative_rejections += 1
    require(negative_rejections == 2, "Singular determinant rejection")

    fixtures = [
        ("unit-at-zero", sp.Matrix([[1 + T]])),
        ("simple-zero", sp.Matrix([[T]])),
        ("double-zero", sp.Matrix([[T**2]])),
        ("triple-zero-parity-insufficient", sp.Matrix([[T**3]])),
        ("mixed-exponents", sp.diag(T, T**2)),
        ("extension-with-unit-off-diagonal", sp.Matrix([[T, 1], [0, T]])),
        ("Schur-complement-delayed-order", sp.Matrix([[T**2, T], [T, 1 + T]])),
        ("paired-even-skew", sp.Matrix([[0, T**2], [-T**2, 0]])),
    ]
    rows = [record(label, matrix) for label, matrix in fixtures]
    generated: list[dict[str, object]] = []
    for n in range(1, 4):
        upper, lower = sp.eye(n), sp.eye(n)
        for i in range(n - 1):
            upper[i, i + 1] = T
            lower[i + 1, i] = T**2
        require(upper.det() == 1 and lower.det() == 1, "Unimodular transform")
        for exponents in itertools.product(range(5), repeat=n):
            matrix = upper * sp.diag(*(T**e for e in exponents)) * lower
            row = record(f"exponents-{exponents}", matrix)
            require(row["order"] == sum(exponents), "Exact determinant order")
            require(row["nullity"] == sum(e > 0 for e in exponents), "Specialized dimension")
            require(row["jetKernelDimensions"] ==
                    [sum(min(m, e) for e in exponents) for m in range(1, 6)],
                    "Independent prescribed-Smith-exponent comparison")
            row["prescribedSmithExponents"] = list(exponents)
            generated.append(row)

    # Follow-up to failure of ordinary specialization: retain anti-Hermitian
    # involution symmetry as well as parity; neither forces simple zeros.
    symmetry_rows = []
    for exponent in range(1, 7):
        matrix = (sp.Matrix([[T**exponent]]) if exponent % 2 else
                  sp.Matrix([[0, T**exponent], [-T**exponent, 0]]))
        require(matrix.subs(T, -T).T == -matrix, "Anti-Hermitian symmetry")
        row = record(f"anti-Hermitian-exponent-{exponent}", matrix)
        require((int(row["order"]) - int(row["nullity"])) % 2 == 0,
                "Required parity agreement")
        symmetry_rows.append(row)

    return {"experiment": "A1", "status": "completed", "sympyVersion": sp.__version__,
            "arithmetic": "exact rationals and polynomials over Q",
            "generatedCases": len(generated), "explicitFixtures": rows,
            "allGeneratedCases": generated, "followupSymmetryCases": symmetry_rows,
            "singularRejections": negative_rejections,
            "scope": "Finite checker tests; universal algebraic proof is separate. No arithmetic realization of these toy modules is claimed."}


if __name__ == "__main__":
    report = run()
    path = ROOT / "results" / "specialization.json"
    path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: report[k] for k in ("experiment", "status", "generatedCases", "singularRejections")}))
    for result in report["explicitFixtures"]:
        print(json.dumps(result))
