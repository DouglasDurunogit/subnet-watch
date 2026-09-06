# Subnet watch — dashboard

_snapshot 2026-09-06T04:34:04Z · block 9006012 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 57 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 94 | `miner_burn` < 0.99 |
| Ranked | 95 | passed every gate |
| **Positive margin** | **57** | income beats machine cost |
| New events this window | 2 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 58 | `████████████████████████████` |
| 0–0.2 | 9 | `████` |
| 0.2–0.4 | 7 | `███` |
| 0.4–0.6 | 3 | `█` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 8 | `████` |
| ≥0.99 dead | 34 | `████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn92 MicroTensor | 81.1 | 210 | 467 | cpu-small | 9 | 26% |
| 2 | sn107 Minos | 76.8 | 86.77 | 5,267 | cpu-small | 21 | 81% |
| 3 | sn3 Teutonic | 75.7 | 4,040 | 4,040 = | rtx4090* | 5 | 20% |
| 4 | sn114 SOMA | 73.8 | 889 | 889 = | cpu-small | 3 | 80% |
| 5 | sn67 Harnyx | 72.1 | 21.42 | 111 | cpu-small | 106 | 33% |
| 6 | sn15 ORO | 70.5 | 22.66 | 42.83 | cpu-small | 76 | 92% |
| 7 | sn91 cascade | 70.4 | 847 | 3,414 | rtx4090* | 5 | 52% |
| 8 | sn111 Claims | 69.3 | 616 | 2,724 | rtx4090* | 5 | 63% |
| 9 | sn96 Verathos | 69.1 | 26.96 | 482 | rtx4090 | 81 | 40% |
| 10 | sn62 Ridges | 68.2 | 431 | 2,179 | rtx4090* | 13 | 26% |
| 11 | sn56 Gradients | 67.6 | 366 | 3,435 | rtx4090* | 7 | 49% |
| 12 | sn124 Swarm | 66.6 | 277 | 855 | rtx4090* | 25 | 11% |
| 13 | sn80 OpenRoboto | 65.5 | 192 | 631 | rtx4090* | 5 | 72% |
| 14 | sn98 NeverPlayAlone | 64.5 | 1,947 | 1,947 = | cpu-small | 1 | 100% |
| 15 | sn108 Prometheon | 63.1 | 93.85 | 361 | rtx4090* | 10 | 30% |
| 16 | sn101 Tag101 | 62.1 | 0.71 | 0.76 | cpu-small | 242 | 90% |
| 17 | sn28 SayGM | 61.2 | 55.05 | 612 | rtx4090* | 44 | 53% |
| 18 | sn41 Almanac | 60.1 | 36.07 | 106 | cpu-small | 86 | 7% |
| 19 | sn14 Cacheon | 59.4 | 1,093 | 2,075 | rtx4090* | 6 | 30% |
| 20 | sn51 lium.io | 57.2 | 23.99 | 2,056 | rtx4090* | 63 | 73% |

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
| concentrated (30–60%) | 18 |
| dominated (60–90%) | 21 |
| captured (>90%) | 24 |

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
| 2026-09-06T04:34 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Isolate Arena failure regressions and ver |
| 2026-09-06T04:34 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Add public registered-miner endpoint pilo |
| 2026-09-06T00:06 | sn74 | RELEASE | sn74 released release-20260905-223823 |
| 2026-09-06T00:06 | sn74 | SCORING_COMMIT | sn74 commit touches scoring: serving miner: an attestation waits for p |
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

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

