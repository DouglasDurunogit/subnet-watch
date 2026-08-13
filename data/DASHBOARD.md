# Subnet watch — dashboard

_snapshot 2026-08-13T02:41:44Z · block 8832679 · run_status **ok**_

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
| New events this window | 5 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 57 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 3 | `█` |
| 0.4–0.6 | 9 | `████` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 38 | `███████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn107 Minos | 77.9 | 108 | 30,427 | cpu-small | 20 | 90% |
| 2 | sn76 Phylax | 76.2 | 58.90 | 184 | cpu-small | 10 | 34% |
| 3 | sn98 NeverPlayAlone | 76 | 1,726 | 1,726 = | cpu-small | 1 | 100% |
| 4 | sn67 Harnyx | 71.1 | 16.83 | 694 | cpu-small | 142 | 19% |
| 5 | sn96 Verathos | 69.1 | 26.46 | 334 | rtx4090 | 57 | 42% |
| 6 | sn91 cascade | 69 | 554 | 1,275 | rtx4090* | 5 | 50% |
| 7 | sn62 Ridges | 68.9 | 538 | 1,946 | rtx4090* | 7 | 35% |
| 8 | sn41 Almanac | 68.9 | 10.13 | 29.72 | cpu-small | 68 | 72% |
| 9 | sn56 Gradients | 68.8 | 525 | 967 | rtx4090* | 7 | 65% |
| 10 | sn100 BASE | 68.3 | 440 | 1,785 | rtx4090* | 5 | 50% |
| 11 | sn26 Perturb | 67.8 | 19.07 | 36.22 | rtx3060 | 11 | 50% |
| 12 | sn21 AdTAO | 67.5 | 7.40 | 33.26 | cpu-small | 88 | 45% |
| 13 | sn15 ORO | 66.9 | 8.83 | 20.80 | cpu-small | 69 | 94% |
| 14 | sn124 Swarm | 65.9 | 223 | 675 | rtx4090* | 23 | 11% |
| 15 | sn85 Vidaio | 64.8 | 159 | 495 | rtx4090* | 10 | 17% |
| 16 | sn38 ChronoLLM | 64.6 | 159 | 3,465 | rtx4090* | 10 | 52% |
| 17 | sn80 OpenRoboto | 64.6 | 148 | 540 | rtx4090* | 4 | 91% |
| 18 | sn51 lium.io | 60.4 | 49.63 | 2,203 | rtx4090* | 48 | 70% |
| 19 | sn61 RedTeam | 58.3 | 21.49 | 1,613 | rtx4090* | 59 | 35% |
| 20 | sn74 Gittensor | 58 | 22.47 | 212 | rtx4090* | 13 | 63% |

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
| concentrated (30–60%) | 23 |
| dominated (60–90%) | 17 |
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
| 2026-08-12T14:09 | sn96 | SCORING_COMMIT | sn96 commit touches scoring: fix: correct validator scoring inputs |
| 2026-08-12T14:09 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: publish bench rollout records: per-task  |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

