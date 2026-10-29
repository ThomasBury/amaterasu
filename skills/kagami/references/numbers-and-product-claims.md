# Numbers and product claims

## Arithmetic before interpretation

Record the numerator, denominator, unit, period, population, baseline, and source.
Recompute with available calculation tools; preserve precision and uncertainty.
For old and new rates expressed as percentages, percentage-point change is
`new - old`; relative change is `(new - old) / old * 100%`. A zero baseline makes
relative change undefined. Missing denominators can prevent comparing rates.

Example: defects fall from 8% to 6%. That is a 2-percentage-point decrease and a
25% relative decrease, not a 25-point decrease. Whether measurements are accurate
and whether the process change caused the decrease are separate questions.
A rise from 0 to 4 incidents has an absolute change of 4; its percentage growth
is undefined. A count doubling while exposure doubles does not imply rising risk.
Do not average percentages without the group denominators.

Check absolute versus relative risk, selection, missing observations, rounding,
and whether uncertainty permits the claimed precision. A p-value above a chosen
threshold is not evidence of equivalence; an equivalence claim needs a relevant
margin and appropriate analysis. Do not reverse it into proof of a difference.
These checks are elementary arithmetic and methodological safeguards, not a
statistical audit, replication, or validation of the measurements.

## Product and benchmark claims

Distinguish measured capability, prototype, roadmap, forecast, and commitment.
For speed or cost compare the same workload, dataset, quality target, hardware,
concurrency, versions, and measurement definition. Lower elapsed time and higher
throughput are different quantities. Report what “faster” means.

Example: one batch takes 10 seconds on A and 5 seconds on B under the same test
conditions. B has half the elapsed time; throughput is twice A's if work is equal.
This establishes neither every workload's performance nor a production guarantee.
A staging percentile is not an average or an availability promise. A vendor's
roadmap is evidence of its stated plan, not of a shipped feature. A missing
benchmark warrants a scoped unresolved verdict, not an accusation of deception.

## Evidence strength and citations

The formulas are arithmetic identities under the stated denominators; the product
checklist is a proposed engineering practice. Neither is evidence of Kagami's
accuracy or effectiveness. Preserve workload limits even when a claim is correct.

[Platt (1964)](https://pages.cs.wisc.edu/~markhill/science64_strong_inference.pdf)
informs comparison of explanations, not an automatic causal test. The foundation
review on 2026-10-29 inspected a transcription, not a replication.
[Serhii Korniienko's detector](https://github.com/SerhiiKorniienko/bullshit-detector)
informs provenance and explicit gaps as an operational implementation. Its
preliminary author/agent-curated evaluation does not validate this checklist.
No advanced statistical modules or external verification service are required.
