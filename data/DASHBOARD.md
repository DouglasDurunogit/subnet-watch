# Subnet watch — dashboard

_snapshot 2026-09-16T22:24:24Z · block 9083175 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 56 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 93 | `miner_burn` < 0.99 |
| Ranked | 93 | passed every gate |
| **Positive margin** | **56** | income beats machine cost |
| New events this window | 6 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 63 | `████████████████████████████` |
| 0–0.2 | 10 | `████` |
| 0.2–0.4 | 7 | `███` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 5 | `██` |
| 0.8–0.99 | 4 | `██` |
| ≥0.99 dead | 35 | `████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn11 TrajectoryRL | 80 | 5,622 | 5,622 = | cpu-small | 1 | 100% |
| 2 | sn92 MicroTensor | 79 | 123 | 276 | cpu-small | 8 | 43% |
| 3 | sn91 cascade | 72.4 | 594 | 2,378 | cpu-small | 5 | 52% |
| 4 | sn1 Apex | 69 | 552 | 905 | rtx4090* | 4 | 58% |
| 5 | sn67 Harnyx | 68.8 | 8.44 | 930 | cpu-small | 117 | 33% |
| 6 | sn107 Minos | 68.7 | 329 | 26,641 | cpu-small | 20 | 79% |
| 7 | sn38 ChronoLLM | 66.4 | 111 | 1,511 | cpu-small | 10 | 52% |
| 8 | sn28 SayGM | 65 | 167 | 1,776 | rtx4090* | 37 | 13% |
| 9 | sn111 Claims | 64.8 | 171 | 2,492 | rtx4090* | 5 | 79% |
| 10 | sn61 RedTeam | 62.5 | 79.95 | 122 | rtx4090* | 112 | 1% |
| 11 | sn81 Reliquary | 61.7 | 62.47 | 103 | rtx4090* | 42 | 33% |
| 12 | sn55 NIOME | 61.7 | 62.46 | 522 | rtx4090* | 11 | 29% |
| 13 | sn62 Ridges | 60.7 | 46.38 | 1,641 | rtx4090* | 19 | 26% |
| 14 | sn23 Trishool | 60.3 | 561 | 561 = | cpu-small | 2 | 80% |
| 15 | sn51 lium.io | 56.8 | 21.54 | 1,973 | rtx4090* | 69 | 81% |
| 16 | sn80 OpenRoboto | 56.6 | 472 | 1,672 | rtx4090* | 5 | 43% |
| 17 | sn9 iota | 56 | 11,926 | 11,926 = | rtx4090* | 3 | 68% |
| 18 | sn56 Gradients | 54.9 | 286 | 4,724 | rtx4090* | 13 | 46% |
| 19 | sn124 Swarm | 54.3 | 244 | 789 | rtx4090* | 25 | 11% |
| 20 | sn102 ConnitoAI | 53.9 | 6.94 | 1,255 | rtx4090* | 9 | 29% |

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
| wide (<30%) | 24 |
| concentrated (30–60%) | 26 |
| dominated (60–90%) | 16 |
| captured (>90%) | 23 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 96 |
| min_compute.yml (curated) | 11 |
| code-submission (validator runs it) | 10 |
| README keywords (GUESS) | 10 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-09-16T22:24 | sn28 | RELEASE | sn28 released v0.4.18 |
| 2026-09-16T22:24 | sn28 | README_TASK_DIFF | sn28 README task/scoring sections changed |
| 2026-09-16T22:24 | sn45 | SCORING_COMMIT | sn45 commit touches scoring: Allow a per-model scale on audit scores |
| 2026-09-16T22:24 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: release: pin fresh validator installs to  |
| 2026-09-16T22:24 | sn102 | RELEASE | sn102 released v0.6.1 |
| 2026-09-16T22:24 | sn102 | SCORING_COMMIT | sn102 commit touches scoring: Merge pull request #274 from Connito-AI/ |
| 2026-09-16T19:46 | sn34 | SCORING_COMMIT | sn34 commit touches scoring: Exclude no_answer rows before the reward- |
| 2026-09-16T19:46 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Fix Sep16 benchmark bank verification |
| 2026-09-16T19:46 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: fix: keep valid bridge miners eligible du |
| 2026-09-16T19:46 | sn92 | RELEASE | sn92 released v0.4.6 |
| 2026-09-16T19:46 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: mt-4g: 3 GiB disk ceiling, matching the a |
| 2026-09-16T16:47 | sn9 | RELEASE | sn9 released v4.13.0 |
| 2026-09-16T16:47 | sn20 | BURN_DROP | sn20 burn fell 1.000 -> 0.754 - miners can earn again |
| 2026-09-16T16:47 | sn51 | RELEASE | sn51 released executor-v1.129 |
| 2026-09-16T16:47 | sn66 | RELEASE | sn66 released v1.0.4 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

