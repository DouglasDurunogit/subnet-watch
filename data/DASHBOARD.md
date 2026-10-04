# Subnet watch — dashboard

_snapshot 2026-10-04T17:05:53Z · block 9210916 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 58 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 99 | `miner_burn` < 0.99 |
| Ranked | 99 | passed every gate |
| **Positive margin** | **58** | income beats machine cost |
| New events this window | 5 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 67 | `████████████████████████████` |
| 0–0.2 | 8 | `███` |
| 0.2–0.4 | 7 | `███` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 7 | `███` |
| 0.8–0.99 | 5 | `██` |
| ≥0.99 dead | 29 | `████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn23 Trishool | 74 | 948 | 948 = | cpu-small | 2 | 80% |
| 2 | sn41 Almanac | 73.9 | 35.11 | 2,093 | cpu-small | 127 | 30% |
| 3 | sn91 cascade | 73.3 | 764 | 2,215 | cpu-small | 5 | 49% |
| 4 | sn53 engy | 71.9 | 1,304 | 3,574 | rtx4090 | 14 | 22% |
| 5 | sn67 Harnyx | 70.6 | 14.20 | 949 | cpu-small | 128 | 30% |
| 6 | sn46 Instant | 70.1 | 298 | 353 | cpu-small | 6 | 51% |
| 7 | sn56 Gradients | 69.4 | 613 | 5,282 | rtx4090* | 8 | 39% |
| 8 | sn1 Apex | 69.2 | 583 | 957 | rtx4090* | 4 | 65% |
| 9 | sn120 Affine | 68.7 | 585 | 585 = | rtx4090* | 86 | 1% |
| 10 | sn26 Perturb | 67.9 | 404 | 483 | rtx3060 | 3 | 60% |
| 11 | sn111 Claims | 67 | 303 | 2,714 | rtx4090* | 5 | 70% |
| 12 | sn15 ORO | 66.8 | 9.27 | 18.12 | cpu-small | 52 | 98% |
| 13 | sn4 Targon | 65.6 | 6,822 | 32,269 | rtx4090* | 5 | 70% |
| 14 | sn62 Ridges | 64.6 | 150 | 2,305 | rtx4090* | 30 | 25% |
| 15 | sn61 RedTeam | 62.7 | 85.07 | 154 | rtx4090* | 113 | 2% |
| 16 | sn28 SayGM | 61.3 | 57.60 | 1,189 | rtx4090* | 61 | 34% |
| 17 | sn14 Cacheon | 61.2 | 53.05 | 1,847 | rtx4090* | 13 | 23% |
| 18 | sn49 Nepher Robotics | 59.5 | 1,138 | 5,339 | rtx4090* | 4 | 69% |
| 19 | sn107 Minos | 59.2 | 428 | 27,972 | cpu-small | 20 | 77% |
| 20 | sn5 Hone | 58.5 | 39.05 | 41.31 | rtx4090* | 242 | 0% |

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
| wide (<30%) | 22 |
| concentrated (30–60%) | 26 |
| dominated (60–90%) | 22 |
| captured (>90%) | 24 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 96 |
| README keywords (GUESS) | 12 |
| min_compute.yml (curated) | 10 |
| code-submission (validator runs it) | 9 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-10-04T17:06 | sn9 | RELEASE | sn9 released v4.13.4 |
| 2026-10-04T17:06 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Verify completed original capture and Yum |
| 2026-10-04T17:06 | sn25 | README_TASK_DIFF | sn25 README task/scoring sections changed |
| 2026-10-04T17:06 | sn116 | BURN_DROP | sn116 burn fell 1.000 -> 0.000 - miners can earn again |
| 2026-10-04T17:06 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: Update public miner setup for signed for |
| 2026-10-04T12:45 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Retain passing signed-history and termina |
| 2026-10-04T12:45 | sn28 | RELEASE | sn28 released v0.4.25 |
| 2026-10-04T12:45 | sn28 | SCORING_COMMIT | sn28 commit touches scoring: Handle scheduled miner price increases as |
| 2026-10-04T12:45 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: validator: keep a banned node verified wh |
| 2026-10-04T12:45 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Bind local verifier fix to protected work |
| 2026-10-04T12:45 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Stabilize checkpoint cache verification |
| 2026-10-04T12:45 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: docs(corpus): episode jobs on the split v |
| 2026-10-04T12:45 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: Document guarded covered-training handof |
| 2026-10-04T06:24 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Retain complete model success and actual  |
| 2026-10-04T06:24 | sn26 | SCORING_COMMIT | sn26 commit touches scoring: feat: rank scanning miners by stake-weigh |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

