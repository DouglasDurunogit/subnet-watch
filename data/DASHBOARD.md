# Subnet watch — dashboard

_snapshot 2026-10-15T00:57:19Z · block 9285268 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 55 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 100 | `miner_burn` < 0.99 |
| Ranked | 100 | passed every gate |
| **Positive margin** | **55** | income beats machine cost |
| New events this window | 2 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 67 | `████████████████████████████` |
| 0–0.2 | 6 | `███` |
| 0.2–0.4 | 3 | `█` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 11 | `█████` |
| 0.8–0.99 | 9 | `████` |
| ≥0.99 dead | 28 | `████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn107 Minos | 81.9 | 276 | 23,400 | cpu-small | 20 | 80% |
| 2 | sn41 Almanac | 78.6 | 112 | 163 | cpu-small | 67 | 3% |
| 3 | sn101 Tag101 | 70.1 | 12.91 | 13.79 | cpu-small | 244 | 1% |
| 4 | sn53 engy | 69.4 | 624 | 2,597 | rtx4090 | 24 | 16% |
| 5 | sn91 cascade | 69.3 | 237 | 953 | cpu-small | 5 | 52% |
| 6 | sn67 Harnyx | 68.6 | 8.17 | 661 | cpu-small | 122 | 25% |
| 7 | sn58 Attune | 68.2 | 443 | 714 | rtx4090* | 5 | 71% |
| 8 | sn96 Verathos | 67.9 | 20.14 | 183 | rtx4090 | 67 | 40% |
| 9 | sn79 MVTRX | 67.3 | 7.60 | 37.63 | cpu-small | 249 | 2% |
| 10 | sn4 Targon | 66.7 | 9,634 | 28,405 | rtx4090* | 5 | 70% |
| 11 | sn15 ORO | 66.4 | 6.30 | 13.08 | cpu-small | 73 | 97% |
| 12 | sn7 Allways | 65.9 | 224 | 324 | rtx4090* | 8 | 19% |
| 13 | sn26 Perturb | 64.8 | 303 | 374 | rtx3060 | 4 | 60% |
| 14 | sn28 SayGM | 64.8 | 157 | 1,511 | rtx4090* | 63 | 29% |
| 15 | sn66 conjectures | 64 | 123 | 254 | rtx4090* | 4 | 80% |
| 16 | sn62 Ridges | 64 | 121 | 1,228 | rtx4090* | 37 | 17% |
| 17 | sn120 Affine | 62.1 | 80.67 | 573 | rtx4090* | 270 | 2% |
| 18 | sn61 RedTeam | 61.6 | 62.52 | 83.96 | rtx4090* | 131 | 1% |
| 19 | sn80 OpenRoboto | 58.6 | 859 | 3,441 | rtx4090* | 10 | 35% |
| 20 | sn111 Claims | 57.9 | 20.53 | 2,936 | rtx4090* | 7 | 90% |

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
| concentrated (30–60%) | 19 |
| dominated (60–90%) | 29 |
| captured (>90%) | 24 |

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
| 2026-10-15T00:57 | sn8 | SCORING_COMMIT | sn8 commit touches scoring: Sync price updates and challenge loop (#95 |
| 2026-10-15T00:57 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Select the startup verified tests and pin |
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

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

