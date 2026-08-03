# Subnet watch — dashboard

_snapshot 2026-08-03T12:02:51Z · block 8763505 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 52 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 94 | `miner_burn` < 0.99 |
| Ranked | 94 | passed every gate |
| **Positive margin** | **52** | income beats machine cost |
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
| 0.4–0.6 | 8 | `████` |
| 0.6–0.8 | 10 | `█████` |
| 0.8–0.99 | 8 | `████` |
| ≥0.99 dead | 34 | `█████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn23 Trishool | 84.9 | 551 | 551 = | cpu-small | 5 | 20% |
| 2 | sn107 Minos | 77.3 | 93.11 | 26,948 | cpu-small | 20 | 90% |
| 3 | sn67 Harnyx | 73.3 | 29.39 | 749 | cpu-small | 123 | 18% |
| 4 | sn102 ConnitoAI | 71.1 | 1,025 | 1,301 | rtx4090* | 4 | 35% |
| 5 | sn41 Almanac | 69.9 | 12.88 | 36.86 | cpu-small | 52 | 75% |
| 6 | sn62 Ridges | 69.7 | 672 | 3,106 | rtx4090* | 7 | 39% |
| 7 | sn56 Gradients | 69.1 | 559 | 1,178 | rtx4090* | 6 | 64% |
| 8 | sn26 Perturb | 68.6 | 23.47 | 189 | rtx3060 | 11 | 51% |
| 9 | sn15 ORO | 67.1 | 7.96 | 17.06 | cpu-small | 80 | 93% |
| 10 | sn74 Gittensor | 66.2 | 239 | 472 | rtx4090* | 8 | 20% |
| 11 | sn124 Swarm | 65.7 | 212 | 644 | rtx4090* | 21 | 12% |
| 12 | sn85 Vidaio | 64.6 | 147 | 476 | rtx4090* | 10 | 16% |
| 13 | sn53 engy | 64 | 124 | 2,916 | rtx4090 | 28 | 17% |
| 14 | sn38 ChronoLLM | 62.8 | 101 | 1,476 | rtx4090* | 10 | 52% |
| 15 | sn71 Leadpoet | 58.9 | 26.14 | 209 | rtx4090* | 16 | 70% |
| 16 | sn61 RedTeam | 58.6 | 23.66 | 85.46 | rtx4090* | 95 | 3% |
| 17 | sn28 gm | 57 | 16.26 | 2,736 | rtx4090* | 14 | 57% |
| 18 | sn9 iota | 55.3 | 8,749 | 8,749 = | rtx4090* | 3 | 52% |
| 19 | sn51 lium.io | 55.3 | 14.95 | 5,618 | rtx4090* | 43 | 49% |
| 20 | sn90 KubeTEE AI Facto | 53.2 | 3,663 | 3,663 = | rtx4090* | 2 | 71% |

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
| concentrated (30–60%) | 25 |
| dominated (60–90%) | 19 |
| captured (>90%) | 24 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 105 |
| code-submission (validator runs it) | 9 |
| min_compute.yml (curated) | 9 |
| README keywords (GUESS) | 4 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-08-03T12:03 | sn51 | RELEASE | sn51 released executor-v1.115 |
| 2026-08-03T12:03 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-2535: add xet challenge in verifyx (# |
| 2026-08-03T12:03 | sn60 | SCORING_COMMIT | sn60 commit touches scoring: changed scorer model to deepseek 3.2 |
| 2026-08-03T12:03 | sn66 | SCORING_COMMIT | sn66 commit touches scoring: name scripts/pin_dependencies.sh when the |
| 2026-08-03T12:03 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Prepare isolated validator host Sentry ru |
| 2026-08-03T05:02 | sn41 | SCORING_COMMIT | sn41 commit touches scoring: Updating README to include the almanac ma |
| 2026-08-03T05:02 | sn41 | README_TASK_DIFF | sn41 README task/scoring sections changed |
| 2026-08-03T05:02 | sn66 | SCORING_COMMIT | sn66 commit touches scoring: Merge pull request #6 from conjectures-io |
| 2026-08-03T05:02 | sn66 | README_TASK_DIFF | sn66 README task/scoring sections changed |
| 2026-08-03T05:02 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Bind model scoring to measured catalog ex |
| 2026-08-03T01:17 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Rebind validator telemetry recovery ident |
| 2026-08-02T23:32 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Bind validator Sentry instrumentation ide |
| 2026-08-02T22:27 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Make validator storage cleanup dependency |
| 2026-08-02T21:08 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Reclaim stale validator builder mounts |
| 2026-08-02T18:45 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Preserve validator builds after failed de |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

