# ALARMS - generated 2026-10-13T01:39:03Z, block 9271077

window: first_seen in [2026-10-13T00:24:30Z, 2026-10-13T01:39:30Z)  (60 min interval + 15 min overlap)

Report ONLY the rows under NEW SINCE LAST RUN. Rows under STILL OPEN were
already reported in an earlier window and must not be re-alarmed.

## NEW SINCE LAST RUN

| event_id | netuid | class | severity | first_seen_utc | one_line |
|---|---|---|---|---|---|
| `sn28:release:v0.4.28` | 28 | RELEASE | P1 | 2026-10-13T01:39:30Z | sn28 released v0.4.28 |
| `sn28:scoring_commit:2026-10-12T21:12:43Z` | 28 | SCORING_COMMIT | P1 | 2026-10-13T01:39:30Z | sn28 commit touches scoring: chore(release): promote gm-miner 0.4.28 (#317) |
| `sn71:scoring_commit:2026-10-12T22:46:22Z` | 71 | SCORING_COMMIT | P1 | 2026-10-13T01:39:30Z | sn71 commit touches scoring: Finish validated bounded evidence reviews without time-only failure |
| `sn74:release:release-20261012-224627` | 74 | RELEASE | P1 | 2026-10-13T01:39:30Z | sn74 released release-20261012-224627 |
| `sn74:scoring_commit:2026-10-12T22:45:40Z` | 74 | SCORING_COMMIT | P1 | 2026-10-13T01:39:30Z | sn74 commit touches scoring: chore(weights): burn all miner emissions (empty registry, compute sha… |
| `sn117:release:everycli v0.3.8` | 117 | RELEASE | P1 | 2026-10-13T01:39:30Z | sn117 released everycli v0.3.8 |

### detail

- **`sn28:release:v0.4.28`** - sn28 released v0.4.28
  - published 2026-10-12T21:28:21Z (was v0.4.27)
- **`sn28:scoring_commit:2026-10-12T21:12:43Z`** - sn28 commit touches scoring: chore(release): promote gm-miner 0.4.28 (#317)
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn71:scoring_commit:2026-10-12T22:46:22Z`** - sn71 commit touches scoring: Finish validated bounded evidence reviews without time-only failure
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn74:release:release-20261012-224627`** - sn74 released release-20261012-224627
  - published 2026-10-12T22:45:40Z (was release-20261002-144641)
- **`sn74:scoring_commit:2026-10-12T22:45:40Z`** - sn74 commit touches scoring: chore(weights): burn all miner emissions (empty registry, compute sha…
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn117:release:everycli v0.3.8`** - sn117 released everycli v0.3.8
  - published 2026-10-13T00:53:06Z (was everycli v0.3.7)

## STILL OPEN (already reported - do not re-alarm)

| event_id | netuid | class | first_seen_utc | one_line |
|---|---|---|---|---|
| `sn108:burn_drop:0.900` | 108 | BURN_DROP | 2026-10-06T19:07:57Z | sn108 burn fell 1.000 -> 0.900 - miners can earn again |
| `sn10:burn_drop:0.902` | 10 | BURN_DROP | 2026-10-06T23:03:41Z | sn10 burn fell 1.000 -> 0.902 - miners can earn again |
| `sn37:burn_drop:0.978` | 37 | BURN_DROP | 2026-10-07T16:23:49Z | sn37 burn fell 1.000 -> 0.978 - miners can earn again |
| `sn25:burn_drop:0.000` | 25 | BURN_DROP | 2026-10-08T07:46:34Z | sn25 burn fell 1.000 -> 0.000 - miners can earn again |
| `sn37:burn_drop:0.000` | 37 | BURN_DROP | 2026-10-09T00:42:20Z | sn37 burn fell 1.000 -> 0.000 - miners can earn again |
| `sn104:mechanism_added:1to2` | 104 | MECHANISM_ADDED | 2026-10-09T19:37:09Z | sn104 now runs 2 incentive mechanisms (was 1) |
| `sn108:burn_drop:0.902` | 108 | BURN_DROP | 2026-10-11T19:38:20Z | sn108 burn fell 1.000 -> 0.902 - miners can earn again |
| `sn30:burn_drop:0.984` | 30 | BURN_DROP | 2026-10-12T02:34:00Z | sn30 burn fell 0.997 -> 0.984 - miners can earn again |
| `sn122:burn_drop:0.100` | 122 | BURN_DROP | 2026-10-12T09:49:01Z | sn122 burn fell 1.000 -> 0.100 - miners can earn again |
| `sn12:mechanism_added:1to2` | 12 | MECHANISM_ADDED | 2026-10-12T19:47:00Z | sn12 now runs 2 incentive mechanisms (was 1) |
| `sn58:burn_drop:0.833` | 58 | BURN_DROP | 2026-10-12T19:47:00Z | sn58 burn fell 1.000 -> 0.833 - miners can earn again |
| `sn25:scoring_commit:2026-10-06T02:25:10Z` | 25 | SCORING_COMMIT | 2026-10-06T06:43:00Z | sn25 commit touches scoring: Merge bounded early miner recovery diagnostics |
| `sn37:scoring_commit:2026-10-06T02:41:33Z` | 37 | SCORING_COMMIT | 2026-10-06T06:43:00Z | sn37 commit touches scoring: feat(validator)!: default-off master switch VALIDATOR_ENABLED (#26) |
| `sn67:scoring_commit:2026-10-06T05:02:36Z` | 67 | SCORING_COMMIT | 2026-10-06T06:43:00Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20261006.post1 |
| `sn71:scoring_commit:2026-10-06T05:47:00Z` | 71 | SCORING_COMMIT | 2026-10-06T06:43:00Z | sn71 commit touches scoring: Verify round diagnostics preserve recovery and failures |
| `sn116:scoring_commit:2026-10-06T03:58:21Z` | 116 | SCORING_COMMIT | 2026-10-06T06:43:00Z | sn116 commit touches scoring: Merge pull request #674 from carbonphysicsai/claude/battery-score-tun… |
| `sn120:scoring_commit:2026-10-06T06:04:01Z` | 120 | SCORING_COMMIT | 2026-10-06T06:43:00Z | sn120 commit touches scoring: feat: opt into bounded single owned verifier checkpoint reuse |
| `sn9:release:v4.13.5` | 9 | RELEASE | 2026-10-06T13:39:56Z | sn9 released v4.13.5 |
| `sn51:scoring_commit:2026-10-06T12:42:30Z` | 51 | SCORING_COMMIT | 2026-10-06T13:39:56Z | sn51 commit touches scoring: DAH-3980 - validator: start the host probes at SSH connect and restor… |
| `sn67:scoring_commit:2026-10-06T07:52:50Z` | 67 | SCORING_COMMIT | 2026-10-06T13:39:56Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20261006.post3 |
| `sn108:scoring_commit:2026-10-06T11:47:46Z` | 108 | SCORING_COMMIT | 2026-10-06T13:39:56Z | sn108 commit touches scoring: Minimum improvement comes from the challenge server (/validator/sync … |
| `sn116:scoring_commit:2026-10-06T13:03:10Z` | 116 | SCORING_COMMIT | 2026-10-06T13:39:56Z | sn116 commit touches scoring: Merge pull request #679 from carbonphysicsai/claude/validator-13d-l1-… |
| `sn120:scoring_commit:2026-10-06T12:39:56Z` | 120 | SCORING_COMMIT | 2026-10-06T13:39:56Z | sn120 commit touches scoring: Document actual E24 learning and partial verifier capacity rollout |
| `sn10:scoring_commit:2026-10-06T15:02:05Z` | 10 | SCORING_COMMIT | 2026-10-06T19:07:57Z | sn10 commit touches scoring: feat(ops): add private PRO6000 FP8 campaign with v5 C4 scoring (#188) |
| `sn21:scoring_commit:2026-10-06T14:07:59Z` | 21 | SCORING_COMMIT | 2026-10-06T19:07:57Z | sn21 commit touches scoring: fix(validator): /health in daily mode no longer echoes the loaded rel… |
| `sn28:release:v0.4.26` | 28 | RELEASE | 2026-10-06T19:07:57Z | sn28 released v0.4.26 |
| `sn50:scoring_commit:2026-10-06T15:38:51Z` | 50 | SCORING_COMMIT | 2026-10-06T19:07:57Z | sn50 commit touches scoring: perf(validator): write predictions to Bigtable from the dendrite work… |
| `sn51:scoring_commit:2026-10-06T14:05:39Z` | 51 | SCORING_COMMIT | 2026-10-06T19:07:57Z | sn51 commit touches scoring: DAH-3947 - [P2] lium-io drops celium-collateral; miner reclaims with … |
| `sn71:scoring_commit:2026-10-06T17:48:44Z` | 71 | SCORING_COMMIT | 2026-10-06T19:07:57Z | sn71 commit touches scoring: Merge PR #238: retain validated company evidence |
| `sn76:scoring_commit:2026-10-06T16:30:48Z` | 76 | SCORING_COMMIT | 2026-10-06T19:07:57Z | sn76 commit touches scoring: ormas-miner CLI and user-only installer (#25) |
| `sn78:scoring_commit:2026-10-06T14:55:05Z` | 78 | SCORING_COMMIT | 2026-10-06T19:07:57Z | sn78 commit touches scoring: Match miner scoring runtime pins and diagnose admission holds |
| `sn111:scoring_commit:2026-10-06T14:44:24Z` | 111 | SCORING_COMMIT | 2026-10-06T19:07:57Z | sn111 commit touches scoring: fix(validator): scope split audit repairs to expected draft units |
| `sn114:scoring_commit:2026-10-01T14:32:15Z` | 114 | SCORING_COMMIT | 2026-10-06T19:07:57Z | sn114 commit touches scoring: feat(scoring): count jev input tokens in miner weighted tokens |
| `sn116:scoring_commit:2026-10-06T19:02:44Z` | 116 | SCORING_COMMIT | 2026-10-06T19:07:57Z | sn116 commit touches scoring: Merge pull request #708 from carbonphysicsai/claude/validator-19-s4-a… |
| `sn120:scoring_commit:2026-10-06T17:07:55Z` | 120 | SCORING_COMMIT | 2026-10-06T19:07:57Z | sn120 commit touches scoring: Calculate hourly current miner weights with six-hour contribution EMA |
| `sn25:release:v2026.10.6-1065229510` | 25 | RELEASE | 2026-10-06T23:03:41Z | sn25 released v2026.10.6-1065229510 |
| `sn25:scoring_commit:2026-10-06T22:10:55Z` | 25 | SCORING_COMMIT | 2026-10-06T23:03:41Z | sn25 commit touches scoring: Merge feat/operator-discovery-miner into feat/operator-discovery |
| `sn71:scoring_commit:2026-10-06T22:49:48Z` | 71 | SCORING_COMMIT | 2026-10-06T23:03:41Z | sn71 commit touches scoring: Prove dynamic Deepline tools through baseline and miner publication |
| `sn78:scoring_commit:2026-10-06T20:23:37Z` | 78 | SCORING_COMMIT | 2026-10-06T23:03:41Z | sn78 commit touches scoring: Reduce intake seal contention and isolate upgraded miner imports (#230 |
| `sn111:scoring_commit:2026-10-06T21:03:45Z` | 111 | SCORING_COMMIT | 2026-10-06T23:03:41Z | sn111 commit touches scoring: feat(validator): default miner burn to 90 percent |
| `sn116:release:worker-images-v1` | 116 | RELEASE | 2026-10-06T23:03:41Z | sn116 released worker-images-v1 |
| `sn116:scoring_commit:2026-10-06T21:40:29Z` | 116 | SCORING_COMMIT | 2026-10-06T23:03:41Z | sn116 commit touches scoring: Fix main: rank the hidden-pool score variant per device class |
| `sn120:scoring_commit:2026-10-06T22:39:33Z` | 120 | SCORING_COMMIT | 2026-10-06T23:03:41Z | sn120 commit touches scoring: Admit exact ROOT-pinned retired verifier terminal reports |
| `sn5:scoring_commit:2026-10-06T23:26:54Z` | 5 | SCORING_COMMIT | 2026-10-07T02:19:32Z | sn5 commit touches scoring: Merge pull request #18 from hone-subnet-org/score-window-100 |
| `sn25:release:v2026.10.6-1065359600` | 25 | RELEASE | 2026-10-07T02:19:32Z | sn25 released v2026.10.6-1065359600 |
| `sn25:scoring_commit:2026-10-06T23:47:29Z` | 25 | SCORING_COMMIT | 2026-10-07T02:19:32Z | sn25 commit touches scoring: Merge feat/operator-discovery-validator |
| `sn71:scoring_commit:2026-10-07T01:32:36Z` | 71 | SCORING_COMMIT | 2026-10-07T02:19:32Z | sn71 commit touches scoring: Preserve commercial terms sources in bounded company verification |
| `sn116:scoring_commit:2026-10-06T23:29:18Z` | 116 | SCORING_COMMIT | 2026-10-07T02:19:32Z | sn116 commit touches scoring: Merge pull request #723 from carbonphysicsai/claude/validator-19-quiz… |
| `sn120:scoring_commit:2026-10-07T02:05:04Z` | 120 | SCORING_COMMIT | 2026-10-07T02:19:32Z | sn120 commit touches scoring: Prepare isolated all750 matched native evaluation CPU lifecycle |
| `sn25:release:v2026.10.6-1065506180` | 25 | RELEASE | 2026-10-07T09:02:39Z | sn25 released v2026.10.6-1065506180 |
| `sn51:scoring_commit:2026-10-07T02:54:22Z` | 51 | SCORING_COMMIT | 2026-10-07T09:02:39Z | sn51 commit touches scoring: DAH-3980 - validator: a filler create stands down at docker run while… |
| `sn71:scoring_commit:2026-10-07T06:05:38Z` | 71 | SCORING_COMMIT | 2026-10-07T09:02:39Z | sn71 commit touches scoring: Record validator source commits in Arena runtime audit data |
| `sn76:scoring_commit:2026-10-07T08:42:56Z` | 76 | SCORING_COMMIT | 2026-10-07T09:02:39Z | sn76 commit touches scoring: Sync public_subnet: doctor cells/hotkey/cap, /runners/me, --miner-id,… |
| `sn81:scoring_commit:2026-10-07T06:43:08Z` | 81 | SCORING_COMMIT | 2026-10-07T09:02:39Z | sn81 commit touches scoring: Keep failed scorer health and release chained forward frames |
| `sn120:scoring_commit:2026-10-07T08:41:08Z` | 120 | SCORING_COMMIT | 2026-10-07T09:02:39Z | sn120 commit touches scoring: Validate frozen blacklist freshness at the authenticated epoch opening |
| `sn3:scoring_commit:2026-10-06T12:20:17Z` | 3 | SCORING_COMMIT | 2026-10-07T16:23:49Z | sn3 commit touches scoring: Add math, code, and text competitions with gradual reward transition |
| `sn15:scoring_commit:2026-10-07T09:22:23Z` | 15 | SCORING_COMMIT | 2026-10-07T16:23:49Z | sn15 commit touches scoring: Bind configured Readers to cancellable miner-funded simulator inferen… |
| `sn38:scoring_commit:2026-10-07T13:55:15Z` | 38 | SCORING_COMMIT | 2026-10-07T16:23:49Z | sn38 commit touches scoring: Leak returns to the score at 30%, over a [-11, -25] window |
| `sn51:scoring_commit:2026-10-07T14:24:30Z` | 51 | SCORING_COMMIT | 2026-10-07T16:23:49Z | sn51 commit touches scoring: DAH-3980 - validator: a customer rent removes the node's filler in on… |
| `sn67:scoring_commit:2026-10-07T09:20:51Z` | 67 | SCORING_COMMIT | 2026-10-07T16:23:49Z | sn67 commit touches scoring: Document miner decision queries and staging smoke results (#1673) |
| `sn71:scoring_commit:2026-10-07T15:24:41Z` | 71 | SCORING_COMMIT | 2026-10-07T16:23:49Z | sn71 commit touches scoring: Assert current scoring adapter and all judge results in managed-provi… |
| `sn120:scoring_commit:2026-10-07T14:22:11Z` | 120 | SCORING_COMMIT | 2026-10-07T16:23:49Z | sn120 commit touches scoring: Record verified checkpoint-32 full held-out regression |
| `sn15:release:v2.3.0` | 15 | RELEASE | 2026-10-07T21:28:20Z | sn15 released v2.3.0 |
| `sn25:scoring_commit:2026-10-07T16:41:48Z` | 25 | SCORING_COMMIT | 2026-10-07T21:28:20Z | sn25 commit touches scoring: Merge the sole validator's activation-pending config path |
| `sn50:release:v1.14.0` | 50 | RELEASE | 2026-10-07T21:28:20Z | sn50 released v1.14.0 |
| `sn51:scoring_commit:2026-10-07T19:36:24Z` | 51 | SCORING_COMMIT | 2026-10-07T21:28:20Z | sn51 commit touches scoring: DAH-3980 - validator: encrypted volume and renter keys in one exec, r… |
| `sn54:scoring_commit:2026-09-28T17:33:55Z` | 54 | SCORING_COMMIT | 2026-10-07T21:28:20Z | sn54 commit touches scoring: help miners to sign message |
| `sn66:scoring_commit:2026-10-07T15:16:57Z` | 66 | SCORING_COMMIT | 2026-10-07T21:28:20Z | sn66 commit touches scoring: tasks: an unusable identity home is an identity failure, not a doctor… |
| `sn71:scoring_commit:2026-10-07T21:26:53Z` | 71 | SCORING_COMMIT | 2026-10-07T21:28:20Z | sn71 commit touches scoring: Merge PR #265: refresh protected verifier manifest |
| `sn81:scoring_commit:2026-10-07T16:49:28Z` | 81 | SCORING_COMMIT | 2026-10-07T21:28:20Z | sn81 commit touches scoring: Fix pinned operator generation task admission |
| `sn120:scoring_commit:2026-10-07T21:07:51Z` | 120 | SCORING_COMMIT | 2026-10-07T21:28:20Z | sn120 commit touches scoring: Admit explicitly signed source-bound verifier capacity sidecars |
| `sn25:scoring_commit:2026-10-07T20:43:00Z` | 25 | SCORING_COMMIT | 2026-10-08T01:21:53Z | sn25 commit touches scoring: Assert the owner-validator's root seat keeps its own coldkey |
| `sn71:scoring_commit:2026-10-07T22:35:21Z` | 71 | SCORING_COMMIT | 2026-10-08T01:21:53Z | sn71 commit touches scoring: Merge PR #266: support verified Finney runtime 475 reveal events |
| `sn78:scoring_commit:2026-10-08T00:04:50Z` | 78 | SCORING_COMMIT | 2026-10-08T01:21:53Z | sn78 commit touches scoring: Restore original C5 progression and preserve miner upgrade state (#231 |
| `sn116:scoring_commit:2026-10-07T23:24:57Z` | 116 | SCORING_COMMIT | 2026-10-08T01:21:53Z | sn116 commit touches scoring: Merge pull request #782 from carbonphysicsai/agent/validator-23-bank-… |
| `sn120:scoring_commit:2026-10-07T23:59:16Z` | 120 | SCORING_COMMIT | 2026-10-08T01:21:53Z | sn120 commit touches scoring: Use signed manifest quotas for miner-bound multi-rollout batches |
| `sn25:scoring_commit:2026-10-08T02:54:58Z` | 25 | SCORING_COMMIT | 2026-10-08T07:46:34Z | sn25 commit touches scoring: Merge runtime upgrade tolerance for the production validator |
| `sn51:release:executor-v1.138` | 51 | RELEASE | 2026-10-08T07:46:34Z | sn51 released executor-v1.138 |
| `sn51:scoring_commit:2026-10-08T07:42:00Z` | 51 | SCORING_COMMIT | 2026-10-08T07:46:34Z | sn51 commit touches scoring: validator: remove the failed container before the stale-mount retry (… |
| `sn71:scoring_commit:2026-10-08T06:51:28Z` | 71 | SCORING_COMMIT | 2026-10-08T07:46:34Z | sn71 commit touches scoring: Merge remote-tracking branch 'origin/main' into codex/public-evaluati… |
| `sn100:scoring_commit:2026-10-08T04:21:19Z` | 100 | SCORING_COMMIT | 2026-10-08T07:46:34Z | sn100 commit touches scoring: docs(repo): remove retired products, add readme and validator script … |
| `sn116:release:producer-code-r2: code-only tag for the ` | 116 | RELEASE | 2026-10-08T07:46:34Z | sn116 released producer-code-r2: code-only tag for the producer and the leak runbook |
| `sn116:scoring_commit:2026-10-08T07:05:19Z` | 116 | SCORING_COMMIT | 2026-10-08T07:46:34Z | sn116 commit touches scoring: Merge pull request #780 from carbonphysicsai/agent/validator-24-withd… |
| `sn120:scoring_commit:2026-10-08T06:54:09Z` | 120 | SCORING_COMMIT | 2026-10-08T07:46:34Z | sn120 commit touches scoring: Validate paired held-out trainer optimization results |
| `sn3:scoring_commit:2026-10-08T10:48:25Z` | 3 | SCORING_COMMIT | 2026-10-08T14:58:35Z | sn3 commit touches scoring: Add competition dataset panel and update evaluation history layout |
| `sn15:release:v2.4.0: Prepare runtime 3.5 validator an` | 15 | RELEASE | 2026-10-08T14:58:35Z | sn15 released v2.4.0: Prepare runtime 3.5 validator and practice delivery (#367) |
| `sn15:scoring_commit:2026-10-08T08:48:54Z` | 15 | SCORING_COMMIT | 2026-10-08T14:58:35Z | sn15 commit touches scoring: Prepare runtime 3.5 validator and practice delivery (#367) |
| `sn21:scoring_commit:2026-10-08T14:35:15Z` | 21 | SCORING_COMMIT | 2026-10-08T14:58:35Z | sn21 commit touches scoring: fix(scoring): copy groups agree on one earner, the earliest submission |
| `sn51:scoring_commit:2026-10-08T09:21:54Z` | 51 | SCORING_COMMIT | 2026-10-08T14:58:35Z | sn51 commit touches scoring: DAH-4001 - validator: shadow never delays the live weights, settlemen… |
| `sn71:scoring_commit:2026-10-08T07:52:06Z` | 71 | SCORING_COMMIT | 2026-10-08T14:58:35Z | sn71 commit touches scoring: Merge PR #276: verify judging through the miner provider route |
| `sn81:scoring_commit:2026-10-08T08:52:59Z` | 81 | SCORING_COMMIT | 2026-10-08T14:58:35Z | sn81 commit touches scoring: docs(corpus): the open route and the agentic miner's use of it |
| `sn116:release:worker-images-v2` | 116 | RELEASE | 2026-10-08T14:58:35Z | sn116 released worker-images-v2 |
| `sn116:scoring_commit:2026-10-08T13:55:12Z` | 116 | SCORING_COMMIT | 2026-10-08T14:58:35Z | sn116 commit touches scoring: Merge pull request #815 from carbonphysicsai/agent/battery-score-rule- |
| `sn120:scoring_commit:2026-10-08T08:41:04Z` | 120 | SCORING_COMMIT | 2026-10-08T14:58:35Z | sn120 commit touches scoring: Keep learner startup independent of an unreachable verifier transport |
| `sn25:release:v2026.10.8-1066912010` | 25 | RELEASE | 2026-10-08T20:40:32Z | sn25 released v2026.10.8-1066912010 |
| `sn41:scoring_commit:2026-10-08T19:33:16Z` | 41 | SCORING_COMMIT | 2026-10-08T20:40:32Z | sn41 commit touches scoring: Merge pull request #55 from corvxai/forecasting_scoring_v2 |
| `sn51:scoring_commit:2026-10-08T15:36:23Z` | 51 | SCORING_COMMIT | 2026-10-08T20:40:32Z | sn51 commit touches scoring: DAH-3769 - Validator: dropped SSH transport becomes a typed error wit… |
| `sn58:scoring_commit:2026-10-08T18:16:01Z` | 58 | SCORING_COMMIT | 2026-10-08T20:40:32Z | sn58 commit touches scoring: fix(miner): `attune miner status` checks the Hub with the submission … |
| `sn71:scoring_commit:2026-10-08T17:08:48Z` | 71 | SCORING_COMMIT | 2026-10-08T20:40:32Z | sn71 commit touches scoring: Allow bounded score batch RPC reads to finish |
| `sn90:scoring_commit:2026-10-08T18:01:39Z` | 90 | SCORING_COMMIT | 2026-10-08T20:40:32Z | sn90 commit touches scoring: docs(nemotron-omni): 256k context verified + NIM 2.0.13 + gateway mod… |
| `sn116:scoring_commit:2026-10-08T19:33:03Z` | 116 | SCORING_COMMIT | 2026-10-08T20:40:32Z | sn116 commit touches scoring: Record the owner's canary answers 2-4 in OWNER-CANARY-MINER-01 |
| `sn120:scoring_commit:2026-10-08T15:53:32Z` | 120 | SCORING_COMMIT | 2026-10-08T20:40:32Z | sn120 commit touches scoring: Verify longer harness cannot reuse shorter-budget calibration |
| `sn25:release:v2026.10.8-1066946420` | 25 | RELEASE | 2026-10-09T00:42:20Z | sn25 released v2026.10.8-1066946420 |
| `sn62:release:v0.3.10` | 62 | RELEASE | 2026-10-09T00:42:20Z | sn62 released v0.3.10 |
| `sn71:scoring_commit:2026-10-09T00:04:40Z` | 71 | SCORING_COMMIT | 2026-10-09T00:42:20Z | sn71 commit touches scoring: Merge pull request #295 from leadpoet/fix/host-score-closed-billing |
| `sn78:scoring_commit:2026-10-08T23:22:27Z` | 78 | SCORING_COMMIT | 2026-10-09T00:42:20Z | sn78 commit touches scoring: Select policy-budget miner release and resume completed-case archives |
| `sn116:release:worker-images-v3` | 116 | RELEASE | 2026-10-09T00:42:20Z | sn116 released worker-images-v3 |
| `sn116:scoring_commit:2026-10-08T22:48:01Z` | 116 | SCORING_COMMIT | 2026-10-09T00:42:20Z | sn116 commit touches scoring: Merge pull request #846 from carbonphysicsai/codex/challenge-value-co… |
| `sn120:scoring_commit:2026-10-08T21:41:26Z` | 120 | SCORING_COMMIT | 2026-10-09T00:42:20Z | sn120 commit touches scoring: Confirm fresh public epoch and authenticated base evaluation |
| `sn51:scoring_commit:2026-10-09T04:13:41Z` | 51 | SCORING_COMMIT | 2026-10-09T06:48:38Z | sn51 commit touches scoring: DAH-4001 - validator: no settled window keeps the weights in force, i… |
| `sn81:scoring_commit:2026-10-09T02:51:22Z` | 81 | SCORING_COMMIT | 2026-10-09T06:48:38Z | sn81 commit touches scoring: Merge pull request #342 from reliquadotai/fix/task-catalog-artifact-r… |
| `sn89:scoring_commit:2026-10-09T02:22:48Z` | 89 | SCORING_COMMIT | 2026-10-09T06:48:38Z | sn89 commit touches scoring: README: IQ Markets for players (web app, /markets, no miner needed; r… |
| `sn101:scoring_commit:2026-10-08T15:09:53Z` | 101 | SCORING_COMMIT | 2026-10-09T06:48:38Z | sn101 commit touches scoring: Add v1.1 scoring, AWS corpus leasing, weight-setting hardening, and l… |
| `sn107:scoring_commit:2026-10-09T03:53:09Z` | 107 | SCORING_COMMIT | 2026-10-09T06:48:38Z | sn107 commit touches scoring: Merge pull request #40 from minos-protocol/fix/scoring-cutoff-lead |
| `sn116:scoring_commit:2026-10-09T05:13:15Z` | 116 | SCORING_COMMIT | 2026-10-09T06:48:38Z | sn116 commit touches scoring: Merge pull request #854 from carbonphysicsai/agent/score-feed-schema |
| `sn120:scoring_commit:2026-10-09T06:24:44Z` | 120 | SCORING_COMMIT | 2026-10-09T06:48:38Z | sn120 commit touches scoring: Bind native recovery imports and keep evaluator read capabilities out… |
| `sn3:scoring_commit:2026-10-09T13:41:35Z` | 3 | SCORING_COMMIT | 2026-10-09T14:20:19Z | sn3 commit touches scoring: Add competition filters to evaluation history and update dataset summ… |
| `sn21:release:SN21 training data v4 (live basket shape` | 21 | RELEASE | 2026-10-09T14:20:19Z | sn21 released SN21 training data v4 (live basket shape) |
| `sn50:scoring_commit:2026-10-09T13:27:10Z` | 50 | SCORING_COMMIT | 2026-10-09T14:20:19Z | sn50 commit touches scoring: Avoid a full miner_predictions scan when loading scores (#337) |
| `sn51:scoring_commit:2026-10-09T09:49:06Z` | 51 | SCORING_COMMIT | 2026-10-09T14:20:19Z | sn51 commit touches scoring: DAH-3980 - Validator: one Docker SDK SSH channel per host, not per UR… |
| `sn71:scoring_commit:2026-10-09T07:27:04Z` | 71 | SCORING_COMMIT | 2026-10-09T14:20:19Z | sn71 commit touches scoring: Refresh protected judge fit manifest for merged scorer |
| `sn76:scoring_commit:2026-10-09T14:10:54Z` | 76 | SCORING_COMMIT | 2026-10-09T14:20:19Z | sn76 commit touches scoring: protected/miner/manifest.json: single admitted compose hash after the… |
| `sn78:scoring_commit:2026-10-09T09:19:01Z` | 78 | SCORING_COMMIT | 2026-10-09T14:20:19Z | sn78 commit touches scoring: Unblock C5 admission reads and correct historical block verification … |
| `sn89:scoring_commit:2026-10-09T08:42:41Z` | 89 | SCORING_COMMIT | 2026-10-09T14:20:19Z | sn89 commit touches scoring: scoring: cache z_for_resolve (pure function, bit-identical output) |
| `sn111:scoring_commit:2026-10-08T19:49:34Z` | 111 | SCORING_COMMIT | 2026-10-09T14:20:19Z | sn111 commit touches scoring: feat(validator): route verified operator miner allocation |
| `sn116:scoring_commit:2026-10-09T12:50:59Z` | 116 | SCORING_COMMIT | 2026-10-09T14:20:19Z | sn116 commit touches scoring: VALIDATOR-30 contract: the refusal order (root allow-list first) and … |
| `sn120:scoring_commit:2026-10-09T11:15:27Z` | 120 | SCORING_COMMIT | 2026-10-09T14:20:19Z | sn120 commit touches scoring: Verify effective-LR evidence for normal optimizer continuation |
| `sn13:release:Release v1.18.74` | 13 | RELEASE | 2026-10-09T19:37:09Z | sn13 released Release v1.18.74 |
| `sn21:scoring_commit:2026-10-09T15:47:13Z` | 21 | SCORING_COMMIT | 2026-10-09T19:37:09Z | sn21 commit touches scoring: docs(rewards): self-mining section lists the operator-run miners (UID… |
| `sn25:scoring_commit:2026-10-09T17:31:17Z` | 25 | SCORING_COMMIT | 2026-10-09T19:37:09Z | sn25 commit touches scoring: Name a rejected network sign-in in the validator |
| `sn71:scoring_commit:2026-10-09T19:30:42Z` | 71 | SCORING_COMMIT | 2026-10-09T19:37:09Z | sn71 commit touches scoring: Include accepted host scores in closed billing selector |
| `sn76:scoring_commit:2026-10-09T18:01:37Z` | 76 | SCORING_COMMIT | 2026-10-09T19:37:09Z | sn76 commit touches scoring: Pool deliveries: claim-refusal backoff + claim_health(); validator --… |
| `sn81:scoring_commit:2026-10-09T09:04:13Z` | 81 | SCORING_COMMIT | 2026-10-09T19:37:09Z | sn81 commit touches scoring: feat(env): score reliquary/stdio-program/v1 sources in the sandbox |
| `sn116:release:producer-code-r5` | 116 | RELEASE | 2026-10-09T19:37:09Z | sn116 released producer-code-r5 |
| `sn116:scoring_commit:2026-10-09T19:34:16Z` | 116 | SCORING_COMMIT | 2026-10-09T19:37:09Z | sn116 commit touches scoring: Merge pull request #935 from carbonphysicsai/codex/v3-score-inputs-01 |
| `sn120:scoring_commit:2026-10-09T19:24:54Z` | 120 | SCORING_COMMIT | 2026-10-09T19:37:09Z | sn120 commit touches scoring: Recover hourly miner weight submissions from finalized chain evidence |
| `sn14:scoring_commit:2026-10-09T21:56:54Z` | 14 | SCORING_COMMIT | 2026-10-09T23:34:47Z | sn14 commit touches scoring: Notify Discord when new hotkeys receive committed and active weights … |
| `sn71:scoring_commit:2026-10-09T23:12:54Z` | 71 | SCORING_COMMIT | 2026-10-09T23:34:47Z | sn71 commit touches scoring: Refresh protected scorer manifest for required-stage retry |
| `sn116:release:producer-code-r6` | 116 | RELEASE | 2026-10-09T23:34:47Z | sn116 released producer-code-r6 |
| `sn116:scoring_commit:2026-10-09T20:56:19Z` | 116 | SCORING_COMMIT | 2026-10-09T23:34:47Z | sn116 commit touches scoring: Merge pull request #943 from carbonphysicsai/codex/landscape-miner-in… |
| `sn120:scoring_commit:2026-10-09T21:02:00Z` | 120 | SCORING_COMMIT | 2026-10-09T23:34:47Z | sn120 commit touches scoring: Retain partial miner batches and advance sampling attempts on retries |
| `sn25:release:v2026.10.9-1067985620` | 25 | RELEASE | 2026-10-10T02:48:16Z | sn25 released v2026.10.9-1067985620 |
| `sn62:release:v0.3.11` | 62 | RELEASE | 2026-10-10T02:48:16Z | sn62 released v0.3.11 |
| `sn71:scoring_commit:2026-10-10T02:16:30Z` | 71 | SCORING_COMMIT | 2026-10-10T02:48:16Z | sn71 commit touches scoring: Merge pull request #322 from leadpoet/codex/arena-partial-score-deadl… |
| `sn120:scoring_commit:2026-10-10T01:21:35Z` | 120 | SCORING_COMMIT | 2026-10-10T02:48:16Z | sn120 commit touches scoring: Support prospective nine-batch mining and 512-task training |
| `sn25:release:v2026.10.10-1068162640` | 25 | RELEASE | 2026-10-10T09:44:36Z | sn25 released v2026.10.10-1068162640 |
| `sn51:scoring_commit:2026-10-10T04:05:02Z` | 51 | SCORING_COMMIT | 2026-10-10T09:44:36Z | sn51 commit touches scoring: NO-TICKET - [P1] validator: cap fresh vloopback volume at the ext4 16… |
| `sn71:scoring_commit:2026-10-10T04:22:43Z` | 71 | SCORING_COMMIT | 2026-10-10T09:44:36Z | sn71 commit touches scoring: Merge pull request #328 from leadpoet/codex/paid-score-abandonment-441 |
| `sn120:scoring_commit:2026-10-10T09:04:36Z` | 120 | SCORING_COMMIT | 2026-10-10T09:44:36Z | sn120 commit touches scoring: Document live epoch 116 distinct-task training intake |
| `sn25:release:v2026.10.10-1068404160` | 25 | RELEASE | 2026-10-10T15:35:44Z | sn25 released v2026.10.10-1068404160 |
| `sn28:release:v0.4.27-dev` | 28 | RELEASE | 2026-10-10T15:35:44Z | sn28 released v0.4.27-dev |
| `sn28:scoring_commit:2026-10-10T13:53:49Z` | 28 | SCORING_COMMIT | 2026-10-10T15:35:44Z | sn28 commit touches scoring: chore(release): gm-miner 0.4.27-dev (#310) |
| `sn71:scoring_commit:2026-10-10T15:33:53Z` | 71 | SCORING_COMMIT | 2026-10-10T15:35:44Z | sn71 commit touches scoring: Rejudge Oct10 saved outputs on final ATS scorer |
| `sn25:release:v2026.10.10-1068595480` | 25 | RELEASE | 2026-10-10T19:34:14Z | sn25 released v2026.10.10-1068595480 |
| `sn71:scoring_commit:2026-10-10T19:08:12Z` | 71 | SCORING_COMMIT | 2026-10-10T19:34:14Z | sn71 commit touches scoring: Merge pull request #354 from leadpoet/fix/arena-confirmed-score-parall |
| `sn108:scoring_commit:2026-10-10T15:01:19Z` | 108 | SCORING_COMMIT | 2026-10-10T19:34:14Z | sn108 commit touches scoring: On a baseline_epoch change the validator's bar is exactly the server'… |
| `sn120:scoring_commit:2026-10-10T17:31:08Z` | 120 | SCORING_COMMIT | 2026-10-10T19:34:14Z | sn120 commit touches scoring: Clarify availability of reused historical evaluations |
| `sn25:scoring_commit:2026-10-10T20:21:02Z` | 25 | SCORING_COMMIT | 2026-10-10T22:59:03Z | sn25 commit touches scoring: Merge seeding validator trails from every online provider |
| `sn71:scoring_commit:2026-10-10T21:43:42Z` | 71 | SCORING_COMMIT | 2026-10-10T22:59:03Z | sn71 commit touches scoring: Merge pull request #363 from leadpoet/fix/arena-oct10-score-claim-cuto |
| `sn25:release:v2026.10.10-1068748650` | 25 | RELEASE | 2026-10-11T01:49:20Z | sn25 released v2026.10.10-1068748650 |
| `sn71:scoring_commit:2026-10-11T01:38:29Z` | 71 | SCORING_COMMIT | 2026-10-11T01:49:20Z | sn71 commit touches scoring: Verify guarded natural expiry retains uncertain execute bills |
| `sn22:scoring_commit:2026-10-11T08:32:04Z` | 22 | SCORING_COMMIT | 2026-10-11T08:43:38Z | sn22 commit touches scoring: fix(validators): restore rendered rechecks and the 5% sample |
| `sn25:release:v2026.10.10-1068958850` | 25 | RELEASE | 2026-10-11T08:43:38Z | sn25 released v2026.10.10-1068958850 |
| `sn116:scoring_commit:2026-10-11T02:06:55Z` | 116 | SCORING_COMMIT | 2026-10-11T08:43:38Z | sn116 commit touches scoring: Merge pull request #1041 from carbonphysicsai/claude/miner-survive-re… |
| `sn120:scoring_commit:2026-10-11T07:02:34Z` | 120 | SCORING_COMMIT | 2026-10-11T08:43:38Z | sn120 commit touches scoring: Document independent epoch openings and hourly reward fallback |
| `sn116:release:producer-code-r7` | 116 | RELEASE | 2026-10-11T15:07:48Z | sn116 released producer-code-r7 |
| `sn116:scoring_commit:2026-10-11T14:34:29Z` | 116 | SCORING_COMMIT | 2026-10-11T15:07:48Z | sn116 commit touches scoring: Merge pull request #1046 from carbonphysicsai/codex/code-verification… |
| `sn15:release:v2.4.1` | 15 | RELEASE | 2026-10-11T19:38:20Z | sn15 released v2.4.1 |
| `sn21:scoring_commit:2026-10-11T17:10:16Z` | 21 | SCORING_COMMIT | 2026-10-11T19:38:20Z | sn21 commit touches scoring: docs(verifying): the standing preview exists only during a notice per… |
| `sn22:scoring_commit:2026-10-11T18:25:03Z` | 22 | SCORING_COMMIT | 2026-10-11T19:38:20Z | sn22 commit touches scoring: fix(validators): no JS rendering, 20 pages per 1,000-URL task, fail o… |
| `sn71:scoring_commit:2026-10-11T16:11:47Z` | 71 | SCORING_COMMIT | 2026-10-11T19:38:20Z | sn71 commit touches scoring: Install current reward RPCs in per-ICP round fixture |
| `sn76:scoring_commit:2026-10-11T16:48:26Z` | 76 | SCORING_COMMIT | 2026-10-11T19:38:20Z | sn76 commit touches scoring: Fix miner registration-first onboarding |
| `sn81:scoring_commit:2026-10-11T06:43:18Z` | 81 | SCORING_COMMIT | 2026-10-11T19:38:20Z | sn81 commit touches scoring: feat(cli): tasks set-cap sets or clears a corpus task's token price |
| `sn116:release:producer-code-r8.1` | 116 | RELEASE | 2026-10-11T19:38:20Z | sn116 released producer-code-r8.1 |
| `sn117:release:everycli v0.2.4` | 117 | RELEASE | 2026-10-11T19:38:20Z | sn117 released everycli v0.2.4 |
| `sn117:release:v0.2.5` | 117 | RELEASE | 2026-10-11T23:13:02Z | sn117 released v0.2.5 |
| `sn71:scoring_commit:2026-10-12T01:30:49Z` | 71 | SCORING_COMMIT | 2026-10-12T02:34:00Z | sn71 commit touches scoring: Verify miner credit diagnostics through PostgreSQL reconciliation |
| `sn117:release:everycli v0.3.1` | 117 | RELEASE | 2026-10-12T02:34:00Z | sn117 released everycli v0.3.1 |
| `sn120:scoring_commit:2026-10-12T00:43:15Z` | 120 | SCORING_COMMIT | 2026-10-12T02:34:00Z | sn120 commit touches scoring: Rotate overused math tasks through existing epoch manifests |
| `sn25:scoring_commit:2026-10-12T00:57:57Z` | 25 | SCORING_COMMIT | 2026-10-12T09:49:01Z | sn25 commit touches scoring: Admit one pinned native gap edge so the validator resumes after misse… |
| `sn51:release:executor-v1.139` | 51 | RELEASE | 2026-10-12T09:49:01Z | sn51 released executor-v1.139 |
| `sn51:scoring_commit:2026-10-12T07:54:49Z` | 51 | SCORING_COMMIT | 2026-10-12T09:49:01Z | sn51 commit touches scoring: DAH-3998 - [P2] Signed node heartbeat; validator forwards only a veri… |
| `sn58:scoring_commit:2026-10-11T10:31:29Z` | 58 | SCORING_COMMIT | 2026-10-12T09:49:01Z | sn58 commit touches scoring: feat(vector): a validator on another host takes the lane up from the … |
| `sn94:scoring_commit:2026-10-12T09:13:20Z` | 94 | SCORING_COMMIT | 2026-10-12T09:49:01Z | sn94 commit touches scoring: Merge pull request #254 from skyrocket2026/feat/verifier-release-next |
| `sn116:scoring_commit:2026-10-12T07:28:34Z` | 116 | SCORING_COMMIT | 2026-10-12T09:49:01Z | sn116 commit touches scoring: Merge pull request #1143 from carbonphysicsai/agent/validator-33a-fee… |
| `sn117:release:everycli v0.3.3` | 117 | RELEASE | 2026-10-12T09:49:01Z | sn117 released everycli v0.3.3 |
| `sn120:scoring_commit:2026-10-12T07:59:56Z` | 120 | SCORING_COMMIT | 2026-10-12T09:49:01Z | sn120 commit touches scoring: Plot fixed previously trained tasks in TRAIN fit series |
| `sn3:scoring_commit:2026-10-12T11:52:12Z` | 3 | SCORING_COMMIT | 2026-10-12T19:47:00Z | sn3 commit touches scoring: Optimize evaluator shard downloads with cached HTTP range reads |
| `sn9:release:v4.13.6` | 9 | RELEASE | 2026-10-12T19:47:00Z | sn9 released v4.13.6 |
| `sn14:scoring_commit:2026-10-12T18:41:34Z` | 14 | SCORING_COMMIT | 2026-10-12T19:47:00Z | sn14 commit touches scoring: Retain audit diagnostics and post bundle results to Discord (#145) |
| `sn21:scoring_commit:2026-10-12T12:32:21Z` | 21 | SCORING_COMMIT | 2026-10-12T19:47:00Z | sn21 commit touches scoring: fix(validator): the validator site sends daily-results requests to th… |
| `sn28:release:v0.4.27` | 28 | RELEASE | 2026-10-12T19:47:00Z | sn28 released v0.4.27 |
| `sn28:scoring_commit:2026-10-12T11:20:56Z` | 28 | SCORING_COMMIT | 2026-10-12T19:47:00Z | sn28 commit touches scoring: chore(release): promote gm-miner 0.4.27 (#313) |
| `sn38:scoring_commit:2026-10-12T14:44:32Z` | 38 | SCORING_COMMIT | 2026-10-12T19:47:00Z | sn38 commit touches scoring: Update validator image to the latest version in docker-compose.valida… |
| `sn51:scoring_commit:2026-10-12T19:29:45Z` | 51 | SCORING_COMMIT | 2026-10-12T19:47:00Z | sn51 commit touches scoring: DAH-4001 - validator: report each live weight submission with the cyc… |
| `sn53:scoring_commit:2026-10-12T12:53:09Z` | 53 | SCORING_COMMIT | 2026-10-12T19:47:00Z | sn53 commit touches scoring: Merge pull request #52 from hanlinai/fix/tee-miner-kv-heartbeat-10s |
| `sn71:scoring_commit:2026-10-12T16:30:43Z` | 71 | SCORING_COMMIT | 2026-10-12T19:47:00Z | sn71 commit touches scoring: Apply existing provider failure classification to interrupted scorer … |
| `sn116:release:producer-code-r8.4` | 116 | RELEASE | 2026-10-12T19:47:00Z | sn116 released producer-code-r8.4 |
| `sn116:scoring_commit:2026-10-12T19:20:37Z` | 116 | SCORING_COMMIT | 2026-10-12T19:47:00Z | sn116 commit touches scoring: Record OWNER-BATTERY-CHAMPIONSHIP-04: miner status rows, laddered sco… |
| `sn117:release:everycli v0.3.7` | 117 | RELEASE | 2026-10-12T19:47:00Z | sn117 released everycli v0.3.7 |
| `sn120:scoring_commit:2026-10-12T17:41:42Z` | 120 | SCORING_COMMIT | 2026-10-12T19:47:00Z | sn120 commit touches scoring: Add prospective verifier-only symmetric sampling adjudication |
| `sn76:readme_task_diff:0fe72f423e42ba2f` | 76 | README_TASK_DIFF | 2026-10-07T09:02:39Z | sn76 README task/scoring sections changed |
| `sn54:readme_task_diff:97fe30779066869c` | 54 | README_TASK_DIFF | 2026-10-07T21:28:20Z | sn54 README task/scoring sections changed |
| `sn66:readme_task_diff:3eb60404bf70ad6f` | 66 | README_TASK_DIFF | 2026-10-07T21:28:20Z | sn66 README task/scoring sections changed |
| `sn101:readme_task_diff:69a3be15960a468f` | 101 | README_TASK_DIFF | 2026-10-09T06:48:38Z | sn101 README task/scoring sections changed |
| `sn76:readme_task_diff:c11a1b8d6bd23a9b` | 76 | README_TASK_DIFF | 2026-10-09T14:20:19Z | sn76 README task/scoring sections changed |
| `sn48:readme_task_diff:681058003f640cf6` | 48 | README_TASK_DIFF | 2026-10-09T19:37:09Z | sn48 README task/scoring sections changed |
| `sn66:readme_task_diff:53ca2fbbcaa75039` | 66 | README_TASK_DIFF | 2026-10-09T19:37:09Z | sn66 README task/scoring sections changed |
| `sn79:readme_task_diff:1ab076cd7112df84` | 79 | README_TASK_DIFF | 2026-10-09T19:37:09Z | sn79 README task/scoring sections changed |
| `sn117:readme_task_diff:ad8c3f68204b01ab` | 117 | README_TASK_DIFF | 2026-10-09T19:37:09Z | sn117 README task/scoring sections changed |
| `sn76:readme_task_diff:0a4c226e1573572b` | 76 | README_TASK_DIFF | 2026-10-11T19:38:20Z | sn76 README task/scoring sections changed |
| `sn117:readme_task_diff:1f5936ceb48b4e59` | 117 | README_TASK_DIFF | 2026-10-11T19:38:20Z | sn117 README task/scoring sections changed |
| `sn117:readme_task_diff:0f4be566c399b388` | 117 | README_TASK_DIFF | 2026-10-11T23:13:02Z | sn117 README task/scoring sections changed |
| `sn28:readme_task_diff:a275dd150e9b5f4f` | 28 | README_TASK_DIFF | 2026-10-12T19:47:00Z | sn28 README task/scoring sections changed |
| `sn117:readme_task_diff:4631619b61bf245f` | 117 | README_TASK_DIFF | 2026-10-12T19:47:00Z | sn117 README task/scoring sections changed |

## RESOLVED IN THIS WINDOW

_none_
