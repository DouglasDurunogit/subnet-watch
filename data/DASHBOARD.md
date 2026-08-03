# Subnet watch — dashboard

_snapshot 2026-08-03T01:17:26Z · block 8760278 · run_status **ok**_

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
| New events this window | 1 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 58 | `████████████████████████████` |
| 0–0.2 | 8 | `████` |
| 0.2–0.4 | 3 | `█` |
| 0.4–0.6 | 9 | `████` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 9 | `████` |
| ≥0.99 dead | 32 | `███████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn23 Trishool | 85 | 565 | 565 = | cpu-small | 5 | 20% |
| 2 | sn107 Minos | 77.8 | 105 | 27,015 | cpu-small | 20 | 90% |
| 3 | sn98 NeverPlayAlone | 75.9 | 1,687 | 1,687 = | cpu-small | 1 | 100% |
| 4 | sn67 Harnyx | 73.5 | 30.64 | 806 | cpu-small | 116 | 18% |
| 5 | sn102 ConnitoAI | 70.2 | 780 | 1,237 | rtx4090* | 5 | 32% |
| 6 | sn62 Ridges | 69.8 | 700 | 2,526 | rtx4090* | 7 | 39% |
| 7 | sn56 Gradients | 69.1 | 573 | 1,208 | rtx4090* | 6 | 64% |
| 8 | sn26 Perturb | 68.6 | 23.58 | 194 | rtx3060 | 11 | 50% |
| 9 | sn15 ORO | 68.6 | 10.69 | 18.50 | cpu-small | 94 | 91% |
| 10 | sn74 Gittensor | 66 | 228 | 366 | rtx4090* | 8 | 19% |
| 11 | sn124 Swarm | 65.9 | 225 | 670 | rtx4090* | 20 | 12% |
| 12 | sn53 engy | 63.9 | 119 | 2,821 | rtx4090 | 28 | 17% |
| 13 | sn85 Vidaio | 63.2 | 98.07 | 515 | rtx4090* | 10 | 18% |
| 14 | sn38 ChronoLLM | 63 | 103 | 1,494 | rtx4090* | 10 | 52% |
| 15 | sn71 Leadpoet | 62.9 | 89.49 | 135 | rtx4090* | 9 | 70% |
| 16 | sn28 gm | 60.7 | 47.75 | 2,986 | rtx4090* | 14 | 53% |
| 17 | sn61 RedTeam | 58.4 | 22.61 | 84.56 | rtx4090* | 98 | 3% |
| 18 | sn9 iota | 55.6 | 9,905 | 9,905 = | rtx4090* | 3 | 50% |
| 19 | sn51 lium.io | 53.8 | 11.18 | 8,774 | rtx4090* | 43 | 39% |
| 20 | sn90 KubeTEE AI Facto | 53.2 | 3,623 | 3,623 = | rtx4090* | 2 | 70% |

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
| no evidence | 106 |
| min_compute.yml (curated) | 9 |
| code-submission (validator runs it) | 8 |
| README keywords (GUESS) | 4 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
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
| 2026-08-02T15:37 | sn89 | SCORING_COMMIT | sn89 commit touches scoring: hf scoreboard: publish each hotkeys own r |
| 2026-08-02T12:34 | sn98 | BURN_DROP | sn98 burn fell 1.000 -> 0.000 - miners can earn again |
| 2026-08-02T12:34 | sn103 | RELEASE | sn103 released v2008 |
| 2026-08-02T12:34 | sn103 | SCORING_COMMIT | sn103 commit touches scoring: validator: release v2008 |
| 2026-08-02T11:08 | sn11 | SCORING_COMMIT | sn11 commit touches scoring: docs(incentive): takeover bar decays to a |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

