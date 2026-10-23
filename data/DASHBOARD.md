# Subnet watch — dashboard

_snapshot 2026-10-23T00:12:08Z · block 9342561 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 53 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 97 | `miner_burn` < 0.99 |
| Ranked | 97 | passed every gate |
| **Positive margin** | **53** | income beats machine cost |
| New events this window | 3 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 66 | `████████████████████████████` |
| 0–0.2 | 5 | `██` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 7 | `███` |
| 0.6–0.8 | 10 | `████` |
| 0.8–0.99 | 5 | `██` |
| ≥0.99 dead | 31 | `█████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn121 sundae_bar | 74.5 | 1,086 | 1,086 = | cpu-small | 2 | 60% |
| 2 | sn3 Teutonic | 73.5 | 2,147 | 2,931 | rtx4090* | 5 | 45% |
| 3 | sn67 Harnyx | 73.1 | 27.21 | 258 | cpu-small | 46 | 11% |
| 4 | sn1 Apex | 68.4 | 464 | 928 | rtx4090* | 5 | 52% |
| 5 | sn82 Noah | 67.9 | 610 | 626 | rtx4090* | 62 | 2% |
| 6 | sn56 Gradients | 67.3 | 326 | 5,224 | rtx4090* | 9 | 46% |
| 7 | sn107 Minos | 67.2 | 234 | 19,444 | cpu-small | 20 | 80% |
| 8 | sn53 engy | 67 | 303 | 2,693 | rtx4090 | 36 | 11% |
| 9 | sn125 Refinery | 66.8 | 281 | 922 | rtx4090* | 4 | 50% |
| 10 | sn120 Affine | 63.1 | 108 | 498 | rtx4090* | 178 | 2% |
| 11 | sn66 conjectures | 62.6 | 81.33 | 185 | rtx4090* | 4 | 84% |
| 12 | sn55 NIOME | 61.7 | 60.88 | 510 | rtx4090* | 11 | 30% |
| 13 | sn34 BitMind | 61.6 | 895 | 7,834 | a100-80 | 3 | 85% |
| 14 | sn41 Almanac | 60.8 | 2.23 | 134 | cpu-small | 159 | 3% |
| 15 | sn111 Claims | 59.3 | 30.30 | 2,749 | rtx4090* | 6 | 90% |
| 16 | sn92 REAX | 59 | 52.16 | 4,117 | rtx4090 | 225 | 17% |
| 17 | sn80 OpenRoboto | 58.8 | 904 | 3,813 | rtx4090* | 11 | 25% |
| 18 | sn28 SayGM | 57.8 | 20.48 | 1,429 | rtx4090* | 123 | 33% |
| 19 | sn117 everyframe.studi | 57.8 | 19.54 | 37.69 | rtx4090* | 10 | 82% |
| 20 | sn4 Targon | 57.7 | 9,447 | 27,887 | rtx4090* | 5 | 70% |

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
| concentrated (30–60%) | 22 |
| dominated (60–90%) | 26 |
| captured (>90%) | 22 |

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
| 2026-10-23T00:12 | sn28 | RELEASE | sn28 released v0.5.10-dev |
| 2026-10-23T00:12 | sn28 | SCORING_COMMIT | sn28 commit touches scoring: chore(release): gm-miner 0.5.10-dev (#347 |
| 2026-10-23T00:12 | sn81 | BURN_DROP | sn81 burn fell 0.996 -> 0.810 - miners can earn again |
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

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

