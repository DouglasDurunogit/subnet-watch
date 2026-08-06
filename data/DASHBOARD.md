# Subnet watch — dashboard

_snapshot 2026-08-06T04:41:15Z · block 8782886 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 55 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 91 | `miner_burn` < 0.99 |
| Ranked | 91 | passed every gate |
| **Positive margin** | **55** | income beats machine cost |
| New events this window | 6 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 56 | `████████████████████████████` |
| 0–0.2 | 6 | `███` |
| 0.2–0.4 | 3 | `██` |
| 0.4–0.6 | 7 | `████` |
| 0.6–0.8 | 7 | `████` |
| 0.8–0.99 | 12 | `██████` |
| ≥0.99 dead | 37 | `██████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn76 Phylax | 78 | 95.25 | 439 | cpu-small | 10 | 28% |
| 2 | sn107 Minos | 77.8 | 104 | 28,188 | cpu-small | 20 | 90% |
| 3 | sn60 Bitsec.ai | 77 | 2,276 | 2,276 = | cpu-small | 2 | 90% |
| 4 | sn67 Harnyx | 72.6 | 24.43 | 1,139 | cpu-small | 126 | 25% |
| 5 | sn114 SOMA | 71.6 | 1,177 | 4,394 | rtx4090* | 4 | 65% |
| 6 | sn96 Verathos | 71 | 42.11 | 183 | rtx4090 | 54 | 43% |
| 7 | sn91 cascade | 70.1 | 754 | 3,042 | rtx4090* | 5 | 52% |
| 8 | sn62 Ridges | 69.5 | 630 | 2,592 | rtx4090* | 7 | 35% |
| 9 | sn102 ConnitoAI | 68.8 | 510 | 1,955 | rtx4090* | 7 | 33% |
| 10 | sn26 Perturb | 68.5 | 22.84 | 926 | rtx3060 | 11 | 51% |
| 11 | sn41 Almanac | 67.4 | 7.26 | 60.87 | cpu-small | 52 | 83% |
| 12 | sn15 ORO | 67 | 8.18 | 18.57 | cpu-small | 73 | 94% |
| 13 | sn74 Gittensor | 66.1 | 237 | 259 | rtx4090* | 9 | 18% |
| 14 | sn124 Swarm | 65.8 | 220 | 632 | rtx4090* | 23 | 10% |
| 15 | sn21 AdTAO | 65.6 | 4.82 | 22.25 | cpu-small | 142 | 45% |
| 16 | sn38 ChronoLLM | 65.5 | 205 | 3,449 | rtx4090* | 10 | 52% |
| 17 | sn80 OpenRoboto | 62.2 | 71.31 | 270 | rtx4090* | 4 | 91% |
| 18 | sn61 RedTeam | 62.1 | 68.78 | 177 | rtx4090* | 40 | 5% |
| 19 | sn101 Tag101 | 59.8 | 0.09 | 0.75 | cpu-small | 243 | 90% |
| 20 | sn51 lium.io | 57.6 | 24.62 | 4,954 | rtx4090* | 43 | 66% |

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
| concentrated (30–60%) | 17 |
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
| 2026-08-06T04:41 | sn2 | RELEASE | sn2 released 14.13.1 |
| 2026-08-06T04:41 | sn66 | SCORING_COMMIT | sn66 commit touches scoring: Merge pull request #28 from conjectures-i |
| 2026-08-06T04:41 | sn66 | README_TASK_DIFF | sn66 README task/scoring sections changed |
| 2026-08-06T04:41 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Honor scoring maintenance between rebench |
| 2026-08-06T04:41 | sn74 | RELEASE | sn74 released release-20260806-043739 |
| 2026-08-06T04:41 | sn74 | SCORING_COMMIT | sn74 commit touches scoring: sparkinfer-k3: 3x faster time-decay for m |
| 2026-08-05T22:45 | sn2 | RELEASE | sn2 released 14.13.0 |
| 2026-08-05T22:45 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: feat(validator): epoch-pinned weights onl |
| 2026-08-05T21:45 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: Merge pull request #6 from ippcteam/docs/ |
| 2026-08-05T21:45 | sn21 | README_TASK_DIFF | sn21 README task/scoring sections changed |
| 2026-08-05T21:45 | sn62 | RELEASE | sn62 released v0.2.6 |
| 2026-08-05T20:18 | sn2 | RELEASE | sn2 released 14.12.21 |
| 2026-08-05T20:18 | sn13 | RELEASE | sn13 released Release v1.18.70 |
| 2026-08-05T20:18 | sn13 | SCORING_COMMIT | sn13 commit touches scoring: Merge pull request #901 from macrocosm-os |
| 2026-08-05T20:18 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Refresh protected validator authority man |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

