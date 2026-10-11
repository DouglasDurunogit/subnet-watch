# Subnet watch — dashboard

_snapshot 2026-10-11T23:12:35Z · block 9263146 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 60 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 100 | `miner_burn` < 0.99 |
| Ranked | 100 | passed every gate |
| **Positive margin** | **60** | income beats machine cost |
| New events this window | 2 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 70 | `████████████████████████████` |
| 0–0.2 | 6 | `██` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 8 | `███` |
| 0.6–0.8 | 7 | `███` |
| 0.8–0.99 | 5 | `██` |
| ≥0.99 dead | 28 | `███████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn107 Minos | 82.3 | 308 | 26,164 | cpu-small | 20 | 80% |
| 2 | sn3 Teutonic | 75 | 3,333 | 3,333 = | rtx4090* | 5 | 40% |
| 3 | sn14 Cacheon | 70.1 | 770 | 6,228 | rtx4090* | 3 | 83% |
| 4 | sn101 Tag101 | 70.1 | 12.83 | 14.48 | cpu-small | 242 | 0% |
| 5 | sn80 OpenRoboto | 69.6 | 651 | 3,406 | rtx4090* | 7 | 35% |
| 6 | sn67 Harnyx | 69 | 9.32 | 965 | cpu-small | 127 | 33% |
| 7 | sn38 ChronoLLM | 68.9 | 223 | 1,016 | cpu-small | 9 | 52% |
| 8 | sn41 Almanac | 68.1 | 9.20 | 178 | cpu-small | 105 | 3% |
| 9 | sn79 MVTRX | 67.4 | 8.17 | 40.98 | cpu-small | 244 | 2% |
| 10 | sn4 Targon | 67 | 10,589 | 31,220 | rtx4090* | 5 | 70% |
| 11 | sn15 ORO | 66.7 | 6.78 | 13.95 | cpu-small | 52 | 98% |
| 12 | sn62 Ridges | 64 | 124 | 1,420 | rtx4090* | 36 | 17% |
| 13 | sn120 Affine | 63.4 | 152 | 277 | rtx4090* | 247 | 1% |
| 14 | sn28 SayGM | 63.3 | 102 | 975 | rtx4090* | 57 | 29% |
| 15 | sn65 True Performance | 62.7 | 88.57 | 185 | rtx4090* | 6 | 75% |
| 16 | sn61 RedTeam | 62.3 | 77.50 | 110 | rtx4090* | 131 | 1% |
| 17 | sn53 engy | 60.3 | 1,416 | 2,716 | rtx4090 | 18 | 17% |
| 18 | sn23 Trishool | 59.5 | 435 | 435 = | cpu-small | 3 | 80% |
| 19 | sn5 Hone | 59.1 | 37.21 | 37.72 | rtx4090* | 246 | 0% |
| 20 | sn81 Reliquary | 58.6 | 23.93 | 357 | rtx4090* | 52 | 56% |

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
| concentrated (30–60%) | 23 |
| dominated (60–90%) | 25 |
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
| 2026-10-11T23:13 | sn117 | RELEASE | sn117 released v0.2.5 |
| 2026-10-11T23:13 | sn117 | README_TASK_DIFF | sn117 README task/scoring sections changed |
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

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

