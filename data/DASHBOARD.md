# Subnet watch — dashboard

_snapshot 2026-09-11T01:19:02Z · block 9040980 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 61 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 91 | `miner_burn` < 0.99 |
| Ranked | 92 | passed every gate |
| **Positive margin** | **61** | income beats machine cost |
| New events this window | 4 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 61 | `████████████████████████████` |
| 0–0.2 | 8 | `████` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 3 | `█` |
| 0.6–0.8 | 10 | `█████` |
| 0.8–0.99 | 3 | `█` |
| ≥0.99 dead | 37 | `█████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn114 SOMA | 84 | 434 | 6,957 | cpu-small | 6 | 80% |
| 2 | sn107 Minos | 83.2 | 371 | 31,463 | cpu-small | 20 | 80% |
| 3 | sn92 MicroTensor | 78.5 | 108 | 327 | cpu-small | 9 | 50% |
| 4 | sn3 Teutonic | 75.7 | 4,076 | 4,076 = | rtx4090* | 5 | 20% |
| 5 | sn67 Harnyx | 70.5 | 14.08 | 675 | cpu-small | 156 | 21% |
| 6 | sn91 cascade | 70 | 746 | 3,010 | rtx4090* | 5 | 52% |
| 7 | sn15 ORO | 70 | 15.44 | 32.91 | cpu-small | 81 | 94% |
| 8 | sn14 Cacheon | 69.4 | 615 | 1,139 | rtx4090* | 12 | 18% |
| 9 | sn96 Verathos | 69.2 | 27.51 | 255 | rtx4090 | 77 | 30% |
| 10 | sn11 TrajectoryRL | 68.4 | 6,163 | 6,163 = | cpu-small | 1 | 100% |
| 11 | sn102 ConnitoAI | 68 | 412 | 1,585 | rtx4090* | 7 | 29% |
| 12 | sn56 Gradients | 68 | 412 | 5,348 | rtx4090* | 9 | 48% |
| 13 | sn80 OpenRoboto | 67.3 | 331 | 1,180 | rtx4090* | 5 | 43% |
| 14 | sn124 Swarm | 66.5 | 271 | 878 | rtx4090* | 25 | 11% |
| 15 | sn21 AdTAO | 66.4 | 6.05 | 112 | cpu-small | 16 | 45% |
| 16 | sn111 Claims | 66.2 | 255 | 3,065 | rtx4090* | 5 | 76% |
| 17 | sn38 ChronoLLM | 66.2 | 105 | 1,433 | cpu-small | 10 | 52% |
| 18 | sn61 RedTeam | 65.9 | 217 | 325 | rtx4090* | 51 | 3% |
| 19 | sn121 sundae_bar | 62.7 | 1,143 | 1,143 = | cpu-small | 2 | 60% |
| 20 | sn108 Prometheon | 60.9 | 49.89 | 294 | rtx4090* | 11 | 30% |

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
| dominated (60–90%) | 19 |
| captured (>90%) | 20 |

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
| 2026-09-11T01:19 | sn20 | BURN_DROP | sn20 burn fell 1.000 -> 0.770 - miners can earn again |
| 2026-09-11T01:19 | sn36 | SCORING_COMMIT | sn36 commit touches scoring: Fix the private-upload commands in the mi |
| 2026-09-11T01:19 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Keep testnet Arena setup aligned with val |
| 2026-09-11T01:19 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: fix(proof): harvest scored runs when vso |
| 2026-09-10T23:19 | sn15 | RELEASE | sn15 released v2.0.3 |
| 2026-09-10T23:19 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: fix(validator): retry SimulatorCompletion |
| 2026-09-10T23:19 | sn20 | SCORING_COMMIT | sn20 commit touches scoring: Smooth mainnet rewards over configurable  |
| 2026-09-10T23:19 | sn62 | RELEASE | sn62 released v0.3.4 |
| 2026-09-10T23:19 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Ship shared SN78 validator bootstrap supe |
| 2026-09-10T23:19 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: docs(miner): minimal tbench Agent constr |
| 2026-09-10T21:14 | sn15 | RELEASE | sn15 released v2.0.2: Record search retries in validator traces (#280) |
| 2026-09-10T21:14 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: Record search retries in validator traces |
| 2026-09-10T21:14 | sn15 | README_TASK_DIFF | sn15 README task/scoring sections changed |
| 2026-09-10T21:14 | sn20 | SCORING_COMMIT | sn20 commit touches scoring: Clarify full burn when every miner has ze |
| 2026-09-10T21:14 | sn20 | README_TASK_DIFF | sn20 README task/scoring sections changed |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

