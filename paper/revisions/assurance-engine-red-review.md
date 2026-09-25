# Independent internal red review of the assurance assignment engine

Review scope: the proposed executable assignment rules against Section 6 of the
revised verification lifecycle manuscript. This is a separate agent's internal
review under the same author-directed orchestration, not independent scientific
validation. No publishing, commits, or changes to the main manuscript are part of
this lane.

## Counterexample requirements derived before seeing the implementation

1. Remove each S1 predicate in turn, including external admission and human
   scientific disposition. None may produce MCRP-1. An empty outcome vector cannot
   receive an assurance level by vacuous universal quantification.
2. Replace every required S1/S2 pass with unknown, failed, or N/A. N/A cannot
   forgive any mandatory gate. S2 needs reconstruction, execution and comparison;
   audit-only and unassessed coverage cannot supply these through an asserted pass.
3. A level-zero record must remain a disclosure or pending record. It cannot
   authorize scientific acceptance by claiming that no predicates are required.
4. S3 exception handling must use the predeclared policy plus separately authorized
   rationale. A broadly named platform or sensitivity category cannot exempt
   overall sensitivity, independent challenge, or exercised freshness. Unknown
   predicate names must not become an accidental exemption extension mechanism.
5. Expired, revoked, disputed or pending assessments have no current level, even
   if their historical vector passed. Evaluation before issuance, after expiry,
   or with missing clock/policy context cannot silently claim present acceptance.
6. Missing evidence references or required role/disposition information must not
   be made equivalent to pass. Correct labels alone are not evidence authenticity;
   the engine must explicitly state which authority and validity facts it trusts.
7. Release aggregation must use the entire prospectively fixed material-claim
   inventory. Missing claims, duplicates, an empty inventory, or choosing only a
   favorable assessment cannot improve the release label. Cross-release, policy,
   or time-context mixing cannot silently create an assessment that never existed.
8. All aggregated claims need full declared scope. A partial assessment can carry
   a bounded per-scope result but cannot become a whole-release label. Slice and
   checkpoint modes need an explicit validated full-scope coverage argument;
   their names alone do not establish full or partial coverage.
9. Altering input dictionaries after construction must not change a supposedly
   fixed policy or historical record. Evaluation must not mutate earlier results.
10. Equal treatment of operator/agent labels is not authority authentication.
    A forged control-group or role string should be identified as a trusted-input
    boundary, not misrepresented as discovered organizational independence.

## Implementation review status

The initial engine passed **207 separately written assertion probes** in
`examples/assurance-assignment/red_probe.py`. These include all core gates removed,
failed, unknown or N/A; each evidence/role/rationale/actor field missing; all 27
three-tier pass/fail/unknown combinations; time expiry; stale/disputed/pending
states; narrowly authorized exemptions; coverage bounds; duplicate, missing and
cross-context assessments; release minima after adding a worse claim; and
nonmutation. These are assertion cases, not 207 independent scientific trials or
additional author unit tests.

**AE-R1, concrete known-author inconsistency:** Although policy construction rejects
literal `author` for external admission and human scientific disposition, it
initially accepted that same known actor as the authorized approver for
`non_author_reconstruction`, `execution`, `comparison`, and `independent_challenge`.
Replacing those four rules with `approvers=('author',)` and matching outcomes
with actor `author` and role `author production` yielded current level three.
This violates the proposed non-author/external action boundary within the fixture's
own declared identity convention. Requested the same explicit known-author
exclusion for those gates. This is not a request for automatic real-world identity
or controller detection: forged aliases and falsely declared roles remain trusted
input limitations. Finding sent to author and root.

**Interpretation limits (not blockers):** `predicate_level` on a stale record is a
contemporaneous gate calculation after excluding stale components; it must not be
called the historical level. Original outcome vectors remain unchanged. This
prototype conservatively withholds the whole current label when a higher-level
predicate is stale, even if lower-level predicates remain current. Actor strings,
role qualification, prospective policy inventories, clock values and genuine
scientific evidential adequacy are supplied assumptions. Exact-context binding
and immutable dataclasses do not authenticate them. Public prose should preserve
these boundaries.

Independent reproducer:

```sh
python3 examples/assurance-assignment/red_probe.py
```

**AE-R1 resolved.** The engine now rejects the known actor `author` across all six
independent-action gates. The regression adds six independent rejection probes.
Missing currentness assertions now default to pending for both assessment and
outcome, checked separately. The independent probe total is **215** and all pass;
the nineteen author unit tests also pass. README explicitly states actor/control
and scientific validity limitations and distinguishes predicate_level from a
historical award.

**AE-R2, same substitution at coverage/exemption boundaries:** At root's request,
probed literal `author` in `coverage_approvers` and `exemption_approvers`. Both
still yielded level three: a slice/full claim with author-asserted coverage and a
platform N/A authorized by the author. Requested exclusion in these separately
authorized disposition lists and targeted regressions. Final disposition pending
AE-R2 correction and rerun.


**AE-R2 resolved; final disposition:** Both policy lists now reject the known
literal author, including lists containing a legitimate actor alongside the
author. Added six separately written probes covering single/mixed lists for
coverage, platform exemption, and sensitivity exemption. All **221 independent
assertion probes** and **20 author unit tests** pass. No remaining implementation
blocker found within the stated supplied-assertion scope. This confirms label
computation on the tested fixtures; it does not authenticate agents, validate
scientific claims, or implement external organizational independence.
