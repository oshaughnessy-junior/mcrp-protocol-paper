# Proposed design revision responding to aiXiv review 1586

Draft integration text; 26 September 2026. No publication performed. These blocks
replace or extend the indicated sections of `paper/position-paper.md`; they are
not a claim that the synthetic implementation already implements every rule.
Existing bibliography keys are retained. The protocol draft must be reconciled
with these proposed rules before claiming conformance to this revision.

## Insertion A: add at end of Section 2

### 2.1 Decomposing the design contribution

The contribution is a lifecycle policy assembled from established mechanisms.
Table 1 distinguishes inheritance, adaptation, and decisions made by this
proposal. “Proposed” identifies our specified choice, not evidence of first
invention; the comparison is not an exhaustive novelty search. A feature absent
from the table's description of a neighboring system must not be read as proven
absent from that system.

| Mechanism | Established source or practice | Status in MCRP | Specific policy commitment evaluated here |
|---|---|---|---|
| Claim–evidence graph with support and challenge | Micropublications and EVI [@micropublications-2014; @evi-2021] | Adopted | Material claims name scoped acceptance predicates and required decisions; the graph alone is not the contribution. |
| Entity, execution, attribution, and derivation records | PROV-O [@w3c-prov-o-2013] | Adopted | Bind each decision to the exact claim and release under review. |
| Packaged research objects and run context | RO-Crate and Workflow Run RO-Crate [@ro-crate-1.2; @workflow-run-ro-crate-2024] | Adopted representation target | Preserve claim scope and decision state across exports; round-trip compatibility remains unimplemented. |
| Content identities and version-specific archival records | CWLProv, Nanopublications, and archive versioning [@khan-cwlprov-2019; @nanopublications-2018; @zenodo-doi-versioning] | Adopted | A material edit creates a successor; historical acceptance is immutable. |
| Independent execution and external completion checking | CODECHECK and Paper-replication [@nust-codecheck-2021; @paper-replication-2026] | Adapted | Fix claim-level predicates prospectively and require a recorded authorization boundary for verification. |
| Execution distinct from scientific judgment | CODECHECK and artifact-review practice [@nust-codecheck-2021; @acm-artifact-badging-2020] | Adopted distinction | Machine outcomes cannot populate the qualified human disposition field. |
| Dependency-triggered reconsideration | Graph propagation and versioned provenance are established; EVI supplies defeasible evidence relations [@evi-2021] | Adapted into lifecycle rules | Mark reachable decisions pending; permit carry-forward only after an unchanged-claim mapping and separately authorized scope-delta disposition. |
| Assurance together with bounded assessment coverage | Artifact policies motivate separate review products [@acm-artifact-badging-2020] | Proposed profile and assignment rules | Report claim-specific predicates, currentness, mode, and coverage before any aggregate label. |
| Resource envelope separate from assurance | Established compute, storage, access, and labor accounting | Proposed composite disclosure profile | Report workload-specific measured or estimated burdens without treating expense as evidence strength. |

The incremental research question is consequently whether this combination of
prospective predicates, exact-version authority, and conservative change handling
improves review decisions relative to equally informative simpler packages. A
positive result would establish usefulness of the tested policy, not novelty of
its constituent graph, signature, archive, or review mechanisms.

## Insertion B: replace final paragraph of Section 5.3

### Operational independence profiles

Independence has at least three distinct coordinates: **decision control**,
**execution custody**, and **scientific failure modes**. A different account,
session, model, or signature establishes none of these by itself. The following
are candidate implementable profiles, not validated governance arrangements.

Every profile must record: (i) candidate producers and controlling principals;
(ii) the separately accountable verifier and authorization source; (iii) who can
change acceptance policy and who controls the verification environment and result
record; (iv) disclosed financial, supervisory, collaboration, and reciprocal-review
relationships; and (v) a conflict disposition under a policy fixed before review.
The author cannot unilaterally replace a refusal or failure with a passing verifier
record. Changing the candidate requires a new digest and attributable patch.

| Setting | Feasible candidate arrangement | Minimum observable evidence | Remaining limitation |
|---|---|---|---|
| Small collaboration | A researcher outside the candidate's author group accepts a bounded review; one competent person may perform both execution and scientific review as separately recorded acts. | That reviewer independently retrieves the identified candidate, controls the verification run or declared witness inspection, records conflicts, and issues their own dated result. | A personal relationship or reciprocal favor may still bias judgment; separate control does not demonstrate independent scientific errors. If nobody meets the policy, report author evidence and pending external review. |
| Community service | A service-appointed maintainer or reviewer operates a separately administered runner and disposition record. | Assignment and conflict decisions, versioned service policy, runner custody, actual execution evidence, and independent result publication are inspectable. Authors cannot write the service result or choose only a favorable result from the declared batch. | Service governance, funding pressure, shared dependencies, and attempts outside the recorded batch remain possible failure sources. |
| Institution | A review unit delegates a named assessor under documented separation from the producing project's approval chain. | The delegation, role permissions, conflicts, execution custody, result record, and appeal path identify accountable decision-makers. | Institutional separation does not establish domain competence or eliminate shared incentives and scientific blind spots. |

For MCRP-2 execution, the verifier must control the actual execution and observation
boundary: a second account on an author-administered environment is insufficient
if authors can alter the tested candidate, effective inputs, or reported outcome
without detection. A restricted-facility inspection can instead be recorded as
`witness`; it does not silently become a non-author rerun. Conflict declarations
and access-control evidence make a boundary inspectable but cannot prove that
undeclared control or collusion is absent. Methodological independence needed for
MCRP-3 requires a specific challenge capable of exposing a stated failure cause,
not merely a different controller or model name.

Agents may perform bounded checks under any profile. They do not hold the qualified
human scientific disposition role in this protocol. Agent-only early adoption can
therefore produce useful machine outcomes and pending-review records without
qualifying for MCRP-1. This is an explicit scope boundary, not a reason to mislabel
a synthetic agent run as human scientific acceptance.

## Insertion C: replace Section 6 assurance assignment paragraphs; retain mode definitions

### Reproducible assignment rules

An assessment is indexed by claim c, immutable release r, scope s, policy version
p, and assessment time t. Each required predicate receives a value in
{pass, fail, unknown, not-applicable}, with its evidence reference, assessing role,
and rationale. Missing evidence is unknown, never pass. A profile may mark an
item not-applicable only when the policy's predeclared applicability rule permits
it and a separately authorized disposition records why; the aggregate cannot be
improved by silently deleting difficult requirements after observing results.

Let S_1 contain the required predicates for content identity, material-claim
mapping, provenance paths within the declared custody boundary, explicit trust
leaves, claim-specific acceptance tests, negative/adversarial controls,
version-specific archive identity, and qualified independent scientific disposition.
Let S_2 contain all S_1 predicates plus reviewer-controlled reconstruction,
execution, and claim-result comparisons over the stated assessment scope. Let S_3
contain all S_2 predicates plus an independent method/data challenge, declared
sensitivity checks for material choices, applicable platform comparisons, and an
exercised freshness/failure response. Each applicable test needs a prospective
procedure and decision threshold. Numerical tolerances are claim-specific and
must be justified scientifically; this protocol does not supply a universal
floating-point threshold or a universal definition of adequate science.

For a current, undisputed assessment define

\[
 L(c,r,s,p,t)=\max\bigl(\{0\}\cup
 \{\ell\in\{1,2,3\}:\ \forall z\in S_\ell,
 \ z\text{ passes or has an authorized applicable exemption}\}\bigr).
\]

Here “applicable exemption” means a policy-permitted not-applicable disposition,
not forgiveness of a failed required test. Identity, external authority, archive
identity, and human scientific disposition are mandatory S_1 gates and cannot be
exempted. Execution and comparison are mandatory S_2 gates; independent challenge
and exercised freshness are mandatory S_3 gates. The exact predicate inventory
and applicability rule set are included with the assessment so two reviewers can
recompute the label from the same recorded outcomes. Disagreement about a predicate
remains a substantive review disagreement; deterministic aggregation cannot settle
it. Report such a component as disputed and withhold its current level until the
authorized disposition is recorded.

For every material claim the release displays the complete tuple
(scope, mode, coverage, outcome vector, policy, assessment date, freshness state).
`Slice` and `checkpoint` cannot receive full-claim coverage unless an explicit
validated coverage argument supports that claim's entire stated scope; otherwise
the assessment is partial and its narrower scope must remain visible. `Audit-only`
and `unassessed` coverage cannot satisfy S_2. A release-wide label, if displayed,
is the minimum level over its prospectively fixed material-claim inventory only
when every component is current, undisputed, and covers the full declared claim
scope. Otherwise display the per-claim results and withhold the aggregate; partial
coverage must not be hidden behind the weakest ordinal number. A material change
or expired freshness trigger leaves the historical tuple intact and removes the
current label until affected predicates and decisions are re-established.

These are proposed operational sufficiency rules. They improve auditability of
assignment, but have not been calibrated against scientific outcomes or tested
for inter-reviewer reliability.

### Resource-profile measurement semantics

For each assessment mode m, a resource envelope records workload definition,
measurement interval, accounting boundary, observed/estimated/unavailable status,
unit, lower and upper estimates when relevant, and the estimation method. Unknown
is not zero. The six RRP coordinates are structured quantities:

| Coordinate | Minimum reportable envelope |
|---|---|
| C: computation | CPU/GPU model and device-hours, wall time, memory peak, run count, including failed and verification runs within the accounting boundary. |
| D: data/storage | Input bytes, transferred bytes, peak working storage, retained bytes and retention interval; identify compression and shared caches. |
| P: platform | Required hardware, operating system, scheduler, service, and software versions; record substitutability constraints rather than assigning a fictitious cardinal cost to a platform name. |
| X: access/governance | Required permissions and agreements, lawful access conditions, access waiting time, and the authorized role needed; categorical restrictions remain categorical. |
| H: human effort | Setup, scientific review, operation, repair, and administration hours by role, with elapsed waiting time separate from active effort. |
| A: agent effort | Model/provider/version, requests, input/output tokens or other measured service units, retries, tool calls, runtime, and actual billed cost where available. |

Agent effort is measured service consumption, not a scale of intelligence.
Compute used by an agent may also appear under C, but these views are marked as
overlapping and are never added as if disjoint. Human hours likewise cannot be
inferred from machine runtime. A comparison R <= R' is permitted only under
matched workload, mode, units, interval, and accounting boundary; numeric resource
requirements must be componentwise no greater and categorical requirements no more
restrictive under an explicitly declared feasibility relation. Otherwise the
profiles are incomparable. Ordinal bins, if used for routing, must state their
thresholds and domain profile version and have no effect on assurance level.

## Insertion D: replace last evaluation paragraph of Section 9

### Falsifiable evaluation predictions

The proposed benefit is a hypothesis about review decisions and total effort.
A preregistered evaluation should compare (B0) a version-pinned repository with
clear instructions; (B1) the same artifacts plus structured claim/provenance
records; (B2) B1 plus independent execution; and (M) B2 plus prospective
claim-scoped predicates, exact-version authorization, and explicit amendment and
carry-forward rules. Match information access, workload, tools, training support,
and permitted reviewer/compute budgets. Costs of creating M-specific records
remain attributed to M rather than being removed as benchmark preparation.

Use public workflows with evaluator-held injected defects and untouched controls.
A fault oracle states the expected affected claims and acceptable findings before
review. It remains separate from agent-generated judgments. Preserve every
in-scope attempt, refusal, timeout, and unresolved case. For changes that are
scientifically ambiguous, score against a declared expert adjudication process
and report disagreement rather than inventing an unambiguous truth label.

| Prediction and contrast | Measured endpoint | Observation that would defeat the predicted advantage |
|---|---|---|
| M vs B2 reduces reliance on stale or wrong-version evidence after an announced change. | Fraction of changed, affected claim-decisions still accepted as current at a fixed decision horizon; denominator is all affected offered decisions. | No reduction, or apparent improvement explained entirely by refusing every decision. |
| M vs B1/B2 improves localization of change effects. | Affected-claim sensitivity and unaffected-claim false-invalidation rate, with unresolved decisions reported separately. | Higher sensitivity accompanied by indiscriminate invalidation beyond the predeclared tolerated false-invalidation rate. |
| M vs B2 reduces acceptance of author-issued or wrong-scope verification as independently authorized. | Incorrect reliance among predeclared authority/scope mismatch cases, alongside correct acceptance of matched controls. | No improvement after equal access to the underlying identity and scope information, or loss of matched-control acceptance beyond the declared margin. |
| M's carry-forward process saves recovery work relative to blanket reverification without losing needed checks. | Total setup, review, computation, repair, and administration cost through one amendment, plus missed affected decisions. | Costs fail to improve under the specified workload or savings require leaving affected decisions unchecked. |

Define a decision horizon, smallest useful improvement, acceptable false-alarm and
control-acceptance margins, cost accounting, and sample-size rationale before
collecting outcomes. Randomize or counterbalance conditions at the workflow or
operator level and account for repeated decisions within those units; claim
counts alone are not independent sample sizes. Analyze assigned/offered workloads,
not only completed reviews. Publish exact denominators and uncertainty appropriate
to the randomization and clustering scheme. Zero findings or excessive unresolved
work are possible results, not grounds for silently changing success criteria.

These predictions isolate the lifecycle's proposed contribution. A comparison
only against a poorly documented repository could establish a benefit of added
information without showing a benefit of MCRP's policy. If B1 or B2 performs as
well at lower total cost, the evidence favors that simpler practice for the tested
setting. No current synthetic test establishes any of these empirical predictions.

## Source verification and integration notes (editorial, omit from manuscript)

Primary pages checked during this revision: W3C PROV-O official specification;
RO-Crate 1.2 official specification; CODECHECK official site; original
Micropublications article through PMC (https://pmc.ncbi.nlm.nih.gov/articles/PMC4530550/);
and Paper-replication arXiv v2. The DOI resolver requests for Micropublications
and EVI and the existing ACM policy URL returned tool errors on this check.
EVI and ACM entries in the table inherit the already-cited manuscript positioning;
they should not be characterized as newly reverified primary documents here.

Insertion A addresses novelty decomposition and is additive. Insertion B replaces
only the unresolved-governance final paragraph of 5.3, retaining the execution
record paragraph. Insertion C replaces the current assurance and resource
paragraphs in Section 6 while retaining the four mode definitions immediately
before the assignment rules. It deliberately strengthens the aggregate-label
rule to forbid partial scope masquerading as whole-claim assurance. Insertion D
replaces the final evaluation-program paragraph in Section 9. Root should reconcile
Abstract/Conclusion with the now-public aiXiv posting, historical archive status,
and actual evidence inventory separately; this file makes no implementation or
archival claims and does not alter the main manuscript.
