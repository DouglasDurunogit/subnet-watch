# ALARMS - generated 2026-11-11T22:18:24Z, block 9485979

window: first_seen in [2026-11-11T21:03:50Z, 2026-11-11T22:18:50Z)  (60 min interval + 15 min overlap)

Report ONLY the rows under NEW SINCE LAST RUN. Rows under STILL OPEN were
already reported in an earlier window and must not be re-alarmed.

## NEW SINCE LAST RUN

| event_id | netuid | class | severity | first_seen_utc | one_line |
|---|---|---|---|---|---|
| `sn126:burn_drop:0.952` | 126 | BURN_DROP | P0 | 2026-11-11T22:18:50Z | sn126 burn fell 1.000 -> 0.952 - miners can earn again |
| `sn8:scoring_commit:2026-11-11T22:14:38Z` | 8 | SCORING_COMMIT | P1 | 2026-11-11T22:18:50Z | sn8 commit touches scoring: New regular miners (#975) |
| `sn12:release:validator-staging-2026-11-11-43092055737` | 12 | RELEASE | P1 | 2026-11-11T22:18:50Z | sn12 released validator-staging-2026-11-11-43092055737-629-1: fix: upgrade vulnerable dependencies across subprojects (#864) |
| `sn17:scoring_commit:2026-11-11T21:55:09Z` | 17 | SCORING_COMMIT | P1 | 2026-11-11T22:18:50Z | sn17 commit touches scoring: Publish verdicts and launch the next validation Pod in one poll (#113) |
| `sn45:scoring_commit:2026-11-11T22:09:58Z` | 45 | SCORING_COMMIT | P1 | 2026-11-11T22:18:50Z | sn45 commit touches scoring: AlphaRidge 4.0.3: validator watchdog; the reference miner no longer p… |
| `sn51:release:watchtower-v1.2.3` | 51 | RELEASE | P1 | 2026-11-11T22:18:50Z | sn51 released watchtower-v1.2.3 |
| `sn51:scoring_commit:2026-11-11T16:03:30Z` | 51 | SCORING_COMMIT | P1 | 2026-11-11T22:18:50Z | sn51 commit touches scoring: DAH-6169 - Validator signs the whole request on every backend call (#… |
| `sn91:scoring_commit:2026-11-11T19:55:46Z` | 91 | SCORING_COMMIT | P1 | 2026-11-11T22:18:50Z | sn91 commit touches scoring: feat(validator): elastic bench host — rent the DEC-CA-0063 sweep pod … |
| `sn111:release:v2.0.0` | 111 | RELEASE | P1 | 2026-11-11T22:18:50Z | sn111 released v2.0.0 |
| `sn111:scoring_commit:2026-11-11T17:38:31Z` | 111 | SCORING_COMMIT | P1 | 2026-11-11T22:18:50Z | sn111 commit touches scoring: Allocate competition weights to miners and normalize legacy carry |
| `sn127:release:Release f9174a9` | 127 | RELEASE | P1 | 2026-11-11T22:18:50Z | sn127 released Release f9174a9 |

### detail

- **`sn126:burn_drop:0.952`** - sn126 burn fell 1.000 -> 0.952 - miners can earn again
  - This subnet paid miners nothing and now pays. Worth a look before the field fills up.
- **`sn8:scoring_commit:2026-11-11T22:14:38Z`** - sn8 commit touches scoring: New regular miners (#975)
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn12:release:validator-staging-2026-11-11-43092055737`** - sn12 released validator-staging-2026-11-11-43092055737-629-1: fix: upgrade vulnerable dependencies across subprojects (#864)
  - published 2026-11-11T19:55:36Z (was miner-staging-2026-11-10-42883644919-432-1: feat: upgrade facilitator from ubuntu 20 to 26 (#862))
- **`sn17:scoring_commit:2026-11-11T21:55:09Z`** - sn17 commit touches scoring: Publish verdicts and launch the next validation Pod in one poll (#113)
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn45:scoring_commit:2026-11-11T22:09:58Z`** - sn45 commit touches scoring: AlphaRidge 4.0.3: validator watchdog; the reference miner no longer p…
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn51:release:watchtower-v1.2.3`** - sn51 released watchtower-v1.2.3
  - published 2026-11-11T14:05:59Z (was watchtower-v1.2.2: DAH-5053: lium-watchtower 1.2.2, the first amd64+arm64 build)
- **`sn51:scoring_commit:2026-11-11T16:03:30Z`** - sn51 commit touches scoring: DAH-6169 - Validator signs the whole request on every backend call (#…
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn91:scoring_commit:2026-11-11T19:55:46Z`** - sn91 commit touches scoring: feat(validator): elastic bench host — rent the DEC-CA-0063 sweep pod …
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn111:release:v2.0.0`** - sn111 released v2.0.0
  - published 2026-11-11T17:16:45Z (was v1.1.0)
- **`sn111:scoring_commit:2026-11-11T17:38:31Z`** - sn111 commit touches scoring: Allocate competition weights to miners and normalize legacy carry
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn127:release:Release f9174a9`** - sn127 released Release f9174a9
  - published 2026-11-11T16:49:54Z (was Release ed8326b)

## STILL OPEN (already reported - do not re-alarm)

| event_id | netuid | class | first_seen_utc | one_line |
|---|---|---|---|---|
| `sn126:burn_drop:0.955` | 126 | BURN_DROP | 2026-11-05T03:46:12Z | sn126 burn fell 1.000 -> 0.955 - miners can earn again |
| `sn127:burn_drop:0.872` | 127 | BURN_DROP | 2026-11-05T11:38:32Z | sn127 burn fell 0.990 -> 0.872 - miners can earn again |
| `sn81:burn_drop:0.965` | 81 | BURN_DROP | 2026-11-05T19:03:37Z | sn81 burn fell 0.999 -> 0.965 - miners can earn again |
| `sn121:burn_drop:0.602` | 121 | BURN_DROP | 2026-11-05T19:03:37Z | sn121 burn fell 1.000 -> 0.602 - miners can earn again |
| `sn76:burn_drop:0.973` | 76 | BURN_DROP | 2026-11-06T00:09:29Z | sn76 burn fell 0.990 -> 0.973 - miners can earn again |
| `sn37:burn_drop:0.091` | 37 | BURN_DROP | 2026-11-07T07:02:35Z | sn37 burn fell 1.000 -> 0.091 - miners can earn again |
| `sn76:burn_drop:0.984` | 76 | BURN_DROP | 2026-11-08T01:42:10Z | sn76 burn fell 0.992 -> 0.984 - miners can earn again |
| `sn126:burn_drop:0.985` | 126 | BURN_DROP | 2026-11-08T01:42:10Z | sn126 burn fell 1.000 -> 0.985 - miners can earn again |
| `sn76:burn_drop:0.985` | 76 | BURN_DROP | 2026-11-08T19:38:31Z | sn76 burn fell 0.996 -> 0.985 - miners can earn again |
| `sn121:burn_drop:0.646` | 121 | BURN_DROP | 2026-11-09T21:33:03Z | sn121 burn fell 1.000 -> 0.646 - miners can earn again |
| `sn127:burn_drop:0.960` | 127 | BURN_DROP | 2026-11-09T21:33:03Z | sn127 burn fell 1.000 -> 0.960 - miners can earn again |
| `sn108:burn_drop:0.823` | 108 | BURN_DROP | 2026-11-11T07:14:22Z | sn108 burn fell 1.000 -> 0.823 - miners can earn again |
| `sn76:burn_drop:0.983` | 76 | BURN_DROP | 2026-11-11T15:30:25Z | sn76 burn fell 0.995 -> 0.983 - miners can earn again |
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
| `sn58:readme_task_diff:3b8b49ad2ebb4e84` | 58 | README_TASK_DIFF | 2026-11-04T23:36:57Z | sn58 README task/scoring sections changed |
| `sn51:readme_task_diff:77525fe4e41362db` | 51 | README_TASK_DIFF | 2026-11-05T11:38:32Z | sn51 README task/scoring sections changed |
| `sn58:readme_task_diff:de3e9164e32563c5` | 58 | README_TASK_DIFF | 2026-11-05T19:03:37Z | sn58 README task/scoring sections changed |
| `sn123:readme_task_diff:855cbeee88da3234` | 123 | README_TASK_DIFF | 2026-11-06T07:08:56Z | sn123 README task/scoring sections changed |
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

## RESOLVED IN THIS WINDOW

_none_
