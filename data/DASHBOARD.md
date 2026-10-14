# Subnet watch — dashboard

_snapshot 2026-10-14T00:38:35Z · block 9277975 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 56 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 99 | `miner_burn` < 0.99 |
| Ranked | 99 | passed every gate |
| **Positive margin** | **56** | income beats machine cost |
| New events this window | 7 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 69 | `████████████████████████████` |
| 0–0.2 | 6 | `██` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 11 | `████` |
| 0.8–0.99 | 5 | `██` |
| ≥0.99 dead | 29 | `████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn107 Minos | 82.1 | 290 | 24,627 | cpu-small | 20 | 80% |
| 2 | sn3 Teutonic | 74.8 | 3,137 | 3,137 = | rtx4090* | 5 | 40% |
| 3 | sn53 engy | 71.7 | 1,243 | 2,741 | rtx4090 | 18 | 17% |
| 4 | sn101 Tag101 | 70.5 | 14.10 | 15.56 | cpu-small | 244 | 1% |
| 5 | sn14 Cacheon | 70 | 735 | 5,952 | rtx4090* | 3 | 83% |
| 6 | sn67 Harnyx | 70 | 12.14 | 706 | cpu-small | 145 | 26% |
| 7 | sn58 Attune | 68.5 | 483 | 670 | rtx4090* | 5 | 74% |
| 8 | sn4 Targon | 66.9 | 10,068 | 29,686 | rtx4090* | 5 | 70% |
| 9 | sn79 MVTRX | 66.8 | 7.35 | 43.26 | cpu-small | 246 | 2% |
| 10 | sn15 ORO | 66.5 | 6.45 | 13.89 | cpu-small | 57 | 98% |
| 11 | sn41 Almanac | 65.8 | 5.63 | 164 | cpu-small | 103 | 5% |
| 12 | sn7 Allways | 64.1 | 129 | 491 | rtx4090* | 9 | 26% |
| 13 | sn120 Affine | 63.9 | 140 | 265 | rtx4090* | 247 | 1% |
| 14 | sn62 Ridges | 63.9 | 119 | 907 | rtx4090* | 37 | 17% |
| 15 | sn61 RedTeam | 61.9 | 67.85 | 90.78 | rtx4090* | 130 | 1% |
| 16 | sn28 SayGM | 61 | 51.44 | 3,097 | rtx4090* | 74 | 19% |
| 17 | sn91 cascade | 60.8 | 634 | 2,032 | cpu-small | 5 | 52% |
| 18 | sn111 Claims | 59.9 | 36.75 | 3,204 | rtx4090* | 6 | 90% |
| 19 | sn23 Trishool | 59.2 | 402 | 402 = | cpu-small | 3 | 80% |
| 20 | sn80 OpenRoboto | 58.7 | 878 | 3,516 | rtx4090* | 10 | 35% |

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
| wide (<30%) | 26 |
| concentrated (30–60%) | 20 |
| dominated (60–90%) | 29 |
| captured (>90%) | 21 |

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
| 2026-10-14T00:39 | sn7 | RELEASE | sn7 released release-20261013-222136 |
| 2026-10-14T00:39 | sn7 | SCORING_COMMIT | sn7 commit touches scoring: Ban a miner from scoring for 12 rounds whe |
| 2026-10-14T00:39 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Merge the validator test and correctness  |
| 2026-10-14T00:39 | sn45 | SCORING_COMMIT | sn45 commit touches scoring: soak report: read rotated validator logs |
| 2026-10-14T00:39 | sn54 | SCORING_COMMIT | sn54 commit touches scoring: adding in query from validators |
| 2026-10-14T00:39 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Merge pull request #247 from Umi-BitSign/ |
| 2026-10-14T00:39 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: Reduce repeated commitment derivation in |
| 2026-10-13T21:35 | sn15 | RELEASE | sn15 released v2.5.0 |
| 2026-10-13T21:35 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: Load v7 and v8 task packs; move to oro-en |
| 2026-10-13T21:35 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Write the validator's settlement v2 adopt |
| 2026-10-13T21:35 | sn41 | SCORING_COMMIT | sn41 commit touches scoring: Adding weights version key to validator l |
| 2026-10-13T21:35 | sn63 | SCORING_COMMIT | sn63 commit touches scoring: Track whether a terminal verify update re |
| 2026-10-13T21:35 | sn66 | SCORING_COMMIT | sn66 commit touches scoring: Port Mathlib headers to the immutable tas |
| 2026-10-13T21:35 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Merge pull request #415: Verify judge pro |
| 2026-10-13T21:35 | sn116 | RELEASE | sn116 released producer-code-r8.6 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

