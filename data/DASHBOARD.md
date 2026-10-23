# Subnet watch — dashboard

_snapshot 2026-10-23T05:09:53Z · block 9344050 · run_status **ok**_

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
| New events this window | 11 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 67 | `████████████████████████████` |
| 0–0.2 | 5 | `██` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 8 | `███` |
| 0.6–0.8 | 11 | `█████` |
| 0.8–0.99 | 3 | `█` |
| ≥0.99 dead | 30 | `█████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn121 sundae_bar | 74.5 | 1,106 | 1,106 = | cpu-small | 2 | 60% |
| 2 | sn3 Teutonic | 73.6 | 2,190 | 2,990 | rtx4090* | 5 | 45% |
| 3 | sn91 cascade | 73.2 | 744 | 1,488 | cpu-small | 5 | 52% |
| 4 | sn67 Harnyx | 73.1 | 27.61 | 261 | cpu-small | 46 | 11% |
| 5 | sn1 Apex | 68.5 | 473 | 925 | rtx4090* | 5 | 52% |
| 6 | sn82 Noah | 68.1 | 631 | 639 | rtx4090* | 62 | 2% |
| 7 | sn56 Gradients | 67.3 | 333 | 5,327 | rtx4090* | 9 | 46% |
| 8 | sn107 Minos | 67.2 | 233 | 19,796 | cpu-small | 20 | 80% |
| 9 | sn53 engy | 67.1 | 316 | 2,801 | rtx4090 | 36 | 11% |
| 10 | sn125 Refinery | 66.8 | 283 | 940 | rtx4090* | 4 | 50% |
| 11 | sn104 TAOstatus | 63.5 | 1,428 | 1,428 = | cpu-small | 2 | 50% |
| 12 | sn66 conjectures | 63.5 | 106 | 221 | rtx4090* | 4 | 80% |
| 13 | sn120 Affine | 63 | 110 | 508 | rtx4090* | 178 | 2% |
| 14 | sn55 NIOME | 61.8 | 63.42 | 529 | rtx4090* | 11 | 30% |
| 15 | sn81 Reliquary | 60.4 | 42.06 | 307 | rtx4090* | 22 | 58% |
| 16 | sn92 REAX | 60.3 | 53.78 | 4,169 | rtx4090 | 226 | 17% |
| 17 | sn34 BitMind | 59.7 | 7,916 | 7,916 = | a100-80 | 2 | 85% |
| 18 | sn41 Almanac | 59.6 | 1.91 | 172 | cpu-small | 159 | 3% |
| 19 | sn111 Claims | 59.3 | 31.14 | 2,809 | rtx4090* | 6 | 90% |
| 20 | sn80 OpenRoboto | 58.8 | 914 | 3,856 | rtx4090* | 11 | 25% |

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
| concentrated (30–60%) | 25 |
| dominated (60–90%) | 26 |
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
| 2026-10-23T05:10 | sn15 | RELEASE | sn15 released v3.0.2: security: patch Python dependencies and supporte |
| 2026-10-23T05:10 | sn21 | RELEASE | sn21 released SN21 training data v5 (rules from 30 Oct 2026) |
| 2026-10-23T05:10 | sn28 | RELEASE | sn28 released v0.5.10 |
| 2026-10-23T05:10 | sn28 | SCORING_COMMIT | sn28 commit touches scoring: chore(release): gm-miner 0.5.10 (#348) |
| 2026-10-23T05:10 | sn51 | RELEASE | sn51 released executor-v1.152 |
| 2026-10-23T05:10 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-5012 - [P0] Validator: a killed fille |
| 2026-10-23T05:10 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Carry verified numeric LinkedIn identity  |
| 2026-10-23T05:10 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Handle runtime483 reward eligibility and  |
| 2026-10-23T05:10 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: Merge pull request #393 from reliquadotai |
| 2026-10-23T05:10 | sn104 | BURN_DROP | sn104 burn fell 1.000 -> 0.000 - miners can earn again |
| 2026-10-23T05:10 | sn123 | SCORING_COMMIT | sn123 commit touches scoring: Update validator.py |
| 2026-10-23T00:12 | sn28 | RELEASE | sn28 released v0.5.10-dev |
| 2026-10-23T00:12 | sn28 | SCORING_COMMIT | sn28 commit touches scoring: chore(release): gm-miner 0.5.10-dev (#347 |
| 2026-10-23T00:12 | sn81 | BURN_DROP | sn81 burn fell 0.996 -> 0.810 - miners can earn again |
| 2026-10-22T21:32 | sn7 | BURN_DROP | sn7 burn fell 0.990 -> 0.986 - miners can earn again |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

