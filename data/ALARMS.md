# ALARMS - generated 2026-08-02T16:39:19Z, block 8757687

window: first_seen in [2026-08-02T15:24:54Z, 2026-08-02T16:39:54Z)  (60 min interval + 15 min overlap)

Report ONLY the rows under NEW SINCE LAST RUN. Rows under STILL OPEN were
already reported in an earlier window and must not be re-alarmed.

## NEW SINCE LAST RUN

| event_id | netuid | class | severity | first_seen_utc | one_line |
|---|---|---|---|---|---|
| `sn24:burn_drop:0.000` | 24 | BURN_DROP | P0 | 2026-08-02T16:39:54Z | sn24 burn fell 1.000 -> 0.000 - miners can earn again |
| `sn71:scoring_commit:2026-08-02T13:57:44Z` | 71 | SCORING_COMMIT | P1 | 2026-08-02T15:37:21Z | sn71 commit touches scoring: Bind verified auditor fallback workflow |
| `sn89:scoring_commit:2026-08-02T14:22:11Z` | 89 | SCORING_COMMIT | P1 | 2026-08-02T15:37:21Z | sn89 commit touches scoring: hf scoreboard: publish each hotkeys own recent_calls |
| `sn71:scoring_commit:2026-08-02T15:36:41Z` | 71 | SCORING_COMMIT | P1 | 2026-08-02T16:39:54Z | sn71 commit touches scoring: Verify candidate recovery against pre-signing receipt |
| `sn76:scoring_commit:2026-08-02T15:40:23Z` | 76 | SCORING_COMMIT | P1 | 2026-08-02T16:39:54Z | sn76 commit touches scoring: Update scoring constants |

### detail

- **`sn24:burn_drop:0.000`** - sn24 burn fell 1.000 -> 0.000 - miners can earn again
  - This subnet paid miners nothing and now pays. Worth a look before the field fills up.
- **`sn71:scoring_commit:2026-08-02T13:57:44Z`** - sn71 commit touches scoring: Bind verified auditor fallback workflow
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn89:scoring_commit:2026-08-02T14:22:11Z`** - sn89 commit touches scoring: hf scoreboard: publish each hotkeys own recent_calls
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn71:scoring_commit:2026-08-02T15:36:41Z`** - sn71 commit touches scoring: Verify candidate recovery against pre-signing receipt
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn76:scoring_commit:2026-08-02T15:40:23Z`** - sn76 commit touches scoring: Update scoring constants
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.

## STILL OPEN (already reported - do not re-alarm)

| event_id | netuid | class | first_seen_utc | one_line |
|---|---|---|---|---|
| `sn104:burn_drop:0.965` | 104 | BURN_DROP | 2026-07-28T07:30:22Z | sn104 burn fell 1.000 -> 0.965 - miners can earn again |
| `sn117:burn_drop:0.000` | 117 | BURN_DROP | 2026-07-28T10:44:07Z | sn117 burn fell 1.000 -> 0.000 - miners can earn again |
| `sn55:burn_drop:0.020` | 55 | BURN_DROP | 2026-07-28T16:58:29Z | sn55 burn fell 1.000 -> 0.020 - miners can earn again |
| `sn76:burn_drop:0.000` | 76 | BURN_DROP | 2026-07-28T18:40:29Z | sn76 burn fell 1.000 -> 0.000 - miners can earn again |
| `sn62:burn_drop:0.038` | 62 | BURN_DROP | 2026-07-28T20:08:41Z | sn62 burn fell 1.000 -> 0.038 - miners can earn again |
| `sn46:burn_drop:0.760` | 46 | BURN_DROP | 2026-07-28T22:44:37Z | sn46 burn fell 1.000 -> 0.760 - miners can earn again |
| `sn7:burn_drop:0.317` | 7 | BURN_DROP | 2026-07-29T07:34:26Z | sn7 burn fell 1.000 -> 0.317 - miners can earn again |
| `sn5:burn_drop:0.846` | 5 | BURN_DROP | 2026-07-30T07:10:45Z | sn5 burn fell 1.000 -> 0.846 - miners can earn again |
| `sn100:burn_drop:0.579` | 100 | BURN_DROP | 2026-07-30T07:10:45Z | sn100 burn fell 1.000 -> 0.579 - miners can earn again |
| `sn43:burn_drop:0.800` | 43 | BURN_DROP | 2026-07-30T09:58:45Z | sn43 burn fell 1.000 -> 0.800 - miners can earn again |
| `sn92:burn_drop:0.000` | 92 | BURN_DROP | 2026-07-30T12:02:23Z | sn92 burn fell 1.000 -> 0.000 - miners can earn again |
| `sn100:burn_drop:0.503` | 100 | BURN_DROP | 2026-07-30T14:28:38Z | sn100 burn fell 1.000 -> 0.503 - miners can earn again |
| `sn55:burn_drop:0.022` | 55 | BURN_DROP | 2026-07-30T17:57:00Z | sn55 burn fell 1.000 -> 0.022 - miners can earn again |
| `sn121:burn_drop:0.826` | 121 | BURN_DROP | 2026-07-30T17:57:00Z | sn121 burn fell 1.000 -> 0.826 - miners can earn again |
| `sn115:burn_drop:0.000` | 115 | BURN_DROP | 2026-07-30T23:33:07Z | sn115 burn fell 1.000 -> 0.000 - miners can earn again |
| `sn8:burn_drop:0.000` | 8 | BURN_DROP | 2026-07-31T11:05:37Z | sn8 burn fell 0.998 -> 0.000 - miners can earn again |
| `sn7:burn_drop:0.926` | 7 | BURN_DROP | 2026-07-31T17:12:35Z | sn7 burn fell 0.995 -> 0.926 - miners can earn again |
| `sn66:burn_drop:0.000` | 66 | BURN_DROP | 2026-07-31T17:12:35Z | sn66 burn fell 1.000 -> 0.000 - miners can earn again |
| `sn102:burn_drop:0.254` | 102 | BURN_DROP | 2026-08-01T07:17:44Z | sn102 burn fell 1.000 -> 0.254 - miners can earn again |
| `sn99:burn_drop:0.000` | 99 | BURN_DROP | 2026-08-01T17:45:57Z | sn99 burn fell 1.000 -> 0.000 - miners can earn again |
| `sn16:burn_drop:0.000` | 16 | BURN_DROP | 2026-08-02T07:40:06Z | sn16 burn fell 1.000 -> 0.000 - miners can earn again |
| `sn98:burn_drop:0.000` | 98 | BURN_DROP | 2026-08-02T12:34:55Z | sn98 burn fell 1.000 -> 0.000 - miners can earn again |
| `sn76:scoring_commit:2026-07-28T06:56:11Z` | 76 | SCORING_COMMIT | 2026-07-28T07:30:22Z | sn76 commit touches scoring: Skip tracks with no task set instead of abandoning the whole round |
| `sn85:scoring_commit:2026-07-28T07:19:51Z` | 85 | SCORING_COMMIT | 2026-07-28T07:30:22Z | sn85 commit touches scoring: defer scoring commit to DB (#180) |
| `sn76:scoring_commit:2026-07-28T08:08:04Z` | 76 | SCORING_COMMIT | 2026-07-28T08:08:26Z | sn76 commit touches scoring: Read served ground truth so findings are scored, not just verdicts |
| `sn67:scoring_commit:2026-07-28T09:37:00Z` | 67 | SCORING_COMMIT | 2026-07-28T10:44:07Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20260728.post5 |
| `sn76:scoring_commit:2026-07-28T11:28:42Z` | 76 | SCORING_COMMIT | 2026-07-28T11:29:26Z | sn76 commit touches scoring: Poll for validator image updates every two minutes |
| `sn71:scoring_commit:2026-07-28T12:00:19Z` | 71 | SCORING_COMMIT | 2026-07-28T12:10:04Z | sn71 commit touches scoring: Verify durable chain settlement readback |
| `sn89:scoring_commit:2026-07-28T12:59:01Z` | 89 | SCORING_COMMIT | 2026-07-28T12:59:29Z | sn89 commit touches scoring: hf scoreboard: publish n_submitters_3d |
| `sn28:release:v0.3.12` | 28 | RELEASE | 2026-07-28T15:04:08Z | sn28 released v0.3.12 |
| `sn56:scoring_commit:2026-07-28T14:55:22Z` | 56 | SCORING_COMMIT | 2026-07-28T15:04:08Z | sn56 commit touches scoring: feat(validator): auto-balance emission split from tournament particip… |
| `sn76:scoring_commit:2026-07-28T14:03:58Z` | 76 | SCORING_COMMIT | 2026-07-28T15:04:08Z | sn76 commit touches scoring: Retry validator self registration until it succeeds |
| `sn103:release:v2003: validator: restore miner burn fra` | 103 | RELEASE | 2026-07-28T15:04:08Z | sn103 released v2003: validator: restore miner burn fraction to 0.8 |
| `sn103:scoring_commit:2026-07-28T13:16:22Z` | 103 | SCORING_COMMIT | 2026-07-28T15:04:08Z | sn103 commit touches scoring: validator: restore miner burn fraction to 0.8 |
| `sn74:release:release-20260728-153232: chore(weights):` | 74 | RELEASE | 2026-07-28T16:58:29Z | sn74 released release-20260728-153232: chore(weights): zero metagraphed and loopover emission shares (#1663) |
| `sn76:scoring_commit:2026-07-28T16:00:07Z` | 76 | SCORING_COMMIT | 2026-07-28T16:58:29Z | sn76 commit touches scoring: Pay the reserved share in full from the first round and cap rewards a… |
| `sn102:release:v0.3.2` | 102 | RELEASE | 2026-07-28T16:58:29Z | sn102 released v0.3.2 |
| `sn102:scoring_commit:2026-07-24T20:54:05Z` | 102 | SCORING_COMMIT | 2026-07-28T16:58:29Z | sn102 commit touches scoring: 📊 telemetry: per-round baseline loss (validator_baseline_loss_by_round |
| `sn124:scoring_commit:2026-07-28T16:31:54Z` | 124 | SCORING_COMMIT | 2026-07-28T16:58:29Z | sn124 commit touches scoring: Start evaluation at the full worker width |
| `sn69:scoring_commit:2026-07-28T18:18:51Z` | 69 | SCORING_COMMIT | 2026-07-28T18:40:29Z | sn69 commit touches scoring: Add miner/validator operator guides + validator Docker fixes (#1) |
| `sn76:scoring_commit:2026-07-28T17:57:20Z` | 76 | SCORING_COMMIT | 2026-07-28T18:40:29Z | sn76 commit touches scoring: Stop counting unrunnable tasks as wrong answers, and say why a repeti… |
| `sn98:scoring_commit:2026-07-28T17:46:47Z` | 98 | SCORING_COMMIT | 2026-07-28T18:40:29Z | sn98 commit touches scoring: feat: auto-prune old validator round workspaces to bound disk use (#21 |
| `sn15:scoring_commit:2026-07-28T19:11:33Z` | 15 | SCORING_COMMIT | 2026-07-28T20:08:41Z | sn15 commit touches scoring: feat(validator): warn on startup when host is under min spec (ORO-174… |
| `sn76:scoring_commit:2026-07-28T18:43:46Z` | 76 | SCORING_COMMIT | 2026-07-28T20:08:41Z | sn76 commit touches scoring: Let the sandboxed agent write its workspace whatever uid the validato… |
| `sn100:scoring_commit:2026-07-28T20:25:29Z` | 100 | SCORING_COMMIT | 2026-07-28T21:37:49Z | sn100 commit touches scoring: feat(agent-challenge): NO_PHALA host pipeline with unattested weight … |
| `sn103:release:v2004: validator: default settle gate bu` | 103 | RELEASE | 2026-07-28T21:37:49Z | sn103 released v2004: validator: default settle gate budget to 1024 |
| `sn103:scoring_commit:2026-07-28T20:35:46Z` | 103 | SCORING_COMMIT | 2026-07-28T21:37:49Z | sn103 commit touches scoring: validator: default settle gate budget to 1024 |
| `sn13:scoring_commit:2026-07-27T16:11:26Z` | 13 | SCORING_COMMIT | 2026-07-28T22:44:37Z | sn13 commit touches scoring: fix(od): treat scraper ERRORS as "no evidence", not as miner failures |
| `sn56:scoring_commit:2026-07-28T22:18:44Z` | 56 | SCORING_COMMIT | 2026-07-28T22:44:37Z | sn56 commit touches scoring: fix(validator): read the dynamic emission split in performance endpoi… |
| `sn74:release:release-20260728-214235` | 74 | RELEASE | 2026-07-28T22:44:37Z | sn74 released release-20260728-214235 |
| `sn7:release:release-20260728-234943` | 7 | RELEASE | 2026-07-29T01:13:34Z | sn7 released release-20260728-234943 |
| `sn7:scoring_commit:2026-07-28T23:48:01Z` | 7 | SCORING_COMMIT | 2026-07-29T01:13:34Z | sn7 commit touches scoring: Verify TAO transfers by settlement rather than by the decoded call (#… |
| `sn67:scoring_commit:2026-07-28T14:27:25Z` | 67 | SCORING_COMMIT | 2026-07-29T01:13:34Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20260728.post9 |
| `sn100:scoring_commit:2026-07-29T00:37:31Z` | 100 | SCORING_COMMIT | 2026-07-29T01:13:34Z | sn100 commit touches scoring: feat(agent-challenge): remove Phala TEE product path (host-trust only… |
| `sn76:scoring_commit:2026-07-29T02:30:43Z` | 76 | SCORING_COMMIT | 2026-07-29T04:44:34Z | sn76 commit touches scoring: Create a writable state directory in the validator image |
| `sn100:scoring_commit:2026-07-29T02:56:56Z` | 100 | SCORING_COMMIT | 2026-07-29T04:44:34Z | sn100 commit touches scoring: fix(master): allowlist public FE agent-challenge reads on proxy |
| `sn101:scoring_commit:2026-07-29T03:26:19Z` | 101 | SCORING_COMMIT | 2026-07-29T04:44:34Z | sn101 commit touches scoring: Penalize incomplete tag submissions in miner score aggregation |
| `sn61:release:4.8.1` | 61 | RELEASE | 2026-07-29T07:34:26Z | sn61 released 4.8.1 |
| `sn71:scoring_commit:2026-07-29T07:01:02Z` | 71 | SCORING_COMMIT | 2026-07-29T07:34:26Z | sn71 commit touches scoring: Preserve live validator runtime during release prune |
| `sn100:scoring_commit:2026-07-29T06:48:23Z` | 100 | SCORING_COMMIT | 2026-07-29T07:34:26Z | sn100 commit touches scoring: fix(agent-challenge): copy golden digest into docker build context |
| `sn8:scoring_commit:2026-07-29T09:27:07Z` | 8 | SCORING_COMMIT | 2026-07-29T10:20:57Z | sn8 commit touches scoring: Full miner payouts (#862) |
| `sn51:scoring_commit:2026-07-29T08:36:45Z` | 51 | SCORING_COMMIT | 2026-07-29T10:20:57Z | sn51 commit touches scoring: DAH-2520, review fixes: guard the scoring cycle against a malformed s… |
| `sn53:scoring_commit:2026-07-29T08:32:57Z` | 53 | SCORING_COMMIT | 2026-07-29T10:20:57Z | sn53 commit touches scoring: Merge pull request #29 from hanlinai/docs/readme-miner-section |
| `sn100:scoring_commit:2026-07-29T10:11:17Z` | 100 | SCORING_COMMIT | 2026-07-29T10:20:57Z | sn100 commit touches scoring: fix(proxy+agent-challenge): unblock miner env routes and engage env g… |
| `sn71:scoring_commit:2026-07-29T09:31:54Z` | 71 | SCORING_COMMIT | 2026-07-29T12:28:47Z | sn71 commit touches scoring: Cap champion lifetime rewards |
| `sn93:scoring_commit:2026-07-29T10:29:48Z` | 93 | SCORING_COMMIT | 2026-07-29T12:28:47Z | sn93 commit touches scoring: feat: Double product placement reward payouts (#161) |
| `sn23:scoring_commit:2026-07-27T09:03:23Z` | 23 | SCORING_COMMIT | 2026-07-29T15:00:19Z | sn23 commit touches scoring: Add universal template support for miners (tri-check + CLI). |
| `sn51:scoring_commit:2026-07-29T14:53:39Z` | 51 | SCORING_COMMIT | 2026-07-29T15:00:19Z | sn51 commit touches scoring: DAH-2527, exclude idle filler ports from port verification and publis… |
| `sn67:scoring_commit:2026-07-29T09:00:51Z` | 67 | SCORING_COMMIT | 2026-07-29T15:00:19Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20260729.post3 |
| `sn93:scoring_commit:2026-07-29T14:43:46Z` | 93 | SCORING_COMMIT | 2026-07-29T15:00:19Z | sn93 commit touches scoring: fix: deploy workflows not updating ECS service to new task definition… |
| `sn100:scoring_commit:2026-07-29T13:14:35Z` | 100 | SCORING_COMMIT | 2026-07-29T15:00:19Z | sn100 commit touches scoring: fix(agent-challenge): allow PyPI index for agent dependency install |
| `sn9:release:v4.9.1` | 9 | RELEASE | 2026-07-29T16:38:26Z | sn9 released v4.9.1 |
| `sn15:release:v1.2.2` | 15 | RELEASE | 2026-07-29T16:38:26Z | sn15 released v1.2.2 |
| `sn53:scoring_commit:2026-07-29T16:37:29Z` | 53 | SCORING_COMMIT | 2026-07-29T16:38:26Z | sn53 commit touches scoring: Merge pull request #30 from hanlinai/docs/miner-tool-call-parser |
| `sn124:scoring_commit:2026-07-29T09:25:10Z` | 124 | SCORING_COMMIT | 2026-07-29T16:38:26Z | sn124 commit touches scoring: Raise validator action compute budget |
| `sn7:release:release-20260729-181714` | 7 | RELEASE | 2026-07-29T19:39:57Z | sn7 released release-20260729-181714 |
| `sn7:scoring_commit:2026-07-29T18:16:30Z` | 7 | SCORING_COMMIT | 2026-07-29T19:39:57Z | sn7 commit touches scoring: Add BURN_RATE with pools scaled to the miner share (#607) |
| `sn66:scoring_commit:2026-07-29T18:25:12Z` | 66 | SCORING_COMMIT | 2026-07-29T19:39:57Z | sn66 commit touches scoring: Introduce tiered solver task pool |
| `sn74:release:release-20260729-181654` | 74 | RELEASE | 2026-07-29T19:39:57Z | sn74 released release-20260729-181654 |
| `sn100:scoring_commit:2026-07-29T19:04:37Z` | 100 | SCORING_COMMIT | 2026-07-29T19:39:57Z | sn100 commit touches scoring: fix(agent-challenge): supply LLM_MODEL to the evaluated agent |
| `sn103:release:v2006: validator: start signer balance g` | 103 | RELEASE | 2026-07-29T19:39:57Z | sn103 released v2006: validator: start signer balance gauge at the unknown sentinel |
| `sn103:scoring_commit:2026-07-29T19:27:15Z` | 103 | SCORING_COMMIT | 2026-07-29T19:39:57Z | sn103 commit touches scoring: validator: start signer balance gauge at the unknown sentinel |
| `sn100:scoring_commit:2026-07-29T22:07:42Z` | 100 | SCORING_COMMIT | 2026-07-29T22:43:24Z | sn100 commit touches scoring: fix(agent-challenge): make Terminal-Bench failures visible and stop w… |
| `sn111:scoring_commit:2026-07-29T22:01:10Z` | 111 | SCORING_COMMIT | 2026-07-29T22:43:24Z | sn111 commit touches scoring: Add tests for agent v1 Silver scoring |
| `sn15:release:v1.2.3` | 15 | RELEASE | 2026-07-30T07:10:45Z | sn15 released v1.2.3 |
| `sn71:scoring_commit:2026-07-30T04:15:15Z` | 71 | SCORING_COMMIT | 2026-07-30T07:10:45Z | sn71 commit touches scoring: Parallelize safe validator restart preparation |
| `sn76:scoring_commit:2026-07-30T05:52:31Z` | 76 | SCORING_COMMIT | 2026-07-30T07:10:45Z | sn76 commit touches scoring: Evaluate the smaller tracks before skills so a long skills pass canno… |
| `sn107:scoring_commit:2026-07-30T06:35:32Z` | 107 | SCORING_COMMIT | 2026-07-30T07:10:45Z | sn107 commit touches scoring: Fix stale reward split: winner 90% / burn 0% / dust top-20 |
| `sn28:release:v0.3.14` | 28 | RELEASE | 2026-07-30T09:58:45Z | sn28 released v0.3.14 |
| `sn38:scoring_commit:2026-07-30T09:09:57Z` | 38 | SCORING_COMMIT | 2026-07-30T09:58:45Z | sn38 commit touches scoring: Add custom architecture registry for miners (#18) |
| `sn51:scoring_commit:2026-07-30T09:35:22Z` | 51 | SCORING_COMMIT | 2026-07-30T09:58:45Z | sn51 commit touches scoring: DAH-2340, publish structured zero-incentive reasons on MACHINE_SPEC_C… |
| `sn71:scoring_commit:2026-07-30T05:32:52Z` | 71 | SCORING_COMMIT | 2026-07-30T09:58:45Z | sn71 commit touches scoring: Keep validator epoch authority fresh during submission |
| `sn67:scoring_commit:2026-07-30T08:55:17Z` | 67 | SCORING_COMMIT | 2026-07-30T12:02:23Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20260730.post1 |
| `sn97:scoring_commit:2026-07-29T19:09:30Z` | 97 | SCORING_COMMIT | 2026-07-30T12:02:23Z | sn97 commit touches scoring: update: Updated evaluator & judge prompts |
| `sn51:scoring_commit:2026-07-30T14:18:11Z` | 51 | SCORING_COMMIT | 2026-07-30T14:28:38Z | sn51 commit touches scoring: feat: DAH-2251 — pay referral incentive from residual burn, split acr… |
| `sn74:release:release-20260730-140609` | 74 | RELEASE | 2026-07-30T14:28:38Z | sn74 released release-20260730-140609 |
| `sn49:scoring_commit:2026-07-30T15:52:08Z` | 49 | SCORING_COMMIT | 2026-07-30T16:17:33Z | sn49 commit touches scoring: Updated Discord link across documentation to new invite. |
| `sn71:scoring_commit:2026-07-30T14:08:31Z` | 71 | SCORING_COMMIT | 2026-07-30T16:17:33Z | sn71 commit touches scoring: Verify no-burn fallback allocation inputs |
| `sn98:scoring_commit:2026-07-30T15:31:29Z` | 98 | SCORING_COMMIT | 2026-07-30T16:17:33Z | sn98 commit touches scoring: fix(miner-cli): add log for hotkey ban (#22) |
| `sn89:scoring_commit:2026-07-30T17:06:44Z` | 89 | SCORING_COMMIT | 2026-07-30T17:57:00Z | sn89 commit touches scoring: hf board: share of the MINER pool, not of the vector; plus LF-parity … |
| `sn28:release:v0.3.15` | 28 | RELEASE | 2026-07-30T19:47:43Z | sn28 released v0.3.15 |
| `sn14:scoring_commit:2026-07-27T16:11:45Z` | 14 | SCORING_COMMIT | 2026-07-30T22:16:59Z | sn14 commit touches scoring: Add object-store proposal transport and validator recovery |
| `sn8:scoring_commit:2026-07-30T22:26:28Z` | 8 | SCORING_COMMIT | 2026-07-30T23:33:07Z | sn8 commit touches scoring: create subaccount elimination cache on entity miner (#861) |
| `sn62:release:v0.2.3` | 62 | RELEASE | 2026-07-30T23:33:07Z | sn62 released v0.2.3 |
| `sn124:scoring_commit:2026-07-30T21:28:44Z` | 124 | SCORING_COMMIT | 2026-07-30T23:33:07Z | sn124 commit touches scoring: Kill host workers when the validator process dies |
| `sn80:scoring_commit:2026-07-31T05:39:39Z` | 80 | SCORING_COMMIT | 2026-07-31T08:08:30Z | sn80 commit touches scoring: docs: document public /api/v1/scan-rejections endpoint (miner self-se… |
| `sn76:scoring_commit:2026-07-31T11:00:01Z` | 76 | SCORING_COMMIT | 2026-07-31T11:05:37Z | sn76 commit touches scoring: Evaluate two agents at a time within a track |
| `sn76:scoring_commit:2026-07-31T12:40:54Z` | 76 | SCORING_COMMIT | 2026-07-31T13:05:28Z | sn76 commit touches scoring: Hold inference keys in the proxy, enforce per task budgets, and refus… |
| `sn126:scoring_commit:2026-07-31T15:20:36Z` | 126 | SCORING_COMMIT | 2026-07-31T15:28:47Z | sn126 commit touches scoring: docs: align miner and validator release guides |
| `sn9:release:v4.9.2` | 9 | RELEASE | 2026-07-31T17:12:35Z | sn9 released v4.9.2 |
| `sn15:release:v1.2.4` | 15 | RELEASE | 2026-07-31T17:12:35Z | sn15 released v1.2.4 |
| `sn101:scoring_commit:2026-07-31T16:39:07Z` | 101 | SCORING_COMMIT | 2026-07-31T17:12:35Z | sn101 commit touches scoring: Allocate 90% of validator weight to burn UID |
| `sn102:release:v0.3.4` | 102 | RELEASE | 2026-07-31T17:12:35Z | sn102 released v0.3.4 |
| `sn126:scoring_commit:2026-07-31T17:01:33Z` | 126 | SCORING_COMMIT | 2026-07-31T17:12:35Z | sn126 commit touches scoring: fix: protect validator dashboard outbox |
| `sn126:scoring_commit:2026-07-31T17:23:08Z` | 126 | SCORING_COMMIT | 2026-07-31T18:52:56Z | sn126 commit touches scoring: release: enable validator auto-update 0.2.1 |
| `sn74:release:release-20260731-214128: chore(weights):` | 74 | RELEASE | 2026-07-31T21:50:00Z | sn74 released release-20260731-214128: chore(weights): point all emissions at sparkinfer-k3 (#1675) |
| `sn74:scoring_commit:2026-07-31T15:04:46Z` | 74 | SCORING_COMMIT | 2026-07-31T21:50:00Z | sn74 commit touches scoring: SparkDistill: 3x faster time-decay for merged-PR scores (#1673) |
| `sn76:scoring_commit:2026-07-31T21:43:47Z` | 76 | SCORING_COMMIT | 2026-07-31T21:50:00Z | sn76 commit touches scoring: Merge pull request #16 from praxi-labs/validator-round-changes |
| `sn102:release:v0.4.0` | 102 | RELEASE | 2026-07-31T23:14:36Z | sn102 released v0.4.0 |
| `sn102:scoring_commit:2026-07-31T18:12:56Z` | 102 | SCORING_COMMIT | 2026-07-31T23:14:36Z | sn102 commit touches scoring: 📊 telemetry: restore round + per-miner telemetry on every recovery (s… |
| `sn71:scoring_commit:2026-07-31T23:59:50Z` | 71 | SCORING_COMMIT | 2026-08-01T01:02:18Z | sn71 commit touches scoring: Bound receipt ancestry validation and persistence retries |
| `sn71:scoring_commit:2026-08-01T03:43:59Z` | 71 | SCORING_COMMIT | 2026-08-01T04:31:25Z | sn71 commit touches scoring: Extend validator gateway alignment wait |
| `sn76:scoring_commit:2026-08-01T05:18:26Z` | 76 | SCORING_COMMIT | 2026-08-01T07:17:44Z | sn76 commit touches scoring: Carry a track's standing forward when a pass does not evaluate it |
| `sn61:release:4.8.2` | 61 | RELEASE | 2026-08-01T09:32:34Z | sn61 released 4.8.2 |
| `sn61:scoring_commit:2026-08-01T09:26:58Z` | 61 | SCORING_COMMIT | 2026-08-01T09:32:34Z | sn61 commit touches scoring: fix: set default value for user_id in _compare_same_score_outputs meth |
| `sn67:scoring_commit:2026-08-01T08:06:19Z` | 67 | SCORING_COMMIT | 2026-08-01T09:32:34Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20260801.post0 |
| `sn71:scoring_commit:2026-08-01T07:04:04Z` | 71 | SCORING_COMMIT | 2026-08-01T09:32:34Z | sn71 commit touches scoring: Validate concurrent restart state continuity |
| `sn126:scoring_commit:2026-08-01T08:32:23Z` | 126 | SCORING_COMMIT | 2026-08-01T09:32:34Z | sn126 commit touches scoring: docs: introduce Poker44 evaluation network |
| `sn71:scoring_commit:2026-08-01T08:57:49Z` | 71 | SCORING_COMMIT | 2026-08-01T11:07:26Z | sn71 commit touches scoring: Bind v8 artifact verification into protected manifest |
| `sn103:release:v2007` | 103 | RELEASE | 2026-08-01T12:13:22Z | sn103 released v2007 |
| `sn103:scoring_commit:2026-08-01T11:36:54Z` | 103 | SCORING_COMMIT | 2026-08-01T12:13:22Z | sn103 commit touches scoring: validator: release v2007 |
| `sn124:scoring_commit:2026-08-01T12:57:13Z` | 124 | SCORING_COMMIT | 2026-08-01T14:06:15Z | sn124 commit touches scoring: Fly next-epoch seeds for pre-evaluation and switch to 14-day epochs |
| `sn111:scoring_commit:2026-08-01T16:22:29Z` | 111 | SCORING_COMMIT | 2026-08-01T16:29:18Z | sn111 commit touches scoring: Wire silver adjudication into validator scoring |
| `sn71:scoring_commit:2026-08-01T18:51:00Z` | 71 | SCORING_COMMIT | 2026-08-01T20:01:00Z | sn71 commit touches scoring: Refresh validator ancestry workflow manifest |
| `sn71:scoring_commit:2026-08-01T20:24:52Z` | 71 | SCORING_COMMIT | 2026-08-01T21:07:37Z | sn71 commit touches scoring: Fix baseline replay and compact weight validation |
| `sn111:scoring_commit:2026-08-01T20:30:47Z` | 111 | SCORING_COMMIT | 2026-08-01T21:07:37Z | sn111 commit touches scoring: Wire production Silver run metadata into validator |
| `sn71:scoring_commit:2026-08-01T21:02:08Z` | 71 | SCORING_COMMIT | 2026-08-01T23:28:58Z | sn71 commit touches scoring: Protect validator settlement constants |
| `sn71:scoring_commit:2026-08-02T00:47:38Z` | 71 | SCORING_COMMIT | 2026-08-02T01:17:45Z | sn71 commit touches scoring: Recycle scoring workers at baseline checkpoints |
| `sn97:scoring_commit:2026-07-31T11:22:32Z` | 97 | SCORING_COMMIT | 2026-08-02T01:17:45Z | sn97 commit touches scoring: feat: Added display overall score + margin on main page |
| `sn61:release:4.8.3` | 61 | RELEASE | 2026-08-02T04:52:47Z | sn61 released 4.8.3 |
| `sn61:scoring_commit:2026-08-02T02:01:13Z` | 61 | SCORING_COMMIT | 2026-08-02T04:52:47Z | sn61 commit touches scoring: fix: set default user_id in _compare_same_score_outputs method |
| `sn71:scoring_commit:2026-08-02T03:44:52Z` | 71 | SCORING_COMMIT | 2026-08-02T04:52:47Z | sn71 commit touches scoring: Preserve scoring state across gateway restart |
| `sn76:scoring_commit:2026-08-02T03:28:23Z` | 76 | SCORING_COMMIT | 2026-08-02T04:52:47Z | sn76 commit touches scoring: Harden scoring inputs and screening |
| `sn67:scoring_commit:2026-08-02T05:04:42Z` | 67 | SCORING_COMMIT | 2026-08-02T07:40:06Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20260802.post0 |
| `sn71:scoring_commit:2026-08-02T09:35:46Z` | 71 | SCORING_COMMIT | 2026-08-02T09:46:10Z | sn71 commit touches scoring: Validate compact finalized weight ancestry |
| `sn11:scoring_commit:2026-08-02T10:05:07Z` | 11 | SCORING_COMMIT | 2026-08-02T11:08:46Z | sn11 commit touches scoring: docs(incentive): takeover bar decays to a -3% terminal handicap |
| `sn71:scoring_commit:2026-08-02T09:58:33Z` | 71 | SCORING_COMMIT | 2026-08-02T11:08:46Z | sn71 commit touches scoring: Delay candidate imports until verifier startup |
| `sn103:release:v2008` | 103 | RELEASE | 2026-08-02T12:34:55Z | sn103 released v2008 |
| `sn103:scoring_commit:2026-08-02T11:23:08Z` | 103 | SCORING_COMMIT | 2026-08-02T12:34:55Z | sn103 commit touches scoring: validator: release v2008 |
| `sn67:readme_task_diff:b615b92c78ccda43` | 67 | README_TASK_DIFF | 2026-07-28T10:44:07Z | sn67 README task/scoring sections changed |
| `sn67:readme_task_diff:2c3937a290a2972c` | 67 | README_TASK_DIFF | 2026-07-29T01:13:34Z | sn67 README task/scoring sections changed |
| `sn23:readme_task_diff:f1596712006feba5` | 23 | README_TASK_DIFF | 2026-07-29T15:00:19Z | sn23 README task/scoring sections changed |
| `sn67:readme_task_diff:214039ad4d05eaac` | 67 | README_TASK_DIFF | 2026-07-29T15:00:19Z | sn67 README task/scoring sections changed |
| `sn6:readme_task_diff:b7a9d9192013aa91` | 6 | README_TASK_DIFF | 2026-07-29T19:39:57Z | sn6 README task/scoring sections changed |
| `sn66:readme_task_diff:93fd61d3541878a9` | 66 | README_TASK_DIFF | 2026-07-29T19:39:57Z | sn66 README task/scoring sections changed |
| `sn26:readme_task_diff:b7cabe77688b0c40` | 26 | README_TASK_DIFF | 2026-07-30T04:18:19Z | sn26 README task/scoring sections changed |
| `sn80:readme_task_diff:524075fdda445069` | 80 | README_TASK_DIFF | 2026-07-30T07:10:45Z | sn80 README task/scoring sections changed |
| `sn107:readme_task_diff:ae5ae44af5a81eba` | 107 | README_TASK_DIFF | 2026-07-30T07:10:45Z | sn107 README task/scoring sections changed |
| `sn26:readme_task_diff:b5ae57c5d606b138` | 26 | README_TASK_DIFF | 2026-07-30T16:17:33Z | sn26 README task/scoring sections changed |
| `sn89:readme_task_diff:2ad9289f8c86f6ec` | 89 | README_TASK_DIFF | 2026-08-01T04:31:25Z | sn89 README task/scoring sections changed |
| `sn111:readme_task_diff:39d25fdcdedf56c8` | 111 | README_TASK_DIFF | 2026-08-02T04:52:47Z | sn111 README task/scoring sections changed |

## RESOLVED IN THIS WINDOW

_none_
