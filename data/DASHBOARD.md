# Subnet watch — dashboard

_snapshot 2026-10-04T12:45:08Z · block 9209612 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 61 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 99 | `miner_burn` < 0.99 |
| Ranked | 99 | passed every gate |
| **Positive margin** | **61** | income beats machine cost |
| New events this window | 8 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 68 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 8 | `███` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 7 | `███` |
| 0.8–0.99 | 5 | `██` |
| ≥0.99 dead | 29 | `████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn23 Trishool | 74.5 | 1,084 | 1,084 = | cpu-small | 2 | 77% |
| 2 | sn41 Almanac | 73.9 | 35.64 | 2,079 | cpu-small | 127 | 30% |
| 3 | sn53 engy | 71.9 | 1,315 | 3,605 | rtx4090 | 14 | 22% |
| 4 | sn91 cascade | 71.4 | 435 | 2,324 | cpu-small | 5 | 52% |
| 5 | sn67 Harnyx | 70.6 | 14.12 | 945 | cpu-small | 128 | 30% |
| 6 | sn111 Claims | 69.9 | 723 | 2,792 | rtx4090* | 3 | 72% |
| 7 | sn56 Gradients | 69.3 | 609 | 5,251 | rtx4090* | 8 | 39% |
| 8 | sn1 Apex | 69.2 | 575 | 973 | rtx4090* | 4 | 65% |
| 9 | sn46 Instant | 69 | 217 | 251 | cpu-small | 8 | 51% |
| 10 | sn120 Affine | 68.6 | 581 | 581 = | rtx4090* | 86 | 1% |
| 11 | sn26 Perturb | 68 | 411 | 741 | rtx3060 | 3 | 59% |
| 12 | sn15 ORO | 67.4 | 9.32 | 18.21 | cpu-small | 52 | 98% |
| 13 | sn4 Targon | 65.5 | 6,785 | 32,093 | rtx4090* | 5 | 70% |
| 14 | sn62 Ridges | 64.6 | 149 | 2,292 | rtx4090* | 30 | 25% |
| 15 | sn28 SayGM | 63.9 | 122 | 1,347 | rtx4090* | 53 | 32% |
| 16 | sn61 RedTeam | 62.8 | 86.47 | 156 | rtx4090* | 112 | 2% |
| 17 | sn14 Cacheon | 61.2 | 52.70 | 1,836 | rtx4090* | 13 | 23% |
| 18 | sn49 Nepher Robotics | 59.5 | 1,138 | 5,340 | rtx4090* | 4 | 69% |
| 19 | sn80 OpenRoboto | 58.7 | 877 | 3,276 | rtx4090* | 8 | 33% |
| 20 | sn5 Hone | 58.7 | 38.53 | 40.95 | rtx4090* | 242 | 0% |

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
| concentrated (30–60%) | 27 |
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
| 2026-10-04T06:24 | sn26 | README_TASK_DIFF | sn26 README task/scoring sections changed |
| 2026-10-04T06:24 | sn30 | BURN_DROP | sn30 burn fell 1.000 -> 0.000 - miners can earn again |
| 2026-10-04T06:24 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Merge pull request #209 from leadpoet/cod |
| 2026-10-04T06:24 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: Preserve checkpoint read access through  |
| 2026-10-04T00:33 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Merge pull request #205 from leadpoet/cod |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

