# Evaluation protocol

**Status: all four skills have pilot artifacts.** Each has 20 original
synthetic cases with provisional AI-author annotations (80 cases total).
Mamoru workplace-expert review is [pending](mamoru-expert-review.md).
Independent annotations, isolated model runs, baseline results, and reader-study
results remain pending. See the [Kagami](kagami-verification.md),
[Kotoba](kotoba-verification.md), [Kakehashi](kakehashi-verification.md), and
[Mamoru](mamoru-verification.md) verification records.
The [annotation rubric](annotation-rubric.md) defines what to collect and how to
judge it. Examples in that rubric are author calibration examples, not evidence
of effectiveness.

The question is whether Amaterasu improves reasoning, preservation, comprehension,
and useful action without false accusations or fabricated meaning. A confident
tone, shorter text, a model's self-rating, or a passing file validator cannot
answer that question.

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
4. Applicable upstream baselines: the existing detector for verification,
   ClaimBuster for claim detection, Vale for style consistency, and De-Jargonizer
   for lexical accessibility. Do not score a style linter as a truth verifier.
5. Original text for rewriting and comprehension comparisons.

Freeze upstream revisions and licensing decisions before use. Record unavailable
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

Add small utilities only when the case format and actual data need them:

- `validate.py`: local references, unique case/claim identifiers, evidence hashes,
  required fields, and shared safeguards. Use standard JSON for case/annotation
  records; use the existing `skills-ref` validator for skill frontmatter.
- `score.py`: calculations and uncertainty from independent annotations. Reject
  incomplete or inconsistent inputs; do not infer truth or manufacture labels.
- `tests/test_eval.py`: meaningful checks for malformed/missing evidence,
  duplicate IDs, denominator errors, partial runs, and dependent variants.

Development will use uv and pytest with a committed lockfile. No custom YAML
parser, Pydantic model layer, mandatory Vale, or model API wrapper is justified.
The skills themselves remain Markdown only.

A pilot-supported release may be **experimental** with its limitations and
failures stated. A stronger effectiveness claim requires the locked benchmark
and reader study. Publish per-configuration methods, counts, intervals,
disagreements, costs, unavailable comparisons, and failures, including evidence
access gaps. None of those results exists yet.
