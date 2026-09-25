# Collective red pass: operational design and response to review 1586

Reviewer: adoption-theory agent, 26 September 2026. Reviewed the integrated
`paper/position-paper.md` after design/evidence integration and before Appendix A
arrival. Discussed gate findings with the formal-semantics author and requested
concurrent evidence-lane confirmation. This is internal review, not external
scientific sign-off. Main manuscript was not edited.

## Required corrections before finalizing the proposed policy

**RD-1: external admission is not explicitly inside S1.** The prose later calls
external authority a mandatory S1 gate, but the defining inventory lists content
identity, mapping, provenance, trust leaves, tests, controls, archive, and scientific
disposition. A literal implementation of the quantified rule can omit the
external admission/authorization decision. Add an explicit S1 predicate requiring
successful external admission under §5.2, including the verifier authority and
independence disposition under §5.3. Record its exact candidate digest, policy
version, scope, and evidence. A candidate with all listed scientific and archival
checks but missing external admission must remain below MCRP-1.

**RD-2: the nonapplicability policy can waive most minimum requirements.** The
formula permits every predicate to pass or receive an authorized exemption;
the subsequent mandatory list protects only identity, external authority, archive,
and scientific disposition in S1. A predeclared policy could thus mark material
claim mapping, required provenance, acceptance tests, and negative controls as
not-applicable and still earn MCRP-1. This is not merely post-hoc cheating; the
present text permits it prospectively. The profile would then fail the original
minimum-content definition despite following the assignment equation.

Recommended resolution: make every S1 and S2 predicate non-exemptible. Use a
closed list of possible S3 nonapplicability decisions: platform comparison where
no alternative platform is relevant to the claim, and a particular sensitivity
check where the domain profile documents no corresponding material varying choice.
Keep independent challenge and exercised freshness mandatory. Alternative domain
profiles changing these minimum gates must use a distinct profile label and cannot
claim the same assurance level. If a wider exemption model is desired, list every
waivable predicate and its applicability rule explicitly rather than delegating
minimum meaning to arbitrary policy text. Include missing-admission and exempted-
core-gate negative cases in the semantics tests if they implement level assignment.

## Review 1586 response coverage

- Novelty decomposition: directly answered by Table 1; “proposed” does not imply
  first invention, neighboring system omissions are not invented negative claims.
- Falsifiable benefit: directly answered through B0/B1/B2/M contrasts, controlled
  information and effort, stale decisions, localization, authority mismatch, and
  recovery cost. Preregister numerical decision margins before any efficacy claim.
- Consistent assurance/resource assignment: substantially answered, contingent on
  RD-1/RD-2. Resource quantities are explicit, unknown is distinct from zero,
  overlapping compute/service counts are not added, and incomparable profiles
  remain incomparable.
- Feasible independence: concrete small/community/institutional options replace
  the unresolved question. They establish inspectable control requirements, not
  proof against hidden control/collusion or statistical error independence.
- Historical evidence inventory: the manuscript honestly withdraws unrecoverable
  counts and substitutes an explicitly separate public subset. This does not
  reconstruct the requested historical mapping; the rebuttal should say so.
- Formal graph/carry-forward semantics: pending the separately owned Appendix A;
  this review makes no claim to have checked absent content.

## Coherent scope boundaries worth retaining

Agent-only initial usage yields machine evidence and pending scientific review;
it does not meet the mandatory human disposition for MCRP-1. That follows the
existing lifecycle and prevents aiXiv's agent feedback from being presented as
human scientific acceptance. Full-release labels require complete declared claim
coverage, currentness, and undisputed predicates. A high-level slice assessment
cannot silently inflate the original claim. Historical records are preserved
when current labels are removed. The observed prototype tests establish only
encoded behavior on named synthetic fixtures. These boundaries are material,
not optional disclaimers.

## Integration-model follow-up

Root reported correcting the recurring-benefit/adoption inference and explicit
mapping to h-c. Those are the proper remedies to I-1/I-2 in the integration-lane
review. They do not change the correct exact loss algebra or corner-extrema proof.

## Collective discussion received before disposition

The evidence reviewer independently confirms RD-1 and identifies an additional
level-zero loophole: §5.4 says acceptance requires all mandatory decisions for the
claimed level, but level 0 can have an empty mandatory set. Define MCRP-0 as
nonconformant disclosure/pending review; accepting an SRR under this lifecycle
requires at least MCRP-1, never vacuous satisfaction of level 0. Evidence reviewer
also requests pinned resolvable supplement links in the actual PDF and qualifying
§4's “every affected” language to declared reachable dependencies.

The formal-semantics reviewer agrees with RD-1/RD-2 and is correcting carry-forward
so a historically approved but now expired, withdrawn, pending, or disputed decision
cannot be reused. Historical approval alone is insufficient; current authorized
status at assessment time must be an explicit premise. They also add changes in
the material-claim inventory to the dirty-root set. These changes need a fresh
appendix integration, not acceptance of an earlier snapshot.

Final release disposition: address the explicit gates/exemptions, level-zero
acceptance, latest-status carry-forward, and accessible evidence references, then
rerun the integrated semantics and rendering checks. The design response is
substantive, but these are real policy ambiguities to resolve before describing
its assignment rules as implementable without interpretation.
