# Subnet watch — dashboard

_snapshot 2026-08-29T03:23:23Z · block 8948084 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 61 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 94 | `miner_burn` < 0.99 |
| Ranked | 94 | passed every gate |
| **Positive margin** | **61** | income beats machine cost |
| New events this window | 2 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 62 | `████████████████████████████` |
| 0–0.2 | 6 | `███` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 6 | `███` |
| 0.6–0.8 | 10 | `█████` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 34 | `███████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn11 TrajectoryRL | 79.8 | 5,236 | 5,236 = | cpu-small | 1 | 100% |
| 2 | sn92 MicroTensor | 76.7 | 69.99 | 1,275 | cpu-small | 9 | 67% |
| 3 | sn3 Teutonic | 75.6 | 3,975 | 3,975 = | rtx4090* | 5 | 20% |
| 4 | sn76 Phylax | 74.9 | 44.12 | 179 | cpu-small | 21 | 20% |
| 5 | sn67 Harnyx | 71.3 | 17.16 | 690 | cpu-small | 121 | 18% |
| 6 | sn15 ORO | 69.9 | 18.16 | 36.56 | cpu-small | 77 | 94% |
| 7 | sn91 cascade | 68.6 | 485 | 2,624 | rtx4090* | 5 | 52% |
| 8 | sn96 Verathos | 68.4 | 23.18 | 155 | rtx4090 | 78 | 40% |
| 9 | sn56 Gradients | 68.3 | 446 | 1,062 | rtx4090* | 7 | 70% |
| 10 | sn80 OpenRoboto | 68 | 403 | 1,819 | rtx4090* | 5 | 71% |
| 11 | sn111 Claims | 67.6 | 374 | 3,339 | rtx4090* | 5 | 70% |
| 12 | sn124 Swarm | 66.6 | 275 | 848 | rtx4090* | 25 | 11% |
| 13 | sn79 MVTRX | 66 | 5.52 | 403 | cpu-small | 217 | 9% |
| 14 | sn61 RedTeam | 64.9 | 163 | 246 | rtx4090* | 41 | 4% |
| 15 | sn98 NeverPlayAlone | 64.6 | 1,968 | 1,968 = | cpu-small | 1 | 100% |
| 16 | sn107 Minos | 64.4 | 124 | 36,786 | cpu-small | 20 | 90% |
| 17 | sn54 Yanez | 64 | 6.07 | 1,040 | a4000 | 101 | 35% |
| 18 | sn81 Reliquary | 63.9 | 120 | 241 | rtx4090* | 38 | 5% |
| 19 | sn121 sundae_bar | 63 | 1,231 | 1,231 = | cpu-small | 2 | 60% |
| 20 | sn65 True Performance | 62.4 | 86.36 | 181 | rtx4090* | 6 | 76% |

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
| concentrated (30–60%) | 20 |
| dominated (60–90%) | 19 |
| captured (>90%) | 28 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 101 |
| code-submission (validator runs it) | 10 |
| min_compute.yml (curated) | 10 |
| README keywords (GUESS) | 6 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-08-29T03:23 | sn15 | RELEASE | sn15 released v1.2.10 |
| 2026-08-29T03:23 | sn25 | RELEASE | sn25 released v2026.8.28-1031618120 |
| 2026-08-28T21:28 | sn15 | RELEASE | sn15 released v1.2.9 |
| 2026-08-28T21:28 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: fix(validator): use revealed top as weigh |
| 2026-08-28T21:28 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: feat(reporting): each miner's row carries |
| 2026-08-28T21:28 | sn25 | RELEASE | sn25 released v2026.8.28-1031286130 |
| 2026-08-28T21:28 | sn28 | RELEASE | sn28 released v0.4.12 |
| 2026-08-28T21:28 | sn35 | RELEASE | sn35 released 1.2.0 |
| 2026-08-28T21:28 | sn35 | SCORING_COMMIT | sn35 commit touches scoring: feat: send all miner emissions to scored  |
| 2026-08-28T21:28 | sn47 | README_TASK_DIFF | sn47 README task/scoring sections changed |
| 2026-08-28T21:28 | sn79 | README_TASK_DIFF | sn79 README task/scoring sections changed |
| 2026-08-28T21:28 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: Accept operator-named hotkeys ahead of th |
| 2026-08-28T21:28 | sn102 | RELEASE | sn102 released v0.5.3 |
| 2026-08-28T21:28 | sn102 | SCORING_COMMIT | sn102 commit touches scoring: ⏪ fix(shared): stop collapsing miner com |
| 2026-08-28T21:28 | sn104 | BURN_DROP | sn104 burn fell 1.000 -> 0.003 - miners can earn again |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

