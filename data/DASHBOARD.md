# Subnet watch — dashboard

_snapshot 2026-09-05T00:53:10Z · block 8997726 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 58 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 95 | `miner_burn` < 0.99 |
| Ranked | 96 | passed every gate |
| **Positive margin** | **58** | income beats machine cost |
| New events this window | 0 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 57 | `████████████████████████████` |
| 0–0.2 | 12 | `██████` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 3 | `█` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 9 | `████` |
| ≥0.99 dead | 33 | `████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn92 MicroTensor | 80.3 | 171 | 381 | cpu-small | 9 | 26% |
| 2 | sn107 Minos | 76.8 | 87.04 | 5,204 | cpu-small | 21 | 81% |
| 3 | sn3 Teutonic | 75.6 | 3,893 | 3,893 = | rtx4090* | 5 | 20% |
| 4 | sn76 Phylax | 72.9 | 26.94 | 71.46 | cpu-small | 21 | 20% |
| 5 | sn67 Harnyx | 72.9 | 25.91 | 132 | cpu-small | 102 | 10% |
| 6 | sn91 cascade | 70.5 | 850 | 3,425 | rtx4090* | 5 | 52% |
| 7 | sn15 ORO | 70.2 | 21.16 | 45.09 | cpu-small | 60 | 94% |
| 8 | sn96 Verathos | 69.4 | 28.89 | 293 | rtx4090 | 79 | 40% |
| 9 | sn102 ConnitoAI | 69.2 | 579 | 1,455 | rtx4090* | 7 | 27% |
| 10 | sn56 Gradients | 69 | 543 | 1,349 | rtx4090* | 5 | 75% |
| 11 | sn111 Claims | 68.4 | 472 | 2,095 | rtx4090* | 5 | 49% |
| 12 | sn11 TrajectoryRL | 68 | 5,395 | 5,395 = | cpu-small | 1 | 100% |
| 13 | sn124 Swarm | 66.5 | 267 | 826 | rtx4090* | 25 | 11% |
| 14 | sn80 OpenRoboto | 65.4 | 186 | 672 | rtx4090* | 5 | 71% |
| 15 | sn98 NeverPlayAlone | 64.4 | 1,881 | 1,881 = | cpu-small | 1 | 100% |
| 16 | sn121 sundae_bar | 63 | 1,225 | 1,225 = | cpu-small | 2 | 60% |
| 17 | sn28 SayGM | 61.3 | 55.99 | 7,508 | rtx4090* | 46 | 49% |
| 18 | sn101 Tag101 | 60.8 | 0.38 | 0.83 | cpu-small | 238 | 90% |
| 19 | sn74 Gittensor | 60.6 | 46.55 | 366 | rtx4090 | 12 | 65% |
| 20 | sn41 Almanac | 59.6 | 32.58 | 96.75 | cpu-small | 88 | 9% |

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
| wide (<30%) | 27 |
| concentrated (30–60%) | 19 |
| dominated (60–90%) | 21 |
| captured (>90%) | 25 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 98 |
| code-submission (validator runs it) | 11 |
| min_compute.yml (curated) | 11 |
| README keywords (GUESS) | 7 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-09-04T23:02 | sn7 | RELEASE | sn7 released release-20260904-214340: Bump version to 3.3.2 (#722) |
| 2026-09-04T23:02 | sn25 | RELEASE | sn25 released v2026.9.4-1037600680 |
| 2026-09-04T23:02 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: ci: classify bundle for the hidden-tests  |
| 2026-09-04T21:04 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: feat(scoring): measurement resolution app |
| 2026-09-04T21:04 | sn25 | RELEASE | sn25 released v2026.9.4-1037517570 |
| 2026-09-04T21:04 | sn34 | SCORING_COMMIT | sn34 commit touches scoring: burn discriminator incentive until KoTH s |
| 2026-09-04T21:04 | sn47 | SCORING_COMMIT | sn47 commit touches scoring: fix extraction and verifier |
| 2026-09-04T21:04 | sn47 | README_TASK_DIFF | sn47 README task/scoring sections changed |
| 2026-09-04T21:04 | sn63 | README_TASK_DIFF | sn63 README task/scoring sections changed |
| 2026-09-04T21:04 | sn71 | README_TASK_DIFF | sn71 README task/scoring sections changed |
| 2026-09-04T21:04 | sn85 | BURN_DROP | sn85 burn fell 1.000 -> 0.360 - miners can earn again |
| 2026-09-04T21:04 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: scoring: refuse sockets with a class so s |
| 2026-09-04T18:32 | sn7 | RELEASE | sn7 released release-20260904-155448: Add min_from_amount and candidat |
| 2026-09-04T18:32 | sn7 | SCORING_COMMIT | sn7 commit touches scoring: CLI: --send verifies source-address contro |
| 2026-09-04T18:32 | sn7 | README_TASK_DIFF | sn7 README task/scoring sections changed |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

