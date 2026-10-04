# Review 1615 disposition

4 October 2026. Proposed source revision; no new empirical or institutional validation.

| Issue | Action | Residual boundary |
|---|---|---|
| Formal invariants/proofs requested | Preserve existing Appendix A S1/S2 definitions/proofs; add A.6 explicit transitions and T1–T3 proof sketches. | Trusted identity, event, epoch and serialized-update premises; not distributed verification or scientific truth. |
| Sufficiency against stale/silent-replay failures | New composed reducer and six finite traces: known invalidation, late completion, actor gate, successor replay, query expiry, missing-event negative case. | Cannot detect undisclosed changes or forged/restamped trusted assertions; cached state is not query currentness. |
| Modes/levels scattered | Section 6 consolidated 4×4 table and caps/scope/withheld explanation. | Mode never awards assurance; human and scientific adequacy unchanged. |
| Agent boundary unclear | Section 5.3 delegation/attribution and recommendation→verifier→human example. | No authenticated human/independence inference from strings, no claimed attention savings. |
| Manual transformation | Named trust leaf/restricted dependency, inspected versus unavailable boundary and mandatory-unknown rule. | No automatic discovery of omitted manual steps. |
| Manipulating verifier | Clarify enforced-path protections and hidden collusion/admin limit. | Real governance and independent custody remain prerequisites. |
| Novelty/direct comparison | Preserve existing closest-work discussion and unperformed-comparison limitation; do not invent competitor deficits. | No superiority, necessity or comprehensive standards-conformance claim. |

Files: `paper/position-paper.md`, `examples/lifecycle-transitions/{transitions.py,test_transitions.py,README.md,LICENSE}`, and response/disposition documents. New code license follows sibling MIT code. No change to the existing assurance algorithm. Validation: 6 transition +22 assurance +16 revision-semantics tests passed. Independent internal red report is separate; these assertions do not preempt it.
