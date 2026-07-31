# Subnet watch — dashboard

_snapshot 2026-07-31T15:28:16Z · block 8742935 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 56 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 96 | `miner_burn` < 0.99 |
| Ranked | 96 | passed every gate |
| **Positive margin** | **56** | income beats machine cost |
| New events this window | 1 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 61 | `████████████████████████████` |
| 0–0.2 | 5 | `██` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 9 | `████` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 32 | `███████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn23 Trishool | 85 | 566 | 566 = | cpu-small | 5 | 20% |
| 2 | sn107 Minos | 78 | 110 | 28,560 | cpu-small | 20 | 89% |
| 3 | sn76 Phylax | 77.2 | 76.74 | 154 | cpu-small | 7 | 70% |
| 4 | sn98 NeverPlayAlone | 76 | 1,725 | 1,725 = | cpu-small | 1 | 100% |
| 5 | sn67 Harnyx | 73.7 | 32.39 | 916 | cpu-small | 118 | 19% |
| 6 | sn62 Ridges | 70.9 | 970 | 4,468 | rtx4090* | 6 | 57% |
| 7 | sn56 Gradients | 69.6 | 657 | 1,212 | rtx4090* | 6 | 64% |
| 8 | sn26 Perturb | 68.8 | 24.89 | 206 | rtx3060 | 11 | 50% |
| 9 | sn85 Vidaio | 68 | 406 | 506 | rtx4090* | 10 | 17% |
| 10 | sn101 Tag101 | 68 | 7.42 | 40.84 | cpu-small | 241 | 2% |
| 11 | sn15 ORO | 67.5 | 8.85 | 18.34 | cpu-small | 80 | 93% |
| 12 | sn124 Swarm | 66.9 | 303 | 702 | rtx4090* | 20 | 12% |
| 13 | sn126 Poker44 | 64 | 127 | 668 | rtx4090* | 12 | 30% |
| 14 | sn53 engy | 63.3 | 101 | 2,452 | rtx4090 | 34 | 13% |
| 15 | sn38 ChronoLLM | 63.2 | 109 | 1,576 | rtx4090* | 10 | 52% |
| 16 | sn71 Leadpoet | 61.4 | 55.52 | 98.06 | rtx4090* | 4 | 92% |
| 17 | sn28 gm | 59.3 | 31.03 | 2,740 | rtx4090* | 13 | 55% |
| 18 | sn61 RedTeam | 58.9 | 26.00 | 126 | rtx4090* | 88 | 4% |
| 19 | sn51 lium.io | 57.6 | 24.71 | 6,754 | rtx4090* | 40 | 45% |
| 20 | sn102 ConnitoAI | 55.8 | 9.69 | 1,482 | rtx4090* | 8 | 40% |

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
| wide (<30%) | 26 |
| concentrated (30–60%) | 24 |
| dominated (60–90%) | 19 |
| captured (>90%) | 26 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 106 |
| min_compute.yml (curated) | 9 |
| code-submission (validator runs it) | 8 |
| README keywords (GUESS) | 4 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-07-31T15:28 | sn126 | SCORING_COMMIT | sn126 commit touches scoring: docs: align miner and validator release  |
| 2026-07-31T13:05 | sn76 | SCORING_COMMIT | sn76 commit touches scoring: Hold inference keys in the proxy, enforce |
| 2026-07-31T11:05 | sn8 | BURN_DROP | sn8 burn fell 0.998 -> 0.000 - miners can earn again |
| 2026-07-31T11:05 | sn76 | SCORING_COMMIT | sn76 commit touches scoring: Evaluate two agents at a time within a tr |
| 2026-07-31T08:08 | sn80 | SCORING_COMMIT | sn80 commit touches scoring: docs: document public /api/v1/scan-reject |
| 2026-07-30T23:33 | sn8 | SCORING_COMMIT | sn8 commit touches scoring: create subaccount elimination cache on ent |
| 2026-07-30T23:33 | sn62 | RELEASE | sn62 released v0.2.3 |
| 2026-07-30T23:33 | sn115 | BURN_DROP | sn115 burn fell 1.000 -> 0.000 - miners can earn again |
| 2026-07-30T23:33 | sn124 | SCORING_COMMIT | sn124 commit touches scoring: Kill host workers when the validator pro |
| 2026-07-30T22:16 | sn14 | SCORING_COMMIT | sn14 commit touches scoring: Add object-store proposal transport and v |
| 2026-07-30T19:47 | sn28 | RELEASE | sn28 released v0.3.15 |
| 2026-07-30T17:57 | sn55 | BURN_DROP | sn55 burn fell 1.000 -> 0.022 - miners can earn again |
| 2026-07-30T17:57 | sn89 | SCORING_COMMIT | sn89 commit touches scoring: hf board: share of the MINER pool, not of |
| 2026-07-30T17:57 | sn121 | BURN_DROP | sn121 burn fell 1.000 -> 0.826 - miners can earn again |
| 2026-07-30T16:17 | sn26 | README_TASK_DIFF | sn26 README task/scoring sections changed |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

