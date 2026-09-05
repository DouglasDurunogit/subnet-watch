# Subnet watch — dashboard

_snapshot 2026-09-05T16:00:23Z · block 9002257 · run_status **ok**_

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
| Ranked | 94 | passed every gate |
| **Positive margin** | **55** | income beats machine cost |
| New events this window | 3 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 57 | `████████████████████████████` |
| 0–0.2 | 10 | `█████` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 8 | `████` |
| ≥0.99 dead | 35 | `█████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn92 MicroTensor | 81.5 | 231 | 696 | cpu-small | 9 | 26% |
| 2 | sn107 Minos | 76.7 | 85.51 | 5,211 | cpu-small | 21 | 81% |
| 3 | sn3 Teutonic | 75.6 | 3,982 | 3,982 = | rtx4090* | 5 | 20% |
| 4 | sn67 Harnyx | 72.9 | 26.04 | 134 | cpu-small | 111 | 6% |
| 5 | sn102 ConnitoAI | 72.1 | 1,379 | 1,656 | rtx4090* | 4 | 30% |
| 6 | sn76 Phylax | 70.6 | 15.80 | 87.35 | cpu-small | 21 | 58% |
| 7 | sn91 cascade | 70.4 | 846 | 3,410 | rtx4090* | 5 | 52% |
| 8 | sn15 ORO | 70.2 | 22.14 | 20,643 | cpu-small | 72 | 93% |
| 9 | sn96 Verathos | 69 | 25.91 | 383 | rtx4090 | 79 | 40% |
| 10 | sn62 Ridges | 68.1 | 423 | 2,140 | rtx4090* | 13 | 26% |
| 11 | sn56 Gradients | 67.9 | 391 | 5,657 | rtx4090* | 7 | 49% |
| 12 | sn124 Swarm | 66.6 | 275 | 848 | rtx4090* | 25 | 11% |
| 13 | sn111 Claims | 66.4 | 266 | 2,392 | rtx4090* | 5 | 55% |
| 14 | sn80 OpenRoboto | 65.4 | 190 | 685 | rtx4090* | 5 | 71% |
| 15 | sn108 Prometheon | 62.9 | 88.54 | 628 | rtx4090* | 10 | 33% |
| 16 | sn101 Tag101 | 62 | 0.70 | 0.84 | cpu-small | 244 | 90% |
| 17 | sn41 Almanac | 60 | 35.26 | 90.83 | cpu-small | 84 | 10% |
| 18 | sn14 Cacheon | 59.3 | 1,072 | 2,057 | rtx4090* | 6 | 30% |
| 19 | sn51 lium.io | 59 | 35.57 | 2,021 | rtx4090* | 62 | 75% |
| 20 | sn74 Gittensor | 58.1 | 23.63 | 157 | rtx4090 | 11 | 64% |

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
| concentrated (30–60%) | 22 |
| dominated (60–90%) | 19 |
| captured (>90%) | 24 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 98 |
| code-submission (validator runs it) | 11 |
| min_compute.yml (curated) | 11 |
| README keywords (GUESS) | 7 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-09-05T16:00 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: validator: add private bounded attempt re |
| 2026-09-05T16:00 | sn56 | SCORING_COMMIT | sn56 commit touches scoring: Make the auditor loop continuously, match |
| 2026-09-05T16:00 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Merge pull request #178 from leadpoet/cod |
| 2026-09-05T12:59 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Merge pull request #177 from leadpoet/cod |
| 2026-09-05T12:59 | sn80 | README_TASK_DIFF | sn80 README task/scoring sections changed |
| 2026-09-05T09:27 | sn47 | SCORING_COMMIT | sn47 commit touches scoring: refine evaluation system |
| 2026-09-05T09:27 | sn47 | README_TASK_DIFF | sn47 README task/scoring sections changed |
| 2026-09-05T09:27 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: fix: exclude stale validator build path f |
| 2026-09-05T09:27 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: fix(challenges): boot when sk/session pl |
| 2026-09-05T05:40 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: docs(scoring): standing and resolution am |
| 2026-09-05T05:40 | sn62 | RELEASE | sn62 released v0.3.0 |
| 2026-09-05T05:40 | sn62 | SCORING_COMMIT | sn62 commit touches scoring: test: :white_check_mark: Add tests valida |
| 2026-09-05T05:40 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: fix: validate retained gateway archives b |
| 2026-09-04T23:02 | sn7 | RELEASE | sn7 released release-20260904-214340: Bump version to 3.3.2 (#722) |
| 2026-09-04T23:02 | sn25 | RELEASE | sn25 released v2026.9.4-1037600680 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

