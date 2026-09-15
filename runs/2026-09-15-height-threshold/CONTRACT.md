# H6: quantitative height extraction and congruence reconstruction

Status: no complete BSD solution or candidate.
Base: private branch research/h2-endpoint-20260914 observed at a340e2213a834fdfc45dd68874fab8501e8256ce; local root /mnt/data/04-birch-swinnerton-dyer.
The original prompt was read from the original archive. All preexisting local files are hashed in preserved-inputs.json and remain unchanged. H5 is the immediate dependency; older first-isogeny errors corrected in H3 are not reused.

## Proof targets
1. For a compatible rational Kummer tower, prove that sub-4^m canonical-height growth forces a single rational representative; determine the sharp universal constant relative to the shortest positive Mordell-Weil height. Keep the existence of rational representatives distinct from existence of local Selmer lifts.
2. Replace that circular starting requirement by an unconditional-to-define local object: minimum coordinate size of primitive congruence solutions to a fixed intersection of two quadrics. Prove a residual-versus-modulus criterion that certifies an exact rational point. Audit whether existing covering minimisation/height comparison theorems supply the necessary bound.
3. Use the locally soluble nonrational 17 covering as a negative control and an explicit rational point on the corresponding 41 covering as a positive control. Neither is a new BSD case. Do not extrapolate local-only obstructions to the persistent-descent subclass.

## Accepted finite experiments, before execution
Tower scalar fixtures: levels 1..64 for the 2-adic inverse 1/3 and sparse digits at positions 2,4,8,16,32,64. Enumerate centered representatives for levels up to10; this does not certify an infinite theorem by itself.
Quadrics: Q1=v^2-w^2-z^2; Q2=u^2-p*w^2+p*z^2. For p=17 enumerate minimum max(|u|,|v|,|w|,|z|) among nonzero congruence solutions modulo 2^k, k=1..16, within coordinate cap512. Require gcd(u,v,w,z,2^k)=1. For p=41 use k=1..17 and cap41, justified by the proposed exact point (41,29,21,20), which must first be verified. All signs are covered because these equations use only squares. A found global minimum is exhaustive within the cap, and also absolute if a solution within the cap exists; a cap miss is inconclusive.
The independent checker will enumerate (u,v) and solve the doubled square congruences with BOTH modulo-2^k branches, unlike the first checker enumerating (w,z). Compare only heights, not tied minimizers.
Use exact bigint/integer arithmetic. Polynomial identities use established SymPy. Focused failure tests must reject nonprimitive vectors and invalid equation residuals.

## Evidence limits
Infinite quantitative lemmas and local-to-global implications require written proofs. Finite tests check encodings and scalar examples. No numerical canonical heights, full general BSD, new Sha-finiteness theorem, formal-kernel proof, or independent expert review is claimed. Sources must be primary/authenticated at exact locators. Additional spending is zero; no external contacts or public publication.

## Registered follow-up after the initial minimum run
The minimum experiment returned the known C41 point as the first minimum at level11. Verify the monotonicity-plus-fixed-witness argument extending that minimum to all later levels; this is not extrapolation of finite data. Add the single explicit equality-bound negative control at M=18, vector(1,1,0,1), to distinguish strict from weak residual inequalities. Verify the generic Pythagorean substitution and its remaining quartic, without claiming a global solver for that quartic.
