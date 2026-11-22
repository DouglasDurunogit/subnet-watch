# ALARMS - generated 2026-11-22T22:26:18Z, block 9565192

window: first_seen in [2026-11-22T21:11:39Z, 2026-11-22T22:26:39Z)  (60 min interval + 15 min overlap)

Report ONLY the rows under NEW SINCE LAST RUN. Rows under STILL OPEN were
already reported in an earlier window and must not be re-alarmed.

## NEW SINCE LAST RUN

| event_id | netuid | class | severity | first_seen_utc | one_line |
|---|---|---|---|---|---|
| `sn37:burn_drop:0.738` | 37 | BURN_DROP | P0 | 2026-11-22T22:26:39Z | sn37 burn fell 0.997 -> 0.738 - miners can earn again |
| `sn70:release:build-v2026.11.22: ci: 90-minute limits ` | 70 | RELEASE | P1 | 2026-11-22T22:26:39Z | sn70 released build-v2026.11.22: ci: 90-minute limits for the test jobs |
| `sn71:scoring_commit:2026-11-22T20:43:38Z` | 71 | SCORING_COMMIT | P1 | 2026-11-22T22:26:39Z | sn71 commit touches scoring: Stop assigning execution to a validator missing the sandbox installer |
| `sn91:scoring_commit:2026-11-22T22:00:58Z` | 91 | SCORING_COMMIT | P1 | 2026-11-22T22:26:39Z | sn91 commit touches scoring: docs(laned): WB20 lane B in MINER, INTERFACE, AGENT_MINING and VALIDA… |

### detail

- **`sn37:burn_drop:0.738`** - sn37 burn fell 0.997 -> 0.738 - miners can earn again
  - This subnet paid miners nothing and now pays. Worth a look before the field fills up.
- **`sn70:release:build-v2026.11.22: ci: 90-minute limits `** - sn70 released build-v2026.11.22: ci: 90-minute limits for the test jobs
  - published 2026-11-22T21:08:56Z (was SUPERSEDED: use image-v2026.11.17b)
- **`sn71:scoring_commit:2026-11-22T20:43:38Z`** - sn71 commit touches scoring: Stop assigning execution to a validator missing the sandbox installer
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn91:scoring_commit:2026-11-22T22:00:58Z`** - sn91 commit touches scoring: docs(laned): WB20 lane B in MINER, INTERFACE, AGENT_MINING and VALIDA…
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.

## STILL OPEN (already reported - do not re-alarm)

| event_id | netuid | class | first_seen_utc | one_line |
|---|---|---|---|---|
| `sn26:burn_drop:0.000` | 26 | BURN_DROP | 2026-11-15T23:57:01Z | sn26 burn fell 1.000 -> 0.000 - miners can earn again |
| `sn113:burn_drop:0.000` | 113 | BURN_DROP | 2026-11-17T17:44:54Z | sn113 burn fell 1.000 -> 0.000 - miners can earn again |
| `sn7:burn_drop:0.000` | 7 | BURN_DROP | 2026-11-18T00:00:43Z | sn7 burn fell 1.000 -> 0.000 - miners can earn again |
| `sn109:burn_drop:0.000` | 109 | BURN_DROP | 2026-11-18T23:10:24Z | sn109 burn fell 1.000 -> 0.000 - miners can earn again |
| `sn99:burn_drop:0.500` | 99 | BURN_DROP | 2026-11-19T21:51:45Z | sn99 burn fell 1.000 -> 0.500 - miners can earn again |
| `sn2:burn_drop:0.936` | 2 | BURN_DROP | 2026-11-20T03:04:29Z | sn2 burn fell 1.000 -> 0.936 - miners can earn again |
| `sn84:burn_drop:0.000` | 84 | BURN_DROP | 2026-11-20T11:26:47Z | sn84 burn fell 1.000 -> 0.000 - miners can earn again |
| `sn58:burn_drop:0.300` | 58 | BURN_DROP | 2026-11-20T19:14:02Z | sn58 burn fell 1.000 -> 0.300 - miners can earn again |
| `sn57:burn_drop:0.000` | 57 | BURN_DROP | 2026-11-21T21:47:24Z | sn57 burn fell 1.000 -> 0.000 - miners can earn again |
| `sn122:burn_drop:0.115` | 122 | BURN_DROP | 2026-11-21T21:47:24Z | sn122 burn fell 1.000 -> 0.115 - miners can earn again |
| `sn14:scoring_commit:2026-11-15T22:59:01Z` | 14 | SCORING_COMMIT | 2026-11-15T23:57:01Z | sn14 commit touches scoring: Merge pull request #161 from latent-to/claude/remeasured-reward-bar |
| `sn25:release:v2026.11.15-1099862510` | 25 | RELEASE | 2026-11-15T23:57:01Z | sn25 released v2026.11.15-1099862510 |
| `sn42:release:v0.6.16` | 42 | RELEASE | 2026-11-15T23:57:01Z | sn42 released v0.6.16 |
| `sn42:scoring_commit:2026-11-15T19:40:06Z` | 42 | SCORING_COMMIT | 2026-11-15T23:57:01Z | sn42 commit touches scoring: docs: the baseline was the setup of CADmind's test miners on testnet |
| `sn90:scoring_commit:2026-11-15T20:34:02Z` | 90 | SCORING_COMMIT | 2026-11-15T23:57:01Z | sn90 commit touches scoring: docs(subnet): enter Phase 1 with external miners |
| `sn116:scoring_commit:2026-11-15T20:34:55Z` | 116 | SCORING_COMMIT | 2026-11-15T23:57:01Z | sn116 commit touches scoring: Build jit: keep the shared level4 registry Challenge-free; Motor 1.8 … |
| `sn24:release:v0.2.1` | 24 | RELEASE | 2026-11-16T06:16:15Z | sn24 released v0.2.1 |
| `sn25:release:v2026.11.15-1100072900` | 25 | RELEASE | 2026-11-16T06:16:15Z | sn25 released v2026.11.15-1100072900 |
| `sn25:scoring_commit:2026-11-16T02:37:34Z` | 25 | SCORING_COMMIT | 2026-11-16T06:16:15Z | sn25 commit touches scoring: Merge release/validator-1115-transient-waits: the validator build 490… |
| `sn51:scoring_commit:2026-11-16T05:08:38Z` | 51 | SCORING_COMMIT | 2026-11-16T06:16:15Z | sn51 commit touches scoring: DAH-6295 - [P0] Validator: a node on another GPU model is reset once,… |
| `sn66:release:v2026.11.16.3` | 66 | RELEASE | 2026-11-16T06:16:15Z | sn66 released v2026.11.16.3 |
| `sn66:scoring_commit:2026-11-16T03:53:45Z` | 66 | SCORING_COMMIT | 2026-11-16T06:16:15Z | sn66 commit touches scoring: Admit reward statements for Hilbert 12 and Hilbert 6 |
| `sn91:scoring_commit:2026-11-16T03:23:08Z` | 91 | SCORING_COMMIT | 2026-11-16T06:16:15Z | sn91 commit touches scoring: deploy gate: refuse unsafe trainer/validator deploys, verify after (r… |
| `sn116:scoring_commit:2026-11-15T23:19:53Z` | 116 | SCORING_COMMIT | 2026-11-16T06:16:15Z | sn116 commit touches scoring: Evaluation key test: the committed row read backwards, not a reversed… |
| `sn127:release:Release 26830a1` | 127 | RELEASE | 2026-11-16T06:16:15Z | sn127 released Release 26830a1 |
| `sn3:scoring_commit:2026-11-16T11:37:13Z` | 3 | SCORING_COMMIT | 2026-11-16T16:14:51Z | sn3 commit touches scoring: Stream Horizon scoring during packed-text sampling |
| `sn25:release:v2026.11.16-1100273030` | 25 | RELEASE | 2026-11-16T16:14:51Z | sn25 released v2026.11.16-1100273030 |
| `sn25:scoring_commit:2026-11-16T06:53:36Z` | 25 | SCORING_COMMIT | 2026-11-16T16:14:51Z | sn25 commit touches scoring: Merge fix/validator-nonce-wait-1116: the validator waits out the weig… |
| `sn42:release:v0.6.18` | 42 | RELEASE | 2026-11-16T16:14:51Z | sn42 released v0.6.18 |
| `sn42:scoring_commit:2026-11-16T08:59:35Z` | 42 | SCORING_COMMIT | 2026-11-16T16:14:51Z | sn42 commit touches scoring: reference miner: a brief that asks for nothing physical is rejected n… |
| `sn51:release:executor-v1.184` | 51 | RELEASE | 2026-11-16T16:14:51Z | sn51 released executor-v1.184 |
| `sn51:scoring_commit:2026-11-16T15:55:07Z` | 51 | SCORING_COMMIT | 2026-11-16T16:14:51Z | sn51 commit touches scoring: Validator: quote executor-reported paths in shell commands (#2280) |
| `sn67:scoring_commit:2026-11-16T10:09:40Z` | 67 | SCORING_COMMIT | 2026-11-16T16:14:51Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20261116.post8 |
| `sn71:scoring_commit:2026-11-16T11:03:00Z` | 71 | SCORING_COMMIT | 2026-11-16T16:14:51Z | sn71 commit touches scoring: Assert exact judgment binding in score projection tests |
| `sn111:scoring_commit:2026-11-16T12:01:40Z` | 111 | SCORING_COMMIT | 2026-11-16T16:14:51Z | sn111 commit touches scoring: Verify carried-forward scoring revisions during production handoff |
| `sn15:release:v3.0.9: fix(sandbox): isolate each task ` | 15 | RELEASE | 2026-11-17T00:22:13Z | sn15 released v3.0.9: fix(sandbox): isolate each task in a run from the run's other tasks |
| `sn15:scoring_commit:2026-11-16T21:42:42Z` | 15 | SCORING_COMMIT | 2026-11-17T00:22:13Z | sn15 commit touches scoring: fix(sandbox): isolate each task in a run from the run's other tasks |
| `sn25:release:v2026.11.16-1100716180` | 25 | RELEASE | 2026-11-17T00:22:13Z | sn25 released v2026.11.16-1100716180 |
| `sn25:scoring_commit:2026-11-16T19:08:58Z` | 25 | SCORING_COMMIT | 2026-11-17T00:22:13Z | sn25 commit touches scoring: Merge fix/validator-upload-encoding-1116: validator uploads go as zst… |
| `sn41:scoring_commit:2026-11-11T19:25:42Z` | 41 | SCORING_COMMIT | 2026-11-17T00:22:13Z | sn41 commit touches scoring: Document the one-agent-per-hotkey upload rule in the miner guide |
| `sn42:release:v0.6.19` | 42 | RELEASE | 2026-11-17T00:22:13Z | sn42 released v0.6.19 |
| `sn42:scoring_commit:2026-11-16T19:56:03Z` | 42 | SCORING_COMMIT | 2026-11-17T00:22:13Z | sn42 commit touches scoring: desk: a sweep of a miner's grants is job-scoped -- one job's grants f… |
| `sn62:scoring_commit:2026-11-16T20:35:34Z` | 62 | SCORING_COMMIT | 2026-11-17T00:22:13Z | sn62 commit touches scoring: add more validation |
| `sn66:release:v2026.11.16.4` | 66 | RELEASE | 2026-11-17T00:22:13Z | sn66 released v2026.11.16.4 |
| `sn70:release:build-v3rc1-2026.11.17: v3: pin the embe` | 70 | RELEASE | 2026-11-17T00:22:13Z | sn70 released build-v3rc1-2026.11.17: v3: pin the embeddings file (EMBEDDINGS_SHA256 + EMBEDDINGS_URL) |
| `sn94:scoring_commit:2026-11-16T17:02:42Z` | 94 | SCORING_COMMIT | 2026-11-17T00:22:13Z | sn94 commit touches scoring: Add miner hotel offer signer to room-kit (AB#347) (#565) |
| `sn127:release:Release 9bd0c63` | 127 | RELEASE | 2026-11-17T00:22:13Z | sn127 released Release 9bd0c63 |
| `sn127:scoring_commit:2026-11-16T00:13:27Z` | 127 | SCORING_COMMIT | 2026-11-17T00:22:13Z | sn127 commit touches scoring: Weekly judge: left-out bodies, scores from cached answers, the week's… |
| `sn25:release:v2026.11.16-1101008320` | 25 | RELEASE | 2026-11-17T08:16:39Z | sn25 released v2026.11.16-1101008320 |
| `sn42:release:v0.6.20` | 42 | RELEASE | 2026-11-17T08:16:39Z | sn42 released v0.6.20 |
| `sn51:scoring_commit:2026-11-17T07:09:42Z` | 51 | SCORING_COMMIT | 2026-11-17T08:16:39Z | sn51 commit touches scoring: DAH-6257 - [P2] Validator: avoid a host identity false positive after… |
| `sn67:scoring_commit:2026-11-16T10:46:55Z` | 67 | SCORING_COMMIT | 2026-11-17T08:16:39Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20261116.post9 |
| `sn70:release:SUPERSEDED: use image-v2026.11.17b` | 70 | RELEASE | 2026-11-17T08:16:39Z | sn70 released SUPERSEDED: use image-v2026.11.17b |
| `sn70:scoring_commit:2026-11-17T06:20:06Z` | 70 | SCORING_COMMIT | 2026-11-17T08:16:39Z | sn70 commit touches scoring: validator: the collateral startup probe only warns, and names itself |
| `sn71:scoring_commit:2026-11-17T06:40:15Z` | 71 | SCORING_COMMIT | 2026-11-17T08:16:39Z | sn71 commit touches scoring: Keep unvalidated paragraph replies out of shared judge cache |
| `sn76:release:Ormas subnet SDK 0.0.4` | 76 | RELEASE | 2026-11-17T08:16:39Z | sn76 released Ormas subnet SDK 0.0.4 |
| `sn91:scoring_commit:2026-11-17T01:24:31Z` | 91 | SCORING_COMMIT | 2026-11-17T08:16:39Z | sn91 commit touches scoring: validator: keep bench-sweep evidence; weight keep-alive during long s… |
| `sn111:scoring_commit:2026-11-17T01:46:11Z` | 111 | SCORING_COMMIT | 2026-11-17T08:16:39Z | sn111 commit touches scoring: Compress controller evaluation transport outside frozen policy |
| `sn3:scoring_commit:2026-11-17T15:26:48Z` | 3 | SCORING_COMMIT | 2026-11-17T17:44:54Z | sn3 commit touches scoring: Add 8×H200 evaluator support with TP2 MiMo replicas |
| `sn7:release:release-20261117-160316` | 7 | RELEASE | 2026-11-17T17:44:54Z | sn7 released release-20261117-160316 |
| `sn7:scoring_commit:2026-11-17T16:01:21Z` | 7 | SCORING_COMMIT | 2026-11-17T17:44:54Z | sn7 commit touches scoring: Drop VALIDATOR_MODE: the validator always sets weights unless told no… |
| `sn12:release:validator-staging-2026-11-17-44119698793` | 12 | RELEASE | 2026-11-17T17:44:54Z | sn12 released validator-staging-2026-11-17-44119698793-630-1: fix: failure to connect to miner creates a MinerIncident (#866) |
| `sn12:scoring_commit:2026-11-17T15:52:57Z` | 12 | SCORING_COMMIT | 2026-11-17T17:44:54Z | sn12 commit touches scoring: fix: failure to connect to miner creates a MinerIncident (#866) |
| `sn25:release:v2026.11.17-1101053110` | 25 | RELEASE | 2026-11-17T17:44:54Z | sn25 released v2026.11.17-1101053110 |
| `sn25:scoring_commit:2026-11-17T17:27:07Z` | 25 | SCORING_COMMIT | 2026-11-17T17:44:54Z | sn25 commit touches scoring: Merge feat/one-extender-stack-per-miner-1117: a provider run builds o… |
| `sn42:release:v0.6.21` | 42 | RELEASE | 2026-11-17T17:44:54Z | sn42 released v0.6.21 |
| `sn42:scoring_commit:2026-11-17T08:46:33Z` | 42 | SCORING_COMMIT | 2026-11-17T17:44:54Z | sn42 commit touches scoring: reference miner: find a fitted product's real geometry before building |
| `sn51:release:lium-protocol-v2.16.0` | 51 | RELEASE | 2026-11-17T17:44:54Z | sn51 released lium-protocol-v2.16.0 |
| `sn51:scoring_commit:2026-11-17T16:58:36Z` | 51 | SCORING_COMMIT | 2026-11-17T17:44:54Z | sn51 commit touches scoring: DAH-6579 - [P1] Validator refuses a reserved volume path instead of m… |
| `sn67:scoring_commit:2026-11-17T11:17:29Z` | 67 | SCORING_COMMIT | 2026-11-17T17:44:54Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20261117.post4 |
| `sn94:scoring_commit:2026-11-17T17:33:54Z` | 94 | SCORING_COMMIT | 2026-11-17T17:44:54Z | sn94 commit touches scoring: Add cathedral_sealed_hotels_v1 schema, pins, golden vector, verifiers… |
| `sn114:scoring_commit:2026-11-17T12:20:39Z` | 114 | SCORING_COMMIT | 2026-11-17T17:44:54Z | sn114 commit touches scoring: Reduce validator prefetch load, reuse a pooled HTTP client for compac… |
| `sn116:scoring_commit:2026-11-17T14:19:33Z` | 116 | SCORING_COMMIT | 2026-11-17T17:44:54Z | sn116 commit touches scoring: f02 deck 3.2: SCALAR_KEYS_V32 and public_scalars_v32 (4 approved scor… |
| `sn12:release:validator-staging-2026-11-17-44146334658` | 12 | RELEASE | 2026-11-18T00:00:43Z | sn12 released validator-staging-2026-11-17-44146334658-631-1: fix: support immutable library release, bump version (#870) |
| `sn22:scoring_commit:2026-11-17T20:44:24Z` | 22 | SCORING_COMMIT | 2026-11-18T00:00:43Z | sn22 commit touches scoring: Merge pull request #410 from Desearch-ai/fix/task-api-request-limits |
| `sn25:scoring_commit:2026-11-17T22:14:19Z` | 25 | SCORING_COMMIT | 2026-11-18T00:00:43Z | sn25 commit touches scoring: Merge feat/verify-cohort-v2-validator-1117: verify cohort v2, validat… |
| `sn51:scoring_commit:2026-11-17T20:16:15Z` | 51 | SCORING_COMMIT | 2026-11-18T00:00:43Z | sn51 commit touches scoring: DAH-6466 - Validator: retry the s3fs volume plugin install when the D… |
| `sn70:scoring_commit:2026-11-17T20:03:28Z` | 70 | SCORING_COMMIT | 2026-11-18T00:00:43Z | sn70 commit touches scoring: validator: approve only images that can prove the protocol in force |
| `sn116:scoring_commit:2026-11-17T21:58:00Z` | 116 | SCORING_COMMIT | 2026-11-18T00:00:43Z | sn116 commit touches scoring: Crowns: the official-score rule is the default for every version; a v… |
| `sn124:scoring_commit:2026-11-17T13:07:25Z` | 124 | SCORING_COMMIT | 2026-11-18T00:00:43Z | sn124 commit touches scoring: Add Swarm Test Field and close two evaluation sandbox gaps |
| `sn51:scoring_commit:2026-11-18T06:59:20Z` | 51 | SCORING_COMMIT | 2026-11-18T07:14:54Z | sn51 commit touches scoring: DAH-6566 - [P0] Validator writes the needrestart guard on hosts set u… |
| `sn67:scoring_commit:2026-11-18T03:06:43Z` | 67 | SCORING_COMMIT | 2026-11-18T07:14:54Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20261118.post1 |
| `sn81:scoring_commit:2026-11-17T11:05:03Z` | 81 | SCORING_COMMIT | 2026-11-18T07:14:54Z | sn81 commit touches scoring: fix(rl): a pod's link reaches its task's trainer routes and writes on… |
| `sn127:release:Release b5a248c` | 127 | RELEASE | 2026-11-18T07:14:54Z | sn127 released Release b5a248c |
| `sn12:release:validator-staging-2026-11-18-44297690409` | 12 | RELEASE | 2026-11-18T16:39:22Z | sn12 released validator-staging-2026-11-18-44297690409-632-1: feat: miner manifest every 5000 blocks, validator ignores >25000 (#873) |
| `sn12:scoring_commit:2026-11-18T12:17:58Z` | 12 | SCORING_COMMIT | 2026-11-18T16:39:22Z | sn12 commit touches scoring: feat: log validator ignored commitments (#874) |
| `sn25:release:v2026.11.18-1101975730` | 25 | RELEASE | 2026-11-18T16:39:22Z | sn25 released v2026.11.18-1101975730 |
| `sn42:release:v0.6.22` | 42 | RELEASE | 2026-11-18T16:39:22Z | sn42 released v0.6.22 |
| `sn42:scoring_commit:2026-11-18T09:39:30Z` | 42 | SCORING_COMMIT | 2026-11-18T16:39:22Z | sn42 commit touches scoring: v0.6.22: the reference miner checks watt status at DONE |
| `sn51:release:executor-v1.190` | 51 | RELEASE | 2026-11-18T16:39:22Z | sn51 released executor-v1.190 |
| `sn51:scoring_commit:2026-11-18T16:26:22Z` | 51 | SCORING_COMMIT | 2026-11-18T16:39:22Z | sn51 commit touches scoring: DAH-6546 - [P2] Validator: an unread pod after a GPU-set move is no v… |
| `sn67:scoring_commit:2026-11-18T13:20:08Z` | 67 | SCORING_COMMIT | 2026-11-18T16:39:22Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20261118.post6 |
| `sn90:release:v1.4.3` | 90 | RELEASE | 2026-11-18T16:39:22Z | sn90 released v1.4.3 |
| `sn90:scoring_commit:2026-11-18T14:27:49Z` | 90 | SCORING_COMMIT | 2026-11-18T16:39:22Z | sn90 commit touches scoring: fix(subnet): score only worker nodes |
| `sn111:scoring_commit:2026-11-18T10:21:20Z` | 111 | SCORING_COMMIT | 2026-11-18T16:39:22Z | sn111 commit touches scoring: Score audited Bronze source faults without an artifact |
| `sn62:release:v0.3.18` | 62 | RELEASE | 2026-11-18T23:10:24Z | sn62 released v0.3.18 |
| `sn71:scoring_commit:2026-11-18T21:05:38Z` | 71 | SCORING_COMMIT | 2026-11-18T23:10:24Z | sn71 commit touches scoring: Allow audited published judgment recovery with unchanged scorer |
| `sn93:scoring_commit:2026-11-18T19:10:32Z` | 93 | SCORING_COMMIT | 2026-11-18T23:10:24Z | sn93 commit touches scoring: feat(validator): score briefs with allowed_channels only for those ch… |
| `sn116:scoring_commit:2026-11-18T21:30:40Z` | 116 | SCORING_COMMIT | 2026-11-18T23:10:24Z | sn116 commit touches scoring: Auto retry: a spent cap (3 per failure code, 5 per task) writes an au… |
| `sn124:scoring_commit:2026-11-18T17:46:16Z` | 124 | SCORING_COMMIT | 2026-11-18T23:10:24Z | sn124 commit touches scoring: Merge pull request #246 from swarm-subnet/feature/ali/validator-memor… |
| `sn56:scoring_commit:2026-11-19T02:57:22Z` | 56 | SCORING_COMMIT | 2026-11-19T04:21:26Z | sn56 commit touches scoring: Incoming changes for miners (#1434) |
| `sn89:scoring_commit:2026-11-18T23:39:14Z` | 89 | SCORING_COMMIT | 2026-11-19T04:21:26Z | sn89 commit touches scoring: Validator: ignore blobs first stored more than 120 seconds after the … |
| `sn94:scoring_commit:2026-11-19T00:17:55Z` | 94 | SCORING_COMMIT | 2026-11-19T04:21:26Z | sn94 commit touches scoring: Merge pull request #434 from cathedralai/feature/go-receipt-verifier |
| `sn116:scoring_commit:2026-11-19T01:01:34Z` | 116 | SCORING_COMMIT | 2026-11-19T04:21:26Z | sn116 commit touches scoring: Miner client: 503 capacity retried like intake_busy (V2 add), with a … |
| `sn12:release:validator-staging-2026-11-19-44521972284` | 12 | RELEASE | 2026-11-19T13:41:44Z | sn12 released validator-staging-2026-11-19-44521972284-633-1: fix: bump nginx (#875) |
| `sn12:scoring_commit:2026-11-19T13:35:45Z` | 12 | SCORING_COMMIT | 2026-11-19T13:41:44Z | sn12 commit touches scoring: fix: build compute-horde-validator-nginx in CD (#876) |
| `sn21:release:SN21 training data v7 (windows 2026-09-2` | 21 | RELEASE | 2026-11-19T13:41:44Z | sn21 released SN21 training data v7 (windows 2026-09-21 to 2026-10-04) |
| `sn24:release:v0.3.0` | 24 | RELEASE | 2026-11-19T13:41:44Z | sn24 released v0.3.0 |
| `sn42:release:v0.6.24` | 42 | RELEASE | 2026-11-19T13:41:44Z | sn42 released v0.6.24 |
| `sn42:scoring_commit:2026-11-19T13:28:49Z` | 42 | SCORING_COMMIT | 2026-11-19T13:41:44Z | sn42 commit touches scoring: v0.6.24: the validator's vote scores reach the platform |
| `sn45:scoring_commit:2026-11-15T03:16:42Z` | 45 | SCORING_COMMIT | 2026-11-19T13:41:44Z | sn45 commit touches scoring: Quality: each paid claim's pay is fixed by the coldkey's score when i… |
| `sn51:scoring_commit:2026-11-19T11:18:32Z` | 51 | SCORING_COMMIT | 2026-11-19T13:41:44Z | sn51 commit touches scoring: DAH-6714 - [P1] Validator: filler GPU process attribution counts in t… |
| `sn71:scoring_commit:2026-11-19T11:35:44Z` | 71 | SCORING_COMMIT | 2026-11-19T13:41:44Z | sn71 commit touches scoring: Fix review outage recovery lock order and verify full lifecycle |
| `sn116:scoring_commit:2026-11-19T11:43:48Z` | 116 | SCORING_COMMIT | 2026-11-19T13:41:44Z | sn116 commit touches scoring: Queue places: unmarked is not waiting; an owner whose unmarked tasks … |
| `sn3:scoring_commit:2026-11-19T16:08:05Z` | 3 | SCORING_COMMIT | 2026-11-19T21:51:45Z | sn3 commit touches scoring: Retry incomplete R2 reads and prefetch evaluation text |
| `sn12:release:validator-testing-2026-11-19-44554669102` | 12 | RELEASE | 2026-11-19T21:51:45Z | sn12 released validator-testing-2026-11-19-44554669102-9-1: fix: build compute-horde-validator-nginx in CD, 2nd take (#877) |
| `sn12:scoring_commit:2026-11-19T14:07:29Z` | 12 | SCORING_COMMIT | 2026-11-19T21:51:45Z | sn12 commit touches scoring: fix: build compute-horde-validator-nginx in CD, 2nd take (#877) |
| `sn25:release:v2026.11.19-1103236710` | 25 | RELEASE | 2026-11-19T21:51:45Z | sn25 released v2026.11.19-1103236710 |
| `sn28:release:v0.5.25` | 28 | RELEASE | 2026-11-19T21:51:45Z | sn28 released v0.5.25 |
| `sn33:scoring_commit:2026-11-19T13:44:08Z` | 33 | SCORING_COMMIT | 2026-11-19T21:51:45Z | sn33 commit touches scoring: Send a single conversation window to all miners of a bundle |
| `sn42:release:v0.6.25` | 42 | RELEASE | 2026-11-19T21:51:45Z | sn42 released v0.6.25 |
| `sn42:scoring_commit:2026-11-19T14:50:07Z` | 42 | SCORING_COMMIT | 2026-11-19T21:51:45Z | sn42 commit touches scoring: reference miner: one answer register for the whole device |
| `sn51:release:executor-v1.191` | 51 | RELEASE | 2026-11-19T21:51:45Z | sn51 released executor-v1.191 |
| `sn51:scoring_commit:2026-11-19T20:39:29Z` | 51 | SCORING_COMMIT | 2026-11-19T21:51:45Z | sn51 commit touches scoring: DAH-4689 validator: ignore live volume and GPU process paths in the s… |
| `sn66:release:v2026.11.19.2` | 66 | RELEASE | 2026-11-19T21:51:45Z | sn66 released v2026.11.19.2 |
| `sn81:scoring_commit:2026-11-19T14:00:51Z` | 81 | SCORING_COMMIT | 2026-11-19T21:51:45Z | sn81 commit touches scoring: fix(cli): let RELIQUARY_HF_REPO_ID set validate's --hf-repo-id (#563) |
| `sn94:scoring_commit:2026-11-19T14:03:29Z` | 94 | SCORING_COMMIT | 2026-11-19T21:51:45Z | sn94 commit touches scoring: Host DNAT 443 to the sealed guest and a DNS-01 challenge service (AB#… |
| `sn116:scoring_commit:2026-11-19T21:18:05Z` | 116 | SCORING_COMMIT | 2026-11-19T21:51:45Z | sn116 commit touches scoring: Updates page: current crown rule, rough-solver zero, Motor 1.9, score… |
| `sn117:release:everycli v1.2.4` | 117 | RELEASE | 2026-11-19T21:51:45Z | sn117 released everycli v1.2.4 |
| `sn127:release:Release e8350f5` | 127 | RELEASE | 2026-11-19T21:51:45Z | sn127 released Release e8350f5 |
| `sn53:scoring_commit:2026-11-19T23:32:44Z` | 53 | SCORING_COMMIT | 2026-11-20T03:04:29Z | sn53 commit touches scoring: Merge pull request #65 from hanlinai/feat/tee-miner-name-only |
| `sn99:scoring_commit:2026-11-19T21:55:03Z` | 99 | SCORING_COMMIT | 2026-11-20T03:04:29Z | sn99 commit touches scoring: A candidate is evaluated on the machine admission built its model on … |
| `sn116:scoring_commit:2026-11-20T02:18:19Z` | 116 | SCORING_COMMIT | 2026-11-20T03:04:29Z | sn116 commit touches scoring: Box loss: a live DOWN mark stays DOWN on a later loss (Validator-2 B1… |
| `sn25:release:v2026.11.19-1103608200` | 25 | RELEASE | 2026-11-20T11:26:47Z | sn25 released v2026.11.19-1103608200 |
| `sn51:release:executor-v1.192` | 51 | RELEASE | 2026-11-20T11:26:47Z | sn51 released executor-v1.192 |
| `sn51:scoring_commit:2026-11-20T09:17:54Z` | 51 | SCORING_COMMIT | 2026-11-20T11:26:47Z | sn51 commit touches scoring: DAH-6666 - [P1] Executor trusts the validator named in a subnet-owner… |
| `sn67:scoring_commit:2026-11-20T08:01:49Z` | 67 | SCORING_COMMIT | 2026-11-20T11:26:47Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20261120.post1 |
| `sn71:scoring_commit:2026-11-20T07:47:14Z` | 71 | SCORING_COMMIT | 2026-11-20T11:26:47Z | sn71 commit touches scoring: Record reviewed scorer changes in protected workflow manifest |
| `sn99:scoring_commit:2026-11-20T09:18:09Z` | 99 | SCORING_COMMIT | 2026-11-20T11:26:47Z | sn99 commit touches scoring: Validator loop: tempo read once, one try per round, sleep to the next… |
| `sn116:scoring_commit:2026-11-20T08:40:42Z` | 116 | SCORING_COMMIT | 2026-11-20T11:26:47Z | sn116 commit touches scoring: L2 FULL RED (release g9334la/lb): the 6 tests that expected a miner's… |
| `sn25:scoring_commit:2026-11-19T18:57:29Z` | 25 | SCORING_COMMIT | 2026-11-20T19:14:02Z | sn25 commit touches scoring: Merge fix/runtime-492-1119 (3e9e6f2b) onto 8c14d437, the validator sn… |
| `sn51:scoring_commit:2026-11-20T13:09:25Z` | 51 | SCORING_COMMIT | 2026-11-20T19:14:02Z | sn51 commit touches scoring: DAH-6769 - [P4] Validator: a readable upper dir decides the reboot's … |
| `sn58:scoring_commit:2026-11-20T13:17:06Z` | 58 | SCORING_COMMIT | 2026-11-20T19:14:02Z | sn58 commit touches scoring: feat(horizon): Horizon miners share Horizon's 70% |
| `sn66:release:v2026.11.20` | 66 | RELEASE | 2026-11-20T19:14:02Z | sn66 released v2026.11.20 |
| `sn71:scoring_commit:2026-11-20T13:29:24Z` | 71 | SCORING_COMMIT | 2026-11-20T19:14:02Z | sn71 commit touches scoring: Update unknown-runtime control after verified 492 support |
| `sn99:scoring_commit:2026-11-20T15:07:44Z` | 99 | SCORING_COMMIT | 2026-11-20T19:14:02Z | sn99 commit touches scoring: task.json drops parent (starts lists it); the real-toolkit check test… |
| `sn116:scoring_commit:2026-11-20T18:11:02Z` | 116 | SCORING_COMMIT | 2026-11-20T19:14:02Z | sn116 commit touches scoring: Client refusal text: miner-x's wording (plain words, withdraw named, … |
| `sn51:scoring_commit:2026-11-20T23:09:15Z` | 51 | SCORING_COMMIT | 2026-11-21T00:54:44Z | sn51 commit touches scoring: DAH-6863 - [P3] Validator runs each pod with the backend's CPU count;… |
| `sn66:release:v2026.11.20.2` | 66 | RELEASE | 2026-11-21T00:54:44Z | sn66 released v2026.11.20.2 |
| `sn66:scoring_commit:2026-11-20T21:36:43Z` | 66 | SCORING_COMMIT | 2026-11-21T00:54:44Z | sn66 commit touches scoring: Publish verification holds for RH, Erdős 462, and Erdős 985 |
| `sn71:scoring_commit:2026-11-20T19:11:30Z` | 71 | SCORING_COMMIT | 2026-11-21T00:54:44Z | sn71 commit touches scoring: Preserve bounded validator readiness delivery during diagnostic floods |
| `sn116:scoring_commit:2026-11-21T00:35:50Z` | 116 | SCORING_COMMIT | 2026-11-21T00:54:44Z | sn116 commit touches scoring: miner_lookup fix: ruff --fix + black (release LINT_DIFF_1cb183d7.patc… |
| `sn90:release:v1.4.5 — Finney oracle and validator rel` | 90 | RELEASE | 2026-11-21T08:14:47Z | sn90 released v1.4.5 — Finney oracle and validator reliability |
| `sn90:scoring_commit:2026-11-21T02:48:26Z` | 90 | SCORING_COMMIT | 2026-11-21T08:14:47Z | sn90 commit touches scoring: feat(validator): prefer Finney oracle for TAO pricing |
| `sn71:scoring_commit:2026-11-21T07:48:58Z` | 71 | SCORING_COMMIT | 2026-11-21T16:18:29Z | sn71 commit touches scoring: Validate canonical Bittensor accounts on lead-order inputs |
| `sn82:scoring_commit:2026-11-21T00:27:34Z` | 82 | SCORING_COMMIT | 2026-11-21T16:18:29Z | sn82 commit touches scoring: Harden report checkpoints and independent verification |
| `sn91:scoring_commit:2026-11-21T13:35:05Z` | 91 | SCORING_COMMIT | 2026-11-21T16:18:29Z | sn91 commit touches scoring: validator: post-gate kings keep their crowning block as the tenure an… |
| `sn92:scoring_commit:2026-11-20T18:43:47Z` | 92 | SCORING_COMMIT | 2026-11-21T16:18:29Z | sn92 commit touches scoring: Verify teacher metadata is independent of weight eligibility |
| `sn99:scoring_commit:2026-11-21T15:04:52Z` | 99 | SCORING_COMMIT | 2026-11-21T16:18:29Z | sn99 commit touches scoring: Validator: a set whose reply was lost counts when the chain shows it … |
| `sn117:release:everycli v1.2.5` | 117 | RELEASE | 2026-11-21T16:18:29Z | sn117 released everycli v1.2.5 |
| `sn92:scoring_commit:2026-11-21T15:13:22Z` | 92 | SCORING_COMMIT | 2026-11-21T21:47:24Z | sn92 commit touches scoring: Add verified public development roster to the REAX yardstick |
| `sn111:scoring_commit:2026-11-21T20:43:24Z` | 111 | SCORING_COMMIT | 2026-11-21T21:47:24Z | sn111 commit touches scoring: Complete scientific result worker delivery and source-task scoring |
| `sn116:scoring_commit:2026-11-21T17:00:53Z` | 116 | SCORING_COMMIT | 2026-11-21T21:47:24Z | sn116 commit touches scoring: DATA: the door holds verified inference snapshots' predictions.json c… |
| `sn117:release:everycli v1.2.6` | 117 | RELEASE | 2026-11-21T21:47:24Z | sn117 released everycli v1.2.6 |
| `sn91:scoring_commit:2026-11-22T01:37:02Z` | 91 | SCORING_COMMIT | 2026-11-22T01:42:02Z | sn91 commit touches scoring: tests(laned): W5d scorer acceptance tests (tests only) (#539) |
| `sn25:release:v2026.11.22-1105365180` | 25 | RELEASE | 2026-11-22T08:53:59Z | sn25 released v2026.11.22-1105365180 |
| `sn53:scoring_commit:2026-11-22T02:53:53Z` | 53 | SCORING_COMMIT | 2026-11-22T08:53:59Z | sn53 commit touches scoring: docs(im): one-pager matches today — no per-response proof verified (T… |
| `sn91:scoring_commit:2026-11-22T07:03:10Z` | 91 | SCORING_COMMIT | 2026-11-22T08:53:59Z | sn91 commit touches scoring: fix(laned): W3b2 pod evidence live verify (suite pin, published refs,… |
| `sn111:scoring_commit:2026-11-22T02:03:22Z` | 111 | SCORING_COMMIT | 2026-11-22T08:53:59Z | sn111 commit touches scoring: Document signed scientific evaluation and evidence downloads |
| `sn116:scoring_commit:2026-11-22T02:55:17Z` | 116 | SCORING_COMMIT | 2026-11-22T08:53:59Z | sn116 commit touches scoring: Bank provenance record (reward lane, owner G-LEAD-36) |
| `sn90:release:v1.4.6` | 90 | RELEASE | 2026-11-22T17:04:41Z | sn90 released v1.4.6 |
| `sn90:scoring_commit:2026-11-22T10:50:47Z` | 90 | SCORING_COMMIT | 2026-11-22T17:04:41Z | sn90 commit touches scoring: docs(validator): describe Lium B300 AC-only pricing |
| `sn91:scoring_commit:2026-11-22T10:55:14Z` | 91 | SCORING_COMMIT | 2026-11-22T17:04:41Z | sn91 commit touches scoring: fix(laned): W5b scores each window from one snapshot; report names ev… |
| `sn94:scoring_commit:2026-11-22T09:55:43Z` | 94 | SCORING_COMMIT | 2026-11-22T17:04:41Z | sn94 commit touches scoring: Revalidate the fresh plant incarnation under the write and sign lock … |
| `sn99:scoring_commit:2026-11-21T15:54:01Z` | 99 | SCORING_COMMIT | 2026-11-22T17:04:41Z | sn99 commit touches scoring: BBH items as the toolkit's build: its 19 generated tasks, 26 each, pi… |
| `sn90:readme_task_diff:a7b301753d76644f` | 90 | README_TASK_DIFF | 2026-11-15T23:57:01Z | sn90 README task/scoring sections changed |
| `sn42:readme_task_diff:dd8a6fb083469151` | 42 | README_TASK_DIFF | 2026-11-16T16:14:51Z | sn42 README task/scoring sections changed |
| `sn76:readme_task_diff:da868f725697bf9f` | 76 | README_TASK_DIFF | 2026-11-17T08:16:39Z | sn76 README task/scoring sections changed |
| `sn124:readme_task_diff:3167f0c564855989` | 124 | README_TASK_DIFF | 2026-11-18T00:00:43Z | sn124 README task/scoring sections changed |
| `sn127:readme_task_diff:0827763d022b8f1f` | 127 | README_TASK_DIFF | 2026-11-18T07:14:54Z | sn127 README task/scoring sections changed |
| `sn99:readme_task_diff:346f6cf3141fc736` | 99 | README_TASK_DIFF | 2026-11-18T23:10:24Z | sn99 README task/scoring sections changed |
| `sn99:readme_task_diff:70f3abe3d8c03fd9` | 99 | README_TASK_DIFF | 2026-11-19T13:41:44Z | sn99 README task/scoring sections changed |
| `sn94:readme_task_diff:ef09606cbd6e8243` | 94 | README_TASK_DIFF | 2026-11-20T11:26:47Z | sn94 README task/scoring sections changed |
| `sn99:readme_task_diff:fd32093daf7672c0` | 99 | README_TASK_DIFF | 2026-11-20T11:26:47Z | sn99 README task/scoring sections changed |
| `sn56:readme_task_diff:eb830460d88616d2` | 56 | README_TASK_DIFF | 2026-11-20T19:14:02Z | sn56 README task/scoring sections changed |
| `sn123:readme_task_diff:f4ae2b06d69e2e0b` | 123 | README_TASK_DIFF | 2026-11-20T19:14:02Z | sn123 README task/scoring sections changed |
| `sn82:readme_task_diff:aa4f39b4e574a688` | 82 | README_TASK_DIFF | 2026-11-21T16:18:29Z | sn82 README task/scoring sections changed |
| `sn91:readme_task_diff:e77d0e82c1da3b20` | 91 | README_TASK_DIFF | 2026-11-21T16:18:29Z | sn91 README task/scoring sections changed |
| `sn99:readme_task_diff:99418d103a242136` | 99 | README_TASK_DIFF | 2026-11-22T17:04:41Z | sn99 README task/scoring sections changed |

## RESOLVED IN THIS WINDOW

_none_
