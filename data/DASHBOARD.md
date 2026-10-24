# Subnet watch — dashboard

_snapshot 2026-10-24T06:10:29Z · block 9351553 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 57 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 97 | `miner_burn` < 0.99 |
| Ranked | 97 | passed every gate |
| **Positive margin** | **57** | income beats machine cost |
| New events this window | 4 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 66 | `████████████████████████████` |
| 0–0.2 | 6 | `███` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 31 | `█████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn3 Teutonic | 73.5 | 2,110 | 4,228 | rtx4090* | 7 | 25% |
| 2 | sn97 Ingot | 73 | 1,837 | 1,837 = | rtx4090* | 5 | 20% |
| 3 | sn56 Gradients | 71.2 | 1,061 | 5,747 | rtx4090* | 6 | 51% |
| 4 | sn41 Almanac | 68.8 | 10.47 | 123 | cpu-small | 166 | 2% |
| 5 | sn1 Apex | 68.2 | 429 | 912 | rtx4090* | 5 | 54% |
| 6 | sn82 Noah | 67.7 | 617 | 622 | rtx4090* | 63 | 2% |
| 7 | sn46 Instant | 67.7 | 145 | 175 | cpu-small | 16 | 7% |
| 8 | sn67 Harnyx | 67.3 | 6.15 | 297 | cpu-small | 178 | 14% |
| 9 | sn107 Minos | 67.2 | 233 | 18,668 | cpu-small | 20 | 79% |
| 10 | sn53 engy | 67 | 306 | 2,506 | rtx4090 | 36 | 11% |
| 11 | sn125 Refinery | 66.6 | 272 | 917 | rtx4090* | 4 | 50% |
| 12 | sn120 Affine | 66.2 | 250 | 2,814 | rtx4090* | 61 | 9% |
| 13 | sn104 TAOstatus | 65.6 | 2,705 | 2,705 = | cpu-small | 1 | 100% |
| 14 | sn15 ORO | 64.3 | 5.04 | 14,651 | cpu-small | 44 | 98% |
| 15 | sn66 conjectures | 63.4 | 103 | 214 | rtx4090* | 4 | 80% |
| 16 | sn62 Ridges | 63.1 | 93.60 | 1,109 | rtx4090* | 43 | 17% |
| 17 | sn23 Trishool | 62.5 | 1,064 | 1,064 = | cpu-small | 2 | 80% |
| 18 | sn34 BitMind | 61.9 | 987 | 8,611 | a100-80 | 3 | 85% |
| 19 | sn55 NIOME | 61.6 | 59.46 | 500 | rtx4090* | 11 | 30% |
| 20 | sn117 everyframe.studi | 61 | 50.45 | 138 | rtx4090* | 7 | 64% |

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
| concentrated (30–60%) | 19 |
| dominated (60–90%) | 29 |
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
| 2026-10-24T06:11 | sn2 | SCORING_COMMIT | sn2 commit touches scoring: Document localnet validator operation and  |
| 2026-10-24T06:11 | sn62 | RELEASE | sn62 released v0.3.12 |
| 2026-10-24T06:11 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Keep degraded proxy events clear of scori |
| 2026-10-24T06:11 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Merge pull request #378 from Umi-BitSign/ |
| 2026-10-24T01:10 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Bind headcount release to committed prote |
| 2026-10-24T01:10 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Keep central model evaluations out of aut |
| 2026-10-24T01:10 | sn117 | RELEASE | sn117 released everycli v0.7.4 |
| 2026-10-23T22:32 | sn7 | BURN_DROP | sn7 burn fell 0.991 -> 0.985 - miners can earn again |
| 2026-10-23T22:32 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Preserve the failed primary-intent reason |
| 2026-10-23T22:32 | sn76 | BURN_DROP | sn76 burn fell 0.992 -> 0.987 - miners can earn again |
| 2026-10-23T22:32 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Retain bounded model pairs and finish res |
| 2026-10-23T22:32 | sn117 | RELEASE | sn117 released everycli v0.7.3 |
| 2026-10-23T19:26 | sn8 | SCORING_COMMIT | sn8 commit touches scoring: Optimizations for miner statistics (#964) |
| 2026-10-23T19:26 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: fix(scoring): only real scored entries co |
| 2026-10-23T19:26 | sn22 | SCORING_COMMIT | sn22 commit touches scoring: fix(bot): open a fresh connection for eac |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

