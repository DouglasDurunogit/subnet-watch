# ALARMS - generated 2026-07-28T10:43:35Z, block 8719929

window: first_seen in [2026-07-28T09:29:07Z, 2026-07-28T10:44:07Z)  (60 min interval + 15 min overlap)

Report ONLY the rows under NEW SINCE LAST RUN. Rows under STILL OPEN were
already reported in an earlier window and must not be re-alarmed.

## NEW SINCE LAST RUN

| event_id | netuid | class | severity | first_seen_utc | one_line |
|---|---|---|---|---|---|
| `sn117:burn_drop:0.000` | 117 | BURN_DROP | P0 | 2026-07-28T10:44:07Z | sn117 burn fell 1.000 -> 0.000 - miners can earn again |
| `sn67:scoring_commit:2026-07-28T09:37:00Z` | 67 | SCORING_COMMIT | P1 | 2026-07-28T10:44:07Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20260728.post5 |
| `sn67:readme_task_diff:b615b92c78ccda43` | 67 | README_TASK_DIFF | P2 | 2026-07-28T10:44:07Z | sn67 README task/scoring sections changed |

### detail

- **`sn117:burn_drop:0.000`** - sn117 burn fell 1.000 -> 0.000 - miners can earn again
  - This subnet paid miners nothing and now pays. Worth a look before the field fills up.
- **`sn67:scoring_commit:2026-07-28T09:37:00Z`** - sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20260728.post5
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn67:readme_task_diff:b615b92c78ccda43`** - sn67 README task/scoring sections changed
  - Only the task-describing headings are hashed, so badge and typo edits do not trigger this.

## STILL OPEN (already reported - do not re-alarm)

| event_id | netuid | class | first_seen_utc | one_line |
|---|---|---|---|---|
| `sn104:burn_drop:0.965` | 104 | BURN_DROP | 2026-07-28T07:30:22Z | sn104 burn fell 1.000 -> 0.965 - miners can earn again |
| `sn76:scoring_commit:2026-07-28T06:56:11Z` | 76 | SCORING_COMMIT | 2026-07-28T07:30:22Z | sn76 commit touches scoring: Skip tracks with no task set instead of abandoning the whole round |
| `sn85:scoring_commit:2026-07-28T07:19:51Z` | 85 | SCORING_COMMIT | 2026-07-28T07:30:22Z | sn85 commit touches scoring: defer scoring commit to DB (#180) |
| `sn76:scoring_commit:2026-07-28T08:08:04Z` | 76 | SCORING_COMMIT | 2026-07-28T08:08:26Z | sn76 commit touches scoring: Read served ground truth so findings are scored, not just verdicts |

## RESOLVED IN THIS WINDOW

_none_
