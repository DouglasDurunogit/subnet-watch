# Subnet watch — dashboard

_snapshot 2026-08-07T20:24:00Z · block 8794799 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 56 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 92 | `miner_burn` < 0.99 |
| Ranked | 92 | passed every gate |
| **Positive margin** | **56** | income beats machine cost |
| New events this window | 5 | see ALARMS.md |

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
| 0.6–0.8 | 9 | `█████` |
| 0.8–0.99 | 8 | `████` |
| ≥0.99 dead | 36 | `███████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn107 Minos | 78 | 110 | 31,752 | cpu-small | 20 | 90% |
| 2 | sn76 Phylax | 77.1 | 75.61 | 275 | cpu-small | 10 | 31% |
| 3 | sn98 NeverPlayAlone | 76 | 1,704 | 1,704 = | cpu-small | 1 | 100% |
| 4 | sn60 Bitsec.ai | 74.9 | 1,234 | 1,234 = | cpu-small | 2 | 50% |
| 5 | sn114 SOMA | 72.7 | 1,674 | 4,366 | rtx4090* | 3 | 65% |
| 6 | sn67 Harnyx | 72.2 | 21.06 | 763 | cpu-small | 135 | 20% |
| 7 | sn1 Apex | 69.9 | 709 | 1,463 | rtx4090* | 4 | 41% |
| 8 | sn102 ConnitoAI | 69.6 | 655 | 1,362 | rtx4090* | 7 | 25% |
| 9 | sn62 Ridges | 69.1 | 564 | 2,041 | rtx4090* | 7 | 35% |
| 10 | sn91 cascade | 68.6 | 494 | 1,402 | rtx4090* | 5 | 52% |
| 11 | sn15 ORO | 68.5 | 11.47 | 10,340 | cpu-small | 74 | 93% |
| 12 | sn26 Perturb | 68.2 | 21.40 | 40.48 | rtx3060 | 11 | 51% |
| 13 | sn100 BASE | 67.9 | 399 | 1,619 | rtx4090* | 5 | 50% |
| 14 | sn41 Almanac | 67.6 | 7.54 | 44.50 | cpu-small | 62 | 80% |
| 15 | sn96 Verathos | 66.9 | 15.44 | 221 | rtx4090 | 65 | 43% |
| 16 | sn124 Swarm | 65.6 | 207 | 596 | rtx4090* | 23 | 10% |
| 17 | sn21 AdTAO | 65.5 | 4.73 | 21.89 | cpu-small | 142 | 45% |
| 18 | sn61 RedTeam | 61.9 | 66.30 | 183 | rtx4090* | 37 | 6% |
| 19 | sn28 gm | 59.9 | 37.50 | 4,352 | rtx4090* | 19 | 49% |
| 20 | sn74 Gittensor | 58.5 | 25.62 | 242 | rtx4090* | 15 | 60% |

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
| 2026-08-07T20:24 | sn1 | RELEASE | sn1 released v4.2.21 |
| 2026-08-07T20:24 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: Fix A10 GPU model normalization in valida |
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

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

