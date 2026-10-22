# Subnet watch — dashboard

_snapshot 2026-10-22T18:06:02Z · block 9340731 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 55 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 95 | `miner_burn` < 0.99 |
| Ranked | 95 | passed every gate |
| **Positive margin** | **55** | income beats machine cost |
| New events this window | 14 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 64 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 6 | `███` |
| 0.6–0.8 | 10 | `████` |
| 0.8–0.99 | 3 | `█` |
| ≥0.99 dead | 33 | `██████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn121 sundae_bar | 74.4 | 1,078 | 1,078 = | cpu-small | 2 | 60% |
| 2 | sn3 Teutonic | 73.5 | 2,138 | 2,918 | rtx4090* | 5 | 46% |
| 3 | sn97 Ingot | 73.3 | 1,966 | 1,966 = | rtx4090* | 4 | 40% |
| 4 | sn67 Harnyx | 73.1 | 27.45 | 260 | cpu-small | 46 | 11% |
| 5 | sn120 Affine | 71 | 998 | 2,948 | rtx4090* | 25 | 9% |
| 6 | sn91 cascade | 70.8 | 363 | 1,456 | cpu-small | 5 | 52% |
| 7 | sn1 Apex | 68.3 | 449 | 950 | rtx4090* | 5 | 53% |
| 8 | sn82 Noah | 67.5 | 560 | 576 | rtx4090* | 62 | 2% |
| 9 | sn56 Gradients | 67.2 | 322 | 5,154 | rtx4090* | 9 | 46% |
| 10 | sn125 Refinery | 67.1 | 314 | 929 | rtx4090* | 4 | 50% |
| 11 | sn53 engy | 67 | 303 | 2,689 | rtx4090 | 36 | 11% |
| 12 | sn107 Minos | 66.9 | 219 | 18,361 | cpu-small | 20 | 80% |
| 13 | sn66 conjectures | 63.2 | 97.20 | 203 | rtx4090* | 4 | 81% |
| 14 | sn15 ORO | 61.9 | 8.50 | 14,463 | cpu-small | 75 | 95% |
| 15 | sn55 NIOME | 61.6 | 60.44 | 507 | rtx4090* | 11 | 30% |
| 16 | sn34 BitMind | 61.5 | 885 | 7,743 | a100-80 | 3 | 85% |
| 17 | sn111 Claims | 59.2 | 30.12 | 2,736 | rtx4090* | 6 | 90% |
| 18 | sn41 Almanac | 58.9 | 1.69 | 124 | cpu-small | 159 | 3% |
| 19 | sn80 OpenRoboto | 58.8 | 919 | 3,875 | rtx4090* | 11 | 25% |
| 20 | sn92 REAX | 57.9 | 44.44 | 4,045 | rtx4090 | 247 | 17% |

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
| wide (<30%) | 28 |
| concentrated (30–60%) | 20 |
| dominated (60–90%) | 26 |
| captured (>90%) | 21 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 96 |
| README keywords (GUESS) | 13 |
| min_compute.yml (curated) | 10 |
| code-submission (validator runs it) | 8 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-10-22T18:06 | sn1 | RELEASE | sn1 released v4.4.15 |
| 2026-10-22T18:06 | sn6 | README_TASK_DIFF | sn6 README task/scoring sections changed |
| 2026-10-22T18:06 | sn12 | RELEASE | sn12 released miner-staging-2026-10-22-39790980356-423-1: fix: securit |
| 2026-10-22T18:06 | sn15 | RELEASE | sn15 released v3.0.0 |
| 2026-10-22T18:06 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: fix(scoring): the outcomes reader keeps e |
| 2026-10-22T18:06 | sn25 | RELEASE | sn25 released v2026.10.22-1078873780 |
| 2026-10-22T18:06 | sn51 | RELEASE | sn51 released executor-v1.151 |
| 2026-10-22T18:06 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-4983 - Validator: a failed edit's und |
| 2026-10-22T18:06 | sn76 | RELEASE | sn76 released v0.0.3 |
| 2026-10-22T18:06 | sn76 | SCORING_COMMIT | sn76 commit touches scoring: Allow manual CI verification after reposi |
| 2026-10-22T18:06 | sn76 | README_TASK_DIFF | sn76 README task/scoring sections changed |
| 2026-10-22T18:06 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: Merge pull request #387: evaluation feed  |
| 2026-10-22T18:06 | sn117 | RELEASE | sn117 released everycli v0.7.1 |
| 2026-10-22T18:06 | sn117 | README_TASK_DIFF | sn117 README task/scoring sections changed |
| 2026-10-22T13:13 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: Validator v3: world packs on oro-env-runt |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

