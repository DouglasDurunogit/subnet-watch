# Subnet watch — dashboard

_snapshot 2026-08-07T15:05:52Z · block 8793208 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 57 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 91 | `miner_burn` < 0.99 |
| Ranked | 91 | passed every gate |
| **Positive margin** | **57** | income beats machine cost |
| New events this window | 5 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 56 | `████████████████████████████` |
| 0–0.2 | 5 | `██` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 11 | `██████` |
| 0.6–0.8 | 6 | `███` |
| 0.8–0.99 | 8 | `████` |
| ≥0.99 dead | 37 | `██████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn11 TrajectoryRL | 79.8 | 5,374 | 5,374 = | cpu-small | 1 | 100% |
| 2 | sn107 Minos | 78.8 | 131 | 31,782 | cpu-small | 20 | 90% |
| 3 | sn76 Phylax | 77.1 | 74.66 | 270 | cpu-small | 10 | 31% |
| 4 | sn98 NeverPlayAlone | 76 | 1,693 | 1,693 = | cpu-small | 1 | 100% |
| 5 | sn60 Bitsec.ai | 75.1 | 1,292 | 1,292 = | cpu-small | 2 | 50% |
| 6 | sn114 SOMA | 72.7 | 1,644 | 4,288 | rtx4090* | 3 | 65% |
| 7 | sn67 Harnyx | 72 | 20.98 | 760 | cpu-small | 135 | 20% |
| 8 | sn62 Ridges | 69 | 557 | 2,016 | rtx4090* | 7 | 35% |
| 9 | sn96 Verathos | 68.8 | 24.34 | 329 | rtx4090 | 45 | 43% |
| 10 | sn91 cascade | 68.7 | 512 | 1,452 | rtx4090* | 5 | 52% |
| 11 | sn15 ORO | 68.4 | 11.37 | 10,254 | cpu-small | 74 | 93% |
| 12 | sn26 Perturb | 68.2 | 21.25 | 38.64 | rtx3060 | 11 | 51% |
| 13 | sn100 BASE | 67.9 | 398 | 1,624 | rtx4090* | 5 | 50% |
| 14 | sn41 Almanac | 67.5 | 7.40 | 44.47 | cpu-small | 62 | 80% |
| 15 | sn124 Swarm | 65.5 | 204 | 588 | rtx4090* | 23 | 10% |
| 16 | sn21 AdTAO | 65.5 | 4.70 | 21.74 | cpu-small | 142 | 45% |
| 17 | sn74 Gittensor | 65.3 | 182 | 385 | rtx4090* | 9 | 18% |
| 18 | sn61 RedTeam | 62.2 | 72.67 | 187 | rtx4090* | 38 | 6% |
| 19 | sn51 lium.io | 59.3 | 36.69 | 2,971 | rtx4090* | 40 | 69% |
| 20 | sn28 gm | 58.4 | 24.13 | 3,528 | rtx4090* | 19 | 41% |

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
| dominated (60–90%) | 16 |
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
| 2026-08-07T15:06 | sn10 | README_TASK_DIFF | sn10 README task/scoring sections changed |
| 2026-08-07T15:06 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: fix(scoring): group copies by behaviour,  |
| 2026-08-07T15:06 | sn100 | RELEASE | sn100 released v3.3.6 — Prism site window truthfulness |
| 2026-08-07T15:06 | sn126 | SCORING_COMMIT | sn126 commit touches scoring: Bump validator auto-update version |
| 2026-08-07T14:01 | sn100 | RELEASE | sn100 released v3.3.5 |
| 2026-08-07T12:31 | sn28 | BURN_DROP | sn28 burn fell 0.998 -> 0.471 - miners can earn again |
| 2026-08-07T12:31 | sn126 | SCORING_COMMIT | sn126 commit touches scoring: Gate validator rounds by launch status |
| 2026-08-07T11:34 | sn66 | SCORING_COMMIT | sn66 commit touches scoring: Merge pull request #30 from conjectures-i |
| 2026-08-07T10:38 | sn66 | SCORING_COMMIT | sn66 commit touches scoring: fix catalag endpoint pydantic type valida |
| 2026-08-07T10:38 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: Document miner batch and PDF options |
| 2026-08-07T10:38 | sn111 | README_TASK_DIFF | sn111 README task/scoring sections changed |
| 2026-08-07T09:31 | sn90 | RELEASE | sn90 released v1.0.1 |
| 2026-08-07T09:31 | sn90 | SCORING_COMMIT | sn90 commit touches scoring: fix(subnet): proxy rejects miners — only  |
| 2026-08-07T09:31 | sn114 | SCORING_COMMIT | sn114 commit touches scoring: Merge pull request #218 from DendriteHQ/ |
| 2026-08-07T08:20 | sn100 | BURN_DROP | sn100 burn fell 1.000 -> 0.269 - miners can earn again |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

