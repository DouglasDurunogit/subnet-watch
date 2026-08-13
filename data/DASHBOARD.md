# Subnet watch — dashboard

_snapshot 2026-08-13T23:11:36Z · block 8838829 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 54 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 90 | `miner_burn` < 0.99 |
| Ranked | 90 | passed every gate |
| **Positive margin** | **54** | income beats machine cost |
| New events this window | 3 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 56 | `████████████████████████████` |
| 0–0.2 | 7 | `████` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 9 | `████` |
| 0.6–0.8 | 7 | `████` |
| 0.8–0.99 | 7 | `████` |
| ≥0.99 dead | 38 | `███████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn107 Minos | 77.8 | 106 | 31,701 | cpu-small | 20 | 90% |
| 2 | sn76 Phylax | 74.6 | 39.43 | 189 | cpu-small | 10 | 34% |
| 3 | sn67 Harnyx | 71.3 | 17.35 | 713 | cpu-small | 148 | 19% |
| 4 | sn1 Apex | 70.4 | 846 | 1,171 | rtx4090* | 4 | 55% |
| 5 | sn91 cascade | 69.9 | 712 | 2,457 | rtx4090* | 5 | 50% |
| 6 | sn15 ORO | 69.1 | 13.18 | 13,572 | cpu-small | 79 | 93% |
| 7 | sn41 Almanac | 69 | 10.41 | 29.49 | cpu-small | 68 | 72% |
| 8 | sn56 Gradients | 68.9 | 532 | 986 | rtx4090* | 7 | 66% |
| 9 | sn26 Perturb | 68.8 | 24.82 | 846 | rtx3060 | 11 | 50% |
| 10 | sn62 Ridges | 68.2 | 430 | 1,995 | rtx4090* | 7 | 35% |
| 11 | sn6 Numinous | 68 | 9.73 | 515 | cpu-small | 19 | 29% |
| 12 | sn38 ChronoLLM | 67.9 | 165 | 3,460 | cpu-small | 10 | 52% |
| 13 | sn21 AdTAO | 67.7 | 7.68 | 34.43 | cpu-small | 88 | 45% |
| 14 | sn96 Verathos | 66.9 | 15.65 | 257 | rtx4090 | 75 | 41% |
| 15 | sn124 Swarm | 65.9 | 227 | 733 | rtx4090* | 24 | 11% |
| 16 | sn80 OpenRoboto | 65.2 | 174 | 631 | rtx4090* | 4 | 91% |
| 17 | sn85 Vidaio | 64.3 | 135 | 423 | rtx4090* | 10 | 22% |
| 18 | sn28 gm | 59.9 | 37.07 | 2,730 | rtx4090* | 30 | 29% |
| 19 | sn102 ConnitoAI | 59.4 | 1,080 | 1,797 | rtx4090* | 6 | 29% |
| 20 | sn51 lium.io | 59.4 | 38.21 | 2,190 | rtx4090* | 45 | 73% |

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
| concentrated (30–60%) | 22 |
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

