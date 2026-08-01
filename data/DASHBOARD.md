# Subnet watch — dashboard

_snapshot 2026-08-01T18:44:51Z · block 8751115 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 59 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 96 | `miner_burn` < 0.99 |
| Ranked | 96 | passed every gate |
| **Positive margin** | **59** | income beats machine cost |
| New events this window | 1 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 58 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 8 | `████` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 11 | `█████` |
| ≥0.99 dead | 32 | `███████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn23 Trishool | 85 | 566 | 566 = | cpu-small | 5 | 20% |
| 2 | sn107 Minos | 77.2 | 91.55 | 26,855 | cpu-small | 20 | 90% |
| 3 | sn76 Phylax | 77.1 | 74.05 | 149 | cpu-small | 7 | 70% |
| 4 | sn98 NeverPlayAlone | 76 | 1,696 | 1,696 = | cpu-small | 1 | 100% |
| 5 | sn67 Harnyx | 72.9 | 26.21 | 956 | cpu-small | 132 | 21% |
| 6 | sn62 Ridges | 71.2 | 1,049 | 4,829 | rtx4090* | 6 | 57% |
| 7 | sn102 ConnitoAI | 70.7 | 916 | 954 | rtx4090* | 5 | 25% |
| 8 | sn56 Gradients | 69.2 | 577 | 1,215 | rtx4090* | 6 | 64% |
| 9 | sn26 Perturb | 68.8 | 24.71 | 194 | rtx3060 | 11 | 50% |
| 10 | sn85 Vidaio | 68.5 | 474 | 487 | rtx4090* | 10 | 16% |
| 11 | sn15 ORO | 67.4 | 9.23 | 18.93 | cpu-small | 65 | 94% |
| 12 | sn124 Swarm | 66 | 232 | 679 | rtx4090* | 20 | 12% |
| 13 | sn38 ChronoLLM | 63.2 | 108 | 1,570 | rtx4090* | 10 | 52% |
| 14 | sn53 engy | 62.9 | 87.73 | 2,214 | rtx4090 | 34 | 13% |
| 15 | sn71 Leadpoet | 62.7 | 82.17 | 167 | rtx4090* | 10 | 70% |
| 16 | sn61 RedTeam | 58.3 | 21.69 | 87.51 | rtx4090* | 97 | 3% |
| 17 | sn28 gm | 57.4 | 17.91 | 2,773 | rtx4090* | 15 | 52% |
| 18 | sn101 Tag101 | 57.4 | 0.08 | 1.31 | cpu-small | 241 | 90% |
| 19 | sn9 iota | 55.1 | 8,119 | 14,888 | rtx4090* | 3 | 75% |
| 20 | sn51 lium.io | 53.6 | 10.87 | 6,737 | rtx4090* | 41 | 41% |

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
| dominated (60–90%) | 23 |
| captured (>90%) | 27 |

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
| 2026-08-01T17:45 | sn99 | BURN_DROP | sn99 burn fell 1.000 -> 0.000 - miners can earn again |
| 2026-08-01T16:29 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: Wire silver adjudication into validator  |
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

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

