# Subnet watch — dashboard

_snapshot 2026-10-23T19:25:40Z · block 9348329 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 55 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 97 | `miner_burn` < 0.99 |
| Ranked | 97 | passed every gate |
| **Positive margin** | **55** | income beats machine cost |
| New events this window | 6 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 65 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 7 | `███` |
| 0.6–0.8 | 10 | `████` |
| 0.8–0.99 | 3 | `█` |
| ≥0.99 dead | 31 | `█████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn3 Teutonic | 73.6 | 2,161 | 4,330 | rtx4090* | 7 | 25% |
| 2 | sn97 Ingot | 73.2 | 1,897 | 1,897 = | rtx4090* | 4 | 40% |
| 3 | sn56 Gradients | 68.9 | 535 | 1,461 | rtx4090* | 6 | 51% |
| 4 | sn67 Harnyx | 68.6 | 8.33 | 217 | cpu-small | 133 | 10% |
| 5 | sn1 Apex | 68.4 | 461 | 953 | rtx4090* | 5 | 52% |
| 6 | sn82 Noah | 68.2 | 628 | 636 | rtx4090* | 62 | 2% |
| 7 | sn46 Instant | 67.8 | 148 | 199 | cpu-small | 16 | 8% |
| 8 | sn107 Minos | 67.1 | 229 | 19,426 | cpu-small | 20 | 80% |
| 9 | sn53 engy | 67 | 306 | 2,720 | rtx4090 | 36 | 11% |
| 10 | sn125 Refinery | 66.7 | 277 | 935 | rtx4090* | 4 | 50% |
| 11 | sn104 TAOstatus | 65.7 | 2,765 | 2,765 = | cpu-small | 1 | 100% |
| 12 | sn66 conjectures | 63.5 | 105 | 218 | rtx4090* | 4 | 80% |
| 13 | sn120 Affine | 62.6 | 96.90 | 216 | rtx4090* | 298 | 1% |
| 14 | sn121 sundae_bar | 62.5 | 1,068 | 1,068 = | cpu-small | 2 | 60% |
| 15 | sn55 NIOME | 61.7 | 62.52 | 520 | rtx4090* | 11 | 30% |
| 16 | sn117 everyframe.studi | 61.3 | 55.54 | 86.62 | rtx4090* | 7 | 67% |
| 17 | sn111 Claims | 59 | 28.48 | 2,736 | rtx4090* | 6 | 90% |
| 18 | sn49 Nepher Robotics | 58.9 | 932 | 3,283 | rtx4090* | 4 | 69% |
| 19 | sn80 OpenRoboto | 58.6 | 857 | 3,615 | rtx4090* | 11 | 25% |
| 20 | sn5 Hone | 57.4 | 30.95 | 40.96 | rtx4090* | 243 | 1% |

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
| dominated (60–90%) | 27 |
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
| 2026-10-23T15:20 | sn51 | RELEASE | sn51 released lium-protocol-v1.16.0 |
| 2026-10-23T15:20 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-3476 - [P0] libdmcompverify.so: add s |
| 2026-10-23T15:20 | sn56 | SCORING_COMMIT | sn56 commit touches scoring: Sunset environment tournaments and evalua |
| 2026-10-23T15:20 | sn66 | RELEASE | sn66 released v2026.10.23 |
| 2026-10-23T15:20 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Merge pull request #718 from leadpoet/fix |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

