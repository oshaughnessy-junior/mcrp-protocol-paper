# Companion post brief

## Purpose

Introduce the MCRP technical supplement to a human reader in a short, high-density post. This is a distinct deliverable from the post about agent meetings and self-improvement loops.

## Authors

Codex and junior.

## Hook

Computational review often verifies the wrong object: a moving repository, an author-controlled rerun, or a result whose claim, evidence, code, environment, and approval no longer refer to the same version. MCRP is a design sketch for binding those pieces to one immutable release and making every remaining trust boundary visible.

## Four-paragraph structure

1. State the version-binding problem with one concrete example: a workflow changes after review but the old approval remains visible.
2. Give the residual proposal in one sentence: prospectively fixed claim tests, external enforcement, release-scoped approvals, and explicit invalidation when dependencies change.
3. State what is not new and not demonstrated: evidence/provenance graphs have substantial prior art; MCRP has not shown better reviewer performance, lower effort, or cross-domain usability.
4. Link the technical supplement as an auditable design record and invite evaluation or reuse, not adoption as a standard.

## Required boundaries

- Call the PDF a technical supplement, not a paper submission or validated protocol.
- Do not claim novelty for graphs, provenance, agent identity, signatures, staged review, or independent execution.
- Attribute the post and supplement to Codex and junior.
- Keep the meetings/self-improvement post separate.
- Do not feature the synthetic reference implementation unless it materially clarifies the lifecycle; if mentioned, describe it only as a fixture test of encoded invariants.
