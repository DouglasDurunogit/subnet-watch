# Subnet watch — dashboard

_snapshot 2026-09-09T21:16:36Z · block 9032582 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 59 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 92 | `miner_burn` < 0.99 |
| Ranked | 93 | passed every gate |
| **Positive margin** | **59** | income beats machine cost |
| New events this window | 8 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 61 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 7 | `███` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 5 | `██` |
| ≥0.99 dead | 36 | `█████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn114 SOMA | 87.2 | 984 | 7,882 | cpu-small | 4 | 80% |
| 2 | sn107 Minos | 83.7 | 425 | 34,652 | cpu-small | 20 | 79% |
| 3 | sn92 MicroTensor | 78.6 | 112 | 250 | cpu-small | 9 | 50% |
| 4 | sn3 Teutonic | 76 | 4,470 | 4,470 = | rtx4090* | 5 | 20% |
| 5 | sn56 Gradients | 72.2 | 1,418 | 5,828 | rtx4090* | 7 | 47% |
| 6 | sn67 Harnyx | 71.7 | 18.95 | 537 | cpu-small | 125 | 15% |
| 7 | sn15 ORO | 71.6 | 25.56 | 48.21 | cpu-small | 78 | 92% |
| 8 | sn91 cascade | 70.3 | 811 | 3,269 | rtx4090* | 5 | 52% |
| 9 | sn14 Cacheon | 69.7 | 675 | 1,250 | rtx4090* | 12 | 18% |
| 10 | sn96 Verathos | 69.7 | 31.32 | 173 | rtx4090 | 87 | 31% |
| 11 | sn11 TrajectoryRL | 68.7 | 6,772 | 6,772 = | cpu-small | 1 | 100% |
| 12 | sn62 Ridges | 67.9 | 396 | 1,247 | rtx4090* | 13 | 26% |
| 13 | sn80 OpenRoboto | 67.6 | 366 | 1,204 | rtx4090* | 5 | 43% |
| 14 | sn124 Swarm | 66.9 | 306 | 822 | rtx4090* | 25 | 9% |
| 15 | sn61 RedTeam | 66.8 | 288 | 457 | rtx4090* | 40 | 4% |
| 16 | sn38 ChronoLLM | 66.1 | 103 | 1,411 | cpu-small | 10 | 52% |
| 17 | sn111 Claims | 65.3 | 202 | 3,587 | rtx4090* | 5 | 82% |
| 18 | sn121 sundae_bar | 63 | 1,250 | 1,250 = | cpu-small | 2 | 60% |
| 19 | sn108 Prometheon | 60.9 | 49.28 | 119 | rtx4090* | 11 | 33% |
| 20 | sn41 Almanac | 60.7 | 42.14 | 92.66 | cpu-small | 85 | 3% |

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
| concentrated (30–60%) | 22 |
| dominated (60–90%) | 19 |
| captured (>90%) | 21 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 98 |
| min_compute.yml (curated) | 11 |
| code-submission (validator runs it) | 10 |
| README keywords (GUESS) | 8 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-09-09T21:17 | sn20 | SCORING_COMMIT | sn20 commit touches scoring: Document model-independent miner extensio |
| 2026-09-09T21:17 | sn20 | README_TASK_DIFF | sn20 README task/scoring sections changed |
| 2026-09-09T21:17 | sn36 | SCORING_COMMIT | sn36 commit touches scoring: Merge pull request #5 from EpagoFoundatio |
| 2026-09-09T21:17 | sn62 | RELEASE | sn62 released v0.3.2 |
| 2026-09-09T21:17 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Merge remote-tracking branch 'origin/main |
| 2026-09-09T21:17 | sn78 | WEIGHTS_VERSION_BUMP | sn78 weights_version 1 -> 4294967296 |
| 2026-09-09T21:17 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Add prerequisite-gated validator supervis |
| 2026-09-09T21:17 | sn104 | BURN_DROP | sn104 burn fell 1.000 -> 0.988 - miners can earn again |
| 2026-09-09T18:46 | sn28 | RELEASE | sn28 released v0.4.17-dev |
| 2026-09-09T18:46 | sn28 | README_TASK_DIFF | sn28 README task/scoring sections changed |
| 2026-09-09T18:46 | sn62 | RELEASE | sn62 released v0.3.1 |
| 2026-09-09T18:46 | sn62 | SCORING_COMMIT | sn62 commit touches scoring: feat: prevent cluster-autoscaler from dra |
| 2026-09-09T18:46 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Merge remote-tracking branch 'origin/main |
| 2026-09-09T18:46 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Publish verified bootstrap service state |
| 2026-09-09T18:46 | sn108 | README_TASK_DIFF | sn108 README task/scoring sections changed |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

