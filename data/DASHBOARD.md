# Subnet watch — dashboard

_snapshot 2026-09-11T21:21:19Z · block 9046977 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 57 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 89 | `miner_burn` < 0.99 |
| Ranked | 90 | passed every gate |
| **Positive margin** | **57** | income beats machine cost |
| New events this window | 4 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 59 | `████████████████████████████` |
| 0–0.2 | 9 | `████` |
| 0.2–0.4 | 7 | `███` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 7 | `███` |
| 0.8–0.99 | 3 | `█` |
| ≥0.99 dead | 39 | `███████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn92 MicroTensor | 80.1 | 165 | 497 | cpu-small | 9 | 24% |
| 2 | sn21 AdTAO | 75.7 | 53.96 | 133 | cpu-small | 21 | 34% |
| 3 | sn91 cascade | 71.5 | 1,155 | 3,094 | rtx4090* | 5 | 52% |
| 4 | sn67 Harnyx | 70.3 | 13.45 | 1,084 | cpu-small | 126 | 33% |
| 5 | sn96 Verathos | 70.2 | 34.83 | 235 | rtx4090 | 68 | 31% |
| 6 | sn14 Cacheon | 69.4 | 619 | 1,146 | rtx4090* | 12 | 18% |
| 7 | sn107 Minos | 69 | 358 | 30,356 | cpu-small | 20 | 80% |
| 8 | sn11 TrajectoryRL | 68.4 | 6,132 | 6,132 = | cpu-small | 1 | 100% |
| 9 | sn56 Gradients | 68 | 411 | 5,342 | rtx4090* | 9 | 48% |
| 10 | sn80 OpenRoboto | 67.5 | 347 | 1,235 | rtx4090* | 5 | 43% |
| 11 | sn124 Swarm | 66.5 | 272 | 879 | rtx4090* | 25 | 11% |
| 12 | sn38 ChronoLLM | 66.1 | 104 | 1,415 | cpu-small | 10 | 52% |
| 13 | sn61 RedTeam | 65.4 | 192 | 287 | rtx4090* | 59 | 3% |
| 14 | sn111 Claims | 64.9 | 180 | 3,203 | rtx4090* | 5 | 82% |
| 15 | sn3 Teutonic | 63.8 | 4,121 | 4,121 = | rtx4090* | 5 | 20% |
| 16 | sn55 NIOME | 62.4 | 76.72 | 629 | rtx4090* | 11 | 29% |
| 17 | sn28 SayGM | 61.5 | 60.48 | 2,976 | rtx4090* | 43 | 21% |
| 18 | sn41 Almanac | 60.4 | 39.42 | 119 | cpu-small | 82 | 4% |
| 19 | sn23 Trishool | 60.2 | 544 | 544 = | cpu-small | 2 | 80% |
| 20 | sn102 ConnitoAI | 59.6 | 1,151 | 1,427 | rtx4090* | 6 | 28% |

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
| wide (<30%) | 27 |
| concentrated (30–60%) | 24 |
| dominated (60–90%) | 15 |
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
| 2026-09-11T21:21 | sn20 | SCORING_COMMIT | sn20 commit touches scoring: Add grounded video scoring and hybrid mai |
| 2026-09-11T21:21 | sn25 | RELEASE | sn25 released v2026.9.11-1043550030 |
| 2026-09-11T21:21 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Verify in-flight Arena leases survive par |
| 2026-09-11T21:21 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: fix(proof): fail-closed harbor partial s |
| 2026-09-11T18:42 | sn15 | RELEASE | sn15 released v2.0.6 |
| 2026-09-11T18:42 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: chore(validator): pin oro-env-runtime 0.2 |
| 2026-09-11T18:42 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Observe provisional validator intents fro |
| 2026-09-11T18:42 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Accept Harvest plural current positions i |
| 2026-09-11T18:42 | sn71 | README_TASK_DIFF | sn71 README task/scoring sections changed |
| 2026-09-11T15:15 | sn9 | RELEASE | sn9 released v4.12.18 |
| 2026-09-11T15:15 | sn55 | SCORING_COMMIT | sn55 commit touches scoring: upload all miners submissions |
| 2026-09-11T15:15 | sn66 | SCORING_COMMIT | sn66 commit touches scoring: Merge pull request #90 from conjectures-i |
| 2026-09-11T15:15 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Fix normal validator startup defaults and |
| 2026-09-11T15:15 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Clarify miner keepalive requirements duri |
| 2026-09-11T15:15 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: fix(proof): bind keyword-only miner setu |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

