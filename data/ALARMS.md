# ALARMS - generated 2026-10-29T00:17:57Z, block 9385791

window: first_seen in [2026-10-28T23:03:27Z, 2026-10-29T00:18:27Z)  (60 min interval + 15 min overlap)

Report ONLY the rows under NEW SINCE LAST RUN. Rows under STILL OPEN were
already reported in an earlier window and must not be re-alarmed.

## NEW SINCE LAST RUN

| event_id | netuid | class | severity | first_seen_utc | one_line |
|---|---|---|---|---|---|
| `sn66:release:v2026.10.28.3` | 66 | RELEASE | P1 | 2026-10-29T00:18:27Z | sn66 released v2026.10.28.3 |
| `sn71:scoring_commit:2026-10-28T22:42:44Z` | 71 | SCORING_COMMIT | P1 | 2026-10-29T00:18:27Z | sn71 commit touches scoring: Allow scored Arena publication during automatic restart drain |
| `sn78:scoring_commit:2026-10-28T23:35:18Z` | 78 | SCORING_COMMIT | P1 | 2026-10-29T00:18:27Z | sn78 commit touches scoring: Keep reserved participation fair and reuse verified cohort history |

### detail

- **`sn66:release:v2026.10.28.3`** - sn66 released v2026.10.28.3
  - published 2026-10-28T20:31:47Z (was v2026.10.28.2)
- **`sn71:scoring_commit:2026-10-28T22:42:44Z`** - sn71 commit touches scoring: Allow scored Arena publication during automatic restart drain
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn78:scoring_commit:2026-10-28T23:35:18Z`** - sn78 commit touches scoring: Keep reserved participation fair and reuse verified cohort history
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.

## STILL OPEN (already reported - do not re-alarm)

| event_id | netuid | class | first_seen_utc | one_line |
|---|---|---|---|---|
| `sn7:burn_drop:0.986` | 7 | BURN_DROP | 2026-10-22T21:32:31Z | sn7 burn fell 0.990 -> 0.986 - miners can earn again |
| `sn81:burn_drop:0.810` | 81 | BURN_DROP | 2026-10-23T00:12:40Z | sn81 burn fell 0.996 -> 0.810 - miners can earn again |
| `sn104:burn_drop:0.000` | 104 | BURN_DROP | 2026-10-23T05:10:24Z | sn104 burn fell 1.000 -> 0.000 - miners can earn again |
| `sn6:weights_version_bump:4000` | 6 | WEIGHTS_VERSION_BUMP | 2026-10-23T15:20:36Z | sn6 weights_version 3000 -> 4000 |
| `sn7:burn_drop:0.985` | 7 | BURN_DROP | 2026-10-23T22:32:24Z | sn7 burn fell 0.991 -> 0.985 - miners can earn again |
| `sn76:burn_drop:0.987` | 76 | BURN_DROP | 2026-10-23T22:32:24Z | sn76 burn fell 0.992 -> 0.987 - miners can earn again |
| `sn117:burn_drop:0.926` | 117 | BURN_DROP | 2026-10-24T19:51:23Z | sn117 burn fell 1.000 -> 0.926 - miners can earn again |
| `sn76:burn_drop:0.982` | 76 | BURN_DROP | 2026-10-25T05:23:07Z | sn76 burn fell 1.000 -> 0.982 - miners can earn again |
| `sn76:burn_drop:0.965` | 76 | BURN_DROP | 2026-10-25T20:01:41Z | sn76 burn fell 1.000 -> 0.965 - miners can earn again |
| `sn117:burn_drop:0.955` | 117 | BURN_DROP | 2026-10-25T22:30:52Z | sn117 burn fell 1.000 -> 0.955 - miners can earn again |
| `sn76:burn_drop:0.978` | 76 | BURN_DROP | 2026-10-27T01:27:07Z | sn76 burn fell 0.998 -> 0.978 - miners can earn again |
| `sn73:burn_drop:0.000` | 73 | BURN_DROP | 2026-10-27T06:46:43Z | sn73 burn fell 1.000 -> 0.000 - miners can earn again |
| `sn32:burn_drop:0.000` | 32 | BURN_DROP | 2026-10-28T20:27:26Z | sn32 burn fell 1.000 -> 0.000 - miners can earn again |
| `sn117:burn_drop:0.982` | 117 | BURN_DROP | 2026-10-28T20:27:26Z | sn117 burn fell 1.000 -> 0.982 - miners can earn again |
| `sn2:scoring_commit:2026-10-22T01:50:24Z` | 2 | SCORING_COMMIT | 2026-10-22T01:57:11Z | sn2 commit touches scoring: Add finalized-chain observer for validator pilot |
| `sn25:release:v2026.10.21-1078274420` | 25 | RELEASE | 2026-10-22T01:57:11Z | sn25 released v2026.10.21-1078274420 |
| `sn117:release:everycli v0.7.0` | 117 | RELEASE | 2026-10-22T01:57:11Z | sn117 released everycli v0.7.0 |
| `sn117:scoring_commit:2026-10-21T23:16:35Z` | 117 | SCORING_COMMIT | 2026-10-22T01:57:11Z | sn117 commit touches scoring: test: record final v0.6.3 offline updater Phala validation |
| `sn28:release:v0.5.8` | 28 | RELEASE | 2026-10-22T07:29:56Z | sn28 released v0.5.8 |
| `sn28:scoring_commit:2026-10-22T06:29:41Z` | 28 | SCORING_COMMIT | 2026-10-22T07:29:56Z | sn28 commit touches scoring: chore(release): gm-miner 0.5.8 (#343) |
| `sn51:scoring_commit:2026-10-22T07:26:30Z` | 51 | SCORING_COMMIT | 2026-10-22T07:29:56Z | sn51 commit touches scoring: DAH-4954 - [P0] Validator: revert the always-on GPU identity enforcem… |
| `sn67:scoring_commit:2026-10-22T06:46:09Z` | 67 | SCORING_COMMIT | 2026-10-22T07:29:56Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20261022.post1 |
| `sn71:scoring_commit:2026-10-22T07:15:03Z` | 71 | SCORING_COMMIT | 2026-10-22T07:29:56Z | sn71 commit touches scoring: Validate Arena round IDs before store filters |
| `sn81:scoring_commit:2026-10-22T02:19:36Z` | 81 | SCORING_COMMIT | 2026-10-22T07:29:56Z | sn81 commit touches scoring: Merge pull request #383 from reliquadotai/fix/validator-application-on |
| `sn15:scoring_commit:2026-10-22T08:44:01Z` | 15 | SCORING_COMMIT | 2026-10-22T13:13:57Z | sn15 commit touches scoring: Validator v3: world packs on oro-env-runtime 4.0.1, a thin world sear… |
| `sn22:scoring_commit:2026-10-22T09:25:54Z` | 22 | SCORING_COMMIT | 2026-10-22T13:13:57Z | sn22 commit touches scoring: fix(validators): a pinned read refused after its task closed is a mis… |
| `sn25:scoring_commit:2026-10-22T08:30:09Z` | 25 | SCORING_COMMIT | 2026-10-22T13:13:57Z | sn25 commit touches scoring: Merge pull request #15 from Ryanmello07/miner/windows-service |
| `sn51:scoring_commit:2026-10-22T11:56:35Z` | 51 | SCORING_COMMIT | 2026-10-22T13:13:57Z | sn51 commit touches scoring: DAH-4817 - [P2] Validator: fresh-node grace, VerifyX EMA hold and reg… |
| `sn56:scoring_commit:2026-10-22T09:05:28Z` | 56 | SCORING_COMMIT | 2026-10-22T13:13:57Z | sn56 commit touches scoring: Fix FP8 LoRA evaluation and Flux cache artifacts (#1403) |
| `sn67:scoring_commit:2026-10-22T10:47:28Z` | 67 | SCORING_COMMIT | 2026-10-22T13:13:57Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20261022.post5 |
| `sn92:release:v1.2.0-rc11` | 92 | RELEASE | 2026-10-22T13:13:57Z | sn92 released v1.2.0-rc11 |
| `sn1:release:v4.4.15` | 1 | RELEASE | 2026-10-22T18:06:27Z | sn1 released v4.4.15 |
| `sn12:release:miner-staging-2026-10-22-39790980356-423` | 12 | RELEASE | 2026-10-22T18:06:27Z | sn12 released miner-staging-2026-10-22-39790980356-423-1: fix: security fixes |
| `sn15:release:v3.0.0` | 15 | RELEASE | 2026-10-22T18:06:27Z | sn15 released v3.0.0 |
| `sn21:scoring_commit:2026-10-22T10:49:09Z` | 21 | SCORING_COMMIT | 2026-10-22T18:06:27Z | sn21 commit touches scoring: fix(scoring): the outcomes reader keeps expected and actual conversio… |
| `sn25:release:v2026.10.22-1078873780` | 25 | RELEASE | 2026-10-22T18:06:27Z | sn25 released v2026.10.22-1078873780 |
| `sn51:release:executor-v1.151` | 51 | RELEASE | 2026-10-22T18:06:27Z | sn51 released executor-v1.151 |
| `sn51:scoring_commit:2026-10-22T15:42:26Z` | 51 | SCORING_COMMIT | 2026-10-22T18:06:27Z | sn51 commit touches scoring: DAH-4983 - Validator: a failed edit's undo repairs a stale volume mou… |
| `sn76:release:v0.0.3` | 76 | RELEASE | 2026-10-22T18:06:27Z | sn76 released v0.0.3 |
| `sn76:scoring_commit:2026-10-22T14:48:07Z` | 76 | SCORING_COMMIT | 2026-10-22T18:06:27Z | sn76 commit touches scoring: Allow manual CI verification after repository recovery (#15) |
| `sn81:scoring_commit:2026-10-22T14:26:47Z` | 81 | SCORING_COMMIT | 2026-10-22T18:06:27Z | sn81 commit touches scoring: Merge pull request #387: evaluation feed destination safeguards |
| `sn117:release:everycli v0.7.1` | 117 | RELEASE | 2026-10-22T18:06:27Z | sn117 released everycli v0.7.1 |
| `sn13:release:Release v1.18.75` | 13 | RELEASE | 2026-10-22T21:32:31Z | sn13 released Release v1.18.75 |
| `sn66:release:v2026.10.22.2` | 66 | RELEASE | 2026-10-22T21:32:31Z | sn66 released v2026.10.22.2 |
| `sn71:scoring_commit:2026-10-22T18:59:12Z` | 71 | SCORING_COMMIT | 2026-10-22T21:32:31Z | sn71 commit touches scoring: Merge pull request #705 from leadpoet/fix/validator-installed-interpr… |
| `sn28:release:v0.5.10-dev` | 28 | RELEASE | 2026-10-23T00:12:40Z | sn28 released v0.5.10-dev |
| `sn28:scoring_commit:2026-10-22T23:53:16Z` | 28 | SCORING_COMMIT | 2026-10-23T00:12:40Z | sn28 commit touches scoring: chore(release): gm-miner 0.5.10-dev (#347) |
| `sn15:release:v3.0.2: security: patch Python dependenc` | 15 | RELEASE | 2026-10-23T05:10:24Z | sn15 released v3.0.2: security: patch Python dependencies and supported runtimes (#388) |
| `sn21:release:SN21 training data v5 (rules from 30 Oct` | 21 | RELEASE | 2026-10-23T05:10:24Z | sn21 released SN21 training data v5 (rules from 30 Oct 2026) |
| `sn28:release:v0.5.10` | 28 | RELEASE | 2026-10-23T05:10:24Z | sn28 released v0.5.10 |
| `sn28:scoring_commit:2026-10-23T01:00:34Z` | 28 | SCORING_COMMIT | 2026-10-23T05:10:24Z | sn28 commit touches scoring: chore(release): gm-miner 0.5.10 (#348) |
| `sn51:release:executor-v1.152` | 51 | RELEASE | 2026-10-23T05:10:24Z | sn51 released executor-v1.152 |
| `sn51:scoring_commit:2026-10-23T04:54:13Z` | 51 | SCORING_COMMIT | 2026-10-23T05:10:24Z | sn51 commit touches scoring: DAH-5012 - [P0] Validator: a killed filler still exiting no longer fa… |
| `sn71:scoring_commit:2026-10-23T02:21:04Z` | 71 | SCORING_COMMIT | 2026-10-23T05:10:24Z | sn71 commit touches scoring: Carry verified numeric LinkedIn identity into investigator evidence (… |
| `sn78:scoring_commit:2026-10-23T01:53:59Z` | 78 | SCORING_COMMIT | 2026-10-23T05:10:24Z | sn78 commit touches scoring: Handle runtime483 reward eligibility and preserve recovery checks (#35 |
| `sn81:scoring_commit:2026-10-23T02:34:18Z` | 81 | SCORING_COMMIT | 2026-10-23T05:10:24Z | sn81 commit touches scoring: Merge pull request #393 from reliquadotai/fix/rl-reward-error |
| `sn123:scoring_commit:2026-10-23T03:36:50Z` | 123 | SCORING_COMMIT | 2026-10-23T05:10:24Z | sn123 commit touches scoring: Update validator.py |
| `sn12:release:miner-staging-2026-10-23-39921557432-424` | 12 | RELEASE | 2026-10-23T10:21:57Z | sn12 released miner-staging-2026-10-23-39921557432-424-1: fix: eMudhra certificates incident immunization |
| `sn28:release:v0.5.11-dev` | 28 | RELEASE | 2026-10-23T10:21:57Z | sn28 released v0.5.11-dev |
| `sn28:scoring_commit:2026-10-23T09:46:31Z` | 28 | SCORING_COMMIT | 2026-10-23T10:21:57Z | sn28 commit touches scoring: chore(release): gm-miner 0.5.11-dev (#350) |
| `sn46:release:Merge pull request #10 from Subnet46/rel` | 46 | RELEASE | 2026-10-23T10:21:57Z | sn46 released Merge pull request #10 from Subnet46/release/v0.1.4 |
| `sn51:scoring_commit:2026-10-23T07:55:50Z` | 51 | SCORING_COMMIT | 2026-10-23T10:21:57Z | sn51 commit touches scoring: miner run.sh: retry the database migration while Postgres is starting… |
| `sn67:scoring_commit:2026-10-23T07:34:32Z` | 67 | SCORING_COMMIT | 2026-10-23T10:21:57Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20261023.post3 |
| `sn78:scoring_commit:2026-10-23T10:05:58Z` | 78 | SCORING_COMMIT | 2026-10-23T10:21:57Z | sn78 commit touches scoring: Reuse verified model references in legacy retry reconciliation (#355) |
| `sn114:scoring_commit:2026-10-23T09:03:37Z` | 114 | SCORING_COMMIT | 2026-10-23T10:21:57Z | sn114 commit touches scoring: Merge pull request #230 from DendriteHQ/miner-logs-enpoint |
| `sn28:release:v0.5.11` | 28 | RELEASE | 2026-10-23T15:20:36Z | sn28 released v0.5.11 |
| `sn28:scoring_commit:2026-10-23T11:46:00Z` | 28 | SCORING_COMMIT | 2026-10-23T15:20:36Z | sn28 commit touches scoring: chore(release): gm-miner 0.5.11 (#351) |
| `sn46:release:v0.1.4` | 46 | RELEASE | 2026-10-23T15:20:36Z | sn46 released v0.1.4 |
| `sn51:release:lium-protocol-v1.16.0` | 51 | RELEASE | 2026-10-23T15:20:36Z | sn51 released lium-protocol-v1.16.0 |
| `sn51:scoring_commit:2026-10-23T14:38:12Z` | 51 | SCORING_COMMIT | 2026-10-23T15:20:36Z | sn51 commit touches scoring: DAH-3476 - [P0] libdmcompverify.so: add sm_75 kernel so Tesla T4 pass… |
| `sn56:scoring_commit:2026-10-23T13:35:41Z` | 56 | SCORING_COMMIT | 2026-10-23T15:20:36Z | sn56 commit touches scoring: Sunset environment tournaments and evaluation runtime (#1397) |
| `sn66:release:v2026.10.23` | 66 | RELEASE | 2026-10-23T15:20:36Z | sn66 released v2026.10.23 |
| `sn71:scoring_commit:2026-10-23T12:24:04Z` | 71 | SCORING_COMMIT | 2026-10-23T15:20:36Z | sn71 commit touches scoring: Merge pull request #718 from leadpoet/fix/oct23-unvalidated-tool-repl… |
| `sn78:scoring_commit:2026-10-23T12:32:14Z` | 78 | SCORING_COMMIT | 2026-10-23T15:20:36Z | sn78 commit touches scoring: Discover proved reward runtimes automatically across upgrades (#358) |
| `sn89:scoring_commit:2026-10-23T13:43:17Z` | 89 | SCORING_COMMIT | 2026-10-23T15:20:36Z | sn89 commit touches scoring: Keep-alive floor for fresh and active miners from 2026-10-23 16:00 UTC |
| `sn92:scoring_commit:2026-10-23T11:35:56Z` | 92 | SCORING_COMMIT | 2026-10-23T15:20:36Z | sn92 commit touches scoring: eval v5.1: public format doc, reference scorer and 300-item dev set (… |
| `sn97:scoring_commit:2026-10-23T11:04:36Z` | 97 | SCORING_COMMIT | 2026-10-23T15:20:36Z | sn97 commit touches scoring: feat(eval): fetch the challenger claimed ahead while the current eval… |
| `sn117:release:everycli v0.7.2` | 117 | RELEASE | 2026-10-23T15:20:36Z | sn117 released everycli v0.7.2 |
| `sn117:scoring_commit:2026-10-23T10:11:21Z` | 117 | SCORING_COMMIT | 2026-10-23T15:20:36Z | sn117 commit touches scoring: docs: record bootstrap artifacts and live validation gates |
| `sn8:scoring_commit:2026-10-23T16:19:53Z` | 8 | SCORING_COMMIT | 2026-10-23T19:26:12Z | sn8 commit touches scoring: Optimizations for miner statistics (#964) |
| `sn21:scoring_commit:2026-10-23T07:40:31Z` | 21 | SCORING_COMMIT | 2026-10-23T19:26:12Z | sn21 commit touches scoring: fix(scoring): only real scored entries count toward the previous-mode… |
| `sn22:scoring_commit:2026-10-23T11:12:15Z` | 22 | SCORING_COMMIT | 2026-10-23T19:26:12Z | sn22 commit touches scoring: fix(bot): open a fresh connection for each task API request again, so… |
| `sn66:release:v2026.10.23.2` | 66 | RELEASE | 2026-10-23T19:26:12Z | sn66 released v2026.10.23.2 |
| `sn71:scoring_commit:2026-10-23T19:17:11Z` | 71 | SCORING_COMMIT | 2026-10-23T19:26:12Z | sn71 commit touches scoring: Bind company-evidence release to reviewed scorer source |
| `sn120:scoring_commit:2026-10-23T19:17:25Z` | 120 | SCORING_COMMIT | 2026-10-23T19:26:12Z | sn120 commit touches scoring: Flip-incentive SHADOW docs + audit helper (LIVE still v9/seq7) (#88) |
| `sn71:scoring_commit:2026-10-23T20:43:00Z` | 71 | SCORING_COMMIT | 2026-10-23T22:32:24Z | sn71 commit touches scoring: Preserve the failed primary-intent reason when a bonus verifies |
| `sn78:scoring_commit:2026-10-23T21:58:21Z` | 78 | SCORING_COMMIT | 2026-10-23T22:32:24Z | sn78 commit touches scoring: Retain bounded model pairs and finish resident evaluation jobs |
| `sn117:release:everycli v0.7.3` | 117 | RELEASE | 2026-10-23T22:32:24Z | sn117 released everycli v0.7.3 |
| `sn71:scoring_commit:2026-10-24T01:08:52Z` | 71 | SCORING_COMMIT | 2026-10-24T01:10:35Z | sn71 commit touches scoring: Bind headcount release to committed protected scorer source |
| `sn78:scoring_commit:2026-10-23T23:09:56Z` | 78 | SCORING_COMMIT | 2026-10-24T01:10:35Z | sn78 commit touches scoring: Keep central model evaluations out of automatic miner absence cutoff |
| `sn117:release:everycli v0.7.4` | 117 | RELEASE | 2026-10-24T01:10:35Z | sn117 released everycli v0.7.4 |
| `sn2:scoring_commit:2026-10-24T01:34:32Z` | 2 | SCORING_COMMIT | 2026-10-24T06:11:04Z | sn2 commit touches scoring: Document localnet validator operation and production boundary |
| `sn62:release:v0.3.12` | 62 | RELEASE | 2026-10-24T06:11:04Z | sn62 released v0.3.12 |
| `sn71:scoring_commit:2026-10-24T04:51:31Z` | 71 | SCORING_COMMIT | 2026-10-24T06:11:04Z | sn71 commit touches scoring: Keep degraded proxy events clear of scoring readiness |
| `sn78:scoring_commit:2026-10-24T03:49:11Z` | 78 | SCORING_COMMIT | 2026-10-24T06:11:04Z | sn78 commit touches scoring: Merge pull request #378 from Umi-BitSign/fix/assignment-verification-… |
| `sn21:scoring_commit:2026-10-24T06:28:19Z` | 21 | SCORING_COMMIT | 2026-10-24T11:23:46Z | sn21 commit touches scoring: docs(scoring): the measurement amendment applies by basket, from the … |
| `sn62:release:v0.3.13` | 62 | RELEASE | 2026-10-24T11:23:46Z | sn62 released v0.3.13 |
| `sn81:scoring_commit:2026-10-24T10:32:01Z` | 81 | SCORING_COMMIT | 2026-10-24T11:23:46Z | sn81 commit touches scoring: fix(rl-price): level mode moves per hour, slower than the miners |
| `sn81:scoring_commit:2026-10-24T11:36:09Z` | 81 | SCORING_COMMIT | 2026-10-24T14:45:03Z | sn81 commit touches scoring: Merge pull request #413 from reliquadotai/fix/rl-active-miner-live-lea |
| `sn71:scoring_commit:2026-10-24T17:11:03Z` | 71 | SCORING_COMMIT | 2026-10-24T17:39:36Z | sn71 commit touches scoring: Preserve source metadata and validated company evidence in Arena judgi |
| `sn78:scoring_commit:2026-10-24T14:56:17Z` | 78 | SCORING_COMMIT | 2026-10-24T17:39:36Z | sn78 commit touches scoring: Reset evaluation forecasts when evaluator processes change (#386) |
| `sn78:scoring_commit:2026-10-24T18:32:39Z` | 78 | SCORING_COMMIT | 2026-10-24T19:51:23Z | sn78 commit touches scoring: Keep threshold shape validation on failed multisig calls |
| `sn81:scoring_commit:2026-10-24T17:47:45Z` | 81 | SCORING_COMMIT | 2026-10-24T19:51:23Z | sn81 commit touches scoring: Merge pull request #416 from reliquadotai/fix/rl-miner-submission-expo |
| `sn25:release:v2026.10.24-1080739690` | 25 | RELEASE | 2026-10-24T22:26:21Z | sn25 released v2026.10.24-1080739690 |
| `sn15:release:v3.0.3: feat: capture BYOK upstream infe` | 15 | RELEASE | 2026-10-25T00:29:02Z | sn15 released v3.0.3: feat: capture BYOK upstream inference cost per call (#391) |
| `sn15:scoring_commit:2026-10-24T23:44:40Z` | 15 | SCORING_COMMIT | 2026-10-25T00:29:02Z | sn15 commit touches scoring: chore: remove dead _upload_logs method from validator (#390) |
| `sn78:scoring_commit:2026-10-25T00:12:57Z` | 78 | SCORING_COMMIT | 2026-10-25T00:29:02Z | sn78 commit touches scoring: Publish compatible model-only cohort readers to miner clients |
| `sn15:release:v3.0.4: fix: gate BYOK cost fields on us` | 15 | RELEASE | 2026-10-25T05:23:07Z | sn15 released v3.0.4: fix: gate BYOK cost fields on usage.is_byok (#392) |
| `sn25:release:v2026.10.24-1080878340` | 25 | RELEASE | 2026-10-25T05:23:07Z | sn25 released v2026.10.24-1080878340 |
| `sn81:scoring_commit:2026-10-25T03:19:05Z` | 81 | SCORING_COMMIT | 2026-10-25T05:23:07Z | sn81 commit touches scoring: Merge pull request #417 from reliquadotai/fix/no-min-incentive-floor |
| `sn71:scoring_commit:2026-10-25T07:57:10Z` | 71 | SCORING_COMMIT | 2026-10-25T10:00:10Z | sn71 commit touches scoring: Allow miner execution alongside baseline judging |
| `sn51:scoring_commit:2026-10-25T12:39:04Z` | 51 | SCORING_COMMIT | 2026-10-25T14:20:01Z | sn51 commit touches scoring: DAH-5061 - [P1] Validator: re-anchor an idle node whose whole GPU set… |
| `sn71:scoring_commit:2026-10-25T10:32:22Z` | 71 | SCORING_COMMIT | 2026-10-25T14:20:01Z | sn71 commit touches scoring: Materialize eligible closed score runs before uncertain calls |
| `sn97:scoring_commit:2026-10-25T13:32:48Z` | 97 | SCORING_COMMIT | 2026-10-25T14:20:01Z | sn97 commit touches scoring: feat(eval): score agent turns mid-trajectory, higher swe and terminal… |
| `sn78:scoring_commit:2026-10-25T17:59:54Z` | 78 | SCORING_COMMIT | 2026-10-25T20:01:41Z | sn78 commit touches scoring: Merge pull request #412 from Umi-BitSign/fix/legacy-original-verifica… |
| `sn78:scoring_commit:2026-10-25T22:24:39Z` | 78 | SCORING_COMMIT | 2026-10-25T22:30:52Z | sn78 commit touches scoring: Reuse native request closure verification through publication and rev… |
| `sn25:release:v2026.10.25-1081686250` | 25 | RELEASE | 2026-10-26T00:45:22Z | sn25 released v2026.10.25-1081686250 |
| `sn25:scoring_commit:2026-10-25T23:59:22Z` | 25 | SCORING_COMMIT | 2026-10-26T00:45:22Z | sn25 commit touches scoring: Project the verified retained predecessor for native gap recovery |
| `sn71:scoring_commit:2026-10-25T21:47:33Z` | 71 | SCORING_COMMIT | 2026-10-26T00:45:22Z | sn71 commit touches scoring: Record final live verification of all twenty-five provider routes |
| `sn78:scoring_commit:2026-10-25T22:48:12Z` | 78 | SCORING_COMMIT | 2026-10-26T00:45:22Z | sn78 commit touches scoring: Score failed paired model candidates without invalidating the incumbe… |
| `sn51:scoring_commit:2026-10-26T03:35:42Z` | 51 | SCORING_COMMIT | 2026-10-26T05:27:56Z | sn51 commit touches scoring: DAH-4568 - [P1] Remove the GPU alias flag: one miner's shared GPU sco… |
| `sn71:scoring_commit:2026-10-26T02:30:24Z` | 71 | SCORING_COMMIT | 2026-10-26T05:27:56Z | sn71 commit touches scoring: Classify verified provider output failures within capture coverage |
| `sn78:scoring_commit:2026-10-26T03:27:58Z` | 78 | SCORING_COMMIT | 2026-10-26T05:27:56Z | sn78 commit touches scoring: Expose native checkpoint metadata progress in reward service logs (#42 |
| `sn9:release:v4.13.9` | 9 | RELEASE | 2026-10-26T11:28:34Z | sn9 released v4.13.9 |
| `sn22:scoring_commit:2026-10-26T09:06:22Z` | 22 | SCORING_COMMIT | 2026-10-26T11:28:34Z | sn22 commit touches scoring: chore(validators): one upload schema and no v1 check or reason; a fil… |
| `sn51:release:executor-v1.155` | 51 | RELEASE | 2026-10-26T11:28:34Z | sn51 released executor-v1.155 |
| `sn51:scoring_commit:2026-10-26T11:08:28Z` | 51 | SCORING_COMMIT | 2026-10-26T11:28:34Z | sn51 commit touches scoring: DAH-5075 - [P0] Central miner: retry an executor's SSH-key upload so … |
| `sn67:scoring_commit:2026-10-26T05:55:47Z` | 67 | SCORING_COMMIT | 2026-10-26T11:28:34Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20261026.post2 |
| `sn71:scoring_commit:2026-10-26T11:18:07Z` | 71 | SCORING_COMMIT | 2026-10-26T11:28:34Z | sn71 commit touches scoring: Merge pull request #794 from leadpoet/fix/recovered-score-credential-… |
| `sn78:scoring_commit:2026-10-26T09:41:35Z` | 78 | SCORING_COMMIT | 2026-10-26T11:28:34Z | sn78 commit touches scoring: Bound native HD suite decode threads within verifier memory |
| `sn81:scoring_commit:2026-10-25T15:22:13Z` | 81 | SCORING_COMMIT | 2026-10-26T11:28:34Z | sn81 commit touches scoring: feat(validator): name every declared card model |
| `sn92:release:v1.2.0-rc11.post7` | 92 | RELEASE | 2026-10-26T11:28:34Z | sn92 released v1.2.0-rc11.post7 |
| `sn123:scoring_commit:2026-10-26T06:24:32Z` | 123 | SCORING_COMMIT | 2026-10-26T11:28:34Z | sn123 commit touches scoring: Update validator.py |
| `sn12:release:validator-staging-2026-10-26-40344021717` | 12 | RELEASE | 2026-10-26T17:40:02Z | sn12 released validator-staging-2026-10-26-40344021717-627-1: fix: eMudhra ca incident immunization - internal deps |
| `sn12:scoring_commit:2026-10-26T16:19:50Z` | 12 | SCORING_COMMIT | 2026-10-26T17:40:02Z | sn12 commit touches scoring: fix(validator): fix prometheus image |
| `sn51:release:miner-v1.010` | 51 | RELEASE | 2026-10-26T17:40:02Z | sn51 released miner-v1.010 |
| `sn51:scoring_commit:2026-10-26T16:46:20Z` | 51 | SCORING_COMMIT | 2026-10-26T17:40:02Z | sn51 commit touches scoring: DAH-5187 - [P1] Validator: re-probe missed ports once before failing … |
| `sn60:scoring_commit:2026-10-26T15:27:49Z` | 60 | SCORING_COMMIT | 2026-10-26T17:40:02Z | sn60 commit touches scoring: changed scorer model to DeepSeek-V3.2 |
| `sn71:scoring_commit:2026-10-26T12:29:53Z` | 71 | SCORING_COMMIT | 2026-10-26T17:40:02Z | sn71 commit touches scoring: Merge pull request #796 from leadpoet/fix/close-scoring-covered-credi… |
| `sn75:release:Runtime 92023 rc2 (srtool, 873384f)` | 75 | RELEASE | 2026-10-26T17:40:02Z | sn75 released Runtime 92023 rc2 (srtool, 873384f) |
| `sn78:scoring_commit:2026-10-26T15:21:01Z` | 78 | SCORING_COMMIT | 2026-10-26T17:40:02Z | sn78 commit touches scoring: Enforce broader C7+ evaluation suites (#441) |
| `sn97:scoring_commit:2026-10-26T16:35:25Z` | 97 | SCORING_COMMIT | 2026-10-26T17:40:02Z | sn97 commit touches scoring: fix(web): display NaN scores properly |
| `sn2:scoring_commit:2026-10-26T19:40:08Z` | 2 | SCORING_COMMIT | 2026-10-26T21:56:01Z | sn2 commit touches scoring: Document live Finney burn validator status |
| `sn28:release:v0.5.12` | 28 | RELEASE | 2026-10-26T21:56:01Z | sn28 released v0.5.12 |
| `sn28:scoring_commit:2026-10-24T09:19:08Z` | 28 | SCORING_COMMIT | 2026-10-26T21:56:01Z | sn28 commit touches scoring: attestd: fix the kubetee.attestation.v1 binding verification (gm-veri… |
| `sn51:scoring_commit:2026-10-26T17:40:00Z` | 51 | SCORING_COMMIT | 2026-10-26T21:56:01Z | sn51 commit touches scoring: DAH-4972 - [P1] Validator fails nodes without pid: host (#1806) |
| `sn123:scoring_commit:2026-10-26T19:14:29Z` | 123 | SCORING_COMMIT | 2026-10-26T21:56:01Z | sn123 commit touches scoring: Update validator.py |
| `sn71:scoring_commit:2026-10-27T00:51:51Z` | 71 | SCORING_COMMIT | 2026-10-27T01:27:07Z | sn71 commit touches scoring: Record the authorized evidence-verification release scope |
| `sn94:scoring_commit:2026-10-26T23:13:36Z` | 94 | SCORING_COMMIT | 2026-10-27T01:27:07Z | sn94 commit touches scoring: Accept a list of AMD ARK pins in the broker verifier config |
| `sn2:scoring_commit:2026-10-27T04:19:07Z` | 2 | SCORING_COMMIT | 2026-10-27T06:46:43Z | sn2 commit touches scoring: Score finalized epoch snapshots and log unsigned weight previews |
| `sn15:release:v3.0.5: fix(validator): policy_view.max_` | 15 | RELEASE | 2026-10-27T06:46:43Z | sn15 released v3.0.5: fix(validator): policy_view.max_steps is the task's own step limit |
| `sn15:scoring_commit:2026-10-27T04:52:29Z` | 15 | SCORING_COMMIT | 2026-10-27T06:46:43Z | sn15 commit touches scoring: fix(validator): policy_view.max_steps is the task's own step limit |
| `sn76:scoring_commit:2026-10-27T02:34:08Z` | 76 | SCORING_COMMIT | 2026-10-27T06:46:43Z | sn76 commit touches scoring: docs: sync worker CONTRACT.md (relay spend cap, verify feedback, plan… |
| `sn78:scoring_commit:2026-10-27T04:29:51Z` | 78 | SCORING_COMMIT | 2026-10-27T06:46:43Z | sn78 commit touches scoring: Merge pull request #445 from Umi-BitSign/feat/reward-operator-early-s… |
| `sn1:release:v4.5.0` | 1 | RELEASE | 2026-10-27T12:46:40Z | sn1 released v4.5.0 |
| `sn2:scoring_commit:2026-10-27T07:31:43Z` | 2 | SCORING_COMMIT | 2026-10-27T12:46:40Z | sn2 commit touches scoring: Gate unverified miner scores and refresh narrow validator dependencies |
| `sn3:scoring_commit:2026-10-27T11:33:11Z` | 3 | SCORING_COMMIT | 2026-10-27T12:46:40Z | sn3 commit touches scoring: Show per-category losses in evaluation history |
| `sn25:release:v2026.10.26-1082839840` | 25 | RELEASE | 2026-10-27T12:46:40Z | sn25 released v2026.10.26-1082839840 |
| `sn51:scoring_commit:2026-10-27T11:28:16Z` | 51 | SCORING_COMMIT | 2026-10-27T12:46:40Z | sn51 commit touches scoring: DAH-5235 - [P0] Validator: publish a node at once when its GPU comes … |
| `sn67:scoring_commit:2026-10-27T10:49:10Z` | 67 | SCORING_COMMIT | 2026-10-27T12:46:40Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20261027.post2 |
| `sn75:release:Runtime 92023` | 75 | RELEASE | 2026-10-27T12:46:40Z | sn75 released Runtime 92023 |
| `sn78:scoring_commit:2026-10-27T09:44:39Z` | 78 | SCORING_COMMIT | 2026-10-27T12:46:40Z | sn78 commit touches scoring: Cap retained reward coverage at native successor activation |
| `sn91:scoring_commit:2026-10-27T00:15:55Z` | 91 | SCORING_COMMIT | 2026-10-27T12:46:40Z | sn91 commit touches scoring: Report static-guard rejections from verify instead of crashing |
| `sn9:release:v4.13.10` | 9 | RELEASE | 2026-10-27T18:24:01Z | sn9 released v4.13.10 |
| `sn25:release:v2026.10.27-1083160450` | 25 | RELEASE | 2026-10-27T18:24:01Z | sn25 released v2026.10.27-1083160450 |
| `sn33:scoring_commit:2026-10-21T15:43:18Z` | 33 | SCORING_COMMIT | 2026-10-27T18:24:01Z | sn33 commit touches scoring: Enable 25% burn and shuffle task dispatch order |
| `sn50:scoring_commit:2026-10-27T16:16:32Z` | 50 | SCORING_COMMIT | 2026-10-27T18:24:01Z | sn50 commit touches scoring: fix(validator): resync the metagraph after a prompt that raised (#350) |
| `sn71:scoring_commit:2026-10-27T17:58:21Z` | 71 | SCORING_COMMIT | 2026-10-27T18:24:01Z | sn71 commit touches scoring: Record verified SSM cutover and permanent AWS account guidance |
| `sn78:scoring_commit:2026-10-27T18:03:38Z` | 78 | SCORING_COMMIT | 2026-10-27T18:24:01Z | sn78 commit touches scoring: Cap C7+ evaluation sources and preserve historical suite semantics (#… |
| `sn81:scoring_commit:2026-10-27T13:02:41Z` | 81 | SCORING_COMMIT | 2026-10-27T18:24:01Z | sn81 commit touches scoring: fix(rl-async): never charge miners for the validator's own downtime |
| `sn89:scoring_commit:2026-10-27T04:02:56Z` | 89 | SCORING_COMMIT | 2026-10-27T18:24:01Z | sn89 commit touches scoring: Signals entity accounts: hosted miners as subaccounts of one UID (arm… |
| `sn8:scoring_commit:2026-10-27T20:14:01Z` | 8 | SCORING_COMMIT | 2026-10-27T22:29:30Z | sn8 commit touches scoring: MinerAccountManager: one lock order (accounts → disk), fixes the orde… |
| `sn51:release:executor-v1.157` | 51 | RELEASE | 2026-10-27T22:29:30Z | sn51 released executor-v1.157 |
| `sn71:scoring_commit:2026-10-27T19:54:01Z` | 71 | SCORING_COMMIT | 2026-10-27T22:29:30Z | sn71 commit touches scoring: docs: scope Tyche capture verification and rollout |
| `sn92:release:v1.2.0-rc11.post8.1` | 92 | RELEASE | 2026-10-27T22:29:30Z | sn92 released v1.2.0-rc11.post8.1 |
| `sn92:scoring_commit:2026-10-27T22:13:15Z` | 92 | SCORING_COMMIT | 2026-10-27T22:29:30Z | sn92 commit touches scoring: 1.2.0rc11.post8.1: validator release for Wed 28 Oct 2026 12:00 UTC. E… |
| `sn34:scoring_commit:2026-10-27T23:51:10Z` | 34 | SCORING_COMMIT | 2026-10-28T01:48:43Z | sn34 commit touches scoring: Merge pull request #27 from BitMind-AI/feat/private-prepared-task-ext… |
| `sn71:scoring_commit:2026-10-28T01:19:48Z` | 71 | SCORING_COMMIT | 2026-10-28T01:48:43Z | sn71 commit touches scoring: docs: update Discord invite link |
| `sn91:scoring_commit:2026-10-28T00:15:26Z` | 91 | SCORING_COMMIT | 2026-10-28T01:48:43Z | sn91 commit touches scoring: Merge pull request #381 from TensorLink-AI/docs/validator-upgrade-11.3 |
| `sn94:scoring_commit:2026-10-27T22:57:38Z` | 94 | SCORING_COMMIT | 2026-10-28T01:48:43Z | sn94 commit touches scoring: Require AMD-verified attestation before planting an Escape nonce |
| `sn1:release:v4.5.1` | 1 | RELEASE | 2026-10-28T08:21:49Z | sn1 released v4.5.1 |
| `sn34:scoring_commit:2026-10-28T03:34:22Z` | 34 | SCORING_COMMIT | 2026-10-28T08:21:49Z | sn34 commit touches scoring: Document wording gate enforcement for new evaluations |
| `sn51:release:lium-protocol-v1.17.0` | 51 | RELEASE | 2026-10-28T08:21:49Z | sn51 released lium-protocol-v1.17.0 |
| `sn51:scoring_commit:2026-10-28T08:21:00Z` | 51 | SCORING_COMMIT | 2026-10-28T08:21:49Z | sn51 commit touches scoring: DAH-5037 - [P1] Validator: attach a default job's last log lines when… |
| `sn62:release:v0.3.14` | 62 | RELEASE | 2026-10-28T08:21:49Z | sn62 released v0.3.14 |
| `sn62:scoring_commit:2026-10-28T02:43:13Z` | 62 | SCORING_COMMIT | 2026-10-28T08:21:49Z | sn62 commit touches scoring: Merge pull request #532 from ridgesai/feat/validator-registry-dev |
| `sn71:scoring_commit:2026-10-28T08:00:36Z` | 71 | SCORING_COMMIT | 2026-10-28T08:21:49Z | sn71 commit touches scoring: Preserve verified pre-dispatch errors in Arena trajectory exports |
| `sn78:scoring_commit:2026-10-28T04:09:07Z` | 78 | SCORING_COMMIT | 2026-10-28T08:21:49Z | sn78 commit touches scoring: Merge pull request #460 from Umi-BitSign/fix/category-capacity-verifi… |
| `sn81:scoring_commit:2026-10-28T03:02:55Z` | 81 | SCORING_COMMIT | 2026-10-28T08:21:49Z | sn81 commit touches scoring: fix(eval): the auditor passes observe to score_sequences only for a d… |
| `sn28:scoring_commit:2026-10-28T14:32:16Z` | 28 | SCORING_COMMIT | 2026-10-28T15:18:42Z | sn28 commit touches scoring: Verify NEAR's GLM-5.3-Flash attested host (#359) |
| `sn32:scoring_commit:2026-10-28T07:45:48Z` | 32 | SCORING_COMMIT | 2026-10-28T15:18:42Z | sn32 commit touches scoring: Bump wandb to 0.31.0 so validator logs reach the current API (v3.15.1) |
| `sn50:release:v1.15.0` | 50 | RELEASE | 2026-10-28T15:18:42Z | sn50 released v1.15.0 |
| `sn51:scoring_commit:2026-10-28T11:12:55Z` | 51 | SCORING_COMMIT | 2026-10-28T15:18:42Z | sn51 commit touches scoring: DAH-5194 - [P1] Validator: key sshd bootstrap and registry pull state… |
| `sn53:scoring_commit:2026-10-28T10:52:11Z` | 53 | SCORING_COMMIT | 2026-10-28T15:18:42Z | sn53 commit touches scoring: Merge pull request #58 from hanlinai/feat/tee-miner-leg-rotation |
| `sn66:release:deployed/dev: Merge pull request #165 fr` | 66 | RELEASE | 2026-10-28T15:18:42Z | sn66 released deployed/dev: Merge pull request #165 from conjectures-io/feat/torchlean-intake-axiom |
| `sn78:scoring_commit:2026-10-28T14:35:16Z` | 78 | SCORING_COMMIT | 2026-10-28T15:18:42Z | sn78 commit touches scoring: Preserve verified captures and retry transient model copies (#468) |
| `sn104:scoring_commit:2026-10-28T09:46:22Z` | 104 | SCORING_COMMIT | 2026-10-28T15:18:42Z | sn104 commit touches scoring: Merge pull request #21 from taostatus/feat/python-script-miner |
| `sn114:scoring_commit:2026-10-28T14:14:48Z` | 114 | SCORING_COMMIT | 2026-10-28T15:18:42Z | sn114 commit touches scoring: Fix validator task image tag resolution |
| `sn17:release:witness-client-v0.2.15` | 17 | RELEASE | 2026-10-28T20:27:26Z | sn17 released witness-client-v0.2.15 |
| `sn66:release:v2026.10.28.2` | 66 | RELEASE | 2026-10-28T20:27:26Z | sn66 released v2026.10.28.2 |
| `sn71:scoring_commit:2026-10-28T19:43:06Z` | 71 | SCORING_COMMIT | 2026-10-28T20:27:26Z | sn71 commit touches scoring: Select preflight process helper before retained-slot recovery validati |
| `sn78:scoring_commit:2026-10-28T18:17:42Z` | 78 | SCORING_COMMIT | 2026-10-28T20:27:26Z | sn78 commit touches scoring: Reuse reservation validation and expose incremental intake progress |
| `sn97:scoring_commit:2026-10-28T16:13:46Z` | 97 | SCORING_COMMIT | 2026-10-28T20:27:26Z | sn97 commit touches scoring: feat(promoter): credit Bonsai 2 on q2 king cards by what the miner ch… |
| `sn78:readme_task_diff:07cc2c9379a76a69` | 78 | README_TASK_DIFF | 2026-10-22T07:29:56Z | sn78 README task/scoring sections changed |
| `sn15:readme_task_diff:71fad80912f70006` | 15 | README_TASK_DIFF | 2026-10-22T13:13:57Z | sn15 README task/scoring sections changed |
| `sn6:readme_task_diff:f71150d0a859d726` | 6 | README_TASK_DIFF | 2026-10-22T18:06:27Z | sn6 README task/scoring sections changed |
| `sn76:readme_task_diff:f81741e228d9d939` | 76 | README_TASK_DIFF | 2026-10-22T18:06:27Z | sn76 README task/scoring sections changed |
| `sn117:readme_task_diff:61eefa3e188bb2fb` | 117 | README_TASK_DIFF | 2026-10-22T18:06:27Z | sn117 README task/scoring sections changed |
| `sn117:readme_task_diff:cb1456ccf5f760fc` | 117 | README_TASK_DIFF | 2026-10-23T15:20:36Z | sn117 README task/scoring sections changed |
| `sn71:readme_task_diff:5bed35973cd7335b` | 71 | README_TASK_DIFF | 2026-10-26T00:45:22Z | sn71 README task/scoring sections changed |
| `sn2:readme_task_diff:48eb164474c3f6a5` | 2 | README_TASK_DIFF | 2026-10-26T21:56:01Z | sn2 README task/scoring sections changed |
| `sn123:readme_task_diff:f9658db3bedf0002` | 123 | README_TASK_DIFF | 2026-10-27T01:27:07Z | sn123 README task/scoring sections changed |
| `sn125:readme_task_diff:1476e035289bbae4` | 125 | README_TASK_DIFF | 2026-10-27T01:27:07Z | sn125 README task/scoring sections changed |
| `sn2:readme_task_diff:1ff49772ce88e83f` | 2 | README_TASK_DIFF | 2026-10-27T06:46:43Z | sn2 README task/scoring sections changed |
| `sn123:readme_task_diff:923cc435a761cf7e` | 123 | README_TASK_DIFF | 2026-10-27T06:46:43Z | sn123 README task/scoring sections changed |
| `sn2:readme_task_diff:db6ec8f75a1e4b61` | 2 | README_TASK_DIFF | 2026-10-27T12:46:40Z | sn2 README task/scoring sections changed |
| `sn91:readme_task_diff:9eb19065ad44711d` | 91 | README_TASK_DIFF | 2026-10-27T12:46:40Z | sn91 README task/scoring sections changed |

## RESOLVED IN THIS WINDOW

_none_
