# Subnet watch — dashboard

_snapshot 2026-09-22T06:49:47Z · block 9121444 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 56 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 97 | `miner_burn` < 0.99 |
| Ranked | 97 | passed every gate |
| **Positive margin** | **56** | income beats machine cost |
| New events this window | 10 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 64 | `████████████████████████████` |
| 0–0.2 | 9 | `████` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 31 | `██████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn4 Targon | 78.6 | 9,578 | 26,895 | rtx4090* | 6 | 53% |
| 2 | sn3 Teutonic | 77 | 5,937 | 5,937 = | rtx4090* | 5 | 20% |
| 3 | sn91 cascade | 73 | 713 | 2,854 | cpu-small | 5 | 52% |
| 4 | sn67 Harnyx | 69.5 | 11.22 | 1,411 | cpu-small | 120 | 37% |
| 5 | sn102 ConnitoAI | 69.3 | 605 | 1,330 | rtx4090* | 7 | 26% |
| 6 | sn107 Minos | 69.3 | 387 | 32,856 | cpu-small | 20 | 80% |
| 7 | sn15 ORO | 68.7 | 11.74 | 22,353 | cpu-small | 63 | 97% |
| 8 | sn38 ChronoLLM | 67.8 | 168 | 2,290 | cpu-small | 10 | 52% |
| 9 | sn124 Swarm | 67.3 | 343 | 1,093 | rtx4090* | 25 | 11% |
| 10 | sn111 Claims | 66.9 | 306 | 3,148 | rtx4090* | 5 | 73% |
| 11 | sn14 Cacheon | 66.1 | 230 | 2,382 | rtx4090* | 16 | 28% |
| 12 | sn28 SayGM | 62.8 | 87.74 | 1,986 | rtx4090* | 67 | 12% |
| 13 | sn56 Gradients | 62.2 | 71.08 | 5,998 | rtx4090* | 18 | 40% |
| 14 | sn74 Gittensor | 61.7 | 66.10 | 327 | rtx4090* | 14 | 63% |
| 15 | sn62 Ridges | 61.7 | 61.22 | 1,130 | rtx4090* | 19 | 30% |
| 16 | sn23 Trishool | 61.6 | 815 | 815 = | cpu-small | 2 | 80% |
| 17 | sn60 Bitsec.ai | 60.5 | 582 | 582 = | cpu-small | 3 | 50% |
| 18 | sn61 RedTeam | 59 | 27.31 | 893 | rtx4090* | 125 | 9% |
| 19 | sn81 Reliquary | 58.6 | 23.77 | 87.92 | rtx4090* | 24 | 86% |
| 20 | sn80 OpenRoboto | 57.7 | 651 | 2,298 | rtx4090* | 5 | 43% |

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
| dominated (60–90%) | 20 |
| captured (>90%) | 25 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 98 |
| README keywords (GUESS) | 10 |
| min_compute.yml (curated) | 10 |
| code-submission (validator runs it) | 9 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-09-22T06:50 | sn15 | RELEASE | sn15 released v2.0.29 |
| 2026-09-22T06:50 | sn25 | RELEASE | sn25 released v2026.9.21-1052448720 |
| 2026-09-22T06:50 | sn26 | SCORING_COMMIT | sn26 commit touches scoring: fix: commitment snapshot carries the mode |
| 2026-09-22T06:50 | sn45 | SCORING_COMMIT | sn45 commit touches scoring: Owe a share again to a miner sent nothing |
| 2026-09-22T06:50 | sn51 | RELEASE | sn51 released executor-v1.134 |
| 2026-09-22T06:50 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-09-22T06:50 | sn78 | RELEASE | sn78 released Cohort 4 miner connection inputs (policy 8) |
| 2026-09-22T06:50 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Publish current C4 miner setup and verifi |
| 2026-09-22T06:50 | sn78 | README_TASK_DIFF | sn78 README task/scoring sections changed |
| 2026-09-22T06:50 | sn100 | BURN_DROP | sn100 burn fell 1.000 -> 0.803 - miners can earn again |
| 2026-09-22T01:35 | sn25 | RELEASE | sn25 released v2026.9.21-1052359470 |
| 2026-09-22T01:35 | sn78 | RELEASE | sn78 released Cohort 3: provisional scores (uncertified) |
| 2026-09-22T01:35 | sn91 | RELEASE | sn91 released worker-v0.12.0 |
| 2026-09-21T22:51 | sn62 | RELEASE | sn62 released v0.3.6 |
| 2026-09-21T22:51 | sn66 | README_TASK_DIFF | sn66 README task/scoring sections changed |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

