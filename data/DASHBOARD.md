# Subnet watch — dashboard

_snapshot 2026-10-12T09:48:31Z · block 9266325 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 59 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 102 | `miner_burn` < 0.99 |
| Ranked | 102 | passed every gate |
| **Positive margin** | **59** | income beats machine cost |
| New events this window | 9 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 71 | `████████████████████████████` |
| 0–0.2 | 6 | `██` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 7 | `███` |
| 0.6–0.8 | 8 | `███` |
| 0.8–0.99 | 6 | `██` |
| ≥0.99 dead | 26 | `██████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn107 Minos | 82.3 | 304 | 25,347 | cpu-small | 20 | 80% |
| 2 | sn3 Teutonic | 75 | 3,329 | 3,329 = | rtx4090* | 5 | 40% |
| 3 | sn101 Tag101 | 69.9 | 12.62 | 13.96 | cpu-small | 241 | 0% |
| 4 | sn38 ChronoLLM | 68.9 | 222 | 1,010 | cpu-small | 9 | 52% |
| 5 | sn67 Harnyx | 68.9 | 9.42 | 933 | cpu-small | 118 | 32% |
| 6 | sn41 Almanac | 68.8 | 10.73 | 176 | cpu-small | 106 | 4% |
| 7 | sn79 MVTRX | 67.1 | 7.91 | 35.82 | cpu-small | 246 | 1% |
| 8 | sn4 Targon | 67 | 10,515 | 31,001 | rtx4090* | 5 | 70% |
| 9 | sn15 ORO | 65.4 | 5.81 | 12.01 | cpu-small | 57 | 98% |
| 10 | sn62 Ridges | 64.2 | 131 | 1,414 | rtx4090* | 36 | 17% |
| 11 | sn120 Affine | 63 | 147 | 242 | rtx4090* | 251 | 1% |
| 12 | sn65 True Performance | 62.7 | 89.08 | 186 | rtx4090* | 6 | 75% |
| 13 | sn61 RedTeam | 62.5 | 82.53 | 113 | rtx4090* | 121 | 1% |
| 14 | sn28 SayGM | 60.6 | 46.81 | 1,263 | rtx4090* | 71 | 26% |
| 15 | sn80 OpenRoboto | 59.8 | 1,214 | 4,133 | rtx4090* | 10 | 35% |
| 16 | sn53 engy | 59.7 | 1,205 | 2,657 | rtx4090 | 18 | 17% |
| 17 | sn23 Trishool | 59.5 | 431 | 431 = | cpu-small | 3 | 80% |
| 18 | sn91 cascade | 59.3 | 415 | 2,218 | cpu-small | 5 | 52% |
| 19 | sn5 Hone | 58.2 | 36.89 | 37.39 | rtx4090* | 244 | 0% |
| 20 | sn111 Claims | 57.9 | 20.83 | 246 | rtx4090* | 6 | 90% |

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
| concentrated (30–60%) | 25 |
| dominated (60–90%) | 27 |
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
| 2026-10-12T09:49 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Admit one pinned native gap edge so the v |
| 2026-10-12T09:49 | sn51 | RELEASE | sn51 released executor-v1.139 |
| 2026-10-12T09:49 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-3998 - [P2] Signed node heartbeat; va |
| 2026-10-12T09:49 | sn58 | SCORING_COMMIT | sn58 commit touches scoring: feat(vector): a validator on another host |
| 2026-10-12T09:49 | sn94 | SCORING_COMMIT | sn94 commit touches scoring: Merge pull request #254 from skyrocket202 |
| 2026-10-12T09:49 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Merge pull request #1143 from carbonphys |
| 2026-10-12T09:49 | sn117 | RELEASE | sn117 released everycli v0.3.3 |
| 2026-10-12T09:49 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: Plot fixed previously trained tasks in T |
| 2026-10-12T09:49 | sn122 | BURN_DROP | sn122 burn fell 1.000 -> 0.100 - miners can earn again |
| 2026-10-12T02:34 | sn30 | BURN_DROP | sn30 burn fell 0.997 -> 0.984 - miners can earn again |
| 2026-10-12T02:34 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Verify miner credit diagnostics through P |
| 2026-10-12T02:34 | sn117 | RELEASE | sn117 released everycli v0.3.1 |
| 2026-10-12T02:34 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: Rotate overused math tasks through exist |
| 2026-10-11T23:13 | sn117 | RELEASE | sn117 released v0.2.5 |
| 2026-10-11T23:13 | sn117 | README_TASK_DIFF | sn117 README task/scoring sections changed |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

