# Make Amaterasu useful from the first review

Kagami is the main experience: supply a URL or text and receive a concise, fair
assessment of empty language, unsupported claims, misleading reasoning, and
promises. Keep all four skill names; Kotoba, Kakehashi, and Mamoru are optional
companions. Useful findings, traceable evidence, honest access limits, and user
feedback guide further work.

Implement one independently reviewable phase per session and stop after its
verification record. Preserve branding, dependencies, the 90 pilot cases,
provisional annotations, tests, and dated records. Publishing and personal host
configuration changes are outside this work.

## Phase 1 — Improve Kagami's everyday workflow

- [x] Accept URLs, pasted posts, articles, and papers. Retrieve supplied material
  with available host tools before searching for corroborating evidence.
- [x] Report complete, partial, or unavailable access. Request text or an export
  for blocked pages; state which paper portions were inspected and continue
  with accessible content without inventing the rest.
- [x] Research up to three consequential unresolved claims, initially using at
  most two targeted searches per claim. Preserve privacy and distinguish unchecked
  claims from attempted but inconclusive verification.
- [x] Check actor, promised outcome, deadline, conditions, and dated fulfillment
  evidence inside Kagami, reusing Mamoru's principles without invoking it.
- [x] Default to a short verdict and up to five material findings, each with a
  quotation, specific problem or supported conclusion, and relevant evidence.
  End with the most useful resolving question and material coverage limits.
- [x] Make claim tables optional, recognize substantive supported material, and
  distinguish unsupported, false, and intentionally deceptive claims.
- [x] Update contracts and packaged references together, retaining attribution,
  numerical checks, source-instruction protection, and no aggregate scores.
- [x] Complete file checks and the six-scenario Codex smoke review; record
  observations and limitations in the verification record.

Completed 2026-11-04. See the [six-scenario review and check record](eval/kagami-workflow-smoke.md):
92 tests, four packages, 90 pilot records, four format checks, and local links
pass. The manual Codex author walkthrough is not an isolated invocation or an
effectiveness result; live corroboration and actual paper retrieval were not tested.

## Phase 2 — Shorten instructions and simplify quality checks

- [x] Embed a compact shared core in every standalone skill. Keep detailed
  evidence-status definitions in Kagami's references and task-specific boundaries
  in each companion. Preserve the shared-rule consistency check and update tests.
- [x] Rewrite `eval/README.md` around existing file checks and a short manual
  smoke checklist. Archive the extensive research protocol; its comparison,
  benchmark, reader-study, scorer, and optimization proposals are optional history.
- [x] Preserve all 90 cases, provisional annotations, tests, and dated records;
  repair affected links and mark old frozen installation packets as historical.
- [x] Retain a brief experimental-use statement. Describe qualitative observations
  without claiming measured accuracy or superiority. Add no policy framework,
  generated files, runtime dependencies, or cosmetic validator cleanup.

Completed 2026-11-04. See the [Phase 2 verification record](eval/compact-instructions-verification.md):
the shared core is 244 words per skill, with detailed definitions retained inside
Kagami; 95 tests, four packages, 90 records, four format checks, and local links
pass. Historical evidence is preserved. No new host behavior or accuracy result
is claimed.

## Phase 3 — Make installation and first use obvious

- [x] Lead `README.md` with purpose, a short input/output example, installation,
  and the first Kagami review. Place companions, methodology, and contributor
  material below the main usage path.
- [x] Document concise Claude Code and Codex plugin routes, and OpenCode and Pi
  skill routes: project/user scope, invocation, updates, and duplicate avoidance.
  Keep the shared four-skill plugin; recommend selecting only Kagami with Skills CLI.
- [x] Explain host-dependent source access and usable pasted text without browsing.
  Remove the stale unpublished-metadata caveat and separate documented routes
  from routes actually tested.
- [x] Verify available hosts with isolated installations where supported; record
  discovery, invocation, reference loading, and one representative review. Mark
  unavailable checks explicitly; do not install missing hosts to fill a table.
- [x] Ask for a nonconfidential example, host/model, and what was missed, unfairly
  flagged, or unnecessarily verbose.
- [x] After the changes are complete, update the plugin description and version
  to `0.2.0`, preserving skill identifiers and invocation names.

Completed 2026-11-05. See the [installation and first-use record](eval/first-use-verification.md):
95 tests, four packages, 90 pilot records, four format checks, local Markdown
links, and the 0.2.0 local plugin catalog pass. Temporary Kagami copies for all
four targets match source. OpenCode loads Kagami and both references, but the
completed restricted review had response errors and the final provider call
failed; no full behavior pass is claimed. Isolated native Codex installation and
Claude Code/Pi runtime checks were unavailable and are explicitly recorded.
No publishing or personal host configuration changes were performed. Stop here
for this session.

No separate OpenCode extension, Pi executable plugin, GitHub App, or GitHub Action
is needed.

## Phase 4 — Optional comparison with existing coverage

- [x] Add an opt-in comparison using supplied sources first, with requested
  discovery of similar articles, posts, papers, or videos.
- [x] Limit discovery to two searches within the shared six-search allowance;
  retain privacy, access, attribution, and claim-checking limits.
- [x] Report Repeated, Added, and Unchecked briefly, distinguishing assertions
  from evidence and limiting additions to the inspected comparison set.
- [x] Align packaged instructions, contract, and a README example; verify local
  files and record a focused author walkthrough without changing pilot records.

Completed 2026-11-17. See the
[coverage-comparison addendum](eval/kagami-workflow-smoke.md#coverage-comparison-addendum--2026-11-17)
for commands, responses, and limits. The walkthrough includes two live discovery
queries and inspection of public page text; video access is limited to page text
and a synthetic transcript case. No independent invocation or accuracy result
is claimed. Stop here for this phase.

## Verification and limits

For each phase, run the existing pytest suite, corpus/package validator,
`skills-ref` format checks, relevant local Markdown link checks, and
`git diff --check`. Use the existing locked development environment.

Keep six manual smoke scenarios in one document: a substantive article, a mixed
promotional post, a paper with limited access, a conditional promise with dated
follow-up evidence, an inaccessible URL, and malicious instructions inside supplied
material. Review once on Codex for useful findings, faithful quotations, restraint,
access limits, and concise output. Record brief observations and failures; no
scoring service, statistical thresholds, or repeated-run matrix is required.

Amaterasu remains experimental. File checks and smoke reviews establish basic
usability, not detection accuracy or comparative benefit. Results depend on the
host model and source access.

The [previous roadmap](eval/roadmap-history.md) preserves completed milestones and
historical research proposals. Its 144-output comparison, large benchmark, reader
study, scorer, and optimization work are not active requirements. The detailed
[research protocol](eval/research-protocol.md) is archived; the
[evaluation guide](eval/README.md) describes current practical checks.
Independent annotations and Mamoru's workplace-expert review remain uncompleted
historical work; no result is implied or required for the next implementation phase.
