# ALARMS - generated 2026-09-29T19:32:43Z, block 9175650

window: first_seen in [2026-09-29T18:18:10Z, 2026-09-29T19:33:10Z)  (60 min interval + 15 min overlap)

Report ONLY the rows under NEW SINCE LAST RUN. Rows under STILL OPEN were
already reported in an earlier window and must not be re-alarmed.

## NEW SINCE LAST RUN

| event_id | netuid | class | severity | first_seen_utc | one_line |
|---|---|---|---|---|---|
| `sn20:burn_drop:0.799` | 20 | BURN_DROP | P0 | 2026-09-29T19:33:10Z | sn20 burn fell 1.000 -> 0.799 - miners can earn again |
| `sn46:burn_drop:0.726` | 46 | BURN_DROP | P0 | 2026-09-29T19:33:10Z | sn46 burn fell 1.000 -> 0.726 - miners can earn again |
| `sn1:release:v4.4.11` | 1 | RELEASE | P1 | 2026-09-29T19:33:10Z | sn1 released v4.4.11 |
| `sn5:scoring_commit:2026-09-29T16:00:26Z` | 5 | SCORING_COMMIT | P1 | 2026-09-29T19:33:10Z | sn5 commit touches scoring: Merge pull request #10 from hone-subnet-org/v3-repo-tasks |
| `sn15:release:v2.0.38: fix(agent): retry a 200 inferen` | 15 | RELEASE | P1 | 2026-09-29T19:33:10Z | sn15 released v2.0.38: fix(agent): retry a 200 inference response whose body is not JSON (#348) |
| `sn20:scoring_commit:2026-09-29T18:56:24Z` | 20 | SCORING_COMMIT | P1 | 2026-09-29T19:33:10Z | sn20 commit touches scoring: Separate website from the public subnet and retain validator evidence… |
| `sn41:scoring_commit:2026-09-28T18:49:08Z` | 41 | SCORING_COMMIT | P1 | 2026-09-29T19:33:10Z | sn41 commit touches scoring: pillar scoring updates around market-relative brier. updating baselin… |
| `sn81:scoring_commit:2026-09-29T15:04:56Z` | 81 | SCORING_COMMIT | P1 | 2026-09-29T19:33:10Z | sn81 commit touches scoring: docs(corpus): ledger v2 migration, verify and rollback in the launch … |
| `sn94:scoring_commit:2026-09-29T14:06:52Z` | 94 | SCORING_COMMIT | P1 | 2026-09-29T19:33:10Z | sn94 commit touches scoring: cli: export the validator's #256 policy file from the signed list |
| `sn5:readme_task_diff:12b2073e10277692` | 5 | README_TASK_DIFF | P2 | 2026-09-29T19:33:10Z | sn5 README task/scoring sections changed |

### detail

- **`sn20:burn_drop:0.799`** - sn20 burn fell 1.000 -> 0.799 - miners can earn again
  - This subnet paid miners nothing and now pays. Worth a look before the field fills up.
- **`sn46:burn_drop:0.726`** - sn46 burn fell 1.000 -> 0.726 - miners can earn again
  - This subnet paid miners nothing and now pays. Worth a look before the field fills up.
- **`sn1:release:v4.4.11`** - sn1 released v4.4.11
  - published 2026-09-29T14:28:28Z (was v4.4.10)
- **`sn5:scoring_commit:2026-09-29T16:00:26Z`** - sn5 commit touches scoring: Merge pull request #10 from hone-subnet-org/v3-repo-tasks
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn15:release:v2.0.38: fix(agent): retry a 200 inferen`** - sn15 released v2.0.38: fix(agent): retry a 200 inference response whose body is not JSON (#348)
  - published 2026-09-29T19:00:41Z (was v2.0.37: fix(proxy): sum inference counters across ProxyClient instances (#347))
- **`sn20:scoring_commit:2026-09-29T18:56:24Z`** - sn20 commit touches scoring: Separate website from the public subnet and retain validator evidence…
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn41:scoring_commit:2026-09-28T18:49:08Z`** - sn41 commit touches scoring: pillar scoring updates around market-relative brier. updating baselin…
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn81:scoring_commit:2026-09-29T15:04:56Z`** - sn81 commit touches scoring: docs(corpus): ledger v2 migration, verify and rollback in the launch …
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn94:scoring_commit:2026-09-29T14:06:52Z`** - sn94 commit touches scoring: cli: export the validator's #256 policy file from the signed list
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn5:readme_task_diff:12b2073e10277692`** - sn5 README task/scoring sections changed
  - Only the task-describing headings are hashed, so badge and typo edits do not trigger this.

## STILL OPEN (already reported - do not re-alarm)

| event_id | netuid | class | first_seen_utc | one_line |
|---|---|---|---|---|
| `sn100:burn_drop:0.708` | 100 | BURN_DROP | 2026-09-23T01:38:19Z | sn100 burn fell 1.000 -> 0.708 - miners can earn again |
| `sn71:burn_drop:0.783` | 71 | BURN_DROP | 2026-09-24T06:47:57Z | sn71 burn fell 1.000 -> 0.783 - miners can earn again |
| `sn112:burn_drop:0.850` | 112 | BURN_DROP | 2026-09-25T10:09:24Z | sn112 burn fell 1.000 -> 0.850 - miners can earn again |
| `sn122:burn_drop:0.724` | 122 | BURN_DROP | 2026-09-27T22:27:12Z | sn122 burn fell 1.000 -> 0.724 - miners can earn again |
| `sn121:burn_drop:0.600` | 121 | BURN_DROP | 2026-09-28T21:19:29Z | sn121 burn fell 1.000 -> 0.600 - miners can earn again |
| `sn25:scoring_commit:2026-09-22T18:16:13Z` | 25 | SCORING_COMMIT | 2026-09-22T20:21:06Z | sn25 commit touches scoring: Resume bounded parallel miner fault controls across transient failures |
| `sn71:scoring_commit:2026-09-22T19:58:10Z` | 71 | SCORING_COMMIT | 2026-09-22T20:21:06Z | sn71 commit touches scoring: Verify shadow rounds under current Arena scheduling policy |
| `sn74:release:release-20260922-190530: spark-hermes: f` | 74 | RELEASE | 2026-09-22T20:21:06Z | sn74 released release-20260922-190530: spark-hermes: full scoring config (50% maintainer cut) (#1791) |
| `sn120:scoring_commit:2026-09-22T19:35:26Z` | 120 | SCORING_COMMIT | 2026-09-22T20:21:06Z | sn120 commit touches scoring: AA gap-fill go-live 1/2: affine_scitext e1 (202 teacher-verified vari… |
| `sn14:release:glm53-mock-submission-20260906: Merge m3` | 14 | RELEASE | 2026-09-22T23:08:21Z | sn14 released glm53-mock-submission-20260906: Merge m3-runtime-seed-restore into main (#108) |
| `sn56:scoring_commit:2026-09-22T22:03:29Z` | 56 | SCORING_COMMIT | 2026-09-22T23:08:21Z | sn56 commit touches scoring: Add Runpod evaluation backend via dstack (#1386) |
| `sn25:release:v2026.9.22-1053244730` | 25 | RELEASE | 2026-09-23T01:38:19Z | sn25 released v2026.9.22-1053244730 |
| `sn78:scoring_commit:2026-09-23T02:08:31Z` | 78 | SCORING_COMMIT | 2026-09-23T06:45:27Z | sn78 commit touches scoring: Retry interrupted miner downloads and redact clip capabilities from l… |
| `sn120:scoring_commit:2026-09-23T03:12:20Z` | 120 | SCORING_COMMIT | 2026-09-23T06:45:27Z | sn120 commit touches scoring: wvk 23 live 17:20 UTC: AGENTS.md snapshot + Discord live lines (first… |
| `sn28:scoring_commit:2026-09-23T11:46:58Z` | 28 | SCORING_COMMIT | 2026-09-23T12:19:18Z | sn28 commit touches scoring: ci: validate rendered Envoy configs with the pinned Envoy image |
| `sn51:scoring_commit:2026-09-23T11:44:49Z` | 51 | SCORING_COMMIT | 2026-09-23T12:19:18Z | sn51 commit touches scoring: DAH-3505 - [P2] validator: keep the Docker SDK's SSH session alive th… |
| `sn67:scoring_commit:2026-09-23T07:25:23Z` | 67 | SCORING_COMMIT | 2026-09-23T12:19:18Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20260923.post2 |
| `sn71:scoring_commit:2026-09-23T08:39:50Z` | 71 | SCORING_COMMIT | 2026-09-23T12:19:18Z | sn71 commit touches scoring: Document company-only validator compatibility |
| `sn97:scoring_commit:2026-09-23T11:59:47Z` | 97 | SCORING_COMMIT | 2026-09-23T12:19:18Z | sn97 commit touches scoring: fix: show tasks and trajectories on the detail page of every distribu… |
| `sn9:release:v4.13.2` | 9 | RELEASE | 2026-09-23T17:21:31Z | sn9 released v4.13.2 |
| `sn25:release:v2026.9.23-1053753970` | 25 | RELEASE | 2026-09-23T17:21:31Z | sn25 released v2026.9.23-1053753970 |
| `sn97:scoring_commit:2026-09-23T15:58:19Z` | 97 | SCORING_COMMIT | 2026-09-23T17:21:31Z | sn97 commit touches scoring: chore: show float score instead of a 0/1 mark |
| `sn120:scoring_commit:2026-09-23T12:45:56Z` | 120 | SCORING_COMMIT | 2026-09-23T17:21:31Z | sn120 commit touches scoring: Merge PR #3 (cursor/discord-mirror-1b92): ops: discord-mirror — archi… |
| `sn14:scoring_commit:2026-09-23T10:47:00Z` | 14 | SCORING_COMMIT | 2026-09-23T20:35:56Z | sn14 commit touches scoring: Drain evaluation workers and remove redundant recovery splits |
| `sn15:scoring_commit:2026-09-23T19:01:26Z` | 15 | SCORING_COMMIT | 2026-09-23T20:35:56Z | sn15 commit touches scoring: docs: correct local-test EnvPack size, families, and runtime/verifier… |
| `sn25:release:v2026.9.23-1053868550` | 25 | RELEASE | 2026-09-23T20:35:56Z | sn25 released v2026.9.23-1053868550 |
| `sn25:scoring_commit:2026-09-23T08:56:00Z` | 25 | SCORING_COMMIT | 2026-09-23T20:35:56Z | sn25 commit touches scoring: Preserve validator readback transport errors and request deadlines |
| `sn28:release:v0.4.21-dev` | 28 | RELEASE | 2026-09-23T20:35:56Z | sn28 released v0.4.21-dev |
| `sn28:scoring_commit:2026-09-23T20:17:29Z` | 28 | SCORING_COMMIT | 2026-09-23T20:35:56Z | sn28 commit touches scoring: feat(image): route Chutes -TEE requests through the attestation verif… |
| `sn120:scoring_commit:2026-09-23T21:51:12Z` | 120 | SCORING_COMMIT | 2026-09-23T23:14:27Z | sn120 commit touches scoring: Merge PR #66 (cursor/band-backfill-outcomes-8929): env-backfill task … |
| `sn120:scoring_commit:2026-09-23T22:13:58Z` | 120 | SCORING_COMMIT | 2026-09-24T01:35:20Z | sn120 commit touches scoring: rollouts.prepass: --uids-file restricts the pool to listed task uids … |
| `sn21:release:SN21 rich training data v3 (slice 2)` | 21 | RELEASE | 2026-09-24T06:47:57Z | sn21 released SN21 rich training data v3 (slice 2) |
| `sn51:scoring_commit:2026-09-24T06:27:30Z` | 51 | SCORING_COMMIT | 2026-09-24T06:47:57Z | sn51 commit touches scoring: DAH-3521 - [P1] validator: a custom build reaches the node's own DNS … |
| `sn71:scoring_commit:2026-09-24T06:33:26Z` | 71 | SCORING_COMMIT | 2026-09-24T06:47:57Z | sn71 commit touches scoring: Bind final verifier extraction release to committed source |
| `sn1:release:v4.4.9` | 1 | RELEASE | 2026-09-24T12:42:03Z | sn1 released v4.4.9 |
| `sn9:release:v4.13.3` | 9 | RELEASE | 2026-09-24T12:42:03Z | sn9 released v4.13.3 |
| `sn22:scoring_commit:2026-08-21T14:46:57Z` | 22 | SCORING_COMMIT | 2026-09-24T12:42:03Z | sn22 commit touches scoring: feat: reject sources a miner could have served itself |
| `sn28:release:v0.4.21` | 28 | RELEASE | 2026-09-24T12:42:03Z | sn28 released v0.4.21 |
| `sn28:scoring_commit:2026-09-24T08:59:00Z` | 28 | SCORING_COMMIT | 2026-09-24T12:42:03Z | sn28 commit touches scoring: chore(release): promote gm-miner 0.4.21 (#274) |
| `sn51:release:executor-v1.135` | 51 | RELEASE | 2026-09-24T12:42:03Z | sn51 released executor-v1.135 |
| `sn51:scoring_commit:2026-09-24T12:38:05Z` | 51 | SCORING_COMMIT | 2026-09-24T12:42:03Z | sn51 commit touches scoring: Validator: pull a present image when the registry tag moved (#1468) |
| `sn71:scoring_commit:2026-09-24T11:42:05Z` | 71 | SCORING_COMMIT | 2026-09-24T12:42:03Z | sn71 commit touches scoring: Preserve local visible article headers in verifier evidence |
| `sn20:scoring_commit:2026-09-24T16:34:09Z` | 20 | SCORING_COMMIT | 2026-09-24T17:35:05Z | sn20 commit touches scoring: Ground native semantic scoring in clip evidence |
| `sn25:scoring_commit:2026-09-24T13:07:35Z` | 25 | SCORING_COMMIT | 2026-09-24T17:35:05Z | sn25 commit touches scoring: Derive policy rollover activations from verified V2 terminal |
| `sn28:release:v0.4.22-dev` | 28 | RELEASE | 2026-09-24T17:35:05Z | sn28 released v0.4.22-dev |
| `sn28:scoring_commit:2026-09-24T17:21:09Z` | 28 | SCORING_COMMIT | 2026-09-24T17:35:05Z | sn28 commit touches scoring: chore(release): gm-miner 0.4.22-dev (#277) |
| `sn71:scoring_commit:2026-09-24T17:22:54Z` | 71 | SCORING_COMMIT | 2026-09-24T17:35:05Z | sn71 commit touches scoring: chore(release): bind verifier evidence reuse source |
| `sn15:release:v2.0.30: fix(validator): lower default s` | 15 | RELEASE | 2026-09-24T20:48:43Z | sn15 released v2.0.30: fix(validator): lower default sandbox max workers to 30 |
| `sn15:scoring_commit:2026-09-24T18:59:25Z` | 15 | SCORING_COMMIT | 2026-09-24T20:48:43Z | sn15 commit touches scoring: fix(validator): lower default sandbox max workers to 30 |
| `sn25:release:v2026.9.24-1054792560` | 25 | RELEASE | 2026-09-24T20:48:43Z | sn25 released v2026.9.24-1054792560 |
| `sn25:scoring_commit:2026-09-24T20:12:46Z` | 25 | SCORING_COMMIT | 2026-09-24T20:48:43Z | sn25 commit touches scoring: Retain on-chain proof of R42 validator source-slot failure |
| `sn28:release:v0.4.23` | 28 | RELEASE | 2026-09-24T20:48:43Z | sn28 released v0.4.23 |
| `sn28:scoring_commit:2026-09-24T19:58:11Z` | 28 | SCORING_COMMIT | 2026-09-24T20:48:43Z | sn28 commit touches scoring: chore(release): promote gm-miner 0.4.23 (#280) |
| `sn45:scoring_commit:2026-09-24T19:23:02Z` | 45 | SCORING_COMMIT | 2026-09-24T20:48:43Z | sn45 commit touches scoring: Score the stock anchor on a sample of audits |
| `sn46:scoring_commit:2026-09-18T08:40:59Z` | 46 | SCORING_COMMIT | 2026-09-24T20:48:43Z | sn46 commit touches scoring: Merge pull request #5 from Subnet46/docs/validator-requirements |
| `sn71:scoring_commit:2026-09-24T20:11:33Z` | 71 | SCORING_COMMIT | 2026-09-24T20:48:43Z | sn71 commit touches scoring: chore(release): bind verifier cache and semantic fixes |
| `sn100:scoring_commit:2026-09-24T18:24:45Z` | 100 | SCORING_COMMIT | 2026-09-24T20:48:43Z | sn100 commit touches scoring: feat(challenges): load docker challenges and move bounty out (#312) |
| `sn69:scoring_commit:2026-09-24T15:23:49Z` | 69 | SCORING_COMMIT | 2026-09-24T23:51:50Z | sn69 commit touches scoring: Merge the v2 validator into dev |
| `sn91:scoring_commit:2026-09-24T22:23:56Z` | 91 | SCORING_COMMIT | 2026-09-24T23:51:50Z | sn91 commit touches scoring: trainer: verify harvested funded checkpoints against in-memory tensor… |
| `sn120:scoring_commit:2026-09-24T08:48:05Z` | 120 | SCORING_COMMIT | 2026-09-24T23:51:50Z | sn120 commit touches scoring: kingboard matrix: leak-audited SWE cells show the score excluding lea… |
| `sn25:release:v2026.9.24-1054966040` | 25 | RELEASE | 2026-09-25T04:49:29Z | sn25 released v2026.9.24-1054966040 |
| `sn71:scoring_commit:2026-09-25T02:03:16Z` | 71 | SCORING_COMMIT | 2026-09-25T04:49:29Z | sn71 commit touches scoring: Bind protected verifier workflows to reviewed stage evidence change |
| `sn120:scoring_commit:2026-09-25T00:41:24Z` | 120 | SCORING_COMMIT | 2026-09-25T04:49:29Z | sn120 commit touches scoring: bench_fail chat suites: option (i) + reasoning-only waiver -- validat… |
| `sn51:release:miner-v1.005` | 51 | RELEASE | 2026-09-25T10:09:24Z | sn51 released miner-v1.005 |
| `sn71:scoring_commit:2026-09-25T08:06:33Z` | 71 | SCORING_COMMIT | 2026-09-25T10:09:24Z | sn71 commit touches scoring: Retain verified Greenhouse department metadata for intent review |
| `sn91:scoring_commit:2026-09-25T05:08:49Z` | 91 | SCORING_COMMIT | 2026-09-25T10:09:24Z | sn91 commit touches scoring: Merge pull request #315 from TensorLink-AI/fix/promotion-scoring-cfg-… |
| `sn96:release:Verathos v0.2.3 – DeepSeek Mesh Proof Co` | 96 | RELEASE | 2026-09-25T10:09:24Z | sn96 released Verathos v0.2.3 – DeepSeek Mesh Proof Compatibility |
| `sn25:scoring_commit:2026-09-25T14:49:07Z` | 25 | SCORING_COMMIT | 2026-09-25T15:24:37Z | sn25 commit touches scoring: competition: clarify staging finalization in score contract |
| `sn51:scoring_commit:2026-09-25T12:37:33Z` | 51 | SCORING_COMMIT | 2026-09-25T15:24:37Z | sn51 commit touches scoring: DAH-3467 - [P2] validator: inspect after a timed-out docker rm before… |
| `sn66:scoring_commit:2026-09-25T09:57:35Z` | 66 | SCORING_COMMIT | 2026-09-25T15:24:37Z | sn66 commit touches scoring: Withhold a miner's source while it is on the Pareto frontier |
| `sn71:scoring_commit:2026-09-25T15:07:15Z` | 71 | SCORING_COMMIT | 2026-09-25T15:24:37Z | sn71 commit touches scoring: Bind verified activity repair to committed protected source |
| `sn102:release:v0.6.4 — the reference miner trains the ` | 102 | RELEASE | 2026-09-25T15:24:37Z | sn102 released v0.6.4 — the reference miner trains the full model |
| `sn102:scoring_commit:2026-09-25T14:15:25Z` | 102 | SCORING_COMMIT | 2026-09-25T15:24:37Z | sn102 commit touches scoring: Merge pull request #283 from Connito-AI/feat/miner-full-topology |
| `sn111:scoring_commit:2026-09-25T13:39:45Z` | 111 | SCORING_COMMIT | 2026-09-25T15:24:37Z | sn111 commit touches scoring: docs(miner): update V1 consensus review setup |
| `sn15:release:v2.0.31: fix(proxy): re-resolve Backend ` | 15 | RELEASE | 2026-09-25T19:26:50Z | sn15 released v2.0.31: fix(proxy): re-resolve Backend host for allowlist fetch (#334) |
| `sn15:scoring_commit:2026-09-25T18:07:06Z` | 15 | SCORING_COMMIT | 2026-09-25T19:26:50Z | sn15 commit touches scoring: refactor(validator): simplify session call orchestration |
| `sn71:scoring_commit:2026-09-25T16:34:18Z` | 71 | SCORING_COMMIT | 2026-09-25T19:26:50Z | sn71 commit touches scoring: Preserve terminal verified intent evidence within Arena retries |
| `sn74:release:release-20260925-183535` | 74 | RELEASE | 2026-09-25T19:26:50Z | sn74 released release-20260925-183535 |
| `sn100:scoring_commit:2026-09-25T18:28:24Z` | 100 | SCORING_COMMIT | 2026-09-25T19:26:50Z | sn100 commit touches scoring: test(network): verify opentype 75/25 sealed payouts (#314) |
| `sn1:release:v4.4.10` | 1 | RELEASE | 2026-09-25T22:43:10Z | sn1 released v4.4.10 |
| `sn62:release:v0.3.7` | 62 | RELEASE | 2026-09-26T06:07:24Z | sn62 released v0.3.7 |
| `sn71:scoring_commit:2026-09-26T03:45:10Z` | 71 | SCORING_COMMIT | 2026-09-26T06:07:24Z | sn71 commit touches scoring: Allow focused validation of saved Arena output assignments |
| `sn71:scoring_commit:2026-09-26T08:19:27Z` | 71 | SCORING_COMMIT | 2026-09-26T11:22:54Z | sn71 commit touches scoring: Bind protected verifier manifest to alias fix |
| `sn120:scoring_commit:2026-09-26T09:23:06Z` | 120 | SCORING_COMMIT | 2026-09-26T11:22:54Z | sn120 commit touches scoring: wvk 25 scoring bundle STAGED (all knobs off until T0 2026-09-30 14:00… |
| `sn7:release:release-20260926-135859` | 7 | RELEASE | 2026-09-26T15:04:18Z | sn7 released release-20260926-135859 |
| `sn7:scoring_commit:2026-09-25T17:45:15Z` | 7 | SCORING_COMMIT | 2026-09-26T15:04:18Z | sn7 commit touches scoring: Hide alpha price flags from alw miner quotes --help (#756) |
| `sn14:scoring_commit:2026-09-26T14:38:01Z` | 14 | SCORING_COMMIT | 2026-09-26T15:04:18Z | sn14 commit touches scoring: Show potential winners and link scoring baselines (#127) |
| `sn22:scoring_commit:2026-09-25T07:25:31Z` | 22 | SCORING_COMMIT | 2026-09-26T15:04:18Z | sn22 commit touches scoring: feat: burn all emission and stop querying miners until the next releas |
| `sn81:scoring_commit:2026-09-26T12:28:35Z` | 81 | SCORING_COMMIT | 2026-09-26T15:04:18Z | sn81 commit touches scoring: docs(corpus): the task has no seats; audit throughput only delays pay… |
| `sn71:scoring_commit:2026-09-26T17:32:25Z` | 71 | SCORING_COMMIT | 2026-09-26T18:34:12Z | sn71 commit touches scoring: Bind protected manifest to evidence quality verifier source |
| `sn81:scoring_commit:2026-09-26T18:16:53Z` | 81 | SCORING_COMMIT | 2026-09-26T18:34:12Z | sn81 commit touches scoring: Merge pull request #281 from reliquadotai/fix/corpus-miner-long-contex |
| `sn15:release:v2.0.32: fix(validator): save downloaded` | 15 | RELEASE | 2026-09-26T21:37:04Z | sn15 released v2.0.32: fix(validator): save downloaded agent source as raw bytes (#336) |
| `sn15:scoring_commit:2026-09-26T19:43:24Z` | 15 | SCORING_COMMIT | 2026-09-26T21:37:04Z | sn15 commit touches scoring: fix(validator): save downloaded agent source as raw bytes (#336) |
| `sn25:release:v2026.9.26-1056505490` | 25 | RELEASE | 2026-09-26T21:37:04Z | sn25 released v2026.9.26-1056505490 |
| `sn71:scoring_commit:2026-09-26T19:50:49Z` | 71 | SCORING_COMMIT | 2026-09-26T21:37:04Z | sn71 commit touches scoring: Reuse verified investigator source for attribute repair |
| `sn71:scoring_commit:2026-09-26T23:16:13Z` | 71 | SCORING_COMMIT | 2026-09-26T23:56:43Z | sn71 commit touches scoring: Bind verified homepage navigation source |
| `sn25:release:v2026.9.26-1056759680` | 25 | RELEASE | 2026-09-27T05:12:30Z | sn25 released v2026.9.26-1056759680 |
| `sn34:scoring_commit:2026-09-27T03:46:53Z` | 34 | SCORING_COMMIT | 2026-09-27T05:12:30Z | sn34 commit touches scoring: Merge pull request #464 from BitMind-AI/docs/align-taxonomy-and-scorin |
| `sn71:scoring_commit:2026-09-27T03:42:38Z` | 71 | SCORING_COMMIT | 2026-09-27T05:12:30Z | sn71 commit touches scoring: Preserve fresh investigation budget when reusing verified source pages |
| `sn15:release:v2.0.34: Authorize inference without a s` | 15 | RELEASE | 2026-09-27T10:40:11Z | sn15 released v2.0.34: Authorize inference without a shared Compose mount |
| `sn61:release:4.10.7` | 61 | RELEASE | 2026-09-27T10:40:11Z | sn61 released 4.10.7 |
| `sn61:scoring_commit:2026-09-27T10:35:08Z` | 61 | SCORING_COMMIT | 2026-09-27T10:40:11Z | sn61 commit touches scoring: Merge pull request #149 from RedTeamSubnet/challenge/bex_tracker |
| `sn71:scoring_commit:2026-09-27T08:15:54Z` | 71 | SCORING_COMMIT | 2026-09-27T10:40:11Z | sn71 commit touches scoring: Bind verifier evidence continuity to reviewed source |
| `sn120:scoring_commit:2026-09-27T08:35:30Z` | 120 | SCORING_COMMIT | 2026-09-27T10:40:11Z | sn120 commit touches scoring: wvk 25 δ fork: flip time 08:35 UTC in AGENTS.md; Discord links |
| `sn71:scoring_commit:2026-09-27T14:35:41Z` | 71 | SCORING_COMMIT | 2026-09-27T15:20:39Z | sn71 commit touches scoring: Bind verifier release to current Arena base |
| `sn111:scoring_commit:2026-09-27T13:52:01Z` | 111 | SCORING_COMMIT | 2026-09-27T15:20:39Z | sn111 commit touches scoring: perf(miner): default consensus review to single-case batches with 50 … |
| `sn120:scoring_commit:2026-09-27T11:40:34Z` | 120 | SCORING_COMMIT | 2026-09-27T15:20:39Z | sn120 commit touches scoring: Merge PR #78 (cursor/task-instruction-gate-8929): task-instruction ga… |
| `sn78:release:Linux amd64 validator recovery installer` | 78 | RELEASE | 2026-09-27T19:09:06Z | sn78 released Linux amd64 validator recovery installer (c0503f5) |
| `sn81:scoring_commit:2026-09-27T16:59:58Z` | 81 | SCORING_COMMIT | 2026-09-27T19:09:06Z | sn81 commit touches scoring: feat(corpus): serve the task's contract and let the miner fetch it |
| `sn111:scoring_commit:2026-09-27T17:45:19Z` | 111 | SCORING_COMMIT | 2026-09-27T19:09:06Z | sn111 commit touches scoring: fix(consensus): exclude validators from reviewer selection |
| `sn56:scoring_commit:2026-09-27T21:33:47Z` | 56 | SCORING_COMMIT | 2026-09-27T22:27:12Z | sn56 commit touches scoring: 3 task round 1 image (#1387) |
| `sn78:release:Yuma validator recovery package 0.1.0` | 78 | RELEASE | 2026-09-27T22:27:12Z | sn78 released Yuma validator recovery package 0.1.0 |
| `sn15:release:v2.0.35: Log nested inference tool types` | 15 | RELEASE | 2026-09-28T01:05:42Z | sn15 released v2.0.35: Log nested inference tool types in proxy access logs |
| `sn15:scoring_commit:2026-09-27T22:53:19Z` | 15 | SCORING_COMMIT | 2026-09-28T01:05:42Z | sn15 commit touches scoring: chore(deps): bump anyio from 4.13.0 to 4.14.2 in /docker/validator |
| `sn28:release:v0.4.24-dev` | 28 | RELEASE | 2026-09-28T01:05:42Z | sn28 released v0.4.24-dev |
| `sn28:scoring_commit:2026-09-27T23:56:42Z` | 28 | SCORING_COMMIT | 2026-09-28T01:05:42Z | sn28 commit touches scoring: chore(release): gm-miner 0.4.24-dev (#290) |
| `sn71:scoring_commit:2026-09-27T22:36:31Z` | 71 | SCORING_COMMIT | 2026-09-28T01:05:42Z | sn71 commit touches scoring: Bind final evidence resolution verifier release |
| `sn91:release:worker-v0.8.2` | 91 | RELEASE | 2026-09-28T01:05:42Z | sn91 released worker-v0.8.2 |
| `sn71:scoring_commit:2026-09-28T02:46:34Z` | 71 | SCORING_COMMIT | 2026-09-28T06:49:13Z | sn71 commit touches scoring: Verify cross-domain company rebrands |
| `sn20:scoring_commit:2026-09-28T15:15:07Z` | 20 | SCORING_COMMIT | 2026-09-28T15:21:54Z | sn20 commit touches scoring: Initialize public Witness subnet with bounded five-video evaluation |
| `sn26:scoring_commit:2026-09-28T12:26:31Z` | 26 | SCORING_COMMIT | 2026-09-28T15:21:54Z | sn26 commit touches scoring: fix: seed evaluation sampling from the pinned dataset commit so it ca… |
| `sn28:release:v0.4.24` | 28 | RELEASE | 2026-09-28T15:21:54Z | sn28 released v0.4.24 |
| `sn28:scoring_commit:2026-09-28T09:37:40Z` | 28 | SCORING_COMMIT | 2026-09-28T15:21:54Z | sn28 commit touches scoring: chore(release): promote gm-miner 0.4.24 (#291) |
| `sn41:scoring_commit:2026-09-28T13:20:51Z` | 41 | SCORING_COMMIT | 2026-09-28T15:21:54Z | sn41 commit touches scoring: Merge pull request #49 from corvxai/forecast_scoring_lastPredictedAt |
| `sn51:scoring_commit:2026-09-28T14:32:49Z` | 51 | SCORING_COMMIT | 2026-09-28T15:21:54Z | sn51 commit touches scoring: NO-TICKET - [P1] validator: an idle node that cannot pull from Docker… |
| `sn66:scoring_commit:2026-09-28T12:57:35Z` | 66 | SCORING_COMMIT | 2026-09-28T15:21:54Z | sn66 commit touches scoring: Merge pull request #109 from conjectures-io/chore/remove-legacy-scorin |
| `sn111:release:v1.0.0` | 111 | RELEASE | 2026-09-28T15:21:54Z | sn111 released v1.0.0 |
| `sn20:scoring_commit:2026-09-28T18:47:48Z` | 20 | SCORING_COMMIT | 2026-09-28T21:19:29Z | sn20 commit touches scoring: Allow verified Archive download mirrors for restricted routes |
| `sn34:scoring_commit:2026-09-28T18:21:09Z` | 34 | SCORING_COMMIT | 2026-09-28T21:19:29Z | sn34 commit touches scoring: Show recent chain-verified reveals alongside validator submissions |
| `sn45:scoring_commit:2026-09-28T16:32:06Z` | 45 | SCORING_COMMIT | 2026-09-28T21:19:29Z | sn45 commit touches scoring: Skip a validation sample when the validator's own reference call retu… |
| `sn51:scoring_commit:2026-09-28T16:19:46Z` | 51 | SCORING_COMMIT | 2026-09-28T21:19:29Z | sn51 commit touches scoring: DAH-3804 - [P1] validator: a new node is rentable in minutes (fast pa… |
| `sn94:release:Cathedral static TDX verifier cathedral-` | 94 | RELEASE | 2026-09-28T21:19:29Z | sn94 released Cathedral static TDX verifier cathedral-tdx-verifier-v1.0.0 |
| `sn94:scoring_commit:2026-09-28T07:10:07Z` | 94 | SCORING_COMMIT | 2026-09-28T21:19:29Z | sn94 commit touches scoring: docs: state what the TDX and SNP validators actually apply (#203) |
| `sn100:scoring_commit:2026-09-28T21:11:51Z` | 100 | SCORING_COMMIT | 2026-09-28T21:19:29Z | sn100 commit touches scoring: feat(master): send the completed epoch's chain time to challenges (#31 |
| `sn15:release:v2.0.36: Send validator heartbeats every` | 15 | RELEASE | 2026-09-29T01:08:37Z | sn15 released v2.0.36: Send validator heartbeats every eight seconds |
| `sn15:scoring_commit:2026-09-28T23:17:34Z` | 15 | SCORING_COMMIT | 2026-09-29T01:08:37Z | sn15 commit touches scoring: Send validator heartbeats every eight seconds |
| `sn51:scoring_commit:2026-09-29T05:54:45Z` | 51 | SCORING_COMMIT | 2026-09-29T07:14:20Z | sn51 commit touches scoring: DAH-2870 - [P2] protocol 1.4.0: pod_ssh and validation_event on Execu… |
| `sn61:release:4.10.8` | 61 | RELEASE | 2026-09-29T07:14:20Z | sn61 released 4.10.8 |
| `sn61:scoring_commit:2026-09-29T06:36:25Z` | 61 | SCORING_COMMIT | 2026-09-29T07:14:20Z | sn61 commit touches scoring: refactor: move bot_virus to inactive challenges and update bex_tracer… |
| `sn15:release:v2.0.37: fix(proxy): sum inference count` | 15 | RELEASE | 2026-09-29T14:13:00Z | sn15 released v2.0.37: fix(proxy): sum inference counters across ProxyClient instances (#347) |
| `sn23:scoring_commit:2026-09-29T10:36:58Z` | 23 | SCORING_COMMIT | 2026-09-29T14:13:00Z | sn23 commit touches scoring: Merge pull request #57 from TrishoolAI/validator-build-fix |
| `sn46:release:v0.1.2` | 46 | RELEASE | 2026-09-29T14:13:00Z | sn46 released v0.1.2 |
| `sn46:scoring_commit:2026-09-28T17:59:23Z` | 46 | SCORING_COMMIT | 2026-09-29T14:13:00Z | sn46 commit touches scoring: Burn whatever leaves the miners the summary's signed USD target, pric… |
| `sn51:release:executor-v1.136` | 51 | RELEASE | 2026-09-29T14:13:00Z | sn51 released executor-v1.136 |
| `sn53:scoring_commit:2026-09-29T09:45:05Z` | 53 | SCORING_COMMIT | 2026-09-29T14:13:00Z | sn53 commit touches scoring: Merge pull request #51 from hanlinai/docs/miner-provider-docs-pointer |
| `sn69:scoring_commit:2026-09-26T06:16:04Z` | 69 | SCORING_COMMIT | 2026-09-29T14:13:00Z | sn69 commit touches scoring: Merge pull request #17 from HeraldMedia/miner-key-lifecycle |
| `sn94:scoring_commit:2026-09-29T13:47:13Z` | 94 | SCORING_COMMIT | 2026-09-29T14:13:00Z | sn94 commit touches scoring: Merge pull request #225 from skyrocket2026/feat/central-access-verifie |
| `sn28:readme_task_diff:b07f84dabcd1a3a1` | 28 | README_TASK_DIFF | 2026-09-23T20:35:56Z | sn28 README task/scoring sections changed |
| `sn88:readme_task_diff:71d034a5ee0cc823` | 88 | README_TASK_DIFF | 2026-09-24T20:48:43Z | sn88 README task/scoring sections changed |
| `sn69:readme_task_diff:3d7258dffafe1a92` | 69 | README_TASK_DIFF | 2026-09-24T23:51:50Z | sn69 README task/scoring sections changed |
| `sn111:readme_task_diff:134d009e42d9c43d` | 111 | README_TASK_DIFF | 2026-09-25T15:24:37Z | sn111 README task/scoring sections changed |
| `sn25:readme_task_diff:8299976ab43651d9` | 25 | README_TASK_DIFF | 2026-09-26T11:22:54Z | sn25 README task/scoring sections changed |
| `sn34:readme_task_diff:46170c9c42dc2e42` | 34 | README_TASK_DIFF | 2026-09-27T05:12:30Z | sn34 README task/scoring sections changed |
| `sn111:readme_task_diff:6726c60aad04c385` | 111 | README_TASK_DIFF | 2026-09-27T15:20:39Z | sn111 README task/scoring sections changed |
| `sn28:readme_task_diff:f38f4d2e27184292` | 28 | README_TASK_DIFF | 2026-09-28T01:05:42Z | sn28 README task/scoring sections changed |
| `sn94:readme_task_diff:f2d2965f7776dbf2` | 94 | README_TASK_DIFF | 2026-09-28T21:19:29Z | sn94 README task/scoring sections changed |
| `sn51:readme_task_diff:170d4566869a3dcc` | 51 | README_TASK_DIFF | 2026-09-29T07:14:20Z | sn51 README task/scoring sections changed |
| `sn53:readme_task_diff:298e8500ae9f9443` | 53 | README_TASK_DIFF | 2026-09-29T14:13:00Z | sn53 README task/scoring sections changed |
| `sn69:readme_task_diff:ad40463d48698a60` | 69 | README_TASK_DIFF | 2026-09-29T14:13:00Z | sn69 README task/scoring sections changed |

## RESOLVED IN THIS WINDOW

_none_
