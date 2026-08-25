# Subnet watch — dashboard

_snapshot 2026-08-25T09:07:34Z · block 8921007 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 54 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 89 | `miner_burn` < 0.99 |
| Ranked | 89 | passed every gate |
| **Positive margin** | **54** | income beats machine cost |
| New events this window | 0 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 60 | `████████████████████████████` |
| 0–0.2 | 6 | `███` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 39 | `██████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn76 Phylax | 79.6 | 142 | 212 | cpu-small | 13 | 20% |
| 2 | sn60 Bitsec.ai | 76.1 | 1,772 | 1,772 = | cpu-small | 2 | 50% |
| 3 | sn3 Teutonic | 75.7 | 4,075 | 4,075 = | rtx4090* | 5 | 20% |
| 4 | sn62 Ridges | 72.3 | 1,467 | 2,998 | rtx4090* | 6 | 39% |
| 5 | sn38 ChronoLLM | 72.3 | 580 | 3,406 | cpu-small | 6 | 53% |
| 6 | sn23 Trishool | 72.1 | 535 | 535 = | cpu-small | 2 | 80% |
| 7 | sn67 Harnyx | 71.6 | 19.17 | 458 | cpu-small | 137 | 12% |
| 8 | sn15 ORO | 71.1 | 23.77 | 21,777 | cpu-small | 90 | 91% |
| 9 | sn102 ConnitoAI | 70.1 | 760 | 2,055 | rtx4090* | 7 | 28% |
| 10 | sn91 cascade | 68.8 | 518 | 1,394 | rtx4090* | 5 | 52% |
| 11 | sn21 AdTAO | 68.8 | 10.23 | 1,196 | cpu-small | 16 | 45% |
| 12 | sn26 Perturb | 67.6 | 18.86 | 269 | rtx3060 | 10 | 70% |
| 13 | sn96 Verathos | 67.5 | 18.09 | 190 | rtx4090 | 99 | 40% |
| 14 | sn124 Swarm | 66.8 | 296 | 887 | rtx4090* | 25 | 11% |
| 15 | sn1 Apex | 66.4 | 254 | 2,071 | rtx4090* | 4 | 53% |
| 16 | sn92 MicroTensor | 65.5 | 75.44 | 122 | cpu-small | 3 | 95% |
| 17 | sn107 Minos | 65.3 | 153 | 40,622 | cpu-small | 19 | 90% |
| 18 | sn81 Reliquary | 63.9 | 119 | 349 | rtx4090* | 34 | 8% |
| 19 | sn108 Prometheon | 63.5 | 106 | 119 | rtx4090* | 9 | 66% |
| 20 | sn28 gm | 60.3 | 42.70 | 1,771 | rtx4090* | 57 | 24% |

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
| concentrated (30–60%) | 17 |
| dominated (60–90%) | 18 |
| captured (>90%) | 26 |

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
| 2026-08-25T05:04 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Verify parity bundle through exact empty  |
| 2026-08-25T03:09 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Merge pull request #109 from leadpoet/cod |
| 2026-08-25T01:49 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: revert: guarded title-corroboration was u |
| 2026-08-24T23:04 | sn66 | SCORING_COMMIT | sn66 commit touches scoring: Normalize verifier image source permissio |
| 2026-08-24T22:40 | sn66 | README_TASK_DIFF | sn66 README task/scoring sections changed |
| 2026-08-24T22:40 | sn102 | SCORING_COMMIT | sn102 commit touches scoring: ♻️ refactor(validator): drop the redunda |
| 2026-08-24T21:53 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Allow bounded measured dev evaluation pay |
| 2026-08-24T21:15 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: Correct the validator setup path end to e |
| 2026-08-24T19:54 | sn3 | SCORING_COMMIT | sn3 commit touches scoring: Enforce ordered evaluations |
| 2026-08-24T19:10 | sn10 | README_TASK_DIFF | sn10 README task/scoring sections changed |
| 2026-08-24T19:10 | sn89 | SCORING_COMMIT | sn89 commit touches scoring: HF board: read the live tail, so a miner  |
| 2026-08-24T18:16 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: docs(scoring): retire the no-zero-for-mis |
| 2026-08-24T18:16 | sn60 | SCORING_COMMIT | sn60 commit touches scoring: Merge pull request #44 from Bitsec-AI/fea |
| 2026-08-24T18:16 | sn92 | BURN_DROP | sn92 burn fell 1.000 -> 0.971 - miners can earn again |
| 2026-08-24T17:42 | sn124 | SCORING_COMMIT | sn124 commit touches scoring: Rename the office challenge family to cf |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

