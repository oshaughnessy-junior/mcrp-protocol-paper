# Recomputing proposed assurance labels

This is an executable **synthetic profile** of revised Section 6 in
`paper/position-paper.md`, following review 1586. It computes labels from supplied
assertions. It does not authenticate identities, prove reviewer independence or
human qualification, resolve evidence references, verify digests, execute science,
validate coverage arguments, discover hidden dependencies, or provide production
conformance. `sha256:synthetic-release` is visibly a fixture identifier, not a hash.
No input in this example should be presented as real scientific sign-off.

## Run

From the repository root:

```sh
python3 -m unittest discover -s examples/assurance-assignment -p 'test_*.py' -v
python3 examples/assurance-assignment/run_demo.py
```

The second command prints the retained `results.json`. Python standard library
only; no network, credentials, clocks, services, or scientific executables are
used. Times are explicit nonnegative **synthetic ticks**. At `at == expires_at`,
the supplied predicate is expired. This code cannot detect a real expiry event
omitted from its inputs.

## Exact mapping to the proposed rules

| Paper obligation | Model representation / decision |
|---|---|
| Assessment indexed by claim, release, scope, policy and time | Immutable `Context`; each `Outcome.binding` must equal the entire assessment context. A mismatch is rejected, not silently recycled. |
| All S1 gates required | `external_admission`, `content_identity`, `claim_mapping`, `provenance`, `trust_leaves`, `acceptance_tests`, `negative_controls`, `archive_identity`, `human_scientific_disposition`. |
| Additional S2 gates | `non_author_reconstruction`, `execution`, `comparison`. |
| Additional mandatory S3 gates | `independent_challenge`, `overall_sensitivity`, `freshness_exercised`. |
| Specific S3 subcases | A fixed policy inventory supplies named `platform:*` and `sensitivity:*` cases. This example requires at least one platform applicability decision. Each subcase must pass or satisfy its named predeclared exemption rule. |
| Missing evidence is unknown | An absent outcome or missing evidence reference, role, rationale, or authorized actor fails that gate. Missing does not become pass. |
| Non-exemptible minimum | No rule can declare an exemption for any S1/S2 gate or the three mandatory S3 gates. An asserted `not-applicable` outcome for these gates fails. |
| Permitted nonapplicability | The subcase must have a predeclared rule; outcome must name that exact rule and a separately recorded policy-authorized exemption actor, with evidence and rationale. Overall sensitivity cannot be waived. |
| Separately authorized external admission and qualified human disposition | Their actor IDs must occur in the externally supplied policy's corresponding authorized lists. The policy rejects the actor literally named `author` for these gates and for non-author reconstruction, execution, comparison and independent challenge. It also rejects that known actor in exemption and full-scope coverage authorizer lists. Real producer/controller discovery and qualification are **outside** the engine. |
| Current and undisputed status | Assessment and outcome freshness default to `pending`. A caller must explicitly assert `current`. Any configured outcome marked stale, expired, withdrawn, pending, disputed, or expired by the stated tick withholds the entire current claim label. |
| Slice/checkpoint full-claim coverage | Full coverage requires a separate reference, rationale and policy-authorized coverage actor. The checker verifies these fields, not the scientific argument. |
| Audit-only / unassessed coverage | Caps the claim label at 1 even if execution assertions say pass. The `witness` mode also caps at 1: it cannot become a non-author rerun. |
| Partial scope | A bounded claim assessment can retain a level with visible partial coverage; any release-wide label is withheld. |
| Release aggregate | Must contain exactly one assessment for every prospectively fixed material claim, in one release/policy/time context and at its exact full scope. Duplicates, extra claims or mixed contexts are rejected; missing claims or partial/withheld components withhold aggregate. |
| Level 0 is not acceptance | Empty evidence yields level 0. `ReleaseResult.accepted` requires a current aggregate >=1. An empty material inventory is rejected. |

S1 has nine predicates, S2 has twelve, and the mandatory part of S3 has fifteen.
The fixture adds two identified subcases, giving seventeen outcome assertions.
The core engine does not accept a caller-specified smaller mandatory inventory.
A policy may select domain subcases prospectively, but the engine cannot prove
when the policy was fixed or that it includes every scientifically relevant case.
It cannot discover undisclosed common control. Those are trusted-input obligations,
not facts inferred from matching role strings.

`Result.predicate_level` is a diagnostic calculation from qualifying fields;
it is **not** a historical award and is never a substitute for `current_level`.
`None` means a current label is withheld. A zero current level means inspected
nonconforming disclosure, not positive acceptance. The original immutable input
can be retained by callers alongside later assessments; this module has no event
store and does not manufacture a historical acceptance record.

## Boundary tests and retained demonstrations

Named tests exercise every core gate under omission, failure, unknown and forbidden
nonapplicability; missing evidence and author substitution; expiry at the boundary;
all withheld statuses; context substitution; duplicate records; invalid policy
inventories; authorized and unauthorized subcase exemptions; slice coverage;
witness caps; material-inventory omissions; empty-inventory acceptance; and input
nonmutation. The tests compare labels to the explicit mathematical gate hierarchy.
They do not claim evidence that any scientific reviewer is correct.

Eight demonstrations retain complete claim/release outputs: all asserted passes,
missing human disposition, author self-admission, expired comparison, partial
slice, unjustified full slice, authorized platform nonapplicability, and forbidden
core exemption. The apparently successful case succeeds only because a synthetic
fixture asserts every required real-world premise.

Frozen dataclasses and immutable tuple inventories prevent in-place changes to
admitted records. The API is a local typed-object reference, not a hardened JSON
parser or concurrent authorization service. Malformed structure may raise
`ValueError`; withholding a well-formed but incomplete scientific record is a
separate outcome. No claim is made about transport, adversarial Python objects,
cryptographic signatures, external services, or resource admission control.

Original documentation is offered under CC BY 4.0. Code is MIT licensed (see
LICENSE). These scoped terms do not relicense cited works.
