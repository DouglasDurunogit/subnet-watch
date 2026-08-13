# Subnet watch — dashboard

_snapshot 2026-08-13T14:10:12Z · block 8836122 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 51 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 89 | `miner_burn` < 0.99 |
| Ranked | 89 | passed every gate |
| **Positive margin** | **51** | income beats machine cost |
| New events this window | 1 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 56 | `████████████████████████████` |
| 0–0.2 | 8 | `████` |
| 0.2–0.4 | 2 | `█` |
| 0.4–0.6 | 9 | `████` |
| 0.6–0.8 | 7 | `████` |
| 0.8–0.99 | 7 | `████` |
| ≥0.99 dead | 39 | `████████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn107 Minos | 78 | 110 | 31,946 | cpu-small | 20 | 90% |
| 2 | sn76 Phylax | 74.7 | 39.85 | 191 | cpu-small | 10 | 34% |
| 3 | sn67 Harnyx | 71.2 | 17.05 | 702 | cpu-small | 148 | 19% |
| 4 | sn91 cascade | 69 | 558 | 1,285 | rtx4090* | 5 | 50% |
| 5 | sn62 Ridges | 69 | 545 | 1,973 | rtx4090* | 7 | 35% |
| 6 | sn41 Almanac | 69 | 10.36 | 29.16 | cpu-small | 68 | 72% |
| 7 | sn56 Gradients | 68.9 | 532 | 982 | rtx4090* | 7 | 65% |
| 8 | sn96 Verathos | 68.6 | 23.68 | 254 | rtx4090 | 56 | 43% |
| 9 | sn100 BASE | 68.1 | 415 | 1,839 | rtx4090* | 5 | 52% |
| 10 | sn26 Perturb | 67.9 | 19.60 | 840 | rtx3060 | 11 | 50% |
| 11 | sn85 Vidaio | 67.6 | 365 | 467 | rtx4090* | 10 | 20% |
| 12 | sn21 AdTAO | 67.6 | 7.61 | 34.11 | cpu-small | 88 | 45% |
| 13 | sn124 Swarm | 65.9 | 223 | 477 | rtx4090* | 23 | 11% |
| 14 | sn38 ChronoLLM | 64.6 | 160 | 3,492 | rtx4090* | 10 | 52% |
| 15 | sn80 OpenRoboto | 62.9 | 87.25 | 604 | rtx4090* | 4 | 92% |
| 16 | sn28 gm | 60.9 | 49.70 | 3,044 | rtx4090* | 28 | 30% |
| 17 | sn51 lium.io | 59.7 | 41.76 | 1,984 | rtx4090* | 45 | 77% |
| 18 | sn74 Gittensor | 58.4 | 24.75 | 216 | rtx4090* | 13 | 63% |
| 19 | sn61 RedTeam | 58.4 | 22.38 | 1,642 | rtx4090* | 58 | 35% |
| 20 | sn2 DSperse | 55.3 | 8.45 | 79.92 | rtx4090* | 13 | 83% |

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
| dominated (60–90%) | 17 |
| captured (>90%) | 24 |

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
| 2026-08-13T14:10 | sn1 | RELEASE | sn1 released v4.3.1 |
| 2026-08-13T12:36 | sn90 | README_TASK_DIFF | sn90 README task/scoring sections changed |
| 2026-08-13T10:35 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-08-13T10:35 | sn67 | README_TASK_DIFF | sn67 README task/scoring sections changed |
| 2026-08-13T09:22 | sn44 | SCORING_COMMIT | sn44 commit touches scoring: blacklist + min common challenges tiebrea |
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

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

