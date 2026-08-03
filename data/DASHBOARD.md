# Subnet watch — dashboard

_snapshot 2026-08-03T15:12:06Z · block 8764451 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 56 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 93 | `miner_burn` < 0.99 |
| Ranked | 93 | passed every gate |
| **Positive margin** | **56** | income beats machine cost |
| New events this window | 8 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 57 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 7 | `███` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 8 | `████` |
| ≥0.99 dead | 35 | `█████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn23 Trishool | 84.9 | 549 | 549 = | cpu-small | 5 | 20% |
| 2 | sn107 Minos | 77.1 | 90.06 | 26,297 | cpu-small | 20 | 90% |
| 3 | sn60 Bitsec.ai | 76.4 | 1,950 | 1,950 = | cpu-small | 2 | 90% |
| 4 | sn67 Harnyx | 73.3 | 29.38 | 749 | cpu-small | 124 | 18% |
| 5 | sn62 Ridges | 70 | 743 | 3,050 | rtx4090* | 7 | 39% |
| 6 | sn41 Almanac | 69.9 | 12.79 | 36.60 | cpu-small | 52 | 75% |
| 7 | sn102 ConnitoAI | 69.7 | 678 | 1,184 | rtx4090* | 5 | 34% |
| 8 | sn56 Gradients | 69.1 | 563 | 1,185 | rtx4090* | 6 | 64% |
| 9 | sn26 Perturb | 68.6 | 23.70 | 189 | rtx3060 | 11 | 51% |
| 10 | sn15 ORO | 67.1 | 8.04 | 16.90 | cpu-small | 83 | 93% |
| 11 | sn74 Gittensor | 66.3 | 247 | 440 | rtx4090* | 8 | 18% |
| 12 | sn124 Swarm | 65.7 | 210 | 637 | rtx4090* | 21 | 12% |
| 13 | sn21 AdTAO | 64.8 | 4.02 | 24.52 | cpu-small | 126 | 50% |
| 14 | sn53 engy | 64.1 | 126 | 2,942 | rtx4090 | 28 | 17% |
| 15 | sn85 Vidaio | 63.6 | 110 | 480 | rtx4090* | 10 | 17% |
| 16 | sn38 ChronoLLM | 62.9 | 101 | 1,472 | rtx4090* | 10 | 52% |
| 17 | sn61 RedTeam | 58.6 | 24.20 | 85.60 | rtx4090* | 94 | 3% |
| 18 | sn71 Leadpoet | 58.4 | 22.43 | 186 | rtx4090* | 16 | 70% |
| 19 | sn51 lium.io | 56.1 | 17.56 | 5,842 | rtx4090* | 43 | 48% |
| 20 | sn28 gm | 55.9 | 11.75 | 2,459 | rtx4090* | 15 | 59% |

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
| dominated (60–90%) | 19 |
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
| 2026-08-03T12:03 | sn60 | SCORING_COMMIT | sn60 commit touches scoring: changed scorer model to deepseek 3.2 |
| 2026-08-03T12:03 | sn66 | SCORING_COMMIT | sn66 commit touches scoring: name scripts/pin_dependencies.sh when the |
| 2026-08-03T12:03 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Prepare isolated validator host Sentry ru |
| 2026-08-03T05:02 | sn41 | SCORING_COMMIT | sn41 commit touches scoring: Updating README to include the almanac ma |
| 2026-08-03T05:02 | sn41 | README_TASK_DIFF | sn41 README task/scoring sections changed |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

