# Subnet watch — dashboard

_snapshot 2026-08-01T16:28:44Z · block 8750434 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 59 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 95 | `miner_burn` < 0.99 |
| Ranked | 95 | passed every gate |
| **Positive margin** | **59** | income beats machine cost |
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
| 0.4–0.6 | 8 | `████` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 10 | `█████` |
| ≥0.99 dead | 33 | `████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn23 Trishool | 85.1 | 569 | 569 = | cpu-small | 5 | 20% |
| 2 | sn107 Minos | 77.1 | 93.11 | 27,917 | cpu-small | 20 | 90% |
| 3 | sn76 Phylax | 77 | 73.22 | 147 | cpu-small | 7 | 70% |
| 4 | sn98 NeverPlayAlone | 76 | 1,711 | 1,711 = | cpu-small | 1 | 100% |
| 5 | sn67 Harnyx | 72.8 | 25.46 | 930 | cpu-small | 132 | 21% |
| 6 | sn62 Ridges | 71.2 | 1,064 | 4,897 | rtx4090* | 6 | 57% |
| 7 | sn102 ConnitoAI | 70.6 | 885 | 1,050 | rtx4090* | 5 | 27% |
| 8 | sn56 Gradients | 69.2 | 579 | 1,219 | rtx4090* | 6 | 64% |
| 9 | sn26 Perturb | 68.9 | 25.03 | 197 | rtx3060 | 11 | 50% |
| 10 | sn85 Vidaio | 68.6 | 486 | 487 | rtx4090* | 10 | 16% |
| 11 | sn15 ORO | 67.5 | 9.12 | 19.05 | cpu-small | 62 | 94% |
| 12 | sn74 Gittensor | 66.4 | 254 | 1,282 | rtx4090* | 6 | 52% |
| 13 | sn124 Swarm | 66 | 233 | 681 | rtx4090* | 20 | 12% |
| 14 | sn38 ChronoLLM | 63.3 | 111 | 1,610 | rtx4090* | 10 | 52% |
| 15 | sn53 engy | 63.1 | 93.05 | 2,338 | rtx4090 | 34 | 13% |
| 16 | sn71 Leadpoet | 62.7 | 82.53 | 167 | rtx4090* | 10 | 70% |
| 17 | sn28 gm | 59.5 | 33.23 | 2,704 | rtx4090* | 14 | 49% |
| 18 | sn101 Tag101 | 59.2 | 0.13 | 1.21 | cpu-small | 245 | 89% |
| 19 | sn61 RedTeam | 58.5 | 22.96 | 107 | rtx4090* | 94 | 3% |
| 20 | sn51 lium.io | 55.4 | 15.21 | 6,639 | rtx4090* | 40 | 41% |

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
| 2026-08-01T01:02 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Bound receipt ancestry validation and per |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

