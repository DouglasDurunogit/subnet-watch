# Subnet watch — dashboard

_snapshot 2026-09-11T11:39:53Z · block 9044076 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 61 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 90 | `miner_burn` < 0.99 |
| Ranked | 91 | passed every gate |
| **Positive margin** | **61** | income beats machine cost |
| New events this window | 9 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 59 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 9 | `████` |
| 0.4–0.6 | 3 | `█` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 3 | `█` |
| ≥0.99 dead | 38 | `██████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn92 MicroTensor | 80.3 | 171 | 515 | cpu-small | 9 | 24% |
| 2 | sn3 Teutonic | 75.6 | 3,991 | 3,991 = | rtx4090* | 5 | 20% |
| 3 | sn67 Harnyx | 70.2 | 13.23 | 1,064 | cpu-small | 121 | 33% |
| 4 | sn91 cascade | 70.1 | 756 | 3,047 | rtx4090* | 5 | 52% |
| 5 | sn14 Cacheon | 69.3 | 603 | 1,118 | rtx4090* | 12 | 18% |
| 6 | sn107 Minos | 69.1 | 362 | 30,692 | cpu-small | 20 | 80% |
| 7 | sn102 ConnitoAI | 69 | 558 | 1,425 | rtx4090* | 7 | 28% |
| 8 | sn96 Verathos | 68.8 | 24.66 | 155 | rtx4090 | 77 | 33% |
| 9 | sn11 TrajectoryRL | 68.3 | 5,979 | 5,979 = | cpu-small | 1 | 100% |
| 10 | sn56 Gradients | 68 | 403 | 5,236 | rtx4090* | 9 | 48% |
| 11 | sn80 OpenRoboto | 67.6 | 363 | 1,292 | rtx4090* | 5 | 43% |
| 12 | sn124 Swarm | 66.4 | 265 | 858 | rtx4090* | 25 | 11% |
| 13 | sn61 RedTeam | 66.2 | 243 | 369 | rtx4090* | 49 | 4% |
| 14 | sn21 AdTAO | 66.2 | 5.70 | 106 | cpu-small | 16 | 45% |
| 15 | sn38 ChronoLLM | 66.1 | 102 | 1,397 | cpu-small | 10 | 52% |
| 16 | sn111 Claims | 65.3 | 202 | 3,117 | rtx4090* | 5 | 80% |
| 17 | sn121 sundae_bar | 62.7 | 1,121 | 1,121 = | cpu-small | 2 | 60% |
| 18 | sn108 Prometheon | 62.5 | 80.06 | 257 | rtx4090* | 13 | 27% |
| 19 | sn28 SayGM | 62.3 | 75.25 | 2,455 | rtx4090* | 38 | 35% |
| 20 | sn41 Almanac | 60.4 | 39.01 | 113 | cpu-small | 82 | 3% |

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
| concentrated (30–60%) | 25 |
| dominated (60–90%) | 18 |
| captured (>90%) | 19 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 96 |
| min_compute.yml (curated) | 11 |
| code-submission (validator runs it) | 10 |
| README keywords (GUESS) | 10 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-09-11T11:40 | sn10 | SCORING_COMMIT | sn10 commit touches scoring: fix(ops): verify staged units against the |
| 2026-09-11T11:40 | sn20 | SCORING_COMMIT | sn20 commit touches scoring: Add scorer v1.1.0 and signed round feedba |
| 2026-09-11T11:40 | sn20 | README_TASK_DIFF | sn20 README task/scoring sections changed |
| 2026-09-11T11:40 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Resume provisional validators from comple |
| 2026-09-11T11:40 | sn51 | RELEASE | sn51 released miner-v1.004 |
| 2026-09-11T11:40 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-3206 - [P2] miner accepts a validator |
| 2026-09-11T11:40 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-09-11T11:40 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Remove unused validator V2 release metada |
| 2026-09-11T11:40 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Make main installer select signed validat |
| 2026-09-11T06:22 | sn7 | RELEASE | sn7 released release-20260911-013831 |
| 2026-09-11T06:22 | sn7 | SCORING_COMMIT | sn7 commit touches scoring: Miner wizard: funding step, one shared EVM |
| 2026-09-11T06:22 | sn7 | README_TASK_DIFF | sn7 README task/scoring sections changed |
| 2026-09-11T06:22 | sn15 | RELEASE | sn15 released v2.0.4 |
| 2026-09-11T06:22 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Honor transition limits for typed validat |
| 2026-09-11T06:22 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-3019 - [P1] validator reports verific |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

