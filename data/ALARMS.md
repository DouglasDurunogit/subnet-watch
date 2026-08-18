# ALARMS - generated 2026-08-18T19:06:45Z, block 8873604

window: first_seen in [2026-08-18T17:52:17Z, 2026-08-18T19:07:17Z)  (60 min interval + 15 min overlap)

Report ONLY the rows under NEW SINCE LAST RUN. Rows under STILL OPEN were
already reported in an earlier window and must not be re-alarmed.

## NEW SINCE LAST RUN

| event_id | netuid | class | severity | first_seen_utc | one_line |
|---|---|---|---|---|---|
| `sn62:scoring_commit:2026-08-18T17:56:49Z` | 62 | SCORING_COMMIT | P1 | 2026-08-18T18:13:46Z | sn62 commit touches scoring: Merge pull request #480 from ridgesai/update/add-testnet-validator |
| `sn15:scoring_commit:2026-08-18T18:29:41Z` | 15 | SCORING_COMMIT | P1 | 2026-08-18T19:07:17Z | sn15 commit touches scoring: docs(miner-guide): note that find_product q matches values, not keys … |
| `sn108:readme_task_diff:fa8dc13fe8c76401` | 108 | README_TASK_DIFF | P2 | 2026-08-18T19:07:17Z | sn108 README task/scoring sections changed |

### detail

- **`sn62:scoring_commit:2026-08-18T17:56:49Z`** - sn62 commit touches scoring: Merge pull request #480 from ridgesai/update/add-testnet-validator
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn15:scoring_commit:2026-08-18T18:29:41Z`** - sn15 commit touches scoring: docs(miner-guide): note that find_product q matches values, not keys …
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn108:readme_task_diff:fa8dc13fe8c76401`** - sn108 README task/scoring sections changed
  - Only the task-describing headings are hashed, so badge and typo edits do not trigger this.

## STILL OPEN (already reported - do not re-alarm)

| event_id | netuid | class | first_seen_utc | one_line |
|---|---|---|---|---|
| `sn70:burn_drop:0.000` | 70 | BURN_DROP | 2026-08-13T04:32:20Z | sn70 burn fell 1.000 -> 0.000 - miners can earn again |
| `sn6:weights_version_bump:3000` | 6 | WEIGHTS_VERSION_BUMP | 2026-08-13T16:39:08Z | sn6 weights_version 2018 -> 3000 |
| `sn118:burn_drop:0.000` | 118 | BURN_DROP | 2026-08-13T17:45:02Z | sn118 burn fell 1.000 -> 0.000 - miners can earn again |
| `sn100:burn_drop:0.000` | 100 | BURN_DROP | 2026-08-13T19:46:45Z | sn100 burn fell 1.000 -> 0.000 - miners can earn again |
| `sn2:burn_drop:0.822` | 2 | BURN_DROP | 2026-08-14T09:18:19Z | sn2 burn fell 1.000 -> 0.822 - miners can earn again |
| `sn20:burn_drop:0.000` | 20 | BURN_DROP | 2026-08-14T15:05:31Z | sn20 burn fell 1.000 -> 0.000 - miners can earn again |
| `sn39:burn_drop:0.000` | 39 | BURN_DROP | 2026-08-14T15:05:31Z | sn39 burn fell 1.000 -> 0.000 - miners can earn again |
| `sn2:burn_drop:0.824` | 2 | BURN_DROP | 2026-08-14T23:33:14Z | sn2 burn fell 1.000 -> 0.824 - miners can earn again |
| `sn19:burn_drop:0.986` | 19 | BURN_DROP | 2026-08-14T23:33:14Z | sn19 burn fell 1.000 -> 0.986 - miners can earn again |
| `sn2:burn_drop:0.823` | 2 | BURN_DROP | 2026-08-17T06:00:04Z | sn2 burn fell 1.000 -> 0.823 - miners can earn again |
| `sn121:burn_drop:0.620` | 121 | BURN_DROP | 2026-08-17T15:52:42Z | sn121 burn fell 1.000 -> 0.620 - miners can earn again |
| `sn2:burn_drop:0.825` | 2 | BURN_DROP | 2026-08-18T13:05:31Z | sn2 burn fell 1.000 -> 0.825 - miners can earn again |
| `sn71:scoring_commit:2026-08-11T18:25:04Z` | 71 | SCORING_COMMIT | 2026-08-11T19:50:00Z | sn71 commit touches scoring: Reuse bounded artifact verification sessions |
| `sn62:scoring_commit:2026-08-11T20:08:25Z` | 62 | SCORING_COMMIT | 2026-08-11T22:58:25Z | sn62 commit touches scoring: update validator api changes |
| `sn71:scoring_commit:2026-08-11T23:29:21Z` | 71 | SCORING_COMMIT | 2026-08-11T23:54:20Z | sn71 commit touches scoring: Reuse artifact verification transport pool |
| `sn71:scoring_commit:2026-08-12T02:30:59Z` | 71 | SCORING_COMMIT | 2026-08-12T02:39:41Z | sn71 commit touches scoring: Isolate concurrent artifact verification transports |
| `sn100:release:v3.3.19 — design auto-enqueue + migratio` | 100 | RELEASE | 2026-08-12T06:05:56Z | sn100 released v3.3.19 — design auto-enqueue + migration 0019 fix |
| `sn100:scoring_commit:2026-08-12T04:29:33Z` | 100 | SCORING_COMMIT | 2026-08-12T06:05:56Z | sn100 commit touches scoring: Merge pull request #120 from BaseIntelligence/feat/prism-miner-paid-li |
| `sn71:scoring_commit:2026-08-12T07:37:36Z` | 71 | SCORING_COMMIT | 2026-08-12T07:49:32Z | sn71 commit touches scoring: Recover artifact verification from stale pools |
| `sn96:release:Verathos v0.1.36 — Runtime and Capacity ` | 96 | RELEASE | 2026-08-12T09:22:09Z | sn96 released Verathos v0.1.36 — Runtime and Capacity Stability |
| `sn85:scoring_commit:2026-08-12T09:34:50Z` | 85 | SCORING_COMMIT | 2026-08-12T10:34:51Z | sn85 commit touches scoring: add audio validation for competitions (#184) |
| `sn100:release:v3.3.21 — Prism Lium single-GPU hard-rej` | 100 | RELEASE | 2026-08-12T10:34:51Z | sn100 released v3.3.21 — Prism Lium single-GPU hard-reject (#129) |
| `sn51:release:executor-v1.117` | 51 | RELEASE | 2026-08-12T11:33:57Z | sn51 released executor-v1.117 |
| `sn28:release:v0.4.4-dev` | 28 | RELEASE | 2026-08-12T12:34:56Z | sn28 released v0.4.4-dev |
| `sn28:scoring_commit:2026-08-12T10:25:25Z` | 28 | SCORING_COMMIT | 2026-08-12T12:34:56Z | sn28 commit touches scoring: Document miner model sourcing options |
| `sn67:scoring_commit:2026-08-12T11:45:36Z` | 67 | SCORING_COMMIT | 2026-08-12T12:34:56Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20260812.post4 |
| `sn120:scoring_commit:2026-08-12T12:26:03Z` | 120 | SCORING_COMMIT | 2026-08-12T12:34:56Z | sn120 commit touches scoring: rollouts: recover 7k terminal_lego tasks by stubbing empty task_file |
| `sn28:release:v0.4.4` | 28 | RELEASE | 2026-08-12T14:09:20Z | sn28 released v0.4.4 |
| `sn28:scoring_commit:2026-08-12T12:46:41Z` | 28 | SCORING_COMMIT | 2026-08-12T14:09:20Z | sn28 commit touches scoring: Release gm-miner v0.4.4 |
| `sn56:scoring_commit:2026-08-12T13:16:40Z` | 56 | SCORING_COMMIT | 2026-08-12T14:09:20Z | sn56 commit touches scoring: Oversample 2026+ models into one R1 and one boss-round task (#1353) |
| `sn96:release:Verathos v0.1.37 — Scoring Integrity and` | 96 | RELEASE | 2026-08-12T14:09:20Z | sn96 released Verathos v0.1.37 — Scoring Integrity and Fairness |
| `sn96:scoring_commit:2026-08-12T11:40:32Z` | 96 | SCORING_COMMIT | 2026-08-12T14:09:20Z | sn96 commit touches scoring: fix: correct validator scoring inputs |
| `sn120:scoring_commit:2026-08-12T13:36:35Z` | 120 | SCORING_COMMIT | 2026-08-12T14:09:20Z | sn120 commit touches scoring: publish bench rollout records: per-task trajectories to hippius + api |
| `sn111:scoring_commit:2026-08-12T14:50:47Z` | 111 | SCORING_COMMIT | 2026-08-12T15:29:26Z | sn111 commit touches scoring: Add validator cost profile |
| `sn54:scoring_commit:2026-08-12T17:46:40Z` | 54 | SCORING_COMMIT | 2026-08-12T18:40:47Z | sn54 commit touches scoring: update miner screen reply readme |
| `sn41:scoring_commit:2026-08-12T22:36:16Z` | 41 | SCORING_COMMIT | 2026-08-12T22:57:11Z | sn41 commit touches scoring: Merge pull request #42 from corvxai/mkt_scoring_v2 |
| `sn51:release:executor-v1.118` | 51 | RELEASE | 2026-08-13T02:42:09Z | sn51 released executor-v1.118 |
| `sn66:scoring_commit:2026-08-13T00:05:35Z` | 66 | SCORING_COMMIT | 2026-08-13T02:42:09Z | sn66 commit touches scoring: Preserve production task retirements |
| `sn89:scoring_commit:2026-08-13T02:13:14Z` | 89 | SCORING_COMMIT | 2026-08-13T02:42:09Z | sn89 commit touches scoring: HF: submission-diversity gate — zero weight for one-sided miners on a… |
| `sn89:scoring_commit:2026-08-13T03:41:31Z` | 89 | SCORING_COMMIT | 2026-08-13T04:32:20Z | sn89 commit touches scoring: HF: measure miner behaviour above the board filter, not below it |
| `sn44:scoring_commit:2026-08-13T09:12:05Z` | 44 | SCORING_COMMIT | 2026-08-13T09:22:53Z | sn44 commit touches scoring: blacklist + min common challenges tiebreak |
| `sn67:scoring_commit:2026-08-13T09:35:16Z` | 67 | SCORING_COMMIT | 2026-08-13T10:35:49Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20260813.post3 |
| `sn1:release:v4.3.1` | 1 | RELEASE | 2026-08-13T14:10:36Z | sn1 released v4.3.1 |
| `sn26:scoring_commit:2026-08-13T14:58:07Z` | 26 | SCORING_COMMIT | 2026-08-13T15:31:13Z | sn26 commit touches scoring: Merge pull request #49 from 0xsigurd/feat/image-hash-verification |
| `sn51:release:executor-v1.119` | 51 | RELEASE | 2026-08-13T15:31:13Z | sn51 released executor-v1.119 |
| `sn75:scoring_commit:2026-08-13T13:14:25Z` | 75 | SCORING_COMMIT | 2026-08-13T15:31:13Z | sn75 commit touches scoring: updated validator weights submitter |
| `sn100:scoring_commit:2026-08-13T15:17:24Z` | 100 | SCORING_COMMIT | 2026-08-13T15:31:13Z | sn100 commit touches scoring: fix(site): attribute arena weight per challenge, not global burn (#142 |
| `sn38:scoring_commit:2026-08-13T16:30:43Z` | 38 | SCORING_COMMIT | 2026-08-13T16:39:08Z | sn38 commit touches scoring: Update validator image to latest version in docker-compose files |
| `sn90:release:v1.1.0 — Targon max $/card + raised GPU ` | 90 | RELEASE | 2026-08-13T16:39:08Z | sn90 released v1.1.0 — Targon max $/card + raised GPU card caps |
| `sn90:scoring_commit:2026-08-13T15:50:20Z` | 90 | SCORING_COMMIT | 2026-08-13T16:39:08Z | sn90 commit touches scoring: chore(validator): bump version to 1.1.0 for Watchtower v1 track |
| `sn15:scoring_commit:2026-08-13T21:50:38Z` | 15 | SCORING_COMMIT | 2026-08-13T22:10:33Z | sn15 commit touches scoring: chore(deps): bump msgpack from 1.1.2 to 1.2.1 in /docker/validator (#… |
| `sn91:scoring_commit:2026-08-13T21:52:49Z` | 91 | SCORING_COMMIT | 2026-08-13T22:10:33Z | sn91 commit touches scoring: miner dashboard: show warm-start init + next-round scheduled checkpoin |
| `sn91:scoring_commit:2026-08-13T23:06:33Z` | 91 | SCORING_COMMIT | 2026-08-13T23:12:08Z | sn91 commit touches scoring: miner dashboard: label warm-start checkpoints with their origin round… |
| `sn90:release:v1.1.1` | 90 | RELEASE | 2026-08-14T06:06:21Z | sn90 released v1.1.1 |
| `sn90:scoring_commit:2026-08-14T06:04:45Z` | 90 | SCORING_COMMIT | 2026-08-14T06:06:21Z | sn90 commit touches scoring: fix(validator): always apply the Targon supply-side clamp |
| `sn100:scoring_commit:2026-08-14T04:35:53Z` | 100 | SCORING_COMMIT | 2026-08-14T06:06:21Z | sn100 commit touches scoring: chore(deploy): promote prod prism-challenge pin for seal TTL fix (#147 |
| `sn44:scoring_commit:2026-08-14T08:54:31Z` | 44 | SCORING_COMMIT | 2026-08-14T09:18:19Z | sn44 commit touches scoring: Merge pull request #52 from score-technologies/tiebreak-enh-exploratio |
| `sn51:scoring_commit:2026-08-14T08:19:45Z` | 51 | SCORING_COMMIT | 2026-08-14T09:18:19Z | sn51 commit touches scoring: DAH-2622: floor a live miner's weight at one u16 unit funded from bur… |
| `sn100:scoring_commit:2026-08-14T08:35:14Z` | 100 | SCORING_COMMIT | 2026-08-14T09:18:19Z | sn100 commit touches scoring: chore(deploy): promote prod prism-challenge pin for METRICS harvest f… |
| `sn67:scoring_commit:2026-08-14T09:41:41Z` | 67 | SCORING_COMMIT | 2026-08-14T11:32:26Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20260814.post1 |
| `sn71:scoring_commit:2026-08-14T10:35:32Z` | 71 | SCORING_COMMIT | 2026-08-14T11:32:26Z | sn71 commit touches scoring: Refresh SOURCE_ADD reward ancestry identity |
| `sn96:release:Verathos v0.1.38 — Runtime and Proof Sta` | 96 | RELEASE | 2026-08-14T11:32:26Z | sn96 released Verathos v0.1.38 — Runtime and Proof Stability |
| `sn96:scoring_commit:2026-08-14T09:27:09Z` | 96 | SCORING_COMMIT | 2026-08-14T11:32:26Z | sn96 commit touches scoring: fix: retry validator updates after partial install |
| `sn97:scoring_commit:2026-08-14T08:09:05Z` | 97 | SCORING_COMMIT | 2026-08-14T11:32:26Z | sn97 commit touches scoring: feat: win both evaluations; increase step amount; question amount reb… |
| `sn90:release:v1.1.2` | 90 | RELEASE | 2026-08-14T12:30:02Z | sn90 released v1.1.2 |
| `sn90:scoring_commit:2026-08-14T12:09:55Z` | 90 | SCORING_COMMIT | 2026-08-14T12:30:02Z | sn90 commit touches scoring: fix(validator): set_weights on the configured subtensor endpoint |
| `sn96:release:Verathos v0.1.39 — Hard-Proof Timing Sta` | 96 | RELEASE | 2026-08-14T15:05:31Z | sn96 released Verathos v0.1.39 — Hard-Proof Timing Stability |
| `sn126:scoring_commit:2026-08-14T15:41:49Z` | 126 | SCORING_COMMIT | 2026-08-14T16:03:52Z | sn126 commit touches scoring: docs: describe continuous miner training tables |
| `sn55:scoring_commit:2026-08-14T16:37:31Z` | 55 | SCORING_COMMIT | 2026-08-14T17:08:05Z | sn55 commit touches scoring: print only valid scores |
| `sn55:scoring_commit:2026-08-14T17:58:40Z` | 55 | SCORING_COMMIT | 2026-08-14T18:24:30Z | sn55 commit touches scoring: print only valid scores |
| `sn100:scoring_commit:2026-08-14T17:13:42Z` | 100 | SCORING_COMMIT | 2026-08-14T18:24:30Z | sn100 commit touches scoring: chore(deploy): promote prod prism-challenge pin for BYOK seal keep (#… |
| `sn55:scoring_commit:2026-08-14T20:02:57Z` | 55 | SCORING_COMMIT | 2026-08-14T20:17:06Z | sn55 commit touches scoring: commit weights after validation |
| `sn96:release:Verathos v0.1.40 — Capacity Audit Schedu` | 96 | RELEASE | 2026-08-14T20:17:06Z | sn96 released Verathos v0.1.40 — Capacity Audit Scheduling Stability |
| `sn62:release:v0.2.7` | 62 | RELEASE | 2026-08-14T22:36:36Z | sn62 released v0.2.7 |
| `sn71:scoring_commit:2026-08-15T00:32:31Z` | 71 | SCORING_COMMIT | 2026-08-15T01:47:28Z | sn71 commit touches scoring: Keep private ICP scores out of telemetry |
| `sn100:scoring_commit:2026-08-15T02:46:25Z` | 100 | SCORING_COMMIT | 2026-08-15T03:25:28Z | sn100 commit touches scoring: chore(deploy): promote prod prism-challenge pin for G8 µP probe base … |
| `sn71:scoring_commit:2026-08-15T03:59:05Z` | 71 | SCORING_COMMIT | 2026-08-15T04:05:09Z | sn71 commit touches scoring: Provision hotkey verification in gateway enclaves |
| `sn108:scoring_commit:2026-08-15T04:00:22Z` | 108 | SCORING_COMMIT | 2026-08-15T04:05:09Z | sn108 commit touches scoring: feat(registry): require every evaluated chute to live in the promethe… |
| `sn67:scoring_commit:2026-08-14T10:52:59Z` | 67 | SCORING_COMMIT | 2026-08-15T04:45:10Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20260814.post2 |
| `sn67:scoring_commit:2026-08-15T08:24:59Z` | 67 | SCORING_COMMIT | 2026-08-15T09:06:33Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20260815.post1 |
| `sn100:scoring_commit:2026-08-15T12:26:39Z` | 100 | SCORING_COMMIT | 2026-08-15T12:56:35Z | sn100 commit touches scoring: feat(prism): live leaf from G2 benchmarks (scoring_version 4) (#160) |
| `sn100:scoring_commit:2026-08-15T13:20:08Z` | 100 | SCORING_COMMIT | 2026-08-15T13:39:18Z | sn100 commit touches scoring: fix(prism): rename lattice_score to satisfy clippy similar_names |
| `sn76:scoring_commit:2026-08-15T17:47:00Z` | 76 | SCORING_COMMIT | 2026-08-15T17:59:54Z | sn76 commit touches scoring: Add a local evaluation command |
| `sn108:scoring_commit:2026-08-15T20:13:27Z` | 108 | SCORING_COMMIT | 2026-08-15T20:35:26Z | sn108 commit touches scoring: docs(miner): drop the second artefact that was never built |
| `sn76:scoring_commit:2026-08-15T23:00:47Z` | 76 | SCORING_COMMIT | 2026-08-15T23:01:41Z | sn76 commit touches scoring: Raise tasks per round across all four tracks |
| `sn71:scoring_commit:2026-08-15T21:01:49Z` | 71 | SCORING_COMMIT | 2026-08-16T01:55:21Z | sn71 commit touches scoring: Fix validator RPC boundary fixture |
| `sn111:scoring_commit:2026-08-16T00:43:24Z` | 111 | SCORING_COMMIT | 2026-08-16T01:55:21Z | sn111 commit touches scoring: Implement resilient batch scoring and winner-takes-most payouts |
| `sn71:scoring_commit:2026-08-16T03:33:59Z` | 71 | SCORING_COMMIT | 2026-08-16T04:08:02Z | sn71 commit touches scoring: Regenerate validator protected workflow manifest |
| `sn67:scoring_commit:2026-08-16T05:46:07Z` | 67 | SCORING_COMMIT | 2026-08-16T06:04:05Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20260816.post0 |
| `sn71:scoring_commit:2026-08-16T04:12:13Z` | 71 | SCORING_COMMIT | 2026-08-16T06:04:05Z | sn71 commit touches scoring: Preserve production clocks in parity validation |
| `sn76:scoring_commit:2026-08-16T07:37:40Z` | 76 | SCORING_COMMIT | 2026-08-16T07:41:32Z | sn76 commit touches scoring: Match CWEs numerically, draw tasks per validator, break ties determin… |
| `sn100:release:v3.3.22` | 100 | RELEASE | 2026-08-16T08:44:18Z | sn100 released v3.3.22 |
| `sn76:scoring_commit:2026-08-16T11:49:10Z` | 76 | SCORING_COMMIT | 2026-08-16T12:00:10Z | sn76 commit touches scoring: Download only the tasks a validator drew |
| `sn68:scoring_commit:2026-08-16T13:01:09Z` | 68 | SCORING_COMMIT | 2026-08-16T13:40:28Z | sn68 commit touches scoring: discard individual validator processing failures before averaging scor |
| `sn100:release:v3.3.23` | 100 | RELEASE | 2026-08-16T16:00:34Z | sn100 released v3.3.23 |
| `sn75:scoring_commit:2026-08-16T16:01:02Z` | 75 | SCORING_COMMIT | 2026-08-16T16:38:36Z | sn75 commit touches scoring: Merge pull request #49 from thenervelab/feat/compute-scoring-runtime |
| `sn85:scoring_commit:2026-08-16T16:50:58Z` | 85 | SCORING_COMMIT | 2026-08-16T17:03:28Z | sn85 commit touches scoring: retry inviting rejected miner UIDs in competition enrollment due to l… |
| `sn100:release:v3.3.24` | 100 | RELEASE | 2026-08-16T17:31:56Z | sn100 released v3.3.24 |
| `sn71:scoring_commit:2026-08-16T23:14:51Z` | 71 | SCORING_COMMIT | 2026-08-17T01:52:42Z | sn71 commit touches scoring: Bound validator worker startup verification |
| `sn71:scoring_commit:2026-08-17T00:26:35Z` | 71 | SCORING_COMMIT | 2026-08-17T06:00:04Z | sn71 commit touches scoring: Refresh provider failures during recovery scoring |
| `sn51:release:executor-v1.120` | 51 | RELEASE | 2026-08-17T08:07:06Z | sn51 released executor-v1.120 |
| `sn75:scoring_commit:2026-08-16T20:57:11Z` | 75 | SCORING_COMMIT | 2026-08-17T08:07:06Z | sn75 commit touches scoring: feat(compute-scoring): root-settable dedicated key for vali submission |
| `sn85:scoring_commit:2026-08-17T08:37:37Z` | 85 | SCORING_COMMIT | 2026-08-17T08:59:45Z | sn85 commit touches scoring: reinvite miners rejected with flag INVITATION_DECLINED in comp enroll… |
| `sn10:scoring_commit:2026-08-17T09:07:35Z` | 10 | SCORING_COMMIT | 2026-08-17T09:54:33Z | sn10 commit touches scoring: feat(bench): score the full workload trace (PAR-65) (#81) |
| `sn67:scoring_commit:2026-08-17T05:33:14Z` | 67 | SCORING_COMMIT | 2026-08-17T10:46:02Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20260817.post0 |
| `sn85:scoring_commit:2026-08-17T10:23:08Z` | 85 | SCORING_COMMIT | 2026-08-17T10:46:02Z | sn85 commit touches scoring: ensure comp scoring worker can access Modal SDK for fetching Modal vo… |
| `sn114:scoring_commit:2026-08-17T09:54:21Z` | 114 | SCORING_COMMIT | 2026-08-17T10:46:02Z | sn114 commit touches scoring: perf(validator): reduce validator write contention |
| `sn85:scoring_commit:2026-08-17T10:59:02Z` | 85 | SCORING_COMMIT | 2026-08-17T11:12:02Z | sn85 commit touches scoring: treat miner sandbox raised error as miner issue rather than validator… |
| `sn111:scoring_commit:2026-08-17T11:55:09Z` | 111 | SCORING_COMMIT | 2026-08-17T13:03:27Z | sn111 commit touches scoring: feat: add adaptive miner selection and run assignment snapshots |
| `sn114:scoring_commit:2026-08-17T12:09:26Z` | 114 | SCORING_COMMIT | 2026-08-17T13:03:27Z | sn114 commit touches scoring: hotfix(scoring): exclude comp 112 stage 2 from final score |
| `sn10:scoring_commit:2026-08-17T16:31:51Z` | 10 | SCORING_COMMIT | 2026-08-17T16:41:40Z | sn10 commit touches scoring: feat: better miner commit patch logs (#83) |
| `sn21:release:SN21 training bundle (1977 records, refr` | 21 | RELEASE | 2026-08-17T18:54:41Z | sn21 released SN21 training bundle (1977 records, refreshed 2026-08-17 18:05 UTC) |
| `sn51:release:executor-v1.121` | 51 | RELEASE | 2026-08-17T19:36:49Z | sn51 released executor-v1.121 |
| `sn65:scoring_commit:2026-08-14T10:47:05Z` | 65 | SCORING_COMMIT | 2026-08-17T19:36:49Z | sn65 commit touches scoring: Merge pull request #3 from taofu-labs/validator-v2 |
| `sn21:release:SN21 training bundle — 10,791 records, r` | 21 | RELEASE | 2026-08-17T21:09:19Z | sn21 released SN21 training bundle — 10,791 records, refreshed 2026-08-17 |
| `sn54:scoring_commit:2026-08-17T16:25:21Z` | 54 | SCORING_COMMIT | 2026-08-17T22:36:59Z | sn54 commit touches scoring: updating miner info |
| `sn62:release:v0.2.8` | 62 | RELEASE | 2026-08-17T22:36:59Z | sn62 released v0.2.8 |
| `sn14:release:v2-finite-debt-preextraction: Pre-extrac` | 14 | RELEASE | 2026-08-17T23:02:57Z | sn14 released v2-finite-debt-preextraction: Pre-extraction snapshot of the inactive V2 finite-debt economics. |
| `sn56:scoring_commit:2026-08-17T23:44:09Z` | 56 | SCORING_COMMIT | 2026-08-18T00:01:21Z | sn56 commit touches scoring: Fix re-finalize crowning the re-evaluated miner instead of re-ranking… |
| `sn71:scoring_commit:2026-08-18T01:01:27Z` | 71 | SCORING_COMMIT | 2026-08-18T01:47:42Z | sn71 commit touches scoring: Repair semantic gate verification fixtures |
| `sn15:release:v1.2.7` | 15 | RELEASE | 2026-08-18T02:44:45Z | sn15 released v1.2.7 |
| `sn91:release:pre-decay-wsd-contract` | 91 | RELEASE | 2026-08-18T04:21:04Z | sn91 released pre-decay-wsd-contract |
| `sn91:scoring_commit:2026-08-15T10:55:48Z` | 91 | SCORING_COMMIT | 2026-08-18T04:21:04Z | sn91 commit touches scoring: audit fixes + miner CLI: warm-start init visibility in `cascade heat` |
| `sn85:scoring_commit:2026-08-18T06:57:35Z` | 85 | SCORING_COMMIT | 2026-08-18T07:14:18Z | sn85 commit touches scoring: debug VBR scoring in compression competitions (#196) |
| `sn89:scoring_commit:2026-08-18T07:04:57Z` | 89 | SCORING_COMMIT | 2026-08-18T07:14:18Z | sn89 commit touches scoring: hf board: keep a re-rolled miner's retired hotkey attributed to its o… |
| `sn51:scoring_commit:2026-08-18T08:26:35Z` | 51 | SCORING_COMMIT | 2026-08-18T08:51:13Z | sn51 commit touches scoring: DAH-2702: verify GPU persistence mode after -pm 1 in the power cap (#… |
| `sn67:scoring_commit:2026-08-18T06:10:26Z` | 67 | SCORING_COMMIT | 2026-08-18T09:46:16Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20260818.post0 |
| `sn65:scoring_commit:2026-08-18T10:41:48Z` | 65 | SCORING_COMMIT | 2026-08-18T10:55:56Z | sn65 commit touches scoring: Merge pull request #4 from taofu-labs/docs/validator |
| `sn67:scoring_commit:2026-08-18T10:35:47Z` | 67 | SCORING_COMMIT | 2026-08-18T10:55:56Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20260818.post1 |
| `sn81:scoring_commit:2026-08-18T07:52:08Z` | 81 | SCORING_COMMIT | 2026-08-18T13:55:30Z | sn81 commit touches scoring: test: lock v4 canonical reward flow |
| `sn108:scoring_commit:2026-08-18T13:35:17Z` | 108 | SCORING_COMMIT | 2026-08-18T13:55:30Z | sn108 commit touches scoring: Docs: the eligible-miner gate is 50 active members, not 500 |
| `sn1:release:v4.3.3` | 1 | RELEASE | 2026-08-18T14:48:11Z | sn1 released v4.3.3 |
| `sn23:scoring_commit:2026-08-18T14:09:05Z` | 23 | SCORING_COMMIT | 2026-08-18T14:48:11Z | sn23 commit touches scoring: Merge pull request #47 from TrishoolAI/feat/challenge-creation |
| `sn28:release:v0.4.5` | 28 | RELEASE | 2026-08-18T14:48:11Z | sn28 released v0.4.5 |
| `sn28:scoring_commit:2026-08-18T14:43:57Z` | 28 | SCORING_COMMIT | 2026-08-18T14:48:11Z | sn28 commit touches scoring: Release gm-miner v0.4.5 |
| `sn33:scoring_commit:2026-08-18T14:35:53Z` | 33 | SCORING_COMMIT | 2026-08-18T14:48:11Z | sn33 commit touches scoring: Merge pull request #135 from afterpartyai/Feat-Add-Skills-Cov-task |
| `sn53:scoring_commit:2026-08-18T15:05:58Z` | 53 | SCORING_COMMIT | 2026-08-18T15:42:54Z | sn53 commit touches scoring: miner: tee_miner, a pure gateway leg with provider-assigned identity … |
| `sn108:scoring_commit:2026-08-18T14:52:43Z` | 108 | SCORING_COMMIT | 2026-08-18T15:42:54Z | sn108 commit touches scoring: Burn 60% of miner emission, split the other 40% by score |
| `sn96:release:Verathos v0.1.41 - Bounded Replay and Ru` | 96 | RELEASE | 2026-08-18T16:12:17Z | sn96 released Verathos v0.1.41 - Bounded Replay and Runtime Stability |
| `sn96:scoring_commit:2026-08-18T12:39:12Z` | 96 | SCORING_COMMIT | 2026-08-18T16:12:17Z | sn96 commit touches scoring: fix: prevent validator-created audit overlap |
| `sn21:scoring_commit:2026-08-18T16:03:58Z` | 21 | SCORING_COMMIT | 2026-08-18T16:57:50Z | sn21 commit touches scoring: validator: daily-stream override was silently dropping every miner (s… |
| `sn92:scoring_commit:2026-08-18T12:27:47Z` | 92 | SCORING_COMMIT | 2026-08-18T16:57:50Z | sn92 commit touches scoring: Correct the loopback sample output in the validator guide |
| `sn21:scoring_commit:2026-08-18T17:28:33Z` | 21 | SCORING_COMMIT | 2026-08-18T17:39:02Z | sn21 commit touches scoring: validator: daily-stream API path crashed on unbound _vol after the ss… |
| `sn25:release:v2026.8.17-1021635350` | 25 | RELEASE | 2026-08-18T17:39:02Z | sn25 released v2026.8.17-1021635350 |
| `sn25:scoring_commit:2026-08-04T21:03:12Z` | 25 | SCORING_COMMIT | 2026-08-18T17:39:02Z | sn25 commit touches scoring: Merge pull request #3 from Ryanmello07/fix/windows-miner-exe-suffix-u… |
| `sn28:readme_task_diff:50edab7d2bab95b4` | 28 | README_TASK_DIFF | 2026-08-12T12:34:56Z | sn28 README task/scoring sections changed |
| `sn126:readme_task_diff:8ff67deb6bfb1a47` | 126 | README_TASK_DIFF | 2026-08-12T14:09:20Z | sn126 README task/scoring sections changed |
| `sn66:readme_task_diff:371ffea333df26ac` | 66 | README_TASK_DIFF | 2026-08-12T23:55:02Z | sn66 README task/scoring sections changed |
| `sn66:readme_task_diff:59994c37a3ef19e9` | 66 | README_TASK_DIFF | 2026-08-13T02:42:09Z | sn66 README task/scoring sections changed |
| `sn89:readme_task_diff:32958de49be3add2` | 89 | README_TASK_DIFF | 2026-08-13T02:42:09Z | sn89 README task/scoring sections changed |
| `sn67:readme_task_diff:a54328c7fbaf2606` | 67 | README_TASK_DIFF | 2026-08-13T10:35:49Z | sn67 README task/scoring sections changed |
| `sn90:readme_task_diff:8fca31852ef23b0f` | 90 | README_TASK_DIFF | 2026-08-13T12:36:13Z | sn90 README task/scoring sections changed |
| `sn26:readme_task_diff:27b06992db454b8d` | 26 | README_TASK_DIFF | 2026-08-13T15:31:13Z | sn26 README task/scoring sections changed |
| `sn38:readme_task_diff:0929297366a7bf8b` | 38 | README_TASK_DIFF | 2026-08-13T16:39:08Z | sn38 README task/scoring sections changed |
| `sn55:readme_task_diff:d7f3a333f8affc99` | 55 | README_TASK_DIFF | 2026-08-14T14:04:14Z | sn55 README task/scoring sections changed |
| `sn121:readme_task_diff:4de589f5fb4cb70d` | 121 | README_TASK_DIFF | 2026-08-14T19:29:32Z | sn121 README task/scoring sections changed |
| `sn67:readme_task_diff:5a8da0f3ba283771` | 67 | README_TASK_DIFF | 2026-08-15T09:06:33Z | sn67 README task/scoring sections changed |
| `sn123:readme_task_diff:6532d2da519e8960` | 123 | README_TASK_DIFF | 2026-08-17T17:55:33Z | sn123 README task/scoring sections changed |
| `sn91:readme_task_diff:465231d881190999` | 91 | README_TASK_DIFF | 2026-08-18T05:02:26Z | sn91 README task/scoring sections changed |
| `sn10:readme_task_diff:126d4086680182f3` | 10 | README_TASK_DIFF | 2026-08-18T12:04:33Z | sn10 README task/scoring sections changed |
| `sn108:readme_task_diff:19f7089d5cc9e961` | 108 | README_TASK_DIFF | 2026-08-18T13:55:30Z | sn108 README task/scoring sections changed |
| `sn33:readme_task_diff:a91e45ad8067f8f2` | 33 | README_TASK_DIFF | 2026-08-18T14:48:11Z | sn33 README task/scoring sections changed |
| `sn92:readme_task_diff:c2e913dd2e41d4bb` | 92 | README_TASK_DIFF | 2026-08-18T16:57:50Z | sn92 README task/scoring sections changed |
| `sn25:readme_task_diff:1a67cd5991549ed6` | 25 | README_TASK_DIFF | 2026-08-18T17:39:02Z | sn25 README task/scoring sections changed |
| `sn108:readme_task_diff:440d4dcceb14f6b4` | 108 | README_TASK_DIFF | 2026-08-18T17:39:02Z | sn108 README task/scoring sections changed |

## RESOLVED IN THIS WINDOW

_none_
