# Subnet watch — dashboard

_snapshot 2026-08-01T04:31:01Z · block 8746849 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 57 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 93 | `miner_burn` < 0.99 |
| Ranked | 93 | passed every gate |
| **Positive margin** | **57** | income beats machine cost |
| New events this window | 2 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 55 | `████████████████████████████` |
| 0–0.2 | 6 | `███` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 7 | `████` |
| 0.6–0.8 | 11 | `██████` |
| 0.8–0.99 | 10 | `█████` |
| ≥0.99 dead | 35 | `██████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn23 Trishool | 85.2 | 587 | 587 = | cpu-small | 5 | 20% |
| 2 | sn107 Minos | 78 | 111 | 29,826 | cpu-small | 20 | 89% |
| 3 | sn76 Phylax | 76.8 | 69.37 | 140 | cpu-small | 7 | 73% |
| 4 | sn98 NeverPlayAlone | 76.1 | 1,765 | 1,765 = | cpu-small | 1 | 100% |
| 5 | sn67 Harnyx | 73.1 | 27.53 | 1,003 | cpu-small | 131 | 21% |
| 6 | sn62 Ridges | 71.2 | 1,048 | 4,827 | rtx4090* | 6 | 57% |
| 7 | sn56 Gradients | 69.3 | 594 | 1,251 | rtx4090* | 6 | 64% |
| 8 | sn26 Perturb | 69.1 | 26.58 | 210 | rtx3060 | 11 | 50% |
| 9 | sn15 ORO | 68 | 9.42 | 19.82 | cpu-small | 82 | 93% |
| 10 | sn85 Vidaio | 67.8 | 382 | 588 | rtx4090* | 10 | 19% |
| 11 | sn124 Swarm | 67 | 310 | 724 | rtx4090* | 20 | 12% |
| 12 | sn38 ChronoLLM | 63.4 | 115 | 1,664 | rtx4090* | 10 | 52% |
| 13 | sn53 engy | 63.3 | 101 | 2,520 | rtx4090 | 34 | 13% |
| 14 | sn71 Leadpoet | 62.3 | 74.26 | 145 | rtx4090* | 11 | 71% |
| 15 | sn61 RedTeam | 58.6 | 24.14 | 113 | rtx4090* | 96 | 3% |
| 16 | sn28 gm | 57.6 | 19.17 | 2,296 | rtx4090* | 13 | 63% |
| 17 | sn51 lium.io | 56.1 | 17.83 | 7,292 | rtx4090* | 41 | 35% |
| 18 | sn9 iota | 55.2 | 8,543 | 15,222 | rtx4090* | 3 | 75% |
| 19 | sn101 Tag101 | 54.6 | 0.03 | 2.88 | cpu-small | 240 | 89% |
| 20 | sn97 Albedo | 52.9 | 3,304 | 3,304 = | rtx4090* | 5 | 20% |

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
| wide (<30%) | 22 |
| concentrated (30–60%) | 22 |
| dominated (60–90%) | 24 |
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
| 2026-07-31T17:12 | sn101 | SCORING_COMMIT | sn101 commit touches scoring: Allocate 90% of validator weight to burn |
| 2026-07-31T17:12 | sn102 | RELEASE | sn102 released v0.3.4 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

