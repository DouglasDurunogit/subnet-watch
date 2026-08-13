# Subnet watch — dashboard

_snapshot 2026-08-13T21:22:50Z · block 8838285 · run_status **ok**_

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
| New events this window | 0 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 55 | `████████████████████████████` |
| 0–0.2 | 8 | `████` |
| 0.2–0.4 | 3 | `██` |
| 0.4–0.6 | 10 | `█████` |
| 0.6–0.8 | 7 | `████` |
| 0.8–0.99 | 7 | `████` |
| ≥0.99 dead | 38 | `███████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn107 Minos | 78.1 | 112 | 31,880 | cpu-small | 20 | 90% |
| 2 | sn76 Phylax | 74.7 | 40.07 | 192 | cpu-small | 10 | 34% |
| 3 | sn67 Harnyx | 71.3 | 17.37 | 714 | cpu-small | 148 | 19% |
| 4 | sn1 Apex | 70.5 | 850 | 1,174 | rtx4090* | 4 | 55% |
| 5 | sn91 cascade | 69.8 | 708 | 2,441 | rtx4090* | 5 | 50% |
| 6 | sn62 Ridges | 69 | 552 | 1,995 | rtx4090* | 7 | 35% |
| 7 | sn41 Almanac | 69 | 10.42 | 29.53 | cpu-small | 68 | 72% |
| 8 | sn56 Gradients | 68.9 | 534 | 989 | rtx4090* | 7 | 65% |
| 9 | sn26 Perturb | 68.8 | 24.88 | 848 | rtx3060 | 11 | 50% |
| 10 | sn38 ChronoLLM | 67.9 | 166 | 3,482 | cpu-small | 10 | 52% |
| 11 | sn6 Numinous | 67.9 | 9.65 | 511 | cpu-small | 19 | 29% |
| 12 | sn21 AdTAO | 67.7 | 7.69 | 34.48 | cpu-small | 88 | 45% |
| 13 | sn96 Verathos | 67.1 | 16.23 | 277 | rtx4090 | 76 | 41% |
| 14 | sn124 Swarm | 66 | 230 | 741 | rtx4090* | 24 | 11% |
| 15 | sn80 OpenRoboto | 65.2 | 176 | 637 | rtx4090* | 4 | 91% |
| 16 | sn85 Vidaio | 64.3 | 136 | 798 | rtx4090* | 10 | 24% |
| 17 | sn102 ConnitoAI | 60.5 | 1,529 | 1,536 | rtx4090* | 4 | 25% |
| 18 | sn28 gm | 60.1 | 39.61 | 2,205 | rtx4090* | 31 | 23% |
| 19 | sn51 lium.io | 58.9 | 33.81 | 2,200 | rtx4090* | 48 | 73% |
| 20 | sn74 Gittensor | 58.1 | 23.27 | 218 | rtx4090* | 14 | 63% |

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
| 2026-08-13T14:10 | sn1 | RELEASE | sn1 released v4.3.1 |
| 2026-08-13T12:36 | sn90 | README_TASK_DIFF | sn90 README task/scoring sections changed |
| 2026-08-13T10:35 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

