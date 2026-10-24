# Subnet watch — dashboard

_snapshot 2026-10-24T22:25:50Z · block 9356430 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 54 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 96 | `miner_burn` < 0.99 |
| Ranked | 96 | passed every gate |
| **Positive margin** | **54** | income beats machine cost |
| New events this window | 1 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 65 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 6 | `███` |
| 0.6–0.8 | 8 | `███` |
| 0.8–0.99 | 4 | `██` |
| ≥0.99 dead | 32 | `██████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn3 Teutonic | 73.4 | 2,075 | 4,158 | rtx4090* | 7 | 25% |
| 2 | sn97 Ingot | 73 | 1,789 | 1,789 = | rtx4090* | 5 | 20% |
| 3 | sn56 Gradients | 71.1 | 1,040 | 5,635 | rtx4090* | 6 | 51% |
| 4 | sn41 Almanac | 69.1 | 11.08 | 129 | cpu-small | 166 | 2% |
| 5 | sn1 Apex | 68.3 | 444 | 896 | rtx4090* | 5 | 52% |
| 6 | sn82 Noah | 67.7 | 594 | 599 | rtx4090* | 63 | 2% |
| 7 | sn67 Harnyx | 67.4 | 5.98 | 290 | cpu-small | 193 | 14% |
| 8 | sn53 engy | 66.9 | 290 | 2,379 | rtx4090 | 36 | 11% |
| 9 | sn107 Minos | 66.9 | 216 | 18,346 | cpu-small | 20 | 80% |
| 10 | sn125 Refinery | 66.4 | 252 | 853 | rtx4090* | 4 | 50% |
| 11 | sn104 TAOstatus | 65.6 | 2,666 | 2,666 = | cpu-small | 1 | 100% |
| 12 | sn120 Affine | 65.5 | 208 | 1,456 | rtx4090* | 95 | 5% |
| 13 | sn46 Instant | 64.7 | 59.47 | 73.12 | cpu-small | 17 | 50% |
| 14 | sn15 ORO | 64.7 | 5.04 | 14,369 | cpu-small | 45 | 98% |
| 15 | sn81 Reliquary | 63.6 | 110 | 336 | rtx4090* | 19 | 33% |
| 16 | sn66 conjectures | 63.3 | 99.32 | 207 | rtx4090* | 4 | 80% |
| 17 | sn62 Ridges | 63 | 92.30 | 1,094 | rtx4090* | 43 | 17% |
| 18 | sn23 Trishool | 62.6 | 1,086 | 1,086 = | cpu-small | 2 | 80% |
| 19 | sn28 SayGM | 62.1 | 70.61 | 1,369 | rtx4090* | 142 | 17% |
| 20 | sn55 NIOME | 61.7 | 62.34 | 521 | rtx4090* | 11 | 30% |

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
| 2026-10-24T22:26 | sn25 | RELEASE | sn25 released v2026.10.24-1080739690 |
| 2026-10-24T19:51 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Keep threshold shape validation on failed |
| 2026-10-24T19:51 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: Merge pull request #416 from reliquadotai |
| 2026-10-24T19:51 | sn117 | BURN_DROP | sn117 burn fell 1.000 -> 0.926 - miners can earn again |
| 2026-10-24T17:39 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Preserve source metadata and validated co |
| 2026-10-24T17:39 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Reset evaluation forecasts when evaluator |
| 2026-10-24T14:45 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: Merge pull request #413 from reliquadotai |
| 2026-10-24T11:23 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: docs(scoring): the measurement amendment  |
| 2026-10-24T11:23 | sn62 | RELEASE | sn62 released v0.3.13 |
| 2026-10-24T11:23 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: fix(rl-price): level mode moves per hour, |
| 2026-10-24T06:11 | sn2 | SCORING_COMMIT | sn2 commit touches scoring: Document localnet validator operation and  |
| 2026-10-24T06:11 | sn62 | RELEASE | sn62 released v0.3.12 |
| 2026-10-24T06:11 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Keep degraded proxy events clear of scori |
| 2026-10-24T06:11 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Merge pull request #378 from Umi-BitSign/ |
| 2026-10-24T01:10 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Bind headcount release to committed prote |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

