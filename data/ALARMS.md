# ALARMS - generated 2026-07-28T15:03:42Z, block 8721229

window: first_seen in [2026-07-28T13:49:08Z, 2026-07-28T15:04:08Z)  (60 min interval + 15 min overlap)

Report ONLY the rows under NEW SINCE LAST RUN. Rows under STILL OPEN were
already reported in an earlier window and must not be re-alarmed.

## NEW SINCE LAST RUN

| event_id | netuid | class | severity | first_seen_utc | one_line |
|---|---|---|---|---|---|
| `sn28:release:v0.3.12` | 28 | RELEASE | P1 | 2026-07-28T15:04:08Z | sn28 released v0.3.12 |
| `sn56:scoring_commit:2026-07-28T14:55:22Z` | 56 | SCORING_COMMIT | P1 | 2026-07-28T15:04:08Z | sn56 commit touches scoring: feat(validator): auto-balance emission split from tournament particip… |
| `sn76:scoring_commit:2026-07-28T14:03:58Z` | 76 | SCORING_COMMIT | P1 | 2026-07-28T15:04:08Z | sn76 commit touches scoring: Retry validator self registration until it succeeds |
| `sn103:release:v2003: validator: restore miner burn fra` | 103 | RELEASE | P1 | 2026-07-28T15:04:08Z | sn103 released v2003: validator: restore miner burn fraction to 0.8 |
| `sn103:scoring_commit:2026-07-28T13:16:22Z` | 103 | SCORING_COMMIT | P1 | 2026-07-28T15:04:08Z | sn103 commit touches scoring: validator: restore miner burn fraction to 0.8 |

### detail

- **`sn28:release:v0.3.12`** - sn28 released v0.3.12
  - published 2026-07-28T14:30:33Z (was v0.3.13-dev)
- **`sn56:scoring_commit:2026-07-28T14:55:22Z`** - sn56 commit touches scoring: feat(validator): auto-balance emission split from tournament particip…
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn76:scoring_commit:2026-07-28T14:03:58Z`** - sn76 commit touches scoring: Retry validator self registration until it succeeds
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn103:release:v2003: validator: restore miner burn fra`** - sn103 released v2003: validator: restore miner burn fraction to 0.8
  - published 2026-07-28T13:16:22Z (was v2002: validator: chunk oversized settle batches to a deterministic gate budget)
- **`sn103:scoring_commit:2026-07-28T13:16:22Z`** - sn103 commit touches scoring: validator: restore miner burn fraction to 0.8
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.

## STILL OPEN (already reported - do not re-alarm)

| event_id | netuid | class | first_seen_utc | one_line |
|---|---|---|---|---|
| `sn104:burn_drop:0.965` | 104 | BURN_DROP | 2026-07-28T07:30:22Z | sn104 burn fell 1.000 -> 0.965 - miners can earn again |
| `sn117:burn_drop:0.000` | 117 | BURN_DROP | 2026-07-28T10:44:07Z | sn117 burn fell 1.000 -> 0.000 - miners can earn again |
| `sn76:scoring_commit:2026-07-28T06:56:11Z` | 76 | SCORING_COMMIT | 2026-07-28T07:30:22Z | sn76 commit touches scoring: Skip tracks with no task set instead of abandoning the whole round |
| `sn85:scoring_commit:2026-07-28T07:19:51Z` | 85 | SCORING_COMMIT | 2026-07-28T07:30:22Z | sn85 commit touches scoring: defer scoring commit to DB (#180) |
| `sn76:scoring_commit:2026-07-28T08:08:04Z` | 76 | SCORING_COMMIT | 2026-07-28T08:08:26Z | sn76 commit touches scoring: Read served ground truth so findings are scored, not just verdicts |
| `sn67:scoring_commit:2026-07-28T09:37:00Z` | 67 | SCORING_COMMIT | 2026-07-28T10:44:07Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20260728.post5 |
| `sn76:scoring_commit:2026-07-28T11:28:42Z` | 76 | SCORING_COMMIT | 2026-07-28T11:29:26Z | sn76 commit touches scoring: Poll for validator image updates every two minutes |
| `sn71:scoring_commit:2026-07-28T12:00:19Z` | 71 | SCORING_COMMIT | 2026-07-28T12:10:04Z | sn71 commit touches scoring: Verify durable chain settlement readback |
| `sn89:scoring_commit:2026-07-28T12:59:01Z` | 89 | SCORING_COMMIT | 2026-07-28T12:59:29Z | sn89 commit touches scoring: hf scoreboard: publish n_submitters_3d |
| `sn67:readme_task_diff:b615b92c78ccda43` | 67 | README_TASK_DIFF | 2026-07-28T10:44:07Z | sn67 README task/scoring sections changed |

## RESOLVED IN THIS WINDOW

_none_
