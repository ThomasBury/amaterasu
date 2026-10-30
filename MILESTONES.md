# Implementation milestones

Implement one phase per session. Each phase must leave a coherent, reviewable
repository and a verification record before stopping. Later phases are pending,
not implicit claims about existing capability.

## 1. Foundation — complete

- [x] Record the evidence assessment, methodological limits, and upstream reuse
  decisions in [docs/evidence.md](docs/evidence.md).
- [x] Define shared safeguards and the four input/output contracts in
  [docs/contracts.md](docs/contracts.md).
- [x] Add MIT licensing and third-party attribution boundaries.
- [x] Define the pilot annotation rubric, independent evaluation design, and
  proposed release gates in [eval/README.md](eval/README.md) and
  [eval/annotation-rubric.md](eval/annotation-rubric.md).
- [x] Define portability requirements without claiming runtime compatibility.

Verification (2026-10-29): inspected research sources and recorded unavailable or
partially inspected material; verified 23 relative links/anchors across eight
Markdown files, corpus totals, and the exact zero-of-60 bound (4.870291%);
checked whitespace in all nine new files, including the license.
No skill, host, baseline, human annotation, or effectiveness test has run.

## 2. Kagami — complete

- [x] Create `skills/kagami/SKILL.md`, with all essential shared safeguards
  embedded and no dependency on repository-level documentation.
- [x] Add `references/evidence-and-arguments.md` and
  `references/numbers-and-product-claims.md` inside that skill.
- [x] Implement supplied-evidence analysis first, then bounded public research.
- [x] Prepare 20 pilot cases; preserve original input and evidence provenance.
  Keep provisional author labels distinct from independent human labels.
- [x] Add the needed development stack (`pyproject.toml`, `uv.lock`, pytest,
  existing `skills-ref`) and small `eval/validate.py` checks for local references,
  identifiers, evidence hashes, required fields, and shared-rule consistency.
- [x] Verify standalone reference loading, numerical correctness, provenance,
  malicious quoted instructions, incomplete evidence, and appropriate abstention.
  Add meaningful validator tests in `tests/test_eval.py`.

Verification (2026-10-29): 20 original synthetic pilot cases with separate
provisional AI-author labels; 23 pytest tests, official skills-ref format check,
and local corpus validation pass. Standalone file loading, arithmetic, provenance,
and safeguard/abstention author walkthrough are recorded in
[eval/kagami-verification.md](eval/kagami-verification.md). No independent human
annotation or isolated host behavioral run has been performed. Kagami was kept
alone because later skills are independent phases; release tests remain pending.

## 3. Kotoba — complete

- [x] Create the standalone skill and `writing-and-accountability.md` reference.
- [x] Prepare 20 pilot cases and check preservation of quantities, attribution,
  uncertainty, scope, commitments, voice, and warranted firmness.
- [x] Check drafting from notes as well as revision; retain visible gaps.

Verification (2026-10-29): 20 original synthetic cases (12 revisions, eight drafts)
with separate provisional AI-author annotations; all 32 pytest tests, official
skills-ref checks for both packages, and validation of 40 pilot records pass.
Standalone reference loading and all 20 preservation examples were checked;
see [the verification record](eval/kotoba-verification.md) for scope and the
initial quick-validator limitation and subsequent successful rerun. No independent human annotation
or isolated host behavioral run was performed. Kotoba was kept alone because
remaining skills do not resolve a dependency; release validation remains pending.

## 4. Kakehashi — complete

- [x] Create the standalone skill and `audiences-and-meaning.md` reference.
- [x] Prepare 20 pilot cases with specified audiences and answer-keyed
  comprehension/action questions.
- [x] Verify technical fidelity, limited analogies, and separation of stated
  requirements from proposed acceptance criteria.

Verification (2026-10-29): 20 original synthetic cases with specified audiences,
60 comprehension/scope/action questions and provisional AI-author answer keys;
all 53 pytest tests, official skills-ref checks for all three packages, and
validation of 60 pilot records pass. Standalone loading, numerical keys, and
an author preservation walkthrough are recorded in
[the verification record](eval/kakehashi-verification.md). After adding PyYAML
as a development dependency, the optional quick validator also passes for all
three packages. No independent human annotation or
isolated host behavioral run was performed. Kakehashi was kept alone because
Mamoru is independent and release validation requires later independent work.

## 5. Mamoru — implemented; workplace-expert review pending

- [x] Create the standalone skill and `commitments-and-conduct.md` reference.
- [x] Prepare 20 pilot cases.
- [ ] Obtain workplace-expert review of conduct labels.
- [x] Verify conditional commitments, actual authority, ordinary feedback,
  documented threats, chronology, and proportionate response options.

Verification (2026-10-29): 20 original synthetic cases with hashed source
snapshots and separate provisional AI-author annotations; all 60 pytest tests,
validation of four packages and 80 records, and both Mamoru format checks pass.
Standalone loading, provenance, and the author walkthrough are recorded in
[the verification record](eval/mamoru-verification.md). The user volunteered as
workplace expert; the [20-case review sheet](eval/mamoru-expert-review.md) awaits
actual assessment. Milestone 5 remains open until review is recorded. No
independent human annotation or isolated host behavioral run was performed.
Mamoru stays alone: release validation requires independent work and is not a
dependency of this implementation.

## Improvement sequence — one phase per implementation session

This four-phase sequence improves the existing four standalone skills. It is
separate from the full release evaluation below. Keep names and directories,
preserve unrelated work and branding assets, and stop after each reviewable
phase. Human review and returned Claude runs remain explicit dependencies.

1. **Repair the pilot and validator — complete (2026-10-30).** Reviewed all
   20 Kagami annotations, corrected forbidden changes, separated assessable
   measurements and conclusions, and versioned the provisional author labels
   with reasons. Added checks and regression tests for proposition wording,
   criticality reasons, and per-proposition evidence relationships. All four
   packages and 80 pilot records pass; see the
   [verification record](eval/pilot-repair-verification.md) and
   [annotation corrections](eval/kagami-annotation-corrections.md). This is a
   structural pass and author review, not independent label validation.
2. **Shorten instructions and close behavior gaps — pending.** Keep essential
   safeguards in every standalone package, compact entrypoints and shared-rule
   validation, strengthen Kagami/Kotoba/Mamoru behaviors, and add 10 targeted
   inputs for a total of 90. Update guidance and the Mamoru expert-review sheet;
   preserve historical verification records.
3. **Make first use obvious and verify both hosts — pending.** Lead with
   functional labels and examples; document safe project-local copying. Verify
   discovery, invocation, local references, duplicates, and offline operation on
   Codex and Claude Code in disposable installations. Prepare the frozen Claude
   transfer packet; its verification stays pending until returned runs are
   recorded. Leave personal host configuration untouched.
4. **Run a bounded comparison and obtain human review — pending.** Freeze the
   specified 12 inputs, model/settings, and evidence/tool access. Compare exactly
   two conditions: the relevant skill and the fixed generic instruction in the
   [comparison guide](eval/README.md#4-run-the-planned-pilot-comparisons).
   Obtain expected human judgments before exposing author proposals. Run three
   repetitions per condition on Codex and Claude Code (144 outputs, 72 blinded
   pairs) with hidden-label and baseline isolation. No-skill and other baseline
   comparisons remain part of the broader evaluation after this bounded pilot;
   they are not counted here. Record human judgments, missing
   runs, critical failures, and exploratory limits; repetitions and role variants
   are not independent cases. Simplify skills without a clear advantage before
   expanding evaluation. Do not send or publish artifacts automatically.

## 6. Full release validation — pending

- [ ] Complete independent pilot annotation and instruction refinement before
  freezing the new 320-case test set plus 80 matched role/title variants.
- [ ] Add `eval/score.py` for independently annotated results, with tests for
  denominators, missing runs, uncertainty, and clustering. It must never infer
  truth or substitute model ratings for human labels.
- [ ] Run the optional compositions and all baseline comparisons, distinguishing
  frozen evidence from live retrieval. Record unavailable baselines.
- [ ] Run three repetitions per tested configuration; full behavior on Codex and
  Claude Code, installation and representative smoke tests on other targets.
- [ ] Verify exact host versions, discovery after initialization, invocation,
  reference loading, duplicate handling, and offline operation.
- [ ] Conduct the 60-reader study with independent comprehension/action scoring.
- [ ] Publish configuration-specific results, uncertainty, costs, failures, and
  limitations. Never publish private evaluation material.

A pilot-supported release may be called **experimental**. A validated release
requires the locked evaluation and reader-study gates; absence of data is not a
pass. No phase authorizes publishing, sending drafts, or changing host settings.
