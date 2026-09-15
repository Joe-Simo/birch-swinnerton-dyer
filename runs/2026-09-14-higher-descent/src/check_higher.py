"""Exact checker for supplied E113 higher-descent certificates.

This is not a point search and does not prove the external descent theorems.
Run with Python and SymPy. All recorded integers are serialized as strings.
"""
from __future__ import annotations

import itertools
import json
import platform

import sympy as s


def require(condition: bool, label: str) -> None:
    if not condition:
        raise AssertionError(label)


def valuation(n: int, prime: int) -> int:
    if n == 0 or prime < 2:
        raise ValueError("Nonzero integer and a prime >= 2 required.")
    exponent = 0
    while n % prime == 0:
        n //= prime
        exponent += 1
    return exponent


def exact_json(value: object) -> object:
    if isinstance(value, bool) or value is None or isinstance(value, str):
        return value
    if isinstance(value, (int, s.Integer)):
        return str(value)
    if isinstance(value, dict):
        return {str(k): exact_json(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [exact_json(v) for v in value]
    raise TypeError(f"Unsupported certificate value {type(value)}")


def main() -> dict[str, object]:
    c, d, th, ps, z, rt, lam, mu = s.symbols("c d theta psi z rt lambda mu")
    l, m, a, b, x = s.symbols("l m a b x")
    variables = (c, d, th, ps)
    p = 113
    identity_count = 0

    def zero(expr: s.Expr, label: str) -> None:
        nonlocal identity_count
        require(s.expand(expr) == 0, label)
        identity_count += 1

    def field(expr: s.Expr) -> s.Expr:
        return s.rem(s.expand(expr), rt**2 - 2, rt)

    def zero_field(expr: s.Expr, label: str) -> None:
        zero(field(expr), label)

    f = p * (-l**2 + 2*l*m + m**2)
    g = l**2 + 2*l*m - m**2
    h = 2*p*(l**2+m**2)
    zero(2*f**2 + 2*p**2*g**2 - h**2, "first conic parametrization")
    p1, p2, p3 = 15*c**2+52*c*d+30*d**2, 11*c**2+8*c*d+22*d**2, p*(c**2-2*d**2)
    q1, q2, q3 = th**2+2*ps**2, th**2+4*th*ps+2*ps**2, th**2-2*ps**2
    zero(f.subs({l:p1,m:p2}, simultaneous=True)-2*p3**2, "f=2s^2")
    zero(g.subs({l:q1,m:q2}, simultaneous=True)-2*q3**2, "g=2t^2")
    param_determinants = {}
    for name, forms, pair in (("first",(f,g,h),(l,m)),
                              ("p",(p1,p2,p3),(c,d)),
                              ("q",(q1,q2,q3),(th,ps))):
        monomials = (pair[0]**2,pair[0]*pair[1],pair[1]**2)
        coeffs = s.Matrix([[s.Poly(form,*pair).coeff_monomial(mon) for mon in monomials]
                           for form in forms])
        param_determinants[name] = coeffs.det()
        require(coeffs.det() != 0, f"{name} is an invertible Veronese parametrization")
    Q = [s.expand(p1-q1), s.expand(p2-q2)]
    mats = [s.hessian(q, variables)/2 for q in Q]
    pencil = s.factor((a*mats[0]+b*mats[1]).det())
    zero(pencil + 4*p*(a**4-6*a*a*b*b+b**4), "pencil determinant")
    disc = s.discriminant(pencil.subs({a:x,b:1}), x)
    require(disc == 2**26*p**6, "pencil discriminant")

    # Norm factorization and an L-rational conic point (L=Q(sqrt(2))).
    z0 = c-rt*d
    alpha0 = 4-11*rt
    zero_field(p1-(1+rt)*p2-alpha0*z0**2, "factorization of p1-epsilon*p2")
    B, A = 4+2*rt, 11-2*rt
    H = th**2+B*th*ps+2*ps**2-A*z**2
    zero_field(q1-(1+rt)*q2 + rt*(th**2+B*th*ps+2*ps**2), "q factorization")
    zero_field(-rt*H.subs(z,z0)-(Q[0]-(1+rt)*Q[1])*(-1), "conic restriction")
    t0, u0 = -1+rt, rt
    zero_field(H.subs({th:t0,ps:u0,z:1}, simultaneous=True), "conic rational point")
    alpha, beta = 1+3*rt, 3*rt
    ell = alpha*th+beta*ps-A*z
    q = lam**2+B*lam*mu+2*mu**2
    linear = alpha*lam+beta*mu
    par = {th:t0*q-2*lam*linear, ps:u0*q-2*mu*linear, z:q}
    zero_field(H.subs(par, simultaneous=True), "tangent conic parametrization")
    zero_field(ell.subs(par, simultaneous=True)+2*linear**2, "tangent pulls back to -2 square")
    ell_c = field(ell.subs(z,z0))
    u = th-11*c-4*d
    v = 3*th+3*ps+2*c+11*d
    zero_field(ell_c-u-rt*v, "tangent linear form")
    F = s.expand(u*u-2*v*v)
    zero_field(ell_c*ell_c.subs(rt,-rt)-F, "norm tangent")
    mixed = [s.Poly(F,variables).coeff_monomial(w) for w in (c*th,c*ps,d*th,d*ps)]
    require(s.gcd_list(mixed) == 2, "F remains a nonzero section at every odd prime")

    # Supplied finite-field witnesses, with actual nonzero Jacobian minors.
    jac = s.Matrix(Q).jacobian(variables)
    samples = [(3,(0,1,1,1)),(5,(1,3,3,1)),(7,(0,4,3,1)),
               (11,(2,2,10,1)),(13,(0,4,7,1)),(17,(2,5,6,1)),
               (19,(2,13,18,1)),(113,(0,1,14,16))]
    finite_rows = []
    for prime, coords in samples:
        require(s.isprime(prime), "residue modulus is prime")
        sub = dict(zip(variables, coords, strict=True))
        values = [int(q.subs(sub)) for q in Q]
        require(all(v % prime == 0 for v in values), f"equations mod {prime}")
        fvalue = int(F.subs(sub))
        require(fvalue % prime != 0 and coords[3] % prime != 0, f"avoid zeros/poles at {prime}")
        j = jac.subs(sub)
        minors = [(i,k,int(j[:,[i,k]].det())) for i,k in itertools.combinations(range(4),2)]
        nonzero = next((row for row in minors if row[2] % prime), None)
        require(nonzero is not None, f"smooth residue point {prime}")
        # A separate residue enumeration, not a Legendre-symbol library call.
        residues = {k*k % prime for k in range(1,prime)}
        symbol = 1 if (fvalue % prime) in residues else -1
        finite_rows.append({"prime":prime,"point":coords,"Q_values":values,
                            "F_value":fvalue,"F_mod_prime":fvalue%prime,
                            "nonzero_minor_columns":nonzero[:2],"minor":nonzero[2],
                            "unit_residue_symbol":symbol,
                            "Hilbert_F_113":symbol if prime==113 else 1})
    require(finite_rows[-1]["unit_residue_symbol"] == -1, "nontrivial local contribution")
    require(int(jac[:,[2,3]].det().subs(dict(zip(variables,samples[-1][1],strict=True)))) % p == 71,
            "recorded 113-adic minor")

    # Genuine 2-adic lifting (not just a modular point).
    T = s.symbols("T")
    h2 = T**4-97*T**2+392
    sub2 = {c:1,d:1,th:T,ps:-14/T}
    for qi in Q:
        zero(s.cancel(qi.subs(sub2)*T**2)+h2, "2-adic equations reduce to h2")
    hv, hd = int(h2.subs(T,5)), int(s.diff(h2,T).subs(T,5))
    require(valuation(hv,2) == 7 and valuation(hd,2) == 1, "strict Hensel valuations")
    require(valuation(hv,2) > 2*valuation(hd,2), "Hensel strict inequality")
    norm_on_branch = s.cancel(F.subs(sub2)*T**2)
    require(s.gcd(h2,norm_on_branch) == 1, "no zero of F on the selected branch")
    resultant = s.resultant(h2,norm_on_branch,T)
    require(resultant != 0, "nonzero resultant")
    require(p % 8 == 1, "113 is a 2-adic square")
    require(0 < 7841 < 97**2 and 97**2-4*392 == 7841, "real positive quadratic roots")
    # For q>=23, q+1-2sqrt(q)>12: check endpoint exactly and monotonicity is proved in report.
    require((23-11)**2 > 4*23, "Hasse endpoint exceeds forbidden divisor bound")

    # Isogeny normalization and torsion bounds are independent of L-values.
    xx, yy = s.symbols("xx yy")
    xu = xx-p*p/xx
    yv = yy*(1+p*p/(xx*xx))
    reduce_A = lambda e: s.rem(s.fraction(s.cancel(e))[0], yy**2-xx**3+p*p*xx, yy)
    zero(reduce_A(yv**2-xu**3-4*p*p*xu), "phi maps A to B")
    xd = (xu+4*p*p/xu)/4
    yd = yv*(1-4*p*p/xu**2)/8
    slope = (3*xx*xx-p*p)/(2*yy)
    xdouble = slope**2-2*xx
    ydouble = slope*(xx-xdouble)-yy
    zero(reduce_A(xd-xdouble), "hatphi phi has doubling x")
    zero(reduce_A(yd-ydouble), "hatphi phi has doubling y")
    reduction_counts = {
        prime: 1+sum((y*y-x*x*x+p*p*x)%prime==0
                     for x in range(prime) for y in range(prime))
        for prime in (3,5)
    }
    require(reduction_counts == {3:4,5:4}, "rational torsion bounded by four")

    # A rejected twist: no primitive point of C2 with xi2=1 modulo 16.
    modulus = 16
    square_roots: dict[int,list[int]] = {}
    for k in range(modulus):
        square_roots.setdefault(k*k % modulus,[]).append(k)
    rejected_count = 0
    for ll,mm in itertools.product(range(modulus),repeat=2):
        ff = p*(-ll*ll+2*ll*mm+mm*mm) % modulus
        gg = (ll*ll+2*ll*mm-mm*mm) % modulus
        for ss,tt in itertools.product(square_roots.get(ff,[]),square_roots.get(gg,[])):
            if any(k%2 for k in (ll,mm,ss,tt)):
                rejected_count += 1
    require(rejected_count == 0, "wrong xi2=1 has no primitive residue solution mod16")

    # Negative tests: changed point or sign is rejected by the decisive algebra.
    bad = dict(zip(variables,(0,1,15,16),strict=True))
    require(any(int(qi.subs(bad)) % p for qi in Q), "perturbed 113-adic point fails")
    require(s.cancel(Q[1].subs({c:1,d:1,th:T,ps:14/T})*T**2) != -h2,
            "wrong 2-adic sign fails")
    require(valuation(-9,113)==0 and 113%4==1 and 2*9**2-7**2==113,
            "prior first-pairing hypotheses")
    require(s.legendre_symbol(-9,113)==1,"prior first pairing is zero")

    return {"status":"completed exact certificate checks; not formal/expert verification",
            "python":platform.python_version(),"sympy":s.__version__,
            "identities_checked":identity_count,
            "conic_parametrization_determinants":param_determinants,
            "quadrics":[str(qi) for qi in Q],"pushout_numerator":str(F),
            "pencil":str(pencil),"pencil_discriminant":disc,
            "mixed_coefficients":mixed,"local_certificates":finite_rows,
            "two_adic":{"polynomial":str(h2),"at_5":hv,"derivative_at_5":hd,
                         "valuations":[valuation(hv,2),valuation(hd,2)],
                         "F_numerator":str(norm_on_branch),"resultant":resultant,
                         "Hilbert_F_113":1},
            "real_Hilbert_F_113":1,
            "all_other_primes":"smooth reduction plus Hasse bound and Bezout; see written proof",
            "global_pairing_sign":-1,
            "torsion_reduction_counts":reduction_counts,
            "rejected_twist_modulus":modulus,"rejected_primitive_count":rejected_count,
            "Selmer_orders_from_proved_group_data":{
                "E113":[4*2**(2*min(j,2)) for j in range(1,5)],
                "E41":[4*2**(2*j) for j in range(1,5)]},
            "scope":"single curve E113; universal BSD remains unresolved"}


if __name__ == "__main__":
    print(json.dumps(exact_json(main()),indent=2,sort_keys=True))
