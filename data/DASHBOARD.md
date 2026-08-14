# Subnet watch — dashboard

_snapshot 2026-08-14T10:32:11Z · block 8842232 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 53 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 89 | `miner_burn` < 0.99 |
| Ranked | 89 | passed every gate |
| **Positive margin** | **53** | income beats machine cost |
| New events this window | 4 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 57 | `████████████████████████████` |
| 0–0.2 | 6 | `███` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 8 | `████` |
| 0.6–0.8 | 7 | `███` |
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 39 | `███████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn107 Minos | 78.1 | 113 | 31,103 | cpu-small | 20 | 90% |
| 2 | sn76 Phylax | 74.6 | 39.72 | 190 | cpu-small | 10 | 34% |
| 3 | sn67 Harnyx | 73.2 | 28.34 | 483 | cpu-small | 122 | 13% |
| 4 | sn60 Bitsec.ai | 73.1 | 716 | 1,003 | cpu-small | 3 | 50% |
| 5 | sn26 Perturb | 71.4 | 46.77 | 355 | rtx3060 | 10 | 70% |
| 6 | sn1 Apex | 70.2 | 790 | 1,147 | rtx4090* | 4 | 56% |
| 7 | sn96 Verathos | 69.1 | 26.65 | 188 | rtx4090 | 64 | 41% |
| 8 | sn41 Almanac | 69 | 10.58 | 26.48 | cpu-small | 68 | 72% |
| 9 | sn56 Gradients | 68.8 | 522 | 972 | rtx4090* | 7 | 66% |
| 10 | sn91 cascade | 68.6 | 495 | 1,138 | rtx4090* | 5 | 50% |
| 11 | sn62 Ridges | 68.1 | 422 | 1,959 | rtx4090* | 7 | 35% |
| 12 | sn15 ORO | 68 | 11.27 | 12,527 | cpu-small | 82 | 93% |
| 13 | sn21 AdTAO | 67.7 | 7.65 | 34.29 | cpu-small | 88 | 45% |
| 14 | sn85 Vidaio | 67.3 | 329 | 891 | rtx4090* | 10 | 27% |
| 15 | sn11 TrajectoryRL | 67.2 | 4,258 | 4,258 = | cpu-small | 1 | 100% |
| 16 | sn6 Numinous | 66.7 | 7.48 | 547 | cpu-small | 19 | 32% |
| 17 | sn38 ChronoLLM | 66.5 | 112 | 1,523 | cpu-small | 10 | 52% |
| 18 | sn124 Swarm | 65.9 | 224 | 724 | rtx4090* | 24 | 11% |
| 19 | sn80 OpenRoboto | 65.2 | 175 | 633 | rtx4090* | 4 | 91% |
| 20 | sn28 gm | 62.7 | 86.05 | 2,797 | rtx4090* | 30 | 30% |

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
| dominated (60–90%) | 18 |
| captured (>90%) | 25 |

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

