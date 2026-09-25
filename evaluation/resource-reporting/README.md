# Operational resource envelopes

See `paper/revisions/review1587-resources.md` for the collection procedure and its
limits. This directory contains a minimal stdlib JSON reporting template and
conservative validator/comparator. No actual resource measurements are supplied.

```sh
python3 -m unittest discover -s evaluation/resource-reporting -p 'test_*.py' -v
python3 evaluation/resource-reporting/resources.py
```

`template.json` includes placeholders and unavailable values for every metric.
Replace all context placeholders and timestamps before use. Validation of the
blank template establishes only its shape; it is neither completed reporting nor
MCRP conformance. Sources must resolve to version-bound provenance in real use;
the validator checks nonempty reference strings, not access, authenticity or truth.

Numeric `observed` values are point instrument readings, not error-free physical
truth. `estimated` intervals need explicit method and supporting sources. The
comparator treats uncertain intervals conservatively. Categorical requirements
are conjunctions of predicate IDs in one shared vocabulary; an empty set means
no recorded requirement, so adequate capture still requires external review.

Consumption summation is deliberately narrow. Users must not add C and A as
independent hardware costs, sum peaks or infer elapsed time from person-hours.
The code can detect reused activity IDs; it cannot detect aliases for one event.
Provider identities, hardware detail and role detail belong in the referenced
accounting/source manifests; this module does not collect them automatically.

CPU and GPU device-hours are not treated as equivalent compute; mixed hardware
sums are rejected. The comparator is a certified bound comparison, not a reflexive
order on uncertain envelopes: identical non-point intervals remain incomparable.

Original prose is CC BY 4.0; code is MIT licensed (LICENSE). Cited works retain
original rights. This is a proposed reporting profile, not a calibrated standard.
