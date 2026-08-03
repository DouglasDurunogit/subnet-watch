# Subnet watch — dashboard

_snapshot 2026-08-03T17:24:22Z · block 8765113 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 56 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 94 | `miner_burn` < 0.99 |
| Ranked | 94 | passed every gate |
| **Positive margin** | **56** | income beats machine cost |
| New events this window | 5 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 57 | `████████████████████████████` |
| 0–0.2 | 6 | `███` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 7 | `███` |
| 0.6–0.8 | 10 | `█████` |
| 0.8–0.99 | 9 | `████` |
| ≥0.99 dead | 34 | `█████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn23 Trishool | 84.8 | 535 | 535 = | cpu-small | 5 | 20% |
| 2 | sn11 TrajectoryRL | 79.5 | 4,911 | 4,911 = | cpu-small | 1 | 100% |
| 3 | sn107 Minos | 77.6 | 101 | 26,159 | cpu-small | 20 | 89% |
| 4 | sn120 Affine | 77.1 | 6,140 | 6,140 = | rtx4090* | 5 | 20% |
| 5 | sn60 Bitsec.ai | 76.4 | 1,950 | 1,950 = | cpu-small | 2 | 90% |
| 6 | sn67 Harnyx | 73.3 | 29.04 | 740 | cpu-small | 125 | 18% |
| 7 | sn102 ConnitoAI | 70.5 | 856 | 856 = | rtx4090* | 4 | 25% |
| 8 | sn62 Ridges | 70 | 742 | 3,045 | rtx4090* | 7 | 39% |
| 9 | sn41 Almanac | 69.9 | 12.86 | 36.79 | cpu-small | 52 | 75% |
| 10 | sn56 Gradients | 69.1 | 567 | 1,195 | rtx4090* | 6 | 64% |
| 11 | sn26 Perturb | 68.6 | 23.15 | 191 | rtx3060 | 11 | 51% |
| 12 | sn15 ORO | 67 | 8.17 | 16.99 | cpu-small | 86 | 93% |
| 13 | sn74 Gittensor | 66 | 229 | 400 | rtx4090* | 8 | 18% |
| 14 | sn124 Swarm | 65.9 | 224 | 680 | rtx4090* | 21 | 12% |
| 15 | sn21 AdTAO | 64.8 | 3.99 | 25.46 | cpu-small | 126 | 51% |
| 16 | sn53 engy | 64.1 | 127 | 2,962 | rtx4090 | 28 | 17% |
| 17 | sn85 Vidaio | 63.7 | 112 | 480 | rtx4090* | 10 | 16% |
| 18 | sn38 ChronoLLM | 62.9 | 98.87 | 1,442 | rtx4090* | 10 | 52% |
| 19 | sn71 Leadpoet | 58.7 | 24.55 | 199 | rtx4090* | 16 | 70% |
| 20 | sn61 RedTeam | 58.2 | 20.98 | 75.25 | rtx4090* | 100 | 3% |

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
| dominated (60–90%) | 21 |
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
| 2026-08-03T15:12 | sn89 | README_TASK_DIFF | sn89 README task/scoring sections changed |
| 2026-08-03T12:03 | sn51 | RELEASE | sn51 released executor-v1.115 |
| 2026-08-03T12:03 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-2535: add xet challenge in verifyx (# |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

