# ALARMS - generated 2026-11-28T17:49:50Z, block 9607010

window: first_seen in [2026-11-28T16:35:23Z, 2026-11-28T17:50:23Z)  (60 min interval + 15 min overlap)

Report ONLY the rows under NEW SINCE LAST RUN. Rows under STILL OPEN were
already reported in an earlier window and must not be re-alarmed.

## NEW SINCE LAST RUN

| event_id | netuid | class | severity | first_seen_utc | one_line |
|---|---|---|---|---|---|
| `sn71:burn_drop:0.959` | 71 | BURN_DROP | P0 | 2026-11-28T17:50:23Z | sn71 burn fell 0.999 -> 0.959 - miners can earn again |
| `sn91:burn_drop:0.950` | 91 | BURN_DROP | P0 | 2026-11-28T17:50:23Z | sn91 burn fell 1.000 -> 0.950 - miners can earn again |
| `sn25:release:v2026.11.28-1110821730` | 25 | RELEASE | P1 | 2026-11-28T17:50:23Z | sn25 released v2026.11.28-1110821730 |
| `sn91:scoring_commit:2026-11-28T16:13:48Z` | 91 | SCORING_COMMIT | P1 | 2026-11-28T17:50:23Z | sn91 commit touches scoring: fix(marketcast): the MarketCast pod runs the validator's shipped rele… |
| `sn120:scoring_commit:2026-11-28T13:30:30Z` | 120 | SCORING_COMMIT | P1 | 2026-11-28T17:50:23Z | sn120 commit touches scoring: Model merge_after_confirm in miner-facing Params |
| `sn129:scoring_commit:2026-11-28T13:53:13Z` | 129 | SCORING_COMMIT | P1 | 2026-11-28T17:50:23Z | sn129 commit touches scoring: Pin validator build 84 and give the one time move to 0.11.0 (#248) |

### detail

- **`sn71:burn_drop:0.959`** - sn71 burn fell 0.999 -> 0.959 - miners can earn again
  - This subnet paid miners nothing and now pays. Worth a look before the field fills up.
- **`sn91:burn_drop:0.950`** - sn91 burn fell 1.000 -> 0.950 - miners can earn again
  - This subnet paid miners nothing and now pays. Worth a look before the field fills up.
- **`sn25:release:v2026.11.28-1110821730`** - sn25 released v2026.11.28-1110821730
  - published 2026-11-28T16:21:21Z (was v2026.11.27-1110314090)
- **`sn91:scoring_commit:2026-11-28T16:13:48Z`** - sn91 commit touches scoring: fix(marketcast): the MarketCast pod runs the validator's shipped rele…
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn120:scoring_commit:2026-11-28T13:30:30Z`** - sn120 commit touches scoring: Model merge_after_confirm in miner-facing Params
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn129:scoring_commit:2026-11-28T13:53:13Z`** - sn129 commit touches scoring: Pin validator build 84 and give the one time move to 0.11.0 (#248)
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.

## STILL OPEN (already reported - do not re-alarm)

| event_id | netuid | class | first_seen_utc | one_line |
|---|---|---|---|---|
| `sn57:burn_drop:0.000` | 57 | BURN_DROP | 2026-11-21T21:47:24Z | sn57 burn fell 1.000 -> 0.000 - miners can earn again |
| `sn122:burn_drop:0.115` | 122 | BURN_DROP | 2026-11-21T21:47:24Z | sn122 burn fell 1.000 -> 0.115 - miners can earn again |
| `sn37:burn_drop:0.738` | 37 | BURN_DROP | 2026-11-22T22:26:39Z | sn37 burn fell 0.997 -> 0.738 - miners can earn again |
| `sn2:burn_drop:0.881` | 2 | BURN_DROP | 2026-11-24T10:13:41Z | sn2 burn fell 1.000 -> 0.881 - miners can earn again |
| `sn40:burn_drop:0.000` | 40 | BURN_DROP | 2026-11-25T23:12:10Z | sn40 burn fell 1.000 -> 0.000 - miners can earn again |
| `sn121:burn_drop:0.500` | 121 | BURN_DROP | 2026-11-25T23:12:10Z | sn121 burn fell 1.000 -> 0.500 - miners can earn again |
| `sn129:new_subnet:b9588847` | 129 | NEW_SUBNET | 2026-11-26T05:17:33Z | NEW SUBNET sn129 "va" first seen |
| `sn70:burn_drop:0.500` | 70 | BURN_DROP | 2026-11-26T15:34:43Z | sn70 burn fell 1.000 -> 0.500 - miners can earn again |
| `sn71:burn_drop:0.989` | 71 | BURN_DROP | 2026-11-27T18:22:48Z | sn71 burn fell 1.000 -> 0.989 - miners can earn again |
| `sn91:burn_drop:0.955` | 91 | BURN_DROP | 2026-11-27T18:22:48Z | sn91 burn fell 1.000 -> 0.955 - miners can earn again |
| `sn35:burn_drop:0.700` | 35 | BURN_DROP | 2026-11-28T09:29:51Z | sn35 burn fell 1.000 -> 0.700 - miners can earn again |
| `sn76:burn_drop:0.950` | 76 | BURN_DROP | 2026-11-28T09:29:51Z | sn76 burn fell 0.999 -> 0.950 - miners can earn again |
| `sn130:new_subnet:b9604508` | 130 | NEW_SUBNET | 2026-11-28T09:29:51Z | NEW SUBNET sn130 "sha" first seen |
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
| `sn70:release:build-v2026.11.22: ci: 90-minute limits ` | 70 | RELEASE | 2026-11-22T22:26:39Z | sn70 released build-v2026.11.22: ci: 90-minute limits for the test jobs |
| `sn71:scoring_commit:2026-11-22T20:43:38Z` | 71 | SCORING_COMMIT | 2026-11-22T22:26:39Z | sn71 commit touches scoring: Stop assigning execution to a validator missing the sandbox installer |
| `sn91:scoring_commit:2026-11-22T22:00:58Z` | 91 | SCORING_COMMIT | 2026-11-22T22:26:39Z | sn91 commit touches scoring: docs(laned): WB20 lane B in MINER, INTERFACE, AGENT_MINING and VALIDA… |
| `sn21:scoring_commit:2026-11-22T09:08:18Z` | 21 | SCORING_COMMIT | 2026-11-23T03:01:39Z | sn21 commit touches scoring: docs(scoring): the exact calculation written down (periods, measured … |
| `sn70:release:Miner image image-v2026.11.22b (v0.7.0, ` | 70 | RELEASE | 2026-11-23T03:01:39Z | sn70 released Miner image image-v2026.11.22b (v0.7.0, protocol v4) |
| `sn70:scoring_commit:2026-11-22T21:38:33Z` | 70 | SCORING_COMMIT | 2026-11-23T03:01:39Z | sn70 commit touches scoring: docs: the validator guide's v4 READY line in the order the validator … |
| `sn71:scoring_commit:2026-11-22T22:55:58Z` | 71 | SCORING_COMMIT | 2026-11-23T03:01:39Z | sn71 commit touches scoring: Preserve a normal execution attempt after verified zero-cost installe… |
| `sn91:scoring_commit:2026-11-23T02:43:11Z` | 91 | SCORING_COMMIT | 2026-11-23T03:01:39Z | sn91 commit touches scoring: fix(laned): W0c list WB16 as a verification WP (D40 option (a) is tod… |
| `sn111:scoring_commit:2026-11-22T23:52:08Z` | 111 | SCORING_COMMIT | 2026-11-23T03:01:39Z | sn111 commit touches scoring: Verify arbiter-confirmed source corrections after unresolved independ… |
| `sn12:release:miner-testing-2026-11-23-45138900060-7-1` | 12 | RELEASE | 2026-11-23T12:19:17Z | sn12 released miner-testing-2026-11-23-45138900060-7-1: feat: preserve commitment envelopes written by others (#878) |
| `sn42:release:v0.6.26` | 42 | RELEASE | 2026-11-23T12:19:17Z | sn42 released v0.6.26 |
| `sn42:scoring_commit:2026-11-23T07:20:49Z` | 42 | SCORING_COMMIT | 2026-11-23T12:19:17Z | sn42 commit touches scoring: release 0.6.26: the miner stats answer reads the votes once |
| `sn51:release:watchtower-v1.2.4` | 51 | RELEASE | 2026-11-23T12:19:17Z | sn51 released watchtower-v1.2.4 |
| `sn51:scoring_commit:2026-11-23T11:36:21Z` | 51 | SCORING_COMMIT | 2026-11-23T12:19:17Z | sn51 commit touches scoring: DAH-6582 - Executor and validator: update a bundled binary (#2377) |
| `sn56:scoring_commit:2026-11-23T11:33:11Z` | 56 | SCORING_COMMIT | 2026-11-23T12:19:17Z | sn56 commit touches scoring: Build and publish the quant evaluator image in CI (#1450) |
| `sn71:scoring_commit:2026-11-23T11:53:12Z` | 71 | SCORING_COMMIT | 2026-11-23T12:19:17Z | sn71 commit touches scoring: Set the verified AWS region for the pilot worker |
| `sn91:scoring_commit:2026-11-23T10:27:12Z` | 91 | SCORING_COMMIT | 2026-11-23T12:19:17Z | sn91 commit touches scoring: feat(laned): W7d satellite verifies the rev6.6 armed context set (#750 |
| `sn94:scoring_commit:2026-11-23T09:00:13Z` | 94 | SCORING_COMMIT | 2026-11-23T12:19:17Z | sn94 commit touches scoring: Count a fresh pass from the challenge, not the verdict (AB#947) (#691) |
| `sn99:scoring_commit:2026-11-23T09:28:54Z` | 99 | SCORING_COMMIT | 2026-11-23T12:19:17Z | sn99 commit touches scoring: A champion is evaluated on benchmarks added after it, rebuilt as admi… |
| `sn12:release:validator-staging-2026-11-23-45269217986` | 12 | RELEASE | 2026-11-24T00:11:22Z | sn12 released validator-staging-2026-11-23-45269217986-635-1: feat: executor download cache (#879) |
| `sn18:release:Release 2.1.5` | 18 | RELEASE | 2026-11-24T00:11:22Z | sn18 released Release 2.1.5 |
| `sn28:release:v0.6.0` | 28 | RELEASE | 2026-11-24T00:11:22Z | sn28 released v0.6.0 |
| `sn39:scoring_commit:2026-11-23T19:58:33Z` | 39 | SCORING_COMMIT | 2026-11-24T00:11:22Z | sn39 commit touches scoring: never repair a day scored with its profit not counted |
| `sn51:scoring_commit:2026-11-23T23:17:44Z` | 51 | SCORING_COMMIT | 2026-11-24T00:11:22Z | sn51 commit touches scoring: DAH-7005 - [P4] Validator: one miner snapshot per cycle for the payme… |
| `sn56:scoring_commit:2026-11-23T18:00:27Z` | 56 | SCORING_COMMIT | 2026-11-24T00:11:22Z | sn56 commit touches scoring: Reuse the Docker layer cache for miner image builds (#1456) |
| `sn67:scoring_commit:2026-11-23T06:17:42Z` | 67 | SCORING_COMMIT | 2026-11-24T00:11:22Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20261123.post1 |
| `sn71:scoring_commit:2026-11-23T12:52:03Z` | 71 | SCORING_COMMIT | 2026-11-24T00:11:22Z | sn71 commit touches scoring: Recover funded pilot attempts without replaying completed miner work |
| `sn91:scoring_commit:2026-11-23T20:48:50Z` | 91 | SCORING_COMMIT | 2026-11-24T00:11:22Z | sn91 commit touches scoring: tests(laned): WB23 miner-chosen lane B leg length acceptance tests (t… |
| `sn92:release:v1.2.0-rc11.post8.16` | 92 | RELEASE | 2026-11-24T00:11:22Z | sn92 released v1.2.0-rc11.post8.16 |
| `sn92:scoring_commit:2026-11-23T15:05:00Z` | 92 | SCORING_COMMIT | 2026-11-24T00:11:22Z | sn92 commit touches scoring: 1.2.0rc11.post8.16: validator source as live since 19 Nov 2026 |
| `sn111:scoring_commit:2026-11-23T23:07:32Z` | 111 | SCORING_COMMIT | 2026-11-24T00:11:22Z | sn111 commit touches scoring: Raise validator source and structured review limits to 128k and 64k |
| `sn116:scoring_commit:2026-11-23T20:09:13Z` | 116 | SCORING_COMMIT | 2026-11-24T00:11:22Z | sn116 commit touches scoring: Ladder: every document a miner was shown is kept append-only (DATA pl… |
| `sn117:release:everycli v1.2.7` | 117 | RELEASE | 2026-11-24T00:11:22Z | sn117 released everycli v1.2.7 |
| `sn51:release:executor-v1.196` | 51 | RELEASE | 2026-11-24T10:13:41Z | sn51 released executor-v1.196 |
| `sn51:scoring_commit:2026-11-24T09:17:23Z` | 51 | SCORING_COMMIT | 2026-11-24T10:13:41Z | sn51 commit touches scoring: DAH-6847 - [P4] Validator: a GPU whose clock reset fails before a cre… |
| `sn56:scoring_commit:2026-11-24T02:50:01Z` | 56 | SCORING_COMMIT | 2026-11-24T10:13:41Z | sn56 commit touches scoring: Bound the database use of the per-miner boss comparisons (#1464) |
| `sn61:release:4.11.1` | 61 | RELEASE | 2026-11-24T10:13:41Z | sn61 released 4.11.1 |
| `sn61:scoring_commit:2026-11-24T08:10:44Z` | 61 | SCORING_COMMIT | 2026-11-24T10:13:41Z | sn61 commit touches scoring: feat: update bot virus challenge configuration and incentives |
| `sn70:scoring_commit:2026-11-24T03:24:26Z` | 70 | SCORING_COMMIT | 2026-11-24T10:13:41Z | sn70 commit touches scoring: Merge pull request #211 from fugal-ai/docs/miner-guide-missing-row |
| `sn71:scoring_commit:2026-11-24T09:29:58Z` | 71 | SCORING_COMMIT | 2026-11-24T10:13:41Z | sn71 commit touches scoring: Authorize bounded fixed correction quotes after ordinary reward cutove |
| `sn82:scoring_commit:2026-11-24T06:05:34Z` | 82 | SCORING_COMMIT | 2026-11-24T10:13:41Z | sn82 commit touches scoring: Document live Mainnet V2.1 scoring |
| `sn91:scoring_commit:2026-11-24T09:25:44Z` | 91 | SCORING_COMMIT | 2026-11-24T10:13:41Z | sn91 commit touches scoring: feat(laned): WB27 lane B miner levers, 12 h legs, token/hour limits, … |
| `sn98:scoring_commit:2026-11-24T04:57:47Z` | 98 | SCORING_COMMIT | 2026-11-24T10:13:41Z | sn98 commit touches scoring: feat: add light validator mode that copies the main validator's weigh… |
| `sn99:scoring_commit:2026-11-23T18:56:12Z` | 99 | SCORING_COMMIT | 2026-11-24T10:13:41Z | sn99 commit touches scoring: Board: the champion's match row shows its scores on benchmarks added … |
| `sn116:scoring_commit:2026-11-24T09:00:58Z` | 116 | SCORING_COMMIT | 2026-11-24T10:13:41Z | sn116 commit touches scoring: miner_lookup re-run charged: release LINT_DIFF_2dd8f459.diff (sha256 … |
| `sn117:release:everycli v1.3.0` | 117 | RELEASE | 2026-11-24T10:13:41Z | sn117 released everycli v1.3.0 |
| `sn12:release:validator-staging-2026-11-24-45412581463` | 12 | RELEASE | 2026-11-24T20:45:14Z | sn12 released validator-staging-2026-11-24-45412581463-636-1: feat: added always_on__cpu__2c__4gb executor class (#865) (#881) |
| `sn39:scoring_commit:2026-11-24T16:04:31Z` | 39 | SCORING_COMMIT | 2026-11-24T20:45:14Z | sn39 commit touches scoring: Merge pull request #34 from kokoahdotcom/kokoah-dev/validator-setup |
| `sn42:scoring_commit:2026-11-24T15:24:55Z` | 42 | SCORING_COMMIT | 2026-11-24T20:45:14Z | sn42 commit touches scoring: miner prompt: a community model comes from a site whose terms allow a… |
| `sn50:release:1.16.0` | 50 | RELEASE | 2026-11-24T20:45:14Z | sn50 released 1.16.0 |
| `sn50:scoring_commit:2026-11-24T17:12:09Z` | 50 | SCORING_COMMIT | 2026-11-24T20:45:14Z | sn50 commit touches scoring: Add a synth-miner Claude Code skill and a one-go GCP miner deploy (#35 |
| `sn51:scoring_commit:2026-11-24T15:29:13Z` | 51 | SCORING_COMMIT | 2026-11-24T20:45:14Z | sn51 commit touches scoring: DAH-7069 - Validator: log VerifyX per-test times, wave duration and C… |
| `sn61:scoring_commit:2026-11-24T11:24:25Z` | 61 | SCORING_COMMIT | 2026-11-24T20:45:14Z | sn61 commit touches scoring: docs: update Bot Virus challenge documentation and navigation for v2 |
| `sn71:scoring_commit:2026-11-24T18:53:32Z` | 71 | SCORING_COMMIT | 2026-11-24T20:45:14Z | sn71 commit touches scoring: Verify retired champion weights before collection payouts start |
| `sn91:scoring_commit:2026-11-24T13:36:13Z` | 91 | SCORING_COMMIT | 2026-11-24T20:45:14Z | sn91 commit touches scoring: feat(miner): lane-b test previews with the validators' judge_expert_s… |
| `sn92:release:v1.2.0-rc11.post8.19` | 92 | RELEASE | 2026-11-24T20:45:14Z | sn92 released v1.2.0-rc11.post8.19 |
| `sn99:scoring_commit:2026-11-24T15:15:25Z` | 99 | SCORING_COMMIT | 2026-11-24T20:45:14Z | sn99 commit touches scoring: Evaluation-host transfers resume a cut file instead of starting over;… |
| `sn116:scoring_commit:2026-11-24T17:30:47Z` | 116 | SCORING_COMMIT | 2026-11-24T20:45:14Z | sn116 commit touches scoring: King hand-over: the previous king's miner starts a fresh decay clock … |
| `sn117:release:everycli v1.3.2` | 117 | RELEASE | 2026-11-24T20:45:14Z | sn117 released everycli v1.3.2 |
| `sn25:scoring_commit:2026-11-24T21:59:07Z` | 25 | SCORING_COMMIT | 2026-11-25T03:48:50Z | sn25 commit touches scoring: Merge docs/validator-rate-class-1125: the operator guide says how the… |
| `sn51:scoring_commit:2026-11-24T23:35:30Z` | 51 | SCORING_COMMIT | 2026-11-25T03:48:50Z | sn51 commit touches scoring: DAH-6876 - [P4] Validator: our own s3fs volume plugin on current s3fs… |
| `sn53:scoring_commit:2026-11-25T01:18:15Z` | 53 | SCORING_COMMIT | 2026-11-25T03:48:50Z | sn53 commit touches scoring: Merge pull request #68 from hanlinai/feat/miner-health-load-urls |
| `sn56:scoring_commit:2026-11-24T22:52:06Z` | 56 | SCORING_COMMIT | 2026-11-25T03:48:50Z | sn56 commit touches scoring: Remove organic task endpoints and unused validator routes (#1467) |
| `sn66:release:v2026.11.25` | 66 | RELEASE | 2026-11-25T03:48:50Z | sn66 released v2026.11.25 |
| `sn70:release:image-v2026.11.24 (SUPERSEDED by image-v` | 70 | RELEASE | 2026-11-25T03:48:50Z | sn70 released image-v2026.11.24 (SUPERSEDED by image-v2026.11.24b, do not use) |
| `sn70:scoring_commit:2026-11-25T02:32:34Z` | 70 | SCORING_COMMIT | 2026-11-25T03:48:50Z | sn70 commit touches scoring: v5: pay miners half the miner emission; the other half burns every epo |
| `sn71:scoring_commit:2026-11-24T23:36:29Z` | 71 | SCORING_COMMIT | 2026-11-25T03:48:50Z | sn71 commit touches scoring: Advance a verified settled pilot into one bounded reference cohort |
| `sn91:scoring_commit:2026-11-25T02:21:59Z` | 91 | SCORING_COMMIT | 2026-11-25T03:48:50Z | sn91 commit touches scoring: fix(validator): offloaded bench sweeps resolve uv on the host (#903) … |
| `sn111:scoring_commit:2026-11-25T02:02:53Z` | 111 | SCORING_COMMIT | 2026-11-25T03:48:50Z | sn111 commit touches scoring: Include replay driver used by scientific launch verification |
| `sn116:scoring_commit:2026-11-24T22:36:14Z` | 116 | SCORING_COMMIT | 2026-11-25T03:48:50Z | sn116 commit touches scoring: Motor 1.8 switch: the miner texts that state the score (MINING.md, th… |
| `sn12:release:validator-staging-2026-11-25-45557483497` | 12 | RELEASE | 2026-11-25T14:12:53Z | sn12 released validator-staging-2026-11-25-45557483497-637-1: feat: allow commitments up to 512 bytes (#880) |
| `sn22:scoring_commit:2026-11-25T09:37:24Z` | 22 | SCORING_COMMIT | 2026-11-25T14:12:53Z | sn22 commit touches scoring: fix(task-api): the signed log, anchors, verdicts, final verdicts, vot… |
| `sn25:scoring_commit:2026-11-25T06:15:46Z` | 25 | SCORING_COMMIT | 2026-11-25T14:12:53Z | sn25 commit touches scoring: Merge docs/validator-data-grant-1125: the operator guide says an admi… |
| `sn26:scoring_commit:2026-11-25T13:27:38Z` | 26 | SCORING_COMMIT | 2026-11-25T14:12:53Z | sn26 commit touches scoring: Report: round the displayed score |
| `sn28:release:v0.6.1` | 28 | RELEASE | 2026-11-25T14:12:53Z | sn28 released v0.6.1 |
| `sn40:scoring_commit:2026-11-25T13:58:42Z` | 40 | SCORING_COMMIT | 2026-11-25T14:12:53Z | sn40 commit touches scoring: Merge pull request #20 from RalphLabsAI/feat/reward-allocation |
| `sn51:release:executor-v1.198` | 51 | RELEASE | 2026-11-25T14:12:53Z | sn51 released executor-v1.198 |
| `sn51:scoring_commit:2026-11-25T11:35:09Z` | 51 | SCORING_COMMIT | 2026-11-25T14:12:53Z | sn51 commit touches scoring: DAH-6967 - [P3] Validator: a rented pod read while its files go back … |
| `sn56:scoring_commit:2026-11-25T12:39:19Z` | 56 | SCORING_COMMIT | 2026-11-25T14:12:53Z | sn56 commit touches scoring: Update roadmap: reward split and GRPO task revamp (#1471) |
| `sn67:scoring_commit:2026-11-24T11:14:02Z` | 67 | SCORING_COMMIT | 2026-11-25T14:12:53Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20261124.post0 |
| `sn71:scoring_commit:2026-11-25T07:29:04Z` | 71 | SCORING_COMMIT | 2026-11-25T14:12:53Z | sn71 commit touches scoring: Merge pull request #1374 from leadpoet/docs/miner-collection-price-ru… |
| `sn94:scoring_commit:2026-11-25T11:51:05Z` | 94 | SCORING_COMMIT | 2026-11-25T14:12:53Z | sn94 commit touches scoring: Check the signed approved list in verify_receipts.py (AB#968, plan PR… |
| `sn99:scoring_commit:2026-11-24T16:43:07Z` | 99 | SCORING_COMMIT | 2026-11-25T14:12:53Z | sn99 commit touches scoring: Evaluation machines hold the benchmarks of every rules version of the… |
| `sn116:scoring_commit:2026-11-25T04:10:17Z` | 116 | SCORING_COMMIT | 2026-11-25T14:12:53Z | sn116 commit touches scoring: The published reader reads an absent tasks_per_epoch as every task, a… |
| `sn120:scoring_commit:2026-11-25T04:00:06Z` | 120 | SCORING_COMMIT | 2026-11-25T14:12:53Z | sn120 commit touches scoring: Merge pull request #322 from AffineFoundation/bb/miner-kl-local |
| `sn39:scoring_commit:2026-11-25T14:35:44Z` | 39 | SCORING_COMMIT | 2026-11-25T23:12:10Z | sn39 commit touches scoring: state that spot fills count for the volume reward from 2026-11-27 |
| `sn51:scoring_commit:2026-11-25T15:01:23Z` | 51 | SCORING_COMMIT | 2026-11-25T23:12:10Z | sn51 commit touches scoring: DAH-6683 - [P0] Validator backup, restore and login check run only it… |
| `sn53:scoring_commit:2026-11-25T14:51:22Z` | 53 | SCORING_COMMIT | 2026-11-25T23:12:10Z | sn53 commit touches scoring: Merge pull request #69 from hanlinai/feat/miner-first-chunk-usage |
| `sn111:scoring_commit:2026-11-25T14:30:50Z` | 111 | SCORING_COMMIT | 2026-11-25T23:12:10Z | sn111 commit touches scoring: Activate staged experimental scientific scoring with shared concurrenc |
| `sn117:release:everycli v1.3.3` | 117 | RELEASE | 2026-11-25T23:12:10Z | sn117 released everycli v1.3.3 |
| `sn127:release:Release eb41ab3` | 127 | RELEASE | 2026-11-25T23:12:10Z | sn127 released Release eb41ab3 |
| `sn25:scoring_commit:2026-11-26T00:03:59Z` | 25 | SCORING_COMMIT | 2026-11-26T05:17:33Z | sn25 commit touches scoring: Merge miner-update-sn-feed: miner self-updates from urfoundation/sn r… |
| `sn30:scoring_commit:2026-11-11T11:39:54Z` | 30 | SCORING_COMMIT | 2026-11-26T05:17:33Z | sn30 commit touches scoring: feat(scoring): weight 30d EMAs by maturity in the blended score (2045… |
| `sn51:release:executor-v1.199` | 51 | RELEASE | 2026-11-26T05:17:33Z | sn51 released executor-v1.199 |
| `sn51:scoring_commit:2026-11-26T04:19:12Z` | 51 | SCORING_COMMIT | 2026-11-26T05:17:33Z | sn51 commit touches scoring: DAH-7109 - [P4] Validator stale-container cleanup: one SSH call per w… |
| `sn67:scoring_commit:2026-11-25T11:19:12Z` | 67 | SCORING_COMMIT | 2026-11-26T05:17:33Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20261125.post4 |
| `sn70:scoring_commit:2026-11-26T00:53:59Z` | 70 | SCORING_COMMIT | 2026-11-26T05:17:33Z | sn70 commit touches scoring: Merge pull request #218 from fugal-ai/ops/validator-autoupdate |
| `sn71:scoring_commit:2026-11-26T02:52:24Z` | 71 | SCORING_COMMIT | 2026-11-26T05:17:33Z | sn71 commit touches scoring: Merge pull request #1378 from leadpoet/feat/pay-verified-collection |
| `sn82:scoring_commit:2026-11-26T01:05:42Z` | 82 | SCORING_COMMIT | 2026-11-26T05:17:33Z | sn82 commit touches scoring: Use live runtime metadata for miner report submissions |
| `sn91:scoring_commit:2026-11-25T23:31:05Z` | 91 | SCORING_COMMIT | 2026-11-26T05:17:33Z | sn91 commit touches scoring: feat(pool): pool_d takes lane A's selection from the sha-verified sna… |
| `sn14:scoring_commit:2026-11-24T10:33:33Z` | 14 | SCORING_COMMIT | 2026-11-26T15:34:43Z | sn14 commit touches scoring: Start the scored span at the cold-round release and grade every load'… |
| `sn42:release:v0.6.27` | 42 | RELEASE | 2026-11-26T15:34:43Z | sn42 released v0.6.27 |
| `sn42:scoring_commit:2026-11-26T10:18:12Z` | 42 | SCORING_COMMIT | 2026-11-26T15:34:43Z | sn42 commit touches scoring: miners: work an improvement job; the practice command and the second … |
| `sn51:release:executor-v1.201` | 51 | RELEASE | 2026-11-26T15:34:43Z | sn51 released executor-v1.201 |
| `sn51:scoring_commit:2026-11-26T10:12:10Z` | 51 | SCORING_COMMIT | 2026-11-26T15:34:43Z | sn51 commit touches scoring: DAH-7044 - [P4] Validation: a node is listed only after a rental prob… |
| `sn67:scoring_commit:2026-11-26T08:41:17Z` | 67 | SCORING_COMMIT | 2026-11-26T15:34:43Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20261126.post0 |
| `sn81:scoring_commit:2026-11-26T14:21:56Z` | 81 | SCORING_COMMIT | 2026-11-26T15:34:43Z | sn81 commit touches scoring: Merge pull request #583 from reliquadotai/fix/restart-keeps-miners |
| `sn91:scoring_commit:2026-11-26T08:47:43Z` | 91 | SCORING_COMMIT | 2026-11-26T15:34:43Z | sn91 commit touches scoring: fix(trainer): lane B judge + merge scores on the eval pod (WB27, stac… |
| `sn116:scoring_commit:2026-11-26T08:59:32Z` | 116 | SCORING_COMMIT | 2026-11-26T15:34:43Z | sn116 commit touches scoring: An overlay dispatch for a Challenge the image registry declares, with… |
| `sn12:release:miner-staging-2026-11-26-45857591810-467` | 12 | RELEASE | 2026-11-27T00:03:58Z | sn12 released miner-staging-2026-11-26-45857591810-467-1: fix: stop the executor's job containers in kill_executor (#884) |
| `sn51:release:watchtower-v1.2.5` | 51 | RELEASE | 2026-11-27T00:03:58Z | sn51 released watchtower-v1.2.5 |
| `sn51:scoring_commit:2026-11-26T22:03:47Z` | 51 | SCORING_COMMIT | 2026-11-27T00:03:58Z | sn51 commit touches scoring: DAH-5238 - [P4] Validator reads liumd's containerd-store disk fields … |
| `sn71:scoring_commit:2026-11-26T22:01:56Z` | 71 | SCORING_COMMIT | 2026-11-27T00:03:58Z | sn71 commit touches scoring: Explain consensus-based payouts before a miner signs a funding offer |
| `sn90:scoring_commit:2026-11-26T17:29:48Z` | 90 | SCORING_COMMIT | 2026-11-27T00:03:58Z | sn90 commit touches scoring: docs(attestation): registry-lookup verification + current+previous re… |
| `sn94:scoring_commit:2026-11-26T20:14:02Z` | 94 | SCORING_COMMIT | 2026-11-27T00:03:58Z | sn94 commit touches scoring: Roll guest-TLS and miner-mode sealed hotels (chi-ur-2) (#768) |
| `sn116:scoring_commit:2026-11-26T23:47:03Z` | 116 | SCORING_COMMIT | 2026-11-27T00:03:58Z | sn116 commit touches scoring: Merge miner error rows 630c36c4 onto the docs restack 2272a51a (owner… |
| `sn117:release:everycli v1.3.4` | 117 | RELEASE | 2026-11-27T00:03:58Z | sn117 released everycli v1.3.4 |
| `sn30:release:v0.1.4 — Archive resilience and horizon-` | 30 | RELEASE | 2026-11-27T08:16:24Z | sn30 released v0.1.4 — Archive resilience and horizon-maturity blend, protocol 2045 |
| `sn51:release:executor-v1.202` | 51 | RELEASE | 2026-11-27T08:16:24Z | sn51 released executor-v1.202 |
| `sn51:scoring_commit:2026-11-27T07:53:24Z` | 51 | SCORING_COMMIT | 2026-11-27T08:16:24Z | sn51 commit touches scoring: DAH-7201 - [P4] Validator: report a restarting rented container in it… |
| `sn61:release:4.12.0` | 61 | RELEASE | 2026-11-27T08:16:24Z | sn61 released 4.12.0 |
| `sn61:scoring_commit:2026-11-27T06:01:39Z` | 61 | SCORING_COMMIT | 2026-11-27T08:16:24Z | sn61 commit touches scoring: refactor: update bot virus challenge version and increase incentive w… |
| `sn71:scoring_commit:2026-11-27T07:29:52Z` | 71 | SCORING_COMMIT | 2026-11-27T08:16:24Z | sn71 commit touches scoring: Run standing funded experiments and verify completed work separately … |
| `sn91:scoring_commit:2026-11-27T01:40:59Z` | 91 | SCORING_COMMIT | 2026-11-27T08:16:24Z | sn91 commit touches scoring: fix(lane-d): public half throughput: warm sweep, parallel reads, scor… |
| `sn116:scoring_commit:2026-11-27T01:56:58Z` | 116 | SCORING_COMMIT | 2026-11-27T08:16:24Z | sn116 commit touches scoring: fix(rewards): fix SN116 Subtensor chain reads and commit-reveal tempo… |
| `sn127:release:Release d92abe3` | 127 | RELEASE | 2026-11-27T08:16:24Z | sn127 released Release d92abe3 |
| `sn25:release:v2026.11.27-1110314090` | 25 | RELEASE | 2026-11-28T09:29:51Z | sn25 released v2026.11.27-1110314090 |
| `sn25:scoring_commit:2026-11-28T01:57:12Z` | 25 | SCORING_COMMIT | 2026-11-28T09:29:51Z | sn25 commit touches scoring: Merge feat/pkg-managed-update-1128: a package-managed miner is update… |
| `sn35:scoring_commit:2026-11-28T04:12:36Z` | 35 | SCORING_COMMIT | 2026-11-28T09:29:51Z | sn35 commit touches scoring: The validator guide says how to publish the Google app, so the YouTub… |
| `sn37:scoring_commit:2026-11-28T03:05:52Z` | 37 | SCORING_COMMIT | 2026-11-28T09:29:51Z | sn37 commit touches scoring: docs: record the runtime 497 serving and funding client verification |
| `sn56:scoring_commit:2026-11-28T07:30:58Z` | 56 | SCORING_COMMIT | 2026-11-28T09:29:51Z | sn56 commit touches scoring: Incoming change: image eval update and harder synthetic image tasks (… |
| `sn61:scoring_commit:2026-11-28T03:01:20Z` | 61 | SCORING_COMMIT | 2026-11-28T09:29:51Z | sn61 commit touches scoring: docs: update the documentation of ada challenge |
| `sn71:scoring_commit:2026-11-28T06:33:22Z` | 71 | SCORING_COMMIT | 2026-11-28T09:29:51Z | sn71 commit touches scoring: Verify registered programs end to end and avoid starting unfunded lane |
| `sn81:scoring_commit:2026-11-28T04:59:39Z` | 81 | SCORING_COMMIT | 2026-11-28T09:29:51Z | sn81 commit touches scoring: Merge pull request #601 from reliquadotai/feat/rl-like-any-task |
| `sn91:release:worker-v2.1.0-mkt-rc3` | 91 | RELEASE | 2026-11-28T09:29:51Z | sn91 released worker-v2.1.0-mkt-rc3 |
| `sn91:scoring_commit:2026-11-28T05:25:21Z` | 91 | SCORING_COMMIT | 2026-11-28T09:29:51Z | sn91 commit touches scoring: feat(lanes): miner-visible queue reasons and settled verdicts (WB27) … |
| `sn111:release:v2.1.0` | 111 | RELEASE | 2026-11-28T09:29:51Z | sn111 released v2.1.0 |
| `sn117:release:everycli v1.3.5` | 117 | RELEASE | 2026-11-28T09:29:51Z | sn117 released everycli v1.3.5 |
| `sn99:readme_task_diff:99418d103a242136` | 99 | README_TASK_DIFF | 2026-11-22T17:04:41Z | sn99 README task/scoring sections changed |
| `sn21:readme_task_diff:b07e6d388638dba8` | 21 | README_TASK_DIFF | 2026-11-23T03:01:39Z | sn21 README task/scoring sections changed |
| `sn39:readme_task_diff:5cdeac4cf1a1b4ef` | 39 | README_TASK_DIFF | 2026-11-24T10:13:41Z | sn39 README task/scoring sections changed |
| `sn82:readme_task_diff:123c16fec7afb63e` | 82 | README_TASK_DIFF | 2026-11-24T10:13:41Z | sn82 README task/scoring sections changed |
| `sn91:readme_task_diff:fd8a0ae169ba905a` | 91 | README_TASK_DIFF | 2026-11-24T10:13:41Z | sn91 README task/scoring sections changed |
| `sn91:readme_task_diff:412ce547772ecf5b` | 91 | README_TASK_DIFF | 2026-11-25T03:48:50Z | sn91 README task/scoring sections changed |
| `sn40:readme_task_diff:2cd1a56dd0799e4e` | 40 | README_TASK_DIFF | 2026-11-25T14:12:53Z | sn40 README task/scoring sections changed |
| `sn91:readme_task_diff:3ebcee68f1d40f73` | 91 | README_TASK_DIFF | 2026-11-25T14:12:53Z | sn91 README task/scoring sections changed |
| `sn121:readme_task_diff:818bbda8fbb171f3` | 121 | README_TASK_DIFF | 2026-11-25T23:12:10Z | sn121 README task/scoring sections changed |
| `sn42:readme_task_diff:62fb90a94c705fb4` | 42 | README_TASK_DIFF | 2026-11-26T15:34:43Z | sn42 README task/scoring sections changed |
| `sn6:readme_task_diff:a7d63b5e8f360b67` | 6 | README_TASK_DIFF | 2026-11-27T00:03:58Z | sn6 README task/scoring sections changed |
| `sn124:readme_task_diff:0e536c389e88ce2e` | 124 | README_TASK_DIFF | 2026-11-27T00:03:58Z | sn124 README task/scoring sections changed |
| `sn37:readme_task_diff:f65f6f7a75609304` | 37 | README_TASK_DIFF | 2026-11-28T09:29:51Z | sn37 README task/scoring sections changed |

## RESOLVED IN THIS WINDOW

_none_
