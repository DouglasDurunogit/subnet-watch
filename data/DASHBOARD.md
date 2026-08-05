# Subnet watch — dashboard

_snapshot 2026-08-05T22:45:10Z · block 8781106 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 52 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 91 | `miner_burn` < 0.99 |
| Ranked | 91 | passed every gate |
| **Positive margin** | **52** | income beats machine cost |
| New events this window | 5 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 55 | `████████████████████████████` |
| 0–0.2 | 8 | `████` |
| 0.2–0.4 | 3 | `██` |
| 0.4–0.6 | 7 | `████` |
| 0.6–0.8 | 7 | `████` |
| 0.8–0.99 | 11 | `██████` |
| ≥0.99 dead | 37 | `███████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn76 Phylax | 79.4 | 136 | 227 | cpu-small | 10 | 20% |
| 2 | sn107 Minos | 77.5 | 98.59 | 28,424 | cpu-small | 20 | 89% |
| 3 | sn67 Harnyx | 72.4 | 23.01 | 985 | cpu-small | 155 | 22% |
| 4 | sn96 Verathos | 72 | 54.57 | 247 | rtx4090 | 37 | 43% |
| 5 | sn114 SOMA | 71.6 | 1,177 | 4,393 | rtx4090* | 4 | 65% |
| 6 | sn91 cascade | 70.1 | 765 | 3,086 | rtx4090* | 5 | 52% |
| 7 | sn102 ConnitoAI | 69.6 | 658 | 2,064 | rtx4090* | 7 | 32% |
| 8 | sn62 Ridges | 69.5 | 634 | 2,606 | rtx4090* | 7 | 35% |
| 9 | sn26 Perturb | 68.8 | 24.87 | 202 | rtx3060 | 11 | 50% |
| 10 | sn41 Almanac | 68.4 | 9.10 | 65.80 | cpu-small | 60 | 78% |
| 11 | sn15 ORO | 67.2 | 8.43 | 18.89 | cpu-small | 76 | 93% |
| 12 | sn74 Gittensor | 66.1 | 235 | 257 | rtx4090* | 9 | 18% |
| 13 | sn124 Swarm | 65.8 | 220 | 632 | rtx4090* | 23 | 10% |
| 14 | sn38 ChronoLLM | 65.5 | 206 | 3,466 | rtx4090* | 10 | 52% |
| 15 | sn21 AdTAO | 65.5 | 4.72 | 21.86 | cpu-small | 142 | 45% |
| 16 | sn80 OpenRoboto | 62.2 | 70.85 | 269 | rtx4090* | 4 | 91% |
| 17 | sn61 RedTeam | 61.9 | 65.94 | 170 | rtx4090* | 40 | 5% |
| 18 | sn51 lium.io | 58.1 | 27.76 | 4,906 | rtx4090* | 44 | 68% |
| 19 | sn56 Gradients | 56.5 | 462 | 974 | rtx4090* | 7 | 71% |
| 20 | sn120 Affine | 55.1 | 8,267 | 8,267 = | rtx4090* | 4 | 25% |

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
| concentrated (30–60%) | 19 |
| dominated (60–90%) | 23 |
| captured (>90%) | 26 |

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
| 2026-08-05T22:45 | sn2 | RELEASE | sn2 released 14.13.0 |
| 2026-08-05T22:45 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: feat(validator): epoch-pinned weights onl |
| 2026-08-05T21:45 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: Merge pull request #6 from ippcteam/docs/ |
| 2026-08-05T21:45 | sn21 | README_TASK_DIFF | sn21 README task/scoring sections changed |
| 2026-08-05T21:45 | sn62 | RELEASE | sn62 released v0.2.6 |
| 2026-08-05T20:18 | sn2 | RELEASE | sn2 released 14.12.21 |
| 2026-08-05T20:18 | sn13 | RELEASE | sn13 released Release v1.18.70 |
| 2026-08-05T20:18 | sn13 | SCORING_COMMIT | sn13 commit touches scoring: Merge pull request #901 from macrocosm-os |
| 2026-08-05T20:18 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Refresh protected validator authority man |
| 2026-08-05T20:18 | sn88 | README_TASK_DIFF | sn88 README task/scoring sections changed |
| 2026-08-05T20:18 | sn96 | RELEASE | sn96 released v0.1.27 - Validator Boundary Hotfix |
| 2026-08-05T18:45 | sn36 | BURN_DROP | sn36 burn fell 1.000 -> 0.000 - miners can earn again |
| 2026-08-05T18:45 | sn96 | RELEASE | sn96 released v0.1.26 - Gleipnir Proof Protocol v3 |
| 2026-08-05T18:45 | sn96 | SCORING_COMMIT | sn96 commit touches scoring: fix: serialize validator block dispatch |
| 2026-08-05T16:50 | sn21 | README_TASK_DIFF | sn21 README task/scoring sections changed |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

