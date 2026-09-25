# Main-text insertion for review 1587: a fully enumerated assessment

**Integration:** insert the following subsection in Section 6 immediately after the
level equation and exemption paragraph; retain existing currentness/coverage and
resource paragraphs. This is a specified synthetic profile, not scientific
validation. The editorial note at the end is for the response letter only.

### A finite assignment profile and recorded example

For profile `synthetic-policy-v1`, the complete predicate inventory is Table 2.
S1 contains its nine level-1 rows; S2 adds the three level-2 rows; S3 adds all five
level-3 rows. The final two rows are explicitly named domain subcases. Requiring
at least one platform-applicability entry is an implementation choice of this
finite profile, stricter than the generic inventory description: absence is not
silently interpreted as “no relevant platform.” Other profiles must publish their
own complete subcase inventories before assessment.

| Exact identifier | First required level | Required evidence meaning | E0 | E2 | E3 |
|---|---:|---|---|---|---|
| `external_admission` | 1 | Separately authorized admission bound to candidate | P | P | P |
| `content_identity` | 1 | Identified claim-bearing objects | P | P | P |
| `claim_mapping` | 1 | Material claims mapped to evidence | P | P | P |
| `provenance` | 1 | Declared-boundary evidence paths | P | P | P |
| `trust_leaves` | 1 | Unexamined dependencies declared | P | P | P |
| `acceptance_tests` | 1 | Prospective claim predicates checked | P | P | P |
| `negative_controls` | 1 | Specified adversarial/negative controls checked | P | P | P |
| `archive_identity` | 1 | Version-specific archival identity | P | P | P |
| `human_scientific_disposition` | 1 | Qualified independent human disposition | M | P | P |
| `non_author_reconstruction` | 2 | Reconstruction under reviewer control | P | P | P |
| `execution` | 2 | Reviewer-controlled run evidence | P | P | P |
| `comparison` | 2 | Claim-bearing results meet stated comparisons | P | P | P |
| `independent_challenge` | 3 | Independent method/data challenge | P | U | P |
| `overall_sensitivity` | 3 | Overall material-choice sensitivity assessment | P | P | P |
| `freshness_exercised` | 3 | Freshness/failure response exercised | P | P | P |
| `platform:alternative` | 3 | Relevant alternative-platform subcase | P | P | NA |
| `sensitivity:calibration` | 3 | Material calibration-choice subcase | P | P | P |

P means recorded pass; U means recorded unknown; M means the record is missing;
NA means authorized not-applicable. E0, E2, and E3 are three separate synthetic
assessment records for the same context, not three votes or simultaneous records
to be selected retrospectively. Their level calculations are 0, 2, and 3.

The common recorded context is claim `claim-1`, release
`sha256:synthetic-release`, scope `full toy claim`, policy
`synthetic-policy-v1`, and assessment tick 10. The release string is a synthetic
identifier, not an actual digest. Mode and coverage are both `full`. All three assessments explicitly assert current freshness. Each supplied
row explicitly asserts `current`, has evidence reference `fixture:<identifier>`,
rationale `synthetic evaluator assertion`, role `fixture role`, and an exact copy
of the common context. The authorized actor is `external-verifier`, except that
human disposition uses `human-reviewer`. These strings are fixture assertions;
they do not establish real independence, human qualification, archive deposition,
or scientific adequacy. No expiry is asserted in this example. A supplied expiry
at or before tick 10 would withhold the current label.

For this profile, only two applicability rules exist:

1. `platform:alternative` may be NA under
   `no-relevant-alternative`, with a separately recorded `domain-steward`
   authorization, evidence and rationale.
2. `sensitivity:calibration` may be NA under
   `no-material-calibration-choice`, with the same required authorization fields.

The rule identifiers denote domain conclusions that must be justified outside
the label calculator; strings alone cannot establish applicability. No other
predicate can be exempted. In particular, `overall_sensitivity` remains required
even when an individual sensitivity subcase is inapplicable. E3 records the first
rule and `domain-steward` as exemption actor for its NA row. E0 has no human-
disposition row at all; E2 retains evidence of an assessment whose independent-
challenge result is unknown. Missing evidence reference, role, rationale or
authorized actor prevents a supplied row from satisfying its gate.

Thus E0 fails S1 and cannot be accepted; later passes do not compensate for a
missing prerequisite. E2 satisfies S2 but not S3. E3 satisfies every S3 obligation
under its one authorized subcase disposition. A failed core predicate gives the
same level ceiling as a missing or unknown core predicate. Unknown scientific
outcome differs from disputed or expired authority: any noncurrent/disputed
component withholds the current label rather than reporting its old result as
current. A historical award must be separately retained, not inferred from a new
calculation over stale fields.

Scope aggregation adds a further condition. Two current, full-scope material
claims at levels 3 and 2 give release level 2. A partial-scope second assessment
withholds the release label, even if its local level is 3. Missing or duplicate
material claims, a mismatched release/policy/time, or an unjustified full-scope
`slice`/`checkpoint` assessment cannot produce an aggregate. An empty claim
inventory cannot pass vacuously. Level 0 is disclosure, not accepted conformance.

The implementation in `examples/assurance-assignment/assurance.py` exposes these
identifiers and consumes immutable outcome records. Its demonstration and tests
reproduce the gate hierarchy, forbidden exemptions, currentness, and scope
aggregation. It checks supplied assertions and declared actor allow-lists; it
neither authenticates those actors nor performs the scientific checks represented
by the rows. The worked level-3 result is therefore an arithmetic example, not
an MCRP-3 award to this manuscript or its prototype.

## Editorial response note: formal appendix was already supplied

The downloaded aiXiv version-1.1 PDF contains Appendix A: A.1 graph/claim-contract
semantics on page 9; A.2 change roots and closure on page 10; A.3 exact carry-
forward eligibility, Current, and Proposition S2 on page 11; A.4 worked failure
cases on page 11; A.5 executable evidence on page 12. The review's blanket
statement that no formal carry-forward semantics were provided is therefore
inaccurate. Respond respectfully with these exact locations and improve main-text
signposting. The request for a complete main-text assurance inventory and recorded
assessment is valid; Appendix A did not supply that different inventory.

Identical claim words do not establish unchanged support: A.1 binds a versioned
claim contract, and A.2 marks declared changed evidence and changed dependency
edges as roots. A.3 then blocks carry-forward for reachable changed support, even
if the claim text remains identical. Missing dependencies remain an explicit
failure premise; these finite semantics do not demonstrate empirical efficacy.
