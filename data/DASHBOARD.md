# Subnet watch — dashboard

_snapshot 2026-08-15T02:40:56Z · block 8847074 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 53 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 90 | `miner_burn` < 0.99 |
| Ranked | 90 | passed every gate |
| **Positive margin** | **53** | income beats machine cost |
| New events this window | 1 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 60 | `████████████████████████████` |
| 0–0.2 | 6 | `███` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 8 | `████` |
| 0.6–0.8 | 5 | `██` |
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 38 | `██████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn107 Minos | 77.9 | 108 | 31,872 | cpu-small | 20 | 90% |
| 2 | sn76 Phylax | 74.7 | 40.33 | 193 | cpu-small | 10 | 34% |
| 3 | sn67 Harnyx | 72.6 | 24.18 | 388 | cpu-small | 107 | 10% |
| 4 | sn6 Numinous | 71.7 | 21.59 | 473 | cpu-small | 15 | 27% |
| 5 | sn26 Perturb | 70.9 | 42.00 | 76.97 | rtx3060 | 10 | 70% |
| 6 | sn1 Apex | 70.8 | 931 | 1,149 | rtx4090* | 4 | 54% |
| 7 | sn91 cascade | 69.6 | 655 | 2,259 | rtx4090* | 5 | 50% |
| 8 | sn41 Almanac | 69.6 | 12.21 | 54.14 | cpu-small | 72 | 66% |
| 9 | sn56 Gradients | 68.8 | 523 | 980 | rtx4090* | 7 | 66% |
| 10 | sn62 Ridges | 68.2 | 426 | 1,978 | rtx4090* | 7 | 35% |
| 11 | sn15 ORO | 68.1 | 11.05 | 22.06 | cpu-small | 84 | 93% |
| 12 | sn21 AdTAO | 67.5 | 7.46 | 33.52 | cpu-small | 88 | 45% |
| 13 | sn96 Verathos | 67.4 | 17.74 | 185 | rtx4090 | 64 | 42% |
| 14 | sn85 Vidaio | 66.2 | 239 | 572 | rtx4090* | 10 | 19% |
| 15 | sn38 ChronoLLM | 66.1 | 101 | 1,379 | cpu-small | 10 | 52% |
| 16 | sn124 Swarm | 65.9 | 227 | 732 | rtx4090* | 24 | 11% |
| 17 | sn80 OpenRoboto | 65.2 | 176 | 637 | rtx4090* | 4 | 91% |
| 18 | sn28 gm | 65 | 169 | 2,574 | rtx4090* | 31 | 28% |
| 19 | sn98 NeverPlayAlone | 64.1 | 1,728 | 1,728 = | cpu-small | 1 | 100% |
| 20 | sn55 NIOME | 61.4 | 56.27 | 486 | rtx4090* | 11 | 30% |

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
| wide (<30%) | 27 |
| concentrated (30–60%) | 18 |
| dominated (60–90%) | 17 |
| captured (>90%) | 26 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 102 |
| code-submission (validator runs it) | 10 |
| min_compute.yml (curated) | 9 |
| README keywords (GUESS) | 6 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-08-15T01:47 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Keep private ICP scores out of telemetry |
| 2026-08-14T23:33 | sn2 | BURN_DROP | sn2 burn fell 1.000 -> 0.824 - miners can earn again |
| 2026-08-14T23:33 | sn19 | BURN_DROP | sn19 burn fell 1.000 -> 0.986 - miners can earn again |
| 2026-08-14T22:36 | sn62 | RELEASE | sn62 released v0.2.7 |
| 2026-08-14T20:17 | sn55 | SCORING_COMMIT | sn55 commit touches scoring: commit weights after validation |
| 2026-08-14T20:17 | sn96 | RELEASE | sn96 released Verathos v0.1.40 — Capacity Audit Scheduling Stability |
| 2026-08-14T19:29 | sn121 | README_TASK_DIFF | sn121 README task/scoring sections changed |
| 2026-08-14T18:24 | sn55 | SCORING_COMMIT | sn55 commit touches scoring: print only valid scores |
| 2026-08-14T18:24 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: chore(deploy): promote prod prism-challe |
| 2026-08-14T17:08 | sn55 | SCORING_COMMIT | sn55 commit touches scoring: print only valid scores |
| 2026-08-14T16:03 | sn126 | SCORING_COMMIT | sn126 commit touches scoring: docs: describe continuous miner training |
| 2026-08-14T15:05 | sn20 | BURN_DROP | sn20 burn fell 1.000 -> 0.000 - miners can earn again |
| 2026-08-14T15:05 | sn39 | BURN_DROP | sn39 burn fell 1.000 -> 0.000 - miners can earn again |
| 2026-08-14T15:05 | sn96 | RELEASE | sn96 released Verathos v0.1.39 — Hard-Proof Timing Stability |
| 2026-08-14T14:04 | sn55 | README_TASK_DIFF | sn55 README task/scoring sections changed |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

