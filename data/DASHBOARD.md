# Subnet watch — dashboard

_snapshot 2026-07-30T07:10:15Z · block 8733254 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 54 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 94 | `miner_burn` < 0.99 |
| Ranked | 94 | passed every gate |
| **Positive margin** | **54** | income beats machine cost |
| New events this window | 8 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 59 | `████████████████████████████` |
| 0–0.2 | 5 | `██` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 8 | `████` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 9 | `████` |
| ≥0.99 dead | 34 | `████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn23 Trishool | 85.4 | 616 | 616 = | cpu-small | 5 | 20% |
| 2 | sn76 Phylax | 81 | 201 | 296 | cpu-small | 4 | 65% |
| 3 | sn107 Minos | 77.4 | 96.67 | 28,723 | cpu-small | 20 | 90% |
| 4 | sn98 NeverPlayAlone | 76.1 | 1,754 | 1,754 = | cpu-small | 1 | 100% |
| 5 | sn67 Harnyx | 71.4 | 17.56 | 1,089 | cpu-small | 94 | 23% |
| 6 | sn101 Tag101 | 69.4 | 10.83 | 20.42 | cpu-small | 243 | 1% |
| 7 | sn56 Gradients | 69.1 | 571 | 1,326 | rtx4090* | 6 | 63% |
| 8 | sn102 ConnitoAI | 68.8 | 515 | 1,533 | rtx4090* | 6 | 41% |
| 9 | sn124 Swarm | 67.5 | 356 | 724 | rtx4090* | 16 | 13% |
| 10 | sn15 ORO | 67.2 | 8.72 | 18.99 | cpu-small | 79 | 94% |
| 11 | sn53 engy | 62.7 | 82.27 | 1,908 | rtx4090 | 34 | 13% |
| 12 | sn71 Leadpoet | 62 | 68.06 | 119 | rtx4090* | 4 | 91% |
| 13 | sn28 gm | 58.2 | 22.59 | 2,082 | rtx4090* | 10 | 66% |
| 14 | sn61 RedTeam | 58.2 | 21.26 | 133 | rtx4090* | 87 | 5% |
| 15 | sn26 Perturb | 55.2 | 1.41 | 5.60 | rtx3060 | 52 | 50% |
| 16 | sn51 lium.io | 54.5 | 12.74 | 2,846 | rtx4090* | 39 | 68% |
| 17 | sn9 iota | 53.9 | 5,005 | 9,630 | rtx4090* | 3 | 50% |
| 18 | sn100 BASE | 50.9 | 1,363 | 1,363 = | rtx4090* | 2 | 58% |
| 19 | sn6 Numinous | 50 | -0.93 | 309 | cpu-small | 214 | 17% |
| 20 | sn11 TrajectoryRL | 49.9 | 5,151 | 5,151 = | cpu-small | 1 | 100% |

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
| concentrated (30–60%) | 22 |
| dominated (60–90%) | 17 |
| captured (>90%) | 27 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 106 |
| min_compute.yml (curated) | 9 |
| code-submission (validator runs it) | 8 |
| README keywords (GUESS) | 4 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-07-30T07:10 | sn5 | BURN_DROP | sn5 burn fell 1.000 -> 0.846 - miners can earn again |
| 2026-07-30T07:10 | sn15 | RELEASE | sn15 released v1.2.3 |
| 2026-07-30T07:10 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Parallelize safe validator restart prepar |
| 2026-07-30T07:10 | sn76 | SCORING_COMMIT | sn76 commit touches scoring: Evaluate the smaller tracks before skills |
| 2026-07-30T07:10 | sn80 | README_TASK_DIFF | sn80 README task/scoring sections changed |
| 2026-07-30T07:10 | sn100 | BURN_DROP | sn100 burn fell 1.000 -> 0.579 - miners can earn again |
| 2026-07-30T07:10 | sn107 | SCORING_COMMIT | sn107 commit touches scoring: Fix stale reward split: winner 90% / bur |
| 2026-07-30T07:10 | sn107 | README_TASK_DIFF | sn107 README task/scoring sections changed |
| 2026-07-30T04:18 | sn26 | README_TASK_DIFF | sn26 README task/scoring sections changed |
| 2026-07-29T22:43 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: fix(agent-challenge): make Terminal-Benc |
| 2026-07-29T22:43 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: Add tests for agent v1 Silver scoring |
| 2026-07-29T19:39 | sn6 | README_TASK_DIFF | sn6 README task/scoring sections changed |
| 2026-07-29T19:39 | sn7 | RELEASE | sn7 released release-20260729-181714 |
| 2026-07-29T19:39 | sn7 | SCORING_COMMIT | sn7 commit touches scoring: Add BURN_RATE with pools scaled to the min |
| 2026-07-29T19:39 | sn66 | SCORING_COMMIT | sn66 commit touches scoring: Introduce tiered solver task pool |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

