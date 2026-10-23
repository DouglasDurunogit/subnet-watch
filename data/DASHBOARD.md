# Subnet watch — dashboard

_snapshot 2026-10-23T22:31:51Z · block 9349260 · run_status **ok**_

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
| New events this window | 5 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 66 | `████████████████████████████` |
| 0–0.2 | 6 | `███` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 6 | `███` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 29 | `████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn3 Teutonic | 73.6 | 2,155 | 4,318 | rtx4090* | 7 | 25% |
| 2 | sn97 Ingot | 73.1 | 1,868 | 1,868 = | rtx4090* | 5 | 20% |
| 3 | sn56 Gradients | 69.9 | 709 | 2,863 | rtx4090* | 6 | 51% |
| 4 | sn67 Harnyx | 68.5 | 8.27 | 216 | cpu-small | 134 | 10% |
| 5 | sn1 Apex | 68.4 | 453 | 956 | rtx4090* | 5 | 52% |
| 6 | sn82 Noah | 67.8 | 633 | 641 | rtx4090* | 62 | 2% |
| 7 | sn46 Instant | 67.8 | 150 | 182 | cpu-small | 16 | 8% |
| 8 | sn53 engy | 67.1 | 311 | 2,764 | rtx4090 | 36 | 11% |
| 9 | sn107 Minos | 67.1 | 228 | 19,340 | cpu-small | 20 | 80% |
| 10 | sn125 Refinery | 66.7 | 277 | 935 | rtx4090* | 4 | 50% |
| 11 | sn104 TAOstatus | 65.7 | 2,757 | 2,757 = | cpu-small | 1 | 100% |
| 12 | sn66 conjectures | 63.5 | 105 | 218 | rtx4090* | 4 | 80% |
| 13 | sn121 sundae_bar | 62.5 | 1,064 | 1,064 = | cpu-small | 2 | 60% |
| 14 | sn23 Trishool | 62.5 | 1,061 | 1,061 = | cpu-small | 2 | 80% |
| 15 | sn120 Affine | 62.4 | 97.97 | 182 | rtx4090* | 300 | 1% |
| 16 | sn55 NIOME | 61.6 | 60.76 | 509 | rtx4090* | 11 | 30% |
| 17 | sn117 everyframe.studi | 61.5 | 58.59 | 132 | rtx4090* | 8 | 54% |
| 18 | sn34 BitMind | 59.6 | 7,836 | 7,836 = | a100-80 | 3 | 85% |
| 19 | sn111 Claims | 59 | 28.29 | 2,722 | rtx4090* | 6 | 90% |
| 20 | sn80 OpenRoboto | 58.5 | 833 | 3,517 | rtx4090* | 11 | 25% |

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
| dominated (60–90%) | 28 |
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
| 2026-10-23T22:32 | sn7 | BURN_DROP | sn7 burn fell 0.991 -> 0.985 - miners can earn again |
| 2026-10-23T22:32 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Preserve the failed primary-intent reason |
| 2026-10-23T22:32 | sn76 | BURN_DROP | sn76 burn fell 0.992 -> 0.987 - miners can earn again |
| 2026-10-23T22:32 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Retain bounded model pairs and finish res |
| 2026-10-23T22:32 | sn117 | RELEASE | sn117 released everycli v0.7.3 |
| 2026-10-23T19:26 | sn8 | SCORING_COMMIT | sn8 commit touches scoring: Optimizations for miner statistics (#964) |
| 2026-10-23T19:26 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: fix(scoring): only real scored entries co |
| 2026-10-23T19:26 | sn22 | SCORING_COMMIT | sn22 commit touches scoring: fix(bot): open a fresh connection for eac |
| 2026-10-23T19:26 | sn66 | RELEASE | sn66 released v2026.10.23.2 |
| 2026-10-23T19:26 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Bind company-evidence release to reviewed |
| 2026-10-23T19:26 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: Flip-incentive SHADOW docs + audit helpe |
| 2026-10-23T15:20 | sn6 | WEIGHTS_VERSION_BUMP | sn6 weights_version 3000 -> 4000 |
| 2026-10-23T15:20 | sn28 | RELEASE | sn28 released v0.5.11 |
| 2026-10-23T15:20 | sn28 | SCORING_COMMIT | sn28 commit touches scoring: chore(release): gm-miner 0.5.11 (#351) |
| 2026-10-23T15:20 | sn46 | RELEASE | sn46 released v0.1.4 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

