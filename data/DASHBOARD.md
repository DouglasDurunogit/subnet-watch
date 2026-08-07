# Subnet watch — dashboard

_snapshot 2026-08-07T06:48:57Z · block 8790723 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 54 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 91 | `miner_burn` < 0.99 |
| Ranked | 91 | passed every gate |
| **Positive margin** | **54** | income beats machine cost |
| New events this window | 2 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 56 | `████████████████████████████` |
| 0–0.2 | 6 | `███` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 9 | `████` |
| 0.6–0.8 | 7 | `████` |
| 0.8–0.99 | 8 | `████` |
| ≥0.99 dead | 37 | `██████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn107 Minos | 77.8 | 104 | 30,495 | cpu-small | 20 | 89% |
| 2 | sn76 Phylax | 76.8 | 69.39 | 251 | cpu-small | 10 | 29% |
| 3 | sn98 NeverPlayAlone | 75.9 | 1,686 | 1,686 = | cpu-small | 1 | 100% |
| 4 | sn102 ConnitoAI | 71.9 | 1,301 | 1,301 | rtx4090* | 4 | 25% |
| 5 | sn67 Harnyx | 71.9 | 20.89 | 756 | cpu-small | 125 | 20% |
| 6 | sn91 cascade | 70 | 738 | 2,977 | rtx4090* | 5 | 52% |
| 7 | sn96 Verathos | 69.5 | 29.21 | 380 | rtx4090 | 41 | 45% |
| 8 | sn62 Ridges | 69 | 548 | 1,984 | rtx4090* | 7 | 35% |
| 9 | sn15 ORO | 68.4 | 11.30 | 18.57 | cpu-small | 72 | 93% |
| 10 | sn26 Perturb | 68.1 | 20.68 | 38.49 | rtx3060 | 11 | 51% |
| 11 | sn41 Almanac | 67.5 | 7.34 | 44.39 | cpu-small | 63 | 80% |
| 12 | sn21 AdTAO | 65.7 | 4.84 | 22.34 | cpu-small | 142 | 45% |
| 13 | sn124 Swarm | 65.6 | 210 | 603 | rtx4090* | 23 | 10% |
| 14 | sn28 gm | 65.2 | 180 | 1,623 | rtx4090* | 19 | 20% |
| 15 | sn74 Gittensor | 65.2 | 178 | 487 | rtx4090* | 9 | 23% |
| 16 | sn80 OpenRoboto | 63.4 | 103 | 382 | rtx4090* | 4 | 91% |
| 17 | sn61 RedTeam | 62.5 | 78.50 | 180 | rtx4090* | 38 | 6% |
| 18 | sn85 Vidaio | 57.7 | 654 | 659 | rtx4090* | 10 | 19% |
| 19 | sn51 lium.io | 57.6 | 24.58 | 2,793 | rtx4090* | 42 | 65% |
| 20 | sn2 DSperse | 56.8 | 13.44 | 142 | rtx4090* | 8 | 83% |

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
| wide (<30%) | 25 |
| concentrated (30–60%) | 21 |
| dominated (60–90%) | 17 |
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
| 2026-08-07T00:33 | sn74 | RELEASE | sn74 released release-20260806-204130 |
| 2026-08-07T00:33 | sn96 | RELEASE | sn96 released v0.1.28 - Gleipnir Proof Runtime Hardening |
| 2026-08-07T00:33 | sn96 | SCORING_COMMIT | sn96 commit touches scoring: fix: refresh authenticated miner artifact |
| 2026-08-07T00:33 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: Update validator artifact hydration and  |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

