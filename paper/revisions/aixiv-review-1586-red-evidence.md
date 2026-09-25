# Red-team review: evidence, scope, and claim consistency

Reviewed the integrated `paper/position-paper.md` during revision in response to
aiXiv review 1586. Appendix A was not yet present in the inspected text; this
report does not certify its eventual integration. Reviewer: a member of the same
author-directed agent team, not an independent scientific reviewer.

## Actionable findings

1. **Publication blocker: give PDF readers a resolvable evidence link.** Section 7
   identifies a commit hash and plain repository-relative filenames, but neither
   tells a reader of the standalone aiXiv PDF where to fetch the inventory. The
   original review specifically objects to an inaccessible itemized mapping.
   Add a clickable public repository URL pinned to the revision commit for the
   evidence Markdown/JSON and Appendix A code; add the clean source-archive URL
   for the distinct 20-test demonstration. Publish those exact files before
   posting the revision and verify anonymously that the links resolve. A local
   file that merely accompanies our working copy does not resolve this issue.

2. **Specification ambiguity: explicitly exclude acceptance at level zero.**
   Section 6 defines L=0 when no S1 requirements pass, but no longer defines
   MCRP-0. Section 5.4 says acceptance requires all mandatory decisions for the
   *claimed assurance level*. An implementer could claim level zero and infer an
   empty acceptance gate. Define MCRP-0 as disclosure/pending status, not scientific
   acceptance or conformance, and require L>=1 plus the applicable currentness,
   coverage and authority conditions before an acceptance transition. Agent-only
   posting or admission remains allowed, but is distinct from acceptance.

3. **Narrow an inherited overstatement about graph completeness.** Section 4 says
   a dependency update can be traced to “every affected output and claim.” The
   new public negative control expressly demonstrates an omitted dependency that
   remains current. Change to every reachable output/claim *in the declared graph*
   and state that omitted causal dependencies are not guaranteed detectable.
   This makes the early definition consistent with Sections 5.2, 5.5 and 9.

4. **Avoid an unmeasured benefit claim.** Section 6 says the new rules “improve
   auditability of assignment.” The defined rules do make recomputation possible
   conditional on the same inventory and recorded outcomes, but no human study
   measured auditability. Prefer “make the aggregation rule explicit and
   recomputable from the recorded predicates; whether this improves reviewer
   auditability remains untested.” This is minor but follows the paper's own
   careful distinction between specified behavior and empirical benefit.

5. **Tighten the list of S1 gates.** The initial S1 inventory omits a separately
   named external-authority predicate, then the following paragraph identifies
   external authority as mandatory. Include it explicitly in the initial set
   and ensure the executable semantics uses the same requirement. Similarly,
   retain the non-author reconstruction requirement in S2's non-exemptible gates
   unless the definition explicitly makes it part of execution. This is a
   consistency fix, not a request to add more governance rules.

## Checks that passed in the inspected main text

- Abstract, Section 7 and limitations consistently distinguish the historical
  withdrawn counts from the separately rerun 20-test domain fixture subset.
- The 20 count is verified by the downloaded immutable public source archive,
  and both regenerated JSON objects equal their committed counterparts after
  parsing. This report does not add those two comparisons as extra unit tests.
- No text claims a DOI, independent scientific sign-off, real scientific
  evaluation, successful MCRP assurance, or demonstrated review-quality gain.
- AI authorship is disclosed; aiXiv Official Agent review is explicitly not human
  scientific disposition. Agent-only uptake is compatible with machine evidence
  and pending states, without becoming MCRP-1.
- Inherited mechanisms are clearly marked adopted/adapted/proposed; “proposed”
  does not imply historical invention or absence in neighboring systems.
- Scope-limited slice/checkpoint evidence cannot silently supply a release-wide
  full-scope label; stale/disputed components withhold current labels.
- Scientific reviewer and execution reviewer may be one competent non-author,
  but are recorded as different acts. This is an explicit weak bootstrap profile,
  with conflicts and correlated errors retained as limitations.
- The suggested evaluation records refused/timed-out offered attempts and
  controls false invalidation and blanket refusal. It does not count dependent
  claim decisions as independent experimental units.

## Release check still required

After Appendix A is integrated, rerun its named tests and verify agreement among
its actual gate inventory, Section 6, and the executable example. Confirm that
any test counts added to the abstract or Section 7 use distinct denominators and
that publication files include the source-pinned inventory, code and response.
The evidence JSON and its linked public source are suitable for release; the
historical unavailable implementation should remain an explicit withdrawn claim.
