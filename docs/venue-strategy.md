# Venue strategy for MCRP

## Recommendation

Prepare the first manuscript for the **Issues in Research Software** section of the *Journal of Open Research Software* (JORS). Submit it as a position paper, not a software metapaper and not an empirical effectiveness paper.

The section explicitly accepts position papers, survey papers, and experience reports about creating, maintaining, and evaluating open research software. Its current guidance targets approximately 3,000–4,000 words and evaluates whether a position is clear, useful, grounded in prior work and experience, and capable of helping others address a recognized problem.

Official sources:

- Scope and submission types: https://openresearchsoftware.metajnl.com/about/submissions
- Position-paper review criteria: https://openresearchsoftware.metajnl.com/en/about/editorialpolicies

Current format requirements to recheck at submission include: an abstract;
no more than three heading levels; Vancouver-style numbered references; PDF
plus source for LaTeX submissions (or DOC/ODT); cited display items supplied in
the requested formats; permissions for third-party material and methods; and
three proposed peer reviewers in the editor comments. The present Markdown
citation keys are stable drafting identifiers and must be rendered into the
venue's numbered reference style for the submission candidate.

## JORS framing

The paper should present MCRP as:

- a prospective protocol and research-software review profile;
- a composition of established provenance, archival, execution, and human-review practices;
- a concrete, falsifiable position about externally enforced and claim-versioned review;
- a public reference implementation with explicit non-conformance fields;
- an evaluation agenda.

The paper should not claim:

- that claim–evidence graphs are novel;
- that MCRP improves scientific outcomes or reviewer performance;
- that the synthetic implementation establishes scientific validity;
- that MCRP is a consensus standard;
- that one scalar badge can summarize availability, execution, reproduction, replication, and validity.

## JORS submission gates

1. **Scope gate**: the final manuscript remains about reusable research-software and reproducibility practice rather than generic AI governance.
2. **Length gate**: main text conforms to the live JORS word guidance after references and supplementary placement are resolved.
3. **Novelty gate**: the literature comparison is refreshed through submission, including recent agentic reproducibility, scientific-workflow, and governance work.
4. **Claim gate**: every consequential statement is entered in a claim ledger with primary-source support or marked as a proposal/evidence gap.
5. **Artifact gate**: the protocol, schemas, synthetic implementation, tests, and review checklist are public, sanitized, licensed, and archived under a version-specific identifier.
6. **Independent-exercise gate**: a non-author runs the exact archived reference implementation and records discrepancies.
7. **Human-review gate**: a reproducibility/provenance reviewer and a qualified scientific reviewer separately assess the exact candidate release.
8. **Privacy gate**: no private paths, repositories, task records, agent/session identifiers, restricted scientific information, personal records, credentials, or infrastructure topology remain.
9. **Integrity gate**: citations resolve; cited sources support the prose at its stated strength; manuscript lint and rendered-document inspection pass.
10. **Authorship gate**: accountable human authors approve the manuscript, and agent assistance is disclosed under the venue's current policy.

Failure of gates 3–10 is a no-go for submission. Evidence markers may remain during drafting but must be resolved, narrowed into explicit future work, or removed before submission.

## Ranked alternatives

### 1. F1000Research Method Article

Use if open peer review, versioning, and iterative protocol development are more important than the JORS research-software audience. F1000 currently accepts new or substantively modified computational methods. Its guidance expects validation results, or use cases and explicit limitations where validation is incomplete.

Official guidance: https://f1000research.com/for-authors/article-guidelines/method-articles

Fit risk: the synthetic demonstration alone may be judged under-validated. Confirm current article-processing charges and institutional eligibility before selecting this route.

### 2. Data Science Journal

Use when the manuscript emphasizes data lineage, preservation, transparent data systems, and cross-domain reuse. A research article would require original outcomes; a practice paper describes a finished project or procedures operating in an established system and should be discussed with the editor before submission.

Official sources:

- Scope: https://datascience.codata.org/about
- Submission types: https://datascience.codata.org/about/submissions

Fit risk: MCRP is not yet an established operational data system. A practice-paper submission should wait for real use cases.

### 3. ACM Conference on Reproducibility and Replicability

This is the strongest specialist community for a later empirical paper or a future short vision paper. ACM REP covers provenance, automated validation, reproducibility infrastructure, privacy, cost, archival practice, and lifecycle maintenance. The 2026 submission cycle is closed; do not infer a future deadline or article category until a new official call appears.

Official conference page: https://acm-rep.github.io/

Fit risk: a future full paper will require comparative empirical evidence and artifact review.

### 4. IEEE eScience

Use for a later systems paper when evaluation includes scientific workflows, distributed or HPC execution, heterogeneous platforms, and restricted-data witness modes. The 2026 paper cycle is closed; monitor future official calls.

Official scope: https://www.escience-conference.org/about/

Fit risk: a protocol-only paper without a substantial eScience system evaluation is likely too early.

### 5. Research Integrity and Peer Review

Use after studying how MCRP affects human review: claim coverage, detected defects, effort, agreement, or reporting quality. The journal's focus on research integrity, reporting, and peer review fits that empirical question.

Fit risk: a technical specification without research-on-research evidence may not meet the journal's evidence-oriented expectations.

### 6. Patterns

Treat as a stretch target for a later cross-domain empirical paper with broad data-science implications, FAIR artifacts, and a demonstrated major advance.

Official scope: https://www.sciencedirect.com/journal/patterns

Fit risk: the current protocol and synthetic fixture do not yet meet the journal's selectivity or breadth threshold.

## Later empirical paper threshold

A later ACM REP, IEEE eScience, or Patterns submission should not begin until the study has:

- at least two, preferably three, public workflows with distinct `RRP[C,D,P,X,H,A]` profiles;
- a repository-plus-instructions baseline and at least one provenance or independent-execution baseline;
- predeclared metrics and stopping rules;
- reviewer-effort and inter-reviewer-agreement measurements;
- defect-detection results with adjudication of false findings;
- ablations for claim indexing, trust leaves, resource profiles, and freshness;
- at least one external reproduction attempt;
- released evaluation data sufficient to regenerate every figure and table;
- an ethics determination for any human-reviewer study.

Until those conditions are met, describe MCRP as a protocol proposal with a tested reference implementation, not as an evidence-backed improvement to scientific review.
