# ALARMS - generated 2026-08-27T03:26:25Z, block 8933701

window: first_seen in [2026-08-27T02:11:56Z, 2026-08-27T03:26:56Z)  (60 min interval + 15 min overlap)

Report ONLY the rows under NEW SINCE LAST RUN. Rows under STILL OPEN were
already reported in an earlier window and must not be re-alarmed.

## NEW SINCE LAST RUN

| event_id | netuid | class | severity | first_seen_utc | one_line |
|---|---|---|---|---|---|
| `sn25:release:v2026.8.26-1029908500` | 25 | RELEASE | P1 | 2026-08-27T03:26:56Z | sn25 released v2026.8.26-1029908500 |

### detail

- **`sn25:release:v2026.8.26-1029908500`** - sn25 released v2026.8.26-1029908500
  - published 2026-08-27T00:41:41Z (was v2026.8.26-1029569170)

## STILL OPEN (already reported - do not re-alarm)

| event_id | netuid | class | first_seen_utc | one_line |
|---|---|---|---|---|
| `sn80:burn_drop:0.908` | 80 | BURN_DROP | 2026-08-20T05:42:25Z | sn80 burn fell 1.000 -> 0.908 - miners can earn again |
| `sn7:burn_drop:0.978` | 7 | BURN_DROP | 2026-08-20T08:54:06Z | sn7 burn fell 0.992 -> 0.978 - miners can earn again |
| `sn113:burn_drop:0.990` | 113 | BURN_DROP | 2026-08-20T08:54:06Z | sn113 burn fell 1.000 -> 0.990 - miners can earn again |
| `sn121:burn_drop:0.611` | 121 | BURN_DROP | 2026-08-20T18:15:10Z | sn121 burn fell 1.000 -> 0.611 - miners can earn again |
| `sn92:burn_drop:0.971` | 92 | BURN_DROP | 2026-08-24T18:16:08Z | sn92 burn fell 1.000 -> 0.971 - miners can earn again |
| `sn121:burn_drop:0.657` | 121 | BURN_DROP | 2026-08-25T14:13:01Z | sn121 burn fell 1.000 -> 0.657 - miners can earn again |
| `sn7:burn_drop:0.910` | 7 | BURN_DROP | 2026-08-26T22:23:22Z | sn7 burn fell 1.000 -> 0.910 - miners can earn again |
| `sn21:release:SN21 rich training data v2` | 21 | RELEASE | 2026-08-20T03:58:21Z | sn21 released SN21 rich training data v2 |
| `sn23:scoring_commit:2026-08-20T03:45:52Z` | 23 | SCORING_COMMIT | 2026-08-20T03:58:21Z | sn23 commit touches scoring: Merge pull request #48 from TrishoolAI/feat/challenge-creation |
| `sn100:scoring_commit:2026-08-20T03:53:06Z` | 100 | SCORING_COMMIT | 2026-08-20T03:58:21Z | sn100 commit touches scoring: Merge pull request #166 from BaseIntelligence/prism-v2.1-scoring |
| `sn71:scoring_commit:2026-08-20T03:58:52Z` | 71 | SCORING_COMMIT | 2026-08-20T04:49:21Z | sn71 commit touches scoring: Preserve restart timing across miner bootstrap handoff |
| `sn111:scoring_commit:2026-08-20T07:12:31Z` | 111 | SCORING_COMMIT | 2026-08-20T07:23:41Z | sn111 commit touches scoring: fix(scoring): handle missing claim assessments safely |
| `sn51:scoring_commit:2026-08-20T07:41:14Z` | 51 | SCORING_COMMIT | 2026-08-20T08:05:07Z | sn51 commit touches scoring: DAH-2715: withhold the unrented incentive from executors that cannot … |
| `sn71:scoring_commit:2026-08-20T08:18:13Z` | 71 | SCORING_COMMIT | 2026-08-20T08:54:06Z | sn71 commit touches scoring: Keep validator CID diagnostics off JSON stdout |
| `sn75:scoring_commit:2026-08-20T08:51:35Z` | 75 | SCORING_COMMIT | 2026-08-20T08:54:06Z | sn75 commit touches scoring: Merge pull request #53 from thenervelab/fix/payminers-from-arion |
| `sn67:scoring_commit:2026-08-20T07:52:49Z` | 67 | SCORING_COMMIT | 2026-08-20T09:47:27Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20260820.post5 |
| `sn92:scoring_commit:2026-08-20T09:42:59Z` | 92 | SCORING_COMMIT | 2026-08-20T09:47:27Z | sn92 commit touches scoring: Take telemetry from miners and serve it back |
| `sn100:release:v3.3.26: fix(validator): persist last se` | 100 | RELEASE | 2026-08-20T09:47:27Z | sn100 released v3.3.26: fix(validator): persist last sealed bundle across restarts |
| `sn100:scoring_commit:2026-08-20T09:41:45Z` | 100 | SCORING_COMMIT | 2026-08-20T09:47:27Z | sn100 commit touches scoring: Merge pull request #183 from BaseIntelligence/fix/validator-public-we… |
| `sn44:scoring_commit:2026-08-20T09:49:53Z` | 44 | SCORING_COMMIT | 2026-08-20T10:16:11Z | sn44 commit touches scoring: update min challenge private |
| `sn92:scoring_commit:2026-08-20T10:11:04Z` | 92 | SCORING_COMMIT | 2026-08-20T10:16:11Z | sn92 commit touches scoring: Add the miner axon and document telemetry |
| `sn89:scoring_commit:2026-08-20T10:46:55Z` | 89 | SCORING_COMMIT | 2026-08-20T10:57:10Z | sn89 commit touches scoring: scripts/import_checkpoint.py: seed a validator journal from the publi… |
| `sn21:scoring_commit:2026-08-20T11:28:23Z` | 21 | SCORING_COMMIT | 2026-08-20T11:38:02Z | sn21 commit touches scoring: docs: point miners at rich training v2 and the expanded change types |
| `sn89:scoring_commit:2026-08-20T11:37:34Z` | 89 | SCORING_COMMIT | 2026-08-20T11:38:02Z | sn89 commit touches scoring: build_hf_scoreboard: HF status speaks the LF vocabulary |
| `sn28:release:v0.4.9-dev` | 28 | RELEASE | 2026-08-20T12:15:50Z | sn28 released v0.4.9-dev |
| `sn66:release:Payment and IAM update` | 66 | RELEASE | 2026-08-20T13:27:01Z | sn66 released Payment and IAM update |
| `sn10:scoring_commit:2026-08-20T12:49:41Z` | 10 | SCORING_COMMIT | 2026-08-20T14:10:38Z | sn10 commit touches scoring: feat(api): public read API for rounds, leader, and score progress |
| `sn28:release:v0.4.9` | 28 | RELEASE | 2026-08-20T14:10:38Z | sn28 released v0.4.9 |
| `sn89:scoring_commit:2026-08-20T13:41:37Z` | 89 | SCORING_COMMIT | 2026-08-20T14:10:38Z | sn89 commit touches scoring: README: a validator needs NO market-data key, and never needed a Taos… |
| `sn10:scoring_commit:2026-08-20T15:19:13Z` | 10 | SCORING_COMMIT | 2026-08-20T15:47:11Z | sn10 commit touches scoring: fix(worker): pass leaders.last_score to rank_round |
| `sn53:scoring_commit:2026-08-20T15:30:56Z` | 53 | SCORING_COMMIT | 2026-08-20T15:47:11Z | sn53 commit touches scoring: tee_miner: lift the 1 MiB websocket frame cap that 504s long-context … |
| `sn100:release:v3.3.27` | 100 | RELEASE | 2026-08-20T15:47:11Z | sn100 released v3.3.27 |
| `sn100:scoring_commit:2026-08-20T15:17:43Z` | 100 | SCORING_COMMIT | 2026-08-20T15:47:11Z | sn100 commit touches scoring: fix(design-challenge): drop crate_name so loc-cap is under 1500 |
| `sn21:scoring_commit:2026-08-20T15:58:11Z` | 21 | SCORING_COMMIT | 2026-08-20T16:17:45Z | sn21 commit touches scoring: docs: rich-era corrections in scoring architecture + whitepaper |
| `sn71:scoring_commit:2026-08-20T16:25:08Z` | 71 | SCORING_COMMIT | 2026-08-20T17:01:22Z | sn71 commit touches scoring: Bind local readiness verifier environment |
| `sn33:scoring_commit:2026-08-20T17:21:26Z` | 33 | SCORING_COMMIT | 2026-08-20T17:41:16Z | sn33 commit touches scoring: Merge pull request #136 from afterpartyai/Fix-Validator-timeout |
| `sn111:scoring_commit:2026-08-20T17:04:54Z` | 111 | SCORING_COMMIT | 2026-08-20T17:41:16Z | sn111 commit touches scoring: docs(validation): document resilient diagnostic batching |
| `sn71:scoring_commit:2026-08-20T18:02:42Z` | 71 | SCORING_COMMIT | 2026-08-20T18:15:10Z | sn71 commit touches scoring: Repair release verifier test isolation |
| `sn89:scoring_commit:2026-08-20T18:09:55Z` | 89 | SCORING_COMMIT | 2026-08-20T18:15:10Z | sn89 commit touches scoring: HF: apply owner-hosted miner integrity verdicts alongside the in-repo… |
| `sn18:release:Release 2.1.2` | 18 | RELEASE | 2026-08-20T19:55:22Z | sn18 released Release 2.1.2 |
| `sn25:release:v2026.8.20-1024555910` | 25 | RELEASE | 2026-08-20T20:41:45Z | sn25 released v2026.8.20-1024555910 |
| `sn13:release:Release v1.18.71` | 13 | RELEASE | 2026-08-20T21:13:04Z | sn13 released Release v1.18.71 |
| `sn13:scoring_commit:2026-08-13T06:08:42Z` | 13 | SCORING_COMMIT | 2026-08-20T21:13:04Z | sn13 commit touches scoring: fix(s3): stop charging miners for passing validation and for growing |
| `sn25:release:v2026.8.20-1024590520` | 25 | RELEASE | 2026-08-20T21:13:04Z | sn25 released v2026.8.20-1024590520 |
| `sn25:scoring_commit:2026-08-20T20:47:44Z` | 25 | SCORING_COMMIT | 2026-08-20T21:13:04Z | sn25 commit touches scoring: Fix miner Windows arm64 cross-build |
| `sn34:scoring_commit:2026-08-20T21:18:29Z` | 34 | SCORING_COMMIT | 2026-08-20T21:53:19Z | sn34 commit touches scoring: tune: double generator challenge frequency (#425) |
| `sn92:scoring_commit:2026-08-20T21:18:03Z` | 92 | SCORING_COMMIT | 2026-08-20T22:40:23Z | sn92 commit touches scoring: Drop the task generator in favour of uploaded corpora |
| `sn34:scoring_commit:2026-08-20T22:43:19Z` | 34 | SCORING_COMMIT | 2026-08-20T23:08:56Z | sn34 commit touches scoring: fix: restore validator config parsing (#427) |
| `sn91:scoring_commit:2026-08-20T23:02:51Z` | 91 | SCORING_COMMIT | 2026-08-20T23:08:56Z | sn91 commit touches scoring: Merge pull request #203 from TensorLink-AI/claude/miner-dethrone-bar |
| `sn34:release:Release 4.9.8` | 34 | RELEASE | 2026-08-21T01:54:45Z | sn34 released Release 4.9.8 |
| `sn53:scoring_commit:2026-08-21T04:53:19Z` | 53 | SCORING_COMMIT | 2026-08-21T05:04:00Z | sn53 commit touches scoring: tee_miner: absorb the reference miner's newer fixes |
| `sn67:scoring_commit:2026-08-21T03:07:16Z` | 67 | SCORING_COMMIT | 2026-08-21T05:46:36Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20260821.post1 |
| `sn100:release:v3.3.28` | 100 | RELEASE | 2026-08-21T07:23:29Z | sn100 released v3.3.28 |
| `sn100:scoring_commit:2026-08-21T06:46:39Z` | 100 | SCORING_COMMIT | 2026-08-21T07:23:29Z | sn100 commit touches scoring: feat(prism): miner Verda BYOK alongside Lium |
| `sn14:release:Fused-epilogue kernel submission archive` | 14 | RELEASE | 2026-08-21T09:49:58Z | sn14 released Fused-epilogue kernel submission archive (2026-08-21) |
| `sn67:scoring_commit:2026-08-21T10:10:17Z` | 67 | SCORING_COMMIT | 2026-08-21T10:43:26Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20260821.post3 |
| `sn25:release:v2026.8.21-1025093570` | 25 | RELEASE | 2026-08-21T11:11:10Z | sn25 released v2026.8.21-1025093570 |
| `sn25:release:v2026.8.21-1025114260` | 25 | RELEASE | 2026-08-21T11:52:03Z | sn25 released v2026.8.21-1025114260 |
| `sn21:scoring_commit:2026-08-21T12:29:40Z` | 21 | SCORING_COMMIT | 2026-08-21T13:07:23Z | sn21 commit touches scoring: feat(verify): mirror the daily verification feeds to the operator API… |
| `sn81:scoring_commit:2026-08-21T12:10:41Z` | 81 | SCORING_COMMIT | 2026-08-21T13:07:23Z | sn81 commit touches scoring: verify short (<CHALLENGE_K) completions at full coverage instead of h… |
| `sn92:scoring_commit:2026-08-21T11:56:26Z` | 92 | SCORING_COMMIT | 2026-08-21T13:07:23Z | sn92 commit touches scoring: Verify the gguf pin inline, since tests are not published |
| `sn108:scoring_commit:2026-08-21T13:03:07Z` | 108 | SCORING_COMMIT | 2026-08-21T13:07:23Z | sn108 commit touches scoring: docs(miner): eligibility now requires active members, not just regist… |
| `sn108:scoring_commit:2026-08-21T13:19:16Z` | 108 | SCORING_COMMIT | 2026-08-21T13:57:42Z | sn108 commit touches scoring: fix(evaluation): reuse the prefix cache the pinned transformers return |
| `sn1:release:v4.3.6` | 1 | RELEASE | 2026-08-21T14:50:15Z | sn1 released v4.3.6 |
| `sn25:release:v2026.8.21-1025223880` | 25 | RELEASE | 2026-08-21T14:50:15Z | sn25 released v2026.8.21-1025223880 |
| `sn21:scoring_commit:2026-08-21T16:09:09Z` | 21 | SCORING_COMMIT | 2026-08-21T16:15:59Z | sn21 commit touches scoring: docs: quickstart matches production — mirror for daily verification, … |
| `sn102:release:v0.5.0` | 102 | RELEASE | 2026-08-21T16:15:59Z | sn102 released v0.5.0 |
| `sn102:scoring_commit:2026-08-20T22:32:03Z` | 102 | SCORING_COMMIT | 2026-08-21T16:15:59Z | sn102 commit touches scoring: Merge pull request #223 from Connito-AI/feat/validator-observer-mode-v |
| `sn92:scoring_commit:2026-08-21T16:31:36Z` | 92 | SCORING_COMMIT | 2026-08-21T17:00:58Z | sn92 commit touches scoring: Turn provenance off until the run store can accept miner runs |
| `sn25:release:v2026.8.21-1025339670` | 25 | RELEASE | 2026-08-21T18:14:54Z | sn25 released v2026.8.21-1025339670 |
| `sn89:scoring_commit:2026-08-21T18:27:38Z` | 89 | SCORING_COMMIT | 2026-08-21T19:06:46Z | sn89 commit touches scoring: Scoring: build the qualified-win as-of window from RESOLVED outcomes |
| `sn92:release:v0.1.0` | 92 | RELEASE | 2026-08-21T19:06:46Z | sn92 released v0.1.0 |
| `sn92:scoring_commit:2026-08-21T18:54:26Z` | 92 | SCORING_COMMIT | 2026-08-21T19:06:46Z | sn92 commit touches scoring: Install the signer's keypair and verify the release the way a validat… |
| `sn90:release:v1.1.5` | 90 | RELEASE | 2026-08-21T22:02:40Z | sn90 released v1.1.5 |
| `sn90:scoring_commit:2026-08-21T22:02:06Z` | 90 | SCORING_COMMIT | 2026-08-21T22:02:40Z | sn90 commit touches scoring: fix(validator): fall back to CoinGecko TAO/USD when Taostats 429s |
| `sn15:scoring_commit:2026-08-21T23:12:08Z` | 15 | SCORING_COMMIT | 2026-08-21T23:35:34Z | sn15 commit touches scoring: chore: remove dead BackendClient top-miner and race-history methods (… |
| `sn97:scoring_commit:2026-08-21T17:21:07Z` | 97 | SCORING_COMMIT | 2026-08-22T00:02:04Z | sn97 commit touches scoring: feat: weighted reference-anchored scoring, split rubric, submit proto… |
| `sn25:release:v2026.8.21-1025613560` | 25 | RELEASE | 2026-08-22T01:47:37Z | sn25 released v2026.8.21-1025613560 |
| `sn53:scoring_commit:2026-08-22T01:50:29Z` | 53 | SCORING_COMMIT | 2026-08-22T02:43:43Z | sn53 commit touches scoring: fix(validator): reuse one chain connection instead of leaking one per… |
| `sn92:scoring_commit:2026-08-22T01:59:31Z` | 92 | SCORING_COMMIT | 2026-08-22T02:43:43Z | sn92 commit touches scoring: Sort the constants import in the validator context |
| `sn53:release:v0.4.5: Merge pull request #42 from hanl` | 53 | RELEASE | 2026-08-22T04:17:59Z | sn53 released v0.4.5: Merge pull request #42 from hanlinai/release/0.4.5 |
| `sn100:release:v3.3.29` | 100 | RELEASE | 2026-08-22T04:17:59Z | sn100 released v3.3.29 |
| `sn25:release:v2026.8.21-1025763520` | 25 | RELEASE | 2026-08-22T05:38:35Z | sn25 released v2026.8.21-1025763520 |
| `sn92:release:v0.1.1` | 92 | RELEASE | 2026-08-22T05:38:35Z | sn92 released v0.1.1 |
| `sn92:scoring_commit:2026-08-22T05:35:10Z` | 92 | SCORING_COMMIT | 2026-08-22T05:38:35Z | sn92 commit touches scoring: Package the version validators actually run |
| `sn61:release:4.9.7` | 61 | RELEASE | 2026-08-22T08:03:45Z | sn61 released 4.9.7 |
| `sn61:scoring_commit:2026-08-22T02:19:35Z` | 61 | SCORING_COMMIT | 2026-08-22T08:03:45Z | sn61 commit touches scoring: deps: update abs_challenge submodule to version 6.0.4 |
| `sn92:release:v0.1.2` | 92 | RELEASE | 2026-08-22T08:03:45Z | sn92 released v0.1.2 |
| `sn92:release:v0.1.3` | 92 | RELEASE | 2026-08-22T08:45:06Z | sn92 released v0.1.3 |
| `sn92:release:v0.1.4` | 92 | RELEASE | 2026-08-22T09:13:18Z | sn92 released v0.1.4 |
| `sn44:scoring_commit:2026-08-22T10:30:38Z` | 44 | SCORING_COMMIT | 2026-08-22T10:36:27Z | sn44 commit touches scoring: Merge pull request #54 from score-technologies/hardening-latency-loop |
| `sn92:release:v0.1.6` | 92 | RELEASE | 2026-08-22T10:36:27Z | sn92 released v0.1.6 |
| `sn92:release:v0.1.7` | 92 | RELEASE | 2026-08-22T11:32:10Z | sn92 released v0.1.7 |
| `sn92:release:v0.1.9` | 92 | RELEASE | 2026-08-22T12:01:08Z | sn92 released v0.1.9 |
| `sn92:release:v0.1.11` | 92 | RELEASE | 2026-08-22T12:57:33Z | sn92 released v0.1.11 |
| `sn92:scoring_commit:2026-08-22T12:40:53Z` | 92 | SCORING_COMMIT | 2026-08-22T12:57:33Z | sn92 commit touches scoring: Make the validator guide match the code and explain the logs |
| `sn92:release:v0.1.13` | 92 | RELEASE | 2026-08-22T13:41:10Z | sn92 released v0.1.13 |
| `sn92:release:v0.1.14` | 92 | RELEASE | 2026-08-22T14:35:06Z | sn92 released v0.1.14 |
| `sn81:scoring_commit:2026-08-21T19:12:16Z` | 81 | SCORING_COMMIT | 2026-08-22T16:00:11Z | sn81 commit touches scoring: feat: validator checkpoint intake — staged R2 download + serial-beat … |
| `sn92:scoring_commit:2026-08-22T16:30:46Z` | 92 | SCORING_COMMIT | 2026-08-22T16:37:16Z | sn92 commit touches scoring: Build the validator registry from the permitted set on chain |
| `sn25:release:v2026.8.22-1026185650` | 25 | RELEASE | 2026-08-22T17:32:39Z | sn25 released v2026.8.22-1026185650 |
| `sn81:scoring_commit:2026-08-22T17:44:49Z` | 81 | SCORING_COMMIT | 2026-08-22T18:00:49Z | sn81 commit touches scoring: fix: train-worker compose must override the validator entrypoint |
| `sn112:scoring_commit:2026-08-22T21:28:29Z` | 112 | SCORING_COMMIT | 2026-08-22T22:00:58Z | sn112 commit touches scoring: fix(api): app creation accepted code it could not validate (#1618) |
| `sn25:release:v2026.8.22-1026545240` | 25 | RELEASE | 2026-08-23T03:13:05Z | sn25 released v2026.8.22-1026545240 |
| `sn14:scoring_commit:2026-08-22T12:14:25Z` | 14 | SCORING_COMMIT | 2026-08-23T04:09:05Z | sn14 commit touches scoring: fix: replace MSA prefill score-sheet ABI |
| `sn25:release:v2026.8.22-1026600400` | 25 | RELEASE | 2026-08-23T05:02:13Z | sn25 released v2026.8.22-1026600400 |
| `sn14:release:MSA block-score mainnet control` | 14 | RELEASE | 2026-08-23T07:10:49Z | sn14 released MSA block-score mainnet control |
| `sn14:release:msa-block-score-control-20260823: fix: o` | 14 | RELEASE | 2026-08-23T12:00:59Z | sn14 released msa-block-score-control-20260823: fix: open paged MSA decode score slot |
| `sn90:release:v1.1.6 — subtensor v445 / typed metagrap` | 90 | RELEASE | 2026-08-23T12:59:07Z | sn90 released v1.1.6 — subtensor v445 / typed metagraph APIs |
| `sn90:scoring_commit:2026-08-23T12:38:07Z` | 90 | SCORING_COMMIT | 2026-08-23T12:59:07Z | sn90 commit touches scoring: chore(validator): release v1.1.6 |
| `sn124:scoring_commit:2026-08-23T12:20:55Z` | 124 | SCORING_COMMIT | 2026-08-23T12:59:07Z | sn124 commit touches scoring: Remove obsolete repo verify flag from docs |
| `sn90:scoring_commit:2026-08-23T13:08:10Z` | 90 | SCORING_COMMIT | 2026-08-23T13:42:25Z | sn90 commit touches scoring: docs(sn28): announce recycler and how to verify AlphaRecycled |
| `sn76:scoring_commit:2026-08-23T16:24:51Z` | 76 | SCORING_COMMIT | 2026-08-23T16:38:55Z | sn76 commit touches scoring: sandbox: authenticate with the sandbox token, not a validator signatur |
| `sn111:scoring_commit:2026-08-23T16:36:27Z` | 111 | SCORING_COMMIT | 2026-08-23T18:45:21Z | sn111 commit touches scoring: feat(setup): add public miner and validator installers |
| `sn102:release:v0.5.1 — release the finished round on s` | 102 | RELEASE | 2026-08-23T19:44:59Z | sn102 released v0.5.1 — release the finished round on swap |
| `sn102:scoring_commit:2026-08-23T18:41:50Z` | 102 | SCORING_COMMIT | 2026-08-23T19:44:59Z | sn102 commit touches scoring: 🩹 fix(validator): release the finished round on swap |
| `sn71:scoring_commit:2026-08-23T17:55:32Z` | 71 | SCORING_COMMIT | 2026-08-23T23:01:52Z | sn71 commit touches scoring: test: verify pinned model runtime in CI |
| `sn53:scoring_commit:2026-08-24T00:47:31Z` | 53 | SCORING_COMMIT | 2026-08-24T01:55:18Z | sn53 commit touches scoring: tee_miner: report live KV-cache pressure in the heartbeat |
| `sn53:scoring_commit:2026-08-24T02:43:24Z` | 53 | SCORING_COMMIT | 2026-08-24T03:13:47Z | sn53 commit touches scoring: tee_miner: withdraw on a health stall that PERSISTS, not on one misse… |
| `sn25:release:v2026.8.23-1027441210` | 25 | RELEASE | 2026-08-24T04:14:02Z | sn25 released v2026.8.23-1027441210 |
| `sn51:scoring_commit:2026-08-24T04:10:40Z` | 51 | SCORING_COMMIT | 2026-08-24T04:14:02Z | sn51 commit touches scoring: DAH-2742: stop transient checks from clearing verified job info (#1244 |
| `sn67:scoring_commit:2026-08-24T05:16:58Z` | 67 | SCORING_COMMIT | 2026-08-24T06:03:24Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20260824.post0 |
| `sn97:scoring_commit:2026-08-22T11:21:02Z` | 97 | SCORING_COMMIT | 2026-08-24T07:17:08Z | sn97 commit touches scoring: feat: weighted score breakdown on eval detail page |
| `sn21:scoring_commit:2026-08-23T13:18:04Z` | 21 | SCORING_COMMIT | 2026-08-24T09:13:31Z | sn21 commit touches scoring: docs(quickstart): troubleshooting row for no_scoreable_predictions ad… |
| `sn53:scoring_commit:2026-08-24T08:20:51Z` | 53 | SCORING_COMMIT | 2026-08-24T09:13:31Z | sn53 commit touches scoring: Merge pull request #43 from hanlinai/fix/tee-miner-load-broadcast-dra… |
| `sn65:scoring_commit:2026-08-24T09:11:32Z` | 65 | SCORING_COMMIT | 2026-08-24T09:13:31Z | sn65 commit touches scoring: update leader default url to mainnet validator |
| `sn3:scoring_commit:2026-08-24T07:53:43Z` | 3 | SCORING_COMMIT | 2026-08-24T11:01:40Z | sn3 commit touches scoring: Update evaluation dataset size to 2000 for finewebedu |
| `sn53:scoring_commit:2026-08-24T10:56:25Z` | 53 | SCORING_COMMIT | 2026-08-24T11:01:40Z | sn53 commit touches scoring: tee_miner: log the WebSocket close code, and what the dying leg took … |
| `sn67:scoring_commit:2026-08-24T09:35:52Z` | 67 | SCORING_COMMIT | 2026-08-24T11:01:40Z | sn67 commit touches scoring: fix(miner): accept monitoring task metadata in local eval (#1374) |
| `sn67:scoring_commit:2026-08-24T11:27:42Z` | 67 | SCORING_COMMIT | 2026-08-24T12:16:34Z | sn67 commit touches scoring: chore(validator): bump repo-owned validator version to 20260824.post4 |
| `sn3:scoring_commit:2026-08-24T13:22:09Z` | 3 | SCORING_COMMIT | 2026-08-24T13:30:22Z | sn3 commit touches scoring: Enforce miner upload size limit |
| `sn89:scoring_commit:2026-08-24T13:22:26Z` | 89 | SCORING_COMMIT | 2026-08-24T13:30:22Z | sn89 commit touches scoring: HF scoreboard: pick the tick dir by newest window, not by list order |
| `sn11:release:v0.6.33` | 11 | RELEASE | 2026-08-24T14:27:54Z | sn11 released v0.6.33 |
| `sn3:scoring_commit:2026-08-24T15:00:07Z` | 3 | SCORING_COMMIT | 2026-08-24T15:24:47Z | sn3 commit touches scoring: Show provisional LCB during evaluations |
| `sn7:release:release-20260824-151246: Bump allways to` | 7 | RELEASE | 2026-08-24T15:24:47Z | sn7 released release-20260824-151246: Bump allways to 3.3.0 (#705) |
| `sn10:scoring_commit:2026-08-24T13:55:36Z` | 10 | SCORING_COMMIT | 2026-08-24T15:24:47Z | sn10 commit touches scoring: fix(miner): match fee-path test to the single-prompt CLI copy |
| `sn25:release:v2026.8.24-1027859650` | 25 | RELEASE | 2026-08-24T16:05:12Z | sn25 released v2026.8.24-1027859650 |
| `sn11:release:v0.6.34` | 11 | RELEASE | 2026-08-24T16:53:39Z | sn11 released v0.6.34 |
| `sn21:scoring_commit:2026-08-24T16:06:33Z` | 21 | SCORING_COMMIT | 2026-08-24T16:53:39Z | sn21 commit touches scoring: docs(rewards): leaderboard vs chain timing, stated once |
| `sn124:scoring_commit:2026-08-24T16:42:42Z` | 124 | SCORING_COMMIT | 2026-08-24T17:42:25Z | sn124 commit touches scoring: Rename the office challenge family to cf_interceptor_office |
| `sn21:scoring_commit:2026-08-24T17:50:10Z` | 21 | SCORING_COMMIT | 2026-08-24T18:16:08Z | sn21 commit touches scoring: docs(scoring): retire the no-zero-for-missing rule the absence penalt… |
| `sn60:scoring_commit:2026-08-24T17:54:28Z` | 60 | SCORING_COMMIT | 2026-08-24T18:16:08Z | sn60 commit touches scoring: Merge pull request #44 from Bitsec-AI/feat/scorer-retries |
| `sn89:scoring_commit:2026-08-24T18:55:25Z` | 89 | SCORING_COMMIT | 2026-08-24T19:10:03Z | sn89 commit touches scoring: HF board: read the live tail, so a miner sees their own call in second |
| `sn3:scoring_commit:2026-08-24T19:11:02Z` | 3 | SCORING_COMMIT | 2026-08-24T19:54:44Z | sn3 commit touches scoring: Enforce ordered evaluations |
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
| `sn92:readme_task_diff:927a737990a07446` | 92 | README_TASK_DIFF | 2026-08-20T05:42:25Z | sn92 README task/scoring sections changed |
| `sn67:readme_task_diff:f4fc3f2cce58d57d` | 67 | README_TASK_DIFF | 2026-08-20T09:47:27Z | sn67 README task/scoring sections changed |
| `sn25:readme_task_diff:c457ae49d232190d` | 25 | README_TASK_DIFF | 2026-08-20T17:41:16Z | sn25 README task/scoring sections changed |
| `sn21:readme_task_diff:24af354b63ad7d31` | 21 | README_TASK_DIFF | 2026-08-21T16:15:59Z | sn21 README task/scoring sections changed |
| `sn90:readme_task_diff:1adff40174e46f0e` | 90 | README_TASK_DIFF | 2026-08-21T19:06:46Z | sn90 README task/scoring sections changed |
| `sn111:readme_task_diff:f9f4504d0df2befc` | 111 | README_TASK_DIFF | 2026-08-23T18:45:21Z | sn111 README task/scoring sections changed |
| `sn124:readme_task_diff:b21cedcc4483b717` | 124 | README_TASK_DIFF | 2026-08-24T17:42:25Z | sn124 README task/scoring sections changed |
| `sn10:readme_task_diff:695b2540d142908e` | 10 | README_TASK_DIFF | 2026-08-24T19:10:03Z | sn10 README task/scoring sections changed |
| `sn66:readme_task_diff:d897794f349f6fcf` | 66 | README_TASK_DIFF | 2026-08-24T22:40:07Z | sn66 README task/scoring sections changed |
| `sn111:readme_task_diff:00bbd31d47cb0fe2` | 111 | README_TASK_DIFF | 2026-08-25T11:14:15Z | sn111 README task/scoring sections changed |
| `sn76:readme_task_diff:e2a786d7f22f73bb` | 76 | README_TASK_DIFF | 2026-08-26T22:23:22Z | sn76 README task/scoring sections changed |

## RESOLVED IN THIS WINDOW

_none_
