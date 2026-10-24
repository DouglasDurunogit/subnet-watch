# Subnet watch — dashboard

_snapshot 2026-10-24T11:23:11Z · block 9353117 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 55 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 97 | `miner_burn` < 0.99 |
| Ranked | 97 | passed every gate |
| **Positive margin** | **55** | income beats machine cost |
| New events this window | 3 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 67 | `████████████████████████████` |
| 0–0.2 | 6 | `███` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 5 | `██` |
| ≥0.99 dead | 31 | `█████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn3 Teutonic | 73.4 | 2,082 | 4,173 | rtx4090* | 7 | 25% |
| 2 | sn97 Ingot | 73 | 1,796 | 1,796 = | rtx4090* | 5 | 20% |
| 3 | sn56 Gradients | 71.2 | 1,051 | 5,691 | rtx4090* | 6 | 51% |
| 4 | sn41 Almanac | 69 | 10.73 | 126 | cpu-small | 166 | 2% |
| 5 | sn1 Apex | 68 | 414 | 880 | rtx4090* | 5 | 55% |
| 6 | sn82 Noah | 67.8 | 610 | 614 | rtx4090* | 63 | 2% |
| 7 | sn46 Instant | 67.7 | 144 | 177 | cpu-small | 16 | 8% |
| 8 | sn67 Harnyx | 67.3 | 6.04 | 293 | cpu-small | 184 | 14% |
| 9 | sn53 engy | 66.9 | 297 | 2,434 | rtx4090 | 36 | 11% |
| 10 | sn107 Minos | 66.9 | 219 | 18,667 | cpu-small | 20 | 80% |
| 11 | sn120 Affine | 66.8 | 302 | 2,693 | rtx4090* | 60 | 9% |
| 12 | sn125 Refinery | 66.6 | 268 | 907 | rtx4090* | 4 | 50% |
| 13 | sn66 conjectures | 63.3 | 99.98 | 208 | rtx4090* | 4 | 80% |
| 14 | sn62 Ridges | 63 | 92.54 | 1,097 | rtx4090* | 43 | 17% |
| 15 | sn15 ORO | 62.7 | 4.99 | 14,534 | cpu-small | 44 | 98% |
| 16 | sn23 Trishool | 62.6 | 1,083 | 1,083 = | cpu-small | 2 | 80% |
| 17 | sn34 BitMind | 61.9 | 980 | 8,556 | a100-80 | 3 | 85% |
| 18 | sn55 NIOME | 61.6 | 59.21 | 498 | rtx4090* | 11 | 30% |
| 19 | sn81 Reliquary | 60.1 | 37.47 | 244 | rtx4090* | 19 | 70% |
| 20 | sn28 SayGM | 59.9 | 37.57 | 1,275 | rtx4090* | 128 | 29% |

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
| wide (<30%) | 30 |
| concentrated (30–60%) | 18 |
| dominated (60–90%) | 27 |
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
| 2026-10-24T11:23 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: docs(scoring): the measurement amendment  |
| 2026-10-24T11:23 | sn62 | RELEASE | sn62 released v0.3.13 |
| 2026-10-24T11:23 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: fix(rl-price): level mode moves per hour, |
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

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

