# Subnet watch — dashboard

_snapshot 2026-08-01T07:17:18Z · block 8747678 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 58 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 94 | `miner_burn` < 0.99 |
| Ranked | 94 | passed every gate |
| **Positive margin** | **58** | income beats machine cost |
| New events this window | 2 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 54 | `████████████████████████████` |
| 0–0.2 | 8 | `████` |
| 0.2–0.4 | 5 | `███` |
| 0.4–0.6 | 7 | `████` |
| 0.6–0.8 | 10 | `█████` |
| 0.8–0.99 | 10 | `█████` |
| ≥0.99 dead | 34 | `██████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn23 Trishool | 85.1 | 581 | 581 = | cpu-small | 5 | 20% |
| 2 | sn107 Minos | 77.9 | 107 | 30,014 | cpu-small | 20 | 90% |
| 3 | sn98 NeverPlayAlone | 76.1 | 1,757 | 1,757 = | cpu-small | 1 | 100% |
| 4 | sn76 Phylax | 74.6 | 39.53 | 114 | cpu-small | 7 | 82% |
| 5 | sn67 Harnyx | 73.1 | 27.67 | 1,008 | cpu-small | 132 | 21% |
| 6 | sn62 Ridges | 71.2 | 1,050 | 4,836 | rtx4090* | 6 | 57% |
| 7 | sn102 ConnitoAI | 70.9 | 961 | 1,106 | rtx4090* | 4 | 29% |
| 8 | sn56 Gradients | 69.2 | 592 | 1,246 | rtx4090* | 6 | 64% |
| 9 | sn26 Perturb | 69 | 25.84 | 206 | rtx3060 | 11 | 51% |
| 10 | sn85 Vidaio | 68.3 | 441 | 526 | rtx4090* | 10 | 17% |
| 11 | sn15 ORO | 67.9 | 9.37 | 11,621 | cpu-small | 58 | 95% |
| 12 | sn124 Swarm | 66.6 | 275 | 719 | rtx4090* | 20 | 12% |
| 13 | sn38 ChronoLLM | 63.4 | 115 | 1,664 | rtx4090* | 10 | 52% |
| 14 | sn53 engy | 63.3 | 101 | 2,517 | rtx4090 | 34 | 13% |
| 15 | sn71 Leadpoet | 62.8 | 84.76 | 172 | rtx4090* | 10 | 70% |
| 16 | sn28 gm | 58.7 | 26.77 | 2,217 | rtx4090* | 13 | 63% |
| 17 | sn61 RedTeam | 58.6 | 24.08 | 113 | rtx4090* | 95 | 3% |
| 18 | sn51 lium.io | 56 | 17.53 | 7,049 | rtx4090* | 41 | 37% |
| 19 | sn9 iota | 55.2 | 8,491 | 15,199 | rtx4090* | 3 | 75% |
| 20 | sn101 Tag101 | 53.6 | 0.03 | 2.90 | cpu-small | 234 | 89% |

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
| concentrated (30–60%) | 22 |
| dominated (60–90%) | 23 |
| captured (>90%) | 24 |

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
| 2026-08-01T07:17 | sn76 | SCORING_COMMIT | sn76 commit touches scoring: Carry a track's standing forward when a p |
| 2026-08-01T07:17 | sn102 | BURN_DROP | sn102 burn fell 1.000 -> 0.254 - miners can earn again |
| 2026-08-01T04:31 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Extend validator gateway alignment wait |
| 2026-08-01T04:31 | sn89 | README_TASK_DIFF | sn89 README task/scoring sections changed |
| 2026-08-01T01:02 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Bound receipt ancestry validation and per |
| 2026-07-31T23:14 | sn102 | RELEASE | sn102 released v0.4.0 |
| 2026-07-31T23:14 | sn102 | SCORING_COMMIT | sn102 commit touches scoring: 📊 telemetry: restore round + per-miner t |
| 2026-07-31T21:50 | sn74 | RELEASE | sn74 released release-20260731-214128: chore(weights): point all emiss |
| 2026-07-31T21:50 | sn74 | SCORING_COMMIT | sn74 commit touches scoring: SparkDistill: 3x faster time-decay for me |
| 2026-07-31T21:50 | sn76 | SCORING_COMMIT | sn76 commit touches scoring: Merge pull request #16 from praxi-labs/va |
| 2026-07-31T18:52 | sn126 | SCORING_COMMIT | sn126 commit touches scoring: release: enable validator auto-update 0. |
| 2026-07-31T17:12 | sn7 | BURN_DROP | sn7 burn fell 0.995 -> 0.926 - miners can earn again |
| 2026-07-31T17:12 | sn9 | RELEASE | sn9 released v4.9.2 |
| 2026-07-31T17:12 | sn15 | RELEASE | sn15 released v1.2.4 |
| 2026-07-31T17:12 | sn66 | BURN_DROP | sn66 burn fell 1.000 -> 0.000 - miners can earn again |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

