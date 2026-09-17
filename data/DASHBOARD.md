# Subnet watch — dashboard

_snapshot 2026-09-17T11:36:28Z · block 9087118 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 55 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 95 | `miner_burn` < 0.99 |
| Ranked | 95 | passed every gate |
| **Positive margin** | **55** | income beats machine cost |
| New events this window | 6 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 64 | `████████████████████████████` |
| 0–0.2 | 9 | `████` |
| 0.2–0.4 | 7 | `███` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 6 | `███` |
| 0.8–0.99 | 5 | `██` |
| ≥0.99 dead | 33 | `██████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn92 MicroTensor | 79 | 124 | 279 | cpu-small | 8 | 43% |
| 2 | sn91 cascade | 72.6 | 628 | 2,514 | cpu-small | 5 | 52% |
| 3 | sn102 ConnitoAI | 68.8 | 520 | 1,278 | rtx4090* | 7 | 28% |
| 4 | sn107 Minos | 68.6 | 321 | 27,246 | cpu-small | 20 | 80% |
| 5 | sn67 Harnyx | 68.4 | 8.33 | 805 | cpu-small | 139 | 28% |
| 6 | sn38 ChronoLLM | 65.6 | 89.03 | 789 | cpu-small | 10 | 52% |
| 7 | sn111 Claims | 65 | 182 | 2,606 | rtx4090* | 5 | 79% |
| 8 | sn61 RedTeam | 62.8 | 88.13 | 135 | rtx4090* | 111 | 1% |
| 9 | sn55 NIOME | 61.8 | 64.04 | 534 | rtx4090* | 11 | 29% |
| 10 | sn28 SayGM | 60.9 | 49.64 | 2,515 | rtx4090* | 47 | 17% |
| 11 | sn62 Ridges | 60.9 | 48.36 | 1,701 | rtx4090* | 19 | 26% |
| 12 | sn81 Reliquary | 60.9 | 48.33 | 109 | rtx4090* | 41 | 45% |
| 13 | sn23 Trishool | 60.5 | 585 | 585 = | cpu-small | 2 | 80% |
| 14 | sn15 ORO | 60.3 | 3.71 | 17,996 | cpu-small | 21 | 100% |
| 15 | sn51 lium.io | 58 | 28.21 | 1,572 | rtx4090* | 69 | 82% |
| 16 | sn80 OpenRoboto | 56.6 | 474 | 1,679 | rtx4090* | 5 | 43% |
| 17 | sn9 iota | 56.1 | 12,413 | 12,413 = | rtx4090* | 3 | 68% |
| 18 | sn56 Gradients | 56 | 392 | 4,870 | rtx4090* | 11 | 46% |
| 19 | sn124 Swarm | 54.4 | 254 | 822 | rtx4090* | 25 | 11% |
| 20 | sn96 Verathos | 53.9 | 20.09 | 135 | rtx4090 | 82 | 33% |

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
| concentrated (30–60%) | 23 |
| dominated (60–90%) | 19 |
| captured (>90%) | 24 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 96 |
| min_compute.yml (curated) | 11 |
| code-submission (validator runs it) | 10 |
| README keywords (GUESS) | 10 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-09-17T11:36 | sn15 | BURN_DROP | sn15 burn fell 0.997 -> 0.000 - miners can earn again |
| 2026-09-17T11:36 | sn51 | RELEASE | sn51 released executor-v1.130 |
| 2026-09-17T11:36 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-3519 - [P2] validator: a node whose s |
| 2026-09-17T11:36 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Merge pull request #153 from Umi-BitSign/ |
| 2026-09-17T11:36 | sn92 | RELEASE | sn92 released v0.4.9 |
| 2026-09-17T11:36 | sn97 | SCORING_COMMIT | sn97 commit touches scoring: feat: add extra attempts, so miners which |
| 2026-09-17T06:06 | sn10 | BURN_DROP | sn10 burn fell 1.000 -> 0.811 - miners can earn again |
| 2026-09-17T06:06 | sn15 | RELEASE | sn15 released v2.0.20 |
| 2026-09-17T06:06 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: Stop generated runs when miner inference  |
| 2026-09-17T06:06 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-3264 - [P2] validator names a GPU ben |
| 2026-09-17T06:06 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Verify retained clip objects before retry |
| 2026-09-17T06:06 | sn92 | RELEASE | sn92 released v0.4.7 |
| 2026-09-17T00:48 | sn40 | SCORING_COMMIT | sn40 commit touches scoring: Docs: round-7 rules, miner CLI flow, audi |
| 2026-09-17T00:48 | sn40 | README_TASK_DIFF | sn40 README task/scoring sections changed |
| 2026-09-17T00:48 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Merge pull request #135 from Umi-BitSign/ |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

