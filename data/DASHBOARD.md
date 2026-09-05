# Subnet watch — dashboard

_snapshot 2026-09-05T20:33:52Z · block 9003619 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 58 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 93 | `miner_burn` < 0.99 |
| Ranked | 94 | passed every gate |
| **Positive margin** | **58** | income beats machine cost |
| New events this window | 3 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 60 | `████████████████████████████` |
| 0–0.2 | 9 | `████` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 3 | `█` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 35 | `████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn114 SOMA | 86.7 | 872 | 6,987 | cpu-small | 3 | 80% |
| 2 | sn92 MicroTensor | 81.1 | 209 | 466 | cpu-small | 9 | 26% |
| 3 | sn107 Minos | 76.6 | 83.83 | 5,055 | cpu-small | 21 | 81% |
| 4 | sn3 Teutonic | 75.6 | 3,937 | 3,937 = | rtx4090* | 5 | 20% |
| 5 | sn76 Phylax | 74.2 | 36.10 | 123 | cpu-small | 21 | 12% |
| 6 | sn67 Harnyx | 72.8 | 25.50 | 132 | cpu-small | 111 | 6% |
| 7 | sn91 cascade | 70.4 | 830 | 3,343 | rtx4090* | 5 | 52% |
| 8 | sn15 ORO | 70.3 | 21.77 | 20,311 | cpu-small | 72 | 93% |
| 9 | sn96 Verathos | 68.9 | 25.80 | 374 | rtx4090 | 81 | 40% |
| 10 | sn102 ConnitoAI | 68.7 | 507 | 1,708 | rtx4090* | 7 | 32% |
| 11 | sn62 Ridges | 68.1 | 419 | 2,117 | rtx4090* | 13 | 26% |
| 12 | sn111 Claims | 67.8 | 397 | 2,359 | rtx4090* | 6 | 55% |
| 13 | sn56 Gradients | 67.8 | 382 | 5,557 | rtx4090* | 7 | 49% |
| 14 | sn124 Swarm | 66.5 | 271 | 838 | rtx4090* | 25 | 11% |
| 15 | sn80 OpenRoboto | 65.4 | 185 | 670 | rtx4090* | 5 | 71% |
| 16 | sn108 Prometheon | 62.8 | 87.42 | 620 | rtx4090* | 10 | 33% |
| 17 | sn101 Tag101 | 62 | 0.67 | 0.76 | cpu-small | 243 | 90% |
| 18 | sn41 Almanac | 59.9 | 35.13 | 90.38 | cpu-small | 84 | 9% |
| 19 | sn14 Cacheon | 59.3 | 1,070 | 2,031 | rtx4090* | 6 | 30% |
| 20 | sn28 SayGM | 58.7 | 26.61 | 431 | rtx4090* | 45 | 85% |

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
| wide (<30%) | 27 |
| concentrated (30–60%) | 19 |
| dominated (60–90%) | 21 |
| captured (>90%) | 23 |

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
| 2026-09-05T20:34 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Protect validator seed custody and qualif |
| 2026-09-05T20:34 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Bind validator workflow to archive retry  |
| 2026-09-05T20:34 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Add external miner pilot launch handoffs |
| 2026-09-05T18:13 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: fix(reporting): rows shown with their acc |
| 2026-09-05T18:13 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: build: refresh reviewed gateway verifier  |
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

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

