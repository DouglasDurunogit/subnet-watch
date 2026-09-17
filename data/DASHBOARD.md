# Subnet watch — dashboard

_snapshot 2026-09-17T15:40:38Z · block 9088331 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 55 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 95 | `miner_burn` < 0.99 |
| Ranked | 95 | passed every gate |
| **Positive margin** | **55** | income beats machine cost |
| New events this window | 7 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 65 | `████████████████████████████` |
| 0–0.2 | 9 | `████` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 7 | `███` |
| 0.8–0.99 | 4 | `██` |
| ≥0.99 dead | 33 | `██████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn92 MicroTensor | 79 | 125 | 353 | cpu-small | 8 | 39% |
| 2 | sn91 cascade | 72.7 | 637 | 2,551 | cpu-small | 5 | 52% |
| 3 | sn102 ConnitoAI | 70 | 752 | 1,428 | rtx4090* | 6 | 31% |
| 4 | sn107 Minos | 68.8 | 337 | 27,910 | cpu-small | 20 | 80% |
| 5 | sn67 Harnyx | 68.5 | 8.35 | 806 | cpu-small | 142 | 28% |
| 6 | sn56 Gradients | 68 | 405 | 4,909 | rtx4090* | 10 | 46% |
| 7 | sn124 Swarm | 66.3 | 257 | 830 | rtx4090* | 25 | 11% |
| 8 | sn38 ChronoLLM | 65.6 | 89.49 | 793 | cpu-small | 10 | 52% |
| 9 | sn111 Claims | 65 | 182 | 2,611 | rtx4090* | 5 | 79% |
| 10 | sn3 Teutonic | 63.9 | 4,146 | 4,146 = | rtx4090* | 5 | 20% |
| 11 | sn55 NIOME | 61.8 | 64.64 | 539 | rtx4090* | 11 | 29% |
| 12 | sn62 Ridges | 61.6 | 60.36 | 1,707 | rtx4090* | 19 | 26% |
| 13 | sn28 SayGM | 61.1 | 53.97 | 2,087 | rtx4090* | 57 | 14% |
| 14 | sn81 Reliquary | 60.6 | 44.48 | 104 | rtx4090* | 37 | 49% |
| 15 | sn23 Trishool | 60.5 | 588 | 588 = | cpu-small | 2 | 80% |
| 16 | sn61 RedTeam | 59.8 | 37.59 | 1,907 | rtx4090* | 118 | 17% |
| 17 | sn51 lium.io | 57.3 | 24.89 | 1,525 | rtx4090* | 69 | 82% |
| 18 | sn80 OpenRoboto | 56.6 | 469 | 1,661 | rtx4090* | 5 | 43% |
| 19 | sn9 iota | 56.1 | 12,552 | 12,552 = | rtx4090* | 3 | 68% |
| 20 | sn15 ORO | 56 | 2.40 | 18,409 | cpu-small | 21 | 100% |

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
| wide (<30%) | 25 |
| concentrated (30–60%) | 25 |
| dominated (60–90%) | 18 |
| captured (>90%) | 24 |

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
| 2026-09-17T15:41 | sn10 | SCORING_COMMIT | sn10 commit touches scoring: fix: refresh campaign fees before payment |
| 2026-09-17T15:41 | sn56 | SCORING_COMMIT | sn56 commit touches scoring: Update autoupdate_validator_steps.sh to e |
| 2026-09-17T15:41 | sn56 | README_TASK_DIFF | sn56 README task/scoring sections changed |
| 2026-09-17T15:41 | sn92 | RELEASE | sn92 released v0.4.11 |
| 2026-09-17T15:41 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: validator: rig verification needs substra |
| 2026-09-17T15:41 | sn124 | SCORING_COMMIT | sn124 commit touches scoring: Pin numpy and repair a drifted validator |
| 2026-09-17T15:41 | sn124 | README_TASK_DIFF | sn124 README task/scoring sections changed |
| 2026-09-17T11:36 | sn15 | BURN_DROP | sn15 burn fell 0.997 -> 0.000 - miners can earn again |
| 2026-09-17T11:36 | sn51 | RELEASE | sn51 released executor-v1.130 |
| 2026-09-17T11:36 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-3519 - [P2] validator: a node whose s |
| 2026-09-17T11:36 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Merge pull request #153 from Umi-BitSign/ |
| 2026-09-17T11:36 | sn92 | RELEASE | sn92 released v0.4.9 |
| 2026-09-17T11:36 | sn97 | SCORING_COMMIT | sn97 commit touches scoring: feat: add extra attempts, so miners which |
| 2026-09-17T06:06 | sn10 | BURN_DROP | sn10 burn fell 1.000 -> 0.811 - miners can earn again |
| 2026-09-17T06:06 | sn15 | RELEASE | sn15 released v2.0.20 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

