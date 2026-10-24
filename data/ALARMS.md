# ALARMS - generated 2026-10-24T17:39:12Z, block 9354997

window: first_seen in [2026-10-24T16:24:36Z, 2026-10-24T17:39:36Z)  (60 min interval + 15 min overlap)

Report ONLY the rows under NEW SINCE LAST RUN. Rows under STILL OPEN were
already reported in an earlier window and must not be re-alarmed.

## NEW SINCE LAST RUN

| event_id | netuid | class | severity | first_seen_utc | one_line |
|---|---|---|---|---|---|
| `sn71:scoring_commit:2026-10-24T17:11:03Z` | 71 | SCORING_COMMIT | P1 | 2026-10-24T17:39:36Z | sn71 commit touches scoring: Preserve source metadata and validated company evidence in Arena judgi |
| `sn78:scoring_commit:2026-10-24T14:56:17Z` | 78 | SCORING_COMMIT | P1 | 2026-10-24T17:39:36Z | sn78 commit touches scoring: Reset evaluation forecasts when evaluator processes change (#386) |

### detail

- **`sn71:scoring_commit:2026-10-24T17:11:03Z`** - sn71 commit touches scoring: Preserve source metadata and validated company evidence in Arena judgi
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn78:scoring_commit:2026-10-24T14:56:17Z`** - sn78 commit touches scoring: Reset evaluation forecasts when evaluator processes change (#386)
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.

## STILL OPEN (already reported - do not re-alarm)

| event_id | netuid | class | first_seen_utc | one_line |
|---|---|---|---|---|
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
| `sn7:burn_drop:0.986` | 7 | BURN_DROP | 2026-10-22T21:32:31Z | sn7 burn fell 0.990 -> 0.986 - miners can earn again |
| `sn81:burn_drop:0.810` | 81 | BURN_DROP | 2026-10-23T00:12:40Z | sn81 burn fell 0.996 -> 0.810 - miners can earn again |
| `sn104:burn_drop:0.000` | 104 | BURN_DROP | 2026-10-23T05:10:24Z | sn104 burn fell 1.000 -> 0.000 - miners can earn again |
| `sn6:weights_version_bump:4000` | 6 | WEIGHTS_VERSION_BUMP | 2026-10-23T15:20:36Z | sn6 weights_version 3000 -> 4000 |
| `sn7:burn_drop:0.985` | 7 | BURN_DROP | 2026-10-23T22:32:24Z | sn7 burn fell 0.991 -> 0.985 - miners can earn again |
| `sn76:burn_drop:0.987` | 76 | BURN_DROP | 2026-10-23T22:32:24Z | sn76 burn fell 0.992 -> 0.987 - miners can earn again |
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
| `sn6:readme_task_diff:f71150d0a859d726` | 6 | README_TASK_DIFF | 2026-10-22T18:06:27Z | sn6 README task/scoring sections changed |
| `sn76:readme_task_diff:f81741e228d9d939` | 76 | README_TASK_DIFF | 2026-10-22T18:06:27Z | sn76 README task/scoring sections changed |
| `sn117:readme_task_diff:61eefa3e188bb2fb` | 117 | README_TASK_DIFF | 2026-10-22T18:06:27Z | sn117 README task/scoring sections changed |
| `sn117:readme_task_diff:cb1456ccf5f760fc` | 117 | README_TASK_DIFF | 2026-10-23T15:20:36Z | sn117 README task/scoring sections changed |

## RESOLVED IN THIS WINDOW

_none_
