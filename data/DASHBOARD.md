# Subnet watch — dashboard

_snapshot 2026-08-01T17:45:22Z · block 8750818 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 60 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 96 | `miner_burn` < 0.99 |
| Ranked | 96 | passed every gate |
| **Positive margin** | **60** | income beats machine cost |
| New events this window | 1 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 57 | `████████████████████████████` |
| 0–0.2 | 8 | `████` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 8 | `████` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 10 | `█████` |
| ≥0.99 dead | 32 | `████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn23 Trishool | 85 | 566 | 566 = | cpu-small | 5 | 20% |
| 2 | sn107 Minos | 77.3 | 93.44 | 27,044 | cpu-small | 20 | 90% |
| 3 | sn76 Phylax | 76.9 | 71.92 | 145 | cpu-small | 7 | 70% |
| 4 | sn98 NeverPlayAlone | 76 | 1,703 | 1,703 = | cpu-small | 1 | 100% |
| 5 | sn67 Harnyx | 72.8 | 25.49 | 931 | cpu-small | 132 | 21% |
| 6 | sn62 Ridges | 71.2 | 1,044 | 4,806 | rtx4090* | 6 | 57% |
| 7 | sn102 ConnitoAI | 70.6 | 880 | 1,045 | rtx4090* | 5 | 27% |
| 8 | sn56 Gradients | 69.2 | 579 | 1,220 | rtx4090* | 6 | 64% |
| 9 | sn26 Perturb | 68.8 | 24.89 | 195 | rtx3060 | 11 | 50% |
| 10 | sn85 Vidaio | 67.4 | 339 | 586 | rtx4090* | 10 | 19% |
| 11 | sn15 ORO | 67.4 | 9.63 | 19.02 | cpu-small | 63 | 94% |
| 12 | sn74 Gittensor | 66.2 | 242 | 1,283 | rtx4090* | 6 | 52% |
| 13 | sn124 Swarm | 66 | 232 | 679 | rtx4090* | 20 | 12% |
| 14 | sn38 ChronoLLM | 63.3 | 111 | 1,602 | rtx4090* | 10 | 52% |
| 15 | sn53 engy | 63.1 | 93.19 | 2,341 | rtx4090 | 34 | 13% |
| 16 | sn71 Leadpoet | 62.7 | 82.31 | 167 | rtx4090* | 10 | 70% |
| 17 | sn28 gm | 60.1 | 39.01 | 2,535 | rtx4090* | 15 | 56% |
| 18 | sn61 RedTeam | 58.4 | 22.23 | 89.18 | rtx4090* | 97 | 3% |
| 19 | sn101 Tag101 | 58.4 | 0.09 | 1.24 | cpu-small | 242 | 89% |
| 20 | sn9 iota | 55.1 | 8,168 | 14,967 | rtx4090* | 3 | 75% |

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

