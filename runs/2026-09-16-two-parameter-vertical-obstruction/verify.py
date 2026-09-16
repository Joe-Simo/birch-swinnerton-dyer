from __future__ import annotations
from contextlib import redirect_stdout
from io import StringIO
from importlib.util import module_from_spec, spec_from_file_location
from math import lcm
from pathlib import Path
import json

# Reuse only the already-audited finite-field/group-law primitives from H22.
# Its horizontal research program is suppressed while loading.
base_path = Path(__file__).resolve().parent.parent / "2026-09-16-two-parameter-horizontal-obstruction" / "verify.py"
spec = spec_from_file_location("bsd_h22_verify", base_path)
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load H22 verifier")
h22 = module_from_spec(spec)
with redirect_stdout(StringIO()):
    spec.loader.exec_module(h22)

leg = h22.leg
seed = h22.seed
add = h22.add
mul = h22.mul
order = h22.order
first_stage = h22.first_stage
lift_surface = h22.lift_surface
E_to_q = h22.E_to_q
phi = h22.phi
fplus = h22.fplus

def local_constraint_vertical(p: int):
    if leg(137, p) != -1:
        raise ValueError("137 must be nonsquare for this checker")
    P, Q = seed(p)
    M = order(mul(-2, Q))
    records = {}
    Ns = []
    amb_m = 0
    amb_n = 0
    for m in range(M):
        try:
            x1, y1, w1 = first_stage(p, m)
            P1, Q1 = lift_surface(x1, y1, w1, p)
            N = order(mul(-2, P1))
            Ns.append(N)
            good = set()
            ambiguous = set()
            for n in range(N):
                try:
                    Qn = add(Q1, mul(-2*n, P1))
                    xs, rps = E_to_q(P1, 1)
                    ys, rms = E_to_q(Qn, -1)
                    W = rps * rms
                    if W.b:
                        raise ValueError("vertical descent did not return to base field")
                    x2, _, _ = phi(xs, ys, W.a, p)
                    F = fplus(x2, p)
                    if F != 0 and leg(F, p) == leg(313, p):
                        good.add(n)
                except Exception:
                    ambiguous.add(n)
                    amb_n += 1
            records[m] = (N, good | ambiguous)
        except Exception:
            records[m] = None
            amb_m += 1
    Np = 1
    for N in Ns:
        Np = lcm(Np, N)
    allow = {}
    for m, rec in records.items():
        if rec is None:
            allow[m] = None
        else:
            N, good = rec
            allow[m] = {n for n in range(Np) if n % N in good}
    return {"p":p, "M":M, "N":Np, "allow":allow, "amb_m":amb_m, "amb_n":amb_n}

def combine(states: set[tuple[int,int]], GM: int, GN: int, constraint):
    LM = lcm(GM, constraint["M"])
    LN = lcm(GN, constraint["N"])
    out: set[tuple[int,int]] = set()
    for m0, n0 in states:
        for m in range(m0, LM, GM):
            allowed = constraint["allow"][m % constraint["M"]]
            for n in range(n0, LN, GN):
                if allowed is None or n % constraint["N"] in allowed:
                    out.add((m,n))
    return out, LM, LN

def period_filter_vertical(p: int, states: set[tuple[int,int]], GM: int, GN: int):
    if leg(137, p) != -1:
        raise ValueError("137 must be nonsquare for period filter")
    P, Q = seed(p)
    if mul(-2*GM, Q) is not None:
        raise AssertionError(f"{GM} is not a first-stage period at {p}")
    cache = {}
    unresolved_m = set()
    for m, _ in states:
        mm = m % GM
        if mm in cache or mm in unresolved_m:
            continue
        try:
            x1, y1, w1 = first_stage(p, mm)
            P1, Q1 = lift_surface(x1, y1, w1, p)
            if mul(-2*GN, P1) is not None:
                raise AssertionError(f"{GN} is not a second-stage vertical period at {p}")
            cache[mm] = (P1, Q1)
        except (ZeroDivisionError, ValueError):
            unresolved_m.add(mm)
    out = set()
    eliminated = []
    for m, n in states:
        mm = m % GM
        if mm in unresolved_m:
            out.add((m,n))
            continue
        P1, Q1 = cache[mm]
        try:
            Qn = add(Q1, mul(-2*n, P1))
            xs, rps = E_to_q(P1, 1)
            ys, rms = E_to_q(Qn, -1)
            W = rps * rms
            if W.b:
                raise ValueError("vertical descent did not return to base field")
            x2, _, _ = phi(xs, ys, W.a, p)
            F = fplus(x2, p)
            if F != 0 and leg(F, p) == leg(313, p):
                out.add((m,n))
            else:
                eliminated.append((m,n))
        except (ZeroDivisionError, ValueError):
            out.add((m,n))
    return out, eliminated, len(unresolved_m)

target_classes = (0,12,37,62,74,76,80,86,92,122,152,158,164,168)
states = {(0,n) for n in target_classes}
GM, GN = 1, 170
rows = []

def add_complete(p: int):
    global states, GM, GN
    c = local_constraint_vertical(p)
    states, GM, GN = combine(states, GM, GN, c)
    rows.append({
        "kind":"complete", "p":p, "local_M":c["M"], "local_N":c["N"],
        "ambiguous_m":c["amb_m"], "ambiguous_n":c["amb_n"],
        "global_M":GM, "global_N":GN, "survivors":len(states)
    })

def add_filter(p: int):
    global states
    before = len(states)
    states, eliminated, unresolved = period_filter_vertical(p, states, GM, GN)
    rows.append({
        "kind":"period_filter", "p":p, "before":before,
        "eliminated":len(eliminated), "unresolved_m":unresolved,
        "global_M":GM, "global_N":GN, "survivors":len(states)
    })

for p in (13,31,29,23,71,79,127,157,179,191,239,359):
    add_complete(p)
for p in (1151,2719):
    add_filter(p)

add_complete(53)
for p in (67,271,349,1223,4079,12239):
    add_filter(p)

add_complete(199)
add_filter(599)

add_complete(113)
for p in (1699,2399,15299,89,122399):
    add_filter(p)

add_complete(83)
for p in (1427,11423,21419,5711,1399,1259):
    add_filter(p)

expected_final_eight = {
    (85172,203272),(85172,631672),(85172,1060072),(85172,1488472),
    (192272,203272),(192272,631672),(192272,1060072),(192272,1488472),
}
if (GM, GN) != (214200, 1713600):
    raise AssertionError((GM,GN))
if states != expected_final_eight:
    raise AssertionError(("final-eight mismatch", sorted(states)))

# Preserve the exact final regular values before eliminating them.
final_values = []
p = 42101
for m, n in sorted(states):
    P, Q = seed(p)
    if mul(-2*GM, Q) is not None:
        raise AssertionError("final first-stage period failure")
    x1, y1, w1 = first_stage(p, m)
    P1, Q1 = lift_surface(x1, y1, w1, p)
    if mul(-2*GN, P1) is not None:
        raise AssertionError("final second-stage period failure")
    Qn = add(Q1, mul(-2*n, P1))
    xs, rps = E_to_q(P1, 1)
    ys, rms = E_to_q(Qn, -1)
    W = rps * rms
    if W.b:
        raise AssertionError("final descent failure")
    x2, _, _ = phi(xs, ys, W.a, p)
    F = fplus(x2, p)
    final_values.append({
        "m":m, "n":n, "x":x2, "Fplus":F,
        "character":leg(F,p), "target_character":leg(313,p)
    })
if {(v["x"],v["Fplus"],v["character"],v["target_character"]) for v in final_values} != {(15355,38394,1,-1)}:
    raise AssertionError(final_values)

add_filter(42101)
if states:
    raise AssertionError(sorted(states))

print(json.dumps({
    "status":"passed",
    "target_classes_mod_170":list(target_classes),
    "final_moduli":[GM,GN],
    "rows":rows,
    "final_eight":final_values,
    "survivors":0,
    "conclusion":"No integer pair (m,n) in H^m Phi V^n Phi can have final squareclass 313."
}, indent=2))
