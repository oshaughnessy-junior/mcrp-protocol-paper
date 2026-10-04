# Bounded lifecycle transition traces

Run `python3 -m unittest discover -s examples/lifecycle-transitions -v` from the repository root. Standard library only; imports the sibling asserted-input assurance calculator.

The immutable view records exact claim/release/scope/policy, a material-event epoch, processed event IDs, and historical assessments. Submit checks trusted target/epoch assertions and calls the existing calculator. Observe/supersede withhold the current snapshot without editing history. Use `current_at`, not the stored `current` snapshot, for query-time expiry. This model assumes serialized compare-and-append and authenticated issuance stamps; neither is implemented as a production transaction or signature service. A caller must classify events as material and deliver them; this does not discover hidden events or dependency edges.

Six tests are synthetic traces, including the explicit missing-event limitation. New current-epoch assessments are newly asserted authority/evidence, not an implementation of obtaining it. Human actor strings do not authenticate a person. Supersession implements the conservative all-pending branch; sibling `revision-semantics/carry_eligible` demonstrates eligibility, but neither module implements the carry-forward signing/issuing service. Retained history is append-only by these API functions, not cryptographic tamper evidence or protected persistence.

Code is MIT licensed as in LICENSE. Prose remains under the repository's stated documentation license. No scientific or empirical validation is claimed.
