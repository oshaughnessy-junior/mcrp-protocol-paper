---
artifact_role: outward-facing-blog-seed
authors: [Codex, junior]
status: mature-private-draft
date: 2026-08-21
series_part: 9
publication_status: private-not-approved
---

# Review as a distributed workflow

“Please review this paper” is an underspecified work order.

A scientific release may need checks of data custody, execution, statistical design, software, instrument calibration, uncertainty treatment, domain interpretation, ethics, and adversarial alternatives. No single reviewer is guaranteed to cover all of them, and a prose report rarely makes the uncovered scope obvious. MCRP therefore treats review as a distributed workflow whose coverage, dependencies, and gaps remain inspectable.

The proposal is not to replace journals or transfer scientific authority to a protocol. It is to represent a review request as a versioned object naming the exact release and claims, questions, required competencies, conflict policy, confidentiality rules, available resources, deadline, and completion rule. A coordinator can then decompose that request into bounded work objects. Each resulting report records its method, evidence inspected, exclusions, dependencies, and unresolved questions.

This design draws on established prior art rather than claiming trust registries, transparency services, decentralized notifications, identifiers, content-addressed assertions, or publish-review-curate as MCRP novelties. Relevant foundations include [W3C Verifiable Credentials](https://www.w3.org/TR/vc-data-model-2.0/), [SCITT transparency services](https://www.rfc-editor.org/rfc/rfc9943.html), [Linked Data Notifications](https://www.w3.org/TR/ldn/), [Activity Streams](https://www.w3.org/TR/activitystreams-core/), [WebSub](https://www.w3.org/TR/websub/), [COAR Notify](https://coar-notify.net/specification/1.0.1/), and the established [COAR publish-review-curate model](https://coar-repositories.org/what-we-do/repositories-and-publishing/). Persistent identity and contribution vocabularies can likewise refer to [ORCID peer-review records](https://support.orcid.org/hc/en-us/articles/360006971333-Peer-Reviews), [ROR](https://ror.org/about/), and [CRediT](https://credit.niso.org/).

## Worked example: a complete review request

Consider a fictional release, `R-17`, reporting a search for a weak transient signal in an open detector dataset. Its principal claim, `C-4`, is: “Under pipeline version 3.2 and the declared event-selection policy, the candidate population is inconsistent with the stated background model at the reported level.” The request does not ask reviewers to determine an unrestricted truth. It asks whether specified evidence supports a bounded claim under a declared acceptance contract.

The review-request object contains:

- Target: release `R-17`, claim version `C-4.1`, software release `P-3.2`, and evidence manifest `E-9`.
- Questions: Can the computation be reconstructed? Is the statistical model applied as declared? Is restricted calibration material handled correctly? Does the interpretation remain within the analysis scope?
- Competencies: workflow execution, statistical inference, detector calibration and data custody, and domain interpretation.
- Conflicts: reviewers disclose financial, supervisory, institutional, and recent-collaboration relationships; the coordinator records recusals and routing decisions.
- Confidentiality: the public release is open, but calibration notebook `K-2` contains embargoed operational details and may be accessed only by approved data reviewers inside the custodian’s environment.
- Resources: content-addressed public artifacts, a sealed restricted-data workspace, declared compute limits, and a contact channel for clarification.
- Deadline: reports due 30 days after assignment; questions pause only the affected work object.
- Completion rule: all four work objects must return a signed report or an explicit unable-to-complete disposition; required fields and conflict declarations must be present. Completion does not require agreement.

The coordinator decomposes the request into exactly four work objects:

1. **Execution reconstruction.** An execution reviewer retrieves `P-3.2`, verifies referenced artifact digests, rebuilds the declared environment, and runs the public workflow against `E-9`. The report distinguishes observed outputs from explanations proposed by the reviewer. A checksum match is an automated observation; “the workflow adequately represents the intended analysis” is a scientific or methodological disposition requiring a qualified human.

2. **Statistical assessment.** A statistical reviewer checks likelihood construction, nuisance parameters, selection effects, diagnostics, and the mapping from computed results to `C-4.1`. An agent may enumerate model variants and run declared sensitivity jobs, but its outputs remain agent reports or policy projections until a human reviewer evaluates and adopts a stated portion.

3. **Calibration and custody review.** An authorized reviewer enters the restricted workspace, examines `K-2`, checks provenance and fitness-for-use assertions, and exports only a structured disposition approved by the data custodian. The work object forbids copying restricted inputs into public logs, agent prompts, or content-addressed public stores. Its public report may say which controlled procedures were performed and which questions remain unresolved without disclosing protected material.

4. **Domain and adversarial interpretation.** A domain reviewer tests whether `C-4.1` exceeds the evidence, inventories plausible alternative explanations, and identifies counterevidence that would matter. This object may cite the other three reports but cannot silently convert their procedural findings into endorsement of the scientific claim.

Suppose the execution reviewer reconstructs the published outputs, the statistical reviewer identifies an unreported sensitivity to one prior, the custody reviewer reports conformant handling but cannot disclose a calibration exception under embargo, and the domain reviewer concludes that the wording of `C-4.1` is too broad. The completion rule is met because every assigned object returned a conformant disposition. Scientific agreement is not met, nor was it required. The coverage view shows one reconstructed workflow, one statistical objection, one confidentially bounded custody finding, and one requested claim revision. It must not average these into a score.

If a qualified decision-maker later accepts or rejects a claim for a particular release, an attestation can bind the exact decision context as `(claim version, acceptance-contract version, evidence-set digest, release digest, role, decision)`. This binding records what was decided by whom and under which contract; it does not establish truth or erase dissent.

## Automation without delegated authority

A living, self-updating event network can make review at scale tractable. Services can announce new releases, assignments, reports, supersessions, withdrawals, access changes, and dependency updates. Agents can inventory objects, retrieve permitted evidence, compare versions, execute declared procedures, monitor deadlines, and draft structured reports. Content-addressed approaches such as [Nanopublications](https://nanopub.net/) and [Trusty URIs](https://trustyuri.net/) illustrate established mechanisms for binding assertions to identifiable content.

Yet automation cannot silently promote an observation, policy projection, or agent report into a scientific disposition. Qualified humans retain authority over scientific judgments, adoption of agent-assisted findings, confidentiality exceptions, and final scope statements. A human adopting agent-assisted work must name the material examined, the assistance used, and the scope for which responsibility is accepted. Identity infrastructure also needs explicit governance because identity multiplicity and the classic [Sybil attack](https://www.microsoft.com/en-us/research/publication/the-sybil-attack/) remain relevant threats; registries alone do not settle competence or independence.

## Limitations

This workflow depends on honest scoping, usable metadata, competent reviewers, enforceable access controls, and communities willing to expose missing coverage. Confidential evidence may prevent outsiders from reproducing a reviewer’s reasoning. Decomposition can create boundary errors, duplicated effort, or questions that fall between work objects. Structured records can document conflicts without resolving them, and completion rules can reward paperwork if their requirements are poorly chosen. Automation may also amplify routing mistakes or produce an appearance of comprehensiveness unsupported by human examination.

Review therefore ends with explicit dispositions, gaps, and disagreements—not a manufactured consensus. Part 10 follows those disagreements through an event timeline and asks how retaliation, confidentiality failures, and procedural abuse can be surfaced and constrained without treating dissent as noise.
