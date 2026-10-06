# Subnet watch — dashboard

_snapshot 2026-10-06T19:07:23Z · block 9225924 · run_status **ok**_

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
| New events this window | 13 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 66 | `████████████████████████████` |
| 0–0.2 | 6 | `███` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 7 | `███` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 29 | `████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn26 Perturb | 79.7 | 376 | 1,274 | rtx3060 | 4 | 60% |
| 2 | sn41 Almanac | 73.5 | 31.94 | 123 | cpu-small | 133 | 2% |
| 3 | sn91 cascade | 72.1 | 531 | 2,127 | cpu-small | 5 | 52% |
| 4 | sn67 Harnyx | 70.3 | 13.02 | 1,075 | cpu-small | 138 | 35% |
| 5 | sn1 Apex | 69.2 | 575 | 922 | rtx4090* | 4 | 69% |
| 6 | sn46 Instant | 69.2 | 227 | 285 | cpu-small | 8 | 50% |
| 7 | sn120 Affine | 68.8 | 583 | 880 | rtx4090* | 65 | 2% |
| 8 | sn80 OpenRoboto | 68.5 | 472 | 2,135 | rtx4090* | 8 | 25% |
| 9 | sn4 Targon | 67.1 | 10,903 | 32,146 | rtx4090* | 5 | 70% |
| 10 | sn111 Claims | 66.9 | 293 | 2,628 | rtx4090* | 5 | 70% |
| 11 | sn62 Ridges | 64 | 122 | 1,609 | rtx4090* | 33 | 19% |
| 12 | sn15 ORO | 63.9 | 8.65 | 17.29 | cpu-small | 52 | 98% |
| 13 | sn23 Trishool | 62.8 | 1,155 | 1,155 = | cpu-small | 2 | 76% |
| 14 | sn65 True Performance | 62.5 | 84.46 | 177 | rtx4090* | 6 | 75% |
| 15 | sn61 RedTeam | 62.1 | 72.55 | 115 | rtx4090* | 134 | 1% |
| 16 | sn14 Cacheon | 60.7 | 46.06 | 1,047 | rtx4090* | 7 | 84% |
| 17 | sn53 engy | 60.3 | 1,424 | 3,901 | rtx4090 | 14 | 22% |
| 18 | sn74 Gittensor | 58.6 | 27.22 | 273 | rtx4090* | 21 | 50% |
| 19 | sn5 Hone | 58.2 | 38.00 | 41.99 | rtx4090* | 245 | 0% |
| 20 | sn107 Minos | 58.1 | 326 | 27,042 | cpu-small | 20 | 79% |

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
| dominated (60–90%) | 24 |
| captured (>90%) | 24 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 96 |
| README keywords (GUESS) | 12 |
| min_compute.yml (curated) | 10 |
| code-submission (validator runs it) | 9 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-10-06T19:07 | sn10 | SCORING_COMMIT | sn10 commit touches scoring: feat(ops): add private PRO6000 FP8 campai |
| 2026-10-06T19:07 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: fix(validator): /health in daily mode no  |
| 2026-10-06T19:07 | sn28 | RELEASE | sn28 released v0.4.26 |
| 2026-10-06T19:07 | sn50 | SCORING_COMMIT | sn50 commit touches scoring: perf(validator): write predictions to Big |
| 2026-10-06T19:07 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-3947 - [P2] lium-io drops celium-coll |
| 2026-10-06T19:07 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Merge PR #238: retain validated company e |
| 2026-10-06T19:07 | sn76 | SCORING_COMMIT | sn76 commit touches scoring: ormas-miner CLI and user-only installer ( |
| 2026-10-06T19:07 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Match miner scoring runtime pins and diag |
| 2026-10-06T19:07 | sn108 | BURN_DROP | sn108 burn fell 1.000 -> 0.900 - miners can earn again |
| 2026-10-06T19:07 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: fix(validator): scope split audit repair |
| 2026-10-06T19:07 | sn114 | SCORING_COMMIT | sn114 commit touches scoring: feat(scoring): count jev input tokens in |
| 2026-10-06T19:07 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Merge pull request #708 from carbonphysi |
| 2026-10-06T19:07 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: Calculate hourly current miner weights w |
| 2026-10-06T13:39 | sn9 | RELEASE | sn9 released v4.13.5 |
| 2026-10-06T13:39 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-3980 - validator: start the host prob |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

