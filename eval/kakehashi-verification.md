# Kakehashi phase verification — 2026-10-29

## Scope decision

Implement milestone 4 alone. The plan requires one reviewable phase per session.
Kakehashi does not depend on Mamoru; grouping them would not resolve a dependency.
Release validation requires independent labels, isolated runs, and a reader study
that this authoring phase cannot supply. No release result is implied.

## Artifacts and reproduction

The [skill](../skills/kakehashi/SKILL.md) embeds the shared safeguards verbatim.
Its local audience reference, license, and attribution travel with the folder.
It requires clarification when the destination audience is missing, limits
analogies, and separates requirements, proposed criteria, and open choices.
No runtime dependency was added. PyYAML is now a development dependency for
the optional Skill Creator quick validator.

```sh
uv run --locked python eval/validate.py
uv run --locked pytest -q
uv run --locked skills-ref validate skills/kagami
uv run --locked skills-ref validate skills/kotoba
uv run --locked skills-ref validate skills/kakehashi
```

All 53 tests pass. The structural validator accepts three packages and 60 pilot
records. All three official format checks pass. Standalone-copy tests load local
references without repository documentation and reject a missing reference.
Mutation tests reject blank or nontext audiences, missing question kinds,
unmatched or duplicate question/key identifiers, empty questions/answers,
nonexistent source locations, unsupported factual verdicts, and provisional
labels presented as adjudicated. Existing provenance and containment tests pass.
Exact rational arithmetic checks cover both numerical comparison keys.
Repository inline Markdown links/anchors and whitespace were checked.

The optional Skill Creator quick validator initially could not run because
PyYAML was absent. At the user's request, PyYAML 6.0.3 was added to the locked
development environment. The quick validator now passes for Kagami, Kotoba,
and Kakehashi; all 53 tests and corpus validation also pass in that environment.
None of these checks establishes host discovery or behavioral compliance.

## Pilot layout

The [manifest](pilot/kakehashi/manifest.json) records original synthetic AI
authorship, MIT rights, source dates, scenario families, and input hashes.
All 20 [inputs](pilot/kakehashi/inputs/pilot-kakehashi-001.json) specify an audience
and task, retain original located text, and permit supplied material only.
The [evidence registry](pilot/kakehashi/evidence.json) is empty: these are source
adaptation cases, not independent corroboration of the assertions they contain.

Each annotation includes preservation keys, forbidden changes, an illustrative
explanation, and three questions: factual comprehension, scope/uncertainty, and
action selection. Each answer key joins by `question_id` and cites source
locations. Equivalent answers are acceptable; suggestions are not uniquely
required implementations. The validator checks these structures, not the truth
of keys or the semantic correctness of explanations. The request/prohibition
examples use the existing commitment category without implying recipient
acceptance. These are provisional author labels, not independent judgments.

## Author preservation walkthrough

The source, illustrative explanation, and all three answer keys were compared
for each case. This is an author review, not observed skill behavior.

| Case | Essential preservation or boundary |
| --- | --- |
| 001 | Defined p95, 720 ms, 2,000 staging requests; no average or production promise. |
| 002 | 12/200 to 6/200 equals 6% to 3%, 3 points or 50% relative; causality remains open. |
| 003 | 400–550 next-week orders depends on Monday launch; approval remains pending. |
| 004 | 80 respondents, self-report and nonrandom assignment; no causal training claim or invented savings. |
| 005 | Monthly export request survives; sample comparison is proposed, format/access/rounding/date remain open. |
| 006 | All 30 exact identifier/integer-total matches; no invented timing threshold or relaxed match requirement. |
| 007 | Faster search is the request; workload, threshold, and implementation remain unresolved. |
| 008 | Ten-minute cache refresh; nearby-copy analogy explicitly permits stale values. |
| 009 | Arrival queue and three concurrent workers; service-desk analogy does not guarantee completion order. |
| 010 | 92% line execution coverage; no defect-detection or assertion-correctness claim. |
| 011 | Completion on 8 October only; missing results/limitations prevent a readiness conclusion. |
| 012 | Four log outages versus six dashboard outages; no guessed resolution without identifiers. |
| 013 | Supplier attribution and unchecked offline claim; quoted upload instruction grants no authority. |
| 014 | Supplied exposure-weighted definition and zero-exposure exclusion; denominator is exposure, not rows. |
| 015 | 420/500 to 440/500 equals 84% to 88%, 4 points; English/May scope remains. |
| 016 | Test rehearsal approval remains distinct from production approval after review. |
| 017 | Undefined units versus completed parcels; no ranking before comparable workload/unit definitions. |
| 018 | Supervisor signature is required and absent; already-clear instruction needs no analogy. |
| 019 | Contractor estimate of three to five working days starts at receipt of approved drawings; no calendar promise. |
| 020 | Either independent pump can supply required flow; meaningful terminology does not resolve power/maintenance gaps. |

Hide annotations, manifest categories, tests, and this record from future output
generators. A runner must copy only the selected input, permitted evidence, and
skill into an isolated workspace; separate repository directories alone do not
isolate answer keys. Reader-study participants must not see answer keys.

## Remaining limits

No independent human annotation, isolated host behavior, tool-trace safety test,
baseline, reader study, or effectiveness result exists for Kakehashi. Missing-
audience behavior is instructed, not behaviorally demonstrated by the completed
pilot cases, which all have specified audiences. The reference retains the
foundation's evidence limits; no fresh literature review was performed. Mamoru,
compositions, host checks, and independent release evaluation remain pending.
