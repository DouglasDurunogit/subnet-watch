# Subnet watch — dashboard

_snapshot 2026-09-16T19:45:53Z · block 9082386 · run_status **ok**_

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
| New events this window | 5 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 64 | `████████████████████████████` |
| 0–0.2 | 10 | `████` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 5 | `██` |
| 0.8–0.99 | 4 | `██` |
| ≥0.99 dead | 35 | `███████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn92 MicroTensor | 80.4 | 176 | 297 | cpu-small | 8 | 34% |
| 2 | sn11 TrajectoryRL | 80 | 5,594 | 5,594 = | cpu-small | 1 | 100% |
| 3 | sn91 cascade | 72.4 | 595 | 2,383 | cpu-small | 5 | 52% |
| 4 | sn102 ConnitoAI | 70.5 | 865 | 1,163 | rtx4090* | 6 | 27% |
| 5 | sn1 Apex | 69.1 | 558 | 899 | rtx4090* | 4 | 58% |
| 6 | sn107 Minos | 68.7 | 331 | 26,413 | cpu-small | 20 | 79% |
| 7 | sn67 Harnyx | 68.7 | 8.38 | 924 | cpu-small | 117 | 33% |
| 8 | sn38 ChronoLLM | 66.4 | 110 | 1,504 | cpu-small | 10 | 52% |
| 9 | sn111 Claims | 65.5 | 208 | 2,331 | rtx4090* | 5 | 74% |
| 10 | sn61 RedTeam | 62.5 | 81.32 | 124 | rtx4090* | 112 | 1% |
| 11 | sn28 SayGM | 62.4 | 76.77 | 2,450 | rtx4090* | 49 | 18% |
| 12 | sn81 Reliquary | 61.9 | 65.87 | 103 | rtx4090* | 41 | 31% |
| 13 | sn55 NIOME | 61.8 | 62.90 | 525 | rtx4090* | 11 | 29% |
| 14 | sn69 Herald | 60.7 | 1,597 | 1,597 = | rtx4090* | 3 | 33% |
| 15 | sn62 Ridges | 60.7 | 45.20 | 1,605 | rtx4090* | 19 | 26% |
| 16 | sn23 Trishool | 60.3 | 560 | 560 = | cpu-small | 2 | 80% |
| 17 | sn51 lium.io | 58.1 | 28.24 | 1,384 | rtx4090* | 66 | 82% |
| 18 | sn80 OpenRoboto | 56.4 | 446 | 1,470 | rtx4090* | 5 | 43% |
| 19 | sn9 iota | 56 | 11,861 | 11,861 = | rtx4090* | 3 | 68% |
| 20 | sn14 Cacheon | 56 | 392 | 892 | rtx4090* | 13 | 15% |

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
| concentrated (30–60%) | 26 |
| dominated (60–90%) | 16 |
| captured (>90%) | 22 |

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
| 2026-09-16T19:46 | sn34 | SCORING_COMMIT | sn34 commit touches scoring: Exclude no_answer rows before the reward- |
| 2026-09-16T19:46 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Fix Sep16 benchmark bank verification |
| 2026-09-16T19:46 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: fix: keep valid bridge miners eligible du |
| 2026-09-16T19:46 | sn92 | RELEASE | sn92 released v0.4.6 |
| 2026-09-16T19:46 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: mt-4g: 3 GiB disk ceiling, matching the a |
| 2026-09-16T16:47 | sn9 | RELEASE | sn9 released v4.13.0 |
| 2026-09-16T16:47 | sn20 | BURN_DROP | sn20 burn fell 1.000 -> 0.754 - miners can earn again |
| 2026-09-16T16:47 | sn51 | RELEASE | sn51 released executor-v1.129 |
| 2026-09-16T16:47 | sn66 | RELEASE | sn66 released v1.0.4 |
| 2026-09-16T16:47 | sn76 | SCORING_COMMIT | sn76 commit touches scoring: feat(client): optional chosen miner_id on |
| 2026-09-16T16:47 | sn92 | RELEASE | sn92 released v0.4.4 |
| 2026-09-16T16:47 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: penalties: declared factors on the standi |
| 2026-09-16T11:55 | sn10 | SCORING_COMMIT | sn10 commit touches scoring: fix(bench): lower Qwen correctness scorer |
| 2026-09-16T11:55 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Allow bounded retained validator history  |
| 2026-09-16T11:55 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-3480 - [P1] validator: GPU probe bloc |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

