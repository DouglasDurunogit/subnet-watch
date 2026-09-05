# Subnet watch — dashboard

_snapshot 2026-09-05T22:21:10Z · block 9004152 · run_status **ok**_

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
| Ranked | 94 | passed every gate |
| **Positive margin** | **57** | income beats machine cost |
| New events this window | 2 | see ALARMS.md |

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
| 1 | sn114 SOMA | 86.8 | 890 | 7,128 | cpu-small | 3 | 80% |
| 2 | sn92 MicroTensor | 81.1 | 211 | 471 | cpu-small | 9 | 26% |
| 3 | sn107 Minos | 76.7 | 85.64 | 5,129 | cpu-small | 21 | 81% |
| 4 | sn3 Teutonic | 75.7 | 4,001 | 4,001 = | rtx4090* | 5 | 20% |
| 5 | sn67 Harnyx | 72.9 | 25.91 | 134 | cpu-small | 111 | 6% |
| 6 | sn15 ORO | 70.8 | 22.92 | 21,006 | cpu-small | 73 | 93% |
| 7 | sn91 cascade | 70.4 | 836 | 3,368 | rtx4090* | 5 | 52% |
| 8 | sn96 Verathos | 69.5 | 29.51 | 356 | rtx4090 | 75 | 41% |
| 9 | sn62 Ridges | 68.2 | 429 | 2,167 | rtx4090* | 13 | 26% |
| 10 | sn111 Claims | 67.8 | 404 | 2,395 | rtx4090* | 6 | 55% |
| 11 | sn56 Gradients | 67.6 | 358 | 3,358 | rtx4090* | 7 | 49% |
| 12 | sn124 Swarm | 66.6 | 276 | 851 | rtx4090* | 25 | 11% |
| 13 | sn80 OpenRoboto | 65.4 | 188 | 680 | rtx4090* | 5 | 71% |
| 14 | sn108 Prometheon | 62.9 | 90.48 | 640 | rtx4090* | 10 | 33% |
| 15 | sn101 Tag101 | 62 | 0.70 | 0.79 | cpu-small | 243 | 90% |
| 16 | sn28 SayGM | 61.6 | 61.17 | 621 | rtx4090* | 45 | 74% |
| 17 | sn41 Almanac | 60 | 36.05 | 92.76 | cpu-small | 84 | 8% |
| 18 | sn14 Cacheon | 59.4 | 1,087 | 2,063 | rtx4090* | 6 | 30% |
| 19 | sn74 Gittensor | 58 | 22.83 | 172 | rtx4090 | 11 | 64% |
| 20 | sn51 lium.io | 57.5 | 25.30 | 2,027 | rtx4090* | 63 | 71% |

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
| concentrated (30–60%) | 19 |
| dominated (60–90%) | 21 |
| captured (>90%) | 23 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 99 |
| min_compute.yml (curated) | 11 |
| code-submission (validator runs it) | 10 |
| README keywords (GUESS) | 7 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-09-05T22:21 | sn7 | RELEASE | sn7 released release-20260905-204833 |
| 2026-09-05T22:21 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: chore(validator): bind existing recovery  |
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

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

