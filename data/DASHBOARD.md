# Subnet watch — dashboard

_snapshot 2026-08-07T18:10:13Z · block 8794130 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 55 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 92 | `miner_burn` < 0.99 |
| Ranked | 92 | passed every gate |
| **Positive margin** | **55** | income beats machine cost |
| New events this window | 4 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 54 | `████████████████████████████` |
| 0–0.2 | 5 | `███` |
| 0.2–0.4 | 5 | `███` |
| 0.4–0.6 | 12 | `██████` |
| 0.6–0.8 | 6 | `███` |
| 0.8–0.99 | 10 | `█████` |
| ≥0.99 dead | 36 | `███████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn107 Minos | 77.9 | 106 | 31,253 | cpu-small | 20 | 89% |
| 2 | sn76 Phylax | 77.1 | 75.07 | 271 | cpu-small | 10 | 31% |
| 3 | sn98 NeverPlayAlone | 75.9 | 1,683 | 1,683 = | cpu-small | 1 | 100% |
| 4 | sn60 Bitsec.ai | 75 | 1,280 | 1,280 = | cpu-small | 2 | 50% |
| 5 | sn114 SOMA | 72.7 | 1,647 | 4,296 | rtx4090* | 3 | 65% |
| 6 | sn67 Harnyx | 72.1 | 20.79 | 754 | cpu-small | 135 | 20% |
| 7 | sn62 Ridges | 69.1 | 558 | 2,018 | rtx4090* | 7 | 35% |
| 8 | sn91 cascade | 68.6 | 483 | 1,372 | rtx4090* | 5 | 52% |
| 9 | sn15 ORO | 68.2 | 11.29 | 10,185 | cpu-small | 74 | 93% |
| 10 | sn26 Perturb | 68.1 | 20.70 | 38.64 | rtx3060 | 11 | 51% |
| 11 | sn96 Verathos | 68 | 20.24 | 274 | rtx4090 | 54 | 43% |
| 12 | sn100 BASE | 67.9 | 394 | 1,599 | rtx4090* | 5 | 50% |
| 13 | sn41 Almanac | 67.5 | 7.35 | 44.16 | cpu-small | 62 | 80% |
| 14 | sn124 Swarm | 65.6 | 207 | 595 | rtx4090* | 23 | 11% |
| 15 | sn21 AdTAO | 65.5 | 4.66 | 21.61 | cpu-small | 142 | 45% |
| 16 | sn61 RedTeam | 62 | 67.07 | 180 | rtx4090* | 37 | 6% |
| 17 | sn102 ConnitoAI | 59.6 | 32.17 | 1,387 | rtx4090* | 8 | 26% |
| 18 | sn28 gm | 59.2 | 30.41 | 4,190 | rtx4090* | 19 | 48% |
| 19 | sn74 Gittensor | 58.4 | 25.04 | 241 | rtx4090* | 15 | 60% |
| 20 | sn51 lium.io | 57.2 | 22.69 | 2,305 | rtx4090* | 43 | 70% |

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
| wide (<30%) | 23 |
| concentrated (30–60%) | 25 |
| dominated (60–90%) | 17 |
| captured (>90%) | 26 |

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
| 2026-08-07T12:31 | sn126 | SCORING_COMMIT | sn126 commit touches scoring: Gate validator rounds by launch status |
| 2026-08-07T11:34 | sn66 | SCORING_COMMIT | sn66 commit touches scoring: Merge pull request #30 from conjectures-i |
| 2026-08-07T10:38 | sn66 | SCORING_COMMIT | sn66 commit touches scoring: fix catalag endpoint pydantic type valida |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

