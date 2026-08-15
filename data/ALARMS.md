# ALARMS - generated 2026-08-15T23:31:00Z, block 8853325

window: first_seen in [2026-08-15T22:16:31Z, 2026-08-15T23:31:31Z)  (60 min interval + 15 min overlap)

Report ONLY the rows under NEW SINCE LAST RUN. Rows under STILL OPEN were
already reported in an earlier window and must not be re-alarmed.

## NEW SINCE LAST RUN

| event_id | netuid | class | severity | first_seen_utc | one_line |
|---|---|---|---|---|---|
| `sn76:scoring_commit:2026-08-15T23:00:47Z` | 76 | SCORING_COMMIT | P1 | 2026-08-15T23:01:41Z | sn76 commit touches scoring: Raise tasks per round across all four tracks |

### detail

- **`sn76:scoring_commit:2026-08-15T23:00:47Z`** - sn76 commit touches scoring: Raise tasks per round across all four tracks
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.

## STILL OPEN (already reported - do not re-alarm)

| event_id | netuid | class | first_seen_utc | one_line |
|---|---|---|---|---|
| `sn6:burn_drop:0.000` | 6 | BURN_DROP | 2026-08-09T02:25:34Z | sn6 burn fell 1.000 -> 0.000 - miners can earn again |
| `sn2:burn_drop:0.826` | 2 | BURN_DROP | 2026-08-09T08:07:46Z | sn2 burn fell 1.000 -> 0.826 - miners can earn again |
| `sn58:burn_drop:0.000` | 58 | BURN_DROP | 2026-08-10T03:01:40Z | sn58 burn fell 1.000 -> 0.000 - miners can earn again |
| `sn103:burn_drop:0.000` | 103 | BURN_DROP | 2026-08-10T18:24:36Z | sn103 burn fell 1.000 -> 0.000 - miners can earn again |
| `sn9:burn_drop:0.950` | 9 | BURN_DROP | 2026-08-11T17:27:32Z | sn9 burn fell 1.000 -> 0.950 - miners can earn again |
| `sn121:burn_drop:0.635` | 121 | BURN_DROP | 2026-08-11T17:27:32Z | sn121 burn fell 1.000 -> 0.635 - miners can earn again |
| `sn70:burn_drop:0.000` | 70 | BURN_DROP | 2026-08-13T04:32:20Z | sn70 burn fell 1.000 -> 0.000 - miners can earn again |
| `sn6:weights_version_bump:3000` | 6 | WEIGHTS_VERSION_BUMP | 2026-08-13T16:39:08Z | sn6 weights_version 2018 -> 3000 |
| `sn118:burn_drop:0.000` | 118 | BURN_DROP | 2026-08-13T17:45:02Z | sn118 burn fell 1.000 -> 0.000 - miners can earn again |
| `sn100:burn_drop:0.000` | 100 | BURN_DROP | 2026-08-13T19:46:45Z | sn100 burn fell 1.000 -> 0.000 - miners can earn again |
| `sn2:burn_drop:0.822` | 2 | BURN_DROP | 2026-08-14T09:18:19Z | sn2 burn fell 1.000 -> 0.822 - miners can earn again |
| `sn20:burn_drop:0.000` | 20 | BURN_DROP | 2026-08-14T15:05:31Z | sn20 burn fell 1.000 -> 0.000 - miners can earn again |
| `sn39:burn_drop:0.000` | 39 | BURN_DROP | 2026-08-14T15:05:31Z | sn39 burn fell 1.000 -> 0.000 - miners can earn again |
| `sn2:burn_drop:0.824` | 2 | BURN_DROP | 2026-08-14T23:33:14Z | sn2 burn fell 1.000 -> 0.824 - miners can earn again |
| `sn19:burn_drop:0.986` | 19 | BURN_DROP | 2026-08-14T23:33:14Z | sn19 burn fell 1.000 -> 0.986 - miners can earn again |
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
| `sn97:scoring_commit:2026-08-10T18:23:39Z` | 97 | SCORING_COMMIT | 2026-08-10T19:31:19Z | sn97 commit touches scoring: feat: add discarded questions to scoring artifact |
| `sn100:release:v3.3.15 — seal epoch sync + Prism submit` | 100 | RELEASE | 2026-08-10T19:31:19Z | sn100 released v3.3.15 — seal epoch sync + Prism submitter WTA |
| `sn2:release:14.13.3` | 2 | RELEASE | 2026-08-10T20:26:15Z | sn2 released 14.13.3 |
| `sn100:release:v3.3.16 — design emit cold-start + perma` | 100 | RELEASE | 2026-08-10T20:26:15Z | sn100 released v3.3.16 — design emit cold-start + permanent seal-sync digests |
| `sn56:scoring_commit:2026-08-10T22:40:49Z` | 56 | SCORING_COMMIT | 2026-08-10T22:55:47Z | sn56 commit touches scoring: Block tournament advancement when a group has no valid scores (#1349) |
| `sn91:scoring_commit:2026-08-10T23:24:09Z` | 91 | SCORING_COMMIT | 2026-08-10T23:47:46Z | sn91 commit touches scoring: DEC-CA-0012: Cascade warm-start promotion — propose-and-verify (#191) |
| `sn108:scoring_commit:2026-08-10T14:25:47Z` | 108 | SCORING_COMMIT | 2026-08-11T00:40:06Z | sn108 commit touches scoring: merge: the canonical miner script and the subnet-published image |
| `sn61:release:4.9.5` | 61 | RELEASE | 2026-08-11T02:55:15Z | sn61 released 4.9.5 |
| `sn61:scoring_commit:2026-08-11T00:14:46Z` | 61 | SCORING_COMMIT | 2026-08-11T02:55:15Z | sn61 commit touches scoring: refactor: update bot virus challenge environment variable for VM endp… |
| `sn91:scoring_commit:2026-08-11T03:25:57Z` | 91 | SCORING_COMMIT | 2026-08-11T04:36:46Z | sn91 commit touches scoring: validator: record the decided challenger's scores LAST in cohort rece… |
| `sn61:release:4.9.6` | 61 | RELEASE | 2026-08-11T07:58:57Z | sn61 released 4.9.6 |
| `sn85:scoring_commit:2026-08-11T08:12:13Z` | 85 | SCORING_COMMIT | 2026-08-11T09:11:54Z | sn85 commit touches scoring: isolate competition batches in separate miner Modal sandboxes (#182) |
| `sn96:release:Verathos v0.1.35 — Concurrent Proof Serv` | 96 | RELEASE | 2026-08-11T09:11:54Z | sn96 released Verathos v0.1.35 — Concurrent Proof Serving |
| `sn96:scoring_commit:2026-08-11T08:46:44Z` | 96 | SCORING_COMMIT | 2026-08-11T09:11:54Z | sn96 commit touches scoring: fix: recover shared-checkout miner updates |
| `sn21:scoring_commit:2026-08-11T12:05:14Z` | 21 | SCORING_COMMIT | 2026-08-11T12:08:46Z | sn21 commit touches scoring: merge: daily model intake, multi-miner execution, and the alpha-hold … |
| `sn66:scoring_commit:2026-08-11T11:34:05Z` | 66 | SCORING_COMMIT | 2026-08-11T12:08:46Z | sn66 commit touches scoring: Merge pull request #38 from conjectures-io/feat/api-retired-task-resul |
| `sn85:scoring_commit:2026-08-11T12:13:42Z` | 85 | SCORING_COMMIT | 2026-08-11T13:53:29Z | sn85 commit touches scoring: optimise validator competition dataset preparation pipeline to remove… |
| `sn1:release:v4.2.22` | 1 | RELEASE | 2026-08-11T15:13:24Z | sn1 released v4.2.22 |
| `sn28:release:v0.4.2-dev` | 28 | RELEASE | 2026-08-11T15:13:24Z | sn28 released v0.4.2-dev |
| `sn111:scoring_commit:2026-08-11T14:44:28Z` | 111 | SCORING_COMMIT | 2026-08-11T15:13:24Z | sn111 commit touches scoring: Improve Silver adjudication and scoring |
| `sn124:scoring_commit:2026-08-11T14:19:50Z` | 124 | SCORING_COMMIT | 2026-08-11T15:13:24Z | sn124 commit touches scoring: Merge per-process validator session and version 5.1.1.1 |
| `sn71:scoring_commit:2026-08-11T15:51:27Z` | 71 | SCORING_COMMIT | 2026-08-11T16:24:27Z | sn71 commit touches scoring: Seed required miner in Git-tree rehearsal |
| `sn100:release:v3.3.18 — design tip-emit from latest sc` | 100 | RELEASE | 2026-08-11T16:24:27Z | sn100 released v3.3.18 — design tip-emit from latest scored round only (#123) |
| `sn28:release:v0.4.3-dev` | 28 | RELEASE | 2026-08-11T17:27:32Z | sn28 released v0.4.3-dev |
| `sn44:scoring_commit:2026-08-11T17:22:55Z` | 44 | SCORING_COMMIT | 2026-08-11T17:27:32Z | sn44 commit touches scoring: Merge pull request #51 from score-technologies/audit-export |
| `sn75:scoring_commit:2026-08-11T08:48:47Z` | 75 | SCORING_COMMIT | 2026-08-11T17:27:32Z | sn75 commit touches scoring: fix: update max 24h miner payout test to 3500 alpha and fix comment |
| `sn74:release:release-20260811-182518: chore(weights):` | 74 | RELEASE | 2026-08-11T18:27:58Z | sn74 released release-20260811-182518: chore(weights): drop the linked-issue bonus for sparkinfer (#1687) |
| `sn89:scoring_commit:2026-08-11T17:49:59Z` | 89 | SCORING_COMMIT | 2026-08-11T18:27:58Z | sn89 commit touches scoring: HF: one submission counter for both signers — a hotkey's own miner wa… |
| `sn71:scoring_commit:2026-08-11T18:25:04Z` | 71 | SCORING_COMMIT | 2026-08-11T19:50:00Z | sn71 commit touches scoring: Reuse bounded artifact verification sessions |
| `sn62:scoring_commit:2026-08-11T20:08:25Z` | 62 | SCORING_COMMIT | 2026-08-11T22:58:25Z | sn62 commit touches scoring: update validator api changes |
| `sn71:scoring_commit:2026-08-11T23:29:21Z` | 71 | SCORING_COMMIT | 2026-08-11T23:54:20Z | sn71 commit touches scoring: Reuse artifact verification transport pool |
| `sn71:scoring_commit:2026-08-12T02:30:59Z` | 71 | SCORING_COMMIT | 2026-08-12T02:39:41Z | sn71 commit touches scoring: Isolate concurrent artifact verification transports |
| `sn100:release:v3.3.19 — design auto-enqueue + migratio` | 100 | RELEASE | 2026-08-12T06:05:56Z | sn100 released v3.3.19 — design auto-enqueue + migration 0019 fix |
| `sn100:scoring_commit:2026-08-12T04:29:33Z` | 100 | SCORING_COMMIT | 2026-08-12T06:05:56Z | sn100 commit touches scoring: Merge pull request #120 from BaseIntelligence/feat/prism-miner-paid-li |
| `sn71:scoring_commit:2026-08-12T07:37:36Z` | 71 | SCORING_COMMIT | 2026-08-12T07:49:32Z | sn71 commit touches scoring: Recover artifact verification from stale pools |
| `sn96:release:Verathos v0.1.36 — Runtime and Capacity ` | 96 | RELEASE | 2026-08-12T09:22:09Z | sn96 released Verathos v0.1.36 — Runtime and Capacity Stability |
| `sn85:scoring_commit:2026-08-12T09:34:50Z` | 85 | SCORING_COMMIT | 2026-08-12T10:34:51Z | sn85 commit touches scoring: add audio validation for competitions (#184) |
| `sn100:release:v3.3.21 — Prism Lium single-GPU hard-rej` | 100 | RELEASE | 2026-08-12T10:34:51Z | sn100 released v3.3.21 — Prism Lium single-GPU hard-reject (#129) |
| `sn51:release:executor-v1.117` | 51 | RELEASE | 2026-08-12T11:33:57Z | sn51 released executor-v1.117 |
| `sn28:release:v0.4.4-dev` | 28 | RELEASE | 2026-08-12T12:34:56Z | sn28 released v0.4.4-dev |
| `sn28:scoring_commit:2026-08-12T10:25:25Z` | 28 | SCORING_COMMIT | 2026-08-12T12:34:56Z | sn28 commit touches scoring: Document miner model sourcing options |
| `sn67:scoring_commit:2026-08-12T11:45:36Z` | 67 | SCORING_COMMIT | 2026-08-12T12:34:56Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20260812.post4 |
| `sn120:scoring_commit:2026-08-12T12:26:03Z` | 120 | SCORING_COMMIT | 2026-08-12T12:34:56Z | sn120 commit touches scoring: rollouts: recover 7k terminal_lego tasks by stubbing empty task_file |
| `sn28:release:v0.4.4` | 28 | RELEASE | 2026-08-12T14:09:20Z | sn28 released v0.4.4 |
| `sn28:scoring_commit:2026-08-12T12:46:41Z` | 28 | SCORING_COMMIT | 2026-08-12T14:09:20Z | sn28 commit touches scoring: Release gm-miner v0.4.4 |
| `sn56:scoring_commit:2026-08-12T13:16:40Z` | 56 | SCORING_COMMIT | 2026-08-12T14:09:20Z | sn56 commit touches scoring: Oversample 2026+ models into one R1 and one boss-round task (#1353) |
| `sn96:release:Verathos v0.1.37 — Scoring Integrity and` | 96 | RELEASE | 2026-08-12T14:09:20Z | sn96 released Verathos v0.1.37 — Scoring Integrity and Fairness |
| `sn96:scoring_commit:2026-08-12T11:40:32Z` | 96 | SCORING_COMMIT | 2026-08-12T14:09:20Z | sn96 commit touches scoring: fix: correct validator scoring inputs |
| `sn120:scoring_commit:2026-08-12T13:36:35Z` | 120 | SCORING_COMMIT | 2026-08-12T14:09:20Z | sn120 commit touches scoring: publish bench rollout records: per-task trajectories to hippius + api |
| `sn111:scoring_commit:2026-08-12T14:50:47Z` | 111 | SCORING_COMMIT | 2026-08-12T15:29:26Z | sn111 commit touches scoring: Add validator cost profile |
| `sn54:scoring_commit:2026-08-12T17:46:40Z` | 54 | SCORING_COMMIT | 2026-08-12T18:40:47Z | sn54 commit touches scoring: update miner screen reply readme |
| `sn41:scoring_commit:2026-08-12T22:36:16Z` | 41 | SCORING_COMMIT | 2026-08-12T22:57:11Z | sn41 commit touches scoring: Merge pull request #42 from corvxai/mkt_scoring_v2 |
| `sn51:release:executor-v1.118` | 51 | RELEASE | 2026-08-13T02:42:09Z | sn51 released executor-v1.118 |
| `sn66:scoring_commit:2026-08-13T00:05:35Z` | 66 | SCORING_COMMIT | 2026-08-13T02:42:09Z | sn66 commit touches scoring: Preserve production task retirements |
| `sn89:scoring_commit:2026-08-13T02:13:14Z` | 89 | SCORING_COMMIT | 2026-08-13T02:42:09Z | sn89 commit touches scoring: HF: submission-diversity gate — zero weight for one-sided miners on a… |
| `sn89:scoring_commit:2026-08-13T03:41:31Z` | 89 | SCORING_COMMIT | 2026-08-13T04:32:20Z | sn89 commit touches scoring: HF: measure miner behaviour above the board filter, not below it |
| `sn44:scoring_commit:2026-08-13T09:12:05Z` | 44 | SCORING_COMMIT | 2026-08-13T09:22:53Z | sn44 commit touches scoring: blacklist + min common challenges tiebreak |
| `sn67:scoring_commit:2026-08-13T09:35:16Z` | 67 | SCORING_COMMIT | 2026-08-13T10:35:49Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20260813.post3 |
| `sn1:release:v4.3.1` | 1 | RELEASE | 2026-08-13T14:10:36Z | sn1 released v4.3.1 |
| `sn26:scoring_commit:2026-08-13T14:58:07Z` | 26 | SCORING_COMMIT | 2026-08-13T15:31:13Z | sn26 commit touches scoring: Merge pull request #49 from 0xsigurd/feat/image-hash-verification |
| `sn51:release:executor-v1.119` | 51 | RELEASE | 2026-08-13T15:31:13Z | sn51 released executor-v1.119 |
| `sn75:scoring_commit:2026-08-13T13:14:25Z` | 75 | SCORING_COMMIT | 2026-08-13T15:31:13Z | sn75 commit touches scoring: updated validator weights submitter |
| `sn100:scoring_commit:2026-08-13T15:17:24Z` | 100 | SCORING_COMMIT | 2026-08-13T15:31:13Z | sn100 commit touches scoring: fix(site): attribute arena weight per challenge, not global burn (#142 |
| `sn38:scoring_commit:2026-08-13T16:30:43Z` | 38 | SCORING_COMMIT | 2026-08-13T16:39:08Z | sn38 commit touches scoring: Update validator image to latest version in docker-compose files |
| `sn90:release:v1.1.0 — Targon max $/card + raised GPU ` | 90 | RELEASE | 2026-08-13T16:39:08Z | sn90 released v1.1.0 — Targon max $/card + raised GPU card caps |
| `sn90:scoring_commit:2026-08-13T15:50:20Z` | 90 | SCORING_COMMIT | 2026-08-13T16:39:08Z | sn90 commit touches scoring: chore(validator): bump version to 1.1.0 for Watchtower v1 track |
| `sn15:scoring_commit:2026-08-13T21:50:38Z` | 15 | SCORING_COMMIT | 2026-08-13T22:10:33Z | sn15 commit touches scoring: chore(deps): bump msgpack from 1.1.2 to 1.2.1 in /docker/validator (#… |
| `sn91:scoring_commit:2026-08-13T21:52:49Z` | 91 | SCORING_COMMIT | 2026-08-13T22:10:33Z | sn91 commit touches scoring: miner dashboard: show warm-start init + next-round scheduled checkpoin |
| `sn91:scoring_commit:2026-08-13T23:06:33Z` | 91 | SCORING_COMMIT | 2026-08-13T23:12:08Z | sn91 commit touches scoring: miner dashboard: label warm-start checkpoints with their origin round… |
| `sn90:release:v1.1.1` | 90 | RELEASE | 2026-08-14T06:06:21Z | sn90 released v1.1.1 |
| `sn90:scoring_commit:2026-08-14T06:04:45Z` | 90 | SCORING_COMMIT | 2026-08-14T06:06:21Z | sn90 commit touches scoring: fix(validator): always apply the Targon supply-side clamp |
| `sn100:scoring_commit:2026-08-14T04:35:53Z` | 100 | SCORING_COMMIT | 2026-08-14T06:06:21Z | sn100 commit touches scoring: chore(deploy): promote prod prism-challenge pin for seal TTL fix (#147 |
| `sn44:scoring_commit:2026-08-14T08:54:31Z` | 44 | SCORING_COMMIT | 2026-08-14T09:18:19Z | sn44 commit touches scoring: Merge pull request #52 from score-technologies/tiebreak-enh-exploratio |
| `sn51:scoring_commit:2026-08-14T08:19:45Z` | 51 | SCORING_COMMIT | 2026-08-14T09:18:19Z | sn51 commit touches scoring: DAH-2622: floor a live miner's weight at one u16 unit funded from bur… |
| `sn100:scoring_commit:2026-08-14T08:35:14Z` | 100 | SCORING_COMMIT | 2026-08-14T09:18:19Z | sn100 commit touches scoring: chore(deploy): promote prod prism-challenge pin for METRICS harvest f… |
| `sn67:scoring_commit:2026-08-14T09:41:41Z` | 67 | SCORING_COMMIT | 2026-08-14T11:32:26Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20260814.post1 |
| `sn71:scoring_commit:2026-08-14T10:35:32Z` | 71 | SCORING_COMMIT | 2026-08-14T11:32:26Z | sn71 commit touches scoring: Refresh SOURCE_ADD reward ancestry identity |
| `sn96:release:Verathos v0.1.38 — Runtime and Proof Sta` | 96 | RELEASE | 2026-08-14T11:32:26Z | sn96 released Verathos v0.1.38 — Runtime and Proof Stability |
| `sn96:scoring_commit:2026-08-14T09:27:09Z` | 96 | SCORING_COMMIT | 2026-08-14T11:32:26Z | sn96 commit touches scoring: fix: retry validator updates after partial install |
| `sn97:scoring_commit:2026-08-14T08:09:05Z` | 97 | SCORING_COMMIT | 2026-08-14T11:32:26Z | sn97 commit touches scoring: feat: win both evaluations; increase step amount; question amount reb… |
| `sn90:release:v1.1.2` | 90 | RELEASE | 2026-08-14T12:30:02Z | sn90 released v1.1.2 |
| `sn90:scoring_commit:2026-08-14T12:09:55Z` | 90 | SCORING_COMMIT | 2026-08-14T12:30:02Z | sn90 commit touches scoring: fix(validator): set_weights on the configured subtensor endpoint |
| `sn96:release:Verathos v0.1.39 — Hard-Proof Timing Sta` | 96 | RELEASE | 2026-08-14T15:05:31Z | sn96 released Verathos v0.1.39 — Hard-Proof Timing Stability |
| `sn126:scoring_commit:2026-08-14T15:41:49Z` | 126 | SCORING_COMMIT | 2026-08-14T16:03:52Z | sn126 commit touches scoring: docs: describe continuous miner training tables |
| `sn55:scoring_commit:2026-08-14T16:37:31Z` | 55 | SCORING_COMMIT | 2026-08-14T17:08:05Z | sn55 commit touches scoring: print only valid scores |
| `sn55:scoring_commit:2026-08-14T17:58:40Z` | 55 | SCORING_COMMIT | 2026-08-14T18:24:30Z | sn55 commit touches scoring: print only valid scores |
| `sn100:scoring_commit:2026-08-14T17:13:42Z` | 100 | SCORING_COMMIT | 2026-08-14T18:24:30Z | sn100 commit touches scoring: chore(deploy): promote prod prism-challenge pin for BYOK seal keep (#… |
| `sn55:scoring_commit:2026-08-14T20:02:57Z` | 55 | SCORING_COMMIT | 2026-08-14T20:17:06Z | sn55 commit touches scoring: commit weights after validation |
| `sn96:release:Verathos v0.1.40 — Capacity Audit Schedu` | 96 | RELEASE | 2026-08-14T20:17:06Z | sn96 released Verathos v0.1.40 — Capacity Audit Scheduling Stability |
| `sn62:release:v0.2.7` | 62 | RELEASE | 2026-08-14T22:36:36Z | sn62 released v0.2.7 |
| `sn71:scoring_commit:2026-08-15T00:32:31Z` | 71 | SCORING_COMMIT | 2026-08-15T01:47:28Z | sn71 commit touches scoring: Keep private ICP scores out of telemetry |
| `sn100:scoring_commit:2026-08-15T02:46:25Z` | 100 | SCORING_COMMIT | 2026-08-15T03:25:28Z | sn100 commit touches scoring: chore(deploy): promote prod prism-challenge pin for G8 µP probe base … |
| `sn71:scoring_commit:2026-08-15T03:59:05Z` | 71 | SCORING_COMMIT | 2026-08-15T04:05:09Z | sn71 commit touches scoring: Provision hotkey verification in gateway enclaves |
| `sn108:scoring_commit:2026-08-15T04:00:22Z` | 108 | SCORING_COMMIT | 2026-08-15T04:05:09Z | sn108 commit touches scoring: feat(registry): require every evaluated chute to live in the promethe… |
| `sn67:scoring_commit:2026-08-14T10:52:59Z` | 67 | SCORING_COMMIT | 2026-08-15T04:45:10Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20260814.post2 |
| `sn67:scoring_commit:2026-08-15T08:24:59Z` | 67 | SCORING_COMMIT | 2026-08-15T09:06:33Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20260815.post1 |
| `sn100:scoring_commit:2026-08-15T12:26:39Z` | 100 | SCORING_COMMIT | 2026-08-15T12:56:35Z | sn100 commit touches scoring: feat(prism): live leaf from G2 benchmarks (scoring_version 4) (#160) |
| `sn100:scoring_commit:2026-08-15T13:20:08Z` | 100 | SCORING_COMMIT | 2026-08-15T13:39:18Z | sn100 commit touches scoring: fix(prism): rename lattice_score to satisfy clippy similar_names |
| `sn76:scoring_commit:2026-08-15T17:47:00Z` | 76 | SCORING_COMMIT | 2026-08-15T17:59:54Z | sn76 commit touches scoring: Add a local evaluation command |
| `sn108:scoring_commit:2026-08-15T20:13:27Z` | 108 | SCORING_COMMIT | 2026-08-15T20:35:26Z | sn108 commit touches scoring: docs(miner): drop the second artefact that was never built |
| `sn126:readme_task_diff:99d35d8a81c2f921` | 126 | README_TASK_DIFF | 2026-08-09T19:56:46Z | sn126 README task/scoring sections changed |
| `sn107:readme_task_diff:9628fd9429b582ad` | 107 | README_TASK_DIFF | 2026-08-10T15:13:27Z | sn107 README task/scoring sections changed |
| `sn108:readme_task_diff:3f08d6dd9fd4b2c2` | 108 | README_TASK_DIFF | 2026-08-11T00:40:06Z | sn108 README task/scoring sections changed |
| `sn126:readme_task_diff:57aeaffcb3f2147f` | 126 | README_TASK_DIFF | 2026-08-11T07:58:57Z | sn126 README task/scoring sections changed |
| `sn28:readme_task_diff:d8d5d6469509a9b6` | 28 | README_TASK_DIFF | 2026-08-11T13:53:29Z | sn28 README task/scoring sections changed |
| `sn28:readme_task_diff:50edab7d2bab95b4` | 28 | README_TASK_DIFF | 2026-08-12T12:34:56Z | sn28 README task/scoring sections changed |
| `sn126:readme_task_diff:8ff67deb6bfb1a47` | 126 | README_TASK_DIFF | 2026-08-12T14:09:20Z | sn126 README task/scoring sections changed |
| `sn66:readme_task_diff:371ffea333df26ac` | 66 | README_TASK_DIFF | 2026-08-12T23:55:02Z | sn66 README task/scoring sections changed |
| `sn66:readme_task_diff:59994c37a3ef19e9` | 66 | README_TASK_DIFF | 2026-08-13T02:42:09Z | sn66 README task/scoring sections changed |
| `sn89:readme_task_diff:32958de49be3add2` | 89 | README_TASK_DIFF | 2026-08-13T02:42:09Z | sn89 README task/scoring sections changed |
| `sn67:readme_task_diff:a54328c7fbaf2606` | 67 | README_TASK_DIFF | 2026-08-13T10:35:49Z | sn67 README task/scoring sections changed |
| `sn90:readme_task_diff:8fca31852ef23b0f` | 90 | README_TASK_DIFF | 2026-08-13T12:36:13Z | sn90 README task/scoring sections changed |
| `sn26:readme_task_diff:27b06992db454b8d` | 26 | README_TASK_DIFF | 2026-08-13T15:31:13Z | sn26 README task/scoring sections changed |
| `sn38:readme_task_diff:0929297366a7bf8b` | 38 | README_TASK_DIFF | 2026-08-13T16:39:08Z | sn38 README task/scoring sections changed |
| `sn55:readme_task_diff:d7f3a333f8affc99` | 55 | README_TASK_DIFF | 2026-08-14T14:04:14Z | sn55 README task/scoring sections changed |
| `sn121:readme_task_diff:4de589f5fb4cb70d` | 121 | README_TASK_DIFF | 2026-08-14T19:29:32Z | sn121 README task/scoring sections changed |
| `sn67:readme_task_diff:5a8da0f3ba283771` | 67 | README_TASK_DIFF | 2026-08-15T09:06:33Z | sn67 README task/scoring sections changed |

## RESOLVED IN THIS WINDOW

_none_
