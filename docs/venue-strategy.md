# Publication-defer and outward-facing plan

## Decision

Defer scholarly publication. No journal, conference, or arXiv submission is planned.

The closest-work review shows that the broad territory is already occupied: claim–evidence graphs, machine-readable assertions, provenance, workflow-run packaging, independent execution, external completion checks, agent identity, and staged review all have substantial precedents. MCRP's residual focus—a prospective, externally enforced, claim-versioned lifecycle—is narrower, has not been comparatively evaluated, and does not currently justify the novelty and validation risk of a scholarly submission.

The existing PDF should instead be maintained as an outward-facing, literature-grounded technical supplement authored by Codex. Its purpose is to expose a design record, precise limitations, closest-work comparisons, and an evaluation agenda for discussion and possible reuse. It must not be framed as establishing priority, consensus, conformance, scientific validity, or improved review outcomes.

## Outward-facing artifact

The release unit should contain:

- the rendered technical-supplement PDF and its exact Markdown, metadata, and bibliography sources;
- the closest-work matrix and claim ledger needed to audit consequential statements;
- the synthetic protocol and reference artifacts only when they are sanitized, licensed, and version-bound;
- an explicit status statement naming Codex as author and identifying any human editorial or release review;
- a short landing-page or blog introduction that links to the supplement and repeats its non-validation limits.

The PDF may retain its academic structure and citations because that structure makes the design record auditable. Retaining scholarly form does not make it a journal or arXiv submission.

## Release gates

An outward-facing release is a go only when all of the following are satisfied:

1. **Framing:** the README, metadata, PDF, and landing text consistently call the artifact a technical supplement and do not imply a submitted or accepted paper.
2. **Attribution:** Codex authorship is explicit, and human editorial or release review is described accurately without implying scientific endorsement.
3. **Claim discipline:** the supplement makes no graph-novelty, effectiveness, consensus-standard, certification, or scientific-validity claim.
4. **Literature integrity:** every cited key resolves, primary sources support the prose at its stated strength, and the closest-work comparison remains current as of the release date.
5. **Limitations:** all present limitations and `[EVIDENCE NEEDED: ...]` markers remain visible unless resolved by auditable evidence; gaps are not polished into claims.
6. **Artifact integrity:** the PDF builds from the released source, rendered output is inspected, and the exact release is content-identified.
7. **Privacy:** no private paths, repository names, issue content, agent or session identifiers, credentials, personal data, restricted scientific material, or operational topology are exposed.
8. **Licensing:** documentation, code, data, and third-party materials have compatible and explicit release terms.
9. **Human release approval:** a human reviews the final outward-facing bundle and authorizes public release.

Failure of any gate is a no-go for outward release. The supplement can remain private until the issue is resolved.

## Communication posture

The outward narrative should lead with the practical design problem: evidence and approvals can become detached from the exact claim and release they assessed. It should then explain the proposed lifecycle, acknowledge the closest collisions, and direct readers to the supplement for details. It should avoid journal-style language such as “novel contribution,” “state of the art,” or “validated framework.”

A concise description is:

> MCRP is a design proposal for binding declared scientific claims, execution evidence, and separately authorized checks to immutable releases. This technical supplement documents the proposal, its relationship to prior work, a synthetic implementation, and the evidence still needed to evaluate it.

## Conditions for reconsidering a scholarly paper

Publication should be reconsidered only if later work changes the evidentiary position substantially. A new assessment would require, at minimum:

- multiple real, public workflows with materially different resource and access profiles;
- a repository-plus-instructions baseline and relevant provenance or independent-execution baselines;
- preregistered or otherwise prospectively fixed metrics and stopping rules;
- defect-detection results with adjudication of false findings;
- reviewer-effort and inter-reviewer-agreement measurements;
- ablations for the lifecycle elements claimed to matter;
- at least one external reproduction attempt;
- released data and artifacts sufficient to regenerate every reported result;
- appropriate ethics determination for any study of human reviewers; and
- a refreshed closest-work analysis showing a contribution beyond composition and documentation.

Meeting these conditions would trigger a fresh go/no-go review; it would not create an automatic publication commitment. Until then, former candidate venues are archival research notes, not active targets.
