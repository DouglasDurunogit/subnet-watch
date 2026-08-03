# Subnet watch — dashboard

_snapshot 2026-08-03T20:38:55Z · block 8766081 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 54 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 94 | `miner_burn` < 0.99 |
| Ranked | 94 | passed every gate |
| **Positive margin** | **54** | income beats machine cost |
| New events this window | 1 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 56 | `████████████████████████████` |
| 0–0.2 | 6 | `███` |
| 0.2–0.4 | 3 | `██` |
| 0.4–0.6 | 9 | `████` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 12 | `██████` |
| ≥0.99 dead | 34 | `█████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn23 Trishool | 84.8 | 538 | 538 = | cpu-small | 5 | 20% |
| 2 | sn11 TrajectoryRL | 79.5 | 4,924 | 4,924 = | cpu-small | 1 | 100% |
| 3 | sn107 Minos | 77.8 | 105 | 26,572 | cpu-small | 20 | 89% |
| 4 | sn76 Phylax | 76.8 | 68.81 | 153 | cpu-small | 7 | 67% |
| 5 | sn60 Bitsec.ai | 76.5 | 1,965 | 1,965 = | cpu-small | 2 | 90% |
| 6 | sn67 Harnyx | 73.4 | 29.18 | 743 | cpu-small | 126 | 18% |
| 7 | sn102 ConnitoAI | 70.5 | 847 | 849 | rtx4090* | 4 | 25% |
| 8 | sn62 Ridges | 70 | 742 | 3,046 | rtx4090* | 7 | 39% |
| 9 | sn26 Perturb | 68.6 | 23.15 | 185 | rtx3060 | 11 | 51% |
| 10 | sn15 ORO | 67.1 | 8.22 | 17.09 | cpu-small | 86 | 93% |
| 11 | sn74 Gittensor | 66.2 | 241 | 387 | rtx4090* | 8 | 18% |
| 12 | sn124 Swarm | 66 | 230 | 675 | rtx4090* | 21 | 12% |
| 13 | sn21 AdTAO | 65.3 | 4.47 | 20.85 | cpu-small | 142 | 45% |
| 14 | sn85 Vidaio | 64.3 | 133 | 495 | rtx4090* | 10 | 17% |
| 15 | sn53 engy | 64.2 | 131 | 3,055 | rtx4090 | 28 | 17% |
| 16 | sn38 ChronoLLM | 62.9 | 99.35 | 1,449 | rtx4090* | 10 | 52% |
| 17 | sn71 Leadpoet | 58.5 | 23.15 | 190 | rtx4090* | 16 | 70% |
| 18 | sn41 Almanac | 58.5 | 1.32 | 66.00 | cpu-small | 34 | 93% |
| 19 | sn61 RedTeam | 58.2 | 21.18 | 75.63 | rtx4090* | 98 | 3% |
| 20 | sn28 gm | 56.6 | 14.50 | 2,513 | rtx4090* | 16 | 58% |

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
| dominated (60–90%) | 20 |
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
| 2026-08-03T20:39 | sn89 | SCORING_COMMIT | sn89 commit touches scoring: closers feed: per-key display-label overr |
| 2026-08-03T19:07 | sn80 | BURN_DROP | sn80 burn fell 1.000 -> 0.950 - miners can earn again |
| 2026-08-03T19:07 | sn112 | SCORING_COMMIT | sn112 commit touches scoring: chore(weights): champion burn 25% -> 80% |
| 2026-08-03T17:24 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: Add configurable PDF readers for claims  |
| 2026-08-03T17:24 | sn111 | README_TASK_DIFF | sn111 README task/scoring sections changed |
| 2026-08-03T17:24 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: Refactor lora evaluation runtime (#603) |
| 2026-08-03T17:24 | sn120 | README_TASK_DIFF | sn120 README task/scoring sections changed |
| 2026-08-03T17:24 | sn121 | BURN_DROP | sn121 burn fell 1.000 -> 0.830 - miners can earn again |
| 2026-08-03T15:12 | sn14 | SCORING_COMMIT | sn14 commit touches scoring: Merge pull request #74 from latent-to/cod |
| 2026-08-03T15:12 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: fix(validator): resolve scoring to weekly |
| 2026-08-03T15:12 | sn28 | RELEASE | sn28 released v0.3.16 |
| 2026-08-03T15:12 | sn50 | RELEASE | sn50 released v1.11.1 |
| 2026-08-03T15:12 | sn60 | SCORING_COMMIT | sn60 commit touches scoring: changed scoring model to kimi |
| 2026-08-03T15:12 | sn66 | SCORING_COMMIT | sn66 commit touches scoring: Merge pull request #8 from conjectures-io |
| 2026-08-03T15:12 | sn78 | BURN_DROP | sn78 burn fell 1.000 -> 0.000 - miners can earn again |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

