# Subnet watch — dashboard

_snapshot 2026-10-14T10:38:40Z · block 9280975 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 58 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 99 | `miner_burn` < 0.99 |
| Ranked | 99 | passed every gate |
| **Positive margin** | **58** | income beats machine cost |
| New events this window | 11 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 67 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 10 | `████` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 29 | `████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn107 Minos | 82 | 286 | 24,262 | cpu-small | 20 | 80% |
| 2 | sn3 Teutonic | 74.8 | 3,088 | 3,088 = | rtx4090* | 5 | 40% |
| 3 | sn91 cascade | 72.6 | 630 | 2,020 | cpu-small | 5 | 52% |
| 4 | sn53 engy | 71.7 | 1,220 | 2,689 | rtx4090 | 18 | 17% |
| 5 | sn101 Tag101 | 70.4 | 13.80 | 15.10 | cpu-small | 244 | 1% |
| 6 | sn67 Harnyx | 68.7 | 8.49 | 685 | cpu-small | 113 | 25% |
| 7 | sn58 Attune | 68.6 | 487 | 660 | rtx4090* | 5 | 74% |
| 8 | sn4 Targon | 66.8 | 9,976 | 29,413 | rtx4090* | 5 | 70% |
| 9 | sn79 MVTRX | 66.8 | 6.77 | 55.74 | cpu-small | 246 | 2% |
| 10 | sn41 Almanac | 65.8 | 5.62 | 156 | cpu-small | 116 | 4% |
| 11 | sn15 ORO | 65.6 | 7.00 | 17,786 | cpu-small | 72 | 97% |
| 12 | sn26 Perturb | 65.1 | 324 | 399 | rtx3060 | 4 | 60% |
| 13 | sn120 Affine | 64 | 133 | 433 | rtx4090* | 249 | 1% |
| 14 | sn62 Ridges | 63.8 | 117 | 1,273 | rtx4090* | 37 | 17% |
| 15 | sn28 SayGM | 62.3 | 77.40 | 1,215 | rtx4090* | 69 | 30% |
| 16 | sn61 RedTeam | 61.9 | 69.83 | 91.40 | rtx4090* | 126 | 1% |
| 17 | sn111 Claims | 59.7 | 34.66 | 3,057 | rtx4090* | 6 | 90% |
| 18 | sn23 Trishool | 59.2 | 399 | 399 = | cpu-small | 3 | 80% |
| 19 | sn7 Allways | 59 | 31.50 | 643 | rtx4090* | 11 | 35% |
| 20 | sn80 OpenRoboto | 58.8 | 904 | 3,619 | rtx4090* | 10 | 35% |

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
| dominated (60–90%) | 27 |
| captured (>90%) | 22 |

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
| 2026-10-14T10:39 | sn25 | RELEASE | sn25 released v2026.10.14-1071632750 |
| 2026-10-14T10:39 | sn37 | BURN_DROP | sn37 burn fell 1.000 -> 0.715 - miners can earn again |
| 2026-10-14T10:39 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-4270 - [P1] Validator: count rented n |
| 2026-10-14T10:39 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-10-14T10:39 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Merge PR #432: repair verified domain con |
| 2026-10-14T10:39 | sn76 | SCORING_COMMIT | sn76 commit touches scoring: security: repair frozen verifier snapshot |
| 2026-10-14T10:39 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Preserve native reward history through wr |
| 2026-10-14T10:39 | sn108 | SCORING_COMMIT | sn108 commit touches scoring: Validator sends its EDA server the batch |
| 2026-10-14T10:39 | sn116 | RELEASE | sn116 released r8.7 |
| 2026-10-14T10:39 | sn117 | RELEASE | sn117 released everycli v0.5.1 |
| 2026-10-14T10:39 | sn117 | SCORING_COMMIT | sn117 commit touches scoring: docs: align miner README with v0.5.1 set |
| 2026-10-14T05:29 | sn25 | RELEASE | sn25 released v2026.10.13-1071515580 |
| 2026-10-14T05:29 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Merge v2/gate-miner-tests into main |
| 2026-10-14T05:29 | sn37 | SCORING_COMMIT | sn37 commit touches scoring: docs: describe planned stake-retention me |
| 2026-10-14T05:29 | sn37 | README_TASK_DIFF | sn37 README task/scoring sections changed |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

