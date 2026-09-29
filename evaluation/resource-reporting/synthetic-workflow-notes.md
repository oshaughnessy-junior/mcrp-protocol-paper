# Filled resource envelope: fictional small reconstruction

This is a fully specified **synthetic planning example**, not measured workload data, reviewer behavior, a usability study, billing evidence or an assurance award. `synthetic-workflow.json` uses the existing `mcrp-resource-envelope/0.1` schema. All numerical fields are `estimated`, including exact scenario assumptions represented by equal endpoints. `observed` on P/X means inspection of these declared scenario requirements only; it is not evidence that an actual run met them.

## Assumptions

A fictional full-mode check reconstructs a mean from three public synthetic values. One CPU is allocated for 180–360 seconds, including a failed attempt and retry; therefore CPU allocation is 1/20–1/10 device-hour. GPU use is stipulated zero. Input is stipulated 12 bytes; 24–48 transferred bytes allow rereads; memory, scratch and retained-result ranges are invented planning bounds. Retention is one week (604800 seconds), a future planning commitment, not elapsed observation. Setup takes 1/4–1/2 person-hour, review 1/2–1, operation 1/20–1/10, repair 1/10–1/5 and administration 1/10–1/5. They are stipulated nonoverlapping role/activity allocations; waiting is not active effort. One or two external agent service requests support clerical checking, with fictional token/runtime/price bounds. Agent service-internal compute is unavailable and excluded from C; it is not imputed as zero. A reports service consumption/cost, never scientific intelligence. No real logs or invoices exist for these assumptions.

The example's synthetic sources resolve to this note; real reporting must substitute immutable collector records. Distinct activity IDs express the scenario's disjoint H intervals; a validator cannot discover hidden physical overlap or verify the assumptions. No C+A sum is justified. Full mode identifies the proposed custody scope, not completed scientific disposition or full assurance.

## Requirements-v1

- `python3-standard-library`: the proposed script uses only the Python standard library.
- `one-cpu-no-gpu`: one CPU allocation, no GPU allocation, for this fictional reconstruction.
- `public-synthetic-inputs`: inputs have no private or restricted evidence.
- `no-restricted-data`: no restricted-data approval is a scenario requirement; zero access wait is a stipulation, not a measured grant interval.

These local predicate names are illustrative and are not a cross-domain requirements ontology. No conversion to the RO-Crate subset is claimed: that subset excludes resource envelopes.
