# Subnet watch — dashboard

_snapshot 2026-09-18T05:16:32Z · block 9092391 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 57 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 96 | `miner_burn` < 0.99 |
| Ranked | 96 | passed every gate |
| **Positive margin** | **57** | income beats machine cost |
| New events this window | 7 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 64 | `████████████████████████████` |
| 0–0.2 | 9 | `████` |
| 0.2–0.4 | 7 | `███` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 4 | `██` |
| ≥0.99 dead | 32 | `██████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn11 TrajectoryRL | 80.3 | 6,200 | 6,200 = | cpu-small | 1 | 100% |
| 2 | sn4 Targon | 77.7 | 7,364 | 20,674 | rtx4090* | 6 | 51% |
| 3 | sn92 MicroTensor | 76.2 | 61.75 | 178 | cpu-small | 8 | 39% |
| 4 | sn91 cascade | 72.8 | 660 | 2,642 | cpu-small | 5 | 52% |
| 5 | sn102 ConnitoAI | 69 | 545 | 1,302 | rtx4090* | 7 | 27% |
| 6 | sn67 Harnyx | 69 | 9.68 | 1,242 | cpu-small | 108 | 41% |
| 7 | sn107 Minos | 68.8 | 337 | 27,753 | cpu-small | 20 | 80% |
| 8 | sn56 Gradients | 68.2 | 429 | 5,203 | rtx4090* | 10 | 46% |
| 9 | sn124 Swarm | 66.5 | 274 | 883 | rtx4090* | 25 | 11% |
| 10 | sn38 ChronoLLM | 65.8 | 95.81 | 848 | cpu-small | 10 | 52% |
| 11 | sn111 Claims | 65.1 | 190 | 2,747 | rtx4090* | 5 | 79% |
| 12 | sn3 Teutonic | 64.2 | 4,558 | 4,558 = | rtx4090* | 5 | 20% |
| 13 | sn62 Ridges | 62.4 | 76.19 | 1,543 | rtx4090* | 20 | 22% |
| 14 | sn28 SayGM | 62 | 70.16 | 1,603 | rtx4090* | 67 | 12% |
| 15 | sn55 NIOME | 62 | 68.11 | 564 | rtx4090* | 11 | 29% |
| 16 | sn74 Gittensor | 61.4 | 58.79 | 268 | rtx4090* | 10 | 62% |
| 17 | sn81 Reliquary | 60.6 | 44.24 | 102 | rtx4090* | 35 | 55% |
| 18 | sn51 lium.io | 59.3 | 38.97 | 1,796 | rtx4090* | 66 | 81% |
| 19 | sn61 RedTeam | 58.8 | 26.39 | 2,224 | rtx4090* | 117 | 21% |
| 20 | sn15 ORO | 57 | 2.38 | 6.63 | cpu-small | 21 | 100% |

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
| concentrated (30–60%) | 27 |
| dominated (60–90%) | 19 |
| captured (>90%) | 23 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 97 |
| min_compute.yml (curated) | 11 |
| code-submission (validator runs it) | 10 |
| README keywords (GUESS) | 9 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-09-18T05:16 | sn15 | RELEASE | sn15 released v2.0.23 |
| 2026-09-18T05:16 | sn25 | RELEASE | sn25 released v2026.9.17-1048981210 |
| 2026-09-18T05:16 | sn49 | SCORING_COMMIT | sn49 commit touches scoring: Enhance tournament reward structure to su |
| 2026-09-18T05:16 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Preserve verified historical local releas |
| 2026-09-18T05:16 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Bind evaluation readiness to the deployed |
| 2026-09-18T05:16 | sn92 | RELEASE | sn92 released v0.4.12 |
| 2026-09-18T05:16 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: scoring: extraction F1 compares leaf fiel |
| 2026-09-18T00:36 | sn15 | RELEASE | sn15 released v2.0.22 |
| 2026-09-18T00:36 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: Score partial harness failures alongside  |
| 2026-09-18T00:36 | sn25 | RELEASE | sn25 released v2026.9.17-1048903120 |
| 2026-09-18T00:36 | sn34 | SCORING_COMMIT | sn34 commit touches scoring: Merge pull request #460 from BitMind-AI/f |
| 2026-09-18T00:36 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Fit Sep18 evaluation schedule to measured |
| 2026-09-18T00:36 | sn74 | RELEASE | sn74 released release-20260917-234413 |
| 2026-09-18T00:36 | sn127 | BURN_DROP | sn127 burn fell 1.000 -> 0.714 - miners can earn again |
| 2026-09-17T22:20 | sn4 | RELEASE | sn4 released v2.0.1 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

