# Subnet watch — dashboard

_snapshot 2026-10-23T15:20:11Z · block 9347102 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 58 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 98 | `miner_burn` < 0.99 |
| Ranked | 98 | passed every gate |
| **Positive margin** | **58** | income beats machine cost |
| New events this window | 16 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 65 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 7 | `███` |
| 0.6–0.8 | 11 | `█████` |
| 0.8–0.99 | 4 | `██` |
| ≥0.99 dead | 30 | `█████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn121 sundae_bar | 74.5 | 1,095 | 1,095 = | cpu-small | 2 | 60% |
| 2 | sn3 Teutonic | 73.6 | 2,175 | 6,541 | rtx4090* | 6 | 38% |
| 3 | sn56 Gradients | 69.6 | 655 | 6,074 | rtx4090* | 6 | 53% |
| 4 | sn67 Harnyx | 68.4 | 8.65 | 225 | cpu-small | 131 | 10% |
| 5 | sn1 Apex | 68.3 | 449 | 875 | rtx4090* | 5 | 54% |
| 6 | sn46 Instant | 68.2 | 170 | 222 | cpu-small | 14 | 9% |
| 7 | sn82 Noah | 68.1 | 615 | 623 | rtx4090* | 62 | 2% |
| 8 | sn53 engy | 67.1 | 313 | 2,777 | rtx4090 | 36 | 11% |
| 9 | sn107 Minos | 67.1 | 230 | 19,506 | cpu-small | 20 | 80% |
| 10 | sn125 Refinery | 66.7 | 276 | 931 | rtx4090* | 4 | 50% |
| 11 | sn104 TAOstatus | 65.8 | 2,831 | 2,831 = | cpu-small | 1 | 100% |
| 12 | sn66 conjectures | 63.5 | 106 | 220 | rtx4090* | 4 | 80% |
| 13 | sn120 Affine | 62.1 | 85.70 | 235 | rtx4090* | 296 | 1% |
| 14 | sn55 NIOME | 61.7 | 61.55 | 515 | rtx4090* | 11 | 30% |
| 15 | sn41 Almanac | 59.9 | 1.98 | 165 | cpu-small | 158 | 3% |
| 16 | sn111 Claims | 59.1 | 29.38 | 2,804 | rtx4090* | 6 | 90% |
| 17 | sn49 Nepher Robotics | 59 | 963 | 3,392 | rtx4090* | 4 | 69% |
| 18 | sn81 Reliquary | 59 | 27.15 | 430 | rtx4090* | 15 | 72% |
| 19 | sn80 OpenRoboto | 58.8 | 907 | 3,825 | rtx4090* | 11 | 25% |
| 20 | sn4 Targon | 57.9 | 10,106 | 27,797 | rtx4090* | 5 | 68% |

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
| dominated (60–90%) | 28 |
| captured (>90%) | 22 |

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
| 2026-10-23T15:20 | sn6 | WEIGHTS_VERSION_BUMP | sn6 weights_version 3000 -> 4000 |
| 2026-10-23T15:20 | sn28 | RELEASE | sn28 released v0.5.11 |
| 2026-10-23T15:20 | sn28 | SCORING_COMMIT | sn28 commit touches scoring: chore(release): gm-miner 0.5.11 (#351) |
| 2026-10-23T15:20 | sn46 | RELEASE | sn46 released v0.1.4 |
| 2026-10-23T15:20 | sn51 | RELEASE | sn51 released lium-protocol-v1.16.0 |
| 2026-10-23T15:20 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-3476 - [P0] libdmcompverify.so: add s |
| 2026-10-23T15:20 | sn56 | SCORING_COMMIT | sn56 commit touches scoring: Sunset environment tournaments and evalua |
| 2026-10-23T15:20 | sn66 | RELEASE | sn66 released v2026.10.23 |
| 2026-10-23T15:20 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Merge pull request #718 from leadpoet/fix |
| 2026-10-23T15:20 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Discover proved reward runtimes automatic |
| 2026-10-23T15:20 | sn89 | SCORING_COMMIT | sn89 commit touches scoring: Keep-alive floor for fresh and active min |
| 2026-10-23T15:20 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: eval v5.1: public format doc, reference s |
| 2026-10-23T15:20 | sn97 | SCORING_COMMIT | sn97 commit touches scoring: feat(eval): fetch the challenger claimed  |
| 2026-10-23T15:20 | sn117 | RELEASE | sn117 released everycli v0.7.2 |
| 2026-10-23T15:20 | sn117 | SCORING_COMMIT | sn117 commit touches scoring: docs: record bootstrap artifacts and liv |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

