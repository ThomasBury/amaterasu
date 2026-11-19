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

Phase 3 needed no separate OpenCode extension, Pi executable plugin, or GitHub
App. Contributor CI is tracked in Phase 6.

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

## Phase 5 — Fix search allocation and chronology

- [x] Inspect the reviewed item and supplied sources first. Reserve two of six
  searches for requested and permitted discovery, run it before corroboration,
  reuse inspected results, and release unused slots. Count every issued query.
  Keep the limits of three claims and two searches per claim. Without requested
  discovery, make all six slots available for corroboration.
- [x] Use **Overlap**. Describe repetition only for passages known to predate the
  reviewed item. Cite dates or uncertainties for later, undated, and ambiguously
  ordered matches. Scope **Added** to inspected sources and distinguish assertions
  from evidence.
- [x] Align the skill, reference, contract, and README. Run the search-budget and
  chronology regressions in fresh Codex sessions and record both in the smoke
  document. Inspect the query trace and chronology wording and citations. Label
  any controlled search used to exercise the ceiling.

Completed 2026-11-17. The
[Phase 5 verification record](eval/kagami-workflow-smoke.md#phase-5-regressions--2026-11-17)
documents fresh Codex runs for the search budget and chronology. Live and
controlled searches both stopped at six, and each chronology case matched the
available dates. Repository checks passed across four skills and 90 pilot cases.

## Phase 6 — Automate validation and verify installation

- [x] Add one fail-fast command and run it in GitHub Actions on pull requests and
  pushes to `main`. Use locked uv and Python 3.11 for pytest, package and corpus
  validation, all four `skills-ref` checks, and repository Markdown links and
  anchors. Check staged and unstaged whitespace locally and the committed change
  range in CI.
- [x] Pin pilot JSON and text fixtures to LF with `.gitattributes`. Use explicit
  UTF-8 for repository validation and test I/O, and Python UTF-8 mode for the
  pinned `skills-ref`. Test a fresh checkout with `core.autocrlf=true`, run the
  check from a forced ASCII locale, and verify byte-for-byte SHA-256 checks still
  reject altered fixtures.
- [x] Test GitHub installation and public updates in available disposable profiles.
  Use the shared plugin for Codex and Claude Code and standalone Kagami for
  OpenCode and Pi. Record install, discovery, invocation, reference loading, and
  update separately. Where supported, also advance a controlled Git source from
  `v0.2.0` to `v0.3.0` and check that installed files change. Record versions,
  commands, revisions, file changes, and outstanding checks. Fix instructions
  that fail on the tested versions.

Completed 2026-11-18. The [Phase 6 verification record](eval/phase-6-verification.md)
documents the Python 3.11 and forced ASCII checkout checks, the live installs
and updates, and the controlled v0.2.0 to v0.3.0 updates. Claude Code and Pi
runtime checks require the corresponding hosts. GitHub-hosted CI ran green on
2026-11-18 for [pull request #11](https://github.com/ThomasBury/amaterasu/actions/runs/44352543751)
and the [main push](https://github.com/ThomasBury/amaterasu/actions/runs/44356618740).

## Phase 7 — Compare all four skills with an ordinary prompt

- [x] Freeze eight prompts and source excerpts. Use the chronology regression and
  pilot `023` for Kagami, `003` and `013` for Kotoba, `001` and `017` for
  Kakehashi, and `001` and `012` for Mamoru. Generate one answer per condition in
  fresh sessions with the same model, settings, permissions, and task wording.
  Load the relevant skill in one condition and use a profile without Amaterasu
  skills for the baseline.
- [ ] Give an independent human reviewer the sources and randomly ordered pairs.
  Withhold condition labels and provisional annotations until judgments are
  recorded. Use the [separate scorecard](eval/phase-7-scorecard.md): record a
  winner, tie, or N/A with a reason per criterion (source fidelity, handling
  of missing evidence, and usefulness for the next decision). Record material
  errors separately for each answer. After judgments are submitted, run the
  post-judgment blinding check (guess, confidence, cue) and report guesses
  descriptively.
- [ ] Before scoring, transfer the condition key and nonce to an independent
  custodian against the published commitment. Reveal both after all judgments
  and blinding guesses are submitted, then verify the digest. Report case-level
  findings including ties, inapplicable criteria, examples, regressions,
  incomplete pairs, and specific wording worth revising. Keep per-skill
  summaries descriptive and scope conclusions to the eight cases and tested
  model. Pairs 03 and 07 are basic
  controls, not equivalence evidence.

Generated eight matched answer pairs on 2026-11-18. The
[Phase 7 verification record](eval/phase-7-verification.md) documents the runs
and SkillEvaluator checks. The [blinded packet](eval/phase-7-review.md) is ready
for independent review; its bytes stay frozen.

Integrity follow-up on 2026-11-19: added the
[separate scorecard](eval/phase-7-scorecard.md) with reporting rules and the
post-judgment blinding check, and published a nonce commitment to the condition
key (`0830130369a7c923d481463d88d3b9099edcaca1703ef23f0a583b47c3993cdd`).
Custodian transfer and independent judgments remain pending. See the
[follow-up verification record](eval/review-followup-verification.md).

## Phase 8 — Redesign the effectiveness study

Execute the [effectiveness protocol](eval/effectiveness-protocol.md). The 90
pilot micro-cases remain fixtures and regression sources, not the study
sample.

- [ ] Preregister before generating answers: freeze case selection, natural
  prompts, conditions, repeat counts, criteria, and the analysis plan. Publish
  digests for private inputs. Commit condition mappings with the
  nonce-and-custodian procedure.
- [ ] Build 12–20 fresh realistic cases with natural requests: ordinary work,
  clean documents deserving few or zero criticisms, and hard cases with buried
  qualifications or conflicting evidence. Keep cases selected for known
  baseline failures as a separate, labeled challenge set.
- [ ] Have independent reviewers record what matters per case before seeing
  outputs. Optionally adjudicate about ten pilot micro-cases; route Mamoru's
  expert sheet to a workplace-domain reviewer separately.
- [ ] Run the skill, an ordinary-prompt baseline, and a concise well-written
  baseline in fresh sessions with identical settings. Give all three conditions
  identical controlled fetch and search access in tool-enabled Kagami cases.
  Inspect traces for retrieval order, query counts, failed searches, and
  private identifiers in public queries.
- [ ] Score fidelity, missing-evidence handling, usefulness, material errors,
  and unnecessary length using the blinded form for each case and repeat.
  Report case-level results with ties and inapplicable criteria. Keep per-skill
  summaries descriptive until sample size and repeated runs support a
  reliable-benefit claim.
- [ ] Apply the decision rule in [docs/evidence.md](docs/evidence.md): simplify
  or retire a companion that repeatedly adds little while a shorter
  alternative preserves the safeguards. Two easy pairs per skill are
  insufficient for that decision.

## Phase 9 — Compare consolidated instructions before shipping

- [ ] Review the [consolidation proposal](eval/instruction-consolidation-proposal.md):
  remove genuinely duplicated detail where the skill reliably reads the
  canonical reference; keep privacy and tool-use rules visible before the
  first relevant action.
- [ ] Compare the shorter wording against the current skill in fresh sessions
  on the smoke scenarios, Phase 5 regressions, tool-enabled cases, a clean
  findings-only review with simulated external actions, and a number-heavy
  claim. Record the comparison in a dated verification record. Ship only if
  safeguards and usefulness are preserved.

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
