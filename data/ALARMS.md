# ALARMS - generated 2026-10-15T05:51:14Z, block 9286738

window: first_seen in [2026-10-15T04:36:38Z, 2026-10-15T05:51:38Z)  (60 min interval + 15 min overlap)

Report ONLY the rows under NEW SINCE LAST RUN. Rows under STILL OPEN were
already reported in an earlier window and must not be re-alarmed.

## NEW SINCE LAST RUN

| event_id | netuid | class | severity | first_seen_utc | one_line |
|---|---|---|---|---|---|
| `sn118:burn_drop:0.700` | 118 | BURN_DROP | P0 | 2026-10-15T05:51:38Z | sn118 burn fell 1.000 -> 0.700 - miners can earn again |
| `sn15:release:v2.5.2` | 15 | RELEASE | P1 | 2026-10-15T05:51:38Z | sn15 released v2.5.2 |
| `sn15:scoring_commit:2026-10-15T05:19:00Z` | 15 | SCORING_COMMIT | P1 | 2026-10-15T05:51:38Z | sn15 commit touches scoring: Treat a miner's OpenRouter credit 402 as an exhausted run key (#374) |
| `sn25:scoring_commit:2026-10-15T04:12:02Z` | 25 | SCORING_COMMIT | P1 | 2026-10-15T05:51:38Z | sn25 commit touches scoring: Update the SN25 timeline with the validator operator's answers |
| `sn51:scoring_commit:2026-10-15T04:20:45Z` | 51 | SCORING_COMMIT | P1 | 2026-10-15T05:51:38Z | sn51 commit touches scoring: DAH-4071 - [P1] validator: SCORING_EXCLUDED_HOTKEYS, listed hotkeys e… |
| `sn67:scoring_commit:2026-10-14T14:32:28Z` | 67 | SCORING_COMMIT | P1 | 2026-10-15T05:51:38Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20261014.post6 |
| `sn78:scoring_commit:2026-10-15T05:43:45Z` | 78 | SCORING_COMMIT | P1 | 2026-10-15T05:51:38Z | sn78 commit touches scoring: Merge pull request #266 from Umi-BitSign/codex/verified-checkpoint-ex… |
| `sn116:scoring_commit:2026-10-15T04:30:56Z` | 116 | SCORING_COMMIT | P1 | 2026-10-15T05:51:38Z | sn116 commit touches scoring: Merge pull request #1371 from carbonphysicsai/codex/scorelab-referenc… |

### detail

- **`sn118:burn_drop:0.700`** - sn118 burn fell 1.000 -> 0.700 - miners can earn again
  - This subnet paid miners nothing and now pays. Worth a look before the field fills up.
- **`sn15:release:v2.5.2`** - sn15 released v2.5.2
  - published 2026-10-15T05:19:11Z (was v2.5.0)
- **`sn15:scoring_commit:2026-10-15T05:19:00Z`** - sn15 commit touches scoring: Treat a miner's OpenRouter credit 402 as an exhausted run key (#374)
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn25:scoring_commit:2026-10-15T04:12:02Z`** - sn25 commit touches scoring: Update the SN25 timeline with the validator operator's answers
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn51:scoring_commit:2026-10-15T04:20:45Z`** - sn51 commit touches scoring: DAH-4071 - [P1] validator: SCORING_EXCLUDED_HOTKEYS, listed hotkeys e…
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn67:scoring_commit:2026-10-14T14:32:28Z`** - sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20261014.post6
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn78:scoring_commit:2026-10-15T05:43:45Z`** - sn78 commit touches scoring: Merge pull request #266 from Umi-BitSign/codex/verified-checkpoint-ex…
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn116:scoring_commit:2026-10-15T04:30:56Z`** - sn116 commit touches scoring: Merge pull request #1371 from carbonphysicsai/codex/scorelab-referenc…
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.

## STILL OPEN (already reported - do not re-alarm)

| event_id | netuid | class | first_seen_utc | one_line |
|---|---|---|---|---|
| `sn25:burn_drop:0.000` | 25 | BURN_DROP | 2026-10-08T07:46:34Z | sn25 burn fell 1.000 -> 0.000 - miners can earn again |
| `sn37:burn_drop:0.000` | 37 | BURN_DROP | 2026-10-09T00:42:20Z | sn37 burn fell 1.000 -> 0.000 - miners can earn again |
| `sn104:mechanism_added:1to2` | 104 | MECHANISM_ADDED | 2026-10-09T19:37:09Z | sn104 now runs 2 incentive mechanisms (was 1) |
| `sn108:burn_drop:0.902` | 108 | BURN_DROP | 2026-10-11T19:38:20Z | sn108 burn fell 1.000 -> 0.902 - miners can earn again |
| `sn30:burn_drop:0.984` | 30 | BURN_DROP | 2026-10-12T02:34:00Z | sn30 burn fell 0.997 -> 0.984 - miners can earn again |
| `sn122:burn_drop:0.100` | 122 | BURN_DROP | 2026-10-12T09:49:01Z | sn122 burn fell 1.000 -> 0.100 - miners can earn again |
| `sn12:mechanism_added:1to2` | 12 | MECHANISM_ADDED | 2026-10-12T19:47:00Z | sn12 now runs 2 incentive mechanisms (was 1) |
| `sn58:burn_drop:0.833` | 58 | BURN_DROP | 2026-10-12T19:47:00Z | sn58 burn fell 1.000 -> 0.833 - miners can earn again |
| `sn37:burn_drop:0.715` | 37 | BURN_DROP | 2026-10-14T10:39:10Z | sn37 burn fell 1.000 -> 0.715 - miners can earn again |
| `sn104:burn_drop:0.953` | 104 | BURN_DROP | 2026-10-14T15:33:11Z | sn104 burn fell 1.000 -> 0.953 - miners can earn again |
| `sn108:burn_drop:0.921` | 108 | BURN_DROP | 2026-10-14T15:33:11Z | sn108 burn fell 1.000 -> 0.921 - miners can earn again |
| `sn10:burn_drop:0.532` | 10 | BURN_DROP | 2026-10-14T19:44:42Z | sn10 burn fell 1.000 -> 0.532 - miners can earn again |
| `sn76:burn_drop:0.988` | 76 | BURN_DROP | 2026-10-14T19:44:42Z | sn76 burn fell 1.000 -> 0.988 - miners can earn again |
| `sn25:scoring_commit:2026-10-08T02:54:58Z` | 25 | SCORING_COMMIT | 2026-10-08T07:46:34Z | sn25 commit touches scoring: Merge runtime upgrade tolerance for the production validator |
| `sn51:release:executor-v1.138` | 51 | RELEASE | 2026-10-08T07:46:34Z | sn51 released executor-v1.138 |
| `sn51:scoring_commit:2026-10-08T07:42:00Z` | 51 | SCORING_COMMIT | 2026-10-08T07:46:34Z | sn51 commit touches scoring: validator: remove the failed container before the stale-mount retry (… |
| `sn71:scoring_commit:2026-10-08T06:51:28Z` | 71 | SCORING_COMMIT | 2026-10-08T07:46:34Z | sn71 commit touches scoring: Merge remote-tracking branch 'origin/main' into codex/public-evaluati… |
| `sn100:scoring_commit:2026-10-08T04:21:19Z` | 100 | SCORING_COMMIT | 2026-10-08T07:46:34Z | sn100 commit touches scoring: docs(repo): remove retired products, add readme and validator script … |
| `sn116:release:producer-code-r2: code-only tag for the ` | 116 | RELEASE | 2026-10-08T07:46:34Z | sn116 released producer-code-r2: code-only tag for the producer and the leak runbook |
| `sn116:scoring_commit:2026-10-08T07:05:19Z` | 116 | SCORING_COMMIT | 2026-10-08T07:46:34Z | sn116 commit touches scoring: Merge pull request #780 from carbonphysicsai/agent/validator-24-withd… |
| `sn120:scoring_commit:2026-10-08T06:54:09Z` | 120 | SCORING_COMMIT | 2026-10-08T07:46:34Z | sn120 commit touches scoring: Validate paired held-out trainer optimization results |
| `sn3:scoring_commit:2026-10-08T10:48:25Z` | 3 | SCORING_COMMIT | 2026-10-08T14:58:35Z | sn3 commit touches scoring: Add competition dataset panel and update evaluation history layout |
| `sn15:release:v2.4.0: Prepare runtime 3.5 validator an` | 15 | RELEASE | 2026-10-08T14:58:35Z | sn15 released v2.4.0: Prepare runtime 3.5 validator and practice delivery (#367) |
| `sn15:scoring_commit:2026-10-08T08:48:54Z` | 15 | SCORING_COMMIT | 2026-10-08T14:58:35Z | sn15 commit touches scoring: Prepare runtime 3.5 validator and practice delivery (#367) |
| `sn21:scoring_commit:2026-10-08T14:35:15Z` | 21 | SCORING_COMMIT | 2026-10-08T14:58:35Z | sn21 commit touches scoring: fix(scoring): copy groups agree on one earner, the earliest submission |
| `sn51:scoring_commit:2026-10-08T09:21:54Z` | 51 | SCORING_COMMIT | 2026-10-08T14:58:35Z | sn51 commit touches scoring: DAH-4001 - validator: shadow never delays the live weights, settlemen… |
| `sn71:scoring_commit:2026-10-08T07:52:06Z` | 71 | SCORING_COMMIT | 2026-10-08T14:58:35Z | sn71 commit touches scoring: Merge PR #276: verify judging through the miner provider route |
| `sn81:scoring_commit:2026-10-08T08:52:59Z` | 81 | SCORING_COMMIT | 2026-10-08T14:58:35Z | sn81 commit touches scoring: docs(corpus): the open route and the agentic miner's use of it |
| `sn116:release:worker-images-v2` | 116 | RELEASE | 2026-10-08T14:58:35Z | sn116 released worker-images-v2 |
| `sn116:scoring_commit:2026-10-08T13:55:12Z` | 116 | SCORING_COMMIT | 2026-10-08T14:58:35Z | sn116 commit touches scoring: Merge pull request #815 from carbonphysicsai/agent/battery-score-rule- |
| `sn120:scoring_commit:2026-10-08T08:41:04Z` | 120 | SCORING_COMMIT | 2026-10-08T14:58:35Z | sn120 commit touches scoring: Keep learner startup independent of an unreachable verifier transport |
| `sn25:release:v2026.10.8-1066912010` | 25 | RELEASE | 2026-10-08T20:40:32Z | sn25 released v2026.10.8-1066912010 |
| `sn41:scoring_commit:2026-10-08T19:33:16Z` | 41 | SCORING_COMMIT | 2026-10-08T20:40:32Z | sn41 commit touches scoring: Merge pull request #55 from corvxai/forecasting_scoring_v2 |
| `sn51:scoring_commit:2026-10-08T15:36:23Z` | 51 | SCORING_COMMIT | 2026-10-08T20:40:32Z | sn51 commit touches scoring: DAH-3769 - Validator: dropped SSH transport becomes a typed error wit… |
| `sn58:scoring_commit:2026-10-08T18:16:01Z` | 58 | SCORING_COMMIT | 2026-10-08T20:40:32Z | sn58 commit touches scoring: fix(miner): `attune miner status` checks the Hub with the submission … |
| `sn71:scoring_commit:2026-10-08T17:08:48Z` | 71 | SCORING_COMMIT | 2026-10-08T20:40:32Z | sn71 commit touches scoring: Allow bounded score batch RPC reads to finish |
| `sn90:scoring_commit:2026-10-08T18:01:39Z` | 90 | SCORING_COMMIT | 2026-10-08T20:40:32Z | sn90 commit touches scoring: docs(nemotron-omni): 256k context verified + NIM 2.0.13 + gateway mod… |
| `sn116:scoring_commit:2026-10-08T19:33:03Z` | 116 | SCORING_COMMIT | 2026-10-08T20:40:32Z | sn116 commit touches scoring: Record the owner's canary answers 2-4 in OWNER-CANARY-MINER-01 |
| `sn120:scoring_commit:2026-10-08T15:53:32Z` | 120 | SCORING_COMMIT | 2026-10-08T20:40:32Z | sn120 commit touches scoring: Verify longer harness cannot reuse shorter-budget calibration |
| `sn25:release:v2026.10.8-1066946420` | 25 | RELEASE | 2026-10-09T00:42:20Z | sn25 released v2026.10.8-1066946420 |
| `sn62:release:v0.3.10` | 62 | RELEASE | 2026-10-09T00:42:20Z | sn62 released v0.3.10 |
| `sn71:scoring_commit:2026-10-09T00:04:40Z` | 71 | SCORING_COMMIT | 2026-10-09T00:42:20Z | sn71 commit touches scoring: Merge pull request #295 from leadpoet/fix/host-score-closed-billing |
| `sn78:scoring_commit:2026-10-08T23:22:27Z` | 78 | SCORING_COMMIT | 2026-10-09T00:42:20Z | sn78 commit touches scoring: Select policy-budget miner release and resume completed-case archives |
| `sn116:release:worker-images-v3` | 116 | RELEASE | 2026-10-09T00:42:20Z | sn116 released worker-images-v3 |
| `sn116:scoring_commit:2026-10-08T22:48:01Z` | 116 | SCORING_COMMIT | 2026-10-09T00:42:20Z | sn116 commit touches scoring: Merge pull request #846 from carbonphysicsai/codex/challenge-value-co… |
| `sn120:scoring_commit:2026-10-08T21:41:26Z` | 120 | SCORING_COMMIT | 2026-10-09T00:42:20Z | sn120 commit touches scoring: Confirm fresh public epoch and authenticated base evaluation |
| `sn51:scoring_commit:2026-10-09T04:13:41Z` | 51 | SCORING_COMMIT | 2026-10-09T06:48:38Z | sn51 commit touches scoring: DAH-4001 - validator: no settled window keeps the weights in force, i… |
| `sn81:scoring_commit:2026-10-09T02:51:22Z` | 81 | SCORING_COMMIT | 2026-10-09T06:48:38Z | sn81 commit touches scoring: Merge pull request #342 from reliquadotai/fix/task-catalog-artifact-r… |
| `sn89:scoring_commit:2026-10-09T02:22:48Z` | 89 | SCORING_COMMIT | 2026-10-09T06:48:38Z | sn89 commit touches scoring: README: IQ Markets for players (web app, /markets, no miner needed; r… |
| `sn101:scoring_commit:2026-10-08T15:09:53Z` | 101 | SCORING_COMMIT | 2026-10-09T06:48:38Z | sn101 commit touches scoring: Add v1.1 scoring, AWS corpus leasing, weight-setting hardening, and l… |
| `sn107:scoring_commit:2026-10-09T03:53:09Z` | 107 | SCORING_COMMIT | 2026-10-09T06:48:38Z | sn107 commit touches scoring: Merge pull request #40 from minos-protocol/fix/scoring-cutoff-lead |
| `sn116:scoring_commit:2026-10-09T05:13:15Z` | 116 | SCORING_COMMIT | 2026-10-09T06:48:38Z | sn116 commit touches scoring: Merge pull request #854 from carbonphysicsai/agent/score-feed-schema |
| `sn120:scoring_commit:2026-10-09T06:24:44Z` | 120 | SCORING_COMMIT | 2026-10-09T06:48:38Z | sn120 commit touches scoring: Bind native recovery imports and keep evaluator read capabilities out… |
| `sn3:scoring_commit:2026-10-09T13:41:35Z` | 3 | SCORING_COMMIT | 2026-10-09T14:20:19Z | sn3 commit touches scoring: Add competition filters to evaluation history and update dataset summ… |
| `sn21:release:SN21 training data v4 (live basket shape` | 21 | RELEASE | 2026-10-09T14:20:19Z | sn21 released SN21 training data v4 (live basket shape) |
| `sn50:scoring_commit:2026-10-09T13:27:10Z` | 50 | SCORING_COMMIT | 2026-10-09T14:20:19Z | sn50 commit touches scoring: Avoid a full miner_predictions scan when loading scores (#337) |
| `sn51:scoring_commit:2026-10-09T09:49:06Z` | 51 | SCORING_COMMIT | 2026-10-09T14:20:19Z | sn51 commit touches scoring: DAH-3980 - Validator: one Docker SDK SSH channel per host, not per UR… |
| `sn71:scoring_commit:2026-10-09T07:27:04Z` | 71 | SCORING_COMMIT | 2026-10-09T14:20:19Z | sn71 commit touches scoring: Refresh protected judge fit manifest for merged scorer |
| `sn76:scoring_commit:2026-10-09T14:10:54Z` | 76 | SCORING_COMMIT | 2026-10-09T14:20:19Z | sn76 commit touches scoring: protected/miner/manifest.json: single admitted compose hash after the… |
| `sn78:scoring_commit:2026-10-09T09:19:01Z` | 78 | SCORING_COMMIT | 2026-10-09T14:20:19Z | sn78 commit touches scoring: Unblock C5 admission reads and correct historical block verification … |
| `sn89:scoring_commit:2026-10-09T08:42:41Z` | 89 | SCORING_COMMIT | 2026-10-09T14:20:19Z | sn89 commit touches scoring: scoring: cache z_for_resolve (pure function, bit-identical output) |
| `sn111:scoring_commit:2026-10-08T19:49:34Z` | 111 | SCORING_COMMIT | 2026-10-09T14:20:19Z | sn111 commit touches scoring: feat(validator): route verified operator miner allocation |
| `sn116:scoring_commit:2026-10-09T12:50:59Z` | 116 | SCORING_COMMIT | 2026-10-09T14:20:19Z | sn116 commit touches scoring: VALIDATOR-30 contract: the refusal order (root allow-list first) and … |
| `sn120:scoring_commit:2026-10-09T11:15:27Z` | 120 | SCORING_COMMIT | 2026-10-09T14:20:19Z | sn120 commit touches scoring: Verify effective-LR evidence for normal optimizer continuation |
| `sn13:release:Release v1.18.74` | 13 | RELEASE | 2026-10-09T19:37:09Z | sn13 released Release v1.18.74 |
| `sn21:scoring_commit:2026-10-09T15:47:13Z` | 21 | SCORING_COMMIT | 2026-10-09T19:37:09Z | sn21 commit touches scoring: docs(rewards): self-mining section lists the operator-run miners (UID… |
| `sn25:scoring_commit:2026-10-09T17:31:17Z` | 25 | SCORING_COMMIT | 2026-10-09T19:37:09Z | sn25 commit touches scoring: Name a rejected network sign-in in the validator |
| `sn71:scoring_commit:2026-10-09T19:30:42Z` | 71 | SCORING_COMMIT | 2026-10-09T19:37:09Z | sn71 commit touches scoring: Include accepted host scores in closed billing selector |
| `sn76:scoring_commit:2026-10-09T18:01:37Z` | 76 | SCORING_COMMIT | 2026-10-09T19:37:09Z | sn76 commit touches scoring: Pool deliveries: claim-refusal backoff + claim_health(); validator --… |
| `sn81:scoring_commit:2026-10-09T09:04:13Z` | 81 | SCORING_COMMIT | 2026-10-09T19:37:09Z | sn81 commit touches scoring: feat(env): score reliquary/stdio-program/v1 sources in the sandbox |
| `sn116:release:producer-code-r5` | 116 | RELEASE | 2026-10-09T19:37:09Z | sn116 released producer-code-r5 |
| `sn116:scoring_commit:2026-10-09T19:34:16Z` | 116 | SCORING_COMMIT | 2026-10-09T19:37:09Z | sn116 commit touches scoring: Merge pull request #935 from carbonphysicsai/codex/v3-score-inputs-01 |
| `sn120:scoring_commit:2026-10-09T19:24:54Z` | 120 | SCORING_COMMIT | 2026-10-09T19:37:09Z | sn120 commit touches scoring: Recover hourly miner weight submissions from finalized chain evidence |
| `sn14:scoring_commit:2026-10-09T21:56:54Z` | 14 | SCORING_COMMIT | 2026-10-09T23:34:47Z | sn14 commit touches scoring: Notify Discord when new hotkeys receive committed and active weights … |
| `sn71:scoring_commit:2026-10-09T23:12:54Z` | 71 | SCORING_COMMIT | 2026-10-09T23:34:47Z | sn71 commit touches scoring: Refresh protected scorer manifest for required-stage retry |
| `sn116:release:producer-code-r6` | 116 | RELEASE | 2026-10-09T23:34:47Z | sn116 released producer-code-r6 |
| `sn116:scoring_commit:2026-10-09T20:56:19Z` | 116 | SCORING_COMMIT | 2026-10-09T23:34:47Z | sn116 commit touches scoring: Merge pull request #943 from carbonphysicsai/codex/landscape-miner-in… |
| `sn120:scoring_commit:2026-10-09T21:02:00Z` | 120 | SCORING_COMMIT | 2026-10-09T23:34:47Z | sn120 commit touches scoring: Retain partial miner batches and advance sampling attempts on retries |
| `sn25:release:v2026.10.9-1067985620` | 25 | RELEASE | 2026-10-10T02:48:16Z | sn25 released v2026.10.9-1067985620 |
| `sn62:release:v0.3.11` | 62 | RELEASE | 2026-10-10T02:48:16Z | sn62 released v0.3.11 |
| `sn71:scoring_commit:2026-10-10T02:16:30Z` | 71 | SCORING_COMMIT | 2026-10-10T02:48:16Z | sn71 commit touches scoring: Merge pull request #322 from leadpoet/codex/arena-partial-score-deadl… |
| `sn120:scoring_commit:2026-10-10T01:21:35Z` | 120 | SCORING_COMMIT | 2026-10-10T02:48:16Z | sn120 commit touches scoring: Support prospective nine-batch mining and 512-task training |
| `sn25:release:v2026.10.10-1068162640` | 25 | RELEASE | 2026-10-10T09:44:36Z | sn25 released v2026.10.10-1068162640 |
| `sn51:scoring_commit:2026-10-10T04:05:02Z` | 51 | SCORING_COMMIT | 2026-10-10T09:44:36Z | sn51 commit touches scoring: NO-TICKET - [P1] validator: cap fresh vloopback volume at the ext4 16… |
| `sn71:scoring_commit:2026-10-10T04:22:43Z` | 71 | SCORING_COMMIT | 2026-10-10T09:44:36Z | sn71 commit touches scoring: Merge pull request #328 from leadpoet/codex/paid-score-abandonment-441 |
| `sn120:scoring_commit:2026-10-10T09:04:36Z` | 120 | SCORING_COMMIT | 2026-10-10T09:44:36Z | sn120 commit touches scoring: Document live epoch 116 distinct-task training intake |
| `sn25:release:v2026.10.10-1068404160` | 25 | RELEASE | 2026-10-10T15:35:44Z | sn25 released v2026.10.10-1068404160 |
| `sn28:release:v0.4.27-dev` | 28 | RELEASE | 2026-10-10T15:35:44Z | sn28 released v0.4.27-dev |
| `sn28:scoring_commit:2026-10-10T13:53:49Z` | 28 | SCORING_COMMIT | 2026-10-10T15:35:44Z | sn28 commit touches scoring: chore(release): gm-miner 0.4.27-dev (#310) |
| `sn71:scoring_commit:2026-10-10T15:33:53Z` | 71 | SCORING_COMMIT | 2026-10-10T15:35:44Z | sn71 commit touches scoring: Rejudge Oct10 saved outputs on final ATS scorer |
| `sn25:release:v2026.10.10-1068595480` | 25 | RELEASE | 2026-10-10T19:34:14Z | sn25 released v2026.10.10-1068595480 |
| `sn71:scoring_commit:2026-10-10T19:08:12Z` | 71 | SCORING_COMMIT | 2026-10-10T19:34:14Z | sn71 commit touches scoring: Merge pull request #354 from leadpoet/fix/arena-confirmed-score-parall |
| `sn108:scoring_commit:2026-10-10T15:01:19Z` | 108 | SCORING_COMMIT | 2026-10-10T19:34:14Z | sn108 commit touches scoring: On a baseline_epoch change the validator's bar is exactly the server'… |
| `sn120:scoring_commit:2026-10-10T17:31:08Z` | 120 | SCORING_COMMIT | 2026-10-10T19:34:14Z | sn120 commit touches scoring: Clarify availability of reused historical evaluations |
| `sn25:scoring_commit:2026-10-10T20:21:02Z` | 25 | SCORING_COMMIT | 2026-10-10T22:59:03Z | sn25 commit touches scoring: Merge seeding validator trails from every online provider |
| `sn71:scoring_commit:2026-10-10T21:43:42Z` | 71 | SCORING_COMMIT | 2026-10-10T22:59:03Z | sn71 commit touches scoring: Merge pull request #363 from leadpoet/fix/arena-oct10-score-claim-cuto |
| `sn25:release:v2026.10.10-1068748650` | 25 | RELEASE | 2026-10-11T01:49:20Z | sn25 released v2026.10.10-1068748650 |
| `sn71:scoring_commit:2026-10-11T01:38:29Z` | 71 | SCORING_COMMIT | 2026-10-11T01:49:20Z | sn71 commit touches scoring: Verify guarded natural expiry retains uncertain execute bills |
| `sn22:scoring_commit:2026-10-11T08:32:04Z` | 22 | SCORING_COMMIT | 2026-10-11T08:43:38Z | sn22 commit touches scoring: fix(validators): restore rendered rechecks and the 5% sample |
| `sn25:release:v2026.10.10-1068958850` | 25 | RELEASE | 2026-10-11T08:43:38Z | sn25 released v2026.10.10-1068958850 |
| `sn116:scoring_commit:2026-10-11T02:06:55Z` | 116 | SCORING_COMMIT | 2026-10-11T08:43:38Z | sn116 commit touches scoring: Merge pull request #1041 from carbonphysicsai/claude/miner-survive-re… |
| `sn120:scoring_commit:2026-10-11T07:02:34Z` | 120 | SCORING_COMMIT | 2026-10-11T08:43:38Z | sn120 commit touches scoring: Document independent epoch openings and hourly reward fallback |
| `sn116:release:producer-code-r7` | 116 | RELEASE | 2026-10-11T15:07:48Z | sn116 released producer-code-r7 |
| `sn116:scoring_commit:2026-10-11T14:34:29Z` | 116 | SCORING_COMMIT | 2026-10-11T15:07:48Z | sn116 commit touches scoring: Merge pull request #1046 from carbonphysicsai/codex/code-verification… |
| `sn15:release:v2.4.1` | 15 | RELEASE | 2026-10-11T19:38:20Z | sn15 released v2.4.1 |
| `sn21:scoring_commit:2026-10-11T17:10:16Z` | 21 | SCORING_COMMIT | 2026-10-11T19:38:20Z | sn21 commit touches scoring: docs(verifying): the standing preview exists only during a notice per… |
| `sn22:scoring_commit:2026-10-11T18:25:03Z` | 22 | SCORING_COMMIT | 2026-10-11T19:38:20Z | sn22 commit touches scoring: fix(validators): no JS rendering, 20 pages per 1,000-URL task, fail o… |
| `sn71:scoring_commit:2026-10-11T16:11:47Z` | 71 | SCORING_COMMIT | 2026-10-11T19:38:20Z | sn71 commit touches scoring: Install current reward RPCs in per-ICP round fixture |
| `sn76:scoring_commit:2026-10-11T16:48:26Z` | 76 | SCORING_COMMIT | 2026-10-11T19:38:20Z | sn76 commit touches scoring: Fix miner registration-first onboarding |
| `sn81:scoring_commit:2026-10-11T06:43:18Z` | 81 | SCORING_COMMIT | 2026-10-11T19:38:20Z | sn81 commit touches scoring: feat(cli): tasks set-cap sets or clears a corpus task's token price |
| `sn116:release:producer-code-r8.1` | 116 | RELEASE | 2026-10-11T19:38:20Z | sn116 released producer-code-r8.1 |
| `sn117:release:everycli v0.2.4` | 117 | RELEASE | 2026-10-11T19:38:20Z | sn117 released everycli v0.2.4 |
| `sn117:release:v0.2.5` | 117 | RELEASE | 2026-10-11T23:13:02Z | sn117 released v0.2.5 |
| `sn71:scoring_commit:2026-10-12T01:30:49Z` | 71 | SCORING_COMMIT | 2026-10-12T02:34:00Z | sn71 commit touches scoring: Verify miner credit diagnostics through PostgreSQL reconciliation |
| `sn117:release:everycli v0.3.1` | 117 | RELEASE | 2026-10-12T02:34:00Z | sn117 released everycli v0.3.1 |
| `sn120:scoring_commit:2026-10-12T00:43:15Z` | 120 | SCORING_COMMIT | 2026-10-12T02:34:00Z | sn120 commit touches scoring: Rotate overused math tasks through existing epoch manifests |
| `sn25:scoring_commit:2026-10-12T00:57:57Z` | 25 | SCORING_COMMIT | 2026-10-12T09:49:01Z | sn25 commit touches scoring: Admit one pinned native gap edge so the validator resumes after misse… |
| `sn51:release:executor-v1.139` | 51 | RELEASE | 2026-10-12T09:49:01Z | sn51 released executor-v1.139 |
| `sn51:scoring_commit:2026-10-12T07:54:49Z` | 51 | SCORING_COMMIT | 2026-10-12T09:49:01Z | sn51 commit touches scoring: DAH-3998 - [P2] Signed node heartbeat; validator forwards only a veri… |
| `sn58:scoring_commit:2026-10-11T10:31:29Z` | 58 | SCORING_COMMIT | 2026-10-12T09:49:01Z | sn58 commit touches scoring: feat(vector): a validator on another host takes the lane up from the … |
| `sn94:scoring_commit:2026-10-12T09:13:20Z` | 94 | SCORING_COMMIT | 2026-10-12T09:49:01Z | sn94 commit touches scoring: Merge pull request #254 from skyrocket2026/feat/verifier-release-next |
| `sn116:scoring_commit:2026-10-12T07:28:34Z` | 116 | SCORING_COMMIT | 2026-10-12T09:49:01Z | sn116 commit touches scoring: Merge pull request #1143 from carbonphysicsai/agent/validator-33a-fee… |
| `sn117:release:everycli v0.3.3` | 117 | RELEASE | 2026-10-12T09:49:01Z | sn117 released everycli v0.3.3 |
| `sn120:scoring_commit:2026-10-12T07:59:56Z` | 120 | SCORING_COMMIT | 2026-10-12T09:49:01Z | sn120 commit touches scoring: Plot fixed previously trained tasks in TRAIN fit series |
| `sn3:scoring_commit:2026-10-12T11:52:12Z` | 3 | SCORING_COMMIT | 2026-10-12T19:47:00Z | sn3 commit touches scoring: Optimize evaluator shard downloads with cached HTTP range reads |
| `sn9:release:v4.13.6` | 9 | RELEASE | 2026-10-12T19:47:00Z | sn9 released v4.13.6 |
| `sn14:scoring_commit:2026-10-12T18:41:34Z` | 14 | SCORING_COMMIT | 2026-10-12T19:47:00Z | sn14 commit touches scoring: Retain audit diagnostics and post bundle results to Discord (#145) |
| `sn21:scoring_commit:2026-10-12T12:32:21Z` | 21 | SCORING_COMMIT | 2026-10-12T19:47:00Z | sn21 commit touches scoring: fix(validator): the validator site sends daily-results requests to th… |
| `sn28:release:v0.4.27` | 28 | RELEASE | 2026-10-12T19:47:00Z | sn28 released v0.4.27 |
| `sn28:scoring_commit:2026-10-12T11:20:56Z` | 28 | SCORING_COMMIT | 2026-10-12T19:47:00Z | sn28 commit touches scoring: chore(release): promote gm-miner 0.4.27 (#313) |
| `sn38:scoring_commit:2026-10-12T14:44:32Z` | 38 | SCORING_COMMIT | 2026-10-12T19:47:00Z | sn38 commit touches scoring: Update validator image to the latest version in docker-compose.valida… |
| `sn51:scoring_commit:2026-10-12T19:29:45Z` | 51 | SCORING_COMMIT | 2026-10-12T19:47:00Z | sn51 commit touches scoring: DAH-4001 - validator: report each live weight submission with the cyc… |
| `sn53:scoring_commit:2026-10-12T12:53:09Z` | 53 | SCORING_COMMIT | 2026-10-12T19:47:00Z | sn53 commit touches scoring: Merge pull request #52 from hanlinai/fix/tee-miner-kv-heartbeat-10s |
| `sn71:scoring_commit:2026-10-12T16:30:43Z` | 71 | SCORING_COMMIT | 2026-10-12T19:47:00Z | sn71 commit touches scoring: Apply existing provider failure classification to interrupted scorer … |
| `sn116:release:producer-code-r8.4` | 116 | RELEASE | 2026-10-12T19:47:00Z | sn116 released producer-code-r8.4 |
| `sn116:scoring_commit:2026-10-12T19:20:37Z` | 116 | SCORING_COMMIT | 2026-10-12T19:47:00Z | sn116 commit touches scoring: Record OWNER-BATTERY-CHAMPIONSHIP-04: miner status rows, laddered sco… |
| `sn117:release:everycli v0.3.7` | 117 | RELEASE | 2026-10-12T19:47:00Z | sn117 released everycli v0.3.7 |
| `sn120:scoring_commit:2026-10-12T17:41:42Z` | 120 | SCORING_COMMIT | 2026-10-12T19:47:00Z | sn120 commit touches scoring: Add prospective verifier-only symmetric sampling adjudication |
| `sn28:release:v0.4.28` | 28 | RELEASE | 2026-10-13T01:39:30Z | sn28 released v0.4.28 |
| `sn28:scoring_commit:2026-10-12T21:12:43Z` | 28 | SCORING_COMMIT | 2026-10-13T01:39:30Z | sn28 commit touches scoring: chore(release): promote gm-miner 0.4.28 (#317) |
| `sn71:scoring_commit:2026-10-12T22:46:22Z` | 71 | SCORING_COMMIT | 2026-10-13T01:39:30Z | sn71 commit touches scoring: Finish validated bounded evidence reviews without time-only failure |
| `sn74:release:release-20261012-224627` | 74 | RELEASE | 2026-10-13T01:39:30Z | sn74 released release-20261012-224627 |
| `sn74:scoring_commit:2026-10-12T22:45:40Z` | 74 | SCORING_COMMIT | 2026-10-13T01:39:30Z | sn74 commit touches scoring: chore(weights): burn all miner emissions (empty registry, compute sha… |
| `sn117:release:everycli v0.3.8` | 117 | RELEASE | 2026-10-13T01:39:30Z | sn117 released everycli v0.3.8 |
| `sn25:release:v2026.10.13-1070793380` | 25 | RELEASE | 2026-10-13T08:31:47Z | sn25 released v2026.10.13-1070793380 |
| `sn25:scoring_commit:2026-10-13T05:05:10Z` | 25 | SCORING_COMMIT | 2026-10-13T08:31:47Z | sn25 commit touches scoring: Merge the validator steering fixes deployed on Oct 13 |
| `sn51:release:executor-v1.140` | 51 | RELEASE | 2026-10-13T08:31:47Z | sn51 released executor-v1.140 |
| `sn51:scoring_commit:2026-10-13T04:12:42Z` | 51 | SCORING_COMMIT | 2026-10-13T08:31:47Z | sn51 commit touches scoring: DAH-3980 - Validator: install sshd without recommended packages (#1547 |
| `sn67:scoring_commit:2026-10-13T02:10:44Z` | 67 | SCORING_COMMIT | 2026-10-13T08:31:47Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20261013.post1 |
| `sn71:scoring_commit:2026-10-13T04:39:21Z` | 71 | SCORING_COMMIT | 2026-10-13T08:31:47Z | sn71 commit touches scoring: Merge pull request #408 from leadpoet/fix/arena-public-completed-scor… |
| `sn117:release:everycli v0.3.9` | 117 | RELEASE | 2026-10-13T08:31:47Z | sn117 released everycli v0.3.9 |
| `sn21:scoring_commit:2026-10-13T15:45:33Z` | 21 | SCORING_COMMIT | 2026-10-13T16:29:14Z | sn21 commit touches scoring: fix(scoring): the configured goal is ranked high, medium, low, then n… |
| `sn25:release:v2026.10.13-1070979130` | 25 | RELEASE | 2026-10-13T16:29:14Z | sn25 released v2026.10.13-1070979130 |
| `sn25:scoring_commit:2026-10-13T08:19:37Z` | 25 | SCORING_COMMIT | 2026-10-13T16:29:14Z | sn25 commit touches scoring: Merge the validator trail fixes and bounded steering cut waits |
| `sn37:scoring_commit:2026-10-13T14:58:28Z` | 37 | SCORING_COMMIT | 2026-10-13T16:29:14Z | sn37 commit touches scoring: Replace the legacy public tree with the v5 miner and participant guid… |
| `sn51:scoring_commit:2026-10-13T13:20:45Z` | 51 | SCORING_COMMIT | 2026-10-13T16:29:14Z | sn51 commit touches scoring: A create that fails on the node itself keeps the node at score 0 unti… |
| `sn53:scoring_commit:2026-10-13T11:57:30Z` | 53 | SCORING_COMMIT | 2026-10-13T16:29:14Z | sn53 commit touches scoring: Merge pull request #53 from hanlinai/fix/tee-miner-no-body-in-logs |
| `sn61:release:4.10.10` | 61 | RELEASE | 2026-10-13T16:29:14Z | sn61 released 4.10.10 |
| `sn61:scoring_commit:2026-10-13T10:21:07Z` | 61 | SCORING_COMMIT | 2026-10-13T16:29:14Z | sn61 commit touches scoring: fix: adjust challenge incentive weights and max unique commits for be… |
| `sn68:scoring_commit:2026-09-18T16:21:27Z` | 68 | SCORING_COMMIT | 2026-10-13T16:29:14Z | sn68 commit touches scoring: route all validator chain calls through one reconnecting client |
| `sn81:scoring_commit:2026-10-13T10:12:22Z` | 81 | SCORING_COMMIT | 2026-10-13T16:29:14Z | sn81 commit touches scoring: feat(envscaler): one call per message in the task prompt; episodes bo… |
| `sn114:scoring_commit:2026-10-13T10:59:50Z` | 114 | SCORING_COMMIT | 2026-10-13T16:29:14Z | sn114 commit touches scoring: Merge pull request #229 from DendriteHQ/fix/soma-task-eval-resource-l… |
| `sn116:release:producer-code-r8.5` | 116 | RELEASE | 2026-10-13T16:29:14Z | sn116 released producer-code-r8.5 |
| `sn116:scoring_commit:2026-10-13T15:01:13Z` | 116 | SCORING_COMMIT | 2026-10-13T16:29:14Z | sn116 commit touches scoring: Merge pull request #1281 from carbonphysicsai/codex/opt15b-score-lab-… |
| `sn117:release:everycli v0.4.0` | 117 | RELEASE | 2026-10-13T16:29:14Z | sn117 released everycli v0.4.0 |
| `sn120:scoring_commit:2026-10-13T15:41:21Z` | 120 | SCORING_COMMIT | 2026-10-13T16:29:14Z | sn120 commit touches scoring: Validate trainer completion against fresh receipt clock |
| `sn15:release:v2.5.0` | 15 | RELEASE | 2026-10-13T21:35:22Z | sn15 released v2.5.0 |
| `sn15:scoring_commit:2026-10-13T20:00:27Z` | 15 | SCORING_COMMIT | 2026-10-13T21:35:22Z | sn15 commit touches scoring: Load v7 and v8 task packs; move to oro-env-runtime 3.7.0 (runtime con… |
| `sn25:scoring_commit:2026-10-13T20:37:33Z` | 25 | SCORING_COMMIT | 2026-10-13T21:35:22Z | sn25 commit touches scoring: Write the validator's settlement v2 adoption commands and hold them t… |
| `sn41:scoring_commit:2026-10-13T16:32:43Z` | 41 | SCORING_COMMIT | 2026-10-13T21:35:22Z | sn41 commit touches scoring: Adding weights version key to validator logs as a helpful indicator t… |
| `sn63:scoring_commit:2026-10-13T21:02:02Z` | 63 | SCORING_COMMIT | 2026-10-13T21:35:22Z | sn63 commit touches scoring: Track whether a terminal verify update reached the platform and HQP L… |
| `sn66:scoring_commit:2026-10-13T20:24:34Z` | 66 | SCORING_COMMIT | 2026-10-13T21:35:22Z | sn66 commit touches scoring: Port Mathlib headers to the immutable task registry and refresh hold … |
| `sn71:scoring_commit:2026-10-13T17:04:42Z` | 71 | SCORING_COMMIT | 2026-10-13T21:35:22Z | sn71 commit touches scoring: Merge pull request #415: Verify judge provider path after fifth failur |
| `sn116:release:producer-code-r8.6` | 116 | RELEASE | 2026-10-13T21:35:22Z | sn116 released producer-code-r8.6 |
| `sn120:scoring_commit:2026-10-13T18:50:26Z` | 120 | SCORING_COMMIT | 2026-10-13T21:35:22Z | sn120 commit touches scoring: Reduce hourly evidence scan cost without changing reward assessment |
| `sn7:release:release-20261013-222136` | 7 | RELEASE | 2026-10-14T00:39:12Z | sn7 released release-20261013-222136 |
| `sn7:scoring_commit:2026-10-13T21:54:01Z` | 7 | SCORING_COMMIT | 2026-10-14T00:39:12Z | sn7 commit touches scoring: Ban a miner from scoring for 12 rounds when it posts an unusable addr… |
| `sn25:scoring_commit:2026-10-13T23:48:30Z` | 25 | SCORING_COMMIT | 2026-10-14T00:39:12Z | sn25 commit touches scoring: Merge the validator test and correctness fixes: steering-limit text, … |
| `sn45:scoring_commit:2026-10-13T06:46:35Z` | 45 | SCORING_COMMIT | 2026-10-14T00:39:12Z | sn45 commit touches scoring: soak report: read rotated validator logs |
| `sn54:scoring_commit:2026-10-13T20:00:04Z` | 54 | SCORING_COMMIT | 2026-10-14T00:39:12Z | sn54 commit touches scoring: adding in query from validators |
| `sn78:scoring_commit:2026-10-14T00:18:48Z` | 78 | SCORING_COMMIT | 2026-10-14T00:39:12Z | sn78 commit touches scoring: Merge pull request #247 from Umi-BitSign/codex/c5-geometric-reward-tr… |
| `sn120:scoring_commit:2026-10-13T22:30:02Z` | 120 | SCORING_COMMIT | 2026-10-14T00:39:12Z | sn120 commit touches scoring: Reduce repeated commitment derivation in hourly reward assessment |
| `sn25:release:v2026.10.13-1071515580` | 25 | RELEASE | 2026-10-14T05:29:19Z | sn25 released v2026.10.13-1071515580 |
| `sn25:scoring_commit:2026-10-14T04:17:54Z` | 25 | SCORING_COMMIT | 2026-10-14T05:29:19Z | sn25 commit touches scoring: Merge v2/gate-miner-tests into main |
| `sn37:scoring_commit:2026-10-14T03:25:35Z` | 37 | SCORING_COMMIT | 2026-10-14T05:29:19Z | sn37 commit touches scoring: docs: describe planned stake-retention mechanism in INCENTIVES.md |
| `sn41:scoring_commit:2026-10-13T23:52:00Z` | 41 | SCORING_COMMIT | 2026-10-14T05:29:19Z | sn41 commit touches scoring: Score update |
| `sn51:scoring_commit:2026-10-14T02:31:17Z` | 51 | SCORING_COMMIT | 2026-10-14T05:29:19Z | sn51 commit touches scoring: DAH-4035 - [P0] Validator: connect to a hostname node only at a check… |
| `sn71:scoring_commit:2026-10-14T01:25:55Z` | 71 | SCORING_COMMIT | 2026-10-14T05:29:19Z | sn71 commit touches scoring: Merge pull request #418: Preserve verified headcount ranges |
| `sn76:scoring_commit:2026-10-14T05:10:32Z` | 76 | SCORING_COMMIT | 2026-10-14T05:29:19Z | sn76 commit touches scoring: security: validate repository scope before execution |
| `sn78:scoring_commit:2026-10-14T02:15:19Z` | 78 | SCORING_COMMIT | 2026-10-14T05:29:19Z | sn78 commit touches scoring: Merge pull request #248 from Umi-BitSign/codex/durable-package-verifi… |
| `sn91:scoring_commit:2026-10-14T02:36:42Z` | 91 | SCORING_COMMIT | 2026-10-14T05:29:19Z | sn91 commit touches scoring: fix(validator): carry staged promotions across a dethrone (DEC-CA-005… |
| `sn116:scoring_commit:2026-10-14T01:37:24Z` | 116 | SCORING_COMMIT | 2026-10-14T05:29:19Z | sn116 commit touches scoring: Merge pull request #1335 from carbonphysicsai/codex/opt15c-score-lab-… |
| `sn25:release:v2026.10.14-1071632750` | 25 | RELEASE | 2026-10-14T10:39:10Z | sn25 released v2026.10.14-1071632750 |
| `sn51:scoring_commit:2026-10-14T08:21:57Z` | 51 | SCORING_COMMIT | 2026-10-14T10:39:10Z | sn51 commit touches scoring: DAH-4270 - [P1] Validator: count rented nodes the miner leaves out (s… |
| `sn67:scoring_commit:2026-10-14T06:48:35Z` | 67 | SCORING_COMMIT | 2026-10-14T10:39:10Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20261014.post3 |
| `sn71:scoring_commit:2026-10-14T09:50:39Z` | 71 | SCORING_COMMIT | 2026-10-14T10:39:10Z | sn71 commit touches scoring: Merge PR #432: repair verified domain conflicts before rebrand invest… |
| `sn76:scoring_commit:2026-10-14T06:05:09Z` | 76 | SCORING_COMMIT | 2026-10-14T10:39:10Z | sn76 commit touches scoring: security: repair frozen verifier snapshot |
| `sn78:scoring_commit:2026-10-14T06:12:46Z` | 78 | SCORING_COMMIT | 2026-10-14T10:39:10Z | sn78 commit touches scoring: Preserve native reward history through writer preparation and cutover |
| `sn108:scoring_commit:2026-10-14T09:43:47Z` | 108 | SCORING_COMMIT | 2026-10-14T10:39:10Z | sn108 commit touches scoring: Validator sends its EDA server the batch's time: time_limit_s (deadli… |
| `sn116:release:r8.7` | 116 | RELEASE | 2026-10-14T10:39:10Z | sn116 released r8.7 |
| `sn117:release:everycli v0.5.1` | 117 | RELEASE | 2026-10-14T10:39:10Z | sn117 released everycli v0.5.1 |
| `sn117:scoring_commit:2026-10-14T09:42:22Z` | 117 | SCORING_COMMIT | 2026-10-14T10:39:10Z | sn117 commit touches scoring: docs: align miner README with v0.5.1 setup and lifecycle (#29) |
| `sn51:scoring_commit:2026-10-14T14:13:17Z` | 51 | SCORING_COMMIT | 2026-10-14T15:33:11Z | sn51 commit touches scoring: DAH-4035 - [P1] Validator: resolve hostname nodes in their own thread… |
| `sn66:scoring_commit:2026-10-14T10:04:47Z` | 66 | SCORING_COMMIT | 2026-10-14T15:33:11Z | sn66 commit touches scoring: feat: extend leaderboard endpoint (add past champions challengers his… |
| `sn71:scoring_commit:2026-10-14T14:16:53Z` | 71 | SCORING_COMMIT | 2026-10-14T15:33:11Z | sn71 commit touches scoring: Merge PR #434: retain bounded validator error causes |
| `sn116:scoring_commit:2026-10-14T12:47:36Z` | 116 | SCORING_COMMIT | 2026-10-14T15:33:11Z | sn116 commit touches scoring: Merge pull request #1347 from carbonphysicsai/codex/incentive-observe… |
| `sn117:release:everycli v0.5.4` | 117 | RELEASE | 2026-10-14T15:33:11Z | sn117 released everycli v0.5.4 |
| `sn117:scoring_commit:2026-10-14T12:01:19Z` | 117 | SCORING_COMMIT | 2026-10-14T15:33:11Z | sn117 commit touches scoring: fix: profile reconnect and miner dashboard identity (v0.5.2) (#30) |
| `sn14:scoring_commit:2026-10-14T19:21:08Z` | 14 | SCORING_COMMIT | 2026-10-14T19:44:42Z | sn14 commit touches scoring: Show evaluator activity from the current worker heartbeat (#150) |
| `sn28:release:v0.4.29-dev` | 28 | RELEASE | 2026-10-14T19:44:42Z | sn28 released v0.4.29-dev |
| `sn28:scoring_commit:2026-10-14T18:30:19Z` | 28 | SCORING_COMMIT | 2026-10-14T19:44:42Z | sn28 commit touches scoring: chore(release): gm-miner 0.4.29-dev (#320) |
| `sn51:scoring_commit:2026-10-14T18:37:43Z` | 51 | SCORING_COMMIT | 2026-10-14T19:44:42Z | sn51 commit touches scoring: NO-TICKET - validator: the spot pay flag is named for the backend's p… |
| `sn76:scoring_commit:2026-10-14T18:51:37Z` | 76 | SCORING_COMMIT | 2026-10-14T19:44:42Z | sn76 commit touches scoring: security: harden public miner and validator boundaries |
| `sn78:scoring_commit:2026-10-14T16:40:24Z` | 78 | SCORING_COMMIT | 2026-10-14T19:44:42Z | sn78 commit touches scoring: Merge pull request #252 from Umi-BitSign/codex/header-verification-ca… |
| `sn96:scoring_commit:2026-10-14T19:13:46Z` | 96 | SCORING_COMMIT | 2026-10-14T19:44:42Z | sn96 commit touches scoring: fix: move the Decide validator handover to block 9,287,280 |
| `sn116:scoring_commit:2026-10-14T19:19:20Z` | 116 | SCORING_COMMIT | 2026-10-14T19:44:42Z | sn116 commit touches scoring: Merge pull request #1354 from carbonphysicsai/codex/v8-8-validator-set |
| `sn117:release:everycli v0.5.5` | 117 | RELEASE | 2026-10-14T19:44:42Z | sn117 released everycli v0.5.5 |
| `sn117:scoring_commit:2026-10-14T15:53:23Z` | 117 | SCORING_COMMIT | 2026-10-14T19:44:42Z | sn117 commit touches scoring: fix: streamline model offers and miner dashboard reporting (#33) |
| `sn21:scoring_commit:2026-10-14T20:58:47Z` | 21 | SCORING_COMMIT | 2026-10-14T22:42:49Z | sn21 commit touches scoring: perf(scoring): read receipts through a small per-day standing index |
| `sn25:scoring_commit:2026-10-14T21:15:56Z` | 25 | SCORING_COMMIT | 2026-10-14T22:42:49Z | sn25 commit touches scoring: State that any v2 request checkpoint write blocks a validator downgrad |
| `sn28:release:v0.5.0` | 28 | RELEASE | 2026-10-14T22:42:49Z | sn28 released v0.5.0 |
| `sn28:scoring_commit:2026-10-14T21:33:01Z` | 28 | SCORING_COMMIT | 2026-10-14T22:42:49Z | sn28 commit touches scoring: chore(release): promote gm-miner 0.5.0 (#322) |
| `sn78:scoring_commit:2026-10-14T22:06:52Z` | 78 | SCORING_COMMIT | 2026-10-14T22:42:49Z | sn78 commit touches scoring: Keep stopped reward reconciliation alive across native history batches |
| `sn116:scoring_commit:2026-10-14T22:11:40Z` | 116 | SCORING_COMMIT | 2026-10-14T22:42:49Z | sn116 commit touches scoring: Merge pull request #1365 from carbonphysicsai/codex/score-lab-champio… |
| `sn117:release:everycli v0.5.6` | 117 | RELEASE | 2026-10-14T22:42:49Z | sn117 released everycli v0.5.6 |
| `sn120:scoring_commit:2026-10-14T20:48:32Z` | 120 | SCORING_COMMIT | 2026-10-14T22:42:49Z | sn120 commit touches scoring: Award contested tasks to the earliest Cloudflare R2 claim |
| `sn8:scoring_commit:2026-10-14T22:26:16Z` | 8 | SCORING_COMMIT | 2026-10-15T00:57:43Z | sn8 commit touches scoring: Sync price updates and challenge loop (#954) |
| `sn25:scoring_commit:2026-10-15T00:43:14Z` | 25 | SCORING_COMMIT | 2026-10-15T00:57:43Z | sn25 commit touches scoring: Select the startup verified tests and pin the memo's replay edge |
| `sn101:readme_task_diff:69a3be15960a468f` | 101 | README_TASK_DIFF | 2026-10-09T06:48:38Z | sn101 README task/scoring sections changed |
| `sn76:readme_task_diff:c11a1b8d6bd23a9b` | 76 | README_TASK_DIFF | 2026-10-09T14:20:19Z | sn76 README task/scoring sections changed |
| `sn48:readme_task_diff:681058003f640cf6` | 48 | README_TASK_DIFF | 2026-10-09T19:37:09Z | sn48 README task/scoring sections changed |
| `sn66:readme_task_diff:53ca2fbbcaa75039` | 66 | README_TASK_DIFF | 2026-10-09T19:37:09Z | sn66 README task/scoring sections changed |
| `sn79:readme_task_diff:1ab076cd7112df84` | 79 | README_TASK_DIFF | 2026-10-09T19:37:09Z | sn79 README task/scoring sections changed |
| `sn117:readme_task_diff:ad8c3f68204b01ab` | 117 | README_TASK_DIFF | 2026-10-09T19:37:09Z | sn117 README task/scoring sections changed |
| `sn76:readme_task_diff:0a4c226e1573572b` | 76 | README_TASK_DIFF | 2026-10-11T19:38:20Z | sn76 README task/scoring sections changed |
| `sn117:readme_task_diff:1f5936ceb48b4e59` | 117 | README_TASK_DIFF | 2026-10-11T19:38:20Z | sn117 README task/scoring sections changed |
| `sn117:readme_task_diff:0f4be566c399b388` | 117 | README_TASK_DIFF | 2026-10-11T23:13:02Z | sn117 README task/scoring sections changed |
| `sn28:readme_task_diff:a275dd150e9b5f4f` | 28 | README_TASK_DIFF | 2026-10-12T19:47:00Z | sn28 README task/scoring sections changed |
| `sn117:readme_task_diff:4631619b61bf245f` | 117 | README_TASK_DIFF | 2026-10-12T19:47:00Z | sn117 README task/scoring sections changed |
| `sn117:readme_task_diff:98a036ed300e2537` | 117 | README_TASK_DIFF | 2026-10-13T08:31:47Z | sn117 README task/scoring sections changed |
| `sn37:readme_task_diff:f7819507937d66e4` | 37 | README_TASK_DIFF | 2026-10-13T16:29:14Z | sn37 README task/scoring sections changed |
| `sn117:readme_task_diff:0955f3d4e32cce12` | 117 | README_TASK_DIFF | 2026-10-13T16:29:14Z | sn117 README task/scoring sections changed |
| `sn117:readme_task_diff:a5f1105da1e310ab` | 117 | README_TASK_DIFF | 2026-10-13T21:35:22Z | sn117 README task/scoring sections changed |
| `sn37:readme_task_diff:6ee01103ec5344ac` | 37 | README_TASK_DIFF | 2026-10-14T05:29:19Z | sn37 README task/scoring sections changed |
| `sn117:readme_task_diff:ffe23d677b34cef6` | 117 | README_TASK_DIFF | 2026-10-14T19:44:42Z | sn117 README task/scoring sections changed |
| `sn117:readme_task_diff:e92bc71aef91f2cd` | 117 | README_TASK_DIFF | 2026-10-14T22:42:49Z | sn117 README task/scoring sections changed |

## RESOLVED IN THIS WINDOW

_none_
