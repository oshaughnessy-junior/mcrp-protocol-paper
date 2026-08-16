# Logical claims audit

| ID | Candidate manuscript claim | Type | Required support | Current disposition |
|---|---|---|---|---|
| C1 | Executable packaging and provenance do not alone establish that evidence warrants a scientific claim. | conceptual synthesis | Official scope/limitations of workflow and provenance standards plus reproducibility-review literature | retain, cite precisely |
| C2 | Existing work already represents claim/evidence and execution/provenance graphs. | prior-art boundary | EVI, Micropublications, Nanopublications, PROV-O, Workflow Run RO-Crate, Paper-replication | retain; blocks broad novelty |
| C3 | MCRP proposes prospective, claim-versioned acceptance contracts. | protocol contribution | Frozen normative MCRP specification and closest-work comparison | conditional |
| C4 | MCRP enforces state transitions outside the generating agent. | implementation/design claim | State-machine specification plus validator/controller evidence | evidence needed |
| C5 | Claim attestations can become stale or be revoked when dependencies change. | protocol contribution | Dependency semantics, test cases, and review record | evidence needed |
| C6 | MCRP improves review completeness, correctness, or speed. | empirical benefit | Controlled comparison with declared baselines and metrics | prohibited in position draft |
| C7 | MCRP conformance establishes scientific validity. | invalid inference | none | prohibited |

## Argument risks

- **Composition fallacy:** integrating known graph and provenance standards is not itself novel.
- **Identity/validity confusion:** signing bytes establishes attribution, not truth or independence.
- **Execution/epistemic confusion:** a green run establishes neither complete evidence coverage nor sound interpretation.
- **Retrospective thresholding:** acceptance predicates written after results are known can encode self-validation.
- **Overgeneralization:** evidence rules differ across computational, observational, and experimental disciplines.

