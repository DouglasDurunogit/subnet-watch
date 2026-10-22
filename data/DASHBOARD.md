# Subnet watch — dashboard

_snapshot 2026-10-22T21:32:08Z · block 9341761 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 53 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 96 | `miner_burn` < 0.99 |
| Ranked | 96 | passed every gate |
| **Positive margin** | **53** | income beats machine cost |
| New events this window | 4 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 66 | `████████████████████████████` |
| 0–0.2 | 5 | `██` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 6 | `███` |
| 0.6–0.8 | 11 | `█████` |
| 0.8–0.99 | 4 | `██` |
| ≥0.99 dead | 32 | `██████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn121 sundae_bar | 74.5 | 1,087 | 1,087 = | cpu-small | 2 | 60% |
| 2 | sn3 Teutonic | 73.6 | 2,166 | 2,956 | rtx4090* | 5 | 46% |
| 3 | sn67 Harnyx | 73.1 | 27.47 | 260 | cpu-small | 46 | 11% |
| 4 | sn1 Apex | 68.5 | 471 | 943 | rtx4090* | 5 | 52% |
| 5 | sn82 Noah | 67.9 | 602 | 619 | rtx4090* | 62 | 2% |
| 6 | sn56 Gradients | 67.3 | 327 | 5,233 | rtx4090* | 9 | 46% |
| 7 | sn107 Minos | 67.2 | 233 | 19,444 | cpu-small | 20 | 80% |
| 8 | sn53 engy | 67 | 299 | 2,655 | rtx4090 | 36 | 11% |
| 9 | sn125 Refinery | 66.8 | 283 | 930 | rtx4090* | 4 | 50% |
| 10 | sn15 ORO | 65.1 | 8.64 | 14,680 | cpu-small | 75 | 95% |
| 11 | sn120 Affine | 63.7 | 128 | 511 | rtx4090* | 179 | 2% |
| 12 | sn66 conjectures | 63.3 | 98.49 | 205 | rtx4090* | 4 | 81% |
| 13 | sn55 NIOME | 61.7 | 60.68 | 509 | rtx4090* | 11 | 30% |
| 14 | sn34 BitMind | 61.6 | 897 | 7,848 | a100-80 | 3 | 85% |
| 15 | sn41 Almanac | 59.9 | 1.96 | 133 | cpu-small | 158 | 3% |
| 16 | sn92 REAX | 59.5 | 48.34 | 3,980 | rtx4090 | 226 | 17% |
| 17 | sn111 Claims | 59.3 | 30.61 | 2,771 | rtx4090* | 6 | 90% |
| 18 | sn80 OpenRoboto | 58.8 | 903 | 3,807 | rtx4090* | 11 | 25% |
| 19 | sn4 Targon | 57.7 | 9,513 | 28,047 | rtx4090* | 5 | 70% |
| 20 | sn117 everyframe.studi | 57.7 | 19.25 | 45.22 | rtx4090* | 10 | 85% |

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
| dominated (60–90%) | 25 |
| captured (>90%) | 23 |

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
| 2026-10-22T21:32 | sn7 | BURN_DROP | sn7 burn fell 0.990 -> 0.986 - miners can earn again |
| 2026-10-22T21:32 | sn13 | RELEASE | sn13 released Release v1.18.75 |
| 2026-10-22T21:32 | sn66 | RELEASE | sn66 released v2026.10.22.2 |
| 2026-10-22T21:32 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Merge pull request #705 from leadpoet/fix |
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

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

