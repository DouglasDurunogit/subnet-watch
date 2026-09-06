# Subnet watch — dashboard

_snapshot 2026-09-06T08:57:43Z · block 9007326 · run_status **ok**_

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
| New events this window | 0 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 59 | `████████████████████████████` |
| 0–0.2 | 9 | `████` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 35 | `█████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn92 MicroTensor | 81.1 | 209 | 466 | cpu-small | 9 | 26% |
| 2 | sn107 Minos | 76.8 | 87.08 | 5,289 | cpu-small | 21 | 81% |
| 3 | sn3 Teutonic | 75.7 | 4,016 | 4,016 = | rtx4090* | 5 | 20% |
| 4 | sn114 SOMA | 73.8 | 899 | 899 = | cpu-small | 3 | 80% |
| 5 | sn67 Harnyx | 72.1 | 21.07 | 109 | cpu-small | 107 | 33% |
| 6 | sn91 cascade | 70.4 | 838 | 3,377 | rtx4090* | 5 | 52% |
| 7 | sn15 ORO | 70.2 | 21.38 | 20,915 | cpu-small | 80 | 92% |
| 8 | sn96 Verathos | 69.1 | 27.06 | 379 | rtx4090 | 80 | 40% |
| 9 | sn62 Ridges | 68.1 | 420 | 2,127 | rtx4090* | 13 | 26% |
| 10 | sn56 Gradients | 67.6 | 357 | 3,353 | rtx4090* | 7 | 49% |
| 11 | sn111 Claims | 66.8 | 300 | 2,686 | rtx4090* | 5 | 62% |
| 12 | sn124 Swarm | 66.6 | 275 | 849 | rtx4090* | 25 | 11% |
| 13 | sn80 OpenRoboto | 65.4 | 189 | 677 | rtx4090* | 5 | 71% |
| 14 | sn121 sundae_bar | 63.1 | 1,266 | 1,266 = | cpu-small | 2 | 60% |
| 15 | sn108 Prometheon | 62.8 | 87.51 | 338 | rtx4090* | 10 | 33% |
| 16 | sn101 Tag101 | 62 | 0.69 | 0.69 = | cpu-small | 248 | 90% |
| 17 | sn41 Almanac | 60.1 | 36.19 | 106 | cpu-small | 86 | 6% |
| 18 | sn14 Cacheon | 59.3 | 1,059 | 2,011 | rtx4090* | 6 | 30% |
| 19 | sn51 lium.io | 57.9 | 27.99 | 2,427 | rtx4090* | 62 | 70% |
| 20 | sn102 ConnitoAI | 57.8 | 19.61 | 1,748 | rtx4090* | 8 | 33% |

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
| concentrated (30–60%) | 21 |
| dominated (60–90%) | 21 |
| captured (>90%) | 22 |

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

