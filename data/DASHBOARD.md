# Subnet watch — dashboard

_snapshot 2026-09-27T19:08:35Z · block 9161130 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 59 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 95 | `miner_burn` < 0.99 |
| Ranked | 95 | passed every gate |
| **Positive margin** | **59** | income beats machine cost |
| New events this window | 3 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 63 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 7 | `███` |
| 0.4–0.6 | 2 | `█` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 33 | `███████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn102 ConnitoAI | 72.1 | 1,381 | 1,905 | rtx4090* | 5 | 30% |
| 2 | sn91 cascade | 71.6 | 458 | 1,222 | cpu-small | 5 | 52% |
| 3 | sn1 Apex | 71.1 | 1,036 | 1,149 | rtx4090* | 4 | 57% |
| 4 | sn38 ChronoLLM | 70.3 | 337 | 2,965 | cpu-small | 10 | 52% |
| 5 | sn67 Harnyx | 70.1 | 12.50 | 1,285 | cpu-small | 113 | 35% |
| 6 | sn56 Gradients | 69.4 | 627 | 6,094 | rtx4090* | 8 | 40% |
| 7 | sn107 Minos | 69.1 | 373 | 31,004 | cpu-small | 20 | 80% |
| 8 | sn15 ORO | 68.7 | 13.97 | 21,987 | cpu-small | 74 | 95% |
| 9 | sn4 Targon | 68.6 | 16,724 | 30,251 | rtx4090* | 5 | 58% |
| 10 | sn96 Verathos | 68.4 | 23.18 | 263 | rtx4090 | 78 | 30% |
| 11 | sn111 Claims | 67.2 | 341 | 3,051 | rtx4090* | 5 | 70% |
| 12 | sn124 Swarm | 67.2 | 331 | 995 | rtx4090* | 25 | 11% |
| 13 | sn3 Teutonic | 65 | 5,749 | 5,749 = | rtx4090* | 5 | 20% |
| 14 | sn62 Ridges | 64.1 | 126 | 1,334 | rtx4090* | 25 | 14% |
| 15 | sn61 RedTeam | 63.7 | 112 | 321 | rtx4090* | 85 | 3% |
| 16 | sn14 Cacheon | 63.3 | 98.35 | 2,540 | rtx4090* | 14 | 30% |
| 17 | sn23 Trishool | 62.2 | 973 | 973 = | cpu-small | 2 | 80% |
| 18 | sn28 SayGM | 62.1 | 73.14 | 980 | rtx4090* | 65 | 34% |
| 19 | sn100 Cortex | 60.1 | 37.71 | 255 | rtx4090* | 19 | 70% |
| 20 | sn81 Reliquary | 59.6 | 32.12 | 122 | rtx4090* | 29 | 80% |

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
| wide (<30%) | 23 |
| concentrated (30–60%) | 21 |
| dominated (60–90%) | 22 |
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
| 2026-09-27T19:09 | sn78 | RELEASE | sn78 released Linux amd64 validator recovery installer (c0503f5) |
| 2026-09-27T19:09 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: feat(corpus): serve the task's contract a |
| 2026-09-27T19:09 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: fix(consensus): exclude validators from  |
| 2026-09-27T15:20 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Bind verifier release to current Arena ba |
| 2026-09-27T15:20 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: perf(miner): default consensus review to |
| 2026-09-27T15:20 | sn111 | README_TASK_DIFF | sn111 README task/scoring sections changed |
| 2026-09-27T15:20 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: Merge PR #78 (cursor/task-instruction-ga |
| 2026-09-27T10:40 | sn15 | RELEASE | sn15 released v2.0.34: Authorize inference without a shared Compose mo |
| 2026-09-27T10:40 | sn61 | RELEASE | sn61 released 4.10.7 |
| 2026-09-27T10:40 | sn61 | SCORING_COMMIT | sn61 commit touches scoring: Merge pull request #149 from RedTeamSubne |
| 2026-09-27T10:40 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Bind verifier evidence continuity to revi |
| 2026-09-27T10:40 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: wvk 25 δ fork: flip time 08:35 UTC in AG |
| 2026-09-27T05:12 | sn25 | RELEASE | sn25 released v2026.9.26-1056759680 |
| 2026-09-27T05:12 | sn34 | SCORING_COMMIT | sn34 commit touches scoring: Merge pull request #464 from BitMind-AI/d |
| 2026-09-27T05:12 | sn34 | README_TASK_DIFF | sn34 README task/scoring sections changed |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

