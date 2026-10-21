# Subnet watch — dashboard

_snapshot 2026-10-21T23:30:03Z · block 9335151 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 55 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 96 | `miner_burn` < 0.99 |
| Ranked | 96 | passed every gate |
| **Positive margin** | **55** | income beats machine cost |
| New events this window | 8 | see ALARMS.md |

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
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 4 | `██` |
| ≥0.99 dead | 32 | `██████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn3 Teutonic | 74.3 | 2,752 | 7,176 | rtx4090* | 5 | 39% |
| 2 | sn97 Ingot | 73.5 | 2,123 | 2,123 = | rtx4090* | 4 | 40% |
| 3 | sn120 Affine | 73.2 | 1,948 | 10,877 | rtx4090* | 10 | 32% |
| 4 | sn91 cascade | 71.1 | 396 | 1,586 | cpu-small | 5 | 52% |
| 5 | sn102 ConnitoAI | 70.5 | 861 | 1,150 | rtx4090* | 5 | 29% |
| 6 | sn1 Apex | 68.6 | 491 | 958 | rtx4090* | 5 | 58% |
| 7 | sn67 Harnyx | 68.3 | 8.16 | 234 | cpu-small | 147 | 9% |
| 8 | sn82 Noah | 67.6 | 610 | 654 | rtx4090* | 61 | 2% |
| 9 | sn125 Refinery | 67.4 | 336 | 993 | rtx4090* | 4 | 50% |
| 10 | sn107 Minos | 67.3 | 240 | 20,240 | cpu-small | 20 | 80% |
| 11 | sn53 engy | 67.2 | 324 | 2,653 | rtx4090 | 36 | 11% |
| 12 | sn15 ORO | 67.1 | 7.75 | 15,558 | cpu-small | 64 | 97% |
| 13 | sn66 conjectures | 63.4 | 103 | 214 | rtx4090* | 4 | 80% |
| 14 | sn26 Perturb | 62.9 | 188 | 235 | rtx3060 | 4 | 60% |
| 15 | sn55 NIOME | 62 | 67.51 | 560 | rtx4090* | 11 | 30% |
| 16 | sn23 Trishool | 61.8 | 869 | 869 = | cpu-small | 2 | 80% |
| 17 | sn117 everyframe.studi | 60.7 | 47.12 | 50.72 | rtx4090* | 6 | 87% |
| 18 | sn81 Reliquary | 59.6 | 32.01 | 108 | rtx4090* | 4 | 95% |
| 19 | sn111 Claims | 59.5 | 32.73 | 2,921 | rtx4090* | 6 | 90% |
| 20 | sn92 REAX | 59.4 | 83.34 | 2,677 | rtx4090 | 235 | 10% |

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
| wide (<30%) | 29 |
| concentrated (30–60%) | 19 |
| dominated (60–90%) | 26 |
| captured (>90%) | 22 |

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
| 2026-10-21T23:30 | sn10 | BURN_DROP | sn10 burn fell 1.000 -> 0.571 - miners can earn again |
| 2026-10-21T23:30 | sn25 | RELEASE | sn25 released v2026.10.21-1078195620 |
| 2026-10-21T23:30 | sn28 | RELEASE | sn28 released v0.5.7 |
| 2026-10-21T23:30 | sn28 | SCORING_COMMIT | sn28 commit touches scoring: chore(release): gm-miner 0.5.7 (#340) |
| 2026-10-21T23:30 | sn71 | BURN_DROP | sn71 burn fell 1.000 -> 0.700 - miners can earn again |
| 2026-10-21T23:30 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Keep restored-score exclusions visible wi |
| 2026-10-21T23:30 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Merge pull request #343 from Umi-BitSign/ |
| 2026-10-21T23:30 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: fix: verify evaluation image against supp |
| 2026-10-21T20:17 | sn7 | RELEASE | sn7 released release-20261021-195318: Scale the miner pool by recent s |
| 2026-10-21T20:17 | sn7 | SCORING_COMMIT | sn7 commit touches scoring: Scale the miner pool by recent swap fees ( |
| 2026-10-21T20:17 | sn28 | RELEASE | sn28 released v0.5.6-dev |
| 2026-10-21T20:17 | sn28 | SCORING_COMMIT | sn28 commit touches scoring: chore(release): gm-miner 0.5.6-dev (#337) |
| 2026-10-21T20:17 | sn28 | README_TASK_DIFF | sn28 README task/scoring sections changed |
| 2026-10-21T20:17 | sn30 | BURN_DROP | sn30 burn fell 0.996 -> 0.981 - miners can earn again |
| 2026-10-21T20:17 | sn37 | BURN_DROP | sn37 burn fell 1.000 -> 0.711 - miners can earn again |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

