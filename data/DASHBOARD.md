# Subnet watch — dashboard

_snapshot 2026-08-05T23:43:10Z · block 8781396 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 53 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 91 | `miner_burn` < 0.99 |
| Ranked | 91 | passed every gate |
| **Positive margin** | **53** | income beats machine cost |
| New events this window | 2 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 55 | `████████████████████████████` |
| 0–0.2 | 8 | `████` |
| 0.2–0.4 | 3 | `██` |
| 0.4–0.6 | 6 | `███` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 11 | `██████` |
| ≥0.99 dead | 37 | `███████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn76 Phylax | 79.5 | 140 | 234 | cpu-small | 10 | 20% |
| 2 | sn107 Minos | 77.7 | 102 | 28,613 | cpu-small | 20 | 90% |
| 3 | sn67 Harnyx | 72.3 | 22.79 | 976 | cpu-small | 155 | 22% |
| 4 | sn96 Verathos | 72 | 54.74 | 241 | rtx4090 | 38 | 41% |
| 5 | sn114 SOMA | 71.6 | 1,180 | 4,404 | rtx4090* | 4 | 65% |
| 6 | sn91 cascade | 70.1 | 771 | 3,110 | rtx4090* | 5 | 52% |
| 7 | sn62 Ridges | 69.5 | 635 | 2,612 | rtx4090* | 7 | 35% |
| 8 | sn102 ConnitoAI | 69.4 | 612 | 2,216 | rtx4090* | 7 | 34% |
| 9 | sn26 Perturb | 68.9 | 25.01 | 203 | rtx3060 | 11 | 50% |
| 10 | sn41 Almanac | 68.4 | 9.11 | 65.88 | cpu-small | 60 | 78% |
| 11 | sn15 ORO | 67 | 8.51 | 19.07 | cpu-small | 76 | 93% |
| 12 | sn74 Gittensor | 66.1 | 236 | 257 | rtx4090* | 9 | 18% |
| 13 | sn124 Swarm | 65.8 | 221 | 634 | rtx4090* | 23 | 10% |
| 14 | sn21 AdTAO | 65.6 | 4.78 | 22.09 | cpu-small | 142 | 45% |
| 15 | sn38 ChronoLLM | 65.5 | 205 | 3,456 | rtx4090* | 10 | 52% |
| 16 | sn80 OpenRoboto | 62.2 | 71.03 | 269 | rtx4090* | 4 | 91% |
| 17 | sn61 RedTeam | 62 | 66.49 | 171 | rtx4090* | 40 | 5% |
| 18 | sn2 DSperse | 58.1 | 20.11 | 101 | rtx4090* | 13 | 83% |
| 19 | sn51 lium.io | 57.5 | 24.46 | 5,114 | rtx4090* | 45 | 68% |
| 20 | sn56 Gradients | 56.5 | 463 | 976 | rtx4090* | 7 | 71% |

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
| concentrated (30–60%) | 18 |
| dominated (60–90%) | 24 |
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

