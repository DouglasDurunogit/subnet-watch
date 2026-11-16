# ALARMS - generated 2026-11-16T16:14:28Z, block 9520160

window: first_seen in [2026-11-16T14:59:51Z, 2026-11-16T16:14:51Z)  (60 min interval + 15 min overlap)

Report ONLY the rows under NEW SINCE LAST RUN. Rows under STILL OPEN were
already reported in an earlier window and must not be re-alarmed.

## NEW SINCE LAST RUN

| event_id | netuid | class | severity | first_seen_utc | one_line |
|---|---|---|---|---|---|
| `sn3:scoring_commit:2026-11-16T11:37:13Z` | 3 | SCORING_COMMIT | P1 | 2026-11-16T16:14:51Z | sn3 commit touches scoring: Stream Horizon scoring during packed-text sampling |
| `sn25:release:v2026.11.16-1100273030` | 25 | RELEASE | P1 | 2026-11-16T16:14:51Z | sn25 released v2026.11.16-1100273030 |
| `sn25:scoring_commit:2026-11-16T06:53:36Z` | 25 | SCORING_COMMIT | P1 | 2026-11-16T16:14:51Z | sn25 commit touches scoring: Merge fix/validator-nonce-wait-1116: the validator waits out the weig… |
| `sn42:release:v0.6.18` | 42 | RELEASE | P1 | 2026-11-16T16:14:51Z | sn42 released v0.6.18 |
| `sn42:scoring_commit:2026-11-16T08:59:35Z` | 42 | SCORING_COMMIT | P1 | 2026-11-16T16:14:51Z | sn42 commit touches scoring: reference miner: a brief that asks for nothing physical is rejected n… |
| `sn51:release:executor-v1.184` | 51 | RELEASE | P1 | 2026-11-16T16:14:51Z | sn51 released executor-v1.184 |
| `sn51:scoring_commit:2026-11-16T15:55:07Z` | 51 | SCORING_COMMIT | P1 | 2026-11-16T16:14:51Z | sn51 commit touches scoring: Validator: quote executor-reported paths in shell commands (#2280) |
| `sn67:scoring_commit:2026-11-16T10:09:40Z` | 67 | SCORING_COMMIT | P1 | 2026-11-16T16:14:51Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20261116.post8 |
| `sn71:scoring_commit:2026-11-16T11:03:00Z` | 71 | SCORING_COMMIT | P1 | 2026-11-16T16:14:51Z | sn71 commit touches scoring: Assert exact judgment binding in score projection tests |
| `sn111:scoring_commit:2026-11-16T12:01:40Z` | 111 | SCORING_COMMIT | P1 | 2026-11-16T16:14:51Z | sn111 commit touches scoring: Verify carried-forward scoring revisions during production handoff |
| `sn42:readme_task_diff:dd8a6fb083469151` | 42 | README_TASK_DIFF | P2 | 2026-11-16T16:14:51Z | sn42 README task/scoring sections changed |

### detail

- **`sn3:scoring_commit:2026-11-16T11:37:13Z`** - sn3 commit touches scoring: Stream Horizon scoring during packed-text sampling
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn25:release:v2026.11.16-1100273030`** - sn25 released v2026.11.16-1100273030
  - published 2026-11-16T11:18:23Z (was v2026.11.15-1100072900)
- **`sn25:scoring_commit:2026-11-16T06:53:36Z`** - sn25 commit touches scoring: Merge fix/validator-nonce-wait-1116: the validator waits out the weig…
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn42:release:v0.6.18`** - sn42 released v0.6.18
  - published 2026-11-16T09:17:57Z (was v0.6.16)
- **`sn42:scoring_commit:2026-11-16T08:59:35Z`** - sn42 commit touches scoring: reference miner: a brief that asks for nothing physical is rejected n…
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn51:release:executor-v1.184`** - sn51 released executor-v1.184
  - published 2026-11-16T08:33:17Z (was executor-v1.182)
- **`sn51:scoring_commit:2026-11-16T15:55:07Z`** - sn51 commit touches scoring: Validator: quote executor-reported paths in shell commands (#2280)
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn67:scoring_commit:2026-11-16T10:09:40Z`** - sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20261116.post8
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn71:scoring_commit:2026-11-16T11:03:00Z`** - sn71 commit touches scoring: Assert exact judgment binding in score projection tests
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn111:scoring_commit:2026-11-16T12:01:40Z`** - sn111 commit touches scoring: Verify carried-forward scoring revisions during production handoff
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn42:readme_task_diff:dd8a6fb083469151`** - sn42 README task/scoring sections changed
  - Only the task-describing headings are hashed, so badge and typo edits do not trigger this.

## STILL OPEN (already reported - do not re-alarm)

| event_id | netuid | class | first_seen_utc | one_line |
|---|---|---|---|---|
| `sn121:burn_drop:0.646` | 121 | BURN_DROP | 2026-11-09T21:33:03Z | sn121 burn fell 1.000 -> 0.646 - miners can earn again |
| `sn127:burn_drop:0.960` | 127 | BURN_DROP | 2026-11-09T21:33:03Z | sn127 burn fell 1.000 -> 0.960 - miners can earn again |
| `sn108:burn_drop:0.823` | 108 | BURN_DROP | 2026-11-11T07:14:22Z | sn108 burn fell 1.000 -> 0.823 - miners can earn again |
| `sn76:burn_drop:0.983` | 76 | BURN_DROP | 2026-11-11T15:30:25Z | sn76 burn fell 0.995 -> 0.983 - miners can earn again |
| `sn126:burn_drop:0.952` | 126 | BURN_DROP | 2026-11-11T22:18:50Z | sn126 burn fell 1.000 -> 0.952 - miners can earn again |
| `sn94:burn_drop:0.000` | 94 | BURN_DROP | 2026-11-12T03:14:04Z | sn94 burn fell 1.000 -> 0.000 - miners can earn again |
| `sn42:burn_drop:0.000` | 42 | BURN_DROP | 2026-11-13T00:38:05Z | sn42 burn fell 1.000 -> 0.000 - miners can earn again |
| `sn10:burn_drop:0.607` | 10 | BURN_DROP | 2026-11-13T15:34:59Z | sn10 burn fell 1.000 -> 0.607 - miners can earn again |
| `sn108:burn_drop:0.800` | 108 | BURN_DROP | 2026-11-14T08:55:08Z | sn108 burn fell 1.000 -> 0.800 - miners can earn again |
| `sn116:burn_drop:0.750` | 116 | BURN_DROP | 2026-11-14T20:09:45Z | sn116 burn fell 1.000 -> 0.750 - miners can earn again |
| `sn76:burn_drop:0.975` | 76 | BURN_DROP | 2026-11-15T06:17:56Z | sn76 burn fell 1.000 -> 0.975 - miners can earn again |
| `sn106:burn_drop:0.000` | 106 | BURN_DROP | 2026-11-15T19:53:52Z | sn106 burn fell 1.000 -> 0.000 - miners can earn again |
| `sn26:burn_drop:0.000` | 26 | BURN_DROP | 2026-11-15T23:57:01Z | sn26 burn fell 1.000 -> 0.000 - miners can earn again |
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
| `sn45:scoring_commit:2026-11-13T03:38:27Z` | 45 | SCORING_COMMIT | 2026-11-13T07:23:28Z | sn45 commit touches scoring: AlphaRidge 4.1.1: validator stability |
| `sn51:scoring_commit:2026-11-13T04:01:45Z` | 51 | SCORING_COMMIT | 2026-11-13T07:23:28Z | sn51 commit touches scoring: DAH-6325 - [P0] Validator FIXED_RATIO follows the 50% miner emission … |
| `sn81:scoring_commit:2026-11-13T04:22:44Z` | 81 | SCORING_COMMIT | 2026-11-13T07:23:28Z | sn81 commit touches scoring: fix(admin): keep a job's counts for good only once its tasks are reti… |
| `sn127:release:Release 3e2660e` | 127 | RELEASE | 2026-11-13T07:23:28Z | sn127 released Release 3e2660e |
| `sn3:scoring_commit:2026-11-13T12:59:12Z` | 3 | SCORING_COMMIT | 2026-11-13T15:34:59Z | sn3 commit touches scoring: Update Horizon scoring, set 60M budgets and live evaluation progress |
| `sn25:release:v2026.11.13-1097815580` | 25 | RELEASE | 2026-11-13T15:34:59Z | sn25 released v2026.11.13-1097815580 |
| `sn42:release:v0.6.9` | 42 | RELEASE | 2026-11-13T15:34:59Z | sn42 released v0.6.9 |
| `sn42:scoring_commit:2026-11-13T13:19:19Z` | 42 | SCORING_COMMIT | 2026-11-13T15:34:59Z | sn42 commit touches scoring: v0.6.8: the operator can take a client job back from a miner that can… |
| `sn51:release:executor-v1.182` | 51 | RELEASE | 2026-11-13T15:34:59Z | sn51 released executor-v1.182 |
| `sn51:scoring_commit:2026-11-13T15:34:45Z` | 51 | SCORING_COMMIT | 2026-11-13T15:34:59Z | sn51 commit touches scoring: DAH-6381 - [P1] Validator: an ownership shift after a container-only … |
| `sn56:scoring_commit:2026-11-13T10:48:42Z` | 56 | SCORING_COMMIT | 2026-11-13T15:34:59Z | sn56 commit touches scoring: Add next image families and native-loss evaluation (#1420) |
| `sn69:scoring_commit:2026-11-13T02:45:24Z` | 69 | SCORING_COMMIT | 2026-11-13T15:34:59Z | sn69 commit touches scoring: Port the validator to bittensor 11.3.2 |
| `sn71:scoring_commit:2026-11-13T09:58:30Z` | 71 | SCORING_COMMIT | 2026-11-13T15:34:59Z | sn71 commit touches scoring: Record deployed Arena migration access and verified recovery evidence |
| `sn81:scoring_commit:2026-11-13T11:36:18Z` | 81 | SCORING_COMMIT | 2026-11-13T15:34:59Z | sn81 commit touches scoring: docs(design): Terminal-Bench 2.1 gold check results (49/89 verified o… |
| `sn111:scoring_commit:2026-11-13T10:53:58Z` | 111 | SCORING_COMMIT | 2026-11-13T15:34:59Z | sn111 commit touches scoring: Document Silver data in evaluation exports |
| `sn116:scoring_commit:2026-11-13T04:13:13Z` | 116 | SCORING_COMMIT | 2026-11-13T15:34:59Z | sn116 commit touches scoring: Grading paths: classify task_wall_overrides.py (Runner-C gate on 669a… |
| `sn117:release:everycli v1.2.1` | 117 | RELEASE | 2026-11-13T15:34:59Z | sn117 released everycli v1.2.1 |
| `sn25:release:v2026.11.13-1097983310` | 25 | RELEASE | 2026-11-13T21:41:00Z | sn25 released v2026.11.13-1097983310 |
| `sn45:scoring_commit:2026-11-13T17:26:43Z` | 45 | SCORING_COMMIT | 2026-11-13T21:41:00Z | sn45 commit touches scoring: AlphaRidge 4.1.2: re-verify reads a republished page at its original … |
| `sn66:release:v2026.11.13` | 66 | RELEASE | 2026-11-13T21:41:00Z | sn66 released v2026.11.13 |
| `sn71:scoring_commit:2026-11-13T15:37:43Z` | 71 | SCORING_COMMIT | 2026-11-13T21:41:00Z | sn71 commit touches scoring: Preserve verified research pairs when judge input capture is unavaila… |
| `sn117:release:everycli v1.2.2` | 117 | RELEASE | 2026-11-13T21:41:00Z | sn117 released everycli v1.2.2 |
| `sn5:scoring_commit:2026-11-14T00:45:57Z` | 5 | SCORING_COMMIT | 2026-11-14T01:52:12Z | sn5 commit touches scoring: Lengthen the new-miner ramp to 30 observations |
| `sn8:scoring_commit:2026-11-13T23:26:20Z` | 8 | SCORING_COMMIT | 2026-11-14T01:52:12Z | sn8 commit touches scoring: Put new regular miners on the static drawdown rules until Grow (#979) |
| `sn42:release:v0.6.11` | 42 | RELEASE | 2026-11-14T01:52:12Z | sn42 released v0.6.11 |
| `sn66:release:v2026.11.13.2` | 66 | RELEASE | 2026-11-14T01:52:12Z | sn66 released v2026.11.13.2 |
| `sn71:scoring_commit:2026-11-13T23:56:56Z` | 71 | SCORING_COMMIT | 2026-11-14T01:52:12Z | sn71 commit touches scoring: Expect mandatory reward history reader in bounded schema fixture |
| `sn116:scoring_commit:2026-11-13T20:28:33Z` | 116 | SCORING_COMMIT | 2026-11-14T01:52:12Z | sn116 commit touches scoring: Test: the in-range case rows add no score, gate or target pool row (s… |
| `sn25:scoring_commit:2026-11-14T05:29:09Z` | 25 | SCORING_COMMIT | 2026-11-14T08:55:08Z | sn25 commit touches scoring: Merge release/validator-1114-idle-fleet: the validator build 47ae3006… |
| `sn94:scoring_commit:2026-11-14T07:44:30Z` | 94 | SCORING_COMMIT | 2026-11-14T08:55:08Z | sn94 commit touches scoring: Admit miner hotels on a declared capacity commitment (AB#331) (#498) |
| `sn116:scoring_commit:2026-11-14T05:27:45Z` | 116 | SCORING_COMMIT | 2026-11-14T08:55:08Z | sn116 commit touches scoring: Re-class: replace the miner-facing marker atomically so the miner sto… |
| `sn25:release:v2026.11.14-1098667430` | 25 | RELEASE | 2026-11-14T15:45:22Z | sn25 released v2026.11.14-1098667430 |
| `sn25:scoring_commit:2026-11-14T08:11:19Z` | 25 | SCORING_COMMIT | 2026-11-14T15:45:22Z | sn25 commit touches scoring: Merge fix/validator-attempt-upload-lane-retry: retry a reserved uploa… |
| `sn42:release:v0.6.13` | 42 | RELEASE | 2026-11-14T15:45:22Z | sn42 released v0.6.13 |
| `sn42:scoring_commit:2026-11-14T09:11:27Z` | 42 | SCORING_COMMIT | 2026-11-14T15:45:22Z | sn42 commit touches scoring: tests: stub the agent CLI checks where the miner's main loop runs (CI… |
| `sn53:scoring_commit:2026-11-09T17:49:36Z` | 53 | SCORING_COMMIT | 2026-11-14T15:45:22Z | sn53 commit touches scoring: tee_miner: forward reported cache write tokens |
| `sn56:scoring_commit:2026-11-14T11:11:50Z` | 56 | SCORING_COMMIT | 2026-11-14T15:45:22Z | sn56 commit touches scoring: Bind subnet API publicly and add task subnet-api (#1415) |
| `sn81:scoring_commit:2026-11-14T13:11:48Z` | 81 | SCORING_COMMIT | 2026-11-14T15:45:22Z | sn81 commit touches scoring: fix(miner): stop agentic children gracefully and never charge our fai… |
| `sn94:scoring_commit:2026-11-14T09:11:23Z` | 94 | SCORING_COMMIT | 2026-11-14T15:45:22Z | sn94 commit touches scoring: Alert the miner operator on a first missed heartbeat and ops on a cus… |
| `sn42:release:v0.6.15` | 42 | RELEASE | 2026-11-14T20:09:45Z | sn42 released v0.6.15 |
| `sn42:scoring_commit:2026-11-14T17:22:34Z` | 42 | SCORING_COMMIT | 2026-11-14T20:09:45Z | sn42 commit touches scoring: v0.6.15: the reference miner hands a finished job in when the agent C… |
| `sn116:scoring_commit:2026-11-14T14:36:51Z` | 116 | SCORING_COMMIT | 2026-11-14T20:09:45Z | sn116 commit touches scoring: Tests: a serve stop leaves a queued task QUEUED (queue-carry), not CA… |
| `sn71:scoring_commit:2026-11-14T23:29:40Z` | 71 | SCORING_COMMIT | 2026-11-15T00:02:49Z | sn71 commit touches scoring: Merge pull request #1240 from leadpoet/fix/miner-responses-output-cit… |
| `sn116:scoring_commit:2026-11-14T22:09:09Z` | 116 | SCORING_COMMIT | 2026-11-15T00:02:49Z | sn116 commit touches scoring: Queue place: a resubmission of a stop-cancelled task's recipe takes t… |
| `sn116:scoring_commit:2026-11-15T05:04:28Z` | 116 | SCORING_COMMIT | 2026-11-15T06:17:56Z | sn116 commit touches scoring: Merge pull request #1433: Dashboard on every page, miner CTA to the d… |
| `sn117:release:everycli v1.2.3` | 117 | RELEASE | 2026-11-15T06:17:56Z | sn117 released everycli v1.2.3 |
| `sn15:scoring_commit:2026-11-15T08:45:01Z` | 15 | SCORING_COMMIT | 2026-11-15T14:11:53Z | sn15 commit touches scoring: chore: remove dead load_episode_artifact from validator (#398) |
| `sn25:release:v2026.11.15-1099387180` | 25 | RELEASE | 2026-11-15T14:11:53Z | sn25 released v2026.11.15-1099387180 |
| `sn71:scoring_commit:2026-11-15T10:55:38Z` | 71 | SCORING_COMMIT | 2026-11-15T14:11:53Z | sn71 commit touches scoring: Allow measured baselines with capture gaps in verified reward comparis |
| `sn81:scoring_commit:2026-11-15T08:40:29Z` | 81 | SCORING_COMMIT | 2026-11-15T14:11:53Z | sn81 commit touches scoring: fix(miner): install reliquary-terminal so miners serve TMax orders (#… |
| `sn116:scoring_commit:2026-11-15T11:18:25Z` | 116 | SCORING_COMMIT | 2026-11-15T14:11:53Z | sn116 commit touches scoring: Miner kit: check_result says why a try ended as it did |
| `sn25:release:v2026.11.15-1099669220` | 25 | RELEASE | 2026-11-15T19:53:52Z | sn25 released v2026.11.15-1099669220 |
| `sn81:scoring_commit:2026-11-15T18:16:14Z` | 81 | SCORING_COMMIT | 2026-11-15T19:53:52Z | sn81 commit touches scoring: Keep honest batch miners' leases: default time while a batch is out, … |
| `sn116:scoring_commit:2026-11-15T14:46:48Z` | 116 | SCORING_COMMIT | 2026-11-15T19:53:52Z | sn116 commit touches scoring: Withdraw review fixes (kit): a withdrawn task is never the round's ve… |
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
| `sn117:readme_task_diff:833c1d2c18a944b2` | 117 | README_TASK_DIFF | 2026-11-09T21:33:03Z | sn117 README task/scoring sections changed |
| `sn70:readme_task_diff:7e6dcc00df19b743` | 70 | README_TASK_DIFF | 2026-11-10T03:50:58Z | sn70 README task/scoring sections changed |
| `sn127:readme_task_diff:1fb144e0f2f9b150` | 127 | README_TASK_DIFF | 2026-11-10T03:50:58Z | sn127 README task/scoring sections changed |
| `sn117:readme_task_diff:5e2cfc5911b6cfb7` | 117 | README_TASK_DIFF | 2026-11-10T20:02:20Z | sn117 README task/scoring sections changed |
| `sn124:readme_task_diff:ed4d53fe1d12dcb7` | 124 | README_TASK_DIFF | 2026-11-10T20:02:20Z | sn124 README task/scoring sections changed |
| `sn81:readme_task_diff:fd4904bbf0014ce9` | 81 | README_TASK_DIFF | 2026-11-11T07:14:22Z | sn81 README task/scoring sections changed |
| `sn25:readme_task_diff:ddb036629e685ec6` | 25 | README_TASK_DIFF | 2026-11-12T03:14:04Z | sn25 README task/scoring sections changed |
| `sn38:readme_task_diff:4acf9ce9cf638fa6` | 38 | README_TASK_DIFF | 2026-11-12T11:38:51Z | sn38 README task/scoring sections changed |
| `sn94:readme_task_diff:6bfe892e700f0a93` | 94 | README_TASK_DIFF | 2026-11-12T19:10:23Z | sn94 README task/scoring sections changed |
| `sn48:readme_task_diff:ccea6584910d3bd5` | 48 | README_TASK_DIFF | 2026-11-13T07:23:28Z | sn48 README task/scoring sections changed |
| `sn42:readme_task_diff:a31e8e8370c6e8f8` | 42 | README_TASK_DIFF | 2026-11-13T15:34:59Z | sn42 README task/scoring sections changed |
| `sn58:readme_task_diff:e5ddb56c3ad66771` | 58 | README_TASK_DIFF | 2026-11-13T15:34:59Z | sn58 README task/scoring sections changed |
| `sn69:readme_task_diff:55670d0ee7030fca` | 69 | README_TASK_DIFF | 2026-11-13T15:34:59Z | sn69 README task/scoring sections changed |
| `sn42:readme_task_diff:c68c8d6462ab6e33` | 42 | README_TASK_DIFF | 2026-11-14T01:52:12Z | sn42 README task/scoring sections changed |
| `sn90:readme_task_diff:a7b301753d76644f` | 90 | README_TASK_DIFF | 2026-11-15T23:57:01Z | sn90 README task/scoring sections changed |

## RESOLVED IN THIS WINDOW

_none_
