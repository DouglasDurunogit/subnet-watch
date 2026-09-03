# ALARMS - generated 2026-09-03T01:31:00Z, block 8983520

window: first_seen in [2026-09-03T00:16:27Z, 2026-09-03T01:31:27Z)  (60 min interval + 15 min overlap)

Report ONLY the rows under NEW SINCE LAST RUN. Rows under STILL OPEN were
already reported in an earlier window and must not be re-alarmed.

## NEW SINCE LAST RUN

| event_id | netuid | class | severity | first_seen_utc | one_line |
|---|---|---|---|---|---|
| `sn105:burn_drop:0.000` | 105 | BURN_DROP | P0 | 2026-09-03T01:31:27Z | sn105 burn fell 1.000 -> 0.000 - miners can earn again |

### detail

- **`sn105:burn_drop:0.000`** - sn105 burn fell 1.000 -> 0.000 - miners can earn again
  - This subnet paid miners nothing and now pays. Worth a look before the field fills up.

## STILL OPEN (already reported - do not re-alarm)

| event_id | netuid | class | first_seen_utc | one_line |
|---|---|---|---|---|
| `sn65:burn_drop:0.762` | 65 | BURN_DROP | 2026-08-27T14:33:13Z | sn65 burn fell 1.000 -> 0.762 - miners can earn again |
| `sn92:burn_drop:0.952` | 92 | BURN_DROP | 2026-08-27T14:33:13Z | sn92 burn fell 1.000 -> 0.952 - miners can earn again |
| `sn59:burn_drop:0.000` | 59 | BURN_DROP | 2026-08-28T00:03:30Z | sn59 burn fell 1.000 -> 0.000 - miners can earn again |
| `sn14:burn_drop:0.000` | 14 | BURN_DROP | 2026-08-28T11:18:26Z | sn14 burn fell 1.000 -> 0.000 - miners can earn again |
| `sn104:burn_drop:0.003` | 104 | BURN_DROP | 2026-08-28T21:28:55Z | sn104 burn fell 1.000 -> 0.003 - miners can earn again |
| `sn111:burn_drop:0.000` | 111 | BURN_DROP | 2026-08-28T21:28:55Z | sn111 burn fell 1.000 -> 0.000 - miners can earn again |
| `sn121:burn_drop:0.606` | 121 | BURN_DROP | 2026-08-28T21:28:55Z | sn121 burn fell 1.000 -> 0.606 - miners can earn again |
| `sn49:burn_drop:0.000` | 49 | BURN_DROP | 2026-08-29T15:10:23Z | sn49 burn fell 0.990 -> 0.000 - miners can earn again |
| `sn10:burn_drop:0.922` | 10 | BURN_DROP | 2026-09-01T15:14:15Z | sn10 burn fell 1.000 -> 0.922 - miners can earn again |
| `sn25:release:v2026.8.26-1029908500` | 25 | RELEASE | 2026-08-27T03:26:56Z | sn25 released v2026.8.26-1029908500 |
| `sn3:scoring_commit:2026-08-27T11:15:32Z` | 3 | SCORING_COMMIT | 2026-08-27T14:33:13Z | sn3 commit touches scoring: Refactor evaluation section in index.html for improved structure |
| `sn21:scoring_commit:2026-08-27T12:19:47Z` | 21 | SCORING_COMMIT | 2026-08-27T14:33:13Z | sn21 commit touches scoring: perf(rewards): per-day fingerprint index — the one-payer check stops … |
| `sn25:release:v2026.8.27-1030161880` | 25 | RELEASE | 2026-08-27T14:33:13Z | sn25 released v2026.8.27-1030161880 |
| `sn55:scoring_commit:2026-08-27T11:33:48Z` | 55 | SCORING_COMMIT | 2026-08-27T14:33:13Z | sn55 commit touches scoring: update validation block number |
| `sn61:release:4.10.1` | 61 | RELEASE | 2026-08-27T14:33:13Z | sn61 released 4.10.1 |
| `sn61:scoring_commit:2026-08-27T11:47:29Z` | 61 | SCORING_COMMIT | 2026-08-27T14:33:13Z | sn61 commit touches scoring: chore: update scoring criteria and clarify human detection requiremen… |
| `sn67:scoring_commit:2026-08-27T07:34:23Z` | 67 | SCORING_COMMIT | 2026-08-27T14:33:13Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20260827.post2 |
| `sn76:scoring_commit:2026-08-27T09:02:45Z` | 76 | SCORING_COMMIT | 2026-08-27T14:33:13Z | sn76 commit touches scoring: validator: attest rejected runs so miners can see why |
| `sn92:scoring_commit:2026-08-27T09:29:56Z` | 92 | SCORING_COMMIT | 2026-08-27T14:33:13Z | sn92 commit touches scoring: Let a miner restore a pointer a reveal overwrote |
| `sn108:scoring_commit:2026-08-27T13:01:50Z` | 108 | SCORING_COMMIT | 2026-08-27T14:33:13Z | sn108 commit touches scoring: docs(validator): re-post every 30 minutes, and say why 30 |
| `sn112:scoring_commit:2026-08-27T08:40:42Z` | 112 | SCORING_COMMIT | 2026-08-27T14:33:13Z | sn112 commit touches scoring: fix(sandbox): scoring JS had no RPC for chain 964, and the wrong one … |
| `sn3:scoring_commit:2026-08-27T14:44:03Z` | 3 | SCORING_COMMIT | 2026-08-28T00:03:30Z | sn3 commit touches scoring: Add evaluation history metrics presentation and update dashboard rend… |
| `sn25:release:v2026.8.27-1030474020` | 25 | RELEASE | 2026-08-28T00:03:30Z | sn25 released v2026.8.27-1030474020 |
| `sn91:release:worker-v0.7.0` | 91 | RELEASE | 2026-08-28T00:03:30Z | sn91 released worker-v0.7.0 |
| `sn92:scoring_commit:2026-08-27T15:01:23Z` | 92 | SCORING_COMMIT | 2026-08-28T00:03:30Z | sn92 commit touches scoring: Attach hidden tests as gold on scored tasks |
| `sn108:scoring_commit:2026-08-27T17:17:43Z` | 108 | SCORING_COMMIT | 2026-08-28T00:03:30Z | sn108 commit touches scoring: fix(validator): a rate-limited mirror cycle killed the scheduler and … |
| `sn112:scoring_commit:2026-08-27T18:37:53Z` | 112 | SCORING_COMMIT | 2026-08-28T00:03:30Z | sn112 commit touches scoring: fix(964): a plan's interactions did not compose, so 964 scored by dif… |
| `sn3:scoring_commit:2026-08-28T08:56:33Z` | 3 | SCORING_COMMIT | 2026-08-28T11:18:26Z | sn3 commit touches scoring: Add source scores handling and presentation to dashboard |
| `sn25:release:v2026.8.28-1031115710` | 25 | RELEASE | 2026-08-28T11:18:26Z | sn25 released v2026.8.28-1031115710 |
| `sn61:release:4.10.2` | 61 | RELEASE | 2026-08-28T11:18:26Z | sn61 released 4.10.2 |
| `sn61:scoring_commit:2026-08-28T05:45:39Z` | 61 | SCORING_COMMIT | 2026-08-28T11:18:26Z | sn61 commit touches scoring: chore: update challenge navigation and fix ADA-3 headless detection s… |
| `sn67:scoring_commit:2026-08-28T06:40:58Z` | 67 | SCORING_COMMIT | 2026-08-28T11:18:26Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20260828.post6 |
| `sn80:scoring_commit:2026-08-28T05:16:34Z` | 80 | SCORING_COMMIT | 2026-08-28T11:18:26Z | sn80 commit touches scoring: docs: point miners to the openroboto CLI and the real-robot track |
| `sn92:scoring_commit:2026-08-28T08:31:19Z` | 92 | SCORING_COMMIT | 2026-08-28T11:18:26Z | sn92 commit touches scoring: Carry the miner's published source through to the control plane |
| `sn96:release:Verathos v0.1.42 – Verified MoE, Account` | 96 | RELEASE | 2026-08-28T11:18:26Z | sn96 released Verathos v0.1.42 – Verified MoE, Account Billing, and Runtime Stability |
| `sn96:scoring_commit:2026-08-26T14:47:41Z` | 96 | SCORING_COMMIT | 2026-08-28T11:18:26Z | sn96 commit touches scoring: fix: decay endpoint-gated scores at epoch close |
| `sn108:scoring_commit:2026-08-28T04:54:03Z` | 108 | SCORING_COMMIT | 2026-08-28T11:18:26Z | sn108 commit touches scoring: docs(validator): the unanimity abort needs two independent sources |
| `sn15:release:v1.2.9` | 15 | RELEASE | 2026-08-28T21:28:55Z | sn15 released v1.2.9 |
| `sn15:scoring_commit:2026-08-28T18:31:26Z` | 15 | SCORING_COMMIT | 2026-08-28T21:28:55Z | sn15 commit touches scoring: fix(validator): use revealed top as weight fallback (#265) |
| `sn21:scoring_commit:2026-08-28T17:07:56Z` | 21 | SCORING_COMMIT | 2026-08-28T21:28:55Z | sn21 commit touches scoring: feat(reporting): each miner's row carries the reason a control acted … |
| `sn25:release:v2026.8.28-1031286130` | 25 | RELEASE | 2026-08-28T21:28:55Z | sn25 released v2026.8.28-1031286130 |
| `sn28:release:v0.4.12` | 28 | RELEASE | 2026-08-28T21:28:55Z | sn28 released v0.4.12 |
| `sn35:release:1.2.0` | 35 | RELEASE | 2026-08-28T21:28:55Z | sn35 released 1.2.0 |
| `sn35:scoring_commit:2026-08-28T16:38:20Z` | 35 | SCORING_COMMIT | 2026-08-28T21:28:55Z | sn35 commit touches scoring: feat: send all miner emissions to scored miners |
| `sn92:scoring_commit:2026-08-28T14:15:37Z` | 92 | SCORING_COMMIT | 2026-08-28T21:28:55Z | sn92 commit touches scoring: Accept operator-named hotkeys ahead of their validator permit |
| `sn102:release:v0.5.3` | 102 | RELEASE | 2026-08-28T21:28:55Z | sn102 released v0.5.3 |
| `sn102:scoring_commit:2026-08-28T13:33:02Z` | 102 | SCORING_COMMIT | 2026-08-28T21:28:55Z | sn102 commit touches scoring: ⏪ fix(shared): stop collapsing miner commits to one model hash |
| `sn108:scoring_commit:2026-08-28T12:10:59Z` | 108 | SCORING_COMMIT | 2026-08-28T21:28:55Z | sn108 commit touches scoring: docs(readme): miner gate is 50 registered AND 25 active members |
| `sn111:scoring_commit:2026-08-28T12:51:57Z` | 111 | SCORING_COMMIT | 2026-08-28T21:28:55Z | sn111 commit touches scoring: docs(validator): enable paper reuse in launch profiles |
| `sn15:release:v1.2.10` | 15 | RELEASE | 2026-08-29T03:23:48Z | sn15 released v1.2.10 |
| `sn25:release:v2026.8.28-1031618120` | 25 | RELEASE | 2026-08-29T03:23:48Z | sn25 released v2026.8.28-1031618120 |
| `sn25:release:v2026.8.28-1031763440` | 25 | RELEASE | 2026-08-29T10:19:28Z | sn25 released v2026.8.28-1031763440 |
| `sn47:scoring_commit:2026-08-29T06:50:23Z` | 47 | SCORING_COMMIT | 2026-08-29T10:19:28Z | sn47 commit touches scoring: rollout verification rules |
| `sn67:scoring_commit:2026-08-29T06:48:42Z` | 67 | SCORING_COMMIT | 2026-08-29T10:19:28Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20260829.post0 |
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
| `sn111:readme_task_diff:4ac99c0122295794` | 111 | README_TASK_DIFF | 2026-08-27T14:33:13Z | sn111 README task/scoring sections changed |
| `sn80:readme_task_diff:a1414d5d9c1406ba` | 80 | README_TASK_DIFF | 2026-08-28T11:18:26Z | sn80 README task/scoring sections changed |
| `sn47:readme_task_diff:3e3cbf15b25c3611` | 47 | README_TASK_DIFF | 2026-08-28T21:28:55Z | sn47 README task/scoring sections changed |
| `sn79:readme_task_diff:cd5eac2da72f58d2` | 79 | README_TASK_DIFF | 2026-08-28T21:28:55Z | sn79 README task/scoring sections changed |
| `sn108:readme_task_diff:e13470c52cc9c2e6` | 108 | README_TASK_DIFF | 2026-08-28T21:28:55Z | sn108 README task/scoring sections changed |
| `sn47:readme_task_diff:40b567f5acce9030` | 47 | README_TASK_DIFF | 2026-08-29T10:19:28Z | sn47 README task/scoring sections changed |
| `sn100:readme_task_diff:86ff6dff152413ad` | 100 | README_TASK_DIFF | 2026-08-29T10:19:28Z | sn100 README task/scoring sections changed |
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

## RESOLVED IN THIS WINDOW

_none_
