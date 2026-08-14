# Subnet watch — dashboard

_snapshot 2026-08-14T02:45:03Z · block 8839896 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 55 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 90 | `miner_burn` < 0.99 |
| Ranked | 90 | passed every gate |
| **Positive margin** | **55** | income beats machine cost |
| New events this window | 0 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 55 | `████████████████████████████` |
| 0–0.2 | 8 | `████` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 9 | `█████` |
| 0.6–0.8 | 7 | `████` |
| 0.8–0.99 | 7 | `████` |
| ≥0.99 dead | 38 | `███████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn107 Minos | 77.9 | 107 | 31,593 | cpu-small | 20 | 90% |
| 2 | sn98 NeverPlayAlone | 76.1 | 1,759 | 1,759 = | cpu-small | 1 | 100% |
| 3 | sn76 Phylax | 74.7 | 39.89 | 191 | cpu-small | 10 | 34% |
| 4 | sn67 Harnyx | 73.3 | 28.52 | 501 | cpu-small | 116 | 13% |
| 5 | sn1 Apex | 70.4 | 841 | 1,197 | rtx4090* | 4 | 55% |
| 6 | sn91 cascade | 69.9 | 716 | 2,470 | rtx4090* | 5 | 50% |
| 7 | sn41 Almanac | 69.1 | 10.75 | 27.03 | cpu-small | 68 | 72% |
| 8 | sn56 Gradients | 68.9 | 535 | 993 | rtx4090* | 7 | 66% |
| 9 | sn85 Vidaio | 68.9 | 529 | 583 | rtx4090* | 10 | 17% |
| 10 | sn26 Perturb | 68.8 | 24.87 | 848 | rtx3060 | 11 | 50% |
| 11 | sn15 ORO | 68.8 | 12.58 | 12,997 | cpu-small | 79 | 93% |
| 12 | sn62 Ridges | 68.2 | 431 | 1,998 | rtx4090* | 7 | 35% |
| 13 | sn96 Verathos | 67.7 | 19.06 | 234 | rtx4090 | 72 | 41% |
| 14 | sn21 AdTAO | 67.6 | 7.67 | 34.39 | cpu-small | 88 | 45% |
| 15 | sn38 ChronoLLM | 66.6 | 114 | 1,559 | cpu-small | 10 | 52% |
| 16 | sn124 Swarm | 66 | 230 | 741 | rtx4090* | 24 | 11% |
| 17 | sn6 Numinous | 65.5 | 6.13 | 552 | cpu-small | 19 | 31% |
| 18 | sn80 OpenRoboto | 65.2 | 176 | 637 | rtx4090* | 4 | 91% |
| 19 | sn28 gm | 62.5 | 79.97 | 2,708 | rtx4090* | 33 | 29% |
| 20 | sn51 lium.io | 60.4 | 49.04 | 2,186 | rtx4090* | 49 | 73% |

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
| dominated (60–90%) | 18 |
| captured (>90%) | 24 |

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
| 2026-08-13T23:12 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: miner dashboard: label warm-start checkpo |
| 2026-08-13T22:10 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: chore(deps): bump msgpack from 1.1.2 to 1 |
| 2026-08-13T22:10 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: miner dashboard: show warm-start init + n |
| 2026-08-13T19:46 | sn100 | BURN_DROP | sn100 burn fell 1.000 -> 0.000 - miners can earn again |
| 2026-08-13T17:45 | sn118 | BURN_DROP | sn118 burn fell 1.000 -> 0.000 - miners can earn again |
| 2026-08-13T16:39 | sn6 | WEIGHTS_VERSION_BUMP | sn6 weights_version 2018 -> 3000 |
| 2026-08-13T16:39 | sn38 | SCORING_COMMIT | sn38 commit touches scoring: Update validator image to latest version  |
| 2026-08-13T16:39 | sn38 | README_TASK_DIFF | sn38 README task/scoring sections changed |
| 2026-08-13T16:39 | sn90 | RELEASE | sn90 released v1.1.0 — Targon max $/card + raised GPU card caps |
| 2026-08-13T16:39 | sn90 | SCORING_COMMIT | sn90 commit touches scoring: chore(validator): bump version to 1.1.0 f |
| 2026-08-13T15:31 | sn26 | SCORING_COMMIT | sn26 commit touches scoring: Merge pull request #49 from 0xsigurd/feat |
| 2026-08-13T15:31 | sn26 | README_TASK_DIFF | sn26 README task/scoring sections changed |
| 2026-08-13T15:31 | sn51 | RELEASE | sn51 released executor-v1.119 |
| 2026-08-13T15:31 | sn75 | SCORING_COMMIT | sn75 commit touches scoring: updated validator weights submitter |
| 2026-08-13T15:31 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: fix(site): attribute arena weight per ch |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

