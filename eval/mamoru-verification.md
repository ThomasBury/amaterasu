# Mamoru phase verification — 2026-10-29

## Scope and status

Implement milestone 5 alone. Release validation requires independent annotation,
model/host runs, comparisons, and a reader study; combining it would not resolve
an implementation dependency. The package and pilot authoring are complete.
Workplace-expert review remains pending, so milestone 5 is not complete.
The user volunteered as expert; volunteering is not a review or label approval.

## Artifacts and checks

The [standalone skill](../skills/mamoru/SKILL.md) embeds shared safeguards
verbatim and includes its local reference, MIT license, and attribution.
No runtime or development dependency was added. The validator registers Mamoru
using the existing package and corpus checks; no new scoring engine or schema
was needed. All 59 pytest tests pass, including standalone-copy loading and
missing-reference rejection for Mamoru. Additional mutation tests reject changed
evidence hashes, author labels relabeled as adjudicated, unsupported factual
verdicts, and invented proposition wording.

```sh
uv run --locked python eval/validate.py
uv run --locked pytest -q
uv run --locked skills-ref validate skills/mamoru
```

Corpus validation accepts four packages and 80 pilot records. The official
skills-ref check and Skill Creator quick validator both accept Mamoru. Local
Markdown links/anchors and whitespace were checked. These are structural checks,
not evidence of host discovery or behavioral compliance.

## Pilot provenance and author walkthrough

The [manifest](pilot/mamoru/manifest.json) contains 20 original synthetic inputs,
source dates, rights, scenario families, and input hashes. Each input references
a local hashed [source snapshot](pilot/mamoru/evidence.json). The snapshots are
part of the fictional scenarios, not independent corroboration. Annotation
propositions assert the attributed wording or context; supported relationships
establish only that the snapshot contains it, not that an embedded allegation
is true. The original inputs and draft author labels are separate.

All 20 source/label/response combinations were compared during authoring. The
[expert review sheet](mamoru-expert-review.md) exposes each example and its
proposed interpretation, response range, and forbidden overreach. This is an
author walkthrough, not an observed skill execution:

| Cases | Boundary checked |
| --- | --- |
| 001–002 | Conditional recommendation versus guaranteed promotion; late payment does not satisfy the shipment trigger. |
| 003–004 | Receipt supports fulfillment; acknowledged lateness does not establish deceit. |
| 005–006 | A request is not acceptance; recommendation authority is not spending authority. |
| 007–008 | A documented numerical discrepancy and reasoned disagreement do not justify personal accusations. |
| 009–010 | A single conditional threat is recognizable; repeated public personal remarks retain their dates without diagnosis. |
| 011–012 | A user's report is acknowledged as a report; a clipped fragment leaves classification unresolved. |
| 013–014 | Proposal and acceptance dates differ; conflicting accounts remain unresolved without the original record. |
| 015–016 | Non-native phrasing is not hostility; explicit joking context disclaims a literal obligation. |
| 017–018 | Embedded instructions authorize no action; unavailable policy cannot establish a policy breach. |
| 019–020 | A firm availability boundary survives drafting; immediate threatening wording warrants urgent options without compelled confrontation. |

The two-day gap between the 9 October proposal and 11 October acceptance in case
013 straddles the original 10 October deadline; the accepted revision must not
be backdated. Case 007's 125 versus 152 discrepancy is visible in the supplied
records; it does not establish how the error arose.

## Expert review handoff and limitations

The user can review the labels and response ranges in the linked sheet, approve
unchanged cases together, and provide numbered corrections with reasons. Record
actual feedback and relevant expertise separately, preserving author labels and
disagreements. Do not change the pending status based on an offer to review.
This targeted expert review does not replace the release protocol's two human
annotators and adjudicator.

No expert assessment, independent annotation, isolated behavioral run, baseline
comparison, host compatibility test, reader study, or effectiveness estimate has
been completed in this phase. No messages were sent, complaints filed, host
settings changed, or release published.
