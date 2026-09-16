# Subnet watch — dashboard

_snapshot 2026-09-16T06:23:02Z · block 9078389 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 58 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 94 | `miner_burn` < 0.99 |
| Ranked | 94 | passed every gate |
| **Positive margin** | **58** | income beats machine cost |
| New events this window | 6 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 68 | `████████████████████████████` |
| 0–0.2 | 9 | `████` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 3 | `█` |
| 0.6–0.8 | 6 | `██` |
| 0.8–0.99 | 3 | `█` |
| ≥0.99 dead | 34 | `██████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn11 TrajectoryRL | 80 | 5,596 | 5,596 = | cpu-small | 1 | 100% |
| 2 | sn92 MicroTensor | 80 | 158 | 351 | cpu-small | 8 | 30% |
| 3 | sn91 cascade | 72.4 | 592 | 2,372 | cpu-small | 5 | 52% |
| 4 | sn1 Apex | 69.3 | 608 | 885 | rtx4090* | 4 | 57% |
| 5 | sn102 ConnitoAI | 69 | 543 | 1,721 | rtx4090* | 6 | 39% |
| 6 | sn107 Minos | 68.6 | 323 | 27,770 | cpu-small | 20 | 80% |
| 7 | sn67 Harnyx | 68.4 | 8.42 | 928 | cpu-small | 114 | 33% |
| 8 | sn38 ChronoLLM | 66.5 | 113 | 1,538 | cpu-small | 10 | 52% |
| 9 | sn124 Swarm | 66.2 | 248 | 799 | rtx4090* | 25 | 11% |
| 10 | sn111 Claims | 64.1 | 145 | 2,618 | rtx4090* | 5 | 82% |
| 11 | sn28 SayGM | 62.8 | 87.68 | 1,829 | rtx4090* | 47 | 14% |
| 12 | sn61 RedTeam | 62.7 | 88.03 | 131 | rtx4090* | 103 | 1% |
| 13 | sn81 Reliquary | 62.4 | 75.54 | 165 | rtx4090* | 37 | 20% |
| 14 | sn55 NIOME | 61.7 | 61.47 | 515 | rtx4090* | 11 | 29% |
| 15 | sn62 Ridges | 60.7 | 44.92 | 1,597 | rtx4090* | 19 | 26% |
| 16 | sn23 Trishool | 60.3 | 558 | 558 = | cpu-small | 2 | 80% |
| 17 | sn69 Herald | 59.7 | 1,187 | 2,383 | rtx4090* | 3 | 50% |
| 18 | sn51 lium.io | 59.1 | 35.82 | 1,555 | rtx4090* | 63 | 82% |
| 19 | sn9 iota | 56.2 | 13,182 | 13,182 = | rtx4090* | 2 | 74% |
| 20 | sn80 OpenRoboto | 56 | 395 | 1,402 | rtx4090* | 5 | 43% |

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
| concentrated (30–60%) | 25 |
| dominated (60–90%) | 17 |
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
| 2026-09-15T23:01 | sn62 | SCORING_COMMIT | sn62 commit touches scoring: test: :white_check_mark: Update tests to  |
| 2026-09-15T23:01 | sn76 | SCORING_COMMIT | sn76 commit touches scoring: docs: FAQ from the first external miner's |
| 2026-09-15T23:01 | sn102 | RELEASE | sn102 released v0.6.0 — scheduled task switching |
| 2026-09-15T23:01 | sn102 | SCORING_COMMIT | sn102 commit touches scoring: ⚡️ perf(validator): cap the in-shard eva |
| 2026-09-15T20:12 | sn15 | RELEASE | sn15 released v2.0.17 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

