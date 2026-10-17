# Subnet watch — dashboard

_snapshot 2026-10-17T12:28:13Z · block 9303123 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 60 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 99 | `miner_burn` < 0.99 |
| Ranked | 99 | passed every gate |
| **Positive margin** | **60** | income beats machine cost |
| New events this window | 5 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 65 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 6 | `███` |
| 0.6–0.8 | 10 | `████` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 29 | `████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn41 Almanac | 76.1 | 60.32 | 101 | cpu-small | 120 | 6% |
| 2 | sn3 Teutonic | 74.6 | 2,948 | 2,948 = | rtx4090* | 5 | 40% |
| 3 | sn102 ConnitoAI | 71.3 | 1,093 | 1,093 = | rtx4090* | 4 | 25% |
| 4 | sn53 engy | 69.4 | 612 | 2,543 | rtx4090 | 24 | 16% |
| 5 | sn91 cascade | 69 | 214 | 861 | cpu-small | 5 | 52% |
| 6 | sn1 Apex | 68.7 | 500 | 986 | rtx4090* | 5 | 53% |
| 7 | sn82 Noah | 68.2 | 666 | 666 = | rtx4090* | 64 | 2% |
| 8 | sn58 Attune | 68 | 419 | 675 | rtx4090* | 5 | 71% |
| 9 | sn67 Harnyx | 68 | 7.51 | 155 | cpu-small | 176 | 9% |
| 10 | sn107 Minos | 67.7 | 266 | 22,580 | cpu-small | 20 | 80% |
| 11 | sn15 ORO | 67.6 | 8.34 | 16.38 | cpu-small | 64 | 97% |
| 12 | sn4 Targon | 66.8 | 9,969 | 29,393 | rtx4090* | 5 | 70% |
| 13 | sn14 Cacheon | 66.3 | 244 | 1,875 | rtx4090* | 9 | 53% |
| 14 | sn66 conjectures | 63.9 | 118 | 245 | rtx4090* | 4 | 80% |
| 15 | sn92 REAX | 63.7 | 140 | 245 | rtx4090 | 217 | 1% |
| 16 | sn54 Yanez | 62.9 | 4.43 | 6.60 | a4000 | 15 | 67% |
| 17 | sn120 Affine | 62.6 | 93.82 | 758 | rtx4090* | 178 | 2% |
| 18 | sn97 Ingot | 61.6 | 2,097 | 2,097 = | rtx4090* | 4 | 40% |
| 19 | sn61 RedTeam | 61.4 | 57.14 | 95.46 | rtx4090* | 129 | 1% |
| 20 | sn81 Reliquary | 60.5 | 43.13 | 256 | rtx4090* | 18 | 72% |

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
| 2026-10-17T12:28 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: feat(scoring): absence charges stop once  |
| 2026-10-17T12:28 | sn25 | RELEASE | sn25 released v2026.10.17-1074370910 |
| 2026-10-17T12:28 | sn51 | RELEASE | sn51 released executor-v1.142 |
| 2026-10-17T12:28 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: Sysbox installer: show the verify contain |
| 2026-10-17T12:28 | sn92 | RELEASE | sn92 released v1.2.0-rc7.post4 |
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

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

