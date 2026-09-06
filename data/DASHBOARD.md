# Subnet watch — dashboard

_snapshot 2026-09-06T22:52:27Z · block 9011488 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 61 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 94 | `miner_burn` < 0.99 |
| Ranked | 95 | passed every gate |
| **Positive margin** | **61** | income beats machine cost |
| New events this window | 2 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 59 | `████████████████████████████` |
| 0–0.2 | 10 | `█████` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 3 | `█` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 8 | `████` |
| ≥0.99 dead | 34 | `████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn92 MicroTensor | 81.4 | 228 | 507 | cpu-small | 9 | 26% |
| 2 | sn107 Minos | 77.1 | 95.28 | 6,003 | cpu-small | 21 | 80% |
| 3 | sn3 Teutonic | 76 | 4,450 | 4,450 = | rtx4090* | 5 | 20% |
| 4 | sn114 SOMA | 74.2 | 1,009 | 1,009 = | cpu-small | 3 | 80% |
| 5 | sn67 Harnyx | 72.5 | 23.35 | 1,204 | cpu-small | 108 | 31% |
| 6 | sn14 Cacheon | 71.5 | 1,170 | 2,220 | rtx4090* | 6 | 30% |
| 7 | sn102 ConnitoAI | 71.1 | 1,040 | 1,675 | rtx4090* | 6 | 29% |
| 8 | sn15 ORO | 70.9 | 23.91 | 46.88 | cpu-small | 82 | 92% |
| 9 | sn91 cascade | 70.8 | 955 | 3,844 | rtx4090* | 5 | 52% |
| 10 | sn96 Verathos | 70.3 | 36.59 | 627 | rtx4090 | 78 | 40% |
| 11 | sn11 TrajectoryRL | 68.9 | 7,260 | 7,260 = | cpu-small | 1 | 100% |
| 12 | sn111 Claims | 68.6 | 506 | 2,240 | rtx4090* | 5 | 47% |
| 13 | sn62 Ridges | 68.3 | 442 | 1,313 | rtx4090* | 13 | 26% |
| 14 | sn56 Gradients | 67.8 | 389 | 3,647 | rtx4090* | 7 | 49% |
| 15 | sn124 Swarm | 66.9 | 306 | 943 | rtx4090* | 25 | 11% |
| 16 | sn80 OpenRoboto | 65.6 | 198 | 713 | rtx4090* | 5 | 71% |
| 17 | sn108 Prometheon | 63.3 | 99.69 | 382 | rtx4090* | 10 | 33% |
| 18 | sn65 True Performance | 62.8 | 95.21 | 199 | rtx4090* | 6 | 75% |
| 19 | sn101 Tag101 | 62.4 | 0.87 | 0.87 = | cpu-small | 241 | 90% |
| 20 | sn41 Almanac | 60.2 | 37.26 | 103 | cpu-small | 86 | 17% |

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
| concentrated (30–60%) | 21 |
| dominated (60–90%) | 21 |
| captured (>90%) | 23 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 99 |
| min_compute.yml (curated) | 11 |
| code-submission (validator runs it) | 10 |
| README keywords (GUESS) | 7 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-09-06T22:52 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Record recovery checkpoints and post-pull |
| 2026-09-06T22:52 | sn34 | README_TASK_DIFF | sn34 README task/scoring sections changed |
| 2026-09-06T20:52 | sn93 | SCORING_COMMIT | sn93 commit touches scoring: chore: scope validator deploy to code/con |
| 2026-09-06T18:30 | sn14 | RELEASE | sn14 released GLM-5.3 mock mainnet submissions (validator self-test, 2 |
| 2026-09-06T18:30 | sn93 | README_TASK_DIFF | sn93 README task/scoring sections changed |
| 2026-09-06T16:12 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Integrate qualified Solidity validator ac |
| 2026-09-06T16:12 | sn47 | BURN_DROP | sn47 burn fell 1.000 -> 0.942 - miners can earn again |
| 2026-09-06T12:51 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Checkpoint held repair sources and valida |
| 2026-09-06T04:34 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Isolate Arena failure regressions and ver |
| 2026-09-06T04:34 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Add public registered-miner endpoint pilo |
| 2026-09-06T00:06 | sn74 | RELEASE | sn74 released release-20260905-223823 |
| 2026-09-06T00:06 | sn74 | SCORING_COMMIT | sn74 commit touches scoring: serving miner: an attestation waits for p |
| 2026-09-05T22:21 | sn7 | RELEASE | sn7 released release-20260905-204833 |
| 2026-09-05T22:21 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: chore(validator): bind existing recovery  |
| 2026-09-05T20:34 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Protect validator seed custody and qualif |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

