# ALARMS - generated 2026-09-17T22:19:51Z, block 9090321

window: first_seen in [2026-09-17T21:05:24Z, 2026-09-17T22:20:24Z)  (60 min interval + 15 min overlap)

Report ONLY the rows under NEW SINCE LAST RUN. Rows under STILL OPEN were
already reported in an earlier window and must not be re-alarmed.

## NEW SINCE LAST RUN

| event_id | netuid | class | severity | first_seen_utc | one_line |
|---|---|---|---|---|---|
| `sn4:release:v2.0.1` | 4 | RELEASE | P1 | 2026-09-17T22:20:24Z | sn4 released v2.0.1 |
| `sn15:scoring_commit:2026-09-17T21:02:27Z` | 15 | SCORING_COMMIT | P1 | 2026-09-17T22:20:24Z | sn15 commit touches scoring: fix(validator): delete orphaned retry_queue.add_progress on logs_s3_k… |
| `sn25:release:v2026.9.17-1048832810` | 25 | RELEASE | P1 | 2026-09-17T22:20:24Z | sn25 released v2026.9.17-1048832810 |
| `sn69:scoring_commit:2026-09-17T19:29:06Z` | 69 | SCORING_COMMIT | P1 | 2026-09-17T22:20:24Z | sn69 commit touches scoring: Re-submit the latest miner weights on a block cadence |
| `sn74:release:release-20260917-220301` | 74 | RELEASE | P1 | 2026-09-17T22:20:24Z | sn74 released release-20260917-220301 |
| `sn90:scoring_commit:2026-09-17T21:14:03Z` | 90 | SCORING_COMMIT | P1 | 2026-09-17T22:20:24Z | sn90 commit touches scoring: feat(validator): raise minimum node spec to 72 cores / 1024 GiB / 5 n… |
| `sn93:scoring_commit:2026-09-17T21:13:10Z` | 93 | SCORING_COMMIT | P1 | 2026-09-17T22:20:24Z | sn93 commit touches scoring: docs: replace CLAUDE.md with AGENTS.md + on-chain liveness verificati… |
| `sn102:release:v0.6.2` | 102 | RELEASE | P1 | 2026-09-17T22:20:24Z | sn102 released v0.6.2 |
| `sn102:scoring_commit:2026-09-17T17:58:30Z` | 102 | SCORING_COMMIT | P1 | 2026-09-17T22:20:24Z | sn102 commit touches scoring: 🐛 fix(validator): drop evaluations that finish after their round is f… |

### detail

- **`sn4:release:v2.0.1`** - sn4 released v2.0.1
  - published 2026-09-17T18:38:37Z (was v2.0.0)
- **`sn15:scoring_commit:2026-09-17T21:02:27Z`** - sn15 commit touches scoring: fix(validator): delete orphaned retry_queue.add_progress on logs_s3_k…
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn25:release:v2026.9.17-1048832810`** - sn25 released v2026.9.17-1048832810
  - published 2026-09-17T22:19:53Z (was v2026.9.17-1048676710)
- **`sn69:scoring_commit:2026-09-17T19:29:06Z`** - sn69 commit touches scoring: Re-submit the latest miner weights on a block cadence
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn74:release:release-20260917-220301`** - sn74 released release-20260917-220301
  - published 2026-09-17T22:01:55Z (was release-20260917-174533)
- **`sn90:scoring_commit:2026-09-17T21:14:03Z`** - sn90 commit touches scoring: feat(validator): raise minimum node spec to 72 cores / 1024 GiB / 5 n…
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn93:scoring_commit:2026-09-17T21:13:10Z`** - sn93 commit touches scoring: docs: replace CLAUDE.md with AGENTS.md + on-chain liveness verificati…
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn102:release:v0.6.2`** - sn102 released v0.6.2
  - published 2026-09-17T21:00:03Z (was v0.6.1)
- **`sn102:scoring_commit:2026-09-17T17:58:30Z`** - sn102 commit touches scoring: 🐛 fix(validator): drop evaluations that finish after their round is f…
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.

## STILL OPEN (already reported - do not re-alarm)

| event_id | netuid | class | first_seen_utc | one_line |
|---|---|---|---|---|
| `sn20:burn_drop:0.770` | 20 | BURN_DROP | 2026-09-11T01:19:31Z | sn20 burn fell 1.000 -> 0.770 - miners can earn again |
| `sn20:burn_drop:0.742` | 20 | BURN_DROP | 2026-09-12T06:24:23Z | sn20 burn fell 1.000 -> 0.742 - miners can earn again |
| `sn125:burn_drop:0.000` | 125 | BURN_DROP | 2026-09-13T19:00:00Z | sn125 burn fell 1.000 -> 0.000 - miners can earn again |
| `sn47:burn_drop:0.000` | 47 | BURN_DROP | 2026-09-13T21:25:03Z | sn47 burn fell 1.000 -> 0.000 - miners can earn again |
| `sn99:burn_drop:0.150` | 99 | BURN_DROP | 2026-09-13T21:25:03Z | sn99 burn fell 1.000 -> 0.150 - miners can earn again |
| `sn69:burn_drop:0.000` | 69 | BURN_DROP | 2026-09-14T13:23:56Z | sn69 burn fell 1.000 -> 0.000 - miners can earn again |
| `sn20:burn_drop:0.793` | 20 | BURN_DROP | 2026-09-15T06:08:06Z | sn20 burn fell 1.000 -> 0.793 - miners can earn again |
| `sn36:burn_drop:0.951` | 36 | BURN_DROP | 2026-09-16T06:23:31Z | sn36 burn fell 1.000 -> 0.951 - miners can earn again |
| `sn20:burn_drop:0.754` | 20 | BURN_DROP | 2026-09-16T16:47:34Z | sn20 burn fell 1.000 -> 0.754 - miners can earn again |
| `sn10:burn_drop:0.811` | 10 | BURN_DROP | 2026-09-17T06:06:18Z | sn10 burn fell 1.000 -> 0.811 - miners can earn again |
| `sn15:burn_drop:0.000` | 15 | BURN_DROP | 2026-09-17T11:36:55Z | sn15 burn fell 0.997 -> 0.000 - miners can earn again |
| `sn15:release:v2.0.3` | 15 | RELEASE | 2026-09-10T23:19:16Z | sn15 released v2.0.3 |
| `sn15:scoring_commit:2026-09-10T22:57:44Z` | 15 | SCORING_COMMIT | 2026-09-10T23:19:16Z | sn15 commit touches scoring: fix(validator): retry SimulatorCompletion inference before env_error … |
| `sn20:scoring_commit:2026-09-10T21:24:32Z` | 20 | SCORING_COMMIT | 2026-09-10T23:19:16Z | sn20 commit touches scoring: Smooth mainnet rewards over configurable round history |
| `sn62:release:v0.3.4` | 62 | RELEASE | 2026-09-10T23:19:16Z | sn62 released v0.3.4 |
| `sn78:scoring_commit:2026-09-10T21:24:05Z` | 78 | SCORING_COMMIT | 2026-09-10T23:19:16Z | sn78 commit touches scoring: Ship shared SN78 validator bootstrap supervisor |
| `sn100:scoring_commit:2026-09-10T21:47:23Z` | 100 | SCORING_COMMIT | 2026-09-10T23:19:16Z | sn100 commit touches scoring: docs(miner): minimal tbench Agent constructor+run example (#275) |
| `sn36:scoring_commit:2026-09-10T20:24:55Z` | 36 | SCORING_COMMIT | 2026-09-11T01:19:31Z | sn36 commit touches scoring: Fix the private-upload commands in the miner guide and CLI hints |
| `sn71:scoring_commit:2026-09-11T01:07:36Z` | 71 | SCORING_COMMIT | 2026-09-11T01:19:31Z | sn71 commit touches scoring: Keep testnet Arena setup aligned with validator authorization |
| `sn100:scoring_commit:2026-09-11T00:30:47Z` | 100 | SCORING_COMMIT | 2026-09-11T01:19:31Z | sn100 commit touches scoring: fix(proof): harvest scored runs when vsock drops done (#278) |
| `sn7:release:release-20260911-013831` | 7 | RELEASE | 2026-09-11T06:22:30Z | sn7 released release-20260911-013831 |
| `sn7:scoring_commit:2026-09-11T01:08:48Z` | 7 | SCORING_COMMIT | 2026-09-11T06:22:30Z | sn7 commit touches scoring: Miner wizard: funding step, one shared EVM key, container check after… |
| `sn15:release:v2.0.4` | 15 | RELEASE | 2026-09-11T06:22:30Z | sn15 released v2.0.4 |
| `sn25:scoring_commit:2026-09-11T06:17:33Z` | 25 | SCORING_COMMIT | 2026-09-11T06:22:30Z | sn25 commit touches scoring: Honor transition limits for typed validator evidence |
| `sn51:scoring_commit:2026-09-11T06:10:30Z` | 51 | SCORING_COMMIT | 2026-09-11T06:22:30Z | sn51 commit touches scoring: DAH-3019 - [P1] validator reports verification start once per miner (… |
| `sn53:scoring_commit:2026-09-11T03:07:35Z` | 53 | SCORING_COMMIT | 2026-09-11T06:22:30Z | sn53 commit touches scoring: Merge pull request #47 from hanlinai/fix/engy-miner-length-finish-reas |
| `sn67:scoring_commit:2026-09-10T08:37:01Z` | 67 | SCORING_COMMIT | 2026-09-11T06:22:30Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20260910.post4 |
| `sn71:scoring_commit:2026-09-11T05:58:19Z` | 71 | SCORING_COMMIT | 2026-09-11T06:22:30Z | sn71 commit touches scoring: Fix normal validator dependency and distribution packaging |
| `sn78:scoring_commit:2026-09-11T05:47:10Z` | 78 | SCORING_COMMIT | 2026-09-11T06:22:30Z | sn78 commit touches scoring: Harden validator supervisor container startup |
| `sn100:scoring_commit:2026-09-11T04:22:33Z` | 100 | SCORING_COMMIT | 2026-09-11T06:22:30Z | sn100 commit touches scoring: fix(proof): retain failed experiment vms for rca + log evaluate refus… |
| `sn10:scoring_commit:2026-09-10T11:52:15Z` | 10 | SCORING_COMMIT | 2026-09-11T11:40:27Z | sn10 commit touches scoring: fix(ops): verify staged units against the live filesystem, record vec… |
| `sn20:scoring_commit:2026-09-11T09:44:50Z` | 20 | SCORING_COMMIT | 2026-09-11T11:40:27Z | sn20 commit touches scoring: Add scorer v1.1.0 and signed round feedback |
| `sn25:scoring_commit:2026-09-11T11:24:07Z` | 25 | SCORING_COMMIT | 2026-09-11T11:40:27Z | sn25 commit touches scoring: Resume provisional validators from completed local recovery and publi… |
| `sn51:release:miner-v1.004` | 51 | RELEASE | 2026-09-11T11:40:27Z | sn51 released miner-v1.004 |
| `sn51:scoring_commit:2026-09-11T10:27:24Z` | 51 | SCORING_COMMIT | 2026-09-11T11:40:27Z | sn51 commit touches scoring: DAH-3206 - [P2] miner accepts a validator sign-in only when it names … |
| `sn67:scoring_commit:2026-09-11T06:52:54Z` | 67 | SCORING_COMMIT | 2026-09-11T11:40:27Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20260911.post0 |
| `sn71:scoring_commit:2026-09-11T08:20:53Z` | 71 | SCORING_COMMIT | 2026-09-11T11:40:27Z | sn71 commit touches scoring: Remove unused validator V2 release metadata and archives |
| `sn78:scoring_commit:2026-09-11T10:40:20Z` | 78 | SCORING_COMMIT | 2026-09-11T11:40:27Z | sn78 commit touches scoring: Make main installer select signed validator release |
| `sn9:release:v4.12.18` | 9 | RELEASE | 2026-09-11T15:15:26Z | sn9 released v4.12.18 |
| `sn55:scoring_commit:2026-09-11T13:39:56Z` | 55 | SCORING_COMMIT | 2026-09-11T15:15:26Z | sn55 commit touches scoring: upload all miners submissions |
| `sn66:scoring_commit:2026-09-11T14:50:25Z` | 66 | SCORING_COMMIT | 2026-09-11T15:15:26Z | sn66 commit touches scoring: Merge pull request #90 from conjectures-io/fix/optional-discord-and-p… |
| `sn71:scoring_commit:2026-09-11T14:34:48Z` | 71 | SCORING_COMMIT | 2026-09-11T15:15:26Z | sn71 commit touches scoring: Fix normal validator startup defaults and local RPC selection |
| `sn78:scoring_commit:2026-09-11T14:41:35Z` | 78 | SCORING_COMMIT | 2026-09-11T15:15:26Z | sn78 commit touches scoring: Clarify miner keepalive requirements during bootstrap |
| `sn100:scoring_commit:2026-09-11T14:04:31Z` | 100 | SCORING_COMMIT | 2026-09-11T15:15:26Z | sn100 commit touches scoring: fix(proof): bind keyword-only miner setup |
| `sn108:scoring_commit:2026-09-11T14:24:07Z` | 108 | SCORING_COMMIT | 2026-09-11T15:15:26Z | sn108 commit touches scoring: feat(validator): a mirror that fell behind catches up on its next re-… |
| `sn15:release:v2.0.6` | 15 | RELEASE | 2026-09-11T18:42:05Z | sn15 released v2.0.6 |
| `sn15:scoring_commit:2026-09-11T18:12:07Z` | 15 | SCORING_COMMIT | 2026-09-11T18:42:05Z | sn15 commit touches scoring: chore(validator): pin oro-env-runtime 0.2.12 (strip agent rulebook) (… |
| `sn25:scoring_commit:2026-09-11T17:13:28Z` | 25 | SCORING_COMMIT | 2026-09-11T18:42:05Z | sn25 commit touches scoring: Observe provisional validator intents from the retained V2 state |
| `sn71:scoring_commit:2026-09-11T18:01:43Z` | 71 | SCORING_COMMIT | 2026-09-11T18:42:05Z | sn71 commit touches scoring: Accept Harvest plural current positions in contact verification |
| `sn20:scoring_commit:2026-09-11T19:18:55Z` | 20 | SCORING_COMMIT | 2026-09-11T21:21:44Z | sn20 commit touches scoring: Add grounded video scoring and hybrid mainnet rounds |
| `sn25:release:v2026.9.11-1043550030` | 25 | RELEASE | 2026-09-11T21:21:44Z | sn25 released v2026.9.11-1043550030 |
| `sn71:scoring_commit:2026-09-11T20:33:14Z` | 71 | SCORING_COMMIT | 2026-09-11T21:21:44Z | sn71 commit touches scoring: Verify in-flight Arena leases survive participation migration |
| `sn100:scoring_commit:2026-09-11T19:56:05Z` | 100 | SCORING_COMMIT | 2026-09-11T21:21:44Z | sn100 commit touches scoring: fix(proof): fail-closed harbor partial scores and forged rewards |
| `sn25:scoring_commit:2026-09-12T00:45:57Z` | 25 | SCORING_COMMIT | 2026-09-12T01:27:39Z | sn25 commit touches scoring: Sync disposable replay scratch once after complete verification |
| `sn71:scoring_commit:2026-09-12T01:00:20Z` | 71 | SCORING_COMMIT | 2026-09-12T01:27:39Z | sn71 commit touches scoring: Preserve Arena miner credential failure evidence |
| `sn25:scoring_commit:2026-09-12T02:44:47Z` | 25 | SCORING_COMMIT | 2026-09-12T06:24:23Z | sn25 commit touches scoring: Reuse verified historical deployment completion in corrective admissio |
| `sn51:scoring_commit:2026-09-12T01:49:58Z` | 51 | SCORING_COMMIT | 2026-09-12T06:24:23Z | sn51 commit touches scoring: DAH-3439 - [P0] validator: outdated executor image is a warning, not … |
| `sn71:scoring_commit:2026-09-12T04:57:15Z` | 71 | SCORING_COMMIT | 2026-09-12T06:24:23Z | sn71 commit touches scoring: Use current billing schema in normal validator transition test |
| `sn44:scoring_commit:2026-09-12T08:31:49Z` | 44 | SCORING_COMMIT | 2026-09-12T11:06:47Z | sn44 commit touches scoring: gather responses before scoring |
| `sn71:scoring_commit:2026-09-12T07:05:12Z` | 71 | SCORING_COMMIT | 2026-09-12T11:06:47Z | sn71 commit touches scoring: Remove the OpenRouter paid-validation budget restriction |
| `sn81:scoring_commit:2026-09-12T08:37:18Z` | 81 | SCORING_COMMIT | 2026-09-12T11:06:47Z | sn81 commit touches scoring: fix(validator): separate reveal accounting from admission failures (#… |
| `sn91:scoring_commit:2026-09-12T10:18:52Z` | 91 | SCORING_COMMIT | 2026-09-12T11:06:47Z | sn91 commit touches scoring: trainer: king rent retries lemon pods and releases the challenger wai… |
| `sn92:scoring_commit:2026-09-12T10:49:32Z` | 92 | SCORING_COMMIT | 2026-09-12T11:06:47Z | sn92 commit touches scoring: fees: a per submission commitment fee; mt miner fee pays and reports … |
| `sn71:scoring_commit:2026-09-12T11:34:03Z` | 71 | SCORING_COMMIT | 2026-09-12T14:06:12Z | sn71 commit touches scoring: Verify original provider statuses in paid fallback ledger receipts |
| `sn100:scoring_commit:2026-09-12T09:01:01Z` | 100 | SCORING_COMMIT | 2026-09-12T14:06:12Z | sn100 commit touches scoring: fix(proof-fc-harvest): zero-scored agent-exception rows need no rewar… |
| `sn36:scoring_commit:2026-09-11T11:52:07Z` | 36 | SCORING_COMMIT | 2026-09-12T17:07:44Z | sn36 commit touches scoring: Run calibration once a day on 200 tasks, in the background |
| `sn71:scoring_commit:2026-09-12T16:43:22Z` | 71 | SCORING_COMMIT | 2026-09-12T17:07:44Z | sn71 commit touches scoring: Set daily Arena admission to twenty challengers |
| `sn92:scoring_commit:2026-09-12T14:25:40Z` | 92 | SCORING_COMMIT | 2026-09-12T17:07:44Z | sn92 commit touches scoring: tracks: the hallucination detection track is guard on mt-4g, scored b… |
| `sn25:scoring_commit:2026-09-12T18:01:31Z` | 25 | SCORING_COMMIT | 2026-09-12T19:19:47Z | sn25 commit touches scoring: Record strict restart verification and canonical repair fee evidence |
| `sn78:scoring_commit:2026-09-12T18:46:12Z` | 78 | SCORING_COMMIT | 2026-09-12T19:19:47Z | sn78 commit touches scoring: Add time-bounded live-miner bridge with equal coldkey group weights |
| `sn81:scoring_commit:2026-09-12T18:27:08Z` | 81 | SCORING_COMMIT | 2026-09-12T19:19:47Z | sn81 commit touches scoring: fix(validator): bound no-reveal debt per window |
| `sn92:scoring_commit:2026-09-12T17:50:00Z` | 92 | SCORING_COMMIT | 2026-09-12T19:19:47Z | sn92 commit touches scoring: tracks: guard is the one live track on mt-4g; the span scorer reads g… |
| `sn25:scoring_commit:2026-09-12T19:54:30Z` | 25 | SCORING_COMMIT | 2026-09-12T21:32:22Z | sn25 commit touches scoring: Record sim-testnet validator and contract generation results |
| `sn71:scoring_commit:2026-09-12T17:00:23Z` | 71 | SCORING_COMMIT | 2026-09-12T21:32:22Z | sn71 commit touches scoring: Verify participation with shared-owner Arena admissions |
| `sn78:scoring_commit:2026-09-12T20:29:58Z` | 78 | SCORING_COMMIT | 2026-09-12T21:32:22Z | sn78 commit touches scoring: Document live-miner bridge activation and finalized reward evidence |
| `sn81:scoring_commit:2026-09-12T21:14:17Z` | 81 | SCORING_COMMIT | 2026-09-12T21:32:22Z | sn81 commit touches scoring: fix(validator): qualify proof lanes and partial rotations |
| `sn15:release:v2.0.7` | 15 | RELEASE | 2026-09-12T23:27:19Z | sn15 released v2.0.7 |
| `sn15:scoring_commit:2026-09-12T22:23:01Z` | 15 | SCORING_COMMIT | 2026-09-12T23:27:19Z | sn15 commit touches scoring: chore(validator): pin oro-env-runtime 0.2.13 (justification + recover… |
| `sn25:scoring_commit:2026-09-12T22:03:18Z` | 25 | SCORING_COMMIT | 2026-09-12T23:27:19Z | sn25 commit touches scoring: Bind historical reward batch RPCs to capture cancellation |
| `sn78:scoring_commit:2026-09-12T22:27:05Z` | 78 | SCORING_COMMIT | 2026-09-12T23:27:19Z | sn78 commit touches scoring: Point new validator installations at the IP-cap host release |
| `sn91:scoring_commit:2026-09-12T23:55:31Z` | 91 | SCORING_COMMIT | 2026-09-13T01:22:07Z | sn91 commit touches scoring: provision: pin the Lium pull by digest and verify worker CODE before … |
| `sn100:scoring_commit:2026-09-13T00:05:10Z` | 100 | SCORING_COMMIT | 2026-09-13T01:22:07Z | sn100 commit touches scoring: fix(proof): align results_path validation across hosts |
| `sn15:release:v2.0.8` | 15 | RELEASE | 2026-09-13T06:30:50Z | sn15 released v2.0.8 |
| `sn15:scoring_commit:2026-09-13T04:37:49Z` | 15 | SCORING_COMMIT | 2026-09-13T06:30:50Z | sn15 commit touches scoring: chore(validator): pin oro-env-runtime 0.2.14 (claim tool-schema vocab… |
| `sn53:scoring_commit:2026-09-13T04:12:59Z` | 53 | SCORING_COMMIT | 2026-09-13T06:30:50Z | sn53 commit touches scoring: Merge pull request #45 from hanlinai/fix/tee-miner-kv-pool-retry |
| `sn78:scoring_commit:2026-09-13T02:33:24Z` | 78 | SCORING_COMMIT | 2026-09-13T06:30:50Z | sn78 commit touches scoring: Record finalized funding-cap rollout on both validators |
| `sn15:release:v2.0.9` | 15 | RELEASE | 2026-09-13T12:20:01Z | sn15 released v2.0.9 |
| `sn61:release:4.10.5` | 61 | RELEASE | 2026-09-13T12:20:01Z | sn61 released 4.10.5 |
| `sn61:scoring_commit:2026-09-13T07:47:58Z` | 61 | SCORING_COMMIT | 2026-09-13T12:20:01Z | sn61 commit touches scoring: deps: update ada_detection challenge image version to 3.0.3 |
| `sn71:scoring_commit:2026-09-13T09:49:04Z` | 71 | SCORING_COMMIT | 2026-09-13T12:20:01Z | sn71 commit touches scoring: Bind recovered Arena future stages to the corrected scorer |
| `sn78:scoring_commit:2026-09-13T06:02:29Z` | 78 | SCORING_COMMIT | 2026-09-13T12:20:01Z | sn78 commit touches scoring: Accept the verified stopped successor during interrupted publication … |
| `sn81:scoring_commit:2026-09-13T09:02:00Z` | 81 | SCORING_COMMIT | 2026-09-13T12:20:01Z | sn81 commit touches scoring: fix: bound validator startup memory (#255) |
| `sn91:scoring_commit:2026-09-13T10:23:14Z` | 91 | SCORING_COMMIT | 2026-09-13T12:20:01Z | sn91 commit touches scoring: pool: publish packs mv_channels iff effective_block >= [scoring] mv_s… |
| `sn100:scoring_commit:2026-09-13T09:53:24Z` | 100 | SCORING_COMMIT | 2026-09-13T12:20:01Z | sn100 commit touches scoring: docs(proof): keep miner tbench rebake pin after skew-hint copy |
| `sn78:scoring_commit:2026-09-13T15:50:06Z` | 78 | SCORING_COMMIT | 2026-09-13T16:33:13Z | sn78 commit touches scoring: Merge pull request #61 from Umi-BitSign/codex/miner-readiness-20260913 |
| `sn71:scoring_commit:2026-09-13T16:53:24Z` | 71 | SCORING_COMMIT | 2026-09-13T19:00:00Z | sn71 commit touches scoring: Bind stage two recovery to tested scorer image |
| `sn78:scoring_commit:2026-09-13T18:55:26Z` | 78 | SCORING_COMMIT | 2026-09-13T19:00:00Z | sn78 commit touches scoring: Merge pull request #64 from Umi-BitSign/codex/endpoint-paired-evaluat… |
| `sn15:release:v2.0.10: Capture complete episode resour` | 15 | RELEASE | 2026-09-13T21:25:03Z | sn15 released v2.0.10: Capture complete episode resource telemetry (#298) |
| `sn15:scoring_commit:2026-09-13T21:09:59Z` | 15 | SCORING_COMMIT | 2026-09-13T21:25:03Z | sn15 commit touches scoring: Use SDK transient status classification for validator retries (#299) |
| `sn78:scoring_commit:2026-09-13T21:00:59Z` | 78 | SCORING_COMMIT | 2026-09-13T21:25:03Z | sn78 commit touches scoring: Merge pull request #65 from Umi-BitSign/codex/competition-evaluator-l… |
| `sn81:scoring_commit:2026-09-13T21:01:46Z` | 81 | SCORING_COMMIT | 2026-09-13T21:25:03Z | sn81 commit touches scoring: feat(validator): explain V1 selection verdicts |
| `sn15:release:v2.0.11: fix: preserve episode inference` | 15 | RELEASE | 2026-09-13T23:21:49Z | sn15 released v2.0.11: fix: preserve episode inference telemetry without sidecar (#300) |
| `sn71:scoring_commit:2026-09-13T22:16:51Z` | 71 | SCORING_COMMIT | 2026-09-13T23:21:49Z | sn71 commit touches scoring: Match verified US contact state aliases |
| `sn78:scoring_commit:2026-09-13T21:56:31Z` | 78 | SCORING_COMMIT | 2026-09-13T23:21:49Z | sn78 commit touches scoring: Connect independent work signing and automatic evaluator order deliver |
| `sn15:release:v2.0.12` | 15 | RELEASE | 2026-09-14T01:21:09Z | sn15 released v2.0.12 |
| `sn15:scoring_commit:2026-09-13T23:48:08Z` | 15 | SCORING_COMMIT | 2026-09-14T01:21:09Z | sn15 commit touches scoring: fix: make validator startup logs formatting-safe (#302) |
| `sn20:scoring_commit:2026-09-13T20:16:47Z` | 20 | SCORING_COMMIT | 2026-09-14T01:21:09Z | sn20 commit touches scoring: Resolve the validator signing key before timed network dispatch |
| `sn81:scoring_commit:2026-09-14T00:28:08Z` | 81 | SCORING_COMMIT | 2026-09-14T01:21:09Z | sn81 commit touches scoring: fix(weight-only): retain only reward fields from archives (#259) |
| `sn15:release:v2.0.14: feat: capture per-episode wall ` | 15 | RELEASE | 2026-09-14T06:42:05Z | sn15 released v2.0.14: feat: capture per-episode wall time (#304) |
| `sn15:scoring_commit:2026-09-14T04:01:53Z` | 15 | SCORING_COMMIT | 2026-09-14T06:42:05Z | sn15 commit touches scoring: fix: reject any generated evaluation infrastructure error (#303) |
| `sn25:release:v2026.9.13-1045655440` | 25 | RELEASE | 2026-09-14T06:42:05Z | sn25 released v2026.9.13-1045655440 |
| `sn71:scoring_commit:2026-09-14T05:15:09Z` | 71 | SCORING_COMMIT | 2026-09-14T06:42:05Z | sn71 commit touches scoring: Retain native provider billing receipts and align scoring timeouts |
| `sn78:scoring_commit:2026-09-14T05:26:34Z` | 78 | SCORING_COMMIT | 2026-09-14T06:42:05Z | sn78 commit touches scoring: docs: use private holdout for automatic competition evaluation |
| `sn81:scoring_commit:2026-09-14T04:57:45Z` | 81 | SCORING_COMMIT | 2026-09-14T06:42:05Z | sn81 commit touches scoring: Warn miners about Transformers runtime differences |
| `sn91:scoring_commit:2026-09-14T02:21:06Z` | 91 | SCORING_COMMIT | 2026-09-14T06:42:05Z | sn91 commit touches scoring: feat(funding): miner-chosen submission label (`cascade fund --label`) |
| `sn15:scoring_commit:2026-09-14T07:58:25Z` | 15 | SCORING_COMMIT | 2026-09-14T13:23:56Z | sn15 commit touches scoring: chore(validator): bump oro-env-runtime 0.2.14 -> 0.2.18 for new-gener… |
| `sn25:release:v2026.9.14-1045806490` | 25 | RELEASE | 2026-09-14T13:23:56Z | sn25 released v2026.9.14-1045806490 |
| `sn25:scoring_commit:2026-09-14T08:31:58Z` | 25 | SCORING_COMMIT | 2026-09-14T13:23:56Z | sn25 commit touches scoring: Validate capture ownership against growing source census |
| `sn28:scoring_commit:2026-09-14T11:05:56Z` | 28 | SCORING_COMMIT | 2026-09-14T13:23:56Z | sn28 commit touches scoring: refactor(near): fold the path check into request validation |
| `sn38:scoring_commit:2026-09-14T12:58:13Z` | 38 | SCORING_COMMIT | 2026-09-14T13:23:56Z | sn38 commit touches scoring: Update validator image to the latest version in docker-compose.valida… |
| `sn51:release:executor-v1.128` | 51 | RELEASE | 2026-09-14T13:23:56Z | sn51 released executor-v1.128 |
| `sn51:scoring_commit:2026-09-14T13:17:55Z` | 51 | SCORING_COMMIT | 2026-09-14T13:23:56Z | sn51 commit touches scoring: DAH-3247 - [P1] lium_protocol: the validator↔backend wire as one vers… |
| `sn67:scoring_commit:2026-09-14T10:53:38Z` | 67 | SCORING_COMMIT | 2026-09-14T13:23:56Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20260914.post5 |
| `sn78:scoring_commit:2026-09-14T11:54:17Z` | 78 | SCORING_COMMIT | 2026-09-14T13:23:56Z | sn78 commit touches scoring: Prioritize pending evaluator evidence over retained upload audits |
| `sn91:scoring_commit:2026-09-14T11:24:34Z` | 91 | SCORING_COMMIT | 2026-09-14T13:23:56Z | sn91 commit touches scoring: Merge pull request #278 from TensorLink-AI/docs/miner-docs-simplify |
| `sn111:scoring_commit:2026-09-14T12:16:34Z` | 111 | SCORING_COMMIT | 2026-09-14T13:23:56Z | sn111 commit touches scoring: fix(validator): attribute dendrite failures to miner UIDs |
| `sn114:scoring_commit:2026-09-14T10:40:48Z` | 114 | SCORING_COMMIT | 2026-09-14T13:23:56Z | sn114 commit touches scoring: add default config value for validator |
| `sn1:release:v4.4.6` | 1 | RELEASE | 2026-09-14T18:48:49Z | sn1 released v4.4.6 |
| `sn21:scoring_commit:2026-09-14T14:13:22Z` | 21 | SCORING_COMMIT | 2026-09-14T18:48:49Z | sn21 commit touches scoring: scoring: the settle schedule is 10 / 17 / 31 days after the basket; p… |
| `sn25:release:v2026.9.14-1046068620` | 25 | RELEASE | 2026-09-14T18:48:49Z | sn25 released v2026.9.14-1046068620 |
| `sn45:scoring_commit:2026-09-14T17:14:32Z` | 45 | SCORING_COMMIT | 2026-09-14T18:48:49Z | sn45 commit touches scoring: Ignore per-validator runtime state and secrets |
| `sn50:scoring_commit:2026-09-14T16:02:59Z` | 50 | SCORING_COMMIT | 2026-09-14T18:48:49Z | sn50 commit touches scoring: feat(validator): add a volatility CRPS term to the crypto-1h score (#… |
| `sn51:scoring_commit:2026-09-14T14:51:23Z` | 51 | SCORING_COMMIT | 2026-09-14T18:48:49Z | sn51 commit touches scoring: DAH-3457 - [P1] validator: a UUID listed twice in the scrape is one c… |
| `sn71:scoring_commit:2026-09-14T18:33:42Z` | 71 | SCORING_COMMIT | 2026-09-14T18:48:49Z | sn71 commit touches scoring: Verify retained weight reveals on runtime profile 458 |
| `sn76:scoring_commit:2026-09-14T14:48:21Z` | 76 | SCORING_COMMIT | 2026-09-14T18:48:49Z | sn76 commit touches scoring: Merge pull request #1 from heroncovelabs/fix/validator-clone-error |
| `sn78:scoring_commit:2026-09-14T13:12:56Z` | 78 | SCORING_COMMIT | 2026-09-14T18:48:49Z | sn78 commit touches scoring: Retire verified redundant successor materializations |
| `sn90:scoring_commit:2026-09-14T14:40:13Z` | 90 | SCORING_COMMIT | 2026-09-14T18:48:49Z | sn90 commit touches scoring: docs: BTLABS (UID 97) live — first production miner on KubeTEE |
| `sn62:scoring_commit:2026-09-14T18:42:44Z` | 62 | SCORING_COMMIT | 2026-09-14T22:27:00Z | sn62 commit touches scoring: add PublicEvaluationRun model |
| `sn71:scoring_commit:2026-09-14T22:21:33Z` | 71 | SCORING_COMMIT | 2026-09-14T22:27:00Z | sn71 commit touches scoring: Refresh protected source for verified paragraph coverage |
| `sn76:scoring_commit:2026-09-14T22:08:23Z` | 76 | SCORING_COMMIT | 2026-09-14T22:27:00Z | sn76 commit touches scoring: docs(miner): credential path leads INSTALL/README; bind is the fallba… |
| `sn78:scoring_commit:2026-09-14T21:24:12Z` | 78 | SCORING_COMMIT | 2026-09-14T22:27:00Z | sn78 commit touches scoring: Publish runtime-independent validator host pin and signed manifests |
| `sn111:release:v0.2.0` | 111 | RELEASE | 2026-09-14T22:27:00Z | sn111 released v0.2.0 |
| `sn71:scoring_commit:2026-09-14T23:58:08Z` | 71 | SCORING_COMMIT | 2026-09-15T00:51:26Z | sn71 commit touches scoring: Refresh reviewed scorer workflow protections |
| `sn81:scoring_commit:2026-09-15T00:01:23Z` | 81 | SCORING_COMMIT | 2026-09-15T00:51:26Z | sn81 commit touches scoring: Merge pull request #267 from reliquadotai/design/task-scoped-emission… |
| `sn71:scoring_commit:2026-09-15T04:46:46Z` | 71 | SCORING_COMMIT | 2026-09-15T06:08:06Z | sn71 commit touches scoring: Preserve declared homepage encodings during company verification |
| `sn76:scoring_commit:2026-09-15T03:56:34Z` | 76 | SCORING_COMMIT | 2026-09-15T06:08:06Z | sn76 commit touches scoring: docs(protocol): production runs one operator-run validator and cross-… |
| `sn78:scoring_commit:2026-09-15T02:49:36Z` | 78 | SCORING_COMMIT | 2026-09-15T06:08:06Z | sn78 commit touches scoring: Merge pull request #97 from Umi-BitSign/codex/uid0-single-evaluator-l… |
| `sn104:scoring_commit:2026-09-10T11:48:51Z` | 104 | SCORING_COMMIT | 2026-09-15T06:08:06Z | sn104 commit touches scoring: fix: burn the full allocation when no miner has earned a score |
| `sn10:scoring_commit:2026-09-15T10:10:42Z` | 10 | SCORING_COMMIT | 2026-09-15T11:58:52Z | sn10 commit touches scoring: feat: add campaign context coverage and reliability scoring for SGLan… |
| `sn11:scoring_commit:2026-09-15T11:10:55Z` | 11 | SCORING_COMMIT | 2026-09-15T11:58:52Z | sn11 commit touches scoring: Merge pull request #321 from trajectoryRL/agent/coding/disable-miner-… |
| `sn15:release:v2.0.15: chore(validator): pin runtime 1` | 15 | RELEASE | 2026-09-15T11:58:52Z | sn15 released v2.0.15: chore(validator): pin runtime 1.0.6 for generated packs |
| `sn15:scoring_commit:2026-09-15T10:19:23Z` | 15 | SCORING_COMMIT | 2026-09-15T11:58:52Z | sn15 commit touches scoring: chore(validator): pin runtime 1.0.6 for generated packs |
| `sn20:scoring_commit:2026-09-15T10:27:48Z` | 20 | SCORING_COMMIT | 2026-09-15T11:58:52Z | sn20 commit touches scoring: Derive semantic verdicts from validated field decisions |
| `sn51:scoring_commit:2026-09-15T10:31:03Z` | 51 | SCORING_COMMIT | 2026-09-15T11:58:52Z | sn51 commit touches scoring: DAH-2834 - [P0] validator consumes the executor's one-call /verify an… |
| `sn67:scoring_commit:2026-09-15T10:10:49Z` | 67 | SCORING_COMMIT | 2026-09-15T11:58:52Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20260915.post4 |
| `sn71:scoring_commit:2026-09-15T09:56:04Z` | 71 | SCORING_COMMIT | 2026-09-15T11:58:52Z | sn71 commit touches scoring: test: prove normal scoring collision rolls back exact Sep15 rerun |
| `sn78:scoring_commit:2026-09-15T06:08:40Z` | 78 | SCORING_COMMIT | 2026-09-15T11:58:52Z | sn78 commit touches scoring: Stop miner HTTP service after terminal background failure (#101) |
| `sn90:scoring_commit:2026-09-15T09:13:04Z` | 90 | SCORING_COMMIT | 2026-09-15T11:58:52Z | sn90 commit touches scoring: docs(roadmap): move scoring-expansion item to Phase 2 |
| `sn91:scoring_commit:2026-09-15T09:37:30Z` | 91 | SCORING_COMMIT | 2026-09-15T11:58:52Z | sn91 commit touches scoring: fix: king rents first — challengers yield the marketplace while the J… |
| `sn10:scoring_commit:2026-09-15T13:11:21Z` | 10 | SCORING_COMMIT | 2026-09-15T16:53:10Z | sn10 commit touches scoring: fix: harden validator API binding and service privileges (#159) |
| `sn66:scoring_commit:2026-09-15T16:49:50Z` | 66 | SCORING_COMMIT | 2026-09-15T16:53:10Z | sn66 commit touches scoring: Raise proof token limit to one million for local verifiers |
| `sn90:release:v1.2.0` | 90 | RELEASE | 2026-09-15T16:53:10Z | sn90 released v1.2.0 |
| `sn90:scoring_commit:2026-09-15T15:53:37Z` | 90 | SCORING_COMMIT | 2026-09-15T16:53:10Z | sn90 commit touches scoring: fix(scoring): divide emission pool by the 50% miner share of combined… |
| `sn15:release:v2.0.17` | 15 | RELEASE | 2026-09-15T20:12:28Z | sn15 released v2.0.17 |
| `sn34:scoring_commit:2026-09-15T17:50:38Z` | 34 | SCORING_COMMIT | 2026-09-15T20:12:28Z | sn34 commit touches scoring: Fix generative callback staleness and validator memory pressure (#449) |
| `sn76:scoring_commit:2026-09-15T18:26:04Z` | 76 | SCORING_COMMIT | 2026-09-15T20:12:28Z | sn76 commit touches scoring: docs: day-one fixes from the first third-party miner (2026-09-15) — I… |
| `sn78:scoring_commit:2026-09-15T18:26:35Z` | 78 | SCORING_COMMIT | 2026-09-15T20:12:28Z | sn78 commit touches scoring: Merge pull request #107 from Umi-BitSign/codex/two-task-scoring-202609 |
| `sn15:release:v2.0.18: search-server sync-worker fix +` | 15 | RELEASE | 2026-09-15T23:01:57Z | sn15 released v2.0.18: search-server sync-worker fix + rebuilt base (ORO-2244) |
| `sn62:scoring_commit:2026-09-15T21:51:17Z` | 62 | SCORING_COMMIT | 2026-09-15T23:01:57Z | sn62 commit touches scoring: test: :white_check_mark: Update tests to validate that the baseline o… |
| `sn76:scoring_commit:2026-09-15T20:44:58Z` | 76 | SCORING_COMMIT | 2026-09-15T23:01:57Z | sn76 commit touches scoring: docs: FAQ from the first external miner's day one (expected first-run… |
| `sn102:release:v0.6.0 — scheduled task switching` | 102 | RELEASE | 2026-09-15T23:01:57Z | sn102 released v0.6.0 — scheduled task switching |
| `sn102:scoring_commit:2026-09-15T20:14:58Z` | 102 | SCORING_COMMIT | 2026-09-15T23:01:57Z | sn102 commit touches scoring: ⚡️ perf(validator): cap the in-shard eval offset independently of sha… |
| `sn34:release:5.0.5 — Generator Qualification & Paid R` | 34 | RELEASE | 2026-09-16T01:23:06Z | sn34 released 5.0.5 — Generator Qualification & Paid Resubmissions |
| `sn62:release:v0.3.5` | 62 | RELEASE | 2026-09-16T01:23:06Z | sn62 released v0.3.5 |
| `sn78:scoring_commit:2026-09-15T23:51:06Z` | 78 | SCORING_COMMIT | 2026-09-16T01:23:06Z | sn78 commit touches scoring: Verify current installer against signed frozen operator bundle |
| `sn15:release:v2.0.19` | 15 | RELEASE | 2026-09-16T06:23:31Z | sn15 released v2.0.19 |
| `sn25:scoring_commit:2026-09-16T03:56:01Z` | 25 | SCORING_COMMIT | 2026-09-16T06:23:31Z | sn25 commit touches scoring: Retain verified reserve repairs for exact software revisions |
| `sn51:scoring_commit:2026-09-16T06:18:33Z` | 51 | SCORING_COMMIT | 2026-09-16T06:23:31Z | sn51 commit touches scoring: DAH-2662 - [P1] validator matches GPU bans against the kernel's GPU U… |
| `sn78:scoring_commit:2026-09-16T01:47:17Z` | 78 | SCORING_COMMIT | 2026-09-16T06:23:31Z | sn78 commit touches scoring: Stage verified successor helpers outside non-executable tmp |
| `sn10:scoring_commit:2026-09-16T08:26:18Z` | 10 | SCORING_COMMIT | 2026-09-16T11:55:55Z | sn10 commit touches scoring: fix(bench): lower Qwen correctness scorer memory allocation (#163) |
| `sn25:scoring_commit:2026-09-16T10:32:54Z` | 25 | SCORING_COMMIT | 2026-09-16T11:55:55Z | sn25 commit touches scoring: Allow bounded retained validator history warmup on every RPC route |
| `sn51:scoring_commit:2026-09-16T08:11:18Z` | 51 | SCORING_COMMIT | 2026-09-16T11:55:55Z | sn51 commit touches scoring: DAH-3480 - [P1] validator: GPU probe blocked by a mid-cycle pod or fi… |
| `sn78:scoring_commit:2026-09-16T08:59:20Z` | 78 | SCORING_COMMIT | 2026-09-16T11:55:55Z | sn78 commit touches scoring: Merge pull request #129 from Umi-BitSign/codex/miner-historical-admis… |
| `sn114:scoring_commit:2026-09-16T07:55:05Z` | 114 | SCORING_COMMIT | 2026-09-16T11:55:55Z | sn114 commit touches scoring: docs: describe complexity incentive layers |
| `sn9:release:v4.13.0` | 9 | RELEASE | 2026-09-16T16:47:34Z | sn9 released v4.13.0 |
| `sn51:release:executor-v1.129` | 51 | RELEASE | 2026-09-16T16:47:34Z | sn51 released executor-v1.129 |
| `sn66:release:v1.0.4` | 66 | RELEASE | 2026-09-16T16:47:34Z | sn66 released v1.0.4 |
| `sn76:scoring_commit:2026-09-16T14:56:09Z` | 76 | SCORING_COMMIT | 2026-09-16T16:47:34Z | sn76 commit touches scoring: feat(client): optional chosen miner_id on registration — receipts, pr… |
| `sn92:release:v0.4.4` | 92 | RELEASE | 2026-09-16T16:47:34Z | sn92 released v0.4.4 |
| `sn92:scoring_commit:2026-09-16T16:42:38Z` | 92 | SCORING_COMMIT | 2026-09-16T16:47:34Z | sn92 commit touches scoring: penalties: declared factors on the standing vector, verified by valid… |
| `sn34:scoring_commit:2026-09-16T18:39:36Z` | 34 | SCORING_COMMIT | 2026-09-16T19:46:19Z | sn34 commit touches scoring: Exclude no_answer rows before the reward-stats row cap. |
| `sn71:scoring_commit:2026-09-16T17:06:43Z` | 71 | SCORING_COMMIT | 2026-09-16T19:46:19Z | sn71 commit touches scoring: Fix Sep16 benchmark bank verification |
| `sn78:scoring_commit:2026-09-16T18:11:28Z` | 78 | SCORING_COMMIT | 2026-09-16T19:46:19Z | sn78 commit touches scoring: fix: keep valid bridge miners eligible during registration churn |
| `sn92:release:v0.4.6` | 92 | RELEASE | 2026-09-16T19:46:19Z | sn92 released v0.4.6 |
| `sn92:scoring_commit:2026-09-16T17:47:30Z` | 92 | SCORING_COMMIT | 2026-09-16T19:46:19Z | sn92 commit touches scoring: mt-4g: 3 GiB disk ceiling, matching the arenas validators enforce (#77 |
| `sn28:release:v0.4.18` | 28 | RELEASE | 2026-09-16T22:24:56Z | sn28 released v0.4.18 |
| `sn45:scoring_commit:2026-09-16T17:29:43Z` | 45 | SCORING_COMMIT | 2026-09-16T22:24:56Z | sn45 commit touches scoring: Allow a per-model scale on audit scores |
| `sn78:scoring_commit:2026-09-16T20:06:28Z` | 78 | SCORING_COMMIT | 2026-09-16T22:24:56Z | sn78 commit touches scoring: release: pin fresh validator installs to registration churn fix |
| `sn102:release:v0.6.1` | 102 | RELEASE | 2026-09-16T22:24:56Z | sn102 released v0.6.1 |
| `sn102:scoring_commit:2026-09-16T20:16:29Z` | 102 | SCORING_COMMIT | 2026-09-16T22:24:56Z | sn102 commit touches scoring: Merge pull request #274 from Connito-AI/feat/switch-task-release-then… |
| `sn40:scoring_commit:2026-09-16T00:55:22Z` | 40 | SCORING_COMMIT | 2026-09-17T00:48:02Z | sn40 commit touches scoring: Docs: round-7 rules, miner CLI flow, auditor weights |
| `sn78:scoring_commit:2026-09-16T22:31:06Z` | 78 | SCORING_COMMIT | 2026-09-17T00:48:02Z | sn78 commit touches scoring: Merge pull request #135 from Umi-BitSign/codex/evaluator-finality-wai… |
| `sn15:release:v2.0.20` | 15 | RELEASE | 2026-09-17T06:06:18Z | sn15 released v2.0.20 |
| `sn15:scoring_commit:2026-09-17T05:30:31Z` | 15 | SCORING_COMMIT | 2026-09-17T06:06:18Z | sn15 commit touches scoring: Stop generated runs when miner inference budget is exhausted (#317) |
| `sn51:scoring_commit:2026-09-17T05:33:07Z` | 51 | SCORING_COMMIT | 2026-09-17T06:06:18Z | sn51 commit touches scoring: DAH-3264 - [P2] validator names a GPU benchmark that could not alloca… |
| `sn78:scoring_commit:2026-09-17T00:15:39Z` | 78 | SCORING_COMMIT | 2026-09-17T06:06:18Z | sn78 commit touches scoring: Verify retained clip objects before retrying an upload |
| `sn92:release:v0.4.7` | 92 | RELEASE | 2026-09-17T06:06:18Z | sn92 released v0.4.7 |
| `sn51:release:executor-v1.130` | 51 | RELEASE | 2026-09-17T11:36:55Z | sn51 released executor-v1.130 |
| `sn51:scoring_commit:2026-09-17T07:44:39Z` | 51 | SCORING_COMMIT | 2026-09-17T11:36:55Z | sn51 commit touches scoring: DAH-3519 - [P2] validator: a node whose scrape lists fewer GPUs than … |
| `sn78:scoring_commit:2026-09-17T08:39:07Z` | 78 | SCORING_COMMIT | 2026-09-17T11:36:55Z | sn78 commit touches scoring: Merge pull request #153 from Umi-BitSign/codex/evaluator-idle-finalit… |
| `sn92:release:v0.4.9` | 92 | RELEASE | 2026-09-17T11:36:55Z | sn92 released v0.4.9 |
| `sn97:scoring_commit:2026-09-16T15:02:19Z` | 97 | SCORING_COMMIT | 2026-09-17T11:36:55Z | sn97 commit touches scoring: feat: add extra attempts, so miners which got FPs can resubmit with p… |
| `sn10:scoring_commit:2026-09-17T10:11:18Z` | 10 | SCORING_COMMIT | 2026-09-17T15:41:12Z | sn10 commit touches scoring: fix: refresh campaign fees before payment and verify inclusion |
| `sn56:scoring_commit:2026-09-17T15:30:38Z` | 56 | SCORING_COMMIT | 2026-09-17T15:41:12Z | sn56 commit touches scoring: Update autoupdate_validator_steps.sh to ensure proper package managem… |
| `sn92:release:v0.4.11` | 92 | RELEASE | 2026-09-17T15:41:12Z | sn92 released v0.4.11 |
| `sn92:scoring_commit:2026-09-17T12:16:02Z` | 92 | SCORING_COMMIT | 2026-09-17T15:41:12Z | sn92 commit touches scoring: validator: rig verification needs substrate-interface, and is skipped… |
| `sn124:scoring_commit:2026-09-17T11:43:08Z` | 124 | SCORING_COMMIT | 2026-09-17T15:41:12Z | sn124 commit touches scoring: Pin numpy and repair a drifted validator at startup |
| `sn25:release:v2026.9.17-1048676710` | 25 | RELEASE | 2026-09-17T19:19:51Z | sn25 released v2026.9.17-1048676710 |
| `sn74:release:release-20260917-174533` | 74 | RELEASE | 2026-09-17T19:19:51Z | sn74 released release-20260917-174533 |
| `sn7:readme_task_diff:dc7b2a4e628af18f` | 7 | README_TASK_DIFF | 2026-09-11T06:22:30Z | sn7 README task/scoring sections changed |
| `sn71:readme_task_diff:f4854b87ceea3027` | 71 | README_TASK_DIFF | 2026-09-11T06:22:30Z | sn71 README task/scoring sections changed |
| `sn20:readme_task_diff:8d48fc82515ff603` | 20 | README_TASK_DIFF | 2026-09-11T11:40:27Z | sn20 README task/scoring sections changed |
| `sn71:readme_task_diff:858d6e3350fdacde` | 71 | README_TASK_DIFF | 2026-09-11T18:42:05Z | sn71 README task/scoring sections changed |
| `sn71:readme_task_diff:691868bd635e63bb` | 71 | README_TASK_DIFF | 2026-09-12T06:24:23Z | sn71 README task/scoring sections changed |
| `sn71:readme_task_diff:d368671e8866d097` | 71 | README_TASK_DIFF | 2026-09-12T21:32:22Z | sn71 README task/scoring sections changed |
| `sn71:readme_task_diff:2b78fd54843d3b86` | 71 | README_TASK_DIFF | 2026-09-13T06:30:50Z | sn71 README task/scoring sections changed |
| `sn40:readme_task_diff:03959b1ab90af5c4` | 40 | README_TASK_DIFF | 2026-09-14T13:23:56Z | sn40 README task/scoring sections changed |
| `sn66:readme_task_diff:e6d3eecf74563f7e` | 66 | README_TASK_DIFF | 2026-09-14T13:23:56Z | sn66 README task/scoring sections changed |
| `sn67:readme_task_diff:9c525b1cc53f9b59` | 67 | README_TASK_DIFF | 2026-09-14T13:23:56Z | sn67 README task/scoring sections changed |
| `sn91:readme_task_diff:9c8c6d309a9f02a7` | 91 | README_TASK_DIFF | 2026-09-14T13:23:56Z | sn91 README task/scoring sections changed |
| `sn40:readme_task_diff:e5e91c3bf216a40b` | 40 | README_TASK_DIFF | 2026-09-14T18:48:49Z | sn40 README task/scoring sections changed |
| `sn90:readme_task_diff:e7ec7e8de55efc5a` | 90 | README_TASK_DIFF | 2026-09-14T18:48:49Z | sn90 README task/scoring sections changed |
| `sn90:readme_task_diff:ffaaddc742488086` | 90 | README_TASK_DIFF | 2026-09-15T11:58:52Z | sn90 README task/scoring sections changed |
| `sn15:readme_task_diff:553c134e9ff5c4e1` | 15 | README_TASK_DIFF | 2026-09-16T06:23:31Z | sn15 README task/scoring sections changed |
| `sn28:readme_task_diff:dbf1289fea38b78e` | 28 | README_TASK_DIFF | 2026-09-16T22:24:56Z | sn28 README task/scoring sections changed |
| `sn40:readme_task_diff:b6863d625c3e10b3` | 40 | README_TASK_DIFF | 2026-09-17T00:48:02Z | sn40 README task/scoring sections changed |
| `sn56:readme_task_diff:ef6f6fe132bb0121` | 56 | README_TASK_DIFF | 2026-09-17T15:41:12Z | sn56 README task/scoring sections changed |
| `sn124:readme_task_diff:5c048f406be8cfd7` | 124 | README_TASK_DIFF | 2026-09-17T15:41:12Z | sn124 README task/scoring sections changed |
| `sn74:readme_task_diff:60b1b8229a2e5bd0` | 74 | README_TASK_DIFF | 2026-09-17T19:19:51Z | sn74 README task/scoring sections changed |

## RESOLVED IN THIS WINDOW

_none_
