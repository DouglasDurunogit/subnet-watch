# Subnet watch — dashboard

_snapshot 2026-09-22T12:33:38Z · block 9123163 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 61 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 98 | `miner_burn` < 0.99 |
| Ranked | 98 | passed every gate |
| **Positive margin** | **61** | income beats machine cost |
| New events this window | 0 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 65 | `████████████████████████████` |
| 0–0.2 | 9 | `████` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 30 | `█████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn4 Targon | 78.7 | 9,747 | 27,368 | rtx4090* | 6 | 53% |
| 2 | sn3 Teutonic | 77 | 5,943 | 5,943 = | rtx4090* | 5 | 20% |
| 3 | sn91 cascade | 73 | 709 | 2,840 | cpu-small | 5 | 52% |
| 4 | sn102 ConnitoAI | 71.3 | 1,096 | 1,544 | rtx4090* | 6 | 30% |
| 5 | sn67 Harnyx | 69.5 | 11.34 | 1,430 | cpu-small | 125 | 37% |
| 6 | sn107 Minos | 69.3 | 393 | 33,114 | cpu-small | 20 | 80% |
| 7 | sn38 ChronoLLM | 68.4 | 199 | 2,709 | cpu-small | 10 | 52% |
| 8 | sn15 ORO | 68 | 12.47 | 25.56 | cpu-small | 64 | 96% |
| 9 | sn111 Claims | 67.3 | 344 | 3,072 | rtx4090* | 5 | 70% |
| 10 | sn124 Swarm | 67.3 | 342 | 1,089 | rtx4090* | 25 | 11% |
| 11 | sn14 Cacheon | 66.2 | 235 | 2,429 | rtx4090* | 16 | 28% |
| 12 | sn28 SayGM | 62.8 | 88.16 | 1,730 | rtx4090* | 62 | 14% |
| 13 | sn56 Gradients | 62.2 | 72.61 | 6,115 | rtx4090* | 18 | 40% |
| 14 | sn74 Gittensor | 62.1 | 75.34 | 321 | rtx4090* | 13 | 64% |
| 15 | sn23 Trishool | 61.7 | 841 | 841 = | cpu-small | 2 | 80% |
| 16 | sn62 Ridges | 61.7 | 62.34 | 3,026 | rtx4090* | 19 | 30% |
| 17 | sn60 Bitsec.ai | 60.5 | 590 | 590 = | cpu-small | 3 | 50% |
| 18 | sn61 RedTeam | 58.9 | 28.01 | 853 | rtx4090* | 117 | 9% |
| 19 | sn81 Reliquary | 58.6 | 24.18 | 89.17 | rtx4090* | 24 | 86% |
| 20 | sn51 lium.io | 58.1 | 32.11 | 2,458 | rtx4090* | 70 | 81% |

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
| concentrated (30–60%) | 24 |
| dominated (60–90%) | 21 |
| captured (>90%) | 26 |

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

