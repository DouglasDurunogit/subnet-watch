# ALARMS - generated 2026-08-22T08:44:36Z, block 8899292

window: first_seen in [2026-08-22T07:30:06Z, 2026-08-22T08:45:06Z)  (60 min interval + 15 min overlap)

Report ONLY the rows under NEW SINCE LAST RUN. Rows under STILL OPEN were
already reported in an earlier window and must not be re-alarmed.

## NEW SINCE LAST RUN

| event_id | netuid | class | severity | first_seen_utc | one_line |
|---|---|---|---|---|---|
| `sn61:release:4.9.7` | 61 | RELEASE | P1 | 2026-08-22T08:03:45Z | sn61 released 4.9.7 |
| `sn61:scoring_commit:2026-08-22T02:19:35Z` | 61 | SCORING_COMMIT | P1 | 2026-08-22T08:03:45Z | sn61 commit touches scoring: deps: update abs_challenge submodule to version 6.0.4 |
| `sn92:release:v0.1.2` | 92 | RELEASE | P1 | 2026-08-22T08:03:45Z | sn92 released v0.1.2 |
| `sn92:release:v0.1.3` | 92 | RELEASE | P1 | 2026-08-22T08:45:06Z | sn92 released v0.1.3 |

### detail

- **`sn61:release:4.9.7`** - sn61 released 4.9.7
  - published 2026-08-22T07:42:19Z (was 4.9.6)
- **`sn61:scoring_commit:2026-08-22T02:19:35Z`** - sn61 commit touches scoring: deps: update abs_challenge submodule to version 6.0.4
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn92:release:v0.1.2`** - sn92 released v0.1.2
  - published 2026-08-22T07:55:29Z (was v0.1.1)
- **`sn92:release:v0.1.3`** - sn92 released v0.1.3
  - published 2026-08-22T08:22:01Z (was v0.1.2)

## STILL OPEN (already reported - do not re-alarm)

| event_id | netuid | class | first_seen_utc | one_line |
|---|---|---|---|---|
| `sn2:burn_drop:0.823` | 2 | BURN_DROP | 2026-08-17T06:00:04Z | sn2 burn fell 1.000 -> 0.823 - miners can earn again |
| `sn121:burn_drop:0.620` | 121 | BURN_DROP | 2026-08-17T15:52:42Z | sn121 burn fell 1.000 -> 0.620 - miners can earn again |
| `sn2:burn_drop:0.825` | 2 | BURN_DROP | 2026-08-18T13:05:31Z | sn2 burn fell 1.000 -> 0.825 - miners can earn again |
| `sn108:burn_drop:0.838` | 108 | BURN_DROP | 2026-08-18T20:36:36Z | sn108 burn fell 1.000 -> 0.838 - miners can earn again |
| `sn14:burn_drop:0.298` | 14 | BURN_DROP | 2026-08-19T01:50:06Z | sn14 burn fell 1.000 -> 0.298 - miners can earn again |
| `sn121:burn_drop:0.607` | 121 | BURN_DROP | 2026-08-19T03:08:34Z | sn121 burn fell 1.000 -> 0.607 - miners can earn again |
| `sn108:burn_drop:0.839` | 108 | BURN_DROP | 2026-08-19T04:51:04Z | sn108 burn fell 1.000 -> 0.839 - miners can earn again |
| `sn62:burn_drop:0.000` | 62 | BURN_DROP | 2026-08-19T08:02:31Z | sn62 burn fell 1.000 -> 0.000 - miners can earn again |
| `sn23:burn_drop:0.847` | 23 | BURN_DROP | 2026-08-19T11:36:23Z | sn23 burn fell 1.000 -> 0.847 - miners can earn again |
| `sn103:burn_drop:0.845` | 103 | BURN_DROP | 2026-08-19T18:50:48Z | sn103 burn fell 1.000 -> 0.845 - miners can earn again |
| `sn80:burn_drop:0.908` | 80 | BURN_DROP | 2026-08-20T05:42:25Z | sn80 burn fell 1.000 -> 0.908 - miners can earn again |
| `sn7:burn_drop:0.978` | 7 | BURN_DROP | 2026-08-20T08:54:06Z | sn7 burn fell 0.992 -> 0.978 - miners can earn again |
| `sn113:burn_drop:0.990` | 113 | BURN_DROP | 2026-08-20T08:54:06Z | sn113 burn fell 1.000 -> 0.990 - miners can earn again |
| `sn121:burn_drop:0.611` | 121 | BURN_DROP | 2026-08-20T18:15:10Z | sn121 burn fell 1.000 -> 0.611 - miners can earn again |
| `sn67:scoring_commit:2026-08-15T08:24:59Z` | 67 | SCORING_COMMIT | 2026-08-15T09:06:33Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20260815.post1 |
| `sn100:scoring_commit:2026-08-15T12:26:39Z` | 100 | SCORING_COMMIT | 2026-08-15T12:56:35Z | sn100 commit touches scoring: feat(prism): live leaf from G2 benchmarks (scoring_version 4) (#160) |
| `sn100:scoring_commit:2026-08-15T13:20:08Z` | 100 | SCORING_COMMIT | 2026-08-15T13:39:18Z | sn100 commit touches scoring: fix(prism): rename lattice_score to satisfy clippy similar_names |
| `sn76:scoring_commit:2026-08-15T17:47:00Z` | 76 | SCORING_COMMIT | 2026-08-15T17:59:54Z | sn76 commit touches scoring: Add a local evaluation command |
| `sn108:scoring_commit:2026-08-15T20:13:27Z` | 108 | SCORING_COMMIT | 2026-08-15T20:35:26Z | sn108 commit touches scoring: docs(miner): drop the second artefact that was never built |
| `sn76:scoring_commit:2026-08-15T23:00:47Z` | 76 | SCORING_COMMIT | 2026-08-15T23:01:41Z | sn76 commit touches scoring: Raise tasks per round across all four tracks |
| `sn71:scoring_commit:2026-08-15T21:01:49Z` | 71 | SCORING_COMMIT | 2026-08-16T01:55:21Z | sn71 commit touches scoring: Fix validator RPC boundary fixture |
| `sn111:scoring_commit:2026-08-16T00:43:24Z` | 111 | SCORING_COMMIT | 2026-08-16T01:55:21Z | sn111 commit touches scoring: Implement resilient batch scoring and winner-takes-most payouts |
| `sn71:scoring_commit:2026-08-16T03:33:59Z` | 71 | SCORING_COMMIT | 2026-08-16T04:08:02Z | sn71 commit touches scoring: Regenerate validator protected workflow manifest |
| `sn67:scoring_commit:2026-08-16T05:46:07Z` | 67 | SCORING_COMMIT | 2026-08-16T06:04:05Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20260816.post0 |
| `sn71:scoring_commit:2026-08-16T04:12:13Z` | 71 | SCORING_COMMIT | 2026-08-16T06:04:05Z | sn71 commit touches scoring: Preserve production clocks in parity validation |
| `sn76:scoring_commit:2026-08-16T07:37:40Z` | 76 | SCORING_COMMIT | 2026-08-16T07:41:32Z | sn76 commit touches scoring: Match CWEs numerically, draw tasks per validator, break ties determin… |
| `sn100:release:v3.3.22` | 100 | RELEASE | 2026-08-16T08:44:18Z | sn100 released v3.3.22 |
| `sn76:scoring_commit:2026-08-16T11:49:10Z` | 76 | SCORING_COMMIT | 2026-08-16T12:00:10Z | sn76 commit touches scoring: Download only the tasks a validator drew |
| `sn68:scoring_commit:2026-08-16T13:01:09Z` | 68 | SCORING_COMMIT | 2026-08-16T13:40:28Z | sn68 commit touches scoring: discard individual validator processing failures before averaging scor |
| `sn100:release:v3.3.23` | 100 | RELEASE | 2026-08-16T16:00:34Z | sn100 released v3.3.23 |
| `sn75:scoring_commit:2026-08-16T16:01:02Z` | 75 | SCORING_COMMIT | 2026-08-16T16:38:36Z | sn75 commit touches scoring: Merge pull request #49 from thenervelab/feat/compute-scoring-runtime |
| `sn85:scoring_commit:2026-08-16T16:50:58Z` | 85 | SCORING_COMMIT | 2026-08-16T17:03:28Z | sn85 commit touches scoring: retry inviting rejected miner UIDs in competition enrollment due to l… |
| `sn100:release:v3.3.24` | 100 | RELEASE | 2026-08-16T17:31:56Z | sn100 released v3.3.24 |
| `sn71:scoring_commit:2026-08-16T23:14:51Z` | 71 | SCORING_COMMIT | 2026-08-17T01:52:42Z | sn71 commit touches scoring: Bound validator worker startup verification |
| `sn71:scoring_commit:2026-08-17T00:26:35Z` | 71 | SCORING_COMMIT | 2026-08-17T06:00:04Z | sn71 commit touches scoring: Refresh provider failures during recovery scoring |
| `sn51:release:executor-v1.120` | 51 | RELEASE | 2026-08-17T08:07:06Z | sn51 released executor-v1.120 |
| `sn75:scoring_commit:2026-08-16T20:57:11Z` | 75 | SCORING_COMMIT | 2026-08-17T08:07:06Z | sn75 commit touches scoring: feat(compute-scoring): root-settable dedicated key for vali submission |
| `sn85:scoring_commit:2026-08-17T08:37:37Z` | 85 | SCORING_COMMIT | 2026-08-17T08:59:45Z | sn85 commit touches scoring: reinvite miners rejected with flag INVITATION_DECLINED in comp enroll… |
| `sn10:scoring_commit:2026-08-17T09:07:35Z` | 10 | SCORING_COMMIT | 2026-08-17T09:54:33Z | sn10 commit touches scoring: feat(bench): score the full workload trace (PAR-65) (#81) |
| `sn67:scoring_commit:2026-08-17T05:33:14Z` | 67 | SCORING_COMMIT | 2026-08-17T10:46:02Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20260817.post0 |
| `sn85:scoring_commit:2026-08-17T10:23:08Z` | 85 | SCORING_COMMIT | 2026-08-17T10:46:02Z | sn85 commit touches scoring: ensure comp scoring worker can access Modal SDK for fetching Modal vo… |
| `sn114:scoring_commit:2026-08-17T09:54:21Z` | 114 | SCORING_COMMIT | 2026-08-17T10:46:02Z | sn114 commit touches scoring: perf(validator): reduce validator write contention |
| `sn85:scoring_commit:2026-08-17T10:59:02Z` | 85 | SCORING_COMMIT | 2026-08-17T11:12:02Z | sn85 commit touches scoring: treat miner sandbox raised error as miner issue rather than validator… |
| `sn111:scoring_commit:2026-08-17T11:55:09Z` | 111 | SCORING_COMMIT | 2026-08-17T13:03:27Z | sn111 commit touches scoring: feat: add adaptive miner selection and run assignment snapshots |
| `sn114:scoring_commit:2026-08-17T12:09:26Z` | 114 | SCORING_COMMIT | 2026-08-17T13:03:27Z | sn114 commit touches scoring: hotfix(scoring): exclude comp 112 stage 2 from final score |
| `sn10:scoring_commit:2026-08-17T16:31:51Z` | 10 | SCORING_COMMIT | 2026-08-17T16:41:40Z | sn10 commit touches scoring: feat: better miner commit patch logs (#83) |
| `sn21:release:SN21 training bundle (1977 records, refr` | 21 | RELEASE | 2026-08-17T18:54:41Z | sn21 released SN21 training bundle (1977 records, refreshed 2026-08-17 18:05 UTC) |
| `sn51:release:executor-v1.121` | 51 | RELEASE | 2026-08-17T19:36:49Z | sn51 released executor-v1.121 |
| `sn65:scoring_commit:2026-08-14T10:47:05Z` | 65 | SCORING_COMMIT | 2026-08-17T19:36:49Z | sn65 commit touches scoring: Merge pull request #3 from taofu-labs/validator-v2 |
| `sn21:release:SN21 training bundle — 10,791 records, r` | 21 | RELEASE | 2026-08-17T21:09:19Z | sn21 released SN21 training bundle — 10,791 records, refreshed 2026-08-17 |
| `sn54:scoring_commit:2026-08-17T16:25:21Z` | 54 | SCORING_COMMIT | 2026-08-17T22:36:59Z | sn54 commit touches scoring: updating miner info |
| `sn62:release:v0.2.8` | 62 | RELEASE | 2026-08-17T22:36:59Z | sn62 released v0.2.8 |
| `sn14:release:v2-finite-debt-preextraction: Pre-extrac` | 14 | RELEASE | 2026-08-17T23:02:57Z | sn14 released v2-finite-debt-preextraction: Pre-extraction snapshot of the inactive V2 finite-debt economics. |
| `sn56:scoring_commit:2026-08-17T23:44:09Z` | 56 | SCORING_COMMIT | 2026-08-18T00:01:21Z | sn56 commit touches scoring: Fix re-finalize crowning the re-evaluated miner instead of re-ranking… |
| `sn71:scoring_commit:2026-08-18T01:01:27Z` | 71 | SCORING_COMMIT | 2026-08-18T01:47:42Z | sn71 commit touches scoring: Repair semantic gate verification fixtures |
| `sn15:release:v1.2.7` | 15 | RELEASE | 2026-08-18T02:44:45Z | sn15 released v1.2.7 |
| `sn91:release:pre-decay-wsd-contract` | 91 | RELEASE | 2026-08-18T04:21:04Z | sn91 released pre-decay-wsd-contract |
| `sn91:scoring_commit:2026-08-15T10:55:48Z` | 91 | SCORING_COMMIT | 2026-08-18T04:21:04Z | sn91 commit touches scoring: audit fixes + miner CLI: warm-start init visibility in `cascade heat` |
| `sn85:scoring_commit:2026-08-18T06:57:35Z` | 85 | SCORING_COMMIT | 2026-08-18T07:14:18Z | sn85 commit touches scoring: debug VBR scoring in compression competitions (#196) |
| `sn89:scoring_commit:2026-08-18T07:04:57Z` | 89 | SCORING_COMMIT | 2026-08-18T07:14:18Z | sn89 commit touches scoring: hf board: keep a re-rolled miner's retired hotkey attributed to its o… |
| `sn51:scoring_commit:2026-08-18T08:26:35Z` | 51 | SCORING_COMMIT | 2026-08-18T08:51:13Z | sn51 commit touches scoring: DAH-2702: verify GPU persistence mode after -pm 1 in the power cap (#… |
| `sn67:scoring_commit:2026-08-18T06:10:26Z` | 67 | SCORING_COMMIT | 2026-08-18T09:46:16Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20260818.post0 |
| `sn65:scoring_commit:2026-08-18T10:41:48Z` | 65 | SCORING_COMMIT | 2026-08-18T10:55:56Z | sn65 commit touches scoring: Merge pull request #4 from taofu-labs/docs/validator |
| `sn67:scoring_commit:2026-08-18T10:35:47Z` | 67 | SCORING_COMMIT | 2026-08-18T10:55:56Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20260818.post1 |
| `sn81:scoring_commit:2026-08-18T07:52:08Z` | 81 | SCORING_COMMIT | 2026-08-18T13:55:30Z | sn81 commit touches scoring: test: lock v4 canonical reward flow |
| `sn108:scoring_commit:2026-08-18T13:35:17Z` | 108 | SCORING_COMMIT | 2026-08-18T13:55:30Z | sn108 commit touches scoring: Docs: the eligible-miner gate is 50 active members, not 500 |
| `sn1:release:v4.3.3` | 1 | RELEASE | 2026-08-18T14:48:11Z | sn1 released v4.3.3 |
| `sn23:scoring_commit:2026-08-18T14:09:05Z` | 23 | SCORING_COMMIT | 2026-08-18T14:48:11Z | sn23 commit touches scoring: Merge pull request #47 from TrishoolAI/feat/challenge-creation |
| `sn28:release:v0.4.5` | 28 | RELEASE | 2026-08-18T14:48:11Z | sn28 released v0.4.5 |
| `sn28:scoring_commit:2026-08-18T14:43:57Z` | 28 | SCORING_COMMIT | 2026-08-18T14:48:11Z | sn28 commit touches scoring: Release gm-miner v0.4.5 |
| `sn33:scoring_commit:2026-08-18T14:35:53Z` | 33 | SCORING_COMMIT | 2026-08-18T14:48:11Z | sn33 commit touches scoring: Merge pull request #135 from afterpartyai/Feat-Add-Skills-Cov-task |
| `sn53:scoring_commit:2026-08-18T15:05:58Z` | 53 | SCORING_COMMIT | 2026-08-18T15:42:54Z | sn53 commit touches scoring: miner: tee_miner, a pure gateway leg with provider-assigned identity … |
| `sn108:scoring_commit:2026-08-18T14:52:43Z` | 108 | SCORING_COMMIT | 2026-08-18T15:42:54Z | sn108 commit touches scoring: Burn 60% of miner emission, split the other 40% by score |
| `sn96:release:Verathos v0.1.41 - Bounded Replay and Ru` | 96 | RELEASE | 2026-08-18T16:12:17Z | sn96 released Verathos v0.1.41 - Bounded Replay and Runtime Stability |
| `sn96:scoring_commit:2026-08-18T12:39:12Z` | 96 | SCORING_COMMIT | 2026-08-18T16:12:17Z | sn96 commit touches scoring: fix: prevent validator-created audit overlap |
| `sn21:scoring_commit:2026-08-18T16:03:58Z` | 21 | SCORING_COMMIT | 2026-08-18T16:57:50Z | sn21 commit touches scoring: validator: daily-stream override was silently dropping every miner (s… |
| `sn92:scoring_commit:2026-08-18T12:27:47Z` | 92 | SCORING_COMMIT | 2026-08-18T16:57:50Z | sn92 commit touches scoring: Correct the loopback sample output in the validator guide |
| `sn21:scoring_commit:2026-08-18T17:28:33Z` | 21 | SCORING_COMMIT | 2026-08-18T17:39:02Z | sn21 commit touches scoring: validator: daily-stream API path crashed on unbound _vol after the ss… |
| `sn25:release:v2026.8.17-1021635350` | 25 | RELEASE | 2026-08-18T17:39:02Z | sn25 released v2026.8.17-1021635350 |
| `sn25:scoring_commit:2026-08-04T21:03:12Z` | 25 | SCORING_COMMIT | 2026-08-18T17:39:02Z | sn25 commit touches scoring: Merge pull request #3 from Ryanmello07/fix/windows-miner-exe-suffix-u… |
| `sn62:scoring_commit:2026-08-18T17:56:49Z` | 62 | SCORING_COMMIT | 2026-08-18T18:13:46Z | sn62 commit touches scoring: Merge pull request #480 from ridgesai/update/add-testnet-validator |
| `sn15:scoring_commit:2026-08-18T18:29:41Z` | 15 | SCORING_COMMIT | 2026-08-18T19:07:17Z | sn15 commit touches scoring: docs(miner-guide): note that find_product q matches values, not keys … |
| `sn75:scoring_commit:2026-08-18T19:33:43Z` | 75 | SCORING_COMMIT | 2026-08-18T19:40:34Z | sn75 commit touches scoring: Merge pull request #51 from thenervelab/feat/pay-compute-miners |
| `sn108:scoring_commit:2026-08-18T19:13:55Z` | 108 | SCORING_COMMIT | 2026-08-18T19:40:34Z | sn108 commit touches scoring: docs(validator): clarify CHUTES_API_KEY is the owner-issued shared key |
| `sn111:scoring_commit:2026-08-18T20:20:14Z` | 111 | SCORING_COMMIT | 2026-08-18T20:36:36Z | sn111 commit touches scoring: feat(scoring): gate Silver coverage on evidence support |
| `sn120:scoring_commit:2026-08-18T20:00:48Z` | 120 | SCORING_COMMIT | 2026-08-18T20:36:36Z | sn120 commit touches scoring: Sync Reason v4 (wvk=7) into score, contract, website, and docs. |
| `sn81:scoring_commit:2026-08-18T20:37:01Z` | 81 | SCORING_COMMIT | 2026-08-18T21:04:08Z | sn81 commit touches scoring: fix(weights): burn to this validator's own uid, not a hardcoded 0 |
| `sn71:scoring_commit:2026-08-18T21:09:08Z` | 71 | SCORING_COMMIT | 2026-08-18T21:35:40Z | sn71 commit touches scoring: Verify restored parity database contract |
| `sn28:release:v0.4.6-dev` | 28 | RELEASE | 2026-08-18T22:37:17Z | sn28 released v0.4.6-dev |
| `sn28:scoring_commit:2026-08-18T22:12:25Z` | 28 | SCORING_COMMIT | 2026-08-18T22:37:17Z | sn28 commit touches scoring: Release gm-miner v0.4.6-dev |
| `sn62:scoring_commit:2026-08-18T20:59:53Z` | 62 | SCORING_COMMIT | 2026-08-18T22:37:17Z | sn62 commit touches scoring: pass pre_screening_policy_version and remove from validator |
| `sn62:release:v0.2.9` | 62 | RELEASE | 2026-08-18T23:03:26Z | sn62 released v0.2.9 |
| `sn46:scoring_commit:2026-08-18T23:50:25Z` | 46 | SCORING_COMMIT | 2026-08-19T00:01:39Z | sn46 commit touches scoring: test: freeze validator report contract |
| `sn46:scoring_commit:2026-08-19T01:46:55Z` | 46 | SCORING_COMMIT | 2026-08-19T01:50:06Z | sn46 commit touches scoring: Merge pull request #18 from instant-subnet/dan/p4-5-run-once-validator |
| `sn71:scoring_commit:2026-08-18T23:59:05Z` | 71 | SCORING_COMMIT | 2026-08-19T01:50:06Z | sn71 commit touches scoring: Isolate parity scoring cache |
| `sn111:scoring_commit:2026-08-19T00:57:56Z` | 111 | SCORING_COMMIT | 2026-08-19T01:50:06Z | sn111 commit touches scoring: fix validator batch reliability and provider resilience |
| `sn46:scoring_commit:2026-08-19T02:41:53Z` | 46 | SCORING_COMMIT | 2026-08-19T03:08:34Z | sn46 commit touches scoring: Merge pull request #20 from instant-subnet/dan/p4-final-validator-depl |
| `sn108:scoring_commit:2026-08-19T05:41:54Z` | 108 | SCORING_COMMIT | 2026-08-19T05:42:50Z | sn108 commit touches scoring: docs(validator): tell operators to re-post weights between cycles (#4) |
| `sn100:release:v3.3.25: fix(prism): stop control-plane ` | 100 | RELEASE | 2026-08-19T07:15:10Z | sn100 released v3.3.25: fix(prism): stop control-plane OOM restarts |
| `sn92:scoring_commit:2026-08-19T07:50:37Z` | 92 | SCORING_COMMIT | 2026-08-19T08:02:31Z | sn92 commit touches scoring: Declare pynacl for token verification |
| `sn71:scoring_commit:2026-08-19T07:32:51Z` | 71 | SCORING_COMMIT | 2026-08-19T08:52:29Z | sn71 commit touches scoring: Use verified local rehearsal base |
| `sn97:scoring_commit:2026-08-18T22:22:27Z` | 97 | SCORING_COMMIT | 2026-08-19T08:52:29Z | sn97 commit touches scoring: feat: score looped trajectories 0 without calling the judge |
| `sn76:scoring_commit:2026-08-19T08:54:49Z` | 76 | SCORING_COMMIT | 2026-08-19T09:46:14Z | sn76 commit touches scoring: Report an abstained row when a track has no task set |
| `sn14:scoring_commit:2026-08-19T07:56:03Z` | 14 | SCORING_COMMIT | 2026-08-19T10:13:41Z | sn14 commit touches scoring: Burn a departed claimant's share to the validator instead of holding … |
| `sn28:release:v0.4.8-dev` | 28 | RELEASE | 2026-08-19T10:54:46Z | sn28 released v0.4.8-dev |
| `sn28:scoring_commit:2026-08-19T10:18:25Z` | 28 | SCORING_COMMIT | 2026-08-19T10:54:46Z | sn28 commit touches scoring: Expand verified NEAR model coverage |
| `sn44:scoring_commit:2026-08-19T10:16:23Z` | 44 | SCORING_COMMIT | 2026-08-19T10:54:46Z | sn44 commit touches scoring: Merge pull request #53 from score-technologies/prv-hf-bfr-commit |
| `sn51:scoring_commit:2026-08-19T10:32:10Z` | 51 | SCORING_COMMIT | 2026-08-19T10:54:46Z | sn51 commit touches scoring: DAH-2703: withhold unrented incentive when a host kills the filler at… |
| `sn51:release:executor-v1.122` | 51 | RELEASE | 2026-08-19T11:36:23Z | sn51 released executor-v1.122 |
| `sn71:scoring_commit:2026-08-19T10:57:23Z` | 71 | SCORING_COMMIT | 2026-08-19T11:36:23Z | sn71 commit touches scoring: Preserve validator app modes in restart rehearsal |
| `sn108:scoring_commit:2026-08-19T10:55:26Z` | 108 | SCORING_COMMIT | 2026-08-19T11:36:23Z | sn108 commit touches scoring: feat(scoring): burn 40%, pay 40% for data and 20% for models (#6) |
| `sn14:release:v2.1.0` | 14 | RELEASE | 2026-08-19T13:56:35Z | sn14 released v2.1.0 |
| `sn28:release:v0.4.8` | 28 | RELEASE | 2026-08-19T13:56:35Z | sn28 released v0.4.8 |
| `sn28:scoring_commit:2026-08-19T13:23:34Z` | 28 | SCORING_COMMIT | 2026-08-19T13:56:35Z | sn28 commit touches scoring: Release gm-miner v0.4.8 |
| `sn81:scoring_commit:2026-08-19T13:11:10Z` | 81 | SCORING_COMMIT | 2026-08-19T13:56:35Z | sn81 commit touches scoring: Merge pull request #184 from reliquadotai/perf/pi-old-from-verify-log… |
| `sn92:scoring_commit:2026-08-19T13:15:41Z` | 92 | SCORING_COMMIT | 2026-08-19T13:56:35Z | sn92 commit touches scoring: Cut the validator guide to specs and steps |
| `sn108:scoring_commit:2026-08-19T14:31:17Z` | 108 | SCORING_COMMIT | 2026-08-19T14:49:08Z | sn108 commit touches scoring: docs(miner): say which architectures the image can actually load (#8) |
| `sn108:scoring_commit:2026-08-19T15:01:26Z` | 108 | SCORING_COMMIT | 2026-08-19T15:42:46Z | sn108 commit touches scoring: feat(miner): refuse an architecture the image cannot load, at render … |
| `sn111:scoring_commit:2026-08-19T15:56:47Z` | 111 | SCORING_COMMIT | 2026-08-19T16:12:42Z | sn111 commit touches scoring: feat(scoring): bound eligible claims and adjudication cases |
| `sn71:scoring_commit:2026-08-19T16:17:00Z` | 71 | SCORING_COMMIT | 2026-08-19T16:56:08Z | sn71 commit touches scoring: Retry pinned validator yum installs safely |
| `sn1:release:v4.3.4` | 1 | RELEASE | 2026-08-19T18:02:34Z | sn1 released v4.3.4 |
| `sn46:scoring_commit:2026-08-19T18:42:46Z` | 46 | SCORING_COMMIT | 2026-08-19T18:50:48Z | sn46 commit touches scoring: Merge pull request #21 from instant-subnet/niki/fix-finney-validator-… |
| `sn46:scoring_commit:2026-08-19T19:00:28Z` | 46 | SCORING_COMMIT | 2026-08-19T19:35:24Z | sn46 commit touches scoring: Restore validator log visibility after the bittensor import |
| `sn25:release:v2026.8.19-1023689220` | 25 | RELEASE | 2026-08-19T20:02:56Z | sn25 released v2026.8.19-1023689220 |
| `sn51:release:executor-v1.123` | 51 | RELEASE | 2026-08-19T20:02:56Z | sn51 released executor-v1.123 |
| `sn108:scoring_commit:2026-08-19T19:48:52Z` | 108 | SCORING_COMMIT | 2026-08-19T20:02:56Z | sn108 commit touches scoring: feat!: validators run miners' models; remove Chutes entirely (#14) |
| `sn1:release:v4.3.5` | 1 | RELEASE | 2026-08-19T20:41:24Z | sn1 released v4.3.5 |
| `sn10:scoring_commit:2026-08-19T20:15:33Z` | 10 | SCORING_COMMIT | 2026-08-19T21:11:13Z | sn10 commit touches scoring: feat(bench): harness round mode with a single batched scorer |
| `sn38:scoring_commit:2026-08-19T20:55:05Z` | 38 | SCORING_COMMIT | 2026-08-19T21:11:13Z | sn38 commit touches scoring: Add multi-layer dedup and weighted leak evaluation (#24) |
| `sn7:release:release-20260819-213008: Record the finn` | 7 | RELEASE | 2026-08-19T21:50:36Z | sn7 released release-20260819-213008: Record the finney TAO bond vault address (#696) |
| `sn7:scoring_commit:2026-08-14T17:14:52Z` | 7 | SCORING_COMMIT | 2026-08-19T21:50:36Z | sn7 commit touches scoring: Trim pre-window crown tails before the scoring-window wipe (#676) |
| `sn81:scoring_commit:2026-08-19T18:29:14Z` | 81 | SCORING_COMMIT | 2026-08-19T21:50:36Z | sn81 commit touches scoring: feat(validator): pipelined window collection behind a flag (default of |
| `sn7:release:release-20260819-235753: Activate: quoru` | 7 | RELEASE | 2026-08-20T00:02:25Z | sn7 released release-20260819-235753: Activate: quorum short-circuit + 30s default dendrite timeout (#697) |
| `sn26:scoring_commit:2026-08-19T18:10:08Z` | 26 | SCORING_COMMIT | 2026-08-20T01:53:55Z | sn26 commit touches scoring: Merge pull request #51 from 0xsigurd/feat/cross-validator-score-conse… |
| `sn71:scoring_commit:2026-08-20T01:36:55Z` | 71 | SCORING_COMMIT | 2026-08-20T01:53:55Z | sn71 commit touches scoring: Preserve verifier literals in restart bootstrap |
| `sn108:scoring_commit:2026-08-20T00:05:32Z` | 108 | SCORING_COMMIT | 2026-08-20T01:53:55Z | sn108 commit touches scoring: fix(cli): model verify printed fields the verdict no longer carries (… |
| `sn71:scoring_commit:2026-08-20T02:22:02Z` | 71 | SCORING_COMMIT | 2026-08-20T03:07:36Z | sn71 commit touches scoring: test: rehearse miner maintenance first rollout |
| `sn92:scoring_commit:2026-08-20T03:03:09Z` | 92 | SCORING_COMMIT | 2026-08-20T03:07:36Z | sn92 commit touches scoring: Show miners the cutoff and what their components earn |
| `sn21:release:SN21 rich training data v2` | 21 | RELEASE | 2026-08-20T03:58:21Z | sn21 released SN21 rich training data v2 |
| `sn23:scoring_commit:2026-08-20T03:45:52Z` | 23 | SCORING_COMMIT | 2026-08-20T03:58:21Z | sn23 commit touches scoring: Merge pull request #48 from TrishoolAI/feat/challenge-creation |
| `sn100:scoring_commit:2026-08-20T03:53:06Z` | 100 | SCORING_COMMIT | 2026-08-20T03:58:21Z | sn100 commit touches scoring: Merge pull request #166 from BaseIntelligence/prism-v2.1-scoring |
| `sn71:scoring_commit:2026-08-20T03:58:52Z` | 71 | SCORING_COMMIT | 2026-08-20T04:49:21Z | sn71 commit touches scoring: Preserve restart timing across miner bootstrap handoff |
| `sn111:scoring_commit:2026-08-20T07:12:31Z` | 111 | SCORING_COMMIT | 2026-08-20T07:23:41Z | sn111 commit touches scoring: fix(scoring): handle missing claim assessments safely |
| `sn51:scoring_commit:2026-08-20T07:41:14Z` | 51 | SCORING_COMMIT | 2026-08-20T08:05:07Z | sn51 commit touches scoring: DAH-2715: withhold the unrented incentive from executors that cannot … |
| `sn71:scoring_commit:2026-08-20T08:18:13Z` | 71 | SCORING_COMMIT | 2026-08-20T08:54:06Z | sn71 commit touches scoring: Keep validator CID diagnostics off JSON stdout |
| `sn75:scoring_commit:2026-08-20T08:51:35Z` | 75 | SCORING_COMMIT | 2026-08-20T08:54:06Z | sn75 commit touches scoring: Merge pull request #53 from thenervelab/fix/payminers-from-arion |
| `sn67:scoring_commit:2026-08-20T07:52:49Z` | 67 | SCORING_COMMIT | 2026-08-20T09:47:27Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20260820.post5 |
| `sn92:scoring_commit:2026-08-20T09:42:59Z` | 92 | SCORING_COMMIT | 2026-08-20T09:47:27Z | sn92 commit touches scoring: Take telemetry from miners and serve it back |
| `sn100:release:v3.3.26: fix(validator): persist last se` | 100 | RELEASE | 2026-08-20T09:47:27Z | sn100 released v3.3.26: fix(validator): persist last sealed bundle across restarts |
| `sn100:scoring_commit:2026-08-20T09:41:45Z` | 100 | SCORING_COMMIT | 2026-08-20T09:47:27Z | sn100 commit touches scoring: Merge pull request #183 from BaseIntelligence/fix/validator-public-we… |
| `sn44:scoring_commit:2026-08-20T09:49:53Z` | 44 | SCORING_COMMIT | 2026-08-20T10:16:11Z | sn44 commit touches scoring: update min challenge private |
| `sn92:scoring_commit:2026-08-20T10:11:04Z` | 92 | SCORING_COMMIT | 2026-08-20T10:16:11Z | sn92 commit touches scoring: Add the miner axon and document telemetry |
| `sn89:scoring_commit:2026-08-20T10:46:55Z` | 89 | SCORING_COMMIT | 2026-08-20T10:57:10Z | sn89 commit touches scoring: scripts/import_checkpoint.py: seed a validator journal from the publi… |
| `sn21:scoring_commit:2026-08-20T11:28:23Z` | 21 | SCORING_COMMIT | 2026-08-20T11:38:02Z | sn21 commit touches scoring: docs: point miners at rich training v2 and the expanded change types |
| `sn89:scoring_commit:2026-08-20T11:37:34Z` | 89 | SCORING_COMMIT | 2026-08-20T11:38:02Z | sn89 commit touches scoring: build_hf_scoreboard: HF status speaks the LF vocabulary |
| `sn28:release:v0.4.9-dev` | 28 | RELEASE | 2026-08-20T12:15:50Z | sn28 released v0.4.9-dev |
| `sn66:release:Payment and IAM update` | 66 | RELEASE | 2026-08-20T13:27:01Z | sn66 released Payment and IAM update |
| `sn10:scoring_commit:2026-08-20T12:49:41Z` | 10 | SCORING_COMMIT | 2026-08-20T14:10:38Z | sn10 commit touches scoring: feat(api): public read API for rounds, leader, and score progress |
| `sn28:release:v0.4.9` | 28 | RELEASE | 2026-08-20T14:10:38Z | sn28 released v0.4.9 |
| `sn89:scoring_commit:2026-08-20T13:41:37Z` | 89 | SCORING_COMMIT | 2026-08-20T14:10:38Z | sn89 commit touches scoring: README: a validator needs NO market-data key, and never needed a Taos… |
| `sn10:scoring_commit:2026-08-20T15:19:13Z` | 10 | SCORING_COMMIT | 2026-08-20T15:47:11Z | sn10 commit touches scoring: fix(worker): pass leaders.last_score to rank_round |
| `sn53:scoring_commit:2026-08-20T15:30:56Z` | 53 | SCORING_COMMIT | 2026-08-20T15:47:11Z | sn53 commit touches scoring: tee_miner: lift the 1 MiB websocket frame cap that 504s long-context … |
| `sn100:release:v3.3.27` | 100 | RELEASE | 2026-08-20T15:47:11Z | sn100 released v3.3.27 |
| `sn100:scoring_commit:2026-08-20T15:17:43Z` | 100 | SCORING_COMMIT | 2026-08-20T15:47:11Z | sn100 commit touches scoring: fix(design-challenge): drop crate_name so loc-cap is under 1500 |
| `sn21:scoring_commit:2026-08-20T15:58:11Z` | 21 | SCORING_COMMIT | 2026-08-20T16:17:45Z | sn21 commit touches scoring: docs: rich-era corrections in scoring architecture + whitepaper |
| `sn71:scoring_commit:2026-08-20T16:25:08Z` | 71 | SCORING_COMMIT | 2026-08-20T17:01:22Z | sn71 commit touches scoring: Bind local readiness verifier environment |
| `sn33:scoring_commit:2026-08-20T17:21:26Z` | 33 | SCORING_COMMIT | 2026-08-20T17:41:16Z | sn33 commit touches scoring: Merge pull request #136 from afterpartyai/Fix-Validator-timeout |
| `sn111:scoring_commit:2026-08-20T17:04:54Z` | 111 | SCORING_COMMIT | 2026-08-20T17:41:16Z | sn111 commit touches scoring: docs(validation): document resilient diagnostic batching |
| `sn71:scoring_commit:2026-08-20T18:02:42Z` | 71 | SCORING_COMMIT | 2026-08-20T18:15:10Z | sn71 commit touches scoring: Repair release verifier test isolation |
| `sn89:scoring_commit:2026-08-20T18:09:55Z` | 89 | SCORING_COMMIT | 2026-08-20T18:15:10Z | sn89 commit touches scoring: HF: apply owner-hosted miner integrity verdicts alongside the in-repo… |
| `sn18:release:Release 2.1.2` | 18 | RELEASE | 2026-08-20T19:55:22Z | sn18 released Release 2.1.2 |
| `sn25:release:v2026.8.20-1024555910` | 25 | RELEASE | 2026-08-20T20:41:45Z | sn25 released v2026.8.20-1024555910 |
| `sn13:release:Release v1.18.71` | 13 | RELEASE | 2026-08-20T21:13:04Z | sn13 released Release v1.18.71 |
| `sn13:scoring_commit:2026-08-13T06:08:42Z` | 13 | SCORING_COMMIT | 2026-08-20T21:13:04Z | sn13 commit touches scoring: fix(s3): stop charging miners for passing validation and for growing |
| `sn25:release:v2026.8.20-1024590520` | 25 | RELEASE | 2026-08-20T21:13:04Z | sn25 released v2026.8.20-1024590520 |
| `sn25:scoring_commit:2026-08-20T20:47:44Z` | 25 | SCORING_COMMIT | 2026-08-20T21:13:04Z | sn25 commit touches scoring: Fix miner Windows arm64 cross-build |
| `sn34:scoring_commit:2026-08-20T21:18:29Z` | 34 | SCORING_COMMIT | 2026-08-20T21:53:19Z | sn34 commit touches scoring: tune: double generator challenge frequency (#425) |
| `sn92:scoring_commit:2026-08-20T21:18:03Z` | 92 | SCORING_COMMIT | 2026-08-20T22:40:23Z | sn92 commit touches scoring: Drop the task generator in favour of uploaded corpora |
| `sn34:scoring_commit:2026-08-20T22:43:19Z` | 34 | SCORING_COMMIT | 2026-08-20T23:08:56Z | sn34 commit touches scoring: fix: restore validator config parsing (#427) |
| `sn91:scoring_commit:2026-08-20T23:02:51Z` | 91 | SCORING_COMMIT | 2026-08-20T23:08:56Z | sn91 commit touches scoring: Merge pull request #203 from TensorLink-AI/claude/miner-dethrone-bar |
| `sn34:release:Release 4.9.8` | 34 | RELEASE | 2026-08-21T01:54:45Z | sn34 released Release 4.9.8 |
| `sn53:scoring_commit:2026-08-21T04:53:19Z` | 53 | SCORING_COMMIT | 2026-08-21T05:04:00Z | sn53 commit touches scoring: tee_miner: absorb the reference miner's newer fixes |
| `sn67:scoring_commit:2026-08-21T03:07:16Z` | 67 | SCORING_COMMIT | 2026-08-21T05:46:36Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20260821.post1 |
| `sn100:release:v3.3.28` | 100 | RELEASE | 2026-08-21T07:23:29Z | sn100 released v3.3.28 |
| `sn100:scoring_commit:2026-08-21T06:46:39Z` | 100 | SCORING_COMMIT | 2026-08-21T07:23:29Z | sn100 commit touches scoring: feat(prism): miner Verda BYOK alongside Lium |
| `sn14:release:Fused-epilogue kernel submission archive` | 14 | RELEASE | 2026-08-21T09:49:58Z | sn14 released Fused-epilogue kernel submission archive (2026-08-21) |
| `sn67:scoring_commit:2026-08-21T10:10:17Z` | 67 | SCORING_COMMIT | 2026-08-21T10:43:26Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20260821.post3 |
| `sn25:release:v2026.8.21-1025093570` | 25 | RELEASE | 2026-08-21T11:11:10Z | sn25 released v2026.8.21-1025093570 |
| `sn25:release:v2026.8.21-1025114260` | 25 | RELEASE | 2026-08-21T11:52:03Z | sn25 released v2026.8.21-1025114260 |
| `sn21:scoring_commit:2026-08-21T12:29:40Z` | 21 | SCORING_COMMIT | 2026-08-21T13:07:23Z | sn21 commit touches scoring: feat(verify): mirror the daily verification feeds to the operator API… |
| `sn81:scoring_commit:2026-08-21T12:10:41Z` | 81 | SCORING_COMMIT | 2026-08-21T13:07:23Z | sn81 commit touches scoring: verify short (<CHALLENGE_K) completions at full coverage instead of h… |
| `sn92:scoring_commit:2026-08-21T11:56:26Z` | 92 | SCORING_COMMIT | 2026-08-21T13:07:23Z | sn92 commit touches scoring: Verify the gguf pin inline, since tests are not published |
| `sn108:scoring_commit:2026-08-21T13:03:07Z` | 108 | SCORING_COMMIT | 2026-08-21T13:07:23Z | sn108 commit touches scoring: docs(miner): eligibility now requires active members, not just regist… |
| `sn108:scoring_commit:2026-08-21T13:19:16Z` | 108 | SCORING_COMMIT | 2026-08-21T13:57:42Z | sn108 commit touches scoring: fix(evaluation): reuse the prefix cache the pinned transformers return |
| `sn1:release:v4.3.6` | 1 | RELEASE | 2026-08-21T14:50:15Z | sn1 released v4.3.6 |
| `sn25:release:v2026.8.21-1025223880` | 25 | RELEASE | 2026-08-21T14:50:15Z | sn25 released v2026.8.21-1025223880 |
| `sn21:scoring_commit:2026-08-21T16:09:09Z` | 21 | SCORING_COMMIT | 2026-08-21T16:15:59Z | sn21 commit touches scoring: docs: quickstart matches production — mirror for daily verification, … |
| `sn102:release:v0.5.0` | 102 | RELEASE | 2026-08-21T16:15:59Z | sn102 released v0.5.0 |
| `sn102:scoring_commit:2026-08-20T22:32:03Z` | 102 | SCORING_COMMIT | 2026-08-21T16:15:59Z | sn102 commit touches scoring: Merge pull request #223 from Connito-AI/feat/validator-observer-mode-v |
| `sn92:scoring_commit:2026-08-21T16:31:36Z` | 92 | SCORING_COMMIT | 2026-08-21T17:00:58Z | sn92 commit touches scoring: Turn provenance off until the run store can accept miner runs |
| `sn25:release:v2026.8.21-1025339670` | 25 | RELEASE | 2026-08-21T18:14:54Z | sn25 released v2026.8.21-1025339670 |
| `sn89:scoring_commit:2026-08-21T18:27:38Z` | 89 | SCORING_COMMIT | 2026-08-21T19:06:46Z | sn89 commit touches scoring: Scoring: build the qualified-win as-of window from RESOLVED outcomes |
| `sn92:release:v0.1.0` | 92 | RELEASE | 2026-08-21T19:06:46Z | sn92 released v0.1.0 |
| `sn92:scoring_commit:2026-08-21T18:54:26Z` | 92 | SCORING_COMMIT | 2026-08-21T19:06:46Z | sn92 commit touches scoring: Install the signer's keypair and verify the release the way a validat… |
| `sn90:release:v1.1.5` | 90 | RELEASE | 2026-08-21T22:02:40Z | sn90 released v1.1.5 |
| `sn90:scoring_commit:2026-08-21T22:02:06Z` | 90 | SCORING_COMMIT | 2026-08-21T22:02:40Z | sn90 commit touches scoring: fix(validator): fall back to CoinGecko TAO/USD when Taostats 429s |
| `sn15:scoring_commit:2026-08-21T23:12:08Z` | 15 | SCORING_COMMIT | 2026-08-21T23:35:34Z | sn15 commit touches scoring: chore: remove dead BackendClient top-miner and race-history methods (… |
| `sn97:scoring_commit:2026-08-21T17:21:07Z` | 97 | SCORING_COMMIT | 2026-08-22T00:02:04Z | sn97 commit touches scoring: feat: weighted reference-anchored scoring, split rubric, submit proto… |
| `sn25:release:v2026.8.21-1025613560` | 25 | RELEASE | 2026-08-22T01:47:37Z | sn25 released v2026.8.21-1025613560 |
| `sn53:scoring_commit:2026-08-22T01:50:29Z` | 53 | SCORING_COMMIT | 2026-08-22T02:43:43Z | sn53 commit touches scoring: fix(validator): reuse one chain connection instead of leaking one per… |
| `sn92:scoring_commit:2026-08-22T01:59:31Z` | 92 | SCORING_COMMIT | 2026-08-22T02:43:43Z | sn92 commit touches scoring: Sort the constants import in the validator context |
| `sn53:release:v0.4.5: Merge pull request #42 from hanl` | 53 | RELEASE | 2026-08-22T04:17:59Z | sn53 released v0.4.5: Merge pull request #42 from hanlinai/release/0.4.5 |
| `sn100:release:v3.3.29` | 100 | RELEASE | 2026-08-22T04:17:59Z | sn100 released v3.3.29 |
| `sn25:release:v2026.8.21-1025763520` | 25 | RELEASE | 2026-08-22T05:38:35Z | sn25 released v2026.8.21-1025763520 |
| `sn92:release:v0.1.1` | 92 | RELEASE | 2026-08-22T05:38:35Z | sn92 released v0.1.1 |
| `sn92:scoring_commit:2026-08-22T05:35:10Z` | 92 | SCORING_COMMIT | 2026-08-22T05:38:35Z | sn92 commit touches scoring: Package the version validators actually run |
| `sn67:readme_task_diff:5a8da0f3ba283771` | 67 | README_TASK_DIFF | 2026-08-15T09:06:33Z | sn67 README task/scoring sections changed |
| `sn123:readme_task_diff:6532d2da519e8960` | 123 | README_TASK_DIFF | 2026-08-17T17:55:33Z | sn123 README task/scoring sections changed |
| `sn91:readme_task_diff:465231d881190999` | 91 | README_TASK_DIFF | 2026-08-18T05:02:26Z | sn91 README task/scoring sections changed |
| `sn10:readme_task_diff:126d4086680182f3` | 10 | README_TASK_DIFF | 2026-08-18T12:04:33Z | sn10 README task/scoring sections changed |
| `sn108:readme_task_diff:19f7089d5cc9e961` | 108 | README_TASK_DIFF | 2026-08-18T13:55:30Z | sn108 README task/scoring sections changed |
| `sn33:readme_task_diff:a91e45ad8067f8f2` | 33 | README_TASK_DIFF | 2026-08-18T14:48:11Z | sn33 README task/scoring sections changed |
| `sn92:readme_task_diff:c2e913dd2e41d4bb` | 92 | README_TASK_DIFF | 2026-08-18T16:57:50Z | sn92 README task/scoring sections changed |
| `sn25:readme_task_diff:1a67cd5991549ed6` | 25 | README_TASK_DIFF | 2026-08-18T17:39:02Z | sn25 README task/scoring sections changed |
| `sn108:readme_task_diff:440d4dcceb14f6b4` | 108 | README_TASK_DIFF | 2026-08-18T17:39:02Z | sn108 README task/scoring sections changed |
| `sn108:readme_task_diff:fa8dc13fe8c76401` | 108 | README_TASK_DIFF | 2026-08-18T19:07:17Z | sn108 README task/scoring sections changed |
| `sn28:readme_task_diff:bea04ee7e3aadb3b` | 28 | README_TASK_DIFF | 2026-08-18T22:37:17Z | sn28 README task/scoring sections changed |
| `sn10:readme_task_diff:2e15c71289199f4e` | 10 | README_TASK_DIFF | 2026-08-19T18:50:48Z | sn10 README task/scoring sections changed |
| `sn90:readme_task_diff:320a058a7749d0fe` | 90 | README_TASK_DIFF | 2026-08-19T18:50:48Z | sn90 README task/scoring sections changed |
| `sn66:readme_task_diff:6d03fe25d3e98c8c` | 66 | README_TASK_DIFF | 2026-08-19T20:02:56Z | sn66 README task/scoring sections changed |
| `sn89:readme_task_diff:af753e3216a79781` | 89 | README_TASK_DIFF | 2026-08-19T20:41:24Z | sn89 README task/scoring sections changed |
| `sn7:readme_task_diff:9594fdc9163bdf75` | 7 | README_TASK_DIFF | 2026-08-19T21:50:36Z | sn7 README task/scoring sections changed |
| `sn26:readme_task_diff:138b96d6c81dee36` | 26 | README_TASK_DIFF | 2026-08-20T01:53:55Z | sn26 README task/scoring sections changed |
| `sn92:readme_task_diff:927a737990a07446` | 92 | README_TASK_DIFF | 2026-08-20T05:42:25Z | sn92 README task/scoring sections changed |
| `sn67:readme_task_diff:f4fc3f2cce58d57d` | 67 | README_TASK_DIFF | 2026-08-20T09:47:27Z | sn67 README task/scoring sections changed |
| `sn25:readme_task_diff:c457ae49d232190d` | 25 | README_TASK_DIFF | 2026-08-20T17:41:16Z | sn25 README task/scoring sections changed |
| `sn21:readme_task_diff:24af354b63ad7d31` | 21 | README_TASK_DIFF | 2026-08-21T16:15:59Z | sn21 README task/scoring sections changed |
| `sn90:readme_task_diff:1adff40174e46f0e` | 90 | README_TASK_DIFF | 2026-08-21T19:06:46Z | sn90 README task/scoring sections changed |

## RESOLVED IN THIS WINDOW

_none_
