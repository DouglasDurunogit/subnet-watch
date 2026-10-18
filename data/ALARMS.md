# ALARMS - generated 2026-10-18T19:42:14Z, block 9312493

window: first_seen in [2026-10-18T18:27:43Z, 2026-10-18T19:42:43Z)  (60 min interval + 15 min overlap)

Report ONLY the rows under NEW SINCE LAST RUN. Rows under STILL OPEN were
already reported in an earlier window and must not be re-alarmed.

## NEW SINCE LAST RUN

| event_id | netuid | class | severity | first_seen_utc | one_line |
|---|---|---|---|---|---|
| `sn1:release:v4.4.14` | 1 | RELEASE | P1 | 2026-10-18T19:42:43Z | sn1 released v4.4.14 |
| `sn25:release:v2026.10.18-1075514170` | 25 | RELEASE | P1 | 2026-10-18T19:42:43Z | sn25 released v2026.10.18-1075514170 |
| `sn82:scoring_commit:2026-10-18T18:10:45Z` | 82 | SCORING_COMMIT | P1 | 2026-10-18T19:42:43Z | sn82 commit touches scoring: Release v0.1.0: multisig receipts and surplus-bonus scoring |
| `sn92:release:v1.2.0-rc9` | 92 | RELEASE | P1 | 2026-10-18T19:42:43Z | sn92 released v1.2.0-rc9 |

### detail

- **`sn1:release:v4.4.14`** - sn1 released v4.4.14
  - published 2026-10-18T19:19:34Z (was v4.4.13)
- **`sn25:release:v2026.10.18-1075514170`** - sn25 released v2026.10.18-1075514170
  - published 2026-10-18T19:33:02Z (was v2026.10.17-1074871400)
- **`sn82:scoring_commit:2026-10-18T18:10:45Z`** - sn82 commit touches scoring: Release v0.1.0: multisig receipts and surplus-bonus scoring
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn92:release:v1.2.0-rc9`** - sn92 released v1.2.0-rc9
  - published 2026-10-18T18:33:06Z (was v1.2.0-rc8)

## STILL OPEN (already reported - do not re-alarm)

| event_id | netuid | class | first_seen_utc | one_line |
|---|---|---|---|---|
| `sn30:burn_drop:0.984` | 30 | BURN_DROP | 2026-10-12T02:34:00Z | sn30 burn fell 0.997 -> 0.984 - miners can earn again |
| `sn122:burn_drop:0.100` | 122 | BURN_DROP | 2026-10-12T09:49:01Z | sn122 burn fell 1.000 -> 0.100 - miners can earn again |
| `sn12:mechanism_added:1to2` | 12 | MECHANISM_ADDED | 2026-10-12T19:47:00Z | sn12 now runs 2 incentive mechanisms (was 1) |
| `sn58:burn_drop:0.833` | 58 | BURN_DROP | 2026-10-12T19:47:00Z | sn58 burn fell 1.000 -> 0.833 - miners can earn again |
| `sn37:burn_drop:0.715` | 37 | BURN_DROP | 2026-10-14T10:39:10Z | sn37 burn fell 1.000 -> 0.715 - miners can earn again |
| `sn104:burn_drop:0.953` | 104 | BURN_DROP | 2026-10-14T15:33:11Z | sn104 burn fell 1.000 -> 0.953 - miners can earn again |
| `sn108:burn_drop:0.921` | 108 | BURN_DROP | 2026-10-14T15:33:11Z | sn108 burn fell 1.000 -> 0.921 - miners can earn again |
| `sn10:burn_drop:0.532` | 10 | BURN_DROP | 2026-10-14T19:44:42Z | sn10 burn fell 1.000 -> 0.532 - miners can earn again |
| `sn76:burn_drop:0.988` | 76 | BURN_DROP | 2026-10-14T19:44:42Z | sn76 burn fell 1.000 -> 0.988 - miners can earn again |
| `sn118:burn_drop:0.700` | 118 | BURN_DROP | 2026-10-15T05:51:38Z | sn118 burn fell 1.000 -> 0.700 - miners can earn again |
| `sn76:burn_drop:0.979` | 76 | BURN_DROP | 2026-10-15T19:27:45Z | sn76 burn fell 1.000 -> 0.979 - miners can earn again |
| `sn122:burn_drop:0.727` | 122 | BURN_DROP | 2026-10-15T19:27:45Z | sn122 burn fell 1.000 -> 0.727 - miners can earn again |
| `sn37:burn_drop:0.713` | 37 | BURN_DROP | 2026-10-16T10:10:43Z | sn37 burn fell 1.000 -> 0.713 - miners can earn again |
| `sn76:burn_drop:0.961` | 76 | BURN_DROP | 2026-10-16T10:10:43Z | sn76 burn fell 0.999 -> 0.961 - miners can earn again |
| `sn100:burn_drop:0.705` | 100 | BURN_DROP | 2026-10-16T18:46:43Z | sn100 burn fell 1.000 -> 0.705 - miners can earn again |
| `sn97:burn_drop:0.600` | 97 | BURN_DROP | 2026-10-16T21:47:16Z | sn97 burn fell 1.000 -> 0.600 - miners can earn again |
| `sn120:mechanism_added:1to2` | 120 | MECHANISM_ADDED | 2026-10-17T08:43:24Z | sn120 now runs 2 incentive mechanisms (was 1) |
| `sn55:burn_drop:0.010` | 55 | BURN_DROP | 2026-10-18T10:56:59Z | sn55 burn fell 1.000 -> 0.010 - miners can earn again |
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
| `sn28:release:v0.4.28` | 28 | RELEASE | 2026-10-13T01:39:30Z | sn28 released v0.4.28 |
| `sn28:scoring_commit:2026-10-12T21:12:43Z` | 28 | SCORING_COMMIT | 2026-10-13T01:39:30Z | sn28 commit touches scoring: chore(release): promote gm-miner 0.4.28 (#317) |
| `sn71:scoring_commit:2026-10-12T22:46:22Z` | 71 | SCORING_COMMIT | 2026-10-13T01:39:30Z | sn71 commit touches scoring: Finish validated bounded evidence reviews without time-only failure |
| `sn74:release:release-20261012-224627` | 74 | RELEASE | 2026-10-13T01:39:30Z | sn74 released release-20261012-224627 |
| `sn74:scoring_commit:2026-10-12T22:45:40Z` | 74 | SCORING_COMMIT | 2026-10-13T01:39:30Z | sn74 commit touches scoring: chore(weights): burn all miner emissions (empty registry, compute sha… |
| `sn117:release:everycli v0.3.8` | 117 | RELEASE | 2026-10-13T01:39:30Z | sn117 released everycli v0.3.8 |
| `sn25:release:v2026.10.13-1070793380` | 25 | RELEASE | 2026-10-13T08:31:47Z | sn25 released v2026.10.13-1070793380 |
| `sn25:scoring_commit:2026-10-13T05:05:10Z` | 25 | SCORING_COMMIT | 2026-10-13T08:31:47Z | sn25 commit touches scoring: Merge the validator steering fixes deployed on Oct 13 |
| `sn51:release:executor-v1.140` | 51 | RELEASE | 2026-10-13T08:31:47Z | sn51 released executor-v1.140 |
| `sn51:scoring_commit:2026-10-13T04:12:42Z` | 51 | SCORING_COMMIT | 2026-10-13T08:31:47Z | sn51 commit touches scoring: DAH-3980 - Validator: install sshd without recommended packages (#1547 |
| `sn67:scoring_commit:2026-10-13T02:10:44Z` | 67 | SCORING_COMMIT | 2026-10-13T08:31:47Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20261013.post1 |
| `sn71:scoring_commit:2026-10-13T04:39:21Z` | 71 | SCORING_COMMIT | 2026-10-13T08:31:47Z | sn71 commit touches scoring: Merge pull request #408 from leadpoet/fix/arena-public-completed-scor… |
| `sn117:release:everycli v0.3.9` | 117 | RELEASE | 2026-10-13T08:31:47Z | sn117 released everycli v0.3.9 |
| `sn21:scoring_commit:2026-10-13T15:45:33Z` | 21 | SCORING_COMMIT | 2026-10-13T16:29:14Z | sn21 commit touches scoring: fix(scoring): the configured goal is ranked high, medium, low, then n… |
| `sn25:release:v2026.10.13-1070979130` | 25 | RELEASE | 2026-10-13T16:29:14Z | sn25 released v2026.10.13-1070979130 |
| `sn25:scoring_commit:2026-10-13T08:19:37Z` | 25 | SCORING_COMMIT | 2026-10-13T16:29:14Z | sn25 commit touches scoring: Merge the validator trail fixes and bounded steering cut waits |
| `sn37:scoring_commit:2026-10-13T14:58:28Z` | 37 | SCORING_COMMIT | 2026-10-13T16:29:14Z | sn37 commit touches scoring: Replace the legacy public tree with the v5 miner and participant guid… |
| `sn51:scoring_commit:2026-10-13T13:20:45Z` | 51 | SCORING_COMMIT | 2026-10-13T16:29:14Z | sn51 commit touches scoring: A create that fails on the node itself keeps the node at score 0 unti… |
| `sn53:scoring_commit:2026-10-13T11:57:30Z` | 53 | SCORING_COMMIT | 2026-10-13T16:29:14Z | sn53 commit touches scoring: Merge pull request #53 from hanlinai/fix/tee-miner-no-body-in-logs |
| `sn61:release:4.10.10` | 61 | RELEASE | 2026-10-13T16:29:14Z | sn61 released 4.10.10 |
| `sn61:scoring_commit:2026-10-13T10:21:07Z` | 61 | SCORING_COMMIT | 2026-10-13T16:29:14Z | sn61 commit touches scoring: fix: adjust challenge incentive weights and max unique commits for be… |
| `sn68:scoring_commit:2026-09-18T16:21:27Z` | 68 | SCORING_COMMIT | 2026-10-13T16:29:14Z | sn68 commit touches scoring: route all validator chain calls through one reconnecting client |
| `sn81:scoring_commit:2026-10-13T10:12:22Z` | 81 | SCORING_COMMIT | 2026-10-13T16:29:14Z | sn81 commit touches scoring: feat(envscaler): one call per message in the task prompt; episodes bo… |
| `sn114:scoring_commit:2026-10-13T10:59:50Z` | 114 | SCORING_COMMIT | 2026-10-13T16:29:14Z | sn114 commit touches scoring: Merge pull request #229 from DendriteHQ/fix/soma-task-eval-resource-l… |
| `sn116:release:producer-code-r8.5` | 116 | RELEASE | 2026-10-13T16:29:14Z | sn116 released producer-code-r8.5 |
| `sn116:scoring_commit:2026-10-13T15:01:13Z` | 116 | SCORING_COMMIT | 2026-10-13T16:29:14Z | sn116 commit touches scoring: Merge pull request #1281 from carbonphysicsai/codex/opt15b-score-lab-… |
| `sn117:release:everycli v0.4.0` | 117 | RELEASE | 2026-10-13T16:29:14Z | sn117 released everycli v0.4.0 |
| `sn120:scoring_commit:2026-10-13T15:41:21Z` | 120 | SCORING_COMMIT | 2026-10-13T16:29:14Z | sn120 commit touches scoring: Validate trainer completion against fresh receipt clock |
| `sn15:release:v2.5.0` | 15 | RELEASE | 2026-10-13T21:35:22Z | sn15 released v2.5.0 |
| `sn15:scoring_commit:2026-10-13T20:00:27Z` | 15 | SCORING_COMMIT | 2026-10-13T21:35:22Z | sn15 commit touches scoring: Load v7 and v8 task packs; move to oro-env-runtime 3.7.0 (runtime con… |
| `sn25:scoring_commit:2026-10-13T20:37:33Z` | 25 | SCORING_COMMIT | 2026-10-13T21:35:22Z | sn25 commit touches scoring: Write the validator's settlement v2 adoption commands and hold them t… |
| `sn41:scoring_commit:2026-10-13T16:32:43Z` | 41 | SCORING_COMMIT | 2026-10-13T21:35:22Z | sn41 commit touches scoring: Adding weights version key to validator logs as a helpful indicator t… |
| `sn63:scoring_commit:2026-10-13T21:02:02Z` | 63 | SCORING_COMMIT | 2026-10-13T21:35:22Z | sn63 commit touches scoring: Track whether a terminal verify update reached the platform and HQP L… |
| `sn66:scoring_commit:2026-10-13T20:24:34Z` | 66 | SCORING_COMMIT | 2026-10-13T21:35:22Z | sn66 commit touches scoring: Port Mathlib headers to the immutable task registry and refresh hold … |
| `sn71:scoring_commit:2026-10-13T17:04:42Z` | 71 | SCORING_COMMIT | 2026-10-13T21:35:22Z | sn71 commit touches scoring: Merge pull request #415: Verify judge provider path after fifth failur |
| `sn116:release:producer-code-r8.6` | 116 | RELEASE | 2026-10-13T21:35:22Z | sn116 released producer-code-r8.6 |
| `sn120:scoring_commit:2026-10-13T18:50:26Z` | 120 | SCORING_COMMIT | 2026-10-13T21:35:22Z | sn120 commit touches scoring: Reduce hourly evidence scan cost without changing reward assessment |
| `sn7:release:release-20261013-222136` | 7 | RELEASE | 2026-10-14T00:39:12Z | sn7 released release-20261013-222136 |
| `sn7:scoring_commit:2026-10-13T21:54:01Z` | 7 | SCORING_COMMIT | 2026-10-14T00:39:12Z | sn7 commit touches scoring: Ban a miner from scoring for 12 rounds when it posts an unusable addr… |
| `sn25:scoring_commit:2026-10-13T23:48:30Z` | 25 | SCORING_COMMIT | 2026-10-14T00:39:12Z | sn25 commit touches scoring: Merge the validator test and correctness fixes: steering-limit text, … |
| `sn45:scoring_commit:2026-10-13T06:46:35Z` | 45 | SCORING_COMMIT | 2026-10-14T00:39:12Z | sn45 commit touches scoring: soak report: read rotated validator logs |
| `sn54:scoring_commit:2026-10-13T20:00:04Z` | 54 | SCORING_COMMIT | 2026-10-14T00:39:12Z | sn54 commit touches scoring: adding in query from validators |
| `sn78:scoring_commit:2026-10-14T00:18:48Z` | 78 | SCORING_COMMIT | 2026-10-14T00:39:12Z | sn78 commit touches scoring: Merge pull request #247 from Umi-BitSign/codex/c5-geometric-reward-tr… |
| `sn120:scoring_commit:2026-10-13T22:30:02Z` | 120 | SCORING_COMMIT | 2026-10-14T00:39:12Z | sn120 commit touches scoring: Reduce repeated commitment derivation in hourly reward assessment |
| `sn25:release:v2026.10.13-1071515580` | 25 | RELEASE | 2026-10-14T05:29:19Z | sn25 released v2026.10.13-1071515580 |
| `sn25:scoring_commit:2026-10-14T04:17:54Z` | 25 | SCORING_COMMIT | 2026-10-14T05:29:19Z | sn25 commit touches scoring: Merge v2/gate-miner-tests into main |
| `sn37:scoring_commit:2026-10-14T03:25:35Z` | 37 | SCORING_COMMIT | 2026-10-14T05:29:19Z | sn37 commit touches scoring: docs: describe planned stake-retention mechanism in INCENTIVES.md |
| `sn41:scoring_commit:2026-10-13T23:52:00Z` | 41 | SCORING_COMMIT | 2026-10-14T05:29:19Z | sn41 commit touches scoring: Score update |
| `sn51:scoring_commit:2026-10-14T02:31:17Z` | 51 | SCORING_COMMIT | 2026-10-14T05:29:19Z | sn51 commit touches scoring: DAH-4035 - [P0] Validator: connect to a hostname node only at a check… |
| `sn71:scoring_commit:2026-10-14T01:25:55Z` | 71 | SCORING_COMMIT | 2026-10-14T05:29:19Z | sn71 commit touches scoring: Merge pull request #418: Preserve verified headcount ranges |
| `sn76:scoring_commit:2026-10-14T05:10:32Z` | 76 | SCORING_COMMIT | 2026-10-14T05:29:19Z | sn76 commit touches scoring: security: validate repository scope before execution |
| `sn78:scoring_commit:2026-10-14T02:15:19Z` | 78 | SCORING_COMMIT | 2026-10-14T05:29:19Z | sn78 commit touches scoring: Merge pull request #248 from Umi-BitSign/codex/durable-package-verifi… |
| `sn91:scoring_commit:2026-10-14T02:36:42Z` | 91 | SCORING_COMMIT | 2026-10-14T05:29:19Z | sn91 commit touches scoring: fix(validator): carry staged promotions across a dethrone (DEC-CA-005… |
| `sn116:scoring_commit:2026-10-14T01:37:24Z` | 116 | SCORING_COMMIT | 2026-10-14T05:29:19Z | sn116 commit touches scoring: Merge pull request #1335 from carbonphysicsai/codex/opt15c-score-lab-… |
| `sn25:release:v2026.10.14-1071632750` | 25 | RELEASE | 2026-10-14T10:39:10Z | sn25 released v2026.10.14-1071632750 |
| `sn51:scoring_commit:2026-10-14T08:21:57Z` | 51 | SCORING_COMMIT | 2026-10-14T10:39:10Z | sn51 commit touches scoring: DAH-4270 - [P1] Validator: count rented nodes the miner leaves out (s… |
| `sn67:scoring_commit:2026-10-14T06:48:35Z` | 67 | SCORING_COMMIT | 2026-10-14T10:39:10Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20261014.post3 |
| `sn71:scoring_commit:2026-10-14T09:50:39Z` | 71 | SCORING_COMMIT | 2026-10-14T10:39:10Z | sn71 commit touches scoring: Merge PR #432: repair verified domain conflicts before rebrand invest… |
| `sn76:scoring_commit:2026-10-14T06:05:09Z` | 76 | SCORING_COMMIT | 2026-10-14T10:39:10Z | sn76 commit touches scoring: security: repair frozen verifier snapshot |
| `sn78:scoring_commit:2026-10-14T06:12:46Z` | 78 | SCORING_COMMIT | 2026-10-14T10:39:10Z | sn78 commit touches scoring: Preserve native reward history through writer preparation and cutover |
| `sn108:scoring_commit:2026-10-14T09:43:47Z` | 108 | SCORING_COMMIT | 2026-10-14T10:39:10Z | sn108 commit touches scoring: Validator sends its EDA server the batch's time: time_limit_s (deadli… |
| `sn116:release:r8.7` | 116 | RELEASE | 2026-10-14T10:39:10Z | sn116 released r8.7 |
| `sn117:release:everycli v0.5.1` | 117 | RELEASE | 2026-10-14T10:39:10Z | sn117 released everycli v0.5.1 |
| `sn117:scoring_commit:2026-10-14T09:42:22Z` | 117 | SCORING_COMMIT | 2026-10-14T10:39:10Z | sn117 commit touches scoring: docs: align miner README with v0.5.1 setup and lifecycle (#29) |
| `sn51:scoring_commit:2026-10-14T14:13:17Z` | 51 | SCORING_COMMIT | 2026-10-14T15:33:11Z | sn51 commit touches scoring: DAH-4035 - [P1] Validator: resolve hostname nodes in their own thread… |
| `sn66:scoring_commit:2026-10-14T10:04:47Z` | 66 | SCORING_COMMIT | 2026-10-14T15:33:11Z | sn66 commit touches scoring: feat: extend leaderboard endpoint (add past champions challengers his… |
| `sn71:scoring_commit:2026-10-14T14:16:53Z` | 71 | SCORING_COMMIT | 2026-10-14T15:33:11Z | sn71 commit touches scoring: Merge PR #434: retain bounded validator error causes |
| `sn116:scoring_commit:2026-10-14T12:47:36Z` | 116 | SCORING_COMMIT | 2026-10-14T15:33:11Z | sn116 commit touches scoring: Merge pull request #1347 from carbonphysicsai/codex/incentive-observe… |
| `sn117:release:everycli v0.5.4` | 117 | RELEASE | 2026-10-14T15:33:11Z | sn117 released everycli v0.5.4 |
| `sn117:scoring_commit:2026-10-14T12:01:19Z` | 117 | SCORING_COMMIT | 2026-10-14T15:33:11Z | sn117 commit touches scoring: fix: profile reconnect and miner dashboard identity (v0.5.2) (#30) |
| `sn14:scoring_commit:2026-10-14T19:21:08Z` | 14 | SCORING_COMMIT | 2026-10-14T19:44:42Z | sn14 commit touches scoring: Show evaluator activity from the current worker heartbeat (#150) |
| `sn28:release:v0.4.29-dev` | 28 | RELEASE | 2026-10-14T19:44:42Z | sn28 released v0.4.29-dev |
| `sn28:scoring_commit:2026-10-14T18:30:19Z` | 28 | SCORING_COMMIT | 2026-10-14T19:44:42Z | sn28 commit touches scoring: chore(release): gm-miner 0.4.29-dev (#320) |
| `sn51:scoring_commit:2026-10-14T18:37:43Z` | 51 | SCORING_COMMIT | 2026-10-14T19:44:42Z | sn51 commit touches scoring: NO-TICKET - validator: the spot pay flag is named for the backend's p… |
| `sn76:scoring_commit:2026-10-14T18:51:37Z` | 76 | SCORING_COMMIT | 2026-10-14T19:44:42Z | sn76 commit touches scoring: security: harden public miner and validator boundaries |
| `sn78:scoring_commit:2026-10-14T16:40:24Z` | 78 | SCORING_COMMIT | 2026-10-14T19:44:42Z | sn78 commit touches scoring: Merge pull request #252 from Umi-BitSign/codex/header-verification-ca… |
| `sn96:scoring_commit:2026-10-14T19:13:46Z` | 96 | SCORING_COMMIT | 2026-10-14T19:44:42Z | sn96 commit touches scoring: fix: move the Decide validator handover to block 9,287,280 |
| `sn116:scoring_commit:2026-10-14T19:19:20Z` | 116 | SCORING_COMMIT | 2026-10-14T19:44:42Z | sn116 commit touches scoring: Merge pull request #1354 from carbonphysicsai/codex/v8-8-validator-set |
| `sn117:release:everycli v0.5.5` | 117 | RELEASE | 2026-10-14T19:44:42Z | sn117 released everycli v0.5.5 |
| `sn117:scoring_commit:2026-10-14T15:53:23Z` | 117 | SCORING_COMMIT | 2026-10-14T19:44:42Z | sn117 commit touches scoring: fix: streamline model offers and miner dashboard reporting (#33) |
| `sn21:scoring_commit:2026-10-14T20:58:47Z` | 21 | SCORING_COMMIT | 2026-10-14T22:42:49Z | sn21 commit touches scoring: perf(scoring): read receipts through a small per-day standing index |
| `sn25:scoring_commit:2026-10-14T21:15:56Z` | 25 | SCORING_COMMIT | 2026-10-14T22:42:49Z | sn25 commit touches scoring: State that any v2 request checkpoint write blocks a validator downgrad |
| `sn28:release:v0.5.0` | 28 | RELEASE | 2026-10-14T22:42:49Z | sn28 released v0.5.0 |
| `sn28:scoring_commit:2026-10-14T21:33:01Z` | 28 | SCORING_COMMIT | 2026-10-14T22:42:49Z | sn28 commit touches scoring: chore(release): promote gm-miner 0.5.0 (#322) |
| `sn78:scoring_commit:2026-10-14T22:06:52Z` | 78 | SCORING_COMMIT | 2026-10-14T22:42:49Z | sn78 commit touches scoring: Keep stopped reward reconciliation alive across native history batches |
| `sn116:scoring_commit:2026-10-14T22:11:40Z` | 116 | SCORING_COMMIT | 2026-10-14T22:42:49Z | sn116 commit touches scoring: Merge pull request #1365 from carbonphysicsai/codex/score-lab-champio… |
| `sn117:release:everycli v0.5.6` | 117 | RELEASE | 2026-10-14T22:42:49Z | sn117 released everycli v0.5.6 |
| `sn120:scoring_commit:2026-10-14T20:48:32Z` | 120 | SCORING_COMMIT | 2026-10-14T22:42:49Z | sn120 commit touches scoring: Award contested tasks to the earliest Cloudflare R2 claim |
| `sn8:scoring_commit:2026-10-14T22:26:16Z` | 8 | SCORING_COMMIT | 2026-10-15T00:57:43Z | sn8 commit touches scoring: Sync price updates and challenge loop (#954) |
| `sn25:scoring_commit:2026-10-15T00:43:14Z` | 25 | SCORING_COMMIT | 2026-10-15T00:57:43Z | sn25 commit touches scoring: Select the startup verified tests and pin the memo's replay edge |
| `sn15:release:v2.5.2` | 15 | RELEASE | 2026-10-15T05:51:38Z | sn15 released v2.5.2 |
| `sn15:scoring_commit:2026-10-15T05:19:00Z` | 15 | SCORING_COMMIT | 2026-10-15T05:51:38Z | sn15 commit touches scoring: Treat a miner's OpenRouter credit 402 as an exhausted run key (#374) |
| `sn25:scoring_commit:2026-10-15T04:12:02Z` | 25 | SCORING_COMMIT | 2026-10-15T05:51:38Z | sn25 commit touches scoring: Update the SN25 timeline with the validator operator's answers |
| `sn51:scoring_commit:2026-10-15T04:20:45Z` | 51 | SCORING_COMMIT | 2026-10-15T05:51:38Z | sn51 commit touches scoring: DAH-4071 - [P1] validator: SCORING_EXCLUDED_HOTKEYS, listed hotkeys e… |
| `sn67:scoring_commit:2026-10-14T14:32:28Z` | 67 | SCORING_COMMIT | 2026-10-15T05:51:38Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20261014.post6 |
| `sn78:scoring_commit:2026-10-15T05:43:45Z` | 78 | SCORING_COMMIT | 2026-10-15T05:51:38Z | sn78 commit touches scoring: Merge pull request #266 from Umi-BitSign/codex/verified-checkpoint-ex… |
| `sn116:scoring_commit:2026-10-15T04:30:56Z` | 116 | SCORING_COMMIT | 2026-10-15T05:51:38Z | sn116 commit touches scoring: Merge pull request #1371 from carbonphysicsai/codex/scorelab-referenc… |
| `sn3:scoring_commit:2026-10-15T11:18:15Z` | 3 | SCORING_COMMIT | 2026-10-15T11:20:44Z | sn3 commit touches scoring: Optimize evaluator model loading by broadcasting weights to GPU replic |
| `sn14:scoring_commit:2026-10-15T10:47:18Z` | 14 | SCORING_COMMIT | 2026-10-15T11:20:44Z | sn14 commit touches scoring: Resume checkpointed evaluations across GPU worker replacement (#151) |
| `sn25:scoring_commit:2026-10-15T08:24:53Z` | 25 | SCORING_COMMIT | 2026-10-15T11:20:44Z | sn25 commit touches scoring: Verify the begun intent before the receipt outage test's timed poll |
| `sn51:scoring_commit:2026-10-15T10:55:56Z` | 51 | SCORING_COMMIT | 2026-10-15T11:20:44Z | sn51 commit touches scoring: validator: name the reason when a rented node scores 0 because Sysbox… |
| `sn67:scoring_commit:2026-10-15T02:32:18Z` | 67 | SCORING_COMMIT | 2026-10-15T11:20:44Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20261015.post0 |
| `sn78:scoring_commit:2026-10-15T08:44:03Z` | 78 | SCORING_COMMIT | 2026-10-15T11:20:44Z | sn78 commit touches scoring: Preserve nested history profile aliases when starting rewards |
| `sn81:scoring_commit:2026-10-14T10:33:36Z` | 81 | SCORING_COMMIT | 2026-10-15T11:20:44Z | sn81 commit touches scoring: test(corpus): the signed-sandbox restart e2e serves period-settled tas |
| `sn89:scoring_commit:2026-10-15T07:37:15Z` | 89 | SCORING_COMMIT | 2026-10-15T11:20:44Z | sn89 commit touches scoring: HF warmup dust: not-yet-eligible HF miners hold DUST_WEIGHT for 8 day… |
| `sn116:scoring_commit:2026-10-15T05:37:59Z` | 116 | SCORING_COMMIT | 2026-10-15T11:20:44Z | sn116 commit touches scoring: Expose battery scorer initializer closure as unproved |
| `sn3:scoring_commit:2026-10-15T12:45:19Z` | 3 | SCORING_COMMIT | 2026-10-15T15:41:01Z | sn3 commit touches scoring: Optimize evaluator dataset downloads with authenticated R2 reads and … |
| `sn10:scoring_commit:2026-10-15T11:54:42Z` | 10 | SCORING_COMMIT | 2026-10-15T15:41:01Z | sn10 commit touches scoring: fix(score): charge short completions at full length in tier timing (#… |
| `sn18:scoring_commit:2026-10-15T11:51:02Z` | 18 | SCORING_COMMIT | 2026-10-15T15:41:01Z | sn18 commit touches scoring: change reward function to win rate (#92) |
| `sn25:release:v2026.10.15-1072765730` | 25 | RELEASE | 2026-10-15T15:41:01Z | sn25 released v2026.10.15-1072765730 |
| `sn25:scoring_commit:2026-10-15T14:28:03Z` | 25 | SCORING_COMMIT | 2026-10-15T15:41:01Z | sn25 commit touches scoring: Merge v2/cheaper-validator-production-tests into main |
| `sn71:scoring_commit:2026-10-15T12:43:48Z` | 71 | SCORING_COMMIT | 2026-10-15T15:41:01Z | sn71 commit touches scoring: Merge pull request #461: broker diagnostics and protected scorer mani… |
| `sn78:scoring_commit:2026-10-15T11:26:49Z` | 78 | SCORING_COMMIT | 2026-10-15T15:41:01Z | sn78 commit touches scoring: Reuse parsed packages across independently verified stored copies |
| `sn92:release:v1.2.0-rc2` | 92 | RELEASE | 2026-10-15T15:41:01Z | sn92 released v1.2.0-rc2 |
| `sn92:scoring_commit:2026-10-15T13:20:37Z` | 92 | SCORING_COMMIT | 2026-10-15T15:41:01Z | sn92 commit touches scoring: tests: tier/split tests keep synthetic track scores floor-free |
| `sn102:release:v0.7.0` | 102 | RELEASE | 2026-10-15T15:41:01Z | sn102 released v0.7.0 |
| `sn102:scoring_commit:2026-10-14T17:10:14Z` | 102 | SCORING_COMMIT | 2026-10-15T15:41:01Z | sn102 commit touches scoring: 📝 docs(miner-faq): base usage varies a little more on c4 than on task… |
| `sn116:scoring_commit:2026-10-15T13:57:09Z` | 116 | SCORING_COMMIT | 2026-10-15T15:41:01Z | sn116 commit touches scoring: Merge pull request #1377 from carbonphysicsai/codex/scorelab-complete… |
| `sn7:release:release-20261015-164605: Gate quotes and` | 7 | RELEASE | 2026-10-15T19:27:45Z | sn7 released release-20261015-164605: Gate quotes and crown reconcile on the offer's own backing bit (#772) |
| `sn9:release:v4.13.7` | 9 | RELEASE | 2026-10-15T19:27:45Z | sn9 released v4.13.7 |
| `sn15:release:v2.5.3` | 15 | RELEASE | 2026-10-15T19:27:45Z | sn15 released v2.5.3 |
| `sn25:scoring_commit:2026-10-15T16:11:13Z` | 25 | SCORING_COMMIT | 2026-10-15T19:27:45Z | sn25 commit touches scoring: Merge test/validator-crash-loop-root-cause into main |
| `sn28:release:v0.5.1-dev` | 28 | RELEASE | 2026-10-15T19:27:45Z | sn28 released v0.5.1-dev |
| `sn51:release:executor-v1.141` | 51 | RELEASE | 2026-10-15T19:27:45Z | sn51 released executor-v1.141 |
| `sn51:scoring_commit:2026-10-15T17:07:10Z` | 51 | SCORING_COMMIT | 2026-10-15T19:27:45Z | sn51 commit touches scoring: DAH-4465 validator: fail an unrented node whose busy GPU is thermally… |
| `sn78:scoring_commit:2026-10-15T19:16:31Z` | 78 | SCORING_COMMIT | 2026-10-15T19:27:45Z | sn78 commit touches scoring: Reuse verified host and OCI identities during worker reconciliation |
| `sn92:release:v1.2.0-rc3` | 92 | RELEASE | 2026-10-15T19:27:45Z | sn92 released v1.2.0-rc3 |
| `sn92:scoring_commit:2026-10-15T15:10:01Z` | 92 | SCORING_COMMIT | 2026-10-15T19:27:45Z | sn92 commit touches scoring: tiers: keep the per-miner tier-order rule (H3); s1-lite / s1-cpu max_… |
| `sn116:release:Carbon worker images v4` | 116 | RELEASE | 2026-10-15T19:27:45Z | sn116 released Carbon worker images v4 |
| `sn116:scoring_commit:2026-10-15T19:09:06Z` | 116 | SCORING_COMMIT | 2026-10-15T19:27:45Z | sn116 commit touches scoring: Merge pull request #1383 from carbonphysicsai/codex/scorelab-v3-calib… |
| `sn7:release:release-20261015-220818: Quote the min f` | 7 | RELEASE | 2026-10-15T22:39:09Z | sn7 released release-20261015-220818: Quote the min for alpha pairs from each candidate's floor (#775) |
| `sn7:scoring_commit:2026-10-15T21:59:48Z` | 7 | SCORING_COMMIT | 2026-10-15T22:39:09Z | sn7 commit touches scoring: Quote /rate from held miner states and a lazy market memo (#774) |
| `sn25:release:v2026.10.15-1072937160` | 25 | RELEASE | 2026-10-15T22:39:09Z | sn25 released v2026.10.15-1072937160 |
| `sn71:scoring_commit:2026-10-15T20:53:09Z` | 71 | SCORING_COMMIT | 2026-10-15T22:39:09Z | sn71 commit touches scoring: Fix Arena progression lock order and close legacy scoring RPC access |
| `sn78:scoring_commit:2026-10-15T19:35:00Z` | 78 | SCORING_COMMIT | 2026-10-15T22:39:09Z | sn78 commit touches scoring: Overlap retained history loading with bounded native verification |
| `sn92:release:v1.2.0-rc4` | 92 | RELEASE | 2026-10-15T22:39:09Z | sn92 released v1.2.0-rc4 |
| `sn92:scoring_commit:2026-10-15T19:21:22Z` | 92 | SCORING_COMMIT | 2026-10-15T22:39:09Z | sn92 commit touches scoring: probe: open each UID's window at the validator's first send to it; la… |
| `sn116:scoring_commit:2026-10-15T20:45:43Z` | 116 | SCORING_COMMIT | 2026-10-15T22:39:09Z | sn116 commit touches scoring: Verify persisted contract record through submission guards |
| `sn117:release:everycli v0.5.7` | 117 | RELEASE | 2026-10-15T22:39:09Z | sn117 released everycli v0.5.7 |
| `sn25:release:v2026.10.15-1073082520` | 25 | RELEASE | 2026-10-16T00:49:24Z | sn25 released v2026.10.15-1073082520 |
| `sn37:scoring_commit:2026-10-16T00:31:00Z` | 37 | SCORING_COMMIT | 2026-10-16T00:49:24Z | sn37 commit touches scoring: fix(miner): support reviewed mainnet runtime479 (#30) |
| `sn116:scoring_commit:2026-10-16T00:40:42Z` | 116 | SCORING_COMMIT | 2026-10-16T00:49:24Z | sn116 commit touches scoring: Merge pull request #1393 from carbonphysicsai/codex/scorelab-guarded4… |
| `sn25:release:v2026.10.15-1073121200` | 25 | RELEASE | 2026-10-16T05:47:49Z | sn25 released v2026.10.15-1073121200 |
| `sn51:scoring_commit:2026-10-16T02:57:37Z` | 51 | SCORING_COMMIT | 2026-10-16T05:47:49Z | sn51 commit touches scoring: DAH-3980 - Validator: new loopback volumes on a v2 plugin installed b… |
| `sn71:scoring_commit:2026-10-16T04:40:16Z` | 71 | SCORING_COMMIT | 2026-10-16T05:47:49Z | sn71 commit touches scoring: Verify failed fallback stays an infrastructure error |
| `sn78:scoring_commit:2026-10-16T03:44:01Z` | 78 | SCORING_COMMIT | 2026-10-16T05:47:49Z | sn78 commit touches scoring: Reuse verified semantics for authenticated sealed package copies |
| `sn81:scoring_commit:2026-10-15T10:03:46Z` | 81 | SCORING_COMMIT | 2026-10-16T05:47:49Z | sn81 commit touches scoring: fix(corpus): serve signed jobs from the split validator's front |
| `sn91:scoring_commit:2026-10-16T02:59:40Z` | 91 | SCORING_COMMIT | 2026-10-16T05:47:49Z | sn91 commit touches scoring: Pin the best-bench round in the receipt index so the scoreboard's bes… |
| `sn94:scoring_commit:2026-10-16T03:19:42Z` | 94 | SCORING_COMMIT | 2026-10-16T05:47:49Z | sn94 commit touches scoring: Merge pull request #281 from cathedralai/docs/sn94-snp-miner-dd7182c |
| `sn116:scoring_commit:2026-10-16T04:42:09Z` | 116 | SCORING_COMMIT | 2026-10-16T05:47:49Z | sn116 commit touches scoring: Merge pull request #1401 from carbonphysicsai/codex/scorelab-guard419… |
| `sn51:scoring_commit:2026-10-16T06:29:35Z` | 51 | SCORING_COMMIT | 2026-10-16T10:10:43Z | sn51 commit touches scoring: DAH-4362 - [P3] Validator: remove settings unchanged for more than 3 … |
| `sn71:scoring_commit:2026-10-16T09:32:28Z` | 71 | SCORING_COMMIT | 2026-10-16T10:10:43Z | sn71 commit touches scoring: Merge pull request #489 from leadpoet/fix/validator-run-recovery-scop… |
| `sn78:scoring_commit:2026-10-16T04:36:39Z` | 78 | SCORING_COMMIT | 2026-10-16T10:10:43Z | sn78 commit touches scoring: Add read-only retained miner revision preflight |
| `sn116:scoring_commit:2026-10-16T07:49:42Z` | 116 | SCORING_COMMIT | 2026-10-16T10:10:43Z | sn116 commit touches scoring: Merge pull request #1404 from carbonphysicsai/codex/scorelab-guarded4… |
| `sn1:release:v4.4.13` | 1 | RELEASE | 2026-10-16T14:58:20Z | sn1 released v4.4.13 |
| `sn21:scoring_commit:2026-10-16T12:06:08Z` | 21 | SCORING_COMMIT | 2026-10-16T14:58:20Z | sn21 commit touches scoring: scoring: an entry without a measurable efficiency is scored on cost a… |
| `sn51:scoring_commit:2026-10-16T14:00:51Z` | 51 | SCORING_COMMIT | 2026-10-16T14:58:20Z | sn51 commit touches scoring: DAH-4123 - Validator: split build-log streams into frames the backend… |
| `sn67:scoring_commit:2026-10-16T11:32:32Z` | 67 | SCORING_COMMIT | 2026-10-16T14:58:20Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20261016.post1 |
| `sn78:scoring_commit:2026-10-16T13:20:49Z` | 78 | SCORING_COMMIT | 2026-10-16T14:58:20Z | sn78 commit touches scoring: Adopt qualified reward runtimes without resetting signed coverage |
| `sn90:scoring_commit:2026-10-16T10:16:08Z` | 90 | SCORING_COMMIT | 2026-10-16T14:58:20Z | sn90 commit touches scoring: docs(subnet): README model lists + validator stats sync |
| `sn92:scoring_commit:2026-10-16T10:25:45Z` | 92 | SCORING_COMMIT | 2026-10-16T14:58:20Z | sn92 commit touches scoring: engine track: protect pending challenger, same-cycle fresh-session co… |
| `sn100:scoring_commit:2026-10-16T13:16:02Z` | 100 | SCORING_COMMIT | 2026-10-16T14:58:20Z | sn100 commit touches scoring: fix(challenges): raise get_weights timeout to 180 seconds (#318) |
| `sn114:scoring_commit:2026-10-16T11:35:50Z` | 114 | SCORING_COMMIT | 2026-10-16T14:58:20Z | sn114 commit touches scoring: update scoring.md docs |
| `sn116:scoring_commit:2026-10-16T10:36:39Z` | 116 | SCORING_COMMIT | 2026-10-16T14:58:20Z | sn116 commit touches scoring: Merge pull request #1405 from carbonphysicsai/codex/scorelab-guarded4… |
| `sn71:scoring_commit:2026-10-16T18:40:01Z` | 71 | SCORING_COMMIT | 2026-10-16T18:46:43Z | sn71 commit touches scoring: Allow selected frozen executions in isolated shadow verification (#493 |
| `sn92:release:v1.2.0-rc6` | 92 | RELEASE | 2026-10-16T18:46:43Z | sn92 released v1.2.0-rc6 |
| `sn102:scoring_commit:2026-10-15T19:51:21Z` | 102 | SCORING_COMMIT | 2026-10-16T18:46:43Z | sn102 commit touches scoring: ✅ test(validator): after a skipped round, stale weights take the fall… |
| `sn116:scoring_commit:2026-10-16T13:41:47Z` | 116 | SCORING_COMMIT | 2026-10-16T18:46:43Z | sn116 commit touches scoring: test(launchpad): bind retain policy fixture to registered challenge |
| `sn121:scoring_commit:2026-10-16T15:26:35Z` | 121 | SCORING_COMMIT | 2026-10-16T18:46:43Z | sn121 commit touches scoring: Update README for skill bundles, the leadership margin and a Discord F |
| `sn25:release:v2026.10.16-1073843780` | 25 | RELEASE | 2026-10-16T21:47:16Z | sn25 released v2026.10.16-1073843780 |
| `sn25:scoring_commit:2026-10-16T19:01:39Z` | 25 | SCORING_COMMIT | 2026-10-16T21:47:16Z | sn25 commit touches scoring: Authenticate finalized chain absence before revoking validator eligib… |
| `sn71:scoring_commit:2026-10-16T19:32:25Z` | 71 | SCORING_COMMIT | 2026-10-16T21:47:16Z | sn71 commit touches scoring: Select verified homepage profile for unbound size citations (#496) |
| `sn91:scoring_commit:2026-10-16T20:57:49Z` | 91 | SCORING_COMMIT | 2026-10-16T21:47:16Z | sn91 commit touches scoring: Merge pull request #370 from TensorLink-AI/docs/miner-admission-guard |
| `sn92:release:v1.2.0-rc7` | 92 | RELEASE | 2026-10-16T21:47:16Z | sn92 released v1.2.0-rc7 |
| `sn102:release:v0.7.1` | 102 | RELEASE | 2026-10-16T21:47:16Z | sn102 released v0.7.1 |
| `sn116:scoring_commit:2026-10-16T20:22:44Z` | 116 | SCORING_COMMIT | 2026-10-16T21:47:16Z | sn116 commit touches scoring: Merge pull request #1408 from carbonphysicsai/codex/gpu-miner-control… |
| `sn25:release:v2026.10.16-1073891640` | 25 | RELEASE | 2026-10-16T23:59:25Z | sn25 released v2026.10.16-1073891640 |
| `sn71:scoring_commit:2026-10-16T23:28:33Z` | 71 | SCORING_COMMIT | 2026-10-16T23:59:25Z | sn71 commit touches scoring: Move scorer checkpoint and output IO behind runtime interface |
| `sn78:scoring_commit:2026-10-16T22:57:25Z` | 78 | SCORING_COMMIT | 2026-10-16T23:59:25Z | sn78 commit touches scoring: Score original forecast ranges and retain comparable outcome evidence |
| `sn116:release:worker-images-v5 (DEVELOPMENT)` | 116 | RELEASE | 2026-10-16T23:59:25Z | sn116 released worker-images-v5 (DEVELOPMENT) |
| `sn116:scoring_commit:2026-10-16T20:58:13Z` | 116 | SCORING_COMMIT | 2026-10-16T23:59:25Z | sn116 commit touches scoring: Format F06 Challenge registry assertions |
| `sn25:release:v2026.10.16-1074037020` | 25 | RELEASE | 2026-10-17T04:17:15Z | sn25 released v2026.10.16-1074037020 |
| `sn71:scoring_commit:2026-10-17T01:24:18Z` | 71 | SCORING_COMMIT | 2026-10-17T04:17:15Z | sn71 commit touches scoring: Merge current main and validate selected judge runtime in training ex… |
| `sn91:scoring_commit:2026-10-17T01:20:18Z` | 91 | SCORING_COMMIT | 2026-10-17T04:17:15Z | sn91 commit touches scoring: fix(promotion): anchor the trainer's reign clock where validators res… |
| `sn92:release:v1.2.0-rc7.post1` | 92 | RELEASE | 2026-10-17T04:17:15Z | sn92 released v1.2.0-rc7.post1 |
| `sn15:release:v2.5.5: Bound validator reads of sandbox` | 15 | RELEASE | 2026-10-17T08:43:24Z | sn15 released v2.5.5: Bound validator reads of sandbox output files (#378) |
| `sn15:scoring_commit:2026-10-17T07:52:59Z` | 15 | SCORING_COMMIT | 2026-10-17T08:43:24Z | sn15 commit touches scoring: Bound validator reads of sandbox output files (#378) |
| `sn25:release:v2026.10.16-1074191560` | 25 | RELEASE | 2026-10-17T08:43:24Z | sn25 released v2026.10.16-1074191560 |
| `sn37:scoring_commit:2026-10-17T05:44:48Z` | 37 | SCORING_COMMIT | 2026-10-17T08:43:24Z | sn37 commit touches scoring: fix(miner): enable reviewed runtime479 funding (#31) |
| `sn51:scoring_commit:2026-10-17T08:20:58Z` | 51 | SCORING_COMMIT | 2026-10-17T08:43:24Z | sn51 commit touches scoring: DAH-4280 - [P0] Validator: cross-check the reported GPU count against… |
| `sn71:scoring_commit:2026-10-17T06:44:45Z` | 71 | SCORING_COMMIT | 2026-10-17T08:43:24Z | sn71 commit touches scoring: fix(arena): retain verified source redirects for fallback (#519) |
| `sn78:scoring_commit:2026-10-17T06:12:23Z` | 78 | SCORING_COMMIT | 2026-10-17T08:43:24Z | sn78 commit touches scoring: Merge pull request #294 from Umi-BitSign/codex/c6-portable-byte-verif… |
| `sn92:release:v1.2.0-rc7.post3` | 92 | RELEASE | 2026-10-17T08:43:24Z | sn92 released v1.2.0-rc7.post3 |
| `sn108:scoring_commit:2026-10-16T09:36:40Z` | 108 | SCORING_COMMIT | 2026-10-17T08:43:24Z | sn108 commit touches scoring: Validators don't pay records the server marks banned (coldkey banned … |
| `sn116:scoring_commit:2026-10-17T04:56:00Z` | 116 | SCORING_COMMIT | 2026-10-17T08:43:24Z | sn116 commit touches scoring: Merge pull request #1416 from carbonphysicsai/codex/s5-challenge-sele… |
| `sn21:scoring_commit:2026-10-17T11:22:46Z` | 21 | SCORING_COMMIT | 2026-10-17T12:28:43Z | sn21 commit touches scoring: feat(scoring): absence charges stop once a hotkey holds no real entry… |
| `sn25:release:v2026.10.17-1074370910` | 25 | RELEASE | 2026-10-17T12:28:43Z | sn25 released v2026.10.17-1074370910 |
| `sn51:release:executor-v1.142` | 51 | RELEASE | 2026-10-17T12:28:43Z | sn51 released executor-v1.142 |
| `sn51:scoring_commit:2026-10-17T11:57:18Z` | 51 | SCORING_COMMIT | 2026-10-17T12:28:43Z | sn51 commit touches scoring: Sysbox installer: show the verify container's error when step 6 fails… |
| `sn92:release:v1.2.0-rc7.post4` | 92 | RELEASE | 2026-10-17T12:28:43Z | sn92 released v1.2.0-rc7.post4 |
| `sn7:release:release-20261017-152034: Bound event ing` | 7 | RELEASE | 2026-10-17T15:58:40Z | sn7 released release-20261017-152034: Bound event ingest per pass and cap its lookback at 6h (#792) |
| `sn28:release:v0.5.2` | 28 | RELEASE | 2026-10-17T15:58:40Z | sn28 released v0.5.2 |
| `sn28:scoring_commit:2026-10-17T13:33:09Z` | 28 | SCORING_COMMIT | 2026-10-17T15:58:40Z | sn28 commit touches scoring: chore(release): promote gm-miner 0.5.2 (#327) |
| `sn51:scoring_commit:2026-10-17T12:38:54Z` | 51 | SCORING_COMMIT | 2026-10-17T15:58:40Z | sn51 commit touches scoring: DAH-4601 - [P0] Validator: fail a node where sshd does not start in t… |
| `sn92:release:v1.2.0-rc8` | 92 | RELEASE | 2026-10-17T15:58:40Z | sn92 released v1.2.0-rc8 |
| `sn41:scoring_commit:2026-10-17T16:02:48Z` | 41 | SCORING_COMMIT | 2026-10-17T18:25:49Z | sn41 commit touches scoring: Merge pull request #59 from corvxai/vali_no_assign_before_scoring |
| `sn78:scoring_commit:2026-10-17T17:36:20Z` | 78 | SCORING_COMMIT | 2026-10-17T18:25:49Z | sn78 commit touches scoring: Backport current reward coverage capture to exact C5 runtime |
| `sn91:scoring_commit:2026-10-17T20:13:24Z` | 91 | SCORING_COMMIT | 2026-10-17T20:51:47Z | sn91 commit touches scoring: Merge pull request #373 from TensorLink-AI/feat/payer-bench-unverified |
| `sn51:release:miner-v1.006` | 51 | RELEASE | 2026-10-17T23:04:30Z | sn51 released miner-v1.006 |
| `sn51:scoring_commit:2026-10-17T21:06:14Z` | 51 | SCORING_COMMIT | 2026-10-17T23:04:30Z | sn51 commit touches scoring: DAH-4539 - Miner: a portal delete removes only the node it names (#166 |
| `sn78:scoring_commit:2026-10-17T21:58:15Z` | 78 | SCORING_COMMIT | 2026-10-17T23:04:30Z | sn78 commit touches scoring: Recover historical reward coverage gaps from durable native endpoints |
| `sn15:release:v2.5.6: Bound per-evaluation sandbox dis` | 15 | RELEASE | 2026-10-18T00:59:01Z | sn15 released v2.5.6: Bound per-evaluation sandbox disk use |
| `sn15:scoring_commit:2026-10-17T23:22:22Z` | 15 | SCORING_COMMIT | 2026-10-18T00:59:01Z | sn15 commit touches scoring: Bound per-evaluation sandbox disk use |
| `sn15:scoring_commit:2026-10-18T05:27:40Z` | 15 | SCORING_COMMIT | 2026-10-18T05:49:20Z | sn15 commit touches scoring: fix(validator): send sandbox_metadata when retrying a completion (#352 |
| `sn25:release:v2026.10.17-1074871400` | 25 | RELEASE | 2026-10-18T05:49:20Z | sn25 released v2026.10.17-1074871400 |
| `sn53:scoring_commit:2026-10-18T04:05:58Z` | 53 | SCORING_COMMIT | 2026-10-18T05:49:20Z | sn53 commit touches scoring: tee_miner: default to half the legs on the LB, half on Cloudflare, sh… |
| `sn55:scoring_commit:2026-10-18T05:30:43Z` | 55 | SCORING_COMMIT | 2026-10-18T05:49:20Z | sn55 commit touches scoring: set weights using valid scores |
| `sn71:scoring_commit:2026-10-18T01:41:09Z` | 71 | SCORING_COMMIT | 2026-10-18T05:49:20Z | sn71 commit touches scoring: Prune superseded Deepline score billing heads before V3 candidate wor… |
| `sn15:scoring_commit:2026-10-18T06:23:50Z` | 15 | SCORING_COMMIT | 2026-10-18T10:56:59Z | sn15 commit touches scoring: docs: update stale pack digest and runtime in miner-guide sample run … |
| `sn71:scoring_commit:2026-10-18T06:55:55Z` | 71 | SCORING_COMMIT | 2026-10-18T10:56:59Z | sn71 commit touches scoring: fix(arena): classify unavailable frozen score routes before dispatch |
| `sn116:scoring_commit:2026-10-17T23:42:51Z` | 116 | SCORING_COMMIT | 2026-10-18T10:56:59Z | sn116 commit touches scoring: docs: lock bank-version reuse and reward-clock safeguards |
| `sn67:scoring_commit:2026-10-18T12:04:24Z` | 67 | SCORING_COMMIT | 2026-10-18T14:32:37Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20261018.post0 |
| `sn66:scoring_commit:2026-10-18T16:02:02Z` | 66 | SCORING_COMMIT | 2026-10-18T17:34:40Z | sn66 commit touches scoring: Activate the Mathlib header task release |
| `sn116:scoring_commit:2026-10-18T16:35:31Z` | 116 | SCORING_COMMIT | 2026-10-18T17:34:40Z | sn116 commit touches scoring: Merge pull request #1423 from carbonphysicsai/codex/scorelab-dual-del… |
| `sn117:readme_task_diff:0f4be566c399b388` | 117 | README_TASK_DIFF | 2026-10-11T23:13:02Z | sn117 README task/scoring sections changed |
| `sn28:readme_task_diff:a275dd150e9b5f4f` | 28 | README_TASK_DIFF | 2026-10-12T19:47:00Z | sn28 README task/scoring sections changed |
| `sn117:readme_task_diff:4631619b61bf245f` | 117 | README_TASK_DIFF | 2026-10-12T19:47:00Z | sn117 README task/scoring sections changed |
| `sn117:readme_task_diff:98a036ed300e2537` | 117 | README_TASK_DIFF | 2026-10-13T08:31:47Z | sn117 README task/scoring sections changed |
| `sn37:readme_task_diff:f7819507937d66e4` | 37 | README_TASK_DIFF | 2026-10-13T16:29:14Z | sn37 README task/scoring sections changed |
| `sn117:readme_task_diff:0955f3d4e32cce12` | 117 | README_TASK_DIFF | 2026-10-13T16:29:14Z | sn117 README task/scoring sections changed |
| `sn117:readme_task_diff:a5f1105da1e310ab` | 117 | README_TASK_DIFF | 2026-10-13T21:35:22Z | sn117 README task/scoring sections changed |
| `sn37:readme_task_diff:6ee01103ec5344ac` | 37 | README_TASK_DIFF | 2026-10-14T05:29:19Z | sn37 README task/scoring sections changed |
| `sn117:readme_task_diff:ffe23d677b34cef6` | 117 | README_TASK_DIFF | 2026-10-14T19:44:42Z | sn117 README task/scoring sections changed |
| `sn117:readme_task_diff:e92bc71aef91f2cd` | 117 | README_TASK_DIFF | 2026-10-14T22:42:49Z | sn117 README task/scoring sections changed |
| `sn37:readme_task_diff:8fd038bdd4d28f3e` | 37 | README_TASK_DIFF | 2026-10-16T00:49:24Z | sn37 README task/scoring sections changed |
| `sn90:readme_task_diff:31c270cb714e86fe` | 90 | README_TASK_DIFF | 2026-10-16T14:58:20Z | sn90 README task/scoring sections changed |
| `sn121:readme_task_diff:3c2e2790982a3aff` | 121 | README_TASK_DIFF | 2026-10-16T18:46:43Z | sn121 README task/scoring sections changed |
| `sn37:readme_task_diff:0aa02311a0f783a4` | 37 | README_TASK_DIFF | 2026-10-17T08:43:24Z | sn37 README task/scoring sections changed |
| `sn125:readme_task_diff:5d449bf6f7a1b5b8` | 125 | README_TASK_DIFF | 2026-10-18T05:49:20Z | sn125 README task/scoring sections changed |

## RESOLVED IN THIS WINDOW

_none_
