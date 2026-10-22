# ALARMS - generated 2026-10-22T18:06:02Z, block 9340731

window: first_seen in [2026-10-22T16:51:27Z, 2026-10-22T18:06:27Z)  (60 min interval + 15 min overlap)

Report ONLY the rows under NEW SINCE LAST RUN. Rows under STILL OPEN were
already reported in an earlier window and must not be re-alarmed.

## NEW SINCE LAST RUN

| event_id | netuid | class | severity | first_seen_utc | one_line |
|---|---|---|---|---|---|
| `sn1:release:v4.4.15` | 1 | RELEASE | P1 | 2026-10-22T18:06:27Z | sn1 released v4.4.15 |
| `sn12:release:miner-staging-2026-10-22-39790980356-423` | 12 | RELEASE | P1 | 2026-10-22T18:06:27Z | sn12 released miner-staging-2026-10-22-39790980356-423-1: fix: security fixes |
| `sn15:release:v3.0.0` | 15 | RELEASE | P1 | 2026-10-22T18:06:27Z | sn15 released v3.0.0 |
| `sn21:scoring_commit:2026-10-22T10:49:09Z` | 21 | SCORING_COMMIT | P1 | 2026-10-22T18:06:27Z | sn21 commit touches scoring: fix(scoring): the outcomes reader keeps expected and actual conversio… |
| `sn25:release:v2026.10.22-1078873780` | 25 | RELEASE | P1 | 2026-10-22T18:06:27Z | sn25 released v2026.10.22-1078873780 |
| `sn51:release:executor-v1.151` | 51 | RELEASE | P1 | 2026-10-22T18:06:27Z | sn51 released executor-v1.151 |
| `sn51:scoring_commit:2026-10-22T15:42:26Z` | 51 | SCORING_COMMIT | P1 | 2026-10-22T18:06:27Z | sn51 commit touches scoring: DAH-4983 - Validator: a failed edit's undo repairs a stale volume mou… |
| `sn76:release:v0.0.3` | 76 | RELEASE | P1 | 2026-10-22T18:06:27Z | sn76 released v0.0.3 |
| `sn76:scoring_commit:2026-10-22T14:48:07Z` | 76 | SCORING_COMMIT | P1 | 2026-10-22T18:06:27Z | sn76 commit touches scoring: Allow manual CI verification after repository recovery (#15) |
| `sn81:scoring_commit:2026-10-22T14:26:47Z` | 81 | SCORING_COMMIT | P1 | 2026-10-22T18:06:27Z | sn81 commit touches scoring: Merge pull request #387: evaluation feed destination safeguards |
| `sn117:release:everycli v0.7.1` | 117 | RELEASE | P1 | 2026-10-22T18:06:27Z | sn117 released everycli v0.7.1 |
| `sn6:readme_task_diff:f71150d0a859d726` | 6 | README_TASK_DIFF | P2 | 2026-10-22T18:06:27Z | sn6 README task/scoring sections changed |
| `sn76:readme_task_diff:f81741e228d9d939` | 76 | README_TASK_DIFF | P2 | 2026-10-22T18:06:27Z | sn76 README task/scoring sections changed |
| `sn117:readme_task_diff:61eefa3e188bb2fb` | 117 | README_TASK_DIFF | P2 | 2026-10-22T18:06:27Z | sn117 README task/scoring sections changed |

### detail

- **`sn1:release:v4.4.15`** - sn1 released v4.4.15
  - published 2026-10-22T17:36:12Z (was v4.4.14)
- **`sn12:release:miner-staging-2026-10-22-39790980356-423`** - sn12 released miner-staging-2026-10-22-39790980356-423-1: fix: security fixes
  - published 2026-10-22T13:53:56Z (was validator-staging-2026-09-18-35368036673-626-1: fix: evict old neurons in allowance evict_old_data task)
- **`sn15:release:v3.0.0`** - sn15 released v3.0.0
  - published 2026-10-22T08:44:01Z (was v2.5.6: Bound per-evaluation sandbox disk use)
- **`sn21:scoring_commit:2026-10-22T10:49:09Z`** - sn21 commit touches scoring: fix(scoring): the outcomes reader keeps expected and actual conversio…
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn25:release:v2026.10.22-1078873780`** - sn25 released v2026.10.22-1078873780
  - published 2026-10-22T16:52:44Z (was v2026.10.21-1078274420)
- **`sn51:release:executor-v1.151`** - sn51 released executor-v1.151
  - published 2026-10-22T17:08:36Z (was miner-v1.009)
- **`sn51:scoring_commit:2026-10-22T15:42:26Z`** - sn51 commit touches scoring: DAH-4983 - Validator: a failed edit's undo repairs a stale volume mou…
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn76:release:v0.0.3`** - sn76 released v0.0.3
  - published 2026-10-22T14:36:27Z (was v0.0.3: Merge pull request #45 from heroncovelabs/fix/recover-public-work-packet)
- **`sn76:scoring_commit:2026-10-22T14:48:07Z`** - sn76 commit touches scoring: Allow manual CI verification after repository recovery (#15)
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn81:scoring_commit:2026-10-22T14:26:47Z`** - sn81 commit touches scoring: Merge pull request #387: evaluation feed destination safeguards
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn117:release:everycli v0.7.1`** - sn117 released everycli v0.7.1
  - published 2026-10-22T14:46:09Z (was everycli v0.7.0)
- **`sn6:readme_task_diff:f71150d0a859d726`** - sn6 README task/scoring sections changed
  - Only the task-describing headings are hashed, so badge and typo edits do not trigger this.
- **`sn76:readme_task_diff:f81741e228d9d939`** - sn76 README task/scoring sections changed
  - Only the task-describing headings are hashed, so badge and typo edits do not trigger this.
- **`sn117:readme_task_diff:61eefa3e188bb2fb`** - sn117 README task/scoring sections changed
  - Only the task-describing headings are hashed, so badge and typo edits do not trigger this.

## STILL OPEN (already reported - do not re-alarm)

| event_id | netuid | class | first_seen_utc | one_line |
|---|---|---|---|---|
| `sn76:burn_drop:0.979` | 76 | BURN_DROP | 2026-10-15T19:27:45Z | sn76 burn fell 1.000 -> 0.979 - miners can earn again |
| `sn122:burn_drop:0.727` | 122 | BURN_DROP | 2026-10-15T19:27:45Z | sn122 burn fell 1.000 -> 0.727 - miners can earn again |
| `sn37:burn_drop:0.713` | 37 | BURN_DROP | 2026-10-16T10:10:43Z | sn37 burn fell 1.000 -> 0.713 - miners can earn again |
| `sn76:burn_drop:0.961` | 76 | BURN_DROP | 2026-10-16T10:10:43Z | sn76 burn fell 0.999 -> 0.961 - miners can earn again |
| `sn100:burn_drop:0.705` | 100 | BURN_DROP | 2026-10-16T18:46:43Z | sn100 burn fell 1.000 -> 0.705 - miners can earn again |
| `sn97:burn_drop:0.600` | 97 | BURN_DROP | 2026-10-16T21:47:16Z | sn97 burn fell 1.000 -> 0.600 - miners can earn again |
| `sn120:mechanism_added:1to2` | 120 | MECHANISM_ADDED | 2026-10-17T08:43:24Z | sn120 now runs 2 incentive mechanisms (was 1) |
| `sn55:burn_drop:0.010` | 55 | BURN_DROP | 2026-10-18T10:56:59Z | sn55 burn fell 1.000 -> 0.010 - miners can earn again |
| `sn122:burn_drop:0.700` | 122 | BURN_DROP | 2026-10-19T10:42:29Z | sn122 burn fell 1.000 -> 0.700 - miners can earn again |
| `sn7:burn_drop:0.505` | 7 | BURN_DROP | 2026-10-19T21:39:26Z | sn7 burn fell 1.000 -> 0.505 - miners can earn again |
| `sn76:burn_drop:0.989` | 76 | BURN_DROP | 2026-10-20T00:43:32Z | sn76 burn fell 1.000 -> 0.989 - miners can earn again |
| `sn117:burn_drop:0.884` | 117 | BURN_DROP | 2026-10-20T00:43:32Z | sn117 burn fell 1.000 -> 0.884 - miners can earn again |
| `sn48:burn_drop:0.000` | 48 | BURN_DROP | 2026-10-20T19:28:18Z | sn48 burn fell 1.000 -> 0.000 - miners can earn again |
| `sn120:burn_drop:0.100` | 120 | BURN_DROP | 2026-10-21T01:02:40Z | sn120 burn fell 1.000 -> 0.100 - miners can earn again |
| `sn30:burn_drop:0.981` | 30 | BURN_DROP | 2026-10-21T20:17:01Z | sn30 burn fell 0.996 -> 0.981 - miners can earn again |
| `sn37:burn_drop:0.711` | 37 | BURN_DROP | 2026-10-21T20:17:01Z | sn37 burn fell 1.000 -> 0.711 - miners can earn again |
| `sn117:burn_drop:0.883` | 117 | BURN_DROP | 2026-10-21T20:17:01Z | sn117 burn fell 1.000 -> 0.883 - miners can earn again |
| `sn10:burn_drop:0.571` | 10 | BURN_DROP | 2026-10-21T23:30:35Z | sn10 burn fell 1.000 -> 0.571 - miners can earn again |
| `sn71:burn_drop:0.700` | 71 | BURN_DROP | 2026-10-21T23:30:35Z | sn71 burn fell 1.000 -> 0.700 - miners can earn again |
| `sn7:release:release-20261015-164605: Gate quotes and` | 7 | RELEASE | 2026-10-15T19:27:45Z | sn7 released release-20261015-164605: Gate quotes and crown reconcile on the offer's own backing bit (#772) |
| `sn9:release:v4.13.7` | 9 | RELEASE | 2026-10-15T19:27:45Z | sn9 released v4.13.7 |
| `sn15:release:v2.5.3` | 15 | RELEASE | 2026-10-15T19:27:45Z | sn15 released v2.5.3 |
| `sn25:scoring_commit:2026-10-15T16:11:13Z` | 25 | SCORING_COMMIT | 2026-10-15T19:27:45Z | sn25 commit touches scoring: Merge test/validator-crash-loop-root-cause into main |
| `sn28:release:v0.5.1-dev` | 28 | RELEASE | 2026-10-15T19:27:45Z | sn28 released v0.5.1-dev |
| `sn51:release:executor-v1.141` | 51 | RELEASE | 2026-10-15T19:27:45Z | sn51 released executor-v1.141 |
| `sn51:scoring_commit:2026-10-15T17:07:10Z` | 51 | SCORING_COMMIT | 2026-10-15T19:27:45Z | sn51 commit touches scoring: DAH-4465 validator: fail an unrented node whose busy GPU is thermally… |
| `sn78:scoring_commit:2026-10-15T19:16:31Z` | 78 | SCORING_COMMIT | 2026-10-15T19:27:45Z | sn78 commit touches scoring: Reuse verified host and OCI identities during worker reconciliation |
| `sn92:release:v1.2.0-rc3` | 92 | RELEASE | 2026-10-15T19:27:45Z | sn92 released v1.2.0-rc3 |
| `sn92:scoring_commit:2026-10-15T15:10:01Z` | 92 | SCORING_COMMIT | 2026-10-15T19:27:45Z | sn92 commit touches scoring: tiers: keep the per-miner tier-order rule (H3); s1-lite / s1-cpu max_… |
| `sn116:release:Carbon worker images v4` | 116 | RELEASE | 2026-10-15T19:27:45Z | sn116 released Carbon worker images v4 |
| `sn116:scoring_commit:2026-10-15T19:09:06Z` | 116 | SCORING_COMMIT | 2026-10-15T19:27:45Z | sn116 commit touches scoring: Merge pull request #1383 from carbonphysicsai/codex/scorelab-v3-calib… |
| `sn7:release:release-20261015-220818: Quote the min f` | 7 | RELEASE | 2026-10-15T22:39:09Z | sn7 released release-20261015-220818: Quote the min for alpha pairs from each candidate's floor (#775) |
| `sn7:scoring_commit:2026-10-15T21:59:48Z` | 7 | SCORING_COMMIT | 2026-10-15T22:39:09Z | sn7 commit touches scoring: Quote /rate from held miner states and a lazy market memo (#774) |
| `sn25:release:v2026.10.15-1072937160` | 25 | RELEASE | 2026-10-15T22:39:09Z | sn25 released v2026.10.15-1072937160 |
| `sn71:scoring_commit:2026-10-15T20:53:09Z` | 71 | SCORING_COMMIT | 2026-10-15T22:39:09Z | sn71 commit touches scoring: Fix Arena progression lock order and close legacy scoring RPC access |
| `sn78:scoring_commit:2026-10-15T19:35:00Z` | 78 | SCORING_COMMIT | 2026-10-15T22:39:09Z | sn78 commit touches scoring: Overlap retained history loading with bounded native verification |
| `sn92:release:v1.2.0-rc4` | 92 | RELEASE | 2026-10-15T22:39:09Z | sn92 released v1.2.0-rc4 |
| `sn92:scoring_commit:2026-10-15T19:21:22Z` | 92 | SCORING_COMMIT | 2026-10-15T22:39:09Z | sn92 commit touches scoring: probe: open each UID's window at the validator's first send to it; la… |
| `sn116:scoring_commit:2026-10-15T20:45:43Z` | 116 | SCORING_COMMIT | 2026-10-15T22:39:09Z | sn116 commit touches scoring: Verify persisted contract record through submission guards |
| `sn117:release:everycli v0.5.7` | 117 | RELEASE | 2026-10-15T22:39:09Z | sn117 released everycli v0.5.7 |
| `sn25:release:v2026.10.15-1073082520` | 25 | RELEASE | 2026-10-16T00:49:24Z | sn25 released v2026.10.15-1073082520 |
| `sn37:scoring_commit:2026-10-16T00:31:00Z` | 37 | SCORING_COMMIT | 2026-10-16T00:49:24Z | sn37 commit touches scoring: fix(miner): support reviewed mainnet runtime479 (#30) |
| `sn116:scoring_commit:2026-10-16T00:40:42Z` | 116 | SCORING_COMMIT | 2026-10-16T00:49:24Z | sn116 commit touches scoring: Merge pull request #1393 from carbonphysicsai/codex/scorelab-guarded4… |
| `sn25:release:v2026.10.15-1073121200` | 25 | RELEASE | 2026-10-16T05:47:49Z | sn25 released v2026.10.15-1073121200 |
| `sn51:scoring_commit:2026-10-16T02:57:37Z` | 51 | SCORING_COMMIT | 2026-10-16T05:47:49Z | sn51 commit touches scoring: DAH-3980 - Validator: new loopback volumes on a v2 plugin installed b… |
| `sn71:scoring_commit:2026-10-16T04:40:16Z` | 71 | SCORING_COMMIT | 2026-10-16T05:47:49Z | sn71 commit touches scoring: Verify failed fallback stays an infrastructure error |
| `sn78:scoring_commit:2026-10-16T03:44:01Z` | 78 | SCORING_COMMIT | 2026-10-16T05:47:49Z | sn78 commit touches scoring: Reuse verified semantics for authenticated sealed package copies |
| `sn81:scoring_commit:2026-10-15T10:03:46Z` | 81 | SCORING_COMMIT | 2026-10-16T05:47:49Z | sn81 commit touches scoring: fix(corpus): serve signed jobs from the split validator's front |
| `sn91:scoring_commit:2026-10-16T02:59:40Z` | 91 | SCORING_COMMIT | 2026-10-16T05:47:49Z | sn91 commit touches scoring: Pin the best-bench round in the receipt index so the scoreboard's bes… |
| `sn94:scoring_commit:2026-10-16T03:19:42Z` | 94 | SCORING_COMMIT | 2026-10-16T05:47:49Z | sn94 commit touches scoring: Merge pull request #281 from cathedralai/docs/sn94-snp-miner-dd7182c |
| `sn116:scoring_commit:2026-10-16T04:42:09Z` | 116 | SCORING_COMMIT | 2026-10-16T05:47:49Z | sn116 commit touches scoring: Merge pull request #1401 from carbonphysicsai/codex/scorelab-guard419… |
| `sn51:scoring_commit:2026-10-16T06:29:35Z` | 51 | SCORING_COMMIT | 2026-10-16T10:10:43Z | sn51 commit touches scoring: DAH-4362 - [P3] Validator: remove settings unchanged for more than 3 … |
| `sn71:scoring_commit:2026-10-16T09:32:28Z` | 71 | SCORING_COMMIT | 2026-10-16T10:10:43Z | sn71 commit touches scoring: Merge pull request #489 from leadpoet/fix/validator-run-recovery-scop… |
| `sn78:scoring_commit:2026-10-16T04:36:39Z` | 78 | SCORING_COMMIT | 2026-10-16T10:10:43Z | sn78 commit touches scoring: Add read-only retained miner revision preflight |
| `sn116:scoring_commit:2026-10-16T07:49:42Z` | 116 | SCORING_COMMIT | 2026-10-16T10:10:43Z | sn116 commit touches scoring: Merge pull request #1404 from carbonphysicsai/codex/scorelab-guarded4… |
| `sn1:release:v4.4.13` | 1 | RELEASE | 2026-10-16T14:58:20Z | sn1 released v4.4.13 |
| `sn21:scoring_commit:2026-10-16T12:06:08Z` | 21 | SCORING_COMMIT | 2026-10-16T14:58:20Z | sn21 commit touches scoring: scoring: an entry without a measurable efficiency is scored on cost a… |
| `sn51:scoring_commit:2026-10-16T14:00:51Z` | 51 | SCORING_COMMIT | 2026-10-16T14:58:20Z | sn51 commit touches scoring: DAH-4123 - Validator: split build-log streams into frames the backend… |
| `sn67:scoring_commit:2026-10-16T11:32:32Z` | 67 | SCORING_COMMIT | 2026-10-16T14:58:20Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20261016.post1 |
| `sn78:scoring_commit:2026-10-16T13:20:49Z` | 78 | SCORING_COMMIT | 2026-10-16T14:58:20Z | sn78 commit touches scoring: Adopt qualified reward runtimes without resetting signed coverage |
| `sn90:scoring_commit:2026-10-16T10:16:08Z` | 90 | SCORING_COMMIT | 2026-10-16T14:58:20Z | sn90 commit touches scoring: docs(subnet): README model lists + validator stats sync |
| `sn92:scoring_commit:2026-10-16T10:25:45Z` | 92 | SCORING_COMMIT | 2026-10-16T14:58:20Z | sn92 commit touches scoring: engine track: protect pending challenger, same-cycle fresh-session co… |
| `sn100:scoring_commit:2026-10-16T13:16:02Z` | 100 | SCORING_COMMIT | 2026-10-16T14:58:20Z | sn100 commit touches scoring: fix(challenges): raise get_weights timeout to 180 seconds (#318) |
| `sn114:scoring_commit:2026-10-16T11:35:50Z` | 114 | SCORING_COMMIT | 2026-10-16T14:58:20Z | sn114 commit touches scoring: update scoring.md docs |
| `sn116:scoring_commit:2026-10-16T10:36:39Z` | 116 | SCORING_COMMIT | 2026-10-16T14:58:20Z | sn116 commit touches scoring: Merge pull request #1405 from carbonphysicsai/codex/scorelab-guarded4… |
| `sn71:scoring_commit:2026-10-16T18:40:01Z` | 71 | SCORING_COMMIT | 2026-10-16T18:46:43Z | sn71 commit touches scoring: Allow selected frozen executions in isolated shadow verification (#493 |
| `sn92:release:v1.2.0-rc6` | 92 | RELEASE | 2026-10-16T18:46:43Z | sn92 released v1.2.0-rc6 |
| `sn102:scoring_commit:2026-10-15T19:51:21Z` | 102 | SCORING_COMMIT | 2026-10-16T18:46:43Z | sn102 commit touches scoring: ✅ test(validator): after a skipped round, stale weights take the fall… |
| `sn116:scoring_commit:2026-10-16T13:41:47Z` | 116 | SCORING_COMMIT | 2026-10-16T18:46:43Z | sn116 commit touches scoring: test(launchpad): bind retain policy fixture to registered challenge |
| `sn121:scoring_commit:2026-10-16T15:26:35Z` | 121 | SCORING_COMMIT | 2026-10-16T18:46:43Z | sn121 commit touches scoring: Update README for skill bundles, the leadership margin and a Discord F |
| `sn25:release:v2026.10.16-1073843780` | 25 | RELEASE | 2026-10-16T21:47:16Z | sn25 released v2026.10.16-1073843780 |
| `sn25:scoring_commit:2026-10-16T19:01:39Z` | 25 | SCORING_COMMIT | 2026-10-16T21:47:16Z | sn25 commit touches scoring: Authenticate finalized chain absence before revoking validator eligib… |
| `sn71:scoring_commit:2026-10-16T19:32:25Z` | 71 | SCORING_COMMIT | 2026-10-16T21:47:16Z | sn71 commit touches scoring: Select verified homepage profile for unbound size citations (#496) |
| `sn91:scoring_commit:2026-10-16T20:57:49Z` | 91 | SCORING_COMMIT | 2026-10-16T21:47:16Z | sn91 commit touches scoring: Merge pull request #370 from TensorLink-AI/docs/miner-admission-guard |
| `sn92:release:v1.2.0-rc7` | 92 | RELEASE | 2026-10-16T21:47:16Z | sn92 released v1.2.0-rc7 |
| `sn102:release:v0.7.1` | 102 | RELEASE | 2026-10-16T21:47:16Z | sn102 released v0.7.1 |
| `sn116:scoring_commit:2026-10-16T20:22:44Z` | 116 | SCORING_COMMIT | 2026-10-16T21:47:16Z | sn116 commit touches scoring: Merge pull request #1408 from carbonphysicsai/codex/gpu-miner-control… |
| `sn25:release:v2026.10.16-1073891640` | 25 | RELEASE | 2026-10-16T23:59:25Z | sn25 released v2026.10.16-1073891640 |
| `sn71:scoring_commit:2026-10-16T23:28:33Z` | 71 | SCORING_COMMIT | 2026-10-16T23:59:25Z | sn71 commit touches scoring: Move scorer checkpoint and output IO behind runtime interface |
| `sn78:scoring_commit:2026-10-16T22:57:25Z` | 78 | SCORING_COMMIT | 2026-10-16T23:59:25Z | sn78 commit touches scoring: Score original forecast ranges and retain comparable outcome evidence |
| `sn116:release:worker-images-v5 (DEVELOPMENT)` | 116 | RELEASE | 2026-10-16T23:59:25Z | sn116 released worker-images-v5 (DEVELOPMENT) |
| `sn116:scoring_commit:2026-10-16T20:58:13Z` | 116 | SCORING_COMMIT | 2026-10-16T23:59:25Z | sn116 commit touches scoring: Format F06 Challenge registry assertions |
| `sn25:release:v2026.10.16-1074037020` | 25 | RELEASE | 2026-10-17T04:17:15Z | sn25 released v2026.10.16-1074037020 |
| `sn71:scoring_commit:2026-10-17T01:24:18Z` | 71 | SCORING_COMMIT | 2026-10-17T04:17:15Z | sn71 commit touches scoring: Merge current main and validate selected judge runtime in training ex… |
| `sn91:scoring_commit:2026-10-17T01:20:18Z` | 91 | SCORING_COMMIT | 2026-10-17T04:17:15Z | sn91 commit touches scoring: fix(promotion): anchor the trainer's reign clock where validators res… |
| `sn92:release:v1.2.0-rc7.post1` | 92 | RELEASE | 2026-10-17T04:17:15Z | sn92 released v1.2.0-rc7.post1 |
| `sn15:release:v2.5.5: Bound validator reads of sandbox` | 15 | RELEASE | 2026-10-17T08:43:24Z | sn15 released v2.5.5: Bound validator reads of sandbox output files (#378) |
| `sn15:scoring_commit:2026-10-17T07:52:59Z` | 15 | SCORING_COMMIT | 2026-10-17T08:43:24Z | sn15 commit touches scoring: Bound validator reads of sandbox output files (#378) |
| `sn25:release:v2026.10.16-1074191560` | 25 | RELEASE | 2026-10-17T08:43:24Z | sn25 released v2026.10.16-1074191560 |
| `sn37:scoring_commit:2026-10-17T05:44:48Z` | 37 | SCORING_COMMIT | 2026-10-17T08:43:24Z | sn37 commit touches scoring: fix(miner): enable reviewed runtime479 funding (#31) |
| `sn51:scoring_commit:2026-10-17T08:20:58Z` | 51 | SCORING_COMMIT | 2026-10-17T08:43:24Z | sn51 commit touches scoring: DAH-4280 - [P0] Validator: cross-check the reported GPU count against… |
| `sn71:scoring_commit:2026-10-17T06:44:45Z` | 71 | SCORING_COMMIT | 2026-10-17T08:43:24Z | sn71 commit touches scoring: fix(arena): retain verified source redirects for fallback (#519) |
| `sn78:scoring_commit:2026-10-17T06:12:23Z` | 78 | SCORING_COMMIT | 2026-10-17T08:43:24Z | sn78 commit touches scoring: Merge pull request #294 from Umi-BitSign/codex/c6-portable-byte-verif… |
| `sn92:release:v1.2.0-rc7.post3` | 92 | RELEASE | 2026-10-17T08:43:24Z | sn92 released v1.2.0-rc7.post3 |
| `sn108:scoring_commit:2026-10-16T09:36:40Z` | 108 | SCORING_COMMIT | 2026-10-17T08:43:24Z | sn108 commit touches scoring: Validators don't pay records the server marks banned (coldkey banned … |
| `sn116:scoring_commit:2026-10-17T04:56:00Z` | 116 | SCORING_COMMIT | 2026-10-17T08:43:24Z | sn116 commit touches scoring: Merge pull request #1416 from carbonphysicsai/codex/s5-challenge-sele… |
| `sn21:scoring_commit:2026-10-17T11:22:46Z` | 21 | SCORING_COMMIT | 2026-10-17T12:28:43Z | sn21 commit touches scoring: feat(scoring): absence charges stop once a hotkey holds no real entry… |
| `sn25:release:v2026.10.17-1074370910` | 25 | RELEASE | 2026-10-17T12:28:43Z | sn25 released v2026.10.17-1074370910 |
| `sn51:release:executor-v1.142` | 51 | RELEASE | 2026-10-17T12:28:43Z | sn51 released executor-v1.142 |
| `sn51:scoring_commit:2026-10-17T11:57:18Z` | 51 | SCORING_COMMIT | 2026-10-17T12:28:43Z | sn51 commit touches scoring: Sysbox installer: show the verify container's error when step 6 fails… |
| `sn92:release:v1.2.0-rc7.post4` | 92 | RELEASE | 2026-10-17T12:28:43Z | sn92 released v1.2.0-rc7.post4 |
| `sn7:release:release-20261017-152034: Bound event ing` | 7 | RELEASE | 2026-10-17T15:58:40Z | sn7 released release-20261017-152034: Bound event ingest per pass and cap its lookback at 6h (#792) |
| `sn28:release:v0.5.2` | 28 | RELEASE | 2026-10-17T15:58:40Z | sn28 released v0.5.2 |
| `sn28:scoring_commit:2026-10-17T13:33:09Z` | 28 | SCORING_COMMIT | 2026-10-17T15:58:40Z | sn28 commit touches scoring: chore(release): promote gm-miner 0.5.2 (#327) |
| `sn51:scoring_commit:2026-10-17T12:38:54Z` | 51 | SCORING_COMMIT | 2026-10-17T15:58:40Z | sn51 commit touches scoring: DAH-4601 - [P0] Validator: fail a node where sshd does not start in t… |
| `sn92:release:v1.2.0-rc8` | 92 | RELEASE | 2026-10-17T15:58:40Z | sn92 released v1.2.0-rc8 |
| `sn41:scoring_commit:2026-10-17T16:02:48Z` | 41 | SCORING_COMMIT | 2026-10-17T18:25:49Z | sn41 commit touches scoring: Merge pull request #59 from corvxai/vali_no_assign_before_scoring |
| `sn78:scoring_commit:2026-10-17T17:36:20Z` | 78 | SCORING_COMMIT | 2026-10-17T18:25:49Z | sn78 commit touches scoring: Backport current reward coverage capture to exact C5 runtime |
| `sn91:scoring_commit:2026-10-17T20:13:24Z` | 91 | SCORING_COMMIT | 2026-10-17T20:51:47Z | sn91 commit touches scoring: Merge pull request #373 from TensorLink-AI/feat/payer-bench-unverified |
| `sn51:release:miner-v1.006` | 51 | RELEASE | 2026-10-17T23:04:30Z | sn51 released miner-v1.006 |
| `sn51:scoring_commit:2026-10-17T21:06:14Z` | 51 | SCORING_COMMIT | 2026-10-17T23:04:30Z | sn51 commit touches scoring: DAH-4539 - Miner: a portal delete removes only the node it names (#166 |
| `sn78:scoring_commit:2026-10-17T21:58:15Z` | 78 | SCORING_COMMIT | 2026-10-17T23:04:30Z | sn78 commit touches scoring: Recover historical reward coverage gaps from durable native endpoints |
| `sn15:release:v2.5.6: Bound per-evaluation sandbox dis` | 15 | RELEASE | 2026-10-18T00:59:01Z | sn15 released v2.5.6: Bound per-evaluation sandbox disk use |
| `sn15:scoring_commit:2026-10-17T23:22:22Z` | 15 | SCORING_COMMIT | 2026-10-18T00:59:01Z | sn15 commit touches scoring: Bound per-evaluation sandbox disk use |
| `sn15:scoring_commit:2026-10-18T05:27:40Z` | 15 | SCORING_COMMIT | 2026-10-18T05:49:20Z | sn15 commit touches scoring: fix(validator): send sandbox_metadata when retrying a completion (#352 |
| `sn25:release:v2026.10.17-1074871400` | 25 | RELEASE | 2026-10-18T05:49:20Z | sn25 released v2026.10.17-1074871400 |
| `sn53:scoring_commit:2026-10-18T04:05:58Z` | 53 | SCORING_COMMIT | 2026-10-18T05:49:20Z | sn53 commit touches scoring: tee_miner: default to half the legs on the LB, half on Cloudflare, sh… |
| `sn55:scoring_commit:2026-10-18T05:30:43Z` | 55 | SCORING_COMMIT | 2026-10-18T05:49:20Z | sn55 commit touches scoring: set weights using valid scores |
| `sn71:scoring_commit:2026-10-18T01:41:09Z` | 71 | SCORING_COMMIT | 2026-10-18T05:49:20Z | sn71 commit touches scoring: Prune superseded Deepline score billing heads before V3 candidate wor… |
| `sn15:scoring_commit:2026-10-18T06:23:50Z` | 15 | SCORING_COMMIT | 2026-10-18T10:56:59Z | sn15 commit touches scoring: docs: update stale pack digest and runtime in miner-guide sample run … |
| `sn71:scoring_commit:2026-10-18T06:55:55Z` | 71 | SCORING_COMMIT | 2026-10-18T10:56:59Z | sn71 commit touches scoring: fix(arena): classify unavailable frozen score routes before dispatch |
| `sn116:scoring_commit:2026-10-17T23:42:51Z` | 116 | SCORING_COMMIT | 2026-10-18T10:56:59Z | sn116 commit touches scoring: docs: lock bank-version reuse and reward-clock safeguards |
| `sn67:scoring_commit:2026-10-18T12:04:24Z` | 67 | SCORING_COMMIT | 2026-10-18T14:32:37Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20261018.post0 |
| `sn66:scoring_commit:2026-10-18T16:02:02Z` | 66 | SCORING_COMMIT | 2026-10-18T17:34:40Z | sn66 commit touches scoring: Activate the Mathlib header task release |
| `sn116:scoring_commit:2026-10-18T16:35:31Z` | 116 | SCORING_COMMIT | 2026-10-18T17:34:40Z | sn116 commit touches scoring: Merge pull request #1423 from carbonphysicsai/codex/scorelab-dual-del… |
| `sn1:release:v4.4.14` | 1 | RELEASE | 2026-10-18T19:42:43Z | sn1 released v4.4.14 |
| `sn25:release:v2026.10.18-1075514170` | 25 | RELEASE | 2026-10-18T19:42:43Z | sn25 released v2026.10.18-1075514170 |
| `sn82:scoring_commit:2026-10-18T18:10:45Z` | 82 | SCORING_COMMIT | 2026-10-18T19:42:43Z | sn82 commit touches scoring: Release v0.1.0: multisig receipts and surplus-bonus scoring |
| `sn92:release:v1.2.0-rc9` | 92 | RELEASE | 2026-10-18T19:42:43Z | sn92 released v1.2.0-rc9 |
| `sn78:scoring_commit:2026-10-18T21:56:00Z` | 78 | SCORING_COMMIT | 2026-10-18T21:56:26Z | sn78 commit touches scoring: Wait for identity-checked validator worker startup (#310) |
| `sn21:scoring_commit:2026-10-19T03:05:03Z` | 21 | SCORING_COMMIT | 2026-10-19T05:03:29Z | sn21 commit touches scoring: feat(executor): the scored run can wait for the basket's change descr… |
| `sn25:release:v2026.10.18-1075707760` | 25 | RELEASE | 2026-10-19T05:03:29Z | sn25 released v2026.10.18-1075707760 |
| `sn51:release:executor-v1.143` | 51 | RELEASE | 2026-10-19T05:03:29Z | sn51 released executor-v1.143 |
| `sn51:scoring_commit:2026-10-19T04:21:15Z` | 51 | SCORING_COMMIT | 2026-10-19T05:03:29Z | sn51 commit touches scoring: DAH-3980 - Validator: customer create removes a leftover filler or fa… |
| `sn71:scoring_commit:2026-10-19T01:00:51Z` | 71 | SCORING_COMMIT | 2026-10-19T05:03:29Z | sn71 commit touches scoring: Resolve verified LinkedIn company redirects in either direction (#537) |
| `sn116:scoring_commit:2026-10-18T18:52:31Z` | 116 | SCORING_COMMIT | 2026-10-19T05:03:29Z | sn116 commit touches scoring: Retain admitted cold overlays from verified original source |
| `sn117:release:everycli v0.5.8` | 117 | RELEASE | 2026-10-19T05:03:29Z | sn117 released everycli v0.5.8 |
| `sn117:scoring_commit:2026-10-19T03:47:45Z` | 117 | SCORING_COMMIT | 2026-10-19T05:03:29Z | sn117 commit touches scoring: fix: validate provider model availability and clarify catalog IDs |
| `sn25:release:v2026.10.19-1076002880` | 25 | RELEASE | 2026-10-19T10:42:29Z | sn25 released v2026.10.19-1076002880 |
| `sn51:release:miner-v1.007` | 51 | RELEASE | 2026-10-19T10:42:29Z | sn51 released miner-v1.007 |
| `sn51:scoring_commit:2026-10-19T10:33:44Z` | 51 | SCORING_COMMIT | 2026-10-19T10:42:29Z | sn51 commit touches scoring: DAH-2834 - [P2] shadow the verify agent over SSH and ship it in the e… |
| `sn53:scoring_commit:2026-10-19T07:16:06Z` | 53 | SCORING_COMMIT | 2026-10-19T10:42:29Z | sn53 commit touches scoring: Merge pull request #56 from hanlinai/fix/tee-miner-prefix-continuation |
| `sn67:scoring_commit:2026-10-19T09:18:23Z` | 67 | SCORING_COMMIT | 2026-10-19T10:42:29Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20261019.post1 |
| `sn71:scoring_commit:2026-10-19T08:17:23Z` | 71 | SCORING_COMMIT | 2026-10-19T10:42:29Z | sn71 commit touches scoring: Preserve first-party funding context through verification and retries |
| `sn78:scoring_commit:2026-10-19T07:58:40Z` | 78 | SCORING_COMMIT | 2026-10-19T10:42:29Z | sn78 commit touches scoring: Merge pull request #315 from Umi-BitSign/fix/miner-direct-upload-retr… |
| `sn92:release:v1.2.0-rc9.post3` | 92 | RELEASE | 2026-10-19T10:42:29Z | sn92 released v1.2.0-rc9.post3 |
| `sn7:release:release-20261019-165322` | 7 | RELEASE | 2026-10-19T17:12:59Z | sn7 released release-20261019-165322 |
| `sn21:scoring_commit:2026-10-19T14:00:58Z` | 21 | SCORING_COMMIT | 2026-10-19T17:12:59Z | sn21 commit touches scoring: feat(scoring): the pooled count score can be published before the cou… |
| `sn22:scoring_commit:2026-10-19T12:52:00Z` | 22 | SCORING_COMMIT | 2026-10-19T17:12:59Z | sn22 commit touches scoring: fix(task-api): reference vectors finish and stay kept even when the a… |
| `sn25:release:v2026.10.19-1076177550` | 25 | RELEASE | 2026-10-19T17:12:59Z | sn25 released v2026.10.19-1076177550 |
| `sn28:release:v0.5.3-dev` | 28 | RELEASE | 2026-10-19T17:12:59Z | sn28 released v0.5.3-dev |
| `sn51:release:miner-v1.008` | 51 | RELEASE | 2026-10-19T17:12:59Z | sn51 released miner-v1.008 |
| `sn51:scoring_commit:2026-10-19T16:11:54Z` | 51 | SCORING_COMMIT | 2026-10-19T17:12:59Z | sn51 commit touches scoring: DAH-4124 - [P2] validator: record EXECUTOR_UNREACHABLE_BY_MINER for a… |
| `sn67:scoring_commit:2026-10-19T11:36:22Z` | 67 | SCORING_COMMIT | 2026-10-19T17:12:59Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20261019.post4 |
| `sn82:scoring_commit:2026-10-19T16:17:18Z` | 82 | SCORING_COMMIT | 2026-10-19T17:12:59Z | sn82 commit touches scoring: Allow configured validator publishing identities (#2) |
| `sn15:scoring_commit:2026-10-19T19:37:29Z` | 15 | SCORING_COMMIT | 2026-10-19T21:39:26Z | sn15 commit touches scoring: fix: use validator lockfile for local tests and CI |
| `sn41:scoring_commit:2026-10-19T18:42:33Z` | 41 | SCORING_COMMIT | 2026-10-19T21:39:26Z | sn41 commit touches scoring: Updating default miner alpha to 3600, or 50% of total emissions with … |
| `sn50:scoring_commit:2026-10-19T20:29:17Z` | 50 | SCORING_COMMIT | 2026-10-19T21:39:26Z | sn50 commit touches scoring: burn 22% of miner emission (#341) |
| `sn51:scoring_commit:2026-10-19T19:42:46Z` | 51 | SCORING_COMMIT | 2026-10-19T21:39:26Z | sn51 commit touches scoring: DAH-4195 - [P2] Skip could-not-reach rows when the miner reached almo… |
| `sn71:scoring_commit:2026-10-19T20:07:21Z` | 71 | SCORING_COMMIT | 2026-10-19T21:39:26Z | sn71 commit touches scoring: Record verified runtime recovery release fingerprint |
| `sn100:scoring_commit:2026-10-19T20:57:30Z` | 100 | SCORING_COMMIT | 2026-10-19T21:39:26Z | sn100 commit touches scoring: docs(validator): cover both profile version caps and restart wording |
| `sn111:release:v1.1.0` | 111 | RELEASE | 2026-10-19T21:39:26Z | sn111 released v1.1.0 |
| `sn111:scoring_commit:2026-10-19T13:02:58Z` | 111 | SCORING_COMMIT | 2026-10-19T21:39:26Z | sn111 commit touches scoring: Integrate approved-group fractional coverage into validator scoring |
| `sn22:scoring_commit:2026-10-19T21:30:20Z` | 22 | SCORING_COMMIT | 2026-10-20T00:43:32Z | sn22 commit touches scoring: fix(validators): embed checks wait up to 120 s for reference vectors,… |
| `sn28:release:v0.5.4` | 28 | RELEASE | 2026-10-20T00:43:32Z | sn28 released v0.5.4 |
| `sn28:scoring_commit:2026-10-19T22:56:58Z` | 28 | SCORING_COMMIT | 2026-10-20T00:43:32Z | sn28 commit touches scoring: chore(release): promote gm-miner 0.5.4 (#333) |
| `sn71:scoring_commit:2026-10-19T23:46:13Z` | 71 | SCORING_COMMIT | 2026-10-20T00:43:32Z | sn71 commit touches scoring: Regenerate protected scorer manifest from committed source |
| `sn37:scoring_commit:2026-10-20T03:53:10Z` | 37 | SCORING_COMMIT | 2026-10-20T05:24:18Z | sn37 commit touches scoring: fix(miner): admit reviewed runtime481 funding (#32) |
| `sn71:scoring_commit:2026-10-20T04:57:34Z` | 71 | SCORING_COMMIT | 2026-10-20T05:24:18Z | sn71 commit touches scoring: Merge pull request #583 from leadpoet/audit/oct20-scoring-quality |
| `sn81:scoring_commit:2026-10-20T03:50:31Z` | 81 | SCORING_COMMIT | 2026-10-20T05:24:18Z | sn81 commit touches scoring: fix(validator): a task on Qwen3.5's text-only class can be served |
| `sn25:release:v2026.10.20-1076869840` | 25 | RELEASE | 2026-10-20T10:18:20Z | sn25 released v2026.10.20-1076869840 |
| `sn51:scoring_commit:2026-10-20T08:46:36Z` | 51 | SCORING_COMMIT | 2026-10-20T10:18:20Z | sn51 commit touches scoring: DAH-4622 - [P1] Validator: report rented cards with uncorrected ECC t… |
| `sn66:release:deployed/dev: Merge pull request #139 fr` | 66 | RELEASE | 2026-10-20T10:18:20Z | sn66 released deployed/dev: Merge pull request #139 from conjectures-io/fix/deploy-task-modes |
| `sn67:scoring_commit:2026-10-20T06:10:57Z` | 67 | SCORING_COMMIT | 2026-10-20T10:18:20Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20261020.post2 |
| `sn71:scoring_commit:2026-10-20T07:07:45Z` | 71 | SCORING_COMMIT | 2026-10-20T10:18:20Z | sn71 commit touches scoring: Reuse validated company authority for consumer ownership checks |
| `sn127:scoring_commit:2026-10-20T09:51:40Z` | 127 | SCORING_COMMIT | 2026-10-20T10:18:20Z | sn127 commit touches scoring: Merge pull request #1 from astridintelligence/astrid-score-payouts |
| `sn3:scoring_commit:2026-10-20T11:26:30Z` | 3 | SCORING_COMMIT | 2026-10-20T15:16:23Z | sn3 commit touches scoring: Sample evaluation sequences from at least five shards per category |
| `sn25:release:v2026.10.20-1077000950` | 25 | RELEASE | 2026-10-20T15:16:23Z | sn25 released v2026.10.20-1077000950 |
| `sn28:release:v0.5.5` | 28 | RELEASE | 2026-10-20T15:16:23Z | sn28 released v0.5.5 |
| `sn28:scoring_commit:2026-10-20T10:26:11Z` | 28 | SCORING_COMMIT | 2026-10-20T15:16:23Z | sn28 commit touches scoring: chore(release): gm-miner 0.5.5 (#335) |
| `sn51:scoring_commit:2026-10-20T14:27:06Z` | 51 | SCORING_COMMIT | 2026-10-20T15:16:23Z | sn51 commit touches scoring: DAH-4481 - [P1] Validator says the miner no longer lists the executor… |
| `sn66:release:deployed/dev: Merge pull request #141 fr` | 66 | RELEASE | 2026-10-20T15:16:23Z | sn66 released deployed/dev: Merge pull request #141 from conjectures-io/ci/prod-hardening |
| `sn67:scoring_commit:2026-10-20T11:02:08Z` | 67 | SCORING_COMMIT | 2026-10-20T15:16:23Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20261020.post3 |
| `sn71:scoring_commit:2026-10-20T14:26:05Z` | 71 | SCORING_COMMIT | 2026-10-20T15:16:23Z | sn71 commit touches scoring: Recover abandoned scorer-image setup through bounded lease recovery |
| `sn97:scoring_commit:2026-10-20T14:46:53Z` | 97 | SCORING_COMMIT | 2026-10-20T15:16:23Z | sn97 commit touches scoring: fix: show diverged challengers as < −50% and republish evals with non… |
| `sn66:release:deployed/dev: Merge pull request #143 fr` | 66 | RELEASE | 2026-10-20T19:28:18Z | sn66 released deployed/dev: Merge pull request #143 from conjectures-io/ci/merge-queue |
| `sn66:scoring_commit:2026-10-20T09:00:23Z` | 66 | SCORING_COMMIT | 2026-10-20T19:28:18Z | sn66 commit touches scoring: Merge pull request #139 from conjectures-io/fix/deploy-task-modes |
| `sn71:scoring_commit:2026-10-20T15:18:06Z` | 71 | SCORING_COMMIT | 2026-10-20T19:28:18Z | sn71 commit touches scoring: Refresh persisted Arena model scores before unpublished evidence (#615 |
| `sn81:scoring_commit:2026-10-20T12:58:45Z` | 81 | SCORING_COMMIT | 2026-10-20T19:28:18Z | sn81 commit touches scoring: ci: replace obsolete validator check runs |
| `sn92:release:v1.2.0-rc9.post6` | 92 | RELEASE | 2026-10-20T19:28:18Z | sn92 released v1.2.0-rc9.post6 |
| `sn5:scoring_commit:2026-10-20T01:48:53Z` | 5 | SCORING_COMMIT | 2026-10-20T22:43:54Z | sn5 commit touches scoring: Keep validator connections alive while miners think |
| `sn71:scoring_commit:2026-10-20T21:51:33Z` | 71 | SCORING_COMMIT | 2026-10-20T22:43:54Z | sn71 commit touches scoring: Bound composed scorer image tags without losing repair identity |
| `sn81:scoring_commit:2026-10-20T20:19:23Z` | 81 | SCORING_COMMIT | 2026-10-20T22:43:54Z | sn81 commit touches scoring: Merge invalidated export filtering (#365) |
| `sn25:release:v2026.10.20-1077406510` | 25 | RELEASE | 2026-10-21T01:02:40Z | sn25 released v2026.10.20-1077406510 |
| `sn71:scoring_commit:2026-10-20T22:59:19Z` | 71 | SCORING_COMMIT | 2026-10-21T01:02:40Z | sn71 commit touches scoring: Evaluate Arena claim admission lazily in priority order |
| `sn92:release:v1.2.0-rc9.post7` | 92 | RELEASE | 2026-10-21T01:02:40Z | sn92 released v1.2.0-rc9.post7 |
| `sn25:release:v2026.10.20-1077553990` | 25 | RELEASE | 2026-10-21T05:59:05Z | sn25 released v2026.10.20-1077553990 |
| `sn30:release:v0.1.3 — Identical-forecast pooling, pro` | 30 | RELEASE | 2026-10-21T05:59:05Z | sn30 released v0.1.3 — Identical-forecast pooling, protocol 2044 |
| `sn30:scoring_commit:2026-10-20T07:46:32Z` | 30 | SCORING_COMMIT | 2026-10-21T05:59:05Z | sn30 commit touches scoring: feat(scoring): identical-forecast pooling (2044) and v0.1.3 release m… |
| `sn51:release:executor-v1.149` | 51 | RELEASE | 2026-10-21T05:59:05Z | sn51 released executor-v1.149 |
| `sn51:scoring_commit:2026-10-21T02:57:33Z` | 51 | SCORING_COMMIT | 2026-10-21T05:59:05Z | sn51 commit touches scoring: DAH-4266 - [P2] validator: keep a pass-through nvidia entrypoint with… |
| `sn81:scoring_commit:2026-10-21T04:53:42Z` | 81 | SCORING_COMMIT | 2026-10-21T05:59:05Z | sn81 commit touches scoring: Merge pull request #372 from reliquadotai/fix/miner-state-metadata-io |
| `sn117:release:everycli v0.6.0` | 117 | RELEASE | 2026-10-21T05:59:05Z | sn117 released everycli v0.6.0 |
| `sn117:scoring_commit:2026-10-20T22:36:00Z` | 117 | SCORING_COMMIT | 2026-10-21T05:59:05Z | sn117 commit touches scoring: docs(release): finalize v0.6.0 routing and four-platform validation |
| `sn51:release:miner-v1.009` | 51 | RELEASE | 2026-10-21T11:40:48Z | sn51 released miner-v1.009 |
| `sn51:scoring_commit:2026-10-21T10:38:31Z` | 51 | SCORING_COMMIT | 2026-10-21T11:40:48Z | sn51 commit touches scoring: DAH-4860 - [P2] validator: CPU truth check always runs (remove CPU_TR… |
| `sn67:scoring_commit:2026-10-21T11:20:00Z` | 67 | SCORING_COMMIT | 2026-10-21T11:40:48Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20261021.post9 |
| `sn92:release:v1.2.0-rc10` | 92 | RELEASE | 2026-10-21T11:40:48Z | sn92 released v1.2.0-rc10 |
| `sn3:scoring_commit:2026-10-21T14:45:39Z` | 3 | SCORING_COMMIT | 2026-10-21T16:08:35Z | sn3 commit touches scoring: Fix category dataset validation and hide retired competition mixes |
| `sn50:scoring_commit:2026-10-21T13:49:08Z` | 50 | SCORING_COMMIT | 2026-10-21T16:08:35Z | sn50 commit touches scoring: feat(validator): one VHFT competition per rewarded asset (#340) |
| `sn51:scoring_commit:2026-10-21T14:02:49Z` | 51 | SCORING_COMMIT | 2026-10-21T16:08:35Z | sn51 commit touches scoring: DAH-4937 - [P1] Validator: a create waits out a miner restart instead… |
| `sn66:release:v2026.10.21.2` | 66 | RELEASE | 2026-10-21T16:08:35Z | sn66 released v2026.10.21.2 |
| `sn81:scoring_commit:2026-10-21T14:21:49Z` | 81 | SCORING_COMMIT | 2026-10-21T16:08:35Z | sn81 commit touches scoring: Merge pull request #375 from reliquadotai/fix/miner-state-cold-start |
| `sn111:scoring_commit:2026-10-21T14:34:11Z` | 111 | SCORING_COMMIT | 2026-10-21T16:08:35Z | sn111 commit touches scoring: fix: retry backend 503 responses for miner and validator uploads |
| `sn114:scoring_commit:2026-10-21T12:16:14Z` | 114 | SCORING_COMMIT | 2026-10-21T16:08:35Z | sn114 commit touches scoring: Improve competition operations and validation dispatch |
| `sn117:release:v0.6.1: Merge pull request #39 from ever` | 117 | RELEASE | 2026-10-21T16:08:35Z | sn117 released v0.6.1: Merge pull request #39 from everyframe-studio/feat/flux3-max |
| `sn7:release:release-20261021-195318: Scale the miner` | 7 | RELEASE | 2026-10-21T20:17:01Z | sn7 released release-20261021-195318: Scale the miner pool by recent swap fees (#811) |
| `sn7:scoring_commit:2026-10-21T19:52:45Z` | 7 | SCORING_COMMIT | 2026-10-21T20:17:01Z | sn7 commit touches scoring: Scale the miner pool by recent swap fees (#811) |
| `sn28:release:v0.5.6-dev` | 28 | RELEASE | 2026-10-21T20:17:01Z | sn28 released v0.5.6-dev |
| `sn28:scoring_commit:2026-10-21T16:47:19Z` | 28 | SCORING_COMMIT | 2026-10-21T20:17:01Z | sn28 commit touches scoring: chore(release): gm-miner 0.5.6-dev (#337) |
| `sn71:scoring_commit:2026-10-21T19:53:06Z` | 71 | SCORING_COMMIT | 2026-10-21T20:17:01Z | sn71 commit touches scoring: Retain proofs and receipts for approved scoring provider routes |
| `sn76:release:v0.0.3: Merge pull request #45 from hero` | 76 | RELEASE | 2026-10-21T20:17:01Z | sn76 released v0.0.3: Merge pull request #45 from heroncovelabs/fix/recover-public-work-packet |
| `sn78:scoring_commit:2026-10-21T19:17:18Z` | 78 | SCORING_COMMIT | 2026-10-21T20:17:01Z | sn78 commit touches scoring: chore(verification): bind qualified baseline guard sources |
| `sn81:scoring_commit:2026-10-21T20:16:18Z` | 81 | SCORING_COMMIT | 2026-10-21T20:17:01Z | sn81 commit touches scoring: Merge pull request #379 from reliquadotai/fix/evaluation-sandbox-scope |
| `sn117:release:everycli v0.6.2` | 117 | RELEASE | 2026-10-21T20:17:01Z | sn117 released everycli v0.6.2 |
| `sn25:release:v2026.10.21-1078195620` | 25 | RELEASE | 2026-10-21T23:30:35Z | sn25 released v2026.10.21-1078195620 |
| `sn28:release:v0.5.7` | 28 | RELEASE | 2026-10-21T23:30:35Z | sn28 released v0.5.7 |
| `sn28:scoring_commit:2026-10-21T21:33:17Z` | 28 | SCORING_COMMIT | 2026-10-21T23:30:35Z | sn28 commit touches scoring: chore(release): gm-miner 0.5.7 (#340) |
| `sn71:scoring_commit:2026-10-21T22:55:23Z` | 71 | SCORING_COMMIT | 2026-10-21T23:30:35Z | sn71 commit touches scoring: Keep restored-score exclusions visible without inventing scores |
| `sn78:scoring_commit:2026-10-21T20:49:08Z` | 78 | SCORING_COMMIT | 2026-10-21T23:30:35Z | sn78 commit touches scoring: Merge pull request #343 from Umi-BitSign/qualify-c6-model-only-reward… |
| `sn81:scoring_commit:2026-10-21T20:51:36Z` | 81 | SCORING_COMMIT | 2026-10-21T23:30:35Z | sn81 commit touches scoring: fix: verify evaluation image against supported sandbox pin |
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
| `sn37:readme_task_diff:8fd038bdd4d28f3e` | 37 | README_TASK_DIFF | 2026-10-16T00:49:24Z | sn37 README task/scoring sections changed |
| `sn90:readme_task_diff:31c270cb714e86fe` | 90 | README_TASK_DIFF | 2026-10-16T14:58:20Z | sn90 README task/scoring sections changed |
| `sn121:readme_task_diff:3c2e2790982a3aff` | 121 | README_TASK_DIFF | 2026-10-16T18:46:43Z | sn121 README task/scoring sections changed |
| `sn37:readme_task_diff:0aa02311a0f783a4` | 37 | README_TASK_DIFF | 2026-10-17T08:43:24Z | sn37 README task/scoring sections changed |
| `sn125:readme_task_diff:5d449bf6f7a1b5b8` | 125 | README_TASK_DIFF | 2026-10-18T05:49:20Z | sn125 README task/scoring sections changed |
| `sn89:readme_task_diff:46569451fd573f74` | 89 | README_TASK_DIFF | 2026-10-19T05:03:29Z | sn89 README task/scoring sections changed |
| `sn90:readme_task_diff:f94fa7f5ba6e1765` | 90 | README_TASK_DIFF | 2026-10-19T17:12:59Z | sn90 README task/scoring sections changed |
| `sn37:readme_task_diff:7d03fd0e56d5b691` | 37 | README_TASK_DIFF | 2026-10-20T05:24:18Z | sn37 README task/scoring sections changed |
| `sn30:readme_task_diff:4a7c5aebb5ea217a` | 30 | README_TASK_DIFF | 2026-10-21T05:59:05Z | sn30 README task/scoring sections changed |
| `sn111:readme_task_diff:6b385b714324083a` | 111 | README_TASK_DIFF | 2026-10-21T16:08:35Z | sn111 README task/scoring sections changed |
| `sn117:readme_task_diff:c73733117d32dcc0` | 117 | README_TASK_DIFF | 2026-10-21T16:08:35Z | sn117 README task/scoring sections changed |
| `sn28:readme_task_diff:2b144e347e430710` | 28 | README_TASK_DIFF | 2026-10-21T20:17:01Z | sn28 README task/scoring sections changed |
| `sn78:readme_task_diff:07cc2c9379a76a69` | 78 | README_TASK_DIFF | 2026-10-22T07:29:56Z | sn78 README task/scoring sections changed |
| `sn15:readme_task_diff:71fad80912f70006` | 15 | README_TASK_DIFF | 2026-10-22T13:13:57Z | sn15 README task/scoring sections changed |

## RESOLVED IN THIS WINDOW

_none_
