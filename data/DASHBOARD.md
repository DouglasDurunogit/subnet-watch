# Subnet watch — dashboard

_snapshot 2026-08-01T09:32:02Z · block 8748352 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 56 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 94 | `miner_burn` < 0.99 |
| Ranked | 94 | passed every gate |
| **Positive margin** | **56** | income beats machine cost |
| New events this window | 5 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 54 | `████████████████████████████` |
| 0–0.2 | 9 | `█████` |
| 0.2–0.4 | 5 | `███` |
| 0.4–0.6 | 7 | `████` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 11 | `██████` |
| ≥0.99 dead | 34 | `██████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn23 Trishool | 85.1 | 576 | 576 = | cpu-small | 5 | 20% |
| 2 | sn107 Minos | 77.2 | 91.39 | 29,795 | cpu-small | 20 | 90% |
| 3 | sn76 Phylax | 76.5 | 64.64 | 146 | cpu-small | 7 | 71% |
| 4 | sn67 Harnyx | 73 | 27.38 | 998 | cpu-small | 132 | 21% |
| 5 | sn62 Ridges | 71.1 | 1,043 | 4,801 | rtx4090* | 6 | 57% |
| 6 | sn102 ConnitoAI | 71 | 1,001 | 1,153 | rtx4090* | 4 | 29% |
| 7 | sn56 Gradients | 69.2 | 587 | 1,236 | rtx4090* | 6 | 64% |
| 8 | sn26 Perturb | 68.9 | 25.52 | 954 | rtx3060 | 11 | 51% |
| 9 | sn85 Vidaio | 68.2 | 437 | 521 | rtx4090* | 10 | 17% |
| 10 | sn15 ORO | 68 | 9.68 | 11,394 | cpu-small | 61 | 95% |
| 11 | sn124 Swarm | 66.2 | 245 | 718 | rtx4090* | 20 | 12% |
| 12 | sn38 ChronoLLM | 63.4 | 114 | 1,651 | rtx4090* | 10 | 52% |
| 13 | sn53 engy | 63.1 | 93.32 | 2,344 | rtx4090 | 34 | 13% |
| 14 | sn71 Leadpoet | 62.7 | 84.16 | 171 | rtx4090* | 10 | 70% |
| 15 | sn28 gm | 58.7 | 26.17 | 2,316 | rtx4090* | 13 | 49% |
| 16 | sn61 RedTeam | 58.7 | 24.30 | 113 | rtx4090* | 95 | 3% |
| 17 | sn51 lium.io | 55.5 | 15.80 | 6,900 | rtx4090* | 41 | 39% |
| 18 | sn9 iota | 55.2 | 8,379 | 15,174 | rtx4090* | 3 | 75% |
| 19 | sn101 Tag101 | 53.8 | 0.01 | 2.83 | cpu-small | 233 | 89% |
| 20 | sn97 Albedo | 52.9 | 3,228 | 3,228 = | rtx4090* | 5 | 20% |

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
| dominated (60–90%) | 22 |
| captured (>90%) | 25 |

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
| 2026-08-01T09:32 | sn61 | RELEASE | sn61 released 4.8.2 |
| 2026-08-01T09:32 | sn61 | SCORING_COMMIT | sn61 commit touches scoring: fix: set default value for user_id in _co |
| 2026-08-01T09:32 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-08-01T09:32 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Validate concurrent restart state continu |
| 2026-08-01T09:32 | sn126 | SCORING_COMMIT | sn126 commit touches scoring: docs: introduce Poker44 evaluation netwo |
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

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

