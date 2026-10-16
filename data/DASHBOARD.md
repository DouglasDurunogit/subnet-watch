# Subnet watch — dashboard

_snapshot 2026-10-16T23:58:52Z · block 9299376 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 54 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 99 | `miner_burn` < 0.99 |
| Ranked | 99 | passed every gate |
| **Positive margin** | **54** | income beats machine cost |
| New events this window | 5 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 67 | `████████████████████████████` |
| 0–0.2 | 5 | `██` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 7 | `███` |
| 0.6–0.8 | 10 | `████` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 29 | `████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn3 Teutonic | 74.7 | 2,985 | 2,985 = | rtx4090* | 5 | 40% |
| 2 | sn41 Almanac | 74.3 | 38.21 | 121 | cpu-small | 114 | 9% |
| 3 | sn53 engy | 69.4 | 620 | 2,576 | rtx4090 | 24 | 16% |
| 4 | sn91 cascade | 69.1 | 220 | 883 | cpu-small | 5 | 52% |
| 5 | sn1 Apex | 68.9 | 538 | 1,077 | rtx4090* | 5 | 58% |
| 6 | sn67 Harnyx | 68.7 | 8.76 | 8.76 = | cpu-small | 222 | 17% |
| 7 | sn82 Noah | 68.4 | 716 | 716 = | rtx4090* | 64 | 2% |
| 8 | sn58 Attune | 68.1 | 426 | 687 | rtx4090* | 5 | 71% |
| 9 | sn107 Minos | 67.8 | 271 | 23,023 | cpu-small | 20 | 80% |
| 10 | sn15 ORO | 67.6 | 8.17 | 16.80 | cpu-small | 66 | 97% |
| 11 | sn4 Targon | 66.9 | 10,104 | 29,791 | rtx4090* | 5 | 70% |
| 12 | sn14 Cacheon | 65.2 | 179 | 1,894 | rtx4090* | 9 | 52% |
| 13 | sn62 Ridges | 63.9 | 118 | 1,220 | rtx4090* | 39 | 17% |
| 14 | sn66 conjectures | 63.8 | 117 | 242 | rtx4090* | 4 | 80% |
| 15 | sn92 REAX | 62.6 | 109 | 337 | rtx4090 | 233 | 1% |
| 16 | sn28 SayGM | 62.6 | 81.99 | 1,291 | rtx4090* | 94 | 43% |
| 17 | sn120 Affine | 62.4 | 89.64 | 925 | rtx4090* | 159 | 3% |
| 18 | sn61 RedTeam | 61.1 | 51.80 | 85.86 | rtx4090* | 137 | 1% |
| 19 | sn81 Reliquary | 58.7 | 24.60 | 263 | rtx4090* | 16 | 73% |
| 20 | sn80 OpenRoboto | 58.6 | 857 | 3,745 | rtx4090* | 10 | 35% |

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
| wide (<30%) | 24 |
| concentrated (30–60%) | 23 |
| dominated (60–90%) | 27 |
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
| 2026-10-16T23:59 | sn25 | RELEASE | sn25 released v2026.10.16-1073891640 |
| 2026-10-16T23:59 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Move scorer checkpoint and output IO behi |
| 2026-10-16T23:59 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Score original forecast ranges and retain |
| 2026-10-16T23:59 | sn116 | RELEASE | sn116 released worker-images-v5 (DEVELOPMENT) |
| 2026-10-16T23:59 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Format F06 Challenge registry assertions |
| 2026-10-16T21:47 | sn25 | RELEASE | sn25 released v2026.10.16-1073843780 |
| 2026-10-16T21:47 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Authenticate finalized chain absence befo |
| 2026-10-16T21:47 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Select verified homepage profile for unbo |
| 2026-10-16T21:47 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: Merge pull request #370 from TensorLink-A |
| 2026-10-16T21:47 | sn92 | RELEASE | sn92 released v1.2.0-rc7 |
| 2026-10-16T21:47 | sn97 | BURN_DROP | sn97 burn fell 1.000 -> 0.600 - miners can earn again |
| 2026-10-16T21:47 | sn102 | RELEASE | sn102 released v0.7.1 |
| 2026-10-16T21:47 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Merge pull request #1408 from carbonphys |
| 2026-10-16T18:46 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Allow selected frozen executions in isola |
| 2026-10-16T18:46 | sn92 | RELEASE | sn92 released v1.2.0-rc6 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

