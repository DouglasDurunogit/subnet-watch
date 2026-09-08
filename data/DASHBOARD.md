# Subnet watch — dashboard

_snapshot 2026-09-08T17:33:49Z · block 9024277 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 59 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 93 | `miner_burn` < 0.99 |
| Ranked | 94 | passed every gate |
| **Positive margin** | **59** | income beats machine cost |
| New events this window | 7 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 60 | `████████████████████████████` |
| 0–0.2 | 8 | `████` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 3 | `█` |
| 0.6–0.8 | 11 | `█████` |
| 0.8–0.99 | 5 | `██` |
| ≥0.99 dead | 35 | `████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn114 SOMA | 87.4 | 1,033 | 8,271 | cpu-small | 4 | 80% |
| 2 | sn92 MicroTensor | 79.2 | 129 | 390 | cpu-small | 9 | 50% |
| 3 | sn107 Minos | 77.5 | 104 | 6,508 | cpu-small | 21 | 81% |
| 4 | sn3 Teutonic | 76.2 | 4,678 | 4,678 = | rtx4090* | 5 | 20% |
| 5 | sn102 ConnitoAI | 71.8 | 1,263 | 1,726 | rtx4090* | 5 | 30% |
| 6 | sn67 Harnyx | 70.9 | 15.60 | 1,375 | cpu-small | 124 | 37% |
| 7 | sn96 Verathos | 70.8 | 41.09 | 418 | rtx4090 | 76 | 30% |
| 8 | sn91 cascade | 70.2 | 788 | 3,176 | rtx4090* | 5 | 52% |
| 9 | sn14 Cacheon | 69.8 | 696 | 1,289 | rtx4090* | 12 | 18% |
| 10 | sn11 TrajectoryRL | 68.8 | 6,964 | 6,964 = | cpu-small | 1 | 100% |
| 11 | sn62 Ridges | 68.2 | 434 | 1,290 | rtx4090* | 13 | 26% |
| 12 | sn80 OpenRoboto | 67.7 | 373 | 1,327 | rtx4090* | 5 | 43% |
| 13 | sn38 ChronoLLM | 67.1 | 137 | 2,899 | cpu-small | 10 | 52% |
| 14 | sn124 Swarm | 66.8 | 301 | 927 | rtx4090* | 25 | 11% |
| 15 | sn111 Claims | 66.5 | 281 | 3,419 | rtx4090* | 5 | 76% |
| 16 | sn56 Gradients | 63.4 | 104 | 1,905 | rtx4090* | 11 | 47% |
| 17 | sn121 sundae_bar | 63.3 | 1,333 | 1,333 = | cpu-small | 2 | 61% |
| 18 | sn65 True Performance | 62.7 | 93.94 | 196 | rtx4090* | 6 | 75% |
| 19 | sn41 Almanac | 60.8 | 43.34 | 120 | cpu-small | 84 | 3% |
| 20 | sn28 SayGM | 57.9 | 21.40 | 10,782 | rtx4090* | 60 | 66% |

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
| concentrated (30–60%) | 21 |
| dominated (60–90%) | 23 |
| captured (>90%) | 20 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 99 |
| min_compute.yml (curated) | 11 |
| code-submission (validator runs it) | 10 |
| README keywords (GUESS) | 7 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-09-08T17:34 | sn25 | RELEASE | sn25 released v2026.9.8-1040779940 |
| 2026-09-08T17:34 | sn34 | BURN_DROP | sn34 burn fell 1.000 -> 0.799 - miners can earn again |
| 2026-09-08T17:34 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Merge remote-tracking branch 'origin/main |
| 2026-09-08T17:34 | sn74 | RELEASE | sn74 released release-20260908-144557 |
| 2026-09-08T17:34 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: tracks: support is the one live track; ca |
| 2026-09-08T17:34 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: Sync validator + eval design (2026-09-07 |
| 2026-09-08T17:34 | sn121 | BURN_DROP | sn121 burn fell 1.000 -> 0.610 - miners can earn again |
| 2026-09-08T13:32 | sn9 | RELEASE | sn9 released v4.12.14 |
| 2026-09-08T13:32 | sn10 | SCORING_COMMIT | sn10 commit touches scoring: Merge pull request #145 from Pareton-ai/b |
| 2026-09-08T13:32 | sn34 | SCORING_COMMIT | sn34 commit touches scoring: Bump version to 5.0.2 so validators autou |
| 2026-09-08T13:32 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Verify approved prior testnet release boo |
| 2026-09-08T13:32 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: fix(eval): install host cc for triton ji |
| 2026-09-08T09:02 | sn66 | SCORING_COMMIT | sn66 commit touches scoring: Release 259 reviewed targets with immutab |
| 2026-09-08T09:02 | sn66 | README_TASK_DIFF | sn66 README task/scoring sections changed |
| 2026-09-08T09:02 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Parse Arena drain quiescence in validator |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

