# Subnet watch — dashboard

_snapshot 2026-07-30T09:58:21Z · block 8734094 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 53 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 94 | `miner_burn` < 0.99 |
| Ranked | 94 | passed every gate |
| **Positive margin** | **53** | income beats machine cost |
| New events this window | 5 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 58 | `████████████████████████████` |
| 0–0.2 | 5 | `██` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 8 | `████` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 9 | `████` |
| ≥0.99 dead | 34 | `████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn23 Trishool | 85.4 | 616 | 616 = | cpu-small | 5 | 20% |
| 2 | sn76 Phylax | 81.3 | 217 | 363 | cpu-small | 4 | 60% |
| 3 | sn107 Minos | 77.5 | 97.47 | 30,267 | cpu-small | 20 | 90% |
| 4 | sn67 Harnyx | 71.4 | 17.61 | 1,091 | cpu-small | 94 | 23% |
| 5 | sn101 Tag101 | 69.2 | 12.06 | 15.83 | cpu-small | 247 | 1% |
| 6 | sn56 Gradients | 69.1 | 573 | 1,316 | rtx4090* | 6 | 63% |
| 7 | sn15 ORO | 68.7 | 11.08 | 20.48 | cpu-small | 81 | 92% |
| 8 | sn102 ConnitoAI | 67.6 | 359 | 1,296 | rtx4090* | 7 | 35% |
| 9 | sn124 Swarm | 67.5 | 355 | 723 | rtx4090* | 16 | 13% |
| 10 | sn85 Vidaio | 67.2 | 324 | 507 | rtx4090* | 10 | 17% |
| 11 | sn28 gm | 64.2 | 131 | 2,296 | rtx4090* | 8 | 60% |
| 12 | sn53 engy | 63.1 | 93.68 | 2,150 | rtx4090 | 34 | 13% |
| 13 | sn71 Leadpoet | 62.1 | 68.84 | 120 | rtx4090* | 4 | 91% |
| 14 | sn38 ChronoLLM | 61.3 | 65.78 | 641 | rtx4090* | 10 | 52% |
| 15 | sn61 RedTeam | 58.3 | 21.73 | 134 | rtx4090* | 85 | 5% |
| 16 | sn26 Perturb | 55.2 | 1.42 | 5.62 | rtx3060 | 52 | 50% |
| 17 | sn9 iota | 54.1 | 5,324 | 9,670 | rtx4090* | 3 | 50% |
| 18 | sn51 lium.io | 52.1 | 8.47 | 2,691 | rtx4090* | 38 | 70% |
| 19 | sn100 BASE | 51.5 | 1,759 | 1,759 = | rtx4090* | 2 | 50% |
| 20 | sn11 TrajectoryRL | 50 | 5,182 | 5,182 = | cpu-small | 1 | 100% |

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
| concentrated (30–60%) | 23 |
| dominated (60–90%) | 18 |
| captured (>90%) | 25 |

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
| 2026-07-30T09:58 | sn28 | RELEASE | sn28 released v0.3.14 |
| 2026-07-30T09:58 | sn38 | SCORING_COMMIT | sn38 commit touches scoring: Add custom architecture registry for mine |
| 2026-07-30T09:58 | sn43 | BURN_DROP | sn43 burn fell 1.000 -> 0.800 - miners can earn again |
| 2026-07-30T09:58 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-2340, publish structured zero-incenti |
| 2026-07-30T09:58 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Keep validator epoch authority fresh duri |
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

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

