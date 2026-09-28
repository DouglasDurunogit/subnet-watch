# Subnet watch — dashboard

_snapshot 2026-09-28T01:05:10Z · block 9162913 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 57 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 96 | `miner_burn` < 0.99 |
| Ranked | 96 | passed every gate |
| **Positive margin** | **57** | income beats machine cost |
| New events this window | 7 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 63 | `████████████████████████████` |
| 0–0.2 | 8 | `████` |
| 0.2–0.4 | 7 | `███` |
| 0.4–0.6 | 2 | `█` |
| 0.6–0.8 | 10 | `████` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 32 | `██████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn102 ConnitoAI | 71.7 | 1,245 | 1,738 | rtx4090* | 6 | 30% |
| 2 | sn91 cascade | 71.5 | 446 | 1,190 | cpu-small | 5 | 52% |
| 3 | sn38 ChronoLLM | 70 | 302 | 2,661 | cpu-small | 10 | 52% |
| 4 | sn67 Harnyx | 70 | 12.00 | 1,237 | cpu-small | 114 | 35% |
| 5 | sn56 Gradients | 69.3 | 601 | 5,842 | rtx4090* | 8 | 40% |
| 6 | sn111 Claims | 69.2 | 591 | 2,612 | rtx4090* | 5 | 63% |
| 7 | sn107 Minos | 69.1 | 370 | 30,382 | cpu-small | 20 | 80% |
| 8 | sn15 ORO | 68.9 | 13.23 | 20,904 | cpu-small | 74 | 95% |
| 9 | sn4 Targon | 68.4 | 16,110 | 29,140 | rtx4090* | 5 | 58% |
| 10 | sn96 Verathos | 68.2 | 22.13 | 227 | rtx4090 | 77 | 30% |
| 11 | sn124 Swarm | 66.9 | 310 | 958 | rtx4090* | 25 | 11% |
| 12 | sn3 Teutonic | 64.8 | 5,499 | 5,499 = | rtx4090* | 5 | 20% |
| 13 | sn62 Ridges | 63.9 | 121 | 1,285 | rtx4090* | 25 | 14% |
| 14 | sn61 RedTeam | 63.5 | 106 | 305 | rtx4090* | 85 | 3% |
| 15 | sn23 Trishool | 62.1 | 933 | 933 = | cpu-small | 2 | 80% |
| 16 | sn14 Cacheon | 62 | 67.90 | 2,469 | rtx4090* | 14 | 30% |
| 17 | sn28 SayGM | 61.7 | 64.66 | 4,214 | rtx4090* | 63 | 22% |
| 18 | sn100 Cortex | 60.4 | 41.47 | 1,818 | rtx4090* | 20 | 52% |
| 19 | sn26 Perturb | 59.4 | 33.03 | 33.03 = | rtx3060 | 4 | 90% |
| 20 | sn81 Reliquary | 59 | 26.96 | 112 | rtx4090* | 29 | 81% |

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
| concentrated (30–60%) | 22 |
| dominated (60–90%) | 21 |
| captured (>90%) | 25 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 97 |
| README keywords (GUESS) | 11 |
| min_compute.yml (curated) | 10 |
| code-submission (validator runs it) | 9 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-09-28T01:05 | sn15 | RELEASE | sn15 released v2.0.35: Log nested inference tool types in proxy access |
| 2026-09-28T01:05 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: chore(deps): bump anyio from 4.13.0 to 4. |
| 2026-09-28T01:05 | sn28 | RELEASE | sn28 released v0.4.24-dev |
| 2026-09-28T01:05 | sn28 | SCORING_COMMIT | sn28 commit touches scoring: chore(release): gm-miner 0.4.24-dev (#290 |
| 2026-09-28T01:05 | sn28 | README_TASK_DIFF | sn28 README task/scoring sections changed |
| 2026-09-28T01:05 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Bind final evidence resolution verifier r |
| 2026-09-28T01:05 | sn91 | RELEASE | sn91 released worker-v0.8.2 |
| 2026-09-27T22:27 | sn56 | SCORING_COMMIT | sn56 commit touches scoring: 3 task round 1 image (#1387) |
| 2026-09-27T22:27 | sn78 | RELEASE | sn78 released Yuma validator recovery package 0.1.0 |
| 2026-09-27T22:27 | sn122 | BURN_DROP | sn122 burn fell 1.000 -> 0.724 - miners can earn again |
| 2026-09-27T19:09 | sn78 | RELEASE | sn78 released Linux amd64 validator recovery installer (c0503f5) |
| 2026-09-27T19:09 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: feat(corpus): serve the task's contract a |
| 2026-09-27T19:09 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: fix(consensus): exclude validators from  |
| 2026-09-27T15:20 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Bind verifier release to current Arena ba |
| 2026-09-27T15:20 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: perf(miner): default consensus review to |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

