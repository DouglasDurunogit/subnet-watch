# Subnet watch — dashboard

_snapshot 2026-11-23T12:18:50Z · block 9569355 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 51 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 105 | `miner_burn` < 0.99 |
| Ranked | 105 | passed every gate |
| **Positive margin** | **51** | income beats machine cost |
| New events this window | 10 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 69 | `████████████████████████████` |
| 0–0.2 | 6 | `██` |
| 0.2–0.4 | 6 | `██` |
| 0.4–0.6 | 2 | `█` |
| 0.6–0.8 | 12 | `█████` |
| 0.8–0.99 | 10 | `████` |
| ≥0.99 dead | 23 | `█████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn42 CADmind | 81.7 | 240 | 240 = | cpu-small | 5 | 20% |
| 2 | sn3 Teutonic | 73.2 | 1,917 | 3,894 | rtx4090* | 4 | 40% |
| 3 | sn15 ORO | 64.9 | 5.00 | 10.70 | cpu-small | 71 | 95% |
| 4 | sn124 Swarm | 64.8 | 166 | 1,299 | rtx4090* | 11 | 29% |
| 5 | sn67 Harnyx | 63.7 | 1.69 | 317 | cpu-small | 120 | 23% |
| 6 | sn53 engy | 63.4 | 103 | 3,614 | rtx4090 | 20 | 61% |
| 7 | sn66 conjectures | 62.6 | 80.76 | 956 | rtx4090* | 4 | 80% |
| 8 | sn120 Affine | 61.9 | 2,325 | 2,325 = | rtx4090* | 9 | 11% |
| 9 | sn58 Attune | 61.6 | 60.92 | 152 | rtx4090* | 57 | 30% |
| 10 | sn41 Almanac | 60.8 | 1.89 | 225 | cpu-small | 121 | 16% |
| 11 | sn62 Ridges | 60.7 | 45.21 | 390 | rtx4090* | 47 | 10% |
| 12 | sn111 Claims | 60.2 | 39.48 | 159 | rtx4090* | 4 | 88% |
| 13 | sn25 UR | 58.1 | 20.71 | 20.71 = | rtx4090* | 10 | 45% |
| 14 | sn102 ConnitoAI | 57 | 530 | 531 | rtx4090* | 4 | 25% |
| 15 | sn99 Axonry | 55.8 | 10,839 | 10,839 = | rtx4090* | 1 | 100% |
| 16 | sn4 Targon | 55.5 | 4,851 | 19,908 | rtx4090* | 5 | 67% |
| 17 | sn46 Instant | 55.5 | 133 | 155 | cpu-small | 9 | 24% |
| 18 | sn107 Minos | 54.6 | 139 | 11,576 | cpu-small | 20 | 79% |
| 19 | sn116 Carbon | 52.4 | 2,651 | 2,651 = | rtx4090* | 2 | 75% |
| 20 | sn14 Cacheon | 50.8 | 83.61 | 683 | rtx4090* | 6 | 71% |

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
| concentrated (30–60%) | 17 |
| dominated (60–90%) | 29 |
| captured (>90%) | 29 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 97 |
| README keywords (GUESS) | 13 |
| min_compute.yml (curated) | 10 |
| code-submission (validator runs it) | 8 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-11-23T12:19 | sn12 | RELEASE | sn12 released miner-testing-2026-11-23-45138900060-7-1: feat: preserve |
| 2026-11-23T12:19 | sn42 | RELEASE | sn42 released v0.6.26 |
| 2026-11-23T12:19 | sn42 | SCORING_COMMIT | sn42 commit touches scoring: release 0.6.26: the miner stats answer re |
| 2026-11-23T12:19 | sn51 | RELEASE | sn51 released watchtower-v1.2.4 |
| 2026-11-23T12:19 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-6582 - Executor and validator: update |
| 2026-11-23T12:19 | sn56 | SCORING_COMMIT | sn56 commit touches scoring: Build and publish the quant evaluator ima |
| 2026-11-23T12:19 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Set the verified AWS region for the pilot |
| 2026-11-23T12:19 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: feat(laned): W7d satellite verifies the r |
| 2026-11-23T12:19 | sn94 | SCORING_COMMIT | sn94 commit touches scoring: Count a fresh pass from the challenge, no |
| 2026-11-23T12:19 | sn99 | SCORING_COMMIT | sn99 commit touches scoring: A champion is evaluated on benchmarks add |
| 2026-11-23T03:01 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: docs(scoring): the exact calculation writ |
| 2026-11-23T03:01 | sn21 | README_TASK_DIFF | sn21 README task/scoring sections changed |
| 2026-11-23T03:01 | sn70 | RELEASE | sn70 released Miner image image-v2026.11.22b (v0.7.0, protocol v4) |
| 2026-11-23T03:01 | sn70 | SCORING_COMMIT | sn70 commit touches scoring: docs: the validator guide's v4 READY line |
| 2026-11-23T03:01 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Preserve a normal execution attempt after |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

