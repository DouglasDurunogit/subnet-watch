# Subnet watch — dashboard

_snapshot 2026-08-03T08:40:40Z · block 8762494 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 52 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 95 | `miner_burn` < 0.99 |
| Ranked | 95 | passed every gate |
| **Positive margin** | **52** | income beats machine cost |
| New events this window | 0 | see ALARMS.md |

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
| 0.8–0.99 | 9 | `████` |
| ≥0.99 dead | 33 | `████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn23 Trishool | 84.9 | 550 | 550 = | cpu-small | 5 | 20% |
| 2 | sn107 Minos | 77.6 | 99.99 | 26,612 | cpu-small | 20 | 89% |
| 3 | sn67 Harnyx | 73.4 | 29.21 | 744 | cpu-small | 123 | 18% |
| 4 | sn102 ConnitoAI | 71.1 | 1,040 | 1,040 = | rtx4090* | 4 | 28% |
| 5 | sn41 Almanac | 69.9 | 12.87 | 36.83 | cpu-small | 52 | 75% |
| 6 | sn62 Ridges | 69.7 | 680 | 3,143 | rtx4090* | 7 | 39% |
| 7 | sn56 Gradients | 69 | 557 | 1,174 | rtx4090* | 6 | 64% |
| 8 | sn26 Perturb | 68.6 | 23.60 | 190 | rtx3060 | 11 | 50% |
| 9 | sn15 ORO | 67.1 | 8.10 | 17.19 | cpu-small | 79 | 94% |
| 10 | sn74 Gittensor | 65.9 | 219 | 364 | rtx4090* | 8 | 19% |
| 11 | sn124 Swarm | 65.8 | 220 | 655 | rtx4090* | 20 | 12% |
| 12 | sn53 engy | 63.9 | 120 | 2,821 | rtx4090 | 28 | 17% |
| 13 | sn85 Vidaio | 63.9 | 120 | 555 | rtx4090* | 10 | 19% |
| 14 | sn38 ChronoLLM | 63 | 102 | 1,479 | rtx4090* | 10 | 52% |
| 15 | sn71 Leadpoet | 58.6 | 24.03 | 196 | rtx4090* | 16 | 70% |
| 16 | sn61 RedTeam | 58.5 | 23.38 | 84.71 | rtx4090* | 96 | 3% |
| 17 | sn28 gm | 56.5 | 13.81 | 2,599 | rtx4090* | 15 | 60% |
| 18 | sn51 lium.io | 55.7 | 16.15 | 5,676 | rtx4090* | 42 | 49% |
| 19 | sn9 iota | 55.5 | 9,731 | 9,731 = | rtx4090* | 3 | 50% |
| 20 | sn90 KubeTEE AI Facto | 53.2 | 3,636 | 3,636 = | rtx4090* | 2 | 72% |

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
| wide (<30%) | 26 |
| concentrated (30–60%) | 23 |
| dominated (60–90%) | 19 |
| captured (>90%) | 25 |

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

