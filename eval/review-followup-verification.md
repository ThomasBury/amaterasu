# Review follow-up verification — 2026-11-19

Implements the agreed adversarial-review follow-up on branch
`fix/evaluation-integrity`, based on `main` at `c1157ab`. Repository changes
only: no live model runs, no scanner rerun, no publishing, and no personal
host configuration changes.

## Phase 7 integrity

- Added the [separate scorecard](phase-7-scorecard.md). The
  [blinded packet](phase-7-review.md) bytes are unchanged; its SHA-256 remains
  `d6d6ea61454aed1c0ce4225f3a76801f21eb2c65d6f72aba0d18b945d7fb346c`.
  The scorecard adds reporting rules (case-level findings, explicit ties and
  inapplicable criteria, descriptive-only per-skill summaries, pairs 03 and 07
  as basic controls), a post-judgment blinding check (guess, confidence, cue;
  reported descriptively, never used to reweight judgments), and the
  condition-key reveal procedure.
- Committed the condition mapping before scoring. The commitment is
  `SHA-256(condition-key.json bytes + nonce bytes)`:
  `0830130369a7c923d481463d88d3b9099edcaca1703ef23f0a583b47c3993cdd`.
  The nonce is 32 random bytes (64 lowercase hex characters) stored in the
  gitignored `.phase7-private/commitment-nonce.txt`. The key file
  `.phase7-private/condition-key.json` must remain byte-identical until
  reveal. The nonce prevents the small A/B mapping from being guessed by
  hashing candidate keys.
- Custodian transfer is pending and required before scoring: the key file and
  nonce pass to an independent custodian, who holds them until judgments and
  the blinding check are submitted, then reveals both for digest verification.
  Until transfer, the commitment is author-held: it binds the mapping but is
  not yet independent.
- Updated the living [roadmap](../MILESTONES.md) Phase 7 items accordingly.
  The dated [Phase 7 verification record](phase-7-verification.md) stays a
  snapshot of the 2026-11-18 runs.

## Effectiveness study redesign

- Added the [effectiveness protocol](effectiveness-protocol.md) as the active
  design for the next study, tracked as Phase 8 in the roadmap:
  preregistration before generation; 12–20 fresh realistic cases with natural
  requests (ordinary work, clean documents deserving few or zero criticisms,
  hard cases with buried qualifications or conflicting evidence); a separate
  labeled challenge set for known baseline failures; independent pre-output
  annotation; skill, ordinary-prompt, and concise well-written baseline
  conditions; tool-enabled Kagami runs with identical controlled fetch and
  search access and a trace checklist; scoring for fidelity, missing-evidence
  handling, usefulness, material errors, and unnecessary length; and the
  simplify-or-retire decision rule from [docs/evidence.md](../docs/evidence.md).
- The 90 pilot micro-cases remain intact as validator fixtures and regression
  sources. Their median source excerpt is under 20 words (range 4–41), which
  isolates single failures but cannot judge ordinary user workflows. Optional
  adjudication of about ten micro-cases and Mamoru's separate expert sheet are
  noted in the protocol; neither replaces independent annotation of new cases.

## Instruction consolidation — draft only

- Added the [consolidation proposal](instruction-consolidation-proposal.md)
  and the plain-text [draft entry point](drafts/kagami-SKILL-draft.txt),
  tracked as Phase 9. Nothing is installed. The draft removes the
  `Final check` repetition and workflow restatements of rules the mandated
  reference already carries, keeps the shared essentials verbatim, and keeps
  privacy and tool-use rules before the first relevant action. Shipping
  requires the fresh-session comparison in the proposal; the behavioral cost
  of the current duplication is unknown.

## Documentation fixes

- Roadmap Phase 6 now records the green GitHub-hosted CI runs of 2026-11-18
  ([pull request #11](https://github.com/ThomasBury/amaterasu/actions/runs/44352543751),
  [main push](https://github.com/ThomasBury/amaterasu/actions/runs/44356618740)).
  The dated [Phase 6 record](phase-6-verification.md) stays a snapshot.
- [README](../README.md) install section now labels host coverage separately:
  Codex and OpenCode runtime checks passed; Pi installation and update were
  exercised with the Pi runtime unavailable; Claude Code was unavailable, so
  its installation and runtime checks are outstanding.
- README comparison wording now says Kagami **is instructed to** reserve two
  of six searches when discovery is requested and permitted; the budget is a
  prompt norm, not a runtime guarantee.
- Reworded one sentence in
  [Kakehashi's reference](../skills/kakehashi/references/audiences-and-meaning.md):
  “Do not judge readers solely by agreement with the explanation or exact
  wording.” became “Agreement with the explanation or repetition of its exact
  wording does not by itself establish understanding.” Meaning is preserved.
  This targets the SkillEvaluator anti-refusal false positive recorded in the
  Phase 7 verification; the scanner rerun is pending because the tool is not
  installed in this environment. The kakehashi package bytes now differ from
  the Phase 7 run revision; the frozen answers are unaffected, and
  `.phase7-private/skill-hashes.json` describes the pre-rewording revision.

## Evidence register refresh

Retried three previously inaccessible sources on 2026-11-19 and updated
[docs/evidence.md](../docs/evidence.md) with what was actually inspected:

- [ERIC EJ1372738](https://eric.ed.gov/?id=EJ1372738): record and abstract
  inspected. Wineburg et al. (2022), Journal of Educational Psychology 114(5),
  893–909; matched-control field study (treatment n = 271, control n = 228),
  six 50-minute lessons, multilevel model reporting significant growth in
  credibility judgment. Full text not inspected; secondary-school transfer
  remains uncertain.
- [SBAR review](https://bmjopen.bmj.com/content/8/8/e022202): full text
  inspected (previously 403). Müller et al. (2018) included eleven studies,
  eight before–after and three controlled (including one randomized). Nine
  were rated weak quality. Of 26 outcomes, eight improved significantly,
  eleven showed descriptive improvement without reported statistical tests,
  six showed no statistically significant change, and one showed a descriptive
  worsening in patient safety (an increase in overall falls). No studies
  reported power calculations, and heterogeneity prevented meta-analysis.
- [NAQ-R DOI](https://doi.org/10.1080/02678370902815673): resolved to the
  publisher citation record (Work & Stress 23(1), 24–44, confirmed); the
  abstract page returned 403. Detailed validation claims remain per supplied
  plan, not independently rechecked.

## Checks run

From the repository root on Linux with the locked Python 3.11 environment:

```sh
sh eval/check.sh
sha256sum eval/phase-7-review.md
```

Results: 95 pytest tests passed; the validator reported four skill packages
and 90 pilot records; repository Markdown links and anchors passed; all four
`skills-ref` checks passed; staged and unstaged whitespace checks passed. The
packet digest matched the recorded value above. The commitment was recomputed
from the stored key bytes and nonce and matched the published digest.

## Pending and untested

- Independent custodian transfer, independent judgments, and the blinding
  check require people; none has happened yet. The extent and direction of
  any unblinding remain unknown.
- The SkillEvaluator rerun of the reworded Kakehashi reference.
- Live model behavior of every skill, the tool-enabled runs, and the
  consolidation comparison. No effectiveness result is claimed.
- No version bump or release; the plugin remains 0.3.1. The Kakehashi
  reference change rides the next release.
