# Subnet watch — dashboard

_snapshot 2026-08-04T04:26:17Z · block 8768416 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 52 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 93 | `miner_burn` < 0.99 |
| Ranked | 93 | passed every gate |
| **Positive margin** | **52** | income beats machine cost |
| New events this window | 5 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 56 | `████████████████████████████` |
| 0–0.2 | 5 | `██` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 6 | `███` |
| 0.6–0.8 | 10 | `█████` |
| 0.8–0.99 | 12 | `██████` |
| ≥0.99 dead | 35 | `██████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn23 Trishool | 84.9 | 542 | 542 = | cpu-small | 5 | 20% |
| 2 | sn107 Minos | 78.4 | 119 | 26,483 | cpu-small | 20 | 88% |
| 3 | sn76 Phylax | 77.2 | 77.44 | 157 | cpu-small | 7 | 66% |
| 4 | sn60 Bitsec.ai | 76.4 | 1,951 | 1,951 = | cpu-small | 2 | 90% |
| 5 | sn98 NeverPlayAlone | 75.9 | 1,675 | 1,675 = | cpu-small | 1 | 100% |
| 6 | sn67 Harnyx | 71.9 | 20.78 | 701 | cpu-small | 144 | 17% |
| 7 | sn102 ConnitoAI | 70 | 751 | 751 = | rtx4090* | 4 | 25% |
| 8 | sn62 Ridges | 70 | 745 | 3,057 | rtx4090* | 7 | 39% |
| 9 | sn26 Perturb | 68.6 | 23.71 | 184 | rtx3060 | 11 | 50% |
| 10 | sn15 ORO | 66.9 | 8.32 | 17.29 | cpu-small | 86 | 93% |
| 11 | sn74 Gittensor | 66.1 | 235 | 355 | rtx4090* | 8 | 18% |
| 12 | sn124 Swarm | 66 | 234 | 684 | rtx4090* | 21 | 12% |
| 13 | sn38 ChronoLLM | 65.4 | 199 | 3,344 | rtx4090* | 10 | 52% |
| 14 | sn41 Almanac | 65.3 | 4.50 | 66.82 | cpu-small | 36 | 89% |
| 15 | sn21 AdTAO | 65.3 | 4.46 | 20.80 | cpu-small | 142 | 45% |
| 16 | sn85 Vidaio | 64.2 | 129 | 457 | rtx4090* | 10 | 16% |
| 17 | sn53 engy | 64.1 | 129 | 3,005 | rtx4090 | 28 | 17% |
| 18 | sn61 RedTeam | 58.3 | 21.68 | 76.43 | rtx4090* | 98 | 3% |
| 19 | sn9 iota | 55.3 | 8,710 | 8,710 = | rtx4090* | 3 | 50% |
| 20 | sn28 gm | 53 | 5.62 | 2,288 | rtx4090* | 17 | 63% |

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
| concentrated (30–60%) | 21 |
| dominated (60–90%) | 22 |
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
| 2026-08-04T04:26 | sn66 | SCORING_COMMIT | sn66 commit touches scoring: Merge pull request #10 from conjectures-i |
| 2026-08-04T04:26 | sn66 | README_TASK_DIFF | sn66 README task/scoring sections changed |
| 2026-08-04T04:26 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-08-04T04:26 | sn107 | WEIGHTS_VERSION_BUMP | sn107 weights_version 13 -> 20 |
| 2026-08-04T04:26 | sn107 | README_TASK_DIFF | sn107 README task/scoring sections changed |
| 2026-08-04T00:59 | sn61 | RELEASE | sn61 released 4.8.4 |
| 2026-08-04T00:59 | sn61 | SCORING_COMMIT | sn61 commit touches scoring: fix: handle miner hotkey changes in updat |
| 2026-08-03T23:17 | sn13 | RELEASE | sn13 released Release v1.18.69 |
| 2026-08-03T23:17 | sn54 | SCORING_COMMIT | sn54 commit touches scoring: Made miner process more Intuitive |
| 2026-08-03T20:39 | sn89 | SCORING_COMMIT | sn89 commit touches scoring: closers feed: per-key display-label overr |
| 2026-08-03T19:07 | sn80 | BURN_DROP | sn80 burn fell 1.000 -> 0.950 - miners can earn again |
| 2026-08-03T19:07 | sn112 | SCORING_COMMIT | sn112 commit touches scoring: chore(weights): champion burn 25% -> 80% |
| 2026-08-03T17:24 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: Add configurable PDF readers for claims  |
| 2026-08-03T17:24 | sn111 | README_TASK_DIFF | sn111 README task/scoring sections changed |
| 2026-08-03T17:24 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: Refactor lora evaluation runtime (#603) |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

