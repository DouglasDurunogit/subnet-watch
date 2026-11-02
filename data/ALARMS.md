# ALARMS - generated 2026-11-02T19:39:37Z, block 9420393

window: first_seen in [2026-11-02T18:25:04Z, 2026-11-02T19:40:04Z)  (60 min interval + 15 min overlap)

Report ONLY the rows under NEW SINCE LAST RUN. Rows under STILL OPEN were
already reported in an earlier window and must not be re-alarmed.

## NEW SINCE LAST RUN

| event_id | netuid | class | severity | first_seen_utc | one_line |
|---|---|---|---|---|---|
| `sn31:burn_drop:0.000` | 31 | BURN_DROP | P0 | 2026-11-02T19:40:04Z | sn31 burn fell 1.000 -> 0.000 - miners can earn again |
| `sn1:release:v4.6.1` | 1 | RELEASE | P1 | 2026-11-02T19:40:04Z | sn1 released v4.6.1 |
| `sn17:release:witness-diagnostics-20261102` | 17 | RELEASE | P1 | 2026-11-02T19:40:04Z | sn17 released witness-diagnostics-20261102 |
| `sn21:scoring_commit:2026-11-02T14:33:30Z` | 21 | SCORING_COMMIT | P1 | 2026-11-02T19:40:04Z | sn21 commit touches scoring: docs: Performance Max campaigns in MINER_MODEL_SPEC (draft; dates to … |
| `sn38:scoring_commit:2026-11-02T11:35:55Z` | 38 | SCORING_COMMIT | P1 | 2026-11-02T19:40:04Z | sn38 commit touches scoring: Update validator image in docker-compose.validator.yml to latest versi |
| `sn51:release:lium-protocol-v2.1.0` | 51 | RELEASE | P1 | 2026-11-02T19:40:04Z | sn51 released lium-protocol-v2.1.0 |
| `sn51:scoring_commit:2026-11-02T15:36:44Z` | 51 | SCORING_COMMIT | P1 | 2026-11-02T19:40:04Z | sn51 commit touches scoring: DAH-5327 - [P1] Validator re-sends the rm of a stuck filler so a cust… |
| `sn56:scoring_commit:2026-11-02T16:14:51Z` | 56 | SCORING_COMMIT | P1 | 2026-11-02T19:40:04Z | sn56 commit touches scoring: Fix the challenger dependency review module name so the validator can… |
| `sn66:release:v2026.11.02.3` | 66 | RELEASE | P1 | 2026-11-02T19:40:04Z | sn66 released v2026.11.02.3 |
| `sn67:scoring_commit:2026-11-02T12:42:16Z` | 67 | SCORING_COMMIT | P1 | 2026-11-02T19:40:04Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20261102.post3 |
| `sn71:scoring_commit:2026-11-02T11:14:11Z` | 71 | SCORING_COMMIT | P1 | 2026-11-02T19:40:04Z | sn71 commit touches scoring: Attribute provider telemetry to validated requested models |
| `sn81:scoring_commit:2026-11-02T10:33:52Z` | 81 | SCORING_COMMIT | P1 | 2026-11-02T19:40:04Z | sn81 commit touches scoring: feat: add retail video training inference and evaluation |
| `sn89:scoring_commit:2026-11-02T12:59:18Z` | 89 | SCORING_COMMIT | P1 | 2026-11-02T19:40:04Z | sn89 commit touches scoring: Agent scoreboard: per-algo breakdown with owner nicknames |
| `sn116:scoring_commit:2026-11-02T16:02:57Z` | 116 | SCORING_COMMIT | P1 | 2026-11-02T19:40:04Z | sn116 commit touches scoring: Miner text: a stage conflict after a receiver update may mean nothing… |
| `sn117:release:everycli v0.9.1` | 117 | RELEASE | P1 | 2026-11-02T19:40:04Z | sn117 released everycli v0.9.1 |
| `sn120:scoring_commit:2026-11-02T16:52:47Z` | 120 | SCORING_COMMIT | P1 | 2026-11-02T19:40:04Z | sn120 commit touches scoring: SN120 task cap 12K (Jacob pt1084u, 2026-11-02 10:25 CR: move the task… |
| `sn17:readme_task_diff:8c892da1ead4dfc7` | 17 | README_TASK_DIFF | P2 | 2026-11-02T19:40:04Z | sn17 README task/scoring sections changed |
| `sn117:readme_task_diff:9d04ab2709490011` | 117 | README_TASK_DIFF | P2 | 2026-11-02T19:40:04Z | sn117 README task/scoring sections changed |

### detail

- **`sn31:burn_drop:0.000`** - sn31 burn fell 1.000 -> 0.000 - miners can earn again
  - This subnet paid miners nothing and now pays. Worth a look before the field fills up.
- **`sn1:release:v4.6.1`** - sn1 released v4.6.1
  - published 2026-11-02T13:28:33Z (was v4.6.0)
- **`sn17:release:witness-diagnostics-20261102`** - sn17 released witness-diagnostics-20261102
  - published 2026-11-02T15:25:40Z (was renderer-client-v0.1.4)
- **`sn21:scoring_commit:2026-11-02T14:33:30Z`** - sn21 commit touches scoring: docs: Performance Max campaigns in MINER_MODEL_SPEC (draft; dates to …
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn38:scoring_commit:2026-11-02T11:35:55Z`** - sn38 commit touches scoring: Update validator image in docker-compose.validator.yml to latest versi
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn51:release:lium-protocol-v2.1.0`** - sn51 released lium-protocol-v2.1.0
  - published 2026-11-02T14:45:34Z (was lium-protocol-v2.0.0)
- **`sn51:scoring_commit:2026-11-02T15:36:44Z`** - sn51 commit touches scoring: DAH-5327 - [P1] Validator re-sends the rm of a stuck filler so a cust…
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn56:scoring_commit:2026-11-02T16:14:51Z`** - sn56 commit touches scoring: Fix the challenger dependency review module name so the validator can…
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn66:release:v2026.11.02.3`** - sn66 released v2026.11.02.3
  - published 2026-11-02T16:25:31Z (was v2026.10.31.2)
- **`sn67:scoring_commit:2026-11-02T12:42:16Z`** - sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20261102.post3
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn71:scoring_commit:2026-11-02T11:14:11Z`** - sn71 commit touches scoring: Attribute provider telemetry to validated requested models
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn81:scoring_commit:2026-11-02T10:33:52Z`** - sn81 commit touches scoring: feat: add retail video training inference and evaluation
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn89:scoring_commit:2026-11-02T12:59:18Z`** - sn89 commit touches scoring: Agent scoreboard: per-algo breakdown with owner nicknames
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn116:scoring_commit:2026-11-02T16:02:57Z`** - sn116 commit touches scoring: Miner text: a stage conflict after a receiver update may mean nothing…
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn117:release:everycli v0.9.1`** - sn117 released everycli v0.9.1
  - published 2026-11-02T18:59:52Z (was everycli v0.8.8)
- **`sn120:scoring_commit:2026-11-02T16:52:47Z`** - sn120 commit touches scoring: SN120 task cap 12K (Jacob pt1084u, 2026-11-02 10:25 CR: move the task…
  - Matched on the commit MESSAGE, not a file diff - weaker evidence than a release; confirm before acting.
- **`sn17:readme_task_diff:8c892da1ead4dfc7`** - sn17 README task/scoring sections changed
  - Only the task-describing headings are hashed, so badge and typo edits do not trigger this.
- **`sn117:readme_task_diff:9d04ab2709490011`** - sn117 README task/scoring sections changed
  - Only the task-describing headings are hashed, so badge and typo edits do not trigger this.

## STILL OPEN (already reported - do not re-alarm)

| event_id | netuid | class | first_seen_utc | one_line |
|---|---|---|---|---|
| `sn76:burn_drop:0.978` | 76 | BURN_DROP | 2026-10-27T01:27:07Z | sn76 burn fell 0.998 -> 0.978 - miners can earn again |
| `sn73:burn_drop:0.000` | 73 | BURN_DROP | 2026-10-27T06:46:43Z | sn73 burn fell 1.000 -> 0.000 - miners can earn again |
| `sn32:burn_drop:0.000` | 32 | BURN_DROP | 2026-10-28T20:27:26Z | sn32 burn fell 1.000 -> 0.000 - miners can earn again |
| `sn117:burn_drop:0.982` | 117 | BURN_DROP | 2026-10-28T20:27:26Z | sn117 burn fell 1.000 -> 0.982 - miners can earn again |
| `sn126:burn_drop:0.950` | 126 | BURN_DROP | 2026-10-30T16:41:00Z | sn126 burn fell 1.000 -> 0.950 - miners can earn again |
| `sn76:burn_drop:0.964` | 76 | BURN_DROP | 2026-10-30T21:08:18Z | sn76 burn fell 0.993 -> 0.964 - miners can earn again |
| `sn76:burn_drop:0.990` | 76 | BURN_DROP | 2026-11-01T13:50:47Z | sn76 burn fell 0.991 -> 0.990 - miners can earn again |
| `sn2:scoring_commit:2026-10-26T19:40:08Z` | 2 | SCORING_COMMIT | 2026-10-26T21:56:01Z | sn2 commit touches scoring: Document live Finney burn validator status |
| `sn28:release:v0.5.12` | 28 | RELEASE | 2026-10-26T21:56:01Z | sn28 released v0.5.12 |
| `sn28:scoring_commit:2026-10-24T09:19:08Z` | 28 | SCORING_COMMIT | 2026-10-26T21:56:01Z | sn28 commit touches scoring: attestd: fix the kubetee.attestation.v1 binding verification (gm-veri… |
| `sn51:scoring_commit:2026-10-26T17:40:00Z` | 51 | SCORING_COMMIT | 2026-10-26T21:56:01Z | sn51 commit touches scoring: DAH-4972 - [P1] Validator fails nodes without pid: host (#1806) |
| `sn123:scoring_commit:2026-10-26T19:14:29Z` | 123 | SCORING_COMMIT | 2026-10-26T21:56:01Z | sn123 commit touches scoring: Update validator.py |
| `sn71:scoring_commit:2026-10-27T00:51:51Z` | 71 | SCORING_COMMIT | 2026-10-27T01:27:07Z | sn71 commit touches scoring: Record the authorized evidence-verification release scope |
| `sn94:scoring_commit:2026-10-26T23:13:36Z` | 94 | SCORING_COMMIT | 2026-10-27T01:27:07Z | sn94 commit touches scoring: Accept a list of AMD ARK pins in the broker verifier config |
| `sn2:scoring_commit:2026-10-27T04:19:07Z` | 2 | SCORING_COMMIT | 2026-10-27T06:46:43Z | sn2 commit touches scoring: Score finalized epoch snapshots and log unsigned weight previews |
| `sn15:release:v3.0.5: fix(validator): policy_view.max_` | 15 | RELEASE | 2026-10-27T06:46:43Z | sn15 released v3.0.5: fix(validator): policy_view.max_steps is the task's own step limit |
| `sn15:scoring_commit:2026-10-27T04:52:29Z` | 15 | SCORING_COMMIT | 2026-10-27T06:46:43Z | sn15 commit touches scoring: fix(validator): policy_view.max_steps is the task's own step limit |
| `sn76:scoring_commit:2026-10-27T02:34:08Z` | 76 | SCORING_COMMIT | 2026-10-27T06:46:43Z | sn76 commit touches scoring: docs: sync worker CONTRACT.md (relay spend cap, verify feedback, plan… |
| `sn78:scoring_commit:2026-10-27T04:29:51Z` | 78 | SCORING_COMMIT | 2026-10-27T06:46:43Z | sn78 commit touches scoring: Merge pull request #445 from Umi-BitSign/feat/reward-operator-early-s… |
| `sn1:release:v4.5.0` | 1 | RELEASE | 2026-10-27T12:46:40Z | sn1 released v4.5.0 |
| `sn2:scoring_commit:2026-10-27T07:31:43Z` | 2 | SCORING_COMMIT | 2026-10-27T12:46:40Z | sn2 commit touches scoring: Gate unverified miner scores and refresh narrow validator dependencies |
| `sn3:scoring_commit:2026-10-27T11:33:11Z` | 3 | SCORING_COMMIT | 2026-10-27T12:46:40Z | sn3 commit touches scoring: Show per-category losses in evaluation history |
| `sn25:release:v2026.10.26-1082839840` | 25 | RELEASE | 2026-10-27T12:46:40Z | sn25 released v2026.10.26-1082839840 |
| `sn51:scoring_commit:2026-10-27T11:28:16Z` | 51 | SCORING_COMMIT | 2026-10-27T12:46:40Z | sn51 commit touches scoring: DAH-5235 - [P0] Validator: publish a node at once when its GPU comes … |
| `sn67:scoring_commit:2026-10-27T10:49:10Z` | 67 | SCORING_COMMIT | 2026-10-27T12:46:40Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20261027.post2 |
| `sn75:release:Runtime 92023` | 75 | RELEASE | 2026-10-27T12:46:40Z | sn75 released Runtime 92023 |
| `sn78:scoring_commit:2026-10-27T09:44:39Z` | 78 | SCORING_COMMIT | 2026-10-27T12:46:40Z | sn78 commit touches scoring: Cap retained reward coverage at native successor activation |
| `sn91:scoring_commit:2026-10-27T00:15:55Z` | 91 | SCORING_COMMIT | 2026-10-27T12:46:40Z | sn91 commit touches scoring: Report static-guard rejections from verify instead of crashing |
| `sn9:release:v4.13.10` | 9 | RELEASE | 2026-10-27T18:24:01Z | sn9 released v4.13.10 |
| `sn25:release:v2026.10.27-1083160450` | 25 | RELEASE | 2026-10-27T18:24:01Z | sn25 released v2026.10.27-1083160450 |
| `sn33:scoring_commit:2026-10-21T15:43:18Z` | 33 | SCORING_COMMIT | 2026-10-27T18:24:01Z | sn33 commit touches scoring: Enable 25% burn and shuffle task dispatch order |
| `sn50:scoring_commit:2026-10-27T16:16:32Z` | 50 | SCORING_COMMIT | 2026-10-27T18:24:01Z | sn50 commit touches scoring: fix(validator): resync the metagraph after a prompt that raised (#350) |
| `sn71:scoring_commit:2026-10-27T17:58:21Z` | 71 | SCORING_COMMIT | 2026-10-27T18:24:01Z | sn71 commit touches scoring: Record verified SSM cutover and permanent AWS account guidance |
| `sn78:scoring_commit:2026-10-27T18:03:38Z` | 78 | SCORING_COMMIT | 2026-10-27T18:24:01Z | sn78 commit touches scoring: Cap C7+ evaluation sources and preserve historical suite semantics (#… |
| `sn81:scoring_commit:2026-10-27T13:02:41Z` | 81 | SCORING_COMMIT | 2026-10-27T18:24:01Z | sn81 commit touches scoring: fix(rl-async): never charge miners for the validator's own downtime |
| `sn89:scoring_commit:2026-10-27T04:02:56Z` | 89 | SCORING_COMMIT | 2026-10-27T18:24:01Z | sn89 commit touches scoring: Signals entity accounts: hosted miners as subaccounts of one UID (arm… |
| `sn8:scoring_commit:2026-10-27T20:14:01Z` | 8 | SCORING_COMMIT | 2026-10-27T22:29:30Z | sn8 commit touches scoring: MinerAccountManager: one lock order (accounts → disk), fixes the orde… |
| `sn51:release:executor-v1.157` | 51 | RELEASE | 2026-10-27T22:29:30Z | sn51 released executor-v1.157 |
| `sn71:scoring_commit:2026-10-27T19:54:01Z` | 71 | SCORING_COMMIT | 2026-10-27T22:29:30Z | sn71 commit touches scoring: docs: scope Tyche capture verification and rollout |
| `sn92:release:v1.2.0-rc11.post8.1` | 92 | RELEASE | 2026-10-27T22:29:30Z | sn92 released v1.2.0-rc11.post8.1 |
| `sn92:scoring_commit:2026-10-27T22:13:15Z` | 92 | SCORING_COMMIT | 2026-10-27T22:29:30Z | sn92 commit touches scoring: 1.2.0rc11.post8.1: validator release for Wed 28 Oct 2026 12:00 UTC. E… |
| `sn34:scoring_commit:2026-10-27T23:51:10Z` | 34 | SCORING_COMMIT | 2026-10-28T01:48:43Z | sn34 commit touches scoring: Merge pull request #27 from BitMind-AI/feat/private-prepared-task-ext… |
| `sn71:scoring_commit:2026-10-28T01:19:48Z` | 71 | SCORING_COMMIT | 2026-10-28T01:48:43Z | sn71 commit touches scoring: docs: update Discord invite link |
| `sn91:scoring_commit:2026-10-28T00:15:26Z` | 91 | SCORING_COMMIT | 2026-10-28T01:48:43Z | sn91 commit touches scoring: Merge pull request #381 from TensorLink-AI/docs/validator-upgrade-11.3 |
| `sn94:scoring_commit:2026-10-27T22:57:38Z` | 94 | SCORING_COMMIT | 2026-10-28T01:48:43Z | sn94 commit touches scoring: Require AMD-verified attestation before planting an Escape nonce |
| `sn1:release:v4.5.1` | 1 | RELEASE | 2026-10-28T08:21:49Z | sn1 released v4.5.1 |
| `sn34:scoring_commit:2026-10-28T03:34:22Z` | 34 | SCORING_COMMIT | 2026-10-28T08:21:49Z | sn34 commit touches scoring: Document wording gate enforcement for new evaluations |
| `sn51:release:lium-protocol-v1.17.0` | 51 | RELEASE | 2026-10-28T08:21:49Z | sn51 released lium-protocol-v1.17.0 |
| `sn51:scoring_commit:2026-10-28T08:21:00Z` | 51 | SCORING_COMMIT | 2026-10-28T08:21:49Z | sn51 commit touches scoring: DAH-5037 - [P1] Validator: attach a default job's last log lines when… |
| `sn62:release:v0.3.14` | 62 | RELEASE | 2026-10-28T08:21:49Z | sn62 released v0.3.14 |
| `sn62:scoring_commit:2026-10-28T02:43:13Z` | 62 | SCORING_COMMIT | 2026-10-28T08:21:49Z | sn62 commit touches scoring: Merge pull request #532 from ridgesai/feat/validator-registry-dev |
| `sn71:scoring_commit:2026-10-28T08:00:36Z` | 71 | SCORING_COMMIT | 2026-10-28T08:21:49Z | sn71 commit touches scoring: Preserve verified pre-dispatch errors in Arena trajectory exports |
| `sn78:scoring_commit:2026-10-28T04:09:07Z` | 78 | SCORING_COMMIT | 2026-10-28T08:21:49Z | sn78 commit touches scoring: Merge pull request #460 from Umi-BitSign/fix/category-capacity-verifi… |
| `sn81:scoring_commit:2026-10-28T03:02:55Z` | 81 | SCORING_COMMIT | 2026-10-28T08:21:49Z | sn81 commit touches scoring: fix(eval): the auditor passes observe to score_sequences only for a d… |
| `sn28:scoring_commit:2026-10-28T14:32:16Z` | 28 | SCORING_COMMIT | 2026-10-28T15:18:42Z | sn28 commit touches scoring: Verify NEAR's GLM-5.3-Flash attested host (#359) |
| `sn32:scoring_commit:2026-10-28T07:45:48Z` | 32 | SCORING_COMMIT | 2026-10-28T15:18:42Z | sn32 commit touches scoring: Bump wandb to 0.31.0 so validator logs reach the current API (v3.15.1) |
| `sn50:release:v1.15.0` | 50 | RELEASE | 2026-10-28T15:18:42Z | sn50 released v1.15.0 |
| `sn51:scoring_commit:2026-10-28T11:12:55Z` | 51 | SCORING_COMMIT | 2026-10-28T15:18:42Z | sn51 commit touches scoring: DAH-5194 - [P1] Validator: key sshd bootstrap and registry pull state… |
| `sn53:scoring_commit:2026-10-28T10:52:11Z` | 53 | SCORING_COMMIT | 2026-10-28T15:18:42Z | sn53 commit touches scoring: Merge pull request #58 from hanlinai/feat/tee-miner-leg-rotation |
| `sn66:release:deployed/dev: Merge pull request #165 fr` | 66 | RELEASE | 2026-10-28T15:18:42Z | sn66 released deployed/dev: Merge pull request #165 from conjectures-io/feat/torchlean-intake-axiom |
| `sn78:scoring_commit:2026-10-28T14:35:16Z` | 78 | SCORING_COMMIT | 2026-10-28T15:18:42Z | sn78 commit touches scoring: Preserve verified captures and retry transient model copies (#468) |
| `sn104:scoring_commit:2026-10-28T09:46:22Z` | 104 | SCORING_COMMIT | 2026-10-28T15:18:42Z | sn104 commit touches scoring: Merge pull request #21 from taostatus/feat/python-script-miner |
| `sn114:scoring_commit:2026-10-28T14:14:48Z` | 114 | SCORING_COMMIT | 2026-10-28T15:18:42Z | sn114 commit touches scoring: Fix validator task image tag resolution |
| `sn17:release:witness-client-v0.2.15` | 17 | RELEASE | 2026-10-28T20:27:26Z | sn17 released witness-client-v0.2.15 |
| `sn66:release:v2026.10.28.2` | 66 | RELEASE | 2026-10-28T20:27:26Z | sn66 released v2026.10.28.2 |
| `sn71:scoring_commit:2026-10-28T19:43:06Z` | 71 | SCORING_COMMIT | 2026-10-28T20:27:26Z | sn71 commit touches scoring: Select preflight process helper before retained-slot recovery validati |
| `sn78:scoring_commit:2026-10-28T18:17:42Z` | 78 | SCORING_COMMIT | 2026-10-28T20:27:26Z | sn78 commit touches scoring: Reuse reservation validation and expose incremental intake progress |
| `sn97:scoring_commit:2026-10-28T16:13:46Z` | 97 | SCORING_COMMIT | 2026-10-28T20:27:26Z | sn97 commit touches scoring: feat(promoter): credit Bonsai 2 on q2 king cards by what the miner ch… |
| `sn66:release:v2026.10.28.3` | 66 | RELEASE | 2026-10-29T00:18:27Z | sn66 released v2026.10.28.3 |
| `sn71:scoring_commit:2026-10-28T22:42:44Z` | 71 | SCORING_COMMIT | 2026-10-29T00:18:27Z | sn71 commit touches scoring: Allow scored Arena publication during automatic restart drain |
| `sn78:scoring_commit:2026-10-28T23:35:18Z` | 78 | SCORING_COMMIT | 2026-10-29T00:18:27Z | sn78 commit touches scoring: Keep reserved participation fair and reuse verified cohort history |
| `sn34:scoring_commit:2026-10-29T00:52:16Z` | 34 | SCORING_COMMIT | 2026-10-29T06:10:57Z | sn34 commit touches scoring: Explain submission quota errors in the miner CLI (#32) |
| `sn51:scoring_commit:2026-10-29T05:17:40Z` | 51 | SCORING_COMMIT | 2026-10-29T06:10:57Z | sn51 commit touches scoring: DAH-5320 - [P0] Validator: idle node disk write check, shadow verdict… |
| `sn71:scoring_commit:2026-10-29T05:23:54Z` | 71 | SCORING_COMMIT | 2026-10-29T06:10:57Z | sn71 commit touches scoring: Verify terminal failure control preserves captured worker receipts |
| `sn28:release:v0.5.14` | 28 | RELEASE | 2026-10-29T13:30:23Z | sn28 released v0.5.14 |
| `sn34:scoring_commit:2026-10-29T10:49:47Z` | 34 | SCORING_COMMIT | 2026-10-29T13:30:23Z | sn34 commit touches scoring: Bound symbolic math grading and preserve unscored failures (#33) |
| `sn51:release:executor-v1.163` | 51 | RELEASE | 2026-10-29T13:30:23Z | sn51 released executor-v1.163 |
| `sn51:scoring_commit:2026-10-29T11:09:39Z` | 51 | SCORING_COMMIT | 2026-10-29T13:30:23Z | sn51 commit touches scoring: DAH-5295 - [P2] Rent survives a central-miner restart that refuses th… |
| `sn66:release:deployed/dev` | 66 | RELEASE | 2026-10-29T13:30:23Z | sn66 released deployed/dev |
| `sn67:scoring_commit:2026-10-29T05:43:31Z` | 67 | SCORING_COMMIT | 2026-10-29T13:30:23Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20261029.post1 |
| `sn71:scoring_commit:2026-10-29T09:44:23Z` | 71 | SCORING_COMMIT | 2026-10-29T13:30:23Z | sn71 commit touches scoring: Verify exact final capture after lost upload acknowledgments |
| `sn78:scoring_commit:2026-10-29T10:16:10Z` | 78 | SCORING_COMMIT | 2026-10-29T13:30:23Z | sn78 commit touches scoring: Drain evaluator status HTTP cleanup before releasing pool slots |
| `sn90:release:v1.3.2` | 90 | RELEASE | 2026-10-29T13:30:23Z | sn90 released v1.3.2 |
| `sn90:scoring_commit:2026-10-29T08:53:38Z` | 90 | SCORING_COMMIT | 2026-10-29T13:30:23Z | sn90 commit touches scoring: feat(validation): remove the minimum node-count gate |
| `sn91:scoring_commit:2026-10-29T11:38:45Z` | 91 | SCORING_COMMIT | 2026-10-29T13:30:23Z | sn91 commit touches scoring: Merge pull request #384 from TensorLink-AI/fix/energy-score-overflow |
| `sn114:scoring_commit:2026-10-29T10:47:22Z` | 114 | SCORING_COMMIT | 2026-10-29T13:30:23Z | sn114 commit touches scoring: Show reset validations as pending |
| `sn124:scoring_commit:2026-10-29T10:27:45Z` | 124 | SCORING_COMMIT | 2026-10-29T13:30:23Z | sn124 commit touches scoring: Give the Sentinel test tasks the family's own benchmark version |
| `sn1:release:v4.5.3` | 1 | RELEASE | 2026-10-29T19:17:09Z | sn1 released v4.5.3 |
| `sn25:scoring_commit:2026-10-29T14:56:25Z` | 25 | SCORING_COMMIT | 2026-10-29T19:17:09Z | sn25 commit touches scoring: Preserve deployed validator recovery in timeout release |
| `sn28:release:v0.5.15` | 28 | RELEASE | 2026-10-29T19:17:09Z | sn28 released v0.5.15 |
| `sn51:scoring_commit:2026-10-29T16:18:13Z` | 51 | SCORING_COMMIT | 2026-10-29T19:17:09Z | sn51 commit touches scoring: DAH-3698 - [P2] Validator: pay a split node's free GPUs per split tha… |
| `sn66:release:v2026.10.29` | 66 | RELEASE | 2026-10-29T19:17:09Z | sn66 released v2026.10.29 |
| `sn67:scoring_commit:2026-10-29T13:26:47Z` | 67 | SCORING_COMMIT | 2026-10-29T19:17:09Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20261029.post2 |
| `sn71:scoring_commit:2026-10-29T19:16:39Z` | 71 | SCORING_COMMIT | 2026-10-29T19:17:09Z | sn71 commit touches scoring: Preserve legacy baseline comparison authority in reward slots (#916) |
| `sn78:scoring_commit:2026-10-29T16:00:09Z` | 78 | SCORING_COMMIT | 2026-10-29T19:17:09Z | sn78 commit touches scoring: Merge pull request #496 from Umi-BitSign/fix/adaptive-challenge-lanes… |
| `sn90:release:v1.3.3` | 90 | RELEASE | 2026-10-29T19:17:09Z | sn90 released v1.3.3 |
| `sn92:release:v1.2.0-rc11.post8.1-kit1: mammoth-1 self` | 92 | RELEASE | 2026-10-29T19:17:09Z | sn92 released v1.2.0-rc11.post8.1-kit1: mammoth-1 self-check (miner side) |
| `sn92:scoring_commit:2026-10-29T16:23:25Z` | 92 | SCORING_COMMIT | 2026-10-29T19:17:09Z | sn92 commit touches scoring: 1.2.0rc11.post8.1 miner kit 1: mammoth-1 self-check for the s1-pro po… |
| `sn94:scoring_commit:2026-10-29T17:21:49Z` | 94 | SCORING_COMMIT | 2026-10-29T19:17:09Z | sn94 commit touches scoring: Room kit: attested guest TLS and hotel key install for miner hotels A… |
| `sn97:scoring_commit:2026-10-29T14:20:37Z` | 97 | SCORING_COMMIT | 2026-10-29T19:17:09Z | sn97 commit touches scoring: fix(web): drop the score axis under the dashboard's benchmark bars |
| `sn117:release:everycli v0.8.0` | 117 | RELEASE | 2026-10-29T19:17:09Z | sn117 released everycli v0.8.0 |
| `sn117:scoring_commit:2026-10-29T17:19:07Z` | 117 | SCORING_COMMIT | 2026-10-29T19:17:09Z | sn117 commit touches scoring: Add Director tool models to miner |
| `sn1:release:v4.5.4` | 1 | RELEASE | 2026-10-29T23:29:16Z | sn1 released v4.5.4 |
| `sn25:scoring_commit:2026-10-29T21:28:46Z` | 25 | SCORING_COMMIT | 2026-10-29T23:29:16Z | sn25 commit touches scoring: Merge leadertop/head-summary-spec: validator head summary v1 spec |
| `sn51:scoring_commit:2026-10-29T21:11:22Z` | 51 | SCORING_COMMIT | 2026-10-29T23:29:16Z | sn51 commit touches scoring: DAH-5177 connector lead lock TTL 15 s -> 6 s so a rollout's validator… |
| `sn62:scoring_commit:2026-10-29T20:08:25Z` | 62 | SCORING_COMMIT | 2026-10-29T23:29:16Z | sn62 commit touches scoring: Merge pull request #528 from ridgesai/feat/ridges-validators |
| `sn94:scoring_commit:2026-10-29T20:51:05Z` | 94 | SCORING_COMMIT | 2026-10-29T23:29:16Z | sn94 commit touches scoring: Validate claims-room upload paths and require https broker URL (#369) |
| `sn25:scoring_commit:2026-10-30T01:11:12Z` | 25 | SCORING_COMMIT | 2026-10-30T03:00:50Z | sn25 commit touches scoring: Merge leadertop/head-summary-upload: the validator's signed head summ… |
| `sn71:scoring_commit:2026-10-29T23:33:53Z` | 71 | SCORING_COMMIT | 2026-10-30T03:00:50Z | sn71 commit touches scoring: Ignore validator runtime state at checkout root |
| `sn89:scoring_commit:2026-10-30T01:36:45Z` | 89 | SCORING_COMMIT | 2026-10-30T03:00:50Z | sn89 commit touches scoring: Agent competition scoreboard builder |
| `sn124:scoring_commit:2026-10-30T00:04:10Z` | 124 | SCORING_COMMIT | 2026-10-30T03:00:50Z | sn124 commit touches scoring: Merge pull request #239 from swarm-subnet/feature/ali/validator-nonro… |
| `sn25:scoring_commit:2026-10-30T04:21:00Z` | 25 | SCORING_COMMIT | 2026-10-30T09:55:02Z | sn25 commit touches scoring: Expose validator preparation stages through bounded diagnostics |
| `sn51:scoring_commit:2026-10-30T09:50:10Z` | 51 | SCORING_COMMIT | 2026-10-30T09:55:02Z | sn51 commit touches scoring: DAH-5327 - [P1] Validator: a killed filler that dockerd removes withi… |
| `sn62:release:v0.3.15` | 62 | RELEASE | 2026-10-30T09:55:02Z | sn62 released v0.3.15 |
| `sn66:release:deployed/dev: Merge pull request #174 fr` | 66 | RELEASE | 2026-10-30T09:55:02Z | sn66 released deployed/dev: Merge pull request #174 from conjectures-io/fix/trace-sql-statements |
| `sn67:scoring_commit:2026-10-30T02:27:14Z` | 67 | SCORING_COMMIT | 2026-10-30T09:55:02Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20261030.post0 |
| `sn71:scoring_commit:2026-10-30T07:55:16Z` | 71 | SCORING_COMMIT | 2026-10-30T09:55:02Z | sn71 commit touches scoring: Verify accepted Greenhouse API judgments require employer ownership |
| `sn28:release:v0.5.16` | 28 | RELEASE | 2026-10-30T16:41:00Z | sn28 released v0.5.16 |
| `sn51:release:lium-protocol-v1.18.0` | 51 | RELEASE | 2026-10-30T16:41:00Z | sn51 released lium-protocol-v1.18.0 |
| `sn51:scoring_commit:2026-10-30T15:56:58Z` | 51 | SCORING_COMMIT | 2026-10-30T16:41:00Z | sn51 commit touches scoring: DAH-5393 - [P0] Validator: a full set of other GPUs re-verifies at on… |
| `sn53:scoring_commit:2026-10-30T10:03:36Z` | 53 | SCORING_COMMIT | 2026-10-30T16:41:00Z | sn53 commit touches scoring: Merge pull request #59 from hanlinai/feat/tee-miner-vllm-kv |
| `sn65:scoring_commit:2026-10-26T12:00:46Z` | 65 | SCORING_COMMIT | 2026-10-30T16:41:00Z | sn65 commit touches scoring: score all candidates |
| `sn66:release:deployed/dev: Merge pull request #176 fr` | 66 | RELEASE | 2026-10-30T16:41:00Z | sn66 released deployed/dev: Merge pull request #176 from conjectures-io/fix/bounty-open-only-missing |
| `sn97:scoring_commit:2026-10-30T14:36:17Z` | 97 | SCORING_COMMIT | 2026-10-30T16:41:00Z | sn97 commit touches scoring: feat(eval): KL decides a win, score per sample, per-domain answer cap… |
| `sn102:release:v0.7.2: Merge pull request #299 from Con` | 102 | RELEASE | 2026-10-30T16:41:00Z | sn102 released v0.7.2: Merge pull request #299 from Connito-AI/feat/validator-prompt-blend |
| `sn102:scoring_commit:2026-10-30T14:28:47Z` | 102 | SCORING_COMMIT | 2026-10-30T16:41:00Z | sn102 commit touches scoring: Merge pull request #299 from Connito-AI/feat/validator-prompt-blend |
| `sn15:release:v3.0.6: fix(validator): keep sandbox out` | 15 | RELEASE | 2026-10-30T21:08:18Z | sn15 released v3.0.6: fix(validator): keep sandbox output from blocking run completion |
| `sn15:scoring_commit:2026-10-30T18:12:56Z` | 15 | SCORING_COMMIT | 2026-10-30T21:08:18Z | sn15 commit touches scoring: fix(validator): keep sandbox output from blocking run completion |
| `sn25:scoring_commit:2026-10-30T18:12:19Z` | 25 | SCORING_COMMIT | 2026-10-30T21:08:18Z | sn25 commit touches scoring: Require verified empty EMA prior for head replica bootstrap |
| `sn117:release:everycli v0.8.2` | 117 | RELEASE | 2026-10-30T21:08:18Z | sn117 released everycli v0.8.2 |
| `sn117:scoring_commit:2026-10-30T19:57:17Z` | 117 | SCORING_COMMIT | 2026-10-30T21:08:18Z | sn117 commit touches scoring: Document the combined v0.8.2 miner and CLI fixes |
| `sn25:release:v2026.10.30-1086064830` | 25 | RELEASE | 2026-10-31T00:56:30Z | sn25 released v2026.10.30-1086064830 |
| `sn78:scoring_commit:2026-10-30T23:30:40Z` | 78 | SCORING_COMMIT | 2026-10-31T00:56:30Z | sn78 commit touches scoring: Add quality-gated CPU efficiency rewards for C8+ [skip ci] |
| `sn91:scoring_commit:2026-10-30T21:27:46Z` | 91 | SCORING_COMMIT | 2026-10-31T00:56:30Z | sn91 commit touches scoring: bench data: a completion marker only for a verified-complete pull |
| `sn116:scoring_commit:2026-10-30T22:43:52Z` | 116 | SCORING_COMMIT | 2026-10-31T00:56:30Z | sn116 commit touches scoring: MINING: help contact is the owner's Telegram (no Discord) |
| `sn25:scoring_commit:2026-10-31T06:54:01Z` | 25 | SCORING_COMMIT | 2026-10-31T06:56:23Z | sn25 commit touches scoring: Record the census fix deployment in taskworker 1086289460 |
| `sn34:scoring_commit:2026-10-30T23:21:18Z` | 34 | SCORING_COMMIT | 2026-10-31T06:56:23Z | sn34 commit touches scoring: fix: score empty stopped ArenaHard answers as incorrect |
| `sn51:scoring_commit:2026-10-31T03:32:27Z` | 51 | SCORING_COMMIT | 2026-10-31T06:56:23Z | sn51 commit touches scoring: DAH-5457 - [P0] Validator: GPU drop report lists the new cards after … |
| `sn62:release:v0.3.16` | 62 | RELEASE | 2026-10-31T06:56:23Z | sn62 released v0.3.16 |
| `sn71:scoring_commit:2026-10-31T03:57:05Z` | 71 | SCORING_COMMIT | 2026-10-31T06:56:23Z | sn71 commit touches scoring: Keep validator checkout warnings out of usable training evidence |
| `sn91:scoring_commit:2026-10-31T03:06:40Z` | 91 | SCORING_COMMIT | 2026-10-31T06:56:23Z | sn91 commit touches scoring: King leg: channel floor by ref, ignore the challenger abort |
| `sn116:scoring_commit:2026-10-30T23:26:11Z` | 116 | SCORING_COMMIT | 2026-10-31T06:56:23Z | sn116 commit touches scoring: Record five owner decisions given in the Validator session (repack al… |
| `sn120:scoring_commit:2026-10-31T01:15:16Z` | 120 | SCORING_COMMIT | 2026-10-31T06:56:23Z | sn120 commit touches scoring: SN120 free-file protocol: miners upload one affine-batch-v1 file (pro… |
| `sn14:scoring_commit:2026-10-30T14:38:17Z` | 14 | SCORING_COMMIT | 2026-10-31T13:35:59Z | sn14 commit touches scoring: Pay no first PASS under the reward margin over stock |
| `sn67:scoring_commit:2026-10-31T05:58:58Z` | 67 | SCORING_COMMIT | 2026-10-31T13:35:59Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20261031.post0 |
| `sn91:scoring_commit:2026-10-31T08:20:08Z` | 91 | SCORING_COMMIT | 2026-10-31T13:35:59Z | sn91 commit touches scoring: Merge pull request #393 from TensorLink-AI/feat/miner-cost-protections |
| `sn108:scoring_commit:2026-10-31T11:29:59Z` | 108 | SCORING_COMMIT | 2026-10-31T13:35:59Z | sn108 commit touches scoring: Between quests the validator checks its EDA server too, so its status… |
| `sn21:scoring_commit:2026-10-31T13:41:41Z` | 21 | SCORING_COMMIT | 2026-10-31T17:58:00Z | sn21 commit touches scoring: docs: the settling window is 2 days everywhere - MINER_MODEL_SPEC (li… |
| `sn71:scoring_commit:2026-10-31T16:38:42Z` | 71 | SCORING_COMMIT | 2026-10-31T17:58:00Z | sn71 commit touches scoring: Preserve verified training pairs from incomplete captures |
| `sn116:scoring_commit:2026-10-31T14:24:06Z` | 116 | SCORING_COMMIT | 2026-10-31T17:58:00Z | sn116 commit touches scoring: Miner client: every HTTP call to a door sends one explicit agent, nev… |
| `sn120:scoring_commit:2026-10-31T13:21:27Z` | 120 | SCORING_COMMIT | 2026-10-31T17:58:00Z | sn120 commit touches scoring: SN120 legacy removal docs: llms.txt (site + dashboard copy) and miner… |
| `sn1:release:v4.6.0` | 1 | RELEASE | 2026-10-31T21:27:52Z | sn1 released v4.6.0 |
| `sn11:release:v0.7.6` | 11 | RELEASE | 2026-10-31T21:27:52Z | sn11 released v0.7.6 |
| `sn11:scoring_commit:2026-10-31T19:27:19Z` | 11 | SCORING_COMMIT | 2026-10-31T21:27:52Z | sn11 commit touches scoring: chore(release): validator 0.7.6 for bounded two-worker SPEC 28 (#343) |
| `sn25:scoring_commit:2026-10-31T20:35:44Z` | 25 | SCORING_COMMIT | 2026-10-31T21:27:52Z | sn25 commit touches scoring: Merge feat/miner-pprof: opt-in pprof and a SIGUSR1 goroutine dump for… |
| `sn34:scoring_commit:2026-10-31T20:28:37Z` | 34 | SCORING_COMMIT | 2026-10-31T21:27:52Z | sn34 commit touches scoring: Batch frozen tasks with redundant sandbox defaults (#40) |
| `sn71:scoring_commit:2026-10-31T18:53:55Z` | 71 | SCORING_COMMIT | 2026-10-31T21:27:52Z | sn71 commit touches scoring: Keep admission source review on verified Google Vertex provider (#950) |
| `sn116:scoring_commit:2026-10-31T17:37:40Z` | 116 | SCORING_COMMIT | 2026-10-31T21:27:52Z | sn116 commit touches scoring: Rewards: testnet-winner-v5-launch resets a king's clock on a verified… |
| `sn117:release:everycli v0.8.3` | 117 | RELEASE | 2026-10-31T21:27:52Z | sn117 released everycli v0.8.3 |
| `sn120:scoring_commit:2026-10-31T18:43:36Z` | 120 | SCORING_COMMIT | 2026-10-31T21:27:52Z | sn120 commit touches scoring: SN120 miner kit (miner/): everything a miner needs, verbatim from the… |
| `sn15:release:v3.0.7` | 15 | RELEASE | 2026-11-01T00:27:23Z | sn15 released v3.0.7 |
| `sn66:release:v2026.10.31.2` | 66 | RELEASE | 2026-11-01T00:27:23Z | sn66 released v2026.10.31.2 |
| `sn11:release:v0.7.7` | 11 | RELEASE | 2026-11-01T06:44:04Z | sn11 released v0.7.7 |
| `sn11:scoring_commit:2026-11-01T04:20:23Z` | 11 | SCORING_COMMIT | 2026-11-01T06:44:04Z | sn11 commit touches scoring: [coding-agent] bump validator version to 0.7.7 (#345) |
| `sn81:scoring_commit:2026-11-01T05:43:16Z` | 81 | SCORING_COMMIT | 2026-11-01T06:44:04Z | sn81 commit touches scoring: Merge pull request #435 from reliquadotai/feat/job-verification-params |
| `sn9:release:v4.14.0` | 9 | RELEASE | 2026-11-01T13:50:47Z | sn9 released v4.14.0 |
| `sn28:release:v0.5.17-dev` | 28 | RELEASE | 2026-11-01T13:50:47Z | sn28 released v0.5.17-dev |
| `sn91:scoring_commit:2026-11-01T12:26:46Z` | 91 | SCORING_COMMIT | 2026-11-01T13:50:47Z | sn91 commit touches scoring: Merge pull request #409 from TensorLink-AI/fix/init-bench-validator-s… |
| `sn94:scoring_commit:2026-11-01T10:17:21Z` | 94 | SCORING_COMMIT | 2026-11-01T13:50:47Z | sn94 commit touches scoring: Remove stale miner box runbook and seedbox proof template (#341) |
| `sn116:scoring_commit:2026-11-01T12:55:30Z` | 116 | SCORING_COMMIT | 2026-11-01T13:50:47Z | sn116 commit touches scoring: MINING.md: practice time limit wording per Validator (per-Challenge, … |
| `sn120:scoring_commit:2026-11-01T13:06:32Z` | 120 | SCORING_COMMIT | 2026-11-01T13:50:47Z | sn120 commit touches scoring: bench tools: per-task MATH-500 cross-check vs calibrated runner |
| `sn116:scoring_commit:2026-11-01T15:36:00Z` | 116 | SCORING_COMMIT | 2026-11-01T18:53:08Z | sn116 commit touches scoring: GPU receipt worker: the per-task run directory is operator-only (0700) |
| `sn117:release:everycli v0.8.4` | 117 | RELEASE | 2026-11-01T18:53:08Z | sn117 released everycli v0.8.4 |
| `sn11:scoring_commit:2026-11-01T22:44:28Z` | 11 | SCORING_COMMIT | 2026-11-01T22:45:13Z | sn11 commit touches scoring: [coding-agent] remove automatic alpha burn from miner sample (#346) |
| `sn28:release:v0.5.18` | 28 | RELEASE | 2026-11-01T22:45:13Z | sn28 released v0.5.18 |
| `sn117:release:everycli v0.8.6` | 117 | RELEASE | 2026-11-01T22:45:13Z | sn117 released everycli v0.8.6 |
| `sn117:release:Merge pull request #57: everycli v0.8.7 ` | 117 | RELEASE | 2026-11-02T01:55:13Z | sn117 released Merge pull request #57: everycli v0.8.7 UI reliability |
| `sn120:scoring_commit:2026-11-02T00:27:39Z` | 120 | SCORING_COMMIT | 2026-11-02T01:55:13Z | sn120 commit touches scoring: bench site: Avg is the first score column (right after Model), divide… |
| `sn17:release:renderer-client-v0.1.4` | 17 | RELEASE | 2026-11-02T09:22:38Z | sn17 released renderer-client-v0.1.4 |
| `sn51:release:lium-protocol-v2.0.0` | 51 | RELEASE | 2026-11-02T09:22:38Z | sn51 released lium-protocol-v2.0.0 |
| `sn51:scoring_commit:2026-11-02T08:40:07Z` | 51 | SCORING_COMMIT | 2026-11-02T09:22:38Z | sn51 commit touches scoring: DAH-5329 - [P1] Validator: fail CC B200/B300 nodes below NVIDIA's R59… |
| `sn56:scoring_commit:2026-11-02T02:50:07Z` | 56 | SCORING_COMMIT | 2026-11-02T09:22:38Z | sn56 commit touches scoring: Redraw text round 1 tasks longer than 2.5h (#1417) |
| `sn71:scoring_commit:2026-11-02T05:03:07Z` | 71 | SCORING_COMMIT | 2026-11-02T09:22:38Z | sn71 commit touches scoring: Keep historical source-access fixtures on their frozen scorer |
| `sn91:scoring_commit:2026-11-02T05:05:14Z` | 91 | SCORING_COMMIT | 2026-11-02T09:22:38Z | sn91 commit touches scoring: Merge pull request #414 from TensorLink-AI/feat/miner-iterate-pool-ben |
| `sn94:scoring_commit:2026-11-02T07:36:46Z` | 94 | SCORING_COMMIT | 2026-11-02T09:22:38Z | sn94 commit touches scoring: Drop deleted MINER_BOX_RUNBOOK from docs integrity. (#382) |
| `sn117:release:everycli v0.8.8` | 117 | RELEASE | 2026-11-02T09:22:38Z | sn117 released everycli v0.8.8 |
| `sn120:scoring_commit:2026-11-02T01:58:06Z` | 120 | SCORING_COMMIT | 2026-11-02T09:22:38Z | sn120 commit touches scoring: gate: task-level cap rule from E507 - RED if >= 33% of the candidate'… |
| `sn2:readme_task_diff:48eb164474c3f6a5` | 2 | README_TASK_DIFF | 2026-10-26T21:56:01Z | sn2 README task/scoring sections changed |
| `sn123:readme_task_diff:f9658db3bedf0002` | 123 | README_TASK_DIFF | 2026-10-27T01:27:07Z | sn123 README task/scoring sections changed |
| `sn125:readme_task_diff:1476e035289bbae4` | 125 | README_TASK_DIFF | 2026-10-27T01:27:07Z | sn125 README task/scoring sections changed |
| `sn2:readme_task_diff:1ff49772ce88e83f` | 2 | README_TASK_DIFF | 2026-10-27T06:46:43Z | sn2 README task/scoring sections changed |
| `sn123:readme_task_diff:923cc435a761cf7e` | 123 | README_TASK_DIFF | 2026-10-27T06:46:43Z | sn123 README task/scoring sections changed |
| `sn2:readme_task_diff:db6ec8f75a1e4b61` | 2 | README_TASK_DIFF | 2026-10-27T12:46:40Z | sn2 README task/scoring sections changed |
| `sn91:readme_task_diff:9eb19065ad44711d` | 91 | README_TASK_DIFF | 2026-10-27T12:46:40Z | sn91 README task/scoring sections changed |
| `sn90:readme_task_diff:54113dbfe0b14a98` | 90 | README_TASK_DIFF | 2026-10-29T13:30:23Z | sn90 README task/scoring sections changed |
| `sn124:readme_task_diff:25de0bc84cbb03ae` | 124 | README_TASK_DIFF | 2026-10-29T13:30:23Z | sn124 README task/scoring sections changed |
| `sn51:readme_task_diff:2556ca8f0ae41586` | 51 | README_TASK_DIFF | 2026-10-29T19:17:09Z | sn51 README task/scoring sections changed |
| `sn21:readme_task_diff:65365716ac8dc6df` | 21 | README_TASK_DIFF | 2026-10-31T17:58:00Z | sn21 README task/scoring sections changed |
| `sn117:readme_task_diff:b849af97332968e4` | 117 | README_TASK_DIFF | 2026-10-31T21:27:52Z | sn117 README task/scoring sections changed |

## RESOLVED IN THIS WINDOW

_none_
