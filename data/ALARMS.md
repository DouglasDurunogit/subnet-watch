# ALARMS - generated 2026-09-12T17:07:11Z, block 9052890

window: first_seen in [2026-09-12T15:52:44Z, 2026-09-12T17:07:44Z)  (60 min interval + 15 min overlap)

Report ONLY the rows under NEW SINCE LAST RUN. Rows under STILL OPEN were
already reported in an earlier window and must not be re-alarmed.

## NEW SINCE LAST RUN

| event_id | netuid | class | severity | first_seen_utc | one_line |
|---|---|---|---|---|---|
| `sn36:scoring_commit:2026-09-11T11:52:07Z` | 36 | SCORING_COMMIT | P1 | 2026-09-12T17:07:44Z | sn36 commit touches scoring: Run calibration once a day on 200 tasks, in the background |
| `sn71:scoring_commit:2026-09-12T16:43:22Z` | 71 | SCORING_COMMIT | P1 | 2026-09-12T17:07:44Z | sn71 commit touches scoring: Set daily Arena admission to twenty challengers |
| `sn92:scoring_commit:2026-09-12T14:25:40Z` | 92 | SCORING_COMMIT | P1 | 2026-09-12T17:07:44Z | sn92 commit touches scoring: tracks: the hallucination detection track is guard on mt-4g, scored b… |

### detail

- **`sn36:scoring_commit:2026-09-11T11:52:07Z`** - sn36 commit touches scoring: Run calibration once a day on 200 tasks, in the background
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn71:scoring_commit:2026-09-12T16:43:22Z`** - sn71 commit touches scoring: Set daily Arena admission to twenty challengers
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn92:scoring_commit:2026-09-12T14:25:40Z`** - sn92 commit touches scoring: tracks: the hallucination detection track is guard on mt-4g, scored b…
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.

## STILL OPEN (already reported - do not re-alarm)

| event_id | netuid | class | first_seen_utc | one_line |
|---|---|---|---|---|
| `sn47:burn_drop:0.942` | 47 | BURN_DROP | 2026-09-06T16:12:33Z | sn47 burn fell 1.000 -> 0.942 - miners can earn again |
| `sn34:burn_drop:0.799` | 34 | BURN_DROP | 2026-09-08T17:34:23Z | sn34 burn fell 1.000 -> 0.799 - miners can earn again |
| `sn121:burn_drop:0.610` | 121 | BURN_DROP | 2026-09-08T17:34:23Z | sn121 burn fell 1.000 -> 0.610 - miners can earn again |
| `sn78:weights_version_bump:1` | 78 | WEIGHTS_VERSION_BUMP | 2026-09-08T22:52:47Z | sn78 weights_version 0 -> 1 |
| `sn78:weights_version_bump:4294967296` | 78 | WEIGHTS_VERSION_BUMP | 2026-09-09T21:17:06Z | sn78 weights_version 1 -> 4294967296 |
| `sn104:burn_drop:0.988` | 104 | BURN_DROP | 2026-09-09T21:17:06Z | sn104 burn fell 1.000 -> 0.988 - miners can earn again |
| `sn20:burn_drop:0.770` | 20 | BURN_DROP | 2026-09-11T01:19:31Z | sn20 burn fell 1.000 -> 0.770 - miners can earn again |
| `sn20:burn_drop:0.742` | 20 | BURN_DROP | 2026-09-12T06:24:23Z | sn20 burn fell 1.000 -> 0.742 - miners can earn again |
| `sn21:scoring_commit:2026-09-05T16:25:15Z` | 21 | SCORING_COMMIT | 2026-09-05T18:13:16Z | sn21 commit touches scoring: fix(reporting): rows shown with their accuracy are scored rows; audit… |
| `sn71:scoring_commit:2026-09-05T16:23:27Z` | 71 | SCORING_COMMIT | 2026-09-05T18:13:16Z | sn71 commit touches scoring: build: refresh reviewed gateway verifier workflow hashes |
| `sn25:scoring_commit:2026-09-05T19:18:14Z` | 25 | SCORING_COMMIT | 2026-09-05T20:34:23Z | sn25 commit touches scoring: Protect validator seed custody and qualify producer gate coverage |
| `sn71:scoring_commit:2026-09-05T20:23:45Z` | 71 | SCORING_COMMIT | 2026-09-05T20:34:23Z | sn71 commit touches scoring: Bind validator workflow to archive retry policy |
| `sn78:scoring_commit:2026-09-05T14:56:55Z` | 78 | SCORING_COMMIT | 2026-09-05T20:34:23Z | sn78 commit touches scoring: Add external miner pilot launch handoffs |
| `sn7:release:release-20260905-204833` | 7 | RELEASE | 2026-09-05T22:21:43Z | sn7 released release-20260905-204833 |
| `sn71:scoring_commit:2026-09-05T21:34:19Z` | 71 | SCORING_COMMIT | 2026-09-05T22:21:43Z | sn71 commit touches scoring: chore(validator): bind existing recovery workflow identity |
| `sn74:release:release-20260905-223823` | 74 | RELEASE | 2026-09-06T00:06:30Z | sn74 released release-20260905-223823 |
| `sn74:scoring_commit:2026-09-05T20:51:26Z` | 74 | SCORING_COMMIT | 2026-09-06T00:06:30Z | sn74 commit touches scoring: serving miner: an attestation waits for prefill and holds admissions,… |
| `sn71:scoring_commit:2026-09-06T00:50:36Z` | 71 | SCORING_COMMIT | 2026-09-06T04:34:35Z | sn71 commit touches scoring: Isolate Arena failure regressions and verify prior publication contin… |
| `sn78:scoring_commit:2026-09-06T02:58:05Z` | 78 | SCORING_COMMIT | 2026-09-06T04:34:35Z | sn78 commit touches scoring: Add public registered-miner endpoint pilot |
| `sn25:scoring_commit:2026-09-06T12:28:31Z` | 25 | SCORING_COMMIT | 2026-09-06T12:51:56Z | sn25 commit touches scoring: Checkpoint held repair sources and validation handoff |
| `sn25:scoring_commit:2026-09-06T15:00:42Z` | 25 | SCORING_COMMIT | 2026-09-06T16:12:33Z | sn25 commit touches scoring: Integrate qualified Solidity validator activation verification |
| `sn14:release:GLM-5.3 mock mainnet submissions (valida` | 14 | RELEASE | 2026-09-06T18:30:56Z | sn14 released GLM-5.3 mock mainnet submissions (validator self-test, 2026-09-06) |
| `sn93:scoring_commit:2026-09-06T20:14:30Z` | 93 | SCORING_COMMIT | 2026-09-06T20:52:43Z | sn93 commit touches scoring: chore: scope validator deploy to code/config paths (#171) |
| `sn25:scoring_commit:2026-09-06T21:52:49Z` | 25 | SCORING_COMMIT | 2026-09-06T22:52:57Z | sn25 commit touches scoring: Record recovery checkpoints and post-pull monitoring validation |
| `sn34:release:5.0.0 — King of the Hill` | 34 | RELEASE | 2026-09-07T00:57:22Z | sn34 released 5.0.0 — King of the Hill |
| `sn91:scoring_commit:2026-09-04T21:55:54Z` | 91 | SCORING_COMMIT | 2026-09-07T00:57:22Z | sn91 commit touches scoring: receipt: publish every duelled challenger's diagnostics (cohort_stats) |
| `sn25:release:v2026.9.6-1039587510` | 25 | RELEASE | 2026-09-07T06:01:32Z | sn25 released v2026.9.6-1039587510 |
| `sn71:scoring_commit:2026-09-07T04:13:16Z` | 71 | SCORING_COMMIT | 2026-09-07T06:01:32Z | sn71 commit touches scoring: fix: verify active provider cache persistence |
| `sn18:release:Release 2.1.4` | 18 | RELEASE | 2026-09-07T12:22:04Z | sn18 released Release 2.1.4 |
| `sn18:scoring_commit:2026-09-07T08:25:21Z` | 18 | SCORING_COMMIT | 2026-09-07T12:22:04Z | sn18 commit touches scoring: Stop emissions for non-participating miners (#88) |
| `sn25:release:v2026.9.7-1039747440` | 25 | RELEASE | 2026-09-07T12:22:04Z | sn25 released v2026.9.7-1039747440 |
| `sn51:scoring_commit:2026-09-07T11:34:42Z` | 51 | SCORING_COMMIT | 2026-09-07T12:22:04Z | sn51 commit touches scoring: [P1] feat: run the miners tests and ruff format on every PR (#1289) |
| `sn66:release:v.1.0.3: Web submissions, payouts, contr` | 66 | RELEASE | 2026-09-07T12:22:04Z | sn66 released v.1.0.3: Web submissions, payouts, contributions... |
| `sn67:scoring_commit:2026-09-07T07:03:25Z` | 67 | SCORING_COMMIT | 2026-09-07T12:22:04Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20260907.post2 |
| `sn71:scoring_commit:2026-09-07T06:56:29Z` | 71 | SCORING_COMMIT | 2026-09-07T12:22:04Z | sn71 commit touches scoring: chore: bind verified controller upgrade recovery |
| `sn78:scoring_commit:2026-09-07T06:42:21Z` | 78 | SCORING_COMMIT | 2026-09-07T12:22:04Z | sn78 commit touches scoring: Harden macOS validator audit origin |
| `sn92:scoring_commit:2026-09-07T08:17:20Z` | 92 | SCORING_COMMIT | 2026-09-07T12:22:04Z | sn92 commit touches scoring: archive: a rewarded system is archived whatever state the leaderboard… |
| `sn1:release:v4.4.2` | 1 | RELEASE | 2026-09-07T17:49:43Z | sn1 released v4.4.2 |
| `sn25:release:v2026.9.7-1039843330` | 25 | RELEASE | 2026-09-07T17:49:43Z | sn25 released v2026.9.7-1039843330 |
| `sn34:scoring_commit:2026-09-07T16:11:18Z` | 34 | SCORING_COMMIT | 2026-09-07T17:49:43Z | sn34 commit touches scoring: Set explicit 100% burn and bypass reward calculation |
| `sn38:scoring_commit:2026-09-07T12:36:00Z` | 38 | SCORING_COMMIT | 2026-09-07T17:49:43Z | sn38 commit touches scoring: Update validator image to the latest version in docker-compose.valida… |
| `sn66:scoring_commit:2026-09-07T15:27:35Z` | 66 | SCORING_COMMIT | 2026-09-07T17:49:43Z | sn66 commit touches scoring: Merge pull request #76 from conjectures-io/fix/verifier-cache-readabl… |
| `sn10:scoring_commit:2026-09-07T19:27:24Z` | 10 | SCORING_COMMIT | 2026-09-07T21:28:22Z | sn10 commit touches scoring: Merge pull request #146 from Pareton-ai/arpan/reveal-miner-commits |
| `sn71:scoring_commit:2026-09-07T19:51:59Z` | 71 | SCORING_COMMIT | 2026-09-07T21:28:22Z | sn71 commit touches scoring: Merge remote-tracking branch 'origin/main' into codex/miner-promotion… |
| `sn78:scoring_commit:2026-09-07T20:51:50Z` | 78 | SCORING_COMMIT | 2026-09-07T21:28:22Z | sn78 commit touches scoring: Open miner pilot enrollment |
| `sn96:release:Verathos v0.2.1 – Sleipnir Cross-Machine` | 96 | RELEASE | 2026-09-07T21:28:22Z | sn96 released Verathos v0.2.1 – Sleipnir Cross-Machine Serving |
| `sn104:scoring_commit:2026-09-07T18:34:43Z` | 104 | SCORING_COMMIT | 2026-09-07T21:28:22Z | sn104 commit touches scoring: Merge pull request #10 from taostatus/feat/discord-key-announcements |
| `sn25:scoring_commit:2026-09-07T16:54:02Z` | 25 | SCORING_COMMIT | 2026-09-07T23:48:23Z | sn25 commit touches scoring: Checkpoint historical validator schedule and finalization progress |
| `sn78:scoring_commit:2026-09-07T23:46:59Z` | 78 | SCORING_COMMIT | 2026-09-07T23:48:23Z | sn78 commit touches scoring: Fix pilot deployment validation |
| `sn67:scoring_commit:2026-09-07T09:39:54Z` | 67 | SCORING_COMMIT | 2026-09-08T04:27:58Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20260907.post3 |
| `sn71:scoring_commit:2026-09-08T03:48:46Z` | 71 | SCORING_COMMIT | 2026-09-08T04:27:58Z | sn71 commit touches scoring: Verify staging SOURCE_ADD restart isolation |
| `sn74:release:release-20260908-031700` | 74 | RELEASE | 2026-09-08T04:27:58Z | sn74 released release-20260908-031700 |
| `sn92:scoring_commit:2026-09-08T00:30:17Z` | 92 | SCORING_COMMIT | 2026-09-08T04:27:58Z | sn92 commit touches scoring: cost is total task latency for every system; empty profile responses … |
| `sn100:scoring_commit:2026-09-08T02:08:11Z` | 100 | SCORING_COMMIT | 2026-09-08T04:27:58Z | sn100 commit touches scoring: fix(proof): stage proxy model + holdout for live score (#234) |
| `sn66:scoring_commit:2026-09-08T04:45:40Z` | 66 | SCORING_COMMIT | 2026-09-08T09:02:01Z | sn66 commit touches scoring: Release 259 reviewed targets with immutable 10 MiB task policies |
| `sn71:scoring_commit:2026-09-08T06:56:07Z` | 71 | SCORING_COMMIT | 2026-09-08T09:02:01Z | sn71 commit touches scoring: Parse Arena drain quiescence in validator handoff |
| `sn80:scoring_commit:2026-09-08T07:33:08Z` | 80 | SCORING_COMMIT | 2026-09-08T09:02:01Z | sn80 commit touches scoring: docs: link shared real-robot task catalog and training data |
| `sn9:release:v4.12.14` | 9 | RELEASE | 2026-09-08T13:32:58Z | sn9 released v4.12.14 |
| `sn10:scoring_commit:2026-09-08T09:22:29Z` | 10 | SCORING_COMMIT | 2026-09-08T13:32:58Z | sn10 commit touches scoring: Merge pull request #145 from Pareton-ai/bohdan/feat/miner-score-trans… |
| `sn34:scoring_commit:2026-09-08T03:06:21Z` | 34 | SCORING_COMMIT | 2026-09-08T13:32:58Z | sn34 commit touches scoring: Bump version to 5.0.2 so validators autoupdate. |
| `sn71:scoring_commit:2026-09-08T13:29:02Z` | 71 | SCORING_COMMIT | 2026-09-08T13:32:58Z | sn71 commit touches scoring: Verify approved prior testnet release boots |
| `sn100:scoring_commit:2026-09-08T09:44:43Z` | 100 | SCORING_COMMIT | 2026-09-08T13:32:58Z | sn100 commit touches scoring: fix(eval): install host cc for triton jit on scoring image (#239) |
| `sn25:release:v2026.9.8-1040779940` | 25 | RELEASE | 2026-09-08T17:34:23Z | sn25 released v2026.9.8-1040779940 |
| `sn71:scoring_commit:2026-09-08T15:54:53Z` | 71 | SCORING_COMMIT | 2026-09-08T17:34:23Z | sn71 commit touches scoring: Merge remote-tracking branch 'origin/main' into codex/validator-test-… |
| `sn74:release:release-20260908-144557` | 74 | RELEASE | 2026-09-08T17:34:23Z | sn74 released release-20260908-144557 |
| `sn92:scoring_commit:2026-09-08T14:53:18Z` | 92 | SCORING_COMMIT | 2026-09-08T17:34:23Z | sn92 commit touches scoring: tracks: support is the one live track; call shaped tests load and scor |
| `sn120:scoring_commit:2026-09-08T14:27:39Z` | 120 | SCORING_COMMIT | 2026-09-08T17:34:23Z | sn120 commit touches scoring: Sync validator + eval design (2026-09-07/08): eval throughput work, w… |
| `sn2:release:14.14.3` | 2 | RELEASE | 2026-09-08T20:19:51Z | sn2 released 14.14.3 |
| `sn2:scoring_commit:2026-09-08T19:26:11Z` | 2 | SCORING_COMMIT | 2026-09-08T20:19:51Z | sn2 commit touches scoring: Introduce weight commit guard for epochs with zero miner scores (#627) |
| `sn71:scoring_commit:2026-09-08T20:17:47Z` | 71 | SCORING_COMMIT | 2026-09-08T20:19:51Z | sn71 commit touches scoring: Merge remote-tracking branch 'origin/main' into codex/arena-miner-rep… |
| `sn78:scoring_commit:2026-09-08T17:55:55Z` | 78 | SCORING_COMMIT | 2026-09-08T20:19:51Z | sn78 commit touches scoring: Fix bootstrap image revision validation |
| `sn96:release:Verathos v0.2.2 – Consistent Validator D` | 96 | RELEASE | 2026-09-08T20:19:51Z | sn96 released Verathos v0.2.2 – Consistent Validator Decisions and Microtensor Support |
| `sn15:release:v1.2.13: compose: forward SUBTENSOR_CHAI` | 15 | RELEASE | 2026-09-08T22:52:47Z | sn15 released v1.2.13: compose: forward SUBTENSOR_CHAIN_ENDPOINT to the validator (#274) |
| `sn15:scoring_commit:2026-09-08T20:21:13Z` | 15 | SCORING_COMMIT | 2026-09-08T22:52:47Z | sn15 commit touches scoring: compose: forward SUBTENSOR_CHAIN_ENDPOINT to the validator (#274) |
| `sn25:release:v2026.9.8-1040985530` | 25 | RELEASE | 2026-09-08T22:52:47Z | sn25 released v2026.9.8-1040985530 |
| `sn28:release:v0.4.15` | 28 | RELEASE | 2026-09-08T22:52:47Z | sn28 released v0.4.15 |
| `sn28:scoring_commit:2026-09-08T21:50:27Z` | 28 | SCORING_COMMIT | 2026-09-08T22:52:47Z | sn28 commit touches scoring: fix(miner): render node secret last and pin C locale |
| `sn71:scoring_commit:2026-09-08T22:52:04Z` | 71 | SCORING_COMMIT | 2026-09-09T01:13:27Z | sn71 commit touches scoring: build: refresh protected scoring source metadata |
| `sn111:scoring_commit:2026-09-09T00:59:16Z` | 111 | SCORING_COMMIT | 2026-09-09T01:13:27Z | sn111 commit touches scoring: fix(validator): enable rigor validation in mainnet profiles |
| `sn51:scoring_commit:2026-09-09T06:11:27Z` | 51 | SCORING_COMMIT | 2026-09-09T06:19:59Z | sn51 commit touches scoring: DAH-2962: delete the dead hashcat scoring path and the GPT-2 sample (… |
| `sn67:scoring_commit:2026-09-09T04:45:43Z` | 67 | SCORING_COMMIT | 2026-09-09T06:19:59Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20260909.post0 |
| `sn71:scoring_commit:2026-09-09T02:00:25Z` | 71 | SCORING_COMMIT | 2026-09-09T06:19:59Z | sn71 commit touches scoring: Stop Arena scoring after exhausted judge failure |
| `sn100:scoring_commit:2026-09-09T01:28:41Z` | 100 | SCORING_COMMIT | 2026-09-09T06:19:59Z | sn100 commit touches scoring: feat(proof): name the topic_id / custom_id hyphen-underscore mix-up (… |
| `sn111:scoring_commit:2026-09-09T03:15:32Z` | 111 | SCORING_COMMIT | 2026-09-09T06:19:59Z | sn111 commit touches scoring: fix(validator): normalize provider routing for DSPy adjudication |
| `sn120:scoring_commit:2026-09-09T03:59:55Z` | 120 | SCORING_COMMIT | 2026-09-09T06:19:59Z | sn120 commit touches scoring: AGENTS.md: first wvk-13 verdicts verified (probe reject, think-close … |
| `sn61:release:4.10.3` | 61 | RELEASE | 2026-09-09T11:41:14Z | sn61 released 4.10.3 |
| `sn66:scoring_commit:2026-09-09T08:24:00Z` | 66 | SCORING_COMMIT | 2026-09-09T11:41:14Z | sn66 commit touches scoring: Merge pull request #80 from conjectures-io/feat/retire-miner-hotkeys |
| `sn71:scoring_commit:2026-09-09T09:18:44Z` | 71 | SCORING_COMMIT | 2026-09-09T11:41:14Z | sn71 commit touches scoring: Preserve terminal company scores across judge retries |
| `sn78:scoring_commit:2026-09-09T07:12:10Z` | 78 | SCORING_COMMIT | 2026-09-09T11:41:14Z | sn78 commit touches scoring: Add legacy validator transition hold |
| `sn89:scoring_commit:2026-09-09T08:32:52Z` | 89 | SCORING_COMMIT | 2026-09-09T11:41:14Z | sn89 commit touches scoring: scoring: points-path earning gate is the points test as-of each call,… |
| `sn97:scoring_commit:2026-09-08T12:09:46Z` | 97 | SCORING_COMMIT | 2026-09-09T11:41:14Z | sn97 commit touches scoring: fix: show all task results for benchmark runs |
| `sn111:scoring_commit:2026-09-09T10:40:55Z` | 111 | SCORING_COMMIT | 2026-09-09T11:41:14Z | sn111 commit touches scoring: docs: clarify Ubuntu validator env setup |
| `sn114:scoring_commit:2026-09-09T08:57:02Z` | 114 | SCORING_COMMIT | 2026-09-09T11:41:14Z | sn114 commit touches scoring: Cap automatic run restarts per miner task |
| `sn1:release:v4.4.5` | 1 | RELEASE | 2026-09-09T15:20:16Z | sn1 released v4.4.5 |
| `sn28:release:v0.4.16-dev` | 28 | RELEASE | 2026-09-09T15:20:16Z | sn28 released v0.4.16-dev |
| `sn28:scoring_commit:2026-09-09T11:24:08Z` | 28 | SCORING_COMMIT | 2026-09-09T15:20:16Z | sn28 commit touches scoring: Anchor deployment staleness to the last successful verification |
| `sn71:scoring_commit:2026-09-09T11:49:48Z` | 71 | SCORING_COMMIT | 2026-09-09T15:20:16Z | sn71 commit touches scoring: Bind dead preflight verifier removal |
| `sn28:release:v0.4.17-dev` | 28 | RELEASE | 2026-09-09T18:46:23Z | sn28 released v0.4.17-dev |
| `sn62:release:v0.3.1` | 62 | RELEASE | 2026-09-09T18:46:23Z | sn62 released v0.3.1 |
| `sn62:scoring_commit:2026-09-07T11:02:04Z` | 62 | SCORING_COMMIT | 2026-09-09T18:46:23Z | sn62 commit touches scoring: feat: prevent cluster-autoscaler from draining a screener mid-evaluati |
| `sn71:scoring_commit:2026-09-09T18:13:57Z` | 71 | SCORING_COMMIT | 2026-09-09T18:46:23Z | sn71 commit touches scoring: Merge remote-tracking branch 'origin/main' into codex/arena-miner-rep… |
| `sn78:scoring_commit:2026-09-09T17:44:05Z` | 78 | SCORING_COMMIT | 2026-09-09T18:46:23Z | sn78 commit touches scoring: Publish verified bootstrap service state |
| `sn111:scoring_commit:2026-09-09T17:55:55Z` | 111 | SCORING_COMMIT | 2026-09-09T18:46:23Z | sn111 commit touches scoring: fix(validator): recover failed Silver adjudication batches |
| `sn124:scoring_commit:2026-09-08T18:12:27Z` | 124 | SCORING_COMMIT | 2026-09-09T18:46:23Z | sn124 commit touches scoring: Keep leased seeds through a validator restart |
| `sn20:scoring_commit:2026-09-08T12:07:25Z` | 20 | SCORING_COMMIT | 2026-09-09T21:17:06Z | sn20 commit touches scoring: Document model-independent miner extension workflow |
| `sn36:scoring_commit:2026-09-09T19:30:44Z` | 36 | SCORING_COMMIT | 2026-09-09T21:17:06Z | sn36 commit touches scoring: Merge pull request #5 from EpagoFoundation/fix/sealed-release-tasks |
| `sn62:release:v0.3.2` | 62 | RELEASE | 2026-09-09T21:17:06Z | sn62 released v0.3.2 |
| `sn71:scoring_commit:2026-09-09T21:09:24Z` | 71 | SCORING_COMMIT | 2026-09-09T21:17:06Z | sn71 commit touches scoring: Merge remote-tracking branch 'origin/main' into codex/arena-miner-rep… |
| `sn78:scoring_commit:2026-09-09T19:48:05Z` | 78 | SCORING_COMMIT | 2026-09-09T21:17:06Z | sn78 commit touches scoring: Add prerequisite-gated validator supervisor |
| `sn25:release:v2026.9.9-1041947070` | 25 | RELEASE | 2026-09-09T23:25:39Z | sn25 released v2026.9.9-1041947070 |
| `sn28:release:v0.4.17` | 28 | RELEASE | 2026-09-09T23:25:39Z | sn28 released v0.4.17 |
| `sn61:release:4.10.4` | 61 | RELEASE | 2026-09-09T23:25:39Z | sn61 released 4.10.4 |
| `sn62:scoring_commit:2026-09-09T18:55:06Z` | 62 | SCORING_COMMIT | 2026-09-09T23:25:39Z | sn62 commit touches scoring: Merge pull request #498 from ridgesai/feat/update-validator-docker |
| `sn71:scoring_commit:2026-09-09T22:53:48Z` | 71 | SCORING_COMMIT | 2026-09-09T23:25:39Z | sn71 commit touches scoring: Cover encoded miner-key echoes through provider routes |
| `sn78:scoring_commit:2026-09-09T22:13:48Z` | 78 | SCORING_COMMIT | 2026-09-09T23:25:39Z | sn78 commit touches scoring: Fix OCI archive annotation verification |
| `sn100:release:ctx CLI v3.3.30` | 100 | RELEASE | 2026-09-09T23:25:39Z | sn100 released ctx CLI v3.3.30 |
| `sn100:scoring_commit:2026-09-09T22:40:23Z` | 100 | SCORING_COMMIT | 2026-09-09T23:25:39Z | sn100 commit touches scoring: feat(proof): continuous leaf emitter with ChallengeInternal cover (#25 |
| `sn25:release:v2026.9.9-1042000000` | 25 | RELEASE | 2026-09-10T01:20:26Z | sn25 released v2026.9.9-1042000000 |
| `sn81:scoring_commit:2026-09-10T00:47:41Z` | 81 | SCORING_COMMIT | 2026-09-10T01:20:26Z | sn81 commit touches scoring: fix: validate sampled entropy coverage at the proof boundary |
| `sn100:release:ctx CLI v3.3.31` | 100 | RELEASE | 2026-09-10T01:20:26Z | sn100 released ctx CLI v3.3.31 |
| `sn100:scoring_commit:2026-09-10T00:49:52Z` | 100 | SCORING_COMMIT | 2026-09-10T01:20:26Z | sn100 commit touches scoring: feat(proof): require miner hotkey signature on submit (#259) |
| `sn15:release:shoppingbench-final` | 15 | RELEASE | 2026-09-10T06:19:09Z | sn15 released shoppingbench-final |
| `sn25:release:v2026.9.9-1042199790` | 25 | RELEASE | 2026-09-10T06:19:09Z | sn25 released v2026.9.9-1042199790 |
| `sn51:release:executor-v1.124` | 51 | RELEASE | 2026-09-10T06:19:09Z | sn51 released executor-v1.124 |
| `sn51:scoring_commit:2026-09-10T02:42:59Z` | 51 | SCORING_COMMIT | 2026-09-10T06:19:09Z | sn51 commit touches scoring: DAH-3006 - [P1] validator stops serialising every Redis command behin… |
| `sn71:scoring_commit:2026-09-10T05:18:12Z` | 71 | SCORING_COMMIT | 2026-09-10T06:19:09Z | sn71 commit touches scoring: Preserve validated page final URLs |
| `sn81:scoring_commit:2026-09-10T05:24:18Z` | 81 | SCORING_COMMIT | 2026-09-10T06:19:09Z | sn81 commit touches scoring: Merge pull request #236 from reliquadotai/codex/v1-miner-readme |
| `sn91:scoring_commit:2026-09-10T05:27:44Z` | 91 | SCORING_COMMIT | 2026-09-10T06:19:09Z | sn91 commit touches scoring: Merge pull request #251 from TensorLink-AI/claude/score-warm-start |
| `sn100:scoring_commit:2026-09-10T06:07:01Z` | 100 | SCORING_COMMIT | 2026-09-10T06:19:09Z | sn100 commit touches scoring: docs(proof): add miner guide for the tbench topic (#261) |
| `sn15:release:v2.0.0` | 15 | RELEASE | 2026-09-10T11:39:13Z | sn15 released v2.0.0 |
| `sn15:scoring_commit:2026-09-10T07:45:35Z` | 15 | SCORING_COMMIT | 2026-09-10T11:39:13Z | sn15 commit touches scoring: Verify scope-bound environment deliveries (#276) |
| `sn25:release:v2026.9.10-1042298530` | 25 | RELEASE | 2026-09-10T11:39:13Z | sn25 released v2026.9.10-1042298530 |
| `sn25:scoring_commit:2026-09-10T09:40:39Z` | 25 | SCORING_COMMIT | 2026-09-10T11:39:13Z | sn25 commit touches scoring: crv4: accept reviewed runtime 455 validator stake layout |
| `sn51:release:executor-v1.125` | 51 | RELEASE | 2026-09-10T11:39:13Z | sn51 released executor-v1.125 |
| `sn62:release:v0.3.3` | 62 | RELEASE | 2026-09-10T11:39:13Z | sn62 released v0.3.3 |
| `sn67:scoring_commit:2026-09-10T07:28:03Z` | 67 | SCORING_COMMIT | 2026-09-10T11:39:13Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20260910.post3 |
| `sn71:scoring_commit:2026-09-10T06:18:11Z` | 71 | SCORING_COMMIT | 2026-09-10T11:39:13Z | sn71 commit touches scoring: docs: state midnight continuous evaluation timing |
| `sn91:scoring_commit:2026-09-10T11:31:44Z` | 91 | SCORING_COMMIT | 2026-09-10T11:39:13Z | sn91 commit touches scoring: docs: concise miner quickstart for funded legs, private submissions, … |
| `sn100:scoring_commit:2026-09-10T11:36:06Z` | 100 | SCORING_COMMIT | 2026-09-10T11:39:13Z | sn100 commit touches scoring: fix(proof): fail closed on incomplete harbor evaluate (#267) |
| `sn9:release:v4.12.16` | 9 | RELEASE | 2026-09-10T15:13:20Z | sn9 released v4.12.16 |
| `sn51:scoring_commit:2026-09-10T12:28:28Z` | 51 | SCORING_COMMIT | 2026-09-10T15:13:20Z | sn51 commit touches scoring: DAH-2748, hide a node the validator cannot reach on one availability … |
| `sn63:scoring_commit:2026-09-10T15:05:19Z` | 63 | SCORING_COMMIT | 2026-09-10T15:13:20Z | sn63 commit touches scoring: Fix issue with migrated validator db |
| `sn81:scoring_commit:2026-09-10T12:25:01Z` | 81 | SCORING_COMMIT | 2026-09-10T15:13:20Z | sn81 commit touches scoring: Document V6 miner submission allowance |
| `sn108:scoring_commit:2026-09-10T11:47:33Z` | 108 | SCORING_COMMIT | 2026-09-10T15:13:20Z | sn108 commit touches scoring: feat(evaluation): optionally discard a checkpoint once it has been sc… |
| `sn9:release:v4.12.17` | 9 | RELEASE | 2026-09-10T18:37:00Z | sn9 released v4.12.17 |
| `sn15:release:v2.0.1` | 15 | RELEASE | 2026-09-10T18:37:00Z | sn15 released v2.0.1 |
| `sn15:scoring_commit:2026-09-10T15:34:08Z` | 15 | SCORING_COMMIT | 2026-09-10T18:37:00Z | sn15 commit touches scoring: Select validator evaluator from claimed pack binding |
| `sn21:scoring_commit:2026-09-10T16:56:54Z` | 21 | SCORING_COMMIT | 2026-09-10T18:37:00Z | sn21 commit touches scoring: docs(rewards): restate the curve with an 80% tail, a twenty-earner ex… |
| `sn25:release:v2026.9.10-1042581110` | 25 | RELEASE | 2026-09-10T18:37:00Z | sn25 released v2026.9.10-1042581110 |
| `sn71:scoring_commit:2026-09-10T18:20:39Z` | 71 | SCORING_COMMIT | 2026-09-10T18:37:00Z | sn71 commit touches scoring: Validate deployed legacy coordinator command |
| `sn78:scoring_commit:2026-09-10T18:02:00Z` | 78 | SCORING_COMMIT | 2026-09-10T18:37:00Z | sn78 commit touches scoring: Expose Linux validator setup |
| `sn15:release:v2.0.2: Record search retries in validat` | 15 | RELEASE | 2026-09-10T21:14:36Z | sn15 released v2.0.2: Record search retries in validator traces (#280) |
| `sn15:scoring_commit:2026-09-10T20:02:22Z` | 15 | SCORING_COMMIT | 2026-09-10T21:14:36Z | sn15 commit touches scoring: Record search retries in validator traces (#280) |
| `sn20:scoring_commit:2026-09-10T20:17:09Z` | 20 | SCORING_COMMIT | 2026-09-10T21:14:36Z | sn20 commit touches scoring: Clarify full burn when every miner has zero current reward |
| `sn81:scoring_commit:2026-09-10T19:13:46Z` | 81 | SCORING_COMMIT | 2026-09-10T21:14:36Z | sn81 commit touches scoring: perf(validator): time the phases of one expensive proof verification |
| `sn100:scoring_commit:2026-09-10T20:16:11Z` | 100 | SCORING_COMMIT | 2026-09-10T21:14:36Z | sn100 commit touches scoring: fix(proof): tbench agent network, custom Python harness, <1h tasks (#… |
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
| `sn93:readme_task_diff:6bd0c74883d58dde` | 93 | README_TASK_DIFF | 2026-09-06T18:30:56Z | sn93 README task/scoring sections changed |
| `sn34:readme_task_diff:535b78cbd7d6207d` | 34 | README_TASK_DIFF | 2026-09-06T22:52:57Z | sn34 README task/scoring sections changed |
| `sn80:readme_task_diff:9cd93d83a14b7502` | 80 | README_TASK_DIFF | 2026-09-07T12:22:04Z | sn80 README task/scoring sections changed |
| `sn67:readme_task_diff:02d3c62272b1d7dd` | 67 | README_TASK_DIFF | 2026-09-08T04:27:58Z | sn67 README task/scoring sections changed |
| `sn66:readme_task_diff:1677dd0cb94b82d3` | 66 | README_TASK_DIFF | 2026-09-08T09:02:01Z | sn66 README task/scoring sections changed |
| `sn80:readme_task_diff:ef9838874bfda548` | 80 | README_TASK_DIFF | 2026-09-08T09:02:01Z | sn80 README task/scoring sections changed |
| `sn28:readme_task_diff:150862184557e02b` | 28 | README_TASK_DIFF | 2026-09-08T22:52:47Z | sn28 README task/scoring sections changed |
| `sn28:readme_task_diff:459971cadb11194f` | 28 | README_TASK_DIFF | 2026-09-09T15:20:16Z | sn28 README task/scoring sections changed |
| `sn45:readme_task_diff:15dfa7fb69a79bef` | 45 | README_TASK_DIFF | 2026-09-09T15:20:16Z | sn45 README task/scoring sections changed |
| `sn28:readme_task_diff:aab5d8d239c04847` | 28 | README_TASK_DIFF | 2026-09-09T18:46:23Z | sn28 README task/scoring sections changed |
| `sn108:readme_task_diff:3f2d87f2c0a1e7e0` | 108 | README_TASK_DIFF | 2026-09-09T18:46:23Z | sn108 README task/scoring sections changed |
| `sn20:readme_task_diff:4594489462f379e3` | 20 | README_TASK_DIFF | 2026-09-09T21:17:06Z | sn20 README task/scoring sections changed |
| `sn71:readme_task_diff:b64ef6137b1c6577` | 71 | README_TASK_DIFF | 2026-09-10T01:20:26Z | sn71 README task/scoring sections changed |
| `sn15:readme_task_diff:17e287861e782246` | 15 | README_TASK_DIFF | 2026-09-10T06:19:09Z | sn15 README task/scoring sections changed |
| `sn66:readme_task_diff:e9a9de7a5084c0f6` | 66 | README_TASK_DIFF | 2026-09-10T15:13:20Z | sn66 README task/scoring sections changed |
| `sn15:readme_task_diff:853d4079fee0eccb` | 15 | README_TASK_DIFF | 2026-09-10T21:14:36Z | sn15 README task/scoring sections changed |
| `sn20:readme_task_diff:b54d839bca570978` | 20 | README_TASK_DIFF | 2026-09-10T21:14:36Z | sn20 README task/scoring sections changed |
| `sn7:readme_task_diff:dc7b2a4e628af18f` | 7 | README_TASK_DIFF | 2026-09-11T06:22:30Z | sn7 README task/scoring sections changed |
| `sn71:readme_task_diff:f4854b87ceea3027` | 71 | README_TASK_DIFF | 2026-09-11T06:22:30Z | sn71 README task/scoring sections changed |
| `sn20:readme_task_diff:8d48fc82515ff603` | 20 | README_TASK_DIFF | 2026-09-11T11:40:27Z | sn20 README task/scoring sections changed |
| `sn71:readme_task_diff:858d6e3350fdacde` | 71 | README_TASK_DIFF | 2026-09-11T18:42:05Z | sn71 README task/scoring sections changed |
| `sn71:readme_task_diff:691868bd635e63bb` | 71 | README_TASK_DIFF | 2026-09-12T06:24:23Z | sn71 README task/scoring sections changed |

## RESOLVED IN THIS WINDOW

_none_
