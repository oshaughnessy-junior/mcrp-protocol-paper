---
artifact_role: outward-facing-blog-draft
authors: [Codex, junior]
status: mature-private-draft
date: 2026-08-23
series: Making Computational Review Version-Specific
series_part: 3
publication_status: private-not-approved
audience:
  - editors and review coordinators
  - agent-workflow builders
  - methods reviewers
  - data custodians
reader_utility: decompose review into bounded machine and human work while preserving accountability
operational_artifact: versioned review-request template and authority table
evidence_status: protocol proposal grounded in prior art; workflow benefits remain untested
source_drafts: [part-03-who-is-allowed-to-say-it-passed, part-09-review-as-a-distributed-workflow]
future_cross_list_slot: internal web/iOS MCRP protocol prototype; unscheduled and not evidence for this post
---

# What agents can check—and who remains accountable

_Making Computational Review Version-Specific, 3 of 6_  
_By Codex and junior_

“Please review this paper” is an underspecified work order.

A computational release may need checks of data custody, execution, statistical design, software, calibration, uncertainty, ethics, and domain interpretation. No reviewer—or agent—is automatically competent, authorized, and equipped to cover all of them. Yet review systems often compress the outcome into one pass state.

That compression creates two errors. First, uncovered scope disappears: a successful execution can look like a review of the method or conclusion. Second, accountability drifts: an agent drafts a recommendation, a person accepts the surrounding workflow, and the recommendation later appears to be a human scientific judgment.

MCRP proposes treating a review request as a versioned work object. It names the exact release and claims, questions, competencies, conflicts, confidentiality, resources, deadline, and completion rule. A coordinator can then decompose the request into bounded tasks and preserve what each task did not cover.

## Four statements that must not become one badge

| Record type | Example | Appropriate issuer | It does not establish |
|---|---|---|---|
| Observation | “The declared command exited successfully and produced these digests.” | Execution service or agent | Correctness of the method or interpretation |
| Agent report | “The output differs from the declared tolerance; these dependencies changed.” | Identified agent under recorded delegation | Scientific acceptance, independence, or role authority |
| Policy projection | “Visible records appear to satisfy policy P, version 4.” | Reproducible policy evaluator | That the policy is legitimate or the scientific claim warranted |
| Scientific disposition | “Within this scope, I accept, reject, narrow, or defer the claim.” | Qualified human in an accountable role | Universal truth, permanence, or adjacent claims |

Automation can do substantial work in the first three rows. It can inventory artifacts, resolve identifiers, reconstruct environments, compare outputs, traverse dependencies, draft discrepancy reports, and identify missing fields. None of those acts should silently cross into the fourth row.

A human adopting agent-assisted work should identify the report examined, state which findings were adopted, and accept responsibility for a defined scope. “Human in the loop” is too vague if nobody can determine what the human actually decided.

## Operational artifact: a versioned review request

Before assigning work, record:

```text
Target
  Exact release, claim versions, evidence manifest, and acceptance conditions

Questions
  The bounded questions this review must answer

Competencies
  Required domain, method, instrument, software, custody, or ethics expertise

Conflicts and independence
  Relationships to disclose, prohibited conflicts, and who evaluates them

Access and confidentiality
  Public, restricted, embargoed, personal, or security-sensitive evidence;
  permitted environments and export rules

Resources
  Compute, software, credentials, time, support, and accessibility needs

Outputs
  Required report fields, evidence references, exclusions, and unresolved questions

Deadline and interruption
  Due date, clarification channel, pause rules, and unable-to-complete state

Completion
  Which work objects must return; whether completion requires coverage,
  conformance, agreement, or a later disposition

Authority
  Who may issue observations, reports, policy projections, and scientific decisions
```

Completion should not require consensus unless the policy explicitly says so. A complete review process may end with one reconstructed workflow, one unresolved statistical objection, one access-bounded data review, and one request to narrow the claim. Averaging those outcomes would destroy information.

## Worked example: four reviewers, one claim

Imagine a release reporting a weak transient signal in an open detector dataset. Its principal claim is bounded to pipeline version 3.2, a declared event-selection policy, and a named background model. One calibration notebook remains restricted because it contains embargoed operational details.

The request becomes four work objects:

1. **Execution reconstruction.** A reviewer-controlled agent resolves the public artifacts, rebuilds the environment, runs the workflow, and records observed outputs and failures. A checksum match remains an observation.
2. **Statistical assessment.** A methods reviewer checks likelihood construction, nuisance parameters, selection effects, diagnostics, and the mapping from computed values to the claim. An agent may run declared sensitivity jobs, but the reviewer decides what those outputs mean.
3. **Calibration and custody.** An authorized reviewer enters the custodian’s environment, examines the restricted notebook, and exports only an approved structured report. Protected inputs do not enter public logs, public stores, or agent prompts outside the authorized boundary.
4. **Domain and adversarial interpretation.** A domain reviewer asks whether the claim exceeds the evidence and names plausible alternatives. Procedural success in the other tasks does not become domain endorsement.

Suppose execution succeeds, the statistical reviewer finds sensitivity to an unreported prior, the custody reviewer confirms the declared procedure but cannot disclose one exception, and the domain reviewer says the wording is too broad. The workflow is complete because all required reports exist. The scientific claim is not accepted merely because the workflow completed.

If an accountable decision-maker later acts, the decision should bind the exact claim version, acceptance-condition version, evidence-set digest, release digest, role, and decision. Changing any component creates a different decision context.

## What is established, proposed, and evidenced

**Established prior art.** Contributor and review roles already have official vocabularies and records, including [CRediT](https://credit.niso.org/), [ORCID peer-review records](https://support.orcid.org/hc/en-us/articles/360006971333-Peer-Reviews), and [Crossref’s peer-review record type](https://www.crossref.org/documentation/schema-library/markup-guide-record-types/peer-reviews/). [W3C Verifiable Credentials](https://www.w3.org/TR/vc-data-model-2.0/) provides a model for attributable claims. These mechanisms can identify statements and roles; they do not establish competence or scientific adequacy.

**MCRP proposal.** The proposal is to bind those identities and reports to exact scientific objects, decompose review prospectively, make uncovered scope visible, and require explicit human adoption where scientific authority is needed.

**Current evidence.** The workflow has been exercised as a design and synthetic implementation. We have not shown that it reduces handoff loss, improves defect detection, protects restricted evidence across real deployments, or uses reviewer time efficiently.

## What remains open

Decomposition can create gaps between tasks, duplicate effort, and reward form completion over thought. Conflict metadata can be incomplete. Restricted evidence may prevent public reconstruction of a reviewer’s reasoning. Agent-generated reports can look more comprehensive than the underlying examination. “Qualified” remains community- and role-specific; a credential or signature cannot settle it.

Those gaps should be reported as outputs, not hidden behind process completion. The practical rule is immediate: give every agent and reviewer a bounded work order, preserve exclusions, and require a named person or institution to own each scientific disposition.

The next post asks how those scoped review products can travel among compute centers, societies, repositories, journals, and curation groups without requiring one universal platform.

