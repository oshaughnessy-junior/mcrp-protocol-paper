# Evidence audit responding to aiXiv review 1586

## Disposition of the historical counts

The reviewer correctly identifies a gap. Version 1.0 reported four checked claims,
nine scientific checks, thirteen unit tests, and eleven rejected corruptions for a
synthetic matched-filter implementation labelled 0.1.2. We cannot reconstruct an
itemized, public, version-bound mapping for those counts from the available
research source and validation records. We withdraw those numerical evidence
claims from the revised manuscript. This is an evidential correction, not a claim
that the historical run failed or never occurred. We also withdraw reliance on
its reported machine-pass status as current substantiation.

The search inspected the paper repository and its tracked tree, nearby MCRP
implementation and publication sources, targeted internal activity records, and
the public repository inventory. The paper repository contains a description,
not the matched-filter implementation. No unpublished internal records are
exported in this response. The historical source may remain unavailable elsewhere;
we do not infer nonexistence from failure to locate it.

| Version 1.0 assertion | Named public mapping recovered? | Revised evidential status |
|---|---|---|
| Four checked matched-filter claims | No | Withdrawn as supporting evidence |
| Nine scientific checks | No | Withdrawn as supporting evidence |
| Thirteen unit tests | No | Withdrawn as supporting evidence |
| Eleven rejected corruptions | No | Withdrawn as supporting evidence |

## Separate, inspectable prototype evidence

A newer prototype is publicly available at exact Git commit
`84d1abc0b3a7cb7738dec6a5b1ad9ed762bdcfe5`. This is a distinct implementation and evidence set. It is not
presented as the missing mapping for the older counts. A clean public source
archive was downloaded for this revision; the domain fixture subset was rerun
by an agent in the same author-directed team. The [public source archive](https://codeload.github.com/oshaughnessy-junior/trust-and-review-papers/tar.gz/84d1abc0b3a7cb7738dec6a5b1ad9ed762bdcfe5) fixes the inspected revision. There was no external scientific
sign-off. The audit JSON beside this file records the archive SHA-256, Python
version, all test names, source links, command output, and regenerated values.
A Git commit identifies source bytes but supplies neither a persistent archival
DOI nor guaranteed preservation. An archived deposition and an independent
scientific assessment remain outstanding.

From the downloaded archive root, reproduce with:

```sh
python3 -m unittest discover -s papers/07-release-packet/domains/fixtures -p 'test_*.py' -v
python3 papers/07-release-packet/domains/fixtures/domain_models.py
python3 papers/07-release-packet/domains/fixtures/replay_receipts.py
```

All 20 named tests passed. Both generated JSON objects matched their respective
committed outputs after parsing. These are deterministic, invented fixtures,
not experiments on real manuscripts or measurements of review efficacy.

| Case | Specific calculation/control | Observed narrow behavior |
|---|---|---|
| Physics | Shared-noise variance; calibration amendment | Exact variance 101/400 versus mistaken independent variance 29/1600; amplitude changes to 10; declared amendment requires reconsideration |
| Biology | Confounded treatment/batch models; crossed arithmetic | Two explanations have equal RSS 4; crossed contrast 1 does not by itself identify a causal effect; unsupported scope upgrades refused |
| Economics | Trial/target mixture and selection | Mixture 8/5 versus 2/5 under declared transport assumptions; completion share 100/109; separate reliance selection can change 1/10 to 1 |
| Law | Toy work ordering and deadline feasibility | FIFO misses one deadline; alternate order misses none for the feasible jobs; one infeasible example remains; legal-authority upgrade refused |
| Known failure | Planted dependency omitted from recorded graph | Undeclared change remains current under toy policy; declared change becomes pending; recall 1/2 on exactly two invented replays |

The last row is a deliberately observed failure of graph-only detection. It is
not relabelled as protection against omitted dependencies. Roles, outcomes,
control groups and clock inputs are locally supplied assertions; these fixtures
do not demonstrate authentication, qualified judgment or actual reviewer independence.

## Itemized test mapping

Names below identify test methods, not independently verified scientific claims.
Their assertions combine exact hand-computed values, countermodels, and negative
controls. Passing establishes only the stated behavior under these fixtures;
the test suite and implementation can still share mistaken assumptions.

| Test method | Immutable source | Rerun |
|---|---|---|
| `test_shared_variance_exact_hand_calculation` | [source line 15](https://github.com/oshaughnessy-junior/trust-and-review-papers/blob/84d1abc0b3a7cb7738dec6a5b1ad9ed762bdcfe5/papers/07-release-packet/domains/fixtures/test_domain_models.py#L15) | pass |
| `test_more_repeats_cannot_remove_shared_floor` | [source line 21](https://github.com/oshaughnessy-junior/trust-and-review-papers/blob/84d1abc0b3a7cb7738dec6a5b1ad9ed762bdcfe5/papers/07-release-packet/domains/fixtures/test_domain_models.py#L21) | pass |
| `test_zero_shared_error_recovers_independent_formula` | [source line 27](https://github.com/oshaughnessy-junior/trust-and-review-papers/blob/84d1abc0b3a7cb7738dec6a5b1ad9ed762bdcfe5/papers/07-release-packet/domains/fixtures/test_domain_models.py#L27) | pass |
| `test_distinct_biological_explanations_are_observationally_equal` | [source line 33](https://github.com/oshaughnessy-junior/trust-and-review-papers/blob/84d1abc0b3a7cb7738dec6a5b1ad9ed762bdcfe5/papers/07-release-packet/domains/fixtures/test_domain_models.py#L33) | pass |
| `test_unconditional_error_mean_does_not_supply_conditional_exogeneity` | [source line 40](https://github.com/oshaughnessy-junior/trust-and-review-papers/blob/84d1abc0b3a7cb7738dec6a5b1ad9ed762bdcfe5/papers/07-release-packet/domains/fixtures/test_domain_models.py#L40) | pass |
| `test_same_crossed_observations_can_have_zero_causal_effect` | [source line 46](https://github.com/oshaughnessy-junior/trust-and-review-papers/blob/84d1abc0b3a7cb7738dec6a5b1ad9ed762bdcfe5/papers/07-release-packet/domains/fixtures/test_domain_models.py#L46) | pass |
| `test_interaction_is_not_mislabeled_as_an_exact_additive_effect` | [source line 56](https://github.com/oshaughnessy-junior/trust-and-review-papers/blob/84d1abc0b3a7cb7738dec6a5b1ad9ed762bdcfe5/papers/07-release-packet/domains/fixtures/test_domain_models.py#L56) | pass |
| `test_transport_changes_estimand` | [source line 68](https://github.com/oshaughnessy-junior/trust-and-review-papers/blob/84d1abc0b3a7cb7738dec6a5b1ad9ed762bdcfe5/papers/07-release-packet/domains/fixtures/test_domain_models.py#L68) | pass |
| `test_equal_completion_preserves_offered_share` | [source line 74](https://github.com/oshaughnessy-junior/trust-and-review-papers/blob/84d1abc0b3a7cb7738dec6a5b1ad9ed762bdcfe5/papers/07-release-packet/domains/fixtures/test_domain_models.py#L74) | pass |
| `test_final_reliance_can_select_again_after_completion` | [source line 79](https://github.com/oshaughnessy-junior/trust-and-review-papers/blob/84d1abc0b3a7cb7738dec6a5b1ad9ed762bdcfe5/papers/07-release-packet/domains/fixtures/test_domain_models.py#L79) | pass |
| `test_no_reliance_is_undefined_not_zero_adverse_share` | [source line 84](https://github.com/oshaughnessy-junior/trust-and-review-papers/blob/84d1abc0b3a7cb7738dec6a5b1ad9ed762bdcfe5/papers/07-release-packet/domains/fixtures/test_domain_models.py#L84) | pass |
| `test_no_completions_is_undefined_not_zero` | [source line 89](https://github.com/oshaughnessy-junior/trust-and-review-papers/blob/84d1abc0b3a7cb7738dec6a5b1ad9ed762bdcfe5/papers/07-release-packet/domains/fixtures/test_domain_models.py#L89) | pass |
| `test_missing_target_support_refused` | [source line 94](https://github.com/oshaughnessy-junior/trust-and-review-papers/blob/84d1abc0b3a7cb7738dec6a5b1ad9ed762bdcfe5/papers/07-release-packet/domains/fixtures/test_domain_models.py#L94) | pass |
| `test_equal_aggregate_work_different_deadline_outcomes` | [source line 98](https://github.com/oshaughnessy-junior/trust-and-review-papers/blob/84d1abc0b3a7cb7738dec6a5b1ad9ed762bdcfe5/papers/07-release-packet/domains/fixtures/test_domain_models.py#L98) | pass |
| `test_scheduler_cannot_drop_a_job_to_claim_success` | [source line 104](https://github.com/oshaughnessy-junior/trust-and-review-papers/blob/84d1abc0b3a7cb7738dec6a5b1ad9ed762bdcfe5/papers/07-release-packet/domains/fixtures/test_domain_models.py#L104) | pass |
| `test_digest_stable_under_mapping_order_but_changes_with_content` | [source line 108](https://github.com/oshaughnessy-junior/trust-and-review-papers/blob/84d1abc0b3a7cb7738dec6a5b1ad9ed762bdcfe5/papers/07-release-packet/domains/fixtures/test_domain_models.py#L108) | pass |
| `test_all_replays_amend_then_support_a_new_version` | [source line 112](https://github.com/oshaughnessy-junior/trust-and-review-papers/blob/84d1abc0b3a7cb7738dec6a5b1ad9ed762bdcfe5/papers/07-release-packet/domains/fixtures/test_domain_models.py#L112) | pass |
| `test_biology_and_law_unsafe_authority_upgrades_rejected` | [source line 120](https://github.com/oshaughnessy-junior/trust-and-review-papers/blob/84d1abc0b3a7cb7738dec6a5b1ad9ed762bdcfe5/papers/07-release-packet/domains/fixtures/test_domain_models.py#L120) | pass |
| `test_amended_receipts_bind_recomputed_domain_results` | [source line 124](https://github.com/oshaughnessy-junior/trust-and-review-papers/blob/84d1abc0b3a7cb7738dec6a5b1ad9ed762bdcfe5/papers/07-release-packet/domains/fixtures/test_domain_models.py#L124) | pass |
| `test_hidden_dependency_is_a_recorded_known_failure` | [source line 129](https://github.com/oshaughnessy-junior/trust-and-review-papers/blob/84d1abc0b3a7cb7738dec6a5b1ad9ed762bdcfe5/papers/07-release-packet/domains/fixtures/test_domain_models.py#L129) | pass |

## Suggested manuscript replacement for Section 7

The previously reported 0.1.2 counts (four claims, nine checks, thirteen tests,
eleven corruptions) lacked a recoverable itemized public mapping. We withdraw
those numerical assertions as evidence. For an inspectable, distinct demonstration,
we instead identify the newer public agent-first prototype at source commit
`84d1abc0b3a7cb7738dec6a5b1ad9ed762bdcfe5`. Its deterministic domain fixture subset contains 20 named unit tests;
a clean source-archive rerun by our agent team passed all 20 and reproduced both
committed JSON outputs. The itemized evidence supplement links every test to
immutable source and records the archive hash and run output. These fixtures
illustrate claim-version amendments, scope restrictions, exact toy arithmetic,
and a known missed-dependency failure. They neither reconstruct the historical
matched-filter evidence nor establish independent scientific sign-off, real-workflow
performance, or MCRP assurance. No archival DOI is claimed for this source commit.
