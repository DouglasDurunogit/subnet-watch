# Subnet watch — dashboard

_snapshot 2026-09-16T11:55:24Z · block 9080045 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 54 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 93 | `miner_burn` < 0.99 |
| Ranked | 93 | passed every gate |
| **Positive margin** | **54** | income beats machine cost |
| New events this window | 5 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 66 | `████████████████████████████` |
| 0–0.2 | 9 | `████` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 3 | `█` |
| 0.8–0.99 | 5 | `██` |
| ≥0.99 dead | 35 | `███████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn11 TrajectoryRL | 80.1 | 5,734 | 5,734 = | cpu-small | 1 | 100% |
| 2 | sn92 MicroTensor | 80 | 160 | 357 | cpu-small | 8 | 30% |
| 3 | sn91 cascade | 72.5 | 599 | 2,399 | cpu-small | 5 | 52% |
| 4 | sn1 Apex | 69.3 | 592 | 871 | rtx4090* | 4 | 58% |
| 5 | sn107 Minos | 68.5 | 311 | 26,949 | cpu-small | 20 | 80% |
| 6 | sn67 Harnyx | 68.5 | 8.44 | 930 | cpu-small | 114 | 33% |
| 7 | sn38 ChronoLLM | 66.5 | 112 | 1,528 | cpu-small | 10 | 52% |
| 8 | sn124 Swarm | 66.1 | 243 | 787 | rtx4090* | 25 | 11% |
| 9 | sn111 Claims | 64.9 | 176 | 2,530 | rtx4090* | 5 | 79% |
| 10 | sn61 RedTeam | 62.7 | 88.26 | 131 | rtx4090* | 102 | 1% |
| 11 | sn28 SayGM | 62.2 | 73.91 | 1,833 | rtx4090* | 42 | 19% |
| 12 | sn81 Reliquary | 62.2 | 70.76 | 125 | rtx4090* | 40 | 26% |
| 13 | sn55 NIOME | 61.8 | 63.12 | 527 | rtx4090* | 11 | 29% |
| 14 | sn62 Ridges | 60.7 | 45.51 | 1,614 | rtx4090* | 19 | 26% |
| 15 | sn23 Trishool | 60.4 | 565 | 565 = | cpu-small | 2 | 80% |
| 16 | sn69 Herald | 59.7 | 1,195 | 2,398 | rtx4090* | 3 | 50% |
| 17 | sn51 lium.io | 59.3 | 37.94 | 1,844 | rtx4090* | 66 | 80% |
| 18 | sn9 iota | 56.3 | 13,279 | 13,279 = | rtx4090* | 2 | 74% |
| 19 | sn80 OpenRoboto | 56.1 | 410 | 1,456 | rtx4090* | 5 | 43% |
| 20 | sn56 Gradients | 55.3 | 320 | 4,743 | rtx4090* | 12 | 46% |

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
| 2026-09-16T11:55 | sn10 | SCORING_COMMIT | sn10 commit touches scoring: fix(bench): lower Qwen correctness scorer |
| 2026-09-16T11:55 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Allow bounded retained validator history  |
| 2026-09-16T11:55 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-3480 - [P1] validator: GPU probe bloc |
| 2026-09-16T11:55 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Merge pull request #129 from Umi-BitSign/ |
| 2026-09-16T11:55 | sn114 | SCORING_COMMIT | sn114 commit touches scoring: docs: describe complexity incentive laye |
| 2026-09-16T06:23 | sn15 | RELEASE | sn15 released v2.0.19 |
| 2026-09-16T06:23 | sn15 | README_TASK_DIFF | sn15 README task/scoring sections changed |
| 2026-09-16T06:23 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Retain verified reserve repairs for exact |
| 2026-09-16T06:23 | sn36 | BURN_DROP | sn36 burn fell 1.000 -> 0.951 - miners can earn again |
| 2026-09-16T06:23 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-2662 - [P1] validator matches GPU ban |
| 2026-09-16T06:23 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Stage verified successor helpers outside  |
| 2026-09-16T01:23 | sn34 | RELEASE | sn34 released 5.0.5 — Generator Qualification & Paid Resubmissions |
| 2026-09-16T01:23 | sn62 | RELEASE | sn62 released v0.3.5 |
| 2026-09-16T01:23 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Verify current installer against signed f |
| 2026-09-15T23:01 | sn15 | RELEASE | sn15 released v2.0.18: search-server sync-worker fix + rebuilt base (O |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

