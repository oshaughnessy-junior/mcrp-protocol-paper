---
artifact_role: outward-facing-season-landing-page-content-packet
authors: [Codex, junior]
status: mature-private-draft
date: 2026-08-23
series: Making Computational Review Version-Specific
publication_status: private-not-approved
audience:
  - computational scientists
  - reviewers and editors
  - research-infrastructure builders
  - agent-workflow designers
reader_utility: choose the relevant MCRP article and understand the series claim boundary before reading
operational_artifact: season map and shared authority legend
evidence_status: editorial packet for a protocol proposal; not evidence of validation
future_cross_list_slot: reserved for separate internal web/iOS MCRP protocol prototype after independent readiness review
---

# Landing-page content packet: Making Computational Review Version-Specific

_By Codex and junior_

## Short page title

Making Computational Review Version-Specific

## Deck

Agents can reconstruct environments, rerun workflows, compare outputs, and route changes. Those capabilities are useful only if a review remains bound to the exact claim, evidence, release, and authority it actually covered. This six-part series develops a practical proposal for doing that—and a test plan that could show the proposal is not worth adopting.

## Opening copy

Computational review has a versioning and authority problem.

A reviewer can approve a repository, then the repository changes. An agent can reproduce a figure, while an upstream calibration remains unknown. A registry can hold three signed reviews without establishing that the reviewers are independent. A correction can be public while downstream claims continue to look current.

The Minimum Credible Reproducibility Protocol, or MCRP, is a bounded design proposal for these failures. It treats review as an event about an immutable scientific release: exact claim versions, evidence, workflows, checks, and scoped human decisions. Later changes append history and trigger follow-up work rather than silently inheriting or erasing approval.

MCRP does not claim originality for provenance graphs, research objects, signed attestations, transparency services, decentralized notifications, persistent identifiers, or publish–review–curate models. The proposal is their disciplined integration around prospective acceptance conditions, externally attributable checks, version-bound scientific dispositions, dependency-sensitive freshness, and conservative limits on automated authority.

The current work has not shown improved reviewer accuracy, reduced effort, cross-domain validity, interoperability, web-scale operation, capture resistance, or better scientific outcomes. The final installment explains how those claims should be tested—and when the design should be narrowed or stopped.

## Season map

### 1. What, exactly, did we review?

The published introduction defines the Scientific Record Release: an immutable object binding the claims, evidence, executions, checks, and human decisions under review.

**Best for:** Readers new to MCRP.  
**Use it to:** Understand why a repository link or green badge is not a stable review target.  
**Status:** Already published; retain its existing canonical URL and supplement link.

### 2. [A rerun is not a justification](part-02-a-rerun-is-not-a-justification.md)

Separates computational derivation from scientific support, then shows how approval should age when dependencies change.

**Best for:** Researchers and reproducibility reviewers.  
**Takeaway:** A claim–evidence–freshness checklist.

### 3. [What agents can check—and who remains accountable](part-03-what-agents-can-check.md)

Turns “please review this paper” into bounded machine and human work while keeping observation, agent report, policy projection, and scientific disposition distinct.

**Best for:** Editors, review coordinators, and agent-workflow builders.  
**Takeaway:** A versioned review-request template.

### 4. [Portable review without a universal platform](part-04-portable-review.md)

Shows how archives, compute centers, societies, journals, registries, and curation groups can contribute compatible review products without collapsing their authority.

**Best for:** Scholarly-infrastructure and institutional leaders.  
**Takeaway:** A responsibility matrix and minimum portable-review record.

### 5. [A scientific record that can change without rewriting history](part-05-a-scientific-record-that-can-change.md)

Defines a living record as append-only events plus recomputed views, including corrections, partitions, access limits, and disagreement.

**Best for:** Infrastructure architects and open-review platforms.  
**Takeaway:** A five-step update loop and disagreement timeline.

### 6. [How this trust layer could fail—and how we would test it](part-06-how-the-trust-layer-could-fail.md)

Derives experiments and stop rules from review rings, captured registries, disclosure risk, burden, and event failure.

**Best for:** Skeptics, security/privacy reviewers, evaluators, and funders.  
**Takeaway:** A threat-to-test decision matrix.

## Shared authority legend

Use these labels consistently throughout the season:

- **Proposal:** a claim, design, or interpretation offered for assessment.
- **Evidence:** an identified object or result offered to support, bound, contextualize, or contradict a proposal.
- **Automated observation:** what a machine process directly recorded, such as execution status or an output comparison.
- **Agent report:** an attributable synthesis or analysis produced under recorded delegation.
- **Policy projection:** what a named executable policy computes from a visible event set.
- **Scientific disposition:** an attributable human judgment—accept, reject, narrow, defer, withdraw, or adjudicate—within a declared role and scope.

No type silently inherits another’s authority.

## Recommended release treatment

- Release in order, no faster than one post per week.
- Approve each article separately; approval of the season does not authorize publication of every draft.
- Put detailed standards citations on one maintained foundations page and keep only argument-essential sources in each post.
- Preserve each operational artifact as a skimmable block that can be reused independently.
- Link every post backward to the landing page and forward to the next installment.
- Retain the eleven-post private corpus as a technical source, not as the public table of contents.

## Future cross-list slot: internal web/iOS protocol prototype

Reserve a clearly labelled card after the six-part article sequence:

> **Future implementation note — not yet available**  
> A separate internal web/iOS MCRP protocol prototype may later exercise exact release binding, review-request decomposition, event exchange, and policy-specific views. Its scope, evidence, and release timeline are independent of this article season. The slot should remain unpublished or display “forthcoming” only after explicit product and publication approval. No current article may imply that the prototype has produced validation results.

Cross-list only when all of the following are true:

1. a stable internal owner and exact artifact are named;
2. implemented functions are distinguished from mockups and planned functions;
3. privacy and security review covers data handling, agent delegation, and review identities;
4. a verification report states what was tested and what was not;
5. the cross-list copy avoids coupling the prototype schedule to the article schedule;
6. management separately approves the link and its claims.

## Explicit gaps before public integration

1. **Existing Part 1 metadata:** The published opening currently describes a four-post series. If this six-part season is approved, its series count and roadmap require a separately approved outward-facing correction; this packet does not alter the live page.
2. **Editorial:** Each draft needs a final human density and voice pass; repeated qualification should be compressed without weakening the authority boundary.
3. **Sources:** Every external link needs interactive verification. Official DocMaps and ORCID pages previously blocked automated clients.
4. **Accessibility:** Diagrams, tables, and code-like artifacts need mobile rendering, screen-reader labels, and meaningful text alternatives.
5. **Privacy and ethics:** Parts 3, 5, and 6 require review of restricted-evidence, retaliation, pseudonymity, and disclosure language.
6. **Security:** Registry, federation, signature, and prototype claims need threat-focused review; no capture- or Sybil-resistance language is justified.
7. **Evaluation:** Numerical effect margins, sample sizes, severity definitions, and service bounds remain unset pending study-design expertise.
8. **Interoperability:** No two-node semantic round trip or lossless crosswalk has been demonstrated.
9. **Evidence:** No real-publication comparison supports claims of improved accuracy, effort, correction uptake, or review quality.
10. **Publication operations:** Canonical URLs, social copy, preview images, metadata, final publication dates, and per-post approvals are not defined here.
11. **Prototype separation:** The internal web/iOS prototype has no claimed result in this packet and must not become a prerequisite or implied validation surface for the season.

## Approval choices

- [ ] Approve the landing-page content for outward-facing integration, not publication.
- [ ] Approve selected post drafts for an editorial pass: ____________________
- [ ] Request revisions before integration: ____________________
- [ ] Defer the season pending: ____________________
