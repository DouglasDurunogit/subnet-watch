# Subnet watch — dashboard

_snapshot 2026-11-23T03:01:18Z · block 9566567 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 53 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 105 | `miner_burn` < 0.99 |
| Ranked | 105 | passed every gate |
| **Positive margin** | **53** | income beats machine cost |
| New events this window | 7 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 69 | `████████████████████████████` |
| 0–0.2 | 6 | `██` |
| 0.2–0.4 | 7 | `███` |
| 0.4–0.6 | 3 | `█` |
| 0.6–0.8 | 10 | `████` |
| 0.8–0.99 | 10 | `████` |
| ≥0.99 dead | 23 | `█████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn42 CADmind | 81.6 | 235 | 235 = | cpu-small | 5 | 20% |
| 2 | sn3 Teutonic | 73.1 | 1,881 | 3,820 | rtx4090* | 4 | 40% |
| 3 | sn15 ORO | 65.9 | 5.63 | 11.55 | cpu-small | 82 | 94% |
| 4 | sn124 Swarm | 64.8 | 163 | 1,274 | rtx4090* | 11 | 29% |
| 5 | sn56 Gradients | 63.9 | 794 | 3,266 | a100-80 | 6 | 43% |
| 6 | sn67 Harnyx | 63.8 | 1.90 | 304 | cpu-small | 115 | 22% |
| 7 | sn53 engy | 63.4 | 103 | 3,605 | rtx4090 | 20 | 61% |
| 8 | sn66 conjectures | 62.5 | 79.27 | 940 | rtx4090* | 4 | 80% |
| 9 | sn120 Affine | 61.9 | 2,283 | 2,283 = | rtx4090* | 9 | 11% |
| 10 | sn58 Attune | 61.6 | 60.03 | 150 | rtx4090* | 57 | 30% |
| 11 | sn62 Ridges | 60.6 | 44.14 | 393 | rtx4090* | 47 | 10% |
| 12 | sn41 Almanac | 60.6 | 1.81 | 222 | cpu-small | 121 | 15% |
| 13 | sn60 Bitsec.ai | 60.5 | 580 | 580 = | cpu-small | 3 | 50% |
| 14 | sn111 Claims | 60.1 | 39.04 | 157 | rtx4090* | 4 | 88% |
| 15 | sn97 Ingot | 59.2 | 1,035 | 1,035 = | rtx4090* | 4 | 40% |
| 16 | sn25 UR | 58.1 | 20.34 | 20.34 = | rtx4090* | 10 | 45% |
| 17 | sn102 ConnitoAI | 57 | 532 | 533 | rtx4090* | 4 | 25% |
| 18 | sn4 Targon | 55.5 | 4,856 | 19,332 | rtx4090* | 5 | 66% |
| 19 | sn46 Instant | 55.4 | 130 | 156 | cpu-small | 9 | 24% |
| 20 | sn107 Minos | 54.4 | 133 | 11,581 | cpu-small | 20 | 81% |

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
| dominated (60–90%) | 29 |
| captured (>90%) | 27 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 97 |
| README keywords (GUESS) | 13 |
| min_compute.yml (curated) | 10 |
| code-submission (validator runs it) | 8 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-11-23T03:01 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: docs(scoring): the exact calculation writ |
| 2026-11-23T03:01 | sn21 | README_TASK_DIFF | sn21 README task/scoring sections changed |
| 2026-11-23T03:01 | sn70 | RELEASE | sn70 released Miner image image-v2026.11.22b (v0.7.0, protocol v4) |
| 2026-11-23T03:01 | sn70 | SCORING_COMMIT | sn70 commit touches scoring: docs: the validator guide's v4 READY line |
| 2026-11-23T03:01 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Preserve a normal execution attempt after |
| 2026-11-23T03:01 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: fix(laned): W0c list WB16 as a verificati |
| 2026-11-23T03:01 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: Verify arbiter-confirmed source correcti |
| 2026-11-22T22:26 | sn37 | BURN_DROP | sn37 burn fell 0.997 -> 0.738 - miners can earn again |
| 2026-11-22T22:26 | sn70 | RELEASE | sn70 released build-v2026.11.22: ci: 90-minute limits for the test job |
| 2026-11-22T22:26 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Stop assigning execution to a validator m |
| 2026-11-22T22:26 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: docs(laned): WB20 lane B in MINER, INTERF |
| 2026-11-22T17:04 | sn90 | RELEASE | sn90 released v1.4.6 |
| 2026-11-22T17:04 | sn90 | SCORING_COMMIT | sn90 commit touches scoring: docs(validator): describe Lium B300 AC-on |
| 2026-11-22T17:04 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: fix(laned): W5b scores each window from o |
| 2026-11-22T17:04 | sn94 | SCORING_COMMIT | sn94 commit touches scoring: Revalidate the fresh plant incarnation un |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

