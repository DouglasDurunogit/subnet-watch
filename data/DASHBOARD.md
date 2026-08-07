# Subnet watch — dashboard

_snapshot 2026-08-07T09:30:55Z · block 8791533 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 56 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 92 | `miner_burn` < 0.99 |
| Ranked | 92 | passed every gate |
| **Positive margin** | **56** | income beats machine cost |
| New events this window | 4 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 56 | `████████████████████████████` |
| 0–0.2 | 6 | `███` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 10 | `█████` |
| 0.6–0.8 | 7 | `████` |
| 0.8–0.99 | 8 | `████` |
| ≥0.99 dead | 36 | `██████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn11 TrajectoryRL | 79.9 | 5,453 | 5,453 = | cpu-small | 1 | 100% |
| 2 | sn107 Minos | 78.1 | 112 | 31,013 | cpu-small | 20 | 89% |
| 3 | sn76 Phylax | 76.8 | 69.80 | 253 | cpu-small | 10 | 29% |
| 4 | sn67 Harnyx | 72 | 21.15 | 766 | cpu-small | 130 | 20% |
| 5 | sn102 ConnitoAI | 69.9 | 713 | 2,374 | rtx4090* | 6 | 43% |
| 6 | sn62 Ridges | 69 | 552 | 1,997 | rtx4090* | 7 | 35% |
| 7 | sn91 cascade | 68.8 | 525 | 1,489 | rtx4090* | 5 | 52% |
| 8 | sn15 ORO | 68.4 | 11.43 | 18.68 | cpu-small | 72 | 93% |
| 9 | sn96 Verathos | 68.2 | 21.35 | 780 | rtx4090 | 43 | 43% |
| 10 | sn26 Perturb | 68.2 | 21.07 | 38.85 | rtx3060 | 11 | 51% |
| 11 | sn41 Almanac | 67.6 | 7.44 | 44.65 | cpu-small | 62 | 80% |
| 12 | sn124 Swarm | 65.7 | 211 | 606 | rtx4090* | 23 | 10% |
| 13 | sn21 AdTAO | 65.6 | 4.79 | 22.11 | cpu-small | 142 | 45% |
| 14 | sn74 Gittensor | 65.4 | 192 | 399 | rtx4090* | 9 | 19% |
| 15 | sn61 RedTeam | 62.8 | 85.87 | 196 | rtx4090* | 38 | 6% |
| 16 | sn28 gm | 60.4 | 43.47 | 2,718 | rtx4090* | 18 | 30% |
| 17 | sn85 Vidaio | 58.1 | 733 | 733 | rtx4090* | 10 | 21% |
| 18 | sn51 lium.io | 57.4 | 23.63 | 2,737 | rtx4090* | 42 | 68% |
| 19 | sn2 DSperse | 56.8 | 13.51 | 144 | rtx4090* | 8 | 83% |
| 20 | sn56 Gradients | 56.4 | 451 | 950 | rtx4090* | 7 | 70% |

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
| wide (<30%) | 23 |
| concentrated (30–60%) | 23 |
| dominated (60–90%) | 18 |
| captured (>90%) | 27 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 104 |
| code-submission (validator runs it) | 9 |
| min_compute.yml (curated) | 9 |
| README keywords (GUESS) | 5 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-08-07T09:31 | sn90 | RELEASE | sn90 released v1.0.1 |
| 2026-08-07T09:31 | sn90 | SCORING_COMMIT | sn90 commit touches scoring: fix(subnet): proxy rejects miners — only  |
| 2026-08-07T09:31 | sn114 | SCORING_COMMIT | sn114 commit touches scoring: Merge pull request #218 from DendriteHQ/ |
| 2026-08-07T08:20 | sn100 | BURN_DROP | sn100 burn fell 1.000 -> 0.269 - miners can earn again |
| 2026-08-07T06:49 | sn98 | SCORING_COMMIT | sn98 commit touches scoring: chore: set TASKS_PER_ROUND as 5 |
| 2026-08-07T06:49 | sn100 | RELEASE | sn100 released v3.3.4 — design screenshots-only viewer + metagraph cac |
| 2026-08-07T03:41 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-08-07T03:41 | sn100 | RELEASE | sn100 released v3.3.3 |
| 2026-08-07T00:33 | sn10 | SCORING_COMMIT | sn10 commit touches scoring: feat: default miner --api-base to https:/ |
| 2026-08-07T00:33 | sn14 | SCORING_COMMIT | sn14 commit touches scoring: Publish the tracked B300 pod evaluation a |
| 2026-08-07T00:33 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: feat(scoring): wire one-payer into the da |
| 2026-08-07T00:33 | sn41 | SCORING_COMMIT | sn41 commit touches scoring: Adding minimum and recommended specs for  |
| 2026-08-07T00:33 | sn66 | SCORING_COMMIT | sn66 commit touches scoring: update task pool and add review |
| 2026-08-07T00:33 | sn66 | README_TASK_DIFF | sn66 README task/scoring sections changed |
| 2026-08-07T00:33 | sn72 | BURN_DROP | sn72 burn fell 1.000 -> 0.000 - miners can earn again |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

