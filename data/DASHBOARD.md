# Subnet watch — dashboard

_snapshot 2026-09-10T06:18:35Z · block 9035288 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 59 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 91 | `miner_burn` < 0.99 |
| Ranked | 92 | passed every gate |
| **Positive margin** | **59** | income beats machine cost |
| New events this window | 9 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 60 | `████████████████████████████` |
| 0–0.2 | 8 | `████` |
| 0.2–0.4 | 8 | `████` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 3 | `█` |
| ≥0.99 dead | 37 | `█████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn114 SOMA | 87.1 | 951 | 7,614 | cpu-small | 4 | 80% |
| 2 | sn107 Minos | 83.6 | 410 | 34,719 | cpu-small | 20 | 80% |
| 3 | sn92 MicroTensor | 78.6 | 113 | 253 | cpu-small | 9 | 50% |
| 4 | sn3 Teutonic | 76 | 4,405 | 4,405 = | rtx4090* | 5 | 20% |
| 5 | sn56 Gradients | 72.1 | 1,400 | 5,759 | rtx4090* | 7 | 47% |
| 6 | sn15 ORO | 71.4 | 25.23 | 47.20 | cpu-small | 78 | 92% |
| 7 | sn67 Harnyx | 70.7 | 15.21 | 727 | cpu-small | 132 | 21% |
| 8 | sn91 cascade | 70.3 | 801 | 3,230 | rtx4090* | 5 | 52% |
| 9 | sn14 Cacheon | 69.6 | 666 | 1,234 | rtx4090* | 12 | 18% |
| 10 | sn96 Verathos | 69.6 | 30.77 | 220 | rtx4090 | 82 | 30% |
| 11 | sn11 TrajectoryRL | 68.6 | 6,614 | 6,614 = | cpu-small | 1 | 100% |
| 12 | sn80 OpenRoboto | 67.6 | 357 | 1,271 | rtx4090* | 5 | 43% |
| 13 | sn38 ChronoLLM | 67.4 | 145 | 3,078 | cpu-small | 10 | 52% |
| 14 | sn124 Swarm | 66.8 | 296 | 921 | rtx4090* | 25 | 11% |
| 15 | sn61 RedTeam | 66.8 | 286 | 461 | rtx4090* | 40 | 5% |
| 16 | sn111 Claims | 65.8 | 232 | 3,236 | rtx4090* | 5 | 73% |
| 17 | sn121 sundae_bar | 63 | 1,233 | 1,233 = | cpu-small | 2 | 60% |
| 18 | sn81 Reliquary | 62.3 | 74.46 | 270 | rtx4090* | 51 | 6% |
| 19 | sn108 Prometheon | 61.2 | 53.83 | 314 | rtx4090* | 11 | 30% |
| 20 | sn41 Almanac | 60.7 | 42.05 | 117 | cpu-small | 84 | 3% |

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
| captured (>90%) | 20 |

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
| 2026-09-10T06:19 | sn15 | RELEASE | sn15 released shoppingbench-final |
| 2026-09-10T06:19 | sn15 | README_TASK_DIFF | sn15 README task/scoring sections changed |
| 2026-09-10T06:19 | sn25 | RELEASE | sn25 released v2026.9.9-1042199790 |
| 2026-09-10T06:19 | sn51 | RELEASE | sn51 released executor-v1.124 |
| 2026-09-10T06:19 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-3006 - [P1] validator stops serialisi |
| 2026-09-10T06:19 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Preserve validated page final URLs |
| 2026-09-10T06:19 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: Merge pull request #236 from reliquadotai |
| 2026-09-10T06:19 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: Merge pull request #251 from TensorLink-A |
| 2026-09-10T06:19 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: docs(proof): add miner guide for the tbe |
| 2026-09-10T01:20 | sn25 | RELEASE | sn25 released v2026.9.9-1042000000 |
| 2026-09-10T01:20 | sn71 | README_TASK_DIFF | sn71 README task/scoring sections changed |
| 2026-09-10T01:20 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: fix: validate sampled entropy coverage at |
| 2026-09-10T01:20 | sn100 | RELEASE | sn100 released ctx CLI v3.3.31 |
| 2026-09-10T01:20 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: feat(proof): require miner hotkey signat |
| 2026-09-09T23:25 | sn25 | RELEASE | sn25 released v2026.9.9-1041947070 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

