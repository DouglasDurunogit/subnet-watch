# Subnet watch — dashboard

_snapshot 2026-10-14T22:42:19Z · block 9284593 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 57 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 100 | `miner_burn` < 0.99 |
| Ranked | 100 | passed every gate |
| **Positive margin** | **57** | income beats machine cost |
| New events this window | 9 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 66 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 11 | `█████` |
| 0.8–0.99 | 8 | `███` |
| ≥0.99 dead | 28 | `████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn107 Minos | 81.9 | 275 | 23,375 | cpu-small | 20 | 80% |
| 2 | sn101 Tag101 | 70.1 | 13.09 | 14.01 | cpu-small | 242 | 1% |
| 3 | sn14 Cacheon | 69.9 | 717 | 5,810 | rtx4090* | 3 | 83% |
| 4 | sn53 engy | 69.4 | 625 | 2,601 | rtx4090 | 24 | 16% |
| 5 | sn91 cascade | 69.3 | 237 | 950 | cpu-small | 5 | 52% |
| 6 | sn67 Harnyx | 68.7 | 8.19 | 663 | cpu-small | 122 | 25% |
| 7 | sn58 Attune | 68.4 | 465 | 749 | rtx4090* | 5 | 71% |
| 8 | sn96 Verathos | 67.6 | 18.99 | 184 | rtx4090 | 67 | 40% |
| 9 | sn79 MVTRX | 67.6 | 7.58 | 41.19 | cpu-small | 249 | 2% |
| 10 | sn4 Targon | 66.7 | 9,653 | 28,461 | rtx4090* | 5 | 70% |
| 11 | sn15 ORO | 66.1 | 6.31 | 13.10 | cpu-small | 73 | 97% |
| 12 | sn26 Perturb | 64.8 | 301 | 372 | rtx3060 | 4 | 60% |
| 13 | sn7 Allways | 64.8 | 161 | 405 | rtx4090* | 8 | 23% |
| 14 | sn66 conjectures | 64 | 124 | 240 | rtx4090* | 4 | 81% |
| 15 | sn62 Ridges | 64 | 122 | 1,230 | rtx4090* | 37 | 17% |
| 16 | sn28 SayGM | 63.7 | 113 | 968 | rtx4090* | 69 | 36% |
| 17 | sn41 Almanac | 62.5 | 3.00 | 147 | cpu-small | 112 | 3% |
| 18 | sn120 Affine | 62.2 | 81.88 | 579 | rtx4090* | 270 | 2% |
| 19 | sn61 RedTeam | 61.7 | 63.32 | 85.12 | rtx4090* | 132 | 1% |
| 20 | sn102 ConnitoAI | 59.5 | 1,141 | 1,141 = | rtx4090* | 4 | 25% |

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
| captured (>90%) | 23 |

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
| 2026-10-14T22:42 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: perf(scoring): read receipts through a sm |
| 2026-10-14T22:42 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: State that any v2 request checkpoint writ |
| 2026-10-14T22:42 | sn28 | RELEASE | sn28 released v0.5.0 |
| 2026-10-14T22:42 | sn28 | SCORING_COMMIT | sn28 commit touches scoring: chore(release): promote gm-miner 0.5.0 (# |
| 2026-10-14T22:42 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Keep stopped reward reconciliation alive  |
| 2026-10-14T22:42 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Merge pull request #1365 from carbonphys |
| 2026-10-14T22:42 | sn117 | RELEASE | sn117 released everycli v0.5.6 |
| 2026-10-14T22:42 | sn117 | README_TASK_DIFF | sn117 README task/scoring sections changed |
| 2026-10-14T22:42 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: Award contested tasks to the earliest Cl |
| 2026-10-14T19:44 | sn10 | BURN_DROP | sn10 burn fell 1.000 -> 0.532 - miners can earn again |
| 2026-10-14T19:44 | sn14 | SCORING_COMMIT | sn14 commit touches scoring: Show evaluator activity from the current  |
| 2026-10-14T19:44 | sn28 | RELEASE | sn28 released v0.4.29-dev |
| 2026-10-14T19:44 | sn28 | SCORING_COMMIT | sn28 commit touches scoring: chore(release): gm-miner 0.4.29-dev (#320 |
| 2026-10-14T19:44 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: NO-TICKET - validator: the spot pay flag  |
| 2026-10-14T19:44 | sn76 | BURN_DROP | sn76 burn fell 1.000 -> 0.988 - miners can earn again |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

