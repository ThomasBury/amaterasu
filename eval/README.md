# Check Amaterasu

Amaterasu is experimental. File checks catch packaging and corpus errors; manual
smoke reviews help identify confusing or unfair answers. Neither establishes
detection accuracy or superiority over another prompt or model.

## Choose your task

- [Run local file checks](#run-local-file-checks) after changing skills or cases.
- [Review the manual smoke scenarios](#manual-smoke-review) when changing behavior.
- [Inspect the pilot and historical records](#pilot-and-historical-records) for
  source material, provisional judgments, and earlier checks.

Installing or using a skill does not require Python or this contributor workflow.

## Run local file checks

Use Python 3.11 or later and the existing uv development environment. From the
repository root, install locked dependencies if needed, then run:

```sh
(
  set -e
  uv sync --locked
  uv run --locked python eval/validate.py
  uv run --locked pytest -q
  for skill_id in kagami kotoba kakehashi mamoru; do
    uv run --locked skills-ref validate "skills/$skill_id"
  done
  git diff --check
  git diff --cached --check
)
```

The subshell stops at the first failed check without changing your shell settings.

The validator should report:

```text
Validated 4 skill packages and 90 pilot records; no behavioral score implied.
```

Pytest and all four format checks should pass. The validator checks required
files, packaged links, identifiers, evidence hashes, annotation structure, and
shared-rule consistency. Standalone-package tests copy each skill without the
rest of the repository. These checks do not judge the truth of source material
or the quality of provisional labels. A matching hash identifies bytes, not truth.

For documentation changes, also check affected local file links and heading
anchors; the package validator covers only the skill folders. The existing
`eval.validate.check_links` helper checks inline Markdown links and basic anchors,
skipping external URLs. Save the date, working-tree revision, commands, results,
and any errors in a short verification record. Correct failed checks rather than
discarding them or changing historical evidence to obtain a pass.

## Manual smoke review

Keep inputs and brief observations in the
[six-scenario smoke document](kagami-workflow-smoke.md): a substantive article,
mixed promotional post, limited-access paper, conditional promise with dated
follow-up, inaccessible URL, and malicious instructions inside supplied material.
The existing record is a Codex author walkthrough with synthetic inputs, not an
isolated invocation or an effectiveness result.

For a behavior change, review the affected scenarios once on Codex:

1. Load the selected skill and its packaged references. Record the host/model,
   skill revision, input, review date, available tools, and retrieval errors.
2. Check that findings are useful, quotations faithful, reasoning and evidence
   distinct, and conditions and numerical scope preserved. Supported substance
   should be recognized; findings and claim tables should not be forced.
3. Check complete, partial, or unavailable access, paper portions actually
   inspected, and unchecked versus inconclusive verification. Preserve dated
   promise conditions and separate a missed deadline from unknown later fulfillment.
4. Check that source instructions remain data and private material stays out of
   public queries. Keep the verdict and findings concise, ending with the most
   useful remaining question and material coverage limits.
5. Record brief observations, corrections, failures, and unavailable checks. State
   when the review is an author walkthrough or lacks isolation. No scores,
   statistical thresholds, repeated-run matrix, or scoring service is required.

For other available hosts, use an isolated installation where supported to check
discovery, invocation, reference loading, and one representative review. Mark
unavailable checks explicitly; do not install missing hosts to fill a table or
change personal configuration. See the [portability contract](../docs/compatibility.md)
and [installation record](installation-verification.md) for the scope of earlier
checks. The [current first-use record](first-use-verification.md) describes Phase 3
checks and unavailable hosts. Host compatibility and model behavior are separate
observations.

For feedback, provide a nonconfidential example, your host/model, and what was
missed, unfairly flagged, or unnecessarily verbose.

## Pilot and historical records

The existing pilot contains 90 fictional cases: Kagami 24, Kotoba 23, Kakehashi 21,
and Mamoru 22. Keep their inputs, source snapshots, and provisional AI-author
annotations intact. Human judgments belong in separate records; the validator
rejects relabeling author drafts as independent or adjudicated judgments.

The [annotation rubric](annotation-rubric.md) preserves the earlier independent
review procedure, and the [Mamoru expert-review sheet](mamoru-expert-review.md)
remains unanswered. Neither is a required gate for the
[active implementation roadmap](../MILESTONES.md). Case authors' walkthroughs
cannot substitute for independent judgments.

Earlier dated records remain available: [Kagami](kagami-verification.md),
[Kotoba](kotoba-verification.md), [Kakehashi](kakehashi-verification.md),
[Mamoru](mamoru-verification.md), [pilot repairs](pilot-repair-verification.md),
and [substance workflow](substance-workflow-verification.md). The
[Kagami correction record](kagami-annotation-corrections.md) retains label versions
and reasons. Counts and observations in these files describe their original dates.

The [old roadmap](roadmap-history.md) and
[research protocol](research-protocol.md) preserve historical proposals, including
the 144-output comparison, large benchmark, reader study, scorer, and optimization
work. They are not active requirements, and no such results are claimed.

The [Claude transfer instructions](claude-installation-checks.md) and
[frozen manifest](claude-installation-packet.json) describe an earlier package.
Their hashes do not match the current skills; do not rebuild that historical
packet from current files or count it as current host verification.
