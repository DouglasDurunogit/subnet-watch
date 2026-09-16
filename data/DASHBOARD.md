# Subnet watch — dashboard

_snapshot 2026-09-16T16:47:05Z · block 9081495 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 55 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 93 | `miner_burn` < 0.99 |
| Ranked | 93 | passed every gate |
| **Positive margin** | **55** | income beats machine cost |
| New events this window | 7 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 63 | `████████████████████████████` |
| 0–0.2 | 11 | `█████` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 4 | `██` |
| 0.8–0.99 | 5 | `██` |
| ≥0.99 dead | 35 | `████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn11 TrajectoryRL | 80 | 5,590 | 5,590 = | cpu-small | 1 | 100% |
| 2 | sn92 MicroTensor | 79.9 | 156 | 348 | cpu-small | 8 | 30% |
| 3 | sn91 cascade | 72.4 | 579 | 2,320 | cpu-small | 5 | 52% |
| 4 | sn1 Apex | 69.1 | 562 | 836 | rtx4090* | 4 | 59% |
| 5 | sn102 ConnitoAI | 68.8 | 520 | 1,089 | rtx4090* | 7 | 25% |
| 6 | sn107 Minos | 68.7 | 329 | 26,226 | cpu-small | 20 | 79% |
| 7 | sn67 Harnyx | 68.4 | 8.25 | 911 | cpu-small | 115 | 33% |
| 8 | sn38 ChronoLLM | 66.2 | 104 | 1,426 | cpu-small | 10 | 52% |
| 9 | sn124 Swarm | 66.1 | 237 | 769 | rtx4090* | 25 | 11% |
| 10 | sn111 Claims | 65.4 | 206 | 2,307 | rtx4090* | 5 | 74% |
| 11 | sn28 SayGM | 63.5 | 107 | 2,484 | rtx4090* | 34 | 19% |
| 12 | sn61 RedTeam | 62.4 | 78.97 | 122 | rtx4090* | 112 | 1% |
| 13 | sn81 Reliquary | 62 | 66.54 | 109 | rtx4090* | 40 | 29% |
| 14 | sn55 NIOME | 61.6 | 59.38 | 499 | rtx4090* | 11 | 29% |
| 15 | sn62 Ridges | 60.6 | 44.44 | 1,582 | rtx4090* | 19 | 26% |
| 16 | sn23 Trishool | 60.3 | 551 | 551 = | cpu-small | 2 | 80% |
| 17 | sn69 Herald | 59.7 | 1,180 | 2,369 | rtx4090* | 3 | 50% |
| 18 | sn51 lium.io | 57.4 | 24.32 | 1,454 | rtx4090* | 66 | 82% |
| 19 | sn14 Cacheon | 56.6 | 474 | 879 | rtx4090* | 13 | 15% |
| 20 | sn9 iota | 56 | 11,839 | 11,839 = | rtx4090* | 3 | 68% |

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
| concentrated (30–60%) | 25 |
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
| 2026-09-16T11:55 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Merge pull request #129 from Umi-BitSign/ |
| 2026-09-16T11:55 | sn114 | SCORING_COMMIT | sn114 commit touches scoring: docs: describe complexity incentive laye |
| 2026-09-16T06:23 | sn15 | RELEASE | sn15 released v2.0.19 |
| 2026-09-16T06:23 | sn15 | README_TASK_DIFF | sn15 README task/scoring sections changed |
| 2026-09-16T06:23 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Retain verified reserve repairs for exact |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

