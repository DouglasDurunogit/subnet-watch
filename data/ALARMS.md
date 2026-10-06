# ALARMS - generated 2026-10-06T13:39:30Z, block 9224284

window: first_seen in [2026-10-06T12:24:56Z, 2026-10-06T13:39:56Z)  (60 min interval + 15 min overlap)

Report ONLY the rows under NEW SINCE LAST RUN. Rows under STILL OPEN were
already reported in an earlier window and must not be re-alarmed.

## NEW SINCE LAST RUN

| event_id | netuid | class | severity | first_seen_utc | one_line |
|---|---|---|---|---|---|
| `sn9:release:v4.13.5` | 9 | RELEASE | P1 | 2026-10-06T13:39:56Z | sn9 released v4.13.5 |
| `sn51:scoring_commit:2026-10-06T12:42:30Z` | 51 | SCORING_COMMIT | P1 | 2026-10-06T13:39:56Z | sn51 commit touches scoring: DAH-3980 - validator: start the host probes at SSH connect and restor… |
| `sn67:scoring_commit:2026-10-06T07:52:50Z` | 67 | SCORING_COMMIT | P1 | 2026-10-06T13:39:56Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20261006.post3 |
| `sn108:scoring_commit:2026-10-06T11:47:46Z` | 108 | SCORING_COMMIT | P1 | 2026-10-06T13:39:56Z | sn108 commit touches scoring: Minimum improvement comes from the challenge server (/validator/sync … |
| `sn116:scoring_commit:2026-10-06T13:03:10Z` | 116 | SCORING_COMMIT | P1 | 2026-10-06T13:39:56Z | sn116 commit touches scoring: Merge pull request #679 from carbonphysicsai/claude/validator-13d-l1-… |
| `sn120:scoring_commit:2026-10-06T12:39:56Z` | 120 | SCORING_COMMIT | P1 | 2026-10-06T13:39:56Z | sn120 commit touches scoring: Document actual E24 learning and partial verifier capacity rollout |

### detail

- **`sn9:release:v4.13.5`** - sn9 released v4.13.5
  - published 2026-10-06T12:20:36Z (was v4.13.4)
- **`sn51:scoring_commit:2026-10-06T12:42:30Z`** - sn51 commit touches scoring: DAH-3980 - validator: start the host probes at SSH connect and restor…
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn67:scoring_commit:2026-10-06T07:52:50Z`** - sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20261006.post3
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn108:scoring_commit:2026-10-06T11:47:46Z`** - sn108 commit touches scoring: Minimum improvement comes from the challenge server (/validator/sync …
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn116:scoring_commit:2026-10-06T13:03:10Z`** - sn116 commit touches scoring: Merge pull request #679 from carbonphysicsai/claude/validator-13d-l1-…
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn120:scoring_commit:2026-10-06T12:39:56Z`** - sn120 commit touches scoring: Document actual E24 learning and partial verifier capacity rollout
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.

## STILL OPEN (already reported - do not re-alarm)

| event_id | netuid | class | first_seen_utc | one_line |
|---|---|---|---|---|
| `sn20:burn_drop:0.799` | 20 | BURN_DROP | 2026-09-29T19:33:10Z | sn20 burn fell 1.000 -> 0.799 - miners can earn again |
| `sn46:burn_drop:0.726` | 46 | BURN_DROP | 2026-09-29T19:33:10Z | sn46 burn fell 1.000 -> 0.726 - miners can earn again |
| `sn117:burn_drop:0.978` | 117 | BURN_DROP | 2026-09-30T20:46:36Z | sn117 burn fell 1.000 -> 0.978 - miners can earn again |
| `sn22:burn_drop:0.809` | 22 | BURN_DROP | 2026-10-01T19:04:22Z | sn22 burn fell 1.000 -> 0.809 - miners can earn again |
| `sn22:burn_drop:0.820` | 22 | BURN_DROP | 2026-10-03T21:49:33Z | sn22 burn fell 1.000 -> 0.820 - miners can earn again |
| `sn30:burn_drop:0.000` | 30 | BURN_DROP | 2026-10-04T06:24:29Z | sn30 burn fell 1.000 -> 0.000 - miners can earn again |
| `sn116:burn_drop:0.000` | 116 | BURN_DROP | 2026-10-04T17:06:18Z | sn116 burn fell 1.000 -> 0.000 - miners can earn again |
| `sn85:burn_drop:0.000` | 85 | BURN_DROP | 2026-10-04T23:26:37Z | sn85 burn fell 1.000 -> 0.000 - miners can earn again |
| `sn15:release:v2.0.37: fix(proxy): sum inference count` | 15 | RELEASE | 2026-09-29T14:13:00Z | sn15 released v2.0.37: fix(proxy): sum inference counters across ProxyClient instances (#347) |
| `sn23:scoring_commit:2026-09-29T10:36:58Z` | 23 | SCORING_COMMIT | 2026-09-29T14:13:00Z | sn23 commit touches scoring: Merge pull request #57 from TrishoolAI/validator-build-fix |
| `sn46:release:v0.1.2` | 46 | RELEASE | 2026-09-29T14:13:00Z | sn46 released v0.1.2 |
| `sn46:scoring_commit:2026-09-28T17:59:23Z` | 46 | SCORING_COMMIT | 2026-09-29T14:13:00Z | sn46 commit touches scoring: Burn whatever leaves the miners the summary's signed USD target, pric… |
| `sn51:release:executor-v1.136` | 51 | RELEASE | 2026-09-29T14:13:00Z | sn51 released executor-v1.136 |
| `sn53:scoring_commit:2026-09-29T09:45:05Z` | 53 | SCORING_COMMIT | 2026-09-29T14:13:00Z | sn53 commit touches scoring: Merge pull request #51 from hanlinai/docs/miner-provider-docs-pointer |
| `sn69:scoring_commit:2026-09-26T06:16:04Z` | 69 | SCORING_COMMIT | 2026-09-29T14:13:00Z | sn69 commit touches scoring: Merge pull request #17 from HeraldMedia/miner-key-lifecycle |
| `sn94:scoring_commit:2026-09-29T13:47:13Z` | 94 | SCORING_COMMIT | 2026-09-29T14:13:00Z | sn94 commit touches scoring: Merge pull request #225 from skyrocket2026/feat/central-access-verifie |
| `sn1:release:v4.4.11` | 1 | RELEASE | 2026-09-29T19:33:10Z | sn1 released v4.4.11 |
| `sn5:scoring_commit:2026-09-29T16:00:26Z` | 5 | SCORING_COMMIT | 2026-09-29T19:33:10Z | sn5 commit touches scoring: Merge pull request #10 from hone-subnet-org/v3-repo-tasks |
| `sn15:release:v2.0.38: fix(agent): retry a 200 inferen` | 15 | RELEASE | 2026-09-29T19:33:10Z | sn15 released v2.0.38: fix(agent): retry a 200 inference response whose body is not JSON (#348) |
| `sn20:scoring_commit:2026-09-29T18:56:24Z` | 20 | SCORING_COMMIT | 2026-09-29T19:33:10Z | sn20 commit touches scoring: Separate website from the public subnet and retain validator evidence… |
| `sn41:scoring_commit:2026-09-28T18:49:08Z` | 41 | SCORING_COMMIT | 2026-09-29T19:33:10Z | sn41 commit touches scoring: pillar scoring updates around market-relative brier. updating baselin… |
| `sn81:scoring_commit:2026-09-29T15:04:56Z` | 81 | SCORING_COMMIT | 2026-09-29T19:33:10Z | sn81 commit touches scoring: docs(corpus): ledger v2 migration, verify and rollback in the launch … |
| `sn94:scoring_commit:2026-09-29T14:06:52Z` | 94 | SCORING_COMMIT | 2026-09-29T19:33:10Z | sn94 commit touches scoring: cli: export the validator's #256 policy file from the signed list |
| `sn20:scoring_commit:2026-09-29T23:10:34Z` | 20 | SCORING_COMMIT | 2026-09-29T23:14:10Z | sn20 commit touches scoring: Bind evaluator publications to their window policy |
| `sn5:scoring_commit:2026-09-29T22:46:58Z` | 5 | SCORING_COMMIT | 2026-09-30T02:18:29Z | sn5 commit touches scoring: Test this release against the previous release's miner and validator |
| `sn15:release:v2.0.39: Translate live Chutes model IDs` | 15 | RELEASE | 2026-09-30T02:18:29Z | sn15 released v2.0.39: Translate live Chutes model IDs on OpenRouter runs (#345) |
| `sn20:scoring_commit:2026-09-30T00:12:27Z` | 20 | SCORING_COMMIT | 2026-09-30T02:18:29Z | sn20 commit touches scoring: Record foreground waits for prefetched challengers |
| `sn94:scoring_commit:2026-09-30T01:23:22Z` | 94 | SCORING_COMMIT | 2026-09-30T02:18:29Z | sn94 commit touches scoring: feat(snp): emit the validator policy entry an observed guest needs (#… |
| `sn20:scoring_commit:2026-09-30T08:36:21Z` | 20 | SCORING_COMMIT | 2026-09-30T08:50:53Z | sn20 commit touches scoring: Keep validator credentials out of local GPU subprocesses |
| `sn51:release:lium-core-v0.1.13` | 51 | RELEASE | 2026-09-30T08:50:53Z | sn51 released lium-core-v0.1.13 |
| `sn51:scoring_commit:2026-09-30T08:43:37Z` | 51 | SCORING_COMMIT | 2026-09-30T08:50:53Z | sn51 commit touches scoring: DAH-3890 - [P1] validator: unique obfuscated key names in the machine… |
| `sn91:scoring_commit:2026-09-30T07:36:25Z` | 91 | SCORING_COMMIT | 2026-09-30T08:50:53Z | sn91 commit touches scoring: Merge pull request #344 from TensorLink-AI/fix/verify-bench-queue |
| `sn20:scoring_commit:2026-09-30T09:55:00Z` | 20 | SCORING_COMMIT | 2026-09-30T15:53:11Z | sn20 commit touches scoring: Isolate GPU model execution and enforce validator download stake floor |
| `sn25:scoring_commit:2026-09-30T07:07:19Z` | 25 | SCORING_COMMIT | 2026-09-30T15:53:11Z | sn25 commit touches scoring: Build mips64 miner targets as softfloat |
| `sn51:scoring_commit:2026-09-30T13:04:53Z` | 51 | SCORING_COMMIT | 2026-09-30T15:53:11Z | sn51 commit touches scoring: NO-TICKET - [P2] validator: log repeated check outcomes at DEBUG, cha… |
| `sn97:scoring_commit:2026-09-29T15:51:34Z` | 97 | SCORING_COMMIT | 2026-09-30T15:53:11Z | sn97 commit touches scoring: fix: accept submits like the bench in eval and pre-eval, stop scoring… |
| `sn111:scoring_commit:2026-09-29T23:46:11Z` | 111 | SCORING_COMMIT | 2026-09-30T15:53:11Z | sn111 commit touches scoring: feat(validator): wait for due canonical batches |
| `sn5:scoring_commit:2026-09-30T18:36:40Z` | 5 | SCORING_COMMIT | 2026-09-30T20:46:36Z | sn5 commit touches scoring: Merge pull request #13 from hone-subnet-org/terminal-task-fixture |
| `sn8:scoring_commit:2026-09-24T08:39:47Z` | 8 | SCORING_COMMIT | 2026-09-30T20:46:36Z | sn8 commit touches scoring: disable miner daily summary (#934) |
| `sn41:scoring_commit:2026-09-30T18:16:49Z` | 41 | SCORING_COMMIT | 2026-09-30T20:46:36Z | sn41 commit touches scoring: Updates to handling excess miner emissions and burn |
| `sn81:scoring_commit:2026-09-30T18:12:28Z` | 81 | SCORING_COMMIT | 2026-09-30T20:46:36Z | sn81 commit touches scoring: fix(corpus): next on a free job is a 409, and the miner stops asking |
| `sn108:scoring_commit:2026-09-30T14:03:10Z` | 108 | SCORING_COMMIT | 2026-09-30T20:46:36Z | sn108 commit touches scoring: Validator: periodic weight status line, change-only state logs, 409 a… |
| `sn117:release:everycli v0.1.3` | 117 | RELEASE | 2026-09-30T20:46:36Z | sn117 released everycli v0.1.3 |
| `sn117:scoring_commit:2026-09-30T17:20:20Z` | 117 | SCORING_COMMIT | 2026-09-30T20:46:36Z | sn117 commit touches scoring: feat: simplify miner onboarding and API key management |
| `sn71:scoring_commit:2026-09-30T23:08:42Z` | 71 | SCORING_COMMIT | 2026-10-01T00:12:52Z | sn71 commit touches scoring: Bind October verifier evidence release |
| `sn74:release:release-20260930-235444` | 74 | RELEASE | 2026-10-01T00:12:52Z | sn74 released release-20260930-235444 |
| `sn78:scoring_commit:2026-09-30T23:10:44Z` | 78 | SCORING_COMMIT | 2026-10-01T00:12:52Z | sn78 commit touches scoring: Separate miner transport signer from cohort reviewers |
| `sn117:release:everycli v0.1.4` | 117 | RELEASE | 2026-10-01T00:12:52Z | sn117 released everycli v0.1.4 |
| `sn25:release:v2026.9.30-1060350310` | 25 | RELEASE | 2026-10-01T06:20:47Z | sn25 released v2026.9.30-1060350310 |
| `sn25:scoring_commit:2026-10-01T04:51:10Z` | 25 | SCORING_COMMIT | 2026-10-01T06:20:47Z | sn25 commit touches scoring: Verify and aggregate pinned mainnet image receipts offline |
| `sn71:scoring_commit:2026-10-01T05:00:38Z` | 71 | SCORING_COMMIT | 2026-10-01T06:20:47Z | sn71 commit touches scoring: Bind protected workflows to verifier recovery source |
| `sn74:release:release-20261001-004737` | 74 | RELEASE | 2026-10-01T06:20:47Z | sn74 released release-20261001-004737 |
| `sn78:scoring_commit:2026-10-01T04:50:44Z` | 78 | SCORING_COMMIT | 2026-10-01T06:20:47Z | sn78 commit touches scoring: Publish C5 miner inputs and connection guide (#198) |
| `sn120:scoring_commit:2026-10-01T06:19:24Z` | 120 | SCORING_COMMIT | 2026-10-01T06:20:47Z | sn120 commit touches scoring: Verify controlled native Agent tool rollouts in isolated images |
| `sn13:release:Release v1.18.73` | 13 | RELEASE | 2026-10-01T13:42:59Z | sn13 released Release v1.18.73 |
| `sn13:scoring_commit:2026-09-30T21:26:32Z` | 13 | SCORING_COMMIT | 2026-10-01T13:42:59Z | sn13 commit touches scoring: docs(agents): rewrite from code-verified review; add on-demand path |
| `sn22:scoring_commit:2026-10-01T13:39:51Z` | 22 | SCORING_COMMIT | 2026-10-01T13:42:59Z | sn22 commit touches scoring: fix(validators): take an upload before waiting on its seed, so parall… |
| `sn25:release:v2026.10.1-1060587890` | 25 | RELEASE | 2026-10-01T13:42:59Z | sn25 released v2026.10.1-1060587890 |
| `sn51:release:validator-v2026.10.01` | 51 | RELEASE | 2026-10-01T13:42:59Z | sn51 released validator-v2026.10.01 |
| `sn51:scoring_commit:2026-10-01T12:36:27Z` | 51 | SCORING_COMMIT | 2026-10-01T13:42:59Z | sn51 commit touches scoring: NO-TICKET - [P2] validator: remove INSPECTOR_ENFORCE_ENABLED, finding… |
| `sn71:scoring_commit:2026-10-01T06:39:33Z` | 71 | SCORING_COMMIT | 2026-10-01T13:42:59Z | sn71 commit touches scoring: Release October 1 provider hold with exact score retries |
| `sn81:scoring_commit:2026-10-01T06:33:05Z` | 81 | SCORING_COMMIT | 2026-10-01T13:42:59Z | sn81 commit touches scoring: docs(design): evaluation on SN81, rulings of the v2 fix pass |
| `sn91:scoring_commit:2026-10-01T11:42:23Z` | 91 | SCORING_COMMIT | 2026-10-01T13:42:59Z | sn91 commit touches scoring: Merge pull request #347 from TensorLink-AI/fix/validator-startup-rest… |
| `sn94:scoring_commit:2026-10-01T10:29:20Z` | 94 | SCORING_COMMIT | 2026-10-01T13:42:59Z | sn94 commit touches scoring: snp friend probe: an unavailable AMD verifier is inconclusive, never … |
| `sn120:scoring_commit:2026-10-01T13:03:37Z` | 120 | SCORING_COMMIT | 2026-10-01T13:42:59Z | sn120 commit touches scoring: Document original Trivia Abstain tasks and distinct native grading co… |
| `sn20:scoring_commit:2026-10-01T17:03:24Z` | 20 | SCORING_COMMIT | 2026-10-01T19:04:22Z | sn20 commit touches scoring: Clarify legacy and event scoring in the benchmark guide |
| `sn46:release:v0.1.3` | 46 | RELEASE | 2026-10-01T19:04:22Z | sn46 released v0.1.3 |
| `sn46:scoring_commit:2026-10-01T15:23:12Z` | 46 | SCORING_COMMIT | 2026-10-01T19:04:22Z | sn46 commit touches scoring: sn46-validator update: signed, scheduled self-update with rollback |
| `sn71:scoring_commit:2026-10-01T18:50:32Z` | 71 | SCORING_COMMIT | 2026-10-01T19:04:22Z | sn71 commit touches scoring: Preserve verified rebrand homepage evidence path |
| `sn81:scoring_commit:2026-10-01T18:50:51Z` | 81 | SCORING_COMMIT | 2026-10-01T19:04:22Z | sn81 commit touches scoring: Merge pull request #293 from reliquadotai/feat/corpus-miner-status |
| `sn108:scoring_commit:2026-10-01T13:52:10Z` | 108 | SCORING_COMMIT | 2026-10-01T19:04:22Z | sn108 commit touches scoring: Validator logs explain the MIN_IMPROVEMENT_PERCENT decision: % gain o… |
| `sn117:release:everycli v0.2.1` | 117 | RELEASE | 2026-10-01T19:04:22Z | sn117 released everycli v0.2.1 |
| `sn117:scoring_commit:2026-10-01T16:42:56Z` | 117 | SCORING_COMMIT | 2026-10-01T19:04:22Z | sn117 commit touches scoring: fix: explain missing miner profiles in status and doctor |
| `sn120:scoring_commit:2026-10-01T18:05:55Z` | 120 | SCORING_COMMIT | 2026-10-01T19:04:22Z | sn120 commit touches scoring: Record independently verified balanced checkpoint publication |
| `sn14:release:GLM crowned baseline source — 2026-10-01` | 14 | RELEASE | 2026-10-01T23:09:13Z | sn14 released GLM crowned baseline source — 2026-10-01 |
| `sn15:release:v2.0.40: Composed situation tasks: valid` | 15 | RELEASE | 2026-10-01T23:09:13Z | sn15 released v2.0.40: Composed situation tasks: validator, proxy and local testing |
| `sn15:scoring_commit:2026-10-01T20:36:02Z` | 15 | SCORING_COMMIT | 2026-10-01T23:09:13Z | sn15 commit touches scoring: Composed situation tasks: validator, proxy and local testing |
| `sn20:scoring_commit:2026-10-01T19:18:50Z` | 20 | SCORING_COMMIT | 2026-10-01T23:09:13Z | sn20 commit touches scoring: Export signed closed-window scores without serving media or model out… |
| `sn62:release:v0.3.9` | 62 | RELEASE | 2026-10-01T23:09:13Z | sn62 released v0.3.9 |
| `sn78:scoring_commit:2026-10-01T20:28:39Z` | 78 | SCORING_COMMIT | 2026-10-01T23:09:13Z | sn78 commit touches scoring: Keep miner upgrades cohort-neutral |
| `sn81:scoring_commit:2026-10-01T20:32:20Z` | 81 | SCORING_COMMIT | 2026-10-01T23:09:13Z | sn81 commit touches scoring: Merge pull request #294 from reliquadotai/feat/corpus-tasks-route |
| `sn120:scoring_commit:2026-10-01T22:38:51Z` | 120 | SCORING_COMMIT | 2026-10-01T23:09:13Z | sn120 commit touches scoring: Document independently verified Wiki signed resource stage |
| `sn14:scoring_commit:2026-10-02T02:05:43Z` | 14 | SCORING_COMMIT | 2026-10-02T02:26:04Z | sn14 commit touches scoring: Show consumed evaluation credits in dashboard fee labels (#136) |
| `sn111:release:v1.0.1` | 111 | RELEASE | 2026-10-02T02:26:04Z | sn111 released v1.0.1 |
| `sn120:scoring_commit:2026-10-02T00:37:49Z` | 120 | SCORING_COMMIT | 2026-10-02T02:26:04Z | sn120 commit touches scoring: Reproduce per-task Pydantic proposal controls with fresh native replay |
| `sn51:release:validator-v2026.10.02` | 51 | RELEASE | 2026-10-02T08:53:07Z | sn51 released validator-v2026.10.02 |
| `sn51:scoring_commit:2026-10-02T08:25:54Z` | 51 | SCORING_COMMIT | 2026-10-02T08:53:07Z | sn51 commit touches scoring: NO-TICKET - [P1] validator: a shell lost mid-check sends its reason c… |
| `sn67:scoring_commit:2026-10-02T04:02:08Z` | 67 | SCORING_COMMIT | 2026-10-02T08:53:07Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20261002.post1 |
| `sn71:scoring_commit:2026-10-02T08:39:30Z` | 71 | SCORING_COMMIT | 2026-10-02T08:53:07Z | sn71 commit touches scoring: Merge pull request #200 from leadpoet/codex/progressive-model-scores |
| `sn78:scoring_commit:2026-10-02T05:43:42Z` | 78 | SCORING_COMMIT | 2026-10-02T08:53:07Z | sn78 commit touches scoring: Point C5 miner upgrade at enrollment runtime (#202) |
| `sn81:scoring_commit:2026-10-02T05:56:09Z` | 81 | SCORING_COMMIT | 2026-10-02T08:53:07Z | sn81 commit touches scoring: Merge pull request #297 from reliquadotai/perf/corpus-tasks-instant |
| `sn91:scoring_commit:2026-10-02T04:47:21Z` | 91 | SCORING_COMMIT | 2026-10-02T08:53:07Z | sn91 commit touches scoring: Receipts verify across code versions; a stale receipt king is never s… |
| `sn117:release:everycli v0.2.2` | 117 | RELEASE | 2026-10-02T08:53:07Z | sn117 released everycli v0.2.2 |
| `sn25:scoring_commit:2026-10-02T12:24:50Z` | 25 | SCORING_COMMIT | 2026-10-02T15:44:59Z | sn25 commit touches scoring: Record scoped native miner monitor and backup custody qualification |
| `sn51:release:validator-v2026.10.02.2` | 51 | RELEASE | 2026-10-02T15:44:59Z | sn51 released validator-v2026.10.02.2 |
| `sn51:scoring_commit:2026-10-02T14:46:23Z` | 51 | SCORING_COMMIT | 2026-10-02T15:44:59Z | sn51 commit touches scoring: DAH-3980 - validator: check a present Docker Hub image's tag from the… |
| `sn71:scoring_commit:2026-10-02T13:19:39Z` | 71 | SCORING_COMMIT | 2026-10-02T15:44:59Z | sn71 commit touches scoring: Verify extended recovery schedule on migration replay |
| `sn74:release:release-20261002-144641` | 74 | RELEASE | 2026-10-02T15:44:59Z | sn74 released release-20261002-144641 |
| `sn78:scoring_commit:2026-10-02T07:14:11Z` | 78 | SCORING_COMMIT | 2026-10-02T15:44:59Z | sn78 commit touches scoring: Alert when successor validators stop reconciling |
| `sn81:scoring_commit:2026-10-02T09:28:38Z` | 81 | SCORING_COMMIT | 2026-10-02T15:44:59Z | sn81 commit touches scoring: fix(corpus): auditor miners.json on the judge client; settle reads en… |
| `sn89:scoring_commit:2026-10-02T13:45:26Z` | 89 | SCORING_COMMIT | 2026-10-02T15:44:59Z | sn89 commit touches scoring: hf: diversity-blocked qualified miners keep the probation dust floor |
| `sn97:scoring_commit:2026-10-02T14:26:23Z` | 97 | SCORING_COMMIT | 2026-10-02T15:44:59Z | sn97 commit touches scoring: fix: swesmith tasks are served as one upstream commit, and git show r… |
| `sn120:scoring_commit:2026-10-02T15:06:50Z` | 120 | SCORING_COMMIT | 2026-10-02T15:44:59Z | sn120 commit touches scoring: Bootstrap external MATH miners from authority-approved source |
| `sn1:release:v4.4.12` | 1 | RELEASE | 2026-10-02T20:11:07Z | sn1 released v4.4.12 |
| `sn15:scoring_commit:2026-10-02T18:43:36Z` | 15 | SCORING_COMMIT | 2026-10-02T20:11:07Z | sn15 commit touches scoring: Capture cached input tokens in private evaluation usage |
| `sn25:scoring_commit:2026-10-02T19:50:40Z` | 25 | SCORING_COMMIT | 2026-10-02T20:11:07Z | sn25 commit touches scoring: Preserve qualification headroom with verified inactive cache reclaim |
| `sn71:scoring_commit:2026-10-02T17:54:51Z` | 71 | SCORING_COMMIT | 2026-10-02T20:11:07Z | sn71 commit touches scoring: Archive October 1 optional-signal scores for full rejudge |
| `sn81:scoring_commit:2026-10-02T15:52:08Z` | 81 | SCORING_COMMIT | 2026-10-02T20:11:07Z | sn81 commit touches scoring: feat(corpus): a GPU process that scores every judge's audits |
| `sn94:scoring_commit:2026-10-02T05:21:24Z` | 94 | SCORING_COMMIT | 2026-10-02T20:11:07Z | sn94 commit touches scoring: Fix fork sentinel command verification (#258) |
| `sn104:scoring_commit:2026-09-30T10:52:16Z` | 104 | SCORING_COMMIT | 2026-10-02T20:11:07Z | sn104 commit touches scoring: Merge pull request #15 from taostatus/feat/security-validator |
| `sn120:scoring_commit:2026-10-02T20:02:41Z` | 120 | SCORING_COMMIT | 2026-10-02T20:11:07Z | sn120 commit touches scoring: Project the separated math pilot and publish verified corpus assets |
| `sn15:scoring_commit:2026-10-02T20:29:49Z` | 15 | SCORING_COMMIT | 2026-10-02T23:56:15Z | sn15 commit touches scoring: Validator v2.0.41: per-event market notices, preflight replay parity … |
| `sn71:scoring_commit:2026-10-02T23:10:33Z` | 71 | SCORING_COMMIT | 2026-10-02T23:56:15Z | sn71 commit touches scoring: Reuse exact Arena verifier requests through the provider ledger |
| `sn81:scoring_commit:2026-10-02T21:06:44Z` | 81 | SCORING_COMMIT | 2026-10-02T23:56:15Z | sn81 commit touches scoring: fix(corpus): bound the audits of one judge pass; log each scoring cal… |
| `sn117:release:everycli v0.2.3` | 117 | RELEASE | 2026-10-02T23:56:15Z | sn117 released everycli v0.2.3 |
| `sn120:scoring_commit:2026-10-02T23:47:07Z` | 120 | SCORING_COMMIT | 2026-10-02T23:56:15Z | sn120 commit touches scoring: Prepare public dashboard projection for corrected H200 miner pilot |
| `sn71:scoring_commit:2026-10-03T01:31:39Z` | 71 | SCORING_COMMIT | 2026-10-03T05:11:26Z | sn71 commit touches scoring: Preserve concurrent verifier lease correction |
| `sn81:scoring_commit:2026-10-03T03:49:09Z` | 81 | SCORING_COMMIT | 2026-10-03T05:11:26Z | sn81 commit touches scoring: perf(corpus): verify drand rounds by BLS here, take the fastest relay… |
| `sn120:scoring_commit:2026-10-03T04:24:40Z` | 120 | SCORING_COMMIT | 2026-10-03T05:11:26Z | sn120 commit touches scoring: Record verified public full-model update and checkpoint publication |
| `sn15:release:Validator v2.1.0: runtime contract on cl` | 15 | RELEASE | 2026-10-03T10:31:46Z | sn15 released Validator v2.1.0: runtime contract on claim and delivery load (#361) |
| `sn15:scoring_commit:2026-10-03T07:47:51Z` | 15 | SCORING_COMMIT | 2026-10-03T10:31:46Z | sn15 commit touches scoring: Validator v2.1.0: runtime contract on claim and delivery load (#361) |
| `sn25:scoring_commit:2026-10-03T09:53:42Z` | 25 | SCORING_COMMIT | 2026-10-03T10:31:46Z | sn25 commit touches scoring: Verify HTTP retry controls and preserve qualification disk headroom |
| `sn71:scoring_commit:2026-10-03T10:07:15Z` | 71 | SCORING_COMMIT | 2026-10-03T10:31:46Z | sn71 commit touches scoring: fix: prefer verified exact homepage brand over title |
| `sn120:scoring_commit:2026-10-03T09:11:08Z` | 120 | SCORING_COMMIT | 2026-10-03T10:31:46Z | sn120 commit touches scoring: Document verified successor, external miner participation and honest … |
| `sn71:scoring_commit:2026-10-03T13:45:43Z` | 71 | SCORING_COMMIT | 2026-10-03T14:57:25Z | sn71 commit touches scoring: Bind unverified homepage context to observed identity and card company |
| `sn81:scoring_commit:2026-10-03T12:08:37Z` | 81 | SCORING_COMMIT | 2026-10-03T14:57:25Z | sn81 commit touches scoring: Merge pull request #308 from reliquadotai/feat/eval-validator-mode |
| `sn120:scoring_commit:2026-10-03T14:53:57Z` | 120 | SCORING_COMMIT | 2026-10-03T14:57:25Z | sn120 commit touches scoring: Keep original audit source pins across approved reward upgrades |
| `sn120:scoring_commit:2026-10-03T18:20:16Z` | 120 | SCORING_COMMIT | 2026-10-03T18:40:15Z | sn120 commit touches scoring: Record verified five-role source staging and ongoing independent audit |
| `sn11:release:v0.7.4` | 11 | RELEASE | 2026-10-03T21:49:33Z | sn11 released v0.7.4 |
| `sn11:scoring_commit:2026-10-03T18:55:49Z` | 11 | SCORING_COMMIT | 2026-10-03T21:49:33Z | sn11 commit touches scoring: [coding-agent] validator: weight-only by default, eval behind EVAL_EN… |
| `sn78:scoring_commit:2026-10-03T14:17:42Z` | 78 | SCORING_COMMIT | 2026-10-03T21:49:33Z | sn78 commit touches scoring: Reject partial successor reward ownership |
| `sn71:scoring_commit:2026-10-04T00:23:22Z` | 71 | SCORING_COMMIT | 2026-10-04T00:33:21Z | sn71 commit touches scoring: Merge pull request #205 from leadpoet/codex/daily-miner-admission |
| `sn81:scoring_commit:2026-10-03T15:52:28Z` | 81 | SCORING_COMMIT | 2026-10-04T00:33:21Z | sn81 commit touches scoring: feat(corpus): new jobs settle by period; tasks close frees a finished… |
| `sn25:scoring_commit:2026-10-04T06:18:37Z` | 25 | SCORING_COMMIT | 2026-10-04T06:24:29Z | sn25 commit touches scoring: Retain complete model success and actual validator reconnect qualific… |
| `sn26:scoring_commit:2026-10-04T03:18:36Z` | 26 | SCORING_COMMIT | 2026-10-04T06:24:29Z | sn26 commit touches scoring: feat: rank scanning miners by stake-weighted consensus rank instead o… |
| `sn71:scoring_commit:2026-10-04T05:56:54Z` | 71 | SCORING_COMMIT | 2026-10-04T06:24:29Z | sn71 commit touches scoring: Merge pull request #209 from leadpoet/codex/arena-score-host-recovery… |
| `sn120:scoring_commit:2026-10-04T03:50:26Z` | 120 | SCORING_COMMIT | 2026-10-04T06:24:29Z | sn120 commit touches scoring: Preserve checkpoint read access through post-epoch verification |
| `sn25:scoring_commit:2026-10-04T12:40:19Z` | 25 | SCORING_COMMIT | 2026-10-04T12:45:39Z | sn25 commit touches scoring: Retain passing signed-history and terminal-custody validator tests |
| `sn28:release:v0.4.25` | 28 | RELEASE | 2026-10-04T12:45:39Z | sn28 released v0.4.25 |
| `sn28:scoring_commit:2026-10-04T08:55:13Z` | 28 | SCORING_COMMIT | 2026-10-04T12:45:39Z | sn28 commit touches scoring: Handle scheduled miner price increases as successful declarations (#29 |
| `sn51:scoring_commit:2026-10-04T09:18:47Z` | 51 | SCORING_COMMIT | 2026-10-04T12:45:39Z | sn51 commit touches scoring: validator: keep a banned node verified while a live rental is running… |
| `sn71:scoring_commit:2026-10-04T07:34:40Z` | 71 | SCORING_COMMIT | 2026-10-04T12:45:39Z | sn71 commit touches scoring: Bind local verifier fix to protected workflow manifest |
| `sn78:scoring_commit:2026-10-04T08:39:44Z` | 78 | SCORING_COMMIT | 2026-10-04T12:45:39Z | sn78 commit touches scoring: Stabilize checkpoint cache verification |
| `sn81:scoring_commit:2026-10-04T08:17:34Z` | 81 | SCORING_COMMIT | 2026-10-04T12:45:39Z | sn81 commit touches scoring: docs(corpus): episode jobs on the split validator, and how to deploy i |
| `sn120:scoring_commit:2026-10-04T09:29:43Z` | 120 | SCORING_COMMIT | 2026-10-04T12:45:39Z | sn120 commit touches scoring: Document guarded covered-training handoff and verify prospective dead… |
| `sn9:release:v4.13.4` | 9 | RELEASE | 2026-10-04T17:06:18Z | sn9 released v4.13.4 |
| `sn25:scoring_commit:2026-10-04T16:31:25Z` | 25 | SCORING_COMMIT | 2026-10-04T17:06:18Z | sn25 commit touches scoring: Verify completed original capture and Yuma Rust regression controls |
| `sn120:scoring_commit:2026-10-04T14:42:39Z` | 120 | SCORING_COMMIT | 2026-10-04T17:06:18Z | sn120 commit touches scoring: Update public miner setup for signed forced sampling epochs |
| `sn25:scoring_commit:2026-10-04T19:11:16Z` | 25 | SCORING_COMMIT | 2026-10-04T20:09:59Z | sn25 commit touches scoring: Record final miner qualification and remaining recovery hardening |
| `sn120:scoring_commit:2026-10-04T19:54:42Z` | 120 | SCORING_COMMIT | 2026-10-04T20:09:59Z | sn120 commit touches scoring: Authorize qualified verifier additions without changing epoch contract |
| `sn120:scoring_commit:2026-10-04T23:19:10Z` | 120 | SCORING_COMMIT | 2026-10-04T23:26:37Z | sn120 commit touches scoring: Recommend bounded per-task mining search without changing the sampler |
| `sn15:release:Validator v2.2.0: oro-env-runtime 3.3.0,` | 15 | RELEASE | 2026-10-05T02:18:48Z | sn15 released Validator v2.2.0: oro-env-runtime 3.3.0, runtime contract 2 (#362) |
| `sn15:scoring_commit:2026-10-05T01:34:33Z` | 15 | SCORING_COMMIT | 2026-10-05T02:18:48Z | sn15 commit touches scoring: Validator v2.2.0: oro-env-runtime 3.3.0, runtime contract 2 (#362) |
| `sn120:scoring_commit:2026-10-05T01:33:05Z` | 120 | SCORING_COMMIT | 2026-10-05T02:18:48Z | sn120 commit touches scoring: Reuse checkpoint evaluation when only source download capability chang |
| `sn49:scoring_commit:2026-09-30T00:44:13Z` | 49 | SCORING_COMMIT | 2026-10-05T09:25:44Z | sn49 commit touches scoring: Upgrade validator sandbox to Isaac Sim 6.1 / Isaac Lab 3.0.0 |
| `sn51:scoring_commit:2026-10-05T09:19:32Z` | 51 | SCORING_COMMIT | 2026-10-05T09:25:44Z | sn51 commit touches scoring: NO-TICKET - [P2] Validator scrape: record the host's Sysbox version (… |
| `sn71:scoring_commit:2026-10-05T04:23:20Z` | 71 | SCORING_COMMIT | 2026-10-05T09:25:44Z | sn71 commit touches scoring: Document resource-safe model capacity for all validators |
| `sn108:scoring_commit:2026-10-05T07:32:21Z` | 108 | SCORING_COMMIT | 2026-10-05T09:25:44Z | sn108 commit touches scoring: docs: validator hardware requirements (min 16 physical cores + 32 GB,… |
| `sn120:scoring_commit:2026-10-05T06:36:49Z` | 120 | SCORING_COMMIT | 2026-10-05T09:25:44Z | sn120 commit touches scoring: Align current verifier roster and publication guide with E12 |
| `sn3:scoring_commit:2026-10-05T11:24:15Z` | 3 | SCORING_COMMIT | 2026-10-05T18:46:20Z | sn3 commit touches scoring: Switch evaluator to single-GPU replicas and adjust batch size |
| `sn21:scoring_commit:2026-10-05T16:48:30Z` | 21 | SCORING_COMMIT | 2026-10-05T18:46:20Z | sn21 commit touches scoring: fix(validator): the reg-index staleness alarm follows the head refresh |
| `sn22:scoring_commit:2026-10-05T18:30:37Z` | 22 | SCORING_COMMIT | 2026-10-05T18:46:20Z | sn22 commit touches scoring: fix(task-api): judge completions when they reach the API, run storage… |
| `sn25:scoring_commit:2026-10-05T17:18:29Z` | 25 | SCORING_COMMIT | 2026-10-05T18:46:20Z | sn25 commit touches scoring: fix(miner): preserve boolean CLI option declarations |
| `sn50:scoring_commit:2026-10-05T16:47:46Z` | 50 | SCORING_COMMIT | 2026-10-05T18:46:20Z | sn50 commit touches scoring: perf(validator): reuse dendrite process pool, as_completed, drop per-… |
| `sn51:scoring_commit:2026-10-05T14:58:10Z` | 51 | SCORING_COMMIT | 2026-10-05T18:46:20Z | sn51 commit touches scoring: DAH-3980 - validator: connector reads the chain off its event loop an… |
| `sn61:release:4.10.9` | 61 | RELEASE | 2026-10-05T18:46:20Z | sn61 released 4.10.9 |
| `sn61:scoring_commit:2026-10-05T10:45:34Z` | 61 | SCORING_COMMIT | 2026-10-05T18:46:20Z | sn61 commit touches scoring: refactor: increase max_unique_commits for ada_detection_v3 challenge |
| `sn65:scoring_commit:2026-10-01T06:43:28Z` | 65 | SCORING_COMMIT | 2026-10-05T18:46:20Z | sn65 commit touches scoring: update miner docs |
| `sn67:scoring_commit:2026-10-05T11:00:55Z` | 67 | SCORING_COMMIT | 2026-10-05T18:46:20Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20261005.post0 |
| `sn76:scoring_commit:2026-10-05T15:29:39Z` | 76 | SCORING_COMMIT | 2026-10-05T18:46:20Z | sn76 commit touches scoring: MINER_TERMS §3: publish rate version earned-bid-2x-v1 (2x from 2026-1… |
| `sn120:scoring_commit:2026-10-05T18:43:57Z` | 120 | SCORING_COMMIT | 2026-10-05T18:46:20Z | sn120 commit touches scoring: Add prospective owned cached native evaluation and telemetry |
| `sn25:scoring_commit:2026-10-05T23:54:13Z` | 25 | SCORING_COMMIT | 2026-10-06T00:24:10Z | sn25 commit touches scoring: Merge executable root validator registration bootstrap |
| `sn51:release:executor-v1.137` | 51 | RELEASE | 2026-10-06T00:24:10Z | sn51 released executor-v1.137 |
| `sn51:scoring_commit:2026-10-05T19:18:41Z` | 51 | SCORING_COMMIT | 2026-10-06T00:24:10Z | sn51 commit touches scoring: NO-TICKET - [P1] verifyx: vendor libverifyx.so from celium-gpu-verifi… |
| `sn71:scoring_commit:2026-10-05T22:08:15Z` | 71 | SCORING_COMMIT | 2026-10-06T00:24:10Z | sn71 commit touches scoring: Stop the scoring-readiness tests from execve-ing the test session |
| `sn94:scoring_commit:2026-10-05T19:11:29Z` | 94 | SCORING_COMMIT | 2026-10-06T00:24:10Z | sn94 commit touches scoring: docs: mission-first miner README and one canonical operating guide (#… |
| `sn97:scoring_commit:2026-10-05T23:47:15Z` | 97 | SCORING_COMMIT | 2026-10-06T00:24:10Z | sn97 commit touches scoring: chore: increase scoring timeout |
| `sn116:scoring_commit:2026-10-06T00:10:09Z` | 116 | SCORING_COMMIT | 2026-10-06T00:24:10Z | sn116 commit touches scoring: Merge pull request #646 from carbonphysicsai/claude/validator-14-test… |
| `sn120:scoring_commit:2026-10-05T23:28:14Z` | 120 | SCORING_COMMIT | 2026-10-06T00:24:10Z | sn120 commit touches scoring: Keep verifier polling after a terminal backend loses its lease |
| `sn25:scoring_commit:2026-10-06T02:25:10Z` | 25 | SCORING_COMMIT | 2026-10-06T06:43:00Z | sn25 commit touches scoring: Merge bounded early miner recovery diagnostics |
| `sn37:scoring_commit:2026-10-06T02:41:33Z` | 37 | SCORING_COMMIT | 2026-10-06T06:43:00Z | sn37 commit touches scoring: feat(validator)!: default-off master switch VALIDATOR_ENABLED (#26) |
| `sn67:scoring_commit:2026-10-06T05:02:36Z` | 67 | SCORING_COMMIT | 2026-10-06T06:43:00Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20261006.post1 |
| `sn71:scoring_commit:2026-10-06T05:47:00Z` | 71 | SCORING_COMMIT | 2026-10-06T06:43:00Z | sn71 commit touches scoring: Verify round diagnostics preserve recovery and failures |
| `sn116:scoring_commit:2026-10-06T03:58:21Z` | 116 | SCORING_COMMIT | 2026-10-06T06:43:00Z | sn116 commit touches scoring: Merge pull request #674 from carbonphysicsai/claude/battery-score-tun… |
| `sn120:scoring_commit:2026-10-06T06:04:01Z` | 120 | SCORING_COMMIT | 2026-10-06T06:43:00Z | sn120 commit touches scoring: feat: opt into bounded single owned verifier checkpoint reuse |
| `sn53:readme_task_diff:298e8500ae9f9443` | 53 | README_TASK_DIFF | 2026-09-29T14:13:00Z | sn53 README task/scoring sections changed |
| `sn69:readme_task_diff:ad40463d48698a60` | 69 | README_TASK_DIFF | 2026-09-29T14:13:00Z | sn69 README task/scoring sections changed |
| `sn5:readme_task_diff:12b2073e10277692` | 5 | README_TASK_DIFF | 2026-09-29T19:33:10Z | sn5 README task/scoring sections changed |
| `sn66:readme_task_diff:6d33aaba03894c45` | 66 | README_TASK_DIFF | 2026-09-30T20:46:36Z | sn66 README task/scoring sections changed |
| `sn108:readme_task_diff:ba7ede20804945f8` | 108 | README_TASK_DIFF | 2026-09-30T20:46:36Z | sn108 README task/scoring sections changed |
| `sn117:readme_task_diff:f5c96a7d91dc6d0c` | 117 | README_TASK_DIFF | 2026-09-30T20:46:36Z | sn117 README task/scoring sections changed |
| `sn117:readme_task_diff:1174f1fc742efb54` | 117 | README_TASK_DIFF | 2026-10-01T00:12:52Z | sn117 README task/scoring sections changed |
| `sn78:readme_task_diff:1b02e745e3230412` | 78 | README_TASK_DIFF | 2026-10-01T06:20:47Z | sn78 README task/scoring sections changed |
| `sn108:readme_task_diff:91f7ce813a4d3359` | 108 | README_TASK_DIFF | 2026-10-01T13:42:59Z | sn108 README task/scoring sections changed |
| `sn117:readme_task_diff:4fe3235ab658f65b` | 117 | README_TASK_DIFF | 2026-10-01T19:04:22Z | sn117 README task/scoring sections changed |
| `sn15:readme_task_diff:b8c62e4a86eca8fd` | 15 | README_TASK_DIFF | 2026-10-01T23:09:13Z | sn15 README task/scoring sections changed |
| `sn74:readme_task_diff:8ab3367c1c73f078` | 74 | README_TASK_DIFF | 2026-10-02T15:44:59Z | sn74 README task/scoring sections changed |
| `sn26:readme_task_diff:417360e9baf6fbbe` | 26 | README_TASK_DIFF | 2026-10-04T06:24:29Z | sn26 README task/scoring sections changed |
| `sn25:readme_task_diff:6dafd77986a370d3` | 25 | README_TASK_DIFF | 2026-10-04T17:06:18Z | sn25 README task/scoring sections changed |
| `sn80:readme_task_diff:7fcffd77dd4a6c7a` | 80 | README_TASK_DIFF | 2026-10-05T09:25:44Z | sn80 README task/scoring sections changed |

## RESOLVED IN THIS WINDOW

_none_
