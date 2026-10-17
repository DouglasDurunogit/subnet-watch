# Subnet watch — dashboard

_snapshot 2026-10-17T08:42:55Z · block 9301996 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 55 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 99 | `miner_burn` < 0.99 |
| Ranked | 99 | passed every gate |
| **Positive margin** | **55** | income beats machine cost |
| New events this window | 12 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 66 | `████████████████████████████` |
| 0–0.2 | 6 | `███` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 6 | `███` |
| 0.6–0.8 | 10 | `████` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 29 | `████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn41 Almanac | 76.4 | 65.63 | 105 | cpu-small | 119 | 6% |
| 2 | sn3 Teutonic | 74.6 | 2,981 | 2,981 = | rtx4090* | 5 | 40% |
| 3 | sn53 engy | 69.3 | 606 | 2,518 | rtx4090 | 24 | 16% |
| 4 | sn91 cascade | 69 | 216 | 868 | cpu-small | 5 | 52% |
| 5 | sn1 Apex | 68.8 | 521 | 1,027 | rtx4090* | 5 | 52% |
| 6 | sn102 ConnitoAI | 68.6 | 488 | 1,283 | rtx4090* | 8 | 29% |
| 7 | sn67 Harnyx | 68.3 | 8.00 | 145 | cpu-small | 168 | 16% |
| 8 | sn82 Noah | 68.2 | 675 | 675 = | rtx4090* | 64 | 2% |
| 9 | sn58 Attune | 68.1 | 421 | 679 | rtx4090* | 5 | 71% |
| 10 | sn107 Minos | 67.8 | 268 | 22,789 | cpu-small | 20 | 80% |
| 11 | sn15 ORO | 67.7 | 8.40 | 16.48 | cpu-small | 64 | 97% |
| 12 | sn4 Targon | 66.9 | 10,121 | 29,842 | rtx4090* | 5 | 70% |
| 13 | sn14 Cacheon | 65.2 | 178 | 1,889 | rtx4090* | 9 | 52% |
| 14 | sn66 conjectures | 63.9 | 119 | 247 | rtx4090* | 4 | 80% |
| 15 | sn92 REAX | 63.7 | 138 | 249 | rtx4090 | 230 | 1% |
| 16 | sn28 SayGM | 62.3 | 76.80 | 1,836 | rtx4090* | 97 | 31% |
| 17 | sn97 Ingot | 61.6 | 2,119 | 2,119 = | rtx4090* | 4 | 40% |
| 18 | sn61 RedTeam | 61.4 | 56.90 | 95.05 | rtx4090* | 130 | 1% |
| 19 | sn120 Affine | 60.5 | 53.70 | 895 | rtx4090* | 177 | 3% |
| 20 | sn81 Reliquary | 59.9 | 35.95 | 273 | rtx4090* | 18 | 71% |

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
| concentrated (30–60%) | 23 |
| dominated (60–90%) | 26 |
| captured (>90%) | 24 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 95 |
| README keywords (GUESS) | 13 |
| min_compute.yml (curated) | 10 |
| code-submission (validator runs it) | 9 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-10-17T08:43 | sn15 | RELEASE | sn15 released v2.5.5: Bound validator reads of sandbox output files (# |
| 2026-10-17T08:43 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: Bound validator reads of sandbox output f |
| 2026-10-17T08:43 | sn25 | RELEASE | sn25 released v2026.10.16-1074191560 |
| 2026-10-17T08:43 | sn37 | SCORING_COMMIT | sn37 commit touches scoring: fix(miner): enable reviewed runtime479 fu |
| 2026-10-17T08:43 | sn37 | README_TASK_DIFF | sn37 README task/scoring sections changed |
| 2026-10-17T08:43 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-4280 - [P0] Validator: cross-check th |
| 2026-10-17T08:43 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: fix(arena): retain verified source redire |
| 2026-10-17T08:43 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Merge pull request #294 from Umi-BitSign/ |
| 2026-10-17T08:43 | sn92 | RELEASE | sn92 released v1.2.0-rc7.post3 |
| 2026-10-17T08:43 | sn108 | SCORING_COMMIT | sn108 commit touches scoring: Validators don't pay records the server  |
| 2026-10-17T08:43 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Merge pull request #1416 from carbonphys |
| 2026-10-17T08:43 | sn120 | MECHANISM_ADDED | sn120 now runs 2 incentive mechanisms (was 1) |
| 2026-10-17T04:17 | sn25 | RELEASE | sn25 released v2026.10.16-1074037020 |
| 2026-10-17T04:17 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Merge current main and validate selected  |
| 2026-10-17T04:17 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: fix(promotion): anchor the trainer's reig |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

