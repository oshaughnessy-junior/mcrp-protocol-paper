# Revision semantics fixture

Added for aiXiv review 1586. This is **new**, synthetic author-side evidence and
must not be counted as the historical v0.1.2 verifier's tests.

```sh
python3 -m unittest discover -s examples/revision-semantics -v
python3 examples/revision-semantics/semantics.py
```

The implementation validates a finite typed graph, rejects cyclic computational
derivation, computes old/new-union revision reachability, and tests eligibility
for explicitly authorized carry-forward. It does not implement scientific truth,
authentication, archive storage, materiality discovery, or an executed carry-forward
transition. Actor IDs, prior decisions, version identities, status/clock evidence, and delta conclusions
are trusted fixture inputs. See `paper/revisions/aixiv-review-1586-semantics.md`
for definitions, proofs, and counterexamples.
