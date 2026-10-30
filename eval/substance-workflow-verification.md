# Substance workflow verification — 2026-10-30

## Scope

This phase makes empty-meaning analysis explicit and adds ten targeted pilot
cases. It does not perform host discovery, retrieve LinkedIn pages, run an
isolated assistant comparison, or establish effectiveness. The next phases remain
real-input/host checks and bounded behavioral comparison.

## Changes

- Kagami now distinguishes clear propositions, vague but repairable wording, and
  no determinate proposition before evidence assessment. Substance findings stay
  separate from factual verdicts; no score or intent inference was introduced.
- Kotoba removes empty abstraction only when doing so does not require invented
  actions, mechanisms, results, metrics, owners, or dates. Missing substance stays
  visible in or beside the draft.
- Kakehashi explicitly refuses to recover absent meaning through a plausible
  plain-English explanation.
- Mamoru preserves chronology for later criteria changes and requests repeated
  after refusal without inferring fake urgency, manipulation, or a broader pattern.
- The user-selected Kagami → Kakehashi composition preserves original wording,
  substance classifications, evidence statuses, and unresolved questions. No skill
  invokes another automatically.
- The pilot grows from 80 to 90 original synthetic cases: Kagami 24, Kotoba 23,
  Kakehashi 21, and Mamoru 22. All labels remain provisional AI-author drafts.
  Kagami annotations require explicit substance labels; no-determinate passages
  use `indeterminate` and `inapplicable`, separately from unsupported clear claims.
  The Mamoru expert-review sheet includes the two new cases and remains pending.

No runtime dependency, ingestion service, buzzword blacklist, aggregate score,
or automatic orchestration was added.

## New-case author walkthrough

| Cases | Expected boundary checked against instructions and provisional keys |
| --- | --- |
| Kagami 021–022 | Empty LinkedIn/job wording is quoted and clarified while concrete results and payroll duties remain distinct and unchecked. |
| Kagami 023 | “Our AI doubles engineering productivity” is clear but unsupported, not semantically empty, contradicted, or proof of a useless product. |
| Kagami 024 | An inaccessible post produces a request for pasted text or an export and explicit zero coverage, never guessed contents. |
| Kotoba 021 | Empty abstraction is omitted while team size, median response metric, 18-to-6-hour change, and January–March scope survive without a year or cause. |
| Kotoba 022 | A job-application draft retains the engineering-leadership role, 24 migrated services, and visible date/outcome gaps without invented success or business impact. |
| Kotoba 023 | AI hype becomes an internal 20-report prototype statement with both accuracy and customer-outcome limitations beside the draft. |
| Kakehashi 021 | Plain English discloses the missing action and result instead of inventing a program or benefit; all three answer keys reject fabricated meaning. |
| Mamoru 021 | Completion on 14 June meets the explicit 30 June 2026 deadline; the later project requirement retains its chronology, recommendation remains distinct from final promotion, and intent remains unknown. |
| Mamoru 022 | Renewed pressure after an approval-based refusal is described exactly without fabricating urgency, diagnosing bullying, or authorizing transfer. |

These are author-created calibration examples, not observed model outputs or
independent labels. Existing cases continue to cover meaningful jargon, honest
forecasts, concrete benchmarks, non-native phrasing, satire, firm feedback, and
other false-positive controls.

## Reproduction and results

Run from the repository root:

```sh
uv run --locked python eval/validate.py
uv run --locked pytest -q
for skill in kagami kotoba kakehashi mamoru; do
  uv run --locked skills-ref validate "skills/$skill"
done
git diff --check
```

Results on 2026-10-30:

- Validator: four standalone packages and 90 pilot records pass.
- Pytest: 91 tests pass, including standalone reference loading, shared-rule
  consistency, substance/claim-type drift, no-determinate evidence-status drift,
  provenance, evidence hashes, and mutation checks.
- Official `skills-ref` validation: all four packages pass.
- `git diff --check`: no whitespace errors.

## Remaining limits

File validation and this author walkthrough do not test instruction obedience,
source retrieval, reader comprehension, or comparative benefit. No real LinkedIn
post, job application, speech, PDF, or slide deck was processed in this phase.
No independent human annotation, Mamoru expert assessment, host behavioral run,
baseline comparison, or release gate is claimed. Historical verification records
retain the counts from their original phases.
