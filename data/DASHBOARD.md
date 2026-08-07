# Subnet watch — dashboard

_snapshot 2026-08-07T10:37:39Z · block 8791867 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 55 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 91 | `miner_burn` < 0.99 |
| Ranked | 91 | passed every gate |
| **Positive margin** | **55** | income beats machine cost |
| New events this window | 6 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 56 | `████████████████████████████` |
| 0–0.2 | 5 | `██` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 12 | `██████` |
| 0.6–0.8 | 5 | `██` |
| 0.8–0.99 | 9 | `████` |
| ≥0.99 dead | 37 | `██████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn11 TrajectoryRL | 79.9 | 5,462 | 5,462 = | cpu-small | 1 | 100% |
| 2 | sn107 Minos | 77.8 | 105 | 31,004 | cpu-small | 20 | 89% |
| 3 | sn76 Phylax | 76.8 | 69.05 | 250 | cpu-small | 10 | 29% |
| 4 | sn67 Harnyx | 72 | 21.19 | 767 | cpu-small | 131 | 20% |
| 5 | sn102 ConnitoAI | 70.5 | 854 | 2,064 | rtx4090* | 6 | 37% |
| 6 | sn62 Ridges | 69 | 553 | 2,001 | rtx4090* | 7 | 35% |
| 7 | sn91 cascade | 68.8 | 527 | 1,493 | rtx4090* | 5 | 52% |
| 8 | sn15 ORO | 68.3 | 11.43 | 18.68 | cpu-small | 72 | 93% |
| 9 | sn26 Perturb | 68.2 | 21.28 | 38.91 | rtx3060 | 11 | 51% |
| 10 | sn96 Verathos | 68 | 20.30 | 871 | rtx4090 | 43 | 41% |
| 11 | sn41 Almanac | 67.6 | 7.54 | 44.72 | cpu-small | 62 | 80% |
| 12 | sn124 Swarm | 65.7 | 211 | 607 | rtx4090* | 23 | 10% |
| 13 | sn21 AdTAO | 65.5 | 4.71 | 21.80 | cpu-small | 142 | 45% |
| 14 | sn74 Gittensor | 65.3 | 187 | 403 | rtx4090* | 9 | 19% |
| 15 | sn61 RedTeam | 62.8 | 84.65 | 195 | rtx4090* | 38 | 6% |
| 16 | sn85 Vidaio | 58 | 725 | 725 = | rtx4090* | 10 | 21% |
| 17 | sn51 lium.io | 57.4 | 23.77 | 2,751 | rtx4090* | 42 | 68% |
| 18 | sn2 DSperse | 56.8 | 13.70 | 146 | rtx4090* | 8 | 83% |
| 19 | sn56 Gradients | 56.4 | 451 | 952 | rtx4090* | 7 | 70% |
| 20 | sn101 Tag101 | 56 | 0.01 | 0.76 | cpu-small | 243 | 90% |

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
| concentrated (30–60%) | 24 |
| dominated (60–90%) | 16 |
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
| 2026-08-07T10:38 | sn66 | SCORING_COMMIT | sn66 commit touches scoring: fix catalag endpoint pydantic type valida |
| 2026-08-07T10:38 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: Document miner batch and PDF options |
| 2026-08-07T10:38 | sn111 | README_TASK_DIFF | sn111 README task/scoring sections changed |
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

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

