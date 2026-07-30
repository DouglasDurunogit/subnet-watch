# Subnet watch — dashboard

_snapshot 2026-07-30T12:01:57Z · block 8734712 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 54 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 95 | `miner_burn` < 0.99 |
| Ranked | 95 | passed every gate |
| **Positive margin** | **54** | income beats machine cost |
| New events this window | 3 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 60 | `████████████████████████████` |
| 0–0.2 | 6 | `███` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 6 | `███` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 10 | `█████` |
| ≥0.99 dead | 33 | `███████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn23 Trishool | 85.4 | 620 | 620 = | cpu-small | 5 | 20% |
| 2 | sn76 Phylax | 81.1 | 208 | 347 | cpu-small | 4 | 60% |
| 3 | sn107 Minos | 77.5 | 98.42 | 30,625 | cpu-small | 20 | 90% |
| 4 | sn98 NeverPlayAlone | 76.1 | 1,749 | 1,749 = | cpu-small | 1 | 100% |
| 5 | sn67 Harnyx | 71.4 | 17.71 | 1,098 | cpu-small | 94 | 23% |
| 6 | sn102 ConnitoAI | 70.5 | 864 | 971 | rtx4090* | 6 | 26% |
| 7 | sn101 Tag101 | 69.7 | 11.93 | 15.38 | cpu-small | 248 | 1% |
| 8 | sn56 Gradients | 69.2 | 582 | 1,331 | rtx4090* | 6 | 63% |
| 9 | sn15 ORO | 68.8 | 11.21 | 20.72 | cpu-small | 81 | 92% |
| 10 | sn124 Swarm | 67.5 | 364 | 740 | rtx4090* | 16 | 13% |
| 11 | sn85 Vidaio | 64.5 | 142 | 506 | rtx4090* | 10 | 16% |
| 12 | sn28 gm | 63.9 | 123 | 1,950 | rtx4090* | 8 | 63% |
| 13 | sn53 engy | 63 | 91.06 | 2,094 | rtx4090 | 34 | 13% |
| 14 | sn71 Leadpoet | 62.3 | 72.75 | 127 | rtx4090* | 4 | 91% |
| 15 | sn38 ChronoLLM | 61.4 | 67.14 | 653 | rtx4090* | 10 | 52% |
| 16 | sn61 RedTeam | 58.4 | 22.53 | 138 | rtx4090* | 85 | 5% |
| 17 | sn26 Perturb | 55.3 | 1.44 | 5.67 | rtx3060 | 52 | 50% |
| 18 | sn9 iota | 54.1 | 5,354 | 9,744 | rtx4090* | 3 | 50% |
| 19 | sn97 Albedo | 53 | 3,331 | 3,331 = | rtx4090* | 5 | 20% |
| 20 | sn51 lium.io | 52.2 | 8.61 | 2,742 | rtx4090* | 38 | 70% |

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
| wide (<30%) | 27 |
| concentrated (30–60%) | 20 |
| dominated (60–90%) | 19 |
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
| 2026-07-30T12:02 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-07-30T12:02 | sn92 | BURN_DROP | sn92 burn fell 1.000 -> 0.000 - miners can earn again |
| 2026-07-30T12:02 | sn97 | SCORING_COMMIT | sn97 commit touches scoring: update: Updated evaluator & judge prompts |
| 2026-07-30T09:58 | sn28 | RELEASE | sn28 released v0.3.14 |
| 2026-07-30T09:58 | sn38 | SCORING_COMMIT | sn38 commit touches scoring: Add custom architecture registry for mine |
| 2026-07-30T09:58 | sn43 | BURN_DROP | sn43 burn fell 1.000 -> 0.800 - miners can earn again |
| 2026-07-30T09:58 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-2340, publish structured zero-incenti |
| 2026-07-30T09:58 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Keep validator epoch authority fresh duri |
| 2026-07-30T07:10 | sn5 | BURN_DROP | sn5 burn fell 1.000 -> 0.846 - miners can earn again |
| 2026-07-30T07:10 | sn15 | RELEASE | sn15 released v1.2.3 |
| 2026-07-30T07:10 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Parallelize safe validator restart prepar |
| 2026-07-30T07:10 | sn76 | SCORING_COMMIT | sn76 commit touches scoring: Evaluate the smaller tracks before skills |
| 2026-07-30T07:10 | sn80 | README_TASK_DIFF | sn80 README task/scoring sections changed |
| 2026-07-30T07:10 | sn100 | BURN_DROP | sn100 burn fell 1.000 -> 0.579 - miners can earn again |
| 2026-07-30T07:10 | sn107 | SCORING_COMMIT | sn107 commit touches scoring: Fix stale reward split: winner 90% / bur |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

