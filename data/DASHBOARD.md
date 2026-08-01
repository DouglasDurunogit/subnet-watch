# Subnet watch — dashboard

_snapshot 2026-08-01T14:05:49Z · block 8749721 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 60 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 95 | `miner_burn` < 0.99 |
| Ranked | 95 | passed every gate |
| **Positive margin** | **60** | income beats machine cost |
| New events this window | 1 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 56 | `████████████████████████████` |
| 0–0.2 | 8 | `████` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 7 | `████` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 11 | `██████` |
| ≥0.99 dead | 33 | `████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn23 Trishool | 85.1 | 573 | 573 = | cpu-small | 5 | 20% |
| 2 | sn107 Minos | 77.4 | 95.63 | 28,361 | cpu-small | 20 | 90% |
| 3 | sn76 Phylax | 76.9 | 70.50 | 142 | cpu-small | 7 | 70% |
| 4 | sn98 NeverPlayAlone | 76 | 1,721 | 1,721 = | cpu-small | 1 | 100% |
| 5 | sn67 Harnyx | 73 | 26.88 | 980 | cpu-small | 132 | 21% |
| 6 | sn62 Ridges | 71.3 | 1,075 | 4,948 | rtx4090* | 6 | 57% |
| 7 | sn102 ConnitoAI | 70.5 | 854 | 1,059 | rtx4090* | 6 | 27% |
| 8 | sn56 Gradients | 69.2 | 582 | 1,226 | rtx4090* | 6 | 64% |
| 9 | sn26 Perturb | 69.1 | 26.38 | 945 | rtx3060 | 11 | 51% |
| 10 | sn15 ORO | 68.1 | 9.63 | 10,857 | cpu-small | 62 | 94% |
| 11 | sn85 Vidaio | 67.4 | 345 | 602 | rtx4090* | 10 | 19% |
| 12 | sn124 Swarm | 66 | 234 | 686 | rtx4090* | 20 | 12% |
| 13 | sn38 ChronoLLM | 63.3 | 113 | 1,632 | rtx4090* | 10 | 52% |
| 14 | sn53 engy | 63.1 | 94.20 | 2,364 | rtx4090 | 34 | 13% |
| 15 | sn71 Leadpoet | 62.8 | 86.41 | 175 | rtx4090* | 10 | 70% |
| 16 | sn101 Tag101 | 59 | 0.21 | 1.07 | cpu-small | 238 | 90% |
| 17 | sn61 RedTeam | 58.5 | 23.09 | 109 | rtx4090* | 95 | 3% |
| 18 | sn28 gm | 57.4 | 17.90 | 2,617 | rtx4090* | 14 | 47% |
| 19 | sn51 lium.io | 56.3 | 18.61 | 6,959 | rtx4090* | 41 | 38% |
| 20 | sn9 iota | 55.1 | 8,305 | 15,152 | rtx4090* | 3 | 75% |

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
| concentrated (30–60%) | 21 |
| dominated (60–90%) | 24 |
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
| 2026-08-01T14:06 | sn124 | SCORING_COMMIT | sn124 commit touches scoring: Fly next-epoch seeds for pre-evaluation  |
| 2026-08-01T12:13 | sn103 | RELEASE | sn103 released v2007 |
| 2026-08-01T12:13 | sn103 | SCORING_COMMIT | sn103 commit touches scoring: validator: release v2007 |
| 2026-08-01T11:07 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Bind v8 artifact verification into protec |
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

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

