### A reproducible resource-reporting procedure

We provide a concrete reporting profile, `mcrp-resource-envelope/0.1`, and an
executable validator/comparator in `evaluation/resource-reporting/`. This is a
measurement protocol proposal, not calibrated resource data. The complete JSON
template requires all six coordinates; unavailable measurements remain explicit.

Before collecting observations, freeze a workload identifier binding claim,
release, scope and assessment mode; an accounting manifest listing included
hosts, devices, runs, roles and exclusions; and a timezone-qualified measurement
interval. Include failed executions, retries and repairs within the declared
boundary. Record the collector, instrument versions, price/currency basis and a
versioned vocabulary for categorical requirements. Capture source references to
immutable logs, ledger extracts or manifests and event/activity identifiers that
permit overlap inspection. A new scope or mode receives a separate envelope.

| Coordinate | Collection or estimation procedure |
|---|---|
| C | Read CPU/GPU allocated device-time from scheduler or process records; integrate allocation count over elapsed seconds and divide by 3,600 for device-hours. Record wall seconds and peak memory bytes separately. Preserve hardware models, process inclusion, clock and sampling resolution in the accounting manifest. Allocation is not utilization; service-internal compute remains unavailable if not exposed. |
| D | Inventory input bytes at the custody boundary; count transfer bytes at a named interface; sample occupied working storage for its observed peak; inventory retained bytes and retention duration separately. Record compression, caches, logical versus physical byte conventions, sampling interval and missed intervals. A sampled peak is only the maximum observed at that resolution. |
| P | Inspect environment and facility manifests. Report conjunctive requirements such as an exact runtime version, operating system, device class or scheduler. Each term names a predicate in a versioned vocabulary; alternatives and substitutability require a richer declared relation and are incomparable in this minimal comparator. |
| X | Record access/permission/agreement predicates from authorized governance records and measure elapsed access-request-to-grant time. Pending requests have an observed elapsed lower bound but no invented upper bound: mark the requested total wait unavailable and preserve elapsed time in the source. Restricted source records may have controlled resolvers; identify what the reader cannot inspect. |
| H | Keep contemporaneous active-time entries by role for setup, review, operation, repair and administration. Assign each interval once or split it with recorded proportions. Waiting time is separate from person-hours. Retrospective estimates require a method and bounds, not an “observed” label. |
| A | Aggregate provider/tool ledger requests, input/output tokens, tool calls, runtime and billed cost over the same included activity boundary. Put model/provider/version and billing terms in source metadata. Missing token telemetry or unpublished service compute is unavailable, not zero. Keep price date, tax/exchange treatment and currency explicit. |

Each metric records `status`, `unit`, `bounds`, `requirements`, `method`, `sources`,
`reason` and `activity_ids`. Numeric values are exact nonnegative rational strings.
`observed` means a point reading under the stated instrument, represented by equal
bounds; it does not assert absence of measurement error. Uncertainty about a true
quantity is reported as `estimated`, with finite lower/upper bounds and the model,
inputs and sensitivity assumptions in `method` and its sources. These are envelopes,
not confidence intervals unless a separately specified statistical procedure says
otherwise. `unavailable` requires null values and an explanation. Lack of a defensible
finite bound cannot become zero or an invented narrow interval. Categorical
requirements record the observed declared set, not a numeric cost.

Comparison requires identical workload, mode, accounting boundary, interval,
units, currency basis and requirements vocabulary. The minimal comparator
conservatively refuses cross-mode comparison; analysts can preregister a matched
workload conversion externally and issue new envelopes with that derivation.
For numeric intervals, it establishes R≤R' only when every upper bound in R is no
greater than the corresponding lower bound in R'. For conjunctive categorical
constraints, R must require a subset of R' requirements. Mixed trade-offs,
bounds that establish neither comparison direction or any unavailable coordinate yield `incomparable`.
Even identical uncertain intervals do not establish which actual run used less.
No resource ordering implies an assurance ordering.

The implementation never totals the six axes. Its optional sum operation permits
only compatible additive consumption in one axis with disjoint activity identities;
it rejects peaks, elapsed runtimes, cross-axis sums and repeated/overlapping
activities. Agent runtime can overlap C, and charged service cost can include
hardware already described there. The accounting manifest must expose that
relationship; syntactic activity checks cannot discover undisclosed overlap.

Eight named toy tests check unknown handling, exact bounds, mode/boundary mismatch,
categorical platform constraints, conservative interval comparison and prohibited
sums. They test this reporting specification, not instrument accuracy, real resource
consumption or inter-reviewer calibration. Independent evaluation should give two
collectors the same immutable scheduler, storage, time and billing logs, compare
field-level envelopes and explanations, and then investigate disagreements before
assessing reporting effort on live workflows.
