# Subnet watch — dashboard

_snapshot 2026-08-25T14:12:34Z · block 8922532 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 55 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 90 | `miner_burn` < 0.99 |
| Ranked | 90 | passed every gate |
| **Positive margin** | **55** | income beats machine cost |
| New events this window | 3 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 60 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 3 | `█` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 38 | `██████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn76 Phylax | 79.5 | 142 | 211 | cpu-small | 13 | 20% |
| 2 | sn60 Bitsec.ai | 76.1 | 1,766 | 1,766 = | cpu-small | 2 | 50% |
| 3 | sn3 Teutonic | 75.7 | 4,054 | 4,054 = | rtx4090* | 5 | 20% |
| 4 | sn102 ConnitoAI | 72.8 | 1,705 | 1,706 | rtx4090* | 4 | 25% |
| 5 | sn62 Ridges | 72.3 | 1,454 | 2,973 | rtx4090* | 6 | 39% |
| 6 | sn23 Trishool | 72.1 | 534 | 534 = | cpu-small | 2 | 80% |
| 7 | sn67 Harnyx | 71.6 | 19.12 | 457 | cpu-small | 141 | 12% |
| 8 | sn38 ChronoLLM | 70.9 | 385 | 1,489 | cpu-small | 6 | 53% |
| 9 | sn15 ORO | 70.8 | 22.85 | 21,122 | cpu-small | 90 | 91% |
| 10 | sn91 cascade | 68.9 | 534 | 1,436 | rtx4090* | 5 | 52% |
| 11 | sn21 AdTAO | 68.8 | 10.24 | 1,197 | cpu-small | 16 | 45% |
| 12 | sn26 Perturb | 67.7 | 18.96 | 270 | rtx3060 | 10 | 70% |
| 13 | sn96 Verathos | 67.5 | 18.39 | 193 | rtx4090 | 97 | 40% |
| 14 | sn124 Swarm | 66.8 | 291 | 918 | rtx4090* | 25 | 11% |
| 15 | sn1 Apex | 66.3 | 246 | 2,009 | rtx4090* | 4 | 54% |
| 16 | sn92 MicroTensor | 65.4 | 74.73 | 121 | cpu-small | 3 | 95% |
| 17 | sn107 Minos | 64.9 | 141 | 40,952 | cpu-small | 20 | 90% |
| 18 | sn81 Reliquary | 63.8 | 114 | 334 | rtx4090* | 35 | 7% |
| 19 | sn108 Prometheon | 63.6 | 109 | 122 | rtx4090* | 9 | 66% |
| 20 | sn121 sundae_bar | 62.5 | 1,078 | 1,078 = | cpu-small | 2 | 66% |

`=` after the ceiling means it equals the median exactly - either one competitive
miner exists, or they all earn the same. Both columns use identical precision;
if they ever disagree the data is wrong, since a median cannot exceed its own max.

`net $/day (median)` is what a newcomer should expect: the MEDIAN non-owner,
non-permitted miner, minus machine cost. `ceiling $/day` is the BEST competitive
miner - reachable only by beating everyone already there. Where the two diverge
wildly, the subnet is winner-take-all and the ceiling is not a plan.

`*` = machine is an assumed default; no hardware evidence was found for that subnet.

![top 20 by score](charts/top20.svg)

## Concentration — reported, never scored

A low top-1 share means many miners share the emission. A high one means a
single UID takes almost everything, so the headline income is not reachable.
**This is deliberately excluded from the score** — judge the shape yourself.

| top-1 share | subnets (of those that pay) |
|---|---:|
| wide (<30%) | 26 |
| concentrated (30–60%) | 18 |
| dominated (60–90%) | 19 |
| captured (>90%) | 25 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 101 |
| code-submission (validator runs it) | 10 |
| min_compute.yml (curated) | 10 |
| README keywords (GUESS) | 6 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-08-25T14:13 | sn102 | RELEASE | sn102 released v0.5.2 — background-eval resume + validator memory fixe |
| 2026-08-25T14:13 | sn121 | BURN_DROP | sn121 burn fell 1.000 -> 0.657 - miners can earn again |
| 2026-08-25T13:08 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: Note the operator-driven submission windo |
| 2026-08-25T11:14 | sn10 | SCORING_COMMIT | sn10 commit touches scoring: feat(chain): validator-side set_weights w |
| 2026-08-25T11:14 | sn111 | README_TASK_DIFF | sn111 README task/scoring sections changed |
| 2026-08-25T10:00 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: feat(setup): streamline public validator |
| 2026-08-25T10:00 | sn112 | SCORING_COMMIT | sn112 commit touches scoring: fix(dedup): a waitlisted miner could nev |
| 2026-08-25T05:04 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Verify parity bundle through exact empty  |
| 2026-08-25T03:09 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Merge pull request #109 from leadpoet/cod |
| 2026-08-25T01:49 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: revert: guarded title-corroboration was u |
| 2026-08-24T23:04 | sn66 | SCORING_COMMIT | sn66 commit touches scoring: Normalize verifier image source permissio |
| 2026-08-24T22:40 | sn66 | README_TASK_DIFF | sn66 README task/scoring sections changed |
| 2026-08-24T22:40 | sn102 | SCORING_COMMIT | sn102 commit touches scoring: ♻️ refactor(validator): drop the redunda |
| 2026-08-24T21:53 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Allow bounded measured dev evaluation pay |
| 2026-08-24T21:15 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: Correct the validator setup path end to e |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

