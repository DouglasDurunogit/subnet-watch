# Subnet watch — dashboard

_snapshot 2026-08-07T22:05:25Z · block 8795306 · run_status **ok**_

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
| New events this window | 1 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 54 | `████████████████████████████` |
| 0–0.2 | 6 | `███` |
| 0.2–0.4 | 5 | `███` |
| 0.4–0.6 | 11 | `██████` |
| 0.6–0.8 | 7 | `████` |
| 0.8–0.99 | 9 | `█████` |
| ≥0.99 dead | 36 | `███████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn107 Minos | 78.1 | 111 | 33,478 | cpu-small | 20 | 90% |
| 2 | sn60 Bitsec.ai | 74.9 | 1,235 | 1,235 = | cpu-small | 2 | 50% |
| 3 | sn114 SOMA | 72.7 | 1,670 | 4,356 | rtx4090* | 3 | 65% |
| 4 | sn67 Harnyx | 72.2 | 21.05 | 763 | cpu-small | 135 | 20% |
| 5 | sn1 Apex | 69.9 | 712 | 1,575 | rtx4090* | 4 | 39% |
| 6 | sn91 cascade | 69.8 | 699 | 2,819 | rtx4090* | 5 | 52% |
| 7 | sn62 Ridges | 69.1 | 566 | 2,047 | rtx4090* | 7 | 35% |
| 8 | sn15 ORO | 68.5 | 11.40 | 10,360 | cpu-small | 74 | 93% |
| 9 | sn26 Perturb | 68.1 | 20.86 | 40.46 | rtx3060 | 11 | 51% |
| 10 | sn100 BASE | 67.9 | 401 | 1,630 | rtx4090* | 5 | 50% |
| 11 | sn41 Almanac | 67.6 | 7.52 | 33.25 | cpu-small | 63 | 80% |
| 12 | sn124 Swarm | 65.6 | 207 | 595 | rtx4090* | 23 | 10% |
| 13 | sn21 AdTAO | 65.5 | 4.70 | 21.76 | cpu-small | 142 | 45% |
| 14 | sn96 Verathos | 64.8 | 9.56 | 219 | rtx4090 | 86 | 42% |
| 15 | sn61 RedTeam | 61.9 | 64.49 | 184 | rtx4090* | 37 | 6% |
| 16 | sn102 ConnitoAI | 59.5 | 31.32 | 1,712 | rtx4090* | 8 | 32% |
| 17 | sn28 gm | 59.4 | 32.32 | 4,512 | rtx4090* | 19 | 51% |
| 18 | sn74 Gittensor | 57.6 | 22.87 | 213 | rtx4090* | 15 | 64% |
| 19 | sn51 lium.io | 57.3 | 22.82 | 2,870 | rtx4090* | 44 | 66% |
| 20 | sn56 Gradients | 56.4 | 451 | 950 | rtx4090* | 7 | 70% |

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
| wide (<30%) | 21 |
| concentrated (30–60%) | 25 |
| dominated (60–90%) | 18 |
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
| 2026-08-07T21:11 | sn28 | RELEASE | sn28 released v0.4.1 |
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

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

