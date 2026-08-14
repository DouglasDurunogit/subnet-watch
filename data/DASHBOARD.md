# Subnet watch — dashboard

_snapshot 2026-08-14T09:17:44Z · block 8841859 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 55 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 89 | `miner_burn` < 0.99 |
| Ranked | 89 | passed every gate |
| **Positive margin** | **55** | income beats machine cost |
| New events this window | 4 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 54 | `████████████████████████████` |
| 0–0.2 | 7 | `████` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 9 | `█████` |
| 0.6–0.8 | 6 | `███` |
| 0.8–0.99 | 9 | `█████` |
| ≥0.99 dead | 39 | `████████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn107 Minos | 77.8 | 104 | 30,999 | cpu-small | 20 | 90% |
| 2 | sn76 Phylax | 74.7 | 40.34 | 193 | cpu-small | 10 | 34% |
| 3 | sn60 Bitsec.ai | 73.2 | 734 | 1,028 | cpu-small | 3 | 50% |
| 4 | sn67 Harnyx | 73.2 | 28.42 | 484 | cpu-small | 122 | 13% |
| 5 | sn1 Apex | 70.2 | 797 | 1,155 | rtx4090* | 4 | 56% |
| 6 | sn41 Almanac | 69.1 | 10.59 | 26.50 | cpu-small | 68 | 72% |
| 7 | sn56 Gradients | 68.8 | 524 | 975 | rtx4090* | 7 | 66% |
| 8 | sn26 Perturb | 68.8 | 24.53 | 837 | rtx3060 | 11 | 50% |
| 9 | sn91 cascade | 68.5 | 473 | 1,086 | rtx4090* | 5 | 50% |
| 10 | sn96 Verathos | 68.3 | 21.93 | 194 | rtx4090 | 70 | 41% |
| 11 | sn62 Ridges | 68.1 | 423 | 1,964 | rtx4090* | 7 | 35% |
| 12 | sn15 ORO | 68 | 11.22 | 12,479 | cpu-small | 82 | 93% |
| 13 | sn21 AdTAO | 67.7 | 7.67 | 34.39 | cpu-small | 88 | 45% |
| 14 | sn11 TrajectoryRL | 67.2 | 4,278 | 4,278 = | cpu-small | 1 | 100% |
| 15 | sn6 Numinous | 66.7 | 7.50 | 548 | cpu-small | 19 | 32% |
| 16 | sn38 ChronoLLM | 66.5 | 112 | 1,526 | cpu-small | 10 | 52% |
| 17 | sn124 Swarm | 65.9 | 224 | 722 | rtx4090* | 24 | 11% |
| 18 | sn80 OpenRoboto | 65.2 | 178 | 644 | rtx4090* | 4 | 91% |
| 19 | sn85 Vidaio | 65 | 168 | 1,051 | rtx4090* | 10 | 32% |
| 20 | sn98 NeverPlayAlone | 64.1 | 1,723 | 1,723 = | cpu-small | 1 | 100% |

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
| wide (<30%) | 22 |
| concentrated (30–60%) | 22 |
| dominated (60–90%) | 17 |
| captured (>90%) | 26 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 103 |
| code-submission (validator runs it) | 9 |
| min_compute.yml (curated) | 9 |
| README keywords (GUESS) | 6 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-08-14T09:18 | sn2 | BURN_DROP | sn2 burn fell 1.000 -> 0.822 - miners can earn again |
| 2026-08-14T09:18 | sn44 | SCORING_COMMIT | sn44 commit touches scoring: Merge pull request #52 from score-technol |
| 2026-08-14T09:18 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-2622: floor a live miner's weight at  |
| 2026-08-14T09:18 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: chore(deploy): promote prod prism-challe |
| 2026-08-14T06:06 | sn90 | RELEASE | sn90 released v1.1.1 |
| 2026-08-14T06:06 | sn90 | SCORING_COMMIT | sn90 commit touches scoring: fix(validator): always apply the Targon s |
| 2026-08-14T06:06 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: chore(deploy): promote prod prism-challe |
| 2026-08-13T23:12 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: miner dashboard: label warm-start checkpo |
| 2026-08-13T22:10 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: chore(deps): bump msgpack from 1.1.2 to 1 |
| 2026-08-13T22:10 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: miner dashboard: show warm-start init + n |
| 2026-08-13T19:46 | sn100 | BURN_DROP | sn100 burn fell 1.000 -> 0.000 - miners can earn again |
| 2026-08-13T17:45 | sn118 | BURN_DROP | sn118 burn fell 1.000 -> 0.000 - miners can earn again |
| 2026-08-13T16:39 | sn6 | WEIGHTS_VERSION_BUMP | sn6 weights_version 2018 -> 3000 |
| 2026-08-13T16:39 | sn38 | SCORING_COMMIT | sn38 commit touches scoring: Update validator image to latest version  |
| 2026-08-13T16:39 | sn38 | README_TASK_DIFF | sn38 README task/scoring sections changed |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

