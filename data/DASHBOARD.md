# Subnet watch — dashboard

_snapshot 2026-09-17T19:19:25Z · block 9089422 · run_status **ok**_

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
| New events this window | 3 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 65 | `████████████████████████████` |
| 0–0.2 | 9 | `████` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 6 | `███` |
| 0.8–0.99 | 4 | `██` |
| ≥0.99 dead | 33 | `██████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn11 TrajectoryRL | 80.2 | 5,904 | 5,904 = | cpu-small | 1 | 100% |
| 2 | sn92 MicroTensor | 77.9 | 93.02 | 315 | cpu-small | 8 | 39% |
| 3 | sn91 cascade | 72.6 | 626 | 2,506 | cpu-small | 5 | 52% |
| 4 | sn107 Minos | 68.9 | 345 | 27,559 | cpu-small | 20 | 79% |
| 5 | sn102 ConnitoAI | 68.5 | 473 | 1,311 | rtx4090* | 7 | 29% |
| 6 | sn67 Harnyx | 68.5 | 8.36 | 807 | cpu-small | 142 | 28% |
| 7 | sn111 Claims | 68.2 | 452 | 2,006 | rtx4090* | 5 | 60% |
| 8 | sn56 Gradients | 68 | 406 | 4,928 | rtx4090* | 10 | 46% |
| 9 | sn124 Swarm | 66.3 | 257 | 830 | rtx4090* | 25 | 11% |
| 10 | sn38 ChronoLLM | 65.6 | 89.64 | 794 | cpu-small | 10 | 52% |
| 11 | sn3 Teutonic | 63.9 | 4,136 | 4,136 = | rtx4090* | 5 | 20% |
| 12 | sn28 SayGM | 63.9 | 121 | 1,216 | rtx4090* | 55 | 8% |
| 13 | sn62 Ridges | 62.2 | 72.55 | 1,476 | rtx4090* | 20 | 22% |
| 14 | sn55 NIOME | 61.9 | 64.96 | 541 | rtx4090* | 11 | 29% |
| 15 | sn81 Reliquary | 60.9 | 48.41 | 105 | rtx4090* | 35 | 50% |
| 16 | sn23 Trishool | 60.5 | 589 | 589 = | cpu-small | 2 | 80% |
| 17 | sn61 RedTeam | 59 | 28.06 | 2,344 | rtx4090* | 118 | 21% |
| 18 | sn51 lium.io | 57.8 | 27.74 | 1,492 | rtx4090* | 69 | 82% |
| 19 | sn15 ORO | 57.7 | 2.36 | 18,196 | cpu-small | 21 | 100% |
| 20 | sn74 Gittensor | 56.7 | 16.11 | 134 | rtx4090* | 9 | 65% |

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
| dominated (60–90%) | 18 |
| captured (>90%) | 24 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 97 |
| min_compute.yml (curated) | 11 |
| code-submission (validator runs it) | 10 |
| README keywords (GUESS) | 9 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-09-17T19:19 | sn25 | RELEASE | sn25 released v2026.9.17-1048676710 |
| 2026-09-17T19:19 | sn74 | RELEASE | sn74 released release-20260917-174533 |
| 2026-09-17T19:19 | sn74 | README_TASK_DIFF | sn74 README task/scoring sections changed |
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

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

