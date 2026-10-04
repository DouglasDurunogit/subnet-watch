# Subnet watch — dashboard

_snapshot 2026-10-04T23:26:12Z · block 9212818 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 60 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 100 | `miner_burn` < 0.99 |
| Ranked | 100 | passed every gate |
| **Positive margin** | **60** | income beats machine cost |
| New events this window | 2 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 68 | `████████████████████████████` |
| 0–0.2 | 9 | `████` |
| 0.2–0.4 | 7 | `███` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 8 | `███` |
| 0.8–0.99 | 4 | `██` |
| ≥0.99 dead | 28 | `████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn23 Trishool | 74.3 | 1,028 | 1,028 = | cpu-small | 2 | 78% |
| 2 | sn41 Almanac | 73.7 | 33.49 | 99.37 | cpu-small | 127 | 29% |
| 3 | sn91 cascade | 73.1 | 717 | 2,295 | cpu-small | 5 | 52% |
| 4 | sn53 engy | 71.9 | 1,310 | 3,591 | rtx4090 | 14 | 22% |
| 5 | sn67 Harnyx | 70.6 | 14.12 | 944 | cpu-small | 128 | 30% |
| 6 | sn1 Apex | 69.1 | 566 | 1,165 | rtx4090* | 4 | 62% |
| 7 | sn46 Instant | 69.1 | 224 | 282 | cpu-small | 8 | 50% |
| 8 | sn111 Claims | 68.9 | 532 | 2,355 | rtx4090* | 5 | 61% |
| 9 | sn26 Perturb | 67.9 | 398 | 473 | rtx3060 | 3 | 60% |
| 10 | sn15 ORO | 67.6 | 9.30 | 18.16 | cpu-small | 52 | 98% |
| 11 | sn4 Targon | 65.5 | 6,807 | 32,196 | rtx4090* | 5 | 70% |
| 12 | sn120 Affine | 64.4 | 228 | 702 | rtx4090* | 117 | 2% |
| 13 | sn62 Ridges | 64 | 124 | 1,917 | rtx4090* | 31 | 21% |
| 14 | sn61 RedTeam | 62.7 | 83.79 | 150 | rtx4090* | 112 | 2% |
| 15 | sn14 Cacheon | 61.2 | 52.91 | 1,842 | rtx4090* | 13 | 23% |
| 16 | sn28 SayGM | 60.4 | 44.37 | 2,501 | rtx4090* | 64 | 23% |
| 17 | sn49 Nepher Robotics | 59.4 | 1,105 | 5,189 | rtx4090* | 4 | 69% |
| 18 | sn5 Hone | 58.5 | 38.70 | 41.29 | rtx4090* | 242 | 0% |
| 19 | sn107 Minos | 58.3 | 343 | 29,069 | cpu-small | 20 | 80% |
| 20 | sn74 Gittensor | 58.1 | 24.31 | 276 | rtx4090* | 21 | 50% |

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
| dominated (60–90%) | 21 |
| captured (>90%) | 25 |

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
| 2026-10-04T23:26 | sn85 | BURN_DROP | sn85 burn fell 1.000 -> 0.000 - miners can earn again |
| 2026-10-04T23:26 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: Recommend bounded per-task mining search |
| 2026-10-04T20:09 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Record final miner qualification and rema |
| 2026-10-04T20:09 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: Authorize qualified verifier additions w |
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

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

