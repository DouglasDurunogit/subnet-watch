# ALARMS - generated 2026-11-09T11:21:47Z, block 9468297

window: first_seen in [2026-11-09T10:07:14Z, 2026-11-09T11:22:14Z)  (60 min interval + 15 min overlap)

Report ONLY the rows under NEW SINCE LAST RUN. Rows under STILL OPEN were
already reported in an earlier window and must not be re-alarmed.

## NEW SINCE LAST RUN

| event_id | netuid | class | severity | first_seen_utc | one_line |
|---|---|---|---|---|---|
| `sn15:release:v3.0.8: feat(validator): report each epi` | 15 | RELEASE | P1 | 2026-11-09T11:22:14Z | sn15 released v3.0.8: feat(validator): report each episode's end reason and duration (#406) |
| `sn51:release:watchtower-v1.2.1: DAH-5942 - docker_bui` | 51 | RELEASE | P1 | 2026-11-09T11:22:14Z | sn51 released watchtower-v1.2.1: DAH-5942 - docker_build.sh: optional multi-arch build to an OCI archive |
| `sn51:scoring_commit:2026-11-09T09:10:49Z` | 51 | SCORING_COMMIT | P1 | 2026-11-09T11:22:14Z | sn51 commit touches scoring: DAH-5917 - [P2] Miner releases: create the GitHub release when a mine… |
| `sn53:scoring_commit:2026-11-09T08:47:21Z` | 53 | SCORING_COMMIT | P1 | 2026-11-09T11:22:14Z | sn53 commit touches scoring: tee_miner: read KV load from sglang /v1/loads when /get_load is gone … |
| `sn66:release:v2026.11.09` | 66 | RELEASE | P1 | 2026-11-09T11:22:14Z | sn66 released v2026.11.09 |
| `sn67:scoring_commit:2026-11-09T07:00:28Z` | 67 | SCORING_COMMIT | P1 | 2026-11-09T11:22:14Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20261109.post1 |
| `sn71:scoring_commit:2026-11-09T09:13:31Z` | 71 | SCORING_COMMIT | P1 | 2026-11-09T11:22:14Z | sn71 commit touches scoring: Allow the fixed reward clock failure label in telemetry |
| `sn97:scoring_commit:2026-11-09T10:05:07Z` | 97 | SCORING_COMMIT | P1 | 2026-11-09T11:22:14Z | sn97 commit touches scoring: fix(miner): Fixed ty format |
| `sn108:scoring_commit:2026-11-09T08:54:14Z` | 108 | SCORING_COMMIT | P1 | 2026-11-09T11:22:14Z | sn108 commit touches scoring: Neuron 1.0.5: a validator updated mid-evaluation waits for the run it… |
| `sn127:scoring_commit:2026-11-09T04:08:30Z` | 127 | SCORING_COMMIT | P1 | 2026-11-09T11:22:14Z | sn127 commit touches scoring: Merge pull request #222 from ooo-hq/miner-delete-data |
| `sn15:readme_task_diff:cf22c88e3fbbce23` | 15 | README_TASK_DIFF | P2 | 2026-11-09T11:22:14Z | sn15 README task/scoring sections changed |

### detail

- **`sn15:release:v3.0.8: feat(validator): report each epi`** - sn15 released v3.0.8: feat(validator): report each episode's end reason and duration (#406)
  - published 2026-11-08T21:47:52Z (was v3.0.7)
- **`sn51:release:watchtower-v1.2.1: DAH-5942 - docker_bui`** - sn51 released watchtower-v1.2.1: DAH-5942 - docker_build.sh: optional multi-arch build to an OCI archive
  - published 2026-11-07T07:59:19Z (was executor-v1.172)
- **`sn51:scoring_commit:2026-11-09T09:10:49Z`** - sn51 commit touches scoring: DAH-5917 - [P2] Miner releases: create the GitHub release when a mine…
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn53:scoring_commit:2026-11-09T08:47:21Z`** - sn53 commit touches scoring: tee_miner: read KV load from sglang /v1/loads when /get_load is gone …
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn66:release:v2026.11.09`** - sn66 released v2026.11.09
  - published 2026-11-09T03:50:03Z (was v2026.11.07)
- **`sn67:scoring_commit:2026-11-09T07:00:28Z`** - sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20261109.post1
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn71:scoring_commit:2026-11-09T09:13:31Z`** - sn71 commit touches scoring: Allow the fixed reward clock failure label in telemetry
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn97:scoring_commit:2026-11-09T10:05:07Z`** - sn97 commit touches scoring: fix(miner): Fixed ty format
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn108:scoring_commit:2026-11-09T08:54:14Z`** - sn108 commit touches scoring: Neuron 1.0.5: a validator updated mid-evaluation waits for the run it…
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn127:scoring_commit:2026-11-09T04:08:30Z`** - sn127 commit touches scoring: Merge pull request #222 from ooo-hq/miner-delete-data
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn15:readme_task_diff:cf22c88e3fbbce23`** - sn15 README task/scoring sections changed
  - Only the task-describing headings are hashed, so badge and typo edits do not trigger this.

## STILL OPEN (already reported - do not re-alarm)

| event_id | netuid | class | first_seen_utc | one_line |
|---|---|---|---|---|
| `sn31:burn_drop:0.000` | 31 | BURN_DROP | 2026-11-02T19:40:04Z | sn31 burn fell 1.000 -> 0.000 - miners can earn again |
| `sn24:burn_drop:0.031` | 24 | BURN_DROP | 2026-11-03T09:27:38Z | sn24 burn fell 1.000 -> 0.031 - miners can earn again |
| `sn76:burn_drop:0.972` | 76 | BURN_DROP | 2026-11-03T09:27:38Z | sn76 burn fell 0.997 -> 0.972 - miners can earn again |
| `sn126:burn_drop:0.956` | 126 | BURN_DROP | 2026-11-03T22:27:15Z | sn126 burn fell 1.000 -> 0.956 - miners can earn again |
| `sn70:burn_drop:0.101` | 70 | BURN_DROP | 2026-11-04T09:56:37Z | sn70 burn fell 1.000 -> 0.101 - miners can earn again |
| `sn10:burn_drop:0.605` | 10 | BURN_DROP | 2026-11-04T17:58:02Z | sn10 burn fell 1.000 -> 0.605 - miners can earn again |
| `sn126:burn_drop:0.955` | 126 | BURN_DROP | 2026-11-05T03:46:12Z | sn126 burn fell 1.000 -> 0.955 - miners can earn again |
| `sn127:burn_drop:0.872` | 127 | BURN_DROP | 2026-11-05T11:38:32Z | sn127 burn fell 0.990 -> 0.872 - miners can earn again |
| `sn81:burn_drop:0.965` | 81 | BURN_DROP | 2026-11-05T19:03:37Z | sn81 burn fell 0.999 -> 0.965 - miners can earn again |
| `sn121:burn_drop:0.602` | 121 | BURN_DROP | 2026-11-05T19:03:37Z | sn121 burn fell 1.000 -> 0.602 - miners can earn again |
| `sn76:burn_drop:0.973` | 76 | BURN_DROP | 2026-11-06T00:09:29Z | sn76 burn fell 0.990 -> 0.973 - miners can earn again |
| `sn37:burn_drop:0.091` | 37 | BURN_DROP | 2026-11-07T07:02:35Z | sn37 burn fell 1.000 -> 0.091 - miners can earn again |
| `sn76:burn_drop:0.984` | 76 | BURN_DROP | 2026-11-08T01:42:10Z | sn76 burn fell 0.992 -> 0.984 - miners can earn again |
| `sn126:burn_drop:0.985` | 126 | BURN_DROP | 2026-11-08T01:42:10Z | sn126 burn fell 1.000 -> 0.985 - miners can earn again |
| `sn76:burn_drop:0.985` | 76 | BURN_DROP | 2026-11-08T19:38:31Z | sn76 burn fell 0.996 -> 0.985 - miners can earn again |
| `sn1:release:v4.6.1` | 1 | RELEASE | 2026-11-02T19:40:04Z | sn1 released v4.6.1 |
| `sn17:release:witness-diagnostics-20261102` | 17 | RELEASE | 2026-11-02T19:40:04Z | sn17 released witness-diagnostics-20261102 |
| `sn21:scoring_commit:2026-11-02T14:33:30Z` | 21 | SCORING_COMMIT | 2026-11-02T19:40:04Z | sn21 commit touches scoring: docs: Performance Max campaigns in MINER_MODEL_SPEC (draft; dates to … |
| `sn38:scoring_commit:2026-11-02T11:35:55Z` | 38 | SCORING_COMMIT | 2026-11-02T19:40:04Z | sn38 commit touches scoring: Update validator image in docker-compose.validator.yml to latest versi |
| `sn51:release:lium-protocol-v2.1.0` | 51 | RELEASE | 2026-11-02T19:40:04Z | sn51 released lium-protocol-v2.1.0 |
| `sn51:scoring_commit:2026-11-02T15:36:44Z` | 51 | SCORING_COMMIT | 2026-11-02T19:40:04Z | sn51 commit touches scoring: DAH-5327 - [P1] Validator re-sends the rm of a stuck filler so a cust… |
| `sn56:scoring_commit:2026-11-02T16:14:51Z` | 56 | SCORING_COMMIT | 2026-11-02T19:40:04Z | sn56 commit touches scoring: Fix the challenger dependency review module name so the validator can… |
| `sn66:release:v2026.11.02.3` | 66 | RELEASE | 2026-11-02T19:40:04Z | sn66 released v2026.11.02.3 |
| `sn67:scoring_commit:2026-11-02T12:42:16Z` | 67 | SCORING_COMMIT | 2026-11-02T19:40:04Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20261102.post3 |
| `sn71:scoring_commit:2026-11-02T11:14:11Z` | 71 | SCORING_COMMIT | 2026-11-02T19:40:04Z | sn71 commit touches scoring: Attribute provider telemetry to validated requested models |
| `sn81:scoring_commit:2026-11-02T10:33:52Z` | 81 | SCORING_COMMIT | 2026-11-02T19:40:04Z | sn81 commit touches scoring: feat: add retail video training inference and evaluation |
| `sn89:scoring_commit:2026-11-02T12:59:18Z` | 89 | SCORING_COMMIT | 2026-11-02T19:40:04Z | sn89 commit touches scoring: Agent scoreboard: per-algo breakdown with owner nicknames |
| `sn116:scoring_commit:2026-11-02T16:02:57Z` | 116 | SCORING_COMMIT | 2026-11-02T19:40:04Z | sn116 commit touches scoring: Miner text: a stage conflict after a receiver update may mean nothing… |
| `sn117:release:everycli v0.9.1` | 117 | RELEASE | 2026-11-02T19:40:04Z | sn117 released everycli v0.9.1 |
| `sn120:scoring_commit:2026-11-02T16:52:47Z` | 120 | SCORING_COMMIT | 2026-11-02T19:40:04Z | sn120 commit touches scoring: SN120 task cap 12K (Jacob pt1084u, 2026-11-02 10:25 CR: move the task… |
| `sn25:scoring_commit:2026-11-02T22:54:33Z` | 25 | SCORING_COMMIT | 2026-11-03T01:50:43Z | sn25 commit touches scoring: Document audited evaluator recovery metadata |
| `sn34:scoring_commit:2026-11-02T21:29:37Z` | 34 | SCORING_COMMIT | 2026-11-03T01:50:43Z | sn34 commit touches scoring: docs: use pack versions in miner scoring guidance |
| `sn91:scoring_commit:2026-11-03T00:59:04Z` | 91 | SCORING_COMMIT | 2026-11-03T01:50:43Z | sn91 commit touches scoring: feat(funding): miner-set total budget per submission (--max-total-spen |
| `sn116:scoring_commit:2026-11-02T23:20:00Z` | 116 | SCORING_COMMIT | 2026-11-03T01:50:43Z | sn116 commit touches scoring: Crown re-measure tests: the fake adapter names its Challenge (rebuild… |
| `sn117:release:everycli v0.9.2` | 117 | RELEASE | 2026-11-03T01:50:43Z | sn117 released everycli v0.9.2 |
| `sn120:scoring_commit:2026-11-02T20:40:25Z` | 120 | SCORING_COMMIT | 2026-11-03T01:50:43Z | sn120 commit touches scoring: miner/README: point the pass-rate references at affine.io/passrate.js… |
| `sn51:release:lium-protocol-v2.4.0` | 51 | RELEASE | 2026-11-03T09:27:38Z | sn51 released lium-protocol-v2.4.0 |
| `sn51:scoring_commit:2026-11-03T09:04:18Z` | 51 | SCORING_COMMIT | 2026-11-03T09:27:38Z | sn51 commit touches scoring: DAH-5372 - [P1] VerifyX: fail a node whose upload EMA is below 10 Mbp… |
| `sn71:scoring_commit:2026-11-03T06:56:37Z` | 71 | SCORING_COMMIT | 2026-11-03T09:27:38Z | sn71 commit touches scoring: Hold November 3 scoring until improved verifier is live (#980) |
| `sn81:scoring_commit:2026-11-03T09:09:32Z` | 81 | SCORING_COMMIT | 2026-11-03T09:27:38Z | sn81 commit touches scoring: Merge pull request #445 from reliquadotai/fix/evaluation-runner-versio |
| `sn91:scoring_commit:2026-11-03T06:36:56Z` | 91 | SCORING_COMMIT | 2026-11-03T09:27:38Z | sn91 commit touches scoring: fix(money): miner spend per RENT, not per reused pod name; make-good … |
| `sn116:scoring_commit:2026-11-03T03:36:57Z` | 116 | SCORING_COMMIT | 2026-11-03T09:27:38Z | sn116 commit touches scoring: Crown origin rebind tests: the cancel request names a real ChallengeKe |
| `sn1:release:v4.6.3` | 1 | RELEASE | 2026-11-03T17:17:02Z | sn1 released v4.6.3 |
| `sn21:release:SN21 training data v6 (windows 15 Aug - ` | 21 | RELEASE | 2026-11-03T17:17:02Z | sn21 released SN21 training data v6 (windows 15 Aug - 20 Sep 2026) |
| `sn51:release:miner-v1.011` | 51 | RELEASE | 2026-11-03T17:17:02Z | sn51 released miner-v1.011 |
| `sn51:scoring_commit:2026-11-03T16:15:58Z` | 51 | SCORING_COMMIT | 2026-11-03T17:17:02Z | sn51 commit touches scoring: DAH-5118 - [P1] Validator: flatten a many-layer image on the chosen n… |
| `sn66:release:v2026.11.03` | 66 | RELEASE | 2026-11-03T17:17:02Z | sn66 released v2026.11.03 |
| `sn66:scoring_commit:2026-11-03T13:57:07Z` | 66 | SCORING_COMMIT | 2026-11-03T17:17:02Z | sn66 commit touches scoring: fix: preserve the task-pool retirement active on production |
| `sn67:scoring_commit:2026-11-02T13:14:16Z` | 67 | SCORING_COMMIT | 2026-11-03T17:17:02Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20261102.post5 |
| `sn71:scoring_commit:2026-11-03T14:33:51Z` | 71 | SCORING_COMMIT | 2026-11-03T17:17:02Z | sn71 commit touches scoring: Clarify both host validators required for target-denial repair |
| `sn81:scoring_commit:2026-11-03T10:21:06Z` | 81 | SCORING_COMMIT | 2026-11-03T17:17:02Z | sn81 commit touches scoring: Retain comparison cells for independent estimator verification |
| `sn90:release:v1.3.4` | 90 | RELEASE | 2026-11-03T17:17:02Z | sn90 released v1.3.4 |
| `sn90:scoring_commit:2026-11-03T11:46:03Z` | 90 | SCORING_COMMIT | 2026-11-03T17:17:02Z | sn90 commit touches scoring: fix(validator): gate scoring on node heartbeat freshness + cluster he… |
| `sn91:scoring_commit:2026-11-03T09:33:02Z` | 91 | SCORING_COMMIT | 2026-11-03T17:17:02Z | sn91 commit touches scoring: perf(validator): stream private-eval forecast samples instead of hold… |
| `sn111:scoring_commit:2026-11-01T02:14:20Z` | 111 | SCORING_COMMIT | 2026-11-03T17:17:02Z | sn111 commit touches scoring: Match competition validation to mainnet harness and limits |
| `sn114:scoring_commit:2026-11-03T09:38:54Z` | 114 | SCORING_COMMIT | 2026-11-03T17:17:02Z | sn114 commit touches scoring: Show reset validations as pending |
| `sn116:scoring_commit:2026-11-03T15:19:27Z` | 116 | SCORING_COMMIT | 2026-11-03T17:17:02Z | sn116 commit touches scoring: Motor data kit: generate, parse, verify and practice score (kits/motor |
| `sn117:release:everycli v0.9.6` | 117 | RELEASE | 2026-11-03T17:17:02Z | sn117 released everycli v0.9.6 |
| `sn117:scoring_commit:2026-11-03T10:54:25Z` | 117 | SCORING_COMMIT | 2026-11-03T17:17:02Z | sn117 commit touches scoring: Fix BFL regional polling and preserve accepted task references |
| `sn25:scoring_commit:2026-11-03T17:23:34Z` | 25 | SCORING_COMMIT | 2026-11-03T22:27:15Z | sn25 commit touches scoring: Merge fix/validator-ledger-startup-prefix: a start authenticates only… |
| `sn28:release:v0.5.19-dev` | 28 | RELEASE | 2026-11-03T22:27:15Z | sn28 released v0.5.19-dev |
| `sn51:scoring_commit:2026-11-03T17:34:44Z` | 51 | SCORING_COMMIT | 2026-11-03T22:27:15Z | sn51 commit touches scoring: DAH-5635 - [P1] Validator: hide an unreachable node as soon as its mi… |
| `sn70:scoring_commit:2026-11-03T21:11:05Z` | 70 | SCORING_COMMIT | 2026-11-03T22:27:15Z | sn70 commit touches scoring: fix(validator): keep a proof's JSON numbers as serialised; int 0 cost… |
| `sn71:scoring_commit:2026-11-03T21:45:36Z` | 71 | SCORING_COMMIT | 2026-11-03T22:27:15Z | sn71 commit touches scoring: Merge pull request #988 from leadpoet/feat/history-rank-by-score |
| `sn78:scoring_commit:2026-11-03T18:42:41Z` | 78 | SCORING_COMMIT | 2026-11-03T22:27:15Z | sn78 commit touches scoring: Merge PR #503: reuse completed work and publish approved rewards |
| `sn91:scoring_commit:2026-11-03T21:02:09Z` | 91 | SCORING_COMMIT | 2026-11-03T22:27:15Z | sn91 commit touches scoring: fix(trainer): carry infra-failed challenger bench sweeps like deferre… |
| `sn108:scoring_commit:2026-11-03T18:12:32Z` | 108 | SCORING_COMMIT | 2026-11-03T22:27:15Z | sn108 commit touches scoring: Neuron 1.0.1: when the challenge server withholds the reward ladder (… |
| `sn111:scoring_commit:2026-11-03T19:58:36Z` | 111 | SCORING_COMMIT | 2026-11-03T22:27:15Z | sn111 commit touches scoring: Separate competition intake from sequential evaluation |
| `sn116:scoring_commit:2026-11-03T20:24:59Z` | 116 | SCORING_COMMIT | 2026-11-03T22:27:15Z | sn116 commit touches scoring: Kit local scorer: a thin caller of the official graph path, plus its … |
| `sn70:scoring_commit:2026-11-04T02:05:25Z` | 70 | SCORING_COMMIT | 2026-11-04T02:38:42Z | sn70 commit touches scoring: Merge pull request #125 from fugal-ai/diag/save-verified-heads |
| `sn71:scoring_commit:2026-11-03T22:30:50Z` | 71 | SCORING_COMMIT | 2026-11-04T02:38:42Z | sn71 commit touches scoring: Accept asserted acquisition-completion announcements and verify final… |
| `sn25:scoring_commit:2026-11-04T03:01:40Z` | 25 | SCORING_COMMIT | 2026-11-04T09:56:37Z | sn25 commit touches scoring: Merge fix/validator-tunnel-tls-timeout: a tunnel's TLS establishment … |
| `sn28:release:v0.5.19` | 28 | RELEASE | 2026-11-04T09:56:37Z | sn28 released v0.5.19 |
| `sn51:release:executor-v1.168` | 51 | RELEASE | 2026-11-04T09:56:37Z | sn51 released executor-v1.168 |
| `sn51:scoring_commit:2026-11-04T09:12:56Z` | 51 | SCORING_COMMIT | 2026-11-04T09:56:37Z | sn51 commit touches scoring: DAH-5682 - [P0] Validator: port check can skip later tiers after two … |
| `sn55:scoring_commit:2026-11-04T06:13:10Z` | 55 | SCORING_COMMIT | 2026-11-04T09:56:37Z | sn55 commit touches scoring: update validation block number |
| `sn70:scoring_commit:2026-11-04T04:01:35Z` | 70 | SCORING_COMMIT | 2026-11-04T09:56:37Z | sn70 commit touches scoring: Merge pull request #126 from fugal-ai/docs/miner-guide-failed-calls |
| `sn71:scoring_commit:2026-11-04T07:50:53Z` | 71 | SCORING_COMMIT | 2026-11-04T09:56:37Z | sn71 commit touches scoring: Reuse validated scoring source within one Arena evidence read |
| `sn89:scoring_commit:2026-11-03T18:21:02Z` | 89 | SCORING_COMMIT | 2026-11-04T09:56:37Z | sn89 commit touches scoring: Agent competition v2: receipts, anchoring, weekly freeze, validator w… |
| `sn91:scoring_commit:2026-11-04T03:53:32Z` | 91 | SCORING_COMMIT | 2026-11-04T09:56:37Z | sn91 commit touches scoring: fix(funded): small our-side losses rerun on the miner's key; ready ti… |
| `sn108:scoring_commit:2026-11-04T06:47:38Z` | 108 | SCORING_COMMIT | 2026-11-04T09:56:37Z | sn108 commit touches scoring: Validator hardware requirements (minimum and recommended): 16 cores /… |
| `sn1:release:v4.7.0` | 1 | RELEASE | 2026-11-04T17:58:02Z | sn1 released v4.7.0 |
| `sn3:scoring_commit:2026-11-04T14:07:31Z` | 3 | SCORING_COMMIT | 2026-11-04T17:58:02Z | sn3 commit touches scoring: Set document evaluation lower bound to 2 tokens |
| `sn28:release:v0.5.21` | 28 | RELEASE | 2026-11-04T17:58:02Z | sn28 released v0.5.21 |
| `sn41:scoring_commit:2026-11-03T16:01:58Z` | 41 | SCORING_COMMIT | 2026-11-04T17:58:02Z | sn41 commit touches scoring: miner: builder-sign request sends only {method, path, body}; Almanac'… |
| `sn51:release:executor-v1.169` | 51 | RELEASE | 2026-11-04T17:58:02Z | sn51 released executor-v1.169 |
| `sn51:scoring_commit:2026-11-04T15:52:23Z` | 51 | SCORING_COMMIT | 2026-11-04T17:58:02Z | sn51 commit touches scoring: DAH-2786 - [P2] Validator: clear the filler's cap claim again once it… |
| `sn66:release:deployed/dev: Merge pull request #190 fr` | 66 | RELEASE | 2026-11-04T17:58:02Z | sn66 released deployed/dev: Merge pull request #190 from conjectures-io/main |
| `sn67:scoring_commit:2026-11-04T10:50:21Z` | 67 | SCORING_COMMIT | 2026-11-04T17:58:02Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20261104.post2 |
| `sn70:scoring_commit:2026-11-04T16:31:01Z` | 70 | SCORING_COMMIT | 2026-11-04T17:58:02Z | sn70 commit touches scoring: docs: MINER_GUIDE: reveal bucket; no GPU needed |
| `sn71:scoring_commit:2026-11-04T11:42:22Z` | 71 | SCORING_COMMIT | 2026-11-04T17:58:02Z | sn71 commit touches scoring: Reuse verified clean text in final training export privacy walk |
| `sn81:scoring_commit:2026-11-04T15:19:03Z` | 81 | SCORING_COMMIT | 2026-11-04T17:58:02Z | sn81 commit touches scoring: fix(admin): skip retired zero-cap tasks in the drain check |
| `sn82:scoring_commit:2026-11-04T16:37:30Z` | 82 | SCORING_COMMIT | 2026-11-04T17:58:02Z | sn82 commit touches scoring: Scope validator collateral reads to the configured subnet (#5) |
| `sn108:scoring_commit:2026-11-04T17:07:20Z` | 108 | SCORING_COMMIT | 2026-11-04T17:58:02Z | sn108 commit touches scoring: Neuron 1.0.2: miner_cli.py replace <zip> [--submission-id <id>] repla… |
| `sn111:scoring_commit:2026-11-04T14:46:19Z` | 111 | SCORING_COMMIT | 2026-11-04T17:58:02Z | sn111 commit touches scoring: Automate sealed-package duplicate preflight before evaluation |
| `sn114:scoring_commit:2026-11-04T13:20:00Z` | 114 | SCORING_COMMIT | 2026-11-04T17:58:02Z | sn114 commit touches scoring: Merge pull request #241 from DendriteHQ/feat/validator-docker-watcher |
| `sn120:scoring_commit:2026-11-04T14:06:41Z` | 120 | SCORING_COMMIT | 2026-11-04T17:58:02Z | sn120 commit touches scoring: miner kit: affine_batch.py check accepts the file after the options; … |
| `sn12:release:sdk-v0.0.20: feat: local executor and lo` | 12 | RELEASE | 2026-11-04T23:36:57Z | sn12 released sdk-v0.0.20: feat: local executor and local bind mount volumes (#861) |
| `sn58:scoring_commit:2026-11-04T13:21:00Z` | 58 | SCORING_COMMIT | 2026-11-04T23:36:57Z | sn58 commit touches scoring: feat(validator): only a permitted Hub account starts |
| `sn70:release:image-v2026.11.05` | 70 | RELEASE | 2026-11-04T23:36:57Z | sn70 released image-v2026.11.05 |
| `sn71:scoring_commit:2026-11-04T19:48:30Z` | 71 | SCORING_COMMIT | 2026-11-04T23:36:57Z | sn71 commit touches scoring: Pin reviewed scorer checkpoint imports in host boundary test |
| `sn81:scoring_commit:2026-11-04T17:48:31Z` | 81 | SCORING_COMMIT | 2026-11-04T23:36:57Z | sn81 commit touches scoring: fix(admin): deliver evaluation files to the platform bucket beside HTT |
| `sn120:scoring_commit:2026-11-04T23:06:44Z` | 120 | SCORING_COMMIT | 2026-11-04T23:36:57Z | sn120 commit touches scoring: local-gsm8k: a reply over 100 KB is passed to the Hub verify.py as it… |
| `sn27:release:archive/worktrees-2026-11-04` | 27 | RELEASE | 2026-11-05T03:46:12Z | sn27 released archive/worktrees-2026-11-04 |
| `sn71:scoring_commit:2026-11-05T00:57:17Z` | 71 | SCORING_COMMIT | 2026-11-05T03:46:12Z | sn71 commit touches scoring: Recover only the infrastructure-damaged Nov4 miner ICP7 slot |
| `sn82:scoring_commit:2026-11-05T02:09:15Z` | 82 | SCORING_COMMIT | 2026-11-05T03:46:12Z | sn82 commit touches scoring: Merge pull request #6: Improve validator publication diagnostics |
| `sn116:scoring_commit:2026-11-05T02:39:53Z` | 116 | SCORING_COMMIT | 2026-11-05T03:46:12Z | sn116 commit touches scoring: Owner manifest migration: encode the Validator's M2 rule |
| `sn51:release:executor-v1.171` | 51 | RELEASE | 2026-11-05T11:38:32Z | sn51 released executor-v1.171 |
| `sn51:scoring_commit:2026-11-05T11:31:04Z` | 51 | SCORING_COMMIT | 2026-11-05T11:38:32Z | sn51 commit touches scoring: DAH-5664 - [P0] Validator: reclaim a killed filler's Dolphin cache di… |
| `sn67:scoring_commit:2026-11-05T08:58:27Z` | 67 | SCORING_COMMIT | 2026-11-05T11:38:32Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20261105.post4 |
| `sn71:scoring_commit:2026-11-05T07:49:03Z` | 71 | SCORING_COMMIT | 2026-11-05T11:38:32Z | sn71 commit touches scoring: Merge pull request #1036 from leadpoet/op/arena-observation-verify-re… |
| `sn81:scoring_commit:2026-11-05T07:55:40Z` | 81 | SCORING_COMMIT | 2026-11-05T11:38:32Z | sn81 commit touches scoring: fix(audit): refuse forced-draw drift without charging the miner |
| `sn116:scoring_commit:2026-11-05T05:47:06Z` | 116 | SCORING_COMMIT | 2026-11-05T11:38:32Z | sn116 commit touches scoring: A2: keep attempt 1's evaluation files so a re-run binds its own (TL 4… |
| `sn21:scoring_commit:2026-11-05T17:26:44Z` | 21 | SCORING_COMMIT | 2026-11-05T19:03:37Z | sn21 commit touches scoring: feat(status): each miner's model start, days unchanged and first day … |
| `sn46:release:v0.1.5` | 46 | RELEASE | 2026-11-05T19:03:37Z | sn46 released v0.1.5 |
| `sn51:release:lium-protocol-v2.9.0` | 51 | RELEASE | 2026-11-05T19:03:37Z | sn51 released lium-protocol-v2.9.0 |
| `sn51:scoring_commit:2026-11-05T15:36:10Z` | 51 | SCORING_COMMIT | 2026-11-05T19:03:37Z | sn51 commit touches scoring: DAH-5462 - [P2] Validator: skip the new-node network re-measure when … |
| `sn55:scoring_commit:2026-11-05T14:45:40Z` | 55 | SCORING_COMMIT | 2026-11-05T19:03:37Z | sn55 commit touches scoring: report seeds after scoring |
| `sn66:release:v2026.11.05` | 66 | RELEASE | 2026-11-05T19:03:37Z | sn66 released v2026.11.05 |
| `sn70:release:image-v2026.11.05b` | 70 | RELEASE | 2026-11-05T19:03:37Z | sn70 released image-v2026.11.05b |
| `sn71:scoring_commit:2026-11-05T17:57:29Z` | 71 | SCORING_COMMIT | 2026-11-05T19:03:37Z | sn71 commit touches scoring: Merge pull request #1046 from leadpoet/docs/task-deployment-responsib… |
| `sn81:scoring_commit:2026-11-05T14:14:51Z` | 81 | SCORING_COMMIT | 2026-11-05T19:03:37Z | sn81 commit touches scoring: build(order-control): signed episode runtime and eval tasksets |
| `sn120:scoring_commit:2026-11-05T14:09:43Z` | 120 | SCORING_COMMIT | 2026-11-05T19:03:37Z | sn120 commit touches scoring: bench site: references shown if on the size-vs-score Pareto front for… |
| `sn5:scoring_commit:2026-11-05T21:08:24Z` | 5 | SCORING_COMMIT | 2026-11-06T00:09:29Z | sn5 commit touches scoring: Shorten the new-miner ramp to 12 observations |
| `sn25:scoring_commit:2026-11-05T19:43:11Z` | 25 | SCORING_COMMIT | 2026-11-06T00:09:29Z | sn25 commit touches scoring: Describe prospective seeded crawl coverage and scorer version three |
| `sn66:release:v2026.11.06` | 66 | RELEASE | 2026-11-06T00:09:29Z | sn66 released v2026.11.06 |
| `sn66:scoring_commit:2026-11-05T22:47:24Z` | 66 | SCORING_COMMIT | 2026-11-06T00:09:29Z | sn66 commit touches scoring: Pin task documentation for part iii display |
| `sn89:scoring_commit:2026-11-05T19:52:30Z` | 89 | SCORING_COMMIT | 2026-11-06T00:09:29Z | sn89 commit touches scoring: Validator: read blobs from extra bases (SN89_R2_EXTRA_BASES) |
| `sn111:scoring_commit:2026-11-05T20:21:56Z` | 111 | SCORING_COMMIT | 2026-11-06T00:09:29Z | sn111 commit touches scoring: Support audited competition amendments and safe scoring continuation |
| `sn120:scoring_commit:2026-11-05T19:50:55Z` | 120 | SCORING_COMMIT | 2026-11-06T00:09:29Z | sn120 commit touches scoring: sn120: gate-pool-v2 = gate-pool-v1 + hard-v1 slice (2,269 tasks, 32K … |
| `sn127:scoring_commit:2026-11-05T20:40:37Z` | 127 | SCORING_COMMIT | 2026-11-06T00:09:29Z | sn127 commit touches scoring: Validator: weights never wait for a soup round to free the GPU (ZIL-16 |
| `sn66:release:v2026.11.06.2` | 66 | RELEASE | 2026-11-06T07:08:56Z | sn66 released v2026.11.06.2 |
| `sn71:scoring_commit:2026-11-06T05:41:44Z` | 71 | SCORING_COMMIT | 2026-11-06T07:08:56Z | sn71 commit touches scoring: Finalize exact unused ninth review after miner planning |
| `sn78:scoring_commit:2026-11-05T18:43:34Z` | 78 | SCORING_COMMIT | 2026-11-06T07:08:56Z | sn78 commit touches scoring: Pass retained coverage through reward service test doubles |
| `sn51:release:executor-v1.172` | 51 | RELEASE | 2026-11-06T15:16:05Z | sn51 released executor-v1.172 |
| `sn51:scoring_commit:2026-11-06T12:40:51Z` | 51 | SCORING_COMMIT | 2026-11-06T15:16:05Z | sn51 commit touches scoring: DAH-5803 - [P1] Validator registry pull: a connection reset to Docker… |
| `sn71:scoring_commit:2026-11-06T13:56:24Z` | 71 | SCORING_COMMIT | 2026-11-06T15:16:05Z | sn71 commit touches scoring: Merge pull request #1087 from leadpoet/fix/arena-unscored-uncertain-o… |
| `sn78:scoring_commit:2026-11-06T05:33:30Z` | 78 | SCORING_COMMIT | 2026-11-06T15:16:05Z | sn78 commit touches scoring: Reuse each freshly validated proof receipt during lookup and capture |
| `sn108:scoring_commit:2026-11-06T12:31:40Z` | 108 | SCORING_COMMIT | 2026-11-06T15:16:05Z | sn108 commit touches scoring: Neuron 1.0.3: report the EDA server's disk. The validator reads disk … |
| `sn116:scoring_commit:2026-11-06T11:48:04Z` | 116 | SCORING_COMMIT | 2026-11-06T15:16:05Z | sn116 commit touches scoring: H5: a door config with no accepted revision is UNKNOWN (Validator-2 1… |
| `sn2:scoring_commit:2026-11-06T20:42:23Z` | 2 | SCORING_COMMIT | 2026-11-06T20:59:00Z | sn2 commit touches scoring: Prepare Finney SN2 validator onboarding and cron updates |
| `sn14:scoring_commit:2026-11-03T07:50:08Z` | 14 | SCORING_COMMIT | 2026-11-06T20:59:00Z | sn14 commit touches scoring: Release reward priority after completed worker HOLDs |
| `sn28:release:v0.5.22` | 28 | RELEASE | 2026-11-06T20:59:00Z | sn28 released v0.5.22 |
| `sn71:scoring_commit:2026-11-06T19:59:13Z` | 71 | SCORING_COMMIT | 2026-11-06T20:59:00Z | sn71 commit touches scoring: Preserve consumed redirect provenance and validate internal Chat trai… |
| `sn104:scoring_commit:2026-11-06T17:39:31Z` | 104 | SCORING_COMMIT | 2026-11-06T20:59:00Z | sn104 commit touches scoring: fix(validator): sync live operational fixes into main |
| `sn108:scoring_commit:2026-11-06T17:42:55Z` | 108 | SCORING_COMMIT | 2026-11-06T20:59:00Z | sn108 commit touches scoring: Validator requirements: 500 GB SSD recommended (300 GB minimum); the … |
| `sn116:scoring_commit:2026-11-06T17:10:02Z` | 116 | SCORING_COMMIT | 2026-11-06T20:59:00Z | sn116 commit touches scoring: Dashboard Updates page (miner Updates), re-cut of 36845338 onto main … |
| `sn120:scoring_commit:2026-11-06T15:23:57Z` | 120 | SCORING_COMMIT | 2026-11-06T20:59:00Z | sn120 commit touches scoring: sn120: gate task cap 32K -> 64K (Jacob pt1324u) |
| `sn2:scoring_commit:2026-11-06T21:26:38Z` | 2 | SCORING_COMMIT | 2026-11-07T00:52:36Z | sn2 commit touches scoring: Publish operator-focused SN2 validator documentation |
| `sn66:release:v2026.11.06.3` | 66 | RELEASE | 2026-11-07T00:52:36Z | sn66 released v2026.11.06.3 |
| `sn66:scoring_commit:2026-11-06T20:07:47Z` | 66 | SCORING_COMMIT | 2026-11-07T00:52:36Z | sn66 commit touches scoring: Bound archive validation resources and enforce chat-log storage quotas |
| `sn71:scoring_commit:2026-11-06T23:18:31Z` | 71 | SCORING_COMMIT | 2026-11-07T00:52:36Z | sn71 commit touches scoring: Test historical verifier finality with its matching frozen caller |
| `sn116:scoring_commit:2026-11-06T21:53:51Z` | 116 | SCORING_COMMIT | 2026-11-07T00:52:36Z | sn116 commit touches scoring: Queue view: a GET never slows a grade (Validator-2 must-fix) |
| `sn120:scoring_commit:2026-11-07T00:17:07Z` | 120 | SCORING_COMMIT | 2026-11-07T00:52:36Z | sn120 commit touches scoring: Clarify independent 64K gate limits in miner documentation |
| `sn34:scoring_commit:2026-11-07T04:54:09Z` | 34 | SCORING_COMMIT | 2026-11-07T07:02:35Z | sn34 commit touches scoring: Rename the miner command from yugos to ycli (#48) |
| `sn37:scoring_commit:2026-11-07T00:56:30Z` | 37 | SCORING_COMMIT | 2026-11-07T07:02:35Z | sn37 commit touches scoring: fix(miner): support reviewed runtime488 funding |
| `sn71:scoring_commit:2026-11-07T05:16:58Z` | 71 | SCORING_COMMIT | 2026-11-07T07:02:35Z | sn71 commit touches scoring: Preserve verified identity and complete paragraph facts; explain Aren… |
| `sn78:scoring_commit:2026-11-07T01:44:01Z` | 78 | SCORING_COMMIT | 2026-11-07T07:02:35Z | sn78 commit touches scoring: Merge pull request #518 from Umi-BitSign/fix/chunked-verification-res… |
| `sn81:scoring_commit:2026-11-06T16:54:21Z` | 81 | SCORING_COMMIT | 2026-11-07T07:02:35Z | sn81 commit touches scoring: feat(order-control): keep an order from miners until its audit execut… |
| `sn116:scoring_commit:2026-11-07T01:02:17Z` | 116 | SCORING_COMMIT | 2026-11-07T07:02:35Z | sn116 commit touches scoring: Queue view: only a built task waits to grade (cancelled / archived ne… |
| `sn120:scoring_commit:2026-11-07T01:44:15Z` | 120 | SCORING_COMMIT | 2026-11-07T07:02:35Z | sn120 commit touches scoring: PE admission: verify every frozen probe cell, not summary counters |
| `sn71:scoring_commit:2026-11-07T12:41:58Z` | 71 | SCORING_COMMIT | 2026-11-07T13:56:48Z | sn71 commit touches scoring: Merge pull request #1106 from leadpoet/codex/audit-sn71-score-retry-2… |
| `sn81:scoring_commit:2026-11-07T11:15:29Z` | 81 | SCORING_COMMIT | 2026-11-07T13:56:48Z | sn81 commit touches scoring: Merge pull request #466 from reliquadotai/perf/sparse-warp-verify |
| `sn93:scoring_commit:2026-11-07T11:48:35Z` | 93 | SCORING_COMMIT | 2026-11-07T13:56:48Z | sn93 commit touches scoring: fix: bound miner refreshes and reject private axon destinations (#179) |
| `sn116:scoring_commit:2026-11-07T13:33:45Z` | 116 | SCORING_COMMIT | 2026-11-07T13:56:48Z | sn116 commit touches scoring: Practice on the data kit's verify set for new versions (owner: "Yes, … |
| `sn17:release:witness-client-v0.2.18` | 17 | RELEASE | 2026-11-07T18:42:57Z | sn17 released witness-client-v0.2.18 |
| `sn17:scoring_commit:2026-11-07T18:17:24Z` | 17 | SCORING_COMMIT | 2026-11-07T18:42:57Z | sn17 commit touches scoring: Apply the request deadline to cached grant validation |
| `sn66:release:v2026.11.07` | 66 | RELEASE | 2026-11-07T18:42:57Z | sn66 released v2026.11.07 |
| `sn71:scoring_commit:2026-11-07T13:44:22Z` | 71 | SCORING_COMMIT | 2026-11-07T18:42:57Z | sn71 commit touches scoring: Continue evidence-source validation past unrelated candidates |
| `sn116:scoring_commit:2026-11-07T14:54:24Z` | 116 | SCORING_COMMIT | 2026-11-07T18:42:57Z | sn116 commit touches scoring: Crown-time D + menu: the Validator's 7 Nov 08:18 must-fixes |
| `sn71:scoring_commit:2026-11-07T20:20:23Z` | 71 | SCORING_COMMIT | 2026-11-07T22:21:04Z | sn71 commit touches scoring: Integrate current training permission metadata before verified release |
| `sn90:release:v1.3.6: feat(subnet): show Chutes median` | 90 | RELEASE | 2026-11-07T22:21:04Z | sn90 released v1.3.6: feat(subnet): show Chutes median GPU revenue on dashboard |
| `sn90:scoring_commit:2026-11-07T20:14:43Z` | 90 | SCORING_COMMIT | 2026-11-07T22:21:04Z | sn90 commit touches scoring: chore(subnet): bump validator fallback version to 1.3.5 |
| `sn127:scoring_commit:2026-11-07T20:18:51Z` | 127 | SCORING_COMMIT | 2026-11-07T22:21:04Z | sn127 commit touches scoring: Miner terms for mainnet subnet 127 and the open tier |
| `sn17:release:witness-gateway-disconnect-20261108` | 17 | RELEASE | 2026-11-08T01:42:10Z | sn17 released witness-gateway-disconnect-20261108 |
| `sn90:release:v1.4.1: feat(pricing): lower three-provi` | 90 | RELEASE | 2026-11-08T01:42:10Z | sn90 released v1.4.1: feat(pricing): lower three-provider markup to five percent |
| `sn116:scoring_commit:2026-11-07T21:44:08Z` | 116 | SCORING_COMMIT | 2026-11-08T01:42:10Z | sn116 commit touches scoring: Held-contender view, miner side: signed feedback v5 + one plain line |
| `sn17:release:witness-gateway-fence-poll-20261108` | 17 | RELEASE | 2026-11-08T08:01:16Z | sn17 released witness-gateway-fence-poll-20261108 |
| `sn71:scoring_commit:2026-11-08T04:41:42Z` | 71 | SCORING_COMMIT | 2026-11-08T08:01:16Z | sn71 commit touches scoring: Verify delegated admission deferral in replacement readiness |
| `sn11:release:v0.7.8` | 11 | RELEASE | 2026-11-08T15:05:15Z | sn11 released v0.7.8 |
| `sn11:scoring_commit:2026-11-08T10:30:24Z` | 11 | SCORING_COMMIT | 2026-11-08T15:05:15Z | sn11 commit touches scoring: Burn all SN11 miner emission to owner UID 74; release 0.7.8 (#347) |
| `sn71:scoring_commit:2026-11-08T18:08:19Z` | 71 | SCORING_COMMIT | 2026-11-08T19:38:31Z | sn71 commit touches scoring: Verify full recovery function security on migration replay |
| `sn90:release:v1.4.2` | 90 | RELEASE | 2026-11-08T19:38:31Z | sn90 released v1.4.2 |
| `sn90:scoring_commit:2026-11-08T17:57:48Z` | 90 | SCORING_COMMIT | 2026-11-08T19:38:31Z | sn90 commit touches scoring: docs(subnet): consolidate miner node onboarding |
| `sn15:scoring_commit:2026-11-08T21:47:52Z` | 15 | SCORING_COMMIT | 2026-11-08T23:11:26Z | sn15 commit touches scoring: feat(validator): report each episode's end reason and duration (#406) |
| `sn71:scoring_commit:2026-11-08T20:35:21Z` | 71 | SCORING_COMMIT | 2026-11-08T23:11:26Z | sn71 commit touches scoring: Merge pull request #1132 from leadpoet/fix/arena-provider-child-score… |
| `sn34:scoring_commit:2026-11-09T00:20:00Z` | 34 | SCORING_COMMIT | 2026-11-09T02:52:26Z | sn34 commit touches scoring: Remove grader versions from prepared tasks |
| `sn71:scoring_commit:2026-11-09T02:03:21Z` | 71 | SCORING_COMMIT | 2026-11-09T02:52:26Z | sn71 commit touches scoring: Merge pull request #1136 from leadpoet/fix/arena-verifier-accuracy-re… |
| `sn116:scoring_commit:2026-11-08T02:06:53Z` | 116 | SCORING_COMMIT | 2026-11-09T02:52:26Z | sn116 commit touches scoring: Door chain reader: an uncollected SDK session-task failure is one typ… |
| `sn17:readme_task_diff:8c892da1ead4dfc7` | 17 | README_TASK_DIFF | 2026-11-02T19:40:04Z | sn17 README task/scoring sections changed |
| `sn117:readme_task_diff:9d04ab2709490011` | 117 | README_TASK_DIFF | 2026-11-02T19:40:04Z | sn117 README task/scoring sections changed |
| `sn48:readme_task_diff:9f1b0dd706840592` | 48 | README_TASK_DIFF | 2026-11-03T01:50:43Z | sn48 README task/scoring sections changed |
| `sn117:readme_task_diff:1f25c890c0113301` | 117 | README_TASK_DIFF | 2026-11-03T01:50:43Z | sn117 README task/scoring sections changed |
| `sn28:readme_task_diff:359c18a4bfd66b7f` | 28 | README_TASK_DIFF | 2026-11-03T17:17:02Z | sn28 README task/scoring sections changed |
| `sn127:readme_task_diff:3849c8ce33ebd107` | 127 | README_TASK_DIFF | 2026-11-03T17:17:02Z | sn127 README task/scoring sections changed |
| `sn78:readme_task_diff:905be9e940ec4dea` | 78 | README_TASK_DIFF | 2026-11-03T22:27:15Z | sn78 README task/scoring sections changed |
| `sn82:readme_task_diff:08b2f7bf22367533` | 82 | README_TASK_DIFF | 2026-11-03T22:27:15Z | sn82 README task/scoring sections changed |
| `sn127:readme_task_diff:501a9ff7ce421afb` | 127 | README_TASK_DIFF | 2026-11-03T22:27:15Z | sn127 README task/scoring sections changed |
| `sn37:readme_task_diff:b959b882769e8d45` | 37 | README_TASK_DIFF | 2026-11-04T09:56:37Z | sn37 README task/scoring sections changed |
| `sn51:readme_task_diff:6c34bfe187921963` | 51 | README_TASK_DIFF | 2026-11-04T09:56:37Z | sn51 README task/scoring sections changed |
| `sn67:readme_task_diff:d645efe7e4c8621a` | 67 | README_TASK_DIFF | 2026-11-04T17:58:02Z | sn67 README task/scoring sections changed |
| `sn90:readme_task_diff:b99aba463098496e` | 90 | README_TASK_DIFF | 2026-11-04T17:58:02Z | sn90 README task/scoring sections changed |
| `sn58:readme_task_diff:3b8b49ad2ebb4e84` | 58 | README_TASK_DIFF | 2026-11-04T23:36:57Z | sn58 README task/scoring sections changed |
| `sn51:readme_task_diff:77525fe4e41362db` | 51 | README_TASK_DIFF | 2026-11-05T11:38:32Z | sn51 README task/scoring sections changed |
| `sn58:readme_task_diff:de3e9164e32563c5` | 58 | README_TASK_DIFF | 2026-11-05T19:03:37Z | sn58 README task/scoring sections changed |
| `sn123:readme_task_diff:855cbeee88da3234` | 123 | README_TASK_DIFF | 2026-11-06T07:08:56Z | sn123 README task/scoring sections changed |
| `sn28:readme_task_diff:3988d29ccf7e7016` | 28 | README_TASK_DIFF | 2026-11-06T20:59:00Z | sn28 README task/scoring sections changed |
| `sn88:readme_task_diff:b0837afa350cd1d5` | 88 | README_TASK_DIFF | 2026-11-06T20:59:00Z | sn88 README task/scoring sections changed |
| `sn37:readme_task_diff:0ff79d9d6b17ca0c` | 37 | README_TASK_DIFF | 2026-11-07T07:02:35Z | sn37 README task/scoring sections changed |
| `sn15:readme_task_diff:4d00db5f525b3425` | 15 | README_TASK_DIFF | 2026-11-07T18:42:57Z | sn15 README task/scoring sections changed |
| `sn90:readme_task_diff:ddf545eb7067fc3b` | 90 | README_TASK_DIFF | 2026-11-08T19:38:31Z | sn90 README task/scoring sections changed |

## RESOLVED IN THIS WINDOW

_none_
