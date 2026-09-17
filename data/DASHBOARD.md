# Subnet watch — dashboard

_snapshot 2026-09-17T06:05:45Z · block 9085473 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 53 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 94 | `miner_burn` < 0.99 |
| Ranked | 94 | passed every gate |
| **Positive margin** | **53** | income beats machine cost |
| New events this window | 6 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 64 | `████████████████████████████` |
| 0–0.2 | 8 | `████` |
| 0.2–0.4 | 7 | `███` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 6 | `███` |
| 0.8–0.99 | 5 | `██` |
| ≥0.99 dead | 34 | `███████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn11 TrajectoryRL | 80 | 5,699 | 5,699 = | cpu-small | 1 | 100% |
| 2 | sn92 MicroTensor | 79 | 124 | 280 | cpu-small | 8 | 43% |
| 3 | sn91 cascade | 72.5 | 602 | 2,409 | cpu-small | 5 | 52% |
| 4 | sn107 Minos | 68.7 | 334 | 26,604 | cpu-small | 20 | 79% |
| 5 | sn67 Harnyx | 68.3 | 8.28 | 801 | cpu-small | 134 | 28% |
| 6 | sn38 ChronoLLM | 65.5 | 88.08 | 780 | cpu-small | 10 | 52% |
| 7 | sn111 Claims | 64.9 | 174 | 2,541 | rtx4090* | 5 | 79% |
| 8 | sn28 SayGM | 63.3 | 102 | 1,891 | rtx4090* | 50 | 13% |
| 9 | sn61 RedTeam | 62.6 | 83.20 | 128 | rtx4090* | 112 | 1% |
| 10 | sn55 NIOME | 61.8 | 63.38 | 529 | rtx4090* | 11 | 29% |
| 11 | sn81 Reliquary | 61.3 | 54.86 | 102 | rtx4090* | 40 | 41% |
| 12 | sn62 Ridges | 60.8 | 47.47 | 1,674 | rtx4090* | 19 | 26% |
| 13 | sn23 Trishool | 60.5 | 585 | 585 = | cpu-small | 2 | 80% |
| 14 | sn51 lium.io | 57.8 | 26.80 | 2,084 | rtx4090* | 68 | 81% |
| 15 | sn80 OpenRoboto | 56.5 | 456 | 1,616 | rtx4090* | 5 | 43% |
| 16 | sn9 iota | 56 | 12,184 | 12,184 = | rtx4090* | 3 | 68% |
| 17 | sn56 Gradients | 55.9 | 388 | 4,822 | rtx4090* | 11 | 46% |
| 18 | sn102 ConnitoAI | 55.7 | 10.97 | 1,677 | rtx4090* | 9 | 37% |
| 19 | sn96 Verathos | 54.5 | 23.00 | 155 | rtx4090 | 79 | 31% |
| 20 | sn124 Swarm | 54.3 | 249 | 807 | rtx4090* | 25 | 11% |

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
| wide (<30%) | 25 |
| concentrated (30–60%) | 24 |
| dominated (60–90%) | 19 |
| captured (>90%) | 23 |

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
| 2026-09-17T06:06 | sn10 | BURN_DROP | sn10 burn fell 1.000 -> 0.811 - miners can earn again |
| 2026-09-17T06:06 | sn15 | RELEASE | sn15 released v2.0.20 |
| 2026-09-17T06:06 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: Stop generated runs when miner inference  |
| 2026-09-17T06:06 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-3264 - [P2] validator names a GPU ben |
| 2026-09-17T06:06 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Verify retained clip objects before retry |
| 2026-09-17T06:06 | sn92 | RELEASE | sn92 released v0.4.7 |
| 2026-09-17T00:48 | sn40 | SCORING_COMMIT | sn40 commit touches scoring: Docs: round-7 rules, miner CLI flow, audi |
| 2026-09-17T00:48 | sn40 | README_TASK_DIFF | sn40 README task/scoring sections changed |
| 2026-09-17T00:48 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Merge pull request #135 from Umi-BitSign/ |
| 2026-09-16T22:24 | sn28 | RELEASE | sn28 released v0.4.18 |
| 2026-09-16T22:24 | sn28 | README_TASK_DIFF | sn28 README task/scoring sections changed |
| 2026-09-16T22:24 | sn45 | SCORING_COMMIT | sn45 commit touches scoring: Allow a per-model scale on audit scores |
| 2026-09-16T22:24 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: release: pin fresh validator installs to  |
| 2026-09-16T22:24 | sn102 | RELEASE | sn102 released v0.6.1 |
| 2026-09-16T22:24 | sn102 | SCORING_COMMIT | sn102 commit touches scoring: Merge pull request #274 from Connito-AI/ |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

