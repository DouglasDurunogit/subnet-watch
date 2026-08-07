# Subnet watch — dashboard

_snapshot 2026-08-07T00:33:22Z · block 8788846 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 55 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 92 | `miner_burn` < 0.99 |
| Ranked | 92 | passed every gate |
| **Positive margin** | **55** | income beats machine cost |
| New events this window | 12 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 57 | `████████████████████████████` |
| 0–0.2 | 5 | `██` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 9 | `████` |
| 0.6–0.8 | 6 | `███` |
| 0.8–0.99 | 10 | `█████` |
| ≥0.99 dead | 36 | `██████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn107 Minos | 78.2 | 115 | 31,241 | cpu-small | 20 | 89% |
| 2 | sn76 Phylax | 77.5 | 83.20 | 418 | cpu-small | 10 | 29% |
| 3 | sn60 Bitsec.ai | 74.8 | 1,207 | 1,207 = | cpu-small | 2 | 50% |
| 4 | sn67 Harnyx | 71.7 | 19.84 | 933 | cpu-small | 126 | 25% |
| 5 | sn91 cascade | 70 | 743 | 2,999 | rtx4090* | 5 | 52% |
| 6 | sn62 Ridges | 69 | 546 | 1,975 | rtx4090* | 7 | 35% |
| 7 | sn96 Verathos | 68.1 | 20.79 | 283 | rtx4090 | 55 | 45% |
| 8 | sn26 Perturb | 68 | 20.05 | 37.98 | rtx3060 | 11 | 50% |
| 9 | sn41 Almanac | 67.5 | 7.28 | 43.33 | cpu-small | 53 | 82% |
| 10 | sn15 ORO | 67.3 | 8.82 | 17.12 | cpu-small | 83 | 93% |
| 11 | sn124 Swarm | 65.6 | 209 | 600 | rtx4090* | 23 | 10% |
| 12 | sn21 AdTAO | 65.6 | 4.75 | 21.97 | cpu-small | 142 | 45% |
| 13 | sn74 Gittensor | 65.2 | 180 | 433 | rtx4090* | 9 | 20% |
| 14 | sn28 gm | 65 | 169 | 1,682 | rtx4090* | 19 | 25% |
| 15 | sn98 NeverPlayAlone | 64.1 | 1,693 | 1,693 = | cpu-small | 1 | 100% |
| 16 | sn80 OpenRoboto | 63.4 | 104 | 384 | rtx4090* | 4 | 91% |
| 17 | sn61 RedTeam | 62.4 | 75.72 | 174 | rtx4090* | 38 | 6% |
| 18 | sn101 Tag101 | 59.7 | 0.08 | 0.74 | cpu-small | 245 | 90% |
| 19 | sn51 lium.io | 57.8 | 25.87 | 2,001 | rtx4090* | 44 | 68% |
| 20 | sn85 Vidaio | 57.2 | 569 | 622 | rtx4090* | 10 | 18% |

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
| concentrated (30–60%) | 21 |
| dominated (60–90%) | 19 |
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
| 2026-08-06T14:55 | sn126 | SCORING_COMMIT | sn126 commit touches scoring: Reduce validator burn default to 30 perc |
| 2026-08-06T14:55 | sn126 | README_TASK_DIFF | sn126 README task/scoring sections changed |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

