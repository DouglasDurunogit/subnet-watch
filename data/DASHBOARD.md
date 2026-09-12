# Subnet watch — dashboard

_snapshot 2026-09-12T17:07:11Z · block 9052890 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 56 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 88 | `miner_burn` < 0.99 |
| Ranked | 89 | passed every gate |
| **Positive margin** | **56** | income beats machine cost |
| New events this window | 3 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 58 | `████████████████████████████` |
| 0–0.2 | 10 | `█████` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 6 | `███` |
| 0.8–0.99 | 3 | `█` |
| ≥0.99 dead | 40 | `███████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn92 MicroTensor | 79.7 | 149 | 449 | cpu-small | 9 | 24% |
| 2 | sn21 AdTAO | 75.6 | 52.28 | 129 | cpu-small | 21 | 34% |
| 3 | sn91 cascade | 71.3 | 1,092 | 2,924 | rtx4090* | 5 | 52% |
| 4 | sn14 Cacheon | 69.4 | 613 | 1,137 | rtx4090* | 12 | 18% |
| 5 | sn96 Verathos | 69.3 | 28.20 | 232 | rtx4090 | 74 | 30% |
| 6 | sn107 Minos | 68.9 | 350 | 29,700 | cpu-small | 20 | 80% |
| 7 | sn67 Harnyx | 68.8 | 9.01 | 1,054 | cpu-small | 126 | 33% |
| 8 | sn11 TrajectoryRL | 68.3 | 6,073 | 6,073 = | cpu-small | 1 | 100% |
| 9 | sn80 OpenRoboto | 67.7 | 370 | 1,316 | rtx4090* | 5 | 43% |
| 10 | sn124 Swarm | 66.5 | 269 | 870 | rtx4090* | 25 | 11% |
| 11 | sn38 ChronoLLM | 66 | 100 | 1,368 | cpu-small | 10 | 52% |
| 12 | sn111 Claims | 65.6 | 218 | 2,847 | rtx4090* | 5 | 77% |
| 13 | sn61 RedTeam | 64.9 | 163 | 258 | rtx4090* | 70 | 2% |
| 14 | sn28 SayGM | 62.7 | 86.11 | 3,476 | rtx4090* | 45 | 24% |
| 15 | sn55 NIOME | 62.1 | 69.18 | 572 | rtx4090* | 11 | 29% |
| 16 | sn62 Ridges | 60 | 36.47 | 3,968 | rtx4090* | 16 | 52% |
| 17 | sn74 Gittensor | 57.4 | 19.53 | 330 | rtx4090 | 12 | 64% |
| 18 | sn51 lium.io | 56.7 | 21.61 | 1,901 | rtx4090* | 64 | 83% |
| 19 | sn81 Reliquary | 56.7 | 12.93 | 171 | rtx4090* | 90 | 5% |
| 20 | sn9 iota | 56.4 | 13,893 | 13,893 = | rtx4090* | 3 | 74% |

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
| dominated (60–90%) | 15 |
| captured (>90%) | 20 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 96 |
| min_compute.yml (curated) | 11 |
| code-submission (validator runs it) | 10 |
| README keywords (GUESS) | 10 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-09-12T17:07 | sn36 | SCORING_COMMIT | sn36 commit touches scoring: Run calibration once a day on 200 tasks,  |
| 2026-09-12T17:07 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Set daily Arena admission to twenty chall |
| 2026-09-12T17:07 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: tracks: the hallucination detection track |
| 2026-09-12T14:06 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Verify original provider statuses in paid |
| 2026-09-12T14:06 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: fix(proof-fc-harvest): zero-scored agent |
| 2026-09-12T11:06 | sn44 | SCORING_COMMIT | sn44 commit touches scoring: gather responses before scoring |
| 2026-09-12T11:06 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Remove the OpenRouter paid-validation bud |
| 2026-09-12T11:06 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: fix(validator): separate reveal accountin |
| 2026-09-12T11:06 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: trainer: king rent retries lemon pods and |
| 2026-09-12T11:06 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: fees: a per submission commitment fee; mt |
| 2026-09-12T06:24 | sn20 | BURN_DROP | sn20 burn fell 1.000 -> 0.742 - miners can earn again |
| 2026-09-12T06:24 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Reuse verified historical deployment comp |
| 2026-09-12T06:24 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-3439 - [P0] validator: outdated execu |
| 2026-09-12T06:24 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Use current billing schema in normal vali |
| 2026-09-12T06:24 | sn71 | README_TASK_DIFF | sn71 README task/scoring sections changed |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

