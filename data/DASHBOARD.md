# Subnet watch — dashboard

_snapshot 2026-08-07T19:28:10Z · block 8794520 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 54 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 92 | `miner_burn` < 0.99 |
| Ranked | 92 | passed every gate |
| **Positive margin** | **54** | income beats machine cost |
| New events this window | 3 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 54 | `████████████████████████████` |
| 0–0.2 | 5 | `███` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 12 | `██████` |
| 0.6–0.8 | 7 | `████` |
| 0.8–0.99 | 10 | `█████` |
| ≥0.99 dead | 36 | `███████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn107 Minos | 78 | 110 | 31,965 | cpu-small | 20 | 90% |
| 2 | sn76 Phylax | 77.1 | 75.73 | 275 | cpu-small | 10 | 31% |
| 3 | sn98 NeverPlayAlone | 76 | 1,706 | 1,706 = | cpu-small | 1 | 100% |
| 4 | sn60 Bitsec.ai | 75.1 | 1,306 | 1,306 = | cpu-small | 2 | 50% |
| 5 | sn114 SOMA | 72.7 | 1,667 | 4,347 | rtx4090* | 3 | 65% |
| 6 | sn67 Harnyx | 72.2 | 21.09 | 764 | cpu-small | 135 | 20% |
| 7 | sn102 ConnitoAI | 69.6 | 656 | 1,363 | rtx4090* | 7 | 25% |
| 8 | sn62 Ridges | 69.1 | 565 | 2,044 | rtx4090* | 7 | 35% |
| 9 | sn91 cascade | 68.6 | 489 | 1,388 | rtx4090* | 5 | 52% |
| 10 | sn15 ORO | 68.4 | 11.48 | 10,348 | cpu-small | 74 | 93% |
| 11 | sn26 Perturb | 68.1 | 20.94 | 39.16 | rtx3060 | 11 | 51% |
| 12 | sn100 BASE | 67.9 | 399 | 1,621 | rtx4090* | 5 | 50% |
| 13 | sn41 Almanac | 67.6 | 7.55 | 44.55 | cpu-small | 62 | 80% |
| 14 | sn96 Verathos | 66.9 | 15.48 | 222 | rtx4090 | 65 | 43% |
| 15 | sn124 Swarm | 65.6 | 211 | 606 | rtx4090* | 23 | 11% |
| 16 | sn21 AdTAO | 65.5 | 4.74 | 21.92 | cpu-small | 142 | 45% |
| 17 | sn61 RedTeam | 61.9 | 66.29 | 183 | rtx4090* | 37 | 6% |
| 18 | sn28 gm | 59.9 | 37.58 | 4,360 | rtx4090* | 19 | 49% |
| 19 | sn74 Gittensor | 58.5 | 25.66 | 243 | rtx4090* | 15 | 60% |
| 20 | sn51 lium.io | 57.9 | 26.52 | 2,745 | rtx4090* | 42 | 69% |

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
| wide (<30%) | 22 |
| concentrated (30–60%) | 25 |
| dominated (60–90%) | 17 |
| captured (>90%) | 27 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 104 |
| code-submission (validator runs it) | 9 |
| min_compute.yml (curated) | 9 |
| README keywords (GUESS) | 5 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-08-07T19:28 | sn28 | RELEASE | sn28 released v0.4.0 |
| 2026-08-07T19:28 | sn60 | SCORING_COMMIT | sn60 commit touches scoring: removed Chutes for miner submission |
| 2026-08-07T19:28 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Authorize isolated autoresearch validatio |
| 2026-08-07T18:10 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: refactor(scoring): one behavioural detect |
| 2026-08-07T17:22 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: feat(scoring): wire the anti-clone layers |
| 2026-08-07T17:22 | sn46 | SCORING_COMMIT | sn46 commit touches scoring: Add localnet miner validator and platform |
| 2026-08-07T17:22 | sn121 | BURN_DROP | sn121 burn fell 1.000 -> 0.828 - miners can earn again |
| 2026-08-07T16:08 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: fix(scoring): bind the medoid closure exp |
| 2026-08-07T16:08 | sn74 | RELEASE | sn74 released release-20260807-154750 |
| 2026-08-07T15:06 | sn10 | README_TASK_DIFF | sn10 README task/scoring sections changed |
| 2026-08-07T15:06 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: fix(scoring): group copies by behaviour,  |
| 2026-08-07T15:06 | sn100 | RELEASE | sn100 released v3.3.6 — Prism site window truthfulness |
| 2026-08-07T15:06 | sn126 | SCORING_COMMIT | sn126 commit touches scoring: Bump validator auto-update version |
| 2026-08-07T14:01 | sn100 | RELEASE | sn100 released v3.3.5 |
| 2026-08-07T12:31 | sn28 | BURN_DROP | sn28 burn fell 0.998 -> 0.471 - miners can earn again |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

