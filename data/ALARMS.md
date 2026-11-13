# ALARMS - generated 2026-11-13T07:23:00Z, block 9495903

window: first_seen in [2026-11-13T06:08:28Z, 2026-11-13T07:23:28Z)  (60 min interval + 15 min overlap)

Report ONLY the rows under NEW SINCE LAST RUN. Rows under STILL OPEN were
already reported in an earlier window and must not be re-alarmed.

## NEW SINCE LAST RUN

| event_id | netuid | class | severity | first_seen_utc | one_line |
|---|---|---|---|---|---|
| `sn45:scoring_commit:2026-11-13T03:38:27Z` | 45 | SCORING_COMMIT | P1 | 2026-11-13T07:23:28Z | sn45 commit touches scoring: AlphaRidge 4.1.1: validator stability |
| `sn51:scoring_commit:2026-11-13T04:01:45Z` | 51 | SCORING_COMMIT | P1 | 2026-11-13T07:23:28Z | sn51 commit touches scoring: DAH-6325 - [P0] Validator FIXED_RATIO follows the 50% miner emission … |
| `sn81:scoring_commit:2026-11-13T04:22:44Z` | 81 | SCORING_COMMIT | P1 | 2026-11-13T07:23:28Z | sn81 commit touches scoring: fix(admin): keep a job's counts for good only once its tasks are reti… |
| `sn127:release:Release 3e2660e` | 127 | RELEASE | P1 | 2026-11-13T07:23:28Z | sn127 released Release 3e2660e |
| `sn48:readme_task_diff:ccea6584910d3bd5` | 48 | README_TASK_DIFF | P2 | 2026-11-13T07:23:28Z | sn48 README task/scoring sections changed |

### detail

- **`sn45:scoring_commit:2026-11-13T03:38:27Z`** - sn45 commit touches scoring: AlphaRidge 4.1.1: validator stability
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn51:scoring_commit:2026-11-13T04:01:45Z`** - sn51 commit touches scoring: DAH-6325 - [P0] Validator FIXED_RATIO follows the 50% miner emission …
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn81:scoring_commit:2026-11-13T04:22:44Z`** - sn81 commit touches scoring: fix(admin): keep a job's counts for good only once its tasks are reti…
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn127:release:Release 3e2660e`** - sn127 released Release 3e2660e
  - published 2026-11-13T01:33:47Z (was Release ba66e7b)
- **`sn48:readme_task_diff:ccea6584910d3bd5`** - sn48 README task/scoring sections changed
  - Only the task-describing headings are hashed, so badge and typo edits do not trigger this.

## STILL OPEN (already reported - do not re-alarm)

| event_id | netuid | class | first_seen_utc | one_line |
|---|---|---|---|---|
| `sn37:burn_drop:0.091` | 37 | BURN_DROP | 2026-11-07T07:02:35Z | sn37 burn fell 1.000 -> 0.091 - miners can earn again |
| `sn76:burn_drop:0.984` | 76 | BURN_DROP | 2026-11-08T01:42:10Z | sn76 burn fell 0.992 -> 0.984 - miners can earn again |
| `sn126:burn_drop:0.985` | 126 | BURN_DROP | 2026-11-08T01:42:10Z | sn126 burn fell 1.000 -> 0.985 - miners can earn again |
| `sn76:burn_drop:0.985` | 76 | BURN_DROP | 2026-11-08T19:38:31Z | sn76 burn fell 0.996 -> 0.985 - miners can earn again |
| `sn121:burn_drop:0.646` | 121 | BURN_DROP | 2026-11-09T21:33:03Z | sn121 burn fell 1.000 -> 0.646 - miners can earn again |
| `sn127:burn_drop:0.960` | 127 | BURN_DROP | 2026-11-09T21:33:03Z | sn127 burn fell 1.000 -> 0.960 - miners can earn again |
| `sn108:burn_drop:0.823` | 108 | BURN_DROP | 2026-11-11T07:14:22Z | sn108 burn fell 1.000 -> 0.823 - miners can earn again |
| `sn76:burn_drop:0.983` | 76 | BURN_DROP | 2026-11-11T15:30:25Z | sn76 burn fell 0.995 -> 0.983 - miners can earn again |
| `sn126:burn_drop:0.952` | 126 | BURN_DROP | 2026-11-11T22:18:50Z | sn126 burn fell 1.000 -> 0.952 - miners can earn again |
| `sn94:burn_drop:0.000` | 94 | BURN_DROP | 2026-11-12T03:14:04Z | sn94 burn fell 1.000 -> 0.000 - miners can earn again |
| `sn42:burn_drop:0.000` | 42 | BURN_DROP | 2026-11-13T00:38:05Z | sn42 burn fell 1.000 -> 0.000 - miners can earn again |
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
| `sn15:release:v3.0.8: feat(validator): report each epi` | 15 | RELEASE | 2026-11-09T11:22:14Z | sn15 released v3.0.8: feat(validator): report each episode's end reason and duration (#406) |
| `sn51:release:watchtower-v1.2.1: DAH-5942 - docker_bui` | 51 | RELEASE | 2026-11-09T11:22:14Z | sn51 released watchtower-v1.2.1: DAH-5942 - docker_build.sh: optional multi-arch build to an OCI archive |
| `sn51:scoring_commit:2026-11-09T09:10:49Z` | 51 | SCORING_COMMIT | 2026-11-09T11:22:14Z | sn51 commit touches scoring: DAH-5917 - [P2] Miner releases: create the GitHub release when a mine… |
| `sn53:scoring_commit:2026-11-09T08:47:21Z` | 53 | SCORING_COMMIT | 2026-11-09T11:22:14Z | sn53 commit touches scoring: tee_miner: read KV load from sglang /v1/loads when /get_load is gone … |
| `sn66:release:v2026.11.09` | 66 | RELEASE | 2026-11-09T11:22:14Z | sn66 released v2026.11.09 |
| `sn67:scoring_commit:2026-11-09T07:00:28Z` | 67 | SCORING_COMMIT | 2026-11-09T11:22:14Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20261109.post1 |
| `sn71:scoring_commit:2026-11-09T09:13:31Z` | 71 | SCORING_COMMIT | 2026-11-09T11:22:14Z | sn71 commit touches scoring: Allow the fixed reward clock failure label in telemetry |
| `sn97:scoring_commit:2026-11-09T10:05:07Z` | 97 | SCORING_COMMIT | 2026-11-09T11:22:14Z | sn97 commit touches scoring: fix(miner): Fixed ty format |
| `sn108:scoring_commit:2026-11-09T08:54:14Z` | 108 | SCORING_COMMIT | 2026-11-09T11:22:14Z | sn108 commit touches scoring: Neuron 1.0.5: a validator updated mid-evaluation waits for the run it… |
| `sn127:scoring_commit:2026-11-09T04:08:30Z` | 127 | SCORING_COMMIT | 2026-11-09T11:22:14Z | sn127 commit touches scoring: Merge pull request #222 from ooo-hq/miner-delete-data |
| `sn28:release:v0.5.24` | 28 | RELEASE | 2026-11-09T21:33:03Z | sn28 released v0.5.24 |
| `sn41:scoring_commit:2026-11-09T17:58:19Z` | 41 | SCORING_COMMIT | 2026-11-09T21:33:03Z | sn41 commit touches scoring: Using the validator gamma api call for the latest prices as proper pr… |
| `sn51:scoring_commit:2026-11-09T13:43:37Z` | 51 | SCORING_COMMIT | 2026-11-09T21:33:03Z | sn51 commit touches scoring: DAH-6008 - [P0] validator: accept GB200 and pay it at the B200 rate a… |
| `sn56:scoring_commit:2026-11-09T15:57:07Z` | 56 | SCORING_COMMIT | 2026-11-09T21:33:03Z | sn56 commit touches scoring: Route multi-GPU tasks to SXM/NVLink trainers only (#1424) |
| `sn67:scoring_commit:2026-11-09T13:21:42Z` | 67 | SCORING_COMMIT | 2026-11-09T21:33:03Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20261109.post5 |
| `sn71:scoring_commit:2026-11-09T19:23:33Z` | 71 | SCORING_COMMIT | 2026-11-09T21:33:03Z | sn71 commit touches scoring: Merge pull request #1160 from leadpoet/fix/verifier-tested-xxhash-ver… |
| `sn116:scoring_commit:2026-11-09T07:06:50Z` | 116 | SCORING_COMMIT | 2026-11-09T21:33:03Z | sn116 commit touches scoring: Kit page Motor: Carbon Validator-Motor must-fixes (both back-EMF cell… |
| `sn117:release:everycli v1.0.0` | 117 | RELEASE | 2026-11-09T21:33:03Z | sn117 released everycli v1.0.0 |
| `sn117:scoring_commit:2026-11-09T12:31:12Z` | 117 | SCORING_COMMIT | 2026-11-09T21:33:03Z | sn117 commit touches scoring: test: verify Phala UI errors and await responsive layout |
| `sn127:scoring_commit:2026-11-09T16:22:46Z` | 127 | SCORING_COMMIT | 2026-11-09T21:33:03Z | sn127 commit touches scoring: Merge pull request #225 from ooo-hq/miner-release-in-claim |
| `sn15:scoring_commit:2026-11-10T02:15:07Z` | 15 | SCORING_COMMIT | 2026-11-10T03:50:58Z | sn15 commit touches scoring: docs: tag oroagents.com links in the miner and validator guides for a… |
| `sn36:scoring_commit:2026-11-10T02:29:05Z` | 36 | SCORING_COMMIT | 2026-11-10T03:50:58Z | sn36 commit touches scoring: Validator: GPUs with a UUID nvidia-smi would not give are not counted… |
| `sn51:release:executor-v1.173` | 51 | RELEASE | 2026-11-10T03:50:58Z | sn51 released executor-v1.173 |
| `sn66:release:v2026.11.10` | 66 | RELEASE | 2026-11-10T03:50:58Z | sn66 released v2026.11.10 |
| `sn70:release:build-v2026.11.10: Merge pull request #1` | 70 | RELEASE | 2026-11-10T03:50:58Z | sn70 released build-v2026.11.10: Merge pull request #185 from fugal-ai/release/v2 |
| `sn70:scoring_commit:2026-11-10T02:28:32Z` | 70 | SCORING_COMMIT | 2026-11-10T03:50:58Z | sn70 commit touches scoring: validator: only a head hash can count as a commitment |
| `sn71:scoring_commit:2026-11-10T00:19:25Z` | 71 | SCORING_COMMIT | 2026-11-10T03:50:58Z | sn71 commit touches scoring: Keep historical publication proofs on their frozen reward economics |
| `sn91:scoring_commit:2026-11-10T02:09:26Z` | 91 | SCORING_COMMIT | 2026-11-10T03:50:58Z | sn91 commit touches scoring: fix(validator): keep private-eval checkpoints on the GPU host, sha256… |
| `sn127:scoring_commit:2026-11-09T23:53:44Z` | 127 | SCORING_COMMIT | 2026-11-10T03:50:58Z | sn127 commit touches scoring: Merge pull request #229 from ooo-hq/docs-pass-miners |
| `sn51:release:miner-v1.012` | 51 | RELEASE | 2026-11-10T12:31:16Z | sn51 released miner-v1.012 |
| `sn51:scoring_commit:2026-11-10T11:34:23Z` | 51 | SCORING_COMMIT | 2026-11-10T12:31:16Z | sn51 commit touches scoring: Validator: judge a rented pod's ownership from / when /root reads emp… |
| `sn67:scoring_commit:2026-11-09T15:21:32Z` | 67 | SCORING_COMMIT | 2026-11-10T12:31:16Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20261109.post7 |
| `sn71:scoring_commit:2026-11-10T08:22:18Z` | 71 | SCORING_COMMIT | 2026-11-10T12:31:16Z | sn71 commit touches scoring: Require visible source excerpts for citation repair and verify native… |
| `sn3:scoring_commit:2026-11-10T12:44:11Z` | 3 | SCORING_COMMIT | 2026-11-10T20:02:20Z | sn3 commit touches scoring: Align evaluation defaults and docs with mainnet: 0 windows, 70M docum… |
| `sn12:release:miner-staging-2026-11-10-42883644919-432` | 12 | RELEASE | 2026-11-10T20:02:20Z | sn12 released miner-staging-2026-11-10-42883644919-432-1: feat: upgrade facilitator from ubuntu 20 to 26 (#862) |
| `sn66:release:v2026.11.10.2` | 66 | RELEASE | 2026-11-10T20:02:20Z | sn66 released v2026.11.10.2 |
| `sn70:scoring_commit:2026-11-10T16:23:25Z` | 70 | SCORING_COMMIT | 2026-11-10T20:02:20Z | sn70 commit touches scoring: Merge pull request #188 from fugal-ai/docs/miner-guide-v2-on-main |
| `sn71:scoring_commit:2026-11-10T16:56:50Z` | 71 | SCORING_COMMIT | 2026-11-10T20:02:20Z | sn71 commit touches scoring: Verify composed evidence prompts without fixed message offsets |
| `sn108:scoring_commit:2026-11-10T17:27:04Z` | 108 | SCORING_COMMIT | 2026-11-10T20:02:20Z | sn108 commit touches scoring: Neuron 1.0.7: miner_cli.py withdraw and replace pick, by default, onl… |
| `sn116:scoring_commit:2026-11-10T13:33:08Z` | 116 | SCORING_COMMIT | 2026-11-10T20:02:20Z | sn116 commit touches scoring: Updates: the lost-task re-queued uploads take the owner's (a): submit… |
| `sn117:release:everycli v1.1.0` | 117 | RELEASE | 2026-11-10T20:02:20Z | sn117 released everycli v1.1.0 |
| `sn124:scoring_commit:2026-11-10T16:24:24Z` | 124 | SCORING_COMMIT | 2026-11-10T20:02:20Z | sn124 commit touches scoring: Build test_RL tasks through the family runtime so a Sentinel run flie… |
| `sn127:scoring_commit:2026-11-10T19:00:30Z` | 127 | SCORING_COMMIT | 2026-11-10T20:02:20Z | sn127 commit touches scoring: Merge pull request #233 from ooo-hq/open-jobs-miners-first |
| `sn2:scoring_commit:2026-11-10T21:17:39Z` | 2 | SCORING_COMMIT | 2026-11-11T00:37:10Z | sn2 commit touches scoring: Merge pull request #1 from mybelovedstar123/test/score-properties |
| `sn17:scoring_commit:2026-11-10T20:39:45Z` | 17 | SCORING_COMMIT | 2026-11-11T00:37:10Z | sn17 commit touches scoring: Add validation worker with manual replays and resumable jobs (#94) |
| `sn54:scoring_commit:2026-11-10T23:12:47Z` | 54 | SCORING_COMMIT | 2026-11-11T00:37:10Z | sn54 commit touches scoring: Validate validator requests and submission integrity (#126) |
| `sn70:release:Fugal Subnet v0.3.1` | 70 | RELEASE | 2026-11-11T00:37:10Z | sn70 released Fugal Subnet v0.3.1 |
| `sn71:scoring_commit:2026-11-10T20:51:26Z` | 71 | SCORING_COMMIT | 2026-11-11T00:37:10Z | sn71 commit touches scoring: Reserve replay network budget after local final validation |
| `sn108:scoring_commit:2026-11-10T21:48:50Z` | 108 | SCORING_COMMIT | 2026-11-11T00:37:10Z | sn108 commit touches scoring: Neuron 1.0.9: the validator stops an evaluation at least 5 minutes be… |
| `sn117:release:everycli v1.1.1` | 117 | RELEASE | 2026-11-11T00:37:10Z | sn117 released everycli v1.1.1 |
| `sn36:scoring_commit:2026-11-11T06:08:30Z` | 36 | SCORING_COMMIT | 2026-11-11T07:14:22Z | sn36 commit touches scoring: Rented pool 10%, capped per miner at the platform fee its rentals pai… |
| `sn45:scoring_commit:2026-11-08T21:20:02Z` | 45 | SCORING_COMMIT | 2026-11-11T07:14:22Z | sn45 commit touches scoring: 3.9.15: starter claims what the validator would pay; well-formed irre… |
| `sn51:scoring_commit:2026-11-11T06:51:21Z` | 51 | SCORING_COMMIT | 2026-11-11T07:14:22Z | sn51 commit touches scoring: DAH-5845 - [P1] Validator: the rental cache reclaim never deletes the… |
| `sn62:release:v0.3.17` | 62 | RELEASE | 2026-11-11T07:14:22Z | sn62 released v0.3.17 |
| `sn62:scoring_commit:2026-11-11T02:39:48Z` | 62 | SCORING_COMMIT | 2026-11-11T07:14:22Z | sn62 commit touches scoring: Merge pull request #540 from ridgesai/fix/cap-miner-patch-size |
| `sn71:scoring_commit:2026-11-11T05:08:55Z` | 71 | SCORING_COMMIT | 2026-11-11T07:14:22Z | sn71 commit touches scoring: Expose private source-backed admission rejection findings to miners (… |
| `sn81:scoring_commit:2026-11-11T06:46:42Z` | 81 | SCORING_COMMIT | 2026-11-11T07:14:22Z | sn81 commit touches scoring: docs: one miner address, https://api.reliqua.ai (#484) |
| `sn116:scoring_commit:2026-11-11T01:09:19Z` | 116 | SCORING_COMMIT | 2026-11-11T07:14:22Z | sn116 commit touches scoring: Updates: testnet Motor + Cooling 1.8 switch notice: miner files are n… |
| `sn127:release:Release ed8326b` | 127 | RELEASE | 2026-11-11T07:14:22Z | sn127 released Release ed8326b |
| `sn127:scoring_commit:2026-11-11T04:16:42Z` | 127 | SCORING_COMMIT | 2026-11-11T07:14:22Z | sn127 commit touches scoring: zils-miner report goes through the hosted API by default (ZIL-197) |
| `sn17:release:Witness SDK 0.3.0` | 17 | RELEASE | 2026-11-11T15:30:25Z | sn17 released Witness SDK 0.3.0 |
| `sn17:scoring_commit:2026-11-11T14:24:20Z` | 17 | SCORING_COMMIT | 2026-11-11T15:30:25Z | sn17 commit touches scoring: Run resumable candidate validation on RunPod (#96) |
| `sn51:release:watchtower-v1.2.2: DAH-5053: lium-watcht` | 51 | RELEASE | 2026-11-11T15:30:25Z | sn51 released watchtower-v1.2.2: DAH-5053: lium-watchtower 1.2.2, the first amd64+arm64 build |
| `sn51:scoring_commit:2026-11-11T13:01:37Z` | 51 | SCORING_COMMIT | 2026-11-11T15:30:25Z | sn51 commit touches scoring: Miner: name the executors a pubkey upload cut off at its deadline (#2… |
| `sn71:scoring_commit:2026-11-11T07:02:19Z` | 71 | SCORING_COMMIT | 2026-11-11T15:30:25Z | sn71 commit touches scoring: Verify additive attempt bindings without replacing export golden hashe |
| `sn81:scoring_commit:2026-11-11T09:18:01Z` | 81 | SCORING_COMMIT | 2026-11-11T15:30:25Z | sn81 commit touches scoring: feat(orders): the admin job status says what the miners were paid per… |
| `sn117:release:everycli v1.1.3` | 117 | RELEASE | 2026-11-11T15:30:25Z | sn117 released everycli v1.1.3 |
| `sn117:scoring_commit:2026-11-11T11:12:58Z` | 117 | SCORING_COMMIT | 2026-11-11T15:30:25Z | sn117 commit touches scoring: Retain reviewed worker artifact for attested release validation |
| `sn8:scoring_commit:2026-11-11T22:14:38Z` | 8 | SCORING_COMMIT | 2026-11-11T22:18:50Z | sn8 commit touches scoring: New regular miners (#975) |
| `sn12:release:validator-staging-2026-11-11-43092055737` | 12 | RELEASE | 2026-11-11T22:18:50Z | sn12 released validator-staging-2026-11-11-43092055737-629-1: fix: upgrade vulnerable dependencies across subprojects (#864) |
| `sn17:scoring_commit:2026-11-11T21:55:09Z` | 17 | SCORING_COMMIT | 2026-11-11T22:18:50Z | sn17 commit touches scoring: Publish verdicts and launch the next validation Pod in one poll (#113) |
| `sn45:scoring_commit:2026-11-11T22:09:58Z` | 45 | SCORING_COMMIT | 2026-11-11T22:18:50Z | sn45 commit touches scoring: AlphaRidge 4.0.3: validator watchdog; the reference miner no longer p… |
| `sn51:release:watchtower-v1.2.3` | 51 | RELEASE | 2026-11-11T22:18:50Z | sn51 released watchtower-v1.2.3 |
| `sn51:scoring_commit:2026-11-11T16:03:30Z` | 51 | SCORING_COMMIT | 2026-11-11T22:18:50Z | sn51 commit touches scoring: DAH-6169 - Validator signs the whole request on every backend call (#… |
| `sn91:scoring_commit:2026-11-11T19:55:46Z` | 91 | SCORING_COMMIT | 2026-11-11T22:18:50Z | sn91 commit touches scoring: feat(validator): elastic bench host — rent the DEC-CA-0063 sweep pod … |
| `sn111:release:v2.0.0` | 111 | RELEASE | 2026-11-11T22:18:50Z | sn111 released v2.0.0 |
| `sn111:scoring_commit:2026-11-11T17:38:31Z` | 111 | SCORING_COMMIT | 2026-11-11T22:18:50Z | sn111 commit touches scoring: Allocate competition weights to miners and normalize legacy carry |
| `sn127:release:Release f9174a9` | 127 | RELEASE | 2026-11-11T22:18:50Z | sn127 released Release f9174a9 |
| `sn17:scoring_commit:2026-11-11T23:11:17Z` | 17 | SCORING_COMMIT | 2026-11-12T03:14:04Z | sn17 commit touches scoring: Improve validation Pod recovery and placement (#115) |
| `sn45:scoring_commit:2026-11-11T23:10:19Z` | 45 | SCORING_COMMIT | 2026-11-12T03:14:04Z | sn45 commit touches scoring: AlphaRidge 4.0.5: chain calls have a deadline; validators parse pages… |
| `sn66:release:v2026.11.12.2` | 66 | RELEASE | 2026-11-12T03:14:04Z | sn66 released v2026.11.12.2 |
| `sn70:release:Fugal Subnet v0.3.2` | 70 | RELEASE | 2026-11-12T03:14:04Z | sn70 released Fugal Subnet v0.3.2 |
| `sn70:scoring_commit:2026-11-12T02:31:18Z` | 70 | SCORING_COMMIT | 2026-11-12T03:14:04Z | sn70 commit touches scoring: release: v0.3.2 (validator-only collection fix; consensus digest unch… |
| `sn111:scoring_commit:2026-11-12T00:13:58Z` | 111 | SCORING_COMMIT | 2026-11-12T03:14:04Z | sn111 commit touches scoring: Publish mainnet miner burn allocation policy |
| `sn116:scoring_commit:2026-11-11T22:55:29Z` | 116 | SCORING_COMMIT | 2026-11-12T03:14:04Z | sn116 commit touches scoring: Merge miner app catalog practice-only (eea0f584) |
| `sn21:scoring_commit:2026-11-12T11:12:43Z` | 21 | SCORING_COMMIT | 2026-11-12T11:38:51Z | sn21 commit touches scoring: docs(rewards): the 40-day count belongs to the digest - going back to… |
| `sn51:release:executor-v1.180` | 51 | RELEASE | 2026-11-12T11:38:51Z | sn51 released executor-v1.180 |
| `sn51:scoring_commit:2026-11-12T11:25:24Z` | 51 | SCORING_COMMIT | 2026-11-12T11:38:51Z | sn51 commit touches scoring: DAH-6222 - [P1] Validator: a filler the validator removed itself is n… |
| `sn71:scoring_commit:2026-11-12T10:20:55Z` | 71 | SCORING_COMMIT | 2026-11-12T11:38:51Z | sn71 commit touches scoring: Merge pull request #1204 from leadpoet/fix/arena-intent-verification-… |
| `sn81:scoring_commit:2026-11-12T09:39:19Z` | 81 | SCORING_COMMIT | 2026-11-12T11:38:51Z | sn81 commit touches scoring: perf(audit): score drawn records ahead of their pass, and size the au… |
| `sn34:scoring_commit:2026-11-12T18:25:22Z` | 34 | SCORING_COMMIT | 2026-11-12T19:10:23Z | sn34 commit touches scoring: Merge pull request #54 from BitMind-AI/fix/receipt-digest-unscored-nan |
| `sn36:scoring_commit:2026-11-12T14:03:58Z` | 36 | SCORING_COMMIT | 2026-11-12T19:10:23Z | sn36 commit touches scoring: Publish miner agent and simplify connection setup |
| `sn51:release:executor-v1.181` | 51 | RELEASE | 2026-11-12T19:10:23Z | sn51 released executor-v1.181 |
| `sn51:scoring_commit:2026-11-12T16:11:22Z` | 51 | SCORING_COMMIT | 2026-11-12T19:10:23Z | sn51 commit touches scoring: DAH-4889 - [P0] validator: a foreign GPU workload on an idle node alw… |
| `sn67:scoring_commit:2026-11-12T15:06:38Z` | 67 | SCORING_COMMIT | 2026-11-12T19:10:23Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20261112.post5 |
| `sn76:scoring_commit:2026-11-12T18:48:07Z` | 76 | SCORING_COMMIT | 2026-11-12T19:10:23Z | sn76 commit touches scoring: docs: runner keys do not expire; to change an existing miner's key, w… |
| `sn116:scoring_commit:2026-11-12T13:53:04Z` | 116 | SCORING_COMMIT | 2026-11-12T19:10:23Z | sn116 commit touches scoring: Merge How rewards work (af0e367f) |
| `sn3:scoring_commit:2026-11-12T20:37:20Z` | 3 | SCORING_COMMIT | 2026-11-13T00:38:05Z | sn3 commit touches scoring: V3 validator preflight and weight publication timing |
| `sn42:release:v0.6.6` | 42 | RELEASE | 2026-11-13T00:38:05Z | sn42 released v0.6.6 |
| `sn45:scoring_commit:2026-11-12T19:58:00Z` | 45 | SCORING_COMMIT | 2026-11-13T00:38:05Z | sn45 commit touches scoring: AlphaRidge 4.1.0: improved breakthrough event logic; validator fetch … |
| `sn51:scoring_commit:2026-11-12T22:45:41Z` | 51 | SCORING_COMMIT | 2026-11-13T00:38:05Z | sn51 commit touches scoring: Validator: log dockerd's reason when docker rm -fv fails before the c… |
| `sn89:scoring_commit:2026-11-13T00:32:51Z` | 89 | SCORING_COMMIT | 2026-11-13T00:38:05Z | sn89 commit touches scoring: Agent books: outside validators pay the agent share without extra setu |
| `sn94:scoring_commit:2026-11-12T22:42:15Z` | 94 | SCORING_COMMIT | 2026-11-13T00:38:05Z | sn94 commit touches scoring: Fetch archived hotel bindings when verifying old receipts (AB#381) (#… |
| `sn127:release:Release ba66e7b` | 127 | RELEASE | 2026-11-13T00:38:05Z | sn127 released Release ba66e7b |
| `sn127:scoring_commit:2026-11-12T23:33:10Z` | 127 | SCORING_COMMIT | 2026-11-13T00:38:05Z | sn127 commit touches scoring: Docs: what the soup round bank holds and why scores move when it chan… |
| `sn28:readme_task_diff:3988d29ccf7e7016` | 28 | README_TASK_DIFF | 2026-11-06T20:59:00Z | sn28 README task/scoring sections changed |
| `sn88:readme_task_diff:b0837afa350cd1d5` | 88 | README_TASK_DIFF | 2026-11-06T20:59:00Z | sn88 README task/scoring sections changed |
| `sn37:readme_task_diff:0ff79d9d6b17ca0c` | 37 | README_TASK_DIFF | 2026-11-07T07:02:35Z | sn37 README task/scoring sections changed |
| `sn15:readme_task_diff:4d00db5f525b3425` | 15 | README_TASK_DIFF | 2026-11-07T18:42:57Z | sn15 README task/scoring sections changed |
| `sn90:readme_task_diff:ddf545eb7067fc3b` | 90 | README_TASK_DIFF | 2026-11-08T19:38:31Z | sn90 README task/scoring sections changed |
| `sn15:readme_task_diff:cf22c88e3fbbce23` | 15 | README_TASK_DIFF | 2026-11-09T11:22:14Z | sn15 README task/scoring sections changed |
| `sn117:readme_task_diff:833c1d2c18a944b2` | 117 | README_TASK_DIFF | 2026-11-09T21:33:03Z | sn117 README task/scoring sections changed |
| `sn70:readme_task_diff:7e6dcc00df19b743` | 70 | README_TASK_DIFF | 2026-11-10T03:50:58Z | sn70 README task/scoring sections changed |
| `sn127:readme_task_diff:1fb144e0f2f9b150` | 127 | README_TASK_DIFF | 2026-11-10T03:50:58Z | sn127 README task/scoring sections changed |
| `sn117:readme_task_diff:5e2cfc5911b6cfb7` | 117 | README_TASK_DIFF | 2026-11-10T20:02:20Z | sn117 README task/scoring sections changed |
| `sn124:readme_task_diff:ed4d53fe1d12dcb7` | 124 | README_TASK_DIFF | 2026-11-10T20:02:20Z | sn124 README task/scoring sections changed |
| `sn81:readme_task_diff:fd4904bbf0014ce9` | 81 | README_TASK_DIFF | 2026-11-11T07:14:22Z | sn81 README task/scoring sections changed |
| `sn25:readme_task_diff:ddb036629e685ec6` | 25 | README_TASK_DIFF | 2026-11-12T03:14:04Z | sn25 README task/scoring sections changed |
| `sn38:readme_task_diff:4acf9ce9cf638fa6` | 38 | README_TASK_DIFF | 2026-11-12T11:38:51Z | sn38 README task/scoring sections changed |
| `sn94:readme_task_diff:6bfe892e700f0a93` | 94 | README_TASK_DIFF | 2026-11-12T19:10:23Z | sn94 README task/scoring sections changed |

## RESOLVED IN THIS WINDOW

_none_
