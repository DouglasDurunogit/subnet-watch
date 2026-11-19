# ALARMS - generated 2026-11-19T13:41:24Z, block 9540994

window: first_seen in [2026-11-19T12:26:44Z, 2026-11-19T13:41:44Z)  (60 min interval + 15 min overlap)

Report ONLY the rows under NEW SINCE LAST RUN. Rows under STILL OPEN were
already reported in an earlier window and must not be re-alarmed.

## NEW SINCE LAST RUN

| event_id | netuid | class | severity | first_seen_utc | one_line |
|---|---|---|---|---|---|
| `sn12:release:validator-staging-2026-11-19-44521972284` | 12 | RELEASE | P1 | 2026-11-19T13:41:44Z | sn12 released validator-staging-2026-11-19-44521972284-633-1: fix: bump nginx (#875) |
| `sn12:scoring_commit:2026-11-19T13:35:45Z` | 12 | SCORING_COMMIT | P1 | 2026-11-19T13:41:44Z | sn12 commit touches scoring: fix: build compute-horde-validator-nginx in CD (#876) |
| `sn21:release:SN21 training data v7 (windows 2026-09-2` | 21 | RELEASE | P1 | 2026-11-19T13:41:44Z | sn21 released SN21 training data v7 (windows 2026-09-21 to 2026-10-04) |
| `sn24:release:v0.3.0` | 24 | RELEASE | P1 | 2026-11-19T13:41:44Z | sn24 released v0.3.0 |
| `sn42:release:v0.6.24` | 42 | RELEASE | P1 | 2026-11-19T13:41:44Z | sn42 released v0.6.24 |
| `sn42:scoring_commit:2026-11-19T13:28:49Z` | 42 | SCORING_COMMIT | P1 | 2026-11-19T13:41:44Z | sn42 commit touches scoring: v0.6.24: the validator's vote scores reach the platform |
| `sn45:scoring_commit:2026-11-15T03:16:42Z` | 45 | SCORING_COMMIT | P1 | 2026-11-19T13:41:44Z | sn45 commit touches scoring: Quality: each paid claim's pay is fixed by the coldkey's score when i… |
| `sn51:scoring_commit:2026-11-19T11:18:32Z` | 51 | SCORING_COMMIT | P1 | 2026-11-19T13:41:44Z | sn51 commit touches scoring: DAH-6714 - [P1] Validator: filler GPU process attribution counts in t… |
| `sn71:scoring_commit:2026-11-19T11:35:44Z` | 71 | SCORING_COMMIT | P1 | 2026-11-19T13:41:44Z | sn71 commit touches scoring: Fix review outage recovery lock order and verify full lifecycle |
| `sn116:scoring_commit:2026-11-19T11:43:48Z` | 116 | SCORING_COMMIT | P1 | 2026-11-19T13:41:44Z | sn116 commit touches scoring: Queue places: unmarked is not waiting; an owner whose unmarked tasks … |
| `sn99:readme_task_diff:70f3abe3d8c03fd9` | 99 | README_TASK_DIFF | P2 | 2026-11-19T13:41:44Z | sn99 README task/scoring sections changed |

### detail

- **`sn12:release:validator-staging-2026-11-19-44521972284`** - sn12 released validator-staging-2026-11-19-44521972284-633-1: fix: bump nginx (#875)
  - published 2026-11-19T12:12:05Z (was validator-staging-2026-11-18-44297690409-632-1: feat: miner manifest every 5000 blocks, validator ignores >25000 (#873))
- **`sn12:scoring_commit:2026-11-19T13:35:45Z`** - sn12 commit touches scoring: fix: build compute-horde-validator-nginx in CD (#876)
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn21:release:SN21 training data v7 (windows 2026-09-2`** - sn21 released SN21 training data v7 (windows 2026-09-21 to 2026-10-04)
  - published 2026-11-19T13:35:26Z (was SN21 training data v6 (windows 15 Aug - 20 Sep 2026))
- **`sn24:release:v0.3.0`** - sn24 released v0.3.0
  - published 2026-11-19T07:28:22Z (was v0.2.1)
- **`sn42:release:v0.6.24`** - sn42 released v0.6.24
  - published 2026-11-19T13:28:49Z (was v0.6.22)
- **`sn42:scoring_commit:2026-11-19T13:28:49Z`** - sn42 commit touches scoring: v0.6.24: the validator's vote scores reach the platform
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn45:scoring_commit:2026-11-15T03:16:42Z`** - sn45 commit touches scoring: Quality: each paid claim's pay is fixed by the coldkey's score when i…
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn51:scoring_commit:2026-11-19T11:18:32Z`** - sn51 commit touches scoring: DAH-6714 - [P1] Validator: filler GPU process attribution counts in t…
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn71:scoring_commit:2026-11-19T11:35:44Z`** - sn71 commit touches scoring: Fix review outage recovery lock order and verify full lifecycle
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn116:scoring_commit:2026-11-19T11:43:48Z`** - sn116 commit touches scoring: Queue places: unmarked is not waiting; an owner whose unmarked tasks …
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn99:readme_task_diff:70f3abe3d8c03fd9`** - sn99 README task/scoring sections changed
  - Only the task-describing headings are hashed, so badge and typo edits do not trigger this.

## STILL OPEN (already reported - do not re-alarm)

| event_id | netuid | class | first_seen_utc | one_line |
|---|---|---|---|---|
| `sn42:burn_drop:0.000` | 42 | BURN_DROP | 2026-11-13T00:38:05Z | sn42 burn fell 1.000 -> 0.000 - miners can earn again |
| `sn10:burn_drop:0.607` | 10 | BURN_DROP | 2026-11-13T15:34:59Z | sn10 burn fell 1.000 -> 0.607 - miners can earn again |
| `sn108:burn_drop:0.800` | 108 | BURN_DROP | 2026-11-14T08:55:08Z | sn108 burn fell 1.000 -> 0.800 - miners can earn again |
| `sn116:burn_drop:0.750` | 116 | BURN_DROP | 2026-11-14T20:09:45Z | sn116 burn fell 1.000 -> 0.750 - miners can earn again |
| `sn76:burn_drop:0.975` | 76 | BURN_DROP | 2026-11-15T06:17:56Z | sn76 burn fell 1.000 -> 0.975 - miners can earn again |
| `sn106:burn_drop:0.000` | 106 | BURN_DROP | 2026-11-15T19:53:52Z | sn106 burn fell 1.000 -> 0.000 - miners can earn again |
| `sn26:burn_drop:0.000` | 26 | BURN_DROP | 2026-11-15T23:57:01Z | sn26 burn fell 1.000 -> 0.000 - miners can earn again |
| `sn113:burn_drop:0.000` | 113 | BURN_DROP | 2026-11-17T17:44:54Z | sn113 burn fell 1.000 -> 0.000 - miners can earn again |
| `sn7:burn_drop:0.000` | 7 | BURN_DROP | 2026-11-18T00:00:43Z | sn7 burn fell 1.000 -> 0.000 - miners can earn again |
| `sn109:burn_drop:0.000` | 109 | BURN_DROP | 2026-11-18T23:10:24Z | sn109 burn fell 1.000 -> 0.000 - miners can earn again |
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
| `sn3:scoring_commit:2026-11-16T11:37:13Z` | 3 | SCORING_COMMIT | 2026-11-16T16:14:51Z | sn3 commit touches scoring: Stream Horizon scoring during packed-text sampling |
| `sn25:release:v2026.11.16-1100273030` | 25 | RELEASE | 2026-11-16T16:14:51Z | sn25 released v2026.11.16-1100273030 |
| `sn25:scoring_commit:2026-11-16T06:53:36Z` | 25 | SCORING_COMMIT | 2026-11-16T16:14:51Z | sn25 commit touches scoring: Merge fix/validator-nonce-wait-1116: the validator waits out the weig… |
| `sn42:release:v0.6.18` | 42 | RELEASE | 2026-11-16T16:14:51Z | sn42 released v0.6.18 |
| `sn42:scoring_commit:2026-11-16T08:59:35Z` | 42 | SCORING_COMMIT | 2026-11-16T16:14:51Z | sn42 commit touches scoring: reference miner: a brief that asks for nothing physical is rejected n… |
| `sn51:release:executor-v1.184` | 51 | RELEASE | 2026-11-16T16:14:51Z | sn51 released executor-v1.184 |
| `sn51:scoring_commit:2026-11-16T15:55:07Z` | 51 | SCORING_COMMIT | 2026-11-16T16:14:51Z | sn51 commit touches scoring: Validator: quote executor-reported paths in shell commands (#2280) |
| `sn67:scoring_commit:2026-11-16T10:09:40Z` | 67 | SCORING_COMMIT | 2026-11-16T16:14:51Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20261116.post8 |
| `sn71:scoring_commit:2026-11-16T11:03:00Z` | 71 | SCORING_COMMIT | 2026-11-16T16:14:51Z | sn71 commit touches scoring: Assert exact judgment binding in score projection tests |
| `sn111:scoring_commit:2026-11-16T12:01:40Z` | 111 | SCORING_COMMIT | 2026-11-16T16:14:51Z | sn111 commit touches scoring: Verify carried-forward scoring revisions during production handoff |
| `sn15:release:v3.0.9: fix(sandbox): isolate each task ` | 15 | RELEASE | 2026-11-17T00:22:13Z | sn15 released v3.0.9: fix(sandbox): isolate each task in a run from the run's other tasks |
| `sn15:scoring_commit:2026-11-16T21:42:42Z` | 15 | SCORING_COMMIT | 2026-11-17T00:22:13Z | sn15 commit touches scoring: fix(sandbox): isolate each task in a run from the run's other tasks |
| `sn25:release:v2026.11.16-1100716180` | 25 | RELEASE | 2026-11-17T00:22:13Z | sn25 released v2026.11.16-1100716180 |
| `sn25:scoring_commit:2026-11-16T19:08:58Z` | 25 | SCORING_COMMIT | 2026-11-17T00:22:13Z | sn25 commit touches scoring: Merge fix/validator-upload-encoding-1116: validator uploads go as zst… |
| `sn41:scoring_commit:2026-11-11T19:25:42Z` | 41 | SCORING_COMMIT | 2026-11-17T00:22:13Z | sn41 commit touches scoring: Document the one-agent-per-hotkey upload rule in the miner guide |
| `sn42:release:v0.6.19` | 42 | RELEASE | 2026-11-17T00:22:13Z | sn42 released v0.6.19 |
| `sn42:scoring_commit:2026-11-16T19:56:03Z` | 42 | SCORING_COMMIT | 2026-11-17T00:22:13Z | sn42 commit touches scoring: desk: a sweep of a miner's grants is job-scoped -- one job's grants f… |
| `sn62:scoring_commit:2026-11-16T20:35:34Z` | 62 | SCORING_COMMIT | 2026-11-17T00:22:13Z | sn62 commit touches scoring: add more validation |
| `sn66:release:v2026.11.16.4` | 66 | RELEASE | 2026-11-17T00:22:13Z | sn66 released v2026.11.16.4 |
| `sn70:release:build-v3rc1-2026.11.17: v3: pin the embe` | 70 | RELEASE | 2026-11-17T00:22:13Z | sn70 released build-v3rc1-2026.11.17: v3: pin the embeddings file (EMBEDDINGS_SHA256 + EMBEDDINGS_URL) |
| `sn94:scoring_commit:2026-11-16T17:02:42Z` | 94 | SCORING_COMMIT | 2026-11-17T00:22:13Z | sn94 commit touches scoring: Add miner hotel offer signer to room-kit (AB#347) (#565) |
| `sn127:release:Release 9bd0c63` | 127 | RELEASE | 2026-11-17T00:22:13Z | sn127 released Release 9bd0c63 |
| `sn127:scoring_commit:2026-11-16T00:13:27Z` | 127 | SCORING_COMMIT | 2026-11-17T00:22:13Z | sn127 commit touches scoring: Weekly judge: left-out bodies, scores from cached answers, the week's… |
| `sn25:release:v2026.11.16-1101008320` | 25 | RELEASE | 2026-11-17T08:16:39Z | sn25 released v2026.11.16-1101008320 |
| `sn42:release:v0.6.20` | 42 | RELEASE | 2026-11-17T08:16:39Z | sn42 released v0.6.20 |
| `sn51:scoring_commit:2026-11-17T07:09:42Z` | 51 | SCORING_COMMIT | 2026-11-17T08:16:39Z | sn51 commit touches scoring: DAH-6257 - [P2] Validator: avoid a host identity false positive after… |
| `sn67:scoring_commit:2026-11-16T10:46:55Z` | 67 | SCORING_COMMIT | 2026-11-17T08:16:39Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20261116.post9 |
| `sn70:release:SUPERSEDED: use image-v2026.11.17b` | 70 | RELEASE | 2026-11-17T08:16:39Z | sn70 released SUPERSEDED: use image-v2026.11.17b |
| `sn70:scoring_commit:2026-11-17T06:20:06Z` | 70 | SCORING_COMMIT | 2026-11-17T08:16:39Z | sn70 commit touches scoring: validator: the collateral startup probe only warns, and names itself |
| `sn71:scoring_commit:2026-11-17T06:40:15Z` | 71 | SCORING_COMMIT | 2026-11-17T08:16:39Z | sn71 commit touches scoring: Keep unvalidated paragraph replies out of shared judge cache |
| `sn76:release:Ormas subnet SDK 0.0.4` | 76 | RELEASE | 2026-11-17T08:16:39Z | sn76 released Ormas subnet SDK 0.0.4 |
| `sn91:scoring_commit:2026-11-17T01:24:31Z` | 91 | SCORING_COMMIT | 2026-11-17T08:16:39Z | sn91 commit touches scoring: validator: keep bench-sweep evidence; weight keep-alive during long s… |
| `sn111:scoring_commit:2026-11-17T01:46:11Z` | 111 | SCORING_COMMIT | 2026-11-17T08:16:39Z | sn111 commit touches scoring: Compress controller evaluation transport outside frozen policy |
| `sn3:scoring_commit:2026-11-17T15:26:48Z` | 3 | SCORING_COMMIT | 2026-11-17T17:44:54Z | sn3 commit touches scoring: Add 8×H200 evaluator support with TP2 MiMo replicas |
| `sn7:release:release-20261117-160316` | 7 | RELEASE | 2026-11-17T17:44:54Z | sn7 released release-20261117-160316 |
| `sn7:scoring_commit:2026-11-17T16:01:21Z` | 7 | SCORING_COMMIT | 2026-11-17T17:44:54Z | sn7 commit touches scoring: Drop VALIDATOR_MODE: the validator always sets weights unless told no… |
| `sn12:release:validator-staging-2026-11-17-44119698793` | 12 | RELEASE | 2026-11-17T17:44:54Z | sn12 released validator-staging-2026-11-17-44119698793-630-1: fix: failure to connect to miner creates a MinerIncident (#866) |
| `sn12:scoring_commit:2026-11-17T15:52:57Z` | 12 | SCORING_COMMIT | 2026-11-17T17:44:54Z | sn12 commit touches scoring: fix: failure to connect to miner creates a MinerIncident (#866) |
| `sn25:release:v2026.11.17-1101053110` | 25 | RELEASE | 2026-11-17T17:44:54Z | sn25 released v2026.11.17-1101053110 |
| `sn25:scoring_commit:2026-11-17T17:27:07Z` | 25 | SCORING_COMMIT | 2026-11-17T17:44:54Z | sn25 commit touches scoring: Merge feat/one-extender-stack-per-miner-1117: a provider run builds o… |
| `sn42:release:v0.6.21` | 42 | RELEASE | 2026-11-17T17:44:54Z | sn42 released v0.6.21 |
| `sn42:scoring_commit:2026-11-17T08:46:33Z` | 42 | SCORING_COMMIT | 2026-11-17T17:44:54Z | sn42 commit touches scoring: reference miner: find a fitted product's real geometry before building |
| `sn51:release:lium-protocol-v2.16.0` | 51 | RELEASE | 2026-11-17T17:44:54Z | sn51 released lium-protocol-v2.16.0 |
| `sn51:scoring_commit:2026-11-17T16:58:36Z` | 51 | SCORING_COMMIT | 2026-11-17T17:44:54Z | sn51 commit touches scoring: DAH-6579 - [P1] Validator refuses a reserved volume path instead of m… |
| `sn67:scoring_commit:2026-11-17T11:17:29Z` | 67 | SCORING_COMMIT | 2026-11-17T17:44:54Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20261117.post4 |
| `sn94:scoring_commit:2026-11-17T17:33:54Z` | 94 | SCORING_COMMIT | 2026-11-17T17:44:54Z | sn94 commit touches scoring: Add cathedral_sealed_hotels_v1 schema, pins, golden vector, verifiers… |
| `sn114:scoring_commit:2026-11-17T12:20:39Z` | 114 | SCORING_COMMIT | 2026-11-17T17:44:54Z | sn114 commit touches scoring: Reduce validator prefetch load, reuse a pooled HTTP client for compac… |
| `sn116:scoring_commit:2026-11-17T14:19:33Z` | 116 | SCORING_COMMIT | 2026-11-17T17:44:54Z | sn116 commit touches scoring: f02 deck 3.2: SCALAR_KEYS_V32 and public_scalars_v32 (4 approved scor… |
| `sn12:release:validator-staging-2026-11-17-44146334658` | 12 | RELEASE | 2026-11-18T00:00:43Z | sn12 released validator-staging-2026-11-17-44146334658-631-1: fix: support immutable library release, bump version (#870) |
| `sn22:scoring_commit:2026-11-17T20:44:24Z` | 22 | SCORING_COMMIT | 2026-11-18T00:00:43Z | sn22 commit touches scoring: Merge pull request #410 from Desearch-ai/fix/task-api-request-limits |
| `sn25:scoring_commit:2026-11-17T22:14:19Z` | 25 | SCORING_COMMIT | 2026-11-18T00:00:43Z | sn25 commit touches scoring: Merge feat/verify-cohort-v2-validator-1117: verify cohort v2, validat… |
| `sn51:scoring_commit:2026-11-17T20:16:15Z` | 51 | SCORING_COMMIT | 2026-11-18T00:00:43Z | sn51 commit touches scoring: DAH-6466 - Validator: retry the s3fs volume plugin install when the D… |
| `sn70:scoring_commit:2026-11-17T20:03:28Z` | 70 | SCORING_COMMIT | 2026-11-18T00:00:43Z | sn70 commit touches scoring: validator: approve only images that can prove the protocol in force |
| `sn116:scoring_commit:2026-11-17T21:58:00Z` | 116 | SCORING_COMMIT | 2026-11-18T00:00:43Z | sn116 commit touches scoring: Crowns: the official-score rule is the default for every version; a v… |
| `sn124:scoring_commit:2026-11-17T13:07:25Z` | 124 | SCORING_COMMIT | 2026-11-18T00:00:43Z | sn124 commit touches scoring: Add Swarm Test Field and close two evaluation sandbox gaps |
| `sn51:scoring_commit:2026-11-18T06:59:20Z` | 51 | SCORING_COMMIT | 2026-11-18T07:14:54Z | sn51 commit touches scoring: DAH-6566 - [P0] Validator writes the needrestart guard on hosts set u… |
| `sn67:scoring_commit:2026-11-18T03:06:43Z` | 67 | SCORING_COMMIT | 2026-11-18T07:14:54Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20261118.post1 |
| `sn81:scoring_commit:2026-11-17T11:05:03Z` | 81 | SCORING_COMMIT | 2026-11-18T07:14:54Z | sn81 commit touches scoring: fix(rl): a pod's link reaches its task's trainer routes and writes on… |
| `sn127:release:Release b5a248c` | 127 | RELEASE | 2026-11-18T07:14:54Z | sn127 released Release b5a248c |
| `sn12:release:validator-staging-2026-11-18-44297690409` | 12 | RELEASE | 2026-11-18T16:39:22Z | sn12 released validator-staging-2026-11-18-44297690409-632-1: feat: miner manifest every 5000 blocks, validator ignores >25000 (#873) |
| `sn12:scoring_commit:2026-11-18T12:17:58Z` | 12 | SCORING_COMMIT | 2026-11-18T16:39:22Z | sn12 commit touches scoring: feat: log validator ignored commitments (#874) |
| `sn25:release:v2026.11.18-1101975730` | 25 | RELEASE | 2026-11-18T16:39:22Z | sn25 released v2026.11.18-1101975730 |
| `sn42:release:v0.6.22` | 42 | RELEASE | 2026-11-18T16:39:22Z | sn42 released v0.6.22 |
| `sn42:scoring_commit:2026-11-18T09:39:30Z` | 42 | SCORING_COMMIT | 2026-11-18T16:39:22Z | sn42 commit touches scoring: v0.6.22: the reference miner checks watt status at DONE |
| `sn51:release:executor-v1.190` | 51 | RELEASE | 2026-11-18T16:39:22Z | sn51 released executor-v1.190 |
| `sn51:scoring_commit:2026-11-18T16:26:22Z` | 51 | SCORING_COMMIT | 2026-11-18T16:39:22Z | sn51 commit touches scoring: DAH-6546 - [P2] Validator: an unread pod after a GPU-set move is no v… |
| `sn67:scoring_commit:2026-11-18T13:20:08Z` | 67 | SCORING_COMMIT | 2026-11-18T16:39:22Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20261118.post6 |
| `sn90:release:v1.4.3` | 90 | RELEASE | 2026-11-18T16:39:22Z | sn90 released v1.4.3 |
| `sn90:scoring_commit:2026-11-18T14:27:49Z` | 90 | SCORING_COMMIT | 2026-11-18T16:39:22Z | sn90 commit touches scoring: fix(subnet): score only worker nodes |
| `sn111:scoring_commit:2026-11-18T10:21:20Z` | 111 | SCORING_COMMIT | 2026-11-18T16:39:22Z | sn111 commit touches scoring: Score audited Bronze source faults without an artifact |
| `sn62:release:v0.3.18` | 62 | RELEASE | 2026-11-18T23:10:24Z | sn62 released v0.3.18 |
| `sn71:scoring_commit:2026-11-18T21:05:38Z` | 71 | SCORING_COMMIT | 2026-11-18T23:10:24Z | sn71 commit touches scoring: Allow audited published judgment recovery with unchanged scorer |
| `sn93:scoring_commit:2026-11-18T19:10:32Z` | 93 | SCORING_COMMIT | 2026-11-18T23:10:24Z | sn93 commit touches scoring: feat(validator): score briefs with allowed_channels only for those ch… |
| `sn116:scoring_commit:2026-11-18T21:30:40Z` | 116 | SCORING_COMMIT | 2026-11-18T23:10:24Z | sn116 commit touches scoring: Auto retry: a spent cap (3 per failure code, 5 per task) writes an au… |
| `sn124:scoring_commit:2026-11-18T17:46:16Z` | 124 | SCORING_COMMIT | 2026-11-18T23:10:24Z | sn124 commit touches scoring: Merge pull request #246 from swarm-subnet/feature/ali/validator-memor… |
| `sn56:scoring_commit:2026-11-19T02:57:22Z` | 56 | SCORING_COMMIT | 2026-11-19T04:21:26Z | sn56 commit touches scoring: Incoming changes for miners (#1434) |
| `sn89:scoring_commit:2026-11-18T23:39:14Z` | 89 | SCORING_COMMIT | 2026-11-19T04:21:26Z | sn89 commit touches scoring: Validator: ignore blobs first stored more than 120 seconds after the … |
| `sn94:scoring_commit:2026-11-19T00:17:55Z` | 94 | SCORING_COMMIT | 2026-11-19T04:21:26Z | sn94 commit touches scoring: Merge pull request #434 from cathedralai/feature/go-receipt-verifier |
| `sn116:scoring_commit:2026-11-19T01:01:34Z` | 116 | SCORING_COMMIT | 2026-11-19T04:21:26Z | sn116 commit touches scoring: Miner client: 503 capacity retried like intake_busy (V2 add), with a … |
| `sn94:readme_task_diff:6bfe892e700f0a93` | 94 | README_TASK_DIFF | 2026-11-12T19:10:23Z | sn94 README task/scoring sections changed |
| `sn48:readme_task_diff:ccea6584910d3bd5` | 48 | README_TASK_DIFF | 2026-11-13T07:23:28Z | sn48 README task/scoring sections changed |
| `sn42:readme_task_diff:a31e8e8370c6e8f8` | 42 | README_TASK_DIFF | 2026-11-13T15:34:59Z | sn42 README task/scoring sections changed |
| `sn58:readme_task_diff:e5ddb56c3ad66771` | 58 | README_TASK_DIFF | 2026-11-13T15:34:59Z | sn58 README task/scoring sections changed |
| `sn69:readme_task_diff:55670d0ee7030fca` | 69 | README_TASK_DIFF | 2026-11-13T15:34:59Z | sn69 README task/scoring sections changed |
| `sn42:readme_task_diff:c68c8d6462ab6e33` | 42 | README_TASK_DIFF | 2026-11-14T01:52:12Z | sn42 README task/scoring sections changed |
| `sn90:readme_task_diff:a7b301753d76644f` | 90 | README_TASK_DIFF | 2026-11-15T23:57:01Z | sn90 README task/scoring sections changed |
| `sn42:readme_task_diff:dd8a6fb083469151` | 42 | README_TASK_DIFF | 2026-11-16T16:14:51Z | sn42 README task/scoring sections changed |
| `sn76:readme_task_diff:da868f725697bf9f` | 76 | README_TASK_DIFF | 2026-11-17T08:16:39Z | sn76 README task/scoring sections changed |
| `sn124:readme_task_diff:3167f0c564855989` | 124 | README_TASK_DIFF | 2026-11-18T00:00:43Z | sn124 README task/scoring sections changed |
| `sn127:readme_task_diff:0827763d022b8f1f` | 127 | README_TASK_DIFF | 2026-11-18T07:14:54Z | sn127 README task/scoring sections changed |
| `sn99:readme_task_diff:346f6cf3141fc736` | 99 | README_TASK_DIFF | 2026-11-18T23:10:24Z | sn99 README task/scoring sections changed |

## RESOLVED IN THIS WINDOW

_none_
