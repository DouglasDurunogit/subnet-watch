# Subnet watch — dashboard

_snapshot 2026-10-24T14:44:37Z · block 9354124 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 55 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 98 | `miner_burn` < 0.99 |
| Ranked | 98 | passed every gate |
| **Positive margin** | **55** | income beats machine cost |
| New events this window | 1 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 67 | `████████████████████████████` |
| 0–0.2 | 6 | `███` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 6 | `███` |
| 0.6–0.8 | 8 | `███` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 30 | `█████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn3 Teutonic | 73.4 | 2,069 | 4,146 | rtx4090* | 7 | 25% |
| 2 | sn97 Ingot | 73 | 1,808 | 1,808 = | rtx4090* | 5 | 20% |
| 3 | sn56 Gradients | 71.2 | 1,045 | 5,659 | rtx4090* | 6 | 51% |
| 4 | sn41 Almanac | 69 | 10.88 | 127 | cpu-small | 166 | 2% |
| 5 | sn1 Apex | 68 | 405 | 862 | rtx4090* | 5 | 56% |
| 6 | sn46 Instant | 68 | 159 | 169 | cpu-small | 15 | 7% |
| 7 | sn82 Noah | 67.7 | 600 | 604 | rtx4090* | 63 | 2% |
| 8 | sn67 Harnyx | 67.1 | 5.98 | 291 | cpu-small | 187 | 14% |
| 9 | sn53 engy | 66.9 | 293 | 2,406 | rtx4090 | 36 | 11% |
| 10 | sn107 Minos | 66.9 | 216 | 18,394 | cpu-small | 20 | 80% |
| 11 | sn125 Refinery | 66.6 | 267 | 901 | rtx4090* | 4 | 50% |
| 12 | sn120 Affine | 65.7 | 220 | 1,849 | rtx4090* | 89 | 6% |
| 13 | sn66 conjectures | 63.3 | 99.31 | 207 | rtx4090* | 4 | 80% |
| 14 | sn15 ORO | 63.2 | 5.06 | 14,402 | cpu-small | 45 | 98% |
| 15 | sn62 Ridges | 63 | 91.80 | 1,089 | rtx4090* | 43 | 17% |
| 16 | sn23 Trishool | 62.5 | 1,063 | 1,063 = | cpu-small | 2 | 80% |
| 17 | sn81 Reliquary | 61.7 | 60.67 | 363 | rtx4090* | 19 | 50% |
| 18 | sn55 NIOME | 61.6 | 59.75 | 502 | rtx4090* | 11 | 30% |
| 19 | sn28 SayGM | 60 | 38.42 | 1,232 | rtx4090* | 129 | 31% |
| 20 | sn111 Claims | 58.9 | 26.88 | 2,625 | rtx4090* | 6 | 90% |

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
| wide (<30%) | 29 |
| concentrated (30–60%) | 19 |
| dominated (60–90%) | 25 |
| captured (>90%) | 25 |

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
| 2026-10-24T14:45 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: Merge pull request #413 from reliquadotai |
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

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

