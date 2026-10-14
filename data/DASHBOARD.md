# Subnet watch — dashboard

_snapshot 2026-10-14T19:44:09Z · block 9283703 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 60 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 102 | `miner_burn` < 0.99 |
| Ranked | 102 | passed every gate |
| **Positive margin** | **60** | income beats machine cost |
| New events this window | 13 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 67 | `████████████████████████████` |
| 0–0.2 | 6 | `███` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 11 | `█████` |
| 0.8–0.99 | 9 | `████` |
| ≥0.99 dead | 26 | `███████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn107 Minos | 81.9 | 274 | 23,510 | cpu-small | 20 | 80% |
| 2 | sn3 Teutonic | 74.7 | 2,992 | 2,992 = | rtx4090* | 5 | 40% |
| 3 | sn101 Tag101 | 70.3 | 13.44 | 14.37 | cpu-small | 245 | 1% |
| 4 | sn14 Cacheon | 69.9 | 711 | 5,760 | rtx4090* | 3 | 83% |
| 5 | sn53 engy | 69.5 | 630 | 2,622 | rtx4090 | 24 | 16% |
| 6 | sn91 cascade | 69.3 | 237 | 953 | cpu-small | 5 | 52% |
| 7 | sn67 Harnyx | 68.7 | 8.21 | 664 | cpu-small | 120 | 25% |
| 8 | sn58 Attune | 68.3 | 448 | 783 | rtx4090* | 5 | 72% |
| 9 | sn79 MVTRX | 67.5 | 7.50 | 49.94 | cpu-small | 246 | 2% |
| 10 | sn96 Verathos | 67.1 | 16.75 | 186 | rtx4090 | 67 | 40% |
| 11 | sn4 Targon | 66.7 | 9,667 | 28,502 | rtx4090* | 5 | 70% |
| 12 | sn7 Allways | 65.9 | 224 | 374 | rtx4090* | 8 | 21% |
| 13 | sn15 ORO | 65 | 6.45 | 16,568 | cpu-small | 72 | 97% |
| 14 | sn26 Perturb | 64.8 | 301 | 371 | rtx3060 | 4 | 60% |
| 15 | sn66 conjectures | 63.8 | 117 | 242 | rtx4090* | 4 | 81% |
| 16 | sn62 Ridges | 63.7 | 113 | 1,232 | rtx4090* | 37 | 17% |
| 17 | sn120 Affine | 62.2 | 82.36 | 581 | rtx4090* | 270 | 2% |
| 18 | sn28 SayGM | 62 | 69.46 | 2,204 | rtx4090* | 72 | 30% |
| 19 | sn61 RedTeam | 61.5 | 59.89 | 82.35 | rtx4090* | 135 | 1% |
| 20 | sn41 Almanac | 60.6 | 2.23 | 149 | cpu-small | 127 | 3% |

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
| dominated (60–90%) | 31 |
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
| 2026-10-14T19:44 | sn10 | BURN_DROP | sn10 burn fell 1.000 -> 0.532 - miners can earn again |
| 2026-10-14T19:44 | sn14 | SCORING_COMMIT | sn14 commit touches scoring: Show evaluator activity from the current  |
| 2026-10-14T19:44 | sn28 | RELEASE | sn28 released v0.4.29-dev |
| 2026-10-14T19:44 | sn28 | SCORING_COMMIT | sn28 commit touches scoring: chore(release): gm-miner 0.4.29-dev (#320 |
| 2026-10-14T19:44 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: NO-TICKET - validator: the spot pay flag  |
| 2026-10-14T19:44 | sn76 | BURN_DROP | sn76 burn fell 1.000 -> 0.988 - miners can earn again |
| 2026-10-14T19:44 | sn76 | SCORING_COMMIT | sn76 commit touches scoring: security: harden public miner and validat |
| 2026-10-14T19:44 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Merge pull request #252 from Umi-BitSign/ |
| 2026-10-14T19:44 | sn96 | SCORING_COMMIT | sn96 commit touches scoring: fix: move the Decide validator handover t |
| 2026-10-14T19:44 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Merge pull request #1354 from carbonphys |
| 2026-10-14T19:44 | sn117 | RELEASE | sn117 released everycli v0.5.5 |
| 2026-10-14T19:44 | sn117 | SCORING_COMMIT | sn117 commit touches scoring: fix: streamline model offers and miner d |
| 2026-10-14T19:44 | sn117 | README_TASK_DIFF | sn117 README task/scoring sections changed |
| 2026-10-14T15:33 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-4035 - [P1] Validator: resolve hostna |
| 2026-10-14T15:33 | sn66 | SCORING_COMMIT | sn66 commit touches scoring: feat: extend leaderboard endpoint (add pa |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

