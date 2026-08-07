# Subnet watch — dashboard

_snapshot 2026-08-07T05:25:24Z · block 8790306 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 52 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 91 | `miner_burn` < 0.99 |
| Ranked | 91 | passed every gate |
| **Positive margin** | **52** | income beats machine cost |
| New events this window | 0 | see ALARMS.md |

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
| 1 | sn107 Minos | 78 | 110 | 30,268 | cpu-small | 20 | 89% |
| 2 | sn76 Phylax | 76.8 | 68.93 | 250 | cpu-small | 10 | 29% |
| 3 | sn67 Harnyx | 71.8 | 20.23 | 733 | cpu-small | 122 | 20% |
| 4 | sn91 cascade | 70 | 733 | 2,956 | rtx4090* | 5 | 52% |
| 5 | sn62 Ridges | 69 | 543 | 1,965 | rtx4090* | 7 | 35% |
| 6 | sn96 Verathos | 68.9 | 25.17 | 353 | rtx4090 | 62 | 42% |
| 7 | sn26 Perturb | 67.9 | 19.93 | 37.77 | rtx3060 | 11 | 50% |
| 8 | sn41 Almanac | 67.5 | 7.24 | 44.06 | cpu-small | 63 | 80% |
| 9 | sn124 Swarm | 65.7 | 212 | 608 | rtx4090* | 23 | 11% |
| 10 | sn21 AdTAO | 65.6 | 4.80 | 22.16 | cpu-small | 142 | 45% |
| 11 | sn74 Gittensor | 65.3 | 184 | 474 | rtx4090* | 9 | 22% |
| 12 | sn15 ORO | 64.3 | 5.13 | 17.61 | cpu-small | 83 | 95% |
| 13 | sn98 NeverPlayAlone | 64 | 1,674 | 1,674 = | cpu-small | 1 | 100% |
| 14 | sn80 OpenRoboto | 63.4 | 103 | 382 | rtx4090* | 4 | 91% |
| 15 | sn61 RedTeam | 62.4 | 76.30 | 175 | rtx4090* | 38 | 6% |
| 16 | sn28 gm | 60.4 | 43.26 | 2,271 | rtx4090* | 19 | 26% |
| 17 | sn2 DSperse | 59.1 | 28.16 | 196 | rtx4090* | 9 | 83% |
| 18 | sn51 lium.io | 58.2 | 28.53 | 2,245 | rtx4090* | 44 | 64% |
| 19 | sn85 Vidaio | 57.7 | 655 | 660 | rtx4090* | 10 | 19% |
| 20 | sn56 Gradients | 56.4 | 445 | 937 | rtx4090* | 7 | 70% |

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
| concentrated (30–60%) | 22 |
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
| 2026-08-07T00:33 | sn111 | README_TASK_DIFF | sn111 README task/scoring sections changed |
| 2026-08-06T14:55 | sn26 | SCORING_COMMIT | sn26 commit touches scoring: Merge pull request #45 from 0xsigurd/feat |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

