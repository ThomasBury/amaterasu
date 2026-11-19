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

With Git and uv installed, run this from the repository root.

```sh
sh eval/check.sh
```

The command uses Python 3.11 and `uv.lock` and stops at the first failed check.
It checks staged and unstaged whitespace locally. GitHub Actions runs the same
checks on pull requests and pushes to `main`, comparing committed whitespace
against the base-branch parent of the tested pull request merge or the previous
`main` tip.

The validator should report:

```text
Validated 4 skill packages and 90 pilot records; no behavioral score implied.
```

Pytest and all four format checks should pass. The validator checks required
files, packaged links, identifiers, evidence hashes, annotation structure, and
shared-rule consistency. Standalone-package tests copy each skill without the
rest of the repository. These checks do not judge the truth of source material
or the quality of provisional labels. A matching hash identifies bytes, not truth.

The command also checks local inline Markdown links and basic heading anchors in
repository documents. It skips external URLs. Record the date, revision, commands,
results, and any errors when verifying a milestone.

## Manual smoke review

Keep inputs and brief observations in the
[six-scenario smoke document](kagami-workflow-smoke.md): a substantive article,
mixed promotional post, limited-access paper, conditional promise with dated
follow-up, inaccessible URL, and malicious instructions inside supplied material.
The existing record is a Codex author walkthrough with synthetic inputs, not an
isolated invocation or an effectiveness result.

The dated [coverage-comparison addendum](kagami-workflow-smoke.md#coverage-comparison-addendum--2026-11-17)
records the optional comparison checks, including a bounded public discovery
walkthrough and transcript-only limits. Keep later observations separate from
the original six-scenario record.

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
checks. The [latest installation verification](phase-6-verification.md) records
the public GitHub routes, updates, and remaining runtime checks.

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

The Phase 7 [blinded packet](phase-7-review.md) stays frozen. Independent
reviewers record judgments in the [separate scorecard](phase-7-scorecard.md),
which adds reporting rules, a post-judgment blinding check, and the
condition-key commitment and reveal procedure.

Earlier dated records remain available: [Kagami](kagami-verification.md),
[Kotoba](kotoba-verification.md), [Kakehashi](kakehashi-verification.md),
[Mamoru](mamoru-verification.md), [pilot repairs](pilot-repair-verification.md),
and [substance workflow](substance-workflow-verification.md). The
[Kagami correction record](kagami-annotation-corrections.md) retains label versions
and reasons. Counts and observations in these files describe their original dates.

The [old roadmap](roadmap-history.md) and
[research protocol](research-protocol.md) preserve historical proposals, including
the 144-output comparison, large benchmark, reader study, scorer, and optimization
work. They are not active requirements, and no such results are claimed. The
[effectiveness protocol](effectiveness-protocol.md) is the active design for the
next study: fresh realistic cases, natural requests, tool-enabled Kagami runs,
and preregistration. The
[instruction consolidation proposal](instruction-consolidation-proposal.md) is
a draft gated on a fresh-session comparison; it is not installed.

The [Claude transfer instructions](claude-installation-checks.md) and
[frozen manifest](claude-installation-packet.json) describe an earlier package.
Their hashes do not match the current skills; do not rebuild that historical
packet from current files or count it as current host verification.
