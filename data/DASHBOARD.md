# Subnet watch — dashboard

_snapshot 2026-08-13T04:31:55Z · block 8833230 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 51 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 90 | `miner_burn` < 0.99 |
| Ranked | 90 | passed every gate |
| **Positive margin** | **51** | income beats machine cost |
| New events this window | 2 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 57 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 3 | `█` |
| 0.4–0.6 | 8 | `████` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 38 | `███████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn107 Minos | 77.8 | 105 | 30,247 | cpu-small | 20 | 90% |
| 2 | sn76 Phylax | 76.2 | 60.01 | 184 | cpu-small | 10 | 34% |
| 3 | sn98 NeverPlayAlone | 76.1 | 1,743 | 1,743 = | cpu-small | 1 | 100% |
| 4 | sn67 Harnyx | 71.2 | 17.01 | 701 | cpu-small | 144 | 19% |
| 5 | sn96 Verathos | 70 | 33.20 | 353 | rtx4090 | 54 | 42% |
| 6 | sn91 cascade | 69 | 558 | 1,284 | rtx4090* | 5 | 50% |
| 7 | sn62 Ridges | 69 | 541 | 1,959 | rtx4090* | 7 | 35% |
| 8 | sn56 Gradients | 68.9 | 530 | 976 | rtx4090* | 7 | 65% |
| 9 | sn41 Almanac | 68.9 | 10.28 | 29.98 | cpu-small | 68 | 72% |
| 10 | sn100 BASE | 68.3 | 443 | 443 = | rtx4090* | 5 | 50% |
| 11 | sn26 Perturb | 67.8 | 19.29 | 36.61 | rtx3060 | 11 | 50% |
| 12 | sn15 ORO | 67.2 | 8.99 | 21.17 | cpu-small | 69 | 94% |
| 13 | sn124 Swarm | 65.9 | 225 | 681 | rtx4090* | 23 | 11% |
| 14 | sn80 OpenRoboto | 64.8 | 156 | 567 | rtx4090* | 4 | 91% |
| 15 | sn85 Vidaio | 64.5 | 145 | 500 | rtx4090* | 10 | 17% |
| 16 | sn38 ChronoLLM | 63.2 | 108 | 1,563 | rtx4090* | 10 | 52% |
| 17 | sn51 lium.io | 60.4 | 49.00 | 2,145 | rtx4090* | 49 | 69% |
| 18 | sn28 gm | 58.5 | 24.66 | 2,750 | rtx4090* | 29 | 28% |
| 19 | sn61 RedTeam | 58.3 | 21.55 | 1,616 | rtx4090* | 59 | 35% |
| 20 | sn74 Gittensor | 57.6 | 19.84 | 215 | rtx4090* | 13 | 63% |

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
| concentrated (30–60%) | 22 |
| dominated (60–90%) | 18 |
| captured (>90%) | 24 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 108 |
| code-submission (validator runs it) | 8 |
| min_compute.yml (curated) | 6 |
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

