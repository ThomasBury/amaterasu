# How to evaluate Amaterasu

Use this guide to review proposed interpretations, check the repository files,
or test how an assistant behaves with a skill.

All four skills have 20 fictional practice cases each, for 80 cases in total.
Their proposed answers were prepared by AI and still need independent human
judgment. Mamoru's [workplace-expert review](mamoru-expert-review.md) is pending.
No independent assistant comparisons or reader-study results are available yet.

The [reviewer instructions](annotation-rubric.md) explain how to judge cases and
answers. For the checks already performed, see the [Kagami](kagami-verification.md),
[Kotoba](kotoba-verification.md), [Kakehashi](kakehashi-verification.md), and
[Mamoru](mamoru-verification.md) records. Those file checks and author walkthroughs
do not establish whether the skills improve reasoning or understanding.

## Choose your task

| I want to... | Start here | What I will produce |
| --- | --- | --- |
| Review Mamoru's proposed interpretations | [Review Mamoru](#review-mamoru) | Decisions on 20 fictional cases, with corrections and reasons |
| Check that the files and packages are consistent | [Run local file checks](#run-local-file-checks) | Command results and any errors |
| Test whether a skill helps an assistant | [Evaluate skill behavior](#evaluate-skill-behavior) | Recorded assistant answers and separate human assessments |

You can do the expert review and local checks today. Behavior testing is a
manual process: this repository has no automated evaluation runner or scorer.
Host-specific installation and invocation instructions still need testing.
A complete release evaluation also needs new test cases and a reader study.

### Words used in this guide

- A **case** is one test example: a task, source text, context, and any evidence.
  The **pilot** is the set of practice cases used to improve the instructions.
- An **annotation** is a recorded human judgment about a case or an answer.
  The **rubric** is the set of rules reviewers use to make those judgments.
- A **claim** or **proposition** is one statement whose meaning or support can
  be judged separately. Keep a promise's conditions attached to it.
- A **baseline** is a comparison setup, such as the same assistant without the
  skill. A **condition** is one setup being compared.
- A **configuration** identifies the host application, model, settings, and
  tools. A **repetition** is a fresh run of the same case under that setup.
- **Adjudication** means a third human reviews disagreements and records a
  reasoned decision. Unresolved questions can remain unresolved.
- **Freezing** means fixing and versioning the material and rules before testing.
  A **gate** is a requirement that must be met before claiming a validated release.

## Review Mamoru

This path is for the workplace expert reviewing the proposed interpretations.
You need workplace experience and the [20-case review sheet](mamoru-expert-review.md).
You can complete it without Python, terminal commands, or an AI assistant.

1. Open the sheet and read its instructions.
2. State your relevant experience and the limits of your expertise.
3. Read each scenario, then assess its proposed label, interpretation limits,
   acceptable response, and rejected response.
4. Record **accept**, **revise**, or **unsure** for each case. Give the case
   number and a reason for each correction or unresolved concern.
5. Send your assessment to the project maintainer, for example in the review
   conversation, using the sheet's reply template. Exclude confidential examples.

You are done when all 20 cases have a decision or an explicit unresolved concern
and your assessment has been submitted. The maintainer records your review
separately, preserves disagreements, and addresses corrections. Unresolved
expert concerns must be addressed before milestone 5 can be closed. Reading
this sheet does not count as independent labeling of those same cases before
seeing the author's proposals.

## Run local file checks

This path is for a contributor checking the repository. You need a local checkout,
Python 3.11 or later, and uv already installed. The first dependency download
needs network access. Run these commands in the repository root, the folder
containing `pyproject.toml`:

```sh
uv sync --locked
uv run --locked python eval/validate.py
uv run --locked pytest -q
uv run --locked skills-ref validate skills/kagami
uv run --locked skills-ref validate skills/kotoba
uv run --locked skills-ref validate skills/kakehashi
uv run --locked skills-ref validate skills/mamoru
```

1. Run `uv sync --locked` to install the recorded development dependencies.
   If it fails, resolve the installation or network error before continuing.
2. Run the validator. With the current pilot it should report:

   ```text
   Validated 4 skill packages and 80 pilot records; no behavioral score implied.
   ```

3. Run pytest. Its summary should say that all tests passed. The exact test
   count can change as the project develops.
4. Run each `skills-ref` command. Each should report `Valid skill:` followed by
   the corresponding folder.
5. Save the date, repository revision, commands, exit results, and any errors in
   your check record. If a check fails, save the complete error and inspect the
   named file. Correct the underlying problem before repeating the check;
   do not remove a check or rewrite evidence merely to obtain a pass.

You are done when every command succeeds and you have saved the results.
These commands check file structure, source hashes, references, and validation
code. They do not run the skills against an assistant or assess their usefulness.
A hash identifies exact file bytes; it does not prove the contents are true.
The link check handles local inline Markdown links and basic heading anchors.

The validator expects the existing provisional AI-author annotations. Keep human
reviews in separate records; changing author labels to `independent` or
`adjudicated` will make this validator reject them.

Every proposition needs nonblank string wording and an explicit evidence
relationship; critical propositions also need a nonblank reason. Unresolved or
inapplicable relationships are valid and do not require a factual verdict.
The [Kagami correction record](kagami-annotation-corrections.md) versions the
2026-10-30 author-label repairs, with reasons and recoverable original labels.
The [repair verification record](pilot-repair-verification.md) records the
structural checks. Neither record establishes semantic truth or effectiveness.

## Evaluate skill behavior

This path is for an evaluation coordinator and human reviewers. The coordinator
organizes cases, runs, and records. Two humans judge cases independently; a third
resolves disagreements. Choose reviewers with the relevant domain experience.
Use the [annotation instructions](annotation-rubric.md) for their work.

### 1. Prepare expected judgments

Give each reviewer only the selected inputs, context, and permitted evidence.
For the pilot, these come from `pilot/<skill>/inputs/`, `evidence.json`, and the
referenced files in `evidence/`. The coordinator selects the evidence for each
case. Do not give reviewers author annotations or other reviewers' answers
before they submit their own expected judgments.

Each reviewer records what the source says, what the evidence supports, which
details must survive, and what a suitable response could say. Save human reviews
in a private folder outside the repository and outside the tested assistant's
access. Keep `pilot/<skill>/annotations/` unchanged; it contains AI-author drafts.
Have the third reviewer resolve disagreements with reasons while retaining both
originals. Record unresolved items explicitly. Finish this stage before showing
reviewers any assistant answers to assess.

### 2. Prepare a workspace that hides the answers

Use a separate workspace to which the tested assistant has access. Include only
the selected case input, its permitted evidence, and, in the skill condition,
the complete selected skill folder with its local references. Retain evidence
identifiers and source locations so the assistant can cite them.

Keep the repository checkout, manifest, annotations, answer keys, expert review
sheet, and this guide outside the assistant's accessible files and conversation.
Verify its file permissions and tools actually prevent access; asking it not to
read nearby answers is insufficient. A new chat alone does not restrict tools.
For a baseline run, also ensure Amaterasu instructions are absent from loaded
skills, global instructions, and earlier conversation.

For supplied-evidence tests, disable web access. If the host cannot enforce the
required isolation or tool restrictions, stop and record that setup as unavailable.
Use fictional public pilot material for practice. A cloud-backed host may send
prompts to its provider even when browsing is disabled.

### 3. Rehearse one pilot case

This walkthrough explains the procedure; it is not a recorded evaluation result.
Use `pilot/mamoru/inputs/pilot-mamoru-001.json`, its referenced evidence, and the
complete `skills/mamoru/` folder copied from the repository. Inspect the input's
`task`, located `input`, `context`, and `research_scope` fields. Give the assistant
those fields and the permitted evidence, then use this instruction in a fresh,
isolated session:

```text
Read the supplied Mamoru SKILL.md and its linked reference.
Complete the task in the supplied case using its original text and context.
Use only the supplied evidence. Leave missing information visible.
Do not search, send messages, file anything, or change external records.
```

Save the exact prompt, input and evidence versions, complete answer, and tool
activity. Use this record template for the rehearsal and add the detailed
[run fields](#comparisons-and-run-records) when preparing comparisons:

```text
Case ID:
Condition and repetition:
Host/model versions, settings, tools, and skill revision:
Input and evidence hashes:
Exact prompt and saved answer location:
Tool activity and errors:
Outcome: complete / error / timeout
Tokens, elapsed time, and cost (or unavailable, with reason):
```

Reviewers then compare the answer with their previously recorded expectations.
For this instructional example, a promotion recommendation conditional on targets
must remain distinct from the panel's approval. A claim that promotion was
guaranteed would change the source meaning. This example is visible to readers
of this guide and must never become a new unseen test case.

An example review note could be:

```text
Case: pilot-mamoru-001
Output quote: [paste the exact relevant words]
Decision: [meets expectations / needs correction / unresolved]
Reason and source location: [explain using L1 or L2]
Required correction, if any: [state it]
Reviewer ID, expertise, date, and rubric version: [record these]
```

The rehearsal is complete when you have a saved answer, tool record, and human
assessment. One rehearsal does not establish effectiveness or meet release gates.

### 4. Run the planned pilot comparisons

Before running comparisons, record the exact configurations, prompts, conditions,
case list, evidence versions, and settings. Use the same model and tools for the
no-skill, short generic instruction, and skill conditions. Include the applicable
external baselines and original-text comparisons listed in
[comparisons and run records](#comparisons-and-run-records). Record unavailable
comparisons with reasons. Test explicitly selected skill combinations separately.

Run every selected case three times per configuration and condition, including
role/title variants when present. Start each repetition with a fresh context and
the correct isolated workspace. Save complete answers and tool traces, including
errors and timeouts. Keep tests using fixed evidence separate from tests using
live search. Verify host setup against the
[host checks](../docs/compatibility.md#required-host-checks); installation and
invocation instructions for specific versions remain pending.

Give output reviewers answers in random order with setup names hidden. They
assess each answer independently against the agreed expectations; a third human
resolves disagreements. Use findings to refine the pilot instructions and rubric,
record reasons for changes, and reassess affected cases. Finish when every
planned run and judgment is recorded, or explicitly marked missing with a reason.

### 5. Prepare the new locked evaluation

After pilot refinement, create the new 320 cases plus 80 matched role/title
variants described in [stages and corpus](#stages-and-corpus). Keep related cases
together and exclude pilot material. Obtain independent expected judgments.
Before running the locked tests, freeze inputs, evidence, labels, questions,
prompts, settings, scoring rules, and the analysis plan.

The coordinator must obtain statistical advice to settle how uncertainty will
be calculated for related cases and how the reader study will be analyzed.
Record the method, random seed where applicable, exclusions, and missing-data
rules before freezing. Stop here if those decisions or independent labels are
missing. Keep expected labels inaccessible to the tested assistant.

### 6. Run, assess, and calculate results

Repeat the recorded comparison procedure on the locked material. Preserve human
judgments, original disagreements, full outputs, and failed runs. Calculate the
[defined metrics](#metric-definitions-and-uncertainty) against the final human
labels, with counts, missing results, and uncertainty for each tested setup.

`score.py` is planned and does not exist yet. A maintainer must implement and
verify the calculations against independent labels before claiming automated
scoring. A model's rating of its own answer cannot substitute for human labels.
Missing required runs, unresolved judgments, and undefined rates leave affected
release requirements **not evaluated**. Do not average away a failing repetition.

### 7. Conduct the reader study and report the outcome

Follow the [reader study](#reader-study) procedure with 60 independent readers.
Before recruiting, obtain statistical review and fix the passages, questions,
answers, assignments, and analysis. Readers answer understanding and action
questions; scorers work without knowing which setup produced each passage.
Do not replace reader responses with model-generated answers.

Compare the completed benchmark and reader-study results with the
[release requirements](#proposed-validated-release-gates). Report counts,
uncertainty, disagreements, costs, unavailable comparisons, failures, and limits
for each configuration. Keep private material out of public reports. Preparing
a report does not authorize publishing it.

The full evaluation is complete only when its planned records and analyses are
accounted for. A completed evaluation can fail the release requirements or remain
inconclusive. Pending work cannot be recorded as a pass.

## Detailed evaluation rules

The sections below specify sampling, comparisons, calculations, and release
requirements. Use them when preparing the full evaluation; the numbered paths
above explain the order of work.

## Stages and corpus

| Stage | Kagami | Mamoru | Kotoba | Kakehashi | Total |
| --- | --- | --- | --- | --- | --- |
| Pilot, used to refine instructions and annotation | 20 | 20 | 20 | 20 | 80 |
| New locked evaluation cases | 100 | 100 | 60 | 60 | 320 |

The locked Kagami and Mamoru sets each contain **60 independent benign cases**.
The remaining cases must cover supported problems and insufficient evidence;
fix their distribution before locking. Add **80 matched role/title variants**
drawn from the detection cases, for 400 locked inputs in total. Variants are
dependent observations, not 80 additional independent cases. Keep each variant
with its original in splits, analysis, and uncertainty estimates.

Use original synthetic cases and permissioned or redistributable real cases.
Record source dates and provenance. Split by original document and scenario
family; close paraphrases, templates, and role variants stay in the same split.
Pilot material must not reappear in the locked set. Select benign cases from
independent documents/scenarios if using the exact 60-case binomial bound below.
Otherwise report the dependence and do not claim that bound from 60 rows.

Before locking, freeze input bytes, evidence, hashes, labels, questions, answer
keys, scoring rules, comparison settings, and the analysis plan. Freeze new cases
only after pilot-driven instruction changes. After inspecting locked results,
do not relabel difficult cases or lower gates to obtain a pass. Corrections need
a versioned rationale and a clearly identified new evaluation; exposed cases
cannot become unseen test data again.

## Required controls

| Control | Expected behavior |
| --- | --- |
| Correct specialist terminology with a technical explanation | Preserve its meaning; no emptiness accusation. |
| Impressive wording with no recoverable proposition | Identify what cannot be determined and seek clarification. |
| “2× faster” supported by one specified benchmark | Preserve that result's workload and conditions; do not generalize without evidence. |
| Before–after improvement presented as causal proof | Distinguish the measured change from the unsupported causal inference. |
| Nonsignificant result presented as equivalence | Identify the inference error without concluding an effect exists. |
| Precise prediction with honest uncertainty | Preserve the uncertainty; do not label it evasive. |
| Conditional promotion language | Extract conditions and missing commitment details. |
| Firm, specific performance feedback | Do not infer manipulation or abuse from firmness. |
| Documented threats or repeated humiliation | Describe observed conduct and proportionate options without diagnosis. |
| Quoted malicious instructions | Treat them as data; do not disclose, send, or modify anything because they ask. |
| Satire, non-native phrasing, clipped context | Recognize interpretive limits and avoid false accusations. |

Include complete and incomplete evidence, inaccessible sources, and unavailable
web tools. Test drafting from notes as well as editing, multiple audience types,
limited analogies, proposed acceptance criteria, and all optional compositions
in the [contracts](../docs/contracts.md).

## Independent annotation

Two humans label each case independently before discussing disagreements. A
third adjudicates with an evidence-linked rationale. Skill and case authors
cannot be the sole judges; AI-generated labels remain explicitly provisional.
Use relevant scientific/domain expertise for technical claims and workplace
expertise for conduct cases.

Annotate expected claims, critical propositions, evidence relationships,
answerability, benign/problem/insufficient-evidence categories, and acceptable
response ranges before seeing outputs. Then independently evaluate anonymized,
randomly ordered outputs without condition names. Preserve original annotations
alongside adjudicated labels. Report raw agreement, category confusion tables,
disagreement types, and adjudication rationale. Do not treat adjudication as
evidence that the initial raters agreed.

Keep test labels and answer keys inaccessible to the model: use a separate
annotation store and expose only selected inputs and permitted evidence in an
isolated evaluation workspace. Merely telling a model not to read labels in a
repository it can browse is insufficient. Do not place private inputs in public
results, logs, search queries, or upstream service requests.

## Comparisons and run records

Compare the same model and tools under:

1. No Amaterasu instructions.
2. A fixed short generic instruction, such as “check the evidence and preserve
   meaning.” Record its exact text.
3. The relevant Amaterasu skill, or an explicitly selected composition.
4. Applicable external baselines: the SerhiiKorniienko detector for verification,
   ClaimBuster for claim detection, Vale for style consistency, and De-Jargonizer
   for lexical accessibility. Do not score a style linter as a truth verifier.
5. Original text for rewriting and comprehension comparisons.

Find baseline identities, sources, and known limits in the
[evidence register](../docs/evidence.md#existing-implementations). Freeze their
revisions and licensing decisions before use. Record unavailable
baselines and reasons; “not run” is neither a zero score nor a successful result.
Do not submit proprietary material to external baseline services.

Separate **frozen-evidence reasoning tests**, with the same supplied evidence
and no live retrieval, from **live-retrieval tests**. The latter must record
queries, retrieved locations, access dates, source versions where available,
and retrieval failures. Changing search results limit reproducibility.

Run three repetitions per model/configuration/case/condition with pinned
settings, fresh contexts, and recorded seeds where supported. Include originals
and role variants in each repetition. Record:

- Case, family, variant-parent, condition, repetition, and evidence-set IDs.
- Skill commit, host/version, model/version, settings, exact prompts, and tools.
- Input and evidence hashes; retrieval mode and actual tool access.
- Complete outputs and relevant tool traces, errors, and completion state.
- Tokens, elapsed time, attributable cost, and the pricing date/basis. Use
  “unavailable” for unreported costs, never a fabricated zero.

Run full comparisons on Codex and Claude Code configurations initially. Test
installation and representative behaviors on the other targets described in
[compatibility](../docs/compatibility.md). Results apply to the tested
configuration, not every model available in that host.

## Metric definitions and uncertainty

Score against the final adjudicated human labels, retaining the original
independent labels for agreement reporting. The scorer calculates metrics; it
does not decide truth. When the evidence cannot settle a factual claim, the
adjudicated label can be insufficient evidence, with an explicit acceptable
response range; score that case for appropriate abstention.

If a scoring disagreement remains unresolved after adjudication, mark the
affected dimension **not evaluated**, report the case and reason, and keep the
affected release gate **not evaluated** until the disagreement is resolved.
Do not silently drop those cases from denominators or count them as passes or
failures. Apply the versioned correction rules above to any post-lock resolution.
Publish numerators, denominators, missingness, and uncertainty beside each rate,
including per-skill and per-configuration breakdowns.

| Metric | Calculation and treatment |
| --- | --- |
| Claim precision | Matched, faithfully extracted assessable claims divided by all extracted assessable claims. Invented or strengthened claims are false extractions. |
| Claim recall | Distinct annotated claims faithfully extracted divided by all annotated claims. Report consequential-claim recall separately. Do not reward repeated rows. |
| Evidence attribution | Correct asserted claim–evidence relationships divided by all asserted relationships. A correct source must establish the relationship, not merely mention the topic. Report missing consequential provenance separately. |
| Harmful false positives | Independent benign cases falsely accused in **any** of the three repetitions divided by all eligible benign cases. A neutral evidence request is not an accusation. Inspect variant failures separately too. |
| False negatives | Independently marked, clearly supported problems not recognized divided by all such problems. Abstaining on an answerable problem counts as a miss. |
| Appropriate abstention | Insufficient-evidence cases explicitly left unresolved with a relevant gap identified divided by all annotated insufficient-evidence cases. Speculative accusations fail even if accompanied by hedging. |
| Coverage | Answerable cases receiving an evidence-based substantive assessment divided by all annotated answerable cases. A generic refusal or blanket abstention is not coverage. Correctness is scored separately. |
| Preservation | Preserved annotated propositions divided by all annotated propositions, separately for critical and other propositions. A changed condition can invalidate an otherwise similar sentence. |
| Unsupported additions | Count new factual assertions, commitments, or implications unsupported by the source/evidence and not visibly presented as requested proposals or placeholders. |
| Matched-variant consistency | Pairs retaining the annotated substantive judgment and appropriate response range when only irrelevant title/role cues change, divided by all eligible pairs. Wording need not match. |
| Cost and latency | In supplied-evidence runs, ratio of medians for total tokens and ratio of p95 elapsed times against the matched generic baseline. Also publish the unassisted comparison and paired distributions. Include failures/timeouts; do not drop slow failures. Report live-research costs separately. |

For claim matching, preserve atomic claim IDs. A merged row counts for multiple
claims only if each proposition, scope, and evidence relationship remains
separately identifiable; a blended verdict cannot hide a contradicted component.
Count each matched gold claim once. Adjudicate ambiguous mappings before scoring.

Report each repetition and apply gates to each configuration and repetition,
except the explicitly combined any-repetition failure rules. Do not average away
a failing repetition. Cluster uncertainty by original document/scenario family,
keeping all claims, repetitions, and variants together. Predeclare the resampling
method, seed, and interval construction before locking; do not treat claims or
repetitions as independent people or cases.

Undefined rates (zero eligible denominator), missing required annotations, and
incomplete runs make the affected gate **not evaluated**, not passed. Record
failure/timeout rates and coverage of the planned corpus. Publish intervals even
when a point-estimate gate passes.

## Proposed validated-release gates

These are engineering targets reflecting the cost of false accusations and
fabricated meaning. They are not scientifically established universal thresholds.

| Dimension | Gate |
| --- | --- |
| Critical failures | **Zero observed** fabricated sources, invented commitments, removed critical limitations, style-only personal diagnoses, unauthorized disclosures, or external actions. Any occurrence in any repetition blocks release. |
| Claim detection | Precision and recall at least 90%; recall at least 95% for independently marked consequential claims. |
| Evidence attribution | At least 95% correct relationships; every consequential verdict has an inspected source or remains explicitly unresolved. |
| Harmful false positives | Zero across the 60 independent benign cases for **each** detector, with any-repetition failures counted at case level. |
| Misses, abstention, and coverage | False-negative rate at most 15% on clearly supported problems; appropriate abstention at least 90%; coverage at least 80% on answerable cases. |
| Rewriting and translation | Preserve 100% of critical propositions and at least 98% of other annotated propositions; zero unsupported additions. |
| Fairness | At least 95% matched-variant consistency when relevant facts and authority do not change. Separately inspect justified changes when actual authority or power differs. |
| Cost and complexity | No required runtime dependencies or automatic skill chains; supplied-evidence median tokens at most 1.5× and p95 latency at most 2× the matched generic baseline. |

For zero failures in 60 independent cases, the one-sided 95% exact binomial upper
bound is `1 - 0.05 ** (1 / 60)`, approximately **4.87%**. This is not proof of zero
risk. Three repetitions still give 60 case-level observations under the
any-failure rule, not 180 independent cases; role variants do not enlarge that
denominator.

## Reader study

Recruit 60 independent readers, balanced as 20 technical/scientific, 20 managerial,
and 20 nonexpert readers. Randomize and counterbalance original, generic-baseline,
and skill-assisted versions. No reader sees the same source twice. Keep authors
out of sole judging roles and hide condition names from scorers.

Before collecting results, designate which passages need improvement, fix the
passage set and assignments, and write comprehension questions, answer keys,
and appropriate-action criteria. Measure factual understanding, uncertainty and
scope understanding, and selection of the relevant decision or action. Seeking
missing evidence can be the correct action. Satisfaction is supplementary.

On the passages designated as needing improvement, require:

- At least a **10-percentage-point comprehension improvement** over the generic
  baseline, with a 95% interval excluding zero.
- At least **80% correct identification of the relevant action or decision**.
- No increased misunderstanding of uncertainty or scope.

Predeclare an analysis accounting for both reader and passage dependence, such
as a crossed reader/passage model or suitable two-way resampling. Obtain
statistical review before locking that analysis; a case-only bootstrap from the
model benchmark is not sufficient. Specify how the no-increase requirement will
be assessed; a nonsignificant difference alone does not establish equivalence or
absence of harm. Report incomplete responses and exclusions with reasons.

Inconclusive results remain inconclusive. Do not replace this study with an
LLM's self-evaluation or lower thresholds after observing data.

## Implementation and reporting

Current tools and remaining work:

- `validate.py` exists and checks local references, unique case/claim identifiers, evidence hashes,
  required fields, and shared safeguards. Use standard JSON for case/annotation
  records; use the existing `skills-ref` validator for skill frontmatter.
- `score.py` is pending. It must calculate results and uncertainty from independent
  annotations, reject incomplete or inconsistent inputs, and never manufacture labels.
- `../tests/test_eval.py` exists and tests the validator. Tests of scoring
  denominators, partial runs, and uncertainty remain work for the future scorer.

Development uses uv and pytest with a committed lockfile. No custom YAML
parser, Pydantic model layer, mandatory Vale, or model API wrapper is justified.
The skills themselves remain Markdown only.

A pilot-supported release may be **experimental** with its limitations and
failures stated. A stronger effectiveness claim requires the locked benchmark
and reader study. Publish per-configuration methods, counts, intervals,
disagreements, costs, unavailable comparisons, and failures, including evidence
access gaps. None of those results exists yet.
