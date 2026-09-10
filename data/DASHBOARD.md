# Subnet watch — dashboard

_snapshot 2026-09-10T18:36:27Z · block 9038969 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 59 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 90 | `miner_burn` < 0.99 |
| Ranked | 90 | passed every gate |
| **Positive margin** | **59** | income beats machine cost |
| New events this window | 7 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 62 | `████████████████████████████` |
| 0–0.2 | 8 | `████` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 7 | `███` |
| 0.8–0.99 | 4 | `██` |
| ≥0.99 dead | 38 | `█████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn114 SOMA | 84 | 442 | 7,093 | cpu-small | 6 | 80% |
| 2 | sn107 Minos | 83.3 | 382 | 32,442 | cpu-small | 20 | 80% |
| 3 | sn92 MicroTensor | 78.6 | 113 | 340 | cpu-small | 9 | 50% |
| 4 | sn3 Teutonic | 75.7 | 4,110 | 4,110 = | rtx4090* | 5 | 20% |
| 5 | sn102 ConnitoAI | 71.2 | 1,055 | 1,815 | rtx4090* | 5 | 34% |
| 6 | sn67 Harnyx | 70.5 | 14.27 | 684 | cpu-small | 153 | 21% |
| 7 | sn15 ORO | 70.3 | 20.91 | 44.24 | cpu-small | 81 | 92% |
| 8 | sn91 cascade | 70.2 | 795 | 3,203 | rtx4090* | 5 | 52% |
| 9 | sn14 Cacheon | 69.4 | 628 | 1,164 | rtx4090* | 12 | 18% |
| 10 | sn96 Verathos | 69.4 | 28.63 | 247 | rtx4090 | 84 | 30% |
| 11 | sn11 TrajectoryRL | 68.5 | 6,335 | 6,335 = | cpu-small | 1 | 100% |
| 12 | sn56 Gradients | 68.1 | 419 | 5,441 | rtx4090* | 9 | 48% |
| 13 | sn38 ChronoLLM | 67.5 | 148 | 3,137 | cpu-small | 10 | 52% |
| 14 | sn80 OpenRoboto | 67.3 | 332 | 1,183 | rtx4090* | 5 | 43% |
| 15 | sn124 Swarm | 66.6 | 276 | 860 | rtx4090* | 25 | 11% |
| 16 | sn21 AdTAO | 66.5 | 6.17 | 114 | cpu-small | 16 | 45% |
| 17 | sn111 Claims | 66.3 | 263 | 3,173 | rtx4090* | 5 | 76% |
| 18 | sn61 RedTeam | 65.9 | 218 | 327 | rtx4090* | 51 | 3% |
| 19 | sn108 Prometheon | 61 | 50.84 | 299 | rtx4090* | 11 | 30% |
| 20 | sn41 Almanac | 60.5 | 39.89 | 110 | cpu-small | 83 | 3% |

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
| concentrated (30–60%) | 25 |
| dominated (60–90%) | 17 |
| captured (>90%) | 21 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 97 |
| min_compute.yml (curated) | 11 |
| code-submission (validator runs it) | 10 |
| README keywords (GUESS) | 9 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-09-10T18:37 | sn9 | RELEASE | sn9 released v4.12.17 |
| 2026-09-10T18:37 | sn15 | RELEASE | sn15 released v2.0.1 |
| 2026-09-10T18:37 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: Select validator evaluator from claimed p |
| 2026-09-10T18:37 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: docs(rewards): restate the curve with an  |
| 2026-09-10T18:37 | sn25 | RELEASE | sn25 released v2026.9.10-1042581110 |
| 2026-09-10T18:37 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Validate deployed legacy coordinator comm |
| 2026-09-10T18:37 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Expose Linux validator setup |
| 2026-09-10T15:13 | sn9 | RELEASE | sn9 released v4.12.16 |
| 2026-09-10T15:13 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-2748, hide a node the validator canno |
| 2026-09-10T15:13 | sn63 | SCORING_COMMIT | sn63 commit touches scoring: Fix issue with migrated validator db |
| 2026-09-10T15:13 | sn66 | README_TASK_DIFF | sn66 README task/scoring sections changed |
| 2026-09-10T15:13 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: Document V6 miner submission allowance |
| 2026-09-10T15:13 | sn108 | SCORING_COMMIT | sn108 commit touches scoring: feat(evaluation): optionally discard a c |
| 2026-09-10T11:39 | sn15 | RELEASE | sn15 released v2.0.0 |
| 2026-09-10T11:39 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: Verify scope-bound environment deliveries |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

