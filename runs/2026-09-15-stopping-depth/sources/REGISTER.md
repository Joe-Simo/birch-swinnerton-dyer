# H4 source ledger — checked 2026-09-15

The mathematical claims and their roles are kept separate below. Primary papers were read through the web tool; full PDF acquisition into the container failed with a DNS-resolution error for all four attempted arXiv downloads. Therefore there is no retained-source content hash or purported local PDF cache. Some PDF screenshots also failed with cache misses; successfully rendered Tunnell pages supplied the scanned formulas. No OCR was used. This file contains extraction/translation notes, not copies of the sources.

## [F] Fisher — filtration and explicit functions

Tom Fisher, *Higher descents on an elliptic curve with a rational 2-torsion point*, arXiv:1509.03234v1, 10 September 2015; Math. Comp.86 (2017),2493–2518.
Locator: https://arxiv.org/pdf/1509.03234v1

Read Section2 pp.4–5, Section3 and Section5, including the displayed pushout list on p.13. Theorem2.1 supplies odd alternating pairings and even cross-pairings with exactly the stated next-stage kernels. The subsequent Sha image sequences give formula(7) of our record after identifying phihat(B) inside A. The source's p denotes the isogeny degree; it is2 here, whereas our p is the odd curve parameter. We use S on E' coordinates. Function f_2 lives on C1. These are established external inputs, not a formal-kernel verification.

## [M] Mortenson — representation identity

Eric Mortenson, *Threefield identities and simultaneous representations of primes by binary quadratic forms*, arXiv:1208.1412v1, 7 August2012; J. Number Theory133 (2013),3902–3920; DOI10.1016/j.jnt.2013.05.001.
Locators: https://arxiv.org/abs/1208.1412 ; https://arxiv.org/pdf/1208.1412

The sole arXiv version was confirmed from submission history; its explicit v1-PDF URL failed, while the unversioned PDF was readable. Theorem2.1 and its proof at the end of Section4, pp.10–11, give the exact32/64-form representability rule used in H4. Mortenson proves the rule himself by weighted theta identities, so this is a primary proof, not just a citation to Kaplansky. Our v is his positive y in p=x^2+16y^2. His two signed-y solutions become one positive solution here. Kaplansky's original article was not acquired. No novelty is inferred from that acquisition gap.

## [T] Tunnell — analytic normalization and local factors

J.B. Tunnell, *A Classical Diophantine Problem and Modular Forms of Weight3/2*, Invent. Math.72 (1983),323–334; DOI10.1007/BF01389327.
Locator: https://sites.math.rutgers.edu/~zeilberg/EM22/JT1983.pdf

Scanned pp.328–330 were inspected as screenshots. Theorem3 gives L(E_p,1)=c_p^2 beta/(4 sqrt(p)), with beta the integral stated in H4. The remark on p.330 states the odd-parameter local factors2 at2 and4 at each odd dividing prime, and rational torsion order4. The source presents the resulting Sha formula as conjectural in1983: it becomes a theorem here only through [BF], not by relabeling Tunnell's conjecture. The displayed table uses division by the divisor count, so the raw coefficient at17 is-4, not-2. Our raw c_p agrees with H3 and the exact q-product.

## [BF] Burungale–Flach — refined rank-zero CM formula

Ashay Burungale and Matthias Flach, *The conjecture of Birch and Swinnerton-Dyer for certain elliptic curves with complex multiplication*, arXiv:2206.09874v3, 4 September2023.
Locators: https://arxiv.org/abs/2206.09874 ; https://arxiv.org/pdf/2206.09874v3

Theorem1.1, Corollary2 and its proof were read; metadata and v3 date were checked. Hypotheses include maximal-order CM, the abelian torsion-extension condition and nonzero central value over the CM field. Corollary2 descends to the conjugation-fixed field; its following paragraph explicitly includes all CM curves over Q with nonzero central value. H4 checks these conditions with K=Q(i), F=K, F+=Q. The statement has no exclusion at2. This supplies full rank-zero BSD and finiteness, but not any claim for the zero-coefficient cases. Application audited; the complete original proof is not independently rederived.

## [BT] Burungale–Tian — converse at2

Ashay A. Burungale and Ye Tian, *A rank zero p-converse to a theorem of Gross–Zagier, Kolyvagin and Rubin*, arXiv:2506.03465v2, 11 October2025.
Locator: https://arxiv.org/pdf/2506.03465v2

Theorem1.1, its rational-descended assertion and the CM-newform formulation Theorem3.1 were checked. Corank-zero p-infinity Selmer implies central nonvanishing, for any prime, including2. H4 uses this only after finite stopping has proved rank zero and finite2-primary Sha. It is not a rank-two converse. In particular it does not identify the source of a persistent corank-two Selmer group.

## Overlap context, not a proof dependency

Shisong Xu, *Representation Defects and Cassels Pairings for Congruent Number Curves: Rédei Symbols and Governing Fields*, arXiv:2609.03238v2, 5 September2026.
Locator: https://arxiv.org/abs/2609.03238

Metadata and the stated CM-BSD-based coefficient/pairing comparison were checked. The readable unversioned text was inspected for overlap; a pinned-v2 PDF fetch failed. We have not audited the full proof, Qin's normalization or the claimed governing fields. It is not used to establish H4. Its broader comparison is a further reason not to market H4 as a newly discovered relationship.

Search scope: primary arXiv papers, author scans and references around first Cassels pairings, binary32/64-form representations, CM rank-zero BSD and the2-converse. Consensus was already quota-exhausted and was not repeatedly invoked; no Scite verification is claimed. This is an overlap check, not an exhaustive novelty search.
