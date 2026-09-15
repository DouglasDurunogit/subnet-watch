# Subnet watch — dashboard

_snapshot 2026-09-15T16:52:36Z · block 9074357 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 51 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 90 | `miner_burn` < 0.99 |
| Ranked | 91 | passed every gate |
| **Positive margin** | **51** | income beats machine cost |
| New events this window | 4 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 64 | `████████████████████████████` |
| 0–0.2 | 8 | `████` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 5 | `██` |
| 0.8–0.99 | 4 | `██` |
| ≥0.99 dead | 38 | `█████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn92 MicroTensor | 80.7 | 191 | 576 | cpu-small | 8 | 30% |
| 2 | sn11 TrajectoryRL | 80.1 | 5,780 | 5,780 = | cpu-small | 1 | 100% |
| 3 | sn114 SOMA | 79.2 | 4,485 | 7,973 | cpu-small | 3 | 80% |
| 4 | sn91 cascade | 72.6 | 621 | 2,488 | cpu-small | 5 | 52% |
| 5 | sn1 Apex | 69.7 | 687 | 926 | rtx4090* | 4 | 56% |
| 6 | sn107 Minos | 68.8 | 341 | 28,904 | cpu-small | 20 | 80% |
| 7 | sn67 Harnyx | 68.7 | 9.20 | 948 | cpu-small | 133 | 32% |
| 8 | sn38 ChronoLLM | 68 | 168 | 3,571 | cpu-small | 10 | 52% |
| 9 | sn96 Verathos | 67.1 | 16.40 | 168 | rtx4090 | 86 | 31% |
| 10 | sn124 Swarm | 66.3 | 253 | 818 | rtx4090* | 25 | 11% |
| 11 | sn111 Claims | 65.1 | 188 | 2,597 | rtx4090* | 5 | 78% |
| 12 | sn61 RedTeam | 62.7 | 87.26 | 138 | rtx4090* | 102 | 1% |
| 13 | sn81 Reliquary | 62.4 | 76.53 | 216 | rtx4090* | 44 | 8% |
| 14 | sn55 NIOME | 61.8 | 63.88 | 533 | rtx4090* | 11 | 29% |
| 15 | sn62 Ridges | 60.4 | 41.94 | 1,108 | rtx4090* | 18 | 35% |
| 16 | sn23 Trishool | 60.1 | 518 | 518 = | cpu-small | 2 | 80% |
| 17 | sn51 lium.io | 59.5 | 40.40 | 1,501 | rtx4090* | 63 | 83% |
| 18 | sn74 Gittensor | 59 | 30.10 | 180 | rtx4090 | 9 | 64% |
| 19 | sn14 Cacheon | 57.3 | 590 | 925 | rtx4090* | 13 | 15% |
| 20 | sn120 Affine | 56.7 | 16,344 | 16,344 = | rtx4090* | 2 | 50% |

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
| 2026-09-15T16:53 | sn10 | SCORING_COMMIT | sn10 commit touches scoring: fix: harden validator API binding and ser |
| 2026-09-15T16:53 | sn66 | SCORING_COMMIT | sn66 commit touches scoring: Raise proof token limit to one million fo |
| 2026-09-15T16:53 | sn90 | RELEASE | sn90 released v1.2.0 |
| 2026-09-15T16:53 | sn90 | SCORING_COMMIT | sn90 commit touches scoring: fix(scoring): divide emission pool by the |
| 2026-09-15T11:58 | sn10 | SCORING_COMMIT | sn10 commit touches scoring: feat: add campaign context coverage and r |
| 2026-09-15T11:58 | sn11 | SCORING_COMMIT | sn11 commit touches scoring: Merge pull request #321 from trajectoryRL |
| 2026-09-15T11:58 | sn15 | RELEASE | sn15 released v2.0.15: chore(validator): pin runtime 1.0.6 for generat |
| 2026-09-15T11:58 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: chore(validator): pin runtime 1.0.6 for g |
| 2026-09-15T11:58 | sn20 | SCORING_COMMIT | sn20 commit touches scoring: Derive semantic verdicts from validated f |
| 2026-09-15T11:58 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-2834 - [P0] validator consumes the ex |
| 2026-09-15T11:58 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-09-15T11:58 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: test: prove normal scoring collision roll |
| 2026-09-15T11:58 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Stop miner HTTP service after terminal ba |
| 2026-09-15T11:58 | sn90 | SCORING_COMMIT | sn90 commit touches scoring: docs(roadmap): move scoring-expansion ite |
| 2026-09-15T11:58 | sn90 | README_TASK_DIFF | sn90 README task/scoring sections changed |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

