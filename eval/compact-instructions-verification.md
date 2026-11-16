# Compact instructions and quality checks — 2026-11-04

Phase 2 of the [active roadmap](../MILESTONES.md), layered on the existing Phase 1
working-tree changes. This phase changes instructions and contributor guidance,
with one expanded regression test. It adds no runtime dependency, policy framework,
generated package files, scorer, or validator behavior.

## Changes

- Replaced the repeated 653-word shared block with a 244-word core in all four
  skills and the contract. The existing shared-rule consistency check is unchanged.
  The core retains claim types, meaning/evidence/reasoning separation, preservation,
  provenance, unresolved versus unchecked status, source-instruction protection,
  privacy, access limits, and limits on scores and external actions.
- Moved the detailed evidence-status table, claim definition, consequentiality,
  source attribution, and verification limits into Kagami's packaged
  [evidence reference](../skills/kagami/references/evidence-and-arguments.md).
  Removed a duplicate provenance paragraph there. Companion workflows and task
  boundaries remain local; none depends on Kagami's files.
- Expanded the existing drift test from Kagami to all four skills. Removing the
  source-instruction safeguard is rejected for each package. No validator cleanup
  or new test framework was introduced.
- Replaced the 547-line evaluation guide with a 114-line guide to existing file
  checks, a short smoke checklist, the pilot, and historical records. The
  [research protocol](research-protocol.md) preserves the previous body verbatim,
  apart from its replacement title and archive notice. The 144-output comparison,
  benchmark, reader study, scorer, and optimization proposals are not active work.
- Repaired links to moved sections and aligned current host-check guidance with
  practical smoke reviews. The frozen Claude packet is explicitly historical;
  its manifest hashes and earlier verification results were not rewritten.
- Kept experimental-use statements and qualified companion evidence summaries.
  No measured accuracy, superiority, or equivalence of model behavior is claimed.

## Verification

Commands used the existing installed development environment:

```sh
.venv/bin/python -m pytest -q
.venv/bin/python eval/validate.py
for skill_id in kagami kotoba kakehashi mamoru; do
  .venv/bin/skills-ref validate "skills/$skill_id"
done
git diff --check
```

Results on 2026-11-04:

- **95 pytest cases passed**, including all four standalone-package checks and
  all four shared-core drift cases. The previous 92 cases were retained; the
  expanded parameterization adds three cases.
- Corpus/package validation passed for **four packages and 90 pilot records**.
- All four official `skills-ref` format checks passed.
- Local Markdown links and heading anchors passed for **35 files**, using the
  existing `check_links` helper on a temporary copy excluding `.git`, `.venv`,
  and cache directories. External URLs were not rechecked.
- `git diff --check` passed.

Byte comparisons against a temporary snapshot taken before Phase 2 confirmed
that all pilot inputs, evidence, provisional annotations, dated verification
records, the Phase 1 smoke document, annotation-correction history, frozen packet
manifest, validator, dependencies/lockfile, plugin metadata, licenses/notices,
and branding assets were preserved. The old evidence-definition block appears
unchanged in Kagami's reference. The archived protocol body also matches its
pre-phase source exactly. Word counts use whitespace splitting; line counts
include blank lines.

The first documentation link check found a stale rubric link to the contract's
removed evidence-definition heading. It now points to the packaged Kagami
reference; the subsequent complete local-link check passed. No test, corpus,
or format failure was hidden or removed.

## Manual review and limits

Reviewed the compact core against the boundaries illustrated by the existing
[six-scenario Codex author walkthrough](kagami-workflow-smoke.md): positive
assessment, unsupported versus false claims, paper coverage, promise chronology,
unavailable content, and malicious source instructions. The inputs, responses,
observations, and corrections in that dated record are unchanged. They were not
rerun or relabeled as results for the shorter instructions.

This phase does not establish that models obey the shorter instructions equally
well. No new model output, isolated host invocation, live paper retrieval,
corroboration search, independent label review, or effectiveness comparison was
performed. Existing qualitative observations remain author observations.

Phase 3 remains pending: installation and first-use documentation, available-host
checks, and the final plugin description/version update. No missing host was
installed, personal configuration changed, or material published.
