# Subnet watch — dashboard

_snapshot 2026-08-03T05:01:28Z · block 8761398 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 54 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 96 | `miner_burn` < 0.99 |
| Ranked | 96 | passed every gate |
| **Positive margin** | **54** | income beats machine cost |
| New events this window | 5 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 58 | `████████████████████████████` |
| 0–0.2 | 6 | `███` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 8 | `████` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 10 | `█████` |
| ≥0.99 dead | 32 | `███████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn23 Trishool | 85 | 555 | 555 = | cpu-small | 5 | 20% |
| 2 | sn107 Minos | 77.7 | 102 | 26,645 | cpu-small | 20 | 89% |
| 3 | sn98 NeverPlayAlone | 75.9 | 1,679 | 1,679 = | cpu-small | 1 | 100% |
| 4 | sn67 Harnyx | 73.4 | 29.62 | 754 | cpu-small | 123 | 18% |
| 5 | sn41 Almanac | 70 | 13.05 | 37.32 | cpu-small | 52 | 75% |
| 6 | sn62 Ridges | 69.8 | 703 | 3,249 | rtx4090* | 7 | 39% |
| 7 | sn102 ConnitoAI | 69.6 | 649 | 1,372 | rtx4090* | 6 | 36% |
| 8 | sn56 Gradients | 69.1 | 570 | 1,202 | rtx4090* | 6 | 64% |
| 9 | sn26 Perturb | 68.7 | 24.00 | 193 | rtx3060 | 11 | 50% |
| 10 | sn15 ORO | 67.1 | 7.63 | 16.08 | cpu-small | 94 | 93% |
| 11 | sn74 Gittensor | 66 | 224 | 368 | rtx4090* | 8 | 19% |
| 12 | sn124 Swarm | 65.9 | 224 | 666 | rtx4090* | 20 | 12% |
| 13 | sn85 Vidaio | 63.9 | 121 | 470 | rtx4090* | 10 | 16% |
| 14 | sn53 engy | 63.8 | 116 | 2,745 | rtx4090 | 28 | 17% |
| 15 | sn38 ChronoLLM | 63 | 102 | 1,488 | rtx4090* | 10 | 52% |
| 16 | sn71 Leadpoet | 58.8 | 25.19 | 203 | rtx4090* | 16 | 70% |
| 17 | sn61 RedTeam | 58.5 | 22.90 | 84.20 | rtx4090* | 97 | 3% |
| 18 | sn28 gm | 57.9 | 20.81 | 2,372 | rtx4090* | 14 | 62% |
| 19 | sn51 lium.io | 55.8 | 16.54 | 5,851 | rtx4090* | 42 | 48% |
| 20 | sn9 iota | 55.5 | 9,856 | 9,856 = | rtx4090* | 3 | 50% |

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
| concentrated (30–60%) | 24 |
| dominated (60–90%) | 20 |
| captured (>90%) | 27 |

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
| 2026-08-02T17:46 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Reconcile terminal settlement frontier re |
| 2026-08-02T16:39 | sn24 | BURN_DROP | sn24 burn fell 1.000 -> 0.000 - miners can earn again |
| 2026-08-02T16:39 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Verify candidate recovery against pre-sig |
| 2026-08-02T16:39 | sn76 | SCORING_COMMIT | sn76 commit touches scoring: Update scoring constants |
| 2026-08-02T15:37 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Bind verified auditor fallback workflow |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

