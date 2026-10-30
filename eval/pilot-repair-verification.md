# Pilot and validator repair — 2026-10-30

## Scope and versions

This completes improvement Phase 1 only. The four standalone skill packages,
80 original inputs, supplied evidence, and manifests retain their bytes. Existing
uncommitted documentation, validator, test, and branding work was preserved.
The working-tree baseline was Git revision
`ea8fa769547b8405a83054de506fa12e04fb2385` plus those existing edits; this record
does not attribute earlier edits to this phase.

All 20 Kagami annotations were reviewed against the located input, permitted
evidence, and rubric. They now use `author-v2` and rubric `pilot-2026-10-30`,
while retaining provisional AI-author draft status. The
[correction record](kagami-annotation-corrections.md) gives case-specific reasons,
hashes of the previous annotation bytes, and the Git revision retaining them.
The [historical Kagami record](kagami-verification.md) is unchanged; its results
describe the earlier version.

## Annotation review

Every `forbidden_changes` item now describes an actual failure. In particular,
requesting equivalence evidence (006), exposing partial coverage (013), and
preserving the conditional Friday commitment (017) are acceptable behaviors.
Their reversals or unsupported conclusions are forbidden instead.

| Cases | Boundary checked |
| --- | --- |
| 001–003 | Measurements/counts and numerical interpretations have separate propositions and evidence judgments. Zero-to-four is supported; 400% is contradicted. |
| 004, 007, 009 | Keep benchmark conditions, the explained FIFO definition, and forecast attribution/range attached. No universal performance or realized forecast is established. |
| 005–006 | Separate the observed decline or reported p-value from the causal or equivalence conclusion. The conclusions remain unresolved, not proven false. |
| 008, 012–013 | Indeterminate meaning, unavailable audit proof, and incomplete site coverage remain explicit gaps. Separate the embedded zero-incident assertion from the claim of audit proof. |
| 010–011 | Distinguish roadmap from shipped functionality, and the report's wording from actual uptime. Quoted malicious instructions grant no authority. |
| 014–015 | Preserve conflicting laboratories' results; distinguish source independence from the reported adoption percentage. Repetition does not verify the underlying survey. |
| 016–020 | Retain preference, the conditional commitment, completion timing versus three check outcomes, satire context, and an unexamined capability. No style-based accusation or invented verification follows. |

All propositions now have case-specific criticality reasons. Exact source spans
remain intact, with attribution and conditions in preservation notes where
needed. Narrowed/retyped propositions must be read with their annotation version;
counts from different versions must not be pooled silently. This is an author
review, not independent human agreement or adjudication.

## Regression evidence

Before changing the validator, the 15 new rejection tests were run against its
starting working-tree version:

```sh
uv run --locked pytest -q tests/test_eval.py -k 'reject_blank_or_nonstring or critical_proposition_requires or every_proposition_requires' --tb=line
```

All 15 failed: empty/space-only wording was accepted, nonstring wording raised
`TypeError`, newline-only wording reached the source-match check, invalid critical
reasons were accepted, and a proposition with no relationship was accepted when
another proposition still had one. The repaired validator rejects these with
`ValueError` at the relevant boundary. Four positive tests retain explicit
insufficient-evidence, not-checked, and inapplicable relationships and allow an
absent reason value for a noncritical proposition. The CLI is unchanged.

## Final checks

Environment: uv 0.12.15, CPython 3.15.0, pytest 9.2.0, skills-ref 0.1.0 from the
existing lockfile (revision `69ef37e9424c0a7ea9dd2293b559e43ec8176379`).

```sh
uv run --locked python eval/validate.py
uv run --locked pytest -q
uv run --locked skills-ref validate skills/kagami
uv run --locked skills-ref validate skills/kotoba
uv run --locked skills-ref validate skills/kakehashi
uv run --locked skills-ref validate skills/mamoru
git diff --check
```

Results: four packages and 80 records validate; all 86 tests pass; all four
official format checks pass. The suite copies each standalone folder into a
temporary directory, loads its local references without repository documents,
and confirms that removing a required reference fails. Local links and anchors
pass across all 28 repository Markdown files; whitespace checks also pass.
Git comparisons confirm unchanged
frozen inputs, evidence, manifests, other skill annotations, and skill packages;
previous annotation hashes match the recorded Git revision.

Sandbox startup repeatedly failed with
`bwrap: loopback: Failed RTM_NEWADDR: Operation not permitted`; affected local
reads and checks were rerun successfully through the approved execution path.

## Limits and next phase

A structural pass does not establish semantic truth, sufficient evidence,
independent label quality, host behavior, or usefulness. No skill behavior,
isolated Codex/Claude run, human assessment, or comparison was performed here.
Those remain later improvement phases and full-release requirements. Phase 2
is pending; no personal host settings, dependencies, or publishing changed.

## PR review follow-up — 2026-10-30

Codex found no issues in `f4928e2`. CodeRabbit identified two corrections:

- Source relationships in cases 014 and 015 included information from another
  evidence artifact. Each now describes only its cited source, with matching
  per-source statuses; the combined conclusion stays in the annotation-level
  answer. These two annotations advance to `author-v3`; their v2 hashes and
  recovery revision are appended to the correction record.
- The milestone summary did not explicitly distinguish the bounded two-condition
  comparison from the broader baseline evaluation. The milestone and evaluation
  guide now name the skill and fixed generic instruction, retain 144 outputs and
  72 pairs, and defer the other comparisons to the broader evaluation afterwards.

The supplied artifacts were reread to check attribution. The locked validator,
86-test suite, local links/anchors, and whitespace checks pass again. Inputs,
evidence, manifests, and skill packages remain unchanged. This follow-up adds no
behavioral or independent-human validation result.
