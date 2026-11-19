# Phase 7 independent review scorecard

Use this scorecard with the frozen [blinded review packet](phase-7-review.md).
The packet bytes are unchanged; its SHA-256 is recorded in the
[Phase 7 verification record](phase-7-verification.md). This separate scorecard
adds the reporting rules and the post-judgment blinding check without altering
the frozen answers. The packet's embedded scorecard remains part of the frozen
artifact; record judgments here.

Coordinators should give reviewers the packet and this scorecard. Keep
coordinator notes with examples of answer features private until all reviewers
have submitted their blinding guesses.

## Before judging

1. Record your reviewer name or ID and the review date below. You should be
   independent of the case design and answer generation.
2. If you have a repository checkout, run
   `git show HEAD:eval/phase-7-review.md | sha256sum` from its root and compare
   the digest with the verification record. Git supplies the committed bytes
   before checkout line-ending conversion.
3. Read each prompt and its source excerpts, then compare answers A and B.
   Open the blinding-check section after submitting your judgments. Wait until
   you submit your blinding guesses to consult pilot annotations or comparison
   notes.

## Judging rules

Judge each criterion separately. Record A, B, Tie, or N/A and a short reason
grounded in the source or the requested decision. Use N/A when the criterion
does not apply. Mark a pair Incomplete if either answer is missing.

- **Fidelity to the source** covers facts, quantities, attribution, dates,
  conditions, scope, and the strength of the original wording.
- **Handling missing evidence** covers which gaps matter and whether the answer
  carries those limits through to its conclusions.
- **Usefulness for the next decision** covers how well the answer helps the
  intended reader do the task or take an appropriate next step. Formatting is
  part of the user experience: judge whether an answer's structure helps the
  reader, rather than penalizing or rewarding style as such.

Record material errors separately for each answer, even when that answer wins.
A material error changes what the source means, what the evidence establishes,
or what the reader can reasonably do next. Quote the relevant answer text and
cite the source line where possible. Enter None after checking an answer with
no material errors.

## Reporting rules

- Case-level findings are the primary result. Record ties and inapplicable
  criteria explicitly; a tie is a finding, not a missing result.
- Pairs 03 and 07 are basic controls. Both answers preserving everything there
  is an expected ceiling, not evidence that the skill and baseline are
  equivalent in general.
- Per-skill summaries carry descriptive weight only: eight cases, two per
  skill, one model, one run per condition. Do not state or imply a reliable
  benefit, an accuracy rate, or superiority from this packet.
- Apparent ties in easy cases are impressions until recorded judgments exist;
  report what reviewers actually recorded, including disagreements.

## Judgment scorecard

Reviewer name or ID …

Review date …

| Pair | Fidelity and reason | Missing evidence and reason | Usefulness and reason | Material errors in A | Material errors in B |
| --- | --- | --- | --- | --- | --- |
| 01 | | | | | |
| 02 | | | | | |
| 03 | | | | | |
| 04 | | | | | |
| 05 | | | | | |
| 06 | | | | | |
| 07 | | | | | |
| 08 | | | | | |

Submit this table before continuing to the blinding check.

## Post-judgment blinding check

After submitting the judgment scorecard, and without revising it, record for
each pair which answer you believe used the skill:

- **Guess:** A, B, or Unsure.
- **Confidence:** low, medium, or high.
- **Cue:** the wording, structure, or habit that drove the guess, if any.

| Pair | Guess (A/B/Unsure) | Confidence | Cue noticed |
| --- | --- | --- | --- |
| 01 | | | |
| 02 | | | |
| 03 | | | |
| 04 | | | |
| 05 | | | |
| 06 | | | |
| 07 | | | |
| 08 | | | |

Report guesses descriptively: counts per answer letter, confidence
distribution, and the cues reviewers noticed, alongside the guess accuracy
against the revealed key. Do not use the guesses to reweight or discard
judgments, and do not present guess accuracy as a validity gate.

## Condition-key commitment and reveal

The A/B condition mapping is committed before scoring so it cannot be chosen
after judgments:

- The commitment is `SHA-256(condition-key.json bytes + nonce bytes)`, where
  the nonce is 32 random bytes recorded as 64 lowercase hex characters.
- The published commitment digest is
  `0830130369a7c923d481463d88d3b9099edcaca1703ef23f0a583b47c3993cdd`.
- Before scoring, the key file and nonce pass to an independent custodian, who
  holds them until judgments and the blinding check are submitted. The nonce
  prevents the small mapping from being guessed by hashing candidate keys.
- After scoring, the custodian reveals the key file and the nonce. Verify that
  `SHA-256(revealed key bytes + bytes.fromhex(revealed nonce))` equals the
  published commitment, then report which letter was the skill condition per
  pair and the blinding-check accuracy.

The commitment procedure and its current status are recorded in the
[follow-up verification record](review-followup-verification.md).
