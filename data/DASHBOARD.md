# Subnet watch — dashboard

_snapshot 2026-07-30T14:28:11Z · block 8735444 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 57 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 96 | `miner_burn` < 0.99 |
| Ranked | 96 | passed every gate |
| **Positive margin** | **57** | income beats machine cost |
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
| 0.4–0.6 | 8 | `████` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 9 | `████` |
| ≥0.99 dead | 32 | `███████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn23 Trishool | 85.4 | 615 | 615 = | cpu-small | 5 | 20% |
| 2 | sn107 Minos | 77.2 | 95.32 | 29,579 | cpu-small | 20 | 90% |
| 3 | sn76 Phylax | 76.8 | 70.08 | 131 | cpu-small | 7 | 72% |
| 4 | sn98 NeverPlayAlone | 76.1 | 1,741 | 1,741 = | cpu-small | 1 | 100% |
| 5 | sn67 Harnyx | 71.4 | 17.87 | 1,107 | cpu-small | 94 | 23% |
| 6 | sn102 ConnitoAI | 70.6 | 883 | 987 | rtx4090* | 5 | 26% |
| 7 | sn101 Tag101 | 69.7 | 11.30 | 15.79 | cpu-small | 246 | 1% |
| 8 | sn56 Gradients | 69.6 | 663 | 1,318 | rtx4090* | 6 | 63% |
| 9 | sn15 ORO | 68.6 | 11.27 | 20.66 | cpu-small | 82 | 92% |
| 10 | sn124 Swarm | 67.6 | 366 | 743 | rtx4090* | 16 | 13% |
| 11 | sn85 Vidaio | 63.2 | 95.55 | 487 | rtx4090* | 10 | 18% |
| 12 | sn53 engy | 63.1 | 92.75 | 2,130 | rtx4090 | 34 | 13% |
| 13 | sn38 ChronoLLM | 63 | 102 | 1,479 | rtx4090* | 10 | 52% |
| 14 | sn71 Leadpoet | 62.5 | 77.79 | 135 | rtx4090* | 4 | 91% |
| 15 | sn28 gm | 60.6 | 45.97 | 2,210 | rtx4090* | 10 | 60% |
| 16 | sn61 RedTeam | 58.5 | 22.86 | 140 | rtx4090* | 85 | 5% |
| 17 | sn51 lium.io | 55.5 | 15.48 | 2,881 | rtx4090* | 39 | 67% |
| 18 | sn26 Perturb | 55.3 | 1.43 | 5.65 | rtx3060 | 52 | 50% |
| 19 | sn9 iota | 54.1 | 5,322 | 9,725 | rtx4090* | 3 | 50% |
| 20 | sn97 Albedo | 53 | 3,352 | 3,352 = | rtx4090* | 5 | 20% |

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
| concentrated (30–60%) | 22 |
| dominated (60–90%) | 18 |
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
| 2026-07-30T14:28 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: feat: DAH-2251 — pay referral incentive f |
| 2026-07-30T14:28 | sn74 | RELEASE | sn74 released release-20260730-140609 |
| 2026-07-30T14:28 | sn100 | BURN_DROP | sn100 burn fell 1.000 -> 0.503 - miners can earn again |
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

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

