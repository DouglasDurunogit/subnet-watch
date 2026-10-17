# Subnet watch — dashboard

_snapshot 2026-10-17T04:16:44Z · block 9300665 · run_status **ok**_

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
| New events this window | 4 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 67 | `████████████████████████████` |
| 0–0.2 | 5 | `██` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 6 | `███` |
| 0.6–0.8 | 10 | `████` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 29 | `████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn3 Teutonic | 74.6 | 2,978 | 2,978 = | rtx4090* | 5 | 40% |
| 2 | sn41 Almanac | 74.2 | 38.18 | 120 | cpu-small | 118 | 10% |
| 3 | sn53 engy | 69.3 | 608 | 2,529 | rtx4090 | 24 | 16% |
| 4 | sn91 cascade | 69.1 | 219 | 879 | cpu-small | 5 | 52% |
| 5 | sn1 Apex | 68.9 | 530 | 1,045 | rtx4090* | 5 | 51% |
| 6 | sn67 Harnyx | 68.7 | 8.70 | 8.70 = | cpu-small | 221 | 18% |
| 7 | sn82 Noah | 68.2 | 674 | 674 = | rtx4090* | 64 | 2% |
| 8 | sn58 Attune | 68.1 | 424 | 683 | rtx4090* | 5 | 71% |
| 9 | sn107 Minos | 67.8 | 269 | 22,897 | cpu-small | 20 | 80% |
| 10 | sn15 ORO | 67.2 | 7.48 | 15.42 | cpu-small | 65 | 97% |
| 11 | sn4 Targon | 66.9 | 10,101 | 29,783 | rtx4090* | 5 | 70% |
| 12 | sn14 Cacheon | 65.2 | 178 | 1,888 | rtx4090* | 9 | 52% |
| 13 | sn28 SayGM | 64.4 | 143 | 2,595 | rtx4090* | 96 | 19% |
| 14 | sn66 conjectures | 63.9 | 118 | 244 | rtx4090* | 4 | 80% |
| 15 | sn92 REAX | 63.6 | 134 | 299 | rtx4090 | 229 | 1% |
| 16 | sn97 Ingot | 61.6 | 2,116 | 2,116 = | rtx4090* | 4 | 40% |
| 17 | sn61 RedTeam | 61.2 | 54.19 | 90.86 | rtx4090* | 133 | 1% |
| 18 | sn120 Affine | 61 | 59.76 | 919 | rtx4090* | 174 | 3% |
| 19 | sn81 Reliquary | 60.5 | 42.56 | 274 | rtx4090* | 18 | 72% |
| 20 | sn80 OpenRoboto | 58.6 | 848 | 3,704 | rtx4090* | 10 | 35% |

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
| concentrated (30–60%) | 24 |
| dominated (60–90%) | 25 |
| captured (>90%) | 25 |

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
| 2026-10-17T04:17 | sn25 | RELEASE | sn25 released v2026.10.16-1074037020 |
| 2026-10-17T04:17 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Merge current main and validate selected  |
| 2026-10-17T04:17 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: fix(promotion): anchor the trainer's reig |
| 2026-10-17T04:17 | sn92 | RELEASE | sn92 released v1.2.0-rc7.post1 |
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

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

