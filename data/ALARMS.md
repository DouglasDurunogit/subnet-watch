# ALARMS - generated 2026-07-28T08:07:51Z, block 8719150

window: first_seen in [2026-07-28T06:53:26Z, 2026-07-28T08:08:26Z)  (60 min interval + 15 min overlap)

Report ONLY the rows under NEW SINCE LAST RUN. Rows under STILL OPEN were
already reported in an earlier window and must not be re-alarmed.

## NEW SINCE LAST RUN

| event_id | netuid | class | severity | first_seen_utc | one_line |
|---|---|---|---|---|---|
| `sn104:burn_drop:0.965` | 104 | BURN_DROP | P0 | 2026-07-28T07:30:22Z | sn104 burn fell 1.000 -> 0.965 - miners can earn again |
| `sn76:scoring_commit:2026-07-28T06:56:11Z` | 76 | SCORING_COMMIT | P1 | 2026-07-28T07:30:22Z | sn76 commit touches scoring: Skip tracks with no task set instead of abandoning the whole round |
| `sn85:scoring_commit:2026-07-28T07:19:51Z` | 85 | SCORING_COMMIT | P1 | 2026-07-28T07:30:22Z | sn85 commit touches scoring: defer scoring commit to DB (#180) |
| `sn76:scoring_commit:2026-07-28T08:08:04Z` | 76 | SCORING_COMMIT | P1 | 2026-07-28T08:08:26Z | sn76 commit touches scoring: Read served ground truth so findings are scored, not just verdicts |

### detail

- **`sn104:burn_drop:0.965`** - sn104 burn fell 1.000 -> 0.965 - miners can earn again
  - This subnet paid miners nothing and now pays. Worth a look before the field fills up.
- **`sn76:scoring_commit:2026-07-28T06:56:11Z`** - sn76 commit touches scoring: Skip tracks with no task set instead of abandoning the whole round
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn85:scoring_commit:2026-07-28T07:19:51Z`** - sn85 commit touches scoring: defer scoring commit to DB (#180)
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn76:scoring_commit:2026-07-28T08:08:04Z`** - sn76 commit touches scoring: Read served ground truth so findings are scored, not just verdicts
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.

## STILL OPEN (already reported - do not re-alarm)

_none_

## RESOLVED IN THIS WINDOW

_none_
