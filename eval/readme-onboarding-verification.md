# README onboarding verification — 2026-11-10

Checked the working tree based on `b3cf38f`. The [README](../README.md) gives
each host an install command and a first review prompt. Its overview table
describes all four skills. Alternate installation routes, updates, and
troubleshooting are in the [installation guide](../docs/installation.md).

## Checks

- `.venv/bin/pytest -q` passed all 95 tests.
- `.venv/bin/python eval/validate.py` passed for four skill packages and 90
  pilot records. `.venv/bin/skills-ref validate skills/<skill>` passed for all
  four skills.
- `eval.validate.check_links` passed on a temporary copy of the tracked and
  unignored working-tree files. The README logo path also exists.
- `pandoc --from=gfm --to=html5 --no-highlight` rendered the README and
  installation guide. Checked the two tables, all 11 contents links, and the
  separate installation and prompt blocks for Claude Code, Codex, OpenCode,
  and Pi. Compared the four routes with the prior documented commands and
  invocation instructions.
- Opened the relocated host and installer documentation links and inspected both
  public example sources. [NASA’s DART announcement](https://www.nasa.gov/news-release/nasa-confirms-dart-mission-impact-changed-asteroids-motion-in-space/)
  and [Attention Is All You Need](https://arxiv.org/abs/1706.03762).
- `git diff --check` passed.

The pasted-text examples use fictional inputs. This pass checked the
documentation and packages. For observed host behavior, see the
[earlier installation record](first-use-verification.md). Fresh host
installations, model responses, and YouTube retrieval remain unverified.
