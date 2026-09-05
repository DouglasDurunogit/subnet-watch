# ALARMS - generated 2026-09-05T12:59:24Z, block 9001354

window: first_seen in [2026-09-05T11:44:57Z, 2026-09-05T12:59:57Z)  (60 min interval + 15 min overlap)

Report ONLY the rows under NEW SINCE LAST RUN. Rows under STILL OPEN were
already reported in an earlier window and must not be re-alarmed.

## NEW SINCE LAST RUN

| event_id | netuid | class | severity | first_seen_utc | one_line |
|---|---|---|---|---|---|
| `sn71:scoring_commit:2026-09-05T12:58:42Z` | 71 | SCORING_COMMIT | P1 | 2026-09-05T12:59:57Z | sn71 commit touches scoring: Merge pull request #177 from leadpoet/codex/validator-missing-object-… |
| `sn80:readme_task_diff:91c32064037eaf29` | 80 | README_TASK_DIFF | P2 | 2026-09-05T12:59:57Z | sn80 README task/scoring sections changed |

### detail

- **`sn71:scoring_commit:2026-09-05T12:58:42Z`** - sn71 commit touches scoring: Merge pull request #177 from leadpoet/codex/validator-missing-object-…
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn80:readme_task_diff:91c32064037eaf29`** - sn80 README task/scoring sections changed
  - Only the task-describing headings are hashed, so badge and typo edits do not trigger this.

## STILL OPEN (already reported - do not re-alarm)

| event_id | netuid | class | first_seen_utc | one_line |
|---|---|---|---|---|
| `sn49:burn_drop:0.000` | 49 | BURN_DROP | 2026-08-29T15:10:23Z | sn49 burn fell 0.990 -> 0.000 - miners can earn again |
| `sn10:burn_drop:0.922` | 10 | BURN_DROP | 2026-09-01T15:14:15Z | sn10 burn fell 1.000 -> 0.922 - miners can earn again |
| `sn105:burn_drop:0.000` | 105 | BURN_DROP | 2026-09-03T01:31:27Z | sn105 burn fell 1.000 -> 0.000 - miners can earn again |
| `sn71:burn_drop:0.974` | 71 | BURN_DROP | 2026-09-03T06:32:43Z | sn71 burn fell 1.000 -> 0.974 - miners can earn again |
| `sn121:burn_drop:0.601` | 121 | BURN_DROP | 2026-09-03T18:49:37Z | sn121 burn fell 1.000 -> 0.601 - miners can earn again |
| `sn49:burn_drop:0.990` | 49 | BURN_DROP | 2026-09-03T21:41:08Z | sn49 burn fell 0.990 -> 0.990 - miners can earn again |
| `sn107:burn_drop:0.812` | 107 | BURN_DROP | 2026-09-04T01:25:22Z | sn107 burn fell 1.000 -> 0.812 - miners can earn again |
| `sn85:burn_drop:0.360` | 85 | BURN_DROP | 2026-09-04T21:04:38Z | sn85 burn fell 1.000 -> 0.360 - miners can earn again |
| `sn21:scoring_commit:2026-08-29T14:49:37Z` | 21 | SCORING_COMMIT | 2026-08-29T15:10:23Z | sn21 commit touches scoring: feat(scoring): honour the reference exemption on the lineage path |
| `sn111:scoring_commit:2026-08-29T11:10:12Z` | 111 | SCORING_COMMIT | 2026-08-29T15:10:23Z | sn111 commit touches scoring: chore(config): shorten validator query interval |
| `sn21:scoring_commit:2026-08-29T15:29:29Z` | 21 | SCORING_COMMIT | 2026-08-29T18:44:56Z | sn21 commit touches scoring: fix(reporting): a published tier must mean the miner is being paid |
| `sn71:scoring_commit:2026-08-29T16:01:20Z` | 71 | SCORING_COMMIT | 2026-08-29T18:44:56Z | sn71 commit touches scoring: Measure admitted model verifier latency |
| `sn89:scoring_commit:2026-08-29T16:20:07Z` | 89 | SCORING_COMMIT | 2026-08-29T18:44:56Z | sn89 commit touches scoring: HF: grade the band the miner declared, not the board's |
| `sn111:scoring_commit:2026-08-29T17:27:58Z` | 111 | SCORING_COMMIT | 2026-08-29T18:44:56Z | sn111 commit touches scoring: fix(validator): preserve completed run status during shutdown |
| `sn89:scoring_commit:2026-08-29T20:55:10Z` | 89 | SCORING_COMMIT | 2026-08-29T21:20:31Z | sn89 commit touches scoring: limit-watcher: a miner-drawn band survives to fire |
| `sn89:scoring_commit:2026-08-29T22:05:27Z` | 89 | SCORING_COMMIT | 2026-08-29T23:29:51Z | sn89 commit touches scoring: scoring: the points gate is per competition, not per chain |
| `sn71:scoring_commit:2026-08-30T00:13:57Z` | 71 | SCORING_COMMIT | 2026-08-30T01:45:42Z | sn71 commit touches scoring: Document miner SOURCE_ADD inputs (#153) |
| `sn89:scoring_commit:2026-08-30T01:06:31Z` | 89 | SCORING_COMMIT | 2026-08-30T01:45:42Z | sn89 commit touches scoring: scoring: the points qualify gate, and the variance that made it too l… |
| `sn92:scoring_commit:2026-08-30T01:18:37Z` | 92 | SCORING_COMMIT | 2026-08-30T01:45:42Z | sn92 commit touches scoring: Validate commitments at discovery, guard partial settles, count dupli… |
| `sn21:scoring_commit:2026-08-30T05:20:42Z` | 21 | SCORING_COMMIT | 2026-08-30T07:32:13Z | sn21 commit touches scoring: fix(validator-api): serve the daily feeds without a weekly release |
| `sn67:scoring_commit:2026-08-29T08:12:36Z` | 67 | SCORING_COMMIT | 2026-08-30T07:32:13Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20260829.post1 |
| `sn92:scoring_commit:2026-08-30T03:19:44Z` | 92 | SCORING_COMMIT | 2026-08-30T07:32:13Z | sn92 commit touches scoring: Satisfy strict typing across the validator, scoring, and engine paths |
| `sn9:release:v4.12.10` | 9 | RELEASE | 2026-08-30T13:20:41Z | sn9 released v4.12.10 |
| `sn21:scoring_commit:2026-08-30T11:29:22Z` | 21 | SCORING_COMMIT | 2026-08-30T13:20:41Z | sn21 commit touches scoring: docs(validator): stop implying a second validator can run the scorer |
| `sn15:release:v1.2.11` | 15 | RELEASE | 2026-08-30T17:40:07Z | sn15 released v1.2.11 |
| `sn21:scoring_commit:2026-08-30T13:48:48Z` | 21 | SCORING_COMMIT | 2026-08-30T17:40:07Z | sn21 commit touches scoring: fix(reporting): tenure rows state how many days the miner actually has |
| `sn25:release:v2026.8.30-1033129380` | 25 | RELEASE | 2026-08-30T20:05:23Z | sn25 released v2026.8.30-1033129380 |
| `sn92:scoring_commit:2026-08-30T20:40:28Z` | 92 | SCORING_COMMIT | 2026-08-30T22:43:10Z | sn92 commit touches scoring: Lock the evaluation environment to the fleet's resolved set |
| `sn111:scoring_commit:2026-08-30T21:57:12Z` | 111 | SCORING_COMMIT | 2026-08-30T22:43:10Z | sn111 commit touches scoring: feat(selection): expand miner pool with provisional performance |
| `sn91:scoring_commit:2026-08-31T05:05:09Z` | 91 | SCORING_COMMIT | 2026-08-31T07:00:21Z | sn91 commit touches scoring: validator: multi-horizon calibration telemetry — groundwork for the s… |
| `sn92:scoring_commit:2026-08-31T06:03:36Z` | 92 | SCORING_COMMIT | 2026-08-31T07:00:21Z | sn92 commit touches scoring: Score module-shaped tasks in miner simulation under the pinned enviro… |
| `sn101:scoring_commit:2026-08-31T03:21:03Z` | 101 | SCORING_COMMIT | 2026-08-31T07:00:21Z | sn101 commit touches scoring: Harden tag normalization and duplicate-set matching in scoring |
| `sn111:scoring_commit:2026-08-31T02:59:02Z` | 111 | SCORING_COMMIT | 2026-08-31T07:00:21Z | sn111 commit touches scoring: feat(selection): make adaptive miner sample size configurable |
| `sn3:scoring_commit:2026-08-31T08:14:55Z` | 3 | SCORING_COMMIT | 2026-08-31T15:03:06Z | sn3 commit touches scoring: Implement evaluation reuse limit handling and cleanup scheduling |
| `sn50:scoring_commit:2026-08-31T13:14:24Z` | 50 | SCORING_COMMIT | 2026-08-31T15:03:06Z | sn50 commit touches scoring: feat(validator): blend VHFT (Synth Ultra) as a 4th competition (#320) |
| `sn51:scoring_commit:2026-08-31T12:25:43Z` | 51 | SCORING_COMMIT | 2026-08-31T15:03:06Z | sn51 commit touches scoring: DAH-2090, validate one executor on request from the backend (#1254) |
| `sn56:scoring_commit:2026-08-31T13:13:56Z` | 56 | SCORING_COMMIT | 2026-08-31T15:03:06Z | sn56 commit touches scoring: Preserve replacement-task invariants across prep-failure reroutes. (#… |
| `sn67:scoring_commit:2026-08-31T06:48:15Z` | 67 | SCORING_COMMIT | 2026-08-31T15:03:06Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20260831.post1 |
| `sn92:scoring_commit:2026-08-31T13:00:04Z` | 92 | SCORING_COMMIT | 2026-08-31T15:03:06Z | sn92 commit touches scoring: Add the novel partition and blend it into the score at its task share |
| `sn97:scoring_commit:2026-08-29T21:22:36Z` | 97 | SCORING_COMMIT | 2026-08-31T15:03:06Z | sn97 commit touches scoring: fix: skip hidden files from validation |
| `sn15:release:v1.2.12` | 15 | RELEASE | 2026-08-31T20:48:23Z | sn15 released v1.2.12 |
| `sn15:scoring_commit:2026-08-31T16:04:15Z` | 15 | SCORING_COMMIT | 2026-08-31T20:48:23Z | sn15 commit touches scoring: fix(validator): don't fail runs on incomplete reasoning-judge coverag… |
| `sn38:scoring_commit:2026-08-31T17:33:12Z` | 38 | SCORING_COMMIT | 2026-08-31T20:48:23Z | sn38 commit touches scoring: Update validator image to the latest version in docker-compose.valida… |
| `sn50:release:v1.12.0` | 50 | RELEASE | 2026-08-31T20:48:23Z | sn50 released v1.12.0 |
| `sn92:release:v0.3.0` | 92 | RELEASE | 2026-08-31T20:48:23Z | sn92 released v0.3.0 |
| `sn92:scoring_commit:2026-08-31T20:39:51Z` | 92 | SCORING_COMMIT | 2026-08-31T20:48:23Z | sn92 commit touches scoring: Grant the validator container the capability the network jail needs |
| `sn111:scoring_commit:2026-08-31T20:40:04Z` | 111 | SCORING_COMMIT | 2026-08-31T20:48:23Z | sn111 commit touches scoring: feat(selection): diversify adaptive miner draws |
| `sn124:scoring_commit:2026-08-31T19:33:52Z` | 124 | SCORING_COMMIT | 2026-08-31T20:48:23Z | sn124 commit touches scoring: Merge pull request #118 from swarm-subnet/feature/ali/miner-folder-mi… |
| `sn25:release:v2026.8.31-1034210530` | 25 | RELEASE | 2026-09-01T00:34:46Z | sn25 released v2026.8.31-1034210530 |
| `sn25:scoring_commit:2026-09-01T00:06:51Z` | 25 | SCORING_COMMIT | 2026-09-01T00:34:46Z | sn25 commit touches scoring: Batch carried fleet refresh verification |
| `sn25:scoring_commit:2026-09-01T10:14:28Z` | 25 | SCORING_COMMIT | 2026-09-01T10:31:56Z | sn25 commit touches scoring: Verify carried conviction under its source policy |
| `sn63:scoring_commit:2026-09-01T06:34:11Z` | 63 | SCORING_COMMIT | 2026-09-01T10:31:56Z | sn63 commit touches scoring: Support multiple validations on single validator and update cli ux |
| `sn67:scoring_commit:2026-09-01T06:46:40Z` | 67 | SCORING_COMMIT | 2026-09-01T10:31:56Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20260901.post1 |
| `sn111:scoring_commit:2026-09-01T08:48:59Z` | 111 | SCORING_COMMIT | 2026-09-01T10:31:56Z | sn111 commit touches scoring: feat(selection): harden adaptive miner selection |
| `sn23:scoring_commit:2026-09-01T13:59:39Z` | 23 | SCORING_COMMIT | 2026-09-01T15:14:15Z | sn23 commit touches scoring: Merge pull request #51 from TrishoolAI/q-3-006-challenge-update |
| `sn92:release:v0.3.2` | 92 | RELEASE | 2026-09-01T15:14:15Z | sn92 released v0.3.2 |
| `sn97:scoring_commit:2026-09-01T07:58:22Z` | 97 | SCORING_COMMIT | 2026-09-01T15:14:15Z | sn97 commit touches scoring: fix: Fixed private hotkey_already_validated false positive |
| `sn107:scoring_commit:2026-09-01T14:01:27Z` | 107 | SCORING_COMMIT | 2026-09-01T15:14:15Z | sn107 commit touches scoring: Merge pull request #37 from minos-protocol/feat/v2-scoring-and-fixes |
| `sn108:scoring_commit:2026-09-01T13:01:55Z` | 108 | SCORING_COMMIT | 2026-09-01T15:14:15Z | sn108 commit touches scoring: docs(scoring): the split section still described the two-to-one pool |
| `sn111:scoring_commit:2026-09-01T11:09:58Z` | 111 | SCORING_COMMIT | 2026-09-01T15:14:15Z | sn111 commit touches scoring: feat(scoring): cap minor-tier coverage at five percent |
| `sn7:release:release-20260901-182140: Set miner burn ` | 7 | RELEASE | 2026-09-01T18:42:47Z | sn7 released release-20260901-182140: Set miner burn to 0% (v3.3.1) (#710) |
| `sn7:scoring_commit:2026-09-01T18:14:46Z` | 7 | SCORING_COMMIT | 2026-09-01T18:42:47Z | sn7 commit touches scoring: Set miner burn to 0% (v3.3.1) (#710) |
| `sn21:scoring_commit:2026-09-01T17:16:02Z` | 21 | SCORING_COMMIT | 2026-09-01T18:42:47Z | sn21 commit touches scoring: feat(scoring): focus column shows per-type rank among qualified miners |
| `sn25:release:v2026.9.1-1034848790` | 25 | RELEASE | 2026-09-01T18:42:47Z | sn25 released v2026.9.1-1034848790 |
| `sn25:scoring_commit:2026-09-01T17:30:15Z` | 25 | SCORING_COMMIT | 2026-09-01T18:42:47Z | sn25 commit touches scoring: sim-testnet: verify direct Connect ingress |
| `sn34:scoring_commit:2026-09-01T17:35:17Z` | 34 | SCORING_COMMIT | 2026-09-01T18:42:47Z | sn34 commit touches scoring: fix: show scoring-aligned augmented metrics (#432) |
| `sn124:scoring_commit:2026-09-01T17:53:33Z` | 124 | SCORING_COMMIT | 2026-09-01T18:42:47Z | sn124 commit touches scoring: Merge pull request #120 from swarm-subnet/feature/ali/validator-folde… |
| `sn25:release:v2026.9.1-1034943860` | 25 | RELEASE | 2026-09-01T21:25:28Z | sn25 released v2026.9.1-1034943860 |
| `sn92:scoring_commit:2026-09-01T21:01:49Z` | 92 | SCORING_COMMIT | 2026-09-01T21:25:28Z | sn92 commit touches scoring: Run the validator image on the pinned interpreter and build its envir… |
| `sn104:scoring_commit:2026-08-30T09:59:38Z` | 104 | SCORING_COMMIT | 2026-09-01T23:29:32Z | sn104 commit touches scoring: multiple llm key and improve the scoring mechanism |
| `sn25:release:v2026.9.1-1035082030` | 25 | RELEASE | 2026-09-02T01:27:43Z | sn25 released v2026.9.1-1035082030 |
| `sn67:scoring_commit:2026-09-01T09:54:56Z` | 67 | SCORING_COMMIT | 2026-09-02T01:27:43Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20260901.post2 |
| `sn25:scoring_commit:2026-09-02T00:23:30Z` | 25 | SCORING_COMMIT | 2026-09-02T06:28:05Z | sn25 commit touches scoring: Join miner and validator lifecycle ownership |
| `sn51:scoring_commit:2026-09-02T05:43:12Z` | 51 | SCORING_COMMIT | 2026-09-02T06:28:05Z | sn51 commit touches scoring: DAH-2701: withhold incentive from executors running an outdated image… |
| `sn71:scoring_commit:2026-09-01T23:59:43Z` | 71 | SCORING_COMMIT | 2026-09-02T06:28:05Z | sn71 commit touches scoring: Handle SOURCE_ADD chain reward quantization |
| `sn3:scoring_commit:2026-09-02T10:23:18Z` | 3 | SCORING_COMMIT | 2026-09-02T11:39:58Z | sn3 commit touches scoring: Update evaluation parameters |
| `sn25:scoring_commit:2026-09-02T10:31:33Z` | 25 | SCORING_COMMIT | 2026-09-02T11:39:58Z | sn25 commit touches scoring: Rate-limit validator verification attempts |
| `sn65:scoring_commit:2026-08-27T13:32:41Z` | 65 | SCORING_COMMIT | 2026-09-02T11:39:58Z | sn65 commit touches scoring: validator improvements + database threading fixes |
| `sn67:scoring_commit:2026-09-02T09:27:57Z` | 67 | SCORING_COMMIT | 2026-09-02T11:39:58Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20260902.post0 |
| `sn71:scoring_commit:2026-09-02T11:01:44Z` | 71 | SCORING_COMMIT | 2026-09-02T11:39:58Z | sn71 commit touches scoring: Repair validator supersession test driver |
| `sn111:scoring_commit:2026-09-01T22:03:12Z` | 111 | SCORING_COMMIT | 2026-09-02T11:39:58Z | sn111 commit touches scoring: docs(validator): update bucket policy and production setup |
| `sn28:release:v0.4.13-dev` | 28 | RELEASE | 2026-09-02T15:21:36Z | sn28 released v0.4.13-dev |
| `sn51:scoring_commit:2026-09-02T11:42:41Z` | 51 | SCORING_COMMIT | 2026-09-02T15:21:36Z | sn51 commit touches scoring: DAH-2828, feat(validator): quote path for customer pods on CVM nodes … |
| `sn102:release:v0.5.4 — restore validator_baseline_loss` | 102 | RELEASE | 2026-09-02T15:21:36Z | sn102 released v0.5.4 — restore validator_baseline_loss telemetry |
| `sn102:scoring_commit:2026-09-02T14:07:33Z` | 102 | SCORING_COMMIT | 2026-09-02T15:21:36Z | sn102 commit touches scoring: 📊 telemetry: restore validator_baseline_loss from the background path |
| `sn13:release:Release v1.18.72` | 13 | RELEASE | 2026-09-02T18:51:15Z | sn13 released Release v1.18.72 |
| `sn13:scoring_commit:2026-08-24T09:13:23Z` | 13 | SCORING_COMMIT | 2026-09-02T18:51:15Z | sn13 commit touches scoring: docs(miner): warn that Reddit.json needs auth, add data-collection ve… |
| `sn21:scoring_commit:2026-09-02T18:39:13Z` | 21 | SCORING_COMMIT | 2026-09-02T18:51:15Z | sn21 commit touches scoring: fix(scoring): absence charges require a fair chance to run |
| `sn28:release:v0.4.14` | 28 | RELEASE | 2026-09-02T18:51:15Z | sn28 released v0.4.14 |
| `sn71:scoring_commit:2026-09-02T16:59:04Z` | 71 | SCORING_COMMIT | 2026-09-02T18:51:15Z | sn71 commit touches scoring: Bind automatic SOURCE_ADD reward workflow |
| `sn74:release:release-20260902-172331` | 74 | RELEASE | 2026-09-02T18:51:15Z | sn74 released release-20260902-172331 |
| `sn74:scoring_commit:2026-09-02T02:34:28Z` | 74 | SCORING_COMMIT | 2026-09-02T18:51:15Z | sn74 commit touches scoring: serving: compose miner takes host ports and runtime/attest URLs from … |
| `sn89:scoring_commit:2026-09-02T16:19:10Z` | 89 | SCORING_COMMIT | 2026-09-02T18:51:15Z | sn89 commit touches scoring: weights: the validator was setting them on the pre-causal rule |
| `sn111:scoring_commit:2026-09-02T17:43:43Z` | 111 | SCORING_COMMIT | 2026-09-02T18:51:15Z | sn111 commit touches scoring: Enforce mainnet Silver validator requirements |
| `sn2:release:14.14.1` | 2 | RELEASE | 2026-09-02T21:47:07Z | sn2 released 14.14.1 |
| `sn2:scoring_commit:2026-09-02T17:50:35Z` | 2 | SCORING_COMMIT | 2026-09-02T21:47:07Z | sn2 commit touches scoring: Resolve slow validator recovery after external address rotation (#620) |
| `sn21:scoring_commit:2026-09-02T19:01:27Z` | 21 | SCORING_COMMIT | 2026-09-02T21:47:07Z | sn21 commit touches scoring: feat(validator): reference partner validator loop |
| `sn25:scoring_commit:2026-09-02T21:30:53Z` | 25 | SCORING_COMMIT | 2026-09-02T21:47:07Z | sn25 commit touches scoring: Revalidate topology for each release plan |
| `sn71:scoring_commit:2026-09-02T21:52:48Z` | 71 | SCORING_COMMIT | 2026-09-02T23:37:16Z | sn71 commit touches scoring: Repair SOURCE_ADD provenance origin rewards |
| `sn67:scoring_commit:2026-09-03T01:49:07Z` | 67 | SCORING_COMMIT | 2026-09-03T06:32:43Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20260903.post0 |
| `sn76:scoring_commit:2026-09-03T05:42:35Z` | 76 | SCORING_COMMIT | 2026-09-03T06:32:43Z | sn76 commit touches scoring: ci: run the non-scoring tests on every push |
| `sn91:scoring_commit:2026-09-03T02:30:30Z` | 91 | SCORING_COMMIT | 2026-09-03T06:32:43Z | sn91 commit touches scoring: scoring: block-scheduled fresh-king margin (2% → 1% at 8992800), reso… |
| `sn1:release:v4.4.0` | 1 | RELEASE | 2026-09-03T11:45:17Z | sn1 released v4.4.0 |
| `sn50:scoring_commit:2026-09-03T09:01:36Z` | 50 | SCORING_COMMIT | 2026-09-03T11:45:17Z | sn50 commit touches scoring: base miner: gzip-compress axon responses (#319) |
| `sn100:scoring_commit:2026-09-03T08:25:50Z` | 100 | SCORING_COMMIT | 2026-09-03T11:45:17Z | sn100 commit touches scoring: fix(relearn): pin proven CUDA scoring eval image digest (#205) |
| `sn1:release:v4.4.1` | 1 | RELEASE | 2026-09-03T15:15:26Z | sn1 released v4.4.1 |
| `sn2:release:14.14.2` | 2 | RELEASE | 2026-09-03T15:15:26Z | sn2 released 14.14.2 |
| `sn53:scoring_commit:2026-09-03T05:50:55Z` | 53 | SCORING_COMMIT | 2026-09-03T18:49:37Z | sn53 commit touches scoring: tee_miner: stop dropping the thinking-token count on the way out |
| `sn69:scoring_commit:2026-09-03T16:15:44Z` | 69 | SCORING_COMMIT | 2026-09-03T18:49:37Z | sn69 commit touches scoring: Point CLI miners at the console to download a brief document (#5) |
| `sn71:scoring_commit:2026-09-03T18:42:37Z` | 71 | SCORING_COMMIT | 2026-09-03T18:49:37Z | sn71 commit touches scoring: Preserve strict identity boundaries in scoring integration |
| `sn74:release:release-20260903-183804` | 74 | RELEASE | 2026-09-03T18:49:37Z | sn74 released release-20260903-183804 |
| `sn25:release:v2026.9.3-1036684010` | 25 | RELEASE | 2026-09-03T21:41:08Z | sn25 released v2026.9.3-1036684010 |
| `sn71:scoring_commit:2026-09-03T18:50:08Z` | 71 | SCORING_COMMIT | 2026-09-03T21:41:08Z | sn71 commit touches scoring: Bind updated scoring protected workflows |
| `sn71:scoring_commit:2026-09-03T22:37:18Z` | 71 | SCORING_COMMIT | 2026-09-03T23:33:40Z | sn71 commit touches scoring: Tell a rate-limited miner which submission cap it hit |
| `sn21:scoring_commit:2026-09-04T00:49:42Z` | 21 | SCORING_COMMIT | 2026-09-04T01:25:22Z | sn21 commit touches scoring: fix(validator): commit the daily vector directly when the weekly stre… |
| `sn25:release:v2026.9.3-1036806790` | 25 | RELEASE | 2026-09-04T01:25:22Z | sn25 released v2026.9.3-1036806790 |
| `sn25:scoring_commit:2026-09-03T19:36:15Z` | 25 | SCORING_COMMIT | 2026-09-04T01:25:22Z | sn25 commit touches scoring: fix semantic reward consensus fixture |
| `sn71:scoring_commit:2026-09-04T00:27:39Z` | 71 | SCORING_COMMIT | 2026-09-04T01:25:22Z | sn71 commit touches scoring: Prevent source add reward queue starvation |
| `sn107:scoring_commit:2026-09-04T00:16:20Z` | 107 | SCORING_COMMIT | 2026-09-04T01:25:22Z | sn107 commit touches scoring: Merge pull request #39 from minos-protocol/feat/round-verification |
| `sn21:scoring_commit:2026-09-04T04:09:32Z` | 21 | SCORING_COMMIT | 2026-09-04T06:21:54Z | sn21 commit touches scoring: test(validator): prove burn composition matches the committer branch … |
| `sn71:scoring_commit:2026-09-04T05:24:15Z` | 71 | SCORING_COMMIT | 2026-09-04T06:21:54Z | sn71 commit touches scoring: Bind protected Arena reward compatibility adapter |
| `sn100:scoring_commit:2026-09-04T04:15:06Z` | 100 | SCORING_COMMIT | 2026-09-04T06:21:54Z | sn100 commit touches scoring: feat(proof): Proof challenge + dynamic topics + RLM judge digest pin … |
| `sn107:release:v0.3.0: Minos 🧬 — Difficulty-weighted sc` | 107 | RELEASE | 2026-09-04T06:21:54Z | sn107 released v0.3.0: Minos 🧬 — Difficulty-weighted scoring (v2), round verification,  config commitments |
| `sn25:scoring_commit:2026-09-04T11:22:34Z` | 25 | SCORING_COMMIT | 2026-09-04T11:33:57Z | sn25 commit touches scoring: Record semantic verifier parallel qualification |
| `sn66:scoring_commit:2026-09-03T14:19:04Z` | 66 | SCORING_COMMIT | 2026-09-04T11:33:57Z | sn66 commit touches scoring: Derive the verifier image tag, not only its digest and version |
| `sn67:scoring_commit:2026-09-04T06:27:51Z` | 67 | SCORING_COMMIT | 2026-09-04T11:33:57Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20260904.post1 |
| `sn78:scoring_commit:2026-09-03T21:48:59Z` | 78 | SCORING_COMMIT | 2026-09-04T11:33:57Z | sn78 commit touches scoring: Expose replay-verified public miner solutions |
| `sn92:scoring_commit:2026-09-04T10:56:43Z` | 92 | SCORING_COMMIT | 2026-09-04T11:33:57Z | sn92 commit touches scoring: Smooth the miner CLI and quiet the archive |
| `sn97:scoring_commit:2026-09-03T16:13:11Z` | 97 | SCORING_COMMIT | 2026-09-04T11:33:57Z | sn97 commit touches scoring: fix: re-key a registration when the miner re-activates with a new sub… |
| `sn100:scoring_commit:2026-09-04T07:41:55Z` | 100 | SCORING_COMMIT | 2026-09-04T11:33:57Z | sn100 commit touches scoring: fix(validator): extract submit outcome helper for clippy |
| `sn3:scoring_commit:2026-09-04T13:38:17Z` | 3 | SCORING_COMMIT | 2026-09-04T15:09:26Z | sn3 commit touches scoring: Show model digests for queued and active evaluations |
| `sn21:scoring_commit:2026-09-04T14:12:08Z` | 21 | SCORING_COMMIT | 2026-09-04T15:09:26Z | sn21 commit touches scoring: fix(validator): reference loop uses bt.Wallet |
| `sn25:release:v2026.9.4-1037327320` | 25 | RELEASE | 2026-09-04T15:09:26Z | sn25 released v2026.9.4-1037327320 |
| `sn47:scoring_commit:2026-09-04T14:48:52Z` | 47 | SCORING_COMMIT | 2026-09-04T15:09:26Z | sn47 commit touches scoring: new datasets list and verifier |
| `sn7:release:release-20260904-155448: Add min_from_am` | 7 | RELEASE | 2026-09-04T18:32:09Z | sn7 released release-20260904-155448: Add min_from_amount and candidates to the seam rate quote (#719) |
| `sn7:scoring_commit:2026-09-02T22:52:26Z` | 7 | SCORING_COMMIT | 2026-09-04T18:32:09Z | sn7 commit touches scoring: CLI: --send verifies source-address control BEFORE the bid (#716) |
| `sn25:release:v2026.9.4-1037416540` | 25 | RELEASE | 2026-09-04T18:32:09Z | sn25 released v2026.9.4-1037416540 |
| `sn78:scoring_commit:2026-09-04T18:06:44Z` | 78 | SCORING_COMMIT | 2026-09-04T18:32:09Z | sn78 commit touches scoring: Install FFmpeg for macOS miner tests |
| `sn96:release:Verathos v0.2.0 – Sleipnir: Verifiable M` | 96 | RELEASE | 2026-09-04T18:32:09Z | sn96 released Verathos v0.2.0 – Sleipnir: Verifiable Multi-Node Model Serving |
| `sn96:scoring_commit:2026-09-04T07:31:31Z` | 96 | SCORING_COMMIT | 2026-09-04T18:32:09Z | sn96 commit touches scoring: fix: qualify mesh scoring on protocol v3 |
| `sn100:scoring_commit:2026-09-04T17:45:13Z` | 100 | SCORING_COMMIT | 2026-09-04T18:32:09Z | sn100 commit touches scoring: docs(miner): Proof + Bounty A→Z at 2000/8000 (#219) |
| `sn102:release:v0.5.5 — publish the round podium to a H` | 102 | RELEASE | 2026-09-04T18:32:09Z | sn102 released v0.5.5 — publish the round podium to a HuggingFace archive repo |
| `sn102:scoring_commit:2026-09-03T21:10:17Z` | 102 | SCORING_COMMIT | 2026-09-04T18:32:09Z | sn102 commit touches scoring: 🏷️ refactor(validator): name podium folders by cycle, not round id |
| `sn21:scoring_commit:2026-09-04T20:27:20Z` | 21 | SCORING_COMMIT | 2026-09-04T21:04:38Z | sn21 commit touches scoring: feat(scoring): measurement resolution applied from a published date |
| `sn25:release:v2026.9.4-1037517570` | 25 | RELEASE | 2026-09-04T21:04:38Z | sn25 released v2026.9.4-1037517570 |
| `sn34:scoring_commit:2026-09-04T18:44:10Z` | 34 | SCORING_COMMIT | 2026-09-04T21:04:38Z | sn34 commit touches scoring: burn discriminator incentive until KoTH ships (#436) |
| `sn47:scoring_commit:2026-09-04T19:22:55Z` | 47 | SCORING_COMMIT | 2026-09-04T21:04:38Z | sn47 commit touches scoring: fix extraction and verifier |
| `sn92:scoring_commit:2026-09-04T20:10:42Z` | 92 | SCORING_COMMIT | 2026-09-04T21:04:38Z | sn92 commit touches scoring: scoring: refuse sockets with a class so ssl and asyncio still import … |
| `sn7:release:release-20260904-214340: Bump version to` | 7 | RELEASE | 2026-09-04T23:02:03Z | sn7 released release-20260904-214340: Bump version to 3.3.2 (#722) |
| `sn25:release:v2026.9.4-1037600680` | 25 | RELEASE | 2026-09-04T23:02:03Z | sn25 released v2026.9.4-1037600680 |
| `sn92:scoring_commit:2026-09-04T21:42:58Z` | 92 | SCORING_COMMIT | 2026-09-04T23:02:03Z | sn92 commit touches scoring: ci: classify bundle for the hidden-tests check; label tasks need one … |
| `sn21:scoring_commit:2026-09-05T04:29:37Z` | 21 | SCORING_COMMIT | 2026-09-05T05:40:43Z | sn21 commit touches scoring: docs(scoring): standing and resolution amendments effective 2026-09-05 |
| `sn62:release:v0.3.0` | 62 | RELEASE | 2026-09-05T05:40:43Z | sn62 released v0.3.0 |
| `sn62:scoring_commit:2026-09-04T10:45:00Z` | 62 | SCORING_COMMIT | 2026-09-05T05:40:43Z | sn62 commit touches scoring: test: :white_check_mark: Add tests validating the new endpoint |
| `sn71:scoring_commit:2026-09-05T05:37:23Z` | 71 | SCORING_COMMIT | 2026-09-05T05:40:43Z | sn71 commit touches scoring: fix: validate retained gateway archives by their supported role layout |
| `sn47:scoring_commit:2026-09-05T08:47:30Z` | 47 | SCORING_COMMIT | 2026-09-05T09:27:28Z | sn47 commit touches scoring: refine evaluation system |
| `sn71:scoring_commit:2026-09-05T08:30:32Z` | 71 | SCORING_COMMIT | 2026-09-05T09:27:28Z | sn71 commit touches scoring: fix: exclude stale validator build path from gateway runtime env |
| `sn100:scoring_commit:2026-09-05T08:03:23Z` | 100 | SCORING_COMMIT | 2026-09-05T09:27:28Z | sn100 commit touches scoring: fix(challenges): boot when sk/session placeholders are empty (#226) |
| `sn71:readme_task_diff:5ecd38a51a4692a8` | 71 | README_TASK_DIFF | 2026-08-30T01:45:42Z | sn71 README task/scoring sections changed |
| `sn45:readme_task_diff:8c971dd579660a1e` | 45 | README_TASK_DIFF | 2026-08-30T07:32:13Z | sn45 README task/scoring sections changed |
| `sn91:readme_task_diff:becad0b5e25c9292` | 91 | README_TASK_DIFF | 2026-08-30T13:20:41Z | sn91 README task/scoring sections changed |
| `sn38:readme_task_diff:6d6f3dfd29d211ce` | 38 | README_TASK_DIFF | 2026-08-31T20:48:23Z | sn38 README task/scoring sections changed |
| `sn80:readme_task_diff:c3d88acb03906c81` | 80 | README_TASK_DIFF | 2026-09-01T05:44:42Z | sn80 README task/scoring sections changed |
| `sn107:readme_task_diff:5f8353ef47bb6eec` | 107 | README_TASK_DIFF | 2026-09-01T15:14:15Z | sn107 README task/scoring sections changed |
| `sn7:readme_task_diff:0ed4024c562bd06a` | 7 | README_TASK_DIFF | 2026-09-01T18:42:47Z | sn7 README task/scoring sections changed |
| `sn104:readme_task_diff:92a67d7788885fe7` | 104 | README_TASK_DIFF | 2026-09-01T23:29:32Z | sn104 README task/scoring sections changed |
| `sn66:readme_task_diff:1f9bcf8a76a45b27` | 66 | README_TASK_DIFF | 2026-09-02T15:21:36Z | sn66 README task/scoring sections changed |
| `sn80:readme_task_diff:7b0ea93609afb2d8` | 80 | README_TASK_DIFF | 2026-09-02T15:21:36Z | sn80 README task/scoring sections changed |
| `sn74:readme_task_diff:4bce422bd3ab6229` | 74 | README_TASK_DIFF | 2026-09-02T18:51:15Z | sn74 README task/scoring sections changed |
| `sn80:readme_task_diff:cdbca72968cc4124` | 80 | README_TASK_DIFF | 2026-09-02T18:51:15Z | sn80 README task/scoring sections changed |
| `sn91:readme_task_diff:2d41cdb0f4f83294` | 91 | README_TASK_DIFF | 2026-09-03T06:32:43Z | sn91 README task/scoring sections changed |
| `sn71:readme_task_diff:ebf6898a52202570` | 71 | README_TASK_DIFF | 2026-09-03T18:49:37Z | sn71 README task/scoring sections changed |
| `sn114:readme_task_diff:8a170d798d34334c` | 114 | README_TASK_DIFF | 2026-09-04T11:33:57Z | sn114 README task/scoring sections changed |
| `sn47:readme_task_diff:ee01fd805919dfa1` | 47 | README_TASK_DIFF | 2026-09-04T15:09:26Z | sn47 README task/scoring sections changed |
| `sn7:readme_task_diff:edbfe0beb3207f5d` | 7 | README_TASK_DIFF | 2026-09-04T18:32:09Z | sn7 README task/scoring sections changed |
| `sn96:readme_task_diff:9b448a83b77e12c9` | 96 | README_TASK_DIFF | 2026-09-04T18:32:09Z | sn96 README task/scoring sections changed |
| `sn47:readme_task_diff:8b345756fdb99755` | 47 | README_TASK_DIFF | 2026-09-04T21:04:38Z | sn47 README task/scoring sections changed |
| `sn63:readme_task_diff:9f841de80403238f` | 63 | README_TASK_DIFF | 2026-09-04T21:04:38Z | sn63 README task/scoring sections changed |
| `sn71:readme_task_diff:7ba0f5e901269ab4` | 71 | README_TASK_DIFF | 2026-09-04T21:04:38Z | sn71 README task/scoring sections changed |
| `sn47:readme_task_diff:478b669831ea7848` | 47 | README_TASK_DIFF | 2026-09-05T09:27:28Z | sn47 README task/scoring sections changed |

## RESOLVED IN THIS WINDOW

_none_
