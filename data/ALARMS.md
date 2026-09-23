# ALARMS - generated 2026-09-23T23:14:01Z, block 9133558

window: first_seen in [2026-09-23T21:59:27Z, 2026-09-23T23:14:27Z)  (60 min interval + 15 min overlap)

Report ONLY the rows under NEW SINCE LAST RUN. Rows under STILL OPEN were
already reported in an earlier window and must not be re-alarmed.

## NEW SINCE LAST RUN

| event_id | netuid | class | severity | first_seen_utc | one_line |
|---|---|---|---|---|---|
| `sn120:scoring_commit:2026-09-23T21:51:12Z` | 120 | SCORING_COMMIT | P1 | 2026-09-23T23:14:27Z | sn120 commit touches scoring: Merge PR #66 (cursor/band-backfill-outcomes-8929): env-backfill task … |

### detail

- **`sn120:scoring_commit:2026-09-23T21:51:12Z`** - sn120 commit touches scoring: Merge PR #66 (cursor/band-backfill-outcomes-8929): env-backfill task …
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.

## STILL OPEN (already reported - do not re-alarm)

| event_id | netuid | class | first_seen_utc | one_line |
|---|---|---|---|---|
| `sn10:burn_drop:0.811` | 10 | BURN_DROP | 2026-09-17T06:06:18Z | sn10 burn fell 1.000 -> 0.811 - miners can earn again |
| `sn15:burn_drop:0.000` | 15 | BURN_DROP | 2026-09-17T11:36:55Z | sn15 burn fell 0.997 -> 0.000 - miners can earn again |
| `sn127:burn_drop:0.714` | 127 | BURN_DROP | 2026-09-18T00:36:11Z | sn127 burn fell 1.000 -> 0.714 - miners can earn again |
| `sn10:burn_drop:0.814` | 10 | BURN_DROP | 2026-09-18T23:15:17Z | sn10 burn fell 1.000 -> 0.814 - miners can earn again |
| `sn10:burn_drop:0.830` | 10 | BURN_DROP | 2026-09-19T11:19:32Z | sn10 burn fell 1.000 -> 0.830 - miners can earn again |
| `sn112:burn_drop:0.867` | 112 | BURN_DROP | 2026-09-19T11:19:32Z | sn112 burn fell 1.000 -> 0.867 - miners can earn again |
| `sn11:burn_drop:0.000` | 11 | BURN_DROP | 2026-09-20T09:45:43Z | sn11 burn fell 1.000 -> 0.000 - miners can earn again |
| `sn71:burn_drop:0.750` | 71 | BURN_DROP | 2026-09-20T13:45:04Z | sn71 burn fell 1.000 -> 0.750 - miners can earn again |
| `sn108:burn_drop:0.000` | 108 | BURN_DROP | 2026-09-20T21:45:24Z | sn108 burn fell 1.000 -> 0.000 - miners can earn again |
| `sn10:burn_drop:0.810` | 10 | BURN_DROP | 2026-09-21T19:40:22Z | sn10 burn fell 1.000 -> 0.810 - miners can earn again |
| `sn100:burn_drop:0.803` | 100 | BURN_DROP | 2026-09-22T06:50:15Z | sn100 burn fell 1.000 -> 0.803 - miners can earn again |
| `sn100:burn_drop:0.708` | 100 | BURN_DROP | 2026-09-23T01:38:19Z | sn100 burn fell 1.000 -> 0.708 - miners can earn again |
| `sn40:scoring_commit:2026-09-16T00:55:22Z` | 40 | SCORING_COMMIT | 2026-09-17T00:48:02Z | sn40 commit touches scoring: Docs: round-7 rules, miner CLI flow, auditor weights |
| `sn78:scoring_commit:2026-09-16T22:31:06Z` | 78 | SCORING_COMMIT | 2026-09-17T00:48:02Z | sn78 commit touches scoring: Merge pull request #135 from Umi-BitSign/codex/evaluator-finality-wai… |
| `sn15:release:v2.0.20` | 15 | RELEASE | 2026-09-17T06:06:18Z | sn15 released v2.0.20 |
| `sn15:scoring_commit:2026-09-17T05:30:31Z` | 15 | SCORING_COMMIT | 2026-09-17T06:06:18Z | sn15 commit touches scoring: Stop generated runs when miner inference budget is exhausted (#317) |
| `sn51:scoring_commit:2026-09-17T05:33:07Z` | 51 | SCORING_COMMIT | 2026-09-17T06:06:18Z | sn51 commit touches scoring: DAH-3264 - [P2] validator names a GPU benchmark that could not alloca… |
| `sn78:scoring_commit:2026-09-17T00:15:39Z` | 78 | SCORING_COMMIT | 2026-09-17T06:06:18Z | sn78 commit touches scoring: Verify retained clip objects before retrying an upload |
| `sn92:release:v0.4.7` | 92 | RELEASE | 2026-09-17T06:06:18Z | sn92 released v0.4.7 |
| `sn51:release:executor-v1.130` | 51 | RELEASE | 2026-09-17T11:36:55Z | sn51 released executor-v1.130 |
| `sn51:scoring_commit:2026-09-17T07:44:39Z` | 51 | SCORING_COMMIT | 2026-09-17T11:36:55Z | sn51 commit touches scoring: DAH-3519 - [P2] validator: a node whose scrape lists fewer GPUs than … |
| `sn78:scoring_commit:2026-09-17T08:39:07Z` | 78 | SCORING_COMMIT | 2026-09-17T11:36:55Z | sn78 commit touches scoring: Merge pull request #153 from Umi-BitSign/codex/evaluator-idle-finalit… |
| `sn92:release:v0.4.9` | 92 | RELEASE | 2026-09-17T11:36:55Z | sn92 released v0.4.9 |
| `sn97:scoring_commit:2026-09-16T15:02:19Z` | 97 | SCORING_COMMIT | 2026-09-17T11:36:55Z | sn97 commit touches scoring: feat: add extra attempts, so miners which got FPs can resubmit with p… |
| `sn10:scoring_commit:2026-09-17T10:11:18Z` | 10 | SCORING_COMMIT | 2026-09-17T15:41:12Z | sn10 commit touches scoring: fix: refresh campaign fees before payment and verify inclusion |
| `sn56:scoring_commit:2026-09-17T15:30:38Z` | 56 | SCORING_COMMIT | 2026-09-17T15:41:12Z | sn56 commit touches scoring: Update autoupdate_validator_steps.sh to ensure proper package managem… |
| `sn92:release:v0.4.11` | 92 | RELEASE | 2026-09-17T15:41:12Z | sn92 released v0.4.11 |
| `sn92:scoring_commit:2026-09-17T12:16:02Z` | 92 | SCORING_COMMIT | 2026-09-17T15:41:12Z | sn92 commit touches scoring: validator: rig verification needs substrate-interface, and is skipped… |
| `sn124:scoring_commit:2026-09-17T11:43:08Z` | 124 | SCORING_COMMIT | 2026-09-17T15:41:12Z | sn124 commit touches scoring: Pin numpy and repair a drifted validator at startup |
| `sn25:release:v2026.9.17-1048676710` | 25 | RELEASE | 2026-09-17T19:19:51Z | sn25 released v2026.9.17-1048676710 |
| `sn74:release:release-20260917-174533` | 74 | RELEASE | 2026-09-17T19:19:51Z | sn74 released release-20260917-174533 |
| `sn4:release:v2.0.1` | 4 | RELEASE | 2026-09-17T22:20:24Z | sn4 released v2.0.1 |
| `sn15:scoring_commit:2026-09-17T21:02:27Z` | 15 | SCORING_COMMIT | 2026-09-17T22:20:24Z | sn15 commit touches scoring: fix(validator): delete orphaned retry_queue.add_progress on logs_s3_k… |
| `sn25:release:v2026.9.17-1048832810` | 25 | RELEASE | 2026-09-17T22:20:24Z | sn25 released v2026.9.17-1048832810 |
| `sn69:scoring_commit:2026-09-17T19:29:06Z` | 69 | SCORING_COMMIT | 2026-09-17T22:20:24Z | sn69 commit touches scoring: Re-submit the latest miner weights on a block cadence |
| `sn74:release:release-20260917-220301` | 74 | RELEASE | 2026-09-17T22:20:24Z | sn74 released release-20260917-220301 |
| `sn90:scoring_commit:2026-09-17T21:14:03Z` | 90 | SCORING_COMMIT | 2026-09-17T22:20:24Z | sn90 commit touches scoring: feat(validator): raise minimum node spec to 72 cores / 1024 GiB / 5 n… |
| `sn93:scoring_commit:2026-09-17T21:13:10Z` | 93 | SCORING_COMMIT | 2026-09-17T22:20:24Z | sn93 commit touches scoring: docs: replace CLAUDE.md with AGENTS.md + on-chain liveness verificati… |
| `sn102:release:v0.6.2` | 102 | RELEASE | 2026-09-17T22:20:24Z | sn102 released v0.6.2 |
| `sn102:scoring_commit:2026-09-17T17:58:30Z` | 102 | SCORING_COMMIT | 2026-09-17T22:20:24Z | sn102 commit touches scoring: 🐛 fix(validator): drop evaluations that finish after their round is f… |
| `sn15:release:v2.0.22` | 15 | RELEASE | 2026-09-18T00:36:11Z | sn15 released v2.0.22 |
| `sn15:scoring_commit:2026-09-18T00:19:14Z` | 15 | SCORING_COMMIT | 2026-09-18T00:36:11Z | sn15 commit touches scoring: Score partial harness failures alongside agent failures (#320) |
| `sn25:release:v2026.9.17-1048903120` | 25 | RELEASE | 2026-09-18T00:36:11Z | sn25 released v2026.9.17-1048903120 |
| `sn34:scoring_commit:2026-09-17T22:39:06Z` | 34 | SCORING_COMMIT | 2026-09-18T00:36:11Z | sn34 commit touches scoring: Merge pull request #460 from BitMind-AI/feat/random-challenge-allocati |
| `sn71:scoring_commit:2026-09-17T23:22:48Z` | 71 | SCORING_COMMIT | 2026-09-18T00:36:11Z | sn71 commit touches scoring: Fit Sep18 evaluation schedule to measured validator capacity |
| `sn74:release:release-20260917-234413` | 74 | RELEASE | 2026-09-18T00:36:11Z | sn74 released release-20260917-234413 |
| `sn15:release:v2.0.23` | 15 | RELEASE | 2026-09-18T05:16:57Z | sn15 released v2.0.23 |
| `sn25:release:v2026.9.17-1048981210` | 25 | RELEASE | 2026-09-18T05:16:57Z | sn25 released v2026.9.17-1048981210 |
| `sn49:scoring_commit:2026-09-18T01:53:42Z` | 49 | SCORING_COMMIT | 2026-09-18T05:16:57Z | sn49 commit touches scoring: Enhance tournament reward structure to support podium placements with… |
| `sn71:scoring_commit:2026-09-18T04:15:55Z` | 71 | SCORING_COMMIT | 2026-09-18T05:16:57Z | sn71 commit touches scoring: Preserve verified historical local release archives |
| `sn78:scoring_commit:2026-09-18T04:12:28Z` | 78 | SCORING_COMMIT | 2026-09-18T05:16:57Z | sn78 commit touches scoring: Bind evaluation readiness to the deployed launch (#159) |
| `sn92:release:v0.4.12` | 92 | RELEASE | 2026-09-18T05:16:57Z | sn92 released v0.4.12 |
| `sn92:scoring_commit:2026-09-18T02:43:45Z` | 92 | SCORING_COMMIT | 2026-09-18T05:16:57Z | sn92 commit touches scoring: scoring: extraction F1 compares leaf fields, so nested JSON scores ag… |
| `sn25:release:v2026.9.17-1049083750` | 25 | RELEASE | 2026-09-18T09:58:19Z | sn25 released v2026.9.17-1049083750 |
| `sn28:release:v0.4.19-dev` | 28 | RELEASE | 2026-09-18T09:58:19Z | sn28 released v0.4.19-dev |
| `sn28:scoring_commit:2026-09-18T09:53:30Z` | 28 | SCORING_COMMIT | 2026-09-18T09:58:19Z | sn28 commit touches scoring: chore(release): bump miner to 0.4.19 |
| `sn51:release:watchtower-v1.1.0` | 51 | RELEASE | 2026-09-18T09:58:19Z | sn51 released watchtower-v1.1.0 |
| `sn71:scoring_commit:2026-09-18T07:44:16Z` | 71 | SCORING_COMMIT | 2026-09-18T09:58:19Z | sn71 commit touches scoring: Seal Sep18 baseline rerun for validated public sales agent |
| `sn3:scoring_commit:2026-09-18T13:31:22Z` | 3 | SCORING_COMMIT | 2026-09-18T14:27:07Z | sn3 commit touches scoring: Add category-stratified evaluation sampling and per-sample loss tracki |
| `sn9:release:v4.13.1` | 9 | RELEASE | 2026-09-18T14:27:07Z | sn9 released v4.13.1 |
| `sn71:scoring_commit:2026-09-18T10:07:01Z` | 71 | SCORING_COMMIT | 2026-09-18T14:27:07Z | sn71 commit touches scoring: Reuse exact retained miner scores for Sep18 rerun295 |
| `sn104:scoring_commit:2026-09-18T10:58:29Z` | 104 | SCORING_COMMIT | 2026-09-18T14:27:07Z | sn104 commit touches scoring: Merge pull request #13 from taostatus/feat/scoring-mech |
| `sn12:release:validator-staging-2026-09-18-35368036673` | 12 | RELEASE | 2026-09-18T17:50:06Z | sn12 released validator-staging-2026-09-18-35368036673-626-1: fix: evict old neurons in allowance evict_old_data task |
| `sn12:scoring_commit:2026-09-18T16:19:52Z` | 12 | SCORING_COMMIT | 2026-09-18T17:50:06Z | sn12 commit touches scoring: fix: evict old neurons in allowance evict_old_data task |
| `sn15:scoring_commit:2026-09-18T17:44:07Z` | 15 | SCORING_COMMIT | 2026-09-18T17:50:06Z | sn15 commit touches scoring: validator: hard-fail generated runs at >=30% harness-failure rate (#32 |
| `sn25:release:v2026.9.18-1049469180` | 25 | RELEASE | 2026-09-18T17:50:06Z | sn25 released v2026.9.18-1049469180 |
| `sn28:release:v0.4.19` | 28 | RELEASE | 2026-09-18T17:50:06Z | sn28 released v0.4.19 |
| `sn71:scoring_commit:2026-09-18T17:43:00Z` | 71 | SCORING_COMMIT | 2026-09-18T17:50:06Z | sn71 commit touches scoring: Clarify validator credentials and required scoring proxy setup |
| `sn74:release:release-20260918-164355` | 74 | RELEASE | 2026-09-18T17:50:06Z | sn74 released release-20260918-164355 |
| `sn90:scoring_commit:2026-09-18T17:37:57Z` | 90 | SCORING_COMMIT | 2026-09-18T17:50:06Z | sn90 commit touches scoring: docs: client-facing attestation of inference — API + verification gui… |
| `sn97:scoring_commit:2026-09-18T14:33:15Z` | 97 | SCORING_COMMIT | 2026-09-18T17:50:06Z | sn97 commit touches scoring: feat: Added scored_output the judge-facing text of a rollout |
| `sn111:scoring_commit:2026-09-18T15:54:53Z` | 111 | SCORING_COMMIT | 2026-09-18T17:50:06Z | sn111 commit touches scoring: docs: document funding-lineage miner selection |
| `sn15:release:v2.0.26: fix(proxy): fail over user-simu` | 15 | RELEASE | 2026-09-18T20:51:36Z | sn15 released v2.0.26: fix(proxy): fail over user-simulator from Mistral Small to Qwen on 429 |
| `sn15:scoring_commit:2026-09-18T18:17:14Z` | 15 | SCORING_COMMIT | 2026-09-18T20:51:36Z | sn15 commit touches scoring: validator: strict > infra boundary — 3/10 not infra, matches Backend … |
| `sn45:scoring_commit:2026-09-18T17:10:04Z` | 45 | SCORING_COMMIT | 2026-09-18T20:51:36Z | sn45 commit touches scoring: Score pool audits under a second matcher, recorded as the audit_v2 ch… |
| `sn71:scoring_commit:2026-09-18T19:06:48Z` | 71 | SCORING_COMMIT | 2026-09-18T20:51:36Z | sn71 commit touches scoring: Add Sep18 cancelled rerun302 with fresh judge scores |
| `sn78:scoring_commit:2026-09-18T20:19:20Z` | 78 | SCORING_COMMIT | 2026-09-18T20:51:36Z | sn78 commit touches scoring: Merge pull request #169 from Umi-BitSign/codex/portable-scoring-runti… |
| `sn25:release:v2026.9.18-1049702080` | 25 | RELEASE | 2026-09-18T23:15:17Z | sn25 released v2026.9.18-1049702080 |
| `sn71:scoring_commit:2026-09-18T22:13:21Z` | 71 | SCORING_COMMIT | 2026-09-18T23:15:17Z | sn71 commit touches scoring: Refresh protected verifier integrity manifest |
| `sn61:release:4.10.6` | 61 | RELEASE | 2026-09-19T01:25:22Z | sn61 released 4.10.6 |
| `sn61:scoring_commit:2026-09-19T01:16:23Z` | 61 | SCORING_COMMIT | 2026-09-19T01:25:22Z | sn61 commit touches scoring: deps: update ada_detection challenge image version to 3.0.4 |
| `sn71:scoring_commit:2026-09-19T00:42:55Z` | 71 | SCORING_COMMIT | 2026-09-19T01:25:22Z | sn71 commit touches scoring: Keep baseline source update independent of miner progress |
| `sn100:scoring_commit:2026-09-19T01:21:57Z` | 100 | SCORING_COMMIT | 2026-09-19T01:25:22Z | sn100 commit touches scoring: feat(bounty): python subnet with production bounty validator |
| `sn15:release:v2.0.27` | 15 | RELEASE | 2026-09-19T06:16:37Z | sn15 released v2.0.27 |
| `sn25:release:v2026.9.18-1049819730` | 25 | RELEASE | 2026-09-19T06:16:37Z | sn25 released v2026.9.18-1049819730 |
| `sn11:release:v0.7.0` | 11 | RELEASE | 2026-09-19T11:19:32Z | sn11 released v0.7.0 |
| `sn11:scoring_commit:2026-09-19T10:49:24Z` | 11 | SCORING_COMMIT | 2026-09-19T11:19:32Z | sn11 commit touches scoring: Season 2 (transition): routing-policy evaluation, policy sidecar + me… |
| `sn25:release:v2026.9.19-1050096260` | 25 | RELEASE | 2026-09-19T11:19:32Z | sn25 released v2026.9.19-1050096260 |
| `sn71:scoring_commit:2026-09-19T08:27:40Z` | 71 | SCORING_COMMIT | 2026-09-19T11:19:32Z | sn71 commit touches scoring: Pass saved stage evidence to Arena verifier |
| `sn81:scoring_commit:2026-09-18T22:15:30Z` | 81 | SCORING_COMMIT | 2026-09-19T11:19:32Z | sn81 commit touches scoring: fix(price): publish the target miners are actually held to |
| `sn11:scoring_commit:2026-09-19T12:33:44Z` | 11 | SCORING_COMMIT | 2026-09-19T14:37:19Z | sn11 commit touches scoring: docs(roadmap): the protocol (objective = environment + verifier, fit … |
| `sn71:scoring_commit:2026-09-19T11:23:50Z` | 71 | SCORING_COMMIT | 2026-09-19T14:37:19Z | sn71 commit touches scoring: Bind rerun316 to fixed scorer image |
| `sn11:scoring_commit:2026-09-19T15:53:33Z` | 11 | SCORING_COMMIT | 2026-09-19T17:29:09Z | sn11 commit touches scoring: docs: Season 2 pass over the public docs (README rewritten, MINER_GUI… |
| `sn34:scoring_commit:2026-09-19T17:11:58Z` | 34 | SCORING_COMMIT | 2026-09-19T17:29:09Z | sn34 commit touches scoring: Merge testnet into reward fix; retain release version 5.0.8 |
| `sn71:scoring_commit:2026-09-19T15:00:49Z` | 71 | SCORING_COMMIT | 2026-09-19T17:29:09Z | sn71 commit touches scoring: Route Luna across verified Azure regions |
| `sn25:scoring_commit:2026-09-19T19:29:32Z` | 25 | SCORING_COMMIT | 2026-09-19T19:37:26Z | sn25 commit touches scoring: Read retained validator runtime through reviewed history |
| `sn78:scoring_commit:2026-09-19T18:07:54Z` | 78 | SCORING_COMMIT | 2026-09-19T19:37:26Z | sn78 commit touches scoring: Bound uncontended dispatch by the longest miner chain |
| `sn11:scoring_commit:2026-09-19T20:43:16Z` | 11 | SCORING_COMMIT | 2026-09-19T21:48:06Z | sn11 commit touches scoring: Merge pull request #328 from trajectoryRL/agent/coding/restore-miner-… |
| `sn71:scoring_commit:2026-09-19T21:06:10Z` | 71 | SCORING_COMMIT | 2026-09-19T21:48:06Z | sn71 commit touches scoring: Retry proved miner-funded Responses throttles |
| `sn74:release:release-20260919-231145` | 74 | RELEASE | 2026-09-20T00:07:19Z | sn74 released release-20260919-231145 |
| `sn71:scoring_commit:2026-09-20T04:44:07Z` | 71 | SCORING_COMMIT | 2026-09-20T04:52:31Z | sn71 commit touches scoring: Seal September 20 verifier and runtime recovery |
| `sn71:scoring_commit:2026-09-20T09:37:09Z` | 71 | SCORING_COMMIT | 2026-09-20T09:45:43Z | sn71 commit touches scoring: Add Sep20 authority-preserving scoring replay |
| `sn78:scoring_commit:2026-09-20T06:21:53Z` | 78 | SCORING_COMMIT | 2026-09-20T09:45:43Z | sn78 commit touches scoring: Reuse validated reserved publications across a signing round |
| `sn91:scoring_commit:2026-09-20T07:38:07Z` | 91 | SCORING_COMMIT | 2026-09-20T09:45:43Z | sn91 commit touches scoring: trainer: one GPU type per manifest — drop and requeue challengers on … |
| `sn100:scoring_commit:2026-09-20T08:42:49Z` | 100 | SCORING_COMMIT | 2026-09-20T09:45:43Z | sn100 commit touches scoring: feat(bounty): activate proportional valid-report rewards |
| `sn11:release:v0.7.1` | 11 | RELEASE | 2026-09-20T13:45:04Z | sn11 released v0.7.1 |
| `sn21:scoring_commit:2026-09-20T12:01:04Z` | 21 | SCORING_COMMIT | 2026-09-20T13:45:04Z | sn21 commit touches scoring: admission: report the gate score per horizon and publish the gate num… |
| `sn71:scoring_commit:2026-09-20T13:21:27Z` | 71 | SCORING_COMMIT | 2026-09-20T13:45:04Z | sn71 commit touches scoring: test(arena): reject unrelated score failures |
| `sn71:scoring_commit:2026-09-20T16:53:41Z` | 71 | SCORING_COMMIT | 2026-09-20T17:03:14Z | sn71 commit touches scoring: Expose public scoring validator attribution |
| `sn71:scoring_commit:2026-09-20T18:33:27Z` | 71 | SCORING_COMMIT | 2026-09-20T19:25:08Z | sn71 commit touches scoring: Bind protected verifier manifest to committed audit fixes |
| `sn78:release:Open competition miner bundle v1 (feed c` | 78 | RELEASE | 2026-09-20T19:25:08Z | sn78 released Open competition miner bundle v1 (feed config + pinned artifacts) |
| `sn25:scoring_commit:2026-09-20T20:10:20Z` | 25 | SCORING_COMMIT | 2026-09-20T21:45:24Z | sn25 commit touches scoring: validator: admit reviewed successor on provisional recovery |
| `sn71:scoring_commit:2026-09-20T20:50:07Z` | 71 | SCORING_COMMIT | 2026-09-20T21:45:24Z | sn71 commit touches scoring: Fix normal validator scoring preflight and Webshare setup |
| `sn25:scoring_commit:2026-09-20T22:32:29Z` | 25 | SCORING_COMMIT | 2026-09-20T23:36:36Z | sn25 commit touches scoring: validator: preserve client key batch steering budget |
| `sn71:scoring_commit:2026-09-20T23:04:23Z` | 71 | SCORING_COMMIT | 2026-09-20T23:36:36Z | sn71 commit touches scoring: fix: keep unrelated verifier guidance out of source budget |
| `sn74:release:release-20260920-225500` | 74 | RELEASE | 2026-09-20T23:36:36Z | sn74 released release-20260920-225500 |
| `sn11:release:v0.7.3` | 11 | RELEASE | 2026-09-21T07:15:57Z | sn11 released v0.7.3 |
| `sn11:scoring_commit:2026-09-21T05:24:33Z` | 11 | SCORING_COMMIT | 2026-09-21T07:15:57Z | sn11 commit touches scoring: feat(validator): report health on the heartbeat, and never blame a mi… |
| `sn51:release:executor-v1.132` | 51 | RELEASE | 2026-09-21T07:15:57Z | sn51 released executor-v1.132 |
| `sn51:scoring_commit:2026-09-21T06:05:21Z` | 51 | SCORING_COMMIT | 2026-09-21T07:15:57Z | sn51 commit touches scoring: DAH-3677 - [P2] validator scrape: disk_type (nvme|ssd|hdd|unknown) of… |
| `sn71:scoring_commit:2026-09-21T04:53:08Z` | 71 | SCORING_COMMIT | 2026-09-21T07:15:57Z | sn71 commit touches scoring: Keep single contact role ID validation simple |
| `sn15:release:v2.0.28: chore(validator): split hosted ` | 15 | RELEASE | 2026-09-21T14:26:07Z | sn15 released v2.0.28: chore(validator): split hosted and local runtime profiles (#327) |
| `sn15:scoring_commit:2026-09-21T07:54:54Z` | 15 | SCORING_COMMIT | 2026-09-21T14:26:07Z | sn15 commit touches scoring: chore(validator): split hosted and local runtime profiles (#327) |
| `sn25:release:v2026.9.21-1051772980` | 25 | RELEASE | 2026-09-21T14:26:07Z | sn25 released v2026.9.21-1051772980 |
| `sn25:scoring_commit:2026-09-21T13:11:56Z` | 25 | SCORING_COMMIT | 2026-09-21T14:26:07Z | sn25 commit touches scoring: Avoid whole-fleet rendering in validator authority fixtures |
| `sn28:release:v0.4.20-dev` | 28 | RELEASE | 2026-09-21T14:26:07Z | sn28 released v0.4.20-dev |
| `sn28:scoring_commit:2026-09-21T12:54:53Z` | 28 | SCORING_COMMIT | 2026-09-21T14:26:07Z | sn28 commit touches scoring: chore: prepare KubeTEE FLUX miner release 0.4.20-dev |
| `sn38:scoring_commit:2026-09-21T13:25:08Z` | 38 | SCORING_COMMIT | 2026-09-21T14:26:07Z | sn38 commit touches scoring: fix: increase max_new_tokens from 50 to 100 for quality evaluation |
| `sn51:release:executor-v1.133` | 51 | RELEASE | 2026-09-21T14:26:07Z | sn51 released executor-v1.133 |
| `sn51:scoring_commit:2026-09-21T08:36:29Z` | 51 | SCORING_COMMIT | 2026-09-21T14:26:07Z | sn51 commit touches scoring: DAH-3678 - [P2] validator: explain add_public_keys failures on exitin… |
| `sn56:scoring_commit:2026-09-21T13:49:51Z` | 56 | SCORING_COMMIT | 2026-09-21T14:26:07Z | sn56 commit touches scoring: Keep prep-failed task rows when replacing tournament tasks (#1383) |
| `sn10:scoring_commit:2026-09-19T07:04:13Z` | 10 | SCORING_COMMIT | 2026-09-21T19:40:22Z | sn10 commit touches scoring: fix(bench): validate both baselines before candidate grading |
| `sn14:scoring_commit:2026-09-21T16:03:35Z` | 14 | SCORING_COMMIT | 2026-09-21T19:40:22Z | sn14 commit touches scoring: Merge pull request #120 from latent-to/release/reward-clock-inclusion… |
| `sn15:scoring_commit:2026-09-21T18:14:18Z` | 15 | SCORING_COMMIT | 2026-09-21T19:40:22Z | sn15 commit touches scoring: fix(validator): fail fast on invalid preflight config (#328) |
| `sn21:scoring_commit:2026-09-21T16:31:00Z` | 21 | SCORING_COMMIT | 2026-09-21T19:40:22Z | sn21 commit touches scoring: verify: the grouping recheck narrows to the same rows the run read |
| `sn26:scoring_commit:2026-09-21T13:03:03Z` | 26 | SCORING_COMMIT | 2026-09-21T19:40:22Z | sn26 commit touches scoring: feat: report model evaluations in the training/evaluations API schema |
| `sn28:release:v0.4.20` | 28 | RELEASE | 2026-09-21T19:40:22Z | sn28 released v0.4.20 |
| `sn28:scoring_commit:2026-09-21T16:14:48Z` | 28 | SCORING_COMMIT | 2026-09-21T19:40:22Z | sn28 commit touches scoring: chore(release): promote gm-miner 0.4.20 |
| `sn33:scoring_commit:2026-09-21T16:36:04Z` | 33 | SCORING_COMMIT | 2026-09-21T19:40:22Z | sn33 commit touches scoring: Merge pull request #137 from afterpartyai/adjust-put-task-ordering |
| `sn71:scoring_commit:2026-09-21T16:02:14Z` | 71 | SCORING_COMMIT | 2026-09-21T19:40:22Z | sn71 commit touches scoring: docs: use validators consistently in setup guides |
| `sn78:scoring_commit:2026-09-21T17:50:38Z` | 78 | SCORING_COMMIT | 2026-09-21T19:40:22Z | sn78 commit touches scoring: Validate continuous intake status and readiness in the public monitor… |
| `sn102:release:v0.6.3` | 102 | RELEASE | 2026-09-21T19:40:22Z | sn102 released v0.6.3 |
| `sn120:scoring_commit:2026-09-21T14:37:50Z` | 120 | SCORING_COMMIT | 2026-09-21T19:40:22Z | sn120 commit touches scoring: eval_client/validator: upstream 5xx / transport / stream-loss are inf… |
| `sn124:scoring_commit:2026-09-21T13:13:22Z` | 124 | SCORING_COMMIT | 2026-09-21T19:40:22Z | sn124 commit touches scoring: Merge pull request #159 from swarm-subnet/feature/ali/validator-image |
| `sn62:release:v0.3.6` | 62 | RELEASE | 2026-09-21T22:51:06Z | sn62 released v0.3.6 |
| `sn100:scoring_commit:2026-09-21T19:49:44Z` | 100 | SCORING_COMMIT | 2026-09-21T22:51:06Z | sn100 commit touches scoring: fix(validator): make gateway authoritative and peer consensus opt-in … |
| `sn120:scoring_commit:2026-09-21T21:22:20Z` | 120 | SCORING_COMMIT | 2026-09-21T22:51:06Z | sn120 commit touches scoring: coverage: unverified / errored_only cells are present, not gaps (51 r… |
| `sn25:release:v2026.9.21-1052359470` | 25 | RELEASE | 2026-09-22T01:35:19Z | sn25 released v2026.9.21-1052359470 |
| `sn78:release:Cohort 3: provisional scores (uncertifie` | 78 | RELEASE | 2026-09-22T01:35:19Z | sn78 released Cohort 3: provisional scores (uncertified) |
| `sn91:release:worker-v0.12.0` | 91 | RELEASE | 2026-09-22T01:35:19Z | sn91 released worker-v0.12.0 |
| `sn15:release:v2.0.29` | 15 | RELEASE | 2026-09-22T06:50:15Z | sn15 released v2.0.29 |
| `sn25:release:v2026.9.21-1052448720` | 25 | RELEASE | 2026-09-22T06:50:15Z | sn25 released v2026.9.21-1052448720 |
| `sn26:scoring_commit:2026-09-22T00:59:43Z` | 26 | SCORING_COMMIT | 2026-09-22T06:50:15Z | sn26 commit touches scoring: fix: commitment snapshot carries the model hash and is the sole verif… |
| `sn45:scoring_commit:2026-09-22T05:57:35Z` | 45 | SCORING_COMMIT | 2026-09-22T06:50:15Z | sn45 commit touches scoring: Owe a share again to a miner sent nothing for six epochs |
| `sn51:release:executor-v1.134` | 51 | RELEASE | 2026-09-22T06:50:15Z | sn51 released executor-v1.134 |
| `sn67:scoring_commit:2026-09-21T11:04:20Z` | 67 | SCORING_COMMIT | 2026-09-22T06:50:15Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20260921.post0 |
| `sn78:release:Cohort 4 miner connection inputs (policy` | 78 | RELEASE | 2026-09-22T06:50:15Z | sn78 released Cohort 4 miner connection inputs (policy 8) |
| `sn78:scoring_commit:2026-09-22T02:52:21Z` | 78 | SCORING_COMMIT | 2026-09-22T06:50:15Z | sn78 commit touches scoring: Publish current C4 miner setup and verified connection inputs (#191) |
| `sn1:release:v4.4.8` | 1 | RELEASE | 2026-09-22T17:19:59Z | sn1 released v4.4.8 |
| `sn25:scoring_commit:2026-09-22T12:54:58Z` | 25 | SCORING_COMMIT | 2026-09-22T17:19:59Z | sn25 commit touches scoring: Make miner fault recovery durable and reconcile ambiguous controls |
| `sn50:release:v1.13.0` | 50 | RELEASE | 2026-09-22T17:19:59Z | sn50 released v1.13.0 |
| `sn74:release:release-20260922-171907` | 74 | RELEASE | 2026-09-22T17:19:59Z | sn74 released release-20260922-171907 |
| `sn120:scoring_commit:2026-09-22T15:44:37Z` | 120 | SCORING_COMMIT | 2026-09-22T17:19:59Z | sn120 commit touches scoring: rollouts: affine_gen_v1 shared store/teacher/verify + genenv catalog … |
| `sn25:scoring_commit:2026-09-22T18:16:13Z` | 25 | SCORING_COMMIT | 2026-09-22T20:21:06Z | sn25 commit touches scoring: Resume bounded parallel miner fault controls across transient failures |
| `sn71:scoring_commit:2026-09-22T19:58:10Z` | 71 | SCORING_COMMIT | 2026-09-22T20:21:06Z | sn71 commit touches scoring: Verify shadow rounds under current Arena scheduling policy |
| `sn74:release:release-20260922-190530: spark-hermes: f` | 74 | RELEASE | 2026-09-22T20:21:06Z | sn74 released release-20260922-190530: spark-hermes: full scoring config (50% maintainer cut) (#1791) |
| `sn120:scoring_commit:2026-09-22T19:35:26Z` | 120 | SCORING_COMMIT | 2026-09-22T20:21:06Z | sn120 commit touches scoring: AA gap-fill go-live 1/2: affine_scitext e1 (202 teacher-verified vari… |
| `sn14:release:glm53-mock-submission-20260906: Merge m3` | 14 | RELEASE | 2026-09-22T23:08:21Z | sn14 released glm53-mock-submission-20260906: Merge m3-runtime-seed-restore into main (#108) |
| `sn56:scoring_commit:2026-09-22T22:03:29Z` | 56 | SCORING_COMMIT | 2026-09-22T23:08:21Z | sn56 commit touches scoring: Add Runpod evaluation backend via dstack (#1386) |
| `sn25:release:v2026.9.22-1053244730` | 25 | RELEASE | 2026-09-23T01:38:19Z | sn25 released v2026.9.22-1053244730 |
| `sn78:scoring_commit:2026-09-23T02:08:31Z` | 78 | SCORING_COMMIT | 2026-09-23T06:45:27Z | sn78 commit touches scoring: Retry interrupted miner downloads and redact clip capabilities from l… |
| `sn120:scoring_commit:2026-09-23T03:12:20Z` | 120 | SCORING_COMMIT | 2026-09-23T06:45:27Z | sn120 commit touches scoring: wvk 23 live 17:20 UTC: AGENTS.md snapshot + Discord live lines (first… |
| `sn28:scoring_commit:2026-09-23T11:46:58Z` | 28 | SCORING_COMMIT | 2026-09-23T12:19:18Z | sn28 commit touches scoring: ci: validate rendered Envoy configs with the pinned Envoy image |
| `sn51:scoring_commit:2026-09-23T11:44:49Z` | 51 | SCORING_COMMIT | 2026-09-23T12:19:18Z | sn51 commit touches scoring: DAH-3505 - [P2] validator: keep the Docker SDK's SSH session alive th… |
| `sn67:scoring_commit:2026-09-23T07:25:23Z` | 67 | SCORING_COMMIT | 2026-09-23T12:19:18Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20260923.post2 |
| `sn71:scoring_commit:2026-09-23T08:39:50Z` | 71 | SCORING_COMMIT | 2026-09-23T12:19:18Z | sn71 commit touches scoring: Document company-only validator compatibility |
| `sn97:scoring_commit:2026-09-23T11:59:47Z` | 97 | SCORING_COMMIT | 2026-09-23T12:19:18Z | sn97 commit touches scoring: fix: show tasks and trajectories on the detail page of every distribu… |
| `sn9:release:v4.13.2` | 9 | RELEASE | 2026-09-23T17:21:31Z | sn9 released v4.13.2 |
| `sn25:release:v2026.9.23-1053753970` | 25 | RELEASE | 2026-09-23T17:21:31Z | sn25 released v2026.9.23-1053753970 |
| `sn97:scoring_commit:2026-09-23T15:58:19Z` | 97 | SCORING_COMMIT | 2026-09-23T17:21:31Z | sn97 commit touches scoring: chore: show float score instead of a 0/1 mark |
| `sn120:scoring_commit:2026-09-23T12:45:56Z` | 120 | SCORING_COMMIT | 2026-09-23T17:21:31Z | sn120 commit touches scoring: Merge PR #3 (cursor/discord-mirror-1b92): ops: discord-mirror — archi… |
| `sn14:scoring_commit:2026-09-23T10:47:00Z` | 14 | SCORING_COMMIT | 2026-09-23T20:35:56Z | sn14 commit touches scoring: Drain evaluation workers and remove redundant recovery splits |
| `sn15:scoring_commit:2026-09-23T19:01:26Z` | 15 | SCORING_COMMIT | 2026-09-23T20:35:56Z | sn15 commit touches scoring: docs: correct local-test EnvPack size, families, and runtime/verifier… |
| `sn25:release:v2026.9.23-1053868550` | 25 | RELEASE | 2026-09-23T20:35:56Z | sn25 released v2026.9.23-1053868550 |
| `sn25:scoring_commit:2026-09-23T08:56:00Z` | 25 | SCORING_COMMIT | 2026-09-23T20:35:56Z | sn25 commit touches scoring: Preserve validator readback transport errors and request deadlines |
| `sn28:release:v0.4.21-dev` | 28 | RELEASE | 2026-09-23T20:35:56Z | sn28 released v0.4.21-dev |
| `sn28:scoring_commit:2026-09-23T20:17:29Z` | 28 | SCORING_COMMIT | 2026-09-23T20:35:56Z | sn28 commit touches scoring: feat(image): route Chutes -TEE requests through the attestation verif… |
| `sn40:readme_task_diff:b6863d625c3e10b3` | 40 | README_TASK_DIFF | 2026-09-17T00:48:02Z | sn40 README task/scoring sections changed |
| `sn56:readme_task_diff:ef6f6fe132bb0121` | 56 | README_TASK_DIFF | 2026-09-17T15:41:12Z | sn56 README task/scoring sections changed |
| `sn124:readme_task_diff:5c048f406be8cfd7` | 124 | README_TASK_DIFF | 2026-09-17T15:41:12Z | sn124 README task/scoring sections changed |
| `sn74:readme_task_diff:60b1b8229a2e5bd0` | 74 | README_TASK_DIFF | 2026-09-17T19:19:51Z | sn74 README task/scoring sections changed |
| `sn71:readme_task_diff:d96d81f0465762fa` | 71 | README_TASK_DIFF | 2026-09-18T23:15:17Z | sn71 README task/scoring sections changed |
| `sn11:readme_task_diff:9c29fc16d2b625fa` | 11 | README_TASK_DIFF | 2026-09-19T17:29:09Z | sn11 README task/scoring sections changed |
| `sn71:readme_task_diff:2291f503cdbc7816` | 71 | README_TASK_DIFF | 2026-09-20T21:45:24Z | sn71 README task/scoring sections changed |
| `sn26:readme_task_diff:aba46e7645c1a7ed` | 26 | README_TASK_DIFF | 2026-09-21T19:40:22Z | sn26 README task/scoring sections changed |
| `sn71:readme_task_diff:7438252e1ccc736e` | 71 | README_TASK_DIFF | 2026-09-21T19:40:22Z | sn71 README task/scoring sections changed |
| `sn66:readme_task_diff:8a675979eb4c570a` | 66 | README_TASK_DIFF | 2026-09-21T22:51:06Z | sn66 README task/scoring sections changed |
| `sn78:readme_task_diff:e68802e7781d35c0` | 78 | README_TASK_DIFF | 2026-09-22T06:50:15Z | sn78 README task/scoring sections changed |
| `sn28:readme_task_diff:b07f84dabcd1a3a1` | 28 | README_TASK_DIFF | 2026-09-23T20:35:56Z | sn28 README task/scoring sections changed |

## RESOLVED IN THIS WINDOW

_none_
