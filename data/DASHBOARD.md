# Subnet watch — dashboard

_snapshot 2026-09-30T20:46:03Z · block 9183217 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 66 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 99 | `miner_burn` < 0.99 |
| Ranked | 99 | passed every gate |
| **Positive margin** | **66** | income beats machine cost |
| New events this window | 11 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 65 | `████████████████████████████` |
| 0–0.2 | 8 | `███` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 3 | `█` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 8 | `███` |
| ≥0.99 dead | 29 | `████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn41 Almanac | 74.3 | 38.86 | 117 | cpu-small | 119 | 14% |
| 2 | sn23 Trishool | 74.1 | 987 | 987 = | cpu-small | 2 | 80% |
| 3 | sn91 cascade | 72.3 | 569 | 2,061 | cpu-small | 5 | 49% |
| 4 | sn53 engy | 72.1 | 1,391 | 3,816 | rtx4090 | 14 | 22% |
| 5 | sn1 Apex | 71.1 | 1,018 | 1,068 | rtx4090* | 4 | 54% |
| 6 | sn102 ConnitoAI | 71 | 1,006 | 1,794 | rtx4090* | 4 | 36% |
| 7 | sn56 Gradients | 69.6 | 656 | 5,321 | rtx4090* | 9 | 39% |
| 8 | sn46 Instant | 69 | 215 | 221 | cpu-small | 6 | 68% |
| 9 | sn15 ORO | 68.9 | 13.11 | 19,863 | cpu-small | 83 | 95% |
| 10 | sn107 Minos | 68.8 | 347 | 29,430 | cpu-small | 20 | 80% |
| 11 | sn96 Verathos | 68 | 21.30 | 312 | rtx4090 | 63 | 31% |
| 12 | sn111 Claims | 67.9 | 409 | 2,493 | rtx4090* | 5 | 64% |
| 13 | sn4 Targon | 65.4 | 6,541 | 33,051 | rtx4090* | 5 | 71% |
| 14 | sn14 Cacheon | 64.8 | 156 | 2,302 | rtx4090* | 16 | 29% |
| 15 | sn62 Ridges | 64.5 | 143 | 1,147 | rtx4090* | 26 | 13% |
| 16 | sn3 Teutonic | 64.4 | 4,916 | 4,916 = | rtx4090* | 5 | 20% |
| 17 | sn61 RedTeam | 62.7 | 84.26 | 153 | rtx4090* | 112 | 2% |
| 18 | sn81 Reliquary | 59.8 | 34.36 | 93.67 | rtx4090* | 22 | 83% |
| 19 | sn5 Hone | 59.5 | 41.47 | 43.99 | rtx4090* | 234 | 0% |
| 20 | sn28 SayGM | 59.5 | 34.47 | 993 | rtx4090* | 70 | 36% |

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
| wide (<30%) | 21 |
| concentrated (30–60%) | 24 |
| dominated (60–90%) | 24 |
| captured (>90%) | 26 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 96 |
| README keywords (GUESS) | 12 |
| min_compute.yml (curated) | 10 |
| code-submission (validator runs it) | 9 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-09-30T20:46 | sn5 | SCORING_COMMIT | sn5 commit touches scoring: Merge pull request #13 from hone-subnet-or |
| 2026-09-30T20:46 | sn8 | SCORING_COMMIT | sn8 commit touches scoring: disable miner daily summary (#934) |
| 2026-09-30T20:46 | sn41 | SCORING_COMMIT | sn41 commit touches scoring: Updates to handling excess miner emission |
| 2026-09-30T20:46 | sn66 | README_TASK_DIFF | sn66 README task/scoring sections changed |
| 2026-09-30T20:46 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: fix(corpus): next on a free job is a 409, |
| 2026-09-30T20:46 | sn108 | SCORING_COMMIT | sn108 commit touches scoring: Validator: periodic weight status line,  |
| 2026-09-30T20:46 | sn108 | README_TASK_DIFF | sn108 README task/scoring sections changed |
| 2026-09-30T20:46 | sn117 | BURN_DROP | sn117 burn fell 1.000 -> 0.978 - miners can earn again |
| 2026-09-30T20:46 | sn117 | RELEASE | sn117 released everycli v0.1.3 |
| 2026-09-30T20:46 | sn117 | SCORING_COMMIT | sn117 commit touches scoring: feat: simplify miner onboarding and API  |
| 2026-09-30T20:46 | sn117 | README_TASK_DIFF | sn117 README task/scoring sections changed |
| 2026-09-30T15:53 | sn20 | SCORING_COMMIT | sn20 commit touches scoring: Isolate GPU model execution and enforce v |
| 2026-09-30T15:53 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Build mips64 miner targets as softfloat |
| 2026-09-30T15:53 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: NO-TICKET - [P2] validator: log repeated  |
| 2026-09-30T15:53 | sn97 | SCORING_COMMIT | sn97 commit touches scoring: fix: accept submits like the bench in eva |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

