# Independent resource-reporting review

Adoption-theory agent, 26 September 2026. Reviewed resource-reporting module,
tests, README and main-text insertion. Internal review, not instrument validation.

**Disposition:** no correctness blocker in the stated measurement-envelope scope.
Eight author tests pass. Independent probes confirm that making any individual
metric unavailable prevents comparison; every required comparison-context field
mismatch prevents comparison; mixed observed/estimated same-unit human-effort sums
retain exact interval endpoints; and validation/comparison do not mutate inputs.

The collection procedures distinguish allocation from utilization, sampled peaks
from physical maxima, measured elapsed lower bounds from completed access wait,
and retrospective estimates from observations. Numeric unknown cannot become zero,
and a blank validated template cannot be called a completed measurement. Exact
units, workload, mode, accounting boundary, interval, pricing and requirements
vocabulary bind comparisons. Unsupported overlaps remain outside syntactic proof.

Two precision improvements were sent to the author:

1. The comparator's docstring calls its relation a “weak order.” On uncertain
   envelopes it is not reflexive: an envelope compared with an identical interval
   is incomparable. This is a conservative certificate over potentially different
   realizations, not a mathematical weak order on report objects. Use “certified
   bound comparison” or explain that distinction explicitly.
2. The sum helper currently permits CPU and GPU device-hours to be combined because
   both use the generic device-hour unit. Such a sum can at most count heterogeneous
   occupied-device time; it cannot measure equivalent computation or substitutable
   capacity. State that limitation or reject cross-hardware sums. This does not
   affect the six-axis comparison but matters if a convenience total is displayed.

The manuscript insertion appropriately supplies an operational collection profile
without claiming calibrated instruments or empirical reporting agreement. Its
proposed independent collector exercise is a credible next validation step; the
toy tests are not that exercise.
