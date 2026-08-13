# Subnet watch — dashboard

_snapshot 2026-08-13T06:07:11Z · block 8833707 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 52 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 89 | `miner_burn` < 0.99 |
| Ranked | 89 | passed every gate |
| **Positive margin** | **52** | income beats machine cost |
| New events this window | 0 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 56 | `████████████████████████████` |
| 0–0.2 | 7 | `████` |
| 0.2–0.4 | 3 | `██` |
| 0.4–0.6 | 9 | `████` |
| 0.6–0.8 | 7 | `████` |
| 0.8–0.99 | 7 | `████` |
| ≥0.99 dead | 39 | `████████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn107 Minos | 77.8 | 105 | 30,475 | cpu-small | 20 | 90% |
| 2 | sn76 Phylax | 76.3 | 61.06 | 186 | cpu-small | 10 | 34% |
| 3 | sn98 NeverPlayAlone | 76.1 | 1,746 | 1,746 = | cpu-small | 1 | 100% |
| 4 | sn67 Harnyx | 71.2 | 17.05 | 702 | cpu-small | 145 | 19% |
| 5 | sn91 cascade | 69 | 559 | 1,287 | rtx4090* | 5 | 50% |
| 6 | sn62 Ridges | 69 | 543 | 1,963 | rtx4090* | 7 | 35% |
| 7 | sn56 Gradients | 68.9 | 531 | 978 | rtx4090* | 7 | 65% |
| 8 | sn41 Almanac | 68.9 | 10.31 | 30.04 | cpu-small | 68 | 72% |
| 9 | sn96 Verathos | 68.4 | 22.23 | 357 | rtx4090 | 58 | 42% |
| 10 | sn100 BASE | 68.1 | 425 | 425 = | rtx4090* | 5 | 50% |
| 11 | sn26 Perturb | 67.8 | 19.34 | 36.70 | rtx3060 | 11 | 50% |
| 12 | sn21 AdTAO | 67.6 | 7.50 | 33.66 | cpu-small | 88 | 45% |
| 13 | sn15 ORO | 67.2 | 8.99 | 21.17 | cpu-small | 69 | 94% |
| 14 | sn124 Swarm | 65.9 | 226 | 685 | rtx4090* | 23 | 11% |
| 15 | sn80 OpenRoboto | 64.7 | 154 | 561 | rtx4090* | 4 | 91% |
| 16 | sn85 Vidaio | 64 | 124 | 420 | rtx4090* | 10 | 17% |
| 17 | sn38 ChronoLLM | 63.1 | 107 | 1,556 | rtx4090* | 10 | 52% |
| 18 | sn28 gm | 61 | 50.90 | 2,930 | rtx4090* | 27 | 30% |
| 19 | sn51 lium.io | 60.6 | 51.65 | 2,236 | rtx4090* | 48 | 69% |
| 20 | sn61 RedTeam | 58.3 | 21.56 | 1,613 | rtx4090* | 59 | 35% |

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
| concentrated (30–60%) | 24 |
| dominated (60–90%) | 16 |
| captured (>90%) | 25 |

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
| 2026-08-13T04:32 | sn70 | BURN_DROP | sn70 burn fell 1.000 -> 0.000 - miners can earn again |
| 2026-08-13T04:32 | sn89 | SCORING_COMMIT | sn89 commit touches scoring: HF: measure miner behaviour above the boa |
| 2026-08-13T02:42 | sn51 | RELEASE | sn51 released executor-v1.118 |
| 2026-08-13T02:42 | sn66 | SCORING_COMMIT | sn66 commit touches scoring: Preserve production task retirements |
| 2026-08-13T02:42 | sn66 | README_TASK_DIFF | sn66 README task/scoring sections changed |
| 2026-08-13T02:42 | sn89 | SCORING_COMMIT | sn89 commit touches scoring: HF: submission-diversity gate — zero weig |
| 2026-08-13T02:42 | sn89 | README_TASK_DIFF | sn89 README task/scoring sections changed |
| 2026-08-12T23:55 | sn66 | README_TASK_DIFF | sn66 README task/scoring sections changed |
| 2026-08-12T22:57 | sn41 | SCORING_COMMIT | sn41 commit touches scoring: Merge pull request #42 from corvxai/mkt_s |
| 2026-08-12T18:40 | sn54 | SCORING_COMMIT | sn54 commit touches scoring: update miner screen reply readme |
| 2026-08-12T15:29 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: Add validator cost profile |
| 2026-08-12T14:09 | sn28 | RELEASE | sn28 released v0.4.4 |
| 2026-08-12T14:09 | sn28 | SCORING_COMMIT | sn28 commit touches scoring: Release gm-miner v0.4.4 |
| 2026-08-12T14:09 | sn56 | SCORING_COMMIT | sn56 commit touches scoring: Oversample 2026+ models into one R1 and o |
| 2026-08-12T14:09 | sn96 | RELEASE | sn96 released Verathos v0.1.37 — Scoring Integrity and Fairness |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

