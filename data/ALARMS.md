# ALARMS - generated 2026-09-10T15:12:51Z, block 9037953

window: first_seen in [2026-09-10T13:58:20Z, 2026-09-10T15:13:20Z)  (60 min interval + 15 min overlap)

Report ONLY the rows under NEW SINCE LAST RUN. Rows under STILL OPEN were
already reported in an earlier window and must not be re-alarmed.

## NEW SINCE LAST RUN

| event_id | netuid | class | severity | first_seen_utc | one_line |
|---|---|---|---|---|---|
| `sn9:release:v4.12.16` | 9 | RELEASE | P1 | 2026-09-10T15:13:20Z | sn9 released v4.12.16 |
| `sn51:scoring_commit:2026-09-10T12:28:28Z` | 51 | SCORING_COMMIT | P1 | 2026-09-10T15:13:20Z | sn51 commit touches scoring: DAH-2748, hide a node the validator cannot reach on one availability … |
| `sn63:scoring_commit:2026-09-10T15:05:19Z` | 63 | SCORING_COMMIT | P1 | 2026-09-10T15:13:20Z | sn63 commit touches scoring: Fix issue with migrated validator db |
| `sn81:scoring_commit:2026-09-10T12:25:01Z` | 81 | SCORING_COMMIT | P1 | 2026-09-10T15:13:20Z | sn81 commit touches scoring: Document V6 miner submission allowance |
| `sn108:scoring_commit:2026-09-10T11:47:33Z` | 108 | SCORING_COMMIT | P1 | 2026-09-10T15:13:20Z | sn108 commit touches scoring: feat(evaluation): optionally discard a checkpoint once it has been sc… |
| `sn66:readme_task_diff:e9a9de7a5084c0f6` | 66 | README_TASK_DIFF | P2 | 2026-09-10T15:13:20Z | sn66 README task/scoring sections changed |

### detail

- **`sn9:release:v4.12.16`** - sn9 released v4.12.16
  - published 2026-09-10T14:10:04Z (was v4.12.14)
- **`sn51:scoring_commit:2026-09-10T12:28:28Z`** - sn51 commit touches scoring: DAH-2748, hide a node the validator cannot reach on one availability …
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn63:scoring_commit:2026-09-10T15:05:19Z`** - sn63 commit touches scoring: Fix issue with migrated validator db
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn81:scoring_commit:2026-09-10T12:25:01Z`** - sn81 commit touches scoring: Document V6 miner submission allowance
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn108:scoring_commit:2026-09-10T11:47:33Z`** - sn108 commit touches scoring: feat(evaluation): optionally discard a checkpoint once it has been sc…
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn66:readme_task_diff:e9a9de7a5084c0f6`** - sn66 README task/scoring sections changed
  - Only the task-describing headings are hashed, so badge and typo edits do not trigger this.

## STILL OPEN (already reported - do not re-alarm)

| event_id | netuid | class | first_seen_utc | one_line |
|---|---|---|---|---|
| `sn121:burn_drop:0.601` | 121 | BURN_DROP | 2026-09-03T18:49:37Z | sn121 burn fell 1.000 -> 0.601 - miners can earn again |
| `sn49:burn_drop:0.990` | 49 | BURN_DROP | 2026-09-03T21:41:08Z | sn49 burn fell 0.990 -> 0.990 - miners can earn again |
| `sn107:burn_drop:0.812` | 107 | BURN_DROP | 2026-09-04T01:25:22Z | sn107 burn fell 1.000 -> 0.812 - miners can earn again |
| `sn85:burn_drop:0.360` | 85 | BURN_DROP | 2026-09-04T21:04:38Z | sn85 burn fell 1.000 -> 0.360 - miners can earn again |
| `sn47:burn_drop:0.942` | 47 | BURN_DROP | 2026-09-06T16:12:33Z | sn47 burn fell 1.000 -> 0.942 - miners can earn again |
| `sn34:burn_drop:0.799` | 34 | BURN_DROP | 2026-09-08T17:34:23Z | sn34 burn fell 1.000 -> 0.799 - miners can earn again |
| `sn121:burn_drop:0.610` | 121 | BURN_DROP | 2026-09-08T17:34:23Z | sn121 burn fell 1.000 -> 0.610 - miners can earn again |
| `sn78:weights_version_bump:1` | 78 | WEIGHTS_VERSION_BUMP | 2026-09-08T22:52:47Z | sn78 weights_version 0 -> 1 |
| `sn78:weights_version_bump:4294967296` | 78 | WEIGHTS_VERSION_BUMP | 2026-09-09T21:17:06Z | sn78 weights_version 1 -> 4294967296 |
| `sn104:burn_drop:0.988` | 104 | BURN_DROP | 2026-09-09T21:17:06Z | sn104 burn fell 1.000 -> 0.988 - miners can earn again |
| `sn1:release:v4.4.1` | 1 | RELEASE | 2026-09-03T15:15:26Z | sn1 released v4.4.1 |
| `sn2:release:14.14.2` | 2 | RELEASE | 2026-09-03T15:15:26Z | sn2 released 14.14.2 |
| `sn53:scoring_commit:2026-09-03T05:50:55Z` | 53 | SCORING_COMMIT | 2026-09-03T18:49:37Z | sn53 commit touches scoring: tee_miner: stop dropping the thinking-token count on the way out |
| `sn69:scoring_commit:2026-09-03T16:15:44Z` | 69 | SCORING_COMMIT | 2026-09-03T18:49:37Z | sn69 commit touches scoring: Point CLI miners at the console to download a brief document (#5) |
| `sn71:scoring_commit:2026-09-03T18:42:37Z` | 71 | SCORING_COMMIT | 2026-09-03T18:49:37Z | sn71 commit touches scoring: Preserve strict identity boundaries in scoring integration |
| `sn74:release:release-20260903-183804` | 74 | RELEASE | 2026-09-03T18:49:37Z | sn74 released release-20260903-183804 |
| `sn25:release:v2026.9.3-1036684010` | 25 | RELEASE | 2026-09-03T21:41:08Z | sn25 released v2026.9.3-1036684010 |
| `sn71:scoring_commit:2026-09-03T18:50:08Z` | 71 | SCORING_COMMIT | 2026-09-03T21:41:08Z | sn71 commit touches scoring: Bind updated scoring protected workflows |
| `sn71:scoring_commit:2026-09-03T22:37:18Z` | 71 | SCORING_COMMIT | 2026-09-03T23:33:40Z | sn71 commit touches scoring: Tell a rate-limited miner which submission cap it hit |
| `sn21:scoring_commit:2026-09-04T00:49:42Z` | 21 | SCORING_COMMIT | 2026-09-04T01:25:22Z | sn21 commit touches scoring: fix(validator): commit the daily vector directly when the weekly stre… |
| `sn25:release:v2026.9.3-1036806790` | 25 | RELEASE | 2026-09-04T01:25:22Z | sn25 released v2026.9.3-1036806790 |
| `sn25:scoring_commit:2026-09-03T19:36:15Z` | 25 | SCORING_COMMIT | 2026-09-04T01:25:22Z | sn25 commit touches scoring: fix semantic reward consensus fixture |
| `sn71:scoring_commit:2026-09-04T00:27:39Z` | 71 | SCORING_COMMIT | 2026-09-04T01:25:22Z | sn71 commit touches scoring: Prevent source add reward queue starvation |
| `sn107:scoring_commit:2026-09-04T00:16:20Z` | 107 | SCORING_COMMIT | 2026-09-04T01:25:22Z | sn107 commit touches scoring: Merge pull request #39 from minos-protocol/feat/round-verification |
| `sn21:scoring_commit:2026-09-04T04:09:32Z` | 21 | SCORING_COMMIT | 2026-09-04T06:21:54Z | sn21 commit touches scoring: test(validator): prove burn composition matches the committer branch … |
| `sn71:scoring_commit:2026-09-04T05:24:15Z` | 71 | SCORING_COMMIT | 2026-09-04T06:21:54Z | sn71 commit touches scoring: Bind protected Arena reward compatibility adapter |
| `sn100:scoring_commit:2026-09-04T04:15:06Z` | 100 | SCORING_COMMIT | 2026-09-04T06:21:54Z | sn100 commit touches scoring: feat(proof): Proof challenge + dynamic topics + RLM judge digest pin … |
| `sn107:release:v0.3.0: Minos 🧬 — Difficulty-weighted sc` | 107 | RELEASE | 2026-09-04T06:21:54Z | sn107 released v0.3.0: Minos 🧬 — Difficulty-weighted scoring (v2), round verification,  config commitments |
| `sn25:scoring_commit:2026-09-04T11:22:34Z` | 25 | SCORING_COMMIT | 2026-09-04T11:33:57Z | sn25 commit touches scoring: Record semantic verifier parallel qualification |
| `sn66:scoring_commit:2026-09-03T14:19:04Z` | 66 | SCORING_COMMIT | 2026-09-04T11:33:57Z | sn66 commit touches scoring: Derive the verifier image tag, not only its digest and version |
| `sn67:scoring_commit:2026-09-04T06:27:51Z` | 67 | SCORING_COMMIT | 2026-09-04T11:33:57Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20260904.post1 |
| `sn78:scoring_commit:2026-09-03T21:48:59Z` | 78 | SCORING_COMMIT | 2026-09-04T11:33:57Z | sn78 commit touches scoring: Expose replay-verified public miner solutions |
| `sn92:scoring_commit:2026-09-04T10:56:43Z` | 92 | SCORING_COMMIT | 2026-09-04T11:33:57Z | sn92 commit touches scoring: Smooth the miner CLI and quiet the archive |
| `sn97:scoring_commit:2026-09-03T16:13:11Z` | 97 | SCORING_COMMIT | 2026-09-04T11:33:57Z | sn97 commit touches scoring: fix: re-key a registration when the miner re-activates with a new sub… |
| `sn100:scoring_commit:2026-09-04T07:41:55Z` | 100 | SCORING_COMMIT | 2026-09-04T11:33:57Z | sn100 commit touches scoring: fix(validator): extract submit outcome helper for clippy |
| `sn3:scoring_commit:2026-09-04T13:38:17Z` | 3 | SCORING_COMMIT | 2026-09-04T15:09:26Z | sn3 commit touches scoring: Show model digests for queued and active evaluations |
| `sn21:scoring_commit:2026-09-04T14:12:08Z` | 21 | SCORING_COMMIT | 2026-09-04T15:09:26Z | sn21 commit touches scoring: fix(validator): reference loop uses bt.Wallet |
| `sn25:release:v2026.9.4-1037327320` | 25 | RELEASE | 2026-09-04T15:09:26Z | sn25 released v2026.9.4-1037327320 |
| `sn47:scoring_commit:2026-09-04T14:48:52Z` | 47 | SCORING_COMMIT | 2026-09-04T15:09:26Z | sn47 commit touches scoring: new datasets list and verifier |
| `sn7:release:release-20260904-155448: Add min_from_am` | 7 | RELEASE | 2026-09-04T18:32:09Z | sn7 released release-20260904-155448: Add min_from_amount and candidates to the seam rate quote (#719) |
| `sn7:scoring_commit:2026-09-02T22:52:26Z` | 7 | SCORING_COMMIT | 2026-09-04T18:32:09Z | sn7 commit touches scoring: CLI: --send verifies source-address control BEFORE the bid (#716) |
| `sn25:release:v2026.9.4-1037416540` | 25 | RELEASE | 2026-09-04T18:32:09Z | sn25 released v2026.9.4-1037416540 |
| `sn78:scoring_commit:2026-09-04T18:06:44Z` | 78 | SCORING_COMMIT | 2026-09-04T18:32:09Z | sn78 commit touches scoring: Install FFmpeg for macOS miner tests |
| `sn96:release:Verathos v0.2.0 – Sleipnir: Verifiable M` | 96 | RELEASE | 2026-09-04T18:32:09Z | sn96 released Verathos v0.2.0 – Sleipnir: Verifiable Multi-Node Model Serving |
| `sn96:scoring_commit:2026-09-04T07:31:31Z` | 96 | SCORING_COMMIT | 2026-09-04T18:32:09Z | sn96 commit touches scoring: fix: qualify mesh scoring on protocol v3 |
| `sn100:scoring_commit:2026-09-04T17:45:13Z` | 100 | SCORING_COMMIT | 2026-09-04T18:32:09Z | sn100 commit touches scoring: docs(miner): Proof + Bounty A→Z at 2000/8000 (#219) |
| `sn102:release:v0.5.5 — publish the round podium to a H` | 102 | RELEASE | 2026-09-04T18:32:09Z | sn102 released v0.5.5 — publish the round podium to a HuggingFace archive repo |
| `sn102:scoring_commit:2026-09-03T21:10:17Z` | 102 | SCORING_COMMIT | 2026-09-04T18:32:09Z | sn102 commit touches scoring: 🏷️ refactor(validator): name podium folders by cycle, not round id |
| `sn21:scoring_commit:2026-09-04T20:27:20Z` | 21 | SCORING_COMMIT | 2026-09-04T21:04:38Z | sn21 commit touches scoring: feat(scoring): measurement resolution applied from a published date |
| `sn25:release:v2026.9.4-1037517570` | 25 | RELEASE | 2026-09-04T21:04:38Z | sn25 released v2026.9.4-1037517570 |
| `sn34:scoring_commit:2026-09-04T18:44:10Z` | 34 | SCORING_COMMIT | 2026-09-04T21:04:38Z | sn34 commit touches scoring: burn discriminator incentive until KoTH ships (#436) |
| `sn47:scoring_commit:2026-09-04T19:22:55Z` | 47 | SCORING_COMMIT | 2026-09-04T21:04:38Z | sn47 commit touches scoring: fix extraction and verifier |
| `sn92:scoring_commit:2026-09-04T20:10:42Z` | 92 | SCORING_COMMIT | 2026-09-04T21:04:38Z | sn92 commit touches scoring: scoring: refuse sockets with a class so ssl and asyncio still import … |
| `sn7:release:release-20260904-214340: Bump version to` | 7 | RELEASE | 2026-09-04T23:02:03Z | sn7 released release-20260904-214340: Bump version to 3.3.2 (#722) |
| `sn25:release:v2026.9.4-1037600680` | 25 | RELEASE | 2026-09-04T23:02:03Z | sn25 released v2026.9.4-1037600680 |
| `sn92:scoring_commit:2026-09-04T21:42:58Z` | 92 | SCORING_COMMIT | 2026-09-04T23:02:03Z | sn92 commit touches scoring: ci: classify bundle for the hidden-tests check; label tasks need one … |
| `sn21:scoring_commit:2026-09-05T04:29:37Z` | 21 | SCORING_COMMIT | 2026-09-05T05:40:43Z | sn21 commit touches scoring: docs(scoring): standing and resolution amendments effective 2026-09-05 |
| `sn62:release:v0.3.0` | 62 | RELEASE | 2026-09-05T05:40:43Z | sn62 released v0.3.0 |
| `sn62:scoring_commit:2026-09-04T10:45:00Z` | 62 | SCORING_COMMIT | 2026-09-05T05:40:43Z | sn62 commit touches scoring: test: :white_check_mark: Add tests validating the new endpoint |
| `sn71:scoring_commit:2026-09-05T05:37:23Z` | 71 | SCORING_COMMIT | 2026-09-05T05:40:43Z | sn71 commit touches scoring: fix: validate retained gateway archives by their supported role layout |
| `sn47:scoring_commit:2026-09-05T08:47:30Z` | 47 | SCORING_COMMIT | 2026-09-05T09:27:28Z | sn47 commit touches scoring: refine evaluation system |
| `sn71:scoring_commit:2026-09-05T08:30:32Z` | 71 | SCORING_COMMIT | 2026-09-05T09:27:28Z | sn71 commit touches scoring: fix: exclude stale validator build path from gateway runtime env |
| `sn100:scoring_commit:2026-09-05T08:03:23Z` | 100 | SCORING_COMMIT | 2026-09-05T09:27:28Z | sn100 commit touches scoring: fix(challenges): boot when sk/session placeholders are empty (#226) |
| `sn71:scoring_commit:2026-09-05T12:58:42Z` | 71 | SCORING_COMMIT | 2026-09-05T12:59:57Z | sn71 commit touches scoring: Merge pull request #177 from leadpoet/codex/validator-missing-object-… |
| `sn25:scoring_commit:2026-09-05T13:48:07Z` | 25 | SCORING_COMMIT | 2026-09-05T16:00:56Z | sn25 commit touches scoring: validator: add private bounded attempt record store |
| `sn56:scoring_commit:2026-09-05T15:35:59Z` | 56 | SCORING_COMMIT | 2026-09-05T16:00:56Z | sn56 commit touches scoring: Make the auditor loop continuously, matching validator weight-set fre… |
| `sn71:scoring_commit:2026-09-05T13:10:16Z` | 71 | SCORING_COMMIT | 2026-09-05T16:00:56Z | sn71 commit touches scoring: Merge pull request #178 from leadpoet/codex/validator-recovery-author… |
| `sn21:scoring_commit:2026-09-05T16:25:15Z` | 21 | SCORING_COMMIT | 2026-09-05T18:13:16Z | sn21 commit touches scoring: fix(reporting): rows shown with their accuracy are scored rows; audit… |
| `sn71:scoring_commit:2026-09-05T16:23:27Z` | 71 | SCORING_COMMIT | 2026-09-05T18:13:16Z | sn71 commit touches scoring: build: refresh reviewed gateway verifier workflow hashes |
| `sn25:scoring_commit:2026-09-05T19:18:14Z` | 25 | SCORING_COMMIT | 2026-09-05T20:34:23Z | sn25 commit touches scoring: Protect validator seed custody and qualify producer gate coverage |
| `sn71:scoring_commit:2026-09-05T20:23:45Z` | 71 | SCORING_COMMIT | 2026-09-05T20:34:23Z | sn71 commit touches scoring: Bind validator workflow to archive retry policy |
| `sn78:scoring_commit:2026-09-05T14:56:55Z` | 78 | SCORING_COMMIT | 2026-09-05T20:34:23Z | sn78 commit touches scoring: Add external miner pilot launch handoffs |
| `sn7:release:release-20260905-204833` | 7 | RELEASE | 2026-09-05T22:21:43Z | sn7 released release-20260905-204833 |
| `sn71:scoring_commit:2026-09-05T21:34:19Z` | 71 | SCORING_COMMIT | 2026-09-05T22:21:43Z | sn71 commit touches scoring: chore(validator): bind existing recovery workflow identity |
| `sn74:release:release-20260905-223823` | 74 | RELEASE | 2026-09-06T00:06:30Z | sn74 released release-20260905-223823 |
| `sn74:scoring_commit:2026-09-05T20:51:26Z` | 74 | SCORING_COMMIT | 2026-09-06T00:06:30Z | sn74 commit touches scoring: serving miner: an attestation waits for prefill and holds admissions,… |
| `sn71:scoring_commit:2026-09-06T00:50:36Z` | 71 | SCORING_COMMIT | 2026-09-06T04:34:35Z | sn71 commit touches scoring: Isolate Arena failure regressions and verify prior publication contin… |
| `sn78:scoring_commit:2026-09-06T02:58:05Z` | 78 | SCORING_COMMIT | 2026-09-06T04:34:35Z | sn78 commit touches scoring: Add public registered-miner endpoint pilot |
| `sn25:scoring_commit:2026-09-06T12:28:31Z` | 25 | SCORING_COMMIT | 2026-09-06T12:51:56Z | sn25 commit touches scoring: Checkpoint held repair sources and validation handoff |
| `sn25:scoring_commit:2026-09-06T15:00:42Z` | 25 | SCORING_COMMIT | 2026-09-06T16:12:33Z | sn25 commit touches scoring: Integrate qualified Solidity validator activation verification |
| `sn14:release:GLM-5.3 mock mainnet submissions (valida` | 14 | RELEASE | 2026-09-06T18:30:56Z | sn14 released GLM-5.3 mock mainnet submissions (validator self-test, 2026-09-06) |
| `sn93:scoring_commit:2026-09-06T20:14:30Z` | 93 | SCORING_COMMIT | 2026-09-06T20:52:43Z | sn93 commit touches scoring: chore: scope validator deploy to code/config paths (#171) |
| `sn25:scoring_commit:2026-09-06T21:52:49Z` | 25 | SCORING_COMMIT | 2026-09-06T22:52:57Z | sn25 commit touches scoring: Record recovery checkpoints and post-pull monitoring validation |
| `sn34:release:5.0.0 — King of the Hill` | 34 | RELEASE | 2026-09-07T00:57:22Z | sn34 released 5.0.0 — King of the Hill |
| `sn91:scoring_commit:2026-09-04T21:55:54Z` | 91 | SCORING_COMMIT | 2026-09-07T00:57:22Z | sn91 commit touches scoring: receipt: publish every duelled challenger's diagnostics (cohort_stats) |
| `sn25:release:v2026.9.6-1039587510` | 25 | RELEASE | 2026-09-07T06:01:32Z | sn25 released v2026.9.6-1039587510 |
| `sn71:scoring_commit:2026-09-07T04:13:16Z` | 71 | SCORING_COMMIT | 2026-09-07T06:01:32Z | sn71 commit touches scoring: fix: verify active provider cache persistence |
| `sn18:release:Release 2.1.4` | 18 | RELEASE | 2026-09-07T12:22:04Z | sn18 released Release 2.1.4 |
| `sn18:scoring_commit:2026-09-07T08:25:21Z` | 18 | SCORING_COMMIT | 2026-09-07T12:22:04Z | sn18 commit touches scoring: Stop emissions for non-participating miners (#88) |
| `sn25:release:v2026.9.7-1039747440` | 25 | RELEASE | 2026-09-07T12:22:04Z | sn25 released v2026.9.7-1039747440 |
| `sn51:scoring_commit:2026-09-07T11:34:42Z` | 51 | SCORING_COMMIT | 2026-09-07T12:22:04Z | sn51 commit touches scoring: [P1] feat: run the miners tests and ruff format on every PR (#1289) |
| `sn66:release:v.1.0.3: Web submissions, payouts, contr` | 66 | RELEASE | 2026-09-07T12:22:04Z | sn66 released v.1.0.3: Web submissions, payouts, contributions... |
| `sn67:scoring_commit:2026-09-07T07:03:25Z` | 67 | SCORING_COMMIT | 2026-09-07T12:22:04Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20260907.post2 |
| `sn71:scoring_commit:2026-09-07T06:56:29Z` | 71 | SCORING_COMMIT | 2026-09-07T12:22:04Z | sn71 commit touches scoring: chore: bind verified controller upgrade recovery |
| `sn78:scoring_commit:2026-09-07T06:42:21Z` | 78 | SCORING_COMMIT | 2026-09-07T12:22:04Z | sn78 commit touches scoring: Harden macOS validator audit origin |
| `sn92:scoring_commit:2026-09-07T08:17:20Z` | 92 | SCORING_COMMIT | 2026-09-07T12:22:04Z | sn92 commit touches scoring: archive: a rewarded system is archived whatever state the leaderboard… |
| `sn1:release:v4.4.2` | 1 | RELEASE | 2026-09-07T17:49:43Z | sn1 released v4.4.2 |
| `sn25:release:v2026.9.7-1039843330` | 25 | RELEASE | 2026-09-07T17:49:43Z | sn25 released v2026.9.7-1039843330 |
| `sn34:scoring_commit:2026-09-07T16:11:18Z` | 34 | SCORING_COMMIT | 2026-09-07T17:49:43Z | sn34 commit touches scoring: Set explicit 100% burn and bypass reward calculation |
| `sn38:scoring_commit:2026-09-07T12:36:00Z` | 38 | SCORING_COMMIT | 2026-09-07T17:49:43Z | sn38 commit touches scoring: Update validator image to the latest version in docker-compose.valida… |
| `sn66:scoring_commit:2026-09-07T15:27:35Z` | 66 | SCORING_COMMIT | 2026-09-07T17:49:43Z | sn66 commit touches scoring: Merge pull request #76 from conjectures-io/fix/verifier-cache-readabl… |
| `sn10:scoring_commit:2026-09-07T19:27:24Z` | 10 | SCORING_COMMIT | 2026-09-07T21:28:22Z | sn10 commit touches scoring: Merge pull request #146 from Pareton-ai/arpan/reveal-miner-commits |
| `sn71:scoring_commit:2026-09-07T19:51:59Z` | 71 | SCORING_COMMIT | 2026-09-07T21:28:22Z | sn71 commit touches scoring: Merge remote-tracking branch 'origin/main' into codex/miner-promotion… |
| `sn78:scoring_commit:2026-09-07T20:51:50Z` | 78 | SCORING_COMMIT | 2026-09-07T21:28:22Z | sn78 commit touches scoring: Open miner pilot enrollment |
| `sn96:release:Verathos v0.2.1 – Sleipnir Cross-Machine` | 96 | RELEASE | 2026-09-07T21:28:22Z | sn96 released Verathos v0.2.1 – Sleipnir Cross-Machine Serving |
| `sn104:scoring_commit:2026-09-07T18:34:43Z` | 104 | SCORING_COMMIT | 2026-09-07T21:28:22Z | sn104 commit touches scoring: Merge pull request #10 from taostatus/feat/discord-key-announcements |
| `sn25:scoring_commit:2026-09-07T16:54:02Z` | 25 | SCORING_COMMIT | 2026-09-07T23:48:23Z | sn25 commit touches scoring: Checkpoint historical validator schedule and finalization progress |
| `sn78:scoring_commit:2026-09-07T23:46:59Z` | 78 | SCORING_COMMIT | 2026-09-07T23:48:23Z | sn78 commit touches scoring: Fix pilot deployment validation |
| `sn67:scoring_commit:2026-09-07T09:39:54Z` | 67 | SCORING_COMMIT | 2026-09-08T04:27:58Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20260907.post3 |
| `sn71:scoring_commit:2026-09-08T03:48:46Z` | 71 | SCORING_COMMIT | 2026-09-08T04:27:58Z | sn71 commit touches scoring: Verify staging SOURCE_ADD restart isolation |
| `sn74:release:release-20260908-031700` | 74 | RELEASE | 2026-09-08T04:27:58Z | sn74 released release-20260908-031700 |
| `sn92:scoring_commit:2026-09-08T00:30:17Z` | 92 | SCORING_COMMIT | 2026-09-08T04:27:58Z | sn92 commit touches scoring: cost is total task latency for every system; empty profile responses … |
| `sn100:scoring_commit:2026-09-08T02:08:11Z` | 100 | SCORING_COMMIT | 2026-09-08T04:27:58Z | sn100 commit touches scoring: fix(proof): stage proxy model + holdout for live score (#234) |
| `sn66:scoring_commit:2026-09-08T04:45:40Z` | 66 | SCORING_COMMIT | 2026-09-08T09:02:01Z | sn66 commit touches scoring: Release 259 reviewed targets with immutable 10 MiB task policies |
| `sn71:scoring_commit:2026-09-08T06:56:07Z` | 71 | SCORING_COMMIT | 2026-09-08T09:02:01Z | sn71 commit touches scoring: Parse Arena drain quiescence in validator handoff |
| `sn80:scoring_commit:2026-09-08T07:33:08Z` | 80 | SCORING_COMMIT | 2026-09-08T09:02:01Z | sn80 commit touches scoring: docs: link shared real-robot task catalog and training data |
| `sn9:release:v4.12.14` | 9 | RELEASE | 2026-09-08T13:32:58Z | sn9 released v4.12.14 |
| `sn10:scoring_commit:2026-09-08T09:22:29Z` | 10 | SCORING_COMMIT | 2026-09-08T13:32:58Z | sn10 commit touches scoring: Merge pull request #145 from Pareton-ai/bohdan/feat/miner-score-trans… |
| `sn34:scoring_commit:2026-09-08T03:06:21Z` | 34 | SCORING_COMMIT | 2026-09-08T13:32:58Z | sn34 commit touches scoring: Bump version to 5.0.2 so validators autoupdate. |
| `sn71:scoring_commit:2026-09-08T13:29:02Z` | 71 | SCORING_COMMIT | 2026-09-08T13:32:58Z | sn71 commit touches scoring: Verify approved prior testnet release boots |
| `sn100:scoring_commit:2026-09-08T09:44:43Z` | 100 | SCORING_COMMIT | 2026-09-08T13:32:58Z | sn100 commit touches scoring: fix(eval): install host cc for triton jit on scoring image (#239) |
| `sn25:release:v2026.9.8-1040779940` | 25 | RELEASE | 2026-09-08T17:34:23Z | sn25 released v2026.9.8-1040779940 |
| `sn71:scoring_commit:2026-09-08T15:54:53Z` | 71 | SCORING_COMMIT | 2026-09-08T17:34:23Z | sn71 commit touches scoring: Merge remote-tracking branch 'origin/main' into codex/validator-test-… |
| `sn74:release:release-20260908-144557` | 74 | RELEASE | 2026-09-08T17:34:23Z | sn74 released release-20260908-144557 |
| `sn92:scoring_commit:2026-09-08T14:53:18Z` | 92 | SCORING_COMMIT | 2026-09-08T17:34:23Z | sn92 commit touches scoring: tracks: support is the one live track; call shaped tests load and scor |
| `sn120:scoring_commit:2026-09-08T14:27:39Z` | 120 | SCORING_COMMIT | 2026-09-08T17:34:23Z | sn120 commit touches scoring: Sync validator + eval design (2026-09-07/08): eval throughput work, w… |
| `sn2:release:14.14.3` | 2 | RELEASE | 2026-09-08T20:19:51Z | sn2 released 14.14.3 |
| `sn2:scoring_commit:2026-09-08T19:26:11Z` | 2 | SCORING_COMMIT | 2026-09-08T20:19:51Z | sn2 commit touches scoring: Introduce weight commit guard for epochs with zero miner scores (#627) |
| `sn71:scoring_commit:2026-09-08T20:17:47Z` | 71 | SCORING_COMMIT | 2026-09-08T20:19:51Z | sn71 commit touches scoring: Merge remote-tracking branch 'origin/main' into codex/arena-miner-rep… |
| `sn78:scoring_commit:2026-09-08T17:55:55Z` | 78 | SCORING_COMMIT | 2026-09-08T20:19:51Z | sn78 commit touches scoring: Fix bootstrap image revision validation |
| `sn96:release:Verathos v0.2.2 – Consistent Validator D` | 96 | RELEASE | 2026-09-08T20:19:51Z | sn96 released Verathos v0.2.2 – Consistent Validator Decisions and Microtensor Support |
| `sn15:release:v1.2.13: compose: forward SUBTENSOR_CHAI` | 15 | RELEASE | 2026-09-08T22:52:47Z | sn15 released v1.2.13: compose: forward SUBTENSOR_CHAIN_ENDPOINT to the validator (#274) |
| `sn15:scoring_commit:2026-09-08T20:21:13Z` | 15 | SCORING_COMMIT | 2026-09-08T22:52:47Z | sn15 commit touches scoring: compose: forward SUBTENSOR_CHAIN_ENDPOINT to the validator (#274) |
| `sn25:release:v2026.9.8-1040985530` | 25 | RELEASE | 2026-09-08T22:52:47Z | sn25 released v2026.9.8-1040985530 |
| `sn28:release:v0.4.15` | 28 | RELEASE | 2026-09-08T22:52:47Z | sn28 released v0.4.15 |
| `sn28:scoring_commit:2026-09-08T21:50:27Z` | 28 | SCORING_COMMIT | 2026-09-08T22:52:47Z | sn28 commit touches scoring: fix(miner): render node secret last and pin C locale |
| `sn71:scoring_commit:2026-09-08T22:52:04Z` | 71 | SCORING_COMMIT | 2026-09-09T01:13:27Z | sn71 commit touches scoring: build: refresh protected scoring source metadata |
| `sn111:scoring_commit:2026-09-09T00:59:16Z` | 111 | SCORING_COMMIT | 2026-09-09T01:13:27Z | sn111 commit touches scoring: fix(validator): enable rigor validation in mainnet profiles |
| `sn51:scoring_commit:2026-09-09T06:11:27Z` | 51 | SCORING_COMMIT | 2026-09-09T06:19:59Z | sn51 commit touches scoring: DAH-2962: delete the dead hashcat scoring path and the GPT-2 sample (… |
| `sn67:scoring_commit:2026-09-09T04:45:43Z` | 67 | SCORING_COMMIT | 2026-09-09T06:19:59Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20260909.post0 |
| `sn71:scoring_commit:2026-09-09T02:00:25Z` | 71 | SCORING_COMMIT | 2026-09-09T06:19:59Z | sn71 commit touches scoring: Stop Arena scoring after exhausted judge failure |
| `sn100:scoring_commit:2026-09-09T01:28:41Z` | 100 | SCORING_COMMIT | 2026-09-09T06:19:59Z | sn100 commit touches scoring: feat(proof): name the topic_id / custom_id hyphen-underscore mix-up (… |
| `sn111:scoring_commit:2026-09-09T03:15:32Z` | 111 | SCORING_COMMIT | 2026-09-09T06:19:59Z | sn111 commit touches scoring: fix(validator): normalize provider routing for DSPy adjudication |
| `sn120:scoring_commit:2026-09-09T03:59:55Z` | 120 | SCORING_COMMIT | 2026-09-09T06:19:59Z | sn120 commit touches scoring: AGENTS.md: first wvk-13 verdicts verified (probe reject, think-close … |
| `sn61:release:4.10.3` | 61 | RELEASE | 2026-09-09T11:41:14Z | sn61 released 4.10.3 |
| `sn66:scoring_commit:2026-09-09T08:24:00Z` | 66 | SCORING_COMMIT | 2026-09-09T11:41:14Z | sn66 commit touches scoring: Merge pull request #80 from conjectures-io/feat/retire-miner-hotkeys |
| `sn71:scoring_commit:2026-09-09T09:18:44Z` | 71 | SCORING_COMMIT | 2026-09-09T11:41:14Z | sn71 commit touches scoring: Preserve terminal company scores across judge retries |
| `sn78:scoring_commit:2026-09-09T07:12:10Z` | 78 | SCORING_COMMIT | 2026-09-09T11:41:14Z | sn78 commit touches scoring: Add legacy validator transition hold |
| `sn89:scoring_commit:2026-09-09T08:32:52Z` | 89 | SCORING_COMMIT | 2026-09-09T11:41:14Z | sn89 commit touches scoring: scoring: points-path earning gate is the points test as-of each call,… |
| `sn97:scoring_commit:2026-09-08T12:09:46Z` | 97 | SCORING_COMMIT | 2026-09-09T11:41:14Z | sn97 commit touches scoring: fix: show all task results for benchmark runs |
| `sn111:scoring_commit:2026-09-09T10:40:55Z` | 111 | SCORING_COMMIT | 2026-09-09T11:41:14Z | sn111 commit touches scoring: docs: clarify Ubuntu validator env setup |
| `sn114:scoring_commit:2026-09-09T08:57:02Z` | 114 | SCORING_COMMIT | 2026-09-09T11:41:14Z | sn114 commit touches scoring: Cap automatic run restarts per miner task |
| `sn1:release:v4.4.5` | 1 | RELEASE | 2026-09-09T15:20:16Z | sn1 released v4.4.5 |
| `sn28:release:v0.4.16-dev` | 28 | RELEASE | 2026-09-09T15:20:16Z | sn28 released v0.4.16-dev |
| `sn28:scoring_commit:2026-09-09T11:24:08Z` | 28 | SCORING_COMMIT | 2026-09-09T15:20:16Z | sn28 commit touches scoring: Anchor deployment staleness to the last successful verification |
| `sn71:scoring_commit:2026-09-09T11:49:48Z` | 71 | SCORING_COMMIT | 2026-09-09T15:20:16Z | sn71 commit touches scoring: Bind dead preflight verifier removal |
| `sn28:release:v0.4.17-dev` | 28 | RELEASE | 2026-09-09T18:46:23Z | sn28 released v0.4.17-dev |
| `sn62:release:v0.3.1` | 62 | RELEASE | 2026-09-09T18:46:23Z | sn62 released v0.3.1 |
| `sn62:scoring_commit:2026-09-07T11:02:04Z` | 62 | SCORING_COMMIT | 2026-09-09T18:46:23Z | sn62 commit touches scoring: feat: prevent cluster-autoscaler from draining a screener mid-evaluati |
| `sn71:scoring_commit:2026-09-09T18:13:57Z` | 71 | SCORING_COMMIT | 2026-09-09T18:46:23Z | sn71 commit touches scoring: Merge remote-tracking branch 'origin/main' into codex/arena-miner-rep… |
| `sn78:scoring_commit:2026-09-09T17:44:05Z` | 78 | SCORING_COMMIT | 2026-09-09T18:46:23Z | sn78 commit touches scoring: Publish verified bootstrap service state |
| `sn111:scoring_commit:2026-09-09T17:55:55Z` | 111 | SCORING_COMMIT | 2026-09-09T18:46:23Z | sn111 commit touches scoring: fix(validator): recover failed Silver adjudication batches |
| `sn124:scoring_commit:2026-09-08T18:12:27Z` | 124 | SCORING_COMMIT | 2026-09-09T18:46:23Z | sn124 commit touches scoring: Keep leased seeds through a validator restart |
| `sn20:scoring_commit:2026-09-08T12:07:25Z` | 20 | SCORING_COMMIT | 2026-09-09T21:17:06Z | sn20 commit touches scoring: Document model-independent miner extension workflow |
| `sn36:scoring_commit:2026-09-09T19:30:44Z` | 36 | SCORING_COMMIT | 2026-09-09T21:17:06Z | sn36 commit touches scoring: Merge pull request #5 from EpagoFoundation/fix/sealed-release-tasks |
| `sn62:release:v0.3.2` | 62 | RELEASE | 2026-09-09T21:17:06Z | sn62 released v0.3.2 |
| `sn71:scoring_commit:2026-09-09T21:09:24Z` | 71 | SCORING_COMMIT | 2026-09-09T21:17:06Z | sn71 commit touches scoring: Merge remote-tracking branch 'origin/main' into codex/arena-miner-rep… |
| `sn78:scoring_commit:2026-09-09T19:48:05Z` | 78 | SCORING_COMMIT | 2026-09-09T21:17:06Z | sn78 commit touches scoring: Add prerequisite-gated validator supervisor |
| `sn25:release:v2026.9.9-1041947070` | 25 | RELEASE | 2026-09-09T23:25:39Z | sn25 released v2026.9.9-1041947070 |
| `sn28:release:v0.4.17` | 28 | RELEASE | 2026-09-09T23:25:39Z | sn28 released v0.4.17 |
| `sn61:release:4.10.4` | 61 | RELEASE | 2026-09-09T23:25:39Z | sn61 released 4.10.4 |
| `sn62:scoring_commit:2026-09-09T18:55:06Z` | 62 | SCORING_COMMIT | 2026-09-09T23:25:39Z | sn62 commit touches scoring: Merge pull request #498 from ridgesai/feat/update-validator-docker |
| `sn71:scoring_commit:2026-09-09T22:53:48Z` | 71 | SCORING_COMMIT | 2026-09-09T23:25:39Z | sn71 commit touches scoring: Cover encoded miner-key echoes through provider routes |
| `sn78:scoring_commit:2026-09-09T22:13:48Z` | 78 | SCORING_COMMIT | 2026-09-09T23:25:39Z | sn78 commit touches scoring: Fix OCI archive annotation verification |
| `sn100:release:ctx CLI v3.3.30` | 100 | RELEASE | 2026-09-09T23:25:39Z | sn100 released ctx CLI v3.3.30 |
| `sn100:scoring_commit:2026-09-09T22:40:23Z` | 100 | SCORING_COMMIT | 2026-09-09T23:25:39Z | sn100 commit touches scoring: feat(proof): continuous leaf emitter with ChallengeInternal cover (#25 |
| `sn25:release:v2026.9.9-1042000000` | 25 | RELEASE | 2026-09-10T01:20:26Z | sn25 released v2026.9.9-1042000000 |
| `sn81:scoring_commit:2026-09-10T00:47:41Z` | 81 | SCORING_COMMIT | 2026-09-10T01:20:26Z | sn81 commit touches scoring: fix: validate sampled entropy coverage at the proof boundary |
| `sn100:release:ctx CLI v3.3.31` | 100 | RELEASE | 2026-09-10T01:20:26Z | sn100 released ctx CLI v3.3.31 |
| `sn100:scoring_commit:2026-09-10T00:49:52Z` | 100 | SCORING_COMMIT | 2026-09-10T01:20:26Z | sn100 commit touches scoring: feat(proof): require miner hotkey signature on submit (#259) |
| `sn15:release:shoppingbench-final` | 15 | RELEASE | 2026-09-10T06:19:09Z | sn15 released shoppingbench-final |
| `sn25:release:v2026.9.9-1042199790` | 25 | RELEASE | 2026-09-10T06:19:09Z | sn25 released v2026.9.9-1042199790 |
| `sn51:release:executor-v1.124` | 51 | RELEASE | 2026-09-10T06:19:09Z | sn51 released executor-v1.124 |
| `sn51:scoring_commit:2026-09-10T02:42:59Z` | 51 | SCORING_COMMIT | 2026-09-10T06:19:09Z | sn51 commit touches scoring: DAH-3006 - [P1] validator stops serialising every Redis command behin… |
| `sn71:scoring_commit:2026-09-10T05:18:12Z` | 71 | SCORING_COMMIT | 2026-09-10T06:19:09Z | sn71 commit touches scoring: Preserve validated page final URLs |
| `sn81:scoring_commit:2026-09-10T05:24:18Z` | 81 | SCORING_COMMIT | 2026-09-10T06:19:09Z | sn81 commit touches scoring: Merge pull request #236 from reliquadotai/codex/v1-miner-readme |
| `sn91:scoring_commit:2026-09-10T05:27:44Z` | 91 | SCORING_COMMIT | 2026-09-10T06:19:09Z | sn91 commit touches scoring: Merge pull request #251 from TensorLink-AI/claude/score-warm-start |
| `sn100:scoring_commit:2026-09-10T06:07:01Z` | 100 | SCORING_COMMIT | 2026-09-10T06:19:09Z | sn100 commit touches scoring: docs(proof): add miner guide for the tbench topic (#261) |
| `sn15:release:v2.0.0` | 15 | RELEASE | 2026-09-10T11:39:13Z | sn15 released v2.0.0 |
| `sn15:scoring_commit:2026-09-10T07:45:35Z` | 15 | SCORING_COMMIT | 2026-09-10T11:39:13Z | sn15 commit touches scoring: Verify scope-bound environment deliveries (#276) |
| `sn25:release:v2026.9.10-1042298530` | 25 | RELEASE | 2026-09-10T11:39:13Z | sn25 released v2026.9.10-1042298530 |
| `sn25:scoring_commit:2026-09-10T09:40:39Z` | 25 | SCORING_COMMIT | 2026-09-10T11:39:13Z | sn25 commit touches scoring: crv4: accept reviewed runtime 455 validator stake layout |
| `sn51:release:executor-v1.125` | 51 | RELEASE | 2026-09-10T11:39:13Z | sn51 released executor-v1.125 |
| `sn62:release:v0.3.3` | 62 | RELEASE | 2026-09-10T11:39:13Z | sn62 released v0.3.3 |
| `sn67:scoring_commit:2026-09-10T07:28:03Z` | 67 | SCORING_COMMIT | 2026-09-10T11:39:13Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20260910.post3 |
| `sn71:scoring_commit:2026-09-10T06:18:11Z` | 71 | SCORING_COMMIT | 2026-09-10T11:39:13Z | sn71 commit touches scoring: docs: state midnight continuous evaluation timing |
| `sn91:scoring_commit:2026-09-10T11:31:44Z` | 91 | SCORING_COMMIT | 2026-09-10T11:39:13Z | sn91 commit touches scoring: docs: concise miner quickstart for funded legs, private submissions, … |
| `sn100:scoring_commit:2026-09-10T11:36:06Z` | 100 | SCORING_COMMIT | 2026-09-10T11:39:13Z | sn100 commit touches scoring: fix(proof): fail closed on incomplete harbor evaluate (#267) |
| `sn71:readme_task_diff:ebf6898a52202570` | 71 | README_TASK_DIFF | 2026-09-03T18:49:37Z | sn71 README task/scoring sections changed |
| `sn114:readme_task_diff:8a170d798d34334c` | 114 | README_TASK_DIFF | 2026-09-04T11:33:57Z | sn114 README task/scoring sections changed |
| `sn47:readme_task_diff:ee01fd805919dfa1` | 47 | README_TASK_DIFF | 2026-09-04T15:09:26Z | sn47 README task/scoring sections changed |
| `sn7:readme_task_diff:edbfe0beb3207f5d` | 7 | README_TASK_DIFF | 2026-09-04T18:32:09Z | sn7 README task/scoring sections changed |
| `sn96:readme_task_diff:9b448a83b77e12c9` | 96 | README_TASK_DIFF | 2026-09-04T18:32:09Z | sn96 README task/scoring sections changed |
| `sn47:readme_task_diff:8b345756fdb99755` | 47 | README_TASK_DIFF | 2026-09-04T21:04:38Z | sn47 README task/scoring sections changed |
| `sn63:readme_task_diff:9f841de80403238f` | 63 | README_TASK_DIFF | 2026-09-04T21:04:38Z | sn63 README task/scoring sections changed |
| `sn71:readme_task_diff:7ba0f5e901269ab4` | 71 | README_TASK_DIFF | 2026-09-04T21:04:38Z | sn71 README task/scoring sections changed |
| `sn47:readme_task_diff:478b669831ea7848` | 47 | README_TASK_DIFF | 2026-09-05T09:27:28Z | sn47 README task/scoring sections changed |
| `sn80:readme_task_diff:91c32064037eaf29` | 80 | README_TASK_DIFF | 2026-09-05T12:59:57Z | sn80 README task/scoring sections changed |
| `sn93:readme_task_diff:6bd0c74883d58dde` | 93 | README_TASK_DIFF | 2026-09-06T18:30:56Z | sn93 README task/scoring sections changed |
| `sn34:readme_task_diff:535b78cbd7d6207d` | 34 | README_TASK_DIFF | 2026-09-06T22:52:57Z | sn34 README task/scoring sections changed |
| `sn80:readme_task_diff:9cd93d83a14b7502` | 80 | README_TASK_DIFF | 2026-09-07T12:22:04Z | sn80 README task/scoring sections changed |
| `sn67:readme_task_diff:02d3c62272b1d7dd` | 67 | README_TASK_DIFF | 2026-09-08T04:27:58Z | sn67 README task/scoring sections changed |
| `sn66:readme_task_diff:1677dd0cb94b82d3` | 66 | README_TASK_DIFF | 2026-09-08T09:02:01Z | sn66 README task/scoring sections changed |
| `sn80:readme_task_diff:ef9838874bfda548` | 80 | README_TASK_DIFF | 2026-09-08T09:02:01Z | sn80 README task/scoring sections changed |
| `sn28:readme_task_diff:150862184557e02b` | 28 | README_TASK_DIFF | 2026-09-08T22:52:47Z | sn28 README task/scoring sections changed |
| `sn28:readme_task_diff:459971cadb11194f` | 28 | README_TASK_DIFF | 2026-09-09T15:20:16Z | sn28 README task/scoring sections changed |
| `sn45:readme_task_diff:15dfa7fb69a79bef` | 45 | README_TASK_DIFF | 2026-09-09T15:20:16Z | sn45 README task/scoring sections changed |
| `sn28:readme_task_diff:aab5d8d239c04847` | 28 | README_TASK_DIFF | 2026-09-09T18:46:23Z | sn28 README task/scoring sections changed |
| `sn108:readme_task_diff:3f2d87f2c0a1e7e0` | 108 | README_TASK_DIFF | 2026-09-09T18:46:23Z | sn108 README task/scoring sections changed |
| `sn20:readme_task_diff:4594489462f379e3` | 20 | README_TASK_DIFF | 2026-09-09T21:17:06Z | sn20 README task/scoring sections changed |
| `sn71:readme_task_diff:b64ef6137b1c6577` | 71 | README_TASK_DIFF | 2026-09-10T01:20:26Z | sn71 README task/scoring sections changed |
| `sn15:readme_task_diff:17e287861e782246` | 15 | README_TASK_DIFF | 2026-09-10T06:19:09Z | sn15 README task/scoring sections changed |

## RESOLVED IN THIS WINDOW

_none_
