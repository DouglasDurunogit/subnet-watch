# Subnet watch — dashboard

_snapshot 2026-10-11T19:37:57Z · block 9262072 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 62 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 100 | `miner_burn` < 0.99 |
| Ranked | 100 | passed every gate |
| **Positive margin** | **62** | income beats machine cost |
| New events this window | 11 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 70 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 7 | `███` |
| 0.6–0.8 | 7 | `███` |
| 0.8–0.99 | 5 | `██` |
| ≥0.99 dead | 28 | `███████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn107 Minos | 82.4 | 311 | 26,462 | cpu-small | 20 | 80% |
| 2 | sn3 Teutonic | 75 | 3,311 | 3,311 = | rtx4090* | 5 | 40% |
| 3 | sn80 OpenRoboto | 72.3 | 1,470 | 7,009 | rtx4090* | 7 | 35% |
| 4 | sn14 Cacheon | 70.1 | 769 | 6,156 | rtx4090* | 3 | 83% |
| 5 | sn101 Tag101 | 70.1 | 12.91 | 14.95 | cpu-small | 244 | 1% |
| 6 | sn67 Harnyx | 68.9 | 9.21 | 954 | cpu-small | 127 | 33% |
| 7 | sn38 ChronoLLM | 68.8 | 219 | 999 | cpu-small | 9 | 52% |
| 8 | sn41 Almanac | 67.9 | 9.13 | 173 | cpu-small | 105 | 3% |
| 9 | sn79 MVTRX | 67.4 | 8.06 | 44.81 | cpu-small | 244 | 2% |
| 10 | sn4 Targon | 67 | 10,469 | 30,865 | rtx4090* | 5 | 70% |
| 11 | sn15 ORO | 66.6 | 6.69 | 13.77 | cpu-small | 52 | 98% |
| 12 | sn62 Ridges | 64 | 122 | 1,404 | rtx4090* | 36 | 17% |
| 13 | sn120 Affine | 63.7 | 153 | 269 | rtx4090* | 245 | 1% |
| 14 | sn65 True Performance | 62.7 | 87.57 | 183 | rtx4090* | 6 | 75% |
| 15 | sn61 RedTeam | 62.2 | 75.25 | 107 | rtx4090* | 133 | 1% |
| 16 | sn28 SayGM | 61.8 | 65.49 | 1,319 | rtx4090* | 63 | 23% |
| 17 | sn53 engy | 60.2 | 1,393 | 2,674 | rtx4090 | 18 | 17% |
| 18 | sn23 Trishool | 59.4 | 430 | 430 = | cpu-small | 3 | 80% |
| 19 | sn5 Hone | 58.7 | 36.76 | 37.42 | rtx4090* | 243 | 0% |
| 20 | sn81 Reliquary | 58.3 | 21.45 | 360 | rtx4090* | 52 | 55% |

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
| concentrated (30–60%) | 23 |
| dominated (60–90%) | 26 |
| captured (>90%) | 23 |

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
| 2026-10-11T19:38 | sn15 | RELEASE | sn15 released v2.4.1 |
| 2026-10-11T19:38 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: docs(verifying): the standing preview exi |
| 2026-10-11T19:38 | sn22 | SCORING_COMMIT | sn22 commit touches scoring: fix(validators): no JS rendering, 20 page |
| 2026-10-11T19:38 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Install current reward RPCs in per-ICP ro |
| 2026-10-11T19:38 | sn76 | SCORING_COMMIT | sn76 commit touches scoring: Fix miner registration-first onboarding |
| 2026-10-11T19:38 | sn76 | README_TASK_DIFF | sn76 README task/scoring sections changed |
| 2026-10-11T19:38 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: feat(cli): tasks set-cap sets or clears a |
| 2026-10-11T19:38 | sn108 | BURN_DROP | sn108 burn fell 1.000 -> 0.902 - miners can earn again |
| 2026-10-11T19:38 | sn116 | RELEASE | sn116 released producer-code-r8.1 |
| 2026-10-11T19:38 | sn117 | RELEASE | sn117 released everycli v0.2.4 |
| 2026-10-11T19:38 | sn117 | README_TASK_DIFF | sn117 README task/scoring sections changed |
| 2026-10-11T15:07 | sn116 | RELEASE | sn116 released producer-code-r7 |
| 2026-10-11T15:07 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Merge pull request #1046 from carbonphys |
| 2026-10-11T08:43 | sn22 | SCORING_COMMIT | sn22 commit touches scoring: fix(validators): restore rendered recheck |
| 2026-10-11T08:43 | sn25 | RELEASE | sn25 released v2026.10.10-1068958850 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

