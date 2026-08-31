# ALARMS - generated 2026-08-31T20:47:50Z, block 8967706

window: first_seen in [2026-08-31T19:33:23Z, 2026-08-31T20:48:23Z)  (60 min interval + 15 min overlap)

Report ONLY the rows under NEW SINCE LAST RUN. Rows under STILL OPEN were
already reported in an earlier window and must not be re-alarmed.

## NEW SINCE LAST RUN

| event_id | netuid | class | severity | first_seen_utc | one_line |
|---|---|---|---|---|---|
| `sn15:release:v1.2.12` | 15 | RELEASE | P1 | 2026-08-31T20:48:23Z | sn15 released v1.2.12 |
| `sn15:scoring_commit:2026-08-31T16:04:15Z` | 15 | SCORING_COMMIT | P1 | 2026-08-31T20:48:23Z | sn15 commit touches scoring: fix(validator): don't fail runs on incomplete reasoning-judge coverag… |
| `sn38:scoring_commit:2026-08-31T17:33:12Z` | 38 | SCORING_COMMIT | P1 | 2026-08-31T20:48:23Z | sn38 commit touches scoring: Update validator image to the latest version in docker-compose.valida… |
| `sn50:release:v1.12.0` | 50 | RELEASE | P1 | 2026-08-31T20:48:23Z | sn50 released v1.12.0 |
| `sn92:release:v0.3.0` | 92 | RELEASE | P1 | 2026-08-31T20:48:23Z | sn92 released v0.3.0 |
| `sn92:scoring_commit:2026-08-31T20:39:51Z` | 92 | SCORING_COMMIT | P1 | 2026-08-31T20:48:23Z | sn92 commit touches scoring: Grant the validator container the capability the network jail needs |
| `sn111:scoring_commit:2026-08-31T20:40:04Z` | 111 | SCORING_COMMIT | P1 | 2026-08-31T20:48:23Z | sn111 commit touches scoring: feat(selection): diversify adaptive miner draws |
| `sn124:scoring_commit:2026-08-31T19:33:52Z` | 124 | SCORING_COMMIT | P1 | 2026-08-31T20:48:23Z | sn124 commit touches scoring: Merge pull request #118 from swarm-subnet/feature/ali/miner-folder-mi… |
| `sn38:readme_task_diff:6d6f3dfd29d211ce` | 38 | README_TASK_DIFF | P2 | 2026-08-31T20:48:23Z | sn38 README task/scoring sections changed |

### detail

- **`sn15:release:v1.2.12`** - sn15 released v1.2.12
  - published 2026-08-31T17:21:38Z (was v1.2.11)
- **`sn15:scoring_commit:2026-08-31T16:04:15Z`** - sn15 commit touches scoring: fix(validator): don't fail runs on incomplete reasoning-judge coverag…
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn38:scoring_commit:2026-08-31T17:33:12Z`** - sn38 commit touches scoring: Update validator image to the latest version in docker-compose.valida…
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn50:release:v1.12.0`** - sn50 released v1.12.0
  - published 2026-08-31T15:32:04Z (was v1.11.1)
- **`sn92:release:v0.3.0`** - sn92 released v0.3.0
  - published 2026-08-31T17:00:04Z (was v0.1.14)
- **`sn92:scoring_commit:2026-08-31T20:39:51Z`** - sn92 commit touches scoring: Grant the validator container the capability the network jail needs
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn111:scoring_commit:2026-08-31T20:40:04Z`** - sn111 commit touches scoring: feat(selection): diversify adaptive miner draws
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn124:scoring_commit:2026-08-31T19:33:52Z`** - sn124 commit touches scoring: Merge pull request #118 from swarm-subnet/feature/ali/miner-folder-mi…
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn38:readme_task_diff:6d6f3dfd29d211ce`** - sn38 README task/scoring sections changed
  - Only the task-describing headings are hashed, so badge and typo edits do not trigger this.

## STILL OPEN (already reported - do not re-alarm)

| event_id | netuid | class | first_seen_utc | one_line |
|---|---|---|---|---|
| `sn121:burn_drop:0.657` | 121 | BURN_DROP | 2026-08-25T14:13:01Z | sn121 burn fell 1.000 -> 0.657 - miners can earn again |
| `sn7:burn_drop:0.910` | 7 | BURN_DROP | 2026-08-26T22:23:22Z | sn7 burn fell 1.000 -> 0.910 - miners can earn again |
| `sn65:burn_drop:0.762` | 65 | BURN_DROP | 2026-08-27T14:33:13Z | sn65 burn fell 1.000 -> 0.762 - miners can earn again |
| `sn92:burn_drop:0.952` | 92 | BURN_DROP | 2026-08-27T14:33:13Z | sn92 burn fell 1.000 -> 0.952 - miners can earn again |
| `sn59:burn_drop:0.000` | 59 | BURN_DROP | 2026-08-28T00:03:30Z | sn59 burn fell 1.000 -> 0.000 - miners can earn again |
| `sn14:burn_drop:0.000` | 14 | BURN_DROP | 2026-08-28T11:18:26Z | sn14 burn fell 1.000 -> 0.000 - miners can earn again |
| `sn104:burn_drop:0.003` | 104 | BURN_DROP | 2026-08-28T21:28:55Z | sn104 burn fell 1.000 -> 0.003 - miners can earn again |
| `sn111:burn_drop:0.000` | 111 | BURN_DROP | 2026-08-28T21:28:55Z | sn111 burn fell 1.000 -> 0.000 - miners can earn again |
| `sn121:burn_drop:0.606` | 121 | BURN_DROP | 2026-08-28T21:28:55Z | sn121 burn fell 1.000 -> 0.606 - miners can earn again |
| `sn49:burn_drop:0.000` | 49 | BURN_DROP | 2026-08-29T15:10:23Z | sn49 burn fell 0.990 -> 0.000 - miners can earn again |
| `sn92:scoring_commit:2026-08-24T20:51:06Z` | 92 | SCORING_COMMIT | 2026-08-24T21:15:06Z | sn92 commit touches scoring: Correct the validator setup path end to end |
| `sn71:scoring_commit:2026-08-24T21:10:53Z` | 71 | SCORING_COMMIT | 2026-08-24T21:53:25Z | sn71 commit touches scoring: Allow bounded measured dev evaluation payloads |
| `sn102:scoring_commit:2026-08-24T16:15:02Z` | 102 | SCORING_COMMIT | 2026-08-24T22:40:07Z | sn102 commit touches scoring: ♻️ refactor(validator): drop the redundant merge hashes |
| `sn66:scoring_commit:2026-08-24T22:51:29Z` | 66 | SCORING_COMMIT | 2026-08-24T23:04:58Z | sn66 commit touches scoring: Normalize verifier image source permissions |
| `sn15:scoring_commit:2026-08-25T00:12:11Z` | 15 | SCORING_COMMIT | 2026-08-25T01:49:22Z | sn15 commit touches scoring: revert: guarded title-corroboration was unsafe on legacy rewards (ORO… |
| `sn71:scoring_commit:2026-08-25T02:00:09Z` | 71 | SCORING_COMMIT | 2026-08-25T03:09:56Z | sn71 commit touches scoring: Merge pull request #109 from leadpoet/codex/full-validator-indent-202… |
| `sn71:scoring_commit:2026-08-25T04:09:03Z` | 71 | SCORING_COMMIT | 2026-08-25T05:04:42Z | sn71 commit touches scoring: Verify parity bundle through exact empty fetch |
| `sn111:scoring_commit:2026-08-25T09:49:43Z` | 111 | SCORING_COMMIT | 2026-08-25T10:00:26Z | sn111 commit touches scoring: feat(setup): streamline public validator deployment |
| `sn112:scoring_commit:2026-08-24T07:39:41Z` | 112 | SCORING_COMMIT | 2026-08-25T10:00:26Z | sn112 commit touches scoring: fix(dedup): a waitlisted miner could never resubmit that solver again… |
| `sn10:scoring_commit:2026-08-25T10:50:13Z` | 10 | SCORING_COMMIT | 2026-08-25T11:14:15Z | sn10 commit touches scoring: feat(chain): validator-side set_weights with permit check (PAR-104) |
| `sn92:scoring_commit:2026-08-25T12:18:18Z` | 92 | SCORING_COMMIT | 2026-08-25T13:08:22Z | sn92 commit touches scoring: Note the operator-driven submission window in miner timing |
| `sn102:release:v0.5.2 — background-eval resume + valida` | 102 | RELEASE | 2026-08-25T14:13:01Z | sn102 released v0.5.2 — background-eval resume + validator memory fixes |
| `sn25:release:v2026.8.25-1028682810` | 25 | RELEASE | 2026-08-25T15:14:33Z | sn25 released v2026.8.25-1028682810 |
| `sn108:scoring_commit:2026-08-25T15:02:35Z` | 108 | SCORING_COMMIT | 2026-08-25T15:14:33Z | sn108 commit touches scoring: fix(evaluation): recover from out of memory instead of compounding it |
| `sn23:scoring_commit:2026-08-25T15:33:12Z` | 23 | SCORING_COMMIT | 2026-08-25T16:08:24Z | sn23 commit touches scoring: Merge pull request #49 from TrishoolAI/feat/challenge-creation |
| `sn92:scoring_commit:2026-08-25T15:53:19Z` | 92 | SCORING_COMMIT | 2026-08-25T16:08:24Z | sn92 commit touches scoring: Score entity extraction with dataset-level micro-F1 |
| `sn108:scoring_commit:2026-08-25T15:20:19Z` | 108 | SCORING_COMMIT | 2026-08-25T16:08:24Z | sn108 commit touches scoring: docs(scoring): drop the note about asserted dataset counts |
| `sn34:scoring_commit:2026-08-25T16:39:00Z` | 34 | SCORING_COMMIT | 2026-08-25T17:05:10Z | sn34 commit touches scoring: docs: align discriminator taxonomy and scoring (#430) |
| `sn92:scoring_commit:2026-08-25T17:00:40Z` | 92 | SCORING_COMMIT | 2026-08-25T17:05:10Z | sn92 commit touches scoring: Unwrap fenced JSON before strict entity validation |
| `sn15:release:v1.2.8` | 15 | RELEASE | 2026-08-25T18:17:26Z | sn15 released v1.2.8 |
| `sn28:release:v0.4.10-dev` | 28 | RELEASE | 2026-08-25T19:55:29Z | sn28 released v0.4.10-dev |
| `sn112:scoring_commit:2026-08-25T20:30:12Z` | 112 | SCORING_COMMIT | 2026-08-25T20:41:44Z | sn112 commit touches scoring: fix(anchor): a validator with no archive for a chain could not pin it… |
| `sn28:release:v0.4.10` | 28 | RELEASE | 2026-08-25T21:53:06Z | sn28 released v0.4.10 |
| `sn56:scoring_commit:2026-08-25T22:56:00Z` | 56 | SCORING_COMMIT | 2026-08-25T23:10:04Z | sn56 commit touches scoring: Add unit tests for get_base_contestant to validate dataset propagatio… |
| `sn112:scoring_commit:2026-08-25T22:56:41Z` | 112 | SCORING_COMMIT | 2026-08-25T23:10:04Z | sn112 commit touches scoring: fix(scoring): plan.metadata is not always a dict, and the scoring pat… |
| `sn25:release:v2026.8.25-1029027010` | 25 | RELEASE | 2026-08-26T01:55:31Z | sn25 released v2026.8.25-1029027010 |
| `sn81:scoring_commit:2026-08-26T00:35:18Z` | 81 | SCORING_COMMIT | 2026-08-26T01:55:31Z | sn81 commit touches scoring: fix(validator): close submission ingress races |
| `sn25:release:v2026.8.25-1029146630` | 25 | RELEASE | 2026-08-26T04:09:47Z | sn25 released v2026.8.25-1029146630 |
| `sn82:scoring_commit:2026-08-25T21:38:56Z` | 82 | SCORING_COMMIT | 2026-08-26T05:48:23Z | sn82 commit touches scoring: fix: score title fights by complete topic pairs |
| `sn111:scoring_commit:2026-08-26T07:22:40Z` | 111 | SCORING_COMMIT | 2026-08-26T07:56:58Z | sn111 commit touches scoring: fix(validation): make claim assessments sparse and non-punitive |
| `sn25:release:v2026.8.26-1029312040` | 25 | RELEASE | 2026-08-26T08:58:49Z | sn25 released v2026.8.26-1029312040 |
| `sn44:scoring_commit:2026-08-26T07:58:36Z` | 44 | SCORING_COMMIT | 2026-08-26T08:58:49Z | sn44 commit touches scoring: Merge pull request #55 from score-technologies/hardeing-latency-refin… |
| `sn61:release:4.10.0` | 61 | RELEASE | 2026-08-26T08:58:49Z | sn61 released 4.10.0 |
| `sn61:scoring_commit:2026-08-26T07:57:37Z` | 61 | SCORING_COMMIT | 2026-08-26T08:58:49Z | sn61 commit touches scoring: deps: update bot virus challenge image version to 1.0.4 |
| `sn112:scoring_commit:2026-08-26T08:41:08Z` | 112 | SCORING_COMMIT | 2026-08-26T08:58:49Z | sn112 commit touches scoring: fix(964): optimizeYield can be scored — four defects between plan and… |
| `sn111:scoring_commit:2026-08-26T09:13:32Z` | 111 | SCORING_COMMIT | 2026-08-26T09:54:13Z | sn111 commit touches scoring: fix(selection): retain serving miners and record evaluation history |
| `sn112:scoring_commit:2026-08-26T09:26:46Z` | 112 | SCORING_COMMIT | 2026-08-26T09:54:13Z | sn112 commit touches scoring: feat(scoring): give the JS sandbox the App's own verdict, not just wh… |
| `sn21:scoring_commit:2026-08-26T10:23:53Z` | 21 | SCORING_COMMIT | 2026-08-26T10:49:02Z | sn21 commit touches scoring: feat(rewards): publish the allocation audit with the daily vector; qu… |
| `sn111:scoring_commit:2026-08-26T10:46:32Z` | 111 | SCORING_COMMIT | 2026-08-26T10:49:02Z | sn111 commit touches scoring: feat(batch): reuse canonical miner artifacts across validators |
| `sn51:scoring_commit:2026-08-26T10:57:03Z` | 51 | SCORING_COMMIT | 2026-08-26T11:40:35Z | sn51 commit touches scoring: DAH-2467, mixed scoring for partially rented GPU-split nodes (#1153) |
| `sn21:scoring_commit:2026-08-26T11:55:13Z` | 21 | SCORING_COMMIT | 2026-08-26T12:18:39Z | sn21 commit touches scoring: fix(rewards): one-payer receipt fingerprinting runs in a subprocess |
| `sn28:release:v0.4.11-dev` | 28 | RELEASE | 2026-08-26T12:18:39Z | sn28 released v0.4.11-dev |
| `sn81:scoring_commit:2026-08-26T13:09:50Z` | 81 | SCORING_COMMIT | 2026-08-26T13:33:28Z | sn81 commit touches scoring: fix(proof): release a finished plan's miner payloads |
| `sn108:scoring_commit:2026-08-26T13:27:13Z` | 108 | SCORING_COMMIT | 2026-08-26T13:33:28Z | sn108 commit touches scoring: Merge feat/mirrored-scoring: submit another validator's published scor |
| `sn44:scoring_commit:2026-08-26T14:00:07Z` | 44 | SCORING_COMMIT | 2026-08-26T14:29:56Z | sn44 commit touches scoring: Merge pull request #56 from score-technologies/security-enhancement |
| `sn25:release:v2026.8.26-1029569170` | 25 | RELEASE | 2026-08-26T16:06:12Z | sn25 released v2026.8.26-1029569170 |
| `sn54:scoring_commit:2026-08-26T17:15:54Z` | 54 | SCORING_COMMIT | 2026-08-26T19:17:48Z | sn54 commit touches scoring: updating UAV all miners not just the queriable miners (#112) |
| `sn108:scoring_commit:2026-08-26T19:00:11Z` | 108 | SCORING_COMMIT | 2026-08-26T19:17:48Z | sn108 commit touches scoring: feat: verify the submitter violating claim; balance the dataset score |
| `sn28:release:v0.4.11` | 28 | RELEASE | 2026-08-26T22:23:22Z | sn28 released v0.4.11 |
| `sn45:scoring_commit:2026-08-26T22:03:30Z` | 45 | SCORING_COMMIT | 2026-08-26T22:23:22Z | sn45 commit touches scoring: Submit one epoch of reward points to the API |
| `sn76:scoring_commit:2026-08-26T20:35:03Z` | 76 | SCORING_COMMIT | 2026-08-26T22:23:22Z | sn76 commit touches scoring: rewards: top five per track, split 40/25/15/12/8 |
| `sn111:scoring_commit:2026-08-26T19:54:44Z` | 111 | SCORING_COMMIT | 2026-08-26T22:23:22Z | sn111 commit touches scoring: docs(validator): add mainnet profile and streamline setup |
| `sn25:release:v2026.8.26-1029908500` | 25 | RELEASE | 2026-08-27T03:26:56Z | sn25 released v2026.8.26-1029908500 |
| `sn3:scoring_commit:2026-08-27T11:15:32Z` | 3 | SCORING_COMMIT | 2026-08-27T14:33:13Z | sn3 commit touches scoring: Refactor evaluation section in index.html for improved structure |
| `sn21:scoring_commit:2026-08-27T12:19:47Z` | 21 | SCORING_COMMIT | 2026-08-27T14:33:13Z | sn21 commit touches scoring: perf(rewards): per-day fingerprint index — the one-payer check stops … |
| `sn25:release:v2026.8.27-1030161880` | 25 | RELEASE | 2026-08-27T14:33:13Z | sn25 released v2026.8.27-1030161880 |
| `sn55:scoring_commit:2026-08-27T11:33:48Z` | 55 | SCORING_COMMIT | 2026-08-27T14:33:13Z | sn55 commit touches scoring: update validation block number |
| `sn61:release:4.10.1` | 61 | RELEASE | 2026-08-27T14:33:13Z | sn61 released 4.10.1 |
| `sn61:scoring_commit:2026-08-27T11:47:29Z` | 61 | SCORING_COMMIT | 2026-08-27T14:33:13Z | sn61 commit touches scoring: chore: update scoring criteria and clarify human detection requiremen… |
| `sn67:scoring_commit:2026-08-27T07:34:23Z` | 67 | SCORING_COMMIT | 2026-08-27T14:33:13Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20260827.post2 |
| `sn76:scoring_commit:2026-08-27T09:02:45Z` | 76 | SCORING_COMMIT | 2026-08-27T14:33:13Z | sn76 commit touches scoring: validator: attest rejected runs so miners can see why |
| `sn92:scoring_commit:2026-08-27T09:29:56Z` | 92 | SCORING_COMMIT | 2026-08-27T14:33:13Z | sn92 commit touches scoring: Let a miner restore a pointer a reveal overwrote |
| `sn108:scoring_commit:2026-08-27T13:01:50Z` | 108 | SCORING_COMMIT | 2026-08-27T14:33:13Z | sn108 commit touches scoring: docs(validator): re-post every 30 minutes, and say why 30 |
| `sn112:scoring_commit:2026-08-27T08:40:42Z` | 112 | SCORING_COMMIT | 2026-08-27T14:33:13Z | sn112 commit touches scoring: fix(sandbox): scoring JS had no RPC for chain 964, and the wrong one … |
| `sn3:scoring_commit:2026-08-27T14:44:03Z` | 3 | SCORING_COMMIT | 2026-08-28T00:03:30Z | sn3 commit touches scoring: Add evaluation history metrics presentation and update dashboard rend… |
| `sn25:release:v2026.8.27-1030474020` | 25 | RELEASE | 2026-08-28T00:03:30Z | sn25 released v2026.8.27-1030474020 |
| `sn91:release:worker-v0.7.0` | 91 | RELEASE | 2026-08-28T00:03:30Z | sn91 released worker-v0.7.0 |
| `sn92:scoring_commit:2026-08-27T15:01:23Z` | 92 | SCORING_COMMIT | 2026-08-28T00:03:30Z | sn92 commit touches scoring: Attach hidden tests as gold on scored tasks |
| `sn108:scoring_commit:2026-08-27T17:17:43Z` | 108 | SCORING_COMMIT | 2026-08-28T00:03:30Z | sn108 commit touches scoring: fix(validator): a rate-limited mirror cycle killed the scheduler and … |
| `sn112:scoring_commit:2026-08-27T18:37:53Z` | 112 | SCORING_COMMIT | 2026-08-28T00:03:30Z | sn112 commit touches scoring: fix(964): a plan's interactions did not compose, so 964 scored by dif… |
| `sn3:scoring_commit:2026-08-28T08:56:33Z` | 3 | SCORING_COMMIT | 2026-08-28T11:18:26Z | sn3 commit touches scoring: Add source scores handling and presentation to dashboard |
| `sn25:release:v2026.8.28-1031115710` | 25 | RELEASE | 2026-08-28T11:18:26Z | sn25 released v2026.8.28-1031115710 |
| `sn61:release:4.10.2` | 61 | RELEASE | 2026-08-28T11:18:26Z | sn61 released 4.10.2 |
| `sn61:scoring_commit:2026-08-28T05:45:39Z` | 61 | SCORING_COMMIT | 2026-08-28T11:18:26Z | sn61 commit touches scoring: chore: update challenge navigation and fix ADA-3 headless detection s… |
| `sn67:scoring_commit:2026-08-28T06:40:58Z` | 67 | SCORING_COMMIT | 2026-08-28T11:18:26Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20260828.post6 |
| `sn80:scoring_commit:2026-08-28T05:16:34Z` | 80 | SCORING_COMMIT | 2026-08-28T11:18:26Z | sn80 commit touches scoring: docs: point miners to the openroboto CLI and the real-robot track |
| `sn92:scoring_commit:2026-08-28T08:31:19Z` | 92 | SCORING_COMMIT | 2026-08-28T11:18:26Z | sn92 commit touches scoring: Carry the miner's published source through to the control plane |
| `sn96:release:Verathos v0.1.42 – Verified MoE, Account` | 96 | RELEASE | 2026-08-28T11:18:26Z | sn96 released Verathos v0.1.42 – Verified MoE, Account Billing, and Runtime Stability |
| `sn96:scoring_commit:2026-08-26T14:47:41Z` | 96 | SCORING_COMMIT | 2026-08-28T11:18:26Z | sn96 commit touches scoring: fix: decay endpoint-gated scores at epoch close |
| `sn108:scoring_commit:2026-08-28T04:54:03Z` | 108 | SCORING_COMMIT | 2026-08-28T11:18:26Z | sn108 commit touches scoring: docs(validator): the unanimity abort needs two independent sources |
| `sn15:release:v1.2.9` | 15 | RELEASE | 2026-08-28T21:28:55Z | sn15 released v1.2.9 |
| `sn15:scoring_commit:2026-08-28T18:31:26Z` | 15 | SCORING_COMMIT | 2026-08-28T21:28:55Z | sn15 commit touches scoring: fix(validator): use revealed top as weight fallback (#265) |
| `sn21:scoring_commit:2026-08-28T17:07:56Z` | 21 | SCORING_COMMIT | 2026-08-28T21:28:55Z | sn21 commit touches scoring: feat(reporting): each miner's row carries the reason a control acted … |
| `sn25:release:v2026.8.28-1031286130` | 25 | RELEASE | 2026-08-28T21:28:55Z | sn25 released v2026.8.28-1031286130 |
| `sn28:release:v0.4.12` | 28 | RELEASE | 2026-08-28T21:28:55Z | sn28 released v0.4.12 |
| `sn35:release:1.2.0` | 35 | RELEASE | 2026-08-28T21:28:55Z | sn35 released 1.2.0 |
| `sn35:scoring_commit:2026-08-28T16:38:20Z` | 35 | SCORING_COMMIT | 2026-08-28T21:28:55Z | sn35 commit touches scoring: feat: send all miner emissions to scored miners |
| `sn92:scoring_commit:2026-08-28T14:15:37Z` | 92 | SCORING_COMMIT | 2026-08-28T21:28:55Z | sn92 commit touches scoring: Accept operator-named hotkeys ahead of their validator permit |
| `sn102:release:v0.5.3` | 102 | RELEASE | 2026-08-28T21:28:55Z | sn102 released v0.5.3 |
| `sn102:scoring_commit:2026-08-28T13:33:02Z` | 102 | SCORING_COMMIT | 2026-08-28T21:28:55Z | sn102 commit touches scoring: ⏪ fix(shared): stop collapsing miner commits to one model hash |
| `sn108:scoring_commit:2026-08-28T12:10:59Z` | 108 | SCORING_COMMIT | 2026-08-28T21:28:55Z | sn108 commit touches scoring: docs(readme): miner gate is 50 registered AND 25 active members |
| `sn111:scoring_commit:2026-08-28T12:51:57Z` | 111 | SCORING_COMMIT | 2026-08-28T21:28:55Z | sn111 commit touches scoring: docs(validator): enable paper reuse in launch profiles |
| `sn15:release:v1.2.10` | 15 | RELEASE | 2026-08-29T03:23:48Z | sn15 released v1.2.10 |
| `sn25:release:v2026.8.28-1031618120` | 25 | RELEASE | 2026-08-29T03:23:48Z | sn25 released v2026.8.28-1031618120 |
| `sn25:release:v2026.8.28-1031763440` | 25 | RELEASE | 2026-08-29T10:19:28Z | sn25 released v2026.8.28-1031763440 |
| `sn47:scoring_commit:2026-08-29T06:50:23Z` | 47 | SCORING_COMMIT | 2026-08-29T10:19:28Z | sn47 commit touches scoring: rollout verification rules |
| `sn67:scoring_commit:2026-08-29T06:48:42Z` | 67 | SCORING_COMMIT | 2026-08-29T10:19:28Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20260829.post0 |
| `sn21:scoring_commit:2026-08-29T14:49:37Z` | 21 | SCORING_COMMIT | 2026-08-29T15:10:23Z | sn21 commit touches scoring: feat(scoring): honour the reference exemption on the lineage path |
| `sn111:scoring_commit:2026-08-29T11:10:12Z` | 111 | SCORING_COMMIT | 2026-08-29T15:10:23Z | sn111 commit touches scoring: chore(config): shorten validator query interval |
| `sn21:scoring_commit:2026-08-29T15:29:29Z` | 21 | SCORING_COMMIT | 2026-08-29T18:44:56Z | sn21 commit touches scoring: fix(reporting): a published tier must mean the miner is being paid |
| `sn71:scoring_commit:2026-08-29T16:01:20Z` | 71 | SCORING_COMMIT | 2026-08-29T18:44:56Z | sn71 commit touches scoring: Measure admitted model verifier latency |
| `sn89:scoring_commit:2026-08-29T16:20:07Z` | 89 | SCORING_COMMIT | 2026-08-29T18:44:56Z | sn89 commit touches scoring: HF: grade the band the miner declared, not the board's |
| `sn111:scoring_commit:2026-08-29T17:27:58Z` | 111 | SCORING_COMMIT | 2026-08-29T18:44:56Z | sn111 commit touches scoring: fix(validator): preserve completed run status during shutdown |
| `sn89:scoring_commit:2026-08-29T20:55:10Z` | 89 | SCORING_COMMIT | 2026-08-29T21:20:31Z | sn89 commit touches scoring: limit-watcher: a miner-drawn band survives to fire |
| `sn89:scoring_commit:2026-08-29T22:05:27Z` | 89 | SCORING_COMMIT | 2026-08-29T23:29:51Z | sn89 commit touches scoring: scoring: the points gate is per competition, not per chain |
| `sn71:scoring_commit:2026-08-30T00:13:57Z` | 71 | SCORING_COMMIT | 2026-08-30T01:45:42Z | sn71 commit touches scoring: Document miner SOURCE_ADD inputs (#153) |
| `sn89:scoring_commit:2026-08-30T01:06:31Z` | 89 | SCORING_COMMIT | 2026-08-30T01:45:42Z | sn89 commit touches scoring: scoring: the points qualify gate, and the variance that made it too l… |
| `sn92:scoring_commit:2026-08-30T01:18:37Z` | 92 | SCORING_COMMIT | 2026-08-30T01:45:42Z | sn92 commit touches scoring: Validate commitments at discovery, guard partial settles, count dupli… |
| `sn21:scoring_commit:2026-08-30T05:20:42Z` | 21 | SCORING_COMMIT | 2026-08-30T07:32:13Z | sn21 commit touches scoring: fix(validator-api): serve the daily feeds without a weekly release |
| `sn67:scoring_commit:2026-08-29T08:12:36Z` | 67 | SCORING_COMMIT | 2026-08-30T07:32:13Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20260829.post1 |
| `sn92:scoring_commit:2026-08-30T03:19:44Z` | 92 | SCORING_COMMIT | 2026-08-30T07:32:13Z | sn92 commit touches scoring: Satisfy strict typing across the validator, scoring, and engine paths |
| `sn9:release:v4.12.10` | 9 | RELEASE | 2026-08-30T13:20:41Z | sn9 released v4.12.10 |
| `sn21:scoring_commit:2026-08-30T11:29:22Z` | 21 | SCORING_COMMIT | 2026-08-30T13:20:41Z | sn21 commit touches scoring: docs(validator): stop implying a second validator can run the scorer |
| `sn15:release:v1.2.11` | 15 | RELEASE | 2026-08-30T17:40:07Z | sn15 released v1.2.11 |
| `sn21:scoring_commit:2026-08-30T13:48:48Z` | 21 | SCORING_COMMIT | 2026-08-30T17:40:07Z | sn21 commit touches scoring: fix(reporting): tenure rows state how many days the miner actually has |
| `sn25:release:v2026.8.30-1033129380` | 25 | RELEASE | 2026-08-30T20:05:23Z | sn25 released v2026.8.30-1033129380 |
| `sn92:scoring_commit:2026-08-30T20:40:28Z` | 92 | SCORING_COMMIT | 2026-08-30T22:43:10Z | sn92 commit touches scoring: Lock the evaluation environment to the fleet's resolved set |
| `sn111:scoring_commit:2026-08-30T21:57:12Z` | 111 | SCORING_COMMIT | 2026-08-30T22:43:10Z | sn111 commit touches scoring: feat(selection): expand miner pool with provisional performance |
| `sn91:scoring_commit:2026-08-31T05:05:09Z` | 91 | SCORING_COMMIT | 2026-08-31T07:00:21Z | sn91 commit touches scoring: validator: multi-horizon calibration telemetry — groundwork for the s… |
| `sn92:scoring_commit:2026-08-31T06:03:36Z` | 92 | SCORING_COMMIT | 2026-08-31T07:00:21Z | sn92 commit touches scoring: Score module-shaped tasks in miner simulation under the pinned enviro… |
| `sn101:scoring_commit:2026-08-31T03:21:03Z` | 101 | SCORING_COMMIT | 2026-08-31T07:00:21Z | sn101 commit touches scoring: Harden tag normalization and duplicate-set matching in scoring |
| `sn111:scoring_commit:2026-08-31T02:59:02Z` | 111 | SCORING_COMMIT | 2026-08-31T07:00:21Z | sn111 commit touches scoring: feat(selection): make adaptive miner sample size configurable |
| `sn3:scoring_commit:2026-08-31T08:14:55Z` | 3 | SCORING_COMMIT | 2026-08-31T15:03:06Z | sn3 commit touches scoring: Implement evaluation reuse limit handling and cleanup scheduling |
| `sn50:scoring_commit:2026-08-31T13:14:24Z` | 50 | SCORING_COMMIT | 2026-08-31T15:03:06Z | sn50 commit touches scoring: feat(validator): blend VHFT (Synth Ultra) as a 4th competition (#320) |
| `sn51:scoring_commit:2026-08-31T12:25:43Z` | 51 | SCORING_COMMIT | 2026-08-31T15:03:06Z | sn51 commit touches scoring: DAH-2090, validate one executor on request from the backend (#1254) |
| `sn56:scoring_commit:2026-08-31T13:13:56Z` | 56 | SCORING_COMMIT | 2026-08-31T15:03:06Z | sn56 commit touches scoring: Preserve replacement-task invariants across prep-failure reroutes. (#… |
| `sn67:scoring_commit:2026-08-31T06:48:15Z` | 67 | SCORING_COMMIT | 2026-08-31T15:03:06Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20260831.post1 |
| `sn92:scoring_commit:2026-08-31T13:00:04Z` | 92 | SCORING_COMMIT | 2026-08-31T15:03:06Z | sn92 commit touches scoring: Add the novel partition and blend it into the score at its task share |
| `sn97:scoring_commit:2026-08-29T21:22:36Z` | 97 | SCORING_COMMIT | 2026-08-31T15:03:06Z | sn97 commit touches scoring: fix: skip hidden files from validation |
| `sn66:readme_task_diff:d897794f349f6fcf` | 66 | README_TASK_DIFF | 2026-08-24T22:40:07Z | sn66 README task/scoring sections changed |
| `sn111:readme_task_diff:00bbd31d47cb0fe2` | 111 | README_TASK_DIFF | 2026-08-25T11:14:15Z | sn111 README task/scoring sections changed |
| `sn76:readme_task_diff:e2a786d7f22f73bb` | 76 | README_TASK_DIFF | 2026-08-26T22:23:22Z | sn76 README task/scoring sections changed |
| `sn111:readme_task_diff:4ac99c0122295794` | 111 | README_TASK_DIFF | 2026-08-27T14:33:13Z | sn111 README task/scoring sections changed |
| `sn80:readme_task_diff:a1414d5d9c1406ba` | 80 | README_TASK_DIFF | 2026-08-28T11:18:26Z | sn80 README task/scoring sections changed |
| `sn47:readme_task_diff:3e3cbf15b25c3611` | 47 | README_TASK_DIFF | 2026-08-28T21:28:55Z | sn47 README task/scoring sections changed |
| `sn79:readme_task_diff:cd5eac2da72f58d2` | 79 | README_TASK_DIFF | 2026-08-28T21:28:55Z | sn79 README task/scoring sections changed |
| `sn108:readme_task_diff:e13470c52cc9c2e6` | 108 | README_TASK_DIFF | 2026-08-28T21:28:55Z | sn108 README task/scoring sections changed |
| `sn47:readme_task_diff:40b567f5acce9030` | 47 | README_TASK_DIFF | 2026-08-29T10:19:28Z | sn47 README task/scoring sections changed |
| `sn100:readme_task_diff:86ff6dff152413ad` | 100 | README_TASK_DIFF | 2026-08-29T10:19:28Z | sn100 README task/scoring sections changed |
| `sn71:readme_task_diff:5ecd38a51a4692a8` | 71 | README_TASK_DIFF | 2026-08-30T01:45:42Z | sn71 README task/scoring sections changed |
| `sn45:readme_task_diff:8c971dd579660a1e` | 45 | README_TASK_DIFF | 2026-08-30T07:32:13Z | sn45 README task/scoring sections changed |
| `sn91:readme_task_diff:becad0b5e25c9292` | 91 | README_TASK_DIFF | 2026-08-30T13:20:41Z | sn91 README task/scoring sections changed |

## RESOLVED IN THIS WINDOW

_none_
