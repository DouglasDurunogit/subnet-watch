# Subnet watch — dashboard

_snapshot 2026-09-12T14:05:47Z · block 9051987 · run_status **ok**_

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
| Ranked | 88 | passed every gate |
| **Positive margin** | **56** | income beats machine cost |
| New events this window | 2 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 59 | `████████████████████████████` |
| 0–0.2 | 9 | `████` |
| 0.2–0.4 | 7 | `███` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 6 | `███` |
| 0.8–0.99 | 3 | `█` |
| ≥0.99 dead | 40 | `███████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn92 MicroTensor | 79.8 | 152 | 458 | cpu-small | 9 | 24% |
| 2 | sn21 AdTAO | 75.6 | 52.41 | 129 | cpu-small | 21 | 34% |
| 3 | sn91 cascade | 71.3 | 1,103 | 2,955 | rtx4090* | 5 | 52% |
| 4 | sn96 Verathos | 69.5 | 29.93 | 227 | rtx4090 | 74 | 33% |
| 5 | sn14 Cacheon | 69.4 | 612 | 1,134 | rtx4090* | 12 | 18% |
| 6 | sn107 Minos | 69 | 355 | 29,568 | cpu-small | 20 | 80% |
| 7 | sn67 Harnyx | 68.7 | 8.99 | 1,052 | cpu-small | 125 | 33% |
| 8 | sn11 TrajectoryRL | 68.3 | 6,058 | 6,058 = | cpu-small | 1 | 100% |
| 9 | sn80 OpenRoboto | 68.3 | 443 | 1,571 | rtx4090* | 5 | 51% |
| 10 | sn56 Gradients | 67.9 | 392 | 5,284 | rtx4090* | 9 | 48% |
| 11 | sn124 Swarm | 66.5 | 269 | 870 | rtx4090* | 25 | 11% |
| 12 | sn38 ChronoLLM | 66 | 100 | 1,367 | cpu-small | 10 | 52% |
| 13 | sn61 RedTeam | 65.8 | 212 | 314 | rtx4090* | 55 | 3% |
| 14 | sn111 Claims | 65.7 | 221 | 2,833 | rtx4090* | 5 | 77% |
| 15 | sn28 SayGM | 62.6 | 82.43 | 2,714 | rtx4090* | 47 | 19% |
| 16 | sn55 NIOME | 62.1 | 69.14 | 572 | rtx4090* | 11 | 29% |
| 17 | sn23 Trishool | 60.3 | 552 | 552 = | cpu-small | 2 | 80% |
| 18 | sn62 Ridges | 59.9 | 36.16 | 3,940 | rtx4090* | 16 | 52% |
| 19 | sn74 Gittensor | 57.5 | 19.87 | 329 | rtx4090 | 12 | 64% |
| 20 | sn81 Reliquary | 56.8 | 13.61 | 180 | rtx4090* | 90 | 5% |

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
| concentrated (30–60%) | 24 |
| dominated (60–90%) | 15 |
| captured (>90%) | 19 |

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
| 2026-09-12T01:27 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Sync disposable replay scratch once after |
| 2026-09-12T01:27 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Preserve Arena miner credential failure e |
| 2026-09-11T21:21 | sn20 | SCORING_COMMIT | sn20 commit touches scoring: Add grounded video scoring and hybrid mai |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

