# Subnet watch — dashboard

_snapshot 2026-10-01T00:12:25Z · block 9184249 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 63 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 98 | `miner_burn` < 0.99 |
| Ranked | 98 | passed every gate |
| **Positive margin** | **63** | income beats machine cost |
| New events this window | 5 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 66 | `████████████████████████████` |
| 0–0.2 | 9 | `████` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 2 | `█` |
| 0.6–0.8 | 10 | `████` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 30 | `█████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn41 Almanac | 74.3 | 39.26 | 861 | cpu-small | 119 | 13% |
| 2 | sn23 Trishool | 74 | 958 | 958 = | cpu-small | 2 | 80% |
| 3 | sn53 engy | 72.1 | 1,389 | 3,810 | rtx4090 | 14 | 22% |
| 4 | sn91 cascade | 72.1 | 544 | 2,181 | cpu-small | 5 | 52% |
| 5 | sn1 Apex | 70.9 | 983 | 1,148 | rtx4090* | 4 | 54% |
| 6 | sn102 ConnitoAI | 70.9 | 959 | 1,442 | rtx4090* | 6 | 29% |
| 7 | sn56 Gradients | 69.6 | 652 | 5,291 | rtx4090* | 9 | 39% |
| 8 | sn15 ORO | 69.2 | 13.29 | 20,110 | cpu-small | 83 | 95% |
| 9 | sn107 Minos | 68.8 | 347 | 29,480 | cpu-small | 20 | 80% |
| 10 | sn46 Instant | 68.1 | 162 | 166 | cpu-small | 7 | 68% |
| 11 | sn111 Claims | 67.9 | 407 | 2,480 | rtx4090* | 5 | 64% |
| 12 | sn96 Verathos | 67 | 16.55 | 300 | rtx4090 | 70 | 33% |
| 13 | sn4 Targon | 65.4 | 6,510 | 32,896 | rtx4090* | 5 | 71% |
| 14 | sn14 Cacheon | 64.8 | 156 | 2,305 | rtx4090* | 16 | 29% |
| 15 | sn3 Teutonic | 64.4 | 4,894 | 4,894 = | rtx4090* | 5 | 20% |
| 16 | sn62 Ridges | 63.8 | 115 | 1,392 | rtx4090* | 25 | 15% |
| 17 | sn61 RedTeam | 62.7 | 85.57 | 156 | rtx4090* | 112 | 2% |
| 18 | sn28 SayGM | 62.3 | 76.07 | 1,007 | rtx4090* | 67 | 17% |
| 19 | sn81 Reliquary | 59.8 | 34.33 | 70.21 | rtx4090* | 25 | 84% |
| 20 | sn5 Hone | 59.7 | 40.54 | 43.67 | rtx4090* | 241 | 0% |

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
| concentrated (30–60%) | 22 |
| dominated (60–90%) | 24 |
| captured (>90%) | 25 |

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
| 2026-10-01T00:12 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Bind October verifier evidence release |
| 2026-10-01T00:12 | sn74 | RELEASE | sn74 released release-20260930-235444 |
| 2026-10-01T00:12 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Separate miner transport signer from coho |
| 2026-10-01T00:12 | sn117 | RELEASE | sn117 released everycli v0.1.4 |
| 2026-10-01T00:12 | sn117 | README_TASK_DIFF | sn117 README task/scoring sections changed |
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

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

