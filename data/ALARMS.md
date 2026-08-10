# ALARMS - generated 2026-08-10T19:30:55Z, block 8816133

window: first_seen in [2026-08-10T18:16:19Z, 2026-08-10T19:31:19Z)  (60 min interval + 15 min overlap)

Report ONLY the rows under NEW SINCE LAST RUN. Rows under STILL OPEN were
already reported in an earlier window and must not be re-alarmed.

## NEW SINCE LAST RUN

| event_id | netuid | class | severity | first_seen_utc | one_line |
|---|---|---|---|---|---|
| `sn103:burn_drop:0.000` | 103 | BURN_DROP | P0 | 2026-08-10T18:24:36Z | sn103 burn fell 1.000 -> 0.000 - miners can earn again |
| `sn97:scoring_commit:2026-08-10T18:23:39Z` | 97 | SCORING_COMMIT | P1 | 2026-08-10T19:31:19Z | sn97 commit touches scoring: feat: add discarded questions to scoring artifact |
| `sn100:release:v3.3.15 — seal epoch sync + Prism submit` | 100 | RELEASE | P1 | 2026-08-10T19:31:19Z | sn100 released v3.3.15 — seal epoch sync + Prism submitter WTA |

### detail

- **`sn103:burn_drop:0.000`** - sn103 burn fell 1.000 -> 0.000 - miners can earn again
  - This subnet paid miners nothing and now pays. Worth a look before the field fills up.
- **`sn97:scoring_commit:2026-08-10T18:23:39Z`** - sn97 commit touches scoring: feat: add discarded questions to scoring artifact
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn100:release:v3.3.15 — seal epoch sync + Prism submit`** - sn100 released v3.3.15 — seal epoch sync + Prism submitter WTA
  - published 2026-08-10T19:12:09Z (was v3.3.13 — design screenshot egress proxy + gateway admin auth)

## STILL OPEN (already reported - do not re-alarm)

| event_id | netuid | class | first_seen_utc | one_line |
|---|---|---|---|---|
| `sn107:weights_version_bump:20` | 107 | WEIGHTS_VERSION_BUMP | 2026-08-04T04:26:43Z | sn107 weights_version 13 -> 20 |
| `sn104:burn_drop:0.968` | 104 | BURN_DROP | 2026-08-04T12:25:39Z | sn104 burn fell 1.000 -> 0.968 - miners can earn again |
| `sn120:burn_drop:0.000` | 120 | BURN_DROP | 2026-08-04T17:01:16Z | sn120 burn fell 1.000 -> 0.000 - miners can earn again |
| `sn36:burn_drop:0.000` | 36 | BURN_DROP | 2026-08-05T18:45:32Z | sn36 burn fell 1.000 -> 0.000 - miners can earn again |
| `sn72:burn_drop:0.000` | 72 | BURN_DROP | 2026-08-07T00:33:55Z | sn72 burn fell 1.000 -> 0.000 - miners can earn again |
| `sn100:burn_drop:0.269` | 100 | BURN_DROP | 2026-08-07T08:20:46Z | sn100 burn fell 1.000 -> 0.269 - miners can earn again |
| `sn28:burn_drop:0.471` | 28 | BURN_DROP | 2026-08-07T12:31:08Z | sn28 burn fell 0.998 -> 0.471 - miners can earn again |
| `sn121:burn_drop:0.828` | 121 | BURN_DROP | 2026-08-07T17:22:41Z | sn121 burn fell 1.000 -> 0.828 - miners can earn again |
| `sn93:burn_drop:0.592` | 93 | BURN_DROP | 2026-08-08T15:42:11Z | sn93 burn fell 0.993 -> 0.592 - miners can earn again |
| `sn55:burn_drop:0.021` | 55 | BURN_DROP | 2026-08-08T20:45:04Z | sn55 burn fell 1.000 -> 0.021 - miners can earn again |
| `sn6:burn_drop:0.000` | 6 | BURN_DROP | 2026-08-09T02:25:34Z | sn6 burn fell 1.000 -> 0.000 - miners can earn again |
| `sn2:burn_drop:0.826` | 2 | BURN_DROP | 2026-08-09T08:07:46Z | sn2 burn fell 1.000 -> 0.826 - miners can earn again |
| `sn58:burn_drop:0.000` | 58 | BURN_DROP | 2026-08-10T03:01:40Z | sn58 burn fell 1.000 -> 0.000 - miners can earn again |
| `sn89:scoring_commit:2026-08-03T19:58:12Z` | 89 | SCORING_COMMIT | 2026-08-03T20:39:27Z | sn89 commit touches scoring: closers feed: per-key display-label overrides (SN89_CLOSERS_MINER_LAB… |
| `sn13:release:Release v1.18.69` | 13 | RELEASE | 2026-08-03T23:17:05Z | sn13 released Release v1.18.69 |
| `sn54:scoring_commit:2026-07-22T23:19:48Z` | 54 | SCORING_COMMIT | 2026-08-03T23:17:05Z | sn54 commit touches scoring: Made miner process more Intuitive |
| `sn61:release:4.8.4` | 61 | RELEASE | 2026-08-04T00:59:07Z | sn61 released 4.8.4 |
| `sn61:scoring_commit:2026-08-04T00:04:26Z` | 61 | SCORING_COMMIT | 2026-08-04T00:59:07Z | sn61 commit touches scoring: fix: handle miner hotkey changes in update_miner_infos method |
| `sn66:scoring_commit:2026-08-04T02:48:27Z` | 66 | SCORING_COMMIT | 2026-08-04T04:26:43Z | sn66 commit touches scoring: Merge pull request #10 from conjectures-io/codex/audited-erdos-task-po |
| `sn67:scoring_commit:2026-08-03T08:56:41Z` | 67 | SCORING_COMMIT | 2026-08-04T04:26:43Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20260803.post0 |
| `sn51:scoring_commit:2026-08-04T07:10:47Z` | 51 | SCORING_COMMIT | 2026-08-04T07:17:01Z | sn51 commit touches scoring: DAH-2546, gate 8x flagship unrented incentive on NCU profiling or rea… |
| `sn71:scoring_commit:2026-08-04T04:42:37Z` | 71 | SCORING_COMMIT | 2026-08-04T07:17:01Z | sn71 commit touches scoring: Bind scoring artifacts to exact commitments |
| `sn104:scoring_commit:2026-08-04T06:17:28Z` | 104 | SCORING_COMMIT | 2026-08-04T07:17:01Z | sn104 commit touches scoring: fix the validator task resolution |
| `sn66:scoring_commit:2026-08-04T08:30:10Z` | 66 | SCORING_COMMIT | 2026-08-04T10:09:01Z | sn66 commit touches scoring: Merge pull request #11 from conjectures-io/fix/missing-task-mode |
| `sn89:scoring_commit:2026-08-04T08:36:48Z` | 89 | SCORING_COMMIT | 2026-08-04T10:09:01Z | sn89 commit touches scoring: closers 10% of total miner incentive (was 20%); LF/HF take the freed … |
| `sn111:scoring_commit:2026-08-04T11:35:22Z` | 111 | SCORING_COMMIT | 2026-08-04T12:25:39Z | sn111 commit touches scoring: Improve agent validation and source grounding |
| `sn114:scoring_commit:2026-08-04T11:22:01Z` | 114 | SCORING_COMMIT | 2026-08-04T12:25:39Z | sn114 commit touches scoring: Improve validation and sandbox dispatch performance |
| `sn126:scoring_commit:2026-08-04T11:03:05Z` | 126 | SCORING_COMMIT | 2026-08-04T12:25:39Z | sn126 commit touches scoring: Ensure validators adopt the 70 percent burn default |
| `sn62:release:v0.2.4` | 62 | RELEASE | 2026-08-04T17:01:16Z | sn62 released v0.2.4 |
| `sn12:release:validator-staging-2026-08-04-30935079890` | 12 | RELEASE | 2026-08-04T18:47:46Z | sn12 released validator-staging-2026-08-04-30935079890-625-1: chore: bump pylon to 2.3.1 and pylon client to 2.3.0 |
| `sn21:release:archive/per-cell-consensus-2026-06: feat` | 21 | RELEASE | 2026-08-04T18:47:46Z | sn21 released archive/per-cell-consensus-2026-06: feat(consensus): epoch reporter + rolling persistence + out-of-band CLI |
| `sn21:scoring_commit:2026-08-04T18:03:00Z` | 21 | SCORING_COMMIT | 2026-08-04T18:47:46Z | sn21 commit touches scoring: feat(validator): burn follows Rob's dated schedule; settle drops cens… |
| `sn126:scoring_commit:2026-08-04T17:06:27Z` | 126 | SCORING_COMMIT | 2026-08-04T18:47:46Z | sn126 commit touches scoring: Release validator deployment gate 0.2.4 |
| `sn62:scoring_commit:2026-08-04T22:06:13Z` | 62 | SCORING_COMMIT | 2026-08-04T23:16:34Z | sn62 commit touches scoring: Merge pull request #473 from ridgesai/update/crucible-labs-validator |
| `sn111:scoring_commit:2026-08-04T21:41:42Z` | 111 | SCORING_COMMIT | 2026-08-05T00:53:57Z | sn111 commit touches scoring: Improve silver alignment and scoring |
| `sn21:scoring_commit:2026-08-05T04:01:57Z` | 21 | SCORING_COMMIT | 2026-08-05T04:24:52Z | sn21 commit touches scoring: feat(verifiability): daily scoring receipt + verify_day — miners reru… |
| `sn91:release:worker-v0.5.0` | 91 | RELEASE | 2026-08-05T04:24:52Z | sn91 released worker-v0.5.0 |
| `sn15:release:v1.2.5` | 15 | RELEASE | 2026-08-05T07:16:10Z | sn15 released v1.2.5 |
| `sn62:release:v0.2.5` | 62 | RELEASE | 2026-08-05T07:16:10Z | sn62 released v0.2.5 |
| `sn66:scoring_commit:2026-08-04T14:07:21Z` | 66 | SCORING_COMMIT | 2026-08-05T10:06:20Z | sn66 commit touches scoring: Make task slug id's permanent |
| `sn71:scoring_commit:2026-08-05T07:40:50Z` | 71 | SCORING_COMMIT | 2026-08-05T10:06:20Z | sn71 commit touches scoring: Scope repeated validator weight evidence |
| `sn12:release:miner-staging-2026-08-05-31002481795-421` | 12 | RELEASE | 2026-08-05T12:15:25Z | sn12 released miner-staging-2026-08-05-31002481795-421-1: fix: replace unmaintained watchtower with nicholas-fedor fork |
| `sn21:scoring_commit:2026-08-05T10:23:09Z` | 21 | SCORING_COMMIT | 2026-08-05T12:15:25Z | sn21 commit touches scoring: feat(verifiability): W1+W3 — miners can now FETCH and rerun their scor |
| `sn61:release:4.9.0` | 61 | RELEASE | 2026-08-05T12:15:25Z | sn61 released 4.9.0 |
| `sn61:scoring_commit:2026-08-05T10:19:58Z` | 61 | SCORING_COMMIT | 2026-08-05T12:15:25Z | sn61 commit touches scoring: fix: uncomment validation for miner container image format |
| `sn66:scoring_commit:2026-08-05T11:06:36Z` | 66 | SCORING_COMMIT | 2026-08-05T12:15:25Z | sn66 commit touches scoring: Merge pull request #17 from conjectures-io/codex/production-verificat… |
| `sn67:scoring_commit:2026-08-05T10:53:54Z` | 67 | SCORING_COMMIT | 2026-08-05T12:15:25Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20260805.post2 |
| `sn21:release:SN21 training bundle` | 21 | RELEASE | 2026-08-05T14:53:57Z | sn21 released SN21 training bundle |
| `sn21:scoring_commit:2026-08-05T14:06:49Z` | 21 | SCORING_COMMIT | 2026-08-05T14:53:57Z | sn21 commit touches scoring: docs: resolve the first-basket date ambiguity and bring miner/validat… |
| `sn66:scoring_commit:2026-08-05T14:48:04Z` | 66 | SCORING_COMMIT | 2026-08-05T14:53:57Z | sn66 commit touches scoring: Merge pull request #23 from conjectures-io/fix/verification-worker-in… |
| `sn120:scoring_commit:2026-08-05T13:12:05Z` | 120 | SCORING_COMMIT | 2026-08-05T14:53:57Z | sn120 commit touches scoring: Disclose the serving stack so miners can pre-flight before burning a … |
| `sn66:scoring_commit:2026-08-05T15:37:52Z` | 66 | SCORING_COMMIT | 2026-08-05T16:50:02Z | sn66 commit touches scoring: Merge pull request #24 from conjectures-io/fix/verifier-initial-condi… |
| `sn96:release:v0.1.26 - Gleipnir Proof Protocol v3` | 96 | RELEASE | 2026-08-05T18:45:32Z | sn96 released v0.1.26 - Gleipnir Proof Protocol v3 |
| `sn96:scoring_commit:2026-08-05T18:24:13Z` | 96 | SCORING_COMMIT | 2026-08-05T18:45:32Z | sn96 commit touches scoring: fix: serialize validator block dispatch |
| `sn2:release:14.12.21` | 2 | RELEASE | 2026-08-05T20:18:55Z | sn2 released 14.12.21 |
| `sn13:release:Release v1.18.70` | 13 | RELEASE | 2026-08-05T20:18:55Z | sn13 released Release v1.18.70 |
| `sn13:scoring_commit:2026-08-05T19:45:21Z` | 13 | SCORING_COMMIT | 2026-08-05T20:18:55Z | sn13 commit touches scoring: Merge pull request #901 from macrocosm-os/feat/s3-quality-scoring-phas |
| `sn71:scoring_commit:2026-08-05T18:51:09Z` | 71 | SCORING_COMMIT | 2026-08-05T20:18:55Z | sn71 commit touches scoring: Refresh protected validator authority manifest |
| `sn96:release:v0.1.27 - Validator Boundary Hotfix` | 96 | RELEASE | 2026-08-05T20:18:55Z | sn96 released v0.1.27 - Validator Boundary Hotfix |
| `sn21:scoring_commit:2026-08-05T20:21:36Z` | 21 | SCORING_COMMIT | 2026-08-05T21:45:49Z | sn21 commit touches scoring: Merge pull request #6 from ippcteam/docs/daily-miner-validator-docs |
| `sn62:release:v0.2.6` | 62 | RELEASE | 2026-08-05T21:45:49Z | sn62 released v0.2.6 |
| `sn2:release:14.13.0` | 2 | RELEASE | 2026-08-05T22:45:44Z | sn2 released 14.13.0 |
| `sn15:scoring_commit:2026-08-05T22:07:55Z` | 15 | SCORING_COMMIT | 2026-08-05T22:45:44Z | sn15 commit touches scoring: feat(validator): epoch-pinned weights only, 22-min cadence, epoch-anc… |
| `sn2:release:14.13.1` | 2 | RELEASE | 2026-08-06T04:41:49Z | sn2 released 14.13.1 |
| `sn66:scoring_commit:2026-08-06T03:41:33Z` | 66 | SCORING_COMMIT | 2026-08-06T04:41:49Z | sn66 commit touches scoring: Merge pull request #28 from conjectures-io/codex/pin-retired-task-rel… |
| `sn71:scoring_commit:2026-08-06T03:51:32Z` | 71 | SCORING_COMMIT | 2026-08-06T04:41:49Z | sn71 commit touches scoring: Honor scoring maintenance between rebenchmark waves |
| `sn74:release:release-20260806-043739` | 74 | RELEASE | 2026-08-06T04:41:49Z | sn74 released release-20260806-043739 |
| `sn74:scoring_commit:2026-08-06T04:37:15Z` | 74 | SCORING_COMMIT | 2026-08-06T04:41:49Z | sn74 commit touches scoring: sparkinfer-k3: 3x faster time-decay for merged-PR scores (#1679) |
| `sn71:scoring_commit:2026-08-06T05:10:27Z` | 71 | SCORING_COMMIT | 2026-08-06T07:28:34Z | sn71 commit touches scoring: Repair Research Lab verifier drift |
| `sn100:release:v3.3.1 — prod validator trust-root roll` | 100 | RELEASE | 2026-08-06T07:28:34Z | sn100 released v3.3.1 — prod validator trust-root roll |
| `sn100:scoring_commit:2026-08-06T07:02:07Z` | 100 | SCORING_COMMIT | 2026-08-06T07:28:34Z | sn100 commit touches scoring: chore(pins): promote prod validator to v3.3.1 digest |
| `sn15:release:v1.2.6: docs(validator): correct stale w` | 15 | RELEASE | 2026-08-06T10:19:12Z | sn15 released v1.2.6: docs(validator): correct stale weight-salt fallback docstrings (#249) |
| `sn15:scoring_commit:2026-08-06T08:42:22Z` | 15 | SCORING_COMMIT | 2026-08-06T10:19:12Z | sn15 commit touches scoring: docs(validator): correct stale weight-salt fallback docstrings (#249) |
| `sn100:release:v3.3.1 — prod trust-root roll + prism ep` | 100 | RELEASE | 2026-08-06T10:19:12Z | sn100 released v3.3.1 — prod trust-root roll + prism epoch-close emission |
| `sn100:scoring_commit:2026-08-06T09:38:47Z` | 100 | SCORING_COMMIT | 2026-08-06T10:19:12Z | sn100 commit touches scoring: fix(design): sandbox miner HTML viewer end-to-end |
| `sn67:scoring_commit:2026-08-06T11:52:39Z` | 67 | SCORING_COMMIT | 2026-08-06T12:25:37Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20260806.post0 |
| `sn100:release:v3.3.2 — miner HTML sandboxing + chain e` | 100 | RELEASE | 2026-08-06T12:25:37Z | sn100 released v3.3.2 — miner HTML sandboxing + chain endpoint failover + ops fixes |
| `sn120:scoring_commit:2026-08-06T12:01:22Z` | 120 | SCORING_COMMIT | 2026-08-06T12:25:37Z | sn120 commit touches scoring: Document the RT-6 incident: sampler + ref-cache bugs found via miner … |
| `sn26:scoring_commit:2026-08-06T13:58:43Z` | 26 | SCORING_COMMIT | 2026-08-06T14:55:04Z | sn26 commit touches scoring: Merge pull request #45 from 0xsigurd/feat/leaderboard-scoring-cleanup |
| `sn126:scoring_commit:2026-08-06T14:12:18Z` | 126 | SCORING_COMMIT | 2026-08-06T14:55:04Z | sn126 commit touches scoring: Reduce validator burn default to 30 percent |
| `sn10:scoring_commit:2026-08-06T20:28:19Z` | 10 | SCORING_COMMIT | 2026-08-07T00:33:55Z | sn10 commit touches scoring: feat: default miner --api-base to https://api.pareton.ai (#53) |
| `sn14:scoring_commit:2026-08-06T20:14:29Z` | 14 | SCORING_COMMIT | 2026-08-07T00:33:55Z | sn14 commit touches scoring: Publish the tracked B300 pod evaluation adapter |
| `sn21:scoring_commit:2026-08-06T15:51:01Z` | 21 | SCORING_COMMIT | 2026-08-07T00:33:55Z | sn21 commit touches scoring: feat(scoring): wire one-payer into the daily allocation, from the rec… |
| `sn41:scoring_commit:2026-08-06T17:42:32Z` | 41 | SCORING_COMMIT | 2026-08-07T00:33:55Z | sn41 commit touches scoring: Adding minimum and recommended specs for running a validator |
| `sn66:scoring_commit:2026-08-06T17:23:11Z` | 66 | SCORING_COMMIT | 2026-08-07T00:33:55Z | sn66 commit touches scoring: update task pool and add review |
| `sn74:release:release-20260806-204130` | 74 | RELEASE | 2026-08-07T00:33:55Z | sn74 released release-20260806-204130 |
| `sn96:release:v0.1.28 - Gleipnir Proof Runtime Hardeni` | 96 | RELEASE | 2026-08-07T00:33:55Z | sn96 released v0.1.28 - Gleipnir Proof Runtime Hardening |
| `sn96:scoring_commit:2026-08-06T23:22:28Z` | 96 | SCORING_COMMIT | 2026-08-07T00:33:55Z | sn96 commit touches scoring: fix: refresh authenticated miner artifacts |
| `sn111:scoring_commit:2026-08-06T17:12:01Z` | 111 | SCORING_COMMIT | 2026-08-07T00:33:55Z | sn111 commit touches scoring: Update validator artifact hydration and batch post-pass |
| `sn67:scoring_commit:2026-08-07T02:31:14Z` | 67 | SCORING_COMMIT | 2026-08-07T03:41:13Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20260807.post0 |
| `sn100:release:v3.3.3` | 100 | RELEASE | 2026-08-07T03:41:13Z | sn100 released v3.3.3 |
| `sn98:scoring_commit:2026-08-07T05:49:16Z` | 98 | SCORING_COMMIT | 2026-08-07T06:49:22Z | sn98 commit touches scoring: chore: set TASKS_PER_ROUND as 5 |
| `sn100:release:v3.3.4 — design screenshots-only viewer ` | 100 | RELEASE | 2026-08-07T06:49:22Z | sn100 released v3.3.4 — design screenshots-only viewer + metagraph cache / real-seal |
| `sn90:release:v1.0.1` | 90 | RELEASE | 2026-08-07T09:31:19Z | sn90 released v1.0.1 |
| `sn90:scoring_commit:2026-08-07T09:14:19Z` | 90 | SCORING_COMMIT | 2026-08-07T09:31:19Z | sn90 commit touches scoring: fix(subnet): proxy rejects miners — only validators with validator_pe… |
| `sn114:scoring_commit:2026-08-07T08:41:26Z` | 114 | SCORING_COMMIT | 2026-08-07T09:31:19Z | sn114 commit touches scoring: Merge pull request #218 from DendriteHQ/fix/scoring_magic_number |
| `sn66:scoring_commit:2026-08-07T10:06:34Z` | 66 | SCORING_COMMIT | 2026-08-07T10:38:14Z | sn66 commit touches scoring: fix catalag endpoint pydantic type validation mismatch - list vs indi… |
| `sn111:scoring_commit:2026-08-07T10:19:22Z` | 111 | SCORING_COMMIT | 2026-08-07T10:38:14Z | sn111 commit touches scoring: Document miner batch and PDF options |
| `sn66:scoring_commit:2026-08-07T11:31:50Z` | 66 | SCORING_COMMIT | 2026-08-07T11:34:31Z | sn66 commit touches scoring: Merge pull request #30 from conjectures-io/feat/miner-side-verificati… |
| `sn126:scoring_commit:2026-08-07T11:17:25Z` | 126 | SCORING_COMMIT | 2026-08-07T12:31:08Z | sn126 commit touches scoring: Gate validator rounds by launch status |
| `sn100:release:v3.3.5` | 100 | RELEASE | 2026-08-07T14:01:48Z | sn100 released v3.3.5 |
| `sn21:scoring_commit:2026-08-07T14:45:16Z` | 21 | SCORING_COMMIT | 2026-08-07T15:06:25Z | sn21 commit touches scoring: fix(scoring): group copies by behaviour, because byte-equality was ev… |
| `sn100:release:v3.3.6 — Prism site window truthfulness` | 100 | RELEASE | 2026-08-07T15:06:25Z | sn100 released v3.3.6 — Prism site window truthfulness |
| `sn126:scoring_commit:2026-08-07T14:37:59Z` | 126 | SCORING_COMMIT | 2026-08-07T15:06:25Z | sn126 commit touches scoring: Bump validator auto-update version |
| `sn21:scoring_commit:2026-08-07T15:10:17Z` | 21 | SCORING_COMMIT | 2026-08-07T16:08:18Z | sn21 commit touches scoring: fix(scoring): bind the medoid closure explicitly |
| `sn74:release:release-20260807-154750` | 74 | RELEASE | 2026-08-07T16:08:18Z | sn74 released release-20260807-154750 |
| `sn21:scoring_commit:2026-08-07T17:15:35Z` | 21 | SCORING_COMMIT | 2026-08-07T17:22:41Z | sn21 commit touches scoring: feat(scoring): wire the anti-clone layers where they decide money |
| `sn46:scoring_commit:2026-08-07T15:24:17Z` | 46 | SCORING_COMMIT | 2026-08-07T17:22:41Z | sn46 commit touches scoring: Add localnet miner validator and platform plumbing |
| `sn21:scoring_commit:2026-08-07T17:32:20Z` | 21 | SCORING_COMMIT | 2026-08-07T18:10:42Z | sn21 commit touches scoring: refactor(scoring): one behavioural detector, not two |
| `sn28:release:v0.4.0` | 28 | RELEASE | 2026-08-07T19:28:43Z | sn28 released v0.4.0 |
| `sn60:scoring_commit:2026-08-07T18:13:15Z` | 60 | SCORING_COMMIT | 2026-08-07T19:28:43Z | sn60 commit touches scoring: removed Chutes for miner submission |
| `sn71:scoring_commit:2026-08-07T18:44:33Z` | 71 | SCORING_COMMIT | 2026-08-07T19:28:43Z | sn71 commit touches scoring: Authorize isolated autoresearch validation skill |
| `sn1:release:v4.2.21` | 1 | RELEASE | 2026-08-07T20:24:27Z | sn1 released v4.2.21 |
| `sn51:scoring_commit:2026-08-07T20:07:04Z` | 51 | SCORING_COMMIT | 2026-08-07T20:24:27Z | sn51 commit touches scoring: Fix A10 GPU model normalization in validator (#1204) |
| `sn28:release:v0.4.1` | 28 | RELEASE | 2026-08-07T21:11:37Z | sn28 released v0.4.1 |
| `sn61:release:4.9.1` | 61 | RELEASE | 2026-08-07T22:54:13Z | sn61 released 4.9.1 |
| `sn61:scoring_commit:2026-08-07T22:36:31Z` | 61 | SCORING_COMMIT | 2026-08-07T22:54:13Z | sn61 commit touches scoring: deps: update bot virus challenge dependencies and image version to 1.0 |
| `sn90:scoring_commit:2026-08-07T23:40:46Z` | 90 | SCORING_COMMIT | 2026-08-07T23:45:13Z | sn90 commit touches scoring: docs(validator): note proxy requires validator_permit (miners get 403) |
| `sn80:scoring_commit:2026-08-08T04:28:24Z` | 80 | SCORING_COMMIT | 2026-08-08T05:08:08Z | sn80 commit touches scoring: protocol+docs: champion margin 0.01, unified status model, burn verif… |
| `sn100:release:v3.3.8 — Design one-prompt / one-attempt` | 100 | RELEASE | 2026-08-08T05:08:08Z | sn100 released v3.3.8 — Design one-prompt / one-attempt / admin reject |
| `sn100:release:v3.3.9: fix(prism): stuck-sweep grace 10` | 100 | RELEASE | 2026-08-08T07:12:03Z | sn100 released v3.3.9: fix(prism): stuck-sweep grace 10h + harness log harvest |
| `sn100:release:v3.3.10: Prism similarity precheck + stu` | 100 | RELEASE | 2026-08-08T08:06:47Z | sn100 released v3.3.10: Prism similarity precheck + stuck-sweep fix |
| `sn38:scoring_commit:2026-08-08T09:07:32Z` | 38 | SCORING_COMMIT | 2026-08-08T09:51:08Z | sn38 commit touches scoring: Add miner self-test endpoint and dynamic quality prompts (#21) |
| `sn100:release:v3.3.11: Site arena UID + sealed weight ` | 100 | RELEASE | 2026-08-08T13:09:33Z | sn100 released v3.3.11: Site arena UID + sealed weight enrichment |
| `sn10:scoring_commit:2026-08-08T14:46:10Z` | 10 | SCORING_COMMIT | 2026-08-08T14:48:26Z | sn10 commit touches scoring: fix: unblock cross-build ccache hits, mount miner cache read-only (#62 |
| `sn21:scoring_commit:2026-08-08T14:21:46Z` | 21 | SCORING_COMMIT | 2026-08-08T14:48:26Z | sn21 commit touches scoring: docs: separate weekly-era scoring from the daily stream, and require … |
| `sn96:release:v0.1.29 - Gleipnir Validator Reliability` | 96 | RELEASE | 2026-08-08T17:43:08Z | sn96 released v0.1.29 - Gleipnir Validator Reliability |
| `sn96:scoring_commit:2026-08-08T15:09:26Z` | 96 | SCORING_COMMIT | 2026-08-08T17:43:08Z | sn96 commit touches scoring: fix: isolate validator epoch control work |
| `sn71:scoring_commit:2026-08-08T19:19:55Z` | 71 | SCORING_COMMIT | 2026-08-08T19:53:36Z | sn71 commit touches scoring: Fix evaluator test import isolation |
| `sn100:release:v3.3.12` | 100 | RELEASE | 2026-08-08T19:53:36Z | sn100 released v3.3.12 |
| `sn100:scoring_commit:2026-08-08T19:36:07Z` | 100 | SCORING_COMMIT | 2026-08-08T19:53:36Z | sn100 commit touches scoring: fix(design): keep challenge-agentic under loc-cap |
| `sn71:scoring_commit:2026-08-08T20:21:46Z` | 71 | SCORING_COMMIT | 2026-08-08T20:45:04Z | sn71 commit touches scoring: Retry signed transient company scoring failures |
| `sn100:release:v3.3.13 — design screenshot egress proxy` | 100 | RELEASE | 2026-08-08T20:45:04Z | sn100 released v3.3.13 — design screenshot egress proxy + gateway admin auth |
| `sn100:scoring_commit:2026-08-08T21:01:32Z` | 100 | SCORING_COMMIT | 2026-08-08T21:15:02Z | sn100 commit touches scoring: Merge pull request #101 from BaseIntelligence/fix/master-no-validator… |
| `sn76:scoring_commit:2026-08-08T21:44:42Z` | 76 | SCORING_COMMIT | 2026-08-08T21:55:55Z | sn76 commit touches scoring: Document the real agent size limits and stop rejecting tasks with no … |
| `sn61:release:4.9.2` | 61 | RELEASE | 2026-08-09T02:25:34Z | sn61 released 4.9.2 |
| `sn61:scoring_commit:2026-08-08T08:01:06Z` | 61 | SCORING_COMMIT | 2026-08-09T02:25:34Z | sn61 commit touches scoring: refactor: update minimum acceptable score for challenges in configura… |
| `sn92:scoring_commit:2026-08-08T22:46:16Z` | 92 | SCORING_COMMIT | 2026-08-09T02:25:34Z | sn92 commit touches scoring: Document the directive as the source of every scoring parameter |
| `sn92:scoring_commit:2026-08-09T05:06:02Z` | 92 | SCORING_COMMIT | 2026-08-09T05:16:01Z | sn92 commit touches scoring: Move inference cost off the validator and onto the submission |
| `sn71:scoring_commit:2026-08-09T07:50:56Z` | 71 | SCORING_COMMIT | 2026-08-09T09:02:27Z | sn71 commit touches scoring: Retry transient company homepage verification |
| `sn96:release:v0.1.30 - Gleipnir FP8 Runtime Precision` | 96 | RELEASE | 2026-08-09T09:02:27Z | sn96 released v0.1.30 - Gleipnir FP8 Runtime Precision |
| `sn71:scoring_commit:2026-08-09T09:39:44Z` | 71 | SCORING_COMMIT | 2026-08-09T09:53:17Z | sn71 commit touches scoring: Use fresh identities for scorer retries |
| `sn61:release:4.9.3` | 61 | RELEASE | 2026-08-09T10:49:31Z | sn61 released 4.9.3 |
| `sn61:scoring_commit:2026-08-09T10:26:10Z` | 61 | SCORING_COMMIT | 2026-08-09T10:49:31Z | sn61 commit touches scoring: deps: update challenge image version for bot_virus_v1 to 1.0.3 |
| `sn67:scoring_commit:2026-08-09T09:41:18Z` | 67 | SCORING_COMMIT | 2026-08-09T10:49:31Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20260809.post0 |
| `sn96:release:v0.1.31 - Validator Auto-Update Drain` | 96 | RELEASE | 2026-08-09T10:49:31Z | sn96 released v0.1.31 - Validator Auto-Update Drain |
| `sn96:scoring_commit:2026-08-09T09:59:04Z` | 96 | SCORING_COMMIT | 2026-08-09T10:49:31Z | sn96 commit touches scoring: fix: drain validator work before auto-update |
| `sn96:release:v0.1.32 - Miner Hard-Proof Transport` | 96 | RELEASE | 2026-08-09T13:30:27Z | sn96 released v0.1.32 - Miner Hard-Proof Transport |
| `sn96:scoring_commit:2026-08-09T12:20:34Z` | 96 | SCORING_COMMIT | 2026-08-09T13:30:27Z | sn96 commit touches scoring: fix: align miner proxy with hard proof deadline |
| `sn71:scoring_commit:2026-08-09T15:45:11Z` | 71 | SCORING_COMMIT | 2026-08-09T16:15:15Z | sn71 commit touches scoring: Preserve handled scorer transport failures |
| `sn90:release:v1.0.2 — proxy version header + owner mi` | 90 | RELEASE | 2026-08-09T18:18:04Z | sn90 released v1.0.2 — proxy version header + owner miner UID hardcode |
| `sn90:scoring_commit:2026-08-09T18:13:35Z` | 90 | SCORING_COMMIT | 2026-08-09T18:18:04Z | sn90 commit touches scoring: feat(validator): v1.0.2 — proxy version header + hardcode owner miner… |
| `sn126:scoring_commit:2026-08-09T19:04:26Z` | 126 | SCORING_COMMIT | 2026-08-09T19:56:46Z | sn126 commit touches scoring: Document miner training benchmark |
| `sn71:scoring_commit:2026-08-09T20:10:42Z` | 71 | SCORING_COMMIT | 2026-08-09T20:49:18Z | sn71 commit touches scoring: Close and verify dev snapshot request sets |
| `sn89:scoring_commit:2026-08-09T22:14:09Z` | 89 | SCORING_COMMIT | 2026-08-09T22:14:48Z | sn89 commit touches scoring: Referrer: score recruiters across every competition, not LF only |
| `sn89:scoring_commit:2026-08-10T02:26:54Z` | 89 | SCORING_COMMIT | 2026-08-10T03:01:40Z | sn89 commit touches scoring: Retire MINER_EMISSION_CAP, and make it replay-safe on the way out |
| `sn92:scoring_commit:2026-08-10T00:47:03Z` | 92 | SCORING_COMMIT | 2026-08-10T03:01:40Z | sn92 commit touches scoring: Tell a validator when no directive exists rather than blaming its buil |
| `sn91:scoring_commit:2026-08-10T04:06:38Z` | 91 | SCORING_COMMIT | 2026-08-10T06:20:21Z | sn91 commit touches scoring: miner: `cascade duel` — full settled-round verdict from public receipt |
| `sn96:release:v0.1.33 - Maximum-Concurrency Proof Serv` | 96 | RELEASE | 2026-08-10T06:20:21Z | sn96 released v0.1.33 - Maximum-Concurrency Proof Serving |
| `sn61:release:4.9.4` | 61 | RELEASE | 2026-08-10T08:13:47Z | sn61 released 4.9.4 |
| `sn71:scoring_commit:2026-08-10T07:15:30Z` | 71 | SCORING_COMMIT | 2026-08-10T08:13:47Z | sn71 commit touches scoring: Gate daily scoring and autoresearch readiness |
| `sn96:release:Verathos v0.1.34 — Reliable Miner Update` | 96 | RELEASE | 2026-08-10T08:13:47Z | sn96 released Verathos v0.1.34 — Reliable Miner Updates |
| `sn96:scoring_commit:2026-08-10T06:32:26Z` | 96 | SCORING_COMMIT | 2026-08-10T08:13:47Z | sn96 commit touches scoring: fix: resume deferred miner updates at idle |
| `sn56:scoring_commit:2026-08-10T08:27:12Z` | 56 | SCORING_COMMIT | 2026-08-10T09:57:17Z | sn56 commit touches scoring: Fix degenerate-dataset filter for DPO boss-round tasks (#1344) |
| `sn89:scoring_commit:2026-08-10T11:35:10Z` | 89 | SCORING_COMMIT | 2026-08-10T12:08:05Z | sn89 commit touches scoring: hf: import time — hf_scoring_config() raised NameError on every bare … |
| `sn51:release:executor-v1.116` | 51 | RELEASE | 2026-08-10T13:54:33Z | sn51 released executor-v1.116 |
| `sn66:scoring_commit:2026-08-10T13:20:05Z` | 66 | SCORING_COMMIT | 2026-08-10T13:54:33Z | sn66 commit touches scoring: Merge pull request #35 from conjectures-io/feat/show-retired-tasks |
| `sn67:scoring_commit:2026-08-10T12:29:01Z` | 67 | SCORING_COMMIT | 2026-08-10T13:54:33Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20260810.post5 |
| `sn75:scoring_commit:2026-08-10T13:09:53Z` | 75 | SCORING_COMMIT | 2026-08-10T13:54:33Z | sn75 commit touches scoring: Merge pull request #36 from thenervelab/feat/arion-miner-payments |
| `sn120:scoring_commit:2026-08-10T12:09:35Z` | 120 | SCORING_COMMIT | 2026-08-10T13:54:33Z | sn120 commit touches scoring: Raise duel max_model_len to 65k and stop burning miners on context-li… |
| `sn124:scoring_commit:2026-08-10T13:51:15Z` | 124 | SCORING_COMMIT | 2026-08-10T13:54:33Z | sn124 commit touches scoring: Report seed scores under the epoch that leased them |
| `sn66:scoring_commit:2026-08-10T14:15:27Z` | 66 | SCORING_COMMIT | 2026-08-10T15:13:27Z | sn66 commit touches scoring: Merge pull request #36 from conjectures-io/feat/show-retired-tasks |
| `sn2:release:14.13.2` | 2 | RELEASE | 2026-08-10T16:22:50Z | sn2 released 14.13.2 |
| `sn120:scoring_commit:2026-08-10T15:52:21Z` | 120 | SCORING_COMMIT | 2026-08-10T16:22:50Z | sn120 commit touches scoring: Reason v3: single-term scoring fork (weight_version_key=3) |
| `sn104:scoring_commit:2026-08-10T16:47:17Z` | 104 | SCORING_COMMIT | 2026-08-10T17:25:08Z | sn104 commit touches scoring: fix validator weight-setting reliability and harden miner/BT-Forecast… |
| `sn66:readme_task_diff:590464a740b5fa2c` | 66 | README_TASK_DIFF | 2026-08-04T04:26:43Z | sn66 README task/scoring sections changed |
| `sn107:readme_task_diff:661e720302e307e2` | 107 | README_TASK_DIFF | 2026-08-04T04:26:43Z | sn107 README task/scoring sections changed |
| `sn104:readme_task_diff:708acebd54cc33f2` | 104 | README_TASK_DIFF | 2026-08-04T07:17:01Z | sn104 README task/scoring sections changed |
| `sn126:readme_task_diff:b1d8478cb914a832` | 126 | README_TASK_DIFF | 2026-08-04T12:25:39Z | sn126 README task/scoring sections changed |
| `sn21:readme_task_diff:e74e71fca670eb67` | 21 | README_TASK_DIFF | 2026-08-04T18:47:46Z | sn21 README task/scoring sections changed |
| `sn21:readme_task_diff:4f50af431820cc6d` | 21 | README_TASK_DIFF | 2026-08-05T12:15:25Z | sn21 README task/scoring sections changed |
| `sn66:readme_task_diff:3b6ca4cc88e47a32` | 66 | README_TASK_DIFF | 2026-08-05T12:15:25Z | sn66 README task/scoring sections changed |
| `sn21:readme_task_diff:dca6a31add16ab48` | 21 | README_TASK_DIFF | 2026-08-05T14:53:57Z | sn21 README task/scoring sections changed |
| `sn21:readme_task_diff:1048bc3f492a891d` | 21 | README_TASK_DIFF | 2026-08-05T16:50:02Z | sn21 README task/scoring sections changed |
| `sn88:readme_task_diff:afb1f6ac01d629e7` | 88 | README_TASK_DIFF | 2026-08-05T20:18:55Z | sn88 README task/scoring sections changed |
| `sn21:readme_task_diff:2d2991d58d2b0594` | 21 | README_TASK_DIFF | 2026-08-05T21:45:49Z | sn21 README task/scoring sections changed |
| `sn66:readme_task_diff:96b14914dd39764d` | 66 | README_TASK_DIFF | 2026-08-06T04:41:49Z | sn66 README task/scoring sections changed |
| `sn100:readme_task_diff:98275d6e78bda7a7` | 100 | README_TASK_DIFF | 2026-08-06T07:28:34Z | sn100 README task/scoring sections changed |
| `sn126:readme_task_diff:7ca8ea1d7f25bb3b` | 126 | README_TASK_DIFF | 2026-08-06T14:55:04Z | sn126 README task/scoring sections changed |
| `sn66:readme_task_diff:a7859610dea4219a` | 66 | README_TASK_DIFF | 2026-08-07T00:33:55Z | sn66 README task/scoring sections changed |
| `sn111:readme_task_diff:e76e2ccadcee7567` | 111 | README_TASK_DIFF | 2026-08-07T00:33:55Z | sn111 README task/scoring sections changed |
| `sn111:readme_task_diff:ec7a7e78b8effd65` | 111 | README_TASK_DIFF | 2026-08-07T10:38:14Z | sn111 README task/scoring sections changed |
| `sn10:readme_task_diff:2aef81117c887b4e` | 10 | README_TASK_DIFF | 2026-08-07T15:06:25Z | sn10 README task/scoring sections changed |
| `sn126:readme_task_diff:99d35d8a81c2f921` | 126 | README_TASK_DIFF | 2026-08-09T19:56:46Z | sn126 README task/scoring sections changed |
| `sn107:readme_task_diff:9628fd9429b582ad` | 107 | README_TASK_DIFF | 2026-08-10T15:13:27Z | sn107 README task/scoring sections changed |

## RESOLVED IN THIS WINDOW

_none_
