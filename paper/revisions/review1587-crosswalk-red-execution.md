# Independent executable inspection of the transport example

Author-directed evidence agent; separate inspection within the same team. No
independent scientific sign-off or external standards certification is implied.

All 14 crosswalk unit tests passed. Additional probes, written independently of
the supplied test harness, found:

- The closed supported SRR object survives exact exporter/importer round-trip.
- All 17 custom MCRP property removals are individually present in the loss
  manifest. The stripped graph contains neither custom MCRP properties nor
  custom MCRP types; it cannot be imported as a supported reliance record.
- An unknown non-MCRP property inserted at each of the nine graph entities is
  rejected. Unknown fields are not silently discarded.
- Replacing one payload byte while preserving total byte length is rejected
  by the actual SHA-256 check. Size equality alone cannot pass.

No blocker was found for the bounded transport demonstration. The following
scope distinctions are required in publication:

1. `verify_payloads` verifies the explicitly listed artifact payloads, not the
   integrity of the whole crate. The local `profile.html` is checked for existence
   but its bytes are not hashed by this helper. Do not claim full-package/profile
   integrity from this check.
2. Descriptor/root-shape assertions are selected metadata checks. The strict
   custom inverse checks self-consistency with its own exporter, not generic
   JSON-LD equivalence or the entire RO-Crate specification.
3. An independent standards validator and independently implemented consumer
   were not run in this inspection. The code records these limits. If subsequent
   work adds them, report exact tool versions and checks separately.
4. The release identity, actor, policy and expiry are transported fields. Keeping
   their text intact neither authenticates the actor nor evaluates whether the
   scientific decision should be trusted.

A generic metadata consumer may still discover names, types and listed files.
The explicit loss projection demonstrates why those discovery fields do not
preserve MCRP scope, authority, expiry or change-propagation semantics by themselves.
